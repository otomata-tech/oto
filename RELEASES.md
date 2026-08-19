# Release log

Hand-written release notes for the Oto platform — product-level, across repos.
Dated entries, free form. (Deployed versions are the `v*` tags on
[oto-backend](https://github.com/otomata-tech/oto-backend) and
[oto-dashboard](https://github.com/otomata-tech/oto-dashboard).)

<!-- Newest first. Suggested shape:

## YYYY-MM-DD — title
What shipped, in product terms. Versions if relevant (backend vX.Y.Z / dashboard vX.Y.Z).
-->

## 2026-08-19 — Prospection sortante, groupes Folk, suivi des tenants (backend v1.130.0 / dashboard v1.40.0)

**Une « Base de connaissance » n'apparaît plus toute seule.** Lire la base d'une
organisation la créait au passage, et cette lecture part au montage de chaque
page : ouvrir l'application suffisait à poser un projet vide dans l'organisation.
Lire ne crée plus rien ; créer est devenu un geste distinct, appelé juste avant
d'écrire la première page. Un script d'entretien archive les bases restées vides
et laisse intactes celles qui portent au moins un document.

**Prospection sortante : deux connecteurs.** TheirStack (signal d'embauche) et
Origami (tables de prospects, campagnes e-mail et LinkedIn). Clé apportée par
l'organisation, hors socle, simulation par défaut sur toute écriture — et l'envoi
part des comptes que l'organisation a elle-même connectés chez le fournisseur.

**Folk : les groupes deviennent pilotables** — création, mise à jour, champs
personnalisés de groupe, ajout et retrait de membres.

**Un espace archivé rend sa place** au quota de création. Archiver ne libérait
rien : une organisation à sa limite y restait après avoir fait le ménage.

**Une organisation neuve porte le front de qui la crée**, au lieu de retomber sur
le front par défaut — suite de l'étage d'identité.

**Le suivi des tenants devient un écran** : comptes, organisations actives et
archivées, appels, comptes actifs, et les organisations *désalignées* — celles
dont le créateur relève d'un autre front — avec leur adresse, pas seulement leur
nombre.

**Sièges de messagerie : un bouton pour libérer, un décompte qui dit vrai.** Un
compte reste facturé tant qu'il existe chez le fournisseur ; se déconnecter ne le
supprime pas. Le tableau chiffre désormais ce qu'on peut cesser de payer, et
n'offre le geste que sur les sièges hors service.

Bibliothèque de connecteurs : `oto-core` 1.83.0 puis 1.84.0 (client Lightfield),
publiées sur PyPI.
