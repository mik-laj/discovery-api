#  Go 1.11 リリースノート

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/gaestd-go-release-notes.xml `
を直接追加します。

##  June 08, 2020

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

##  May 14, 2020

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/go111/labeling-
resources?hl=ja) .

##  April 20, 2020

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

##  March 13, 2020

**FEATURE:**

App Engine is now available in the ` asia-northeast3 ` region (Seoul).

##  March 06, 2020

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

##  February 06, 2020

**DEPRECATED:**

  * You can no longer apply new spending limits to projects. Existing spending limits will continue to work. For more information on how you can limit app costs, see [ Limiting Costs ](https://cloud.google.com/appengine/docs/managing-costs?hl=ja)

##  December 11, 2019

**FEATURE:**

  * [ Serverless VPC Access ](https://cloud.google.com/appengine/docs/standard/go111/connecting-vpc?hl=ja) is now GA. 

##  October 16, 2019

**FEATURE:**

  * The [ Go 1.13 runtime ](https://cloud.google.com/appengine/docs/standard/go113/runtime?hl=ja) for the App Engine standard environment is now Beta. 

##  September 27, 2019

**FEATURE:**

  * Updated Go SDK version to 1.9.71: 

    * Support for Go versions 1.9 and older has been removed. 
    * The ` goapp ` tool has been removed. 
    * The Go 1.9 GOROOT directory has been removed. 

##  July 30, 2019

**FEATURE:**

  * The AppCfg tooling and the legacy standalone App Engine SDK, delivered through the ` GoogleAppEngineLauncher.dmg ` , ` GoogleAppEngine.msi ` , and ` google_appengine.zip ` files, are now deprecated. Google will shut down and remove support on July 30, 2020. 

**FEATURE:**

  * The functionalities of the App Engine SDK is delivered exclusively through [ Cloud SDK ](https://cloud.google.com/sdk/docs?hl=ja) . For more information, see [ Migrating to Cloud SDK ](https://cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration?hl=ja) . 

##  June 27, 2019

**DEPRECATED:**

  * Support for Go 1.9 on App Engine is now [ deprecated ](https://cloud.google.com/appengine/docs/deprecations/?hl=ja) . 

**DEPRECATED:**

  * New Go 1.9 app deployments will not be possible from October 1, 2019. Upgrade your Go 1.9 app to use the [ Go 1.11 runtime ](https://cloud.google.com/appengine/docs/standard/go111/go-differences?hl=ja) or the [ Go 1.12 runtime ](https://cloud.google.com/appengine/docs/standard/go112/go-differences?hl=ja) . 

##  May 23, 2019

**FIXED:**

  * Fixed a bug with ` main ` in app.yaml files for Go 1.11 and Go 1.12 runtimes that rejected valid main package paths. 

##  May 16, 2019

**FEATURE:**

  * The [ Go 1.12 runtime ](https://cloud.google.com/appengine/docs/standard/go112/runtime?hl=ja) on the App Engine standard environment is now generally available. 

##  April 18, 2019

**FEATURE:**

  * App Engine is now available in the ` asia-northeast2 ` region (Osaka, Japan). 

##  April 15, 2019

**FEATURE:**

  * App Engine is now available in the ` europe-west6 ` region (Zürich, Switzerland). 

##  April 09, 2019

**FEATURE:**

  * [ Cloud Tasks ](https://cloud.google.com/tasks/docs?hl=ja) is now GA and can be used to set up tasks to be performed asychronously, outside of user requests. 

**FEATURE:**

  * [ Serverless VPC Access ](https://cloud.google.com/appengine/docs/standard/go111/connecting-vpc?hl=ja) is now in beta. Serverless VPC Access enables your app to connect to internal resources in your VPC network, such as Compute Engine VM instances, Memorystore instances, and more. 

##  March 25, 2019

**FEATURE:**

  * The [ Go 1.12 runtime ](https://cloud.google.com/appengine/docs/standard/go112/?hl=ja) for the App Engine standard environment is now in beta. 

**FEATURE:**

  * A migration guide for [ moving apps from Go 1.9 to Go 1.12 ](https://cloud.google.com/appengine/docs/standard/go112/go-differences?hl=ja) is available. 

##  March 20, 2019

**FEATURE:**

  * The [ Go 1.11 runtime ](https://cloud.google.com/appengine/docs/standard/go111/runtime?hl=ja) for the App Engine standard environment is now GA. 

##  November 06, 2018

**FEATURE:**

  * Updated Go SDK to version 1.9.70. 

**DEPRECATED:**

  * Go 1.6 and Go 1.8 deployments from ` gcloud ` are now blocked. 

##  October 22, 2018

**FEATURE:**

  * App Engine is now available in the ` asia-east2 ` region (Hong Kong). 

##  October 10, 2018

**FEATURE:**

  * The [ Go 1.11 runtime ](https://cloud.google.com/appengine/docs/standard/go111?hl=ja) for the App Engine standard environment is now in beta. 

**FEATURE:**

  * A migration guide for [ moving apps from Go 1.9 to Go 1.11 ](https://cloud.google.com/appengine/docs/standard/go111/go-differences?hl=ja) is available. 

##  September 12, 2018

**FEATURE:**

  * Updated Go SDK to version 1.9.68. 

**FIXED:**

  * Minor bug fixes. 

##  August 01, 2018

**DEPRECATED:**

  * Support for Go 1.6 and Go 1.8 on App Engine is now [ deprecated ](https://cloud.google.com/appengine/docs/deprecations/?hl=ja) . 

**DEPRECATED:**

  * New Go 1.6 and Go 1.8 app deployments will not be possible from November 1, 2018. 

##  July 13, 2018

**FEATURE:**

  * Updated Go SDK to version 1.9.67. 

**FIXED:**

  * Fixed a bug which impacted the local development server. 

##  July 10, 2018

**FEATURE:**

  * App Engine is now available in the ` us-west2 ` region (Los Angeles). 

##  July 03, 2018

**FEATURE:**

  * Updated Go SDK to version 1.9.66. 

**FEATURE:**

  * The [ local development server ](https://cloud.google.com/appengine/docs/standard/go/tools/using-local-server?hl=ja) now prints the process ID of the running process on startup. You can use the process ID when debugging your app. 

##  July 02, 2018

**FIXED:**

Fixed a bug in [ auto scaling configuration
](https://cloud.google.com/appengine/docs/standard/go111/config/appref?hl=ja#scaling_elements)
where App Engine was aggressively shutting down instances when the `
max_instances ` setting was used.

##  June 26, 2018

**FEATURE:**

  * Updated Go SDK to version 1.9.65. 

**FEATURE:**

  * Version 1.9 of the [ Go runtime ](https://cloud.google.com/appengine/docs/standard/go/runtime?hl=ja) is now generally available and is set as the default runtime for Go in the App Engine standard environment. 

Re-deploying all new and existing applications using [ ` api_version: go1 `
](https://cloud.google.com/appengine/docs/standard/go/config/appref?hl=ja#api_version)
, will now run on Go 1.9. To continue using other API versions, such as Go
1.6, you must specify ` api_version: go1.6 ` in your ` app.yaml ` file.

##  May 15, 2018

**FEATURE:**

  * Completed a gradual rollout of an upgrade to the automatic scaling system: 
    * Improved efficiency resulting generally in lower instance cost (up to 6% reduction for many users) and up to 30% reduction for _loading requests_ , which are the first request to a new instance. 
    * New max instances setting allows you to cap the total number of instances to be scheduled. 
    * New min instances setting allows you to specify a minimum number of instance to keep running for your app. 
    * New target CPU utilization setting lets you optimize between latency and cost. 
    * New target throughput utilization setting lets you optimize for the number of concurrent requests at which new instances are started. 
    * No more resident instances in auto scaling. Previously, if you used the ` min_idle_instances ` setting, the minimum idle instances were labelled as _Resident_ in the Cloud Console, with the remainder of the instances labelled as _Dynamic_ . The new scheduler simply labels all instances as _Dynamic_ with auto scaling. However, the underlying behavior remains similar to previous behavior. If you use ` min_idle_instances ` and enable warmup requests, you will see at least that many dynamic instances running even during periods with no traffic. 
    * For more details, see the [ auto scaling documentation ](https://cloud.google.com/appengine/docs/standard/go111/config/appref?hl=ja#scaling_elements) . 

##  March 28, 2018

**FEATURE:**

  * Updated Go SDK to version 1.9.64. 

**FEATURE:**

  * App Engine flexible environment applications that declare ` runtime: go ` in their ` app.yaml ` configuration file now deploy with the Go 1.10 runtime. 

##  March 19, 2018

**FEATURE:**

  * Updated Go SDK to version 1.9.63. 

**FEATURE:**

  * Added beta support for version 1.9 of the Go runtime. 

You can try out Go 1.9 by specifying [ ` api_version: go1.9 `
](https://cloud.google.com/appengine/docs/standard/go/config/appref?hl=ja#api_version)
in your ` app.yaml ` configuration file.

To use the 1.9 beta version, you must first update your Go SDK to 1.9.63 or
later. For details about downloading and installing the SDK, see the [
Downloads
](https://cloud.google.com/appengine/docs/standard/go/download?hl=ja) page.

During the beta period, ` api_version: go1 ` continues to be an alias for `
go1.8 ` . Note that ` go1.9 ` is not guaranteed to work correctly while it is
in beta. We are relying on user feedback to ensure that ` go1.9 ` meets users'
needs before promoting it to a GA release. Post feedback to the [ google-
appengine-go ](https://groups.google.com/forum/?hl=ja#!forum/google-appengine-
go) Google Group.

##  January 08, 2018

**FEATURE:**

  * Updated Go SDK to 1.9.62 

**FEATURE:**

  * Includes internal updates for how applications are deployed. 

##  December 14, 2017

**FEATURE:**

  * Improved access control documentation around deploying apps with IAM roles and service accounts: 

    * [ Predefined App Engine roles ](https://cloud.google.com/appengine/docs/standard/go111/access-control?hl=ja#predefined_app_engine_roles)
    * [ Deploying using IAM roles ](https://cloud.google.com/appengine/docs/standard/go111/granting-project-access?hl=ja#deploying_using_iam_roles)
    * [ Require permissions ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=ja#required_permissions)

##  November 15, 2017

**FEATURE:**

  * Updated Go SDK to 1.9.61 

**FEATURE:**

  * Add ` --go_debugging ` flag to ` dev_appserver.py ` to enable [ Delve debugging ](https://github.com/derekparker/delve) . 

**FEATURE:**

  * Add ` -debug ` flag to ` goapp serve ` to enable Delve debugging. 

**FIXED:**

  * Fix ` gcloud app deploy ` failing at finding dependencies that are not required. 

##  October 31, 2017

**FEATURE:**

  * App Engine is now available in the ` asia-south1 ` region (Mumbai, India). 

##  October 25, 2017

**FEATURE:**

  * Updated Go SDK to version 1.9.60. 

**FEATURE:**

  * Version 1.8 of the [ Go runtime ](https://cloud.google.com/appengine/docs/standard/go/runtime?hl=ja) is now generally available and is set as the default runtime for Go in the App Engine standard environment. 

Now, when you deploy any new or existing apps that use [ ` api_version: go1 `
](https://cloud.google.com/appengine/docs/standard/go/config/appref?hl=ja#api_version)
, those apps run on Go 1.8. To continue using Go 1.6, you must specify `
api_version: go1.6 ` in your ` app.yaml ` file.

Before you can use the Go 1.8 runtime locally with ` dev_appserver.py ` or `
goapp ` , you must first [ update to the latest version of the SDK for App
Engine
](https://cloud.google.com/appengine/docs/standard/go/download?hl=ja#updating-
the-sdk-for-go) .

Changes that might affect your app:

    * As of Go 1.7, the ` context ` package has [ moved into the stdlib ](https://golang.org/doc/go1.7#context) . You must ensure that your code and dependencies work correctly with this change. You can use the [ ` fix ` command ](https://golang.org/cmd/fix/) to change your app's imports from ` "golang.org/x/net/context" ` to ` "context" ` , for example: [ ` go tool fix -r context ` ](https://golang.org/doc/go1.8#tool_fix) . 
    * In Go 1.8, the internal representation of ` time.Time ` objects has changed and might break your app if you use either ` reflect.DeepEqual ` or ` == ` to compare ` time.Time ` values. Use [ ` time.Equal ` ](https://golang.org/pkg/time/#Time.Equal) to compare timestamps. 

##  October 11, 2017

**FEATURE:**

  * Announced general availability of [ App Engine firewall ](https://cloud.google.com/appengine/docs/standard/go111/creating-firewalls?hl=ja) . 

##  October 03, 2017

**FEATURE:**

  * Updated Go SDK to 1.9.59 

**FIXED:**

  * Fixed bug in ` dev_appserver.py ` which used incorrect build constraints for the Go 1.8 beta. 

##  September 13, 2017

**FEATURE:**

  * You can now use managed certificates to add SSL to your custom domain. Once you map your custom domain to your application, App Engine provisions an SSL certificate automatically and handles renewing the certificate before it expires and revoking it if you remove the custom domain. Managed certificates are in beta. For more information, see [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/standard/go111/securing-custom-domains-with-ssl?hl=ja) . 

**FEATURE:**

  * If you have an existing domain mapping and SSL certificate, then it continues to function as expected. You can also [ upgrade to managed SSL certificates ](https://cloud.google.com/appengine/docs/standard/go111/securing-custom-domains-with-ssl?hl=ja#updating_to_managed_ssl_certificates) . 

**FEATURE:**

  * The ` gcloud ` commands and Admin API methods used to [ map custom domains ](https://cloud.google.com/appengine/docs/standard/go111/mapping-custom-domains?hl=ja) are now generally available. This includes [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains/?hl=ja) and [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=ja) . However, if you want to use managed SSL certificates, use the beta commands and methods that are specified in [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/standard/go111/securing-custom-domains-with-ssl?hl=ja) . 

##  September 11, 2017

**FEATURE:**

  * Updated Go SDK to version 1.9.58 

**FIXED:**

  * Fixed a bug in goapp.bat which resulted in processes not being properly terminated. 

**FIXED:**

  * Fixed a bug introduced in 1.9.56 which caused signals and stdin to not be propagated correctly. 

##  September 05, 2017

**FEATURE:**

  * App Engine is now available in the ` southamerica-east1 ` region (São Paulo, Brazil). 

##  August 23, 2017

**FEATURE:**

  * Beta release of the [ App Engine firewall ](https://cloud.google.com/appengine/docs/standard/go111/creating-firewalls?hl=ja) . 

##  August 09, 2017

**FEATURE:**

  * Updated Go SDK to version 1.9.57. 

**FEATURE:**

  * The ` aetest ` package now reuses HTTP connections, fixing a bug that exhausted file descriptors when running tests. 

**FEATURE:**

  * Go 1.8 uses the new standard library context package when calling ` appengine.NewContext() ` . 

##  August 01, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west3 ` region (Frankfurt, Germany). 

##  July 18, 2017

**FEATURE:**

  * App Engine is now available in the ` australia-southeast1 ` region (Sydney, Australia). 

##  July 01, 2017

**FEATURE:**

  * Updated Go SDK to version 1.9.56 

**FIXED:**

  * Fixed an issue with auto-reloading apps. 

##  June 27, 2017

**FEATURE:**

  * Updated Go SDK to version 1.9.55 

**FEATURE:**

  * Enable the Go 1.8 beta 

This release adds beta support for ` go1.8 ` . To use Go 1.8, set `
api_version: go1.8 ` in your ` app.yaml ` configuration file. You must also
use App Engine SDK, not Cloud SDK. To download the App Engine SDK, go to the [
Downloads page
](https://cloud.google.com/appengine/docs/standard/go/download?hl=ja) and at
the bottom of the page, expand the **Or, you can download the original App
Engine SDK for Go** section.

Go 1.8 will be available with the next Cloud SDK release.

During the beta period, ` api_version: go1 ` will continue to be an alias for
` go1.6 ` . Note that ` go1.8 ` is not guaranteed to work correctly while it
is in beta. We are relying on user feedback to ensure that ` go1.8 ` meets our
users' needs before promoting it to a GA release. Send feedback to the [
google-appengine-go ](https://groups.google.com/forum/?hl=ja#!forum/google-
appengine-go) google group.

**BREAKING:**

  * As of ` go1.7 ` the ` context ` package has [ moved into the stdlib ](https://golang.org/doc/go1.7#context) . Ensure that your code and dependencies work correctly with this change. 

**BREAKING:**

  * Note that ` go1.8 ` changes the way that local timezones and UTC are represented. If you use ` reflect.DeepEqual ` or ` == ` to compare ` time.Time ` values, this might be a breaking change. Instead, use [ ` time.Equal ` ](https://golang.org/pkg/time/#Time.Equal) when comparing timestamps. 

##  June 06, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west2 ` region (London). 

**FEATURE:**

  * You can now use the beta-level features in the Admin API and ` gcloud ` command-line tool to [ create and manage your custom domains and SSL certificates ](https://cloud.google.com/appengine/docs/standard/go111/mapping-custom-domains?hl=ja) . 

##  May 22, 2017

**FEATURE:**

  * Updated Go SDK to version 1.9.54. 

**FEATURE:**

  * ` api_version: go1 ` and ` api_version: go1.6 ` both use the new ` goroot-1.6 ` directory. 

**FEATURE:**

  * Upgraded to Go 1.6.4 

##  May 09, 2017

**FEATURE:**

  * App Engine is now available in the ` us-east4 ` region (North Virginia). 

##  May 04, 2017

**FEATURE:**

  * Updated Go SDK to version 1.9.53. 

**FEATURE:**

  * In preparation for the Go 1.8 beta, Go ` api_version ` s are mapped to specific ` GOROOT ` directories. 

##  December 01, 2016

**FEATURE:**

  * Updated Go SDK to version 1.9.48. 

##  November 03, 2016

**FEATURE:**

  * Updated Go SDK to version 1.9.46. 

##  October 27, 2016

**DEPRECATED:**

  * The Channel and XMPP services are now [ deprecated ](https://cloud.google.com/appengine/docs/deprecations/?hl=ja) . These services will be turned down on October 31, 2017. 

##  August 01, 2016

**FEATURE:**

**Admin API notes**

  * Version 1 of the [ Admin API ](https://cloud.google.com/appengine/docs/admin-api/?hl=ja) is now generally available. 

**FEATURE:**

Version 1.9.42

**Go 1.11 runtime notes**

  * This release does not include a new Go 1.11 SDK. Go 1.11 users should continue to use the 1.9.40 SDK. 

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

  * New [ App Engine guided walkthrough ](https://console.cloud.google.com/start/appengine?hl=ja) in the Cloud Console. Pick your preferred language and launch an interactive tutorial directly in the console. 

**FEATURE:**

  * Increases the maximum cron tasks limit to 250. 

##  July 01, 2016

**FEATURE:**

**Cloud Datastore**

  * New [ Cloud Datastore Pricing ](https://cloud.google.com/appengine/pricing?hl=ja#costs-for-datastore-calls) is now in effect. 

##  May 25, 2016

**FEATURE:**

Version 1.9.38

**FEATURE:**

  * The error returned by URL Fetch for a request to a port outside of the permitted ranges (80-90, 440-450, 1024-65535) will now always return ` INVALID_URL ` as documented. 

**FEATURE:**

**Cloud Datastore**

  * When committing a cross-group transaction, version numbers returned for new or updated entities are all the same. With the previous behavior, entities within the same group committed as part of a cross-group transaction, had the same version number, but entities in different groups might have had different version numbers. This change ensures all new and updated entities have an identical version number, regardless of their entity group, when committed as part of a cross-group transaction. As before, entities that are not updated will not have a new version number. 

**FEATURE:**

  * App Engine Go runtime updated to Go 1.6.2. 

**FEATURE:**

Version 1.9.37 SDK uses the release tags go1.1–go1.6 when compiling with the
development SDK to bring it inline with those used in typical Go 1.6 builds.
Starting with the 1.9.37 SDK, all the necessary Go files in your gopath will
be uploaded to the server regardless of the release tags they require. This
will ensure that the server always has all the files it needs to compile your
app regardless of the release tags being used. This addresses problems that
may arise from mismatched release tags in the 1.9.35 SDK.

##  May 04, 2016

**FIXED:**

Version 1.9.37

Includes general bug fixes and improvements.

##  May 02, 2016

**FEATURE:**

**App Engine flexible environment**

  * The [ Ruby runtime ](https://cloud.google.com/appengine/docs/flexible/ruby/?hl=ja) is now available for the App Engine flexible environment. 

##  April 18, 2016

**FEATURE:**

Version 1.9.36

In response to your requests, the App Engine Users API joins the rest of App
Engine in supporting IAM roles and group expansion. This means that any user
who is a project Owner, Editor or Viewer or an App Engine Admin is considered
an "admin" by the Users API, regardless of whether the user was granted the
role directly or by membership in a group. * This release populates error
details, when available, in error messages associated with the "OverQuota"
exception type.

  * Google no longer accepts quota increase requests for the mail service. Customers should use [ Sendgrid ](https://cloud.google.com/appengine/docs/standard/go/mail/sendgrid?hl=ja) instead. ############END############ ############START########## 2016-03-24 

FEATURE

Version 1.9.35

  * App Engine Managed VMs is renamed to [ App Engine flexible environment ](https://cloud.google.com/appengine/docs/flexible/?hl=ja) . 
  * Fixes trace timestamps to match log timestamps. 
  * This release is based on Go 1.6. 

  * The SDK now includes support for vendoring external dependencies. See the [ go command documentation ](https://golang.org/cmd/go/#hdr-Vendor_Directories) for more details. 

##  March 04, 2016

**FEATURE:**

Version 1.9.34

  * Increases default quota for URL fetch for billed apps. Refer to the [ Quotas page ](https://cloud.google.com/appengine/docs/quotas?hl=ja#UrlFetch) for details. 

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
Cloud Build ](https://cloud.google.com/cloud-build/docs/?hl=ja) service. To
use the Cloud Build service, follow these steps:

    1. [ Activate the Cloud Build API ](https://support.google.com/cloud/answer/6158841?hl=ja) for your project. 
    2. Use the command ` gcloud config set app/use_cloud_build True ` . This will cause all invocations of ` gcloud preview app deploy ` to use the service. (To return to the default behavior, use the command ` gcloud config set app/use_cloud_build False ` . 

**FEATURE:**

  * Enabled response compression in Go runtime. This might reduce bandwidth usage for some users. 

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

  * Stop calculating and storing queue depth for non-existent queues, queues marked for deletion, and in the case of queue table outages. 

**FEATURE:**

  * For developers using the [ endpoints API ](https://cloud.google.com/appengine/docs/standard/python/endpoints/create_api?hl=ja#defining_the_api_endpointsapi) , added a discoverable boolean parameter to the @Api annotation to allow users to disable API discovery. Using this feature will prevent some client libraries (e.g. JavaScript) and the API Explorer from working, as they depend on discovery. 

##  October 29, 2015

**FEATURE:**

Version 1.9.28

**DEPRECATED:**

The Prospective Search API, which was deprecated on July 14, is now restricted
to existing users. It will fully shutdown on December 1.

**FEATURE:**

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
](https://console.cloud.google.com/project/_/appengine/settings?hl=ja) . For
more information, see [ Setting a daily budget
](https://cloud.google.com/appengine/docs/developers-
console/?hl=ja#setting_a_daily_budget) .

**FIXED:**

Datastore

  * Bugfix: Repeated numeric facets are now allowed. 

**FEATURE:**

Datastore

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

  * Added PyAMF version 0.7.2 (Beta). 

**FEATURE:**

  * Admin Console menus start redirecting to Cloud Console. Select services such as the Admin Logs will continue to be available in the Admin Console. 

**FEATURE:**

  * Datastore now allows properties to represent the empty list. 

**FEATURE:**

  * Failed tasks in queues configured with a ` retry_limit ` of zero will no longer be retried. 

**FEATURE:**

  * appengine/search: 
    * Support offsets and cursors in search requests and responses. 
  * appengine/user:new 
    * Add ` User.ClientID ` field. 

