#  Release notes

This page documents product updates to NetApp Cloud Volumes Service for Google
Cloud. You can periodically check this page for announcements about new and
changed features and related product information.

##  August 2020

  * **Feature** : Introduces a new Cloud Volumes [ service type ](/solutions/partners/netapp-cloud-volumes/service-types) . Cloud Volumes Service provides two service types: CVS and CVS-Performance. The new general-purpose CVS service type is intended for standard workloads, such as file and application shares, secondary storage, and moderate application workloads that need up to 100 MiB/s of performance. The _CVS-Performance service type_ name refers to the service that was previously available as _Cloud Volumes Service_ before the introduction of separate service types. 

  * **Feature** : The CVS service type is available in the following regions: ` us-west1 ` (Oregon), ` us-east1 ` (South Carolina), ` europe-west1 ` (Belgium), ` europe-north1 ` (Finland), and ` southamerica-east1 ` (São Paulo, Brazil). The CVS-Performance service type is available in the ` europe-west4 ` (Netherlands) and ` northamerica-northeast1 ` (Montreal) regions. See [ Regional availability for Cloud Volumes Service ](/solutions/partners/netapp-cloud-volumes/regional-availability) . 

  * **Feature** : Volumes that use the CVS service type can be backed up to Google Cloud Storage using the API for long-term protection and disaster recovery. See [ Backing up and restoring a cloud volume ](/solutions/partners/netapp-cloud-volumes/backing-up-and-restoring) . 

  * **Feature** : Volumes that use the CVS-Performance service type can use NFSv4.1 ACLs. See [ Creating and managing NFS volumes ](/solutions/partners/netapp-cloud-volumes/creating-nfs-volumes) . 

##  May 2020

  * **Feature** : CVS-Performance is certified to run as the storage platform for SAP HANA workloads in Google Cloud. See the [ SAP certifications page on Google Cloud ](https://cloud.google.com/solutions/sap/docs/certifications-sap-hana#netapp_cloud_volumes_service) for details about supported SAP HANA configurations. 

##  April 2020

  * **Feature** : Terraform provider support is available for automated Cloud Volumes Service infrastructure deployments. For more information, see [ Managing cloud volumes using Terraform ](/solutions/partners/netapp-cloud-volumes/managing-cloud-volumes-service-google-cloud-using-terraform) . 

##  March 2020

  * **Feature** : Cloud Volumes Service is available in the ` australia-southeast1 ` (Sydney, Australia) region. See [ Regional availability for Cloud Volumes Service ](/solutions/partners/netapp-cloud-volumes/regional-availability) . 

##  February 2020

  * **Feature** : Cloud Volumes Service supports the NFSv4.1 protocol during volume creation. NFSv4.1 offers better performance, built-in locking, and composite remote procedure calls (RPCs) for applications requiring these additional capabilities. See [ Creating and managing NFS volumes ](/solutions/partners/netapp-cloud-volumes/creating-nfs-volumes) . 

  * **Feature** : Cloud Volumes Service supports SMBv3 multichannel to achieve higher performance for Windows applications. See [ best practices when deploying SMB volumes with SMBv3 multichannel ](/solutions/partners/netapp-cloud-volumes/faqs-netapp#smb_performance_faqs) . 

##  November 2019

  * **Feature** : Cloud Volumes Service is generally available in Google Cloud, as [ announced at Google NEXT '19 UK ](https://www.netapp.com/us/company/news/press-releases/news-rel-20191120-575930.aspx) . 

  * **Feature** : Cloud Volumes Service is generally available in the following regions: ` us-west2 ` (Los Angeles), ` us-central1 ` (Iowa), ` us-east4 ` (Virginia), ` europe-west3 ` (Frankfurt), and ` europe-west2 ` (London). See [ Regional availability for Cloud Volumes Service ](/solutions/partners/netapp-cloud-volumes/regional-availability) . 

