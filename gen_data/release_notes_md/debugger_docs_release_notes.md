#  Release Notes

This page documents production updates to Debugger. You can periodically check
this page for announcements about new or updated features, bug fixes, known
issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/stackdriver-release-notes.xml `

##  June 17, 2020

**FEATURE:**

Cloud Debugger now lets you canary snapshots and logpoints on your Python
applications. To learn more, see the [ Python page for setting up Cloud
Debugger ](https://cloud.google.com/debugger/docs/setup/python) .

##  May 19, 2020

**FEATURE:**

Cloud Debugger now lets you canary snapshots and logpoints on your Java
applications. To learn more, see the [ Java page for setting up Cloud Debugger
](https://cloud.google.com/debugger/docs/setup/java) .

##  November 12, 2019

**FEATURE:**

[ Stackdriver Debugger ](https://cloud.google.com/debugger/docs) has an
updated and expanded quickstart guide showing how to install the agent and
debug an app while it's in production. See the [ Debugger Quickstart guide
](https://cloud.google.com/debugger/docs/quickstart) for more information.

##  July 31, 2019

**FEATURE:**

**Cloud Run** and **Cloud Run on GKE** : Stackdriver Debugger can now be used
to debug applications on Cloud Run and Cloud Run on GKE that are written in [
Node.js ](https://cloud.google.com/debugger/docs/setup/nodejs) , [ Python
](https://cloud.google.com/debugger/docs/setup/python) , and [ Java
](https://cloud.google.com/debugger/docs/setup/java) .

##  November 03, 2017

**CHANGED:**

**Compute Engine (Go)** : The support for Go applications on Compute Engine VM
instances is in Beta release. Your Go applications should be compiled without
the default optimizations, or else Stackdriver Debugger might show incorrect
information about your application.

##  October 20, 2016

**CHANGED:**

**Debugger GA & logs integration ** : Debugger is generally available.
Debugger now integrates a log panel into the debug view and will remember the
last selected location. Additionally, you can insert logpoints dynamically
without any rebuilds or restarts. The left and right panels in debug view can
now be collapsed for additional viewing space for source.

