This version is deprecated and its documentation will be removed soon. See the
[ current version ](/migrate/compute-engine/docs/) for the latest
documentation.

#  Release Notes

This page documents production updates to Velostrata. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/velostrata-release-notes.xml `

##  Velostrata V4.0 Release Notes

###  New features

####  Migration Waves management

Velostrata V4.0 introduces Migration Wave management in the Velostrata Manager
web UI. A Migration Wave is a construct to organize a set of source virtual
machines and their target specifications, using runbooks. With Migration
Waves, administrators can perform and monitor multiple migration actions on
the set without having to upload a Runbook for each action as in previous
versions of Velostrata.

New or enhanced features of [ Migration Waves ](/migrate/compute-
engine/docs/4.0/how-to/organizing-migrations/overview) allow you to:

  1. [ Create a wave ](/migrate/compute-engine/docs/4.0/how-to/organizing-migrations/creating-and-modifying-runbooks) by querying your VM inventory 
  2. [ Perform migration ](/migrate/compute-engine/docs/4.0/how-to/organizing-migrations/overview#performing_operations_on_migration_waves) operations on a wave 
  3. [ Validate ](/migrate/compute-engine/docs/4.0/how-to/organizing-migrations/creating-and-modifying-runbooks#validating_a_runbook) runbooks 
  4. [ Monitor ](/migrate/compute-engine/docs/4.0/how-to/organizing-migrations/monitoring-waves-runbooks-jobs) Wave activity 
  5. View a [ history of jobs ](/migrate/compute-engine/docs/4.0/how-to/organizing-migrations/monitoring-waves-runbooks-jobs) run on the wave 
  6. View [ detailed logs ](/migrate/compute-engine/docs/4.0/how-to/organizing-migrations/monitoring-waves-runbooks-jobs) for VMs within the wave 

For detailed instructions on how to use the new features, see [ Organizing
migrations with waves ](/migrate/compute-engine/docs/4.0/how-to/organizing-
migrations/overview) .

####  Deployment of Velostrata Manager on Google Cloud via Cloud Marketplace

Velostrata V4.0 Manager deployment is now available via [ Google Cloud
Marketplace's
](https://console.cloud.google.com/marketplace/browse?q=Velostrata) Click-to-
Deploy feature, offering wizard-based configuration.

####  AWS -> GCP instance rightsizing

Velostrata V4.0 introduces support for instance right sizing recommendation
when migrating VMs from AWS EC2 to Google Cloud.

####  Option to convert migrated enterprise Linux from BYOL to GCP Premium
Licenses

Velostrata V4.0 supports automatic conversion of migrated RHEL (6.x/7.x) and
SLES (11.x/12.x) from BYOL licenses to GCP premium licenses (Pay As You Go).
This is available by setting the [ OS license ](/migrate/compute-
engine/docs/4.0/reference/runbooks) field in your runbook.

###  Compatibility

####  ESXi, vCenter Server, and vSphere Web Client compatibility

This Velostrata release is compatible with VMware versions:

  * vCenter: 5.5U1, 6.0U1, 6.5, 6.5U1, 6.7 
  * ESXi: 5.5U1, 6.0 U1, 6.5, 6.7 

**Note:** vCenter is a required component in a deployment.  
Note: 5.0 and 5.1 may be used in certain configurations; contact support for
details.

####  Web browser compatibility

The latest versions of the Chrome, Internet Explorer, Firefox, and Safari Web
browsers are known to be compatible with the Velostrata vCenter Web Client
plugin.  
The vCenter Web Client uses the Adobe Flash extension in your browser.
Velostrata recommends that the Flash plug-in for your browser be updated to
the latest version (19.0.0.245 or later).  
To check your current Flash player version, go to [
http://www.adobe.com/software/flash/about/.
](http://www.adobe.com/software/flash/about/)

####  Virtual machine compatibility

Virtual Machines configured with BIOS virtual firmware are supported. In
addition, UEFI virtual firmware is supported via conversion to BIOS firmware.  
Velostrata makes use of snapshots. Virtual Machine disks in Dependent mode
(default) and Virtual RDM mode are supported with full functionality.

####  Guest Operating System compatibility for 4.0:

Supported Windows versions:

  * Windows Server 2008 (32 and 64 bit) 
  * Windows Server 2008 R2 SP1 or higher. 
  * Windows Server 2012/Windows Server 2012 R2. 
  * Windows 2016 
  * Windows server 1709 

Supported Windows versions with offline migration (see further details in [
Using Offline Migration ](/migrate/compute-engine/docs/4.0/how-to/prepare-vms-
servers/using-offline-migration) ):

  * Windows Server 2003, Windows Server 2003R2 
  * Windows Server 2008 32 bit (contact support for assistance) 

Supported Linux distributions and versions:

  * CentOS 6.4+ 
  * CentOS 7 
  * RHEL 6.4+ 
  * RHEL 7 
  * Debian 8.5+ 
  * Debian 9 
  * Ubuntu 14 
  * Ubuntu 16 
  * Ubuntu 18 
  * Suse 11 SP3+ 
  * Suse 12 SP2+ 
  * Suse 15 beta 

Supported Linux versions in offline migration (see further details in [ Using
Offline Migration ](/migrate/compute-engine/docs/4.0/how-to/prepare-vms-
servers/using-offline-migration) ):

  * Ubuntu 12.x 

###  Fixed issues

**FIXED:**

**#6095:** RHEL-7.5_HVM_GA-20180322-x86_64-1-Hourly2-GP2 (ami-7c491f05) based
instance migrated from AWS to GCP will not boot on GCP.

**FIXED:**

**#6026:** In rare cases Ubuntu based instance may hang at first boot in
cloud.

**FIXED:**

**#6024:** When login to the System Setting section in the Web UI with
"apiuser" the system returns 403.

**FIXED:**

**#5974:** In certain environments with high latency between Velostrata
Management appliance and vCenter, restarting the Velostrata Management
appliance may cause VMs in cloud and their migration to get stuck.

###  Known limitations

  1. VMware virtual disk consolidation warning: when write-back consistency checkpoints are persisted in the vSphere Datastore on-premises, a snapshot rotation and virtual disk consolidation is performed. During consolidation, the virtual machine has an event showing that its disks require consolidation. This status is temporary and resolves automatically when consolidation triggered by Velostrata has completed. A similar behavior occurs when moving a virtual machine to run back on-premises. 
  2. Typical storage throughput per virtual disk - Due to vSphere Storage API limitations, throughput achieved on-premises per VMDK limited to about 20-30Mbytes/sec. When workloads are highly concentrated into a single virtual disk, the initial performance seen in the cloud may be limited due to an increase in storage access latency back on-premises. This situation typically resolves itself within minutes, as soon as an active working set is established in the Velostrata cache, in the cloud. 
  3. Maximum concurrent read sessions per ESX host - Due to vSphere Storage API limitations, the number of storage access sessions per ESX host is constrained. For virtual machines that are actively running in the cloud, Velostrata enforces a limit of up to 60 VMDKs or RDMs per ESX host. Multiple ESX hosts may be used. Given that these virtual machines are not actually executing on the ESX hosts, these hosts can be of minimal specs. 
  4. Virtual Machine disks in Independent mode (persistent and non-persistent) and Physical RDM mode are supported with limited functionality; contact Velostrata Support for details if used. 
  5. IDE virtual disks are currently not supported. Change the virtual disk type to SCSI to enable migration to cloud. 
  6. Free space on source datastore - Write back activity for a VM running in the cloud is temporarily paused when the vSphere Datastore's free capacity is lower than 10%, and a vCenter alarm is raised to indicate of the issue. Write back will resume automatically as space is freed up on the datastore 

**Workaround:** Monitor the Uncommitted Writes counter and correlate it to
low-disk space events from the vSphere datastore. When write back is put on-
hold, the Uncommitted Writes graph indicates a growing count for longer
periods.

###  Known Issues

**ISSUE:**

**#4266:** Run-in-cloud and migration operations may fail for Windows Server
2016 workload when Symantec Endpoint Protection (SEP) is installed. This may
also happen when SEP appears to be disabled.  
**Workaround:** Modify workload Network interface bindings to remove SEP
option. Download [ Microsoft Network VSP Bind (nvspbind)
](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850) ,
Install Microsoft_Nvspbind_package.EXE into c:\temp. , Open Command prompt as
an Administrator, and run the following: `nvspbind.exe /d* symc_teefer2`.

**ISSUE:**

**#1257:** When Velostrata Prep RPM is installed on a SUSE Linux Enterprise
Server 11, the VM obtains a DHCP IP address in addition to an existing static
IP configuration. This issue occurs when the VM is started on-premises in a
subnet that is enabled with DHCP services.  
Note: The issue does not occur when the subnet has no DHCP services. There is
no connectivity impact for communications with the original static IP address.

**ISSUE:**

**#1027:** In some cases, when a VM is moved to Run-in-Cloud while a 3rd party
VM-level backup solution holds a temporary snapshot, the Velostrata periodic
write-back operations will not complete even after the backup solution deletes
the temporary snapshot. The uncommitted writes counter on the VM will show an
increasing size and no consistency checkpoint will be created on-premises.  
**Workaround:** Select the Run On-Premises action for the VM and wait for the
task to complete, which will commit all pending writes. Then select the Run-
in-Cloud action again. Note that committing many pending writes may take a
while. Do not use the Force option as this will result in the loss of the
uncommitted writes.

**ISSUE:**

**#1745:** After registering the Velostrata plug-in, running the Cloud
Extension wizard might generate an error "XXXXXXXXXX" upon "Finish".  
**Workaround:** Un-register the Velostrata plug-in and restart the vSphere Web
client service, then re-register the plug-in. Contact support if the issue
persists.

**ISSUE:**

**#1667:** vCenter reboot causes Velostrata tasks in vCenter to disappear from
UI. This is a vCenter limitation.  
**Workaround:** Use the Velostrata PowerShell module to monitor Velostrata
managed VMs or Cloud Extensions tasks that are currently running.

**ISSUE:**

**#1951:** With an ESXi host in maintenance mode, if a VM is moved to cloud,
the operation will fail and get stuck in the rollback phase.  
**Workaround:** Manually cancel the Run-in-Cloud task, migrate the VM to
another ESXi host in the cluster and retry the Run-in-Cloud operation.

**ISSUE:**

**#1917:** A Run-in-Cloud operation fails with the error - "Failed to create
virtual machine snapshot. The attempted operation cannot be performed in the
current state (Powered off)".  
**Workaround:** The VMware VM snapshot file may be pointing to a non-existent
snapshot. Contact support for assistance in correcting the issue.

**ISSUE:**

**#1808:** In rare cases, after running a Workload back on-premises - Workload
VMDK's are locked. In certain cases, this is due to network disruptions
between the Velostrata management appliance and the ESXi host on which the
workload is running.  
Note: The issue will resolve itself after 1-2 hours.

**ISSUE:**

**#2736:** During Detach, the operation might fail with the following error
message "Operation was canceled".  
**Workaround:** Retry the Detach operation.

**ISSUE:**

**#3775:** When performing a detach after a cancel detach operation, the
action may fail.  
**Workaround:** Retry the operation.

**ISSUE:**

**#3682:** In the event of certain system failures, Velostrata components
disconnect from vCenter. In this case, an event may not be sent, resulting in
the alarm either not being set properly or not being cleared properly.  
**Workaround:** Clear the alarm manually in vCenter.

**ISSUE:**

**#3320:** For workloads with Windows machine using a retail license, when
returning from the cloud, the license is not present.  
**Workaround:** Reinstall the license.

**ISSUE:**

**#3281:** vCenter "Export OVA" operation is available when the VM in cloud is
running in cache mode, however, this operation results in a corrupted OVA.  
**Workaround:** Only create OVA after the detach.

**ISSUE:**

**#3142:** In rare cases, when a cloud component instance is created and
system fails before it is tagged, the instance will remain untagged. This will
not allow full clean-up or repair of the CE.  
**Workaround:** Manually tag the instance, and then run "Repair".

**ISSUE:**

**#4604:** Cloud Extension high availability does not work for workloads
running Ubuntu OS with LVM configuration.  
**Workaround:** Update the kernel to 3.13.0-161 or higher.

**ISSUE:**

**#3199:** Suse12: Due to a bug in SUSE kernel older than 4.2, configurations
that include BTRFS mounts with subvolumes are not supported.  
**Workaround:** Upgrade to SUSE version with Kernel >=4.2 (SP2).

**ISSUE:**

**#4619:** Velostrata telemetry configuration for frontend will not update
after backend changes.  
**Workaround:** Contact technical support to update the FE telemetry
configuration.

**ISSUE:**

**#3570:** When using the Create Cloud Extension wizard, using illegal http
proxy address will not generate a warning message.  
**Workaround:** Delete the CE and then create the CE with a valid http proxy
address.

**ISSUE:**

**#3133:** Run on-premises operation succeeded but the status is marked as
failed with error "Failed to consolidate snapshots"  
**Workaround:** Consolidate snapshots via vCenter, and clear the error
manually.

**ISSUE:**

**#5547:** PowerShell client for cloud to cloud Runbook reports errors when
running on PowerShell 3.0  
**Workaround:** Upgrade to PowerShell 4.0

**ISSUE:**

**#5709:** When migrating RHEL 7.4 from AWS to GCP, GCP agent will not be
installed automatically.  
**Workaround:** Manually remove the AWS agent and install GCP agent

