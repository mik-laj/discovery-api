#  Release notes

This page documents production updates to Config Sync. Check this page for
announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/kubernetes-engine-add-on-
config-sync-release-notes.xml `

##  1.2.0

Config Sync v1.2.0 is generally available for use in production. This is the
first version of the product.

###  Known issues

**ISSUE:**

Adding an [ APIService ](https://kubernetes.io/docs/concepts/extend-
kubernetes/api-extension) to the repo will leave Config Sync in a bad state,
with the error message "[KNV2002](/kubernetes-engine/docs/add-on/config-
sync/reference/errors#knv2002): failed to get server resources: unable to
retrieve the complete list of server APIs." This issue will affect both new
and existing clusters syncing from this repo. To correct the issue:

* find the name of the ` git-importer ` and ` syncer ` pods using ` kubectl get pods -n config-management-system `
* copy those names and restart the pods with ` kubectl delete -n config-management-system pods git-importer-xxxx-xxxx syncer-xxxx-xxxx `
* These steps are required once for each cluster. 
Once the pods for a cluster are restarted, syncing will be back to normal.

**ISSUE:**

` nomos view ` can fail to parse CRDs (Custom Resource Definitions) that exist
in the local clone of the repo but have not yet been synced to a cluster.

To work around this issue, use [ ` nomos hydrate ` ](/kubernetes-
engine/docs/add-on/config-sync/how-to/nomos-command#hydrate) instead of `
nomos view ` .

