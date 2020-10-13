#  Release Notes

This page documents production updates to Migrate for Anthos. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/migrateanthos-release-notes.xml
`

##  July 28, 2020

On July 28, 2020 we released Migrate for Anthos 1.4.

For instructions on upgrading from version 1.3, see [ Upgrading Migrate for
Anthos to 1.4 ](/migrate/anthos/docs/upgrade) .

**FEATURE:**

Added support for Anthos GKE on-prem clusters running on VMware. On-prem
support lets you migrate source VM workloads in a vCenter/vSphere environment
to a GKE on-prem cluster running in the same vCenter/vSphere environment. See
[ Prerequisites for migrating Linux VMs on-prem
](/migrate/anthos/docs/migration-prerequisites-on-prem) for the requirements
for on-prem migration.

**FEATURE:**

The [ Google Cloud Console ](https://console.cloud.google.com/) provides a
web-based, graphical user interface that you can use to manage your Google
Cloud Console(GCP) projects and resources. Migrate for Anthos now supports the
migration of workloads by using the [ Google Cloud Console
](https://console.cloud.google.com/) . See [ Migrate for Anthos management
interfaces ](/migrate/anthos/docs/dev-env-overview) .

In this release, the Migrate for Anthos [ Google Cloud Console
](https://console.cloud.google.com/) does not support migrations for Windows
or for on-prem, including monitoring Windows or on-prem migrations.

**FEATURE:**

You can use Migrate for Anthos to migrate Windows VMs to workloads on GKE.
This process clones your Compute Engine VM disks and uses the clone to
generate artifacts (including a Dockerfile and a zip archive with extracted
workload files and settings) you can use to build a deployable container
image. This feature is currently in Beta. See [ Adding a Windows migration
source ](/migrate/anthos/docs/windows/migrating-win-vm-overview) .

**FEATURE:**

Migrate for Anthos now includes [ Custom Resource Definitions (CRDs)
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) that enable you to easily create and manage migrations using an
API automation solution or code. For example, you can use these CRDs to build
your own automated tools.

For more on the Migrate for Anthos CRDs, see [ CRD overview
](/migrate/anthos/docs/crd-overview) .

**FEATURE:**

Added the new ` --json-key sa.json ` option to the ` migctl source create ce `
command to create a migration for Compute Engine, where ` sa.json ` specifies
a service account. See [ Optionally creating a service account when using
Compute Engine as a migration source ](/migrate/anthos/docs/config-dev-
env#optionally_creating_a_service_account_when_using_as_a_migration_source)
for more.

**FEATURE:**

To edit the migration plan, you must now use the ` migctl migration get my-
migration ` command to download the plan. After you are done editing the plan,
you have to upload it by using the ` migctl migration update my-migration `
command. See [ Customizing a migration plan
](/migrate/anthos/docs/customizing-a-migration-plan) for more.

**FEATURE:**

Added the ` node-selectors ` and ` tolerations ` options to the ` migctl setup
install ` installation command that lets you install Migrate for Anthos on a
specific set of nodes or node pools in a cluster. See [ Installing Migrate for
Anthos ](/migrate/anthos/docs/installing-migrate-components) .

**DEPRECATED:**

The ` migctl migration cleanup ` command has been removed and is no longer
necessary.

**DEPRECATED:**

In previous releases, you used a command in the form: ` migctl source create
ce my-ce-src --project my-project --zone zone ` to create a migration for
Compute Engine. The ` --zone ` option has been removed when creating a Compute
Engine migration. Using the ` --zone ` option in this release causes an error.

**DEPRECATED:**

The ` migctl migration logs ` command has been removed. You now use the Google
Console to view logs.

**DEPRECATED:**

By default Migrate for Anthos installs to and performs migrations in the `
v2k-system ` namespace. In previous releases, you could specify the namespace.
The option to specify a namespace has been removed.

**FIXED:**

**GKE on-prem preview:** If a source was created with ` migctl source create `
using the wrong credentials, you could not delete the migration with ` migctl
migration delete ` . This issue has been fixed in the GA release of on-prem
support.

**ISSUE:**

**160309992:** Editing a migration plan from the GUI console might fail if it
was also edited using ` migctl ` .

**ISSUE:**

**161135630:** Attempting multiple migrations of the same remote VM (from
VMware, AWS or Azure) simultaneously, might result in a stuck migration
process.

**Workaround:** Delete the stuck migration.

**ISSUE:**

**161214397:** For Anthos on-prem, in case of a missing service-account to
upload container images to the Container Registry, the migration might get
stuck.

**Workaround:** Add the service-account. If you are using the Migrate for
Anthos CRD API, delete the GenerateArtifactsTask object using ` kubectl ` and
recreate it either using the CRD or re-running ` migctl migration generate-
artifacts ` . Alternatively, you can use ` migctl ` to delete the migration
and recreate it. You can first download the migration YAML using ` migctl
migration get ` to backup any customizations you have made.

**ISSUE:**

**161110816:** ` migctl migration create ` with a source that doesn't exist
fails with a non-informative error message: ` request was denied ` .

**ISSUE:**

**161104564:** Creating a Linux migration with wrong ` os-type ` specification
causes the migration process to get stuck until deleted.

**ISSUE:**

**160858543, 160836394, 160844377, 154430477, 154403665, 153241390,153239696,
152408818, 151516642, 132002453:** Unstable network in Migrate for Compute
Engine infrastructure, or a GKE node restart, might cause migration to get
stuck.

**Workaround:** Delete the migration and re-create it. If recreating the
migration does not solve the issue, please contact [ support
](https://cloud.google.com/support-hub#migrate-for-compute-engine-formerly-
velostrata) .

**ISSUE:**

**161787358:** In some cases, upgrading from version v1.3 to v1.4 might fail
with ` Failed to convert source ` message.

**Workaround:** Re-run the upgrade command.

**ISSUE:**

**153811691, 153439420:** Migrate for Anthos support for older Java does not
handle OpenJDK 7 and 8 CPU resource calculations.

**ISSUE:**

**152974631:** Using GKE nodes with CPU and Memory configurations below the
recommended values might cause migrations to get stuck.

**ISSUE:**

**157890913, 160082702, 161125635, 159693579** :A migration might continue to
indicate that it is running, while an issue encountered prevents further
processing.

**Workaround:** Check event messages on the migration object using the verbose
` migctl ` status command: ` migclt migration status migration_name -v ` . You
might be able to correct the issue to allow the migration to continue or the
migration should be deleted and recreated if an Error event is listed without
further retries.

An example is when creating a Windows migration on a cluster with no Windows
nodes. In this case the event message will show:

` Warning FailedScheduling 10s Pod discover-xyz 0/1 nodes are available: 1
node(s) didn't match node selector. `

##  March 30, 2020

v1.3.0

**FEATURE:**

New ` migctl ` CLI for deploying Migrate for Anthos, creating and operating
migrations using a structured workflow and a migration processing cluster.

**FEATURE:**

Introducing a unified migration workflow across all supported VM sources --
VMware, AWS EC2, Azure VMs and Compute Engine VMs.

**FEATURE:**

Migrations are defined and operated using a Kubernetes CRD.

**FEATURE:**

Automated generation of a suggested migration plan (specified in a CRD), CI/CD
artifacts and deployment specs. The migration process now results in
extracting and generating container and deployment artifacts, including a
container image and a Dockerfile, extracted data in a persistent volume,
deployment/statefulSet, PVC and PV specs in an auto-generated YAML file for
easy workload deployment.

**FEATURE:**

The Migrate for Anthos software runtime layer now offers a compatibility
feature for older Java versions that are not container aware by reflecting the
correct resource allocations in the container's /proc file system.

**FEATURE:**

Migrate for Anthos v1.0 Marketplace deployment is now removed. Migrate for
Anthos v1.3 allows installation in v1.0 compatibility mode where needed.

**FEATURE:**

Preview features -- contact your Google Sales representative to enroll.

  * Migrating Windows VMs with IIS ASP.NET web applications to Windows 2019 containers on GKE. 
  * Processing migrations in Anthos on-prem. 

**ISSUE:**

**147211918:** In some cases, migration from AWS or Azure as a source can be
stuck with no progress. If this happens, run ` kubectl describe storageclass `
to view related events. You can also check the status of the matching Cloud
Details in Migrate for Compute Engine.

**ISSUE:**

**146699220:** When the source VM has a systemd service with a ` NICE ` config
property, the service might not start when running in a container.

**Workaround:** Remove the ` NICE ` property in the source VM before the
migration.

**ISSUE:**

**144896313:** Migration of Security-Enhanced Linux (SELinux) is not
supported.

**ISSUE:**

**149900626:** Some file systems not listed in [ Compatible VM operating
systems ](/migrate/anthos/docs/compatible-os-versions) may fail to migrate.
When running ` migctl migration logs migration-name ` , the logs in Cloud
Logging may show a message such as:

    
    
    failed to mount - exit status 32 - mount: /tmp/bootdir: unknown filesystem type 'LVM2\_member'.

**ISSUE:**

**152194161:** Your migrated workload container fails when running a cluster
with GKE nodes of type "COS". When you run the command ` kubectl logs
[podname] ` , you might see the following:

    
    
    apparmor.go:385] Couldn't set label to lxc-container-default - write /proc/1/attr/current: no such file or directory

This is an indication that the required AppArmor profiles are not installed on
the GKE nodes. To solve this, run ` migctl setup install --cos-runtime ` .

**ISSUE:**

**148334068:** When Migrating a physical VM from on-premises connected via
Migrate for Compute Engine, Migrate for Anthos attempts to optimize network
utilization and discards (rather than stream) blocks that are not in use on
the source VM file system. In some cases, this might cause VMware storage
sessions to time out. For assistance, please contact support.

**ISSUE:**

**GKE on-prem preview:** If a source was created with ` migctl source create `
using the wrong credentials, migrations will fail. Attempts to delete the
migration with ` migctl migration delete ` may hang in a "Terminating" state,
as in the following example:

    
    
    $ migctl migration list
    NAME       PROCESS              STATE                   STATUS        PROGRESS   AGE
    my-vm-01   generate-artifacts   createSourceSnapshots   TERMINATING   [2/13]

##  December 19, 2019

v1.0.1

**FIXED:**

When specifying a mixed-case value for the ` clone_vm_disks ` script's ` -A
<var>app-name</var> ` argument, the YAML file generated by the script would
include a workload name that could not be deployed.

The command now checks for a valid input value.

**FIXED:**

The Migrate for Compute Engine password could be inadvertently logged in
Stackdriver Logging.

**FIXED:**

Migrate for Anthos failed to recognize a reference to a disk specified as a `
PARTUUID ` in the ` fstab ` file. ` PARTUUID ` is now supported.

**FIXED:**

Deleting a ` StatefulSet ` attached to a persistent volume would leave the
volume in an attached state./p>

**FIXED:**

Using configuration YAML from a version prior to 1.0 caused the pod to enter a
crashloop stage.

An error message now is now displayed to request that you update to [ the
latest definition ](/migrate/anthos/docs/yaml-reference) .

**FIXED:**

When resolving block devices in a multipath device, the operation appeared to
succeed even if there was an error with one of the block devices.

**FIXED:**

Resolving source storage devices would sometimes fail without error if one of
the devices has no partitions.

**FIXED:**

Using ` kubectl exec ` on a migration pod would sometimes display superfluous
` bash ` warnings about ` LC_ALL ` .

**FIXED:**

Attempting to switch to a non-root user with the ` su ` command after
connecting to the machine with ` ssh ` would fail when you had previously used
` su ` to switch to another user.

**FIXED:**

Migrate for Anthos CSI drive would sometimes fail connecting to the migrated
VM.

**FIXED:**

The ` kubectl cp ` command would fail when copying files to the migrated pod.

##  November 13, 2019

v1.0.0

**FEATURE:**

Migrate for Anthos supports migrating existing VMware, Amazon EC2, Azure, and
Compute Engine VMs to containers on Google Kubernetes Engine. For more
information, see [ Benefits of Migrate for Anthos
](/migrate/anthos/docs/anthos-migrate-benefits) .

**FEATURE:**

You can monitor export of short-term storage to a persistent volume using `
kubectl ` . For more information, see [ Exporting streaming PVs to permanent
storage ](/migrate/anthos/docs/export-storage) .

**FEATURE:**

Using a ` ConfigMap ` , you can have content from application log files you
specify written to Stackdriver Logging (a default list is included). For more,
see [ Configuring logging to Stackdriver Logging
](/migrate/anthos/docs/configuring-stackdriver-logging) .

**FEATURE:**

For information on operating systems supported by Migrate for Anthos, see [
Compatible VM operating systems ](/migrate/anthos/docs/compatible-os-versions)
.

**ISSUE:**

On the Migrate for Compute Engine portlet in VMWare vCenter, VMs will be shown
as Managed by Migrate for Compute Engine during migration process. Only the
cache and storage migration status are updated in this view. Other
functionality, such as Migrate for Compute Engine actions, may not be
functional.

**ISSUE:**

For known issues and workarounds, see [ Troubleshooting Migrate for Anthos
](/migrate/anthos/docs/troubleshooting) .

**ISSUE:**

VMs using EFI configurations are not compatible for migration with this
release.

**ISSUE:**

Operating systems running ` systemd ` versions lower than 234 are limited to
65536 open files.

**ISSUE:**

When using a private GKE cluster, the GKE master might be unable to reach
Migrate for Anthos infrastructure (specifically, the admission-controller) by
default. This is because the admission-controller pod listens on port 7000.

To work around this issue, add port 7000 to the firewall rules of the master
node. For more, see [ Creating a private cluster
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters#add_firewall_rules) .

**ISSUE:**

When specifying a mixed-case value for the ` clone_vm_disks ` script's ` -A
<var>app-name</var> ` argument, the YAML file generated by the script includes
a workload name that can not be deployed.

To work around this issue, specify the argument's value in lowercase only.

**ISSUE:**

The Migrate for Compute Engine password can be inadvertently logged in
Stackdriver Logging.

**ISSUE:**

Migrate for Anthos fails to recognize a reference to a disk specified as a `
PARTUUID ` in the ` fstab ` file.

**ISSUE:**

Deleting a StatefulSet attached to a persistent volume will leave the volume
in an attached state.

**ISSUE:**

Using configuration YAML from a version prior to 1.0 causes the pod to enter a
crashloop stage.

To work around this, update your YAML file to conform to [ the latest
definition ](/migrate/anthos/docs/yaml-reference) .

**ISSUE:**

When resolving block devices in a multipath device, the operation appears to
succeed even if there was an error with one of the block devices.

**ISSUE:**

Resolving source storage devices would sometimes fail without error if one of
the devices has no partitions.

**ISSUE:**

Using ` kubectl exec ` on a migration pod sometimes displays superfluous `
bash ` warnings about ` LC_ALL ` . These are only cosmetic.

**ISSUE:**

Attempting to switch to a non-root user with the ` su ` command after
connecting to the machine with ` ssh ` fails when you have previously used `
su ` to switch to another user.

To work around this issue, use ` kubectl exec ` instead of ` ssh ` to get a
shell to the container.

**ISSUE:**

Migrate for Anthos CSI drive may sometimes fail connecting to the migrated VM.

**ISSUE:**

The ` kubectl cp ` command fails when copying files to the migrated pod.

