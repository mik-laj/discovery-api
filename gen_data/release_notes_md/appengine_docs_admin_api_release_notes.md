#  Admin API release notes

Python  2.7  / [ 3.7 ](/appengine/docs/standard/python3/

release-notes "View this page in the Python 3.7 runtime") |  Java [ 8
](/appengine/docs/standard/java/release-notes "View this page in the Java 8
runtime") / [ 11 ](/appengine/docs/standard/java11/

release-notes "View this page in the Java 11 runtime") |  PHP [ 5
](/appengine/docs/standard/php/release-notes "View this page in the PHP 5
runtime") / [ 7 ](/appengine/docs/standard/php7/

release-notes "View this page in the PHP 7 runtime") |  [ Ruby
](/appengine/docs/standard/ruby/

release-notes "View this page in the Ruby runtime") |  Go [ 1.11
](/appengine/docs/standard/go111/

release-notes "View this page in the Go 1.11 runtime") / [ 1.12+
](/appengine/docs/standard/go/

release-notes "View this page in the Go 1.12 and newer runtimes") |  [ Node.js
](/appengine/docs/standard/nodejs/

release-notes "View this page in the Node.js runtime")

In addition to the release notes below, you can also track known issues on the
[ issue tracker
](https://issuetracker.google.com/issues?q=componentid:187191%2B) .

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/app-engine-admin-api-release-
notes.xml `

##  February 11, 2020

App Engine is changing the URLs that you use to send requests to your apps.
You can now [ include a region ID ](/appengine/docs/standard/python/how-
requests-are-routed#region-id) to help Google route your requests more
efficiently and reliably. For example, an app can receive requests at `
https://  PROJECT_ID  .  REGION_ID  .r.appspot.com ` . This new URL is
optional for existing apps, and will soon be required for all new apps.

To ensure a smooth transition, we are slowly updating App Engine to use region
IDs. If we haven't updated your Google Cloud project yet, you won't see a
region ID for your app. Since the ID is optional for existing apps, you don't
need to update URLs or make other changes once the region ID is available for
your existing apps.

##  February 6, 2020

  * You can no longer apply new spending limits to projects. Existing spending limits will continue to work. For more information on how you can limit app costs, see [ Limiting Costs ](/appengine/docs/managing-costs) . 

##  Jan 2, 2019

  * Updated Python SDK to version 1.9.88. 

##  December 11, 2019

  * [ Serverless VPC Access ](/appengine/docs/standard/python/connecting-vpc) is now GA. 

##  October 30, 2019

  * Updated Python SDK to version 1.9.87. 

