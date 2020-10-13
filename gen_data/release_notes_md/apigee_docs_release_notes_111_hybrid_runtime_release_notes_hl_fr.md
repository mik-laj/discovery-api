**REMARQUE** : Certains aspects de ce produit sont en version bêta. Les
options d'installation hybride sont en disponibilité générale. Pour rejoindre
le programme bêta, contactez votre représentant Apigee.

#  1.1.1 - Notes de publication d'un environnement d'exécution hybride Apigee

Le 14 février 2020, nous avons lancé la version 1.1.1 de l'environnement
d'exécution hybride Apigee.

**REMARQUE :** Les API Apigee, l'interface utilisateur Apigee hybride, les
services intégrés GCP et le portail intégré sont en [ version bêta
](https://cloud.google.com/products/?hl=fr#product-launch-stages) . Tous les
autres composants Apigee hybrides sont en phase de disponibilité générale.
Pour plus d'informations, consultez la page [ Gestion des versions et
terminologie ](https://cloud.google.com/apigee/docs/hybrid/terminology?hl=fr)
.  Pour en savoir plus, consultez les ressources suivantes :

  * _[ En savoir plus sur l'installation hybride ](https://cloud.google.com/apigee/docs/hybrid/what-is-hybrid?hl=fr) _ ou _[ Démarrer l'installation ](https://cloud.google.com/apigee/docs/hybrid/big-picture?hl=fr) _
  * _Créer un compte payant :_ contactez le [ service commercial d'Apigee ](https://pages.apigee.com/contact-sales-reg.html?hl=fr)
  * _Questions ou problèmes_ Contactez l' [ assistance Apigee ](https://cloud.google.com/apigee/support/?hl=fr)

##  Mise à niveau

Vous ne pouvez pas mettre à niveau une version de 1.0.0 vers 1.1.1, et la
nouvelle version n'est pas rétrocompatible avec la version 1.0.0. Si vous
utilisez la version 1.0.0, la version 1.1.1 nécessite une nouvelle
installation. Si vous utilisez actuellement la version 1.1.0, vous pouvez
mettre à niveau en suivant ces instructions : [ Mettre à niveau Apigee hybrid
](https://cloud.google.com/apigee/docs/hybrid/upgrade?hl=fr) .

##  Nouvelles fonctionnalités et mises à jour

Voici les nouvelles fonctionnalités et améliorations apportées à cette version
:

###  Compatibilité avec GKE On-Prem et AKS

Vous pouvez maintenant installer l'environnement d'exécution hybride sur
Anthos GKE déployé sur site (GKE on-Prem) et Microsoft® Azure Kubernetes
Service (AKS). Pour commencer, consultez la [ partie 2 : Démarrage rapide
](https://cloud.google.com/apigee/docs/hybrid/install-before-begin?hl=fr) .

Les déploiements multirégionaux sont également compatibles avec GKE On-Prem et
AKS. Consultez les pages [ Déploiement multirégional sur GKE et GKE On-Prem
](https://cloud.google.com/apigee/docs/hybrid/multi-region?hl=fr) et [
Déploiement multirégional sur AKS
](https://cloud.google.com/apigee/docs/hybrid/multi-region-aks?hl=fr) .

###  Variables de proxy pour les composants hybrides

Vous pouvez maintenant fournir des paramètres de configuration pour un serveur
proxy HTTP de transfert. Lorsque cette règle est configurée, toutes les
communications Internet des composants d'UDCA, de MART et du Synchronisateur
passent par le serveur proxy. Pour en savoir plus sur la propriété de
configuration ` httpProxy ` , consultez la page sur les [ propriétés httpProxy
](https://cloud.google.com/apigee/docs/hybrid/config-prop-ref?hl=fr#httpProxy)
. (132167490)

##  Corrections de bugs

Les bugs suivants sont corrigés dans cette version. Cette liste est
principalement destinée aux utilisateurs qui vérifient si leurs demandes
d'assistance ont été corrigées. Il n'est pas conçu pour fournir des
informations détaillées à tous les utilisateurs.

ID du problème  |  Nom du composant  |  Description  
---|---|---  
144448262  |  Plate-forme K8S  |

**Écarts dans la métrique UDCA` udca_upstream_http_error_count label ` **  
  
147258525  |  CPS  |

**Activer l'index de hachage partitionnée en mode hybride**  
  
144286363  |  Trace  |

**Un problème a été résolu, le masque de débogage dans` env.json ` ne masque
pas les données de réponse. **  
  
147191247  |  Plate-forme K8S  |

**La clé de chiffrement du contrat ne doit pas faire partie de` apigeectl init
` **  
  
146932903  |  Plate-forme K8S  |

**Supprimer les ports indésirables de l'entrée Istio**  
  
146426226  |  Plate-forme K8S  |

**Les journaux d'entrée ne sont pas collectés**  
  
143660032  |  RMP  |

**com.apigee.test.runtime.steps.quota.DefaultQuotaTypeTest échoue en hybride**  
  
144973407  |  RMP  |

**Il existe actuellement deux ID de corrélation pour une transaction. Il ne
devrait n'y en avoir qu'un.**  
  
144321473  |  UAP  |

**UDCA : ne supprimer aucun avertissement de vérification de l'état dans la
journalisation**  
  
144321491  |  RMP  |

**CacheConfiguration.warnMaxEntriesLocalHeap() log indique un problème de
performances**  
  
##  Problèmes connus

Le tableau suivant décrit les problèmes connus de cette version :

Problème  |  Description  
---|---  
150187652  |  Vous ne pouvez pas utiliser de tirets dans les noms
d'environnement. Un nom d'environnement avec un tiret entraîne des erreurs de
démarrage du pod d'exécution.  
149220463  |

Lorsque vous passez à la version 1.1.1, les proxys précédemment déployés ne
sont pas déployés.

**Solution :** Pour contourner ce problème, redéployez tous les proxys
précédemment déployés.  
  
ND  |  Vous ne pouvez pas utiliser "*" pour la propriété ` hostAlias ` pour
les configurations ` mart ` et ` envs ` . Il est recommandé d'utiliser un nom
d'hôte spécifique pour la configuration ` mart ` .  
ND  |  La définition des variables ` HTTP_PROXY ` , ` HTTPS_PROXY ` et `
NO_PROXY ` n'est pas prise en charge dans la version Alpha d'Apigee Connect.  
ND  |

Erreur d'en-tête HTTP non valide : l'entrée Istio transfère toutes les
réponses cibles entrantes au protocole HTTP2. Comme le processeur de messages
hybride n'accepte que le protocole HTTP1, vous pouvez rencontrer l'erreur
suivante lorsqu'un proxy d'API est appelé :

    
    
    
    http2 error: Invalid HTTP header field was received: frame type: 1, stream: 1,
       name: [:authority], value: [domain_name]

Si cette erreur s'affiche, vous pouvez effectuer l'une des actions suivantes
pour résoudre le problème :

  * Modifiez le service cible pour omettre l'en-tête "Host" dans la réponse. 
  * Supprimez l'en-tête Host à l'aide de la règle AssignMessage de votre proxy d'API si nécessaire. 

  
144584813  |  Si vous créez une session de débogage, mais que la session ne
comporte pas encore de transactions, elle ne figure pas dans la [ liste des
sessions débogage de l'API
](https://cloud.google.com/hybrid/reference/apis/rest/v1/organizations.environments.apis.revisions.debugsessions/list?hl=fr)
. L'API n'inclut des sessions dans la réponse que si la session contient au
moins une transaction.  
144436206  |  Dans la vue **Performances du cache** , le calcul du taux
d'accès au cache est incorrect.  
144321144  |  Impossible de recharger les proxys avec des hôtes virtuels
sécurisés.  
143659917  |

Le paramètre d'expiration de la règle PopulateCache doit être défini sur une
valeur explicite comprise entre 1 et 30. Exemple :

    
    
    
    <ExpirySettings>
      <TimeoutInSec>30</TimeoutInSec>
    </ExpirySettings>  
  
133192879  |

Résumé : Il existe une latence très élevée lorsque vous utilisez l'API ou
l'interface utilisateur pour obtenir l'état de déploiement de votre
organisation. Cette latence peut entraîner une réponse ` HTTP 204 (No Content)
` ou ` HTTP 400 (Bad Request) ` .

Solution : actualisez votre navigateur (ou renvoyez la requête).

