You're viewing documentation for a prior version of Migrate for Compute Engine
(formerly Velostrata). You can continue using this version, or use the [
current version ](/migrate/compute-engine/docs) .

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

##  4.2

###  Build history

Build number  |  Release date  |  Description  
---|---|---  
24499  |  April 15, 2019  |  Initial release.  
25715  |  June 13, 2019  |  This build fixes an issue in which detach or
prepare to detach tasks would hang, then eventually fail.

If you're using a version 4.2 build prior to 25715, you can fix this issue by
applying the hotfix described in [ Velostrata v4.2 Hotfix #135093085
](https://storage.googleapis.com/velostrata-
release/V4.2.0/4.2%20Revision%20Hot%20Fix%20135093085/Velostrata%20V4.2%20Hotfix%20%23135093085.pdf)
.  
  
###  New features

####  Migration to Sole Tenants

**FEATURE:**

Velostrata 4.2 introduces migration to [ Compute Engine Sole Tenant Nodes
](/compute/docs/nodes) . After [ creating nodes ](/compute/docs/nodes/create-
nodes) on Compute Engine, Velostrata handles migration to [ Sole Tenants
](/migrate/compute-engine/docs/4.2/how-to/organizing-migrations/sole-tenant-
nodes) using Waves.

####  Windows Bring Your Own License (BYOL)

**FEATURE:**

Velostrata 4.2 introduces support for [ migration to Compute Engine
](/migrate/compute-engine/docs/4.2/how-to/organizing-migrations/sole-tenant-
nodes) with [ Windows BYOL ](/compute/docs/instances/windows/bring-your-own-
license/bringing-your-own-license-sole-tenant-nodes) . Because of common
licensing considerations, we recommend to migrating VMs with Windows BYOL to
sole tenant nodes.

####  Integration with Google Cloud's operations suite

**FEATURE:**

Velostrata 4.2 can now send [ logs ](/migrate/compute-engine/docs/4.2/how-
to/monitoring/using-stackdriver-monitoring) and [ telemetry data
](/migrate/compute-engine/docs/4.2/how-to/monitoring/viewing-stackdriver-logs)
to Google Cloud's operations suite. You can [ enable or disable logs and
telemetry ](/migrate/compute-engine/docs/4.2/how-to/monitoring/disabling-
stackdriver) data sent to Google Cloud's operations suite at any point in
time.

####  Requirements and OS Support

See [ Requirements ](/migrate/compute-engine/docs/4.2/concepts/requirements)
and [ Supported operating systems ](/migrate/compute-
engine/docs/4.2/reference/supported-os-versions) .

###  Known Issues

**ISSUE:**

**#4266:** Run-in-cloud and migration operations may fail for Windows Server
2016 workload when Symantec Endpoint Protection (SEP) is installed. This may
also happen when SEP appears to be disabled.  
**Workaround:** Modify workload Network interface bindings to remove SEP
option. Download [ Microsoft Network VSP Bind (nvspbind)
](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850) ,
Install Microsoft_Nvspbind_package.EXE into c:\temp. , Open Command prompt as
an Administrator, and run the following: `nvspbind.exe /d * symc_teefer2`.

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

