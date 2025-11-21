
# TP12 – Personnalisation

## Introduction, Contexte et Objectifs

```
Pour le moment, nous avons diƯérents types d’utilisateurs :
```
- le superuser, qui a un accès privilégié à la page par défaut d’administration proposée
    par django,
- les utilisateurs staƯ, à qui on a donné les droits classiques du CRUD (create, read,
    update, delete)
- les clients connectés,
- les internautes non connectés.

```
Tout ceci se fait grâce au modèle User par défaut de Django, de sorte qu’on n’a pas eu à coder
de modèle pour l’application applicompte. Mais ce modèle va s’avérer incomplet, car nous
allons ajouter une image au profil d’un utilisateur. Nous allons donc définir un modèle User
personnalisé : TravelUser
```
```
Il nous restera aussi dans ce TP à adapter toutes les views (passage de User à TravelUser), et à
créer la page de profil, puisque c’est du grand classique.
```
## Personnalisation du modèle User

1. Dans le fichier models.py d’applicompte, créez un modèle TravelUser qui étend User (le
    modèle django User vient de django.contrib.auth.models), avec un attribut
    supplémentaire nommé image. Comme cet attribut servira à modéliser la photo de
    l’utilisateur, il faut, comme pour les images de voyage, prévoir un fichier par défaut et un
    répertoire d’upload :
2. Mettez en place la migration de ce nouveau modèle. Vérifiez que, dans la base de
    données, vous avez maintenant une nouvelle table applicompte_traveluser


```
Concrètement vous avez un champ qui permet de faire la jointure avec la table user, et
le champ supplémentaire image, défini dans le modèle TravelUser.
```
3. Faites en sorte que le modèle TravelUser puisse être géré par le superuser via l’interface
    d’administration proposée par django (comme cela a été fait pour Voyage, Ville et
    Etape).
4. Connectez-vous en tant qu’administrateur sur le portail de django. Créez un nouvel
    utilisateur (pas en ajoutant un nouvel User d’applicompte, mais un nouvel User
    classique). Ensuite, dans sqlitebrowser, vérifiez que le nouvel utilisateur existe bien, et
    complétez à la main le champ « image » correspondant dans la table
    applicompte_traveluser. Faites-le pour tous les utilisateurs existants.

```
Vérifiez que vous pouvez vous connecter et vous déconnecter avec ce nouvel utilisateur.
```
5. Récupérez localement les photos des futurs utilisateurs proposées sur Moodle (ou
    choisissez-en d’autres si vous préférez). Elles serviront aux futurs clients.

```
Créez un répertoire images/imagesUsers (en parallèle de imagesVoyages) et placez-y
les photos utiles.
```
```
Nous allons maintenant personnaliser la page de l’utilisateur connecté.
```
## Personnalisation du menu

```
Nous allons faire en sorte que maintenant, quand un utilisateur est connecté, il ait sa
photo aƯichée, avec un message personnalisé, et un lien vers sa page de profil, en plus
des liens panier et commandes :
```
1. Adaptez d’abord, dans toutes les views (y compris connexion), l’utilisateur récupéré. Voici
    par exemple la view voyages modifiée :


```
Ne pas oublier d’importer le modèle :
```
```
from applicompte.models import TravelUser
```
```
Le passage, dans toutes les vues, de User à TravelUser est indispensable pour récupérer
la photo.
```
2. Adaptez ensuite les trois menus pour qu’ils aƯichent la photo avec message adapté (pour
    client et staƯ) ou juste un message de bienvenue (pour utilisateur non connecté). Voici
    un exemple pour menuClient.html

```
Pour le moment, le lien profil (comme les liens panier et commandes) ne sont pas
opérationnels.
```
## La page de profil

```
Concrètement, c’est une page de modification du TravelUser (sauf le mot de passe qui passera
par une procédure spéciale, voir TP suivant).
```
```
Dans la capture du menu « client connecté » précédente, on voit un lien de la forme
```
```
<a class="nav-link" href="/user/update/"> profil </a>
```

1. Dans le fichier urls.py d’applicompte, ajoutez le path

```
path('user/update', views.formulaireProfil),
```
2. Créez ensuite dans views.py d’applicompte la view suivante :

```
3.Créez un fichier applicompte/forms.py avec une classe TravelUserForm comme cela
avait été déjà fait dans applitravel :
```
```
Vous pouvez personnalisez les labels comme nous l’avons vu pour applitravel.
```
```
4.Créez ensuite le template applicompte/profil.html
```

```
Ce formulaire aƯiche les valeurs actuelles de l’identifiant, des prénom, nom, email, et
l’image actuelle. Testez l’accès à ce formulaire.
```
```
Ce formulaire évoque une action="/user/updated/". Il faut donc prévoir cette action dans
views.py et le path correspondant dans urls.py.
```
5.Dans urls.py, ajoutez le path

```
path('user/updated', views.traitementFormulaireProfil),
```
6.Dans views.py, écrivez la view de traitement suivante, en comprenant bien les étapes :

```
▪ récupération du TravelUser
▪ récupération du formulaire (instance de TravelUser)
▪ sauvegarde du TravelUser via la sauvegarde du formulaire
▪ récupération du TravelUser modifié
▪ récupération des voyagees
▪ appel de voyages.html
```

Ne pas oublier d’importer le formulaire :
from applicompte.forms import TravelUserForm

7. Vérifiez que tout fonctionne, y compris la mise à jour d’image, et que cela s’actualise sur
    la barre de menu.


# TP11 – Connexion et Déconnexion

## Introduction, Contexte et Objectifs

```
Pour le moment, nous avons codé un CRUD complet, sans nous préoccuper de savoir qui aura
les privilèges du CRUD.
```
```
Le moment est venu de créer un administrateur du site, qui aura seul les autorisations
sensibles.
```
```
Cela passe par la création, avec django, d’un « superuser ». Ce superuser aura accès à la partie
administration du site, avec une interface standard toute prête. Nous verrons alors l’interface
admin par défaut.
```
```
Nous aborderons aussi les fonctionnalités login et logout du système de connexion, ainsi que
la diƯérenciation des menus et des liens.
```
## Le fichier de configuration de l’administration

```
Modifiez le fichier admin.py de l’application applitravel pour y ajouter la gestion de
chacune de vos tables.
```
```
Par ces commandes, on prévoit l’administration des modèles Ville, Voyage et Etape par
le superuser, via l’interface administrateur proposée par django.
```
## Le super-utilisateur

```
Django a besoin d’un superuser pour garantir que quelqu’un a les super-pouvoirs
d’administration. En particulier, si on crée des utilisateurs connectés, il pourra les modifier, les
supprimer.
```

```
1.En ligne de commande, créez le superuser par : python manage.py createsuperuser
```
```
Renseignez l’email et le mot de passe.
```
```
2.Lancez le serveur web et connectez-vous à l’adresse http://127.0.0.1:8000/admin/
```
```
Saisissez l’identifiant et mot de passe du superuser.
```
```
3.Vous avez acès à une interface d’administrateur permettant d’ajouter, modifier ou
supprimer des voyages, des villes ou des étapes. Testez en créant un nouveau voyage,
de nouvelles villes.
```
```
4.En tant que superuser, créez deux autres utilisateurs. L’un ne sera pas « staƯ », l’autre sera
« staƯ ». Vous verrez que ce statut hiérarchise les users et nous permettra, par la suite,
de diƯérencier les menus et les permissions.
```
## L’application de gestion des comptes

```
Nous allons mettre en place une nouvelle application, en parallèle de l’application applitravel.
Elle gèrera tous les aspects de la connexion (login, logout, création de compte, etc).
```
```
Django propose une application dédiée à la gestion des comptes, toute faite et prête à l’emploi,
mais nous allons personnaliser la nôtre, et notamment ses templates, pour utiliser au mieux
bootstrap et contrôler le contenu des divers formulaires. Nous utiliserons les fonctionnalités
d’authentification de django (authenticate, login, logout, ...).
```
```
1.Créez la nouvelle application applicompte par la commande :
python manage.py startapp applicompte
Comme pour applitravel, cette commande a créé de nouveaux fichiers dans le projet.
```
```
2.Enregistrez cette application dans la liste INSTALLED_APPS du fichier settings.py comme
nous l’avions fait pour applitravel.
```
```
3.Nous allons maintenant nous occuper des urls. Jusqu’à maintenant, elles étaient toutes
regroupées dans le fichier urls.py de webtravel, et c’est logique puisqu’il n’y avait qu’une
application applitravel.
```
```
Maintenant, nous allons gérer plusieurs applications (au moins 2) et donc nous allons
pourvoir chacune d’un fichier urls.py avec ses propres url.
```
```
Nous allons donc transférer les url propres à applitravel dans le dossier applitravel, et
créer séparément des url propres à l’application applicompte.
```

Enfin, le fichier urls.py de webtravel centralisera toutes les urls par des inclusions.

Dans un premier temps, nous allons nettoyer le fichier urls.py de webtravel.

a. Créez un fichier urls.py dans applitravel (au même niveau que models.py ou views.py)

b. Reportez-y toutes les url propres à applitravel. Votre fichier devrait plus ou moins
ressembler à :

C .Modifiez le fichier urls.py de webtravel pour qu’il insère les urls de applitravel :

d. Vérifiez que tout fonctionne. C’est plus logique de faire ainsi : à chaque application
ses urls, et le fichier urls.py du projet inclut les fichiers urls.py de toutes les
applications.

e. Créez maintenant un fichier urls.py propre à l’application applicompte, et n’oubliez
pas de l’inclure dans le fichier urls.py du projet webtravel. Ce nouveau fichier urls.py
contiendra au départ le code suivant :


```
Ce path, qui utilise le système d’authentification prêt à l’emploi de django
(django.contrib.auth) permet d’inclure l’url de login. Cette url n’est bien sûr pas
encore opérationnelle puisque nous n’avons pas encore codé le template
login.html.
```
```
Comme nous allons personnaliser la connexion, nous allons redéfinir les templates
nécessaires.
```
```
Nous allons aussi personnaliser les menus, car un utilisateur non connecté, un
utilisateur basique connecté (un client) ou un utilisateur « staƯ » n’auront pas les
mêmes menus.
```
```
Pour le moment, le template menu.html a été codé dans l’application applitravel,
puisque c’était la seule. Cependant, il peut aussi y avoir une certaine logique à coder
les menus dans applicompte, puisque les menus proposés vont dépendre du statut
de l’utilisateur. C’est ce que nous allons finalement choisir comme solution : coder
les menus dans applicompte.
```
## Relocalisation du menu

```
Pour le moment, vous avez dans applitravel un template menu.html.
```
```
Ce menu est en fait adapté à un utilisateur qui a des permissions avancées de type staƯ
(les permissions liées à la création, la modification et la suppression d’objets).
```
```
Nous allons maintenant traduire la hiérarchie chez les utilisateurs, ce qui conduira à
une personnalisation du menu.
```
```
Nous allons donc créer, sur la base de menu.html, trois fichiers menuStaƯ.html,
menuBasicUser.html et enfin, le menu sans connexion menuNonConnecte.html.
```
1. Créez un répertoire templates/applicompte dans le répertoire applicompte, comme
    cela avait été fait pour applitravel.


2. Déplacez-y le template menu.html.
3. Dans le template base.html d’applitravel, modifiez l’include du menu pour qu’il soit
    récupéré dans les templates d’applicompte à l’avenir.
4. Testez que tout fonctionne. Attention, si vous obtenez une erreur de la forme «
    TemplateDoesNotExist », il faut probablement relancer le serveur.

## Personnalisation du menu

```
Nous allons en fait créer trois menus diƯérents, ce sera plus simple :
```
```
▪ un menu pour les internautes non connectés
▪ un menu pour les clients connectés
▪ un menu pour les administrateurs
```
1. Créez le template applicompte/menuNonConnecte.html dont le code permettra
    d’accéder à la liste des voyages, de s’inscrire et de se connecter :
2. Créez le template menuStaƯ.html, qui présente les 4 liens du CRUD, avec en plus un
    lien de déconnexion :


3. Créez enfin le template menuClient.html, qui propose un lien vers la liste des voyages,
    et des liens vers le panier, vers l’historique de commandes et un lien de déconnexion :

```
Pour le moments les liens de login, logout, inscription, panier et commandes ne sont
pas opérationnels.
```
Remarques :

```
a. Nous ne pouvons pas vraiment tester ces templates puisque nous n’avons pas encore
le moyen de nous connecter autrement qu’en étant staƯ;
```
```
b. Il va aussi falloir, plus tard, personnaliser les accès aux fonctions du CRUD accessible
à partir de voyages.html. Un utilisateur quelconque aura aussi une diƯérentiation
dans l’aƯichage d’un voyage. Nous réglerons cela plus tard.
```
4. Vous allez maintenant, dans applitravel/base.html, insérer des tests qui permettront de
    savoir quel menu il faut insérer :

```
si user est staƯ on insère menuStaƯ.html sinon si user est authentifié on
insère menuClient.html
sinon on insère menuNonConnecte.html
```

5. Vérifiez ce que vous pouvez vérifier, à savoir ce qui se passe dans le cas d’un user staƯ et
    dans le cas d’un user non connecté. Pour le non connecté, vous devrez vous
    déconnecter à partir du portail administrateur, puis relancer l’url voyages/.

## Création des templates login et logout d’applicompte

1. Dans applicompte, créez le fichier template login.html avec le code suivant :

```
Dans ce code il y a un formulaire de connexion, en mode bootstrap, et hors-formulaire
des liens d’inscription et de renouvellement du mot de passe.
```
```
Testez maintenant l’url http://127.0.0.1:8000/login/ et vérifiez que vous arrivez à la page
de connexion.
```

```
Par contre l’envoi du formulaire provoquera une erreur puisque rien n’est prévu encore
pour l’action de connexion (ni url, ni view).
```
2. Créez le template applicompte/logout.html sur le modèle suivant (vous pouvez
    personnaliser)

## Les url et les views

1. Complétez le fichier urls.py d’applicompte pour y ajouter l’appel de deux views : logout
    et connexion

```
2 Dans le fichier views.py d’applicompte, créez les views suivantes :
```
```
a. connexion, qui récupère les éléments du formulaire de connexion (username et
password), authentifie la connexion (en retournant par authenticate un user ou bien
None), et qui retourne le contexte adapté (avec notamment le user, qui servira
forcément d’une manière ou d’une autre)
```

```
b. deconnexion, qui déconnecte le user connecté et retourne le contexte avec le
template de logout.
```
3. Faites des tests de connexion : staƯ et client (non staƯ), et aussi internaute non connecté.
Vous devez voir la diƯérentiation des menus. Vous pouvez aussi, une fois connecté, aller sur
la page d’administration du projet django pour voir comment vous êtes reconnu. Par contre,
vous constatez que tout le monde a encore accès au CRUD! C’est un des points sur lesquels
allons travailler.


## DiƯérenciation des liens aƯichés

```
Pour le moment, tout le monde a les mêmes boutons d’actions dans la liste des voyages
ou dans les détails d’un voyage. Arrangez-vous, comme pour les menus, pour que :
```
```
a. Dans la liste des voyages, un utilisateur staƯ ait à sa disposition les liens détails,
modification et suppression,
```
```
b. Dans la liste des voyages, un client ait un lien d’achat (type panier) et le lien détails,
```
```
c. Dans la liste des voyages, un utilisateur non connecté ait le lien détails,
```
```
d. Dans les détails d’un voyage, les actions de suppression d’une étape et d’ajout d’une
étape ne soient accessibles qu’au staƯ (et qu’un client ou un utilisateur non
connecté n’aient accès qu’au tableau simplifié des étapes).
```
```
Vous pourrez utiliser les instructions :
```
```
▪ {% if user.is_staƯ %} (utilisateur staƯ)
```
```
▪ {% if user.is_authenticated %} (staƯ ou client)
```
## Mise en garde de sécurité!

```
Vous ferez attention à une chose : la sécurisation n’est pas faite sur les views (pour
preuve, un utilisateur non connecté peut directement entrer une url de la forme
```
```
http://127.0.0.1:8000/voyages/1/update/
```
```
et disposer des privilèges staƯ.
```
```
Il faut impérativement l’empêcher.
```
## Sécurisation des views

1. Sécurisation de la liste des villes de la view villes est un cas de base :

```
▪ si l’utilisateur est staƯ, on lui retourne la liste des villes,
▪ sinon, si c’est un client, on lui retourne la liste des voyages,
▪ sinon, (utilisateur non connecté), on lui retourne la page de connexion.
```

```
Cela se traduit par un aménagement de la view villes. Remarquez qu’à partir de
maintenant, on retournera le user, ça peut toujours servir. En particulier, plus tard
on aƯichera la photo de l’utilisateur connecté.
```
Pensez à importer User à l’aide de :

```
from django.contrib.auth.models import User
```

```
2.Testez maintenant, dans les trois cas (utilisateur non connecté, client, staƯ), ce que
donne l’injection dans la barre d’url de l’url
```
```
http://127.0.0.1:8000/villes/
```
```
3.Sécurisez maintenant TOUTES LES VIEWS. Les permissions d’accès aux pages du site
ou aux actions de type contrôleur sont indiquées ci-dessous :
```
```
Page du site
```
```
non
connecté
```
```
client
connecté
```
```
staƯ
connecté
voyages autorisé autorisé autorisé
voyage autorisé autorisé autorisé
villes interdit interdit autorisé
formulaire création d’un voyage interdit interdit autorisé
formulaire de modification d’un voyage interdit interdit autorisé
formulaire de création d’une ville interdit interdit autorisé
formulaire de modification d’une ville interdit interdit autorisé
formulaire de connexion autorisé interdit interdit
déconnexion interdit autorisé autorisé
```
```
Action
```
```
non
connecté
```
```
client
connecté
```
```
staƯ
connecté
creerViller interdit interdit autorisé
supprimerVille interdit interdit autorisé
modifierVille interdit interdit autorisé
creerVoyage interdit interdit autorisé
supprimerVoyage interdit interdit autorisé
modifierVoyage interdit interdit autorisé
ajouterEtape interdit interdit autorisé
supprimerEtapeDansVoyage interdit interdit autorisé
```
4. Comme pour la page villes, testez tous les accès.


# TP10 – Modification du modèle Voyage - Upload d’image

## Introduction, Contexte et Objectifs

```
Le moment est venu d’apporter un élément visuel à notre projet. Le CRUD est opérationnel,
mais la liste des voyages n’est pas vraiment attirante. Rien ne vaut une belle image de voyage
pour donner envie aux acheteurs.
```
```
Dans ce TP nous allons, étape par étape, arriver à intégrer une image au modèle de Voyage.
```
```
Cette image sera dynamique : au moment de la création d’un voyage ou de sa modification,
l’image sera à renseigner ou à modifier dans le formulaire dédié.
```
```
Nous allons donc faire évoluer le modèle Voyage pour ajouter un attribut de type fichier
(ImageField).
```
```
Nous allons aussi donner un aspect plus pratique à la liste des voyages. L’image du voyage sera
cliquable pour accéder aux détails, et nous intégrerons les icônes bootstrap habituels.
```
## Le répertoire de stockage des images

- Créez, au niveau de la racine webravel du projet, un répertoire « images » puis un sous-
    répertoire imagesVoyages qui contiendra les images qui seront téléversées
       (« uploadées ») par l’utilisateur plus tard.
- Dans le fichier settings.py, ajoutez les lignes suivantes, qui indiquent le répertoire des
    fichiers téléversés :
- Dans le fichier settings.py, ajoutez à la variable TEMPLATES la ligne de la capture
    suivante. Elle permet aux templates d’accéder aux fichiers images (notamment) :


- Dans le fichier urls.py, ajoutez les deux import suivants :

```
Ces deux import permettent l’ajout qui suit :
```
- Ajoutez à la fin du fichier urls.py la ligne suivante :

```
Les modifications précédentes vont permettre d’aƯicher les images des voyages.
```
```
Tout est maintenant prêt pour aller chercher les images au moment de la création ou de la
modification.
```
## Installation de la bibliothèque Pillow

```
Pour gérer des données de type ImageField, il est nécessaire d’installer la bibliothèque Pillow
```
```
a. Positionner vous dans le répertoire du projet webtravel
```
```
b. Puis lancer l’installation : python -m pip install Pillow
```

## Modification du modèle Voyage dans models.py

```
Dans cette partie, nous incorporons au modèle Voyage un nouvel attribut image qui
indiquera le nom du fichier à aƯicher. Créez, dans le modèle Voyage, un attribut de type
ImageField :
```
## Migration de Voyage

- Procédez maintenant à la migration qui permettra de tenir compte de la modification du
    modèle Voyage : makemigration puis migrate
- Vérifiez, dans sqlitebrowser, que tout a été pris en compte :
- Ouvrez le fichier images.zip fournit sur Moodle. Vous pouvez utiliser les images fournies
    ou celles de votre choix (taille 300x150 environ au format JPG ou PNG)
- Déplacez à la main, dans images/imagesVoyages, les images qui vous intéressent pour
    ces voyages uniquement (en quelque sorte, nous faisons un upload à la main).
- Changez ensuite à la main, dans sqlitebrowser, la valeur du champ image de chaque
    voyage en lui donnant le nom du fichier correspondant.


- Pensez à enregistrer les modifications dans sqlitebrowser.

## Modification du template voyages.html

- Dans le template voyages.html, faites en sorte que l’aƯichage d’un voyage incorpore
    l’image en ajoutant une balise image :

```
Si tout s’est bien passé, vous devriez voir apparaître vos images.
```
- Dotez les diƯérentes balises div de classes css dont vous écrirez vous-même le code
    pour qu’avec un peu de technologie flex, vous ayez une mis en forme de la page
    voyages.html plus propre.
- Enfin, en utilisant les icônes bootstrap (vous pouvez les récupérer sur la page
    https://icons.getbootstrap.com/), remplacez les liens textuels par des liens plus

```
intuitifs du style
```

## Mise à jour du formulaire de création d’un voyage

1. Dans la définition du formulaire du fichier forms.py, nous allons ajouter le champ
image au sein de la classe VoyageForm
2. Dans le fichier formulaireCreationvoyage.html, il faut ajouter le type d’encodage des
fichiers

```
Cette modification interviendra également dans le formulaire de modification (voir plus
tard).
```
```
3.Testez votre nouveau formulaire.
```
## Mise à jour de la view creerVoyage dans views.py

- Modifiez la view creerVoyage pour qu’elle prenne en compte la gestion des fichiers


- Testez que tout fonctionne en créant un nouveau voyage. Vérifiez, dans votre
    architecture de fichiers, que la fichier image a bien été uploadé et que son nom a bien
    été renseigné dans la base de données.

## Mise à jour du formulaire de modification d’un voyage

```
Les modifications apportées au formulaire de création vont être également apportées à
celui de la modification.
```
- Modifiez la balise form pour permettre l’envoi de fichiers (enctype).
- Ajoutez un champ « input » permettant de sélectionner un fichier, comme pour la
    création.
- Vérifiez l’aƯichage du formulaire

## Mise à jour de la view modifierVoyage dans views.py

```
Dans la view modifierVoyage, insérez le paramètre request.FILES dans la récupération du
formulaire puis vérifiez que tout fonctionne
```

## Complément CSS

```
Si ce n’est pas déjà fait, stylisez un peu la liste des villes pour avoir quelque chose de plus «
bootstrap » notamment des icônes
```

# TP9 – Supprimer et modifier les étapes d’un voyage

## Introduction, Contexte et Objectifs

```
Nous savons maintenant supprimer ou modifier un voyage et une ville.
```
```
On retient aussi que, grâce aux liens en cascade, toute modification ou suppression d’un
voyage ou d’une ville a des conséquences sur les autres tables, automatiquement gérées par
les mécanismes de django.
```
```
Dans ce TP, on va mettre en place la suppression et la modification d’une étape (le détail du
voyage).
```
```
Dans les faits, soit on supprime la ville dans le voyage, soit on modifie le nombre de jours de
l’étape dans le voyage.
```
## Les liens de suppression dans le tableau des étapes

```
Dans le template voyage.html, créer pour chaque ligne du tableau des étapes un lien de
suppression, de la forme :
```
```
<a href="/voyages/{{voyage.IDVoyage}}/deleteEtape/{{uneetape.IDEtape}}">Supprimer</a>
```
```
Chaque lien « Supprimer » embarque à la fois l’idVoyage et l’idEtape.
```
```
L’url correspondante dans urls.py et la vue dans view.py n’ont pas encore été créées, c’est la
suite du programme.
```
## L’url de suppression dans urls.py

```
Créez, dans urls.py, une nouvelle ligne path qui fera correspondre le lien précédent de
suppression à la vue (pas encore créée) supprimerEtapeDansVoyage.
```
```
Ce path sera de la forme :
```
```
path('voyages/<int:voyage_id>/deleteEtape/<int:etape_id>/',
views.supprimerEtapeDansVoyage),
```

## La view de suppression dans views.py

1. Créez ans le fichier views.py la vue

```
supprimerEtapeDansVoyage (request, voyage_id, etape_id)
```
```
Cette vue devra :
```
```
a. Récupérer l’étape à supprimer (méthode get),
```
```
b. Appeler la méthode delete() sur cette composition,
```
```
c. Récupérer le voyage dont l’iIDVoyage est passé en paramètre,
```
```
d. Récupérer toutes les étapes concernant le voyage dont l’IDVoyage est passé en
paramètre,
```
```
e. Refabriquer la liste des villes du voyage (les étapes),
```
```
f. Récupérer toutes les villes,
```
```
g. Appeler le template voyage.html en lui fournissant le voyage, les Etapes du voyage et
la liste des villes (comme on l’a fait dans le formulaire d’ajout d’une étape.
```
```
2.Vérifiez que tout fonctionne.
```
```
3.Si ce n’est pas déjà fait, améliorez le visuel avec l’icône bootstrap « poubelle ».
```
## Et la modification?

```
Pour modifier, on écrase tout simplement la ligne correspondant à la modification souhaitée,
en indiquant une autre quantité : l’appel à delete eƯace l’étape, puis on le recrée
immédiatement avec le bon nombre de jours. Nous l’avons déjà fait lors de l’ajout d’une étape.
```
```
Ajouter une icône juste avant l’icone poubelle pour chaque ligne, permettant l’appel d’un
formulaire demandant le nombre de jours de l’ étape et modifiant l’étape dans la base de
données.
```

# TP8 – Supprimer et modifier voyage et ville

## Introduction, Contexte et Objectifs

```
Nous savons maintenant créer des formulaires, les récupérer, alimenter la base de données,
et la lire. Autrement dit, les aspects C (create) et R (read) du CRUD. Il nous reste à voir les
aspects U (update) et D (delete).
```
```
Nous allons tout d’abord voir comment de supprimer un voyage puis comment le modifier.
Nous ferons ensuite la même chose pour les villes.
```
## Les liens de modification et de suppression dans voyages.html

```
Dans le template voyages.html, créer pour chaque voyage listée un lien de modification
et un lien de suppression personnalisés, de la forme :
```
```
Les urls correspondantes dans urls.py et les vues dans view.py n’ont pas encore été
créées, c’est la suite du programme.
```
## L’url de suppression dans urls.py

```
Créez, dans urls.py, une nouvelle ligne path qui fera correspondre le lien précédent de
suppression à la vue (pas encore créée) supprimerVoyage(request, voyage_id). Ce path
sera de la forme
```
```
path('voyages/<int:voyage_id>/delete/', views.supprimerVoyage),
```

## La view de suppression dans views.py

1. Créez la view supprimerVoyage(request, voyage_id) dans le fichier views.py. Cette vue
    devra :

```
a. Récupérer le voyage à supprimer (grâce à la méthode get),
```
```
b. Appeler la méthode delete() sur cette voyage,
```
```
c. Récupérer la liste de toutes les voyages grâce à la méthode all() comme dans la vue
voyages,
```
```
d. Appeler le template voyages.html en lui fournissant le liste des voyages (comme dans
la vue voyages).
```
2. Vérifiez qu’après avoir créé un voyage de test, sans ville ajouté, vous pouvez la supprimer.
    Contrôlez l’eƯet dans sqlitebrowser.

```
3.Créez un nouveau voyage, ajoutez-lui des villes, et vérifiez avec sqlitebrowser que les
villes sont apparus dans la composition de la voyage créée. Puis supprimez le voyage,
et vérifiez que les lignes correspondant à ce voyage dans la table Etape ont aussi
disparu, ainsi que le voyage dans la table Voyage.
```
## L’url de création du formulaire de modification dans urls.py

```
Créez, dans urls.py, une nouvelle ligne path qui fera correspondre le lien précédent de
modification à la view (pas encore créée)
```
```
aƯicherFormulaireModificationVoyage(request, voyage_id)
```
```
Ce path sera de la forme
```
```
path('voyages/<int:voyage_id>/update/', views.aƯicherFormulaireModificationVoyage),
```

## La view formulaire de modification dans views.py

```
Créez, dans le fichier views.py, la view
```
```
aƯicherFormulaireModificationVoyage(request, voyage_id)
```
```
Cette view devra :
```
```
a. Récupérer le voyage à aƯicher dans le formulaire (grâce à la méthode get),
```
```
b. Appeler formulaireModificationvoyage.html, le template qui sera chargé d’aƯicher le
formulaire prérempli, avec comme contexte le voyage à modifier.
```
## Le template formulaireModificationVoyage.html

```
Créez le template formulaireModificationVoyage.html. Il aƯiche le même formulaire que
le template de création d’une voyage, à la diƯérence près que pour les input, les value
sont renseignées à partir des attributs de la voyage à modifier.
```
```
Autre diƯérence bien sûr : Le lien de traitement qui indique une action updated n’est pas
encore codée.
```

## L’url de modification dans urls.py

```
Créez, dans urls.py, une nouvelle ligne path qui fera correspondre le lien précédent de
modification à la vue (pas encore créée) modifierVoyage(request, voyage_id)
```
```
Ce path sera de la forme
```
```
path('voyages/<int:voyage_id>/updated/', views.modifierVoyage),
```
## La view modifierVoyage dans views.py

```
Créez la view modifierVoyage(request, voyage_id) dans le fichier views.py. Cette vue
devra :
```
```
a.Rrécupérer la voyage à modifier (grâce à la méthode get),
```
```
b. Récupérer le formulaire posté, avec pour instance le voyage récupéré,
```
```
c. Si le formulaire est valide, appeler sur lui la méthode save(), ce qui aura pour eƯet de
mettre la voyage à jour dans la base de données,
```
```
d. Aller rechercher dans la base la voyage modifié,
```

```
e. Appeler traitementFormulaireModificationVoyage.html, le template qui sera chargé
d’aƯicher un message de confirmation de la modification (en précisant le nom du
voyage modifié).
```
## Le template traitementFormulaireModificationVoyage.html

```
Créez le template traitementFormulaireModificationVoyage.html. Il confirme
simplement que le voyage (dont on précise le nom) a bien été modifié. Vérifiez
maintenant que tout fonctionne.
```
## Et pour les villes?

```
Recommencez tout pour les villes pour permettre la modification et la suppression
d’une ville.
```

# TP7 – Formulaire de détail d’un voyage

## Introduction, Contexte et Objectifs

```
Nous savons maintenant mener à bien toutes les étapes qui permettent de créer un formulaire
simple, et récupérable selon un modèle de formulaire (VilleForm, VoyageForm), qui permet
une cohérence totale entre les modèles et les tables de données.
```
```
Pour les étapes, nous allons créer un formulaire de même type, qui proposera une liste (type «
select ») de villes pouvant entrer dans la constitution d’un voyage.
```
```
Ce formulaire ne fera pas l’objet d’une page à part, comme pour la création d’une ville ou d’un
voyage, mais sera directement intégré à la page de détail d’un voyage, sous le tableau des
étapes d’un voyage. C’est plus simple car nous verrons ainsi évoluer en direct le tableau des
étapes.
```
## Création d’un nouveau formulaire

```
Dans le fichier forms.py, créez une nouvelle classe de formulaire :
```
1. son nom est EtapeForm, il hérite de ModelForm
2. ses deux champs sont :

```
 Ville, qui donnera un select dont les choix seront tirés de la table Villes,
 Nb_Jours, dont la valeur sera une chaîne de caractères à remplir par l’utilisateur.
```
```
Inspirez-vous des formulaires déjà existants et mis en place dans le TP précédent.
```
## Modification de la view voyage dans le fichier views.py

```
Modifiez la view voyage :
```
1. Récupérez tous les villes par une requête all(), ils serviront à construire un select de
    formulaire,

```
b. Passez cette liste de ville au contenu à transmettre au template, en plus de ce qui
était déjà transmis.
```

## Modification du template voyage.html

```
Sous le tableau du détail du voyage, insérez un formulaire composé d’un select de ville
(avec son label) et d’un input pour saisir la quantité. Vous noterez que ce formulaire est
à la mode bootstrap (c’est une autre manière de faire des formulaires), et que le select
est construit dans une boucle for à partir de la liste des villes calculée dans la view
précédente.
```
```
Le code peut être le suivant :
```
```
Pour le moment, l’url décrite et la vue de traitement du formulaire ne sont pas écrites.
Néanmoins, vous pouvez aƯicher le formulaire d’ajout.
```
## Création de l’url

```
Modifiez le fichier urls.py pour renseigner le nouveau path :
```
## Création de la view ajouterEtape

```
Ajoutez la view ajouterEtape dans le fichier views.py. Cette vue ressemble beaucoup à
la vue voyage.
```
1. On récupère le formulaire posté,


2. Si l’étape est déjà présent dans le détail de la ville, on eƯace la ligne
    correspondante,
3. On crée la nouvelle instance de Etape pour la ville constituant l’étape, avec
    son nombre de jour,
4. On l’insère dans la base,
5. On reecrée le tableau des étapes et prépare un nouveau formulaire d’ajout
    d’étape.
6. On rappelle le template voyage.html

C’est un peu compliqué (les valeurs des attributs de la composition créée), donc voici
un exemple de code, commenté :


Vérifiez que tout fonctionne, et que le tableau s’enrichit au fur et à mesure.

Utilisez Bootstrap pour améliorer l’interface de votre page.


# TP6 – Premiers formulaires

## Introduction, Contexte et Objectifs

```
Pour le moment nous accédons à la base de données, et nous consultons les données, pour
aƯichage. C’est de la « lecture seule ». L’idée est ici de :
```
- construire un formulaire pour récupérer les données de futurs villes,
- traiter l’envoi du formulaire et ainsi avoir une action d’écriture sur la base de données.
    Cette action se fera sans être connecté au site. Autrement dit, tout le monde est «
    administrateur ». Nous verrons la connexion plus tard.

```
Il y a une méthode complètement automatique pour créer un formulaire adapté aux attributs
d’une classe. Nous allons l’utiliser pour les formulaires de création d’un voyage et d’une ville.
```
## Création du fichier forms.py

1. Au même niveau que views.py, créez un fichier forms.py. Nous allons y définir notre
    formulaire.
2. Dans ce fichier, importez la bibliothèque forms de django, puis de forms importez
    ModelForm, qui permet les formulaires automatiques.

```
Créez la classe VilleForm, qui hérite de ModelForm, et qui représentera le formulaire
correspondant à une nouvelle Ville. Le code, donné juste après, est vraiment des plus
simples. La classe Meta fait le travail.
```

## Création d’une view dans le fichier views.py

1. Créez dans views.py, la view formulaireCreationVille qui retourne un render qui indique
    un template (pas encore créé) applitravel/formulaireCreationVille.html, ainsi qu’un
    instanciation du formulaire :

```
Ne pas oubliez d’importer le formulaire : from applitravel.forms import VilleForm
```
2. Dans le fichier urls.py, définissez un path qui permet d’accéder à ce formulaire.
Ce path pourra être de la forme villes/add et appellera la « vue » précédente.
3. Dans le répertoire template/applitravel, créez un fichier formulaireCreationVille.html
    qui aura la même base que les autres :


On voit tout la puissance des modèles Django pour la génération du formulaire.

Le « csrf_token » est un « jeton » qui sert à lutter contre les failles CSRF.

https://www.leblogduhacker.fr/faille-csrf-explications-contre-mesures/

Pour le moment, on ne renseigne pas l’action du formulaire. Plus tard, l’action sera la
création de la nouvelle ville.

Si tout est bien fait, l’url 127.0.0.1:8000/villes/add doit amener au formulaire, qu’on
peut remplir, mais dont l’envoi ne donnera rien, puisque le traitement du formulaire n’a
pas encore été programmé.

Pensez à ajouter un lien dans le menu pour amener au formulaire.


## L’action lancée suite à l’envoi du formulaire

```
1.Créez dans views.py la view creerVille qui va gérer le traitement des informations reçues
via le formulaire :
```
```
a. on récupère le formulaire :
```
```
form = VilletForm(request.POST)
```
```
b. si le formulaire est « valide » (vérification automatique) alors on récupère le nom de
laville par :
```
```
nomV = form.cleaned_data['nomVille']
```
```
c. puis on sauvegarde les données saisies en base.
```
```
d.Enfin, on retourne un render vers le template nommé
applitravel/traitementFormulaireCreationVille.html, avec comme contenu le nom
de la ville récupéré (template pas encore créé).
```
```
2.Dans le fichier urls.py, définissez un path qui permet d’accéder à la page annonçant que
le traitement a bien été eƯectué. Ce path sera de la forme villes/create et appellera la
view précédente.
```

```
3.Dans le template formulaireCreationVille.html, indiquez maintenant la bonne action :
/villes/create
```
```
4.Créez traitementFormulaireCreationVille.html, template qui hérite de base.html,
comme tous les autres, et prévient juste que la création a été eƯectuée, et utilisant la
variable de gabarit {{nom}} qui permet de rappeler le nom de la nouvelle ville :
```
```
5.Testez que tout fonctionne. Vous pourrez aussi contrôler, dans sqlitebrowser,
l’enrichissement progressif de la table des villes.
```
## Avez-vous bien tout assimilé?

```
Recommencez tout, cette fois pour la création d’un nouveau voyage (titre, et prix).
```

# TP5 – Vue et template de détail d’un voyage

## Introduction, Contexte et Objectifs

```
Les premiers templates, améliorées par le gabarit base.html, font des listes des voyages et de
villes. Nous allons agrémenter notre projet d’un nouveau template qui donnera les détails sur
un voyage (étapes parcourues). Nous mettrons aussi en place l’url vers ce template, ainsi que
le lien vers ce template dans la liste globale des voyages.
```
## Modification du fichier urls.py

```
1.Nous allons créer une url générique pour le détail d’un voyage. Nous pourrons l’appeler
ainsi :
```
```
http://127.0.0.1:8000/voyages/1/ http://127.0.0.1:8000/voyages/2/
```
```
Dans le fichier urls.py, ajoutez le path de la dernière ligne (il contient un int variable
nommé voyage_id), path qui envoie vers une nouvelle vue « voyage », pas encore codée
dans le fichier applitravel/views.py.
```
```
2.Créez dans applitravel/views.py une view voyage dont le code est le suivant. Vous
remarquerez qu’elle utilise un paramètre supplémentaire voyage_id qui correspond à la
variable du path.
```

```
Notez la requête pour récupérer LE bon voyage :
```
```
leVoyage = Voyage.objects.get(IDVoyage = voyage_id)
```
```
a. la méthode get qui récupère un élément de la base en fonction du critère
qui suit en paramètres
```
```
b. le critère donné : l’attribut IDVoyage doit avoir la même valeur que l’int voyage_id
récupéré par la view voyage.
```
```
Notez aussi, comme précédemment, la façon de transmettre au template l’information
concernant ce voyage (sous forme de dictionnaire dans le render).
```
3. Créez maintenant le template voyage.html avec le code suivant. Analysez ce code, vous
    y retrouverez des éléments déjà vus. Vous remarquerez en particulier l’utilisation de la
    variable de gabarit dans l’aƯichage <p>{{voyage}}</p>.

```
Cette variable voyage est celle qui a été passée dans le dictionnaire de la view
précédente.
```

4. Essayez maintenant les deux url du 1.
5. Nous allons maintenant ajouter, dans la page voyages.html, les liens de détail menant à

```
la page relative à chaque voyage. Changez le code pour intégrer ces liens :
```
6.Vérifiez l’eƯet. Pour le moment, cela ne présente pas vraiment d’intérêt, puisque la vue de
détail n’apporte rien de plus que les renseignements déjà donnés par la page
voyages.html.

```
Mais cela va bientôt changer, puisque vous allez compléter cette vue de détail d’un
voyage en listant les étapes proposée.
```

## Amélioration du template détail d’un voyage

```
Cette partie est à faire en autonomie en utilisant ce que nous avons déjà vu.
```
```
Vous devrez améliorer la view d’un voyage, définie dans views.py, pour qu’elle donne
aussi les villes visitée et le nombre de jour pour chaque étape.
```
1. Cette amélioration demandera de faire une requête sur la base de données, en
    récupérant de la table Etape toutes les entrées pour lesquelles l’identifiant du
    voyage correspond à celui passé en argument (voyage_id). Cette requête utilise la
    méthode « filter » :

```
lesEtapes = Etape.objects.filter(voyage = voyage_id)
```
```
avec voyage qui désigne la clé étrangère de la classe Etape et voyage_id est le
paramètre passé dans l’url.
```
```
Puis vous transmettrez la liste des étapes au template par l’intermédiaire du
dictionnaire python dans lequel il n’y a pour le moment que le voyage à aƯicher. Voici en
gros les étapes de la view que vous pouvez valider :
```
```
# récupération le voyage dont l'identifiant a été passé
# en paramètre (c'est l'int voyage_id)
```
```
# récupération des étapes constituant le voyage en utilisant le méthode .filter
```
```
# on retourne l'emplacement du template, le voyage récupérée de la base
# et la liste des étapes
```
```
Enfin, au niveau du template voyage.html, vous devez aƯicher le contenu de chaque
étape à l’aide de la méthode __str__
```
2. Vous utiliserez les classe BOOTSTRAP pour aƯicher les étapes dans un tableau mis
    en forme


# TP4 – Les gabarits et les fichiers statiques

## Introduction, Contexte et Objectifs

```
Les premières vues (templates) montrent de la répétition de code html. Par exemple, l’entête
html est dupliquée. Ou encore, le menu issu de code bootstrap : tout changement doit être
reproduit dans les deux templates voyages.html et ville.html, ce qui n’est pas pratique, et
source d’oublis.
```
```
L’idée est de fournir un « gabarit » pour que chaque vue produite adopte ce gabarit, en le
personnalisant.
```
```
Nous allons aussi ajouter quelques fichiers « statiques » comme des fichiers css ou des
images.
```
## La vue de base

```
1.Créez dans le répertoire templates/applitravel un fichier base.html dont le code est le
suivant :
```
```
Dans ce fichier base.html, il y a quatre parties spéciales : deux include et deux block
```
```
{% block title%}{% endblock%}
{% include 'applitravel/menu.html' %}
{% block main%}{% endblock%}
{% include 'applitravel/footer.html' %}
```

```
Les deux include vont inclure des parties de code servant à terme à tous les templates
(menu et pied de page), et qu’on va donc factoriser en 2 fichiers pour les inclure à
chaque fois.
```
```
Ces include vont être stockés dans des fichiers html, localisés dans le répertoire des
templates.
```
```
Les deux block seront juste des blocs de code précisés dans les diƯérents templates
(voyages.html, villes.html).
```
```
Ces block ne feront donc pas l’objet de fichiers à part. Ils seront intégrés aux templates.
```
2.Créez les deux fichiers suivants pour les include :

```
a.menu.html
```
```
Ce fichier contient le code html du menu bootstrap. On le perfectionne encore un
peu. Voir la page :
```
```
https://getbootstrap.com/docs/5.3/components/navbar/
```
```
b.footer.html
```
```
Ce fichier contient le code html du footer
```

```
3.Vous pouvez donner les noms que vous voulez aux blocs suivants, les noms title, footer
ne sont pas imposés.
```
```
Ces blocs correspondent à des zones que nous allons pouvoir personnaliser. Modifiez
la page voyages.html pour qu’elle se présente ainsi
```
- la première ligne est une balise de gabarit qui indique que voyages.html hérite de
    base.html
- la deuxième partie est une autre balise de gabarit qui indique quel doit être le contenu
    du bloc « title »
- la troisième indique le contenu du bloc « main »

```
Sauvegardez, lancez le serveur et vous constaterez sauf erreur que le visuel n’a pas
changé.
```
```
4.Reproduisez le même changement pour villes.html
```
En résumé :


- voyages.html et villes.html héritent de base.html,
- base.html se charge d’inclure les liens bootstrap, le menu et le footer qui sont dans
    des fichiers facilement identifiables et modifiables,
- pour compléter base.html, voyages.html et villes.html proposent des block
    personnalisés, décrits dans chaque template.

## Un peu de css personnalisé

```
Ajoutons un fichier css personnalisé à notre projet : ce sera un fichier « statique », dont le
chemin d’accès est spécifique.
```
```
1.Dans la liste INSTALLED_APPS du fichier settings.py, vérifiez que la ligne
'django.contrib.staticfiles' est présente.
```
```
2.Vérifiez que la ligne STATIC_URL = 'static/' y figure aussi.
```
```
3.Créez un répertoire applitravel/static/applitravel/css et créez un fichier styles.css dans ce
répertoire. Ecrivez le css pour donner aux titres h2 un background-color red.
```
```
4.Modifiez votre fichier base.html pour incorporer, en première ligne, le code {% load static
%}
```
```
5.Ajoutez la balise link qui permet d’aller récupérer le css, avec un href comme ci-dessous
```

```
6.Vérifiez que tout fonctionne et que les titres sont bien aƯichés en rouge, pour les voyages
et les villes. Comme ce n’est pas ce qui se fait de mieux en termes de css, on ne va pas
garder ces titres rouges, mais vous allez faire en sorte que le footer soit un « sticky footer
».
```
```
Autrement dit, le footer colle en bas de la fenêtre. C’est particulièrement visible quand
le contenu de la page est si petit que le footer a tendance à apparaître en plein milieu.
```
```
Pour cela, vous pouvez utiliser le display : flex, ou d’autres techniques :
```
```
https://codeconvey.com/flexbox-sticky-footer/
```
## Une icône pour l’application applitravel

```
1.Sélectionnez une image que vous allez enregistrer au format png (vous pouvez prendre
une taille 50 x 50 pixels de votre choix où celle fournie avec le TP). Enregistrez-la dans
un répertoire static/applitravel/img (à créer, en parallèle de css).
```
```
2.Ajoutez, dans base.html, une balise dans le head :
```

Vérifiez que l’icône apparaît dans l’onglet du navigateur.

```
3.Faites en sorte que dans la navbar bootstrap, une image apparaisse aussi. Attention, vous
aurez à ajouter, dans le template menu.html, la ligne qui permet d’utiliser les fichiers
static.
```

# TP3 – Les premiers templates

## Introduction, Contexte et Objectifs

Pour le moment, nous pouvons aƯicher en console python les Villes, les Voyages et les Etapes.
Nous avons défini les modèles, nous les avons fait migrer pour créer les tables de données.

Il reste maintenant à créer des vues pour que ces listes des Villes et des Voyages puissent
apparaître sur le navigateur. Pour ces premières vues, l’objectif est juste de comprendre le
mécanisme qui agit pour les créer et les aƯicher.

## AƯichage de la liste des Voyages

Pour arriver à l’aƯichage des Voyages, il y a plusieurs étapes :

```
1.L’url dans le fichier urls.py
```
```
a. dans le fichier urls.py du PROJET, ajoutez la ligne d’import from applitravel
import views
Cette ligne permet de construire des urls qui iront chercher des fonctions présentes
dans applitravel/views.py
```
```
b. dans la liste urlpatterns, ajoutez le path suivant path('voyages/', views.voyages),
```

```
Ceci signifie que l’url http://127.0.0.1:8000/voyages/ dans le navigateur appellera la
fonction voyages du fichier views.py. C’est cette fonction contrôleur qui fera les
calculs adaptés et appellera le template adéquat aƯichant les voyages. Ce template
sera précisé dans la fonction voyages du fichier views.py.
```
2.La fonction voyages dans views.py (similaire à un contrôleur)

```
a. Dans le fichier de l’APPLICATION applitravel/views.py, réalisez l’import du modèle
Voyage :
```
```
b. dans le même fichier, on définit la fonction voyages, qui prend en charge un
paramètre request de type HttpRequest, non utilisé ici.
```
```
Ce paramètre request sera très utile plus tard, car il embarque de nombreux
renseignements, comme par exemple l’utilisateur connecté, le tableau POST
(équivalent du $_POST de PHP), etc.
```
```
Cette fonction voyages récupère les données de la base sur les voyages, et appelle
le bon template (ici, un fichier applitravel/voyages .html, pas encore créé). Ceci est
typique d’une méthode de contrôleur à la PHP :
```
- récupérer ce qui vient de l’url ou d’un formulaire (POST ou GET),
- en fonction de la demande, récupérer les données de la base de données,
- grâce à ces données, créer des contenus (en PHP, des objets ou des tableaux,
    en python, des dictionnaires par exemple),
- appeler le bon template en lui fournissant ces contenus pour qu’il gère
    l’aƯichage attendu.


```
Voici le code simple de cette fonction :
```
3.Le fichier voyages.html (similaire à une vue)

```
a.créez dans le répertoire applitravel (l’application) un sous-répertoire templates, et
dans templates un sous-répertoire applitravel.
```
```
b.Créez, dans applitravel/templates/applitravel/, le fichier voyages.html et donnez-lui le
contenu proposé ci-dessous :
```

- on rencontre des « variables de gabarit », encadrées par des doubles accolades
    : ici, la variable voyages qu’on utilise avec sa longueur : {{ voyages|length }}.
- cette variable de gabarit est en correspondance avec la variable python
    lesVoyages du fichier views.py.
- on rencontre aussi des insertions de code python (un peu comme on insère du
    code PHP dans un fichier html par des balises <?php ... ?>) : ces insertions se
    font au moyen d’accolades et de %.
- ce n’est pas exactement la syntaxe python quand même : voir le « endfor » par
    exemple.

```
N’oubliez pas de mettre à jour le dépôt distant.
```
```
4.Appel de la vue
```
```
lancez le serveur : commande python manage.py runserver, puis appelez l’url
http://127.0.0.1:8000/voyages/
```
```
Vous devez voir aƯicher la page HTML. Le menu est à moitié opérationnel, car rien
n’a été fait pour la vue des villes. Il fonctionnera réellement après le travail à faire sur
les villes. Pour le moment, le clic sur « les villes » amènera un message « page not
found », puisque l’url des villes n’a pas été écrite.
```
## AƯichage de la liste des villes

Refaites le même travail que précédemment pour les villes (n’oubliez pas d’importer les
classes dans views.py) :

```
 L’url dans le fichier urls.py
 La fonction villes dans views.py (ne pas oublier l’import)
 Le fichier villes.html avec le rendu similaire à cet exemple (varie en fonction des
données dans votre base) :
```

Le détail des étapes n’interviendra que plus tard, dans la vue de détail d’un voyage. Donc on se
limite ici aux voyages et aux villes.

Le point à améliorer est clairement la généricité des fichiers template, puisque les deux fichiers

```
pizzas.html et ingredients.html ont la même structure. C’est ce que nous ferons plus tard avec
les gabarits django.
```
## Le css Bootstrap 5

Nous allons maintenant, pour terminer ce TP, intégrer Bootstrap 5 à notre projet. Cela peut se
faire très simplement en indiquant, dans le head de nos templates, les liens vers les fichiers
css et js de bootstrap.

Nous allons aussi changer le format html de notre menu, pour lui donner un format qui répond
au css de bootstrap.

Dans le head de vos deux fichiers template, intégrez le lien vers le css et le javascript de
bootstrap.

Voir le lien suivant pour intégrer dans la balise head les bons éléments :

https://getbootstrap.com/docs/5.0/getting-started/introduction/

N’oubliez pas qu’un lien css se place habituellement dans le head, alors qu’un script JS se

```
place juste avant la balise fermante </body>. En eƯet, pour que le script fonctionne
correctement, il faut que toutes les balises html soient chargées.
```
Ensuite, changez dans le fichier voyages.html le menu actuel

par


Faire la même chose dans le fichiers villes.html

Cette deuxième version utilise les classes css de bootstrap.

Vous allez constater le changement, y compris au niveau des polices de caractères, ainsi que

```
des styles des titres h2 par exemple. Cela nous montre un premier aperçu des possibilités de
Bootstrap. Par la suite, nous fouillerons plus en détail les possibilités de bootstrap.
```

```
IUT d’Orsay – 3ème année – Année 2025-2026 - UML
```
# TP2 – Les modèles

## Introduction, Contexte et Objectifs

```
Django permet de créer à la main les modèles (équivalent des classes). Ensuite, par le
mécanisme des migrations, les tables de données sont automatiquement ajoutées à la base
de données.
```
```
Nous avons donc besoin du schéma relationnel de l’application applitravel. Pour le moment
nous nous contenterons d’un MCD simple, avec deux entités VILLE et VOYAGE, et une
association ETAPE. Une ville peut entrer dans la composition de plusieurs voyage, et un voyage
est composée d’un certain nombre de villes visitées.
```
```
Plus tard, nous modifierons le modèle de Voyage pour lui donner un attribut supplémentaire
(une image). Ce sera un complément intéressant.
```
```
Dans une version plus évoluée nous pourrions avoir une table avec la liste des pays, mais dans
une première approche nous nous limitons à saisir le nom du pays dans la ville.
```
```
Nous avons donc le MCD suivant :
```
```
Et sa transcription en Schéma Relationnel
```

```
IUT d’Orsay – 3ème année – Année 2025-2026 - UML
```
## Les modèles avec Django

```
Une fois que le schéma relationnel est établi, nous allons confier à django le soin de créer les
tables de données, en lui indiquant seulement quelles classes nous souhaitons construire.
```
```
Ceci permet une cohérence forte qui pouvait être mise en défaut dans le système classique
PHP / MySQL pur, puisque la création de tables n’était pas automatisée à partir des classes
PHP construites.
```
```
Notre première étape est donc de construire les classes python, et ceci se fait dans le fichier
models.py du projet.
```
```
1.Ajout des modèles dans models.py
```
```
a. changez le fichier models.py du répertoire applitravel pour qu’il définisse la classe
Ville. Cette classe héritera de la classe Model de la bibliothèque models. On indique
les champs IDVille, NomVille et NomPays, et on définit la méthode __str__ ,
équivalent de toString() en java. Le code suivant est donné en modèle :
```
```
Vous pouvez avoir plus d’information sur la création de modèle sur :
https://docs.djangoproject.com/en/5.2/topics/db/models/
```

IUT d’Orsay – 3ème année – Année 2025-2026 - UML

```
b. Modifier la méthode __str__ pour quelle renvoie le nom de la ville avec entre
parenthèse le nom du pays
```
```
Ex : Athènes (Grèce)
```
```
c. Créez de même la classe Voyage (dans le même fichier, à la suite de la classe Ville).
Vous pourrez utiliser le type DecimalField pour le prix.
```
```
2.Migrez les modèles vers la base de données
```
```
a. Dans le répertoire webtravel(là où il y a le fichier qui gère les commandes,
manage.py), lancez la commande python manage.py makemigrations
qui prépare l’adaptation de la base de données en fonction des nouveaux modèles.
Cela produira un aƯichage comme ceci :
```
```
Cet aƯichage montre les deux modèles créés. Un fichier de migration nommé
0001_initial.py a aussi été écrit, dans lequel vous trouverez les instructions qui
permettront de créer la structure de données dans la base sqlite.
```
```
b. Ensuite, validez la migration par la commande python manage.py migrate
```
```
c. Constatez l’eƯet sur la base de données en ouvrant sqlitebrowser. Pour le moment
vous ne voyez que la structure des tables Ville et Voyage.
```

IUT d’Orsay – 3ème année – Année 2025-2026 - UML

```
Pour le moment, il n’y a pas encore de données, mais vous pouvez accéder à la vue
des données dans l’onglet parcourir les données.
```
```
3.Enregistrer, consulter des données
```
```
a. Vous pouvez enregistrer ou consulter des données par l’interface, c’est le plus simple,
grâce au bouton d’insertion d’un nouvel enregistrement.
```
```
N’oubliez pas d’enregistrer les modifications de la table (si vous ne le faites pas, le
navigateur vous demandera de sauvegarder en quittant).
```
```
Enregistrez 3 nouvelles villes : Los Angeles (Etats-Unis), San Francisco (Etats-Unis)
et Las Vegas (Etats-Unis)
```

IUT d’Orsay – 3ème année – Année 2025-2026 - UML

```
b. Vous pouvez aussi ajouter des enregistrements en ligne de commande grâce au shell
python :
```
- python manage.py shell pour entrer dans le shell python
    (CTRL + Z pour quitter)
- from applitravel.models import Ville
- NY = Ville()
- NY.NomVille = 'New-York'
- NY.NomPays = 'Etats Unis'
- NY.save()

```
Ouvrez de nouveau sqlitebrowser pour constater qu’il y a bien une nouvelle entrée,
puis quittez sqlitebrowser :
```
```
c. Vous pouvez consulter les données dans la console python (accessible par la
commande python manage.py shell).
```
```
Ci-dessous, on a récupéré toutes les villes, puis parcouru la liste correspondante et
appelé la méthode print sur chaque ville (ceci a implicitement appelé la méthode
__str__ redéfinie précédemment).
```

IUT d’Orsay – 3ème année – Année 2025-2026 - UML

```
Vous pouvez donc agir sur les données ou les consulter par le shell python ou par
l’interface.
```
```
Remarques : en console vous devez comme dans l’éditeur de texte inclure des
tabulations (boucle for) sinon l’instruction python n’est pas comprise. En python, les
blocs sont délimités par la hiérarchie des indentations. La fonction python len
renvoie la longueur de l’ensemble passé en paramètre : ici, 4 villes en tout. N’oubliez
pas de mettre votre dépôt distant à jour.
```
4. Un modèle avec clés étrangères

```
La classe Etape aura donc une clé primaire IDEtape, et une contrainte d’unicité sur le
couple (IDVoyage, IDVille).
```
```
Voici le code correspondant. Vous noterez que la contrainte d’unicité est gérée dans une
classe interne « Meta » qui gère tout ce qui est hors déclaration de champs.
```

IUT d’Orsay – 3ème année – Année 2025-2026 - UML

```
a. créez la classe dans models.py
```
```
b. mettez en place la migration.
```
```
c. enregistrez des données via sqlitebrowser, pour avoir un jeu de données intéressant
(vous devrez actualiser la base pour voir la nouvelle table composition) :
 Avec au moins 10 Villes
 3 Voyages d’au moins 3 étapes chacun
```
```
N’oubliez pas d’enregistrer les modifications de la base, et n’oubliez pas de mettre à
jour le dépôt distant.
```
```
d. Entraînez-vous aussi à consulter les tables dans le shell python pour vous habituer à
la manœuvre.
```

# TP1 – Commencer un projet Django

## Introduction et Contexte

```
Pour cette suite de TP, nous utiliserons des outils importants :
```
- un environnement Windows
- un outil de versionnage (git, et le serveur gitlab de l’IUT)
- un framework de programmation web serveur python : Django, installé en local
- Un framework css : Bootstrap 5
- Un framework JS : Chart.js pour des graphiques évolués
- Un IDE comme Visual Studio Code

```
Le framework Django nous permettra de concevoir petit à petit un travail classique pour voir
comment gérer de A à Z, sans tout réinventer, un projet web avec des données persistantes.
```
```
Le framework css Bootstrap 5 nous permettra de bénéficier d’un travail conséquent et abouti,
en css et même en JavaScript. Nous pourrions utiliser du css pur, mais la logique de ce module
est de nous orienter vers ces outils.
```
```
Le framework JS chart.js nous permettra d’inclure des graphiques oƯrant des fonctionalités
statistiques utiles à l’administrateur.
```
```
Le serveur gitlab de l’IUT nous habituera, si ce n’est pas déjà le cas, à des pratiques nécessaires
au travail collaboratif. Même si, en l’occurrence, vous ne collaborerez qu’avec vous-même,
puisque les TP sont à faire individuellement.
```
```
Avec l’IDE Visual Studio Code, nous aurons accès à un éditeur de texte évolué et qui intègrera
également un terminal, dont vous pourrez vous servir à la place du terminal classique.
```
## Le gitLab de l’iut

```
Nous pouvons utiliser le gitlab de l’IUT (ou toute autre plateforme de dépôts git) pour disposer
d’un dépôt de fichiers distant. C’est une habitude essentielle en travail d’équipe. Même quand
l’équipe est réduite à une personne.
```
```
1.Connexion au gitlab de l’iut
a. allez à https://git.iut-orsay.fr/users/sign_in
b. connectez-vous avec login court et password
```

2.Création d’un nouveau projet et clonage

```
a. allez dans vos projets et créez un nouveau projet vierge nommé webtravel. Vous
pouvez le créer en privé. Laissez cochée l’option de création du README.md, c’est
un fichier d’accueil de la page gitlab de votre projet, vous pourrez la personnaliser
plus tard.
b. allez dans le projet et récupérez l’url du clonage en https qui doit être du type
https://git.iut-orsay.fr/prenom.nom/webtravel.git
```
```
c. Dans votre architecture locale, créez un nouveau dossier (par exemple R5A05) puis
allez dans ce dossier.
d. Lancez le clonage à cet endroit par la commande git clone <lien du
projet git>
```
```
e. Vérifiez qu’il y a maintenant dans R5A05 un répertoire webtravel, avec à l’intérieur un
le fichier README.md créé par Git
```
3.Rappel de quelques commandes essentielles git

```
a. où en êtes-vous?
La commande « git status » vous indique si votre copie locale est en retard (ou en
avance) sur la copie distante.
```
```
b. ajouter des fichiers à suivre
La commande « git add. » ajoute tous les fichiers pas encore suivis dans la liste des
fichiers à suivre. Tout changement sur ces fichiers sera indiqué.
```
```
c. valider les changements sur les fichiers suivis
La commande « git commit -m "message pour ce commit" » permet de valider les
changements et indique un message de repérage.
```
```
d. pousser les changements validés sur la branche distante
La commande « git push » met à jour la branche distante.
```
```
e. la commande de récupération de la branche distante La commande « git pull » est
très importante. Si vous n’êtes pas seul à travailler sur le même projet, il y a de
grandes chances que des push aient été eƯectués par d’autres et si vous vous
apprêtez à faire un push sans avoir mis à jour votre version locale avant, il va y avoir
des conflits de version qu’il vaut mieux éviter.
```
4.Chronologie classique

```
a.git pull
```

```
b.... vos changements de code
c.git status
d.git add.
e.git commit -m "mon message personnalisé"
f.git push
g.git status par acquis de conscience
```
```
Il vaut mieux faire trop de pull/push que pas assez.
```
## L’outil Django pour le projet webtravel

```
1.Installation de Django
```
```
a. Ouvrez une fenêtre de commande en ligne puis allez dans le répertoire du projet
webtravel et lancez la commande python –version pour connaitre la version de
pyhton installée. Celle-ci doit être supérieure à 3.
```
```
b. Nous allons maintenant installer PIP (le gestionnaire de paquets oƯiciel de Python).
Pour cela lancez la commande python -m pip install --upgrade pip
```
```
c. Nous pouvons créer un environnement virtuel nommé « env » pour Django avec la
commande python -m venv env
```
```
d. Activer l’environnement virtuel par la commande env\Scripts\activate
L’activation se voit par (env). L’environnement doit être activé pour faire tourner le
serveur web. Si une désactivation se produit, reprendre la procédure d’activation du d.
```
```
e. Installation de Django dans l’environnement virtuel
```
```
Dans webtravel, en n’oubliant pas d’activer l’environnement virtuel, nous allons
installer le framework django pour notre projet.
```
```
commande d’installation de django : pip install django
```
```
f. Ouvrez votre IDE VS Code, avec comme répertoire de travail webtravel :
```
```
e. Le fichier .gitignore
```
```
Ce fichier indiquera les répertoires ou fichiers qui doivent être ignorés lors des
procédures git. Créez, au niveau de la racine (au même niveau que README.md et
env), un fichier .gitignore (ce sera un fichier caché) qui contiendra la ligne suivante
:
1 /env
```

```
Ce fichier sera certainement mis à jour par la suite.
Mettez à jour votre dépôt distant pour ajouter ce fichier .gitignore. Rappel :
```
- git status
- git add.
- git commit -m "ajout du fichier .gitignore"
- git push

## Création du projet webtravel

```
1.La commande django-admin startproject webtravel
```
```
a. Nous allons créer un projet portant le même nom que le dossier la contenant
webtravel. Ce nom aurait pu être diƯérent.
```
```
b. Cette commande a en fait créé de nombreux fichiers que nous réutiliserons, et qui
structurent la base de notre projet.
```
```
2.La base de données du projet webtravel
Une base sqlite par défaut est utilisée par Django. On peut configurer sans problème
une base de données MySQL, mais à l’IUT les sécurités sont fortes pour pouvoir agir
sur les bases MySQL autrement que via PHP qui a reçu les droits nécessaires.
Nous allons donc, en travaillant totalement en local, utiliser une base de données
sqlite, avec comme interface graphique sqlitebrowser.
```
```
a. La commande python manage.py migrate
```
```
Nous allons utiliser la commande python3 manage.py migrate qui va mettre en
place la base de données du projet. Elle s’exécute dans le répertoire webtravel
(celui du projet), où on trouve aussi le fichier manage.py qui permet de lancer les
commandes en ligne python.
```
```
Cette commande ne sert pas qu’à la mise en place, mais de manière générale à
permettre les « migrations », qui ne sont que les traductions de nos modèles vers des
tables de données. Exécutez cette commande.
```
```
Vous constatez que maintenant dans votre projet il y a un fichier db.sqlite3, c’est
notre base de données. Pour le moment nous n’y avons pas créé de tables.
```

```
Vous pouvez ajouter ce fichier db.sqlite3 à .gitignore, car il n’est pas utile de le suivre
dans le dépôt distant.
Mettez le dépôt à jour (vos commandes git doivent s’eƯectuer dans webtravel, pas
dans webtravel/webtravel).
```
3.L’outil sqlitebrowser

```
Cet outil est une interface permettant de consulter/modifier la base de données du
projet. Il nous servira probablement pour insérer des jeux de données.
```
```
Vérifiez que vous arrivez à ouvrir la base de données du projet avec sqlitebrowser.
Vérifiez que dans la liste de tables, il n’y a encore rien concernant le projet, et que
pour le moment il n’y a que des tables structurelles, ce qui est normal car nous
n’avons pas encore conçu de tables ni enregistré de données.
```

## Création d’une application dans le projet

```
Par souci de modularité, un projet peut contenir plusieurs « applications ».
```
```
Notre première application dans ce projet sera appelée applitravel. C’est dans cette
application que l’utilisateur gèrera les voyages.
```
```
Le nom webtravel est interdit car c’est le nom du projet contenant l’application.
```
```
Il pourrait y avoir d’autres applications dans le même projet, et une application d’un projet peut
être utilisée dans d’autres projets.
```
```
Par exemple, une autre application gèrera les connexions au site.
Nous la coderons plus tard.
```
```
1.Création de l’application
```
```
a. Lancez, dans l’environnement virtuel du projet webpizza, la commande python
manage.py startapp applitravel
```
```
b. On constate immédiatement l’eƯet produit par la création de l’application au niveau
de l’architecture du projet. Dans webtravel (où on retrouve les fichiers essentiels au
projet webtravel, comme settings.py), il y a maintenant un répertoire applitravel.
```
```
b. Déclaration de l’application dans les paramètres du projet
```
```
Dans le fichiers settings.py, il y a la liste python appelée INSTALLED_APS. Il faut
ajouter, en fin de la liste, l’application nouvellement créée : applitravel
```

```
d. N’oubliez pas de mettre à jour votre dépôt distant, et vérifiez sur la page web du gitlab
que le dépôt distant est bien à jour.
```
## Lancement du serveur web

```
Nous allons maintenant observer le site créé
```
```
a. Lancez la commande python manage.py runserver
```
```
2.Dans le navigateur, aller à l’url http://127.0.0.1:8000/ pour voir le site actuel
```
```
Pour le moment c’est très pauvre et anonyme, mais si vous obtenez ceci, c’est bon signe
pour la suite.
```


