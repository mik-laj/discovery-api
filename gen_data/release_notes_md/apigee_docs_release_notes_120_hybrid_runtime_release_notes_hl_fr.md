**REMARQUE** : Certains aspects de ce produit sont en version bêta. Les
options d'installation hybride sont en disponibilité générale. Pour rejoindre
le programme bêta, contactez votre représentant Apigee.

#  1.2.0 - Notes de version de l'environnement d'exécution Apigee hybrid

Le 3 avril 2020, nous avons lancé la version 1.2.0 de l'environnement
d'exécution Apigee hybrid.

Pour en savoir plus, consultez les ressources suivantes :

  * _[ En savoir plus sur les environnements hybrides ](https://cloud.google.com/apigee/docs/hybrid/v1.2/what-is-hybrid?hl=fr) _ ou _[ Commencer l'installation ](https://cloud.google.com/apigee/docs/hybrid/v1.2/big-picture?hl=fr) _
  * _Créer un compte payant_ : contactez le [ service commercial d'Apigee ](https://pages.apigee.com/contact-sales-reg.html?hl=fr)
  * _Questions ou problèmes ?_ Contactez l' [ assistance Apigee ](https://cloud.google.com/apigee/support/?hl=fr)

####  Aide et notifications

**Questions ou problèmes ?** [ Cliquez ici pour obtenir de l'aide.
](https://cloud.google.com/apigee/support/?hl=fr)

**Notifications de version** : accédez à [ http://status.apigee.com
](http://status.apigee.com?hl=fr) et cliquez sur **S'abonner aux mises à
jour** .

[ Page d'accueil des notes de version
](https://cloud.google.com/apigee/docs/release/notes/apigee-release-
notes?hl=fr)

##  Mise à niveau…

Pour passer de la version 1.1.1 à la version 1.2.0, vous devez modifier votre
fichier de remplacement qui est incompatible avec la version 1.1.1. Ces
modifications sont nécessaires pour effectuer la mise à niveau. La nouvelle
configuration corrige un problème, dans certains cas où les appels d'API ont
été acheminés vers le mauvais environnement. Pour en savoir plus, consultez la
section [ Mettre à niveau Apigee hybrid
](https://cloud.google.com/apigee/docs/hybrid/v1.2/upgrade?hl=fr) .

##  Nouvelles fonctionnalités et mises à jour

Voici les nouvelles fonctionnalités et mises à jour de cette version.

###  Une nouvelle configuration d'hôte virtuel a été ajoutée pour spécifier
des règles de routage

La nouvelle fonctionnalité de configuration ` virtualhosts ` résout un
problème selon lequel l'ordre dans lequel les chemins de base ont été
acheminés vers plusieurs environnements n'était pas garanti. Pour en savoir
plus, consultez l'article [ Configurer des hôtes virtuels
](https://cloud.google.com/apigee/docs/hybrid/v1.2/base-path-routing?hl=fr) .
(150336519)

###  Version bêta de la stratégie OASValidation

La stratégie OASValidation (OpenAPI Spécification Validation) (bêta) vous
permet de valider une requête ou un message de réponse entrants par rapport à
une spécification OpenAPI 3.0 (JSON ou YAML). Pour plus d'informations,
consultez la [ stratégie OASValidation (bêta)
](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oas-
validation-policy?hl=fr) . (144949685)

###  Version bêta de la compatibilité WebSocket

Apigee hybrid est compatible avec les connexions WebSocket. Les clients proxy
d'API peuvent désormais demander une mise à niveau du protocole de HTTP vers
WebSockets. Pour en savoir plus, consultez la section [ Utiliser WebSockets
(version bêta)
](https://cloud.google.com/apigee/docs/hybrid/v1.2/websockets?hl=fr) .

###  Accéder aux valeurs de secret des règles à partir de secrets Kubernetes

Une nouvelle fonctionnalité vous permet d'accéder aux valeurs stockées dans un
secret Kubernetes dans les variables de flux proxy. Pour en savoir plus,
consultez la section [ Stocker des données dans un secret Kubernetes
](https://cloud.google.com/apigee/docs/hybrid/v1.2/k8s-secrets?hl=fr) .
(133377603)

###  L'élément Apigee Operator (AO) remplace ADAC et ADAH

Les opérateurs Apigee (AO) créent et mettent à jour les ressources Kubernetes
et Istio de bas niveau nécessaires au déploiement et à la gestion de l'AD. Par
exemple, le contrôleur effectue le lancement des processeurs de message.
Validez également la configuration ApigeeDeployment avant de la conserver dans
le cluster Kubernetes. AO remplace Apigee Deployment Admissionhook (ADAH) et
Apigee Deployment Control (ADC). Voir [ ao dans la documentation de référence
sur les propriétés de configuration
](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref?hl=fr#ao) .
(151250559)

###  Remplacer et rendre obsolètes certaines propriétés de configuration du
cluster et du projet

Deux propriétés de configuration ont été ajoutées : ` k8sCluster ` et ` gcp `
. Ces propriétés remplacent les propriétés obsolètes suivantes : `
k8sClusterName ` , ` gcpRegion ` et ` gcpProjectID ` . Pour en savoir plus,
consultez la [ documentation de référence sur les propriétés de configuration
](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref?hl=fr) .
(146299599)

###  Expansion du volume persistant pour Cassandra sur Kubernetes

Un processus a été ajouté pour étendre le volume persistant utilisé par
apigee-cassandra pour répondre aux besoins de stockage, sans avoir à ajouter
d'autres nœuds pour augmenter le stockage. Consultez la section [ Développer
les volumes persistants Cassandra
](https://cloud.google.com/apigee/docs/hybrid/v1.2/expand-persistent-
volumes?hl=fr) . (138167919)

###  Compatibilité avec des sources supplémentaires pour les certificats, les
clés de chiffrement et les autorités de contrôle

De nouvelles propriétés de configuration ont été ajoutées pour offrir une plus
grande flexibilité dans la manière de spécifier des certificats TLS, des clés
de chiffrement et des clés de compte de service. Ces nouvelles propriétés sont
répertoriées ci-dessous :

  * ` kmsEncryptionPath `
  * ` kmsEncryptionSecret.key `
  * ` kmsEncryptionSecret.name `
  * ` cassandra.backup.serviceAccountSecretRef `
  * ` cassandra.restore.serviceAccountSecretRef `
  * ` envs[].cacheEncryptionPath `
  * ` envs[].cacheEncryptionSecret.key `
  * ` envs[].cacheEncryptionSecret.name `
  * ` envs[].kmsEncryptionPath `
  * ` envs[].kmsEncryptionSecret.key `
  * ` envs[].kmsEncryptionSecret.name `
  * ` envs[].serviceAccountSecretRefs.synchronizer `
  * ` envs[].serviceAccountSecretRefs.udca `
  * ` envs[].sslSecret `
  * ` logger.serviceAccountSecretRef `
  * ` mart.serviceAccountSecretRef `
  * ` mart.sslSecret `
  * ` metrics.serviceAccountSecretRef `
  * ` synchronizer.serviceAccountSecretRef `
  * ` udca.serviceAccountSecretRef `

Pour plus d'informations, consultez la [ documentation de référence sur les
propriétés de configuration
](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref?hl=fr) .
(145303466)

###  Autoriser les clients à obscurcir les données avant de les envoyer à
Google Analytics

Une fonctionnalité a été ajoutée pour vous permettre de obscurcir certaines
données d'analyse avant leur envoi au plan de gestion. Pour en savoir plus,
consultez la page [ Obscurcir des données utilisateur pour l'analyse
](https://cloud.google.com/apigee/docs/hybrid/v1.2/obfuscate-userdata-for-
analytics?hl=fr) . (142578910)

###  Développer les volumes persistants pour les ensembles avec état

Une fonctionnalité a été ajoutée pour vous permettre d'étendre le volume
persistant utilisé par apigee-cassandra pour répondre aux besoins de stockage,
sans ajouter de puissance de calcul supplémentaire. Pour en savoir plus,
consultez la section [ Développer des volumes persistants pour les ensembles
avec état
](https://cloud.google.com/apigee/docs/release/notes/hybrid/v1.2/expand-
persistent-volumes?hl=fr) . (138167919)

###  Les versions minimales compatibles de GKE, Anthos et AKS sont mises à
niveau.

Apigee hybride est désormais compatible avec GKE 1.14.x, Anthos 1.2 et AKS
1.14.x. (149578101)

###  Compatibilité avec TLS 1.3 pour les connexions Northbound

Deux propriétés de configuration vous permettent de définir la version TLS
minimale et maximale de l'entrée : ` ingress.minTLSProtocolVersion ` et `
maxTLSProtocolVersion ` . Les valeurs possibles sont 1.0, 1.1, 1.2, et 1.3.
Pour en savoir plus, consultez la [ documentation de référence sur les
propriétés de configuration
](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref?hl=fr) .
(117580780)

###  Possibilité de configurer le proxy de transfert pour l'environnement
d'exécution hybride

Le proxy de transfert HTTP est désormais compatible avec les proxys d'API
déployés dans un environnement. Pour en savoir plus, consultez [ Configurer
l'envoi par proxy ](https://cloud.google.com/apigee/docs/hybrid/v1.2/forward-
proxy?hl=fr) . (148970527)

###  Compatibilité avec plusieurs alias d'hôte par environnement

Une nouvelle propriété de configuration, ` envs[].hostAliases ` , a été
ajoutée. Cette propriété vous permet d'ajouter plusieurs alias d'hôte à un
environnement. Utilisez cet élément au lieu de ` hostAlias ` , qui a été
abandonné. Pour plus d'informations, consultez la section [ Ajouter plusieurs
alias d'hôte à un environnement
](https://cloud.google.com/apigee/docs/hybrid/v1.2/environment-
create?hl=fr#adding-multiple-host-aliases-to-an-environment) . (150738495)

###  Autoriser les modèles pour les ensembles de propriétés

Un nouvel élément <PropertySetRef> a été ajouté à l'élément <AssignVariable>
de la règle <AssignMessage>. <PropertySetRef> vous permet de créer une paire
nom/clé de propriété de manière dynamique. Cette fonctionnalité n'est
disponible que pour les proxys d'API déployés sur Apigee hybrid. Consultez la
section [ AssignVariable ](https://cloud.google.com/apigee/docs/api-
platform/reference/policies/assign-message-policy?hl=fr#assignvariable) .
(148612340)

##  Bugs résolus

Les bugs suivants sont corrigés dans cette version. Cette liste est
principalement destinée aux utilisateurs qui vérifient si leurs demandes
d'assistance ont été corrigées. Il n'est pas conçu pour fournir des
informations détaillées pour tous les utilisateurs.

ID du problème  |  Nom du composant  |  Description  
---|---|---  
147958049  |  Exécution  |  Un problème de minutage dans le séquençage de
l'environnement d'exécution a été résolu, ce qui a parfois empêché le
démarrage de la synchronisation.  
149867244  |  Plate-forme K8S  |  Échec du pod apigee-cps-setup dans une
configuration multirégionale  
150187652 / 149117839  |  Exécution  |  Impossible d'utiliser des traits
d'union dans les noms d'environnement  
149220463  |  Pod MP  |  Les proxys précédemment déployés doivent être
redéployés.  
144321144  |  Exécution  |  Les proxys avec des hôtes virtuels sécurisés n'ont
pas pu être actualisés.  
147685310  |  Exécution  |  Échec de l'initialisation de l'outil de
synchronisation en raison de l'échec de la récupération du jeton GCP lors de
l'initialisation.  
151115900  |  Exécution  |  La vérification interne périodique n'apparaît pas
pour HybridMART, ce qui entraîne de faux résultats.  
  
##  Problèmes connus

Le tableau suivant décrit les problèmes connus de cette version :

Problème  |  Description  
---|---  
161658025  |

État de déploiement inexact pour les flux partagés

Pour les flux partagés, l'état du déploiement n'est pas correctement signalé à
l'interface utilisateur, ce qui crée une icône de déploiement en rotation
permanente. Si vous avez déployé un flux partagé et que l'icône de déploiement
en cours d'exécution s'affiche, vous devez supposer que le déploiement a
échoué.

Pour obtenir l'état correct du déploiement, utilisez l'API [
v1.organizations.environments.sharedflows.revisions.deployments
](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest?hl=fr#rest-
resource:-v1.organizations.environments.sharedflows.revisions.deployments) .
Exemple :

    
    
    
    curl -s -H "$AUTH" \
    "https://apigee.googleapis.com/v1/o/$ORG/e/$ENV/sharedflows/$FLOW/revisions/$REV/deployments"  
  
ND  |

Erreur d'en-tête HTTP non valide : l'entrée Istio transfère toutes les
réponses cibles entrantes au protocole HTTP2. Comme le processeur de messages
hybride n'accepte que le protocole HTTP1, vous pouvez rencontrer l'erreur
suivante lorsqu'un proxy d'API est appelé :

    
    
    
    http2 error: Invalid HTTP header field was received: frame type: 1, stream: 1,
       name: [:authority], value: [domain_name]

Si cette erreur s'affiche, vous pouvez effectuer l'une des actions suivantes
pour corriger le problème :

  * Modifiez le service cible pour omettre l'en-tête "Host" dans la réponse. 
  * Si nécessaire, supprimez l'en-tête d'hôte à l'aide de la règle AssignMessage dans votre proxy d'API. 

  
144584813  |  Si vous créez une session de débogage, mais qu'elle ne comporte
pas encore de transactions, l' [ API List Debug Sessions
](https://cloud.google.com/hybrid/v1.2/reference/apis/rest/v1/organizations.environments.apis.revisions.debugsessions/list?hl=fr)
ne l'inclut pas dans la liste. L'API n'inclut les sessions dans la réponse que
si elles contiennent au moins une transaction.  
143659917  |

Le paramètre d'expiration de la règle PopulateCache doit être défini sur une
valeur explicite comprise entre 1 et 30. Exemple :

    
    
    
    <ExpirySettings>
      <TimeoutInSec>30</TimeoutInSec>
    </ExpirySettings>  
  
133192879  |

Résumé : La latence est très élevé lorsque vous utilisez l'API ou l'interface
utilisateur pour obtenir l'état de déploiement de votre organisation. Cette
latence peut aboutir à une réponse ` HTTP 204 (No Content) ` ou ` HTTP 400
(Bad Request) ` .

Solution : actualisez votre navigateur (ou renvoyez la requête).

