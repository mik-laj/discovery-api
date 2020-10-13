#  Release notes

This page documents production updates to Managed Service for Microsoft Active
Directory. Check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/managedmicrosoftad-release-
notes.xml `

##  July 09, 2020

**FEATURE:**

The [ Managed Microsoft AD SLA ](https://cloud.google.com/managed-microsoft-
ad/sla) has been published.

##  March 23, 2020

**CHANGED:**

**GA pricing now in effect**

New pricing for Managed Microsoft AD is now in effect. Learn more about
standard [ Managed AD pricing ](https://cloud.google.com/managed-microsoft-
ad/pricing) and view [ pricing examples ](https://cloud.google.com/managed-
microsoft-ad/pricing#pricing_examples) .

##  March 10, 2020

**FEATURE:**

[ VPC Service Controls ](https://cloud.google.com/vpc-service-
controls/docs/overview) integration is now in [ beta
](https://cloud.google.com/products/#product-launch-stages) .

Learn more about [ configuring VPC Service Controls
](https://cloud.google.com/managed-microsoft-ad/docs/how-to-use-vpc-service-
controls) for Managed Microsoft AD to provide additional security.

##  February 20, 2020

**FEATURE:**

Managed Service for Microsoft AD General Availability

  * Added support for deploying domain controllers from the following regions: 

    * asia-east2 
    * asia-northeast1 
    * asia-northeast2 
    * asia-south1 
    * australia-southeast1 
    * europe-west2 
    * europe-west3 
    * europe-west6 
    * northamerica-northeast1 
    * southamerica-east1 

Learn about the [ full list of supported regions
](https://cloud.google.com/managed-microsoft-ad/docs/add-remove-
regions#regions) .

  * AD-dependent VMs and apps can use multi-regional VPCs to reach domain controllers in any region, regardless of their relative locations. 

  * Domain controllers from the same AD domain can be deployed in up to 4 regions, at domain creation or later. 

  * The [ Domain Functional Level ](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels) (DFL) of all new Managed AD domains is Windows Server 2012 R2. Domains created during the Managed AD Beta may have an earlier DFL. Learn [ how to check your DFL ](https://www.technipages.com/active-directory-how-to-check-domain-and-forest-functional-level) . 

**ISSUE:**

Trust status is stale

When the trust between a Managed Microsoft AD domain and an on-premises Active
Directory domain is broken, the status in the Cloud Console may not be
correctly updated.

To validate the status of a trust, [ go to the Managed Microsoft AD page
](https://console.cloud.google.com/security/cloud-ad) in the Cloud Console and
then select the domain. On the **Domain** page, in the **Trust relationships**
table, select **Validate Trust** . Learn more about [ getting domain info
](https://cloud.google.com/managed-microsoft-ad/docs/list-describe-delete-
domains#getting_domain_info) .

##  August 21, 2019

**FEATURE:**

Managed Microsoft AD is now in beta!

