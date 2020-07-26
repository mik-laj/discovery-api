#  Release Notes

This page contains the latest release notes for features and updates to the
Compute Engine service. For older release notes, see [ the archive
](/compute/docs/release-notes-archive) .

**Latest API version: v1**

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/compute-release-notes.xml `

##  July 24, 2020

**FEATURE:**

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones: 

    * Ashburn, Northern Virginia, USA: ` us-east4-b `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus/) .

**FEATURE:**

N2 machines are now available in Northern Virginia ` us-east4-c ` . Read more
information on the [ VM instance pricing
](https://cloud.google.com/compute/vm-instance-pricing#n2_machine_types) page.

##  July 21, 2020

**FEATURE:**

You can now create _balanced persistent disks_ , in addition to standard and
SSD persistent disks. Balanced persistent disks are an alternative to SSD
persistent disks that balance performance and cost. For more information, see
[ Persistent disk types
](https://cloud.google.com/compute/docs/disks/index#disk-types) .

##  July 17, 2020

**FEATURE:**

The Organization Policy for [ restricting protocol forwarding creation
](https://cloud.google.com/compute/docs/protocol-
forwarding#enforcing_protocol_forwarding_settings_across_a_project_folder_or_organization)
has launched into **Beta** .

##  July 16, 2020

**CHANGED:**

SSD persistent disks on certain machine types now have a maximum write
throughput of 1,200 MB/s. To learn more about the requirements to reach these
limits, see [ Block storage performance
](https://cloud.google.com/compute/docs/disks/performance#size_price_performance)
.

**FEATURE:**

You can now [ suspend and resume
](https://cloud.google.com/compute/docs/instances/suspend-resume-instance)
your VM instances. This feature is available in **Beta** .

##  July 06, 2020

**FEATURE:**

E2 machine types now offer up to 32 vCPUs. See [ E2 machine types
](https://cloud.google.com/compute/docs/machine-types#e2_machine_types) for
more information.

##  June 26, 2020

**FEATURE:**

To support a wide variety of BYOL scenarios, you can now [ configure VMs to
live migrate within a sole-tenant node group during host maintenance events
](https://cloud.google.com/compute/docs/nodes/bringing-your-own-licenses) .
This is **Generally Available** .

##  June 22, 2020

**FEATURE:**

N2D machine types are now available in Belgium, europe-west1, in all three
zones. Read more information on the [ VM instance pricing
](https://cloud.google.com/compute/vm-instance-pricing#n2d_machine_types)
page.

##  June 15, 2020

**FEATURE:**

[ New sole-tenant node types (c2-node-60-240, n1-node-96-1433, and
n2d-node-224-896) ](https://cloud.google.com/compute/docs/nodes#node_types)
are available in **Beta** .

##  June 08, 2020

**FEATURE:**

The ` asia-southeast2 ` Jakarta, Indonesia region is now available to all
projects and users. The zones in the ` asia-southeast2 ` region have [ E2 and
N1 machine types ](https://cloud.google.com/compute/docs/machine-types) . See
[ Regions and zones ](https://cloud.google.com/compute/docs/regions-zones) for
more information.

**FEATURE:**

Enhancements to the pre-configured Cloud Monitoring Compute Engine **VM
Instances** dashboard. Compute Engine cross-fleet metrics and detail views
specific to CPU, Disk, Memory, and Network are now available. Use filters to
narrow down the set of VMs being inspected, and use the time selector or in-
chart time selection to change the time window. VMs with the Monitoring agent
installed get detailed memory and disk analysis out of the box.

##  June 05, 2020

**FEATURE:**

[ CPU overcommit on sole-tenant nodes
](https://cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-
vms) lets you overprovision sole-tenant node resources and schedule more VM
CPUs on a sole-tenant node than are normally available. This feature is in
**Beta** .

**FEATURE:**

[ New sole-tenant node types (m1-node-96-1433 and n2-node-80-640)
](https://cloud.google.com/compute/docs/nodes#node_types) are available in
**Beta** .

##  June 01, 2020

**FEATURE:**

NVIDIA® Tesla® T4 GPUs are now available in the following additional regions
and zones:

  * Changua County, Taiwan ` asia-east1-c `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus) .

##  May 21, 2020

**FEATURE:**

E2 shared-core machine types now support committed use discounts in all
regions. See the [ VM instance ](https://cloud.google.com/compute/vm-instance-
pricing#e2_sharedcore_machine_types) pricing page for more information.

**FEATURE:**

You can now SSH to your VMs using hardware-backed SSH key pairs. For more
information, see [ SSH with security keys
](https://cloud.google.com/compute/docs/tutorials/ssh-with-sk) .

##  May 20, 2020

**FEATURE:**

If your managed instance group encountered errors - for example, if a VM could
not be created - you can [ view those errors
](https://cloud.google.com/compute/docs/instance-groups/getting-info-about-
migs#listing_instance_errors) to diagnose and mitigate the cause. This is
**Generally available** .

##  May 19, 2020

**FEATURE:**

Troubleshoot VMs by [ capturing screenshots
](https://cloud.google.com/compute/docs/instances/capturing-vm-screenshots) .
This is in **beta** .

##  May 12, 2020

**FEATURE:**

Automatically manage the size of sole-tenant node groups with the [ sole-
tenant node group autoscaler
](https://cloud.google.com/compute/docs/nodes/node-group-autoscaler) . This is
**Generally Available** .

##  May 11, 2020

**FEATURE:**

You can identify idle persistent disk resources by using [ idle persistent
disk recommendations ](https://cloud.google.com/compute/docs/disks/viewing-
and-applying-idle-pd-recommendations) . Following these recommendations will
help reduce unused resources and reduce your compute bill. This feature is
**Generally available** .

##  April 30, 2020

**CHANGED:**

SSD persistent disks now have increased write throughput limits on instances
with 1 to 15 vCPUs. This improvement applies to SSD persistent disks on all
machine types except C2 machine types. To learn more about the requirements to
reach these limits, see [ Block storage performance
](https://cloud.google.com/compute/docs/disks/performance#size_price_performance)
.

##  April 20, 2020

**FEATURE:**

  * The ` us-west4 ` Las Vegas, Nevada region is now available to all projects and users. The zones in the ` us-west4 ` region have [ N1 and E2 machine types ](https://cloud.google.com/compute/docs/machine-types) . See [ Regions and zones ](https://cloud.google.com/compute/docs/regions-zones) for more information. 

##  April 16, 2020

**FEATURE:**

  * Committed use discount shared billing is now available in **beta** . You can share committed use discounts among all your projects that fall under the same billing account. For more information, see [ Signing up committed use discounts ](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) . 

##  April 15, 2020

**FEATURE:**

You can identify VM instances that are not being used with [ idle VM
recommendations ](https://cloud.google.com/compute/docs/instances/viewing-and-
applying-idle-vm-recommendations) . Use these recommendations to reduce unused
resources and reduce your compute bill. This feature is **Generally
available** .

**FEATURE:**

You can manage, maintain, and view patch compliance for your VM instances
using the OS patch management feature. For more information, see [ OS patch
management ](https://cloud.google.com/compute/docs/os-patch-management) . This
feature is now **Generally available** .

**FEATURE:**

The latest stable version of the OS Config agent is [ ` 20200402.01 `
](https://github.com/GoogleCloudPlatform/osconfig/releases/tag/20200402.01) .
If you were using OS patch management in Beta, you can update the agent on
your existing VMs, see [ Updating the OS Config agent
](https://cloud.google.com/compute/docs/manage-os#update-agent) .

##  April 09, 2020

**FEATURE:**

  * **GA:** [ Compute Engine enables Shielded VM features by default ](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm) . 

##  April 08, 2020

**FEATURE:**

  * You can identify idle persistent disk resources by using [ idle persistent disk recommendations ](https://cloud.google.com/compute/docs/disks/viewing-and-applying-idle-pd-recommendations) . Following these recommendations will help reduce unused resources and reduce your compute bill. This feature is in **Beta** . 

##  April 06, 2020

**FEATURE:**

  * C2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Ashburn, Northern Virginia, USA ` us-east4-b,c `

**FEATURE:**

  * N2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * The Dalles, Oregon, USA ` us-west1-b `
    * Ashburn, Northern Virginia, USA ` us-east4-a `
    * St. Ghislain, Belgium ` europe-west1-d `

**FEATURE:**

  * [ N2D machine types ](https://cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now **Generally Available** . 

##  April 01, 2020

**FEATURE:**

  * You can now define where your VM instances are located relative to each other on the underlying host systems in a Google datacenter. Create a placement policy to locate VM instances close to each other for low latency, or create a policy to spread VM instances out so that they do not share the same infrastructure. See [ Defining instance location within a zone ](https://cloud.google.com/compute/docs/instances/define-instance-placement) to learn more. 

**FEATURE:**

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones: 

    * Frankfurt, Germany: ` europe-west3-b `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus) .

##  March 31, 2020

**FEATURE:**

  * **Beta:** [ Collect diagnostic information from Windows VMs ](https://cloud.google.com/compute/docs/instances/collecting-diagnostic-information) . 

**FEATURE:**

  * C2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Frankfurt, Germany ` europe-west3-a,b `
    * Ashburn, Northern Virginia, USA ` us-east4-a `

**FEATURE:**

  * N2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * The Dalles, Oregon, USA ` us-west1-a `
    * Changua County, Taiwan ` asia-east1-c `

**FEATURE:**

  * M1 megamem machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Eemshaven, Netherlands ` europe-west4-b `

**FEATURE:**

  * M1 ultramem machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Ashburn, Northern Virginia, USA ` us-east4-a `

**FEATURE:**

  * M2 ultramem machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Los Angeles, California, USA ` us-west2-a,c `

##  March 24, 2020

**FEATURE:**

  * Committed use discounts no longer require specific ratios for cores and memory. Now you can create separate committed use discount contracts for either cores or memory. Separating cores and memory provides more flexibility and improved cost optimization. Learn more at [ Purchasing commitments for machine types ](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#purchasecommitment) . 

**FEATURE:**

  * You can [ preserve the names ](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#preserving_instance_names) of your VM instances when rolling out updates in a managed instance group. This is **Generally available** . 

**FEATURE:**

  * You can [ update selected VM instances in a managed instance group ](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#updating_selected_instances) , with minimal disruption and in a controlled way. This is **Generally available** . 

##  March 19, 2020

**FEATURE:**

  * [ E2 machine types ](https://cloud.google.com/compute/docs/machine-types#e2_machine_types) are **Generally available** . 

##  March 16, 2020

**FEATURE:**

  * N2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * London, England UK ` europe-west2-b `

**FEATURE:**

  * C2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * St. Ghislain, Belgium ` europe-west1-c,d `

##  March 11, 2020

**FEATURE:**

  * You can identify VM instances that are not being used with [ idle VM recommendations ](https://cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations) . Use these recommendations to reduce unused resources and reduce your compute bill. This feature is **Beta** . 

**FEATURE:**

  * In **beta** , you can create an instance with 16 or 24 local SSD partitions for 6 TB and 9 TB of local SSD space, respectively. With 24 local SSD partitions, performance can reach a combined total of 2.4 million read IOPS. For more information, see [ 9 TB Local SSD maximum capacity beta ](https://cloud.google.com/compute/docs/disks/local-ssd#capacity_9tb) . 

##  March 09, 2020

**FEATURE:**

  * [ Machine image ](https://cloud.google.com/compute/docs/machine-images) is now available in **beta** . You can use machine images to store configuration, metadata, permission, and data required to create a VM instance in a single resource. 

##  March 05, 2020

**DEPRECATED:**

  * CoreOS Container Linux images will reach their end of life on May 26, 2020. For more information, see [ CoreOS End-Of-Life (EOL) ](https://cloud.google.com/compute/docs/eol/coreOS) . 

##  March 03, 2020

**FEATURE:**

  * You can now create [ E2 machine types ](https://cloud.google.com/compute/docs/machine-types#e2_machine_types) in all [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) . 

##  March 02, 2020

**FEATURE:**

  * You can now [ use the Google Cloud Console to export images to Cloud Storage ](https://cloud.google.com/compute/docs/images/export-image#exporting_an_image_with_a_single_command) . This is **Generally Available** . 

##  February 27, 2020

**FEATURE:**

  * E2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Los Angeles, USA ` us-west2-a,b,c `
    * London, England, UK ` europe-west2-a,b,c `
    * Frankfurt, Germany ` europe-west3-b,c `
    * Tokyo, Japan ` asia-northeast1-a,b,c `
  * N2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Frankfurt, Germany ` europe-west3 a,b `

**FEATURE:**

  * C2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Council Bluffs, Iowa, US ` us-central1-a `

**FEATURE:**

  * M2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Mumbai, India ` asia-south1-a `

**FEATURE:**

  * You can now manage, maintain, and view patch compliance for your VM instances using the OS patch management feature. For more information, see [ OS patch management ](https://cloud.google.com/compute/docs/os-patch-management) . This feature is available in **beta** . 

##  February 24, 2020

**FEATURE:**

  * The ` us-west3 ` Salt Lake City, UT region is now available to all projects and users. The zones in the ` us-west3 ` region have the [ Skylake CPU platform ](https://cloud.google.com/compute/docs/cpu-platforms) . See [ Regions and zones ](https://cloud.google.com/compute/docs/regions-zones) for more information. 

##  February 21, 2020

**FEATURE:**

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones: 

    * Changhua County, Taiwan: ` asia-east1-a `
    * London, England, UK: ` europe-west2-b `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus) .

##  February 19, 2020

**FEATURE:**

  * M2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Northern Virginia ` us-east4-a,b `

**FEATURE:**

  * If you have configured autohealing for your managed instance group, you can [ review the health state ](https://cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#checking_whether_instances_are_healthy) of each VM in the group. This is **Generally Available** . 

##  February 18, 2020

**FEATURE:**

  * N2D machine types are available in beta. N2D machine types are built on top of second generation AMD EPYC Rome processors. They are a great fit for general purpose workloads and for workloads that require high memory bandwidth. Learn more about these [ general purpose machine types ](https://cloud.google.com/compute/docs/machine-types#n2d_machine_types_beta) . 

##  February 13, 2020

**FEATURE:**

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones: 

    * London, England, UK: ` europe-west2-a `
    * Seoul, South Korea: ` asia-northeast3-b,c `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus) .

##  February 12, 2020

**FEATURE:**

  * You can now maintain consistent software configurations across VM instances using guest policies. For more information, see [ OS configuration management ](https://cloud.google.com/compute/docs/os-config-management) . This feature is available in **beta** . 

##  February 11, 2020

**FEATURE:**

  * To support a wide variety of BYOL scenarios, you can now [ configure VMs to live migrate within a sole-tenant node group during host maintenance events ](https://cloud.google.com/compute/docs/instances/windows/bring-your-own-license) . This is available in **Beta** . 

##  February 07, 2020

**FEATURE:**

  * G Suite administrators can now choose whether to include the domain suffix in usernames generated by the OS Login API. For more information, see [ Managing the OS Login API ](https://cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#manage-oslogin-api) . This feature is **Generally Available** . 

##  February 05, 2020

**CHANGED:**

  * Read an [ FAQ ](https://cloud.google.com/compute/docs/nodes/sole-tenancy-accounting-faq) that can help you evaluate whether to classify [ sole-tenant node ](https://cloud.google.com/compute/docs/nodes) payments as capital expenditures (CAPEX) or operational expenditures (OPEX). 

##  February 03, 2020

**FEATURE:**

  * You can build highly available deployments of stateful workloads on VM instances using [ stateful managed instance groups (stateful MIGs) ](https://cloud.google.com/compute/docs/instance-groups/stateful-migs) . A stateful MIG preserves the unique state of each instance (instance name, attached persistent disks, and/or metadata) on machine restart, recreation, autohealing, or update. Stateful MIGs are available in **beta** . 

##  January 31, 2020

**FEATURE:**

  * You can now [ reschedule VMs on, off, or between sole-tenant nodes ](https://cloud.google.com/compute/docs/nodes/vm-tenancy) . This is **Generally Available** . 

**FEATURE:**

  * You can now enable an [ autoscaler ](https://cloud.google.com/compute/docs/nodes/node-group-autoscaler) on your sole-tenant node groups. This is available in **Beta** . 

##  January 24, 2020

**FEATURE:**

  * The ` asia-northeast3 ` Seoul region is now available to all projects and users. The zones in the ` asia-northeast3 ` region have the [ Skylake CPU platform ](https://cloud.google.com/compute/docs/cpu-platforms) . See [ Regions and zones ](https://cloud.google.com/compute/docs/regions-zones) for more information. 

##  January 21, 2020

**FEATURE:**

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional zones: 

    * Tokyo: ` asia-northeast1-c `
    * Singapore: ` asia-southeast1-c `
    * Iowa: ` us-central1-f `
    * Mumbai: ` asia-south1-a `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus) .

**FEATURE:**

  * You can temporarily turn off or restrict managed instance group autoscaling. The autoscaler's configuration remains intact, and all autoscaling activities resume when you turn it on again or lift the restriction. [ Turning off or restricting autoscaling ](https://cloud.google.com/compute/docs/autoscaler/managing-autoscalers#disable_or_restrict_an_autoscaler) for managed instance groups is now **Generally available** . 

##  January 09, 2020

**CHANGED:**

  * NVIDIA® Tesla® T4 GPU prices are reduced in all regions. For more information about the new prices for each region, see [ GPU pricing ](https://cloud.google.com/compute/gpus-pricing) . 

##  December 18, 2019

**FEATURE:**

  * Specifying an image storage location is now **Generally Available** for custom images. Specifying your image storage location helps you meet your regulatory and compliance requirements for data locality as well as your high availability needs by ensuring redundancy across regions. See [ Creating, deleting, and deprecating custom images ](https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) , and [ Creating a Windows image ](https://cloud.google.com/compute/docs/instances/windows/creating-windows-os-image) . 

##  December 17, 2019

**FEATURE:**

  * E2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Iowa ` us-central1-a `

##  December 16, 2019

**CHANGED:**

  * On November 21, 2019, we announced that organizations would be disabled from using nested virtualization by default starting January 31, 2020. This will no longer happen and nested virtualization will be allowed by default. However, we recommend [ explicitly setting your organizational policy ](https://cloud.google.com/compute/docs/instances/enable-nested-virtualization-vm-instances#enable_nested_virt_org) to allow or prevent nested virtualization as a best practice. 

##  December 13, 2019

**FEATURE:**

  * N2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Tokyo ` asia-northeast1-a,b `
    * Singapore ` asia-southeast1-a `
    * Sydney ` australia-southeast1-b `

##  December 11, 2019

**FEATURE:**

  * E2 machine types are available in **beta** . These machine types are ideal for small to medium workloads that require 16 vCPUs or less, no local SSDs, and no GPUs. Learn more about these [ cost-optimized machine types ](https://cloud.google.com/compute/docs/machine-types#e2_machine_types) . 

##  December 10, 2019

**FEATURE:**

  * You can now create VM instances with V100 AND T4 GPUs that support network bandwidths of up to 100 Gbps. See [ Using network bandwidths of up to 100 Gbps ](https://cloud.google.com/compute/docs/gpus/optimize-gpus#high-bandwidth) . This feature is available in **beta** . 

##  November 22, 2019

**FEATURE:**

  * N2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * South Carolina ` us-east1-d `
    * Belgium ` europe-west1-c `
    * London ` europe-west2-c `
    * Sydney ` australia-southeast1-a `

**FEATURE:**

  * Virtual machines with 2 or 4 vCPUs now have a maximum egress rate of 10 Gbps. This feature is now **Generally Available** . For more information, see [ Machine types ](https://cloud.google.com/compute/docs/machine-types) . 

##  November 21, 2019

**BREAKING:**

  * After January 31, 2020, nested virtualization will be disabled by default by an organizational policy. To avoid interruptions to your workloads, [ update the organization policy ](https://cloud.google.com/compute/docs/instances/enable-nested-virtualization-vm-instances#enable_nested_virt_org) to allow nested virtualization. 

##  November 08, 2019

**FEATURE:**

  * N2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * South Carolina ` us-east1-c `
    * Belgium ` europe-west1-b `
    * London ` europe-west2-a `

##  November 06, 2019

**FEATURE:**

  * You can temporarily turn off or restrict managed instance group autoscaling. The autoscaler's configuration remains intact, and all autoscaling activities resume when you turn it on again or lift the restriction. [ Turning off or restricting autoscaling ](https://cloud.google.com/compute/docs/autoscaler/managing-autoscalers#turn_off_or_restrict_an_autoscaler) for managed instance groups is now available in **Beta** . 

##  October 25, 2019

**FEATURE:**

We launched this to GA amazing.

**FEATURE:**

  * As a G Suite admin, you can now complete the following tasks for the OS Login feature: 

    * Enable OS Login using an organization policy. For more information, see [ Setting up an OS Login organization policy ](https://cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#set_org_policy) . 
    * Track interactions with the OS Login API. For more information, see [ Auditing OS Login events ](https://cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#audit-events)

##  October 22, 2019

**FEATURE:**

  * You can attach up to 257 TB of persistent disk storage to each instance. This feature is **Generally available** for most [ machine types ](https://cloud.google.com/compute/docs/machine-types) . 

**FEATURE:**

  * You can issue 100K read I/Os per second on SSD persistent disks. Read the [ persistent disk performance ](https://cloud.google.com/compute/docs/disks#introduction) document for details. 

##  October 21, 2019

**FEATURE:**

  * Increased the per-instance persistent disk write throughput performance for zonal and regional SSD. Read the [ persistent disk performance documentation ](https://cloud.google.com/compute/docs/disks#introduction) for details. 

##  October 07, 2019

**FEATURE:**

  * You can now create a VM instance from a persistent disk snapshot in the API or the ` gcloud ` tool. This feature is now **Generally available** . Read [ Creating a VM instance from a snapshot ](https://cloud.google.com/compute/docs/instances/create-start-instance#createsnapshot) for more information 

##  October 02, 2019

**FEATURE:**

  * OS Inventory Management is now **Generally available** . For more information, read [ Viewing operating system details ](https://cloud.google.com/compute/docs/instances/view-os-details) . 

##  October 01, 2019

**FEATURE:**

  * Importing VM instances using open virtual appliance (OVA) is now **Generally available** . For more information, read [ Importing virtual appliances ](https://cloud.google.com/compute/docs/import/import-ovf-files) . 

##  September 27, 2019

**FEATURE:**

  * N2 machine types are now **Generally Available** . Learn more about [ N2 machine types ](https://cloud.google.com/compute/docs/machine-types#n2_machine_types) . 

##  September 25, 2019

**FEATURE:**

  * The gVNIC virtual network interface is now available in **Beta** . For more information, see [ Creating VM instances that use the gVNIC network interface ](https://cloud.google.com/compute/docs/instances/create-vm-with-gvnic) . 

**DEPRECATED:**

  * The v1beta1 server and v0.1 metadata server endpoints are deprecated and are scheduled for shutdown. For information about transitioning to the v1 metadata server endpoint, see [ Transitioning to the v1 metadata server endpoint ](https://cloud.google.com/compute/docs/storing-retrieving-metadata#transitioning) . 

**FEATURE:**

  * For additional security when connecting to Linux instances, you can now store your host keys as guest attributes. This feature is now in **General availability** , see [ Storing host keys ](https://cloud.google.com/compute/docs/instances/connecting-to-instance#store-host-key) . 

##  September 24, 2019

**FEATURE:**

  * Instances with more than 16 vCPUs have an increased standard persistent disk bandwidth limit of 1200 MB/s for reads and 400 MB/s for writes. Instances with between 8 and 15 vCPUs also have an increased standard persistent disk bandwidth limit of 800 MB/s reads and 400 MB/s for writes. Read the [ Persistent Disk Performance ](https://cloud.google.com/compute/docs/disks/#introduction) page for details. 

##  September 23, 2019

**FEATURE:**

  * N2 machine types are now available in the following regions and zones: 

    * Taiwan ` asia-east1-a ` , ` asia-east1-b `
    * Netherlands ` europe-west4-a `
    * Iowa ` us-central1-f `

**FEATURE:**

  * C2 machine types are now available in following regions and zones: 

    * Singapore ` asia-southeast1-b ` , ` asia-southeast1-c `
    * Netherlands ` europe-west4-a `
    * Los Angeles ` us-west2-a ` , ` us-west2-c `
    * Iowa ` us-central1-f `

##  September 16, 2019

**FEATURE:**

  * C2 machine types are now available in the South Carolina ` us-east1 ` region in all zones. 

##  September 13, 2019

**FEATURE:**

  * Launched support for [ virtual displays ](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display) to **General availability** . 

##  September 04, 2019

**FEATURE:**

  * [ Reserving zonal resources ](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) is now **Generally available** . Reserve VMs, with or without GPUs and local SSD, in a specific zone. 

##  September 03, 2019

**CHANGED:**

  * Renamed ` n1-megamem ` and ` n1-ultramem ` machine types to ` m1-megamem ` and ` m1-ultramem ` respectively. 

**FEATURE:**

  * M1 machine types are now available in Taiwan, London, and Mumbai. 

##  August 26, 2019

**FEATURE:**

  * Larger memory-optimized machine types are now **Generally Available** . Learn more about these [ larger ultramem machine types ](https://cloud.google.com/compute/docs/machine-types#memory-optimized_machine_type_family) . 

##  August 23, 2019

**FEATURE:**

  * N2 machine types are now available in Singapore and in the ` europe-west4-a ` zone in the Netherlands. See [ machine types ](https://cloud.google.com/compute/docs/machine-types) for more information. 

**FEATURE:**

  * C2 machine types are now available in zones in Taiwan, Tokyo, London, and in the ` europe-west4-a ` zone in the Netherlands. See [ machine types ](https://cloud.google.com/compute/docs/machine-types) for more information. 

##  August 13, 2019

**FEATURE:**

  * Specifying an image storage location is now available in **Beta** for custom images. Specifying your image storage location helps you meet your regulatory and compliance requirements for data locality as well as your high availability needs by ensuring redundancy across regions. See [ Creating, deleting, and deprecating custom images ](https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) , and [ Creating a Windows image ](https://cloud.google.com/compute/docs/instances/windows/creating-windows-os-image) . 

**FEATURE:**

  * For additional security when connecting to Linux instances, you can now store your host keys as guest attributes. This feature is now available in **Beta** , see [ Storing host keys ](https://cloud.google.com/compute/docs/instances/connecting-to-instance#store-host-key) . 

##  August 12, 2019

**FEATURE:**

  * Scheduled snapshots for persistent disks are now **Generally Available** . For more information, see [ Creating scheduled snapshots for persistent disk ](https://cloud.google.com/compute/docs/disks/scheduled-snapshots) . 

**FEATURE:**

  * New general-purpose [ N2 machine types ](https://cloud.google.com/compute/docs/machine-types#n2_machine_types) are now available in **Beta** . 

##  July 31, 2019

**FEATURE:**

  * [ Compute-optimized machine types ](https://cloud.google.com/compute/docs/machine-types#c2_machine_types) , are now available in **General Availability** . Applicable [ charges ](https://cloud.google.com/compute/vm-instance-pricing#c2_machine_types) will apply. 

##  July 25, 2019

**FEATURE:**

  * New larger memory-optimized machine types are now available in **Beta** . Learn more about these [ larger ultramem machine types ](https://cloud.google.com/compute/docs/machine-types#memory-optimized_machine_type_family) . 

##  July 17, 2019

**FEATURE:**

  * Memory-optimized commitments are now available in **Beta** . Read about [ Committed Use Discounts ](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) . 

##  July 08, 2019

**FEATURE:**

  * You can now create VMs with [ compute-optimized machine types ](https://cloud.google.com/compute/docs/machine-types#c2_machine_types) , available in **Beta** . Applicable [ charges ](https://cloud.google.com/compute/vm-instance-pricing#c2_machine_types) will apply. 

**FEATURE:**

  * You can now view operating system details for your VM instances using OS Inventory Management. This feature is available in **Beta** . For more information, read [ Viewing operating system details ](https://cloud.google.com/compute/docs/instances/view-os-details) . 

##  July 02, 2019

**FEATURE:**

  * [ Updating selected VM instances in a managed instance group ](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#updating_selected_instances) , with minimal disruption and in a controlled way, is now available in **Beta** . 

**FEATURE:**

  * Importing VM Instances using OVA or OVF virtual appliances is now available in **Beta** . For more information, read [ Importing OVF virtual appliances ](https://cloud.google.com/compute/docs/import/import-ovf-files) . 

**FEATURE:**

  * [ Setting and querying guest attributes ](https://cloud.google.com/compute/docs/storing-retrieving-metadata#guest_attributes) is now **Generally Available** . You can use guest attributes to communicate the status of applications and scripts within your instance. 

##  June 27, 2019

**FEATURE:**

  * [ Mounting a persistent disk as a data volume in a container on Compute Engine ](https://cloud.google.com/compute/docs/containers/configuring-options-to-run-containers#mounting_a_persistent_disk_as_a_data_volume) is now **Generally Available** . 

##  June 18, 2019

**FEATURE:**

  * [ Bring your own license with in-place restarts ](https://cloud.google.com/compute/docs/instances/windows/bring-your-own-license/bringing-your-own-license-sole-tenant-nodes) is now available in **General Availability** . 

##  May 17, 2019

**FEATURE:**

  * Regional persistent disks can now be attached to multiple VMs in read-only mode. For more information, read [ Sharing a regional persistent disk between multiple instances ](https://cloud.google.com/compute/docs/disks/regional-persistent-disk#use_multi_instances) . 

**FEATURE:**

  * You can now use the [ Google Cloud Platform Console ](https://console.cloud.google.com/) to [ import virtual disks ](https://cloud.google.com/compute/docs/images/importing-virtual-disks#importing_virtual_disks) . 

##  May 16, 2019

**FEATURE:**

  * Snapshot locations are now **Generally Available** . The storage location of a snapshot affects the availability of the snapshot and networking costs for creating and restoring a snapshot. For more information, see [ Selecting the storage location for a snapshot ](https://cloud.google.com/compute/docs/disks/create-snapshots#selecting_a_storage_location) . 

**CHANGED:**

  * Multi-regional snapshot pricing is now separated from regional snapshot pricing. Read the [ Persistent disk pricing ](https://cloud.google.com/compute/disks-image-pricing#disk) page to learn about multi-regional snapshot pricing. 

##  May 07, 2019

**FEATURE:**

  * The following operating systems are now **Generally Available** as [ public images ](https://cloud.google.com/compute/docs/images#rhel) : 

    * Red Hat Enterprise Linux 8 
    * Red Hat Enterprise Linux for SAP with Update Services and High Availability 7.4 and 7.6 

**DEPRECATED:**

  * Red Hat has deprecated Red Hat Enterprise Linux 7 for SAP Applications and Red Hat Enterprise Linux 7 for HANA. For more information, read the [ RHEL for SAP offerings ](https://access.redhat.com/articles/3751271) page. As a result, these images are now marked deprecated on Compute Engine. 

##  April 29, 2019

**FEATURE:**

  * [ Reserving zonal resources ](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) is now available in **Beta** . You can reserve memory-optimized and general purpose VMs, with or without GPUs and local SSD, in a specific zone. 

##  April 19, 2019

**FEATURE:**

  * Regional persistent disk is now **Generally Available** . To learn more, read [ Adding or resizing regional persistent disks ](https://cloud.google.com/compute/docs/disks/regional-persistent-disk) . See the [ pricing page ](https://cloud.google.com/compute/disks-image-pricing#disk) to learn how this disk type is billed. 

##  April 18, 2019

**FEATURE:**

  * The ` asia-northeast2 ` Osaka region is now available to all projects and users. The zones in the ` asia-northeast2 ` region have the [ Skylake CPU platform ](https://cloud.google.com/compute/docs/cpu-platforms) . See [ Regions and Zones ](https://cloud.google.com/compute/docs/regions-zones/) for more information. 

##  April 10, 2019

**FEATURE:**

  * NVIDIA® Tesla® T4 GPU and NVIDIA® Tesla® T4 Virtual Workstations are now **Generally available** , in eight regions. See the [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus) page to learn more. 

##  April 05, 2019

**FEATURE:**

  * [ Memory-optimized machine types ](https://cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the following zones: 

    * ` us-east4-b `
    * ` us-east4-c `

See the [ pricing page ](https://cloud.google.com/compute/vm-instance-
pricing#megamem) to learn how these machine types are billed.

##  April 02, 2019

**FEATURE:**

  * [ Bringing your own licenses with sole-tenant nodes ](https://cloud.google.com/compute/docs/instances/windows/bring-your-own-license/) is now available in **Beta** . 

##  March 29, 2019

**FEATURE:**

  * [ Viewing VM serial port output in Stackdriver ](https://cloud.google.com/compute/docs/instances/viewing-serial-port-output) is now **Generally Available** . If you enable serial port output logging to Stackdriver, logs are retained for 30 days, even if your VM is deleted. 

##  March 28, 2019

**CHANGED:**

  * The Compute Engine [ SLA ](https://cloud.google.com/compute/sla) has been updated. 

##  March 27, 2019

**FEATURE:**

  * You can add virtual display devices to your instances. Use virtual display devices to run applications that require a display device without adding a phyiscal GPU device. Virtual display devices are available in **Beta** . Read [ Enabling Virtual Displays on Instances ](https://cloud.google.com/compute/docs/instances/enable-instance-virtual-display) to learn more. 

**FEATURE:**

  * You can now add extra security when connecting to instances using OS Login. For more information, see [ Setting up OS Login with two-factor authentication ](https://cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication) . 

##  March 22, 2019

**FEATURE:**

  * Increased the per-instance persistent disk throughput performance to 240 MB/s for read and write bandwidth. See the [ Persistent Disk Performance ](https://cloud.google.com/compute/docs/disks/#introduction) for details. 

##  March 11, 2019

**FEATURE:**

  * Added new ` europe-west6 ` region in Zürich, Switzerland. The ` europe-west6 ` region contains Skylake zones that are now available to all projects and users. See [ Regions and Zones ](https://cloud.google.com/compute/docs/regions-zones/) for more information. 

##  February 27, 2019

**FEATURE:**

  * [ Memory-optimized machine types ](https://cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the following zones: 

    * ` asia-northeast1-a `
    * ` asia-southeast1-b `
    * ` northamerica-northeast1-b `
    * ` northamerica-northeast1-c `
    * ` southamerica-east1-b `
    * ` southamerica-east1-c `
    * ` us-central1-a `

See the [ pricing page ](https://cloud.google.com/compute/vm-instance-
pricing#megamem) to learn how these machine types are billed.

##  February 21, 2019

**FEATURE:**

  * You can now attach up to 128 independent persistent disks to custom machine types and most predefined machine types. For more details, see [ Persistent disk limits ](https://cloud.google.com/compute/docs/disks/#pdnumberlimits) . 

##  February 14, 2019

**FEATURE:**

  * User-created scheduled snapshots for zonal and regional persistent disks is now available in **Beta** . Scheduled snapshots allows you to create an automatic snapshot schedule and include a retention policy for maintaining those snapshots. For more information, see [ Creating scheduled snapshots for persistent disk ](https://cloud.google.com/compute/docs/disks/scheduled-snapshots) . 

##  February 11, 2019

**FEATURE:**

  * [ Sole tenant nodes ](https://cloud.google.com/compute/docs/nodes) are now available in Hong Kong ( ` asia-east2 ` ). 

**FEATURE:**

  * [ Application-based health checking and autohealing for managed instance groups ](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups) is now **Generally Available** . 

##  February 06, 2019

**FEATURE:**

  * Selecting 16 KB physical block size is now in **Beta** . You can create zonal and regional persistent disks with a 16 KB physical block. Some database applications might see greater performance by using 16 KB physical block. Read [ Adding Persistent Disks ](https://cloud.google.com/compute/docs/disks/add-persistent-disk#physical_block_storage) for feature details. Read [ Optimizing Persistent Disk and Local SSD Performance ](https://cloud.google.com/compute/docs/disks/performance#size_price_performance) for performance comparisons. Read the [ Best practices for 16 KB persistent disk and MySQL ](https://cloud.google.com/compute/docs/tutorials/16kb-mysql-best-practices) tutorial to learn about performance improvements to a MySQL database. 

**FEATURE:**

  * Users and applications can now write to instance-specific guest-writeable metadata values. You can use guest attributes to communicate status of applications and scripts within your instance. Read [ Setting and querying guest attributes ](https://cloud.google.com/compute/docs/storing-retrieving-metadata#guest-attributes) to learn more. 

**FEATURE:**

  * The [ Managed Instance Group Updater ](https://cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups) is now **Generally Available** . This feature enables proactive, flexible rolling updates with the option to canary a new version on a subset of managed instance group VMs. 

##  January 29, 2019

**FEATURE:**

  * [ Granting access to specific Compute resources ](https://cloud.google.com/compute/docs/access/granting-access-to-resources) , such as VM instances, disks, and images, is now **Generally Available** . This feature gives you flexibility to apply the principle of least privilege, for example, to grant collaborators permissions only to the specific resources that they need to do their work. 

##  January 24, 2019

**FEATURE:**

  * Detaching and reattaching boot disks from a stopped VM instance is now available in **GA** . Use the [ Google Cloud Platform Console ](https://console.cloud.google.com/) , ` gcloud ` or API to detach a failed boot disk, fix it, then reattach it back to the original VM instance. You can also use this feature for rollbacks: detach a disk, create a new disk using an earlier snapshot, and attach that restored disk to your VM. See [ Detaching and Reattaching Boot Disks ](https://cloud.google.com/compute/docs/disks/detach-reattach-boot-disk) for details. 

**FEATURE:**

  * [ Creating a VM Instance with a Custom Hostname ](https://cloud.google.com/compute/docs/instances/custom-hostname-vm) is now **Generally Available** . 

##  January 16, 2019

**FEATURE:**

  * NVIDIA® Tesla® T4 GPU and NVIDIA® Tesla® T4 Virtual Workstations are now available, as **Beta** , in eight regions. See the [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus) page to learn more. 

##  January 11, 2019

**FEATURE:**

  * Windows Server 2019 images are now **Generally Available** as a [ public image ](https://cloud.google.com/compute/docs/images) . 

**FEATURE:**

  * Windows Server, version 1809 images are now **Generally Available** as a [ public image ](https://cloud.google.com/compute/docs/images) . This is a Server Core image that is part of the [ semi-annual release cycle ](https://docs.microsoft.com/en-us/windows-server/get-started/semi-annual-channel-overview) for Windows Server. 

##  December 14, 2018

**FEATURE:**

  * User-selected snapshot storage locations are now available in **Beta** . The storage location of a snapshot affects the availability of the snapshot and networking costs. For more information, see [ Selecting the storage location for a snapshot ](https://cloud.google.com/compute/docs/disks/create-snapshots#selecting_a_storage_location) . 

**CHANGED:**

  * Snapshot creation might now incur networking charges. These charges will begin after this feature reaches General Availability (GA), and will depend upon the [ storage location of a snapshot ](https://cloud.google.com/compute/docs/disks/create-snapshots#selecting_a_storage_location) and the location of the source disk. For more information, see [ Network charges for snapshot creation and restoration ](https://cloud.google.com/compute/disks-image-pricing#disk) . 

##  November 15, 2018

**FEATURE:**

  * Windows Service Activation using Private Google Access is **Generally Available** . Read the [ Private Google Access ](https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#internal_ip_activation) page to learn more. 

##  November 13, 2018

**FEATURE:**

  * Detaching and reattaching boot disks from a stopped VM instance is now available in **Beta** . Use the gcloud or API command to detach a failed boot disk, fix it, then reattach it to a different VM instance. See [ Detaching and Reattaching Boot Disks ](https://cloud.google.com/compute/docs/disks/detach-reattach-boot-disk) for details. 

##  November 08, 2018

**FEATURE:**

  * [ Memory-optimized machine types ](https://cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the ` southamerica-east1-a ` zone. See the [ pricing page ](https://cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  November 07, 2018

**FEATURE:**

  * [ Creating a VM Instance with a Custom Hostname ](https://cloud.google.com/compute/docs/instances/custom-hostname-vm) is available in **Beta** . 

##  October 24, 2018

**FEATURE:**

  * [ Viewing VM serial port output in Stackdriver ](https://cloud.google.com/compute/docs/instances/viewing-serial-port-output) is available in **Beta** . To help with troubleshooting, these logs can be retained for up to 30 days after a VM instance is deleted. 

##  October 22, 2018

**FEATURE:**

  * The ` asia-east2 ` Hong Kong region is now available to all projects and users. The zones in the ` asia-east2 ` region have the [ Skylake CPU platform ](https://cloud.google.com/compute/docs/cpu-platforms) . See [ Regions and Zones ](https://cloud.google.com/compute/docs/regions-zones/) for more information. 

##  October 19, 2018

**FEATURE:**

  * [ Memory-optimized machine types ](https://cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the ` asia-southeast1-c ` , ` australia-southeast1-c ` , ` europe-west3-a ` , ` europe-west3-b ` and ` us-west2-b ` zones. See the [ pricing page ](https://cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  October 02, 2018

**FEATURE:**

  * Compute Engine now uses a [ resource based pricing model ](https://cloud.google.com/compute/vm-instance-pricing#pricing) that provides greater savings from [ sustained use discounts ](https://cloud.google.com/compute/docs/sustained-use-discounts) . All machine types except for shared-core machine types are now billed by their individual vCPU and memory usage rather than billing by each machine type. Sustained use discounts are calculated for vCPU and memory usage across an entire region rather than separately for each machine type in each zone. See the [ Compute Engine Pricing ](https://cloud.google.com/compute/vm-instance-pricing#pricing) page for details. 

**FEATURE:**

2018-10-02

FEATURE * Protect data on Compute Engine with Cloud Key Management Service
encryption keys. [ Customer-Managed Encryption Keys
](https://cloud.google.com/compute/docs/disks/customer-managed-encryption) are
now generally available.

##  September 26, 2018

**FEATURE:**

  * NVIDIA® Tesla® P4 GPUs are now **Generally Available** . For information about using GPUs on Compute Engine, see [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus/) . 

**FEATURE:**

  * For graphics-intensive workloads, NVIDIA® GRID®-based virtual workstations using NVIDIA® Tesla® P4 and P100 GPUs are now **Generally Available** . For information on GPUs for graphics-intensive applications, see [ GPUs for graphics workloads ](https://cloud.google.com/compute/docs/gpus/#gpu-virtual-workstations) . 

**FEATURE:**

  * NVIDIA® Tesla® v100 GPUs are now available in the ` us-central1-b ` and ` europe-west4-b ` zones. See [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus/#gpus-list) for a complete list of zones where GPUs are available. 

**FEATURE:**

  * NVIDIA® Tesla® P4 GPUs are now available in the ` australia-southeast1-a ` , and ` australia-southeast1-b ` zones. See [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus/#gpus-list) for a complete list of zones where GPUs are available. 

##  September 25, 2018

**FEATURE:**

  * Windows Server instances no longer require a public IP for Windows Service Activation. If your Windows Server instance uses a subnetwork that is enabled for [ Private Google Access ](https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#internal_ip_activation) , that instance can complete Windows Service Activation over its internal VPC network. Windows Service Activation using Private Google Access is available in **Beta** . Read the [ Private Google Access ](https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#internal_ip_activation) page to learn more. 

##  September 20, 2018

**FEATURE:**

  * [ Deploying Docker Containers on Compute Engine ](https://cloud.google.com/compute/docs/containers/deploying-containers) is now **Generally Available** . 

##  September 12, 2018

**FEATURE:**

  * Now in **Beta** , you can [ grant access to specific Compute resources ](https://cloud.google.com/compute/docs/access/granting-access-to-resources) , such as VM instances, disks, and images. This feature gives you flexibility to apply the principle of least privilege, for example, to grant collaborators permissions only to the specific resources that they need to do their work. 

##  September 06, 2018

**FEATURE:**

  * [ Zonal DNS names ](https://cloud.google.com/compute/docs/internal-dns#zonal-dns) are now **Generally Available** . Projects that enable the Compute Engine API after today will use zonal DNS names by default. Projects and organizations that enabled the Compute Engine API before today will continue to use global DNS names by default. Migrating a project to an organization will not change the default DNS name for the project. Zonal DNS names are unique to each zone on your internal [ VPC ](https://cloud.google.com/vpc/docs/vpc) networks. Zonal DNS names improve the fault tolerance of your applications when they reference instances on your internal VPC network. New and existing projects can still use global DNS names, but [ migration ](https://cloud.google.com/compute/docs/internal-dns#migrating-to-zonal) is encouraged. Read [ Internal DNS ](https://cloud.google.com/compute/docs/internal-dns) to learn more. 

##  September 04, 2018

**FEATURE:**

  * The ` simulateMaintenanceEvent ` API method is **Generally Available** . Read [ testing your availability policies ](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#testingpolicies) to learn how to simulate a Compute Engine maintenance event and observe how the instance availability settings affect the behavior of your instances. 

##  August 27, 2018

**FEATURE:**

  * NVIDIA® Tesla® V100 GPUs are now **Generally Available** . For information about using V100 GPUs on Compute Engine, see [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus/) . 

##  August 17, 2018

**FEATURE:**

  * Zonal SSD persistent disks and regional SSD persistent disks now have increased read throughput and read input/output operations per second (IOPS). See [ Optimizing Persistent Disk and Local SSD Performance ](https://cloud.google.com/compute/docs/disks/performance) for more information. 

##  August 08, 2018

**FEATURE:**

  * Sole-tenant nodes are now **Generally Available** . Read [ Sole-tenant Nodes ](https://cloud.google.com/compute/docs/nodes) to learn how you can use these systems to isolate your workloads from each other and from other Compute Engine projects. 

##  August 03, 2018

**FEATURE:**

  * If you have graphics-intensive workloads, such as 3D rendering or video editing, you can create virtual workstations that use NVIDIA® GRID® technology, using NVIDIA® Tesla® P4 and P100 GPUs. For information on GPUs for graphics-intensive applications, see [ GPUs for graphics workloads ](https://cloud.google.com/compute/docs/gpus/#gpu-virtual-workstations) . 

**FEATURE:**

  * You can use organization policies to restrict use of your disks, custom images, and snapshots so that they can be used only within your organization or specific projects. This prevents users from creating copies of disks, outside of your organization. Read [ restricting use of your shared images, disks, and snapshots ](https://cloud.google.com/compute/docs/images/sharing-images-across-projects#restrict) to learn more. 

##  July 25, 2018

**FEATURE:**

  * [ Shielded VM ](https://cloud.google.com/security/shielded-cloud/shielded-vm) is now available in **Beta** . Shielded VM images offer security features like UEFI-compliant firmware, Secure Boot, and vTPM-protected Measured Boot. 

##  July 23, 2018

**FEATURE:**

  * The ` n1-megamem-* ` family of [ memory-optimized machine types ](https://cloud.google.com/compute/docs/machine-types#megamem) with 1.4 TB of memory are now **Generally Available** to all projects. See the [ pricing page ](https://cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  July 19, 2018

**FEATURE:**

2018-07-19

FEATURE * Selecting specific zones for regional managed instance groups is now
**Generally Available** . See [ Distributing Instances using Regional Managed
Instance Groups ](https://cloud.google.com/compute/docs/instance-
groups/distributing-instances-with-regional-instance-groups#selecting_zones) .

**FEATURE:**

  * Windows Server for Containers is now **Generally Available** as a [ public image ](https://cloud.google.com/compute/docs/images#os-compute-support) . 

##  July 18, 2018

**FEATURE:**

  * [ Memory-optimized machine types ](https://cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now **Generally Available** . See the [ pricing page ](https://cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  July 17, 2018

**FEATURE:**

  * If you need high availability and redundancy for your Microsoft SQL Server on Compute Engine, you can [ configure an Always On Failover Cluster Instance (FCI) with Storage Spaces Direct (S2D) ](https://cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance) . 

##  July 11, 2018

**FEATURE:**

  * [ Virtual machine sizing recommendations ](https://cloud.google.com/compute/docs/instances/viewing-sizing-recommendations-for-instances) are now **Generally Available** . 

##  July 10, 2018

**FEATURE:**

  * Added new ` us-west2 ` Los Angeles region. ` us-west2 ` contains Skylake zones that are now available to all projects and users. See [ Regions and Zones ](https://cloud.google.com/compute/docs/regions-zones/) for more information. 

**ISSUE:**

  * If you try to create a new instance in this zone for a project that existed before this release date, you may receive the following error message: "No default subnetwork was found in the region of the instance." This issue will be resolved within three days of this launch. In the meantime, the workaround is to [ manually create a subnet ](https://cloud.google.com/vpc/docs/using-vpc) and use it for a new VM. 

**FEATURE:**

  * [ Creating an instance template from a VM instance ](https://cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) is now **Generally Available** . This feature can be used for instance duplication, backup, and recreation. 

##  July 02, 2018

**FEATURE:**

  * You can now add 2 and 4 NVIDIA® Tesla® V100 GPUs to your Compute Engine instances. For information about using GPUs on Compute Engine, see [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus/) . 

##  June 22, 2018

**FEATURE:**

  * You can [ purchase committed use discounts ](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) for [ memory-optimized machine types ](https://cloud.google.com/compute/docs/machine-types#megamem) . Memory-optimized machine types use their own commitment type with different pricing. You must [ request access ](https://docs.google.com/forms/d/e/1FAIpQLSe534-lhy0aQq4agiSi7ERSKddJS2QrwZo_jYQDNKkKnT3Y3Q/viewform?usp=sf_link) to use committed use discounts for memory-optimized machine types. See the [ pricing page ](https://cloud.google.com/compute/vm-instance-pricing#committed_use) for pricing details about committed use discounts. 

##  June 19, 2018

**FEATURE:**

  * The Compute Engine Trusted Images policy is now **Generally Available** . Use this policy to control which boot disk images your project members can access. Read [ Restricting Access to Images ](https://cloud.google.com/compute/docs/images/restricting-image-access) for more information. 

##  June 11, 2018

**FEATURE:**

  * Added new ` europe-north1 ` region. ` europe-north1 ` contains Skylake zones that are now available to all projects and users. See [ Regions and Zones ](https://cloud.google.com/compute/docs/regions-zones/) for more information. 

**ISSUE:**

  * If you try to create a new instance in this zone for a project that existed before this release date, you may receive the following error message: "No default subnetwork was found in the region of the instance." This issue will be resolved within three days of this launch. In the meanwhile, the workaround is to [ manually create a subnet ](https://cloud.google.com/vpc/docs/using-vpc) and use it for a new VM. 

**CHANGED:**

  * The prices for GPUs on preemptible VM instances have reduced. For the updated prices, see the [ GPUs pricing page ](https://cloud.google.com/compute/gpus-pricing) . 

**FEATURE:**

  * GPUs on preemptible VM instances are now **Generally Available** . 

For information about using GPUs on Compute Engine, see [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus/) .

##  June 07, 2018

**FEATURE:**

  * You can create sole-tenant nodes, which are physical Compute Engine servers that are dedicated to hosting only VM instances from your specific project. Read [ Sole-tenant Nodes ](https://cloud.google.com/compute/docs/nodes) to learn how you can use these systems to isolate your workloads from each other and from other Compute Engine projects. 

##  June 05, 2018

**FEATURE:**

  * Protect data on Compute Engine with Cloud Key Management Service encryption keys. [ Customer-Managed Encryption Keys ](https://cloud.google.com/compute/docs/disks/customer-managed-encryption) are now available in beta. 

##  May 28, 2018

**FEATURE:**

NVIDIA® Tesla® V100 GPUs are now available in the following regions:

  * us-west1-a 
  * us-central1-a 
  * asia-east1-c 

For information about using V100 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus/) .

##  May 23, 2018

**FEATURE:**

  * Added support for [ regional persistent disks ](https://cloud.google.com/compute/docs/disks/#repds) into **Beta** . This feature provides synchronous block-level replication across two zones in a region for each regional persistent disk. 

##  May 16, 2018

**FEATURE:**

  * Instances with NVIDIA® Tesla® V100 GPUs can now use Local SSD devices. For information on using V100 GPUs on Compute Engine, see [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus/) . 

##  May 08, 2018

**FEATURE:**

  * [ Memory-optimized machine types ](https://cloud.google.com/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in **Beta** . See the [ pricing page ](https://cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  May 07, 2018

**FEATURE:**

  * Added local SSD support to the ` europe-west4-a ` zone. See [ Regions and Zones ](https://cloud.google.com/compute/docs/regions-zones/) for more information. 

##  May 01, 2018

**FEATURE:**

  * Added a third zone to the ` asia-southeast1 ` region. This zone supports machine types with up to 96 vCPUs when using the Skylake platform. See [ Regions and Zones ](https://cloud.google.com/compute/docs/regions-zones/) for more information. 

##  April 30, 2018

**FEATURE:**

  * NVIDIA® Tesla® V100 GPUs are now available in **Beta** . For information on the zones where V100 GPUs are available, see [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus/) . 

##  April 20, 2018

**FEATURE:**

  * NVIDIA® Tesla® P100 GPUs are now **Generally Available** . To learn about the zones where P100 GPUs are available, read [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus/) . 

**FEATURE:**

  * Creating multiple secondary non-boot disks when you [ create your VM instance ](https://cloud.google.com/compute/docs/instances/create-start-instance) is now **Generally Available** . 

##  April 19, 2018

**CHANGED:**

  * The price of SLES for SAP images is reduced. Read [ SUSE premium image pricing ](https://cloud.google.com/compute/disks-image-pricing#suse_images) for details. 

##  April 17, 2018

**FEATURE:**

NVIDIA® Tesla® P100 GPUs are now available in the following zones:

  * ` asia-east1-c `
  * ` europe-west4-a `

To learn more about using GPUs on Compute Engine, see [ GPUs on Compute Engine
](https://cloud.google.com/compute/docs/gpus/) .

##  April 11, 2018

**FEATURE:**

  * You can now run simulated maintenance events to test the effects of live migration, termination, and preemption on your instances. Simulated maintenance events are available in **Beta** . Read [ testing your availability policies ](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#testingpolicies) to learn how to test maintenance events on your instances. 

**FEATURE:**

  * [ Nested Virtualization ](https://cloud.google.com/compute/docs/instances/enable-nested-virtualization-vm-instances) is now **Generally Available** . 

##  March 28, 2018

**FEATURE:**

  * You can import existing virtual disks (VMDKs, VHDs, etc) into Compute Engine as custom images. [ Importing virtual disks ](https://cloud.google.com/compute/docs/images/importing-virtual-disks) is now **Generally Available** . 

##  March 23, 2018

**FEATURE:**

  * You can import a Windows Server 2003 server to Compute Engine using the CloudEndure migration service. For steps, see [ Migrating VMs to Compute Engine ](https://cloud.google.com/compute/docs/instances/migrating-vms-compute-engine) . 

##  March 14, 2018

**FEATURE:**

  * Creating an image from a snapshot is now **Generally Available** . See the [ creating custom images ](https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#creating_a_custom_image) page. 

##  March 13, 2018

**FEATURE:**

  * Added a third zone to the ` europe-west4 ` region. This zone supports 96 vCPU high memory/high CPU machines. There is no support for local SSDs at this time. See [ Regions and Zones ](https://cloud.google.com/compute/docs/regions-zones/) for more information. For regional managed instance group users, the addition of a third zone in ` europe-west4 ` offers you more flexibilty to specify zones in this region. Note that if you do not specify the zones for your instances, Compute Engine, by default, selects all three zones. See [ Distributing Instances using Regional Managed Instance Groups ](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) to learn more. 

##  March 08, 2018

**FEATURE:**

  * Added support for PTR records on VM instances to **General Availability** . See [ Creating a PTR record for VM instances ](https://cloud.google.com/compute/docs/instances/create-ptr-record) . 

##  March 07, 2018

**FEATURE:**

  * You can import existing virtual disks (VMDKs, VHDs, etc) into Compute Engine as functioning images. [ Importing virtual disks ](https://cloud.google.com/compute/docs/images/importing-virtual-disks) is available in **Beta** . 

##  March 02, 2018

**FEATURE:**

  * [ Mega-memory machine types ](https://cloud.google.com/compute/docs/machine-types#megamem) with 1.4 TB of memory are now available in **Beta** . See the [ pricing page ](https://cloud.google.com/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  February 22, 2018

**FEATURE:**

  * Creating multiple secondary non-boot disks when you [ create your VM instance ](https://cloud.google.com/compute/docs/instances/create-start-instance) is now available in Beta. 

##  February 09, 2018

**FEATURE:**

  * [ 96 vCPU machine types ](https://cloud.google.com/compute/docs/machine-types) are **Generally Available** . These machine types are now available in several additional zones only on the Skylake platform. Read the list of [ available regions and zones ](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) to see where 96 vCPU machine types are available. 

##  February 01, 2018

**FEATURE:**

  * Added support for [ creating an instance template from a VM instance ](https://cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) into **Beta** . This feature can be used for instance duplication, backup, and recreation. 

##  January 31, 2018

**FEATURE:**

  * Compute Engine supports [ IAM Custom Roles ](https://cloud.google.com/iam/docs/understanding-custom-roles) . Read the [ IAM Custom Roles documentation ](https://cloud.google.com/iam/docs/understanding-custom-roles) to learn more. You can identify which permissions are required to run Compute Engine methods in both the [ V1 Compute Engine API reference ](https://cloud.google.com/compute/docs/reference/rest/v1/) and on the [ Compute Engine IAM Permissions ](https://cloud.google.com/compute/docs/access/iam-permissions) page. 

**FEATURE:**

  * You can configure autoscaling for groups of instances based on a wider range of metrics, which allow you to scale managed instance groups on per-group metrics rather than average resource utilization across all of the instances in a group. [ Autoscaling using per-group metrics ](https://cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics#per_group_metrics) is available in **Beta** . 

**FEATURE:**

  * You can filter Stackdriver monitoring metrics when you use them to configure autoscaling for your managed instance groups. [ Filtering per-instance metrics ](https://cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics#filter_per_instance_metrics) is available in **Beta** . 

##  January 24, 2018

**FEATURE:**

  * The OS Login API and key management feature is now **Generally Available** . You can associate your public SSH keys with your Google account or with individual member accounts in a G Suite organization or Cloud Identity organization. Read [ Managing Instance Access ](https://cloud.google.com/compute/docs/instances/managing-instance-access) for more information. 

##  January 22, 2018

**FEATURE:**

  * For NVIDIA® Tesla® K80 GPUs in the ` asia-east1-a ` and ` us-east1-d ` zones, you can create GPU instances with up to 416 GB of memory. 

To learn more about the zones where GPUs are available, read [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus/) .

##  January 11, 2018

**FEATURE:**

  * [ VM Deletion Protection ](https://cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion) is now **Generally Available** . 

##  January 10, 2018

**FEATURE:**

  * Added new ` europe-west4 ` region. ` europe-west4 ` contains Skylake zones that are now available to all projects and users. See [ Regions and Zones ](https://cloud.google.com/compute/docs/regions-zones/) for more information. 

**FEATURE:**

  * Added new ` northamerica-northeast1 ` Montréal region. ` northamerica-northeast1 ` contains Skylake zones that are now available to all projects and users. See [ Regions and Zones ](https://cloud.google.com/compute/docs/regions-zones/) for more information. 

##  January 08, 2018

**FEATURE:**

  * [ Zonal DNS names ](https://cloud.google.com/compute/docs/internal-dns#zonal-dns) are available in **Beta** . Zonal DNS names are unique to each zone on your internal [ VPC ](https://cloud.google.com/vpc/docs/vpc) networks. Global DNS names continue to resolve, but you can enable zonal DNS names to improve the fault tolerance of your applications when they reference instances on your internal VPC network. Read [ Zonal DNS ](https://cloud.google.com/compute/docs/internal-dns#zonal-dns) to learn more. 

