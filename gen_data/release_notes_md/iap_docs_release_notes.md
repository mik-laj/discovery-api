#  Release Notes

This page documents production updates to IAP. You can periodically check this
page for announcements about new or updated features, bug fixes, known issues,
and deprecated functionality.

**Current version: release**

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/iap-release-notes.xml `

##  May 29, 2020

**FEATURE:**

The ability to authenticate users with [ external identities
](https://cloud.google.com/iap/docs/enable-external-identities) is now
generally available.

##  February 12, 2020

**FEATURE:**

API for OAuth clients now generally available

You can now programmatically create OAuth clients in IAP via REST or gcloud.
See [ this topic ](https://cloud.google.com/iap/docs/programmatic-oauth-
clients) for more information.

##  August 07, 2019

**FEATURE:**

Cloud IAP TCP forwarding general availability release

Using [ Cloud IAP for TCP forwarding ](https://cloud.google.com/iap/docs/tcp-
forwarding-overview) is now generally available. Cloud IAP for TCP forwarding
lets you control who can access administrative services like SSH and RDP on
your backends.

##  April 10, 2019

**FEATURE:**

Cloud IAP with context-aware access general availability release

The ability to extend Cloud IAP access policies with [ access levels
](https://cloud.google.com/access-context-manager/docs/) and the [ IAM
Conditions Framework ](https://cloud.google.com/iam/docs/conditions-overview)
is now generally available.

##  February 26, 2019

**FEATURE:**

Cloud IAP for on-premises apps general availability release

You can now [ manage access to HTTP-based apps outside of Google Cloud
Platform ](https://cloud.google.com/iap/docs/cloud-iap-for-on-prem-apps-
overview) . This includes apps on-premises in your enterprise's data centers
and on other cloud providers.

##  February 14, 2019

**FEATURE:**

Cloud IAP Per-Resource Policies general availability release

The ability to [ manage Cloud IAP policies
](https://cloud.google.com/iap/docs/managing-access) for each individual
resource in a Google Cloud Platform project is now generally available.

##  January 22, 2019

**FEATURE:**

Cloud IAP TCP forwarding beta release

You can now use [ Cloud IAP for TCP forwarding
](https://cloud.google.com/iap/docs/tcp-forwarding-overview) , allowing you to
control who can access administrative services like SSH and RDP on your
backends.

##  October 04, 2018

**FEATURE:**

Cloud IAP with context-aware access beta release

Cloud IAP access policies for Cloud IAP-secured applications, services, and
versions have been extended to use [ access levels
](https://cloud.google.com/access-context-manager/docs/) and the [ IAM
Conditions Framework ](https://cloud.google.com/iam/docs/conditions-overview)
. Access levels allow access restrictions to resources based on IP address and
end-user device attributes. IAM conditions allow access restrictions based on
URL hosts, paths, date, and time.

##  August 16, 2018

**FEATURE:**

Cloud IAP Per-Resource Policies beta release

Cloud IAP policies can now be [ managed
](https://cloud.google.com/iap/docs/managing-access) for each individual
resource in a GCP project.

##  August 31, 2017

**FEATURE:**

Welcome to the Cloud IAP general release for App Engine standard environment,
Compute Engine, and GKE!

**ISSUE:**

Cloud IAP for App Engine flexible environment is still in [ beta
](https://cloud.google.com/terms/launch-stages) . This feature is not covered
by any SLA or deprecation policy and may be subject to backward-incompatible
changes for App Engine flexible environment.

**CHANGED:**

Java code samples were updated with security enhancements on August 15, 2017.
If you're using the Java [ signed headers
](https://cloud.google.com/iap/docs/signed-headers-howto) code sample, please
update your application per the current samples.

**CHANGED:**

When you use the programmatic authentication feature, the aud claim in the JWT
must now be the Cloud IAP client ID. Previously, it could also be the
application URL. For applications that used programmatic authentication
recently, we placed this feature on our whitelist. We will remove the
functionality on November 15, 2017. For details and updated code samples,
refer to [ programmatic authentication
](https://cloud.google.com/iap/docs/authentication-howto) .

**CHANGED:**

Due to internal security enhancements, App Engine standard environment apps no
longer require ` login: required ` in ` app.yaml ` (or ` security-constraint `
for Java).

**FEATURE:**

[ Forseti Security ](http://forsetisecurity.org/) is now available and
strongly encouraged for Compute Engine apps. If you have any questions or
require assistance, please post to discuss@forsetisecurity.org.

**FEATURE:**

Cloud IAP now supports Cloud Audit Logging. Learn about [ enabling Cloud Audit
Logging ](https://cloud.google.com/iap/docs/audit-log-howto) .

**FEATURE:**

Cloud IAP now supports desktop and command-line applications. Learn about [
authenticating from a desktop app
](https://cloud.google.com/iap/docs/authentication-
howto#authenticating_from_a_desktop_app) .

**FEATURE:**

AJAX requests with missing or expired credentials will now get an HTTP 401
response instead of being served a Google login page.

##  August 07, 2017

**FIXED:**

Cloud IAP can once again be enabled for App Engine flexible environment apps.

##  July 20, 2017

**FEATURE:**

Cloud IAP now supports [ special URLs
](https://cloud.google.com/iap/docs/special-urls-howto) to help you enhance
and personalize your app.

##  July 14, 2017

**CHANGED:**

Cloud IAP now uses the following values when you secure your app with signed
headers:

  * The JWT is now in the HTTP request header ` x-goog-iap-jwt-assertion ` instead of ` x-goog-authenticated-user-jwt ` . 
  * When you [ verify the ID token payload ](https://cloud.google.com/iap/docs/signed-headers-howto#verify_the_id_token_payload) , the ` aud ` value should now be a string with client ID details instead of a URL. 

##  July 11, 2017

**FEATURE:**

Added [ best practices for caching
](https://cloud.google.com/iap/docs/concepts-best-practices) .

##  June 19, 2017

**FEATURE:**

Cloud Audit Logging is now available for Cloud IAP-secured resources. Read
about how to [ Enable Cloud Audit Logging
](https://cloud.google.com/iap/docs/audit-log-howto) .

**CHANGED:**

The Cloud IAP 403 "failed access" page now includes product and email details
from the OAuth consent screen. As with the login page, these details are
publicly visible to anyone who accesses your URL. You can change the
information that displays on the [ OAuth consent screen
](https://console.cloud.google.com/apis/credentials/consent?_ga=2.250325059.-492396546.1528399541)
.

##  June 07, 2017

**FEATURE:**

Added information about [ Authenticating from a desktop app
](https://cloud.google.com/iap/docs/authentication-
howto#authenticating_from_a_desktop_app) for Cloud IAP-secured resources.

##  April 17, 2017

**CHANGED:**

When you use Cloud IAP with Compute Engine, GKE, or the App Engine flexible
environment, you must also use [ signed headers
](https://cloud.google.com/iap/docs/signed-headers-howto) to secure your app.

**ISSUE:**

Cloud IAP can't currently be enabled for App Engine flexible environment apps.

##  March 09, 2017

**ISSUE:**

Cloud IAP has a static 403 "failed access" page. In a future release, admins
will be able to customize the failure message text.

