#  Release notes

This page documents production updates to Cloud Storage. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/storage-release-notes.xml `

##  July 20, 2020

**FEATURE:**

[ Detailed audit logging mode ](https://cloud.google.com/storage/docs/org-
policy-constraints#audit-logging) launched.

##  June 08, 2020

**FEATURE:**

Jakarta region ( ` asia-southeast2 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  May 18, 2020

**CHANGED:**

The V4 signing process is now in GA.

  * The V4 signing process is an improved method for creating [ signatures ](https://cloud.google.com/storage/docs/authentication/signatures) using RSA or HMAC keys. 

##  April 20, 2020

**FEATURE:**

Las Vegas region ( ` us-west4 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  February 28, 2020

**CHANGED:**

[ IAM Conditions for Cloud Storage
](https://cloud.google.com/storage/docs/access-control/using-iam-
permissions#conditions-iam) is now in GA.

##  February 24, 2020

**FEATURE:**

Salt Lake City region ( ` us-west3 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  January 24, 2020

**FEATURE:**

Seoul region ( ` asia-northeast3 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  January 08, 2020

**FEATURE:**

Archive Storage now available.

  * New [ storage class ](https://cloud.google.com/storage/docs/storage-classes#archive) for storing your long-term, rarely accessed data. 

##  December 13, 2019

**FEATURE:**

IAM Conditions  BETA  for Cloud Storage is now available.

  * [ IAM Conditions ](https://cloud.google.com/iam/docs/conditions-overview) allows you to grant permissions for a specified period of time, or to a subset of objects in your buckets. 
  * See [ Using IAM Conditions on buckets ](https://cloud.google.com/storage/docs/access-control/using-iam-permissions#conditions-iam) for step-by-step instructions. 

##  November 18, 2019

**CHANGED:**

[ Uniform bucket-level access ](https://cloud.google.com/storage/docs/uniform-
bucket-level-access) is now in GA.

##  November 15, 2019

**CHANGED:**

JSON API requests should now be made through the ` storage.googleapis.com `
endpoint.

  * New preferred [ request endpoint ](https://cloud.google.com/storage/docs/request-endpoints) for the JSON API. 

**CHANGED:**

New display for bucket lists in the GCP Console.

  * The **Name** column is now always visible in the bucket list. 
  * The column selector now appears as an icon ( ![Column options icon.](/storage/images/bucket-column-options.png) ). 

##  November 07, 2019

**CHANGED:**

The name of the Bucket Policy Only feature is now changed to [ uniform bucket-
level access ](https://cloud.google.com/storage/docs/uniform-bucket-level-
access) .

  * The organization policy and API fields referring to Bucket Policy Only are still supported, but we recommend using the equivalent uniform bucket-level access organization policy and API fields. 

##  October 29, 2019

**CHANGED:**

HMAC keys for service accounts are now in GA.

  * Use the XML API to [ manage your HMAC keys for service accounts ](https://cloud.google.com/storage/docs/authentication/managing-hmackeys) . 

##  September 06, 2019

**CHANGED:**

New Stackdriver metric available to [ check for ACL usage.
](https://cloud.google.com/storage/docs/using-bucket-policy-only#acl-check)

  * Use [ Stackdriver ](https://cloud.google.com/monitoring/) to determine if enabling Bucket Policy Only would break your workflow. 

##  August 14, 2019

**CHANGED:**

Multi-Regional Storage and Regional Storage are now Standard Storage.

  * Combining these into a single [ Standard Storage class ](https://cloud.google.com/storage/docs/storage-classes#standard) separates your storage class considerations from your location considerations. 

##  August 09, 2019

**FEATURE:**

HMAC keys for service accounts  BETA  are now available.

  * Use [ HMAC keys ](https://cloud.google.com/storage/docs/authentication/hmackeys) to create signed requests for the XML API. 
  * [ Creating HMAC keys for service accounts ](https://cloud.google.com/storage/docs/authentication/managing-hmackeys) replaces the need to have HMAC keys for user accounts. 

##  June 28, 2019

**FEATURE:**

[ Dual-regions ](https://cloud.google.com/storage/docs/locations#location-dr)
are now in GA.

##  June 20, 2019

**FEATURE:**

You can now inspect buckets for sensitive information using Cloud Data Loss
Prevention in the [ GCP Console
](https://console.cloud.google.com/storage/browser) .

  * See [ Inspect a Cloud Storage location ](https://cloud.google.com/dlp/docs/inspecting-storage#inspecting-gcs) for step-by-step instructions. 

##  June 18, 2019

**CHANGED:**

Improved object interaction in the GCP Console.

  * [ Object downloads ](https://cloud.google.com/storage/docs/downloading-objects) can be performed using the **more options** menu associated with each object. 
  * Clicking on an object's name opens a page dedicated to details about the object. 

##  June 17, 2019

**ISSUE:**

[ Object composition ](https://cloud.google.com/storage/docs/composite-
objects) cannot be performed if any of the source objects are encrypted with [
customer-managed encryption keys
](https://cloud.google.com/storage/docs/encryption/customer-managed-keys) .

##  May 30, 2019

**CHANGED:**

Improved workflow for creating new buckets in the [ GCP Console
](https://console.cloud.google.com/storage/browser) .

  * See the [ Creating storage buckets ](https://cloud.google.com/storage/docs/creating-buckets) guide for step-by-step instructions. 
  * Estimate your bucket's monthly costs during the bucket creation process. 

##  April 18, 2019

**FEATURE:**

Osaka region ( ` asia-northeast2 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

**CHANGED:**

The C++ Cloud Storage Client Library is now in GA.

  * See the [ list of Cloud Storage guides ](https://cloud.google.com/storage/docs/how-to) for code samples that use the client library. 

##  April 05, 2019

**FEATURE:**

V4 signing process  BETA  launched.

  * The V4 signing process is an improved method for creating signed requests using RSA or HMAC signatures. 
  * Use the process to [ create signed URLs ](https://cloud.google.com/storage/docs/access-control/signing-urls-manually) . 

##  March 11, 2019

**FEATURE:**

Zürich region ( ` europe-west6 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  March 01, 2019

**CHANGED:**

Price reduction for storing Coldline Storage data in regional locations.

  * Data storage rate is now [ as low as $0.004/GB/month ](https://cloud.google.com/storage/pricing#storage-pricing) . 

##  February 15, 2019

**FEATURE:**

Bucket Policy Only  BETA  launched.

  * [ Bucket Policy Only ](https://cloud.google.com/storage/docs/bucket-policy-only) unifies your access controls by [ disabling object-level ACLs ](https://cloud.google.com/storage/docs/using-bucket-policy-only#enable) . 
  * You can [ set an organizational policy ](https://cloud.google.com/storage/docs/setting-org-policies#bucket-policy) that helps to enforce the use of Bucket Policy Only in your buckets. 

##  February 13, 2019

**CHANGED:**

The C++ Cloud Storage Client Library is now in BETA.

  * See the [ list of Cloud Storage guides ](https://cloud.google.com/storage/docs/how-to) for code samples that use the client library. 

##  January 24, 2019

**FIXED:**

Bucket updates - such as editing lifecycle policies, adding bucket labels, or
enabling bucket features - no longer require the updater to have the `
storage.buckets.setIamPolicy ` permission.

##  December 20, 2018

**CHANGED:**

[ Customer-Managed Encryption Keys
](https://cloud.google.com/storage/docs/encryption/customer-managed-keys) can
now be used with data stored in the ` eur4 ` and ` nam4 ` bucket locations.

##  October 22, 2018

**FEATURE:**

Hong Kong region ( ` asia-east2 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

**CHANGED:**

[ Limit ](https://cloud.google.com/storage/quotas) change for [ object
composition ](https://cloud.google.com/storage/docs/composite-objects) .

  * There is no longer a limit to the rate at which objects can be composed. 

##  October 19, 2018

**FEATURE:**

Retention policies and object holds are now available.

  * [ Retention policies ](https://cloud.google.com/storage/docs/bucket-lock) allow you to [ set a minimum age ](https://cloud.google.com/storage/docs/using-bucket-lock#set-policy) that objects must reach before they can be deleted or overwritten. 
  * You can [ lock your policy ](https://cloud.google.com/storage/docs/using-bucket-lock#lock-bucket) so that it can not be removed or reduced. 
  * You can [ place holds on your objects ](https://cloud.google.com/storage/docs/holding-objects) as another way to prevent unintended deletion or overwrite. 

##  October 11, 2018

**FEATURE:**

[ Dual-regions ](https://cloud.google.com/storage/docs/locations#location-dr)
BETA  launched.

  * Data stored in a dual-regional location have copies stored in two specific locations. 

**CHANGED:**

Geo-redundancy expanded in multi-regional locations.

  * All data stored in [ multi-regional locations ](https://cloud.google.com/storage/docs/locations#location-mr) are now [ geo-redundant ](https://cloud.google.com/storage/docs/key-terms#geo-redundant) , regardless of storage class. 

##  October 09, 2018

**FEATURE:**

[ C++ Cloud Storage Client Library
](https://cloud.google.com/storage/docs/reference/libraries) ALPHA

  * See the [ list of Cloud Storage guides ](https://cloud.google.com/storage/docs/how-to) for code samples that use the client library. 

##  August 15, 2018

**CHANGED:**

[ Cloud Key Management Service keys with Cloud Storage
](https://cloud.google.com/storage/docs/encryption/customer-managed-keys) is
now in GA.

##  July 18, 2018

**CHANGED:**

Improved security in the Google Cloud Platform Console.

  * Objects can no longer be made public through one-click actions. See [ Making data public ](https://cloud.google.com/storage/docs/access-control/making-data-public) for updated guides. 
  * [ Public access columns ](https://cloud.google.com/storage/docs/cloud-console#_publicaccess) for buckets and objects show you when the general public has access to your resources. 

##  July 10, 2018

**FEATURE:**

Los Angeles region ( ` us-west2 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  June 21, 2018

**CHANGED:**

[ Limit ](https://cloud.google.com/storage/quotas) changes for [ object
composition ](https://cloud.google.com/storage/docs/composite-objects) .

  * There is no longer a limit to the number of components in a composite object. 
  * The composition rate is now measured by the number of source objects, instead of the number of components within those source objects. 
  * Copying a composite object is no longer considered when determining a project's composition rate. 

##  June 11, 2018

**FEATURE:**

Finland region ( ` europe-north1 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  May 29, 2018

**CHANGED:**

New query parameter in JSON API object listing.

  * The optional query parameter ` includeTrailingDelimiter ` can now be used in your [ JSON API object listing requests ](https://cloud.google.com/storage/docs/json_api/v1/objects/list) . 

##  May 07, 2018

**FEATURE:**

Customer-Managed Encryption Keys  BETA  .

  * [ Cloud Key Management Service keys with Cloud Storage ](https://cloud.google.com/storage/docs/encryption/customer-managed-keys) allow you to manage the encryption keys used on your Cloud Storage objects. 
  * Google Cloud Platform Console functionality for the feature is fully available starting April 20. 

##  February 07, 2018

**CHANGED:**

Changed endpoint for batch requests to the JSON API.

  * When making [ HTTP batch requests ](https://cloud.google.com/storage/docs/json_api/v1/how-tos/batch) to the JSON API, users should utilize the ` www.googleapis.com/batch/storage/v1 ` endpoint instead of the ` www.googleapis.com/batch ` endpoint. 

##  February 01, 2018

**CHANGED:**

Price reduction for Nearline Storage and Coldline Storage in select regions.

  * Nearline Storage price reductions apply to the following regions: Northern Virginia, London, and Frankfurt. 
  * Coldline Storage price reductions apply to the following regions: London, Frankfurt, Mumbai, and Sydney. 
  * Details regarding Cloud Storage pricing can be found on the [ Pricing page ](https://cloud.google.com/storage/pricing) . 

##  January 10, 2018

**FEATURE:**

Montréal region ( ` northamerica-northeast1 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

**FEATURE:**

Netherlands region ( ` europe-west4 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  January 04, 2018

**CHANGED:**

The [ Cloud Pub/Sub Notifications for Cloud Storage
](https://cloud.google.com/storage/docs/pubsub-notifications) feature can now
have up to 10 different notification configurations send notifications for the
same event.

##  November 14, 2017

**FEATURE:**

[ Requester Pays ](https://cloud.google.com/storage/docs/requester-pays)
feature is now available.

  * When [ enabled on a bucket ](https://cloud.google.com/storage/docs/using-requester-pays#enable) , users accessing the bucket or its contents must specify a project to bill for charges that arise from their request. 
  * Callers can [ specify a billing project ](https://cloud.google.com/storage/docs/using-requester-pays#using) on requests to buckets both with and without Requester Pays enabled. 

**CHANGED:**

The [ Cloud Pub/Sub Notifications for Cloud Storage
](https://cloud.google.com/storage/docs/pubsub-notifications) feature is now
in GA.

**DEPRECATED:**

The **resource** attribute of [ Cloud Pub/Sub Notifications for Cloud Storage
](https://cloud.google.com/storage/docs/pubsub-notifications) is now
deprecated. It does not appear for new subscriptions and will not appear in
any subscription after June 1, 2018.

##  October 31, 2017

**FEATURE:**

Mumbai region ( ` asia-south1 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  September 18, 2017

**ISSUE:**

Bucket metadata ` PATCH ` requests to the JSON API require the `
storage.buckets.setIamPolicy ` permission if the requester has `
storage.buckets.getIamPolicy ` permission. This is true even for patches that
_do not change_ ACLs or IAM permissions.

See [ IAM permissions for JSON ](https://cloud.google.com/storage/docs/access-
control/iam-json) and [ IAM permissions for gsutil
](https://cloud.google.com/storage/docs/access-control/iam-gsutil) for
affected methods and commands.

##  September 05, 2017

**FEATURE:**

São Paulo region ( ` southamerica-east1 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  August 14, 2017

**CHANGED:**

You can now [ control Object Lifecycle Management
](https://cloud.google.com/storage/docs/managing-lifecycles) from the [
Storage Console ](https://console.cloud.google.com/storage/browser) .

##  August 01, 2017

**FEATURE:**

Frankfurt region ( ` europe-west3 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  June 20, 2017

**FEATURE:**

Sydney region ( ` australia-southeast1 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  June 06, 2017

**FEATURE:**

New public dataset stored in Cloud Storage.

  * Data for [ NEXRAD ](https://cloud.google.com/storage/docs/public-datasets/nexrad) are now hosted publicly in Cloud Storage. 

**FEATURE:**

London region ( ` europe-west2 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  May 31, 2017

**CHANGED:**

[ Identity and Access Management (IAM)
](https://cloud.google.com/storage/docs/access-control/iam) policies are now
GA for buckets. Policies applied at the bucket level can be used to control
access to individual buckets as well as all the objects within them.

##  May 24, 2017

**CHANGED:**

Attempts to access a non-existent object returns a 403 error instead of a 404
error if the requester lacks object listing permission for the associated
bucket.

##  May 09, 2017

**FEATURE:**

Northern Virginia region ( ` us-east4 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  April 26, 2017

**CHANGED:**

The [ Cloud Storage Client Libraries
](https://cloud.google.com/storage/docs/reference/libraries) for the Cloud
Storage API is now in GA.

##  April 11, 2017

**FEATURE:**

Singapore region ( ` asia-southeast1 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  April 06, 2017

**FEATURE:**

[ Labels ](https://cloud.google.com/storage/docs/key-terms#bucket-labels) can
now be [ used with your buckets ](https://cloud.google.com/storage/docs/using-
bucket-labels) in order to better organize all of your Google Cloud Platform
resources.

##  March 27, 2017

**FEATURE:**

Cloud Pub/Sub Notifications for Cloud Storage  BETA

  * [ Track changes ](https://cloud.google.com/storage/docs/reporting-changes) to objects in your buckets through notifications sent to Cloud Pub/Sub. 
  * You can set the [ event types ](https://cloud.google.com/storage/docs/pubsub-notifications#events) that generate notifications as well as the [ information contained within notifications ](https://cloud.google.com/storage/docs/pubsub-notifications#format) . 

##  December 07, 2016

**CHANGED:**

The [ per-object storage class ](https://cloud.google.com/storage/docs/per-
object-storage-class) feature is now in GA.

##  November 07, 2016

**FEATURE:**

` asia-northeast1 ` region launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  October 20, 2016

**FEATURE:**

Coldline, a new [ archival storage class
](https://cloud.google.com/storage/archival/) , is now available.

  * The [ Coldline Storage class ](https://cloud.google.com/storage/docs/storage-classes#coldline) provides low price, immediately accessible data storage for your backup, archival and disaster recovery needs. 
  * Ideal for data that intends to be accessed less than once a year. 

**CHANGED:**

Standard Storage class is now Multi-Regional Storage and Regional Storage.

  * The [ Multi-Regional Storage class ](https://cloud.google.com/storage/docs/storage-classes#multi-regional) provides the same price and performance along with geo-redundant copies of your data and a 99.95% availability SLA. 
  * The [ Regional Storage class ](https://cloud.google.com/storage/docs/storage-classes#regional) provides the same performance at a reduced price. 

**FEATURE:**

Per-object storage classes  BETA

  * Users can [ set the storage class at the object level ](https://cloud.google.com/storage/docs/per-object-storage-class) . 
  * Users can configure [ lifecycle management ](https://cloud.google.com/storage/docs/lifecycle) to automatically change the storage class of an object when designated criteria are met. 

##  October 04, 2016

**FEATURE:**

Public datasets stored in Cloud Storage

  * Datasets for the Landsat and Sentinel-2 missions are now hosted publicly in Cloud Storage. 
  * [ Read about the Landsat dataset ](https://cloud.google.com/storage/docs/public-datasets/landsat)
  * [ Read about the Sentinel-2 dataset ](https://cloud.google.com/storage/docs/public-datasets/sentinel-2)

##  September 26, 2016

**FEATURE:**

Alpha release for bucket-level IAM.

  * _Access to this feature is currently by[ request/invite ](https://docs.google.com/a/google.com/forms/d/e/1FAIpQLSeZkzvcpwwXZhffC9-N9YHXsWQxnMETSSMmhASukCvD0JwI_g/viewform) only. _ [ Apply IAM permissions to individual buckets ](https://cloud.google.com/storage/docs/access-control/iam) in your projects. 

##  August 29, 2016

**CHANGED:**

Improved upload experience in the [ Storage Console
](https://console.cloud.google.com/storage/browser) .

  * Users can retry failed uploads. 
  * The upload drawer persists when navigating to other parts of the Storage Console. 
  * Users are immediately notified when an upload starts and ends. 

##  August 03, 2016

**CHANGED:**

Nearline latency times reduced.

  * Buckets created in the [ Nearline storage class ](https://cloud.google.com/storage/docs/storage-classes#nearline) now have the same sub-second latency as other storage class buckets. 

##  August 01, 2016

**CHANGED:**

Object generation numbers no longer have ordering guarantees.

  * [ Generation numbers ](https://cloud.google.com/storage/docs/generations-preconditions) associated with Cloud Storage objects no longer increase monotonically or have ordering guarantees between generations. 
  * Generation numbers continue to be unique resource identifiers. 
  * [ See the announcement ](https://groups.google.com/forum/#!msg/gs-announce/XdSq25nsHio/-GuZxzyOAwAJ) . 

##  July 20, 2016

**FEATURE:**

` us-west1 ` region launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

##  June 24, 2016

**FEATURE:**

` X-Goog-Content-Length-Range ` custom header available.

  * New header for [ XML ](https://cloud.google.com/storage/docs/xml-api/reference-headers#xgoogcontentlengthrange) and [ JSON ](https://cloud.google.com/storage/docs/json_api/v1/parameters#xgoogcontentlengthrange) . 
  * Allows for checking the size of content sent to Cloud Storage. 

##  June 13, 2016

**CHANGED:**

On-Demand I/O for Nearline-class buckets no longer necessary.

  * Buckets created in the [ Nearline storage class ](https://cloud.google.com/storage/docs/storage-classes#nearline) now have throughput and QPS that automatically scale with your needs, at no extra cost. 

