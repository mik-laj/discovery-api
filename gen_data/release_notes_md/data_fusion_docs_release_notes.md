#  Release notes

This page documents production updates to Cloud Data Fusion. Check this page
for announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/clouddatafusion-release-
notes.xml `

##  July 16, 2020

**FEATURE:**

Cloud Data Fusion version 6.1.3 is now available. This version includes
performance improvements and minor bug fixes.

  * Improved performance of Joiner plugins, aggregators, program startup, and previews. 
  * Added support for custom images. You can select a custom Dataproc image by specifying the image URI. 
  * Added support for rendering large schemas (>1000 fields) in the pipelines UI. 
  * Added payload compression support to the messaging service. 

##  April 22, 2020

**FEATURE:**

Cloud Data Fusion version 6.1.2 is now available. This version includes
several stability and performance improvements and new features.

  * Added support for [ Field Level Lineage ](https://cloud.google.com/data-fusion/docs/tutorials/lineage) for Spark plugins and Streaming pipelines 
  * Added support for Spark 2.4 
  * Added an option to skip header in the files in delimited, CSV, TSV, and text formats 
  * Added an option for database source to replace the characters in the field names 

**FIXED:**

Reduced preview startup by 60%. Also added limit to max concurrent preview
runs (10 by default).

**FIXED:**

Fixed a bug that caused errors when Wrangler's parse-as-csv with header was
used when reading multiple small files.

**FIXED:**

Fixed a bug that caused zombie processes when using the Remote Hadoop
Provisioner.

**FIXED:**

Fixed a bug that caused DBSource plugin to fail in preview mode.

**FIXED:**

Fixed a race condition that caused a failure when running a Spark program.

##  January 10, 2020

**FEATURE:**

Cloud Data Fusion version 6.1.1 is now available. This version includes
several stability and performance improvements, as well as these new features:

  * Azure Data Lake storage support in Wrangler 
  * Enabled Field Level Lineage (Beta) 
  * Data Loss Prevention plugin to identify, tokenize, or encrypt sensitive data at scale (Beta) 

##  December 10, 2019

**FEATURE:**

Cloud Data Fusion version 6.1.0.5 is now available. This version includes
several stability and performance improvements.

##  November 21, 2019

**FEATURE:**

Cloud Data Fusion is now generally available.

**FEATURE:**

Added support for creating Cloud Data Fusion instances that use [ private IP
](https://cloud.google.com/data-fusion/docs/how-to/create-private-ip)
addresses.

**FEATURE:**

Added support for creating private Cloud Data Fusion instances and executing
data pipelines in a VPC-SC environment.

**FEATURE:**

Added support to encrypt resources created in Cloud Storage, BigQuery, and
Pub/Sub using Cloud Data Fusion with Customer Managed Encryption Keys.

**FEATURE:**

Added [ reference documentation ](https://cloud.google.com/data-
fusion/docs/reference/cdap-reference) for creating and managing pipelines and
datasets.

**CHANGED:**

The Cloud Data Fusion UI is now available at a different URL in the format: `
<instance-name>-<project-id>-dot-<region
identifier>.datafusion.googleusercontent.com ` .

##  May 31, 2019

**CHANGED:**

Renamed "Cloud Dataprep service" to "Wrangler service" in the **System Admin**
page of the Cloud Data Fusion UI.

**CHANGED:**

Added a version number field to the Cloud Data Fusion **Instance details**
page in the GCP Console.

**FIXED:**

Fixed a bug that caused Cloud Data Fusion to launch Cloud Dataproc clusters in
an incorrect project.

**FIXED:**

Added support for specifying a subnet for the Cloud Dataproc provisioner.

**FIXED:**

Fixed the Cloud Dataproc provisioner to handle networks that do not use
automatic subnet creation.

##  April 10, 2019

**FEATURE:**

Cloud Data Fusion is now publicly available in beta.

