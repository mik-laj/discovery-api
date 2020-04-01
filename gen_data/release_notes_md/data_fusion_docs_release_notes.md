#  Release notes

This page documents production updates to Cloud Data Fusion. Check this page
for announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/clouddatafusion-release-
notes.xml `

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

