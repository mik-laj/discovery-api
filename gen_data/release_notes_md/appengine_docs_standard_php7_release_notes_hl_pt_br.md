#  Notas da versão do PHP 7.2

Você pode ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas de versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt-br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/gaestd-php-release-
notes.xml `

##  July 08, 2020

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs?hl=pt-br) . Notably, this
feature allows you to use [ Cloud CDN ](https://cloud.google.com/cdn?hl=pt-br)
with App Engine.  
This feature is available in Beta.

##  June 08, 2020

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

##  May 14, 2020

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/php7/labeling-
resources?hl=pt-br) .

##  April 20, 2020

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

##  March 13, 2020

**FEATURE:**

App Engine is now available in the ` asia-northeast3 ` region (Seoul).

##  March 06, 2020

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

##  February 11, 2020

**FEATURE:**

App Engine is changing the URLs that you use to send requests to your apps.
You can now [ include a region ID
](https://cloud.google.com/appengine/docs/standard/php7/how-requests-are-
routed?hl=pt-br#region-id) to help Google route your requests more efficiently
and reliably. For example, an app can receive requests at `
https://<var>PROJECT_ID</var>.<var>REGION_ID</var>.r.appspot.com ` . This new
URL is optional for existing apps, and will soon be required for all new apps.

To ensure a smooth transition, we are slowly updating App Engine to use region
IDs. If we haven't updated your Google Cloud project yet, you won't see a
region ID for your app. Since the ID is optional for existing apps, you don't
need to update URLs or make other changes once the region ID is available for
your existing apps.

##  February 06, 2020

**DEPRECATED:**

  * You can no longer apply new spending limits to projects. Existing spending limits will continue to work. For more information on how you can limit app costs, see [ Limiting Costs ](https://cloud.google.com/appengine/docs/managing-costs?hl=pt-br) . 

##  December 11, 2019

**FEATURE:**

  * [ Serverless VPC Access ](https://cloud.google.com/appengine/docs/standard/php7/connecting-vpc?hl=pt-br) is now GA. 

##  October 10, 2019

**FEATURE:**

  * The [ PHP 7.3 runtime ](https://cloud.google.com/appengine/docs/standard/php7/runtime?hl=pt-br) for the App Engine standard environment is now GA. 

##  July 30, 2019

**DEPRECATED:**

  * The AppCfg tooling and the legacy standalone App Engine SDK, delivered through the ` GoogleAppEngineLauncher.dmg ` , ` GoogleAppEngine.msi ` , and ` google_appengine.zip ` files, are now deprecated. Google will shut down and remove support on July 30, 2020. 

**FEATURE:**

  * The functionalities of the App Engine SDK is delivered exclusively through [ Cloud SDK ](https://cloud.google.com/sdk/docs?hl=pt-br) . For more information, see [ Migrating to Cloud SDK ](https://cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration?hl=pt-br) . 

##  May 28, 2019

**FEATURE:**

  * The [ PHP 7.3 runtime ](https://cloud.google.com/appengine/docs/standard/php7/runtime?hl=pt-br) for the App Engine standard environment in now beta. 

##  April 18, 2019

**FEATURE:**

  * App Engine is now available in the ` asia-northeast2 ` region (Osaka, Japan). 

##  April 15, 2019

**FEATURE:**

  * App Engine is now available in the ` europe-west6 ` region (Zürich, Switzerland). 

##  April 09, 2019

**FEATURE:**

  * [ Cloud Tasks ](https://cloud.google.com/tasks/docs?hl=pt-br) is now GA and can be used to set up tasks to be performed asychronously, outside of user requests. 

**FEATURE:**

  * [ Serverless VPC Access ](https://cloud.google.com/appengine/docs/standard/php7/connecting-vpc?hl=pt-br) is now in beta. Serverless VPC Access enables your app to connect to internal resources in your VPC network, such as Compute Engine VM instances, Memorystore instances, and more. 

##  March 20, 2019

**FEATURE:**

  * The [ PHP 7.2 runtime ](https://cloud.google.com/appengine/docs/standard/php7/runtime?hl=pt-br) for the App Engine standard environment in now GA. 

##  October 22, 2018

**FEATURE:**

  * App Engine is now available in the ` asia-east2 ` region (Hong Kong). 

##  August 21, 2018

**FEATURE:**

  * The [ PHP 7.2 runtime ](https://cloud.google.com/appengine/docs/standard/php7?hl=pt-br) for the App Engine standard environment is now in beta. 

**FEATURE:**

  * A migration guide for [ moving apps from PHP 5.5 to PHP 7.2 ](https://cloud.google.com/appengine/docs/standard/php7/php-differences?hl=pt-br) is available. 

##  July 10, 2018

**FEATURE:**

  * App Engine is now available in the ` us-west2 ` region (Los Angeles). 

##  July 02, 2018

**FIXED:**

Fixed a bug in [ auto scaling configuration
](https://cloud.google.com/appengine/docs/standard/php7/config/appref?hl=pt-
br#scaling_elements) where App Engine was aggressively shutting down instances
when the ` max_instances ` setting was used.

##  May 15, 2018

**FEATURE:**

  * Completed a gradual rollout of an upgrade to the automatic scaling system: 
    * Improved efficiency resulting generally in lower instance cost (up to 6% reduction for many users) and up to 30% reduction for _loading requests_ , which are the first request to a new instance. 
    * New max instances setting allows you to cap the total number of instances to be scheduled. 
    * New min instances setting allows you to specify a minimum number of instance to keep running for your app. 
    * New target CPU utilization setting lets you optimize between latency and cost. 
    * New target throughput utilization setting lets you optimize for the number of concurrent requests at which new instances are started. 
    * No more resident instances in auto scaling. Previously, if you used the ` min_idle_instances ` setting, the minimum idle instances were labelled as _Resident_ in the Cloud Console, with the remainder of the instances labelled as _Dynamic_ . The new scheduler simply labels all instances as _Dynamic_ with auto scaling. However, the underlying behavior remains similar to previous behavior. If you use ` min_idle_instances ` and enable warmup requests, you will see at least that many dynamic instances running even during periods with no traffic. 
    * For more details, see the [ auto scaling documentation ](https://cloud.google.com/appengine/docs/standard/php7/config/appref?hl=pt-br#scaling_elements) . 

##  January 23, 2018

**FEATURE:**

  * Updated Python SDK to 1.9.66. 

**FIXED:**

  * Fixes the [ ` ipaddr ` library import issue ](https://issuetracker.google.com/issues/71704025?hl=pt-br) when starting PHP app with the local development server. 

##  December 14, 2017

**FEATURE:**

  * Improved access control documentation around deploying apps with IAM roles and service accounts: 

    * [ Predefined App Engine roles ](https://cloud.google.com/appengine/docs/standard/php7/access-control?hl=pt-br#predefined_app_engine_roles)
    * [ Deploying using IAM roles ](https://cloud.google.com/appengine/docs/standard/php7/granting-project-access?hl=pt-br#deploying_using_iam_roles)
    * [ Require permissions ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=pt-br#required_permissions)

##  October 31, 2017

**FEATURE:**

  * App Engine is now available in the ` asia-south1 ` region (Mumbai, India). 

##  October 11, 2017

**FEATURE:**

  * Announced general availability of [ App Engine firewall ](https://cloud.google.com/appengine/docs/standard/php7/creating-firewalls?hl=pt-br) . 

##  September 13, 2017

**FEATURE:**

  * You can now use managed certificates to add SSL to your custom domain. Once you map your custom domain to your application, App Engine provisions an SSL certificate automatically and handles renewing the certificate before it expires and revoking it if you remove the custom domain. Managed certificates are in beta. For more information, see [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/standard/php7/securing-custom-domains-with-ssl?hl=pt-br) . 

**FEATURE:**

  * If you have an existing domain mapping and SSL certificate, then it continues to function as expected. You can also [ upgrade to managed SSL certificates ](https://cloud.google.com/appengine/docs/standard/php7/securing-custom-domains-with-ssl?hl=pt-br#updating_to_managed_ssl_certificates) . 

**FEATURE:**

  * The ` gcloud ` commands and Admin API methods used to [ map custom domains ](https://cloud.google.com/appengine/docs/standard/php7/mapping-custom-domains?hl=pt-br) are now generally available. This includes [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains/?hl=pt-br) and [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=pt-br) . However, if you want to use managed SSL certificates, use the beta commands and methods that are specified in [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/standard/php7/securing-custom-domains-with-ssl?hl=pt-br) . 

##  September 05, 2017

**FEATURE:**

  * App Engine is now available in the ` southamerica-east1 ` region (São Paulo, Brazil). 

##  August 01, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west3 ` region (Frankfurt, Germany). 

##  July 18, 2017

**FEATURE:**

  * App Engine is now available in the ` australia-southeast1 ` region (Sydney, Australia). 

##  June 06, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west2 ` region (London). 

**FEATURE:**

  * You can now use the beta-level features in the Admin API and ` gcloud ` command-line tool to [ create and manage your custom domains and SSL certificates ](https://cloud.google.com/appengine/docs/standard/php7/mapping-custom-domains?hl=pt-br) . 

##  May 09, 2017

**FEATURE:**

  * App Engine is now available in the ` us-east4 ` region (North Virginia). 

##  August 01, 2016

**FEATURE:**

**Admin API notes**

  * Version 1 of the [ Admin API ](https://cloud.google.com/appengine/docs/admin-api/?hl=pt-br) is now generally available. 

**FEATURE:**

Version 1.9.42

**CHANGED:**

**PHP 7 runtime notes**

  * This release does not include a new PHP 7 SDK. PHP 7 users should continue to use the 1.9.40 SDK. 

##  July 18, 2016

**FEATURE:**

Version 1.9.40

**CHANGED:**

  * Version 1.9.39 was skipped. 

**FEATURE:**

  * LeaseTasksByTag requests will be limited to 25 requests per second. 

**FEATURE:**

  * Server Errors and Client Errors now more accurately reflect per-URL status errors in the App Engine dashboard. 

**FEATURE:**

  * New [ App Engine guided walkthrough ](https://console.cloud.google.com/start/appengine?hl=pt-br) in the Cloud Console. Pick your preferred language and launch an interactive tutorial directly in the console. 

**FEATURE:**

  * Increases the maximum cron tasks limit to 250. 

##  July 01, 2016

**FEATURE:**

**Cloud Datastore**

  * New [ Cloud Datastore Pricing ](https://cloud.google.com/appengine/pricing?hl=pt-br#costs-for-datastore-calls) is now in effect. 

##  May 25, 2016

**FEATURE:**

Version 1.9.38

**FEATURE:**

  * The error returned by URL Fetch for a request to a port outside of the permitted ranges (80-90, 440-450, 1024-65535) will now always return ` INVALID_URL ` as documented. 

**FEATURE:**

**Cloud Datastore**

  * When committing a cross-group transaction, version numbers returned for new or updated entities are all the same. With the previous behavior, entities within the same group committed as part of a cross-group transaction, had the same version number, but entities in different groups might have had different version numbers. This change ensures all new and updated entities have an identical version number, regardless of their entity group, when committed as part of a cross-group transaction. As before, entities that are not updated will not have a new version number. 

**FEATURE:**

**PHP runtime notes**

  * App Engine PHP runtime updated to PHP 5.5.34. 

##  May 04, 2016

**FEATURE:**

Version 1.9.37

**FIXED:**

Includes general bug fixes and improvements.

##  May 02, 2016

**FEATURE:**

**App Engine flexible environment**

  * The [ Ruby runtime ](https://cloud.google.com/appengine/docs/flexible/ruby/?hl=pt-br) is now available for the App Engine flexible environment. 

##  April 18, 2016

**FEATURE:**

Version 1.9.36

**FEATURE:**

In response to your requests, the App Engine Users API joins the rest of App
Engine in supporting IAM roles and group expansion. This means that any user
who is a project Owner, Editor or Viewer or an App Engine Admin is considered
an "admin" by the Users API, regardless of whether the user was granted the
role directly or by membership in a group. * This release populates error
details, when available, in error messages associated with the "OverQuota"
exception type.

**DEPRECATED:**

**PHP runtime notes**

  * Google no longer accepts quota increase requests for the mail service. Customers should use [ Sendgrid ](https://cloud.google.com/appengine/docs/standard/php/mail/sendgrid?hl=pt-br) instead. 

##  March 24, 2016

**FEATURE:**

Version 1.9.35

**CHANGED:**

  * App Engine Managed VMs is renamed to [ App Engine flexible environment ](https://cloud.google.com/appengine/docs/flexible/?hl=pt-br) . 

**FIXED:**

  * Fixes trace timestamps to match log timestamps. 

##  March 04, 2016

**FEATURE:**

Version 1.9.34

**FEATURE:**

  * Increases default quota for URL fetch for billed apps. Refer to the [ Quotas page ](https://cloud.google.com/appengine/docs/quotas?hl=pt-br#UrlFetch) for details. 

##  February 17, 2016

**FEATURE:**

Version 1.9.33

**FEATURE:**

  * The URL path "/form" is now allowed and will be forwarded to applications. Previously, this path was blocked. 

##  February 03, 2016

**FEATURE:**

Version 1.9.32

**FEATURE:**

  * Container construction choices for Managed VMs 

The ` gcloud preview app deploy ` (and ` mvn gcloud:deploy ` ) commands upload
your artifacts to our servers and build a container to deploy your app to the
Managed VM environment.

There are two mechanisms for building the container image remotely. The
default behavior is to build the container on a transient Compute Engine
Virtual Machine which has Docker installed. Alternatively, you can use the [
Cloud Build ](https://cloud.google.com/cloud-build/docs/?hl=pt-br) service. To
use the Cloud Build service, follow these steps:

    1. [ Activate the Cloud Build API ](https://support.google.com/cloud/answer/6158841?hl=pt-br) for your project. 
    2. Use the command ` gcloud config set app/use_cloud_build True ` . This will cause all invocations of ` gcloud preview app deploy ` to use the service. (To return to the default behavior, use the command ` gcloud config set app/use_cloud_build False ` . 

##  January 14, 2016

**FEATURE:**

Version 1.9.31

**FEATURE:**

App Engine now supports Google Groups: Adding a Google Group as a member of a
project grants the members of the group access to App Engine. For example, if
a Google Group is an Editor on a project, all members of the group now have
Editor access to the App Engine application.

##  November 30, 2015

**FEATURE:**

Version 1.9.30

**FEATURE:**

Headers for push queue requests made for Task Queue tasks with no payload will
now contain a Content-Length entry set to '0'. Previously headers for such
requests contained no Content-Length entry.

**FEATURE:**

Version 1.9.29

**FEATURE:**

  * Stop calculating and storing queue depth for non-existent queues, queues marked for deletion, and in the case of queue table outages. 

**FEATURE:**

  * For developers using the [ endpoints API ](https://cloud.google.com/appengine/docs/standard/python/endpoints/create_api?hl=pt-br#defining_the_api_endpointsapi) , added a discoverable boolean parameter to the @Api annotation to allow users to disable API discovery. Using this feature will prevent some client libraries (e.g. JavaScript) and the API Explorer from working, as they depend on discovery. 

**FEATURE:**

**PHP runtime notes**

  * Add [ fileinfo ](http://php.net/manual/en/book.fileinfo.php) as a dynamically loadable extension. 

##  October 29, 2015

**FEATURE:**

Version 1.9.28

**BREAKING:**

The Prospective Search API, which was deprecated on July 14, 2015, is now
restricted to existing users. It will fully shutdown on December 1, 2015. *
Improved accuracy of Geo filtering in Search queries.

##  September 25, 2015

**FEATURE:**

Version 1.9.27

**FEATURE:**

Applications that are newly enabled for billing now default to an unlimited
daily budget, and no longer default to a maximum daily budget of $0. This
prevents unwanted outages due to running out of budget. To set a ceiling on
your application's daily cost, after you enable billing, set a budget in the [
app engine settings
](https://console.cloud.google.com/project/_/appengine/settings?hl=pt-br) .
For more information, see [ Setting a daily budget
](https://cloud.google.com/appengine/docs/developers-console/?hl=pt-
br#setting_a_daily_budget) .

**FEATURE:**

Datastore

**FIXED:**

  * Bugfix: Repeated numeric facets are now allowed. 

**FEATURE:**

  * Faceted Search is now GA. 

##  August 27, 2015

**FEATURE:**

Version 1.9.26

**FEATURE:**

  * oauth2client library upgraded to version [ 1.4.2 ](https://github.com/google/oauth2client/blob/master/CHANGELOG.md)

**FEATURE:**

  * Adds "show in context" menu for MVM application logs that have thread_id or request_id as a field in their log entry. This allows sorting app logs based on either field. 

**FEATURE:**

  * Capability to provision applications for current load and configure elastic provisioning based on both VM and application level metrics. 

**FEATURE:**

  * Remote API can now be accessed using OAuth2 credentials using https://developers.google.com/identity/protocols/application-default-credentials 

**FEATURE:**

  * Use RequestPayloadTooLargeException for URLFetch requests with payloads that are too large. 

##  August 14, 2015

**FEATURE:**

Version 1.9.25

**FEATURE:**

  * Added PyAMF version 0.7.2 (Beta). 

**FEATURE:**

  * Admin Console menus start redirecting to Cloud Console. Select services such as the Admin Logs will continue to be available in the Admin Console. 

**FEATURE:**

  * Datastore now allows properties to represent the empty list. 

**FEATURE:**

  * Failed tasks in queues configured with a ` retry_limit ` of zero will no longer be retried. 

**DEPRECATED:**

**PHP runtime notes**

  * Development server no longer supports the "php" runtime. This will result in a Runtime Error. Please use "php55" instead. 

