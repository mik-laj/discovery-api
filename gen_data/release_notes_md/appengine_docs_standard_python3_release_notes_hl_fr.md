#  Notes de version Python 3

Python [ 2.7
](https://cloud.google.com/appengine/docs/standard/python/release-notes?hl=fr
"Afficher cette page dans l'environnement d'exécution Python 2.7") /  3.7  |
Java [ 8 ](https://cloud.google.com/appengine/docs/standard/java/release-
notes?hl=fr "Afficher cette page dans l'environnement d'exécution Java 8") / [
11 ](https://cloud.google.com/appengine/docs/standard/java11/

release-notes?hl=fr "Afficher cette page dans l'environnement d'exécution
Java 11") |  PHP [ 5
](https://cloud.google.com/appengine/docs/standard/php/release-notes?hl=fr
"Afficher cette page dans l'environnement d'exécution PHP 5") / [ 7
](https://cloud.google.com/appengine/docs/standard/php7/

release-notes?hl=fr "Afficher cette page dans l'environnement d'exécution
PHP 7") |  [ Ruby ](https://cloud.google.com/appengine/docs/standard/ruby/

release-notes?hl=fr "Afficher cette page dans l'environnement d'exécution
Ruby") |  Go [ 1.9
](https://cloud.google.com/appengine/docs/standard/go/release-notes?hl=fr
"Afficher cette page dans l'environnement d'exécution Go 1.9") / [ 1.11
](https://cloud.google.com/appengine/docs/standard/go111/

release-notes?hl=fr "Afficher cette page dans l'environnement d'exécution
Go 1.11") / [ 1.12 ](https://cloud.google.com/appengine/docs/standard/go112/

release-notes?hl=fr "Afficher cette page dans l'environnement d'exécution
Go 1.12") |  [ Node.js
](https://cloud.google.com/appengine/docs/standard/nodejs/

release-notes?hl=fr "Afficher cette page dans l'environnement d'exécution
Node.js")

En plus des notes de version ci-dessous, vous pouvez également suivre les
problèmes connus dans l' [ outil de suivi des problèmes
](https://issuetracker.google.com/issues?q=componentid%3A187191%2B&hl=fr) .

Pour recevoir les dernières mises à jour de ce produit, ajoutez l'URL de cette
page à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  30 juillet 2019

  * Les outils AppCfg et l'ancien SDK App Engine autonome fournis via les fichiers ` GoogleAppEngineLauncher.dmg ` , ` GoogleAppEngine.msi ` et ` google_appengine.zip ` sont désormais obsolètes. Google interrompra et supprimera la compatibilité avec ces derniers le 30 juillet 2020. 
  * Les fonctionnalités du SDK App Engine sont exclusivement fournies via le [ SDK Cloud ](https://cloud.google.com/sdk/docs?hl=fr) . Pour en savoir plus, consultez la page [ Migrer vers le SDK Cloud ](https://cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration?hl=fr) . 

##  18 avril 2019

  * App Engine est désormais disponible dans la région ` asia-northeast2 ` (Osaka, Japon). 

##  15 avril 2019

  * App Engine est désormais disponible dans la région ` europe-west6 ` (Zurich, Suisse). 

##  9 avril 2019

  * [ Cloud Tasks ](https://cloud.google.com/tasks/docs?hl=fr) est désormais accessible à tous et peut être utilisé pour configurer des tâches à exécuter de manière asynchrone, en dehors des requêtes utilisateur. 

  * L' [ accès au VPC sans serveur ](https://cloud.google.com/appengine/docs/standard/python3/connecting-vpc?hl=fr) est désormais disponible en version bêta. Il permet à votre application de se connecter aux ressources internes de votre réseau VPC, telles que des instances de VM Compute Engine, des instances Cloud Memorystore, etc. 

##  4 avril 2019

  * L'environnement d'exécution Python 3 a été mis à jour à la version 3.7.3. 

##  11 janvier 2019

  * L'environnement d'exécution Python 3 a été mis à jour à la version 3.7.2. 

##  14 décembre 2018

  * L' [ environnement d'exécution Python 3.7 ](https://cloud.google.com/appengine/docs/standard/python3?hl=fr) pour l'environnement standard App Engine est désormais accessible à tous. 

##  12 décembre 2018

  * Le SDK Python a été mis à jour à la version 1.9.81. 
  * Toutes les applications utilisent désormais des sockets réseau BSD. Aucune modification n'est requise. 
  * L' [ API Sockets ](https://cloud.google.com/appengine/docs/standard/python/sockets?hl=fr) est désormais accessible à tous. 

##  16 novembre 2018

  * nginx est désormais le serveur Web par défaut. Aucune modification n'est requise. 

##  31 octobre 2018

  * L'environnement d'exécution Python 3 a été mis à jour à la version 3.7.1. 
  * L'environnement d'exécution Python 3 accepte les entrées récursives dans le fichier ` requirements.txt ` . 

##  22 octobre 2018

  * App Engine est désormais disponible dans la région ` asia-east2 ` (Hong Kong). 

##  8 août 2018

  * L' [ environnement d'exécution Python 3.7 ](https://cloud.google.com/appengine/docs/standard/python3?hl=fr) pour l'environnement standard App Engine est désormais disponible en version bêta. 
  * Vous pouvez consulter la liste des [ différences entre les environnements d'exécution Python 2.7 et Python 3.7 ](https://cloud.google.com/appengine/docs/standard/python3/python-differences?hl=fr) . 

##  10 juillet 2018

  * App Engine est désormais disponible dans la région ` us-west2 ` (Los Angeles). 

##  2 juillet 2018

Correction d'un bug dans la [ configuration d'autoscaling
](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=fr#scaling_elements)
à cause duquel App Engine arrêtait les instances de manière agressive quand le
paramètre ` max_instances ` était utilisé.

##  15 mai 2018

  * Fin du déploiement progressif d'une mise à niveau du système d'autoscaling : 
    * L'efficacité a été améliorée, ce qui entraîne généralement un coût d'instance inférieur (jusqu'à 6 % de réduction pour de nombreux utilisateurs) et jusqu'à 30 % de réduction pour les _requêtes de chargement_ , qui sont les premières requêtes adressées à une nouvelle instance. 
    * Le nouveau paramètre concernant le nombre maximal d'instances vous permet de limiter le nombre total d'instances à planifier. 
    * Le nouveau paramètre concernant le nombre minimal d'instances vous permet de spécifier le nombre minimal d'instances devant rester actives pour votre application. 
    * Le nouveau paramètre concernant l'utilisation du processeur cible vous permet d'optimiser la latence par rapport au coût. 
    * Le nouveau paramètre concernant l'utilisation du débit cible vous permet d'optimiser le nombre de requêtes simultanées à partir duquel de nouvelles instances sont démarrées. 
    * L'autoscaling n'utilise plus d'instances résidentes. Auparavant, si vous utilisiez le paramètre ` min_idle_instances ` , les instances inactives étaient considérées comme _résidentes_ dans Cloud Console, tandis que les autres étaient considérées comme _dynamiques_ . Le nouveau programmeur marque simplement toutes les instances comme étant _dynamiques_ avec autoscaling. Toutefois, le comportement sous-jacent reste semblable au comportement précédent. Si vous utilisez ` min_idle_instances ` et activez les requêtes de préchauffage, vous constaterez qu'au moins autant d'instances dynamiques sont en cours d'exécution, même pendant les périodes sans trafic. 
    * Pour en savoir plus, consultez la [ documentation sur l'autoscaling ](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=fr#scaling_elements) . 

##  14 décembre 2017

  * La documentation sur le contrôle d'accès concernant le déploiement d'applications avec des rôles et des comptes de service IAM a été améliorée : 

    * [ Rôles App Engine prédéfinis ](https://cloud.google.com/appengine/docs/standard/python3/access-control?hl=fr#predefined_app_engine_roles)
    * [ Déployer à l'aide de rôles IAM ](https://cloud.google.com/appengine/docs/standard/python3/granting-project-access?hl=fr#deploying_using_iam_roles)
    * [ Autorisations requises ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=fr#required_permissions)

##  31 octobre 2017

  * App Engine est désormais disponible dans la région ` asia-south1 ` (Mumbai, Inde). 

##  11 octobre 2017

  * La disponibilité générale du [ pare-feu App Engine ](https://cloud.google.com/appengine/docs/standard/python3/creating-firewalls?hl=fr) a été annoncée. 

##  13 septembre 2017

  * Vous pouvez désormais utiliser des certificats gérés pour ajouter SSL à votre domaine personnalisé. Une fois que vous avez mappé le domaine personnalisé à votre application, App Engine provisionne automatiquement un certificat SSL, procède à son renouvellement avant son expiration, et le révoque si vous supprimez le domaine personnalisé. Les certificats gérés sont disponibles en version bêta. Pour en savoir plus, consultez la page [ Sécuriser les domaines personnalisés avec SSL ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=fr) . 

  * Si vous disposez déjà d'un mappage de domaine et d'un certificat SSL, ce dernier continue de fonctionner comme prévu. Vous pouvez également [ passer à des certificats SSL gérés ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=fr#updating_to_managed_ssl_certificates) . 

  * Les commandes ` gcloud ` et les méthodes de l'API Admin permettant de [ mapper des domaines personnalisés ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=fr) sont désormais accessibles à tous. Cela inclut [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains?hl=fr) et [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=fr) . Toutefois, si vous souhaitez employer des certificats SSL gérés, utilisez les commandes et méthodes bêta spécifiées sur la page [ Sécuriser les domaines personnalisés avec SSL ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=fr) . 

##  5 septembre 2017

  * App Engine est désormais disponible dans la région ` southamerica-east1 ` (São Paulo, Brésil). 

##  1er août 2017

  * App Engine est désormais disponible dans la région ` europe-west3 ` (Francfort, Allemagne). 

##  18 juillet 2017

  * App Engine est désormais disponible dans la région ` australia-southeast1 ` (Sydney, Australie). 

##  6 juin 2017

  * App Engine est désormais disponible dans la région ` europe-west2 ` (Londres). 
  * Vous pouvez désormais utiliser les fonctionnalités de niveau bêta de l'API Admin et de l'outil de ligne de commande ` gcloud ` pour [ créer et gérer vos domaines personnalisés et vos certificats SSL ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=fr) . 

##  9 mai 2017

  * App Engine est désormais disponible dans la région ` us-east4 ` (Virginie du Nord). 

##  27 octobre 2016

  * Les services Channel et XMPP sont désormais [ obsolètes ](https://cloud.google.com/appengine/docs/deprecations?hl=fr) . Ils seront abandonnés le 31 octobre 2017. 

##  1er août 2016

**Notes concernant l'API Admin**

  * La version 1 de l' [ API Admin ](https://cloud.google.com/appengine/docs/admin-api?hl=fr) est désormais accessible à tous. 

##  1er août 2016 – Version 1.9.42

**Notes concernant l'environnement d'exécution Python 3.7**

  * Cette version n'inclut pas un nouveau SDK Python 3.7. Les utilisateurs de l'environnement Python 3.7 doivent continuer à utiliser le SDK 1.9.40. 

##  18 juillet 2016 – Version 1.9.40

  * La version 1.9.39 a été ignorée. 

  * Les requêtes LeaseTasksByTag seront limitées à 25 requêtes par seconde. 

  * Les erreurs liées au serveur et au client reflètent désormais plus précisément les erreurs d'état par URL dans le tableau de bord d'App Engine. 

  * Un nouveau [ tutoriel App Engine ](https://console.cloud.google.com/start/appengine?hl=fr) est disponible dans la console GCP. Choisissez votre langue de préférence et lancez un tutoriel interactif directement dans la console. 

  * La limite maximale de tâches Cron est passée à 250. 

##  1er juillet 2016

**Cloud Datastore**

  * La nouvelle [ tarification Cloud Datastore ](https://cloud.google.com/appengine/pricing?hl=fr#costs-for-datastore-calls) est désormais en vigueur. 

##  25 mai 2016 – Version 1.9.38

  * L'erreur renvoyée par le service de récupération d'URL pour une requête adressée à un port situé en dehors des plages autorisées (80–90, 440–450, 1024–65535) renverra désormais toujours ` INVALID_URL ` , comme indiqué dans la documentation. 

**Cloud Datastore**

  * Lors du commit d'une transaction entre groupes, les numéros de version renvoyés pour les entités nouvelles ou mises à jour sont identiques. Auparavant, les entités du même groupe validées dans le cadre d'une seule transaction entre groupes possédaient le même numéro de version, mais les entités de groupes différents pouvaient avoir des numéros de version distincts. Cette modification garantit que toutes les entités nouvelles et mises à jour ont un numéro de version identique lorsqu'elles sont validées dans le cadre d'une transaction entre groupes, quel que soit leur groupe d'entités. Comme avec le comportement précédent, les entités qui ne sont pas mises à jour ne disposeront pas d'un nouveau numéro de version. 

##  4 mai 2016 – Version 1.9.37

Des améliorations et des corrections de bugs générales ont été apportées.

##  2 mai 2016

**Environnement flexible App Engine**

  * L' [ environnement d'exécution Ruby ](https://cloud.google.com/appengine/docs/flexible/ruby?hl=fr) est désormais disponible pour l'environnement flexible App Engine. 

##  18 avril 2016 – Version 1.9.36

En réponse à vos demandes, l'API Users d'App Engine rejoint le reste d'App
Engine et est désormais compatible avec les rôles IAM et l'extension de
groupes. Cela signifie que les utilisateurs détenant le rôle de propriétaire,
d'éditeur ou de lecteur de projet, ou encore le rôle d'administrateur App
Engine, sont considérés comme des "administrateurs" par l'API Users, que le
rôle leur ait été attribué directement ou parce qu'ils appartiennent à un
groupe. * Dans cette version, les détails des erreurs associées au type
d'exception "OverQuota" sont indiqués lorsqu'ils sont disponibles.

##  24 mars 2016 – Version 1.9.35

  * Les VM App Engine gérées ont été renommées [ environnement flexible App Engine ](https://cloud.google.com/appengine/docs/flexible?hl=fr) . 
  * Les horodatages de trace ont été corrigés de façon à correspondre aux horodatages de journal. 

##  4 mars 2016 – Version 1.9.34

  * Le quota par défaut lié à la récupération d'URL pour les applications facturées a été augmenté. Consultez la page [ Quotas ](https://cloud.google.com/appengine/docs/quotas?hl=fr#UrlFetch) pour en savoir plus. 

##  17 février 2016 – Version 1.9.33

  * Le chemin d'URL "/form" est désormais autorisé et sera transmis aux applications. Auparavant, ce chemin était bloqué. 

##  3 février 2016 – Version 1.9.32

  * Choix de création de conteneur pour les VM gérées 

Les commandes ` gcloud preview app deploy ` (et ` mvn gcloud:deploy ` )
importent vos artefacts dans nos serveurs et créent un conteneur pour déployer
votre application dans l'environnement de la VM gérée.

Deux mécanismes permettent de créer l'image de conteneur à distance. Le
comportement par défaut consiste à créer le conteneur sur une VM temporaire
Compute Engine sur laquelle Docker est installé. Vous pouvez également
utiliser le service [ Cloud Build ](https://cloud.google.com/cloud-
build/docs?hl=fr) . Pour cela, procédez comme suit :

    1. [ Activez l'API Cloud Build ](https://support.google.com/cloud/answer/6158841?hl=fr) pour votre projet. 
    2. Utilisez la commande ` gcloud config set app/use_cloud_build True ` . Ainsi, les appels de ` gcloud preview app deploy ` exploiteront le service. (Pour revenir au comportement par défaut, servez-vous de la commande ` gcloud config set app/use_cloud_build False ` .) 

##  14 février 2016 – Version 1.9.31

App Engine est désormais compatible avec les groupes Google. L'ajout d'un
groupe Google en tant que membre d'un projet permet aux membres du groupe
d'accéder à App Engine. Par exemple, si un groupe Google détient le rôle
d'éditeur sur un projet, tous les membres du groupe disposent désormais d'un
accès éditeur à l'application App Engine.

##  30 novembre 2015 – Version 1.9.30

Les en-têtes des requêtes de file d'attente d'envoi adressées à des tâches
Task Queue sans charge utile contiendront désormais une entrée Content-Length
définie sur "0". Auparavant, les en-têtes de ces requêtes ne contenaient
aucune entrée Content-Length.

##  30 novembre 2015 – Version 1.9.29

  * Le calcul et le stockage de la profondeur de file d'attente n'est plus effectué pour les files d'attente inexistantes, les files d'attente marquées pour suppression, ni en cas de panne des tables de files d'attente. 
  * Pour les développeurs utilisant l' [ API Endpoints ](https://cloud.google.com/appengine/docs/standard/python/endpoints/create_api?hl=fr#defining_the_api_endpointsapi) , un paramètre booléen détectable a été ajouté à l'annotation @Api pour permettre aux utilisateurs de désactiver la découverte d'API. L'utilisation de cette fonctionnalité empêchera certaines bibliothèques clientes (par exemple, JavaScript) et l'API Explorer de fonctionner, car elles dépendent de la découverte. 

##  29 octobre 2015 – Version 1.9.28

L'API Prospective Search, obsolète depuis le 14 juillet 2015, est désormais
limitée aux utilisateurs existants. Elle sera complètement abandonnée le 1er
décembre 2015. * La précision du filtrage géographique dans les requêtes de
recherche.a été améliorée.

##  25 septembre 2015 – Version 1.9.27

Le budget quotidien par défaut des applications nouvellement activées pour la
facturation est désormais illimité et n'est plus défini sur 0 $. Cela permet
d'éviter les interruptions indésirables causées par un dépassement de budget.
Pour définir un plafond quotidien pour votre application, activez la
facturation pour celle-ci, puis spécifiez un budget dans les [ paramètres
d'App Engine
](https://console.cloud.google.com/project/_/appengine/settings?hl=fr) . Pour
en savoir plus, consultez la page concernant la [ définition d'un budget
quotidien ](https://cloud.google.com/appengine/docs/developers-
console?hl=fr#setting_a_daily_budget) .

Datastore

  * Correction d'un bug : les attributs numériques répétés sont désormais autorisés. 
  * La recherche par attribut est désormais accessible à tous. 

##  27 août 2015 – Version 1.9.26

  * La bibliothèque oauth2client a été mise à niveau à la version [ 1.4.2 ](https://github.com/google/oauth2client/blob/master/CHANGELOG.md) . 
  * Ajout du menu "Afficher dans le contexte" pour les journaux d'application MVM ayant des valeurs thread_id ou request_id définies en tant que champ dans leur entrée de journal. Cela permet de trier les journaux d'application en fonction de l'un des champs. 
  * Vous pouvez désormais provisionner des applications pour la charge actuelle et configurer un provisionnement élastique en fonction des métriques au niveau de la VM et de l'application. 
  * Il est maintenant possible d'accéder aux API distantes à l'aide d'identifiants OAuth2, comme indiqué sur la page https://developers.google.com/identity/protocols/application-default-credentials. 
  * Vous pouvez utiliser RequestPayloadTooLargeException pour les requêtes de récupération d'URL avec des charges utiles trop volumineuses. 

##  14 août 2015 – Version 1.9.25

  * Ajout de PyAMF version 0.7.2 (bêta). 
  * Les menus de la console d'administration commencent à rediriger les utilisateurs vers la console GCP. Certains services, tels que les journaux d'administration, resteront disponibles dans la console d'administration. 
  * Datastore permet désormais aux propriétés de représenter la liste vide. 
  * Les tâches ayant échoué dans les files d'attente configurées avec un paramètre retry_limit défini sur zéro ne seront plus relancées. 

