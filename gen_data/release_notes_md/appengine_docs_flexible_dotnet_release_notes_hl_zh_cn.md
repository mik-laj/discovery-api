#  .NET 版本说明

您可以在 [ Google Cloud 版本说明 ](https://cloud.google.com/release-notes?hl=zh-cn)
页面上查看所有 Google Cloud 的最新产品动态。

要接收最新产品动态，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接添加 Feed 网址： `
https://cloud.google.com/feeds/gaeflex-net-release-notes.xml `

##  July 08, 2020

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs?hl=zh-cn) . Notably, this
feature allows you to use [ Cloud CDN ](https://cloud.google.com/cdn?hl=zh-cn)
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
](https://cloud.google.com/appengine/docs/flexible/dotnet/labeling-
resources?hl=zh-cn) .

##  April 20, 2020

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV)

##  April 13, 2020

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data you can send and receive through a
socket.

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
](https://cloud.google.com/appengine/docs/flexible/dotnet/how-requests-are-
routed?hl=zh-cn#region-id) to help Google route your requests more efficiently
and reliably. For example, an app can receive requests at `
https://PROJECT_ID.REGION_ID.r.appspot.com ` . This new URL is optional for
existing apps, and will soon be required for all new apps.

To ensure a smooth transition, we are slowly updating App Engine to use region
IDs. If we haven't updated your Google Cloud project yet, you won't see a
region ID for your app. Since the ID is optional for existing apps, you don't
need to update URLs or make other changes once the region ID is available for
your existing apps.

##  April 18, 2019

**FEATURE:**

  * App Engine is now available in the ` asia-northeast2 ` region (Osaka, Japan). 

##  April 15, 2019

**FEATURE:**

  * App Engine is now available in the ` europe-west6 ` region (Zürich, Switzerland). 

##  April 09, 2019

**FEATURE:**

[ Cloud Tasks ](https://cloud.google.com/tasks/docs?hl=zh-cn) is now GA and
can be used to set up tasks to be performed asychronously, outside of user
requests.

##  March 04, 2019

**FEATURE:**

[ Cloud Scheduler ](https://cloud.google.com/scheduler/docs?hl=zh-cn) is now
GA and can be used to set up scheduled units of work (cron jobs).

##  October 22, 2018

**FEATURE:**

  * App Engine is now available in the ` asia-east2 ` region (Hong Kong). 

##  July 10, 2018

**FEATURE:**

  * App Engine is now available in the ` us-west2 ` region (Los Angeles). 

##  May 04, 2018

**FEATURE:**

  * Applications in the App Engine flexible environment currently use a Debian 8 "Jessie" operating system. The Debian 8 "Jessie" OS will lose full support from the Debian maintainers in June 2018. In advance of this change, Google will migrate customers to an Ubuntu-based OS starting on May 30, 2018. To update your application to the Ubuntu 16.04 OS, re-deploy your application after May 30, 2018. 

If for some reason you need to opt-out of this automatic upgrade, you can [
pin your application to the old Debian 8 "Jessie" OS
](https://cloud.google.com/appengine/docs/deprecations/pin-app-to-
debian?hl=zh-cn) .

##  January 10, 2018

**FEATURE:**

  * App Engine is now available in the ` northamerica-northeast1 ` region (Montréal, Canada).bn ` 

##  December 14, 2017

**FEATURE:**

  * Improved access control documentation around deploying apps with IAM roles and service accounts: 

    * [ Predefined App Engine roles ](https://cloud.google.com/appengine/docs/flexible/dotnet/access-control?hl=zh-cn#predefined_app_engine_roles)
    * [ Deploying using IAM roles ](https://cloud.google.com/appengine/docs/flexible/dotnet/granting-project-access?hl=zh-cn#deploying_using_iam_roles)
    * [ Require permissions ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=zh-cn#required_permissions)

##  October 31, 2017

**FEATURE:**

  * App Engine is now available in the ` asia-south1 ` region (Mumbai, India). 

##  October 11, 2017

**FEATURE:**

  * Announced general availability of [ App Engine firewall ](https://cloud.google.com/appengine/docs/flexible/dotnet/creating-firewalls?hl=zh-cn) . 

##  October 05, 2017

**FEATURE:**

  * .NET Core support is generally available on the App Engine flexible environment. Docker images are available for .NET Core 1.0, 1.1, and 2.0. 

##  October 02, 2017

**FEATURE:**

  * For the App Engine flexible environment, all responses are now compressed with gzip by default once you redeploy your app. No changes need to be made to your ` app.yaml ` file. 

##  September 26, 2017

**FEATURE:**

  * For the App Engine flexible environment, billing increments for instances are reduced from per-minute increments to per-second increments. Additionally, the minimum usage cost for instance resources is reduced from 10 minutes to 1 minute. 

##  September 18, 2017

**FEATURE:**

  * [ Updated health checks ](https://cloud.google.com/appengine/docs/flexible/dotnet/reference/app-yaml?hl=zh-cn#updated_health_checks) are now the default for new projects. To upgrade a project from legacy health checks, run the command ` gcloud app update --split-health-checks ` . 

**DEPRECATED:**

Legacy health checks will no longer be available after September 30th, 2018.

##  September 13, 2017

**FEATURE:**

  * You can now use managed certificates to add SSL to your custom domain. Once you map your custom domain to your application, App Engine provisions an SSL certificate automatically and handles renewing the certificate before it expires and revoking it if you remove the custom domain. Managed certificates are in beta. For more information, see [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/flexible/dotnet/securing-custom-domains-with-ssl?hl=zh-cn) . 

**FEATURE:**

  * If you have an existing domain mapping and SSL certificate, then it continues to function as expected. You can also [ upgrade to managed SSL certificates ](https://cloud.google.com/appengine/docs/flexible/dotnet/securing-custom-domains-with-ssl?hl=zh-cn#updating_to_managed_ssl_certificates) . 

**FEATURE:**

  * The ` gcloud ` commands and Admin API methods used to [ map custom domains ](https://cloud.google.com/appengine/docs/flexible/dotnet/mapping-custom-domains?hl=zh-cn) are now generally available. This includes [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains/?hl=zh-cn) and [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=zh-cn) . However, if you want to use managed SSL certificates, use the beta commands and methods that are specified in [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/flexible/dotnet/securing-custom-domains-with-ssl?hl=zh-cn) . 

##  September 05, 2017

**FEATURE:**

  * App Engine is now available in the ` southamerica-east1 ` region (São Paulo, Brazil). 

##  August 23, 2017

**FEATURE:**

  * Beta release of the [ App Engine firewall ](https://cloud.google.com/appengine/docs/flexible/dotnet/creating-firewalls?hl=zh-cn) . 

##  August 01, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west3 ` region (Frankfurt, Germany). 

##  July 18, 2017

**FEATURE:**

  * App Engine is now available in the ` australia-southeast1 ` region (Sydney, Australia). 

##  July 12, 2017

**FEATURE:**

  * You can now use updated health checks, which allow you to use separate checks to confirm that your instance is running and ready to serve content. You must enable updated health checks, which are currently in Beta. For more information, see [ Health checks ](https://cloud.google.com/appengine/docs/flexible/dotnet/configuring-your-app-with-app-yaml?hl=zh-cn#health_checks) . 

**CHANGED:**

  * If you use updated health checks, deployments will fail if your application does not reach a ready state. 

##  June 06, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west2 ` region (London). 

**FEATURE:**

  * You can now use the beta-level features in the Admin API and ` gcloud ` command-line tool to [ create and manage your custom domains and SSL certificates ](https://cloud.google.com/appengine/docs/flexible/dotnet/using-custom-domains-and-ssl?hl=zh-cn) . 

##  May 09, 2017

**FEATURE:**

  * App Engine is now available in the ` us-east4 ` region (North Virginia). 

##  March 28, 2017

**FEATURE:**

  * The flexible environment is now available in the [ ` europe-west ` region ](https://cloud.google.com/appengine/docs/locations?hl=zh-cn) . 

##  March 09, 2017

**FEATURE:**

  * The App Engine flexible environment is now generally available (GA). You can run Node.js, Ruby, Python, Java, and Go applications with a [ 99.95% SLA ](https://cloud.google.com/appengine/sla?hl=zh-cn) . 

**FEATURE:**

  * The [ PHP 7 runtime ](https://cloud.google.com/appengine/docs/flexible/php/?hl=zh-cn) for the App Engine flexible environment is now in Beta. 

**FEATURE:**

  * The [ .NET core runtime ](https://cloud.google.com/appengine/docs/flexible/dotnet/?hl=zh-cn) for the App Engine flexible environment is now in Beta. 

##  December 06, 2016

**FEATURE:**

  * New applications that have not been deployed in the flexible environment must specify ` env: true ` in the ` app.yaml ` file instead of ` vm:true ` . Applications that were previously deployed can continue to use ` vm:true ` but will need to switch to ` env:true ` in the future. For more details, see [ upgrade guide ](https://cloud.google.com/appengine/docs/flexible/python/upgrading?hl=zh-cn) . 

##  November 15, 2016

**FEATURE:**

There is a new release of the App Engine flexible environment. To choose this
environment, use ` env:flex ` instead of ` vm:true ` in your ` app.yaml `
configuration file. You can learn more about the details of this release by
visiting the [ upgrade guide
](https://cloud.google.com/appengine/docs/flexible/python/upgrading?hl=zh-cn)
.

**FEATURE:**

This release includes a few key new features:

  * Multi-zonal deployment support. 
  * A modern networking stack with increased throughput. 
  * Custom machine types. 
  * Asia-Northeast1 region availability. 

**DEPRECATED:**

This release also marks the deprecation of a few features:

  * The python-compat runtime. 
  * The python27 runtime. 
  * The java-compat runtime. 
  * The jetty9-compat runtime. 
  * The [ Go App Engine package ](https://github.com/golang/appengine) no longer works on the App Engine flexible environment. Instead, use the [ ` cloud.google.com/go/... ` package ](https://github.com/GoogleCloudPlatform/google-cloud-go) . 

**CHANGED:**

There are also a few breaking changes:

  * HTTP headers have been changed. 
  * Environment variables have been changed. 
  * There are multiple changes to the ` app.yaml ` schema. 

For details and a full list of changes, visit the [ upgrade guide
](https://cloud.google.com/appengine/docs/flexible/python/upgrading?hl=zh-cn)
.

##  May 02, 2016

**FEATURE:**

  * The [ Ruby runtime ](https://cloud.google.com/appengine/docs/flexible/ruby/?hl=zh-cn) is now available for the App Engine flexible environment. 

##  March 24, 2016

**FEATURE:**

  * App Engine Managed VMs is renamed to [ App Engine flexible environment ](https://cloud.google.com/appengine/docs/flexible/?hl=zh-cn) . 

##  February 03, 2016

**FEATURE:**

  * Container construction choices for Managed VMs 

The ` gcloud preview app deploy ` (and ` mvn gcloud:deploy ` ) commands upload
your artifacts to our servers and build a container to deploy your app to the
Managed VM environment.

There are two mechanisms for building the container image remotely. The
default behavior is to build the container on a transient Compute Engine
Virtual Machine which has Docker installed. Alternatively, you can use the [
Cloud Build ](https://cloud.google.com/cloud-build/docs/?hl=zh-cn) service,
which is in Beta. To use the Cloud Build service, follow these steps:

    1. [ Activate the Cloud Build API ](https://support.google.com/cloud/answer/6158841?hl=zh-cn) for your project. 
    2. Use the command ` gcloud config set app/use_cloud_build True ` . This will cause all invocations of ` gcloud preview app deploy ` to use the service. To return to the default behavior, use the command ` gcloud config set app/use_cloud_build False ` . 

