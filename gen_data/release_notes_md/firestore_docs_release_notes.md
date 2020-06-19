#  Release notes

This page documents production updates to Firestore. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/fs-release-notes.xml `

##  June 08, 2020

**FEATURE:**

Support for the [ ` asia-southeast2 ` (Jakarta)
](https://cloud.google.com/firestore/docs/locations) .

##  April 20, 2020

**FEATURE:**

Support for [ ` us-west4 ` region (Las Vegas)
](https://cloud.google.com/firestore/docs/locations) .

##  March 11, 2020

**FEATURE:**

Support for [ ` us-west3 ` (Salt Lake City) and ` asia-northeast3 ` (Seoul)
](https://cloud.google.com/firestore/docs/locations) .

##  November 07, 2019

**FEATURE:**

Cloud Firestore now supports the [ ` in ` and ` array-contains-any ` query
operators ](https://cloud.google.com/firestore/docs/query-
data/queries#in_and_array-contains-any) .

##  July 08, 2019

**FEATURE:**

Added the **Active Connections** and **Snapshot Listeners** [ Cloud Firestore
metrics ](https://cloud.google.com/firestore/docs/monitor-usage#stackdriver-
monitoring) to Stackdriver Monitoring. To learn more about using these metrics
to set up dashboards and alerts, see [ Monitoring usage
](https://cloud.google.com/firestore/docs/monitor-usage) .

##  May 07, 2019

**FEATURE:**

Cloud Firestore now supports [ collection group queries
](https://cloud.google.com/firestore/docs/query-data/queries#collection-group-
query) . A collection group consists of all collections with the same ID. By
default, queries retrieve results from a single collection in your database.
Use a collection group query to retrieve documents from a collection group
instead of from a single collection.

##  April 18, 2019

**FEATURE:**

Support for [ ` asia-northeast2 ` region (Osaka)
](https://cloud.google.com/firestore/docs/locations) .

##  April 15, 2019

**FEATURE:**

Support for [ ` europe-west6 ` region (Zürich)
](https://cloud.google.com/firestore/docs/locations) .

##  March 28, 2019

**FEATURE:**

You can now [ use the increment operation
](https://cloud.google.com/firestore/docs/manage-data/add-
data#increment_a_numeric_value) to increase or decrease the current value of a
numeric field by a given amount. For more on this feature, see our [
announcement ](https://firebase.googleblog.com/2019/03/increment-server-side-
cloud-firestore.html?linkId=65365800) .

##  January 31, 2019

**FEATURE:**

General Availability release of Cloud Firestore. The [ Cloud Firestore SLA
](https://cloud.google.com/firestore/sla) is now in effect, including 99.999%
availability for multi-region instances and 99.99% availability for regional
instances.

**FEATURE:**

Cloud Firestore now supports the following 10 additional locations:

  * Multi-region 

    * ` eur3 ` Europe 
  * North America (regional) 

    * ` us-west2 ` Los Angeles 
    * ` northamerica-northeast1 ` Montréal 
    * ` us-east4 ` Northern Virginia 
  * South America (regional) 

    * ` southamerica-east1 ` São Paulo 
  * Europe (regional) 

    * ` europe-west2 ` London 
  * Asia (regional) 

    * ` asia-south1 ` Mumbai 
    * ` asia-east2 ` Hong Kong 
    * ` asia-northeast1 ` Tokyo 
  * Australia (regional) 

    * ` australia-southeast1 ` Sydney 

For a full list of supported multi-regions and regions, see [ Cloud Firestore
Locations ](https://cloud.google.com/firestore/docs/locations) .

##  October 29, 2018

**FEATURE:**

We added a Cloud Firestore emulator you can use for local testing. To set up
the emulator, see [ Testing Cloud Firestore Security Rules
](https://cloud.google.com/firestore/docs/security/test-rules-emulator) .

##  August 09, 2018

**FEATURE:**

We added two new features to help you work with arrays:

  * [ Array contains queries ](https://cloud.google.com/firestore/docs/query-data/queries#array_membership) : query for documents that contain a particular array value. 
  * [ Array transforms ](https://cloud.google.com/firestore/docs/manage-data/add-data#update_elements_in_an_array) : the ` arrayUnion() ` and ` arrayRemove() ` functions allow you to directly modify array field values. 

##  August 08, 2018

**FEATURE:**

You can now create a [ Cloud Firestore database in Datastore mode
](https://cloud.google.com/firestore/docs/firestore-or-
datastore#choosing_a_database) . Datastore mode allows you to use Cloud
Datastore client libraries with an improved Cloud Firestore storage layer,
removing eventual consistency limitations.

**FEATURE:**

Cloud Firestore now supports the ` europe-west3 ` and ` us-east1 ` regions,
see [ Cloud Firestore Locations
](https://cloud.google.com/firestore/docs/locations) .

**FEATURE:**

You can now add [ single-field index exemptions
](https://cloud.google.com/firestore/docs/concepts/index-overview#exemptions)
to exempt specific fields from automatic indexing.

**FEATURE:**

You can now [ manage your Cloud Firestore instance from the Google Cloud
Platform console ](https://cloud.google.com/firestore/docs/using-console) .

**FEATURE:**

Added support for importing and exporting of documents, see [ Exporting and
Importing Data ](https://cloud.google.com/firestore/docs/manage-data/export-
import) .

##  June 13, 2018

**CHANGED:**

Added code examples for the [ Ruby server client library
](https://googleapis.dev/ruby/google-cloud-
firestore/v0.21.1/Google/Cloud/Firestore.html) .

##  May 16, 2018

**CHANGED:**

Documentation updates:

  * [ New page on Cloud Firestore indexes ](https://cloud.google.com/firestore/docs/concepts/index-overview) . This page describes Cloud Firestore index types, the relationship between queries and indexes, and index merging for equality filters. 
  * Added code examples for the [ C# server client library ](http://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Firestore/) . 

##  May 11, 2018

**CHANGED:**

We raised the [ Cloud Firestore Security Rules limits
](https://cloud.google.com/firestore/quotas#security_rules) for document
access calls.

##  April 03, 2018

**CHANGED:**

The Firebase SDK for Cloud Functions v1.0.0 is now available and introduces
some breaking changes, see the [ Cloud Firestore section of the Firebase SDK
for Cloud Functions Migration Guide
](https://firebase.google.com/docs/functions/beta-v1-diff#cloud-firestore) .

##  March 29, 2018

**FEATURE:**

Cloud Firestore Security Rules now support the [ ` getAfter() `
](https://cloud.google.com/firestore/docs/reference/security/#getafter)
function. Use this function to [ enforce data validation for atomic operations
](https://cloud.google.com/firestore/docs/manage-
data/transactions#data_validation_for_atomic_operations) .

##  February 23, 2018

**FEATURE:**

New documentation page on [ Cloud Firestore Security Rules and queries.
](https://cloud.google.com/firestore/docs/security/rules-query)

This page clarifies how Cloud Firestore Security Rules evaluate query
requests. Read this page to learn how to write queries that satisfy your
security rules and how to write security rules based on query properties like
` limit ` and ` orderby ` .

##  February 08, 2018

**FEATURE:**

New Cloud Firestore server client libraries:

  * [ C# ](http://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Firestore/)
  * [ PHP ](https://github.com/GoogleCloudPlatform/google-cloud-php#cloud-firestore-beta)
  * [ Ruby ](https://github.com/GoogleCloudPlatform/google-cloud-ruby/tree/master/google-cloud-firestore)

##  January 18, 2018

**CHANGED:**

Overhaul of the Cloud Firestore Security Rules documentation. These improved
pages add more examples and give a clearer introduction to the structure of
Cloud Firestore Security Rules:

  * [ Getting Started with Security Rules ](https://cloud.google.com/firestore/docs/security/get-started)
  * [ Structuring Security Rules ](https://cloud.google.com/firestore/docs/security/rules-structure)
  * [ Writing Conditions for Security Rules ](https://cloud.google.com/firestore/docs/security/rules-conditions)

##  January 10, 2018

**FEATURE:**

Cloud Firestore Security Rules now offer the ability to limit read or write
access to data based on query parameters. [ Learn more about query-based rules
](https://cloud.google.com/firestore/docs/reference/security/#query) .

##  October 03, 2017

**FEATURE:**

Beta release of Cloud Firestore.

