#  Release Notes

This page documents production updates to Web Security Scanner. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/websecurityscanner-release-
notes.xml `

##  August 05, 2019

**FEATURE:**

API updated to v1.

**CHANGED:**

findingType string XSS_CALLBACK changed to XSS.

##  March 26, 2019

**FEATURE:**

API updated to v1beta.

**CHANGED:**

findingType field changed to string value

The findingType field has changed from an enum to a string in the Beta release
of the Web Security Scanner API. You can find details in the [ Scan Result
Details ](https://cloud.google.com/security-scanner/docs/scan-result-details)
topic.

**ISSUE:**

Web Security Scanner does not yet support applications protected by Cloud
Identity-Aware Proxy (Cloud IAP).

