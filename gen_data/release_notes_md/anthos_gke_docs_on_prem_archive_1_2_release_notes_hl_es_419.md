#  Notas de la versión

En esta página, se documentan las actualizaciones de producción de Anthos GKE
On-Prem. Puedes revisar esta página de forma periódica para ver anuncios sobre
características nuevas o actualizadas, correcciones de errores, problemas
conocidos y funciones obsoletas.

También consulta lo siguiente:

  * [ Descargas ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=es-419)
  * [ Control de versiones y actualizaciones ](https://cloud.google.com/anthos/gke/docs/on-prem/versioning-and-upgrades?hl=es-419)
  * [ Actualizar GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/how-to/upgrading?hl=es-419)

Puedes ver las últimas actualizaciones de productos de todo Google Cloud en la
página [ Notas de la versión de Google Cloud
](https://cloud.google.com/release-notes?hl=es-419) .

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , o agrega
directamente la URL del feed: ` https://cloud.google.com/feeds/gkeonprem-
release-notes.xml `

##  August 20, 2020

**FEATURE:**

Anthos GKE on-prem 1.4.2-gke.3 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.comanthos/gke/docs/on-prem/how-
to/upgrading) . GKE on-prem 1.4.2-gke.3 clusters run on Kubernetes
1.16.11-gke.11.

**FEATURE:**

GPU support (beta solution in collaboration with Nvidia)

[ In partnership with Nvidia
](https://cloud.google.com/blog/products/compute/anthos-supports-nvidia-
gpus?hl=es-419) , users can now manually attach a GPU to a worker node VM to
run GPU workloads. This requires using the [ open source Nvidia GPU operator
](https://github.com/NVIDIA/gpu-operator) .

**Note:** Manually attached GPUs do not persist through node lifecycle events.
You must manually re-attach them. This is a beta solution and can be used for
evaluation and proof of concept.

**CHANGED:**

The Ubuntu image is upgraded to include the newest packages.

**CHANGED:**

` gkectl delete loadbalancer ` is updated to support the new version of
configuration files for admin and user clusters.

**FIXED:**

**Fixes:**

  * Resolved a few incorrect Kubelet Metrics' names collected by Prometheus. 
  * Updated restarting machines process during admin cluster upgrade to make the upgrade process more resilient to transient connection issues. 
  * Resolved a preflight check OS image validation error when using a non-default vSphere folder for cluster creation; the OS image template is expected to be in that folder. 
  * Resolved a ` gkectl upgrade loadbalancer ` issue to avoid validating the upgraded SeesawGroup. This fix lets the existing SeesawGroup config be updated without negatively affecting the upgrade process. 
  * Resolved an issue where ClientConfig CRD is deleted when the upgrade to the latest version is run multiple times. 
  * Resolved a ` gkectl update credentials vsphere ` issue where the vsphere-metrics-exporter was using the old credentials even after updating the credentials. 
  * Resolved an issue where the VIP preflight check reported a user cluster add-on load balancer IP false positive. 
  * Fixed ` gkeadm ` updating config after upgrading on Windows, specifically for the ` gkeOnPremVersion ` and ` bundlePath ` fields. 
  * Automatically mount the data disk after rebooting on admin workstations created using ` gkeadm ` 1.4.0 and later. 
  * Reverted thin disk provisioning change for boot disks in 1.4.0 and 1.4.1 on all normal (excludes test VMs) cluster nodes. 
  * Removed vCenter Server access check from user cluster nodes. 

##  July 30, 2020

**FEATURE:**

Anthos GKE on-prem 1.3.3-gke.0 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading?hl=es-419) . GKE on-prem 1.3.3-gke.0 clusters run on Kubernetes
1.15.12-gke.9.

**FIXED:**

**Fixes:**

  * Fixed [ CVE-2020-8559 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559) described in [ Security bulletins ](https://cloud.google.com/anthos/gke/docs/on-prem/security-bulletins?hl=es-419#gcp-2020-009) . 
  * Updated the git-sync image to fix security vulnerability [ CVE-2019-5482 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5482) . 
  * Updated the kindest/node image to fix security vulnerability [ CVE-2020-13777 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13777) . 

##  July 23, 2020

**FEATURE:**

Anthos GKE on-prem 1.4.1-gke.1 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading?hl=es-419) . GKE on-prem 1.4.1-gke.1 clusters run on Kubernetes
1.16.9-gke.14.

**FEATURE:**

**Anthos Identity Service LDAP authentication is now available in Alpha for
GKE on-prem**

Contact support if you are interested in a trial of the LDAP authentication
feature in GKE on-prem.

**FEATURE:**

**Support for F5 BIG-IP load balancer credentials update**

This preview release enables customers to manage and update the F5 BIG-IP load
balancer credentials by using the ` gkectl update credentials f5bigip `
command.

**CHANGED:**

**Functionality changes:**

  * The Ubuntu image is upgraded to include the newest packages. 
  * Preflight checks are updated to validate that the ` gkectl ` version matches the target cluster version for cluster creation and upgrade. 
  * Preflight checks are updated to validate the Window OS version used for running ` gkeadm ` . The ` gkeadm ` command-line tool is only available for Linux, Windows 10, and Windows Server 2019. 
  * ` gkeadm ` is updated to populate ` network.vCenter.networkName ` in both [ admin cluster ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/admin-cluster-configuration-file?hl=es-419) and [ user cluster ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/user-cluster-configuration-file?hl=es-419) configuration files. 

**FIXED:**

**Fixes:**

  * Removed the static IP used by admin workstation after upgrade from ` ~/.ssh/known_hosts ` to avoid manual workaround. 
  * Resolved a known issue that ` network.vCenter.networkName ` is not populated in the user cluster configuration file during user cluster creation. 
  * Resolved a user cluster upgrade–related issue to only wait for the machines and pods in the same namespace within the cluster to be ready to complete the cluster upgrade. 
  * Updated the default value for ` ingressHTTPNodePort ` and ` ingressHTTPSNodePort ` in the ` loadBalancer.manualLB ` section of the [ admin cluster configuration ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/admin-cluster-configuration-file?hl=es-419) file. 
  * Fixed [ CVE-2020-8558 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8558) and [ CVE-2020-8559 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559) described in [ Security bulletins ](https://cloud.google.com/anthos/gke/docs/on-prem/security-bulletins?hl=es-419#gcp-2020-009) . 
  * Logging and monitoring: Resolved an issue that stackdriver-log-forwarder was not scheduled on the master node on the admin cluster. 
  * Resolved the following known issues published in the 1.4.0 release notes: 
    * If a user cluster is created without any node pool named the same as the cluster, managing the node pools using ` gkectl update cluster ` would fail. To avoid this issue, when creating a user cluster, you need to name one node pool the same as the cluster. 
    * The ` gkectl ` command might exit with panic when converting config from "/path/to/config.yaml" to v1 config files. When that occurs, you can resolve the issue by removing the unused bundled load balancer section ("loadbalancerconfig") in the config file. 
    * When using gkeadm to upgrade an admin workstation on Windows, the info file filled out from this template needs to have the line endings converted to use Unix line endings (LF) instead of Windows line endings (CRLF). You can use Notepad++ to convert the line endings. 
    * When running a preflight check for ` config.yaml ` that contains both ` admincluster ` and ` usercluster ` sections, the "data disk" check in the "user cluster vCenter" category might fail with the message: ` [FAILURE] Data Disk: Data disk is not in a folder. Use a data disk in a folder when using vSAN datastore. ` User clusters don't use data disks, and it's safe to ignore the failure. 
    * When upgrading the admin cluster, the preflight check for the user cluster OS image validation will fail. The user cluster OS image is not used in this case, and it's safe to ignore the "User Cluster OS Image Exists" failure in this case. 
    * User cluster creation and upgrade might be stuck with the error: ` Failed to update machine status: no matches for kind "Machine" in version "cluster.k8s.io/v1alpha1". ` To resolve this, you need to delete the clusterapi pod in the user cluster namespace in the admin cluster. 

**ISSUE:**

**Known issues:**

  * During reboots, the data disk is not remounted on the admin workstation when using GKE on-prem 1.4.0 or 1.4.1 because the startup script is not run after the initial creation. To resolve this, you can run ` sudo mount /dev/sdb1 /home/ubuntu ` . 

##  June 25, 2020

**FEATURE:**

Anthos GKE on-prem 1.4.0-gke.13 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading?hl=es-419) . GKE on-prem 1.4.0-gke.13 clusters run on Kubernetes
1.16.8-gke.6.

**FEATURE:**

**Updated to Kubernetes 1.16:**

  * Please note that Kubernetes 1.16 has deprecated some of its APIs. For more information, see [ Kubernetes 1.16 deprecated APIs ](https://cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-16?hl=es-419) . 

**FEATURE:**

**Simplified upgrade:**

  * This release provides a simplified upgrade experience via the following changes: 

    * Automatically migrate information from the previous version of admin workstation using ` gkeadm ` . 
    * Extend preflight checks to better prepare for upgrades. 
    * Support skip version upgrade to enable users to upgrade the cluster from any patch release of a minor release to any patch release of the next minor release. For more information about the detailed upgrade procedure and limitations, see [ upgrading GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=es-419) . 
    * The [ alternate upgrade scenario for Common Vulnerabilities and Exposures ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=es-419) has been deprecated. All upgrades starting with version 1.3.2 need to upgrade the entire admin workstation. 
    * The bundled load balancer is now automatically upgraded during cluster upgrade. 

**FEATURE:**

**Improved installation and cluster configuration:**

  * The user cluster [ node pools ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/user-cluster-basic?hl=es-419#nodepoolsname) feature is now generally available. 
  * This release improves the installation experience via the following changes: 

    * Supports ` gkeadm ` for Windows OS. 
    * Introduces a standalone command for creating admin clusters. 
  * Introduce a new version of configuration files to separate admin and user cluster configurations and commands. This is designed to provide a consistent user experience and better configuration management. 

**FEATURE:**

**Improved disaster recovery capabilities:**

  * This release provides enhanced disaster recovery functionality to [ support backup and restore ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/backing-up?hl=es-419#user_cluster_backups) HA user cluster with etcd. 
  * This release also provides a manual process to recover a single etcd replica failure in a HA cluster without any data loss. 

**FEATURE:**

**Enhanced monitoring with Cloud Monitoring (formerly Stackdriver):**

  * This release provides better product monitoring and resource usage management via the following changes: 

    * Introduces a [ default monitoring dashboard ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/logging-and-monitoring?hl=es-419#dashboards) . 
    * Enables vSphere resource metrics collection by default. 
  * Ubuntu Image now conforms with PCI DSS, NIST Baseline High, and DoD SRG IL2 compliance configurations. 

**CHANGED:**

**Functionality changes:**

  * Enabled Horizontal Pod Autoscaler (HPA) for the Istio ingress gateway. 
  * Removed ingress controller from admin cluster. 
  * Consolidated sysctl configs with Google Kubernetes Engine. 
  * Added etcd defrag pod in admin cluster and user cluster, which will be responsible for monitoring etcd's database size and defragmenting it as needed. This helps reclaim etcd database size and recover etcd when its disk space is exceeded. 

**CHANGED:**

**Support for a vSphere folder (Preview):**

  * This release allows customers to install GKE on-prem in a vSphere folder, reducing the scope of the permission required for the vSphere user. 

**CHANGED:**

**Improved scale:**

  * This release improves the cluster scalability by supporting [ a maximum of 10 instead of 5 user clusters for each admin cluster ](https://cloud.google.com/anthos/gke/docs/on-prem/quotas?hl=es-419) . 

**FIXED:**

**Fixes:**

  * Fixed the issue of the user cluster's Kubernetes API server not being able to connect to kube-etcd after admin nodes and user cluster master reboot. In previous versions, kube-dns in admin clusters was configured through kubeadm. In 1.4, this configuration is moved from kubeadm to bundle, which enables deploying two kube-dns replicas on two admin nodes. As a result, a single admin node reboot/failure won't disrupt user cluster API access. 
  * Fixed the issue that controllers such as calico-typha can't be scheduled on an admin cluster master node, when the admin cluster master node is under disk pressure. 
  * Resolved pods failure with MatchNodeSelector on admin cluster master after node reboot or kubelet restart. 
  * Tuned etcd quota limit settings based on the etcd data disk size and the settings in GKE Classic. 

**ISSUE:**

**Known issues:**

  * If a user cluster is created without any node pool named the same as the cluster, managing the node pools using ` gkectl update cluster ` would fail. To avoid this issue, when creating a user cluster, you need to name one node pool the same as the cluster. 
  * The ` gkectl ` command might exit with panic when converting config from "/path/to/config.yaml" to v1 config files. When that occurs, you can resolve the issue by removing the unused bundled load balancer section ("loadbalancerconfig") in the config file. 
  * When using gkeadm to upgrade an admin workstation on Windows, the info file filled out from this template needs to have the line endings converted to use Unix line endings (LF) instead of Windows line endings (CRLF). You can use Notepad++ to convert the line endings. 
  * After upgrading an admin workstation with a static IP using gkeadm, you need to run ` ssh-keygen -R <admin-workstation-ip> ` to remove the IP from the known hosts, because the host identification changed after VM re-creation. 
  * We have added Horizontal Pod Autoscaler for istio-ingress and istio-pilot deployments. HPA can scale up unnecessarily for istio-ingress and istio-pilot deployments during cluster upgrades. This happens because the metrics server is not able to report usage of some pods (newly created and terminating; for more information, see [ this Kubernetes issue ](https://github.com/kubernetes/kubernetes/issues/72775) ). No actions are needed; scale down will happen five minutes after the upgrade finishes. 
  * When running a preflight check for ` config.yaml ` that contains both ` admincluster ` and ` usercluster ` sections, the "data disk" check in the "user cluster vCenter" category might fail with the message: ` [FAILURE] Data Disk: Data disk is not in a folder. Use a data disk in a folder when using vSAN datastore. ` User clusters don't use data disks, and it's safe to ignore the failure. 
  * When upgrading the admin cluster, the preflight check for the user cluster OS image validation will fail. The user cluster OS image is not used in this case, and it's safe to ignore the "User Cluster OS Image Exists" failure in this case. 
  * A Calico-node pod might be stuck in an unready state after node IP changes. To resolve this issue, you need to delete any unready Calico-node pods. 
  * The BIG-IP controller might fail to update F5 VIP after any admin cluster master IP changes. To resolve this, you need to use the admin cluster master node IP in kubeconfig and delete the bigip-controller pod from the admin master. 
  * The stackdriver-prometheus-k8s pod could enter a crashloop after host failure. To resolve this, you need to remove any corrupted PersistentVolumes that the stackdriver-prometheus-k8s pod uses. 
  * After node IP change, pods running with hostNetwork don't get podIP corrected until Kubelet restarts. To resolve this, you need to restart Kubelet or delete those pods using previous IPs. 
  * An admin cluster fails after any admin cluster master node IP address changes. To avoid this, you should avoid changing the admin master IP address if possible by using a static IP or a non-expired DHCP lease instead. If you encounter this issue and need further assistance, please contact Google Support. 
  * User cluster upgrade might be stuck with the error: ` Failed to update machine status: no matches for kind "Machine" in version "cluster.k8s.io/v1alpha1". ` To resolve this, you need to delete the clusterapi pod in the user cluster namespace in the admin cluster. 

**ISSUE:**

If your vSphere environment has fewer than three hosts, user cluster upgrade
might fail. To resolve this, you need to disable ` antiAffinityGroups ` in the
cluster config before upgrading the user cluster. For v1 config, please set `
antiAffinityGroups.enabled = false ` ; for v0 config, please set `
usercluster.antiaffinitygroups.enabled = false ` .

**Note:** Disabling ` antiAffinityGroups ` in the cluster config during
upgrade is only allowed for the 1.3.2 to 1.4. _x_ upgrade to resolve the
upgrade issue; the support might be removed in the future.

##  May 21, 2020

**FEATURE:**

Workload Identity is now available in Alpha for GKE on-prem. Please contact
support if you are interested in a trial of Workload Identity in GKE on-prem.

**CHANGED:**

Preflight check for VM internet and Docker Registry access validation is
updated.

**CHANGED:**

Preflight check for internet validation is updated to not follow redirect. If
your organization requires outbound traffic to pass through a proxy server,
you no longer need to whitelist the following addresses in your proxy server:

  * console.cloud.google.com 
  * cloud.google.com 

**CHANGED:**

The Ubuntu image is upgraded to include the newest packages.

**FIXED:**

Upgraded the Istio image to version 1.4.7 to fix a security vulnerability.

**FIXED:**

Some ConfigMaps in the admin cluster were refactored to Secrets to allow for
more granular access control of sensitive configuration data.

##  April 23, 2020

**CHANGED:**

Preflight check in ` gkeadm ` for access to the Cloud Storage bucket that
holds the admin workstation OVA.

**CHANGED:**

Preflight check for internet access includes additional URL `
www.googleapis.com ` .

**CHANGED:**

Preflight check for test VM DNS availability.

**CHANGED:**

Preflight check for test VM NTP availability.

**CHANGED:**

Preflight check for test VM F5 access.

**CHANGED:**

Before downloading and creating VM templates from OVAs, GKE on-prem checks if
the VM template already exists in vCenter.

**CHANGED:**

Rename ` gkeadm ` ’s automatically created service accounts.

**CHANGED:**

OVA download displays download progress.

**CHANGED:**

` gkeadm ` prepopulates ` bundlepath ` in the seed config on the admin
workstation.

**CHANGED:**

Fix for Docker failed DNS resolution on admin workstation at startup.

**CHANGED:**

Admin workstation provisioned by ` gkeadm ` uses thin disk provisioning.

**CHANGED:**

Improved user cluster Istio ingress gateway reliability.

**CHANGED:**

Ubuntu image is upgraded to include newest packages.

**CHANGED:**

Update the vCenter credentials for your clusters using the preview command [ `
gkectl update credentials vsphere `
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/updating-cluster-
credentials?hl=es-419) .

**FIXED:**

The ` gkeadm ` configuration file, ` admin-ws-config.yaml ` , accepts paths
that are prefixed with ` ~/ ` for the Certificate Authority (CA) certificate.

**FIXED:**

Test VMs wait until the network is ready before starting preflight checks.

**FIXED:**

Improve the error message in preflight check failure for F5 BIG-IP.

**FIXED:**

Skip VIP check in preflight check in manual load balancing mode.

**FIXED:**

Upgraded Calico to version 3.8.8 to fix several security vulnerabilities.

**FIXED:**

Upgraded F5 BIG-IP Controller Docker image to version 1.14.0 to fix a security
vulnerability.

**FIXED:**

Fixed ` gkeadm ` admin workstation ` gcloud ` proxy username and password
configuration.

**FIXED:**

Fixed the bug that was preventing ` gkectl check-config ` from automatically
using the proxy that you set in your configuration file when running the full
set of [ preflight validation checks
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/preflight-
checks?hl=es-419) with any GKE on-prem [ download image
](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=es-419#bundle-
latest) .

**FIXED:**

Fixed an admin workstation upgrade failure when the upgrade process was unable
to retrieve SSH keys, which would cause a Golang segmentation fault.

##  April 01, 2020

**ISSUE:**

When upgrading from version 1.2.2 to 1.3.0 by using the Bundle download in the
[ alternate upgrade method ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/upgrading?hl=es-419#alternate_upgrade_scenario) , a timeout might
occur that will cause your user cluster upgrade to fail. To avoid this issue,
you must perform the [ full upgrade process
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=es-419)
that includes upgrading your admin workstation with the OVA file.

##  March 23, 2020

**FEATURE:**

Anthos GKE on-prem 1.3.0-gke.16 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading?hl=es-419) .

GKE on-prem 1.3.0-gke.16 clusters run on Kubernetes 1.15.7-gke.32.

**FEATURE:**

A new installer helps you [ create and prepare the admin workstation
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/admin-
workstation?hl=es-419) .

**FEATURE:**

Support for [ vSAN ](https://docs.vmware.com/en/VMware-vSAN/index.html)
datastore on your admin and user clusters.

**FEATURE:**

In bundled load balancing mode, GKE on-prem provides and manages the [ Seesaw
load balancer ](https://github.com/google/seesaw) .

**FEATURE:**

The [ Authentication Plugin for Anthos
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/oidc?hl=es-419) has
been integrated into and replaced with the Google Cloud command-line
interface, which improves the authentication process and provides the user
consent flow through ` gcloud ` commands.

**FEATURE:**

Added support for up to [ 100 nodes per user cluster
](https://cloud.google.com/anthos/gke/docs/on-prem/quotas?hl=es-419) .

**FEATURE:**

The Cluster CA now signs the TLS certificates that the Kubelet API serves, and
the TLS certificates are auto-rotated.

**FEATURE:**

vSphere credential rotation is enabled. Users can now use Solution User
Certificates to authenticate to GKE deployed on-prem.

**FEATURE:**

` gkectl ` automatically uses the proxy URL from ` config.yaml ` to configure
the proxy on the admin workstation.

**FEATURE:**

Preview Feature: Introducing User cluster Nodepools. A _node pool_ is a group
of nodes within a cluster that all have the same configuration. In GKE on-prem
1.3.0, node pools are a preview feature in the user clusters. This feature
lets users create multiple node pools in a cluster, and update them as needed.

**CHANGED:**

The metric ` kubelet_containers_per_pod_count ` is changed to a [ histogram
metric ](https://prometheus.io/docs/concepts/metric_types/#histogram) .

**FIXED:**

Fixed an issue in the vSphere storage plugin that prevented vSphere storage
policies from working. [ This is an example
](https://github.com/kubernetes/examples/blob/master/staging/volumes/vsphere/vsphere-
volume-spbm-policy.yaml) of how you might use this feature.

**ISSUE:**

Prometheus + Grafana: two graphs on the **Machine** dashboard don't work
because of missing metrics: **Disk Usage** and **Disk Available** .

**ISSUE:**

All OOM events for containers trigger a SystemOOM event, even if they are
container/pod OOM events. To check whether an OOM is actually a SystemOOM,
check the kernel log for a message ` oom-kill:… ` . If ` oom_memcg=/ `
(instead of ` oom_memcg=/kubepods/… ` ), then it's a SystemOOM. If it's not a
SystemOOM, it's safe to ignore.

**ISSUE:**

**Affected versions: 1.3.0-gke.16**

If you configured a proxy in the ` config.yaml ` and also used a bundle other
than the full bundle ( [ static IP
](http://cloud.google.com/anthos/gke/docs/on-prem/how-to/install-static-
ips?hl=es-419#bundlepath) | [ DHCP
](http://cloud.google.com/anthos/gke/docs/on-prem/how-to/install-
dhcp?hl=es-419#bundlepath) ), you must append the ` --fast ` flag to run `
gkectl check-config ` . For example: ` gkectl check-config --config
config.yaml --fast ` .

**ISSUE:**

Running the 1.3 version of the [ ` gkectl diagnose `
](http://cloud.google.com/anthos/gke/docs/on-
prem/reference/gkectl/diagnose?hl=es-419) command might fail if your clusters:

  * Are older than Anthos GKE on-prem version 1.3. 
  * Include manually installed add-ons in the ` kube-system ` namespace. 

##  February 21, 2020

**FEATURE:**

GKE on-prem version 1.2.2-gke.2 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading?hl=es-419) .

**CHANGED:**

Improved ` gkectl check-config ` to validate any valid Google Cloud service
accounts regardless of whether an IAM role is set.

**CHANGED:**

You need to use vSphere provider version 1.15 when using [ Terraform to create
the admin workstation ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/admin-workstation?hl=es-419#copy_terraform) . vSphere provider version 1.16
introduces [ breaking changes ](https://github.com/terraform-
providers/terraform-provider-vsphere/issues/966) that would affect all Anthos
versions.

**CHANGED:**

Skip the preflight check when resuming cluster creation/upgrade.

**FIXED:**

Resolved a known issue of cluster upgrade when using a vSAN datastore
associated with a GKE on-prem version before 1.2

**FIXED:**

Resolved the following warning when uploading an OS image with the [
enableMPTSupport ](https://www.vmware.com/support/orchestrator/doc/vro-
vsphere65-api/html/VcVirtualMachineVideoCard.html) configuration flag set.
This flag is used to indicate whether the virtual video card supports mediated
passthrough.

` Warning: Line 102: Unable to parse 'enableMPTSupport' for attribute 'key' on
element 'Config'. `

**FIXED:**

Fixed the BigQuery API service name for the preflight check service
requirements validation.

**FIXED:**

Fixed the preflight check to correctly validate the default resource pool in
the case where the ` resourcepool ` field in the GKE on-prem configuration
file is empty.

**FIXED:**

Fixed a comment about the ` workernode.replicas ` field in the GKE on-prem [
configuration file ](https://cloud.google.com/anthos/gke/docs/on-
prem/reference/config?hl=es-419) to say that the minimum number of worker
nodes is three.

**FIXED:**

Fixed ` gktctl prepare ` to skip checking the data disk.

**FIXED:**

Fixed ` gktctl check-config ` so that it cleans up F5 BIG-IP resources on
exit.

##  January 31, 2020

**FEATURE:**

GKE on-prem version 1.2.1-gke.4 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading?hl=es-419) .

This patch version includes the following changes:

**FEATURE:**

Adds ` searchdomainsfordns ` field to static IPs host configuration file. `
searchdomainsfordns ` is an array of DNS search domains to use in the cluster.
These domains are used as part of a domain search list.

**FEATURE:**

Adds a [ preflight check ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/preflight-checks?hl=es-419#list) that validates an NTP server is
available.

**FEATURE:**

` gkectl check-config ` now automatically uploads GKE on-prem's node OS image
to vSphere. You no longer need to run ` gkectl prepare ` before ` gkectl
check-config ` .

**FEATURE:**

Adds a ` --cleanup ` flag for ` gkectl check-config ` . The flag's default
value is ` true ` .

Passing in ` --cleanup=false ` preserves the test VM and associated SSH keys
that ` gkectl check-config ` creates for its preflight checks. Preserving the
VM can be helpful for debugging.

**FIXED:**

Fixes a [ known issue ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/preflight-checks?hl=es-419#known_issue) from 1.2.0-gke.6 that prevented `
gkectl check-config ` from performing all of its validations against clusters
in nested resource pools or the default resource pool.

**FIXED:**

Fixes an issue that caused F5 BIG-IP VIP validation to fail due to timing out.
The timeout window for F5 BIG-IP VIP validation is now longer.

**FIXED:**

Fixes an issue that caused cluster upgrades to overwrite changes to add-on
configurations.

**FIXED:**

Fixes the [ known issue ](https://cloud.google.com/anthos/gke/docs/on-
prem/release-notes?hl=es-419#January_28_2020) from 1.2.0-gke.6 that affects
routing updates due to the route reflector configuration.

##  January 28, 2020

**ISSUE:**

**Affected versions:** 1.2.0-gke.6

In some cases, certain nodes in a user cluster fail to get routing updates
from the route reflector. Consequently Pods on a node may not be able to
communicate with Pods on other nodes. One possible symptom is a ` kube-dns `
resolution error.

To work around this issue, follow these steps to create a BGPPeer object in
your user cluster.

Save the following BGPPeer manifest as ` full-mesh.yaml ` :

    
    
    apiVersion: crd.projectcalico.org/v1
    kind: BGPPeer
    metadata:
      name: full-mesh
    spec:
      nodeSelector: "!has(route-reflector)"
      peerSelector: "!has(route-reflector)" 
    

Create the BGPPeer in your user cluster:

` kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] apply -f full-mesh.yaml `

Verify that the ` full-mesh ` BGPPeer was created:

` kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] get bgppeer `

The output shows ` full-mesh ` in the list of BGPPeers:

    
    
    NAME            AGE
      full-mesh       61s
      gke-group-1     3d21h
      ...
    

This issue will be fixed in version 1.2.1.

##  January 03, 2020

**ISSUE:**

**Affected versions:** 1.1.0-gke.6 and later

Starting with [ version 1.1.0-gke.6 ](https://cloud.google.com/gke-on-
prem/docs/release-notes?hl=es-419#september_26_2019) , the ` gkeconnect.proxy
` field is no longer in the GKE on-prem [ configuration file
](https://cloud.google.com/gke-on-prem/docs/reference/config?hl=es-419) .

If you include ` gkeconnect.proxy ` in the configuration file, the [ ` gkectl
check-config ` ](https://cloud.google.com/gke-on-prem/docs/how-to/preflight-
checks?hl=es-419) command can fail with this error:

    
    
    [FAILURE] Config: Could not parse config file: error unmarshaling JSON: 
    while decoding JSON: json: unknown field "proxy"
    

To correct this issue, remove ` gkeconnect.proxy ` from the configuration
file.

In versions prior to 1.1.0-gke.6, the Connect Agent used the proxy server
specified in ` gkeconnect.proxy ` . Starting with version 1.1.0-gke.6, the
Connect Agent uses the proxy server specified in the global ` proxy ` field.

##  December 20, 2019

**CHANGED:**

**Warning:** If you installed GKE on-prem versions before 1.2, and you use a
vSAN datastore, you should contact Google Support before attempting an upgrade
to 1.2.0-gke.6.

GKE on-prem version 1.2.0-gke.6 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.com/gke-on-prem/docs/how-
to/upgrading?hl=es-419) .

This minor version includes the following changes:

**FEATURE:**

The default Kubernetes version for cluster nodes is now version 1.14.7-gke.24
(previously 1.13.7-gke.20).

**FEATURE:**

GKE on-prem now supports vSphere 6.7 Update 3. [ Read its release notes.
](https://docs.vmware.com/en/VMware-vSphere/6.7/rn/vsphere-vcenter-
server-67u3-release-notes.html)

**FEATURE:**

GKE on-prem now supports [ VMware NSX-T version 2.4.2
](https://cloud.google.com/gke-on-
prem/docs/concepts/networking?hl=es-419#support_for_vmware_nsx-t) .

**FEATURE:**

Any user cluster, even your first use cluster, can now use a datastore that is
separate from the admin cluster's datastore. If you specify a separate
datastore for a user cluster, the user cluster nodes, PersistentVolumes (PVs)
for the user cluster nodes, user control plane VMs, and PVs for the user
control plane VMs all use the separate datastore.

**FEATURE:**

Expanded [ preflight checks ](https://cloud.google.com/gke-on-prem/docs/how-
to/preflight-checks?hl=es-419) for validating your GKE on-prem configuration
file before your create your clusters. These new checks can validate that your
Google Cloud project, vSphere network, and other elements of your environment
are correctly configured.

**FEATURE:**

Published [ basic installation ](https://cloud.google.com/gke-on-
prem/docs/how-to/install-overview-basic?hl=es-419) workflow. This workflow
offers a simplified workflow for quickly installing GKE on-prem using static
IPs.

**FEATURE:**

Published guidelines for [ installing Container Storage Interface
](https://cloud.google.com/gke-on-prem/docs/how-to/install-csi-
driver?hl=es-419) (CSI) drivers. CSI enables using storage devices not
natively supported by Kubernetes.

**FEATURE:**

Updated documentation for [ authenticating using OpenID Connect (OIDC)
](https://cloud.google.com/gke-on-prem/docs/how-to/oidc?hl=es-419) with the
Anthos Plugin for Kubectl. GKE on-prem's OIDC integration is now generally
available.

**CHANGED:**

From the admin workstation, gcloud now requires that you log in to gcloud with
a Google Cloud user account. The user account should have at least the Viewer
IAM role in all Google Cloud projects associated with your clusters.

**CHANGED:**

You can now create admin and user clusters separately from one another.

**FIXED:**

Fixes an issue that prevented resuming cluster creation for HA user clusters.

**ISSUE:**

**Affected versions:** 1.1.0-gke.6, 1.2.0-gke.6

The ` stackdriver.proxyconfigsecretname ` field was removed in version
1.1.0-gke.6. GKE on-prem's preflight checks will return an error if the field
is present in your configuration file.

To work around this, before you install or upgrade to 1.2.0-gke.6, delete the
` proxyconfigsecretname ` field from your configuration file.

**ISSUE:**

**Affected versions:** 1.2.0-6-gke.6

In user clusters, Prometheus and Grafana get automatically disabled during
upgrade. However, the configuration and metrics data are not lost. In admin
clusters, Prometheus and Grafana stay enabled.

To work around this issue, after the upgrade, open ` monitoring-sample ` for
editing and set ` enablePrometheus ` to ` true ` :

1\. ` kubectl edit monitoring --kubeconfig [USER_CLUSTER_KUBECONFIG] \ -n
kube-system monitoring-sample `

2\. Set the field ` enablePrometheus ` to ` true ` .

**ISSUE:**

**Affected versions:** All versions

Before version 1.2.0-gke.6, a known issue prevents Stackdriver from updating
its configuration after cluster upgrades. Stackdriver still references an old
version, which prevents Stackdriver from receiving the latest features of its
telemetry pipeline. This issue can make it difficult for Google Support to
troubleshoot clusters.

After you upgrade clusters to 1.2.0-gke.6, run the following command against
admin and user clusters:

    
    
    kubectl --kubeconfig=[KUBECONFIG] \
    -n kube-system --type=json patch stackdrivers stackdriver \
    -p '[{"op":"remove","path":"/spec/version"}]'
    

where **[KUBECONFIG]** is the path to the cluster's kubeconfig file.

##  November 19, 2019

**FEATURE:**

GKE On-Prem version 1.1.2-gke.0 is now available. To download version
1.1.2-gke.0's OVA, ` gkectl ` , and upgrade bundle, see [ Downloads
](https://cloud.google.com/gke-on-prem/docs/downloads?hl=es-419#latest) .
Then, see [ Upgrading admin workstation ](https://cloud.google.com/gke-on-
prem/docs/how-to/upgrading?hl=es-419) and [ Upgrading clusters
](https://cloud.google.com/gke-on-prem/docs/how-to/upgrading?hl=es-419) .

This patch version includes the following changes:

**FEATURE:**

###  New Features

**FEATURE:**

Published [ Hardening your cluster ](https://cloud.google.com/gke-on-
prem/docs/how-to/security/hardening-your-cluster?hl=es-419) .

**FEATURE:**

Published [ Managing clusters ](https://cloud.google.com/gke-on-prem/docs/how-
to/administration/managing-clusters?hl=es-419) .

**FIXED:**

###  Fixes

**FIXED:**

Fixed the known issue from  November 5  .

**FIXED:**

Fixed the known issue from  November 8  .

**ISSUE:**

###  Known Issues

**ISSUE:**

If you are running multiple data centers in vSphere, running ` gkectl diagnose
cluster ` might return the following error, which you can safely ignore:

` Checking storage...FAIL path '*' resolves to multiple datacenters `

**ISSUE:**

If you are running a vSAN datastore, running ` gkectl diagnose cluster ` might
return the following error, which you can safely ignore:

` PersistentVolume [NAME]: virtual disk "[[DATASTORE_NAME]] [PVC]" IS NOT
attached to machine "[MACHINE_NAME]" but IS listed in the Node.Status `

##  November 08, 2019

**ISSUE:**

In GKE On-Prem version 1.1.1-gke.2, a known issue prevents creation of
clusters configured to use a Docker registry. You configure a Docker registry
by populating the GKE On-Prem configuration file's ` privateregistryconfig `
field. Cluster creation fails with an error such as ` Failed to create root
cluster: could not create external client: could not create external control
plane: docker run error: exit status 125 `

A fix is targeted for version 1.1.2. In the meantime, if you want to create a
cluster configured to use a Docker registry, pass in the ` --skip-validation-
docker ` flag to ` gkectl create cluster ` .

##  November 05, 2019

**ISSUE:**

GKE On-Prem's configuration file has a field, ` vcenter.datadisk ` , which
looks for a path to a virtual machine disk (VMDK) file. During installation,
you choose a name for the VMDK. By default, GKE On-Prem creates a VMDK and
saves it to the root of your vSphere datastore.

If you are using a vSAN datastore, you need to create a folder in the
datastore in which to save the VMDK. You provide the full path to the
field—for example, ` datadisk: gke-on-prem/datadisk.vmdk ` —and GKE On-Prem
saves the VMDK in that folder.

When you create the folder, vSphere assigns the folder a universally unique
identifier (UUID). Although you provide the folder path to the GKE On-Prem
config, the vSphere API looks for the folder's UUID. Currently, this mismatch
can cause cluster creation and upgrades to fail.

A fix is targeted for version 1.1.2. In the meantime, you need to provide the
folder's UUID instead of the folder's path. Follow the workaround instructions
currently available in the [ upgrading clusters
](https://cloud.google.com/gke-on-prem/docs/how-to/administration/upgrading-
clusters?hl=es-419#admin_datadisk_folder) and installation topics.

##  October 25, 2019

**FEATURE:**

GKE On-Prem version 1.1.1-gke.2 is now available. To download version
1.1.1-gke.2's OVA, ` gkectl ` , and upgrade bundle, see [ Downloads
](https://cloud.google.com/gke-on-prem/docs/downloads?hl=es-419#latest) .
Then, see [ Upgrading admin workstation ](https://cloud.google.com/gke-on-
prem/docs/how-to/upgrading?hl=es-419) and [ Upgrading clusters
](https://cloud.google.com/gke-on-prem/docs/how-to/upgrading?hl=es-419) .

This patch version includes the following changes:

**FEATURE:**

###  New Features

**FEATURE:**

**Action required:** This version upgrades the minimum ` gcloud ` version on
the admin workstation to 256.0.0. You should [ upgrade your admin workstation
](https://cloud.google.com/gke-on-prem/docs/how-to/administration/upgrading-
admin-workstation?hl=es-419) . Then, you should [ upgrade your clusters
](https://cloud.google.com/gke-on-prem/docs/how-to/administration/upgrading-
clusters?hl=es-419) .

**FEATURE:**

The open source [ CoreOS toolbox ](https://github.com/coreos/toolbox) is now
included in all GKE On-Prem cluster nodes. This suite of tools is useful for
troubleshooting node issues. See [ Debugging node issues using toolbox
](https://cloud.google.com/gke-on-prem/docs/support/toolbox?hl=es-419) .

**FIXED:**

###  Fixes

**FIXED:**

Fixed an issue that prevented clusters configured with OIDC from being
upgraded.

**FIXED:**

Fixed [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) described in [ Security bulletins
](https://cloud.google.com/gke-on-prem/docs/security-
bulletins?hl=es-419#october-16-2019) .

**FIXED:**

Fixed an issue that caused cluster metrics to be lost due to a lost connection
to Google Cloud. When a GKE On-Prem cluster's connection to Google Cloud is
lost for a period of time, that cluster's metrics are now fully recovered.

**FIXED:**

Fixed an issue that caused ingestion of admin cluster metrics to be slower
than ingesting user cluster metrics.

**ISSUE:**

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

  1. ####  List MachineDeployments in the admin cluster 
    
        kubectl get machinedeployments --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]
    

  2. ####  Update a user control plane MachineDeployment from your shell 
    
        kubectl edit machinedeployment --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINEDEPLOYMENT_NAME]
    

  3. ####  List Machines in the admin cluster 
    
        kubectl get machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]
    

  4. ####  Delete user control plane Machines in the admin cluster 
    
        kubectl delete machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINE_NAME]
    

##  September 26, 2019

**FEATURE:**

GKE On-Prem version 1.1.0-gke.6 is now available. To download version
1.1.0-gke.6's ` gkectl ` and upgrade bundle, see [ Downloads
](https://cloud.google.com/gke-on-prem/docs/downloads?hl=es-419#latest) .
Then, see [ Upgrading clusters ](https://cloud.google.com/gke-on-
prem/docs/how-to/upgrading?hl=es-419) .

This minor version includes the following changes:

**FEATURE:**

The default Kubernetes version for cluster nodes is now version 1.13.7-gke.20
(previously 1.12.7-gke.19).

**FEATURE:**

**Action required:** As of version 1.1.0-gke.6, GKE On-Prem now creates
vSphere [ Distributed Resource Scheduler (DRS)
](https://www.vmware.com/products/vsphere/drs-dpm.html) rules for your user
cluster's nodes (vSphere VMs), causing them to be spread across at least three
physical hosts in your datacenter.

**This feature is enabled by default for all new and existing user clusters
running version 1.1.0-gke.6.**

The feature requires that your vSphere environment meets the following
conditions:

  * VMware DRS must be enabled. VMware DRS requires vSphere Enterprise Plus license edition. To learn how to enable DRS, see [ Enabling VMware DRS in a cluster ](https://kb.vmware.com/s/article/1034280) . 
  * The vSphere user account provided in your GKE On-Prem configuration file's ` vcenter ` field must have the ` Host.Inventory.EditCluster ` permission. 
  * There are at least three physical hosts available. 

If you _do not_ want to enable this feature for your existing user
clusters—for example, if you don't have enough hosts to accommdate the
feature—perform the following steps _before_ you upgrade your user clusters:

  1. Open your existing GKE On-Prem configuration file. 
  2. Under the ` usercluster ` specification, add the ` antiaffinitygroups ` field as described in the [ ` antiaffinitygroups ` documentation ](https://cloud.google.com/gke-on-prem/docs/how-to/installation/install?hl=es-419#antiaffinitygroups) : ` usercluster: ... antiaffinitygroups: enabled: false `

  3. Save the file. 

  4. Use the configuration file to upgrade. Your clusters are upgraded, but the feature is not enabled. 

**FEATURE:**

You can now set the [ default storage class ](https://cloud.google.com/gke-on-
prem/docs/how-to/administration/default-storage-class?hl=es-419) for your
clusters.

**FEATURE:**

You can now use [ Container Storage Interface (CSI) 1.0
](https://github.com/container-storage-interface/spec) as a storage class for
your clusters.

**FEATURE:**

You can now [ delete broken or unhealthy user clusters
](https://cloud.google.com/gke-on-prem/docs/how-to/administration/deleting-a-
user-cluster?hl=es-419#delete_unhealthy_cluster) with ` gkectl delete cluster
--force `

**FEATURE:**

You can now [ diagnose node issues ](https://cloud.google.com/gke-on-
prem/docs/support/debug-toolbox?hl=es-419) using the ` debug-toolbox `
container image.

**FEATURE:**

You can now [ skip validatations ](https://cloud.google.com/gke-on-
prem/docs/how-to/installation/install?hl=es-419#skip_validate) run by ` gkectl
` commands.

**FEATURE:**

The tarball that ` gkectl diagnose snapshot ` creates now includes a log of
the command's output by default.

**FEATURE:**

Adds ` gkectl diagnose snapshot ` flag ` --seed-config ` . When you pass the
flag, it includes your clusters' GKE On-Prem configuration file in the tarball
procduced by ` snapshot ` .

**CHANGED:**

The ` gkeplatformversion ` field has been removed from the GKE On-Prem
configuration file. To specify a cluster's version, provide the version's
bundle to the ` bundlepath ` field.

**CHANGED:**

You need to add the vSphere permission, ` Host.Inventory.EditCluster ` ,
before you can use [ ` antiaffinitygroups ` ](https://cloud.google.com/gke-on-
prem/docs/how-to/installation/install?hl=es-419#antiaffinitygroups) .

**CHANGED:**

You now specify a configuration file in ` gkectl diagnose snapshot ` by
passing the ` --snapshot-config ` (previously ` --config ` ). See [ Diagnosing
cluster issues ](https://cloud.google.com/gke-on-
prem/docs/support/diagnose?hl=es-419#diagnose_snapshot) .

**CHANGED:**

You now capture your cluster's configuration file with ` gkectl diagnose
snapshot ` by passing ` --snapshot-config ` (previously ` --config ` ). See [
Diagnosing cluster issues ](https://cloud.google.com/gke-on-
prem/docs/support/diagnose?hl=es-419#diagnose_snapshot) .

**CHANGED:**

` gkectl diagnose ` commands now return an error if you provide a user
cluster's kubeconfig, rather than an admin cluster's kubeconfig.

**CHANGED:**

Cloud Console now notifies you when an upgrade is available for a registered
user cluster.

**ISSUE:**

A known issue prevents version 1.0.11, 1.0.1-gke.5, and 1.0.2-gke.3 clusters
using OIDC from being upgraded to version 1.1. A fix is targeted for version
1.1.1. If you configured a version 1.0.11, 1.0.1-gke.5, or 1.0.2-gke.3 cluster
with OIDC, you are not able to upgrade it. Create a version 1.1 cluster by
following [ Installing GKE On-Prem ](https://cloud.google.com/gke-on-
prem/docs/how-to/installation/install?hl=es-419) .

##  August 22, 2019

**FEATURE:**

GKE On-Prem version 1.0.2-gke.3 is now available. This patch release includes
the following changes:

**FEATURE:**

Seesaw is now supported for manual load balancing.

**FEATURE:**

You can now specify a different vSphere network for admin and user clusters.

**FEATURE:**

You can now delete user clusters using ` gkectl ` . See [ Deleting a user
cluster ](https://cloud.google.com/gke-on-prem/docs/how-
to/administration/deleting-a-user-cluster?hl=es-419) .

**CHANGED:**

` gkectl diagnose snapshot ` now gets logs from the user cluster control
planes.

**CHANGED:**

GKE On-Prem OIDC specification has been updated with several new fields: `
kubectlredirecturl ` , ` scopes ` , ` extraparams ` , and ` usehttpproxy ` .

**CHANGED:**

Calico updated to version 3.7.4.

**CHANGED:**

Stackdriver Monitoring's system metrics prefixed changed from `
external.googleapis.com/prometheus/ ` to ` kubernetes.io/anthos/ ` . If you
are tracking metrics or alerts, update your dashbaords with the next prefix.

**FIXED:**

[ Fixed a vulnerability from CVE-2019-11247 ](https://cloud.google.com/gke-on-
prem/docs/security-bulletins?hl=es-419#august-22-2019) .

**FIXED:**

[ Fixed a vulnerability in RBAC proxy ](https://cloud.google.com/gke-on-
prem/docs/security-bulletins?hl=es-419#august-23-2019) .

##  July 30, 2019

**FEATURE:**

GKE On-Prem version 1.0.1-gke.5 is now available. This patch release includes
the following changes:

**FEATURE:**

###  New Features

**FEATURE:**

Published [ GKE On-Prem cheatsheet ](https://cloud.google.com/gke-on-
prem/docs/reference/cheatsheet?hl=es-419) .

**CHANGED:**

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

**FIXED:**

###  Fixes

**FIXED:**

Fixes registry data persistence issues with the admin workstation's Docker
registry.

**FIXED:**

Fixes validation that checks whether a user cluster's name is already in use.

##  July 25, 2019

**FEATURE:**

GKE On-Prem version 1.0.11 is now available.

##  June 17, 2019

**FEATURE:**

GKE On-Prem is now generally available. Version 1.0.10 includes the following
changes:

**CHANGED:**

###  Upgrading from beta-1.4 to 1.0.10

Before upgrading your beta clusters to the first general availability version,
perform the steps described in [ Upgrading from GKE On-Prem beta to general
availability ](https://cloud.google.com/gke-on-prem/docs/how-
to/upgrading/from-beta?hl=es-419) , and review the following points:

  * If you are running a beta version before beta-1.4, be sure to upgrade to beta-1.4 first. 

  * If your beta clusters are running their own L4 load balancers (not the default, F5 BIG-IP), you need to delete and recreate your clusters to run the latest GKE On-Prem version. 

  * If your clusters were upgraded to beta-1.4 from beta-1.3, run the following command _for each user cluster_ before upgrading: 
    
        kubectl delete crd networkpolicies.crd.projectcalico.org

  * vCenter certificate verification is now required. ( ` vsphereinsecure ` is no longer supported.) If you're upgrading your beta 1.4 clusters to 1.0.10, you need to provide a vCenter trusted root CA public certificate in the upgrade configuration file. 

  * You need to upgrade _all_ of your running clusters. For this upgrade to succeed, your clusters can't run in a mixed version state. 

  * You need to upgrade your admin clusters to the latest version first, then upgrade your user clusters. 

**FEATURE:**

###  New Features

**FEATURE:**

You can now enable the [ Manual load balancing mode
](https://cloud.google.com/gke-on-prem/docs/how-to/installation/manual-
lb?hl=es-419) to configure a L4 load balancer. You can still choose to use the
default load balancer, F5 BIG-IP.

**FEATURE:**

GKE On-Prem's configuration-driven installation process has been updated. You
now declaratively install using a singular [ configuration file
](https://cloud.google.com/gke-on-prem/docs/overview?hl=es-419#config) .

**FEATURE:**

Adds ` gkectl create-config ` , which generates a configuration file for
installing GKE On-Prem, upgrading existing clusters, and for creating
additional user clusters in an existing installation. This replaces the
installation wizard and ` create-config.yaml ` from previous versions. See the
updated documentation for [ installing GKE On-Prem
](https://cloud.google.com/gke-on-prem/docs/how-
to/installation/install?hl=es-419#generate_config) .

**FEATURE:**

Adds ` gkectl check-config ` , which validates the GKE On-Prem configuration
file. See the updated documentation for [ installing GKE On-Prem
](https://cloud.google.com/gke-on-prem/docs/how-
to/installation/install?hl=es-419#validate_config) .

**FEATURE:**

Adds an optional ` --validate-attestations ` flag to ` gkectl prepare ` . This
flag verifies that the container images included in your admin workstationwere
built and signed by Google and are ready for deployment. See the updated
documentation for [ installing GKE On-Prem ](https://cloud.google.com/gke-on-
prem/docs/how-to/installation/install?hl=es-419#prepare) .

**CHANGED:**

###  Changes

**CHANGED:**

Upgrades Kubernetes version to 1.12.7-gke.19. You can now [ upgrade your
clusters ](https://cloud.google.com/gke-on-prem/docs/how-
to/administration/upgrading-clusters?hl=es-419) to this version. You can no
longer create clusters that run Kubernetes version 1.11.2-gke.19.

We recommend upgrading your admin cluster before you upgrade your user
clusters.

**CHANGED:**

Upgrades Istio ingress controller to version 1.1.7.

**CHANGED:**

vCenter certificate verification is now required. ` vsphereinsecure ` is no
longer supported). You provide the certificate in the GKE On-Prem configration
file's ` cacertpath ` field.

When a client calls the vCenter server, the vCenter server must prove its
identity to the client by presenting a certificate. That certificate must be
signed by a certificate authority (CA). The certificate is must not be self-
signed.

If you're upgrading your beta 1.4 clusters to 1.0.10, you need to provide a
vCenter trusted root CA public certificate in the upgrade configuration file.

**ISSUE:**

###  Known Issues

**ISSUE:**

[ Upgrading clusters ](https://cloud.google.com/gke-on-prem/docs/upgrading-
clusters?hl=es-419) can cause disruption or downtime for workloads that use [
PodDisruptionBudgets
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) (PDBs).

**ISSUE:**

You might not be able to upgrade beta clusters that use the [ Manual load
balancing mode ](https://cloud.google.com/gke-on-prem/docs/how-
to/installation/manual-lb?hl=es-419) to GKE On-Prem version 1.0.10. To upgrade
and continue using your own load balancer with these clusters, you need to
recreate the clusters.

##  May 24, 2019

**FEATURE:**

GKE On-Prem beta version 1.4.7 is now available. This release includes the
following changes:

**FEATURE:**

###  New Features

**FEATURE:**

In the [ ` gkectl diagnose snapshot ` ](https://cloud.google.com/gke-on-
prem/docs/beta-1.4/how-to/administration/diagnose?hl=es-419#capture_admin)
command, the ` --admin-ssh-key-path ` parameter is now optional.

**CHANGED:**

###  Changes

**CHANGED:**

On May 8, 2019, we introduced a change to Connect, the service that enables
you to interact with your GKE On-Prem clusters using Cloud Console. To use the
new Connect agent, you must re-register your clusters with Cloud Console, or
you must upgrade to GKE On-Prem beta-1.4.

Your GKE On-Prem clusters and the workloads running on them will continue to
operate uninterrupted. However, your clusters will not be visible in Cloud
Console until you re-register them or upgrade to beta-1.4.

Before you re-register or upgrade, make sure your service account has the `
gkehub.connect ` role. Also, if your service account has the old
clusterregistry.connect role, it's a good idea to remove that role.

Grant your service account the gkehub.connect role:

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \n      --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \n      --role="roles/gkehub.connect"

If your service account has the old ` clusterregistry.connect ` role, remove
the old role:

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \n      --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \n      --role="roles/clusterregistry.connect"

Re-register you cluster, or upgrade to GKE On-Prem beta-1.4.

To [ re-register your cluster ](https://cloud.google.com/kubernetes-
engine/connect/updating-agent?hl=es-419) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \n      --context=[USER_CLUSTER_CONTEXT] \n      --service-account-key-file=[LOCAL_KEY_PATH] \n      --kubeconfig-file=[KUBECONFIG_PATH] \n      --project=[PROJECT_ID]
          

To [ upgrade to GKE On-Prem beta-1.4 ](https://cloud.google.com/gke-on-
prem/docs/beta-1.4/how-to/administration/upgrading-a-cluster?hl=es-419) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

**ISSUE:**

###  Known Issues

**ISSUE:**

There is an issue that prevents the Connect agent from being updated to the
new version during an upgrade. To work around this issue, run the following
command after you upgrade a cluster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  May 13, 2019

**ISSUE:**

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

  2. For each user cluster, open the ` <var>[USER_CLUSTER_NAME]</var>_create_secret.yaml ` file in an editor. If the values for ` registerserviceaccountkey ` and ` connectserviceaccountkey ` are not ` REDACTED ` , no further action is required: the Secrets do not need to be re-encoded and written to the cluster. 

  3. Open the original ` create_config.yaml ` file in another editor. 

  4. In ` <var>[USER_CLUSTER_NAME]</var>_create_secret.yaml ` , replace the ` registerserviceaccountkey ` and ` connectserviceaccountkey ` values with the values from the original ` create_config.yaml ` file. Save the changed file. 

  5. Repeat steps 3-5 for each ` <var>[USER_CLUSTER_NAME]</var>_create_secret.yaml ` , and for the ` kube-system_create_secret.yaml ` file. 

  6. Base64-encode each ` <var>[USER_CLUSTER_NAME]</var>_create_secret.yaml ` file and the ` kube-system_create_secret.yaml ` file: 
    
        cat [USER_CLUSTER_NAME]_create_secret.yaml | base64 > [USER_CLUSTER_NAME]_create_secret_create_secret.b64
    
        cat kube-system-cluster_create_secret.yaml | base64 >kube-system-cluster_create_secret.b64

  7. Replace the ` data[cfg] ` field in each Secret in the cluster with the contents of the corresponding file: 
    
        kubectl edit secret create-config -n [USER_CLUSTER_NAME]
      # kubectl edit opens the file in the shell's default text editor
      # Open `first-user-cluster_create_secret.b64` in another editor, and replace
      # the `cfg` value with the copied value
      # Make sure the copied string has no newlines in it!

  8. Repeat step 8 for each ` <var>[USER_CLUSTER_NAME]</var>_create_secret.yaml ` Secret, and for the ` kube-system_create_secret.yaml ` Secret. 

  9. To ensure that the update was successful, repeat step 1. 

##  May 07, 2019

**FEATURE:**

GKE On-Prem beta version 1.4.1 is now available. This release includes the
following changes:

**FEATURE:**

###  New Features

**FEATURE:**

In the [ ` gkectl diagnose snapshot ` ](https://cloud.google.com/gke-on-
prem/docs/beta-1.4/how-to/administration/diagnose?hl=es-419#capture_admin)
command, the ` --admin-ssh-key-path ` parameter is now optional.

**CHANGED:**

###  Changes

**CHANGED:**

On May 8, 2019, we introduced a change to Connect, the service that enables
you to interact with your GKE On-Prem clusters using Cloud Console. To use the
new Connect agent, you must re-register your clusters with Cloud Console, or
you must upgrade to GKE On-Prem beta-1.4.

Your GKE On-Prem clusters and the workloads running on them will continue to
operate uninterrupted. However, your clusters will not be visible in Cloud
Console until you re-register them or upgrade to beta-1.4.

Before your re-register or upgrade, make sure your service account has the
gkehub.connect role. Also, if your service account has the old
clusterregistry.connect role, it's a good idea to remove that role.

Grant your service account the gkehub.connect role:

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \n      --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \n      --role="roles/gkehub.connect"

If your service account has the old clusterregistry.connect role, remove the
old role:

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \n      --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \n      --role="roles/clusterregistry.connect"

Re-register you cluster, or upgrade to GKE On-Prem beta-1.4.

To [ re-register your cluster ](https://cloud.google.com/kubernetes-
engine/connect/updating-agent?hl=es-419) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \n      --context=[USER_CLUSTER_CONTEXT] \n      --service-account-key-file=[LOCAL_KEY_PATH] \n      --kubeconfig-file=[KUBECONFIG_PATH] \n      --project=[PROJECT_ID]
          

To [ upgrade to GKE On-Prem beta-1.4 ](https://cloud.google.com/gke-on-
prem/docs/beta-1.4/how-to/administration/upgrading-a-cluster?hl=es-419) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

**ISSUE:**

###  Known Issues

**ISSUE:**

There is an issue that prevents the Connect agent from being updated to the
new version during an upgrade. To work around this issue, run the following
command after you upgrade a cluster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  April 25, 2019

**FEATURE:**

GKE On-Prem beta version 1.3.1 is now available. This release includes the
following changes:

**FEATURE:**

###  New Features

**FEATURE:**

The ` gkectl diagnose snapshot ` command now has a [ ` --dry-run `
](https://cloud.google.com/gke-on-prem/docs/beta-1.3/how-
to/administration/diagnose?hl=es-419#performing_a_dry_run_for_a_snapshot)
flag.

**FEATURE:**

The ` gkectl diagnose snapshot ` command now supports four [ scenarios
](https://cloud.google.com/gke-on-prem/docs/beta-1.3/how-
to/administration/diagnose?hl=es-419#snapshot_scenarios) .

**FEATURE:**

The ` gkectl diagnose snapshot ` command now supports regular expressions for
specifying namespaces.

**CHANGED:**

###  Changes

**CHANGED:**

Istio 1.1 is now the default [ ingress controller
](https://cloud.google.com/gke-on-prem/docs/beta-1.3/how-
to/administration/upgrading-a-
cluster?hl=es-419#upgrading_the_ingress_controller) . The ingress controller
runs in the ` gke-system ` namespace for both admin and user clusters. This
enables easier TLS management for Ingress. To enable ingress, or to re-enable
ingress after an upgrade, follow the instructions under [ Enabling ingress
](https://cloud.google.com/gke-on-prem/docs/beta-1.3/how-
to/installation/install?hl=es-419#enabling_ingress) .

**CHANGED:**

The ` gkectl ` tool no longer uses Minikube and KVM for bootstrapping. This
means you do not have to enable nested virtualization on your admin
workstation VM.

**ISSUE:**

###  Known Issues

**ISSUE:**

GKE On-Prem's ingress controller uses Istio 1.1 with automatic Secret
discovery. However, the node agent for Secret discovery may fail to get Secret
updates after Secret deletion. So avoid deleting Secrets. If you must delete a
Secret and Ingress TLS fails afterwards, manually restart the Ingress Pod in
the gke-system namespace.

##  April 11, 2019

**FEATURE:**

GKE On-Prem beta version 1.2.1 is now available. This release includes the
following changes:

**FEATURE:**

###  New Features

**FEATURE:**

GKE On-Prem clusters now automatically connect back to Google using [ Connect
](https://cloud.google.com/kubernetes-engine/connect/?hl=es-419) .

**FEATURE:**

You can now run up to three control planes per user cluster.

**CHANGED:**

###  Changes

**CHANGED:**

` gkectl ` now validates vSphere and F5 BIG-IP credentials creating clusters.

**ISSUE:**

###  Known Issues

**ISSUE:**

A regression causes ` gkectl diagnose snapshot ` commands to use the wrong SSH
key, which prevents the command from collecting information from user
clusters. As a workaround for support cases, you might need to SSH into
individual user cluster nodes and manually gather data.

##  April 02, 2019

**FEATURE:**

GKE On-Prem beta version 1.1.1 is now available. This release includes the
following changes:

**FEATURE:**

###  New Features

**FEATURE:**

You now install GKE On-Prem with an [ Open Virtual Appliance (OVA)
](https://cloud.google.com/gke-on-prem/docs/beta-1.1/how-
to/installation/getting-started?hl=es-419#download_ova) , a pre-configured
virtual machine image that includes several command-line interface tools. This
change makes installations easier and removes a layer of virtualization. You
no longer need to run ` gkectl ` inside a Docker container.

If you installed GKE On-Prem versions before beta-1.1.1, you should create a
new admin workstation following the documented instructions. After you install
the new admin workstation, copy over any SSH keys, configuration files,
kubeconfigs, and any other files you need, from your previous workstation to
the new one.

**FEATURE:**

Added documentation for [ backing up and restoring clusters
](https://cloud.google.com/gke-on-prem/docs/beta-1.1/how-
to/administration/backing-up?hl=es-419) .

**FEATURE:**

You can now configure authentication for clusters using OIDC and ADFS. To
learn more, refer to [ Authenticating with OIDC and ADFS
](https://cloud.google.com/gke-on-prem/docs/beta-1.1/how-to/security/oidc-
adfs?hl=es-419) and [ Authentication ](https://cloud.google.com/gke-on-
prem/docs/concepts/authentication?hl=es-419) .

**CHANGED:**

###  Changes

**CHANGED:**

You now must use an admin cluster's private key to run ` gkectl diagnose
snapshot ` .

**CHANGED:**

Added a configuration option during installation for deploying multi-master
user clusters.

**CHANGED:**

[ Connect documentation ](https://cloud.google.com/kubernetes-
engine/connect/?hl=es-419) has been migrated.

**FIXED:**

###  Fixes

**FIXED:**

Fixed an issue where cluster networking could be interrupted when a node is
removed unexpectedly.

**ISSUE:**

###  Known Issues

**ISSUE:**

GKE On-Prem's Configuration Management has been upgraded from version 0.11 to
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

**FEATURE:**

GKE On-Prem beta version 1.0.3 is now available. This release includes the
following changes:

**FIXED:**

###  Fixes

**FIXED:**

Fixed an issue that caused Docker certificates to be saved to the wrong
location.

##  March 04, 2019

**FEATURE:**

GKE On-Prem beta version 1.0.2 is now available. This release includes the
following changes:

**FEATURE:**

###  New Features

**FEATURE:**

You can now run ` gkectl version ` to check which version of ` gkectl ` you're
running.

**FEATURE:**

You can now [ upgrade user clusters ](https://cloud.google.com/gke-on-
prem/docs/beta-1.0/how-to/administration/upgrading-a-cluster?hl=es-419) to
future beta versions.

**FEATURE:**

[ Anthos Config Management ](https://cloud.google.com/anthos-config-
management/docs/?hl=es-419) version 0.11.6 is now available.

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

**CHANGED:**

###  Changes

**CHANGED:**

You can now update IP blocks in the cluster specification to expand the IP
range for a given cluster.

**CHANGED:**

If clusters you installed during alpha were disconnected from Google after
beta, you might need to connect them again. Refer to [ Manually registering a
user cluster. ](https://cloud.google.com/gke-on-prem/docs/how-
to/installation/registering-a-user-cluster?hl=es-419)

**CHANGED:**

[ Getting started ](https://cloud.google.com/gke-on-prem/docs/how-
to/installation/getting-started?hl=es-419) has been updated with steps for
activating your service account and running ` gkectl prepare ` .

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

**FIXED:**

###  Fixes

**FIXED:**

Cluster resizing operations improved to prevent unintended node deletion.

##  February 07, 2019

**FEATURE:**

GKE On-Prem alpha version 1.3 is now available. This release includes the
following changes:

**FEATURE:**

###  New Features

**FEATURE:**

During installation, you can now provide YAML files with ` nodeip ` blocks to
configure static IPAM.

**CHANGED:**

###  Changes

**CHANGED:**

You now need to provision a 100GB disk in vSphere Datastore. GKE On-Prem uses
the disk to store some of its vital data, such as etcd. See [ System
requirements ](https://cloud.google.com/gke-on-
prem/docs/requirements?hl=es-419) .

**CHANGED:**

You can now only provide lowercase hostnames to ` nodeip ` blocks.

**CHANGED:**

GKE On-Prem now enforces unique names for user clusters.

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

**ISSUE:**

###  Known Issues

**ISSUE:**

If your vCenter user account uses a format like ` DOMAINUSER ` , you might
need to escape the backslash ( ` DOMAIN\USER ` ). Be sure to do this when
prompted to enter the user account during installation.

##  January 23, 2019

**FEATURE:**

GKE On-Prem alpha version 1.2.1 is now available. This release includes the
following changes:

**FEATURE:**

###  New Features

**FEATURE:**

You can now use ` gkectl ` to [ delete admin clusters
](https://cloud.google.com/gke-on-prem/docs/how-to/administration/deleting-an-
admin-cluster?hl=es-419) .

**CHANGED:**

###  Changes

**CHANGED:**

` gkectl diagnose snapshot ` commands now allow you to specify nodes while
capturing snapshots of remote command results and files.

##  January 14, 2019

**FEATURE:**

GKE On-Prem alpha version 1.1.2 is now available. This release includes the
following changes:

**FEATURE:**

###  New Features

**FEATURE:**

You can now use the ` gkectl prepare ` command to pull and push GKE On-Prem's
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

**CHANGED:**

###  Changes

**CHANGED:**

GKE On-Prem now runs Kubernetes version **1.11.2-gke.19** .

**CHANGED:**

The default footprint for GKE On-Prem has changed:

  * Minimum memory requirement for user cluster nodes is now 8192M. 

**CHANGED:**

GKE On-Prem now runs minikube version **0.28.0** .

**CHANGED:**

GKE Policy Management has been upgraded to version **0.11.1** .

**CHANGED:**

` gkectl ` no longer prompts you to provide a proxy configuration by default.

**CHANGED:**

There are three new ConfigMap resources in the user cluster namespace: `
cluster-api-etcd-metrics-config ` , ` kube-etcd-metrics-config ` , and ` kube-
apiserver-config ` . GKE On-Prem uses these files to quickly bootstrap the
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

**FIXED:**

###  Fixes

**FIXED:**

Fixed issues with minikube caching that caused unexpected network calls.

**FIXED:**

Fixed an issue with pulling F5 BIG-IP credentials. Credentials are now read
from a credentials file instead of using environment variables.

**ISSUE:**

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

**FEATURE:**

GKE On-Prem alpha 1.0.4 is now available. This release includes the following
changes:

**FIXED:**

###  Fixes

**FIXED:**

The vulnerability caused by [ CVE-2018-1002105
](https://github.com/kubernetes/kubernetes/issues/71411) has been patched.

##  November 30, 2018

**FEATURE:**

GKE On-Prem alpha 1.0 is now available. The following changes are included in
this release:

**CHANGED:**

###  Changes

**CHANGED:**

GKE On-Prem alpha 1.0 runs Kubernetes 1.11.

**CHANGED:**

The default footprint for GKE On-Prem has changed:

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

**FIXED:**

###  Fixes

**FIXED:**

The vulnerability caused by [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) has been patched.

**ISSUE:**

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

GKE On-Prem alpha 1.0 does not yet pass all conformance tests.

**ISSUE:**

Only one user cluster per admin cluster can be created. To create additional
user clusters, create another admin cluster.

##  October 31, 2018

**FEATURE:**

GKE On-Prem EAP 2.1 is now available. The following changes are included in
this release:

**CHANGED:**

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

**FEATURE:**

GKE On-Prem EAP 2.0 is now available. The following changes are included in
this release:

**CHANGED:**

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

**ISSUE:**

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

