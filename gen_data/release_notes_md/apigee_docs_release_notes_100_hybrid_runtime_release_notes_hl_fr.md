**REMARQUE** : Certains aspects de ce produit sont en version bêta. Les
options d'installation hybride sont en disponibilité générale. Pour rejoindre
le programme bêta, contactez votre représentant Apigee.

#  1.0.0 (disponibilité générale) - Notes de publication de l'environnement
d'exécution hybride Apigee

Le 20 novembre 2019, Google a lancé la version 1.0.0 de l'environnement
d'exécution hybride Apigee. Cette section décrit les corrections de bugs et
les problèmes connus liés à la version 1.0.0.

**REMARQUE** : Les API Apigee, l'interface utilisateur Apigee Apigee, les
services intégrés GCP et le portail intégré sont disponibles en [ version bêta
](https://cloud.google.com/products/?hl=fr#product-launch-stages) . Tous les
autres composants hybrides Apigee sont disponibles dans Google Analytics. Pour
en savoir plus, consultez la page [ Gestion des versions et terminologie
](https://cloud.google.com/apigee/docs/hybrid/terminology?hl=fr) .  Pour en
savoir plus, consultez les ressources suivantes :

  * _[ En savoir plus sur les environnements hybrides ](https://cloud.google.com/apigee/docs/hybrid/what-is-hybrid?hl=fr) _ ou _[ Commencer l'installation ](https://cloud.google.com/apigee/docs/hybrid/big-picture?hl=fr) _
  * _Créer un compte payant_ : contactez le [ service commercial d'Apigee ](https://pages.apigee.com/contact-sales-reg.html?hl=fr)
  * _Questions ou problèmes ?_ Contacter l' [ assistance Apigee ](https://cloud.google.com/apigee/support/?hl=fr)

###  Problèmes connus (disponibilité générale)

Le tableau suivant décrit les problèmes connus de cette version:

Problème  |  Description  
---|---  
144886537  |  Le routage de chemin de base ne fonctionne pas dans la version
hybride 1.0.0 de Apigee. Lorsque les remplacements sont configurés pour
acheminer le trafic vers différents environnements avec le même hôte
hostAliase, l'entrée n'est pas acheminé vers l'environnement en fonction du
chemin.  
144584813  |  Si vous créez une session de débogage, mais que la session ne
contient encore aucune transaction, l' [ API List Debug Sessions
](https://cloud.google.com/hybrid/reference/apis/rest/v1/organizations.environments.apis.revisions.debugsessions/list?hl=fr)
n'inclut pas la session dans cette liste. L'API n'inclut des sessions dans la
réponse que si la session contient au moins une transaction.  
144436206  |  Dans la vue **Performances du cache** , le calcul du taux
d'accès au cache est incorrect.  
144321491  |  Apigee hybride enregistre les notifications "Création de cache
manquant" indiquant une dégradation potentielle des performances. Ces messages
sont attendus et peuvent être ignorés.  
144321144  |  Les proxys avec des hôtes virtuels sécurisés  ne peuvent pas
être actualisés.  
144286363  |

Le masque de débogage dans env.json ne masque pas les données de réponse.

L'API suivante ne permet pas de mettre à jour le masque de débogage "env.json"
avec un champ "responseJSONPaths" :

    
    
    
    PATCH /v1/organizations/org/environments/env/debugmask?replaceRepeatedFields=true
    {
      "responseJSONPaths": ["$.maskedDataEnv"]
    }

Pour contourner ce problème avec la trace, vous pouvez supprimer une session
de trace entière dans l'interface utilisateur ou utiliser les API de trace
pour supprimer des transactions individuelles au sein d'une session.  
  
143774187  |  L'interface utilisateur hybride affiche le libellé "Company"
(Entreprise) dans la vue "Apps" (Applications).  
143659917  |

Le paramètre d'expiration de la règle PopuleCache doit être défini sur une
valeur explicite comprise entre 1 et 30. Exemple :

    
    
    
    <ExpirySettings>
      <TimeoutInSec>30</TimeoutInSec>
    </ExpirySettings>  
  
133192879  |

Résumé : il existe une latence très élevée lorsque vous utilisez l'API ou
l'interface utilisateur pour obtenir l'état de déploiement de votre
organisation. Cette latence peut entraîner une réponse ` HTTP 204 (No Content)
` ou ` HTTP 400 (Bad Request) ` .

Solution : actualisez votre navigateur (ou renvoyez la requête).  
  
123932912  |  Avec un déploiement sans interruption, lorsque le déploiement
d'une nouvelle révision échoue, la révision d'origine n'est toujours pas
déployée. Vous devrez redéployer la révision d'origine pour restaurer son état
de déploiement.  
ND  |

Erreur d'en-tête HTTP non valide : l'entrée Istio bascule toutes les réponses
cibles entrantes vers le protocole HTTP2. Comme le processeur de messages
hybride n'accepte que HTTP1, le message d'erreur suivant peut s'afficher
lorsqu'un proxy API est appelé:

    
    
    
    http2 error: Invalid HTTP header field was received: frame type: 1, stream: 1,
       name: [:authority], value: [domain_name]

Si cette erreur s'affiche, vous pouvez effectuer l'une des actions suivantes
pour corriger le problème :

  * Modifiez le service cible pour omettre l'en-tête "Host" dans la réponse. 
  * Supprimez l'en-tête "Host" à l'aide de la stratégie "AssignMessage" dans votre proxy d'API, si nécessaire. 

  
  
###  Bugs résolus

Les problèmes suivants répertoriés dans les notes de version d'Apigee hybride
bêta 2 ont été résolus :

Problème  |  Description  
---|---  
**133444606** |

L'API de mise à jour des applications pour les développeurs n'accepte pas tous
les champs d'entrée documentés.  
  
**133192879** |

Il existe une latence très élevée lorsque vous utilisez l'API ou l'interface
utilisateur pour obtenir l'état de déploiement de votre organisation. Cette
latence peut entraîner une réponse ` HTTP 204 (No Content) ` ou ` HTTP 400
(Bad Request) ` .  
  
**131111865** |

L'outil de synchronisation échoue lorsque le système de fichiers est trop
saturé. Cela est dû au processus de récupération de mémoire de Kubernetes : il
n'est déclenché qu'à atteindre 85 % par défaut.

Fermée : non reproductible.  
  
##  Fonctionnalités Apigee Edge non compatibles

Google _ne prévoit pas_ de prendre en charge les fonctionnalités suivantes
dans Apigee hybride:

  * API vers : 
    * Manipuler les entrées KVM 
    * Rechercher ou révoquer des jetons d'accès OAuth (car les jetons sont hachés) 
  * Développement du portail des développeurs avec Drupal 7 
  * OAuth v1 ou [ stratégie OAuthv1.0a ](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oauth-10-policy-policy?hl=fr)
  * Règle de limitation du débit de [ ConcurrentRateLimit ](https://cloud.google.com/apigee/docs/api-platform/reference/policies/concurrent-rate-limit-policy?hl=fr)
  * Trireme (fin de vie le 10/10/2019) 

Pour une comparaison complète des fonctionnalités entre hybride et Edge,
consultez la section [ Comparer hybride et Edge
](https://cloud.google.com/apigee/docs/hybrid/compare-hybrid-edge?hl=fr) .

##  Étape suivante

  * [ En savoir plus sur les environnements hybrides ](https://cloud.google.com/apigee/docs/hybrid/what-is-hybrid?hl=fr)
  * [ Commencer l'installation ](https://cloud.google.com/apigee/docs/hybrid/big-picture?hl=fr)

