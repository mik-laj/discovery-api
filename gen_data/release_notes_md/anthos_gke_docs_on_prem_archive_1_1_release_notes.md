#  Release Notes

This page documents production updates to GKE on-prem. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

See also:

  * [ Downloads ](/anthos/gke/docs/on-prem/downloads)
  * [ Versioning and upgrades ](/anthos/gke/docs/on-prem/versioning-and-upgrades)
  * [ Upgrading GKE on-prem ](/anthos/gke/docs/on-prem/how-to/upgrading)

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/gkeonprem-release-notes.xml `

##  November 19, 2019

GKE on-prem version 1.1.2-gke.0 is now available. To download version
1.1.2-gke.0's OVA, ` gkectl ` , and upgrade bundle, see [ Downloads
](/anthos/gke/docs/on-prem/downloads#latest) . Then, see [ Upgrading admin
workstation ](/anthos/gke/docs/on-prem/how-to/upgrading) and [ Upgrading
clusters ](/anthos/gke/docs/on-prem/how-to/upgrading) .

This patch version includes the following changes:

###  New Features

**FEATURE:**

Published [ Hardening your cluster ](/anthos/gke/docs/on-prem/archive/1.1/how-
to/security/hardening-your-cluster) .

**FEATURE:**

Published [ Managing clusters ](/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/managing-clusters) .

###  Fixes

**FIXED:**

Fixed the known issue from  November 5  .

**FIXED:**

Fixed the known issue from  November 8  .

###  Known Issues

**ISSUE:**

If you are running multiple data centers in vSphere, running ` gkectl diagnose
cluster ` might return the following error, which you can safely ignore:

    
    
    Checking storage...FAIL
    path '*' resolves to multiple datacenters

**ISSUE:**

If you are running a vSAN datastore, running ` gkectl diagnose cluster ` might
return the following error, which you can safely ignore:

    
    
    PersistentVolume [NAME]: virtual disk "[[DATASTORE_NAME]]
    [PVC]" IS NOT attached to machine "[MACHINE_NAME]" but IS listed in the Node.Status

##  November 8, 2019

**ISSUE:**

In GKE on-prem version 1.1.1-gke.2, a known issue prevents creation of
clusters configured to use a Docker registry. You configure a Docker registry
by populating the GKE on-prem configuration file's ` privateregistryconfig `
field. Cluster creation fails with an error such as ` Failed to create root
cluster: could not create external client: could not create external control
plane: docker run error: exit status 125 `

A fix is targeted for version 1.1.2. In the meantime, if you want to create a
cluster configured to use a Docker registry, pass in the ` --skip-validation-
docker ` flag to ` gkectl create cluster ` .

##  November 5, 2019

**ISSUE:**

GKE on-prem's configuration file has a field, ` vcenter.datadisk ` , which
looks for a path to a virtual machine disk (VMDK) file. During installation,
you choose a name for the VMDK. By default, GKE on-prem creates a VMDK and
saves it to the root of your vSphere datastore.

If you are using a vSAN datastore, you need to create a folder in the
datastore in which to save the VMDK. You provide the full path to the
field—for example, ` datadisk: anthos/gke/docs/on-prem/datadisk.vmdk ` —and
GKE on-prem saves the VMDK in that folder.

When you create the folder, vSphere assigns the folder a universally unique
identifier (UUID). Although you provide the folder path to the GKE on-prem
config, the vSphere API looks for the folder's UUID. Currently, this mismatch
can cause cluster creation and upgrades to fail.

A fix is targeted for version 1.1.2. In the meantime, you need to provide the
folder's UUID instead of the folder's path. Follow the workaround instructions
currently available in the [ upgrading clusters ](/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/upgrading-
clusters#admin_datadisk_folder) and installation topics.

##  October 25, 2019

GKE on-prem version 1.1.1-gke.2 is now available. To download version
1.1.1-gke.2's OVA, ` gkectl ` , and upgrade bundle, see [ Downloads
](/anthos/gke/docs/on-prem/downloads#latest) . Then, see [ Upgrading admin
workstation ](/anthos/gke/docs/on-prem/how-to/upgrading) and [ Upgrading
clusters ](/anthos/gke/docs/on-prem/how-to/upgrading) .

This patch version includes the following changes:

###  New Features

**FEATURE:**

**Action required:** This version upgrades the minimum ` gcloud ` version on
the admin workstation to 256.0.0. You should [ upgrade your admin workstation
](/anthos/gke/docs/on-prem/archive/1.1/how-to/administration/upgrading-admin-
workstation) . Then, you should [ upgrade your clusters ](/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/upgrading-clusters) .

**FEATURE:**

The open source [ CoreOS toolbox ](https://github.com/coreos/toolbox) is now
included in all GKE on-prem cluster nodes. This suite of tools is useful for
troubleshooting node issues. See [ Debugging node issues using toolbox
](/anthos/gke/docs/on-prem/archive/1.1/support/toolbox) .

###  Fixes

**FIXED:**

Fixed an issue that prevented clusters configured with OIDC from being
upgraded.

**FIXED:**

Fixed [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) described in [ Security bulletins
](/anthos/gke/docs/on-prem/archive/1.1/security-bulletins#october-16-2019) .

**FIXED:**

Fixed an issue that caused cluster metrics to be lost due to a lost connection
to Google Cloud. When a GKE on-prem cluster's connection to Google Cloud is
lost for a period of time, that cluster's metrics are now fully recovered.

**FIXED:**

Fixed an issue that caused ingestion of admin cluster metrics to be slower
than ingesting user cluster metrics.

###  Known Issues

**ISSUE:**

For user clusters that are using static IPs and a different network than their
admin cluster: If you overwrite the user cluster's network configuration, the
user control plane might not be able to start. This occurs because it's using
the user cluster's network, but allocates an IP address and gateway from the
admin cluster.

As a workaround, you can update each user control plane's MachineDeployment
specification to use the correct network. Then, delete each user control plane
Machine, causing the MachineDeployment to create new Machines:

  1.     # List MachineDeployments in the admin cluster
        kubectl get machinedeployments --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

  2.     # Update a user control plane MachineDeployment from your shell
        kubectl edit machinedeployment --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINEDEPLOYMENT_NAME]

  3.     # List Machines in the admin cluster
        kubectl get machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

  4.     # Delete user control plane Machines in the admin cluster
        kubectl delete machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINE_NAME]

##  September 26, 2019

GKE on-prem version 1.1.0-gke.6 is now available. To download version
1.1.0-gke.6's ` gkectl ` and upgrade bundle, see [ Downloads
](/anthos/gke/docs/on-prem/downloads#latest) . Then, see [ Upgrading clusters
](/anthos/gke/docs/on-prem/how-to/upgrading) .

This minor version includes the following changes:

###  New Features

**FEATURE:**

The default Kubernetes version for cluster nodes is now version 1.13.7-gke.20
(previously 1.12.7-gke.19).

**FEATURE:**

**Action required:** As of version 1.1.0-gke.6, GKE on-prem now creates
vSphere [ Distributed Resource Scheduler (DRS)
](https://www.vmware.com/products/vsphere/drs-dpm.html) rules for your user
cluster's nodes (vSphere VMs), causing them to be spread across at least three
physical hosts in your datacenter.

**This feature is enabled by default for all new and existing user clusters
running version 1.1.0-gke.6.**

The feature requires that your vSphere environment meets the following
conditions:

  * VMware DRS must be enabled. VMware DRS requires vSphere Enterprise Plus license edition. To learn how to enable DRS, see [ Enabling VMware DRS in a cluster ](https://kb.vmware.com/s/article/1034280) . 
  * The vSphere user account provided in your GKE on-prem configuration file's ` vcenter ` field must have the ` Host.Inventory.EditCluster ` permission. 
  * There are at least three physical hosts available. 

If you _do not_ want to enable this feature for your existing user
clusters—for example, if you don't have enough hosts to accommdate the
feature—perform the following steps _before_ you upgrade your user clusters:

  1. Open your existing GKE on-prem configuration file. 
  2. Under the ` usercluster ` specification, add the ` antiaffinitygroups ` field as described in the [ ` antiaffinitygroups ` documentation ](/anthos/gke/docs/on-prem/archive/1.1/how-to/installation/install#antiaffinitygroups) : 
    
        usercluster:
          ...
          antiaffinitygroups:
            enabled: false
    

  3. Save the file. 
  4. Use the configuration file to upgrade. Your clusters are upgraded, but the feature is not enabled. 

**FEATURE:**

You can now set the [ default storage class ](/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/default-storage-class) for your
clusters.

**FEATURE:**

You can now use [ Container Storage Interface (CSI) 1.0
](https://github.com/container-storage-interface/spec) as a storage class for
your clusters.

**FEATURE:**

You can now [ delete broken or unhealthy user clusters ](/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/deleting-a-user-
cluster#delete_unhealthy_cluster) with ` gkectl delete cluster --force `

**FEATURE:**

You can now [ diagnose node issues ](/anthos/gke/docs/on-
prem/archive/1.1/support/debug-toolbox) using the ` debug-toolbox ` container
image.

**FEATURE:**

You can now [ skip validatations ](/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install#skip_validate) run by ` gkectl ` commands.

**FEATURE:**

The tarball that ` gkectl diagnose snapshot ` creates now includes a log of
the command's output by default.

**FEATURE:**

Adds ` gkectl diagnose snapshot ` flag ` --seed-config ` . When you pass the
flag, it includes your clusters' GKE on-prem configuration file in the tarball
procduced by ` snapshot ` .

###  Changes

**CHANGED:**

The ` gkeplatformversion ` field has been removed from the GKE on-prem
configuration file. To specify a cluster's version, provide the version's
bundle to the ` bundlepath ` field.

**CHANGED:**

You need to add the vSphere permission, ` Host.Inventory.EditCluster ` ,
before you can use [ ` antiaffinitygroups ` ](/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/install#antiaffinitygroups) .

**CHANGED:**

You now specify a configuration file in ` gkectl diagnose snapshot ` by
passing the ` --snapshot-config ` (previously ` --config ` ). See [ Diagnosing
cluster issues ](/anthos/gke/docs/on-
prem/archive/1.1/support/diagnose#diagnose_snapshot) .

**CHANGED:**

You now capture your cluster's configuration file with ` gkectl diagnose
snapshot ` by passing ` --snapshot-config ` (previously ` --config ` ). See [
Diagnosing cluster issues ](/anthos/gke/docs/on-
prem/archive/1.1/support/diagnose#diagnose_snapshot) .

**CHANGED:**

` gkectl diagnose ` commands now return an error if you provide a user
cluster's kubeconfig, rather than an admin cluster's kubeconfig.

**CHANGED:**

Cloud Console now notifies you when an upgrade is available for a registered
user cluster.

###  Known Issues

**ISSUE:**

A known issue prevents version 1.0.11, 1.0.1-gke.5, and 1.0.2-gke.3 clusters
using OIDC from being upgraded to version 1.1. A fix is targeted for version
1.1.1. If you configured a version 1.0.11, 1.0.1-gke.5, or 1.0.2-gke.3 cluster
with OIDC, you are not able to upgrade it. Create a version 1.1 cluster by
following [ Installing GKE on-prem ](/anthos/gke/docs/on-prem/how-to/install)
.

##  August 22, 2019

GKE on-prem version 1.0.2-gke.3 is now available. This patch release includes
the following changes:

###  New Features

**FEATURE:**

Seesaw is now supported for manual load balancing.

**FEATURE:**

You can now specify a different vSphere network for admin and user clusters.

**FEATURE:**

You can now delete user clusters using ` gkectl ` . See [ Deleting a user
cluster ](/anthos/gke/docs/on-prem/archive/1.1/how-to/administration/deleting-
a-user-cluster) .

###  Changes

**CHANGED:** ` gkectl diagnose snapshot ` now gets logs from the user cluster
control planes.

**CHANGED:**

GKE on-prem OIDC specification has been updated with several new fields: `
kubectlredirecturl ` , ` scopes ` , ` extraparams ` , and ` usehttpproxy ` .

**CHANGED:**

Calico updated to version 3.7.4.

**CHANGED:**

Cloud Monitoring's system metrics prefixed changed from `
external.googleapis.com/prometheus/ ` to ` kubernetes.io/anthos/ ` . If you
are tracking metrics or alerts, update your dashbaords with the next prefix.

###  Fixed

**FIXED:**

[ Fixed a vulnerability from CVE-2019-11247 ](/anthos/gke/docs/on-
prem/archive/1.1/security-bulletins#august-22-2019) .

**FIXED:**

[ Fixed a vulnerability in RBAC proxy ](/anthos/gke/docs/on-
prem/archive/1.1/security-bulletins#august-23-2019) .

##  July 30, 2019

GKE on-prem version 1.0.1-gke.5 is now available. This patch release includes
the following changes:

###  New Features

**FEATURE:**

Published [ GKE on-prem cheatsheet ](/anthos/gke/docs/on-
prem/archive/1.1/reference/cheatsheet) .

###  Changes

**CHANGED:**

` gkectl check-config ` now also checks node IP availability if you are using
static IPs.

**CHANGED:**

` gkectl prepare ` now checks if a VM exists and is marked as a template in
vSphere before attempting to upload the VM's OVA image.

**CHANGED:**

Adds support for specifying a vCenter cluster, and resource pool in that
cluster.

**CHANGED:**

Upgrades F5 BIG-IP controller to version 1.9.0.

**CHANGED:**

Upgrades Istio ingress controller to version 1.2.2.

###  Fixes

**FIXED:**

Fixes registry data persistence issues with the admin workstation's Docker
registry.

**FIXED:**

Fixes validation that checks whether a user cluster's name is already in use.

##  July 25, 2019

GKE on-prem version 1.0.11 is now available.

##  June 17, 2019

GKE on-prem is now generally available. Version 1.0.10 includes the following
changes:

###  Upgrading from beta-1.4 to 1.0.10

Before upgrading your beta clusters to the first general availability version,
perform the steps described in [ Upgrading from GKE on-prem beta to general
availability ](/anthos/gke/docs/on-prem/archive/1.1/how-to/upgrading/from-
beta) , and review the following points:

  * If you are running a beta version before beta-1.4, be sure to upgrade to beta-1.4 first. 

  * If your beta clusters are running their own L4 load balancers (not the default, F5 BIG-IP), you need to delete and recreate your clusters to run the latest GKE on-prem version. 

  * If your clusters were upgraded to beta-1.4 from beta-1.3, run the following command _for each user cluster_ before upgrading: 
    
        kubectl delete crd networkpolicies.crd.projectcalico.org

  * vCenter certificate verification is now required. ( ` vsphereinsecure ` is no longer supported.) If you're upgrading your beta 1.4 clusters to 1.0.10, you need to provide a vCenter trusted root CA public certificate in the upgrade configuration file. 

  * You need to upgrade _all_ of your running clusters. For this upgrade to succeed, your clusters can't run in a mixed version state. 

  * You need to upgrade your admin clusters to the latest version first, then upgrade your user clusters. 

###  New Features

**FEATURE:**

You can now enable the [ Manual load balancing mode ](/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/manual-lb) to configure a L4 load
balancer. You can still choose to use the default load balancer, F5 BIG-IP.

**FEATURE:**

GKE on-prem's configuration-driven installation process has been updated. You
now declaratively install using a singular [ configuration file
](/anthos/gke/docs/on-prem/archive/1.1/overview#config) .

**FEATURE:**

Adds ` gkectl create-config ` , which generates a configuration file for
installing GKE on-prem, upgrading existing clusters, and for creating
additional user clusters in an existing installation. This replaces the
installation wizard and ` create-config.yaml ` from previous versions. See the
updated documentation for [ installing GKE on-prem ](/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/install#generate_config) .

**FEATURE:**

Adds ` gkectl check-config ` , which validates the GKE on-prem configuration
file. See the updated documentation for [ installing GKE on-prem
](/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install#validate_config) .

**FEATURE:**

Adds an optional ` --validate-attestations ` flag to ` gkectl prepare ` . This
flag verifies that the container images included in your admin workstationwere
built and signed by Google and are ready for deployment. See the updated
documentation for [ installing GKE on-prem ](/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/install#prepare) .

###  Changes

**CHANGED:**

Upgrades Kubernetes version to 1.12.7-gke.19. You can now [ upgrade your
clusters ](/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters) to this version. You can no longer
create clusters that run Kubernetes version 1.11.2-gke.19.

We recommend upgrading your admin cluster before you upgrade your user
clusters.

**CHANGED:**

Upgrades Istio ingress controller to version 1.1.7.

**CHANGED:**

vCenter certificate verification is now required. ` vsphereinsecure ` is no
longer supported). You provide the certificate in the GKE on-prem configration
file's ` cacertpath ` field.

When a client calls the vCenter server, the vCenter server must prove its
identity to the client by presenting a certificate. That certificate must be
signed by a certificate authority (CA). The certificate is must not be self-
signed.

If you're upgrading your beta 1.4 clusters to 1.0.10, you need to provide a
vCenter trusted root CA public certificate in the upgrade configuration file.

###  Known Issues

**ISSUE:**

[ Upgrading clusters ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/upgrading-clusters) can cause disruption or downtime for
workloads that use [ PodDisruptionBudgets
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) (PDBs).

**ISSUE:**

You might not be able to upgrade beta clusters that use the [ Manual load
balancing mode ](/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/manual-lb) to GKE on-prem version 1.0.10. To upgrade and
continue using your own load balancer with these clusters, you need to
recreate the clusters.

##  May 24, 2019

GKE on-prem beta version 1.4.7 is now available. This release includes the
following changes:

###  New Features

**FEATURE:**

In the [ ` gkectl diagnose snapshot ` ](/anthos/gke/docs/on-
prem/archive/1.1/beta-1.4/how-to/administration/diagnose#capture_admin)
command, the ` --admin-ssh-key-path ` parameter is now optional.

###  Changes

**CHANGED:**

On May 8, 2019, we introduced a change to Connect, the service that enables
you to interact with your GKE on-prem clusters using Cloud Console. To use the
new Connect agent, you must re-register your clusters with Cloud Console, or
you must upgrade to GKE on-prem beta-1.4.

Your GKE on-prem clusters and the workloads running on them will continue to
operate uninterrupted. However, your clusters will not be visible in Cloud
Console until you re-register them or upgrade to beta-1.4.

Before you re-register or upgrade, make sure your service account has the `
gkehub.connect ` role. Also, if your service account has the old
clusterregistry.connect role, it's a good idea to remove that role.

Grant your service account the gkehub.connect role:

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

If your service account has the old ` clusterregistry.connect ` role, remove
the old role:

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

Re-register you cluster, or upgrade to GKE on-prem beta-1.4.

To [ re-register your cluster ](/kubernetes-engine/connect/updating-agent) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]
          

To [ upgrade to GKE on-prem beta-1.4 ](/anthos/gke/docs/on-
prem/archive/1.1/beta-1.4/how-to/administration/upgrading-a-cluster) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Known Issues

**ISSUE:**

There is an issue that prevents the Connect agent from being updated to the
new version during an upgrade. To work around this issue, run the following
command after you upgrade a cluster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  May 13, 2019

###  Known Issues

**ISSUE:**

Clusters upgraded from version beta-1.2 to beta-1.3 might be affected by a
known issue that damages the cluster's configuration file and prevents future
cluster upgrades. This issue affects all future cluster upgrades.

You can resolve this issue by deleting and recreating clusters upgraded from
beta-1.2 to beta-1.3.

To resolve the issue without deleting and recreating the cluster, you need to
re-encode and apply each cluster's Secrets. Perform the following steps:

  1. Get the contents of the ` create-config ` Secrets stored in the admin cluster. This must be done for the ` create-config ` Secret in the kube-system namespace, and for the ` create-config ` Secrets in each user cluster's namespace: 
    
        kubectl get secret create-config -n kube-system -o jsonpath={.data.cfg} | base64 -d > kube-system_create_secret.yaml
    
        kubectl get secret create-config -n [USER_CLUSTER_NAME] -o jsonpath={.data.cfg} | base64 -d > [USER_CLUSTER_NAME]_create_secret.yaml

  2. For each user cluster, open the ` [USER_CLUSTER_NAME]  _create_secret.yaml ` file in an editor. If the values for ` registerserviceaccountkey ` and ` connectserviceaccountkey ` are not ` REDACTED ` , no further action is required: the Secrets do not need to be re-encoded and written to the cluster. 
  3. Open the original ` create_config.yaml ` file in another editor. 
  4. In ` [USER_CLUSTER_NAME]  _create_secret.yaml ` , replace the ` registerserviceaccountkey ` and ` connectserviceaccountkey ` values with the values from the original ` create_config.yaml ` file. Save the changed file. 
  5. Repeat steps 3-5 for each ` [USER_CLUSTER_NAME]  _create_secret.yaml ` , and for the ` kube-system_create_secret.yaml ` file. 
  6. Base64-encode each ` [USER_CLUSTER_NAME]  _create_secret.yaml ` file and the ` kube-system_create_secret.yaml ` file: 
    
        cat [USER_CLUSTER_NAME]_create_secret.yaml | base64 > [USER_CLUSTER_NAME]_create_secret_create_secret.b64
    
        cat kube-system-cluster_create_secret.yaml | base64 >kube-system-cluster_create_secret.b64

  7. Replace the ` data[cfg] ` field in each Secret in the cluster with the contents of the corresponding file: 
    
        kubectl edit secret create-config -n [USER_CLUSTER_NAME]
    
      # kubectl edit opens the file in the shell's default text editor
      # Open `first-user-cluster_create_secret.b64` in another editor, and replace
      # the `cfg` value with the copied value
      # Make sure the copied string has no newlines in it!

  8. Repeat step 8 for each ` [USER_CLUSTER_NAME]  _create_secret.yaml ` Secret, and for the ` kube-system_create_secret.yaml ` Secret. 
  9. To ensure that the update was successful, repeat step 1. 

##  May 7, 2019

GKE on-prem beta version 1.4.1 is now available. This release includes the
following changes:

###  New Features

**FEATURE:**

In the [ ` gkectl diagnose snapshot ` ](/anthos/gke/docs/on-
prem/archive/1.1/beta-1.4/how-to/administration/diagnose#capture_admin)
command, the ` --admin-ssh-key-path ` parameter is now optional.

###  Changes

**CHANGED:**

On May 8, 2019, we introduced a change to Connect, the service that enables
you to interact with your GKE on-prem clusters using Cloud Console. To use the
new Connect agent, you must re-register your clusters with Cloud Console, or
you must upgrade to GKE on-prem beta-1.4.

Your GKE on-prem clusters and the workloads running on them will continue to
operate uninterrupted. However, your clusters will not be visible in Cloud
Console until you re-register them or upgrade to beta-1.4.

Before your re-register or upgrade, make sure your service account has the
gkehub.connect role. Also, if your service account has the old
clusterregistry.connect role, it's a good idea to remove that role.

Grant your service account the gkehub.connect role:

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

If your service account has the old clusterregistry.connect role, remove the
old role:

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

Re-register you cluster, or upgrade to GKE on-prem beta-1.4.

To [ re-register your cluster ](/kubernetes-engine/connect/updating-agent) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]
          

To [ upgrade to GKE on-prem beta-1.4 ](/anthos/gke/docs/on-
prem/archive/1.1/beta-1.4/how-to/administration/upgrading-a-cluster) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Known Issues

**ISSUE:**

There is an issue that prevents the Connect agent from being updated to the
new version during an upgrade. To work around this issue, run the following
command after you upgrade a cluster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  April 25, 2019

GKE on-prem beta version 1.3.1 is now available. This release includes the
following changes:

###  New Features

**FEATURE:**

The ` gkectl diagnose snapshot ` command now has a [ ` --dry-run `
](/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/diagnose#performing_a_dry_run_for_a_snapshot) flag.

**FEATURE:**

The ` gkectl diagnose snapshot ` command now supports four [ scenarios
](/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/diagnose#snapshot_scenarios) .

**FEATURE:**

The ` gkectl diagnose snapshot ` command now supports regular expressions for
specifying namespaces.

###  Changes

**CHANGED:**

Istio 1.1 is now the default [ ingress controller ](/anthos/gke/docs/on-
prem/archive/1.1/beta-1.3/how-to/administration/upgrading-a-
cluster#upgrading_the_ingress_controller) . The ingress controller runs in the
` gke-system ` namespace for both admin and user clusters. This enables easier
TLS management for Ingress. To enable ingress, or to re-enable ingress after
an upgrade, follow the instructions under [ Enabling ingress
](/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/installation/install#enabling_ingress) .

**CHANGED:**

The ` gkectl ` tool no longer uses Minikube and KVM for bootstrapping. This
means you do not have to enable nested virtualization on your admin
workstation VM.

###  Known Issues

**ISSUE:**

GKE on-prem's ingress controller uses Istio 1.1 with automatic Secret
discovery. However, the node agent for Secret discovery may fail to get Secret
updates after Secret deletion. So avoid deleting Secrets. If you must delete a
Secret and Ingress TLS fails afterwards, manually restart the Ingress Pod in
the gke-system namespace.

##  April 11, 2019

GKE on-prem beta version 1.2.1 is now available. This release includes the
following changes:

###  New Features

**FEATURE:**

GKE on-prem clusters now automatically connect back to Google using [ Connect
](/kubernetes-engine/connect) .

**FEATURE:**

You can now run up to three control planes per user cluster.

###  Changes

**CHANGED:**

` gkectl ` now validates vSphere and F5 BIG-IP credentials creating clusters.

###  Known Issues

**ISSUE:**

A regression causes ` gkectl diagnose snapshot ` commands to use the wrong SSH
key, which prevents the command from collecting information from user
clusters. As a workaround for support cases, you might need to SSH into
individual user cluster nodes and manually gather data.

##  April 2, 2019

GKE on-prem beta version 1.1.1 is now available. This release includes the
following changes:

###  New Features

**FEATURE:**

You now install GKE on-prem with an [ Open Virtual Appliance (OVA)
](/anthos/gke/docs/on-prem/archive/1.1/beta-1.1/how-to/installation/getting-
started#download_ova) , a pre-configured virtual machine image that includes
several command-line interface tools. This change makes installations easier
and removes a layer of virtualization. You no longer need to run ` gkectl `
inside a Docker container.

If you installed GKE on-prem versions before beta-1.1.1, you should create a
new admin workstation following the documented instructions. After you install
the new admin workstation, copy over any SSH keys, configuration files,
kubeconfigs, and any other files you need, from your previous workstation to
the new one.

**FEATURE:**

Added documentation for [ backing up and restoring clusters
](/anthos/gke/docs/on-prem/archive/1.1/beta-1.1/how-to/administration/backing-
up) .

**FEATURE:**

You can now configure authentication for clusters using OIDC and ADFS. To
learn more, refer to [ Authenticating with OIDC and ADFS
](/anthos/gke/docs/on-prem/archive/1.1/beta-1.1/how-to/security/oidc-adfs) and
[ Authentication ](/anthos/gke/docs/on-
prem/archive/1.1/concepts/authentication) .

###  Changes

**CHANGED:**

You now must use an admin cluster's private key to run ` gkectl diagnose
snapshot ` .

**CHANGED:**

Added a configuration option during installation for deploying multi-master
user clusters.

**CHANGED:**

[ Connect documentation ](/kubernetes-engine/connect) has been migrated.

###  Fixes

**FIXED:**

Fixed an issue where cluster networking could be interrupted when a node is
removed unexpectedly.

###  Known Issues

**ISSUE:**

GKE on-prem's Configuration Management has been upgraded from version 0.11 to
0.13. Several components of the system have been renamed. You need to take
some steps to clean up the previous versions' resources and install a new
instance.

If you have an active instance of Configuration Management:

  1. Uninstall the instance: 
    
        kubectl -n=nomos-system delete nomos --all

  2. Make sure that the instance's namespace has no resources: 
    
        kubectl -n nomos-system get all

  3. Delete the namespace: 
    
        kubectl delete ns nomos-system

  4. Delete the CRD: 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  5. Delete all kube-system resources for the operator: 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

If you don't have an active instance of Configuration Management:

  1. Delete the Configuration Management namespace: 
    
        kubectl delete ns nomos-system

  2. Delete the CRD: 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  3. Delete all kube-system resources for the operator: 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

##  March 12, 2019

GKE on-prem beta version 1.0.3 is now available. This release includes the
following changes:

###  Fixes

**FIXED:**

Fixed an issue that caused Docker certificates to be saved to the wrong
location.

##  March 4, 2019

GKE on-prem beta version 1.0.2 is now available. This release includes the
following changes:

###  New Features

**FEATURE:**

You can now run ` gkectl version ` to check which version of ` gkectl ` you're
running.

**FEATURE:**

You can now [ upgrade user clusters ](/anthos/gke/docs/on-
prem/archive/1.1/beta-1.0/how-to/administration/upgrading-a-cluster) to future
beta versions.

**FEATURE:**

[ Anthos Config Management ](/anthos-config-management/docs) version 0.11.6 is
now available.

**FEATURE:**

Stackdriver Logging is now enabled on each node. By default, the logging agent
replicates logs to your GCP project for only control plane services, cluster
API, vSphere controller, Calico, BIG-IP controller, Envoy proxy, Connect,
Anthos Config Management, Prometheus and Grafana services, Istio control
plane, and Docker. Application container logs are excluded by default, but can
be optionally enabled.

**FEATURE:**

Stackdriver Prometheus Sidecar captures metrics for the same components as the
logging agent.

**FEATURE:**

[ Kubernetes Network Policies ](https://kubernetes.io/docs/concepts/services-
networking/network-policies/) are now supported.

###  Changes

**CHANGED:**

You can now update IP blocks in the cluster specification to expand the IP
range for a given cluster.

**CHANGED:**

If clusters you installed during alpha were disconnected from Google after
beta, you might need to connect them again. Refer to [ Manually registering a
user cluster. ](/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/registering-a-user-cluster)

**CHANGED:**

[ Getting started ](/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/getting-started) has been updated with steps for activating
your service account and running ` gkectl prepare ` .

**CHANGED:**

` gkectl diagnose snapshot ` now only collects configuration data and excludes
logs. This tool is used to capture details of your environment prior to
opening a support case.

**CHANGED:**

Support for optional SNAT pool name configuration for F5 BIG-IP at cluster-
creation time. This can be used to configure "--vs-snat-pool-name" value on [
F5 BIG-IP controller ](https://clouddocs.f5.com/products/connectors/k8s-bigip-
ctlr/v1.8/) .

**CHANGED:**

You now need to provide a VIP for add-ons that run in the admin cluster.

###  Fixes

**FIXED:**

Cluster resizing operations improved to prevent unintended node deletion.

##  February 7, 2019

GKE on-prem alpha version 1.3 is now available. This release includes the
following changes:

###  New Features

**FEATURE:**

During installation, you can now provide YAML files with ` nodeip ` blocks to
configure static IPAM.

###  Changes

**CHANGED:**

You now need to provision a 100GB disk in vSphere Datastore. GKE on-prem uses
the disk to store some of its vital data, such as etcd. See [ System
requirements ](/anthos/gke/docs/on-prem/requirements) .

**CHANGED:**

You can now only provide lowercase hostnames to ` nodeip ` blocks.

**CHANGED:**

GKE on-prem now enforces unique names for user clusters.

**CHANGED:**

Metrics endpoints and APIs that use Istio endpoints are now secured using mTLS
and role-based access control.

**CHANGED:**

External communication by Grafana is disabled.

**CHANGED:**

Improvements to Prometheus and Alertmanager health-checking.

**CHANGED:**

Prometheus now uses secured port for scraping metrics.

**CHANGED:**

Several updates to Grafana dashboards.

###  Known Issues

**ISSUE:**

If your vCenter user account uses a format like ` DOMAIN\USER ` , you might
need to escape the backslash ( ` DOMAIN\\USER ` ). Be sure to do this when
prompted to enter the user account during installation.

##  January 23, 2019

GKE on-prem alpha version 1.2.1 is now available. This release includes the
following changes:

###  New Features

**FEATURE:**

You can now use ` gkectl ` to [ delete admin clusters ](/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/deleting-an-admin-cluster) .

###  Changes

**CHANGED:**

` gkectl diagnose snapshot ` commands now allow you to specify nodes while
capturing snapshots of remote command results and files.

##  January 14, 2019

GKE on-prem alpha version 1.1.2 is now available. This release includes the
following changes:

###  New Features

**FEATURE:**

You can now use the ` gkectl prepare ` command to pull and push GKE on-prem's
container images, which deprecates the ` populate_registry.sh ` script.

**FEATURE:**

` gkectl prepare ` now prompts you to enter information about your vSphere
cluster and resource pool.

**FEATURE:**

You can now use the ` gkectl create ` command to create and add user clusters
to existing admin control planes by passing in an existing kubeconfig file
when prompted during cluster creation.

**FEATURE:**

You can now pass in a Ingress TLS Secret for admin and user clusters at
cluster creation time. You will see the following new prompt:

` Do you want to use TLS for Admin Control Plane/User Cluster ingress? `

Providing the TLS Secret and certs allows ` gkectl ` to set up the Ingress
TLS. HTTP is not automatically disabled with TLS installation.

###  Changes

**CHANGED:**

GKE on-prem now runs Kubernetes version **1.11.2-gke.19** .

**CHANGED:**

The default footprint for GKE on-prem has changed:

  * Minimum memory requirement for user cluster nodes is now 8192M. 

**CHANGED:**

GKE on-prem now runs minikube version **0.28.0** .

**CHANGED:**

GKE Policy Management has been upgraded to version **0.11.1** .

**CHANGED:**

` gkectl ` no longer prompts you to provide a proxy configuration by default.

**CHANGED:**

There are three new ConfigMap resources in the user cluster namespace: `
cluster-api-etcd-metrics-config ` , ` kube-etcd-metrics-config ` , and ` kube-
apiserver-config ` . GKE on-prem uses these files to quickly bootstrap the
metrics proxy container.

**CHANGED:**

kube-apiserver events now live in their own etcd. You can see kube-etcd-events
in your user cluster's namespace.

**CHANGED:**

Cluster API controllers now use leader election.

**CHANGED:**

vSphere credentials are now pulled from credential files.

**CHANGED:**

` gkectl diagnose ` commands now work with both admin and user clusters.

**CHANGED:**

` gkectl diagnose snapshot ` can now take snapshots of remote files on the
node, results of remote commands on the nodes, and Prometheus queries.

**CHANGED:**

` gkectl diagnose snapshot ` can now take snapshots in multiple parallel
threads.

**CHANGED:**

` gkectl diagnose snapshot ` now allows you to specify words to be excluded
from the snapshot results.

###  Fixes

**FIXED:**

Fixed issues with minikube caching that caused unexpected network calls.

**FIXED:**

Fixed an issue with pulling F5 BIG-IP credentials. Credentials are now read
from a credentials file instead of using environment variables.

###  Known Issues

**ISSUE:**

You might encounter the following [ ` govmomi `
](https://github.com/vmware/govmomi) warning when you run ` gkectl prepare ` :

` Warning: Line 102: Unable to parse 'enableMPTSupport' for attribute 'key' on
element 'Config' `

**ISSUE:**

Resizing user clusters can cause inadvertent node deletion or recreation.

**ISSUE:**

PersistentVolumes can fail to mount, producing the error ` devicePath is empty
` . As a workaround, delete and re-create the associated
PersistentVolumeClaim.

**ISSUE:**

Resizing IPAM address blocks if using static IP allocation for nodes, is not
supported in alpha. To work around this, consider allocating more IP addresses
than you currently need.

**ISSUE:**

On slow disks, VM creation can timeout and cause deployments to fail. If this
occurs, delete all resources and try again.

##  December 19, 2018

GKE on-prem alpha 1.0.4 is now available. This release includes the following
changes:

###  Fixes

**FIXED:**

The vulnerability caused by [ CVE-2018-1002105
](https://github.com/kubernetes/kubernetes/issues/71411) has been patched.

##  November 30, 2018

GKE on-prem alpha 1.0 is now available. The following changes are included in
this release:

###  Changes

**CHANGED:**

GKE on-prem alpha 1.0 runs Kubernetes 1.11.

**CHANGED:**

The default footprint for GKE on-prem has changed:

  * The admin control plane runs three nodes, which use 4 CPUs and 16GB memory. 
  * The user control plane runs one node that uses 4 CPUs 16GB memory. 
  * User clusters run a minimum of three nodes, which use 4 CPUs and 16GB memory. 

**CHANGED:**

Support for high-availability Prometheus setup.

**CHANGED:**

Support for custom Alert Manager configuration.

**CHANGED:**

Prometheus upgraded from **2.3.2** to **2.4.3** .

**CHANGED:**

Grafana upgraded from **5.0.4** to **5.3.4** .

**CHANGED:**

kube-state-metrics upgraded from **1.3.1** to **1.4.0** .

**CHANGED:**

Alert Manager upgraded from **1.14.0** to **1.15.2** .

**CHANGED:**

node_exporter upgraded from **1.15.2** to **1.16.0** .

###  Fixes

**FIXED:**

The vulnerability caused by [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) has been patched.

###  Known Issues

**ISSUE:**

PersistentVolumes can fail to mount, producing the error ` devicePath is empty
` . As a workaround, delete and re-create the associated
PersistentVolumeClaim.

**ISSUE:**

Resizing IPAM address blocks if using static IP allocation for nodes, is not
supported in alpha. To work around this, consider allocating more IP addresses
than you currently need.

**ISSUE:**

GKE on-prem alpha 1.0 does not yet pass all conformance tests.

**ISSUE:**

Only one user cluster per admin cluster can be created. To create additional
user clusters, create another admin cluster.

##  October 31, 2018

GKE on-prem EAP 2.1 is now available. The following changes are included in
this release:

###  Changes

**CHANGED:**

When you create admin and user clusters at the same time, you can now re-use
the admin cluster's F5 BIG-IP credentials to create the user cluster. Also,
the CLI now requires that BIG-IP credentials be provided; this requirement
cannot be skipped using ` --dry-run ` .

**CHANGED:**

F5 BIG-IP controller upgraded to use the latest OSS version, 1.7.0.

**CHANGED:**

To improve stability for slow vSphere machines, cluster machine creation
timeout is now 15 minutes (previously five minutes).

##  October 17, 2018

GKE on-prem EAP 2.0 is now available. The following changes are included in
this release:

###  Changes

**CHANGED:**

Support for GKE Connect.

**CHANGED:**

Support for Monitoring.

**CHANGED:**

Support for installation using private registries.

**CHANGED:**

Support for front-ending the L7 load-balancer as a L4 VIP on F5 BIG-IP.

**CHANGED:**

Support for static IP allocation for nodes during cluster bootstrap.

###  Known Issues

**ISSUE:**

Only one user cluster per admin cluster can be created. To create additional
user clusters, create another admin cluster.

**ISSUE:**

Cluster upgrades are not supported in EAP 2.0.

**ISSUE:**

On slow disks, VM creation can timeout and cause deployments to fail. If this
occurs, delete all resources and try again.

**ISSUE:**

As part of the cluster bootstrapping process, a short-lived minikube instance
is run. The minikube version used has security vulnerability [
CVE-2018-1002103 ](https://github.com/kubernetes/minikube/issues/3208) .

