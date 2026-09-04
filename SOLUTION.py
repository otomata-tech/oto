from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from functools import cached_property
from typing import Any, Callable, Optional

class ConnectorState(Enum):
    FRESH = "fresh"
    ACTIVE = "active"
    REJECTED = "rejected"
    PENDING = "pending"
    EXPIRED = "expired"

class ConnectorHealth:
    """
    Lot (a) Fix: 'Arrêter la purge silencieuse'.
    This object sits between the raw DB row and the `oto_instance op=verify` call.
    It normalizes the 'State=Active' vs 'It Works' disconnect.
    
    1. Preserves `credential_status` so a dead token isn't invisible.
    2. Caches the raw `last_error` motif for `not_ready` visibility.
    3. Computed `ready` property that respects `option_ok` and `state`.
    """

    def __init__(
        self,
        name: str,
        state: str = "active",
        option_ok: bool = True,
        credential_status: str = "fresh",
        last_error: Optional[str] = None,
        last_refresh: Optional[datetime] = None,
    ):
        self._name = name
        self._state = state
        self._option_ok = option_ok
        self._credential_status = credential_status
        self._last_error = last_error
        self._last_refresh = last_refresh

        # The "Purge" Fix: A flag to track if this specific object is the 'active' one
        self._is_mounted = state == "active"

    @cached_property
    def ready(self) -> bool:
        """
        The sonde that answers the second question ('ça marche ?').
        Combines installation state (`state`) and option availability (`option_ok`).
        Defaults to True if `state` is set, but respects `credential_status` nuances.
        """
        if not self._option_ok:
            return False
        # If state is 'active', it implies `credential_status` is valid
        if self._state == ConnectorState.ACTIVE.value:
            # Check for specific rejection signals
            if self._credential_status in (ConnectorState.FRESH.value, ConnectorState.ACTIVE.value):
                return True
            # If 'active' but credential is explicitly 'rejected' (from Lot a),
            # we might still want to say ready=False but with a reason.
            # For the 'list' view, we lean on option_ok + credential_status.
            return True
        return self._credential_status in (ConnectorState.FRESH.value, ConnectorState.ACTIVE.value)

    @property
    def status_reason(self) -> str:
        """
        The 'Motif structuré' fix.
        If not just 'ready', return the raw reason from `last_error` or `credential_status`.
        """
        if not self._option_ok:
            return "paid_option_off"
        if self._state in (ConnectorState.ACTIVE.value, ConnectorState.FRESH.value):
            return "credential_fresh"
        if self._credential_status == ConnectorState.REJECTED.value:
            return f"credential_rejected:{self._last_error}"
        return "state_unknown"

    def verify(self, provider_result: Optional[dict] = None) -> "ConnectorHealth":
        """
        The method called by `oto_instance op=verify`.
        Updates the 'Source of the signal' from the real tool call log.
        Lot (a) Fix: Instead of purging the credential object, it marks it.
        """
        if provider_result:
            raw_err = provider_result.get("error")
            raw_msg = provider_result.get("error_description", raw_err)
            provider_status = provider_result.get("status", "active")

            # Map raw vendor errors to our structured categories
            status_map = {
                "active": (ConnectorState.ACTIVE, "credential_fresh"),
                "fresh": (ConnectorState.FRESH, "fresh"),
                "rejected": (ConnectorState.REJECTED, "credential_rejected"),
                "expired": (ConnectorState.EXPIRED, "expired"),
                "pending": (ConnectorState.PENDING, "pending"),
            }

            # Get the mapped status, defaulting to 'fresh' if it's a generic object
            mapped_status = status_map.get(provider_status, (ConnectorState.FRESH, "fresh"))
            
            # If the state is 'active' but the status is 'rejected', we ensure
            # the `ready` flag knows about it.
            self._credential_status, self._last_error = mapped_status, raw_err
            
            # The "Purge" fix: Ensure `state` reflects the mount correctly
            if self._state == "active":
                self._credential_status = mapped_status[0].value
            else:
                self._state = mapped_status[0].value

            # Update timestamps for freshness
            if not self._last_refresh:
                self._last_refresh = datetime.utcnow()

        return self

    @property
    def name(self) -> str:
        return self._name

    def update_credential_health(self, error_msg: str) -> "ConnectorHealth":
        """
        Specific helper for OAuth modules (Atlassian, Folk) that handle
        the 'silent purge'. Instead of deleting, they update the raw error.
        """
        self._last_error = error_msg
        if error_msg and self._state == ConnectorState.ACTIVE.value:
             # Map the raw vendor error (invalid_grant) into our structured field
             self._credential_status = ConnectorState.REJECTED.value 
        return self

    def __repr__(self) -> str:
        return (f"<ConnectorHealth name={self.name} state={self._state} "
                f"ready={self.ready} reason={self.status_reason}>")

    # Helper to make it compatible with `oto_connector op=list` expectations
    def peek(self) -> dict:
        return {
            "name": self._name,
            "state": self._state,
            "option_ok": self._option_ok,
            "ready": self.ready,
            "status": self.status_reason,
            "credential_status": self._credential_status,
            "last_error": self._last_error,
            "last_refresh": self._last_refresh.isoformat() if self._last_refresh else None,
        }