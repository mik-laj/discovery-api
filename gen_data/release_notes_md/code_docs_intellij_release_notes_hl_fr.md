#  Notes de version

Cette page répertorie les mises à jour en production de Cloud Code. Consultez-
la pour obtenir des informations sur les fonctionnalités nouvelles ou mises à
jour, les corrections de bugs, les problèmes connus et les fonctionnalités
obsolètes.

Les dernières mises à jour sont également disponibles sur la page des [ notes
de version de GitHub ](https://github.com/GoogleCloudPlatform/cloud-code-
intellij/blob/master/CHANGELOG.md) .

Vous pouvez consulter les dernières mises à jour de produits pour l'ensemble
de Google Cloud sur la page [ Notes de version de Google Cloud
](https://cloud.google.com/release-notes?hl=fr) .

Pour recevoir les dernières mises à jour concernant ce produit, ajoutez l'URL
de cette page à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou ajoutez l'URL
du flux directement : ` https://cloud.google.com/feeds/cloud-code-for-
intellij-release-notes.xml `

##  18.5.1

Cloud Code est désormais disponible dans PyCharm (Community et Professional).
Parcourez vos buckets Cloud Storage et interagissez avec Cloud Source
Repositories depuis PyCharm. D'autres IDE seront disponibles prochainement.

###  Ajout

  * Plug-in refactorisé afin que les fonctionnalités agnostiques de langage (Cloud Storage, Cloud Source Repositories) soient disponibles dans d'autres IDE JetBrains en plus d'IDEA. [ 1896 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1896)

###  Modification

  * Le SDK Cloud géré ne sera plus installé sur chaque chargement IDE après la première annulation manuelle. [ 2113 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2113)

###  Correction

  * Correction de l'exception en 2018.2 EAP. [ 2124 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2124)

##  18.4.1

###  Ajout

  * Le plug-in Google Cloud Tools est autorisé à gérer le SDK Cloud, y compris le téléchargement, l'installation et les mises à jour. Vous n'avez plus besoin de télécharger manuellement le SDK. [ 673 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/673)
  * Diminution des conflits de version de dépendance grâce à la compatibilité intégrée avec le BOM Java de Google Cloud. Cela inclut l'ajout automatique du BOM lors de l'ajout de bibliothèques clientes Google, ainsi que des inspections pom.xml pour faciliter la gestion des conflits de version de dépendance. [ 1921 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1921)
  * Ajout automatique des variables d'environnement requises aux configurations d'exécution locales d'App Engine pour accéder localement aux API Google Cloud. [ 1917 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1917)

##  18.3.2

  * Correction d'un bug entraînant une erreur d'initialisation du plug-in sur IntelliJ IDEA 2017.2 et versions antérieures. [ 1972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1972)

##  18.3.1

###  Ajout

  * Possibilité de créer des comptes de service et de télécharger des clés de compte de service à partir du flux de travail de la bibliothèque cliente IDE. [ 1808 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1808)

###  Correction

  * Correction de situations où ` appengine-web.xml ` n'était pas généré en raison de l'absence de ` web.xml ` . [ 1903 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1903)

##  18.2.1

###  Ajout

  * Découverte et ajout depuis l'IDE de la bibliothèque cliente Google Cloud Java. [ 1806 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1806)
  * Possibilité d'activer les API Google Cloud à partir de l'IDE. [ 1807 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1807)

###  Modification

  * Mise à jour du sélecteur de projet Cloud avec une expérience utilisateur grandement améliorée. [ 1719 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1719)
  * Mise à jour du sélecteur de projet Cloud afin que la dernière sélection soit mémorisée et utilisée par défaut. [ 1812 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1812)

###  Correction

  * Intégration des artefacts d'exécution locale standard App Engine manquants. [ 1625 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1625)

##  18.1.1

###  Correction

  * Correction du mécanisme de rapport d'erreur non fonctionnel. [ 1842 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1842)

##  17.12.2

###  Correction

  * Correction de la configuration des propriétés Analytics non fonctionnelle entraînant la perte de données d'analyses. [ 1773 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1773)

##  17.12.1

Le plug-in de compte Google a maintenant été fusionné avec le plug-in Cloud
Tools et ne constitue plus une installation distincte. Si vous aviez déjà
installé le plug-in Account Tools, suivez la nouvelle invite de la boîte de
dialogue pour le supprimer et redémarrez l'IDE afin d'éviter tout problème.

###  Correction

  * Correction d'une erreur de mémoire lors de la saisie et de la recherche de plusieurs projets dans le sélecteur de projets Cloud. [ 1742 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1742)

###  Modification

  * Le plug-in de compte Google est désormais intégré dans le plug-in Google Cloud Tools. Une installation distincte du plug-in de compte Google n'est plus nécessaire. [ 1735 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1735)

##  17.11.1

###  Ajout

  * Intégration de Cloud Storage dans IntelliJ. Vous pouvez désormais parcourir vos buckets et afficher leur contenu sans quitter l'IDE. [ 1696 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1696)
  * Fonctions de recherche et de filtrage dans le sélecteur de projet Cloud. [ 1660 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1660)
  * Nouveau raccourci permettant d'ajouter la compatibilité avec App Engine depuis le menu d'outils d'un projet. Vous disposez ainsi d'un autre moyen pour ajouter la compatibilité avec App Engine dans un projet. [ 1685 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1685)

###  Correction

  * Correction du message d'état de l'indicateur de région App Engine affiché lorsqu'aucun projet Cloud n'a été sélectionné. [ 1607 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1607)

##  17.9.2

Java 8 dans l'environnement standard App Engine est désormais en phase de [
disponibilité générale
](https://cloudplatform.googleblog.com/2017/09/Java-8-on-App-Engine-Standard-
environment-is-now-generally-available.html) .

###  Modification

  * Mise à jour du nouvel assistant de projet dans l'environnement standard App Engine pour générer des applications Java 8 par défaut. [ 1641 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1641)

##  17.9.1

###  Ajout

  * Possibilité de modifier le nom de l'artefact de préproduction pour les déploiements dans l'environnement flexible App Engine. [ 1610 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1610)

###  Modification

  * Par défaut, les configurations de déploiement flexibles App Engine déploient l'artefact tel quel, sans renommer ` target.jar ` ni ` target.war ` . [ 1151 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1151)
  * Mise à jour du nom de l'artefact d'espace réservé dans les modèles Dockerfile générés pour indiquer qu'il doit être mis à jour par l'utilisateur. [ 1648 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1648)
  * Les configurations de déploiement dans l'environnement standard App Engine sont désormais configurées par défaut pour mettre à jour les fichiers dos, dispatch, Cron, les files d'attente et les index du datastore. [ 1613 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1613)
  * Les projets natifs qui ajoutent la compatibilité Endpoints Frameworks pour App Engine utilisent désormais Endpoints V2. [ 1612 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1612)

###  Correction

  * Correction de l'erreur ` Deployment source not found ` lors du déploiement d'artefacts Maven. [ 1220 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1220)
  * Correction de la taille de l'icône d'utilisateur sur les écrans HiDPI. [ 1633 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1633)
  * Résolution du problème de retour à une version antérieure du plug-in sur IDEA 2017.3. EAP. [ 1631 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1631)

##  17.8.2

###  Correction

  * Correction de l'erreur "Erreur: invalid_scope" obtenue lors de la connexion à votre compte Google. [ 1598 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1598)

##  17.8.1

###  Ajout

  * Création d'un lien pour ajouter des commentaires et signaler des problèmes dans le menu contextuel Google Cloud Tools. [ 1560 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1560)

###  Modification

  * Les utilisateurs peuvent désormais enregistrer les configurations d'exécution de déploiement partiellement terminées ou en état d'erreur. [ 1407 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1407)

###  Correction

  * Résolution du conflit de langage enregistré dans Docker, causant des problèmes lors de l’exécution du plug-in avec .ignore plugin. [ 1535 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1535)
  * Résolution des exceptions NPE lors de l'analyse de l'horodatage des points d'arrêt Cloud Debugger. [ 1537 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1537)
  * Suppression du fichier EAR en tant que type d'artefact App Engine accepté pour les exécutions de serveur de développement en local. [ 1190 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1190)
  * Les déploiements sont désormais affichés dans plusieurs fenêtres IDE. [ 1432 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1432)
  * Résolution du plantage causé par une tentative de modification d'une collection en lecture seule. [ 1571 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1571)

##  17.6.2

###  Correction

  * Correction des exceptions NPE survenant en présence d'une configuration de serveur de développement locale, mais sans attribut standard. [ 1525 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1525)

##  17.6.1

###  Ajout

  * Attribut flexible App Engine avec configuration ` app.yaml ` et Dockerfile. [ 1514 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1514)
  * Détection de la compatibilité avec le framework d'environnement flexible App Engine. [ 1277 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1277)

###  Modification

  * Utilisateur autorisé à spécifier un répertoire Docker au lieu d'un fichier Docker simple pour les déploiements en environnement flexible. [ 1304 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1304)
  * Nouvelle expérience utilisateur de la boîte de dialogue de déploiement (environnement standard et flexible). [ 1477 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1477)

###  Correction

  * Correction de la taille de l'avatar Google pour les écrans HiDPI. [ 1391 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1391)

##  17.2.5_2017

###  Ajout

  * Les variables d'environnement de la configuration d'exécution locale en environnement standard App Engine sont maintenant transmises au serveur de développement. [ #1364 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1364)
  * Les variables d'environnement configurées dans appengine-web.xml sont maintenant reconnues et transmises au serveur de développement. [ #377 ](https://github.com/GoogleCloudPlatform/appengine-plugins-core/issues/377)

##  17.2.4_2017

###  Ajout

  * Case à cocher permettant de déployer tous les fichiers de configuration App Engine lors du déploiement du service. [ #1346 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1346)

##  17.2.3_2017

###  Modification

  * Suppression de l'indicateur Clear Datastore de la configuration du serveur de développement local dans l'environnement standard App Engine, car la version actuelle du serveur ne le prend pas en charge. ( [ #1345 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1345) ) 

##  17.2.2_2017

###  Correction

  * Environnement d'exécution Java (JRE) non valide lors de la préproduction d'une application en environnement standard App Engine ( [ #1316 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1316) ) : 
    
        > Unable to stage app: Cannot get the System Java Compiler. Please use a JDK, not a JRE.
    

##  17.2.1

Bonne année aux utilisateurs de Cloud Code ! La première version de l'année
est principalement une version de maintenance. Si vous rencontrez des
problèmes d'authentification avec Cloud Source Repositories et notre plug-in,
essayez [ cette solution ](https://github.com/GoogleCloudPlatform/google-
cloud-intellij/issues/1174) .

Voici une liste des changements visibles :

###  Ajout

  * Prise en charge de plusieurs dépôts Cloud Source Repositories pour un seul projet GCP. ( [ #1024 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1024) ) 
  * Initialisation App Engine et sélection de la région. ( [ #1232 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1232) ) 

###  Correction

  * L'arrêt de dev_appserver sous Windows échoue toujours avec ` com.intellij.execution.ExecutionException ` . ( [ #1215 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1215) ) 
  * Le nouvel assistant de projet pour l'environnement standard App Engine doit générer le fichier web.xml avec le servlet 2.5. ( [ #1194 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1194) ) 
  * La case à cocher Clear Datastore pour l'environnement standard App Engine ne fonctionne pas. ( [ #1188 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1188) ) 
  * N'affiche pas les projets dont la suppression est prévue dans le sélecteur de projet. ( [ #1119 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1119) ) 

Pour en savoir plus, rendez-vous sur la page [ Jalon de version 17.2
](https://github.com/GoogleCloudPlatform/google-cloud-
intellij/milestone/19?closed=1) .

##  16.11.6

###  Ajout

  * Extension du menu Google Cloud Tools avec divers raccourcis d'actions. ( [ #1061 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1061) ) 
  * Vérifie la version minimale compatible du SDK Cloud. ( [ #1051 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1051) ) 
  * Crée automatiquement toutes les configurations d'exécution pertinentes pour les applications de l'environnement standard App Engine. ( [ #1063 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1063) ) 
  * Le framework App Engine est désormais un enfant du framework Web dans le nouvel assistant de projet. ( [ #1065 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1065) ) 

###  Correction

  * Les sources de déploiement uniques dans le panneau de déploiement du serveur d'applications apparaissent désormais comme des éléments de ligne distincts. ( [ #821 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/821) ) 
  * Validation des chemins d'accès SDK Cloud non valides sous Windows. ( [ #1091 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1091) ) 

##  16.10.5

IMPORTANT : Ce plug-in nécessite l'utilisation du SDK Cloud v 133.0.0 pour une
exécution correcte du serveur de développement local avec le dernier SDK Java
8. Veuillez exécuter ` gcloud components update ` depuis votre shell pour vous
assurer que vous disposez de la dernière version du SDK Cloud.

###  Correction

  * Résolution du problème lié au mode de débogage du serveur de développement local lorsque des modifications sont effectuées pendant l'exécution du serveur. ( [ #972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/972) ) 
  * Amélioration de la formulation du message obtenu lorsque le serveur de développement comporte un chemin d'accès au SDK Cloud non valide. ( [ #1043 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1043) ) 
  * Mise à jour des noms de configuration d'exécution avec le préfixe "Google" ( [ #1021 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1021) ). 

##  16.10.1

  * Notez que nous planifions de remplacer le schéma de gestion des versions par YY.MM.i. Nous prévoyons une fréquence de publication mensuelle afin de minimiser les interruptions des mises à jour. Notez également que nous avons abandonné le libellé "Bêta". 
  * ATTENTION : Le serveur de développement local App Engine ne fonctionne pas avec les dernières versions de JDK 8. ( [ #920 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/920) ) Cela devrait être résolu avec la prochaine version du SDK App Engine, disponible prochainement. 

###  Ajout

  * Importateur de bibliothèque en environnement standard App Engine dans l'assistant d'attributs et de projets. ( [ #866 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/866) ) 
  * Les applications de l'environnement standard App Engine utilisant le langage Java 8 recevront une notification leur indiquant d'utiliser le niveau de langage 7. ( [ # 966 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/966) ) 

###  Modification

  * Mise à jour des libellés et des icônes de configuration d'exécution. (Cloud Debugger se nomme désormais Cloud Debugger.) ( [ # 936 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/936) ) 

###  Correction

  * Le mode de débogage du serveur de développement local a été corrigé. ( [ #928 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/928) ) 
  * Le déploiement de l'environnement flexible ne fonctionne pas sous Windows 10. ( [ #937 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/937) ) 
  * L'inspecteur d'objets Cloud Debugger fonctionne à nouveau. ( [ #929 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/929) ) 
  * Horodatage des instantanés Cloud Debugger à l'origine des exceptions NPE. ( [ # 919 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/919) ) 

##  1.0-bêta - 2016-09-14

###  Ajout

  * Compatibilité avec l'environnement standard App Engine. ( [ # 767 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/767) ) 
  * Champs supplémentaires désormais disponibles dans la configuration de déploiement. ( [ # 868 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/868) ) 

##  0.9.7.5-bêta - 2016-08-29

###  Ajout

  * Vérification de la validité du déploiement pour l'utilisateur associé aux identifiants fournis, et invite pour ajouter un nouvel utilisateur si ce n'est pas le cas. ( [ 837 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/837) ) 

##  0.9.6-bêta - 2016-06-23

###  Ajout

  * Compatibilité avec le déploiement dans l'environnement flexible App Engine _compat_ . ( [ #720 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/720) ) 
  * Compatibilité avec le déploiement dans l'environnement standard App Engine. ( [ #665 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/665) ) 
  * Vérification de la compatibilité des plug-ins Cloud Tools et du compte Cloud. ( [ #651 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/650) ) 

###  Modification

  * Le champ de saisie de la version est déplacé afin de devenir une configuration de premier niveau dans la boîte de dialogue de configuration de déploiement. ( [ #639 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/639) ) 

##  0.9.4-bêta - 2016-04-20

###  Ajout

  * Élément de menu d'outils pour le déploiement dans l'environnement flexible App Engine. ( [ #635 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/635) ) 
  * Compatibilité des projets basés sur Maven en tant que sources de déploiement pour les déploiements dans l'environnement flexible App Engine. ( [ # 600 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/600) ) 

###  Modification

  * Le déploiement dans l'environnement flexible App Engine peut être annulé en se déconnectant du serveur d'applications App Engine. ( [ #581 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/581) ) 
  * Les fichiers Dockerfile et ` app.yaml ` générés dans l’environnement flexible App Engine sont désormais automatiquement stockés à l'emplacement recommandé dans un projet Java basé sur Maven. ( [ #575 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/575) ) 

###  Correction

  * Erreur au moment de la connexion qui pourrait avoir pour conséquence qu'aucun utilisateur actif ne soit sélectionné lors de l'ajout d'un utilisateur. ( [ #644 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/644) ) 
  * L'annulation du déploiement App Engine peut entraîner une erreur. ( [ #599 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/599) ) 

