#  Release Notes

This page details updates to Service Usage. You can periodically check this
page for announcements about new or updated features, bug fixes, known issues,
and deprecated functionality.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/service-usage-release-notes.xml
`

##  June 2018

**FEATURE:** **Public v1 release:** Service Usage is now generally available.
You can use version 1 of Service Usage to discover and manage other APIs and
services in your Google Cloud project.

**CHANGED:** The default behavior of the [ ` services.disable ` ](/service-
usage/docs/reference/rest/v1/services/disable) method now generates an error
if any currently enabled services depend on the service you are trying to
disable. If you set the ` disableDependentServices ` field to true, any
enabled services that depend on the service you are disabling, are also
disabled.

##  March 2018

**FEATURE:** When you call the [ ` services.list ` ](/service-
usage/docs/reference/rest/v1beta1/services/list) method, you can now filter
for disabled APIs and services.

##  February 2018

**FEATURE:** **Public beta release:** Service Usage is an infrastructure
service of Google Cloud that lets you discover and manage other APIs and
services in your Cloud project.

