#  Release notes

This page documents production updates to Data Catalog. Check this page for
announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/data-catalog-release-notes.xml
`

##  July 24, 2020

v1

**FEATURE:**

Data Catalog is now available in Seoul ( ` asia-northeast3 ` ).

##  July 20, 2020

v1

**FEATURE:**

Data Catalog is now available in Salt Lake City ( ` us-west3 ` ) and Las Vegas
( ` us-west4 ` ).

##  April 30, 2020

v1

**FEATURE:**

Data Catalog is now generally available (GA). \- The Data Catalog v1 API,
gcloud commands, and UI are now available. For details, [ see the API
reference ](https://cloud.google.com/data-catalog/docs/reference) . Code
samples throughout the documentation have been updated to use the new API. \-
Data Catalog has been regionalized, and now hosts user metadata in [ 23
regions worldwide ](https://cloud.google.com/data-
catalog/docs/concepts/regions) . \- Billing has been enabled for Data Catalog
API calls and storage using all supported resources. For more info, see the [
pricing page ](https://cloud.google.com/data-catalog/pricing) .

##  March 12, 2020

v1beta1

**FEATURE:**

[ Support for custom entries ](https://cloud.google.com/data-catalog/docs/how-
to/custom-entries) is now in beta. This feature lets you ingest metadata of
any type, so it can be tagged and searched in Data Catalog.

##  January 27, 2020

v1beta1

**FEATURE:**

Data Catalog users, when creating a tag template, can now specify an attribute
as [ required ](https://cloud.google.com/data-
catalog/docs/reference/rest/v1beta1/projects.locations.tagTemplates.fields#TagTemplateField.SCHEMA_REPRESENTATION)
( [ Beta ](https://cloud.google.com/terms/launch-stages#launch-stages)
release). A tag cannot be created unless all the required attributes are
populated with valid values. For an example, see [ Create a tag template and
attach the tag to your table ](https://cloud.google.com/data-
catalog/docs/quickstarts/quickstart-search-
tag#create_a_tag_template_and_attach_tags_to_your_table) .

##  January 21, 2020

v1beta1

**CHANGED:**

IAM policies are no longer available for individual entries, but still are
available for tag templates and entry groups. With this change, users will not
be able to set ACLs for individual entries such as filesets, only for tag
templates and entry groups. Each fileset belongs to an entry group and an
entry group can contain multiple filesets or entries.

This change is relevant to users who have created filesets in Data Catalog.
Data Catalog users who do not have filesets are not impacted by this change.

##  June 27, 2019

v1beta1

**FEATURE:**

Announcing the [ Beta ](https://cloud.google.com/terms/launch-stages#launch-
stages) release of [ Data Catalog ](https://cloud.google.com/data-
catalog/docs/) , a fully managed and scalable metadata management service that
allows organizations to quickly discover, manage, and understand their data in
Google Cloud.

