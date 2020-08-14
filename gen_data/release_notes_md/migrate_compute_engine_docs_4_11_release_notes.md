#  Release Notes

This page documents production updates to Migrate for Compute Engine. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/migrategce-release-notes.xml `

For a list of builds for this release and others, see the [ Build history
](/migrate/compute-engine/docs/build-history) .

##  Requirements and OS Support

See [ Requirements ](/migrate/compute-engine/docs/4.11/concepts/requirements)
and [ Supported operating systems ](/migrate/compute-
engine/docs/4.11/reference/supported-os-versions) .

##  4.11 new features

###  Google Cloud Secret Manager password and encryption key management

**FEATURE:**

V4.11 offers integration with Secret Manager. You can store Migrate for
Compute Engine password and encryption key as objects in secret manager to
provide a higher level of security and control. See [ Configuring the
migration manager ](/migrate/compute-engine/docs/4.11/how-to/configure-
manager/configuring-migration-manager) for more.

###  Windows 2008R2 to Windows 2012R2 upgrade with BYOL

**FEATURE:**

V4.11 introduces Windows upgrade with bring-your-own-license (BYOL) feature.
Migrating Windows Server 2008R2 with a customer owned license (BYOL) can
upgrade to Windows Server 2012R2 using BYOL as part of the migration process.
See [ Upgrading Windows Server VMs ](/migrate/compute-engine/docs/4.11/how-
to/upgrading-vms/upgrading-windows-vms) for more.

###  Automatic enablement of OS patch management service in migrating VMs

**FEATURE:**

V4.11 introduces automatic deployment of Google Cloud OS Config agent to
migrating VMs. This allows you to get insights on your migrated VM patch
status and automate deployment of software patches to migrated VMs. See [
Adapting VMs to run on Google Cloud ](/migrate/compute-
engine/docs/4.11/concepts/planning-a-migration/vm-adaptations) for more.

###  Reduced network connectivity requirements

**FEATURE:**

Migrate Backend network connectivity requirement to Migrate Manager and Cloud
Extensions have been reduced, all traffic on this channel is performed over
port 443 (HTTPS and TLS) instead of using port 9111. See [ Network access
requirements ](/migrate/compute-engine/docs/4.11/concepts/planning-a-
migration/network-access-requirements) for more.

###  Usability enhancements

**FEATURE:**

Usability enhancements in the following flows:

  * Automatic adjustments of VDDK max open sessions when accessing vSphere V6.5 to avoid overloading VDDK max connections limit. 
  * Support for vCenter certificate update flow. 
  * Enhancement of automatic license assignment feature to offline migration flow. 

##  4.11 Known Issues

**ISSUE:**

**#160405343:** Due to a [ change in behavior
](https://www.suse.com/support/kb/doc/?id=000019633) on the activation flow
for SUSE, configuring repositories on SUSE Enterprise Linux instances post-
detach now fail.

**Workaround:** The following workaround can be used prior to detach (either
before migration or before detach).

  1. Follow the instructions described for Situation 4 at [ https://www.suse.com/support/kb/doc/?id=000019633 ](https://www.suse.com/support/kb/doc/?id=000019633) to download the required packages for Compute Engine as a tar.gz file. 
  2. **For SLES 12.x** , then run the following commands: 
    
        sha1sum late_instance_offline_update_gce_SLE12.tar.gz
    tar -xf late_instance_offline_update_gce_SLE12.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm

  3. **For SLES 15.x** , then run the following commands: 
    
        sha1sum late_instance_offline_update_gce_SLE15.tar.gz
    tar -xf late_instance_offline_update_gce_SLE15.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm

**ISSUE:**

**#149004085:** Ubuntu 14 from on-premise may fail to start networking post
detach.

**Workaround:** Connect via the serial console and manually add the network
interface with DHCP.

**ISSUE:**

**#145086776:** In rare cases, older versions of RHEL7 may hang during
streaming or reach a Kernel panic. This issues were resolved in later versions
of RHEL7.

**Workaround:** Run ` sudo yum update ` before migrating to update the system.

**ISSUE:**

**#145644737:** Clones created on Azure or AWS from instances of Linux
distributions that use cloud-init may experience issues in booting after
installing the Linux prep package.

**Workaround:** Uninstall the package before cloning and reinstall when
preparing to migrate.

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
    
        nvspbind.exe /d * symc_teefer2

**ISSUE:**

**#131614405:** When the Velostrata Prep RPM is installed on SUSE Linux
Enterprise Server 11, the VM obtains a DHCP IP address in addition to an
existing static IP configuration. This issue occurs when the VM is started on-
premises in a subnet that is enabled with DHCP services.

Note: The issue does not occur when the subnet has no DHCP services. There is
no connectivity impact for communications with the original static IP address.

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

Note: The issue will resolve itself after 1-2 hours.

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

Workaround: The VM storage can be attached to a different VM, and the NIC
Registry entry could be imported manually using a similar VM as a reference.
Contact support for assistance.

**ISSUE:**

**#131532666:** Linux versions running with kernel version 2.6.32 may
experience a kernel panic on ephemeral storage access failures; these are more
likely while streaming over iSCSI.

Workaround: Upgrade your kernel. The issue will also reduce in likelihood
after Detach.

**ISSUE:**

**#131532846:** Certain firewalls and anti-viruses may cause Windows VMs to
fail when moved to cloud by blocking iSCSI traffic.

Workaround: Disable the affecting service while migrating and reinstall after
Detach.

**ISSUE:**

**#131532882:** In certain cases, initiating Run in Cloud during a Windows
update may cause the update to terminate abruptly and cause a failure to boot
in the cloud.

Workaround: Allow the system to finish Windows update and/or suspend Windows
updates before migrating.

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

**Workaround:** Wait a couple of minutes and try again.

**ISSUE:**

**#137082702:** In rare cases, the Cancel detach operation succeeds but the VM
instance will fail to start.

**Workaround** : Move the instance back and move it again to the cloud.

