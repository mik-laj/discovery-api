#  Release notes

This page documents production updates to Data Catalog. Check this page for
announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/data-catalog-release-notes.xml
`

##  March 12, 2020

**FEATURE:**

[ Support for custom entries ](https://cloud.google.com/data-catalog/docs/how-
to/custom-entries) is now in beta. This feature lets you ingest metadata of
any type, so it can be tagged and searched in Data Catalog.

##  January 27, 2020

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

**CHANGED:**

IAM policies are no longer available for individual entries, but still are
available for tag templates and entry groups. With this change, users will not
be able to set ACLs for individual entries such as filesets, only for tag
templates and entry groups. Each fileset belongs to an entry group and an
entry group can contain multiple filesets or entries.

This change is relevant to users who have created filesets in Data Catalog.
Data Catalog users who do not have filesets are not impacted by this change.

##  June 27, 2019

**FEATURE:**

Announcing the [ Beta ](https://cloud.google.com/terms/launch-stages#launch-
stages) release of [ Data Catalog ](https://cloud.google.com/data-
catalog/docs/) , a fully managed and scalable metadata management service that
allows organizations to quickly discover, manage, and understand their data in
Google Cloud.

Send feedback

