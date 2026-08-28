# Release log

Hand-written release notes for the Oto platform — product-level, across repos.
Dated entries, free form. (Deployed versions are the `v*` tags on
[oto-backend](https://github.com/otomata-tech/oto-backend) and
[oto-dashboard](https://github.com/otomata-tech/oto-dashboard).)

<!-- Newest first. Suggested shape:

## YYYY-MM-DD — title
What shipped, in product terms. Versions if relevant (backend vX.Y.Z / dashboard vX.Y.Z).
-->

## 2026-08-28 — Modifier un identifiant sans en connaître le secret (backend v1.153.0 / dashboard v1.49.2)

**Changer une valeur d'un identifiant partagé n'oblige plus à tout resaisir.** Un
connecteur configuré pour une équipe ou une organisation ne pouvait pas être
relu : l'écran de modification s'ouvrait entièrement vide, y compris sur les
valeurs qui n'ont rien de secret — une adresse de service, un mode
d'authentification, un nom d'en-tête. Et l'enregistrement remplaçait tout. Corriger
une adresse revenait donc à retrouver ailleurs une clé qu'aucune surface ne
restitue, sous peine de l'écraser par du vide.

Désormais les valeurs non secrètes se relisent — à son niveau, et seulement pour
qui administre ce niveau —, et l'enregistrement complète ce qu'on ne renvoie pas.
Un champ laissé vide conserve ce qui est en place ; le vider explicitement
l'efface. Les secrets, eux, ne se relisent toujours pas, à aucun niveau.

**Un écran cesse de dire « demande à un admin » à l'administrateur.** Quand aucune
clé n'était encore posée, la fiche d'un connecteur affichait « Réservé à
certaines équipes — demande à un admin ». Or « aucune clé ne résout » n'est pas
« l'accès t'est refusé » : c'est l'état par défaut de tout connecteur pas encore
connecté. Le mur s'affichait donc à des gens que rien ne bloquait, jusqu'à un
responsable devant le connecteur de sa propre organisation — le bouton pour poser
sa clé était là, sous la phrase, et plus personne ne le lisait. La restriction
réelle est désormais servie séparément, et le mot « Réservé » ne sort que si
c'en est un.

Dans la foulée : quand une clé existe dans une équipe, l'écran ne se contente
plus de dire « active cette équipe » — il rappelle qu'on peut poser la sienne, qui
passe avant. Cette phrase, écrite deux fois dans le même bloc, ne l'est plus
qu'une. Et le bouton s'appelle « Poser ma clé » quand une clé existe déjà
ailleurs, au lieu de porter le nom du connecteur.

**Un formulaire ne montre plus que les champs qui servent.** Un connecteur peut
déclarer que l'un de ses champs décide des autres : le connecteur HTTP générique
en affichait douze quel que soit le mode d'authentification choisi, là où trois
suffisent. Les valeurs à choix fermé se choisissent dans une liste au lieu de se
taper — une faute de frappe était acceptée à l'enregistrement puis refusée au
premier appel réel. La cohérence est vérifiée à l'écriture, et le refus nomme le
champ en cause.

**Une erreur d'API distante remonte enfin son motif.** Un appel sortant en échec
ne rendait que son code — « HTTP 502 » — sans un mot de ce que le service répondait.
Un service resté indisponible plusieurs semaines n'a jamais pu être diagnostiqué
autrement qu'en lisant les journaux du serveur, hors de portée d'un agent. Le
message du service accompagne maintenant le code, borné et étiqueté comme une
donnée à ne pas prendre pour une instruction, avec une indication explicite de ce
qui vaut la peine d'être retenté.

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
