#  Release notes

This page documents production updates to Anthos Config Management. Check this
page for announcements about new or updated features, bug fixes, known issues,
and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/anthosconfig-release-notes.xml
`

##  May 21, 2020

1.3.2

**CHANGED:**

This release includes several performance and memory improvements.

In order to help prevent accidental deletion, Anthos Config Management will no
longer allow a user to remove all namespaces or cluster-scoped resources in a
single commit. If you wish to delete the full set of resources under
management, it now requires two steps: remove all but one in a first commit,
allow ACM to sync those changes, then remove the final resource in a second
commit.

**CHANGED:**

[ Error documentation ](https://cloud.google.com/anthos-config-
management/docs/reference/errors) has been updated to add more information on
error codes. Errors that are no longer encountered in the product have been
removed. Most error references have been embellished with examples and steps
for remediation.

**CHANGED:**

Anthos Config Management now supports a GKE-only authentication mechanism
based on the service account of the cluster's node pool. Documentation on its
use is [ here ](https://cloud.google.com/anthos-config-management/docs/how-
to/installing#git-creds-gcenode) .

**FEATURE:**

Anthos Config Management now includes [ Config Connector
](https://cloud.google.com/config-connector) v1.8.0.

**CHANGED:**

Anthos Config Management will now attempt to detect when resources that it
manages are also managed by other controllers. Documentation on this behavior
is available in [ error ` knv2005 ` ](https://cloud.google.com/anthos-config-
management/docs/reference/errors#knv2005) which ACM will log in that case.

**CHANGED:**

Policy Controller has been upgraded to include a newer version of [ Open
Policy Agent Gatekeeper ](https://github.com/open-policy-
agent/gatekeeper/tree/480baac44179d75d418b88fbd2c80581fcf183dd) .

This version includes updates to improve the management of policy resources.
As a consequence, finalizers are no longer used to manage Constraints and
Constraint Templates.

The following metrics have been made obsolete due to these changes and have
been removed:

  * gatekeeper_watch_manager_is_running 

  * gatekeeper_watch_manager_last_restart_check_time 

  * gatekeeper_watch_manager_last_restart_time 

  * gatekeeper_watch_manager_restart_attempts 

The following metrics were removed and will be re-implemented in a later
version:

  * gatekeeper_watch_manager_intended_watch_gvk 

  * gatekeeper_watch_manager_watched_gvk 

##  April 23, 2020

1.3.1

**CHANGED:**

Anthos Config Management images are now included in the Google-provided system
images for [ Binary Authorization ](https://cloud.google.com/binary-
authorization) .

**FEATURE:**

Policy Agent now allows configuration of namespaces that will bypass the
admission controller. For more information, see [ Excluding Namespaces from
Policy Controller ](https://cloud.google.com/anthos-config-
management/docs/how-to/policy-controller-exclude-namespaces)

**CHANGED:**

You can now [ exempt Namespaces ](https://cloud.google.com/anthos-config-
management/docs/how-to/policy-controller-exclude-namespaces) from Policy
Controller enforcement

**FIXED:**

Anthos Config Management v1.3.1 now supports Kubernetes v1.16 and higher.
Earlier versions of Anthos Config Management relied on APIs that have been [
deprecated in Kubernetes v1.16 ](https://cloud.google.com/kubernetes-
engine/docs/deprecations/apis-1-16) .

**FIXED:**

The Anthos Config Management Syncer pod now reports when it detects that it is
fighting with another process over a resource.

**FIXED:**

Anthos Config Management no longer allows managing resources in unmanaged
Namespaces.

**ISSUE:**

If you define a CRD with an integer field that has min/max values, Anthos
Config Management will be unable to update the CRD.

**FIXED:**

Anthos Config Management no longer overwrites undeclared labels and
annotations on Namespaces.

##  March 24, 2020

1.3.0

**CHANGED:**

Anthos Policy Controller is now Generally Available

**CHANGED:**

Anthos Config Management now includes the generally-available version of
Config Connector.

**CHANGED:**

Anthos Config Management now supports the use of a [ Personal Access Tokens
](https://help.github.com/en/github/authenticating-to-github/creating-a-
personal-access-token-for-the-command-line) for authentication against
supported Git providers. More information can be found in [ Installing Anthos
Config Management ](https://cloud.google.com/anthos-config-
management/docs/how-to/installing) .

**CHANGED:**

Anthos Config Management now supports the use of an HTTP or HTTPS proxy to
connect with your Git host. More information can be found at [ Installing
Anthos Config Management ](https://cloud.google.com/anthos-config-
management/docs/how-to/installing) .

##  February 21, 2020

1.2.2

**ISSUE:**

GKE On-prem 1.2.2 includes images for ACM 1.2.1. Upgrading from ACM 1.2.1 to
ACM 1.3 is a valid, tested, safe upgrade path.

**FIXED:**

Minor updates and bug fixes.

##  February 10, 2020

1.2.1

**FEATURE:**

Anthos Config Management v1.2.1 is generally available for use in production.

**FEATURE:**

Git repos with submodules are now also supported by Anthos Configuration
Management out of the box without additional configuration. This allows
delegation of config authoring in a Git-idiomatic way. For more information,
please see [ Git's documentation on submodules ](https://git-
scm.com/book/en/v2/Git-Tools-Submodules) .

**FEATURE:**

A new CLI subcommand is available. ` nomos bugreport ` bundles up Anthos
Config Management log information into a Zip file, which can be attached to a
Google support ticket.

**FIXED:**

Previously, adding an [ APIService
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension) to the
repo will leave Anthos Config Management in a bad state, with the error
message " [ KNV2002 ](https://cloud.google.com/anthos-config-
management/docs/reference/errors#knv2002) : failed to get server resources:
unable to retrieve the complete list of server APIs." This issue has been
mitigated; Anthos Config Management will now sync APIService objects
correctly.

**ISSUE:**

It is not currently possible to downgrade to v1.0.x after upgrading to a more
recent version of Anthos Config Management.

**ISSUE:**

Currently, Config Connector can only be installed on a single cluster. If
multiple Config Connector instances attempt to create or mutate the same
Google Cloud resource, conflicts or errors may occur, and you may exhaust
quota for a given resource.

**FEATURE:**

Anthos Config Management now can optionally support an unstructured
repository, though some features that relied on hierarchical namespaces are
disabled in this mode. More information can be found [ here
](https://cloud.google.com/anthos-config-management/docs/how-to/unstructured-
repo) .

##  December 20, 2019

1.2.0

**FEATURE:**

Anthos Config Management v1.2.0 is generally available for use in production.

This release has minor bug fixes and performance improvements.

##  September 19, 2019

1.1.0

**FEATURE:**

Anthos Config Management v1.1.0 is generally available for use in production.

**FEATURE:**

[ Policy Controller ](https://cloud.google.com/anthos-config-
management/docs/concepts/policy-controller) (Beta) is a Kubernetes dynamic
admission controller that checks, audits, and enforces your clusters'
compliance with policies related to security, regulations, or business rules.
It is built using [ Gatekeeper ](https://github.com/open-policy-
agent/gatekeeper) , an open source project.

**FEATURE:**

You can now enable integration with [ Config Connector
](https://cloud.google.com/config-connector/docs/overview) (beta), a
Kubernetes addon that allows you to manage your Google Cloud Platform
resources through Kubernetes configuration. You can sync configs for GCP
resources with your Anthos Config Management repo and apply them
automatically. For more information, see [ Installing Config Connector
](https://cloud.google.com/anthos-config-management/docs/how-to/installing-
config-connector) .

**CHANGED:**

The ` apiVersion ` for the ConfigManagement CustomResource has changed. No
action is required; the CustomResource is upgraded automatically when you
upgrade to v1.1.0. You can read more about [ configuring Anthos Config
Management ](https://cloud.google.com/anthos-config-management/docs/how-
to/installing#configuring-config-management-operator) .

**CHANGED:**

Managed CRDs (CustomResourceDefinitions) are now Namespace-scoped by default,
instead of cluster-scoped. This matches the semantics of the ` kubectl `
command.

If a CRD explicitly specifies a scope, Anthos Config Management honors that
scope.

**CHANGED:**

The [ ` nomos hydrate ` ](https://cloud.google.com/anthos-config-
management/docs/how-to/nomos-command#hydrate) command is a replacement for the
` nomos view ` command, and reports your Anthos Config Management
configuration in a human-readable way.

To use ` nomos hydrate ` , upgrade the ` nomos ` command to v1.1.

If you need to continue using ` nomos view ` , do not upgrade the nomos
command from v1.0. It will remain forward-compatible for the foreseeable
future.

You can read about a [ known issue with nomos view
](https://cloud.google.com/anthos-config-management/docs/release-
notes#known_issue_nomos_view) .

**CHANGED:**

Anthos Config Management can now be installed on clusters using
PodSecurityPolicies.

**DEPRECATED:**

The ` nomos view ` command is deprecated and is not included in v1.1 or higher
of the ` nomos ` command.

If you need to continue using ` nomos view ` , do not upgrade the ` nomos `
command from v1.0. It will remain forward-compatible for the foreseeable
future.

**ISSUE:**

It is not currently possible to downgrade to v1.0.x after upgrading to v1.1.0.

**ISSUE:**

Currently, Config Connector can only be installed on a single cluster. If
multiple Config Connector instances attempt to create or mutate the same GCP
resource, conflicts or errors may occur, and you may exhaust quota for a given
resource.

**ISSUE:**

Adding an [ APIService ](https://kubernetes.io/docs/concepts/extend-
kubernetes/api-extension) to the repo will leave Anthos Config Management in a
bad state, with the error message [ KNV2002 ](https://cloud.google.com/anthos-
config-management/docs/reference/errors#knv2002) : failed to get server
resources: unable to retrieve the complete list of server APIs." This issue
will affect both new and existing clusters syncing from this repo. To correct
the issue:

  * find the name of the ` git-importer ` and ` syncer ` pods using ` kubectl get pods -n config-management-system `
  * copy those names and restart the pods with ` kubectl delete -n config-management-system pods git-importer-xxxx-xxxx syncer-xxxx-xxxx `
  * These steps are required once for each cluster. 

Once the pods for a cluster are restarted, syncing will be back to normal.

**ISSUE:**

` nomos view ` can fail to parse CRDs (Custom Resource Definitions) that exist
in the local clone of the repo but have not yet been synced to a cluster.

To work around this issue, use ` nomos hydrate ` instead of ` nomos view ` .

##  June 14, 2019

1.0.0

**FEATURE:**

Anthos Config Management v1.0.0 is generally available for use in production.

To upgrade to this version, follow the instructions for [ upgrading
](https://cloud.google.com/anthos-config-management/docs/how-
to/installing#upgrading) .

You must update all ` nomos ` binaries when you upgrade to Anthos Config
Management v1.0.0.

Versions older than v1.0.0 are no longer available. If you participated in the
early-access program for Anthos Config Management, you must upgrade to v1.0.0.

**FEATURE:**

You can now sync CustomResourceDefinitions (CRDs). Anthos Config Management
can now sync any type of Kubernetes object. For more information, see [
Configuring CustomResourceDefinitions ](https://cloud.google.com/anthos-
config-management/docs/configs#configuring-CustomResourceDefinitions) .

**FEATURE:**

We document how to [ stop Anthos Config Management from syncing configs
](https://cloud.google.com/anthos-config-management/docs/stopping-resuming-
syncing) as quickly as possible. This allows you to mitigate the potential for
propagating unintended configs to clusters.

**FEATURE:**

The [ ` nomos status ` ](https://cloud.google.com/anthos-config-
management/docs/nomos-command#status) subcommand provides a top-level view of
the state of Anthos Config Management on all enrolled clusters, including
errors and sync status. It reports on all clusters that ` kubectl ` can
access.

**CHANGED:**

The product name is now Anthos Config Management.

**CHANGED:**

The ` nomos version ` command now provides version details for the Config
Management Operator on each configured cluster, as well as the version of the
` nomos ` command itself.

**CHANGED:**

New [ metrics ](https://cloud.google.com/anthos-config-
management/docs/monitoring) allow you to monitor counts, latencies, and
timestamps of specific operations.

**CHANGED:**

The following changes have been made to the canonical example repository:

  * The [ canonical example repo ](https://github.com/GoogleCloudPlatform/csp-config-management) has moved. If you use this repo or a fork, update your Git repository's remotes or create a separate clone of the new repo to ensure that you receive updates. 

  * The filesystem standard and the value of the Repo object's spec.version for this version of Anthos Config Management are both ` 1.0.0 ` . 

  * A new branch named ` 1.0.0 ` contains configs compatible with Anthos Config Management v1.0.0. 

**CHANGED:**

An [ example NetworkPolicy ](https://cloud.google.com/anthos-config-
management/docs/configs#network-policy-config) illustrates some methods for
enforcing good security practices across your clusters.

**CHANGED:**

We improved the [ instructions for setting up SSH keys
](https://cloud.google.com/anthos-config-management/docs/installing#git-creds-
secret) for authenticating to a Git repository.

**BREAKING:**

HierarchicalResourceQuotas are no longer supported.

##  March 29, 2019

0.13.1

**FEATURE:**

Anthos Config Management v0.13.1 (beta) is a maintenance release, and is
compatible with Anthos Config Management v0.13.0.

To upgrade from v0.13.0 on an existing cluster, [ deploy the new Config
Management Operator ](https://cloud.google.com/anthos-config-
management/docs/installing#installing) . You may need to remove an object that
is no longer used, to prevent spurious log messages. See the release note
about the change below.

**FEATURE:**

You can now manage the ` default ` Namespace as well as Namespaces with names
beginning with ` kube ` -.

**FIXED:**

Previously, if a config change removed a controller object (for example, a
Deployment that has a ReplicaSet), removing the controller object did not
remove objects it controlled. All of a controller object's child objects are
now correctly removed when the controller object itself is removed.

**FIXED:**

Previously, if your repo contained only configs for Namespaces and no other
configs, the Namespace configs would fail to sync. Repos now sync correctly
even if it only contains configs for Namespaces.

**CHANGED:**

The ` git-policy-importer ` application has been renamed to ` git-importer ` .

**CHANGED:**

The ` nomos-cluster-policy ` ClusterConfig has been renamed to ` config-
management-cluster-config ` . After upgrading, both ClusterConfig objects both
exist on the cluster. This does not impact the functionality of the cluster,
but you may see spurious log messages if the older ClusterConfig is still
present. You can remove the old ClusterConfig to avoid these log messages:

    
    
    kubectl delete clusterconfig nomos-cluster-policy
    

**ISSUE:**

Syncing of CustomResourceDefinitions is not currently supported. If
CustomResourceDefinition has been applied to the cluster, you can sync
associated CustomResources.

**Update:** This issue no longer exists in Anthos Config Management v1.0.0 and
higher.

##  March 20, 2019

0.13.0

**BREAKING:**

Anthos Config Management 13.0.0 is the second beta release of Anthos Config
Management. It represents a major change from v0.11.6, is not backward-
compatible with any prior release, and cannot be installed on a cluster with a
previous installation of Anthos Config Management. Backward-incompatible
releases will always use a new minor version number.

**FEATURE:**

You can now share a ResourceQuota among multiple Namespaces with a common
abstract namespace directory. See [ Aggregate ResourceQuotas
](https://cloud.google.com/anthos-config-management/docs/namespace-scoped-
objects#resourcequota-aggregate) .

**CHANGED:**

Syncs are no longer required, and are now silently ignored by the Config
Management Operator. You can now create a config for any object in your
cluster except a CustomResourceDefinition or the Config Management Operator
itself.

**CHANGED:**

The ` nomos-system ` Namespace has been renamed to ` config-management-system
` .

**CHANGED:**

The ` nomos.dev/ ` API group has been renamed to ` configmanagement.gke.io/ `
.

**CHANGED:**

The Nomos object has been renamed to the ConfigManagement object and is now
cluster-scoped.

**CHANGED:**

The ` nomos-resource-quota ` object, which combines all of a Namespace's
effective ResourceQuotas into a single one that is more efficient for
Kubernetes to check and enforce, has been renamed to ` config-management-
resource-quota ` .

**CHANGED:**

Prometheus now uses the ` gkeconfig ` Namespace.

**CHANGED:**

Annotations, rather than labels, are now used to determine that Anthos Config
Management is managing a Kubernetes object.

**ISSUE:**

Syncing of CustomResourceDefinitions is not currently supported. If a
CustomResourceDefinition has been applied to the cluster, you can sync
associated CustomResources.

**Update:** This issue no longer exists in Anthos Config Management v1.0.0 and
higher.

##  March 04, 2019

0.11.6

**BREAKING:**

This is the beta release of Anthos Config Management. It represents a major
change from v0.10.4, and cannot be installed on a cluster with a previous
installation of Anthos Config Management. An existing installation of the
alpha from v0.10.4 or earlier will conflict with a new installation of v0.11.6
due to changes in the repository structure.

**FEATURE:**

Added support for syncing all Kubernetes resources generically. For current
limitations, see the list of known issues for this release.

**FEATURE:**

Added support for NamespaceSelectors.

**CHANGED:**

Moved repository format to Filesystem Standard v0.1.0.

**CHANGED:**

Moved installation to use the Config Management Operator.

**ISSUE:**

Syncing of CustomResourceDefinitions is not currently supported. If a
CustomResourceDefinition has been applied to the cluster, you can sync
associated CustomResources.

**Update:** This issue no longer exists in Anthos Config Management v1.0.0 and
higher.

**ISSUE:**

In some cases, local changes to managed resources made by ` kubectl apply `
can result in the removal of the ` nomos.dev/managed: enabled ` label, causing
the resource to become unmanaged. As a workaround, use ` kubectl edit `
instead, or include the label in the YAML manifest you are applying.

**Update:** This issue no longer exists in Anthos Config Management v1.0.0 and
higher. If changes are manually applied to managed Kubernetes objects, Anthos
Config Management effectively reverts those changes as soon as it notices a
difference between the config in the repo and the object in the cluster.

For more information, see [ Managing and unmanaging objects
](https://cloud.google.com/anthos-config-management/docs/how-to/configs) .

