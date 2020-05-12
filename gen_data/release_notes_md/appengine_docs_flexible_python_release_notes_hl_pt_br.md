#  Notas da versão do Python

Você pode ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas de versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt-br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/gaeflex-py-release-
notes.xml `

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
](https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-
routed?hl=pt-br#region-id) to help Google route your requests more efficiently
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

[ Cloud Tasks ](https://cloud.google.com/tasks/docs?hl=pt-br) is now GA and
can be used to set up tasks to be performed asychronously, outside of user
requests.

##  March 04, 2019

**FEATURE:**

[ Cloud Scheduler ](https://cloud.google.com/scheduler/docs?hl=pt-br) is now
GA and can be used to set up scheduled units of work (cron jobs).

##  January 07, 2019

**FEATURE:**

  * You can now use [ WebSockets and session affinity ](https://cloud.google.com/appengine/docs/flexible/python/using-websockets-and-session-affinity?hl=pt-br) to create persistent connections to an App Engine instance. 

##  October 22, 2018

**FEATURE:**

  * App Engine is now available in the ` asia-east2 ` region (Hong Kong). 

##  July 10, 2018

**FEATURE:**

  * App Engine is now available in the ` us-west2 ` region (Los Angeles). 

##  May 04, 2018

**DEPRECATED:**

  * Applications in the App Engine flexible environment currently use a Debian 8 "Jessie" operating system. The Debian 8 "Jessie" OS will lose full support from the Debian maintainers in June 2018. In advance of this change, Google will migrate customers to an Ubuntu-based OS starting on May 30, 2018. To update your application to the Ubuntu 16.04 OS, re-deploy your application after May 30, 2018. 

If for some reason you need to opt-out of this automatic upgrade, you can [
pin your application to the old Debian 8 "Jessie" OS
](https://cloud.google.com/appengine/docs/deprecations/pin-app-to-
debian?hl=pt-br) .

##  March 29, 2018

**DEPRECATED:**

  * The Python 3.4 runtime is [ deprecated ](https://cloud.google.com/appengine/docs/deprecations/python34?hl=pt-br) and will be shut down on March 29, 2019. Update to a more recent Python version as soon as possible. 

##  March 21, 2018

**FEATURE:**

  * The Python 3.4 runtime is updated to version [ 3.4.8 ](https://docs.python.org/3.4/whatsnew/changelog.html#python-3-4-8-final) . This includes some security and bug fixes. 

##  February 14, 2018

**FEATURE:**

  * The Python 3.6 runtime is now updated to version [ 3.6.4 ](https://docs.python.org/3.6/whatsnew/changelog.html#python-3-6-4-final) . This includes some security and bug fixes. 

**FEATURE:**

  * The Python 3.5 runtime is now updated to version [ 3.5.5 ](https://docs.python.org/3.5/whatsnew/changelog.html#python-3-5-5-final) . This includes some security and bug fixes. 

##  January 10, 2018

**FEATURE:**

  * App Engine is now available in the ` northamerica-northeast1 ` region (Montréal, Canada). 

##  December 14, 2017

**FEATURE:**

  * Improved access control documentation around deploying apps with IAM roles and service accounts: 

    * [ Predefined App Engine roles ](https://cloud.google.com/appengine/docs/flexible/python/access-control?hl=pt-br#predefined_app_engine_roles)
    * [ Deploying using IAM roles ](https://cloud.google.com/appengine/docs/flexible/python/granting-project-access?hl=pt-br#deploying_using_iam_roles)
    * [ Require permissions ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=pt-br#required_permissions)

##  October 31, 2017

**FEATURE:**

  * App Engine is now available in the ` asia-south1 ` region (Mumbai, India). 

##  October 11, 2017

**FEATURE:**

  * Announced general availability of [ App Engine firewall ](https://cloud.google.com/appengine/docs/flexible/python/creating-firewalls?hl=pt-br) . 

##  October 04, 2017

**FEATURE:**

  * The App Engine flexible environment now defaults to Python 3.6 when Python 3 is requested. Update your [ Cloud SDK ](https://cloud.google.com/sdk/gcloud/reference/components/update?hl=pt-br) to version 174.0.0 or later to use this new default. To revert to Python 3.5, specify ` python_version: 3.5 ` in the ` runtime_config ` element of your [ ` app.yaml ` configuration file ](https://cloud.google.com/appengine/docs/flexible/python/configuring-your-app-with-app-yaml?hl=pt-br)

##  October 02, 2017

**FEATURE:**

  * For the App Engine flexible environment, all responses are now compressed with gzip by default once you redeploy your app. No changes need to be made to your ` app.yaml ` file. 

##  September 26, 2017

**FEATURE:**

  * For the App Engine flexible environment, billing increments for instances are reduced from per-minute increments to per-second increments. Additionally, the minimum usage cost for instance resources is reduced from 10 minutes to 1 minute. 

##  September 18, 2017

**FEATURE:**

  * [ Updated health checks ](https://cloud.google.com/appengine/docs/flexible/python/reference/app-yaml?hl=pt-br#updated_health_checks) are now the default for new projects. To upgrade a project from legacy health checks, run the command ` gcloud app update --split-health-checks ` . 

**DEPRECATED:**

Legacy health checks will no longer be available after September 30th, 2018.

##  September 13, 2017

**FEATURE:**

  * You can now use managed certificates to add SSL to your custom domain. Once you map your custom domain to your application, App Engine provisions an SSL certificate automatically and handles renewing the certificate before it expires and revoking it if you remove the custom domain. Managed certificates are in beta. For more information, see [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/flexible/python/securing-custom-domains-with-ssl?hl=pt-br) . 

**FEATURE:**

  * If you have an existing domain mapping and SSL certificate, then it continues to function as expected. You can also [ upgrade to managed SSL certificates ](https://cloud.google.com/appengine/docs/flexible/python/securing-custom-domains-with-ssl?hl=pt-br#updating_to_managed_ssl_certificates) . 

**FEATURE:**

  * The ` gcloud ` commands and Admin API methods used to [ map custom domains ](https://cloud.google.com/appengine/docs/flexible/python/mapping-custom-domains?hl=pt-br) are now generally available. This includes [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains/?hl=pt-br) and [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=pt-br) . However, if you want to use managed SSL certificates, use the beta commands and methods that are specified in [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/flexible/python/securing-custom-domains-with-ssl?hl=pt-br) . 

##  September 05, 2017

**FEATURE:**

  * App Engine is now available in the ` southamerica-east1 ` region (São Paulo, Brazil). 

##  August 25, 2017

**FEATURE:**

  * The Python 3.5 runtime is now updated to version [ 3.5.4 ](https://docs.python.org/3.5/whatsnew/changelog.html#python-3-5-4-final) . This includes some security and bug fixes. 

##  August 23, 2017

**FEATURE:**

  * Beta release of the [ App Engine firewall ](https://cloud.google.com/appengine/docs/flexible/python/creating-firewalls?hl=pt-br) . 

##  August 01, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west3 ` region (Frankfurt, Germany). 

##  July 25, 2017

**FEATURE:**

  * The Python 3.6 runtime is now updated to version [ 3.6.2 ](https://docs.python.org/3/whatsnew/changelog.html#python-3-6-2) . This includes some security and bug fixes. 

##  July 18, 2017

**FEATURE:**

  * App Engine is now available in the ` australia-southeast1 ` region (Sydney, Australia). 

##  July 12, 2017

**FEATURE:**

  * You can now use updated health checks, which allow you to use separate checks to confirm that your instance is running and ready to serve content. You must enable updated health checks, which are currently in Beta. For more information, see [ Health checks ](https://cloud.google.com/appengine/docs/flexible/python/configuring-your-app-with-app-yaml?hl=pt-br#health_checks) . 

**FEATURE:**

  * If you use updated health checks, deployments will fail if your application does not reach a ready state. 

##  June 06, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west2 ` region (London). 

**FEATURE:**

  * You can now use the beta-level features in the Admin API and ` gcloud ` command-line tool to [ create and manage your custom domains and SSL certificates ](https://cloud.google.com/appengine/docs/flexible/python/using-custom-domains-and-ssl?hl=pt-br) . 

##  May 24, 2017

**FEATURE:**

  * The flexible environment now includes Python 3.6 support (Beta). To use the Python 3.6 runtime, specify ` python_version: 3.6 ` in the ` runtime_config ` element of your [ ` app.yaml ` configuration file ](https://cloud.google.com/appengine/docs/flexible/python/configuring-your-app-with-app-yaml?hl=pt-br) . 

##  May 09, 2017

**FEATURE:**

  * App Engine is now available in the ` us-east4 ` region (North Virginia). 

##  April 11, 2017

**FEATURE:**

  * Added [ information ](https://cloud.google.com/appengine/docs/flexible/python/upgrading?hl=pt-br) about upgrading from the App Engine Task Queue API in the compat runtimes to using Cloud Tasks in the flexible environment and added information for how to verify requests from the Task Queue API. 

##  March 28, 2017

**FEATURE:**

  * The flexible environment is now available in the [ ` europe-west ` region ](https://cloud.google.com/appengine/docs/locations?hl=pt-br) . 

##  March 09, 2017

**FEATURE:**

  * The App Engine flexible environment is now generally available (GA). You can run Node.js, Ruby, Python, Java, and Go applications with a [ 99.95% SLA ](https://cloud.google.com/appengine/sla?hl=pt-br) . 

**FEATURE:**

  * The [ PHP 7 runtime ](https://cloud.google.com/appengine/docs/flexible/php/?hl=pt-br) for the App Engine flexible environment is now in Beta. 

**FEATURE:**

  * The [ .NET core runtime ](https://cloud.google.com/appengine/docs/flexible/dotnet/?hl=pt-br) for the App Engine flexible environment is now in Beta. 

##  December 06, 2016

**FEATURE:**

  * New applications that have not been deployed in the flexible environment must specify ` env: true ` in the ` app.yaml ` file instead of ` vm:true ` . Applications that were previously deployed can continue to use ` vm:true ` but will need to switch to ` env:true ` in the future. For more details, see [ upgrade guide ](https://cloud.google.com/appengine/docs/flexible/python/upgrading?hl=pt-br) . 

##  December 05, 2016

**FEATURE:**

  * Python support updated from version 3.4 to version 3.5 for flexible environment apps that specify using the latest version of the Python runtime ( ` python_version: 3 ` ). Apps can specifically target this version by specifying ` python_version: 3.5 ` in their [ ` app.yaml ` configuration file (/appengine/docs/flexible/python/configuring-your-app-with-app-yaml). 

##  November 15, 2016

**FEATURE:**

There is a new release of the App Engine flexible environment. To choose this
environment, use ` env:flex ` instead of ` vm:true ` in your ` app.yaml `
configuration file. You can learn more about the details of this release by
visiting the [ upgrade guide
](https://cloud.google.com/appengine/docs/flexible/python/upgrading?hl=pt-br)
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
](https://cloud.google.com/appengine/docs/flexible/python/upgrading?hl=pt-br)
.

##  May 02, 2016

**FEATURE:**

  * The [ Ruby runtime ](https://cloud.google.com/appengine/docs/flexible/ruby/?hl=pt-br) is now available for the App Engine flexible environment. 

##  March 24, 2016

**FEATURE:**

  * App Engine Managed VMs is renamed to [ App Engine flexible environment ](https://cloud.google.com/appengine/docs/flexible/?hl=pt-br) . 

##  February 03, 2016

**FEATURE:**

  * Container construction choices for Managed VMs 

The ` gcloud preview app deploy ` (and ` mvn gcloud:deploy ` ) commands upload
your artifacts to our servers and build a container to deploy your app to the
Managed VM environment.

There are two mechanisms for building the container image remotely. The
default behavior is to build the container on a transient Compute Engine
Virtual Machine which has Docker installed. Alternatively, you can use the [
Cloud Build ](https://cloud.google.com/cloud-build/docs/?hl=pt-br) service,
which is in Beta. To use the Cloud Build service, follow these steps:

    1. [ Activate the Cloud Build API ](https://support.google.com/cloud/answer/6158841?hl=pt-br) for your project. 
    2. Use the command ` gcloud config set app/use_cloud_build True ` . This will cause all invocations of ` gcloud preview app deploy ` to use the service. To return to the default behavior, use the command ` gcloud config set app/use_cloud_build False ` . 

