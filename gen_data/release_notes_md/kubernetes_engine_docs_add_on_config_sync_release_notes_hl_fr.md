#  Notes de version

Cette page répertorie les mises à jour en production de Config Sync.
Consultez-la pour obtenir des informations sur les fonctionnalités nouvelles
ou mises à jour, les corrections de bugs, les problèmes connus et les
fonctionnalités obsolètes.

Vous pouvez consulter les dernières mises à jour de produits pour l'ensemble
de Google Cloud sur la page [ Notes de version de Google Cloud
](https://cloud.google.com/release-notes?hl=fr) .

Pour recevoir les dernières mises à jour concernant ce produit, ajoutez l'URL
de cette page à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou ajoutez l'URL
du flux directement : ` https://cloud.google.com/feeds/kubernetes-engine-add-
on-config-sync-release-notes.xml `

##  1.2.0

Config Sync v1.2.0 est en disponibilité générale pour une utilisation en
production. Il s'agit de la première version du produit.

###  Problèmes connus

**ISSUE:**

L'ajout d'un [ service d'API ](https://kubernetes.io/docs/concepts/extend-
kubernetes/api-extension) au dépôt met Config Sync dans un état non
opérationnel, avec le message d'erreur "[KNV2002](/kubernetes-engine/docs/add-
on/config-sync/reference/errors#knv2002): failed to get server resources:
unable to retrieve the complete list of server APIs" (échec de l'obtention des
ressources du serveur : impossible de récupérer la liste complète des API du
serveur). Ce problème affecte aussi bien les nouveaux clusters que les
clusters existants qui se synchronisent avec ce dépôt. Pour corriger ce
problème :

* Recherchez le nom des pods ` git-importer ` et ` syncer ` à l'aide de la commande ` kubectl get pods -n config-management-system ` . 
* Copiez ces noms et relancez les pods avec la commande ` kubectl delete -n config-management-system pods git-importer-xxxx-xxxx syncer-xxxx-xxxx ` . 
* Ces étapes sont à effectuer pour chaque cluster. 
Une fois que vous avez redémarré les pods d'un cluster, la synchronisation
revient à la normale.

**ISSUE:**

` nomos view ` peut ne pas parvenir à analyser les définitions de ressources
personnalisées (CRD, Custom Resource Definitions) qui existent dans le clone
local du dépôt, mais n'ont pas encore été synchronisées avec un cluster.

Pour contourner ce problème, utilisez [ ` nomos hydrate `
](https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/how-
to/nomos-command?hl=fr#hydrate) au lieu de ` nomos view ` .

