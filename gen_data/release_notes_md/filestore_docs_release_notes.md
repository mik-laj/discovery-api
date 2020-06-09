#  Release notes

This page documents production updates to Filestore. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/filestore-release-notes.xml `

##  June 08, 2020

**FEATURE:**

[ **High Scale SSD** ](https://cloud.google.com/filestore/docs/high-scale)
tier released to beta. This new service tier for Filestore provides greater
performance and allows you to grow and shrink capacity between 60-320 TB.

**FEATURE:**

[ **IP-based access control**
](https://cloud.google.com/filestore/docs/creating-instances#configuring_ip-
based_access_control) released to beta. This feature allows you to control
access to file shares by the IP addresses of clients.

**CHANGED:**

Filestore service tier name change:

  * **Standard** tier is now called **Basic HDD** . 
  * **Premium** tier is now called **Basic SSD** . 
  * You can still use the old tier names and they will continue to be supported. 

This change may affect you if you use:  
* The ` gcloud beta filestore ` command line tool (beta). * The Filestore beta API (v1beta1). * The Cloud Console in combination with the Filestore API. * The Cloud Console in combination with the ` gcloud ` tool. 

For details, see [ New service tier names
](https://cloud.google.com/filestore/docs/high-scale#new_service_tier_names) .

**FEATURE:**

Filestore is available in the ` asia-southeast2 ` (Jakarta) region. See [
Regions and zones ](https://cloud.google.com/filestore/docs/regions) .

##  May 19, 2020

**FEATURE:**

Learn how to create [ low disk space alerts
](https://cloud.google.com/filestore/docs/monitoring-instances) for your
Filestore instances.

##  April 20, 2020

**FEATURE:**

Filestore is available in the ` us-west4 ` (Las Vegas) region. See [ Regions
and zones ](https://cloud.google.com/filestore/docs/regions) .

##  January 24, 2020

**FEATURE:**

Cloud Filestore is now available in the Seoul ( ` asia-northeast3 ` ) [ region
](https://cloud.google.com/filestore/docs/regions) .

##  April 08, 2019

**FEATURE:**

GA release of Cloud Filestore

  * Cloud Filestore is now generally available for use. 

##  July 12, 2018

**FEATURE:**

Beta release of Cloud Filestore

  * The Beta version of Cloud Filestore is now available for use. 

