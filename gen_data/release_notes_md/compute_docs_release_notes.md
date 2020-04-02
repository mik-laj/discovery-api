#  Release Notes

This page contains the latest release notes for features and updates to the
Compute Engine service. For older release notes, see [ the archive
](/compute/docs/release-notes-archive) .

**Latest API version: v1**

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/compute-engine-release-
notes.xml `

##  April 01, 2020

  * You can now define where your VM instances are located relative to each other on the underlying host systems in a Google datacenter. Create a placement policy to locate VM instances close to each other for low latency, or create a policy to spread VM instances out so that they do not share the same infrastructure. See [ Defining instance location within a zone ](/compute/docs/instances/define-instance-placement) to learn more. 

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones: 

    * Frankfurt, Germany: ` europe-west3-b `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](/compute/docs/gpus) .

##  March 31, 2020

  * **Beta:** [ Collect diagnostic information from Windows VMs ](/compute/docs/instances/collecting-diagnostic-information) . 

  * C2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * Frankfurt, Germany ` europe-west3-a,b `
    * Ashburn, Northern Virginia, USA ` us-east4-a `
  * N2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * The Dalles, Oregon, USA ` us-west1-a `
    * Changua County, Taiwan ` asia-east1-c `
  * M1 megamem machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * Eemshaven, Netherlands ` europe-west4-b `
  * M1 ultramem machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * Ashburn, Northern Virginia, USA ` us-east4-a `
  * M2 ultramem machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * Los Angeles, California, USA ` us-west2-a,c `

##  March 24, 2020

  * Committed use discounts no longer require specific ratios for cores and memory. Now you can create separate committed use discount contracts for either cores or memory. Separating cores and memory provides more flexibility and improved cost optimization. Learn more at [ Purchasing commitments for machine types ](/compute/docs/instances/signing-up-committed-use-discounts#purchasecommitment) . 

  * You can [ preserve the names ](/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#preserving_instance_names) of your VM instances when rolling out updates in a managed instance group. This is **Generally available** . 

  * You can [ update selected VM instances in a managed instance group ](/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#updating_selected_instances) , with minimal disruption and in a controlled way. This is **Generally available** . 

##  March 19, 2020

  * [ E2 machine types ](/compute/docs/machine-types#e2_machine_types) are **Generally available** . 

##  March 16, 2020

  * N2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * London, England UK ` europe-west2-b `
  * C2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * St. Ghislain, Belgium ` europe-west1-c,d `

##  March 11, 2020

  * You can identify VM instances that are not being used with [ idle VM recommendations ](/compute/docs/instances/viewing-and-applying-idle-vm-recommendations) . Use these recommendations to reduce unused resources and reduce your compute bill. This feature is **Generally available** . 

  * In **beta** , you can create an instance with 16 or 24 local SSD partitions for 6 TB and 9 TB of local SSD space, respectively. With 24 local SSD partitions, performance can reach a combined total of 2.4 million read IOPS. For more information, see [ 9 TB Local SSD maximum capacity beta ](/compute/docs/disks/local-ssd#capacity_9tb) . 

##  March 09, 2020

  * [ Machine image ](/compute/docs/machine-images) is now available in **beta** . You can use machine images to store configuration, metadata, permission, and data required to create a VM instance in a single resource. 

##  March 05, 2020

  * CoreOS Container Linux images will reach their end of life on May 26, 2020. For more information, see [ CoreOS End-Of-Life (EOL) ](/compute/docs/eol/coreOS) . 

##  March 3, 2020

  * You can now create [ E2 machine types ](/compute/docs/machine-types#e2_machine_types) in all [ regions and zones ](/compute/docs/regions-zones#available) . 

##  March 2, 2020

  * You can now [ use the Google Cloud Console to export images to Cloud Storage ](/compute/docs/images/export-image#exporting_an_image_with_a_single_command) . This is **Generally Available** . 

##  February 27, 2020

  * E2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * Los Angeles, USA ` us-west2-a,b,c `
    * London, England, UK ` europe-west2-a,b,c `
    * Frankfurt, Germany ` europe-west3-b,c `
    * Tokyo, Japan ` asia-northeast1-a,b,c `
  * N2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * Frankfurt, Germany ` europe-west3 a,b `
  * C2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * Council Bluffs, Iowa, US ` us-central1-a `
  * M2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * Mumbai, India ` asia-south1-a `
  * You can now manage, maintain, and view patch compliance for your VM instances using the OS patch management feature. For more information, see [ OS patch management ](/compute/docs/os-patch-management) . This feature is available in **beta** . 

##  February 24, 2020

  * The ` us-west3 ` Salt Lake City, UT region is now available to all projects and users. The zones in the ` us-west3 ` region have the [ Skylake CPU platform ](/compute/docs/cpu-platforms) . See [ Regions and zones ](/compute/docs/regions-zones) for more information. 

##  February 21, 2020

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones: 

    * Changhua County, Taiwan: ` asia-east1-a `
    * London, England, UK: ` europe-west2-b `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](/compute/docs/gpus) .

##  February 19, 2020

  * M2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * Northern Virginia ` us-east4-a,b `
  * If you have configured autohealing for your managed instance group, you can [ review the health state ](/compute/docs/instance-groups/autohealing-instances-in-migs#checking_whether_instances_are_healthy) of each VM in the group. This is **Generally Available** . 

##  February 18, 2020

  * N2D machine types are available in beta. N2D machine types are built on top of second generation AMD EPYC Rome processors. They are a great fit for general purpose workloads and for workloads that require high memory bandwidth. Learn more about these [ general purpose machine types ](/compute/docs/machine-types#n2d_machine_types_beta) . 

##  February 13, 2020

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones: 

    * London, England, UK: ` europe-west2-a `
    * Seoul, South Korea: ` asia-northeast3-b,c `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](/compute/docs/gpus) .

##  February 12, 2020

  * You can now maintain consistent software configurations across VM instances using guest policies. For more information, see [ OS configuration management ](/compute/docs/os-config-management) . This feature is available in **beta** . 

##  February 11, 2020

  * To support a wide variety of BYOL scenarios, you can now [ configure VMs to live migrate within a sole-tenant node group during host maintenance events ](/compute/docs/instances/windows/bring-your-own-license) . This is available in **Beta** . 

##  February 07, 2020

  * G Suite administrators can now choose whether to include the domain suffix in usernames generated by the OS Login API. For more information, see [ Managing the OS Login API ](/compute/docs/oslogin/manage-oslogin-in-an-org#manage-oslogin-api) . This feature is **Generally Available** . 

##  February 5, 2020

  * Read an [ FAQ ](/compute/docs/nodes/sole-tenancy-accounting-faq) that can help you evaluate whether to classify [ sole-tenant node ](/compute/docs/nodes) payments as capital expenditures (CAPEX) or operational expenditures (OPEX). 

##  February 3, 2020

  * You can build highly available deployments of stateful workloads on VM instances using [ stateful managed instance groups (stateful MIGs) ](/compute/docs/instance-groups/stateful-migs) . A stateful MIG preserves the unique state of each instance (instance name, attached persistent disks, and/or metadata) on machine restart, recreation, autohealing, or update. Stateful MIGs are available in **beta** . 

##  January 31, 2020

  * You can now [ reschedule VMs on, off, or between sole-tenant nodes ](/compute/docs/nodes/vm-tenancy) . This is **Generally Available** . 

  * You can now enable an [ autoscaler ](/compute/docs/nodes/node-group-autoscaler) on your sole-tenant node groups. This is available in **Beta** . 

##  January 24, 2020

  * The ` asia-northeast3 ` Seoul region is now available to all projects and users. The zones in the ` asia-northeast3 ` region have the [ Skylake CPU platform ](/compute/docs/cpu-platforms) . See [ Regions and zones ](/compute/docs/regions-zones) for more information. 

##  January 21, 2020

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional zones: 

    * Tokyo: ` asia-northeast1-c `
    * Singapore: ` asia-southeast1-c `
    * Iowa: ` us-central1-f `
    * Mumbai: ` asia-south1-a `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](/compute/docs/gpus) .

  * You can temporarily turn off or restrict managed instance group autoscaling. The autoscaler's configuration remains intact, and all autoscaling activities resume when you turn it on again or lift the restriction. [ Turning off or restricting autoscaling ](/compute/docs/autoscaler/managing-autoscalers#disable_or_restrict_an_autoscaler) for managed instance groups is now **Generally available** . 

##  January 09, 2020

  * NVIDIA® Tesla® T4 GPU prices are reduced in all regions. For more information about the new prices for each region, see [ GPU pricing ](/compute/gpus-pricing) . 

##  December 18, 2019

  * Specifying an image storage location is now **Generally Available** for custom images. Specifying your image storage location helps you meet your regulatory and compliance requirements for data locality as well as your high availability needs by ensuring redundancy across regions. See [ Creating, deleting, and deprecating custom images ](/compute/docs/images/create-delete-deprecate-private-images) , and [ Creating a Windows image ](/compute/docs/instances/windows/creating-windows-os-image) . 

##  December 17, 2019

  * E2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * Iowa ` us-central1-a `

##  December 16, 2019

  * On November 21, 2019, we announced that organizations would be disabled from using nested virtualization by default starting January 31, 2020. This will no longer happen and nested virtualization will be allowed by default. However, we recommend [ explicitly setting your organizational policy ](/compute/docs/instances/enable-nested-virtualization-vm-instances#enable_nested_virt_org) to allow or prevent nested virtualization as a best practice. 

##  December 13, 2019

  * N2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * Tokyo ` asia-northeast1-a,b `
    * Singapore ` asia-southeast1-a `
    * Sydney ` australia-southeast1-b `

##  December 11, 2019

  * E2 machine types are available in **beta** . These machine types are ideal for small to medium workloads that require 16 vCPUs or less, no local SSDs, and no GPUs. Learn more about these [ cost-optimized machine types ](/compute/docs/machine-types#e2_machine_types) . 

##  December 10, 2019

  * You can now create VM instances with V100 AND T4 GPUs that support network bandwidths of up to 100 Gbps. See [ Using network bandwidths of up to 100 Gbps ](/compute/docs/gpus/optimize-gpus#high-bandwidth) . This feature is available in **beta** . 

##  November 22, 2019

  * N2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * South Carolina ` us-east1-d `
    * Belgium ` europe-west1-c `
    * London ` europe-west2-c `
    * Sydney ` australia-southeast1-a `
  * Virtual machines with 2 or 4 vCPUs now have a maximum egress rate of 10 Gbps. This feature is now **Generally Available** . For more information, see [ Machine types ](/compute/docs/machine-types) . 

##  November 21, 2019

  * After January 31, 2020, nested virtualization will be disabled by default by an organizational policy. To avoid interruptions to your workloads, [ update the organization policy ](/compute/docs/instances/enable-nested-virtualization-vm-instances#enable_nested_virt_org) to allow nested virtualization. 

##  November 8, 2019

  * N2 machine types are now available in the following [ regions and zones ](/compute/docs/regions-zones#available) : 

    * South Carolina ` us-east1-c `
    * Belgium ` europe-west1-b `
    * London ` europe-west2-a `

##  November 6, 2019

  * You can temporarily turn off or restrict managed instance group autoscaling. The autoscaler's configuration remains intact, and all autoscaling activities resume when you turn it on again or lift the restriction. [ Turning off or restricting autoscaling ](/compute/docs/autoscaler/managing-autoscalers#turn_off_or_restrict_an_autoscaler) for managed instance groups is now available in **Beta** . 

##  October 25, 2019

  * As a G Suite admin, you can now complete the following tasks for the OS Login feature: 

    * Enable OS Login using an organization policy. For more information, see [ Setting up an OS Login organization policy ](/compute/docs/oslogin/manage-oslogin-in-an-org#set_org_policy) . 
    * Track interactions with the OS Login API. For more information, see [ Auditing OS Login events ](/compute/docs/oslogin/manage-oslogin-in-an-org#audit-events)

##  October 22, 2019

  * You can attach up to 257 TB of persistent disk storage to each instance. This feature is **Generally available** for most [ machine types ](/compute/docs/machine-types) . 

  * You can issue 100K read I/Os per second on SSD persistent disks. Read the [ persistent disk performance ](/compute/docs/disks#introduction) document for details. 

##  October 21, 2019

  * Increased the per-instance persistent disk write throughput performance for zonal and regional SSD. Read the [ persistent disk performance documentation ](/compute/docs/disks#introduction) for details. 

##  October 07, 2019

  * You can now create a VM instance from a persistent disk snapshot in the API or the ` gcloud ` tool. This feature is now **Generally available** . Read [ Creating a VM instance from a snapshot ](/compute/docs/instances/create-start-instance#createsnapshot) for more information. 

##  October 02, 2019

  * OS Inventory Management is now **Generally available** . For more information, read [ Viewing operating system details ](/compute/docs/instances/view-os-details) . 

##  October 01, 2019

  * Importing VM instances using open virtual appliance (OVA) is now **Generally available** . For more information, read [ Importing virtual appliances ](/compute/docs/import/import-ovf-files) . 

##  September 27, 2019

  * N2 machine types are now **Generally available** . Learn more about [ N2 machine types ](/compute/docs/machine-types#n2_machine_types) . 

##  September 25, 2019

  * The gVNIC virtual network interface is now available in **Beta** . For more information, see [ Creating VM instances that use the gVNIC network interface ](/compute/docs/instances/create-vm-with-gvnic) . 
  * The v1beta1 server and v0.1 metadata server endpoints are deprecated and are scheduled for shutdown. For information about transitioning to the v1 metadata server endpoint, see [ Transitioning to the v1 metadata server endpoint ](/compute/docs/storing-retrieving-metadata#transitioning) . 
  * For additional security when connecting to Linux instances, you can now store your host keys as guest attributes. This feature is now in **General availability** , see [ Storing host keys ](/compute/docs/instances/connecting-to-instance#store-host-key) . 

##  September 24, 2019

  * Instances with more than 16 vCPUs have an increased standard persistent disk bandwidth limit of 1200 MB/s for reads and 400 MB/s for writes. Instances with between 8 and 15 vCPUs also have an increased standard persistent disk bandwidth limit of 800 MB/s reads and 400 MB/s for writes. Read the [ Persistent Disk Performance ](/compute/docs/disks#introduction) page for details. 

##  September 23, 2019

  * N2 machine types are now available in the following regions and zones: 

    * Taiwan ` asia-east1-a ` , ` asia-east1-b `
    * Netherlands ` europe-west4-a `
    * Iowa ` us-central1-f `
  * C2 machine types are now available in following regions and zones: 

    * Singapore ` asia-southeast1-b ` , ` asia-southeast1-c `
    * Netherlands ` europe-west4-a `
    * Los Angeles ` us-west2-a ` , ` us-west2-c `
    * Iowa ` us-central1-f `

##  September 16, 2019

  * C2 machine types are now available in the South Carolina ` us-east1 ` region in all zones. 

##  September 13, 2019

  * Launched support for [ virtual displays ](/compute/docs/instances/enable-instance-virtual-display) to **General availability** . 

##  September 04, 2019

  * [ Reserving zonal resources ](/compute/docs/instances/reserving-zonal-resources) is now **Generally available** . Reserve VMs, with or without GPUs and local SSD, in a specific zone. 

##  September 03, 2019

  * Renamed ` n1-megamem ` and ` n1-ultramem ` machine types to ` m1-megamem ` and ` m1-ultramem ` respectively. 
  * M1 machine types are now available in Taiwan, London, and Mumbai. 

##  August 26, 2019

  * Larger memory-optimized machine types are now **Generally Available** . Learn more about these [ larger ultramem machine types ](/compute/docs/machine-types#memory-optimized_machine_type_family) . 

##  August 23, 2019

  * N2 machine types are now available in Singapore and in the ` europe-west4-a ` zone in the Netherlands. See [ machine types ](/compute/docs/machine-types) for more information. 
  * C2 machine types are now available in zones in Taiwan, Tokyo, London, and in the ` europe-west4-a ` zone in the Netherlands. See [ machine types ](/compute/docs/machine-types) for more information. 

##  August 13, 2019

  * Specifying an image storage location is now available in **beta** for custom images. Specifying your image storage location helps you meet your regulatory and compliance requirements for data locality as well as your high availability needs by ensuring redundancy across regions. See [ Creating, deleting, and deprecating custom images ](/compute/docs/images/create-delete-deprecate-private-images) , and [ Creating a Windows image ](/compute/docs/instances/windows/creating-windows-os-image) . 
  * For additional security when connecting to Linux instances, you can now store your host keys as guest attributes. This feature is now available in **beta** , see [ Storing host keys ](/compute/docs/instances/connecting-to-instance#store-host-key) . 

##  August 12, 2019

  * Scheduled snapshots for persistent disks are now **Generally Available** . For more information, see [ Creating scheduled snapshots for persistent disk ](/compute/docs/disks/scheduled-snapshots) . 

  * New general-purpose [ N2 machine types ](/compute/docs/machine-types#n2_machine_types) are now available in **beta** . 

##  July 31, 2019

  * [ Compute-optimized machine types ](/compute/docs/machine-types#c2_machine_types) , are now available in **General Availability** . Applicable [ charges ](/compute/vm-instance-pricing#c2_machine_types) will apply. 

##  July 25, 2019

  * New larger memory-optimized machine types are now available in **beta** . Learn more about these [ larger ultramem machine types ](/compute/docs/machine-types#memory-optimized_machine_type_family) . 

##  July 17, 2019

  * Memory-optimized commitments are now available in **beta** . Read about [ Committed Use Discounts ](/compute/docs/instances/signing-up-committed-use-discounts) . 

##  July 8, 2019

  * You can now create VMs with [ compute-optimized machine types ](/compute/docs/machine-types#c2_machine_types) , available in **beta** . Applicable [ charges ](/compute/vm-instance-pricing#c2_machine_types) will apply. 
  * You can now view operating system details for your VM instances using OS Inventory Management. This feature is available in **beta** . For more information, read [ Viewing operating system details ](/compute/docs/instances/view-os-details) . 

##  July 2, 2019

  * [ Updating selected VM instances in a managed instance group ](/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#updating_selected_instances) , with minimal disruption and in a controlled way, is now available in **beta** . 
  * Importing VM Instances using OVA or OVF virtual appliances is now available in **beta** . For more information, read [ Importing OVF virtual appliances ](/compute/docs/import/import-ovf-files) . 
  * [ Setting and querying guest attributes ](/compute/docs/storing-retrieving-metadata#guest_attributes) is now **Generally Available** . You can use guest attributes to communicate the status of applications and scripts within your instance. 

##  June 27, 2019

  * [ Mounting a persistent disk as a data volume in a container on Compute Engine ](/compute/docs/containers/configuring-options-to-run-containers#mounting_a_persistent_disk_as_a_data_volume) is now **Generally Available** . 

##  June 18, 2019

  * [ Bring your own license with in-place restarts ](/compute/docs/instances/windows/bring-your-own-license/bringing-your-own-license-sole-tenant-nodes) is now available in **General Availability** . 

##  May 17, 2019

  * Regional persistent disks can now be attached to multiple VMs in read-only mode. For more information, read [ Sharing a regional persistent disk between multiple instances ](/compute/docs/disks/regional-persistent-disk#use_multi_instances) . 
  * You can now use the [ Google Cloud Console ](https://console.cloud.google.com/) to [ import virtual disks ](/compute/docs/images/importing-virtual-disks#importing_virtual_disks) . 

##  May 16, 2019

  * Snapshot locations are now **Generally Available** . The storage location of a snapshot affects the availability of the snapshot and networking costs for creating and restoring a snapshot. For more information, see [ Selecting the storage location for a snapshot ](/compute/docs/disks/create-snapshots#selecting_a_storage_location) . 

  * Multi-regional snapshot pricing is now separated from regional snapshot pricing. Read the [ Persistent disk pricing ](/compute/disks-image-pricing#disk) page to learn about multi-regional snapshot pricing. 

##  May 07, 2019

  * The following operating systems are now **Generally Available** as [ public images ](/compute/docs/images#rhel) : 

    * Red Hat Enterprise Linux 8 
    * Red Hat Enterprise Linux for SAP with Update Services and High Availability 7.4 and 7.6 
  * Red Hat has deprecated Red Hat Enterprise Linux 7 for SAP Applications and Red Hat Enterprise Linux 7 for HANA. For more information, read the [ RHEL for SAP offerings ](https://access.redhat.com/articles/3751271) page. As a result, these images are now marked deprecated on Compute Engine. 

##  April 29, 2019

  * [ Reserving zonal resources ](/compute/docs/instances/reserving-zonal-resources) is now available in **beta** . You can reserve memory-optimized and general purpose VMs, with or without GPUs and local SSD, in a specific zone. 

##  April 19, 2019

  * Regional persistent disk is now **Generally Available** . To learn more, read [ Adding or resizing regional persistent disks ](/compute/docs/disks/regional-persistent-disk) . See the [ pricing page ](/compute/disks-image-pricing#disk) to learn how this disk type is billed. 

##  April 18, 2019

  * The ` asia-northeast2 ` Osaka region is now available to all projects and users. The zones in the ` asia-northeast2 ` region have the [ Skylake CPU platform ](/compute/docs/cpu-platforms) . See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

##  April 10, 2019

  * NVIDIA® Tesla® T4 GPU and NVIDIA® Tesla® T4 Virtual Workstations are now **Generally available** , in eight regions. See the [ GPUs on Compute Engine ](/compute/docs/gpus) page to learn more. 

##  April 05, 2019

  * [ Memory-optimized machine types ](/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the following zones: 

    * ` us-east4-b `
    * ` us-east4-c `

See the [ pricing page ](/compute/vm-instance-pricing#megamem) to learn how
these machine types are billed.

##  April 02, 2019

  * [ Bringing your own licenses with sole-tenant nodes ](/compute/docs/instances/windows/bring-your-own-license) is now available in **beta** . 

##  March 29, 2019

  * [ Viewing VM serial port output in Stackdriver ](/compute/docs/instances/viewing-serial-port-output) is now **Generally Available** . If you enable serial port output logging to Stackdriver, logs are retained for 30 days, even if your VM is deleted. 

##  March 28, 2019

  * The Compute Engine [ SLA ](/compute/sla) has been updated. 

##  March 27, 2019

  * You can add virtual display devices to your instances. Use virtual display devices to run applications that require a display device without adding a phyiscal GPU device. Virtual display devices are available in **beta** . Read [ Enabling Virtual Displays on Instances ](/compute/docs/instances/enable-instance-virtual-display) to learn more. 
  * You can now add extra security when connecting to instances using OS Login. For more information, see [ Setting up OS Login with two-factor authentication ](/compute/docs/oslogin/setup-two-factor-authentication) . 

##  March 22, 2019

  * Increased the per-instance persistent disk throughput performance to 240 MB/s for read and write bandwidth. See the [ Persistent Disk Performance ](/compute/docs/disks#introduction) for details. 

##  March 11, 2019

  * Added new ` europe-west6 ` region in Zürich, Switzerland. The ` europe-west6 ` region contains Skylake zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

##  February 27, 2019

  * [ Memory-optimized machine types ](/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the following zones: 

    * ` asia-northeast1-a `
    * ` asia-southeast1-b `
    * ` northamerica-northeast1-b `
    * ` northamerica-northeast1-c `
    * ` southamerica-east1-b `
    * ` southamerica-east1-c `
    * ` us-central1-a `

See the [ pricing page ](/compute/vm-instance-pricing#megamem) to learn how
these machine types are billed.

##  February 21, 2019

  * You can now attach up to 128 independent persistent disks to custom machine types and most predefined machine types. For more details, see [ Persistent disk limits ](/compute/docs/disks#pdnumberlimits) . 

##  February 14, 2019

  * User-created scheduled snapshots for zonal and regional persistent disks is now available in **beta** . Scheduled snapshots allows you to create an automatic snapshot schedule and include a retention policy for maintaining those snapshots. For more information, see [ Creating scheduled snapshots for persistent disk ](/compute/docs/disks/scheduled-snapshots) . 

##  February 11, 2019

  * [ Sole tenant nodes ](/compute/docs/nodes) are now available in Hong Kong ( ` asia-east2 ` ). 
  * [ Application-based health checking and autohealing for managed instance groups ](/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups) is now **Generally Available** . 

##  February 06, 2019

  * Selecting 16 KB physical block size is now in **beta** . You can create zonal and regional persistent disks with a 16 KB physical block. Some database applications might see greater performance by using 16 KB physical block. Read [ Adding Persistent Disks ](/compute/docs/disks/add-persistent-disk#physical_block_storage) for feature details. Read [ Optimizing Persistent Disk and Local SSD Performance ](/compute/docs/disks/performance#size_price_performance) for performance comparisons. Read the [ Best practices for 16 KB persistent disk and MySQL ](/compute/docs/tutorials/16kb-mysql-best-practices) tutorial to learn about performance improvements to a MySQL database. 
  * Users and applications can now write to instance-specific guest-writeable metadata values. You can use guest attributes to communicate status of applications and scripts within your instance. Read [ Setting and querying guest attributes ](/compute/docs/storing-retrieving-metadata#guest-attributes) to learn more. 

##  February 6, 2019

  * The [ Managed Instance Group Updater ](/compute/docs/instance-groups/updating-managed-instance-groups) is now **Generally Available** . This feature enables proactive, flexible rolling updates with the option to canary a new version on a subset of managed instance group VMs. 

##  January 29, 2019

  * [ Granting access to specific Compute resources ](/compute/docs/access/granting-access-to-resources) , such as VM instances, disks, and images, is now **Generally Available** . This feature gives you flexibility to apply the principle of least privilege, for example, to grant collaborators permissions only to the specific resources that they need to do their work. 

##  January 24, 2019

  * Detaching and reattaching boot disks from a stopped VM instance is now available in **GA** . Use the [ Google Cloud Console ](https://console.cloud.google.com/) , ` gcloud ` or API to detach a failed boot disk, fix it, then reattach it back to the original VM instance. You can also use this feature for rollbacks: detach a disk, create a new disk using an earlier snapshot, and attach that restored disk to your VM. See [ Detaching and Reattaching Boot Disks ](/compute/docs/disks/detach-reattach-boot-disk) for details. 

  * [ Creating a VM Instance with a Custom Hostname ](/compute/docs/instances/custom-hostname-vm) is now **Generally Available** . 

##  January 16, 2019

  * NVIDIA® Tesla® T4 GPU and NVIDIA® Tesla® T4 Virtual Workstations are now available, as **beta** , in eight regions. See the [ GPUs on Compute Engine ](/compute/docs/gpus) page to learn more. 

##  January 11, 2019

  * Windows Server 2019 images are now **Generally Available** as a [ public image ](/compute/docs/images) . 
  * Windows Server, version 1809 images are now **Generally Available** as a [ public image ](/compute/docs/images) . This is a Server Core image that is part of the [ semi-annual release cycle ](https://docs.microsoft.com/en-us/windows-server/get-started/semi-annual-channel-overview) for Windows Server. 

##  December 14, 2018

  * User-selected snapshot storage locations are now available in **beta** . The storage location of a snapshot affects the availability of the snapshot and networking costs. For more information, see [ Selecting the storage location for a snapshot ](/compute/docs/disks/create-snapshots#selecting_a_storage_location) . 
  * Snapshot creation might now incur networking charges. These charges will begin after this feature reaches General Availability (GA), and will depend upon the [ storage location of a snapshot ](/compute/docs/disks/create-snapshots#selecting_a_storage_location) and the location of the source disk. For more information, see [ Network charges for snapshot creation and restoration ](https://cloud.google.com/compute/disks-image-pricing#disk) . 

##  November 15, 2018

  * Windows Service Activation using Private Google Access is **Generally Available** . Read the [ Private Google Access ](/compute/docs/instances/windows/creating-managing-windows-instances#internal_ip_activation) page to learn more. 

##  November 13, 2018

  * Detaching and reattaching boot disks from a stopped VM instance is now available in **Beta** . Use the gcloud or API command to detach a failed boot disk, fix it, then reattach it to a different VM instance. See [ Detaching and Reattaching Boot Disks ](/compute/docs/disks/detach-reattach-boot-disk) for details. 

##  November 08, 2018

  * [ Memory-optimized machine types ](/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the ` southamerica-east1-a ` zone. See the [ pricing page ](/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  November 07, 2018

  * [ Creating a VM Instance with a Custom Hostname ](/compute/docs/instances/custom-hostname-vm) is available in **Beta** . 

##  October 24, 2018

  * [ Viewing VM serial port output in Stackdriver ](/compute/docs/instances/viewing-serial-port-output) is available in **Beta** . To help with troubleshooting, these logs can be retained for up to 30 days after a VM instance is deleted. 

##  October 22, 2018

  * The ` asia-east2 ` Hong Kong region is now available to all projects and users. The zones in the ` asia-east2 ` region have the [ Skylake CPU platform ](/compute/docs/cpu-platforms) . See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

##  October 19, 2018

  * [ Memory-optimized machine types ](/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in the ` asia-southeast1-c ` , ` australia-southeast1-c ` , ` europe-west3-a ` , ` europe-west3-b ` and ` us-west2-b ` zones. See the [ pricing page ](/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  October 02, 2018

  * Compute Engine now uses a [ resource based pricing model ](/compute/vm-instance-pricing#pricing) that provides greater savings from [ sustained use discounts ](/compute/docs/sustained-use-discounts) . All machine types except for shared-core machine types are now billed by their individual vCPU and memory usage rather than billing by each machine type. Sustained use discounts are calculated for vCPU and memory usage across an entire region rather than separately for each machine type in each zone. See the [ Compute Engine Pricing ](/compute/vm-instance-pricing#pricing) page for details. 

  * Protect data on Compute Engine with Cloud Key Management Service encryption keys. [ Customer-Managed Encryption Keys ](/compute/docs/disks/customer-managed-encryption) are now generally available. 

##  September 26, 2018

  * NVIDIA® Tesla® P4 GPUs are now **Generally Available** . For information about using GPUs on Compute Engine, see [ GPUs on Compute Engine ](/compute/docs/gpus) . 

  * For graphics-intensive workloads, NVIDIA® GRID®-based virtual workstations using NVIDIA® Tesla® P4 and P100 GPUs are now **Generally Available** . For information on GPUs for graphics-intensive applications, see [ GPUs for graphics workloads ](/compute/docs/gpus#gpu-virtual-workstations) . 

  * NVIDIA® Tesla® v100 GPUs are now available in the ` us-central1-b ` and ` europe-west4-b ` zones. See [ GPUs on Compute Engine ](/compute/docs/gpus#gpus-list) for a complete list of zones where GPUs are available. 

  * NVIDIA® Tesla® P4 GPUs are now available in the ` australia-southeast1-a ` , and ` australia-southeast1-b ` zones. See [ GPUs on Compute Engine ](/compute/docs/gpus#gpus-list) for a complete list of zones where GPUs are available. 

##  September 25, 2018

  * Windows Server instances no longer require a public IP for Windows Service Activation. If your Windows Server instance uses a subnetwork that is enabled for [ Private Google Access ](/compute/docs/instances/windows/creating-managing-windows-instances#internal_ip_activation) , that instance can complete Windows Service Activation over its internal VPC network. Windows Service Activation using Private Google Access is available in **Beta** . Read the [ Private Google Access ](/compute/docs/instances/windows/creating-managing-windows-instances#internal_ip_activation) page to learn more. 

##  September 20, 2018

  * [ Deploying Docker Containers on Compute Engine ](/compute/docs/containers/deploying-containers) is now **Generally Available** . 

##  September 12, 2018

  * Now in **Beta** , you can [ grant access to specific Compute resources ](/compute/docs/access/granting-access-to-resources) , such as VM instances, disks, and images. This feature gives you flexibility to apply the principle of least privilege, for example, to grant collaborators permissions only to the specific resources that they need to do their work. 

##  September 06, 2018

  * [ Zonal DNS names ](/compute/docs/internal-dns#zonal-dns) are now **Generally Available** . Projects that enable the Compute Engine API after today will use zonal DNS names by default. Projects and organizations that enabled the Compute Engine API before today will continue to use global DNS names by default. Migrating a project to an organization will not change the default DNS name for the project. Zonal DNS names are unique to each zone on your internal [ VPC ](/vpc/docs/vpc) networks. Zonal DNS names improve the fault tolerance of your applications when they reference instances on your internal VPC network. New and existing projects can still use global DNS names, but [ migration ](/compute/docs/internal-dns#migrating-to-zonal) is encouraged. Read [ Internal DNS ](/compute/docs/internal-dns) to learn more. 

##  September 4, 2018

  * The ` simulateMaintenanceEvent ` API method is **Generally Available** . Read [ testing your availability policies ](/compute/docs/instances/setting-instance-scheduling-options#testingpolicies) to learn how to simulate a Compute Engine maintenance event and observe how the instance availability settings affect the behavior of your instances. 

##  August 27, 2018

  * NVIDIA® Tesla® V100 GPUs are now **Generally Available** . For information about using V100 GPUs on Compute Engine, see [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus/) . 

##  August 17, 2018

  * Zonal SSD persistent disks and regional SSD persistent disks now have increased read throughput and read input/output operations per second (IOPS). See [ Optimizing Persistent Disk and Local SSD Performance ](/compute/docs/disks/performance) for more information. 

##  August 8, 2018

  * Sole-tenant nodes are now **Generally Available** . Read [ Sole-tenant Nodes ](/compute/docs/nodes) to learn how you can use these systems to isolate your workloads from each other and from other Compute Engine projects. 

##  August 3, 2018

  * If you have graphics-intensive workloads, such as 3D rendering or video editing, you can create virtual workstations that use NVIDIA® GRID® technology, using NVIDIA® Tesla® P4 and P100 GPUs. For information on GPUs for graphics-intensive applications, see [ GPUs for graphics workloads ](/compute/docs/gpus#gpu-virtual-workstations) . 
  * You can use organization policies to restrict use of your disks, custom images, and snapshots so that they can be used only within your organization or specific projects. This prevents users from creating copies of disks, outside of your organization. Read [ restricting use of your shared images, disks, and snapshots ](/compute/docs/images/sharing-images-across-projects#restrict) to learn more. 

##  July 25, 2018

  * [ Shielded VM ](/security/shielded-cloud/shielded-vm) is now available in **Beta** . Shielded VM images offer security features like UEFI-compliant firmware, Secure Boot, and vTPM-protected Measured Boot. 

##  July 23, 2018

  * The ` n1-megamem-* ` family of [ memory-optimized machine types ](/compute/docs/machine-types#megamem) with 1.4 TB of memory are now **Generally Available** to all projects. See the [ pricing page ](/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  July 19, 2018

  * Selecting specific zones for regional managed instance groups is now **Generally Available** . See [ Distributing Instances using Regional Managed Instance Groups ](/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selecting_zones) . 

  * Windows Server for Containers is now **Generally Available** as a [ public image ](/compute/docs/images#os-compute-support) . 

##  July 18, 2018

  * [ Memory-optimized machine types ](/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now **Generally Available** . See the [ pricing page ](/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  July 17, 2018

  * If you need high availability and redundancy for your Microsoft SQL Server on Compute Engine, you can [ configure an Always On Failover Cluster Instance (FCI) with Storage Spaces Direct (S2D) ](https://cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance) . 

##  July 11, 2018

  * [ Virtual machine sizing recommendations ](/compute/docs/instances/viewing-sizing-recommendations-for-instances) are now **Generally Available** . 

##  July 10, 2018

  * Added new ` us-west2 ` Los Angeles region. ` us-west2 ` contains Skylake zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

  * If you try to create a new instance in this zone for a project that existed before this release date, you may receive the following error message: "No default subnetwork was found in the region of the instance." This issue will be resolved within three days of this launch. In the meantime, the workaround is to [ manually create a subnet ](/vpc/docs/using-vpc) and use it for a new VM. 

  * [ Creating an instance template from a VM instance ](/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) is now **Generally Available** . This feature can be used for instance duplication, backup, and recreation. 

##  July 2, 2018

  * You can now add 2 and 4 NVIDIA® Tesla® V100 GPUs to your Compute Engine instances. For information about using GPUs on Compute Engine, see [ GPUs on Compute Engine ](/compute/docs/gpus) . 

##  June 22, 2018

  * You can [ purchase committed use discounts ](/compute/docs/instances/signing-up-committed-use-discounts) for [ memory-optimized machine types ](/compute/docs/machine-types#megamem) . Memory-optimized machine types use their own commitment type with different pricing. You must [ request access ](https://docs.google.com/forms/d/e/1FAIpQLSe534-lhy0aQq4agiSi7ERSKddJS2QrwZo_jYQDNKkKnT3Y3Q/viewform?usp=sf_link) to use committed use discounts for memory-optimized machine types. See the [ pricing page ](/compute/vm-instance-pricing#committed_use) for pricing details about committed use discounts. 

##  June 19, 2018

  * The Compute Engine Trusted Images policy is now **Generally Available** . Use this policy to control which boot disk images your project members can access. Read [ Restricting Access to Images ](/compute/docs/images/restricting-image-access) for more information. 

##  June 11, 2018

  * Added new ` europe-north1 ` region. ` europe-north1 ` contains Skylake zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

  * If you try to create a new instance in this zone for a project that existed before this release date, you may receive the following error message: "No default subnetwork was found in the region of the instance." This issue will be resolved within three days of this launch. In the meanwhile, the workaround is to [ manually create a subnet ](/vpc/docs/using-vpc) and use it for a new VM. 

  * The prices for GPUs on preemptible VM instances have reduced. For the updated prices, see the [ GPUs pricing page ](/compute/gpus-pricing) . 

  * GPUs on preemptible VM instances are now **Generally Available** . 

For information about using GPUs on Compute Engine, see [ GPUs on Compute
Engine ](/compute/docs/gpus) .

##  June 07, 2018

  * You can create sole-tenant nodes, which are physical Compute Engine servers that are dedicated to hosting only VM instances from your specific project. Read [ Sole-tenant Nodes ](/compute/docs/nodes) to learn how you can use these systems to isolate your workloads from each other and from other Compute Engine projects. 

##  June 05, 2018

  * Protect data on Compute Engine with Cloud Key Management Service encryption keys. [ Customer-Managed Encryption Keys ](/compute/docs/disks/customer-managed-encryption) are now available in beta. 

##  May 28, 2018

NVIDIA® Tesla® V100 GPUs are now available in the following regions:

  * us-west1-a 
  * us-central1-a 
  * asia-east1-c 

For information about using V100 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus/) .

##  May 23, 2018

  * Added support for [ regional persistent disks ](/compute/docs/disks#repds) into **Beta** . This feature provides synchronous block-level replication across two zones in a region for each regional persistent disk. 

##  May 16, 2018

  * Instances with NVIDIA® Tesla® V100 GPUs can now use Local SSD devices. For information on using V100 GPUs on Compute Engine, see [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus/) . 

##  May 08, 2018

  * [ Memory-optimized machine types ](/compute/docs/machine-types#megamem) with up to 160 vCPUs and 3.75 TB of memory are now available in **Beta** . See the [ pricing page ](/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  May 07, 2018

  * Added local SSD support to the ` europe-west4-a ` zone. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

##  May 01, 2018

  * Added a third zone to the ` asia-southeast1 ` region. This zone supports machine types with up to 96 vCPUs when using the Skylake platform. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

##  April 30, 2018

  * NVIDIA® Tesla® V100 GPUs are now available in **Beta** . For information on the zones where V100 GPUs are available, see [ GPUs on Compute Engine ](https://cloud.google.com/compute/docs/gpus/) . 

##  April 20, 2018

  * NVIDIA® Tesla® P100 GPUs are now **Generally Available** . To learn about the zones where P100 GPUs are available, read [ GPUs on Compute Engine ](/compute/docs/gpus) . 

  * Creating multiple secondary non-boot disks when you [ create your VM instance ](/compute/docs/instances/create-start-instance) is now **Generally Available** . 

##  April 19, 2018

  * The price of SLES for SAP images is reduced. Read [ SUSE premium image pricing ](/compute/disks-image-pricing#suse_images) for details. 

##  April 17, 2018

NVIDIA® Tesla® P100 GPUs are now available in the following zones:

  * ` asia-east1-c `
  * ` europe-west4-a `

To learn more about using GPUs on Compute Engine, see [ GPUs on Compute Engine
](https://cloud.google.com/compute/docs/gpus/) .

##  April 11, 2018

  * You can now run simulated maintenance events to test the effects of live migration, termination, and preemption on your instances. Simulated maintenance events are available in **Beta** . Read [ testing your availability policies ](/compute/docs/instances/setting-instance-scheduling-options#testingpolicies) to learn how to test maintenance events on your instances. 

  * [ Nested Virtualization ](/compute/docs/instances/enable-nested-virtualization-vm-instances) is now **Generally Available** . 

##  March 28, 2018

  * You can import existing virtual disks (VMDKs, VHDs, etc) into Compute Engine as custom images. [ Importing virtual disks ](/compute/docs/images/importing-virtual-disks) is now **Generally Available** . 

##  March 23, 2018

  * You can import a Windows Server 2003 server to Compute Engine using the CloudEndure migration service. For steps, see [ Migrating VMs to Compute Engine ](/compute/docs/instances/migrating-vms-compute-engine) . 

##  March 14, 2018

  * Creating an image from a snapshot is now **Generally Available** . See the [ creating custom images ](/compute/docs/images/create-delete-deprecate-private-images#creating_a_custom_image) page. 

##  March 13, 2018

  * Added a third zone to the ` europe-west4 ` region. This zone supports 96 vCPU high memory/high CPU machines. There is no support for local SSDs at this time. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. For regional managed instance group users, the addition of a third zone in ` europe-west4 ` offers you more flexibilty to specify zones in this region. Note that if you do not specify the zones for your instances, Compute Engine, by default, selects all three zones. See [ Distributing Instances using Regional Managed Instance Groups ](/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) to learn more. 

##  March 08, 2018

  * Added support for PTR records on VM instances to **General Availability** . See [ Creating a PTR record for VM instances ](/compute/docs/instances/create-ptr-record) . 

##  March 07, 2018

  * You can import existing virtual disks (VMDKs, VHDs, etc) into Compute Engine as functioning images. [ Importing virtual disks ](/compute/docs/images/importing-virtual-disks) is available in **Beta** . 

##  March 02, 2018

  * [ Mega-memory machine types ](/compute/docs/machine-types#megamem) with 1.4 TB of memory are now available in **Beta** . See the [ pricing page ](/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

##  February 22, 2018

  * Creating multiple secondary non-boot disks when you [ create your VM instance ](/compute/docs/instances/create-start-instance) is now available in Beta. 

##  February 9, 2018

  * [ 96 vCPU machine types ](/compute/docs/machine-types) are **Generally Available** . These machine types are now available in several additional zones only on the Skylake platform. Read the list of [ available regions and zones ](/compute/docs/regions-zones/regions-zones#available) to see where 96 vCPU machine types are available. 

##  February 1, 2018

  * Added support for [ creating an instance template from a VM instance ](/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) into **Beta** . This feature can be used for instance duplication, backup, and recreation. 

##  January 31, 2018

  * Compute Engine supports [ IAM Custom Roles ](/iam/docs/understanding-custom-roles) . Read the [ IAM Custom Roles documentation ](/iam/docs/understanding-custom-roles) to learn more. You can identify which permissions are required to run Compute Engine methods in both the [ V1 Compute Engine API reference ](/compute/docs/reference/rest/v1) and on the [ Compute Engine IAM Permissions ](/compute/docs/access/iam-permissions) page. 

  * You can configure autoscaling for groups of instances based on a wider range of metrics, which allow you to scale managed instance groups on per-group metrics rather than average resource utilization across all of the instances in a group. [ Autoscaling using per-group metrics ](/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics#per_group_metrics) is available in **Beta** . 

  * You can filter Stackdriver monitoring metrics when you use them to configure autoscaling for your managed instance groups. [ Filtering per-instance metrics ](/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics#filter_per_instance_metrics) is available in **Beta** . 

##  January 24, 2018

  * The OS Login API and key management feature is now **Generally Available** . You can associate your public SSH keys with your Google account or with individual member accounts in a G Suite organization or Cloud Identity organization. Read [ Managing Instance Access ](/compute/docs/instances/managing-instance-access) for more information. 

##  January 22, 2018

  * For NVIDIA® Tesla® K80 GPUs in the ` asia-east1-a ` and ` us-east1-d ` zones, you can create GPU instances with up to 416 GB of memory. 

To learn more about the zones where GPUs are available, read [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus/) .

##  January 11, 2018

  * [ VM Deletion Protection ](/compute/docs/instances/preventing-accidental-vm-deletion) is now **Generally Available** . 

##  January 10, 2018

  * Added new ` europe-west4 ` region. ` europe-west4 ` contains Skylake zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

  * Added new ` northamerica-northeast1 ` Montréal region. ` northamerica-northeast1 ` contains Skylake zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

##  January 8, 2018

  * [ Zonal DNS names ](/compute/docs/internal-dns#zonal-dns) are available in **Beta** . Zonal DNS names are unique to each zone on your internal [ VPC ](/vpc/docs/vpc) networks. Global DNS names continue to resolve, but you can enable zonal DNS names to improve the fault tolerance of your applications when they reference instances on your internal VPC network. Read [ Zonal DNS ](/compute/docs/internal-dns#zonal-dns) to learn more. 

