You're viewing documentation for a prior version of Migrate for Compute Engine
(formerly Velostrata). You can continue using this version, or use the [
current version ](/migrate/compute-engine/docs) .

#  Release Notes

This page documents production updates to Migrate for Compute Engine. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/migrate-for-compute-engine-
release-notes.xml `

##  December 20, 2019

4.8.1

**FIXED:**

In some scenarios, migrating a VM from Azure may fail due to missing instance
type at Azure region.

**FIXED:**

Create token API authentication mechanism.

**FIXED:**

This release fixes several issues related to preparing Linux VMs for Compute
Engine in the migration process. These fixes increase stability and broaden
source platform support.

##  November 12, 2019

4.8.0

**CHANGED:**

For a list of builds for this release and others, see the [ Build History
](https://cloud.google.com/migrate/compute-engine/docs/build-history) .

####  Requirements and OS Support

See [ Requirements ](https://cloud.google.com/migrate/compute-
engine/docs/4.8/concepts/requirements) and [ Supported operating systems
](https://cloud.google.com/migrate/compute-
engine/docs/4.8/reference/supported-os-versions) .

**FEATURE:**

####  Azure to Google Cloud migration (GA)

Version 4.8 promotes Azure to GCP migration to GA level. You can migrate VMs
to Compute Engine using [ Waves migration
](https://cloud.google.com/migrate/compute-engine/docs/4.8/how-to/organizing-
migrations/overview) . The system now supports migration at scale of instances
from Azure to Compute Engine.

**FEATURE:**

####  System upgrade/patch management

Version 4.8 introduces upgrades and patch management. You can [ manage system
upgrades and patch installation ](https://cloud.google.com/migrate/compute-
engine/docs/4.8/support/applying-patches-and-upgrades) via the system UI.

**FEATURE:**

####  Reduced network connectivity requirement

Version 4.8 requires reduced network connectivity between all components.
Network connectivity requirement for Cloud Extension and Workers is reduced to
single direction to Migrate for Compute Engine Manager. This simplifies system
deployment.

**ISSUE:**

**#143313211:** Customer migrating RHEL 6.8 VM may experience boot issues in
the cloud destination.

RHEL 6.x systems using kernel versions 2.6.32-xxx and using LVM may reach a
kernel panic when booting in Compute Engine during migration.

**Workaround:** The kernel should be upgraded to 2.6.32-754 or higher before
migrating.

**ISSUE:**

**#143262721:** Migration of VM from Azure fails when data disk is greater
than 4 terabytes.

At this time, Migrate for Compute Engine does not support migration of Azure
VMs with data disks bigger than 4TB.

**Workaround:** Make sure VM has data disk smaller than 4TB.

**ISSUE:**

**#131532690:** Run-in-cloud and migration operations may fail for Windows
Server 2016 workload when Symantec Endpoint Protection (SEP) is installed.
This may also happen when SEP appears to be disabled.

**Workaround:** Modify workload Network interface bindings to remove the SEP
option.

  1. Download [ Microsoft Network VSP Bind (nvspbind) ](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850)
  2. Install Microsoft_Nvspbind_package.EXE into c:\temp. 
  3. Open a command prompt as an Administrator and run the following: 

` nvspbind.exe /d * symc_teefer2 `

**ISSUE:**

**#131614405:** When the Velostrata Prep RPM is installed on SUSE Linux
Enterprise Server 11, the VM obtains a DHCP IP address in addition to an
existing static IP configuration. This issue occurs when the VM is started on-
premises in a subnet that is enabled with DHCP services.

**Note:** The issue does not occur when the subnet has no DHCP services. There
is no connectivity impact for communications with the original static IP
address.

**ISSUE:**

**#131637800:** After registering the Velostrata plug-in, running the Cloud
Extension wizard might generate an error "XXXXXXXXXX" upon "Finish".

**Workaround:** Un-register the Velostrata plug-in and restart the vSphere Web
client service, then re-register the plug-in. Contact support if the issue
persists.

**ISSUE:**

**#131548730:** In some cases, when a VM is moved to Run-in-Cloud while a 3rd
party VM-level backup solution holds a temporary snapshot, the Migrate for
Compute Engine periodic write-back operations will not complete even after the
backup solution deletes the temporary snapshot. The uncommitted writes counter
on the VM will show an increasing size and no consistency checkpoint will be
created on-premises.

**Workaround:** Select the Run On-Premises action for the VM and wait for the
task to complete, which will commit all pending writes. Then select the Run-
in-Cloud action again. Note that committing many pending writes may take a
while. Do not use the Force option as this will result in the loss of the
uncommitted writes.

**ISSUE:**

**#131605387:** vCenter reboot causes Velostrata tasks in vCenter to disappear
from UI. This is a vCenter limitation.

**Workaround:** Use the Velostrata PowerShell module to monitor Velostrata
managed VMs or Cloud Extensions tasks that are currently running.

**ISSUE:**

**#131638716:** With an ESXi host in maintenance mode, if a VM is moved to
cloud, the operation will fail and get stuck in the rollback phase.

**Workaround:** Manually cancel the Run-in-Cloud task, migrate the VM to
another ESXi host in the cluster and retry the Run-in-Cloud operation.

**ISSUE:**

**#131638455:** A Run-in-Cloud operation fails with the error - "Failed to
create virtual machine snapshot. The attempted operation cannot be performed
in the current state (Powered off)".

**Workaround:** The VMware VM snapshot file may be pointing to a non-existent
snapshot. Contact support for assistance in correcting the issue.

**ISSUE:**

**#131534862:** In rare cases, after running a Workload back on-premises -
Workload VMDK's are locked. In certain cases, this is due to network
disruptions between the Velostrata management appliance and the ESXi host on
which the workload is running.

**Note:** The issue will resolve itself after 1-2 hours.

**ISSUE:**

**#131550214:** During Detach, the operation might fail with the following
error message: "Operation was canceled".

**Workaround:** Retry the Detach operation.

**ISSUE:**

**#131650367:** When performing a detach after a cancel detach operation, the
action may fail.

**Workaround:** Retry the operation.

**ISSUE:**

**#131649978:** In the event of certain system failures, Velostrata components
disconnect from vCenter. In this case, an event may not be sent, resulting in
the alarm either not being set properly or not being cleared properly.

**Workaround:** Clear the alarm manually in vCenter.

**ISSUE:**

**#131532549:** For workloads with a Windows machine using a retail license,
when returning from the cloud, the license is not present.

**Workaround:** Reinstall the license.

**ISSUE:**

**#131555885:** vCenter "Export OVA" operation is available when the VM in
cloud is running in cache mode, however, this operation results in a corrupted
OVA.

**Workaround:** Only create OVA after the detach.

**ISSUE:**

**#131647857:** In rare cases, when a cloud component instance is created and
system fails before it is tagged, the instance will remain untagged. This will
not allow full clean-up or repair of the CE.

**Workaround:** Manually tag the instance, and then run "Repair".

**ISSUE:**

**#131537125:** Cloud Extension high availability does not work for workloads
running Ubuntu OS with LVM configuration.

**Workaround:** Update the kernel to 3.13.0-161 or higher.

**ISSUE:**

**#131560126:** Suse12: Due to a bug in SUSE kernel older than 4.2,
configurations that include BTRFS mounts with subvolumes are not supported.

**Workaround:** Upgrade to SUSE version with Kernel >=4.2 (SP2).

**ISSUE:**

**#131533480:** When using the Create Cloud Extension wizard, using an illegal
HTTP proxy address will not generate a warning message.

**Workaround:** Delete the CE and then create the CE with a valid HTTP proxy
address.

**ISSUE:**

**#131647654:** Run on-premises operation succeeded but the status is marked
as failed with error "Failed to consolidate snapshots"

**Workaround:** Consolidate snapshots via vCenter, and clear the error
manually.

**ISSUE:**

**#131558198:** PowerShell client for cloud to cloud Runbook reports errors
when running on PowerShell 3.0

**Workaround:** Upgrade to PowerShell 4.0

**ISSUE:**

**#131533056:** When migrating RHEL 7.4 from AWS to Google Cloud, Google Cloud
agent will not be installed automatically.

**Workaround:** Manually remove the AWS agent and install Google Cloud agent

**ISSUE:**

**#131532713:** After Offline Migration of Windows 2003R2, if a NIC is
manually deleted, it may be impossible to auto-detect and automatically
reinstall it.

**Workaround:** The VM storage can be attached to a different VM, and the NIC
Registry entry could be imported manually using a similar VM as a reference.
Contact support for assistance.

**ISSUE:**

**#131532666:** Linux versions running with kernel version 2.6.32 may
experience a kernel panic on ephemeral storage access failures; these are more
likely while streaming over iSCSI.

**Workaround:** Upgrade your kernel. The issue will also reduce in likelihood
after Detach.

**ISSUE:**

**#131532846:** Certain firewalls and anti-viruses may cause Windows VMs to
fail when moved to cloud by blocking iSCSI traffic.

**Workaround:** Disable the affecting service while migrating and reinstall
after Detach.

**ISSUE:**

**#131532882:** In certain cases, initiating Run in Cloud during a Windows
update may cause the update to terminate abruptly and cause a failure to boot
in the cloud.

**Workaround:** Allow the system to finish Windows update and/or suspend
Windows updates before migrating.

**ISSUE:**

**#135664281:** When completing or canceling Azure to Google Cloud migration,
if Velostrata Management failed to start the importer, Velostrata-created
resources may be left in the original instance's resource group.

**ISSUE:**

**#133137658:** Scenario: No network connection between Migration Manager and
VSphere

Customer Impact: RunInCloud task will stay stuck due to failure in call to
getReadSessions on VSphere.

**Workaround** : Fix the network connection. If not, cancel the task and try
again.

**ISSUE:**

**#135573857** Scenario: When moving a VM back on-prem with "force" flag,
failure to consolidate snapshot will cause the VM to remain as managed by
Velostrata. RunInCloud on the same VM may fail since it is not allowed on
managed VMs.

* **_Workaround:_ ** * Wait a couple of minutes and try again. 

**ISSUE:**

**#137082702:** In rare cases, the Cancel detach operation succeeds but the VM
instance will fail to start.

**Workaround** : Move the instance back and move it again to the cloud.

##  September 06, 2019

4.5.0

**CHANGED:**

For a list of builds for this release and others, see the [ Build History
](https://cloud.google.com/migrate/compute-engine/docs/build-history)

**FEATURE:**

####  Azure to Google Cloud migration (Beta)

Version 4.5 introduces beta support for Azure to Google Cloud migration. You
can migrate VMs to Azure using Waves migration. Please note that in this
version, a storage account is used per each VM migrated from Azure to Google
Cloud, which, pending on the storage account usage in your subscription, may
limit the amount of concurrent migration you can do.

**FEATURE:**

####  Migration of UEFI VMs to Google Cloud and Shielded VMs

Version 4.5 introduces support for migration of UEFI-based VMs from on-prem to
Google Cloud. The system will automatically migrate UEFI-based VMs to Google
Cloud UEFI-enabled hosts. In addition, you can enable activation of the
Shielded VMs secure boot feature in the runbook specs for waves.

**FEATURE:**

####  Windows 2019

Version 4.5 introduces support for migrating Windows 2019 OS to Google Cloud.

Note that when migrating Windows 2019 from Azure or AWS to Google Cloud, you
will need to explicitly add the license tag of Windows 2019 in the Runbook
file.

####  Requirements and OS Support

See [ Requirements ](https://cloud.google.com/migrate/compute-
engine/docs/4.5/concepts/requirements) and [ Supported operating systems
](https://cloud.google.com/migrate/compute-
engine/docs/4.5/reference/supported-os-versions) .

**ISSUE:**

**#131532690:** Run-in-cloud and migration operations may fail for Windows
Server 2016 workload when Symantec Endpoint Protection (SEP) is installed.
This may also happen when SEP appears to be disabled.

**Workaround:** Modify workload Network interface bindings to remove the SEP
option.

  1. Download [ Microsoft Network VSP Bind (nvspbind) ](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850)
  2. Install Microsoft_Nvspbind_package.EXE into c:\temp. 
  3. Open a command prompt as an Administrator and run the following: 

` nvspbind.exe /d * symc_teefer2 `

**ISSUE:**

**#131614405:** When the Velostrata Prep RPM is installed on SUSE Linux
Enterprise Server 11, the VM obtains a DHCP IP address in addition to an
existing static IP configuration. This issue occurs when the VM is started on-
premises in a subnet that is enabled with DHCP services.

**Note:** The issue does not occur when the subnet has no DHCP services. There
is no connectivity impact for communications with the original static IP
address.

**ISSUE:**

**#131548730:** In some cases, when a VM is moved to Run-in-Cloud while a 3rd
party VM-level backup solution holds a temporary snapshot, the Migrate for
Compute Engine periodic write-back operations will not complete even after the
backup solution deletes the temporary snapshot. The uncommitted writes counter
on the VM will show an increasing size and no consistency checkpoint will be
created on-premises.

**Workaround:** Select the Run On-Premises action for the VM and wait for the
task to complete, which will commit all pending writes. Then select the Run-
in-Cloud action again. Note that committing many pending writes may take a
while. Do not use the Force option as this will result in the loss of the
uncommitted writes.

**ISSUE:**

**#131637800:** After registering the Velostrata plug-in, running the Cloud
Extension wizard might generate an error "XXXXXXXXXX" upon "Finish".

**Workaround:** Un-register the Velostrata plug-in and restart the vSphere Web
client service, then re-register the plug-in. Contact support if the issue
persists.

**ISSUE:**

**#131605387:** vCenter reboot causes Velostrata tasks in vCenter to disappear
from UI. This is a vCenter limitation.

**Workaround:** Use the Velostrata PowerShell module to monitor Velostrata
managed VMs or Cloud Extensions tasks that are currently running.

**ISSUE:**

**#131638716:** With an ESXi host in maintenance mode, if a VM is moved to
cloud, the operation will fail and get stuck in the rollback phase.

**Workaround:** Manually cancel the Run-in-Cloud task, migrate the VM to
another ESXi host in the cluster and retry the Run-in-Cloud operation.

**ISSUE:**

**#131638455:** A Run-in-Cloud operation fails with the error - "Failed to
create virtual machine snapshot. The attempted operation cannot be performed
in the current state (Powered off)".

**Workaround:** The VMware VM snapshot file may be pointing to a non-existent
snapshot. Contact support for assistance in correcting the issue.

**ISSUE:**

**#131534862:** In rare cases, after running a Workload back on-premises -
Workload VMDK's are locked. In certain cases, this is due to network
disruptions between the Velostrata management appliance and the ESXi host on
which the workload is running.

**Note:** The issue will resolve itself after 1-2 hours.

**ISSUE:**

**#131550214:** During Detach, the operation might fail with the following
error message: "Operation was canceled".

**Workaround:** Retry the Detach operation.

**ISSUE:**

**#131650367:** When performing a detach after a cancel detach operation, the
action may fail.

**Workaround:** Retry the operation.

**ISSUE:**

**#131649978:** In the event of certain system failures, Velostrata components
disconnect from vCenter. In this case, an event may not be sent, resulting in
the alarm either not being set properly or not being cleared properly.

**Workaround:** Clear the alarm manually in vCenter.

**ISSUE:**

**#131532549:** For workloads with a Windows machine using a retail license,
when returning from the cloud, the license is not present.

**Workaround:** Reinstall the license.

**ISSUE:**

**#131555885:** vCenter "Export OVA" operation is available when the VM in
cloud is running in cache mode, however, this operation results in a corrupted
OVA.

**Workaround:** Only create OVA after the detach.

**ISSUE:**

**#131647857:** In rare cases, when a cloud component instance is created and
system fails before it is tagged, the instance will remain untagged. This will
not allow full clean-up or repair of the CE.

**Workaround:** Manually tag the instance, and then run "Repair".

**ISSUE:**

**#131537125:** Cloud Extension high availability does not work for workloads
running Ubuntu OS with LVM configuration.

**Workaround:** Update the kernel to 3.13.0-161 or higher.

**ISSUE:**

**#131560126:** Suse12: Due to a bug in SUSE kernel older than 4.2,
configurations that include BTRFS mounts with subvolumes are not supported.

**Workaround:** Upgrade to SUSE version with Kernel >=4.2 (SP2).

**ISSUE:**

**#131533480:** When using the Create Cloud Extension wizard, using an illegal
HTTP proxy address will not generate a warning message.

**Workaround:** Delete the CE and then create the CE with a valid HTTP proxy
address.

**ISSUE:**

**#131647654:** Run on-premises operation succeeded but the status is marked
as failed with error "Failed to consolidate snapshots"

**Workaround:** Consolidate snapshots via vCenter, and clear the error
manually.

**ISSUE:**

**#131558198:** PowerShell client for cloud to cloud Runbook reports errors
when running on PowerShell 3.0

**Workaround:** Upgrade to PowerShell 4.0

**ISSUE:**

**#131533056:** When migrating RHEL 7.4 from AWS to Google Cloud, Google Cloud
agent will not be installed automatically.

**Workaround:** Manually remove the AWS agent and install Google Cloud agent

**ISSUE:**

**#131532713:** After Offline Migration of Windows 2003R2, if a NIC is
manually deleted, it may be impossible to auto-detect and automatically
reinstall it.

**Workaround** : The VM storage can be attached to a different VM, and the NIC
Registry entry could be imported manually using a similar VM as a reference.
Contact support for assistance.

**ISSUE:**

**#131532666:** Linux versions running with kernel version 2.6.32 may
experience a kernel panic on ephemeral storage access failures; these are more
likely while streaming over iSCSI.

**Workaround** : Upgrade your kernel. The issue will also reduce in likelihood
after Detach.

**ISSUE:**

**#131532846:** Certain firewalls and anti-viruses may cause Windows VMs to
fail when moved to cloud by blocking iSCSI traffic.

**Workaround:** Disable the affecting service while migrating and reinstall
after Detach.

**ISSUE:**

**#131532882:** In certain cases, initiating Run in Cloud during a Windows
update may cause the update to terminate abruptly and cause a failure to boot
in the cloud.

**Workaround:** Allow the system to finish Windows update and/or suspend
Windows updates before migrating.

**ISSUE:**

**#135664281:** When completing or canceling Azure to Google Cloud migration,
if Velostrata Management failed to start the importer, Velostrata-created
resources may be left in the original instance's resource group.

**ISSUE:**

**#133137658:** Scenario: No network connection between Migration Manager and
VSphere

Customer Impact: RunInCloud task will stay stuck due to failure in call to
getReadSessions on VSphere.

**Workaround** : Fix the network connection. If not, cancel the task and try
again.

**ISSUE:**

**#135573857** Scenario: When moving a VM back on-prem with "force" flag,
failure to consolidate snapshot will cause the VM to remain as managed by
Velostrata. RunInCloud on the same VM may fail since it is not allowed on
managed VMs.

* **_Workaround:_ ** * Wait a couple of minutes and try again. 

**ISSUE:**

**#137082702:** In rare cases, the Cancel detach operation succeeds but the VM
instance will fail to start.

**Workaround** : Move the instance back and move it again to the cloud.

