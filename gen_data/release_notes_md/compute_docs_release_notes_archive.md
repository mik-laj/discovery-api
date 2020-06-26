#  Release Notes

This page contains release notes for features and updates to the Compute
Engine service.

**Latest API version: v1**

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/compute-engine-release-
notes.xml `

##  December 2017

**December 22, 2017**

* GPUs are now available in the following zones: 

  * NVIDIA® Tesla® P100 GPUs: 
    * ` us-central1-c `
    * ` us-central1-f `
  * NVIDIA® Tesla® K80 GPUs: 
    * ` us-central1-c `

To learn more about the zones where GPUs are available, read [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus/) .

**December 14, 2017**

  * The OS Login API accepts connections from users who have the Owner or Editor [ legacy roles ](/compute/docs/access#primitive_iam_roles) . Read [ Managing SSH keys using the OS Login API ](/compute/docs/instances/managing-instance-access) to learn more about using OS Login to manage authentication and authorization on Compute Engine instances. 

**December 13, 2017**

  * Added support for [ Preventing VM Deletion ](/compute/docs/instances/preventing-accidental-vm-deletion) . 

**December 06, 2017**

  * Added support for [ creating a VM instance from an instance template ](/compute/docs/instances/create-vm-from-instance-template) into **Beta** . 

##  November 2017

**November 21, 2017**

  * Added support for specifying a static internal IP to **General Availability** . See [ Reserving a Static Internal IP Address ](/compute/docs/ip-addresses/reserve-static-internal-ip-address)

**November 16, 2017**

  * [ Deploying Docker Containers on Compute Engine ](/compute/docs/containers/deploying-containers) is now available in **Beta** . 

**November 15, 2017**

  * Effective today, the Skylake platform no longer incurs a premium charge. Prices for 96 vCPU machine types have been updated to reflect the removal of the Skylake premium. See the [ pricing page ](/compute/vm-instance-pricing#n1_predefined) for more information. 

**November 13, 2017**

  * Launched new [ mega-memory machine types ](/compute/docs/machine-types#megamem) to private **Beta** . See the [ pricing page ](/compute/vm-instance-pricing#megamem) to learn how these machine types are billed. 

**November 06, 2017**

  * The User Accounts service (previously in Beta) is being discontinued and will stop being supported on February 15, 2018. It is recommended that users transition to the [ OS Login API ](/compute/docs/instances/managing-instance-access) in place of the User Accounts service. 

  * Added support for viewing autoscaler logs into **Beta** . See [ Viewing Autoscaler Logs ](/compute/docs/autoscaler/viewing-autoscaler-logs) for more information. 

  * Windows Server for Containers is now available in **Beta** as a [ public image ](/compute/docs/images#os-compute-support) . 

**November 01, 2017**

  * You can associate PTR records with the primary network interface on your instance. Support for PTR records on VM instances is available in **Beta** . Read [ Creating a PTR record for VM instances ](/compute/docs/instances/create-ptr-record) to learn more. 

##  October 2017

**October 31, 2017**

  * Added new ` asia-south1 ` Mumbai region. ` asia-south1 ` contains Skylake zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

**October 30, 2017**

  * Windows Server, version 1709 is now **Generally Available** as a [ public image ](/compute/docs/images) . This is a Server Core image that is part of the [ semi-annual release cycle ](https://docs.microsoft.com/en-us/windows-server/get-started/semi-annual-channel-overview) for Windows Server. Use these images to access newer Windows Server features that are not available in the Long-term Servicing Channel releases. 

  * [ SQL Server 2017 images ](/compute/docs/instances/windows#sql_server) are now available. These images include Windows Server 2016 with SQL Server 2017 preinstalled. 

**October 26, 2017**

  * Launched new [ ` roles/computeViewer ` ](/compute/docs/access/iam) roles to **General Availability** . For more information on IAM roles, read the Compute Engine [ IAM documentation ](/compute/docs/access/iam) . 

**October 19, 2017**

  * You can associate your public SSH keys with your Google account or with individual member accounts in a G Suite organization. When you connect to an instance, those public keys are automatically sent to instances where you have the necessary roles or permissions. This method is an alternative to managing your SSH key pairs in project or instance metadata. This feature is in **Beta** . Read [ Managing Instance Access ](/compute/docs/instances/managing-instance-access) for more information. 

**October 18, 2017**

  * Launched support for [ Specifying a Minimum CPU Platform ](/compute/docs/instances/specify-min-cpu-platform) to **General Availability** . 

**October 13, 2017**

  * Added support for sizing recommendations for managed instance groups to **Beta** . See [ Applying Sizing Recommendations for Managed Instance Groups ](/compute/docs/instance-groups/apply-sizing-recommendations-managed-instance-groups) for more information. 

**October 12, 2017**

  * You can now copy images from other images, including images that are shared from other Cloud Platform projects. This feature is **Generally Available** . To learn how to copy images from these sources, see [ Creating Custom Images ](/compute/docs/images/create-delete-deprecate-private-images) . 

**October 05, 2017**

  * Added support for [ disabling external IPs for VM instances ](/compute/docs/ip-addresses/reserve-static-external-ip-address#disableexternalip) using Organization Polices to **General Availability** . 

  * Launched new [ ` roles/compute.admin ` ](/compute/docs/access/iam) roles to **General Availability** . For more information on IAM roles, read the Compute Engine [ IAM documentation ](/compute/docs/access/iam) . 

  * [ 96-vCPU machine types ](/compute/docs/machine-types) are now available in **Beta** on VM instances in specific zones. 96-vCPU machine types can run only on the Skylake platform. Read the list of [ available regions and zones ](/compute/docs/regions-zones/regions-zones#available) to see where 96-vCPU machine types are available. 

**October 02, 2017**

  * Added support for selecting specific zones for regional managed instance groups into **Beta** . See [ Distributing Instances using Regional Managed Instance Groups ](/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#selecting_zones)

##  September 2017

**September 28, 2017**

  * Added support for [ Nested Virtualization ](/compute/docs/instances/enable-nested-virtualization-vm-instances) into **Beta** . 

**September 27, 2017**

  * NVIDIA® Tesla® P100 GPUs are now available in the ` europe-west1-d ` zone in addition to the previously announced zones. Read [ GPUs on Compute Engine ](/compute/docs/gpus) to learn more about the zones where P100 GPUs are available. 

  * NVIDIA® Tesla® K80 GPUs are now available in the ` asia-east1-b ` zone in addition to the previously announced zones. Read [ GPUs on Compute Engine ](/compute/docs/gpus) to learn more about the zones where GPUs are available. 

**September 26, 2017**

  * Billing increments for Compute Engine virtual machine instances are reduced from per-minute increments to per-second increments. Additionally, the minimum usage cost for these resources is reduced from 10 minutes to 1 minute. Read the [ Compute Engine billing model ](/compute/vm-instance-pricing#billingmodel) page for details. 

**September 21, 2017**

  * NVIDIA® Tesla® P100 GPUs are now available in **Beta** . Read [ GPUs on Compute Engine ](/compute/docs/gpus) to learn more about the zones where P100 GPUs are available. 

  * NVIDIA® Tesla® K80 GPUs are now **Generally Available** . Read [ GPUs on Compute Engine ](/compute/docs/gpus) to learn more about the zones where GPUs are available. 

**September 19, 2017**

  * Instance identity verification is now **Generally Available** for all users and projects. Read [ Verifying the Identity of Instances ](/compute/docs/instances/verifying-instance-identity) to learn how to request and verify signed instance tokens. 

**September 13, 2017**

  * Committed Use Discounts are now **Generally Available** . To learn more, read the documentation for [ Committed Use Discounts ](/compute/docs/instances/signing-up-committed-use-discounts) . 

**September 11, 2017**

  * The Compute Engine Trusted Images policy is now available in **Beta** . Use this policy to control which boot disk images your project members can access. Read [ Restricting Access to Images ](/compute/docs/images/restricting-image-access) for more information. 

**September 05, 2017**

  * Managed Instance Group Updater is now available in **Beta** . Read [ Updating Managed Instance Groups ](/compute/docs/instance-groups/updating-managed-instance-groups) for more information. 

  * Added new ` southamerica-east1 ` region. ` southamerica-east1 ` contains Broadwell zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

##  August 2017

**August 28, 2017**

  * Launched audit logging for Compute Engine to **General Availability** . For more information, read [ Viewing Audit Logs ](/compute/docs/audit-logging) . 

**August 25, 2017**

  * Launched new [ ` roles/compute.admin ` and ` roles/compute.viewer ` ](/compute/docs/access/iam) roles to **Beta** . For more information on IAM roles, read the Compute Engine [ IAM documentation ](/compute/docs/access/iam) . 

**August 21, 2017**

  * The Skylake Platform is now available in zones in the following regions: ` us-central1 ` , ` europe-west1 ` , ` asia-east1 ` , ` us-east1 ` and ` asia-southeast1 ` . For a detailed list of zones that support Skylake, see the [ Regions and Zones ](/compute/docs/regions-zones#available) documentation. 

**August 17, 2017**

  * You can now create [ custom images ](/compute/docs/images#custom_images) from disks even while they are attached to instances. If necessary, you can create images while the instance is running. Read [ Creating Custom Images ](/compute/docs/images/create-delete-deprecate-private-images#creating_a_custom_image) to learn more. 

**August 11, 2017**

  * Added support for specifying a static internal IP to **Beta** . See [ Reserving a Static Internal IP Address ](/compute/docs/ip-addresses/reserve-static-internal-ip-address) for more information. 

**August 08, 2017**

  * Introduced new preemptible pricing for local SSD and lowered normal local SSD by up to 63%. For more information, see the [ Pricing ](/compute/disks-image-pricing#localssdpricing) documentation. 

**August 04, 2017**

  * Added support for newer-style health checks that support TCP, SSL, HTTP, and HTTPS health checking to [ managed instance group autohealing ](/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups) . 

**August 02, 2017**

  * Launched audit logging for Compute Engine to **Beta** . For more information, read [ Viewing Audit Logs ](/compute/docs/audit-logging) . 

**August 01, 2017**

  * Added new ` europe-west3 ` region. ` europe-west3 ` contains Broadwell zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

##  July 2017

**July 27, 2017**

  * You can now use the [ ` gcloud ` command-line tool ](/sdk/downloads) to [ connect to instances without external IP addresses ](/compute/docs/instances/connecting-advanced#sshbetweeninstances) . This feature is available in **Beta** . 

**July 20, 2017**

  * Extended memory is now available in **general availability** . For more information, read [ Adding extended memory to a machine type ](/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory) . 

##  June 2017

**June 28, 2017**

  * Instances with service accounts can now request JSON Web Tokens from their metadata servers. Your applications can use these tokens to verify the identity of an instance before transmitting data to the instance. Read [ Verifying the Identity of Instances ](/compute/docs/instances/verifying-instance-identity) to learn how to request and verify signed instance tokens. This feature is available in **Beta** . 

**June 23, 2017**

  * The [ Skylake Platform ](/compute/docs/regions-zones#available) is now available in the ` us-central1-a ` and ` us-central1-b ` zones. 

**June 21, 2017**

  * [ TCP Proxy Load Balancing ](/compute/docs/load-balancing/tcp-ssl/tcp-proxy) is now **generally available** for all users and projects. 

  * You can now copy images from other images and images that are shared from other Cloud Platform projects. This feature is available in **Beta** . To learn how to copy images from these sources, see [ Creating Custom Images ](/compute/docs/images/create-delete-deprecate-private-images) . 

**June 20, 2017**

  * Added new ` australia-southeast1 ` region. ` australia-southeast1 ` contains Broadwell zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

**June 19, 2017**

  * [ Audit logging for the serial console ](/compute/docs/instances/interacting-with-serial-console#viewing_serial_console_logs) is now available in **General Availability** . 

**June 14, 2017**

  * The ability to [ change the service account identity and access scopes ](/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) for a VM instance is now **generally available** . 

**June 07, 2017**

  * [ Shared VPC ](/compute/docs/shared-vpc) (Previously Cross-Project Networking (XPN)) is now available in **General Availability** . 

  * NVIDIA® Tesla® K80 GPUs are now available in **Beta** in the ` us-east1-c ` and ` europe-west1-d ` zones. Read about [ GPUs on Compute Engine ](/compute/docs/gpus) to learn more about the zones where GPUs are available. 

**June 06, 2017**

  * Added new ` europe-west2 ` region. ` europe-west2 ` contains Broadwell zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

##  May 2017

**May 31, 2017**

  * Launched new [ Skylake Platform ](/compute/docs/regions-zones#available) into **General Availability** . 

  * Launched new feature for [ Specifying a Minimum CPU Platform ](/compute/docs/instances/specify-min-cpu-platform) to **Beta** . 

  * Launched new [ Extended Memory for Custom Machine Types ](/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory) into **Beta** . 

**May 30, 2017**

  * Added new zone, ` us-west1-c ` . See the [ Zones and Region ](/compute/docs/regions-zones#available) documentation for more details. 

**May 25, 2017**

  * [ Labels ](/compute/docs/labeling-resources) are now available in **general availability** . 

**May 15, 2017**

  * [ SLES for SAP ](https://www.suse.com/products/sles-for-sap/) images are now available as [ public images ](/compute/docs/images#os-compute-support) . These images are optimized for SAP applications. 

**May 11, 2017**

  * Server Core for Windows Server [ public images ](/compute/docs/images#os-compute-support) are reduced in size from 50GB to 32GB to reduce the boot disk costs for your instances. By default, these images create boot persistent disks that are 32GB in size. If you require larger boot disks, specify a larger boot disk size when you create your instances or [ resize the boot persistent disk ](/compute/docs/disks/add-persistent-disk) . 

**May 09, 2017**

  * Added new ` us-east4 ` region. ` us-east4 ` contains Broadwell zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

**May 01, 2017**

  * [ 64-vCPUs machine types ](/compute/docs/machine-types) are now **Generally Available** to all users and projects. 

  * Decoupled labels and tags so that creating either a label or a tag will not create the opposing resource. For example, creating a label will no longer create a tag and vice-versa. For more information, read [ Relationship between instance labels and network tags ](/compute/docs/labeling-resources#labels_tags) . 

You can now find information about network tags in the [ Networking
](/compute/docs/vpc/add-remove-network-tags) documentation.

##  April 2017

**April 28, 2017**

  * [ Ubuntu 17.04 Zesty Zapus ](https://wiki.ubuntu.com/ZestyZapus/ReleaseNotes) is available as a [ public image ](/compute/docs/images#os-compute-support) . You can use this image to [ create instances ](/compute/docs/instances/create-start-instance#publicimage) . 
  * [ Ubuntu 12.04 Precise Pangolin ](https://wiki.ubuntu.com/PrecisePangolin/ReleaseNotes) is no longer available as a [ public image ](/compute/docs/images#os-compute-support) . Optionally, you can [ upgrade instances ](https://help.ubuntu.com/lts/serverguide/installing-upgrading.html) that run Ubuntu 12.04 to a newer Ubuntu LTS version. 

**April 27, 2017**

  * Added an API for [ listing references between resources ](/compute/docs/instances/view-references-between-resources) into **Beta** . 

**April 24, 2017**

  * Added support for [ disabling external IPs for VM instances ](/compute/docs/ip-addresses/reserve-static-external-ip-address#disableexternalip) using Organization Polices to **Beta** . 

**April 19, 2017**

  * Created project quota limits that apply to [ All Regions ](/compute/quotas#cpus) . 

**April 12, 2017**

  * Added new ` asia-southeast1 ` region. ` asia-southeast1 ` contains Broadwell zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

  * [ Egress firewall rules ](/compute/docs/firewalls) are now available in **Beta** to all users and projects. 

**April 07, 2017**

  * Added support for [ updating managed instance groups ](/compute/docs/instance-groups/updating-managed-instance-groups) to the [ Google Cloud Console ](https://console.cloud.google.com/) . 

**April 05, 2017**

  * [ TCP proxy load balancing ](/compute/docs/load-balancing/tcp-ssl/tcp-proxy) is now available in **Beta** to all users and projects. 

##  March 2017

**March 28, 2017**

  * Added Debian 9 'Stretch' testing image to ` debian-cloud-testing ` project. For more information, see the [ Debian Testing ](/compute/docs/images#debian_testing) documentation. 

**March 24, 2017**

  * Added support for [ disabling interactive serial console access ](/compute/docs/instances/interacting-with-serial-console#disabling_interactive_serial_console_access_through_organization_policy) using Organization Polices into **Beta** . 

**March 21, 2017**

  * NVIDIA® Tesla® K80 GPUs are now available in **Beta** in the ` us-west1-b ` zone. Read about [ GPUs on Compute Engine ](/compute/docs/gpus) to learn more about the zones where GPUs are available. 

**March 09, 2017**

  * Launched new [ Committed Use Discounts ](/compute/docs/instances/signing-up-committed-use-discounts) feature into Beta, which allows you to purchase committed use contracts in return for deeply discounted prices for VM usage. To learn more, read the documentation for [ Signing Up for Committed Use Discounts ](/compute/docs/instances/signing-up-committed-use-discounts) . 

  * Lowered prices for [ predefined machine types ](/compute/vm-instance-pricing#n1_predefined) and [ custom machine types ](/compute/vm-instance-pricing#custommachinetypepricing) . Preemptible VM prices remain unchanged. 

**March 07, 2017**

  * SSD persistent disks now have increased throughput and IOPS performance, which are particularly beneficial for database and analytics workloads. Instances with 32 vCPUs provide up to 40k read IOPS and 30k write IOPS as well as 800 MB/s of read throughput and 400 MB/s of write throughput. Instances with 16 - 31 vCPUs provide up to 25k read or write IOPS, 480 MB/s of read throughput, and 240 MB/S of write throughput. For complete details about persistent disk performance limits, read [ Persistent Disk Performance ](/compute/docs/disks/performance) . 

  * Simultaneous reads and writes on SSD persistent disks no longer share the same throughput limits. SSD persistent disks can simultaneously read and write at their individual advertised throughput limits. For more information about simultaneous read and write capabilities, read [ Persistent Disk Performance ](/compute/docs/disks/performance#simultaneous-read-write) for details. 

**March 07, 2017**

  * [ Cross-Project Networking (XPN) ](/compute/docs/xpn) is now available in **Beta** to all users and projects. 

**March 06, 2017**

  * SQL Server Enterprise Edition images are now generally available. You can use these [ Public Images ](/compute/docs/images#application_images) to run SQL Server Enterprise Edition on various versions of Windows Server. Additionally, you can use SQL Server Enterprise on Compute Engine to [ create SQL Server Availability Groups ](/compute/docs/instances/sql-server/configure-availability) . 

  * Volume Shadow Copy Service (VSS) snapshots for persistent disks are now generally available. Use VSS snapshots to [ create snapshots of persistent disks ](/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot) on Windows instances without detaching the disk or stopping the instance. 

**March 03, 2017**

  * [ 64-core machine types ](/compute/docs/machine-types) are now available in **Beta** to all users and projects. 

##  February 2017

**February 21, 2017**

  * Launched new [ ` roles/compute.instanceAdmin.v1 ` ](/compute/docs/access/iam) role to General Availability. For more information on IAM roles read the Compute Engine [ IAM documentation ](/compute/docs/access/iam) . 

**February 17, 2017**

  * NVIDIA® Tesla® K80 GPUs are now available on Compute Engine in **Beta** . Attach one or more of these GPUs to your instances to accelerate specific workloads and offload tasks from your vCPUs. [ Add GPUs to your instances ](/compute/docs/gpus/add-gpus) or read about [ GPUs on Compute Engine ](/compute/docs/gpus) to learn more. 

**February 14, 2017**

  * Launched the Compute Engine Image Sharing role, ` compute.imageUser ` , to General Availability. For more information, read [ Sharing Images Across Projects ](/compute/docs/images/sharing-images-across-projects) . 

##  January 2017

**January 30, 2017**

  * Launched new [ VM Migration Service ](/compute/docs/tutorials/migrating-vms-compute-engine) to help users migrate VMs into Compute Engine. 

**January 18, 2017**

  * SQL Server Enterprise Edition images are now available in **Beta** . You can use these [ Public Images ](/compute/docs/images#application_images) to run SQL Server Enterprise Edition on various versions of Windows Server. Additionally, you can use SQL Server Enterprise on Compute Engine to [ create SQL Server Availability Groups ](/compute/docs/instances/sql-server/configure-availability) . 

  * Server Core for Windows Server 2016 and Server Core for Windows Server 2012 R2 are now available as [ public images ](/compute/docs/images) . Use these images to run Windows Server on smaller instances, to save boot disk space, or to run applications that do not require the complete Desktop Experience. 

**January 04, 2017**

  * The size limit for [ importing boot disk images ](/compute/docs/images/import-existing-image) increased from 100GB to 2048GB (2TB). See [ image import requirements ](/compute/docs/images/import-existing-image#requirements) for details. 

**January 03, 2017**

  * Added support for autoscaling charts into the Google Cloud Console. Read [ Viewing autoscaling charts for CPU utilization ](/compute/docs/autoscaler/understanding-autoscaler-decisions#viewing_autoscaling_charts_for_cpu_utilization) for more information. 

##  December 2016

**December 15, 2016**

  * [ Interacting with the Serial Console ](/compute/docs/instances/interacting-with-serial-console) is now generally available. 

**December 14, 2016**

  * Added the [ ability to change the service account and scopes ](/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) assigned to an instance to **Beta** . 

  * It is now possible to view audit logs for the serial console. For more information, see [ Viewing serial console logs ](/compute/docs/instances/interacting-with-serial-console#viewing_serial_console_logs) . 

##  November 2016

**November 22, 2016**

  * Container-VM Image is now called Container-Optimized OS from Google. Container-VM Image has been renamed to Container-Optimized OS to better reflect its focus on container technology and the value it provides. Learn more at [ Container-Optimized OS from Google Documentation ](/container-optimized-os/docs)

**November 21, 2016**

  * Volume Shadow Copy Service (VSS) snapshots for persistent disks are now available in **Beta** . Use VSS snapshots to [ create snapshots of persistent disks ](/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot) on Windows instances without detaching the disk or stopping the instance. 

**November 18, 2016**

  * Launched [ Regional Managed Instance Groups ](/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) into **General Availability** . 

**November 07, 2016**

  * Added new ` asia-northeast1 ` region. ` asia-northeast1 ` contains Broadwell zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

  * Launched new IAM role, ` roles/compute.imageUser ` , into **Beta** , which allows users to get, list, and use images from another project. For more information, read [ Sharing Images Across Projects ](/compute/docs/images/sharing-images-across-projects) . 

**November 01, 2016**

  * [ Customer-Supplied Encryption Keys ](/compute/docs/disks/customer-supplied-encryption) are now available in the following additional countries: 
    * Belgium 
    * Colombia 
    * Finland 
    * Ireland 
    * Netherlands 
    * New Zealand 

##  October 2016

**October 26, 2016**

  * Released a security bulletin about [ CVE-2016-5195 ](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails) . See [ Security Bulletins ](/compute/docs/security-bulletins) for more information. 

**October 17, 2016**

  * Windows Server 2016 and Windows SQL Server 2016 on Windows Server 2016 are now available as [ Public Images ](/compute/docs/images) . You can use these images to [ create Windows instances ](/compute/docs/instances/windows/creating-managing-windows-instances) . 

**October 14, 2016**

  * Launched a new autoscaling feature that supports [ queue-based autoscaling ](/compute/docs/autoscaler/scaling-queue-based) into **Alpha** . You can request access to the feature on the [ documentation ](/compute/docs/autoscaler/scaling-queue-based) . 

##  September 2016

**September 29, 2016**

  * [ SQL Server images ](/compute/docs/instances/windows#sql_server) are now **generally available** . These images include Windows Server with SQL Server preinstalled. The price for SQL Server images includes the licensing cost for SQL Server. This allows you to pay for SQL Server only when you use it with pay as you go billing on a per-minute basis. See the cost for these SQL Server images on the [ pricing page ](/compute/disks-image-pricing#sql_server_pricing) . 

**September 19, 2016**

  * Added support for new [ preemptible CPU quotas ](/compute/docs/instances/create-start-preemptible-instance#preemptible_cpu_quotas) . 

**September 14, 2016**

  * Launched new [ Instance Group Updater ](/compute/docs/instance-groups/updating-managed-instance-groups) into **Alpha** . 
  * Deprecated [ previous Instance Group Updater API ](/compute/docs/instance-groups/creating-groups-of-managed-instances#starting_an_update) . Users should transition to using the new [ Instance Group Updater API ](/compute/docs/instance-groups/updating-managed-instance-groups) instead. 

**September 12, 2016**

  * Instances with 3 TB of total local SSD space are **generally available** . You can create instances with eight [ local SSD devices ](/compute/docs/disks/local-ssd) for a total 3 TB of local SSD storage space. See [ Local SSD limits ](/compute/docs/disks#local_ssd_limits) for available zones and machine types. 

**September 08, 2016**

  * Added new ` guestOsFeatures ` property into Beta, which lets you enable certain guest OS features for your images. For more information, see the documentation for [ guestOsFeatures ](/compute/docs/reference/beta/images#guestOsFeatures) . 

##  August 2016

**August 16, 2016**

  * [ SQL Server images ](/compute/docs/instances/windows#sql_server) are now available in **Beta** . These images include Windows Server with SQL Server preinstalled. The price for SQL Server images includes the licensing cost for SQL Server. This allows you to pay for SQL Server only when you use it with pay as you go billing on a per-minute basis. See the cost for these SQL Server images on the [ pricing page ](/compute/disks-image-pricing#sql_server_pricing) . 

**August 12, 2016**

  * [ SSD persistent disks ](/compute/docs/disks#pdspecs) now have improved IOPS performance. Instances with 16 or more cores can achieve 20,000 IOPS, and instances with 32 vCPUs can achieve 25,000 IOPS with SSD persistent disks of a sufficient size. See the [ persistent disk performance ](/compute/docs/disks/performance#type_comparison) page for details. 

**August 09, 2016**

  * Lowered prices of preemptible virtual machine instances for predefined and custom machine types. To see the new pricing, see the pricing table for [ machine types ](/compute/vm-instance-pricing) . 

##  July 2016

**July 21, 2016**

  * [ Virtual machine sizing recommendations ](/compute/docs/instances/viewing-sizing-recommendations-for-instances) are now available in **Beta** . 

**July 20, 2016**

  * The ` us-west1 ` region is now available, and offers Broadwell zones ` us-west1-a ` and ` us-west1-b ` . See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

  * [ Regional managed instance groups ](/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) are now available in **Beta** . You can use regional managed instance groups to distribute instances across multiple zones in a region and improve your application availability. 

**July 1, 2016**

  * Shutdown Scripts are now **generally available** to use with Compute Engine instances. Shutdown scripts allow users to execute commands, on a best-effort basis, right before an instance is terminated or restarted. For more information, see [ Running Shutdown Scripts ](/compute/docs/shutdownscript) . 

##  June 2016

**June 29, 2016**

  * Protect data on Compute Engine with your own encryption keys. [ Customer-Supplied Encryption Keys ](/compute/docs/disks/customer-supplied-encryption) are now **generally available** for select countries. You can now also [ stop an instance ](/compute/docs/instances/stopping-or-deleting-an-instance) with a persistent disk that is encrypted with your own key. Compute Engine is able to restart your instance if you provide the key. 

**June 27, 2016**

  * Released a new feature into **Beta** where you can enable interactive access to the serial console so you can more easily troubleshoot instances that are not booting properly or that are otherwise inaccessible. See [ Interacting with the Serial Console ](/compute/docs/instances/interacting-with-serial-console) for more information. 

**June 20, 2016**

  * Fixed a bug with how Compute Engine accounts for and computes the metric used to create CPU usage graphs shown in the [ Google Cloud Console ](https://console.cloud.google.com/) VM Instances page and Instance Details page. These graphs should now report CPU usage numbers much closer to the CPU usage inside the guest, and should match numbers reported by guest tools like ` top ` and ` uptime ` . 

**June 14, 2016**

  * The metadata server has been updated so that it only gives a 60 second advance notice before a maintenance event if you have queried for the ` maintenance-event ` attribute of that instance at least once since the last migration. Otherwise, Compute Engine assumes that you do not need advance notice of maintenance events and will not provide a notice 60 seconds before an imminent maintenance event. To learn more about the ` maintenance-event ` attribute, read the [ Getting transparent maintenance notices ](/compute/docs/storing-retrieving-metadata#maintenanceevents) section. 

  * You can now [ specify an instance's internal IP address ](/compute/docs/ip-addresses/reserve-static-external-ip-address#assigninternalip) at instance creation. 

**June 09, 2016**

  * The Debian 7 images and Debian 7 backports images are deprecated. Use the latest [ Debian 8 public image ](/compute/docs/images#os-compute-support) to create new instances or [ upgrade your Debian 7 instances ](https://www.debian.org/releases/jessie/amd64/release-notes/ch-upgrading.en.html) to Debian 8. If you still require Debian 7, see the [ advisory ](https://groups.google.com/forum/#!topic/gce-discussion/eMYFdtVvWK0) message. 

  * CentOS, Debian, and RHEL images version v20160606 or newer now include a new guest environment with the following significant changes: 

    * Linux guest software is installed from, and hosted in, a Google Cloud repository, and is updateable with standard package management tools such as ` apt ` or ` yum ` . 
    * Images no longer contain the deprecated ` gcimagebundle ` tool. If you need to create image file from a Compute Engine instance, use the instructions for [ Exporting an Image to Google Cloud Storage ](/compute/docs/images/export-image) . 
    * Debian images include ` unattended-upgrades ` for security updates. Security updates are installed daily by default. 
    * Debian images install Google Cloud SDK from a deb package hosted in a Google Cloud repository. You can update the ` gcloud ` tool in Debian using the ` apt-get update; apt-get dist-upgrade ` command instead of the ` gcloud components update ` command. 
    * Debian images automatically expand boot disk partitions up to 2 TB regardless of the boot disk size. Previously, if your disk was over 2 TB, Debian images would not expand the boot disk at all. 
    * Debian images include a compiled ` python-crcmod ` library so that composite objects in Google Cloud Storage work correctly with ` gsutil ` . 
  * The new Linux guest environment is published on [ GitHub ](https://github.com/GoogleCloudPlatform/compute-image-packages) . 

##  May 2016

**May 11, 2016**

The following Compute Engine IAM roles are now generally available:

  * ` roles/compute.networkAdmin `
  * ` roles/compute.securityAdmin `
  * ` roles/iam.serviceAccountUser `

For more information, read the [ IAM ](/compute/docs/access/iam)
documentation.

##  April 2016

**April 28, 2016**

  * Images can now be organized into image families for easier management and use. Image families point to the latest version of an operating system image that is not marked as deprecated. [ Create an instance ](/compute/docs/instances/create-start-instance) by specifying an image family with one of the available [ public images ](/compute/docs/images#os-compute-support) . To organize your own images into image families, [ create a custom image ](/compute/docs/images/create-delete-deprecate-private-images) . 

**April 21, 2016**

  * The Ubuntu 16.04 LTS [ Xenial Xerus ](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes) image is available. 

**April 5, 2016**

  * [ Health checking ](/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups) is available in **Beta** for managed instance groups. Use [ health checking ](/compute/docs/instance-groups/creating-groups-of-managed-instances#monitoring_groups) to automatically identify and recreate failing instances in a [ managed instance group ](/compute/docs/instance-groups) . 

**April 4, 2016**

  * You can now attach more than 16 unique persistent disks to an instance with a [ predefined machine type ](/compute/docs/machine-types#predefined_machine_types) . Total persistent disk space per instance is still limited to 64 TB. The number of disks depends on the number of vCPUs that the instance has. This feature is available in **Beta** . See [ disk number limits ](/compute/docs/disks#pdnumberlimits) for details. 

**April 01, 2016**

  * Added support for [ labeling disks, snapshots, and images ](/compute/docs/label-or-tag-resources) into **Beta** . 

##  March 2016

**March 30, 2016**

  * [ Resizeable persistent disks ](/compute/docs/disks#resize_pd) are now **generally available** to all users and projects. You can increase the size of existing persistent disks even while they are attached to running VM instances. 
  * Persistent disks larger than 10 TB are **generally available** . You can now [ create ](/compute/docs/disks/add-persistent-disk#create_disk) or [ resize ](/compute/docs/disks/add-persistent-disk#resize_pd) persistent disks to be up to 64 TB in size. Persistent disks larger than 10 TB can be attached only to [ specific machine types ](/compute/docs/disks#pdlimits) . 

**March 24, 2016**

  * Launched [ virtual machine sizing recommendations ](/compute/docs/instances/viewing-sizing-recommendations-for-instances) into **Alpha** . 

**March 15, 2016**

  * Launched [ regional managed instance groups ](/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) into **Alpha** . 

**March 10, 2016**

  * Launched Compute Engine IAM roles into **Beta** . [ Learn more about Compute Engine IAM roles ](/compute/docs/access/iam) . 

  * Added support for [ custom service accounts ](/compute/docs/access/service-accounts) into **Beta** . 

**March 7, 2016**

  * Updated the way that SSH keys work in project metadata and instance metadata. If you manage SSH keys manually, [ use the new metadata values ](/compute/docs/instances/adding-removing-ssh-keys) . 

##  February 2016

**February 23, 2016**

  * Added a requirement that account owners who are enabled for [ user accounts ](/compute/docs/access/user-accounts) must also be granted permission to act as a service account before they can connect to instances that are enabled for service accounts. Read the [ documentation ](/compute/docs/access/user-accounts#create_a_new_user_account) for more information. 

**February 17, 2016**

  * Custom machine types are now **generally available** to all projects and users. [ Learn more about custom machine types ](/compute/docs/instances/creating-instance-with-custom-machine-type) . 

**February 16, 2016**

  * Released a security bulletin about [ CVE-2015-7547 ](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-getaddrinfo-stack.html) . See [ Security Bulletins ](/compute/docs/security-bulletins) for more information. 

**February 10, 2016**

  * Launched support for [ changing the machine type of a stopped instance ](/compute/docs/instances/changing-machine-type-of-stopped-instance) into **General Availability** . 

**February 05, 2016**

  * [ OpenSUSE Leap 42 images ](/compute/docs/images) are now available to all users and projects starting with image opensuse-leap-42-1-v20160202. 

##  January 2016

**January 29, 2016**

  * You can now attach up to eight [ local SSD devices ](/compute/docs/disks/local-ssd) to each of your instances for a total of 3 TB of local SSD space per instance. Attaching more than 1.5 TB of local SSD space to a single instance is a **Beta** feature and is available only in some zones. See [ Local SSD limits ](/compute/docs/disks#local_ssd_limits) for details. 

##  December 2015

**December 17, 2015**

  * Persistent disks larger than 10 TB are in **Beta** . You can now create disks up to 64 TB in size. Persistent disks larger than 10 TB can be attached only to [ specific machine types ](/compute/docs/disks#increased_persistent_disk_limits) . 
  * You can [ resize persistent disks ](/compute/docs/disks/add-persistent-disk#resize_pd) to provide more disk space and throughput to your instances. This feature is now available in **Beta** . 

##  November 2015

**November 18, 2015**

  * Launched support for [ custom machine types ](/compute/docs/instances/creating-instance-with-custom-machine-type) into **Beta** . 

**November 13, 2015**

  * Updated the [ resource quotas ](/compute/quotas) page to reflect that quotas are now listed on the [ Quotas ](https://console.cloud.google.com/iam-admin/quotas) page in the Cloud Console. 

**November 12, 2015**

  * Launched support for [ changing the machine type of a stopped instance ](/compute/docs/instances/changing-machine-type-of-stopped-instance) into **Beta** . 

##  October 2015

**October 15, 2015**

  * Launched [ Instance Labels ](/compute/docs/label-or-tag-resources#labeling_resources) into **Beta** . 
  * Added support for filtering on nested fields in the Compute Engine [ Beta API ](/compute/docs/reference/beta/instances/list#filter) . 

**October 09, 2015**

  * Added support for using [ Mailgun ](http://mailgun.com) to [ send email ](/compute/docs/tutorials/sending-mail/using-mailgun) . 

**October 05, 2015**

  * Updated [ activity logs ](/compute/docs/activity-logs) so that the log data contains a ` structPayload ` in JSON format instead of a ` textPayload ` in protobuf format. See [ examples ](/compute/docs/activity-logs#sample_log_entry) in the [ Activity Logs documentation ](/compute/docs/activity-logs) for more information. 

**October 01, 2015**

  * Added new us-east1 region. us-east1 contains Haswell zones that are now available to all projects and users. See [ Regions and Zones ](/compute/docs/regions-zones) for more information. 

##  September 2015

**September 30, 2015**

  * The [ User Accounts ](/compute/docs/access/user-accounts) service is now available in **Beta** . Updates include: 
    * Release of new ` beta-accounts.. ` images that have user accounts enabled. 
    * Update to [ quota ](/compute/docs/access/user-accounts#quotas) limits. 

**September 08, 2015**

  * [ Preemptible instances ](/compute/docs/instances/preemptible) are now * _Generally Available_ to all users and projects. 

**September 03, 2015**

  * [ 32-vCPUs machine types ](/compute/docs/machine-types) are now **Generally Available** to all users and projects. 
  * [ Instance Groups ](/compute/docs/instance-groups) and [ Autoscaler ](/compute/docs/autoscaler) are now **Generally Available** to all users and projects. 

##  July 2015

**July 28, 2015**

  * [ Debian 8 images ](/compute/docs/images#debian) are now available to all users and projects starting with debian-8-jessie-v20150710. 
  * Protect data on Compute Engine with your own encryption keys. The [ Customer-Supplied Encryption Keys ](/compute/docs/disks/customer-supplied-encryption) feature is now available in **Beta** for select countries. 

**July 15, 2015**

  * Updated the [ User Accounts API ](/compute/docs/access/user-accounts/api/latest) to use a new API endpoint: 
    
        https://www.googleapis.com/clouduseraccounts/alpha/...
    

**July 14, 2015**

  * [ Windows images ](/compute/docs/images#windows) are now generally available to all users and projects. Commands for managing Windows instances are no longer in beta. 

**July 01, 2015**

  * Released new Windows images, **20150629** , that supports [ service account scopes ](/compute/docs/access/create-enable-service-accounts-for-instances#tools) . This removes the restriction that users must make their startup script publicly-accessible for Windows instances. 
  * Added new Python and Java script that can programmatically reset a Windows password. See [ Progammatically generate a username and password ](/compute/docs/instances/automate-pw-generation) for more information. 

##  June 2015

**June 29, 2016**

  * Updated the [ User Accounts service ](/compute/docs/access/user-accounts#restrictions) to support the latest Ubuntu images. 

**June 03, 2015**

  * Updated Windows authentication process. Windows images v20150511 and later will use the new scheme by default. ` gcloud ` will now generate a random password for Windows login; it is no longer possible to manually set a Windows password through ` gcloud ` but you can set a custom password in the instance. 

##  May 2015

**May 18, 2015**

  * Added preemptible instances that you can create and run at a much [ lower price ](/compute/vm-instance-pricing) than normal instances. For more information about how to use these instances in your Compute Engine project, see the [ preemptible instances ](/compute/docs/instances/preemptible) documentation. 
  * Lowered the price of all machine types in all locations. For more information, see the [ pricing page ](/compute/vm-instance-pricing) . 

**May 13, 2015**

  * Removed support for running ` sysprep-oobe-script-* ` startup scripts on Windows virtual machines. We recommend using ` windows-startup-script-* ` keys as replacements. For more information, see [ Startup scripts ](/compute/docs/startupscript#providing_a_startup_script_for_windows_instances) . 

**May 08, 2015**

  * Added documentation for configuring [ network time protocol (NTP) ](/compute/docs/instances/managing-instances#configure-ntp) on virtual machine instances. Make sure you adjust your NTP settings before the upcoming leap second on June 30th, 2015**. 

**May 04, 2015**

  * Updated [ activity logs ](/compute/docs/activity-logs) so that the format of the log data is provided in [ protobuf ](https://github.com/google/protobuf) rather than JSON. See [ examples ](/compute/docs/activity-logs#sample_log_entry) in the [ Activity Logs documentation ](/compute/docs/activity-logs) for more information. 

##  April 2015

**April 30, 2015**

  * Added new [ User Accounts ](/compute/docs/access/user-accounts) feature, available in **Alpha** . User accounts allow you to create Linux user accounts for your virtual machines. 

**April 29, 2015**

  * Released instance [ ` stop() ` ](/compute/docs/reference/latest/instances/stop) and [ ` start() ` ](/compute/docs/reference/latest/instances/start) features into **General Availability** . Additionally, stopped instances no longer count towards your CPU resource quotas. See [ Stopping an instance ](/compute/docs/instances/stopping-or-deleting-an-instance) and [ Restarting a stopped instance ](/compute/docs/instances/restarting-an-instance) for more information. 
  * Upgraded us-central1-b to use [ Haswell ](https://en.wikipedia.org/wiki/Haswell_%28microarchitecture%29) processors. All new virtual machines started in us-central1-b will use Haswell processors by default. Existing instances in us-central1-b have been upgraded from Sandy Bridge to Haswell processors. See [ Zones ](/compute/docs/regions-zones#available) and [ Machine Types ](/compute/docs/machine-types) for a full list of available zones and processors. 

**April 27, 2015**

  * Released new Ubuntu 15.04 [ Vivid Vervet ](https://wiki.ubuntu.com/VividVervet/ReleaseNotes) images. See [ Operating Systems ](/compute/docs/images#ubuntu) for more information. 

**April 23, 2015**

  * Added location information about Compute Engine regions. To see specific geographic location of regions, see the [ Regions & Zones ](/compute/docs/regions-zones) documentation. 
  * Added support for [ autoscaling with multiple policies ](/compute/docs/autoscaler/multiple-policies) . 

##  March 2015

**March 30, 2015**

  * Removed europe-west1-a zone, which was deprecated on  October 15, 2014  . 

**March 25, 2015**

  * Added [ shutdown script support on Windows ](/compute/docs/images#windows) for Windows images * _v20150310_ or later. 

**March 19, 2015**

  * [ Windows Server 2012 R2 ](/compute/docs/images#windows) is now available in **Beta** to all users and projects. 
  * Released a security bulletin about [ CVE-2015-1427 ](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) . See [ Security Bulletins ](/compute/docs/security-bulletins) for more information. 

**March 13, 2015**

  * Released the RHEL 7.1 image, ` rhel-7-v20150311 ` . For a full list of new features , see the [ RHEL 7.1 Release Notes ](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/7.1_Release_Notes/index.html) . To use the new image on Compute Engine, see [ Using RHEL 7 images ](/compute/docs/images#rhel) . 
  * For RHEL 7.1 images, Red Hat provides the Kubernetes package to help you manage your containers. 

**March 12, 2015**

  * Added new us-central1-c zone. us-central1-c zone is a Haswell zone that is now available to all projects and users. For more information, see [ Zones ](/compute/docs/regions-zones#available) . 
  * Released new [ Activity Logs ](/compute/docs/activity-logs) feature in **Beta** as part of the [ Cloud Logging service ](/logging) . 

**March 11, 2015**

  * Added new 32-core machine types in **Beta** . For more information and pricing, see [ Machine Types ](/compute/docs/machine-types) and [ Pricing ](/compute/vm-instance-pricing) . 

**March 05, 2015**

  * Released new [ ` moveInstance() ` ](/compute/docs/reference/latest/projects/moveInstance) feature that moves an instance and its attached disks to another zone. See [ Moving an instance between zones ](/compute/docs/instances/moving-instance-across-zones) for more information. 
  * VPN is now available in **Beta** . For more information, see the [ VPN documentation ](/network-connectivity/docs/vpn/concepts/overview) . 

##  February 2015

**February 20, 2015**

  * Removed the limit on number of API requests per day for all projects. See [ API rate limits ](/compute/docs/api-rate-limits) for more information. 

**February 19, 2015**

  * Added new europe-west1-d zone. europe-west1-d zone is a Haswell zone that is now available to all projects and users. Currently, europe-west1-d zone offers 2.3 GHz Intel Xeon E5 v3 [ Haswell ](https://en.wikipedia.org/wiki/Haswell_%28microarchitecture%29) processors. For more information, see [ Zones ](/compute/docs/regions-zones) and [ Machine Types ](/compute/docs/machine-types) . 

**February 05, 2015**

  * Released new Debian 7 images **v20150127** which performs automatic resizing of boot persistent disks up to 2 TB. For more information, see [ Repartition a boot persistent disk ](/compute/docs/disks/add-persistent-disk#resize_pd) . 

**February 04, 2015**

  * Added UUIDs to virtual machine instances that can be queried through the [ dmidecode ](http://www.nongnu.org/dmidecode/) tool. For more information, see [ Identifying an instance through the UUID ](/compute/docs/instances/managing-instances#uuid) . 

##  January 2015

**January 20, 2015**

  * [ Local SSDs ](/compute/docs/local-ssd) are now in General Availability and can be used by all projects and users. 

**January 13, 2015**

  * Released new instance [ ` stop() ` ](/compute/docs/reference/latest/instances/stop) and [ ` start() ` ](/compute/docs/reference/latest/instances/start) features in **Beta** . See [ Stopping an instance ](/compute/docs/instances/stopping-or-deleting-an-instance) and [ Restarting a stopped instance ](/compute/docs/instances/restarting-an-instance) for more information. 

**Note:** Currently, virtual machines with local SSDs cannot be restarted but
we expect to add this functionality in the future. Additionally, during Beta,
stopped virtual machines count toward your available CPU quota but we will
remove this restriction before this feature is generally available.

##  December 2014

**December 23, 2014**

  * Added instructions for [ Importing an AMI image ](/compute/docs/images/import-existing-image#create_image_file) into Compute Engine. 

**December 17, 2014**

  * [ Ubuntu ](/compute/docs/images#ubuntu) images are now in General Availability. 

**December 10, 2014**

  * Added new Windows images alias to ` gcloud compute ` . You can now specify the latest version of the Windows image by providing the following flag with your instance or disk creation request: 
    
        --image windows-2008-r2
    

**December 08, 2014**

  * [ Windows Server 2008 R2 ](/compute/docs/images#windows) is now available in **Beta** to all users and projects. Additionally, we've also added support for [ Microsoft license mobility ](/compute/docs/instances/ms-licensing) . 

**December 02, 2014**

  * Added support for [ local SSD ](/compute/docs/disks/local-ssd) in all zones, **except** us-central1-b and europe-west1-a (which is deprecated). 

##  November 2014

**November 19, 2014**

  * ` gcloud ` version 0.9.37 and higher now has support for local SSD flags without an additional repository download. Additionally, the command-line flags have changed for creating local SSDs. For more information, see [ Local SSD ](/compute/docs/disks/local-ssd) . 
  * Added support for [ shutdown scripts ](/compute/docs/shutdownscript) in [ Ubuntu ](/compute/docs/images#ubuntu) images. 

**November 13, 2014**

  * Released new shutdown script feature in **Beta** for image versions v20141007 and newer. Shutdown scripts allow users to execute commands, on a best-effort basis, right before an instance is terminated or restarted. For more information, see [ Shutdown scripts ](/compute/docs/shutdownscript) . 

**November 04, 2014**

  * Lowered pricing for persistent SSD and persistent disk snapshots. See [ Persistent disk pricing ](/compute/disks-image-pricing#persistentdisk) for more information. 
  * Lowered network pricing. See [ Network pricing ](/vpc/network-pricing) for more information. 
  * Autoscaler is now available in Beta and available to all users and projects. See [ Autoscaler ](/compute/docs/autoscaler) for more information. 

**November 03, 2014**

  * [ Canonical Ubuntu images ](/compute/docs/images#ubuntu) are now in [ Beta ](/terms/launch-stages) . For full release notes, see the [ Canonical release notes ](https://wiki.ubuntu.com/Releases) . 

##  October 2014

**October 29, 2014**

  * Added new europe-west1-c zone. europe-west1-c zone is an Ivy Bridge zone that is now available to all projects and users. See [ Zones ](/compute/docs/regions-zones) for more information. 
  * Released new local SSDs in Beta phase. This is now available to all users and projects. See [ Local SSD ](/compute/docs/disks/local-ssd) for more information. 

**October 15, 2014**

  * Deprecated europe-west1-a zone. ` europe-west1-a ` has been deprecated and will be permanently turned down on March 29th, 2015. You should move all resources to ` europe-west1-b ` and ensure that you are no longer using any resources in ` europe-west1-a ` after March 29th, 2015. 

We expect that an additional zone, ` europe-west1-c ` will be available in two
weeks, on October 31st, 2014.

For instructions on how to move your instances, see [ Moving an instance
between zones ](/compute/docs/instances/moving-instance-across-zones) .

**October 06, 2014**

  * Released new RHEL 7 image, ` rhel-7-v20141001 ` . For more information, see [ Operating Systems ](/compute/docs/images#rhel) . 
  * For RHEL 7 images, updated the firewall configuration so that all traffic is allowed by default, similar to existing CentOS images. 

**October 01, 2014** \+ Lowered pricing for all machine types in all
locations. For more information, see the [ pricing page ](/compute/vm-
instance-pricing) .

##  September 2014

**September 29, 2014**

  * Released new images, ` v20140926 ` , that mitigates additional vulnerabilities in the bash security bug. See [ Security bulletins ](/compute/docs/security-bulletins#20140924) for detailed information. 

**September 19, 2014**

  * Added new ` utilizationTargetType ` property in the API and new ` --custom-metric-utilization-target-type CUSTOM_METRIC_UTILIZATION_TARGET_TYPE ` flag in ` gcloud compute ` that specifies how the target value should be measured, either as a ` GAUGE ` value or a ` DELTA_PER_MINUTE ` value. This property is required if you are specifying a Stackdriver Monitoring metric. For more information, see the [ Autoscaler documentation ](/compute/docs/autoscaler) . 

**September 16, 2014**

  * Updated ` gcloud compute ` behavior so creating a new Windows instance requires an image name and the image project. See [ Starting a new Windows virtual machine ](/compute/docs/instances/creating-and-starting-an-instance) for more information. 

**September 04, 2014**

  * Released new [ CentOS 7 image ](/compute/docs/images#centos) , ` centos-7-v20140903 ` . See [ Operating Systems ](/compute/docs/images#centos) for more information. 

##  August 2014

**August 13, 2014**

  * Released [ ` gcloud compute ` ](/compute/docs/gcloud-compute) into General Availability. Major changes from the last Open Preview release are: 
    * Added new ` compute/zone ` and ` compute/region ` properties that can be used to set a default zone and region. To set the properties, run ` gcloud config set compute/zone ZONE ` and ` gcloud config set compute/region REGION ` . 
    * Added support for overriding disk auto-deletion during instance deletion. 
    * Updated the output of commands that mutate resources to be more human-friendly. The --format flag can be used for more verbose output. 
    * Replaced all ` get ` subcommands with ` describe ` subcommands (e.g., ` gcloud compute instances get ` has been replaced with ` gcloud compute instances describe ` ). 
    * Renamed the ` firewalls ` collection to ` firewall-rules ` . 
    * Added support to the ` addresses ` collection for interacting with global addresses. 

**August 12, 2014**

  * The scheduled maintenance for europe-west1-a zone has been cancelled and all zones have now transitioned to using transparent maintenance. This means that virtual machines set to live migrate will no longer be taken offline for maintenance in any zone. For information on transparent maintenance and how to set your virtual machines to live migrate, see the [ Setting instance scheduling options ](/compute/docs/instances/setting-instance-scheduling-options) documentation. 

**August 04, 2014**

  * Added new zone, ` asia-east1-c ` , with transparent maintenance support. ` asia-east1-c ` is now available to all projects and users. See the [ Zones and Region ](/compute/docs/regions-zones#available) documentation for more details. 

##  July 2014

**July 22, 2014**

  * Released new Windows images ` windows-server-2008-r2-dc-v20140716 ` with the following updates: 

    * Allows load balancing for Windows virtual machines that are not in a zone marked by a ` -windows ` suffix. See the [ Load Balancing ](/compute/docs/load-balancing) documentation for more information. 
    * Fixes a bug where Windows snapshots could not start new instances. 
  * Enabled support for [ Windows virtual machine instances ](/compute/docs/images#windows) in all zones. Windows instances are no longer limited to Windows-specific zones. For information on starting and using Windows instances, see the [ Operating Systems ](/compute/docs/images#windows) documentation. Existing ` -windows ` zones will be inaccessible starting August 15th, 2014 and it is recommended that you restart your instance using the newest Windows image in a non-Windows zone before August 15, 2014. 

**July 10, 2014**

  * Added new zone, ` us-central1-f ` , with transparent maintenance support. ` us-central1-f ` is now available to all projects and users. See the [ Zones and Region ](/compute/docs/regions-zones#available) documentation for more details. 

##  June 2014

**June 25, 2014**

  * SSD persistent disks are now available in General Availability and open to all users and projects. For detailed information about SSD persistent disks, see [ Types of persistent disks ](/compute/docs/disks#introduction) . For pricing information, see the [ pricing page ](/compute/disks-image-pricing#persistentdisk) . 

**June 09, 2014**

  * Released new images ` sles-11-sp3-v20140609 ` to address the [ OpenSSL security bulletin (CVE-2014-0224) ](/compute/docs/security-bulletins) for SUSE Linux Enterprise Server. 

**June 05, 2014**

  * Released new images ` v20140605 ` to address the [ OpenSSL security bulletin (CVE-2014-0224) ](/compute/docs/security-bulletins) . New images include: 
    * ` debian-7-wheezy-v20140605 `
    * ` backports-debian-7-wheezy-v20140605 `
    * ` centos-6-v20140605 `
    * ` rhel-6-v20140605 `

**June 04, 2014**

  * Released new [ SSD persistent disks ](/compute/docs/disks#introduction) in Limited Preview. SSD persistent disks are also charged at a [ different rate ](/compute/docs/pricing#persistentdisk) than standard persistent disks. 
  * Added new [ Usage Export ](/compute/docs/usage-export) feature that lets you export daily and monthly rollup reports about your project's detailed Compute Engine usage. 

##  May 2014

**May 27, 2014**

  * 16 core machine types are now in General Availability. For pricing, review the [ pricing page ](/compute/vm-instance-pricing) . 

**May 13, 2014**

  * Added new field to Image resources, named ` diskSizeGb ` , which shows the size of the image when it is restored to a persistent disk, in GB. 

**May 05, 2014**

  * Updated default firewall rule names. Default firewall rules are automatically created with every project. These rules were previously named ` default-internal ` and ` default-ssh ` . New projects will have the same default firewalls but with the following new names: 

    * ` default-allow-internal ` \- Allows network connections of any protocol and port between any two instances. 
    * ` default-allow-ssh ` \- Allows TCP connections from any source to any instance on the network, over port 22. 
  * Introduced new default firewall rule that will be created with each new project. 

    * ` default-allow-icmp ` \- Allows ICMP traffic from any source to any instance on the network. 

##  April 2014

**April 17, 2014**

  * Updated default Compute Engine API rate limit from 50,000 requests/day to 250,000 requests/day. See [ API rate limits ](/compute/docs/api-rate-limits) for more information. 
  * Introduced new ` Metadata-Flavor: Google ` header to replace the ` X-Google-Metadata-Request: True ` header. This also allows users to easily detect if they are running in Compute Engine by querying for the new header. For more information, see [ Metadata Server ](/compute/docs/metadata#default) . 

**April 14, 2014**

  * Introduced an Asia Pacific region ( ` asia-east1 ` ) and two new supported zones, ` asia-east1-a ` and ` asia-east1-b ` . 

**April 09, 2014**

  * Released new images ` v20140408 ` to address the [ OpenSSL security bulletin (CVE-2014-0160) ](/compute/docs/security-bulletins) . New images include: 
    * ` debian-7-wheezy-v20140408 `
    * ` backports-debian-7-wheezy-v20140408 `
    * ` centos-6-v20140408 `
    * ` rhel-6-v20140408 `

**April 07, 2014**

  * [ RHEL images ](/compute/docs/images#rhel) have moved to General Availability status and are open to all users and projects. 

Note that there is an additional fee for using premium operating systems,
including RHEL. Please review the [ pricing page ](/compute/disks-image-
pricing#premiumimages) for more information.

  * Added new [ Red Hat Cloud Access ](/compute/docs/images#rhel) feature, which allows users to use their RHEL licenses on Compute Engine virtual machine instances. 

  * Removed support for v1beta16. Please transition to using [ v1 ](/compute/docs/reference/latest) if you haven't already. 

**April 02, 2014**

  * gcutil Release 1.15.0 
    * Added feature where gcutil prompts the user to set an initial Windows password in the ` addinstance ` command if the source image is from a Google Windows project. 

##  March 2014

**March 25, 2014**

  * Introduced sustained use discounts. Sustained use discounts lower the effective price of your instances as your usage goes up. When you use a virtual machine for an entire month, this amounts to an additional 30% discount. For more information, see the [ pricing page ](/compute/vm-instance-pricing#sustained_use) . 

Sustained use discounts are effective starting April 1st, 2014.

  * [ Windows Server images ](/compute/docs/images#windows) are now available in limited preview. 

Although we do not currently charge for use, you can review the [ pricing page
](/compute/disks-image-pricing#premiumimages) for the intended Windows Server
image pricing.

  * [ SUSE images ](/compute/docs/images#suse) are now generally available and is available for all users. 

Note that Compute Engine will start charging for SUSE images on April 1st,
2014. See the [ pricing page ](/compute/disks-image-pricing#premiumimages) for
more information.

  * Introduced new [ Replica Pool service ](/compute/docs/replica-pool) , which allows you to create a managed pool of virtual machines based on a reusable template. For more information, see the [ Replica Pool ](/compute/docs/replica-pool) documentation, or the [ Replica Pool API reference ](/compute/docs/replica-pool/v1beta1) . 

**March 19, 2014**

  * [ RHEL images ](/compute/docs/images#rhel) are now in open preview with a new image version, ` v20140318 ` . 

RHEL images are available to all users at no extra cost until April 1,

    1. On April 1, 2014, Compute Engine will start charging for use of these images according to the [ pricing page ](/compute/disks-image-pricing#premiumimages) . 
  * Released new Debian, CentOS, and Debian Backports images, ` v20140318 ` . 

    * For Debian images, network time protocol (NTP) is now configured to use Google services instead of the public NTP pool. 
  * Updated image packages 

    * Google Daemon now syncs ssh keys immediately instead of on a per-minute intervals. 
    * Improved systemd integration. 
    * Fixed Google Daemon data corruption bug. 
    * Startup scripts are now downloaded with curl instead of wget. 
    * Removed harmless warnings. 

**March 14, 2014**

  * Released gcutil 1.14.2. 
    * Fixed issue where performing ` gcutil moveinstances ` with instances with disks whose autoDelete status is set to true would lead to loss of user data. ` gcutil moveinstances ` is now compatible with Compute Engine API v1 only. 

**March 10, 2014**

  * Temporarily disabled support for [ Advanced Vector Extensions (AVX) ](https://wikipedia.org/wiki/Advanced_Vector_Extensions) . Compute Engine has disabled support for AVX due to a stability issue that we are actively investigating. We will re-enable AVX support as soon as we find and fix the root cause. 

**March 06, 2014**

  * [ SUSE images ](/compute/docs/images#suse) are now in open preview. This means that SUSE images are available to all users at no extra cost until April 1, 2014. On April 1, 2014, Compute Engine will start charging for use of these images according to the [ pricing page ](/compute/disks-image-pricing#premiumimages) . 

**March 05, 2014**

  * Added ability for creating and deleting a boot persistent disk when a virtual machine instance is created or deleted. See the [ Instances ](/compute/docs/reference/latest/instances/insert) documentation for more information. 

  * Added support for restoring persistent disk snapshots to a persistent disk of a user-specified size. 

It is now possible to use the ` sizeGb ` parameter when restoring a snapshot.
This can be used to create a persistent disk that is larger than the
persistent disk snapshot. See [ Restoring snapshots to a Larger Size
](/compute/docs/disks/create-snapshots#restoresnapshotlargersize) for more
information.

  * Added support for setting the [ auto-delete state ](/compute/docs/disks/add-persistent-disk#updateautodelete) of a read-write persistent disk. 

  * Released gcutil 1.14.0. 

    * Switched to new, single API call for creating a virtual machine instance with a boot persistent disk. 
    * Added new command, ` setinstancediskautodelete ` , that sets the auto-delete option for persistent disks attached to virtual machine instances. 
    * Added support for specifying a disk size when creating a disk using a snapshot. 
    * Decreased the time spent waiting for SSH keys to propagate during initial instance creation from 120 seconds to 10 seconds. 

##  February 2014

**February 20, 2014**

  * Added support for [ Advanced Vector Extensions (AVX) ](https://wikipedia.org/wiki/Advanced_Vector_Extensions) in new virtual machine instances. 
  * All virtual machine instances created after February 11, 2014 have this feature enabled. To check if your virtual machine instance has this enabled, run the following command in your virtual machine instance: 
    
        $ cat /proc/cpuinfo | grep avx
    
    

If you need to update your instance to use AVX, you must delete and recreate
the instance.

##  December 2013

**December 17, 2013**

  * Released new Protocol Forwarding feature. [ Protocol forwarding ](/compute/docs/protocol-forwarding) allows you to forward traffic to a single virtual machine instance, using a target. instance. Protocol forwarding provides support for these additional features: 
    * ` AH ` : [ IP Authentication Header ](http://tools.ietf.org/html/rfc4302.html) protocol. 
    * ` ESP ` : [ IP Encapsulating Security Payload ](http://www.ietf.org/rfc/rfc2406.txt) protocol. 
    * ` SCTP ` : [ Stream Control Transmission ](http://www.ietf.org/rfc/rfc2960.txt) protocol. 
  * Added support for new [ Target Instance resources ](/compute/docs/load-balancing#targetinstances) , which allows for non-NAT'ed traffic to be forwarded to a single virtual machine instance. 

See [ Protocol forwarding ](/compute/docs/protocol-forwarding) for more
information.

**December 03, 2013**

  * **Compute Engine is now generally available!** Users can now feel confident using Compute Engine to support mission-critical workloads with 24/7 support and a 99.95% monthly SLA. The move to general availability also comes with a host of new features and changes, detailed below. 

  * Released new v1 API. [ v1beta16 ](/compute/docs/reference/v1beta16) is now deprecated and customers should switch to [ v1 ](/compute/docs/reference/latest) . v1beta16 will remain available until March 04, 2014 and v1beta15 will be discontinued on January 03, 

    1. Changes in v1 include (but are not limited to): 

      * **New support for custom kernels and removed support for Google-provided kernels**

Users can now use custom kernels with their images and no longer need to use
Google-built kernels. The Kernels collection has been removed from v1 and all
new images will include embedded kernel binaries as part of the image.

      * **Removed scratch boot disks from v1.**

All scratch boot disks have been deprecated and we recommend transitioning to
using [ persistent disks ](/compute/docs/disks) . In the v1 API, it is not
possible to create a scratch boot disk.

      * **Deprecated *-d machine types.**

All ` *-d ` machine types have been deprecated and no longer supported.
Although you can still create instances with these machine types, we do not
recommend this and will eventually remove these machine types completely.

  * **New machine types** : We've added new 16-core-machine types that are now available for your instances. For more information, review [ machine types ](/compute/docs/machine-types) and [ pricing ](/compute/vm-instance-pricing) . 

  * We've introduced a new **persistent disk model** . Persistent disk performance now scales linearly with the size of the disk. Additionally, we are removing I/O charges for persistent disks completely and lowering the price of persistent disk storage. For more information, review the [ pricing ](/compute/disks-image-pricing) documentation. 

  * Released new metadata server version v1. The following are new changes with the v1 metadata server: 

    * Requests to the metadata server will now require a security header. All requests to the metadata server will require the following header: 

X-Google-Metadata-Requests: True

    * Requests containing the header ` X-Forwarded-For ` will automatically be rejected. 

  * **Released gcutil v1.12.0.**

    * Added awareness of deprecated machine types to ` listmachinetypes ` and the machine type prompt when creating instances. 
    * Made ` --persistent_boot_disk ` the default setting for the ` addinstance ` subcommand since scratch disks were removed from the v1 API. The ` --nopersistent_boot_disk ` flag can only be specified using the v1beta16 API. 
    * Deprecated all kernel-related subcommands and flags when using the v1 API. 
    * Updated gcutil to be distributed with the [ Cloud SDK ](/sdk/docs) . 
    * Raised the default size of persistent disks to 500GB. 
    * Made v1 the default API version. 
  * As part of the Compute Engine move to using **full disk operating system** images, we have made the following changes: 

    * Released new ` backports-debian-wheezy ` image, which allows users to access new features and bug fixes from the backports kernel. 
    * Deprecated Kernels collection. 
    * Remove all support for kernels from the v1 API. 
    * Additionally, [ FreeBSD ](http://www.freebsd.org/) , [ SELinux ](http://selinuxproject.org/page/Main_Page) , and [ CoreOS ](http://coreos.com/) images now known to be functional on Compute Engine instances with the move to full disk operation system images. 
  * Introduced new **premium operating systems limited preview program** . The new premium OS limited preview program lets you use a [ SUSE ](https://www.suse.com/) or [ Red Hat Enterprise Linux (RHEL) ](https://www.redhat.com/products/enterprise-linux/) images built explicitly for Compute Engine instances. Users who are interested in the program can review the documentation and sign up for the program on the [ OS page ](/compute/docs/images) . 

##  November 2013

**November 25, 2013**

  * Released new Debian 7 and CentOS 6 images, ` v20131120 ` . 

    * New images now contain embedded kernels rather than Google-built kernels. For instructions on how to upgrade you persistent disk to use an embedded kernel, review the [ documentation ](/compute/docs/disks#upgrade) . Similarly, you can also upgrade your custom image to use an embedded kernel. 
    * New images allow you to use dmidecode to determine if you are running on Compute Engine. See the [ documentation ](/compute/docs/instances/managing-instances#dmi) for more information. 
  * Deprecated the Kernel resource. Google will no longer provide custom kernels and will instead use community-provided kernels in Google-provided images. 

**November 12, 2013**

  * Added new instance migration and transparent scheduled maintenance features. Compute Engine now offers transparent scheduled maintenance in ` us-central1-a ` and ` us-central1-b ` ; these zones will no longer go offline for scheduled maintenance and Compute Engine will automatically move your instances out of the way of any scheduled maintenance activity. For more information, see [ maintenance events ](/compute/docs/regions-zones#maintenance) . 

  * Added new gcutil release 1.11.0. 

    * Added a new subcommand, ` gcutil whoami ` , that prints out the email of the currently-authenticated user to standard out. 
    * Added two new scope aliases: datastore and userinfo-email. 
    * Added flags to ` gcutil addinstance ` and a new subcommand, ` gcutil setscheduling ` , for controlling instance scheduling parameters. 
    * Disabled host key checking for commands that rely on ssh because there is no secure channel to pass the host key to the client for the first time. 
  * Marked all Debian 6 images as deprecated. 

  * Marked Debian 7 images older than ` debian-7-wheezy-v20130926 ` as deprecated. 

##  October 2013

**October 22, 2013**

  * Deprecated us-central2-a zone. ` us-central2-a ` has been deprecated and will be permanently turned down by December 31st, 2013. You should move all resources to ` us-central1-a ` and/or ` us-central1-b ` (after November 11, 2013) and ensure that you are no longer using any resources in ` us-central2-a ` after December 31st, 2013. 

**October 10, 2013**

  * Added new kernel, ` gce-no-conn-track-v20130813 ` , and images ` v20130926 ` . 
    * ` gce-no-conn-track-v20120813 ` kernel is identical to ` gce-v20130813 kernel ` except that [ connection tracking ](https://wikipedia.org/wiki/Netfilter#Connection_Tracking) is no longer enabled. 
    * Images ` v20130926 ` will use the new ` gce-no-conn-track ` kernel. To use a kernel with connection tracking turned on, specify the ` --kernel ` flag with a previous kernel version, such as ` gce-v20130813 ` . 

**October 07, 2013**

  * Reduce duration of two upcoming maintenance windows for ` us-central1-a ` and ` us-central1-b ` zones. The new maintenance window durations are as follows: 

    * ` us-central2-a ` : Oct 12, 2013 12:00:00 PM - Oct 22, 2013 10:00:00 AM 
    * ` us-central1-b ` : Nov 2, 2013 12:00:00 PM - Nov 10, 2013 12:00:00 PM 
  * Released gcutil 1.9.1. 

    * Fixed a bug in which the tilde in the authentication file path was not being expanded properly. 

**October 3rd, 2013**

  * Added new features to [ load balancing ](/compute/docs/load-balancing) : 

    * New [ ` sessionAffinity ` ](/compute/docs/load-balancing#sessionAffinity) feature allows users to determine the hashing method used to select backend machines that receive traffic. 
    * New [ ` backupPools ` ](/compute/docs/load-balancing#backupPools) and [ ` failoverRatio ` ](/compute/docs/load-balancing#failoverRation) feature allows users to specify a backup target pool, in case a primary target pool becomes unhealthy. 
  * Released new API version v1beta16. [ v1beta15 ](/compute/docs/reference/v1beta15) is now deprecated and customers should switch to [ v1beta16 ](/compute/docs/reference/latest) . v1beta15 will remain available until **January 03, 2014** . Changes in v1beta16 include: 

    * Removed zone quotas. 
    * Added new [ regional quotas ](/compute/docs/resource-quotas) . 
    * Updated the [ global default quotas ](/compute/docs/resource-quotas) with new default limits. 
    * Changed ` addresses().user ` field from a string to a list and renamed the field to ` addresses().users ` . 
    * Added new [ ` setBackup ` ](/compute/docs/reference/latest/targetPools/setBackup) method to set backup target pools for existing primary target pools. 
    * Updated [ TargetPools ](/compute/docs/reference/latest/targetPools) resource representation to describe backup pools, failover ratios, and session affinity. 
  * Released gcutil 1.9.0. 

    * Added ` gcutil settargetpoolbackup ` command. 
    * Added new ` --backup_pool ` and ` --failover_ratio ` flags for the ` gcutil addtargetpool ` command. 
    * Removed ` usage ` field from ` gcutil getzone ` response. 
    * Added new ` usage ` field to ` gcutil getregion ` response. 
    * gcutil now outputs tables thats respect the terminal width. This feature can be turned off using the ` --respect_terminal_width ` flag. 
    * ` gcutil deleteinstance ` with the ` --force ` flag now requests users to explicitly provide ` --[no]delete_boot_pd ` if any of the instances have a boot disk. 
  * Stopped allowing cross-project resource references, such as the ability to create a disk from a snapshot in another project. Previously, it was allowed for projects whose access control lists (ACLs) allowed it, such as situations where multiple projects were owned by one user. 

##  September 2013

**September 10, 2013**

  * Released gcutil 1.8.4. 
    * Fixed an issue whereby reserved IP addresses were not preserved in the ` gcutil moveinstances ` subcommand. 
    * Bug fixed where global flags were not being displayed on ` gcutil --help ` . 
    * Updated gcutil help text. 

**September 05, 2013**

  * Added new Debian images ` v20130816 ` . 
    * Updated images to use latest kernel. 
    * Updated images to use latest gcutil too. 

**September 04, 2013**

  * Removed support for v1beta14. 

**(Updated 09/09/2013)** Removed support for cross-region external IP address
assignment.

##  August 2013

**August 26, 2013**

  * Added support for [ differential snapshots ](/compute/docs/disks/create-snapshots) . 
  * Added information on how to [ send email ](/compute/docs/sending-mail) using [ SendGrid ](http://sendgrid.com) . 
  * Added new CentOS image ` v20130813 ` with the following updates: 

    * Updated image to use the latest kernel. 
    * Updated image to use the latest gcutil tool. 
  * Added new kernels ` v20130813 ` with the following updates: 

    * Added multiqueue support. 
    * Fixed an issue in scheduler that impacted Hadoop. 
    * Added backport pvclock enlightment for softlockup detector. 

**August 6th, 2013**

  * Launched new load balancing service. Compute Engine has launched a load balancing feature that lets you distribute traffic across your instances. Load balancing is especially useful for supporting heavy traffic to your instances and to provide redundancy to avoid failures. For more information, visit the [ load balancing documentation ](/compute/docs/load-balancing) . Additionally, you can review the load balancing [ reference documentation ](/compute/docs/reference/latest/forwardingRules) . 

  * Released gcutil 1.8.3 

    * Added new prompt to select a persistent or scratch boot disk when using ` gcutil addinstance ` . 

**Caution:** Customers with scripts that programmatically create instances in
gcutil will need to update their script to use the `
--[no]persistent_boot_disk ` flag to continue programmatically creating
instances. For more information, see [ ` gcutil addinstance `
](/compute/docs/instances#start_vm) .

    * Changed naming of persistent boot disks that are created during instance creation from ` boot-<instance-name> ` to ` <instance-name> ` . 

    * Added prompt to delete attached persistent disk when using ` gcutil deleteinstance ` . 

    * Added support for [ load balancing ](/compute/docs/load-balancing) . 

  * Added source code for custom tools that Compute Engine images uses, onto [ GitHub ](https://github.com/GoogleCloudPlatform/compute-image-packages) . The list of tools include: 

    * Image Bundle - Creates an image file our of a disk attached to a virtual machine instance. 
    * Google Startup Scripts - Scripts and configuration files that set up a Linux-based image to work smoothly with Compute Engine. 
    * Google Daemon - A service that manages user accounts, maintains SSH login keys, and syncs public endpoint IP addresses. 
  * Added new Debian and CentOS images ` v20130723 ` , with the following updates: 

    * Added latest gsutil version which addresses issues where gsutil was not working properly. 
    * Fixed typo which causes erroneous startup-script-url error. 

##  July 2013

**July 15th, 2013**

  * Marked kernels older than ` gce-v20130603 ` as ` DEPRECATED ` . 
  * Marked deprecated kernels ` gce-v20120912 ` and older as ` OBSOLETE ` . For a list of kernels and their deprecation states, run the following command: 
    
        gcutil --project=<project-id> listkernels
    

**June 26th, 2013**

  * Added bursting for ` f1-micro ` instances. See [ machine types ](/compute/docs/machine-types) for more information. 
  * Added ability to reset an instance through the API. Review the [ documentation for resetting instances ](/compute/docs/instances/restarting-an-instance#resetting_an_instance) for more information, or review the [ ` instances().reset ` ](/compute/docs/reference/latest/instances/reset) reference documentation. 
  * Released gcutil 1.8.2. 
    * Added new ` gcutil resetinstance ` command that allows resetting virtual machine instances. 
    * Fixed region detection when releasing addresses from multiple regions. 
    * Fixed aggregated resource listing with ` --format=names ` . 
    * Fixed the usage help string for ` gcutil addroute ` command. 

##  June 2013

**June 19th, 2013**

  * Added new Debian images ` v20130617 ` . 
  * Added the following updates for Debian 6 and 7 images ` v20130617 ` : 

    * Updated gsutil to 3.31 and gcutil to 1.8.1. 
    * Disable IPv6 by default via /etc/sysctl.d, for optimal user experience. Compute Engine does not currently support IPv6. 
  * Added the following updates for Debian 7 image ` v20130617 ` : 

    * Upgrade pre-installed packages to Debian 7.1, incorporating security updates and miscellaneous important bug fixes. For more information, see the [ Debian announcements ](http://lists.debian.org/debian-announce/2013/msg00003.html) . 

**June 18th, 2013**

  * Added new images ` v20130522 ` and kernels ` v20130603 ` . 
  * Patched new kernel version ` gcg-3.3.8-201305211623 ` and ` gcg-3.3.8-201305291443 ` to address vulnerability in previous kernels. See [ Security Bulletins ](/compute/docs/security_bulletins) for more information. 
  * Fixed kernel warning printed on boot about virtio net multiqueue. 
  * Made ext4 kernel fixes (for ` xfstest ` ). 

##  May 2013

**May 21st, 2013**

  * Increased default per-project total disk quota to 1TB. 
  * Updated gcutil: 
    * Updated documentation for ` gcutil moveinstances ` to provide a warning of possible failures during the moving process. 
    * Improved error detection in the ` gcutil moveinstances ` command. 
    * Fixed behavior where gcutil attempted to use existing persistent disk when recreating an instance with the same name and the ` --persistent_boot_disk ` flag. 
    * Machine type prompts in gcutil now provides a description of the machine types and ` gcutil listimages ` will now only display the name and description of images. 

**May 15th, 2013**

  * Google Compute Engine is available for open signups! We're excited to announce that Google Compute Engine is now available for open signups and anyone can sign up for the service. For signup instructions, see the [ signup page ](/compute/docs/signup) . 

  * Released new API version v1beta15. v1beta14 is now deprecated and customers should switch to v1beta15. v1beta14 will remain available until August 15, 2013 and v1beta13 will be discontinued on **May 31, 2013** . Changes in v1beta15 include: 

    * **Introduced[ new region scope and regional resources ](/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) . **

      * Added new * _regional resource URIs_ to access regional resources, in the form: 
            
                            https://compute.googleapis.com/compute/v1beta15/project/<project-id>/regions/<region-name>/<resource-type>/<resource-name>
            

For example, to access [ regional reserved IPs
](/compute/docs/instances_and_network#reservedaddress) , use the following
regional URI:

            
                            https://compute.googleapis.com/compute/v1beta15/project/example.com:myproject/regions/example-region/addresses
            

      * Updated reserved IP addresses to a regional resource. 

External static IPs are now referred to as reserved IP addresses and are no
longer a global resource. Reserved IPs are now a regional resource that can be
managed through the [ Addresses collection
](/compute/docs/reference/latest/addresses) .

You can also provision, promote, and release external IP addresses through the
Addresses collection, without having to manually request one. For more
information, see the [ Reserved Addresses documentation
](/compute/docs/instances_and_network#reservedaddress) .

    * **Converted machine type resources to per-zone resources.**

To use a machine type, you must now specify the zone in which that machine
type lives:

        
                https://compute.googleapis.com/compute/v1beta15/project/example.com:myproject/zones/example-zone/machineTypes/machineTypeName
        

    * **Changed method of creating Snapshot resources to use a custom verb on the Disk resource.**

To create a Snapshot resource, you must now make a request to the following
URI:

https://compute.googleapis.com/compute/v1beta15/projects/PROJECT_ID/zones/ZONE/disks/DISK/createSnapshot

Snapshots are still accessible by making requests to the Snapshot collection.

    * **Removed ability to assign an internal IP address.**

The ` internalIp ` field on a virtual machine instance is now read-only and
you can no longer manually assign internal IPs to your instances. Compute
Engine will assign internal IPs automatically.

    * **Added a number of new features.**

      * Added new [ Routes ](/compute/docs/reference/latest/routes) collection that lets you set up and manage a virtual machine's routing table. 
      * Added ability to [ reserve and release static IPs ](/compute/docs/reference/latest/addresses) , and to promote ephemeral IPs to static IPs. 
      * Added the ability to request [ aggregate lists ](/compute/docs/reference/latest/instances/aggregatedList) for per-zone and per-region resources. You can request aggregate lists for the following resources: 

        * Instance resources 
        * Disk resources 
        * Address resources 
        * Machine type resources 

For example, you can list instances across all zones by making a request to
the following URI:

        
                https://compute.googleapis.com/compute/v1beta15/project/example.com:myproject/aggregated/instances
        

    * **Introduced new[ shared-core machine types ](/compute/docs/vm-instance-pricing) . **

Shared-core machine types are more cost-effective for running applications
that don't require a lot of resources. New available machine types are `
g1-small ` and ` f1-micro ` .

    * **Updated maximum total persistent disk size that can be attached to a machine type.**

Standard, high-memory, and high-CPU machine types now have an updated maximum
total disk size of **10 TB** . See [ machine types ](/compute/docs/machine-
types) for more information.

  * Updated [ billing model ](/compute/docs/pricing#billingmodel) for instances. Compute Engine has updated our billing model so that instances are billed based on per-minute usage. All instances that run for **10 minutes or less** will be charged for 10 minutes of usage. After the first 10 minutes, usage is charged on a per-minute basis. 

  * Added new images and kernels ` v20130515 ` . 

  * Removed Google-specific repositories from images. The only packaged repositories configured in images are now the Debian archive. Compute Engine still installs Google-specific packages at build time but removed Google- specific repositories for various reasons. 

  * Removed default installation of the ` apiclient ` library. 

  * Changed log location of startup script output to ` /var/log/startupscript.log ` . Also, added startup script log output to the instance's serial port console so you can also run ` gcutil getserialportoutput ` to retrieve startup script log information. 

  * Improved instance creation and deletion time for Debian. 

  * Fixed issue preventing startup script specified in metadata to be downloaded from Google Cloud Storage. 

  * Removed ` dist-upgrade ` from starting on instance boot. 

  * Removed ` google_storage_download ` script. 

  * Released gcutil 1.8.0. 

    * Added support for v1beta15 Compute Engine API. (addresses, regions, per-zone machine types, aggregated lists). 
    * Added ` gcutil config ` command, an alias for ` gcutil auth ` . 
    * When prompting the user to select an image, gcutil will include standard images (CentOS, Debian). 
    * With v1beta15 API, gcutil will use aggregated list API call by default. Aggregated list method will aggregate all resources across all scopes in which the resource of that type exist (for example, aggregated list of instances will list instances in all zones). 
    * Users can specify image from the standard project by specifying image name prefix. For example: ` gcutil addinstance my-instance --image=debian-7 ` . 
      * When moving instances using ` gcutil moveinstances ` , if some of the instances depend on deprecated resources (image, kernel), gcutil will warn before it proceeds with the migration (migration would fail). New flag ` --replace_deprecated ` will create instances in the destination zone with dependencies on deprecated resources updated to recommended replacement resources. 
    * ` List ` commands will display all resources by default. Number of resources listed may be limited using ` --max_results ` flag. ` --fetch_all_pages ` flag is now deprecated. 
    * Improved display of images and kernels list. By default, only newest kernels/images will be displayed when listed or when user is prompted to select an image or kernel. Use ` --old_images ` or ` --old_kernels ` to list all images or kernels, respectively. 
    * When listing imges, the standard images (CentOS, Debian) will be listed in addition to images from the specified project. To list images in the specified project only, use ` --nostandard_images ` flag. 
    * When prompting user to select a machine type, gcutil displays machine type description in addition to the name. 
    * Removed support for v1beta13 Google Compute Engine API. 
  * gcelib is no longer available and if you haven't already, we strongly encourage users to transition to the [ Google APIs Python Client Library ](https://github.com/google/google-api-python-client) . 

**May 7th, 2013**

  * Released new Debian images. Compute Engine is happy to announce that Debian images for Compute Engine are now available for your instances. To view a list of Debian images available to your project, run the following gcutil command: 
    
        gcutil --project=debian-cloud listimages
    

For information about Debian images, see the [ Debian wiki
](http://wiki.debian.org/Cloud/GoogleComputeEngineImage) .

Similarly, you can see a list of CentOS images like so:

    
        gcutil --project=centos-cloud listimages
    

  * Deprecated gcel images. gcel images are now deprecated and we encourage users to transition to either Debian or CentOS images. 

##  April 2013

**April 4th, 2013**

  * Compute Engine available for Role-based signups! We're excited to announce that Compute Engine is now available for users who sign up for [ Role-based Support ](https://cloud.google.com/support/packages) for the Google Cloud Platform! Visit the [ signup page ](/compute/docs/signup) to get started. 
  * Console updates 
    * Added new feature to [ attach a persistent disk to a running instance ](/compute/docs/console#attachingdisk) . 
    * Added new feature to [ start an instance using a boot persistent disk ](/compute/docs/console#bootfrompd) . 
    * Migrated the ability to view REST details of a request to [ Google Cloud Console ](https://console.cloud.google.com/) . 

##  March 2013

**March 29th, 2013**

  * Changed service account token cache period. The metadata server no longer caches service account tokens within 5 minutes of their expiration window. If you need to ensure you always have a valid access token, you can fetch one anytime within 5 minutes of the expiration window. 
  * Fixed a bug where operations created using v1beta13 could not be retrieved using v1beta14. 
  * Fixed a bug where attaching persistent disks with device names may collide with scratch disks. 

**March 8th, 2013**

  * Released new metadata server version v1beta1. See the [ transition guide ](/compute/docs/metadata#transitioning) to help transition your code away from the previous metadata version. v1beta1 changes include: 

    * New metadata server URL: ` http://metadata.google.internal/computeMetadata/v1beta1/ `
    * New metadata tree structure where metadata now live under a ` project/ ` or ` instance/ ` directory. 
    * New URL query parameters. 
      * [ ` wait_for_change ` ](/compute/docs/metadata#waitforchange) : Perform a hanging GET request that returns when the value of the specified metadata key changes. 
      * [ ` recursive ` ](/compute/docs/metadata#aggcontents) : retrieve all content from underneath a directory. 
      * [ ` alt ` ](/compute/docs/metadata#endpoints) : specify the format of the response. 
  * Updated or added new [ default metadata keys ](/compute/docs/metadata#default) . 

  * Added new feature for [ attaching ](/compute/docs/disks#attachdiskrunninginstance) and [ detaching ](/compute/docs/disks#detachdisk) persistent disks to a running instance and new API documentation for [ ` attachDisk ` ](/compute/docs/reference/latest/instances/attachDisk) and [ ` detachDisk ` ](/compute/docs/reference/latest/instances/detachDisk) methods. 

  * Added new images and kernels ` v20130225 ` . 

  * Patched kernels 3.3x to address security vulnerability in kernels 2.6x. 

  * Released new [ security bulletins ](/compute/docs/security_bulletins) page that lists known security issues and their associated fixes. 

  * Removed ` /dev/<em>&lt;disk&gt;</em> ` paths; users should be referencing their disks using the [ ` /dev/disk/by-id/ ` aliases ](/compute/docs/disks/add-persistent-disk) . 

  * Released gcutil 1.7.2. 

    * Added two new commands [ attachDisk ](/compute/docs/disks#attachdiskrunninginstance) and [ detachDisk ](/compute/docs/disks#detachdisk) , which can be used to attach/detach a persistent disk to and from running virtual machine instance. 
    * Fixed an issue where list operations were incorrectly capped at maximum number of results of 100. 
    * Improved of project's IP addresses in ` gcutil getproject ` . 
    * Deprecation information is now printed for deprecated resources. 
    * Removed support for v1beta12 Google Compute Engine API. 

##  February 2013

**February 19th, 2013**

  * gcelib is now deprecated. Downloads and documentation of gcelib will continue to be available for three months, until **May 15, 2013** . During that time, gcelib will work with the v1beta13 API only (it won’t be upgraded to work with v1beta14). Between now and May 15, developers using gcelib are strongly encouraged to migrate their applications to use an alternative client library, such as the [ Google APIs Python Client Library ](/compute/docs/api/python_guide) . 
  * Enabled billing for persistent disk snapshots. For more information on snapshot pricing, see the [ pricing page ](/compute/docs/pricing#persistentdisk) . 

**February 8th, 2013**

  * Released gcutil 1.7.0. 
    * Added a new subcommand, ` gcutil moveinstances ` , for moving instances (and their persistent disks) from one zone to another. 
    * Added ` --zone ` flag to ` gcutil listdisks ` . 
    * Fixed a bug where ` gcutil addsnapshot ` would crash if the ` --zone ` flag was not specified. 
    * Added zone column to the table output of ` gcutil listoperations ` . 
    * Increased the timeout of synchronous operations from 2 minutes to 4 minutes. 

##  January 2013

**January 30th, 2013**

  * Released new API version v1beta14 

v1beta13 is now deprecated and customers should switch to [ v1beta14
](/compute/docs/reference/latest) . v1beta13 will remain available until
**April 30, 2013** , and v1beta12 will be discontinued **February 11, 2013** .

Changes in v1beta14 include:

    * **Introduced[ per-zone and global resources ](/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) **

      * Added new * _per-zone resource URIs_ to access per-zone resources, in the form: 
            
                            https://compute.googleapis.com/compute/v1beta14/projects/<project-id>/zones/<zone>/<resource-type>/<resource-name>
            

For example, accessing a Disk resource requires the following per-zone URI:

            
                            https://compute.googleapis.com/compute/v1beta14/project/example.com:myproject/zones/some-example-zone/disks/mydisk
            

    * _Added new global resource URIs for accessing global resources, in the form:_ * 
        
                https://compute.googleapis.com/compute/v1beta14/projects/<project-id>/<resource-type>/<resource-name>
        

For example, accessing a Machine Type resource requires the following global
URI:

        
                https://compute.googleapis.com/compute/v1beta14/project/example.com:myproject/global/machineTypes/somemachinetype
        

    * **Added a number of new features**

      * Added new [ ` setTags ` ](/compute/docs/reference/latest/instances/setTags) method which allows you to update instance tags for a running instances. 
      * Added new [ ` setMetadata ` ](/compute/docs/reference/latest/instances/setMetadata) method which allows you to update metadata for a running instance. 
      * Added new [ ` deprecate ` ](/compute/docs/reference/latest/images/deprecate) method which allows you to set the deprecation status for an image. 
      * Added new [ boot from Persistent Disk ](/compute/docs/disks#rootfrompd) feature which allows you to store an operating system image on a persistent disk so that it persists through the life of the instance. Multiple instances can also attach to a boot persistent disk in read-only mode. 
    * **Updated existing resource properties**

      * Removed ` kind ` property from ` instance.networkInterfaces ` and ` instance.serviceAccounts ` . 
      * Removed support for using default images and default kernels when creating an instance or an image through the API. Users must now explicitly specify an image or kernel. 
      * Added new [ deprecate status ](/compute/docs/reference/latest/images/deprecate) to resources. 
    * **Updated response codes**

      * Changed error response for inserting an existing instance from ` HTTP 400 ` to ` HTTP 409 ` . 
      * Changed server response for accepting an asynchronous request from ` HTTP 200 ` to ` HTTP 202 ` . 
  * Released gcutil 1.6.0. 

    * Added support for v1beta14 per-zone resources. 
    * Added a new subcommand, [ ` gcutil setinstancemetadata ` ](/compute/docs/metadata#updatinginstancemetadata) , for updating instance metadata. 
    * Added a new subcommand, [ ` gcutil setinstancetags ` ](/compute/docs/label-or-tag-resources#tags) , for updating and setting instance tags. 

      * Added a new subcommand, [ ` gcutil deprecateimage ` ](/compute/docs/images/create-delete-deprecate-private-images#deprecating_an_image) , for setting the deprecated field on an image resource. 
      * Added support for specifying a [ boot persistent disk ](/compute/docs/disks#rootfrompd) when creating a new instance: 

gcutil addinstance my-instance --disk=my-disk,boot

      * Changed the ordering of the machine type prompt when creating instances so the standard machine types show up first, followed by the highcpu and highmem machine types. 

**January 24th, 2013**

  * Added new VM images ` centos-6-v20130104 ` , ` gcel-12-04-v20130104 ` , and ` gcel-10-04-v20130104 `

##  December 2012

**December 14th, 2012**

  * New persistent disk snapshot feature 

Added [ Persistent Disk Snapshot ](/compute/docs/disks/create-snapshots)
feature which allows you to create snapshots of existing persistent disks and
apply them to new disks.

**Note:** Although persistent disk snapshot rates are available on the [
pricing page ](/compute/docs/pricing#persistentdisk) , billing for snapshots
is not yet enabled. We expect to enable snapshot billing in January 2013.

  * Added new error message when querying the metadata server for a service account token that has not been authorized for that instance. 

  * Added new operation types for instance restarts and shutdowns 

  * Released gcutil 1.5.0. 

    * Added subcommands for interacting with snapshots. 

**December 6th, 2012**

  * Added new high-memory and high-CPU machine types. 
    * For instances that require more memory relative to virtual cores, use [ high-memory machine types ](/compute/docs/machine-types) . 
    * For instances that require more virtual cores relative to memory, use [ high-CPU machine types ](/compute/docs/machine-types) . 
  * Added new [ diskless ](/compute/docs/machine-types) machine types. 
  * Lowered pricing for [ standard machine types ](/compute/docs/vm-instance-pricings) . 
  * Added new [ European zones ](/compute/docs/regions-zones) . 
    * ` europe-west1-a `
    * ` europe-west1-b `

##  November 2012

**November 9th, 2012**

  * Released gcutil 1.4.1. 
    * Added new subcommand, ` gcutil getserialportoutput ` , for getting the serial port output from an instance. 
    * Fixed an issue where gcutil waited for instances that failed to be created. 
    * Changed the zone selection feature to display maintenance window information next to the zone names. 
    * Changed the display of operation resources to show the user responsible for the operation. 
  * New VM images and kernel for v20121106 
    * All new images that use a Debian package manager are now named ` gcel-<version> ` . Current images ` ubuntu-12-04-vYYYYMMDD ` and ` ubuntu-10-04-vYYYYMMDD ` are deprecated and will remain available until Feb. 9th, 2013. 
    * Updated ` /etc/lsb-release ` file to reflect new distribution information. 
    * Added support for [ SCSI ](https://wikipedia.org/wiki/SCSI) disk interface; for information on how to convert your instances, see [ Disks Interfaces ](/compute/docs/disks#interface) . 
    * Added ability to clone instances in the console. It is now possible to clone an instance by visiting the instance's details page and clicking the **Clone** button. 

##  October 2012

**October 11th, 2012**

  * Released new API Version v1beta13. v1beta12 is now deprecated and customers should switch to v1beta13. b1Beta12 will remain available until **January 11, 2013** . Changes in v1beta13 include: 

    * Removed ` hostCpus ` field from the machineType resource 
    * Changed API nouns and verbs to use camelCase, specifically: 

      * ` machine-types ` is now ` machineTypes `
      * ` add-access-config ` and ` delete-access-config ` is now ` addAccessConfig ` and ` deleteAccessConfig `
      * ` set-common-instance-metadata ` is now ` setCommonInstanceMetadata `
    * Made ` setCommonInstanceMetadata ` an asynchronous operation, returning an operation resource to track completion of the request 

    * Add serial port output API 

    * Fix metadata key validation and prevent duplicate metadata keys 

    * ` PENDING ` and ` RUNNING ` states of long-running operations now reflect the full lifetime of the request 

    * Delete operations now guarantee that the ` DONE ` state is not reached until after the resource has been completely torn down 

**To update your application code to v1beta13:**

    1. Change all URIs from ` v1beta12 ` to ` v1beta13 ` . For example: 
        
                https://compute.googleapis.com/compute/ **v1beta13** /disks

    2. Update API nouns and verbs that have a dash to use camelCase (e.g. ` machineTypes ` instead of ` machine-types ` ) 

    3. Update your application code to reflect the following changes, if necessary: 

      * ` setCommonInstanceMetadata ` now returns an Operations resource 
      * New metadata keys must match the regex ` [a-zA-Z0-9-_]{1,128} ` and be less than 128 bytes in length. Metadata values cannot be longer than 32768 bytes 

**Note:** If your metadata value exceeds 32768 bytes, consider using a [
startup script ](/compute/docs/howtos/startupscript)

      * Operations can take longer to complete as they now reflect the total time it takes to roll out and confirm the request 

      * Delete operations only return ` DONE ` after the resource has been completely torn down 

      * Instances have new additional ` STOPPING ` state, which means that the instance is currently in process of being stopped 

  * Released gcutil 1.3.4. 

    * Implemented batch ` adddisk ` . It is now possible to add multiple disks with a single call to ` gcutil adddisk ` . 
    * Implemented batch delete operations for additional resources. It is now possible to delete multiple disks, firewalls, images, instances, networks, operations, and snapshots. 
    * Added a ` --format ` flag for the list subcommands. The flag accepts the following values: ` table ` , ` sparse ` , ` json ` , ` csv ` , and ` names ` . ` --format=names ` allows gcutil to be used with Unix tool pipelines: 
        
                gcutil listinstances --format=names | xargs gcutil deleteinstance --force
        

    * Fixed the sorting in list subcommands. Instead of sorting each page individually, gcutil now sorts all results before displaying them to the user. 

    * Changed ` --cache_flag_values ` to not cache flags when the underlying command fails. 

    * Deprecated ` --project_id ` in favor of ` --project ` . ` --project_id ` still works, but will produce a warning. 

    * Reconfigured the version checking to take place when gcutil exits. 

    * Improved documentation for firewall commands. 

    * Changed the headings for ` list ` and ` get ` subcommands. The new headings use dashes instead of spaces and are in lower-case. This eliminates the need to use quotes with the ` --sort_by ` flag and makes the display of the headings more user-friendly. 

  * Added serial console output from a VM instance to the instance details page. 

  * Added support for attaching persistent disks in read-only mode as well as read-write mode. 

  * Added new example gcutil commands for adding instances, disks, networks, and firewalls. 

  * Added support for adding and deleting networks. 

  * Fixed assorted bugs. 

##  September 2012

**September 18th, 2012**

  * Released gcutil 1.2.0. 
    * Added support for ` gs:// ` URLs to the ` addimage ` command. 
    * Implemented support for multiple flag cache files. gcutil now searches for a ` .gcutil.flags ` file starting in the current directory, followed by the parent directories, and the home directory until a file is found. 
    * Added a check to commands dealing with metadata to warn the user of duplicate metadata keys instead of silently ignoring duplicates. 
    * Fixed an issue where ` listoperations ` would not fetch multiple pages when encountering an operation that contains an error. 
      * Changed the way gcutil is packaged. 
      * Made some of the flag descriptions and an error messages more informative. 
  * New Linux VM images v20120912 
    * Added more aggressive validation for ssh keys. 
    * [ make ](http://linux.die.net/man/1/make) package is now included by default. 

**September 13th, 2012**

  * Added newline to the end of ` fstab ` for images created using the image bundling tool. 
  * Added a warning when users try to create hostnames that are 33 characters or longer. 
  * Improved error messaging when a user tries to use an IP address reserved for system purposes. 
  * Added ability to add or remove networks using the Console. 

**September 5th, 2012**

  * Faster asynchronous job completion. 
  * Improved scalability for resource creation, updates, and monitoring. 
  * [ Resource quotas enabled ](/compute/docs/resource-quotas) on a per-project basis, for images, firewalls, and networks. 
  * Enable NAT on ICMP packets. 

##  June 2012

**June 28, 2012** \+ Compute Engine is available for limited preview!

