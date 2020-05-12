Python 2 不再受社区支持。我们建议您 [ 将 Python 2 应用迁移到 Python 3
](https://cloud.google.com/appengine/docs/standard/python/migrate-to-
python3/?hl=zh-cn) 。

#  Python 2.7 版本说明

如需接收最新产品动态，请将此页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接添加 Feed 网址： `
https://cloud.google.com/feeds/gaestd-py-release-notes.xml `

##  May 11, 2020

**CHANGED:**

Updated Python SDK to version 1.9.91.

##  April 20, 2020

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

##  April 13, 2020

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data your Python 2 app can send and
receive through a socket.

##  April 08, 2020

**CHANGED:**

Updated Python SDK to version 1.9.90

##  March 25, 2020

**CHANGED:**

Updated Python SDK to version 1.9.89.

##  March 13, 2020

**FEATURE:**

App Engine is now available in the ` asia-northeast3 ` region (Seoul).

##  March 06, 2020

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

##  March 05, 2020

**CHANGED:**

Updated Python SDK to version 1.9.89.

##  February 11, 2020

**FEATURE:**

App Engine is changing the URLs that you use to send requests to your apps.
You can now [ include a region ID
](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-
routed?hl=zh-cn#region-id) to help Google route your requests more efficiently
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

  * You can no longer apply new spending limits to projects. Existing spending limits will continue to work. For more information on how you can limit app costs, see [ Limiting Costs ](https://cloud.google.com/appengine/docs/managing-costs?hl=zh-cn) . 

##  December 11, 2019

**FEATURE:**

  * [ Serverless VPC Access ](https://cloud.google.com/appengine/docs/standard/python/connecting-vpc?hl=zh-cn) is now GA. 

##  October 30, 2019

**FEATURE:**

  * Updated Python SDK to version 1.9.87. 

##  July 30, 2019

**DEPRECATED:**

  * The AppCfg tooling and the legacy standalone App Engine SDK, delivered through the ` GoogleAppEngineLauncher.dmg ` , ` GoogleAppEngine.msi ` , and ` google_appengine.zip ` files, are now deprecated. Google will shut down and remove support on July 30, 2020. 

**FEATURE:**

  * The functionalities of the App Engine SDK is delivered exclusively through [ Cloud SDK ](https://cloud.google.com/sdk/docs?hl=zh-cn) . For more information, see [ Migrating to Cloud SDK ](https://cloud.google.com/appengine/docs/standard/python/sdk-gcloud-migration?hl=zh-cn) . 

##  June 03, 2019

**FEATURE:**

  * Updated Python SDK to version 1.9.86. 

##  April 18, 2019

**FEATURE:**

  * App Engine is now available in the ` asia-northeast2 ` region (Osaka, Japan). 

##  April 15, 2019

**FEATURE:**

  * App Engine is now available in the ` europe-west6 ` region (Zürich, Switzerland). 

##  April 09, 2019

**FEATURE:**

  * [ Serverless VPC Access ](https://cloud.google.com/appengine/docs/standard/python/connecting-vpc?hl=zh-cn) is now in beta. Serverless VPC Access enables your app to connect to internal resources in your VPC network, such as Compute Engine VM instances, Memorystore instances, and more. 

##  March 28, 2019

**FEATURE:**

  * Updated Python SDK to version 1.9.85. 

##  March 05, 2019

**FEATURE:**

  * Updated Python SDK to version 1.9.84. 

##  February 13, 2019

**FEATURE:**

  * Updated Python SDK to version 1.9.83. 

##  January 17, 2019

**FEATURE:**

  * Updated Python SDK to version 1.9.82. 

##  January 11, 2019

**FEATURE:**

  * The Python 3 runtime has been updated to version 3.7.2. 

##  January 02, 2019

**FEATURE:**

  * Updated Python SDK to version 1.9.88. 

##  December 21, 2018

**FEATURE:**

  * Added ` select ` , ` mmap ` , ` grp ` , ` fcntl ` , ` spwd ` modules to the Python interpreter. 

**FEATURE:**

  * Added ` fork ` , ` waitpid ` , ` chown ` , ` execv ` , ` fchmod ` , ` fchown ` , ` ftruncate ` , ` kill ` , ` lchown ` , ` lstat ` , ` readline ` , ` setuid ` functions to the ` os ` module. 

##  December 14, 2018

**FEATURE:**

  * The [ Python 3.7 runtime ](https://cloud.google.com/appengine/docs/standard/python3/?hl=zh-cn) for the App Engine standard environment is now GA. 

##  December 12, 2018

**FEATURE:**

  * Updated Python SDK to version 1.9.81. 

**FEATURE:**

  * All apps have been switched to BSD network sockets. No changes to apps are required. 

**FEATURE:**

  * The [ Sockets API ](https://cloud.google.com/appengine/docs/standard/python/sockets/?hl=zh-cn) is now GA. 

##  November 16, 2018

**CHANGED:**

  * nginx is now the default web server. No changes to apps are required. 

##  November 08, 2018

**FEATURE:**

  * Updated Python SDK to version 1.9.80. 

**FIXED:**

  * Minor bug fixes. 

##  October 31, 2018

**FEATURE:**

  * The Python 3 runtime has been updated to Python version 3.7.1. 

**FEATURE:**

  * The Python 3 runtime supports recursive entries in the ` requirements.txt ` file. 

##  October 25, 2018

**FEATURE:**

  * Updated Python SDK to version 1.9.78. 

**FIXED:**

  * Minor bug fixes. 

##  October 22, 2018

**FEATURE:**

  * App Engine is now available in the ` asia-east2 ` region (Hong Kong). 

##  October 15, 2018

**FEATURE:**

  * All apps on the Python 2.7 runtime now run in the [ gVisor sandbox ](https://github.com/google/gvisor) . 
  * App Engine is now available in the ` asia-east2 ` region (Hong Kong). 

**FEATURE:**

  * All Python 2.7 apps now run on 64-bit Python interpreter. 

##  October 04, 2018

**FEATURE:**

  * Updated Python SDK to version 1.9.77. 

##  September 26, 2018

**FEATURE:**

  * Updated Python SDK to version 1.9.76. 

**FEATURE:**

  * Allow using locally installed ` grpcio ` as a workaround for import failures on dev_appserver. 

##  September 05, 2018

**FEATURE:**

  * Updated Python SDK to version 1.9.75. 

**FEATURE:**

  * Started rolling out [ Cloud Datastore Emulator ](https://cloud.google.com/appengine/docs/standard/python/tools/migrate-cloud-datastore-emulator?hl=zh-cn) as the default local datastore emulation when using the ` dev_appserver ` local development server. 

##  August 24, 2018

**DEPRECATED:**

**Shutdown of Cloud Endpoints Frameworks v1 is approaching**

Cloud Endpoints Frameworks v1 for the App Engine standard environment was
deprecated on August 2, 2017. The [ service is scheduled to be shutdown
](https://cloud.google.com/appengine/docs/deprecations/endpoints-v1?hl=zh-cn)
on September 3, 2018, and the documentation will be removed. To avoid an
outage, you must migrate your v1 application. For information on migrating
your application to Endpoints Frameworks v2, see the [ Python Migration Guide
](https://cloud.google.com/endpoints/docs/frameworks/python/migrating?hl=zh-
cn) .

##  August 14, 2018

**FEATURE:**

  * Updated Python SDK to version 1.9.74. 

**FIXED:**

  * Minor bug fixes. 

##  August 08, 2018

**FEATURE:**

  * The [ Python 3.7 runtime ](https://cloud.google.com/appengine/docs/standard/python3/?hl=zh-cn) for the App Engine standard environment is now in beta. 

**FEATURE:**

  * A list of [ differences between Python 2.7 and Python 3.7 runtimes ](https://cloud.google.com/appengine/docs/standard/python3/python-differences?hl=zh-cn) is available. 

##  July 12, 2018

**FEATURE:**

  * Updated Python SDK to version 1.9.73. 

**FIXED:**

  * Fix a crush that happened when dev_appserver speaked to a running Cloud Datastore Emulator. Previously, the crush happened when the environment variable "DATASTORE_PROJECT_ID" existed in the shell that ran dev_appserver. 

**FEATURE:**

  * The [ local development server ](https://cloud.google.com/appengine/docs/standard/go/tools/using-local-server?hl=zh-cn) now prints the process ID of the running process on startup. You can use the process ID when debugging your app. 

##  July 10, 2018

**FEATURE:**

  * App Engine is now available in the ` us-west2 ` region (Los Angeles). 

##  July 02, 2018

**FIXED:**

Fixed a bug in [ auto scaling configuration
](https://cloud.google.com/appengine/docs/standard/python/config/appref?hl=zh-
cn#scaling_elements) where App Engine was aggressively shutting down instances
when the ` max_instances ` setting was used.

##  June 28, 2018

**FEATURE:**

  * Updated Python SDK to version 1.9.72. 

**FEATURE:**

  * Purged the ` DATASTORE_PROJECT_ID ` environment variable from the local development server ( ` dev_appserver ` ) process. Now ` dev_appserver ` can run alongside the Cloud Datastore Emulator. 

**FEATURE:**

  * The local development server will now print the process ID of the app process on startup. 

##  June 21, 2018

**FEATURE:**

  * Updated Python SDK to version 1.9.71. 

**FIXED:**

  * Minor bug fixes. 

##  May 24, 2018

**FEATURE:**

  * Migrated SSL library from version 2.7 to version 2.7.11 for all apps. See the [ Python SSL version 2.7 shutdown docs ](https://cloud.google.com/appengine/docs/deprecations/python-ssl-27?hl=zh-cn) for details. 

##  May 17, 2018

**FEATURE:**

  * Updated Python SDK to version 1.9.70. 

**FIXED:**

  * Minor bug fixes. 

##  May 15, 2018

**FEATURE:**

  * Completed a gradual rollout of an upgrade to the automatic scaling system: 
    * Improved efficiency resulting generally in lower instance cost (up to 6% reduction for many users) and up to 30% reduction for _loading requests_ , which are the first request to a new instance. 
    * New max instances setting allows you to cap the total number of instances to be scheduled. 
    * New min instances setting allows you to specify a minimum number of instance to keep running for your app. 
    * New target CPU utilization setting lets you optimize between latency and cost. 
    * New target throughput utilization setting lets you optimize for the number of concurrent requests at which new instances are started. 
    * No more resident instances in auto scaling. Previously, if you used the ` min_idle_instances ` setting, the minimum idle instances were labelled as _Resident_ in the Cloud Console, with the remainder of the instances labelled as _Dynamic_ . The new scheduler simply labels all instances as _Dynamic_ with auto scaling. However, the underlying behavior remains similar to previous behavior. If you use ` min_idle_instances ` and enable warmup requests, you will see at least that many dynamic instances running even during periods with no traffic. 
    * For more details, see the [ auto scaling documentation ](https://cloud.google.com/appengine/docs/standard/python/config/appref?hl=zh-cn#scaling_elements) . 

##  April 11, 2018

**FEATURE:**

**Python runtime notes**

**FEATURE:**

  * Updated Python SDK to version 1.9.69. 

**FEATURE:**

  * Added [ PyTz version 2017.3 ](https://pypi.python.org/pypi/pytz/2017.3) to the built-in third-party libraries. 

##  April 03, 2018

**FEATURE:**

**Python runtime notes**

  * Updated Python SDK to version 1.9.68. 

**FIXED:**

  * Minor bug fixes. 

##  February 14, 2018

**FEATURE:**

**Python runtime notes**

  * Updated Python SDK to version 1.9.67. 

##  January 23, 2018

**FEATURE:**

  * Updated Python SDK to 1.9.66. 

**FIXED:**

  * Fixes the [ ` ipaddr ` library import issue ](https://issuetracker.google.com/issues/71704025?hl=zh-cn) when starting PHP app with the local development server. 

##  December 20, 2017

**FEATURE:**

**Python runtime notes**

**FEATURE:**

  * Updated Python SDK to version 1.9.65. 

**FEATURE:**

  * Added [ SetupTools version 36.6.0 ](https://pypi.python.org/pypi/setuptools/36.6.0) to the built-in third-party libraries. 

##  December 14, 2017

**FEATURE:**

  * Improved access control documentation around deploying apps with IAM roles and service accounts: 

    * [ Predefined App Engine roles ](https://cloud.google.com/appengine/docs/standard/python/access-control?hl=zh-cn#predefined_app_engine_roles)
    * [ Deploying using IAM roles ](https://cloud.google.com/appengine/docs/standard/python/granting-project-access?hl=zh-cn#deploying_using_iam_roles)
    * [ Require permissions ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=zh-cn#required_permissions)

##  December 09, 2017

**ISSUE:**

**Known problem** : [ Werkzeug 0.13 update adds a module that is not supported
by App Engine ](https://issuetracker.google.com/issues/70426718?hl=zh-cn) that
results in a ` ImportError: cannot import name SpooledTemporaryFile ` error.
You can downgrade or pin your app to an earlier version of werkzeug to fix the
error. See the linked issue for details.

##  December 05, 2017

**FEATURE:**

**Python runtime notes**

**FEATURE:**

  * Updated Python SDK to version 1.9.64. 

**FEATURE:**

  * For all incoming HTTP requests, ` dev_appserver.py ` now requires that all HTTP requests must have an HTTP ` Host ` header and its value is either ` localhost ` , an IPv4 or IPv6 loopback address, or if specified, the value passed in via ` --host ` . For HTTP/1.0 only, requests with no ` Host ` header are still allowed. To disable host checking, set the ` --enable_host_checking ` flag to ` false ` . However, it is strongly recommended to leave host checking enabled, as it guards against DNS rebinding attacks. 

**FEATURE:**

  * Introduced additional security-header related behavior to the ` dev_appserver.py ` admin console: 
    * Inbound requests containing an ` Origin ` header are rejected. 
    * Added the following headers to all responses: 
      * ` X-Frame-Options=SAMEORIGIN `
      * ` X-XSS-Protection=1; mode=block `
      * ` Content-Security-Policy=default-src 'self'; frame-ancestors 'none' `

##  November 15, 2017

**FEATURE:**

**Python runtime notes**

**FEATURE:**

  * Updated Python SDK to version 1.9.63. 

**DEPRECATED:**

  * Announced the [ deprecation of the Python SSL library version 2.7 ](https://cloud.google.com/appengine/docs/deprecations/python-ssl-27?hl=zh-cn) . Applications should migrate to use SSL version 2.7.11. 

**FEATURE:**

  * Updates within the Python SDK to support the [ Go SDK ](https://cloud.google.com/appengine/docs/standard/go/release-notes?hl=zh-cn#november_15_2017) . 

##  October 31, 2017

**FEATURE:**

  * App Engine is now available in the ` asia-south1 ` region (Mumbai, India). 

##  October 25, 2017

**FEATURE:**

**Python runtime notes**

  * Updated Python SDK to version 1.9.62 

**FIXED:**

  * Minor bug fixes 

##  October 11, 2017

**FEATURE:**

  * Announced general availability of [ App Engine firewall ](https://cloud.google.com/appengine/docs/standard/python/creating-firewalls?hl=zh-cn) . 

##  September 21, 2017

**FEATURE:**

**Python runtime notes**

**FEATURE:**

  * Updated Python SDK to version 1.9.61 

**FEATURE:**

  * Updated ` pytz ` to 2017.2 

##  September 13, 2017

**FEATURE:**

  * You can now use managed certificates to add SSL to your custom domain. Once you map your custom domain to your application, App Engine provisions an SSL certificate automatically and handles renewing the certificate before it expires and revoking it if you remove the custom domain. Managed certificates are in beta. For more information, see [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/standard/python/securing-custom-domains-with-ssl?hl=zh-cn) . 

**FEATURE:**

  * If you have an existing domain mapping and SSL certificate, then it continues to function as expected. You can also [ upgrade to managed SSL certificates ](https://cloud.google.com/appengine/docs/standard/python/securing-custom-domains-with-ssl?hl=zh-cn#updating_to_managed_ssl_certificates) . 

**FEATURE:**

  * The ` gcloud ` commands and Admin API methods used to [ map custom domains ](https://cloud.google.com/appengine/docs/standard/python/mapping-custom-domains?hl=zh-cn) are now generally available. This includes [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains/?hl=zh-cn) and [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=zh-cn) . However, if you want to use managed SSL certificates, use the beta commands and methods that are specified in [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/standard/python/securing-custom-domains-with-ssl?hl=zh-cn) . 

##  September 05, 2017

**FEATURE:**

  * App Engine is now available in the ` southamerica-east1 ` region (São Paulo, Brazil). 

**FEATURE:**

**Python runtime notes**

**FEATURE:**

  * Updated Python SDK to version 1.9.60 

**FIXED:**

  * Release includes minor bug fixes. 

##  August 30, 2017

**FEATURE:**

  * Updated Python SDK to version 1.9.59 

##  August 28, 2017

**FEATURE:**

  * Updated Python SDK to version 1.9.58 

**FEATURE:**

  * This release adds client support for gRPC so that you can connect to gRPC servers from your App Engine application. For more information on how to request and install the ` grpcio ` library, see [ Using third-party libraries ](https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27?hl=zh-cn) . 

**CHANGED:**

  * This release does not include support for [ Google Cloud Client Libraries ](https://googleapis.github.io/google-cloud-python/) or for gRPC server requests. 

##  August 01, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west3 ` region (Frankfurt, Germany). 

##  July 18, 2017

**FEATURE:**

  * App Engine is now available in the ` australia-southeast1 ` region (Sydney, Australia). 

##  July 01, 2017

**FEATURE:**

  * Updated Python SDK to version 1.9.57 

##  June 27, 2017

**FEATURE:**

  * Updated Python SDK to version 1.9.56. 

**FEATURE:**

  * Added Django v1.11 to the [ built-in third-party libraries ](https://cloud.google.com/appengine/docs/standard/python/tools/built-in-libraries-27?hl=zh-cn) . 

##  June 21, 2017

**FEATURE:**

  * Updated Python SDK to version 1.9.55. 

**FEATURE:**

  * Added the following new libraries to the [ built-in third party libraries ](https://cloud.google.com/appengine/docs/standard/python/tools/built-in-libraries-27?hl=zh-cn) : 

    * ujson v1.35 
    * lxml v3.7.3 
    * flask v0.12. 

**FEATURE:**

  * Search API: increased the maximum [ facet discovery value limit ](https://cloud.google.com/appengine/docs/standard/python/refdocs/google.appengine.api.search.search?hl=zh-cn#google.appengine.api.search.search.FacetOptions) to 100. 

##  June 15, 2017

**FEATURE:**

  * For MySQLdb, you can now use the ` utf8mb4 ` character set. 

**FEATURE:**

  * For SSL ` 2.7.11 ` , if you don't specify the certificate root path, the default is set to ` /etc/ca-certificates.crt ` . 

**FEATURE:**

  * You can use the [ PWD module ](https://docs.python.org/2/library/pwd.html) for the Unix password database. 

##  June 06, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west2 ` region (London). 

**FEATURE:**

  * You can now use the beta-level features in the Admin API and ` gcloud ` command-line tool to [ create and manage your custom domains and SSL certificates ](https://cloud.google.com/appengine/docs/standard/python/mapping-custom-domains?hl=zh-cn) . 

##  May 22, 2017

**FEATURE:**

  * Updated Python SDK to version 1.9.54. 

**FEATURE:**

  * Updated the Python SDK to be based on Python 2.7.12. 

##  May 15, 2017

**FEATURE:**

  * Updated the Python runtime to Python 2.7.12. 

**FEATURE:**

  * Modified the SSL certificate validation behavior in the SSL module versioned as ` 2.7.11 ` to not validate certificates. This behavior can be controlled by an [ environment variable ](https://cloud.google.com/appengine/docs/standard/python/config/appref?hl=zh-cn#environment_variables) ` PYTHONHTTPSVERIFY ` , which can be set to ` 1 ` to require certificate validation. 

**FEATURE:**

  * To ensure application compatibility, removed the fix for [ https://bugs.python.org/issue22221 ](https://bugs.python.org/issue22221) for the tokenizer, which would ensure PEP-263 is correctly handled. 

##  May 09, 2017

**FEATURE:**

  * App Engine is now available in the ` us-east4 ` region (North Virginia). 

##  April 27, 2017

**FEATURE:**

  * Updated Python SDK to version 1.9.53. 

**FEATURE:**

  * In preparation for the Go 1.8 beta, Go ` api_version ` s are mapped to specific ` GOROOT ` directories. 

##  April 05, 2017

**FEATURE:**

  * Updated Python SDK to version 1.9.52. 

**FIXED:**

  * Fixed a bug preventing Server Name Indication (SNI) from working for remote API shell. 

##  March 20, 2017

**FEATURE:**

  * Updated Python SDK to version 1.9.51. 

**FEATURE:**

  * Support Server Name Indication (SNI) for remote API shell. 

##  January 23, 2017

**FEATURE:**

  * Updated Python SDK to version 1.9.50. 

**FIXED:**

  * Fixed a bug that caused the ` remote_api_shell.py ` tool to not work on Cloud Shell. 

##  December 01, 2016

**FEATURE:**

  * Updated Python SDK to version 1.9.49. 

**FEATURE:**

  * Includes pycrypto update to 2.6.1. 

**FEATURE:**

  * Includes pytz update to 2016.4. 

##  October 27, 2016

**DEPRECATED:**

  * The Channel and XMPP services are now [ deprecated ](https://cloud.google.com/appengine/docs/deprecations/?hl=zh-cn) . These services will be turned down on October 31, 2017. 

##  August 01, 2016

**FEATURE:**

**Admin API notes**

  * Version 1 of the [ Admin API ](https://cloud.google.com/appengine/docs/admin-api/?hl=zh-cn) is now generally available. 

**FEATURE:**

Version 1.9.42

######  #####END

######  ######START

2016-08-01

FEATURE

**Python 2 runtime notes**

  * This release does not include a new Python 2 SDK. Python 2 users should continue to use the 1.9.40 SDK. 

##  July 26, 2016

**FEATURE:**

**Python 2 runtime notes**

SSL 2.7.11 is now available by default to all apps. If ` version: 2.7 ` or `
version: latest ` is specified for the ` ssl ` library in the ` app.yaml `
configuration file, apps will get the 2.7 version. [ More information about
using built-in libraries
](https://cloud.google.com/appengine/docs/standard/python/tools/using-
libraries-python-27?hl=zh-cn#requesting_a_library) .

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

  * New [ App Engine guided walkthrough ](https://console.cloud.google.com/start/appengine?hl=zh-cn) in the Cloud Console. Pick your preferred language and launch an interactive tutorial directly in the console. 

**FEATURE:**

  * Increases the maximum cron tasks limit to 250. 

**FEATURE:**

**Python runtime notes**

  * Python Endpoints accepts all valid Google ID token issuers. 

##  July 01, 2016

**FEATURE:**

**Cloud Datastore**

  * New [ Cloud Datastore Pricing ](https://cloud.google.com/appengine/pricing?hl=zh-cn#costs-for-datastore-calls) is now in effect. 

##  May 25, 2016

**FEATURE:**

Version 1.9.38

**FEATURE:**

  * The error returned by URL Fetch for a request to a port outside of the permitted ranges (80-90, 440-450, 1024-65535) will now always return ` INVALID_URL ` as documented. 

**FEATURE:**

**Cloud Datastore**

  * When committing a cross-group transaction, version numbers returned for new or updated entities are all the same. With the previous behavior, entities within the same group committed as part of a cross-group transaction, had the same version number, but entities in different groups might have had different version numbers. This change ensures all new and updated entities have an identical version number, regardless of their entity group, when committed as part of a cross-group transaction. As before, entities that are not updated will not have a new version number. 

##  May 04, 2016

**FEATURE:**

Version 1.9.37

**FIXED:**

Includes general bug fixes and improvements.

**FEATURE:**

**Python runtime notes**

  * Includes a new version of the third_party library "ssl" based on Python 2.7.11. The library can be selected with version: "2.7.11" in the [ ` libraries ` ](https://cloud.google.com/appengine/docs/standard/python/config/appref?hl=zh-cn#libraries) section of the ` app.yaml ` file. 

##  May 02, 2016

**FEATURE:**

**App Engine flexible environment**

  * The [ Ruby runtime ](https://cloud.google.com/appengine/docs/flexible/ruby/?hl=zh-cn) is now available for the App Engine flexible environment. 

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

**Python runtime notes**

  * Google no longer accepts quota increase requests for the mail service. Customers should use [ Sendgrid ](https://cloud.google.com/appengine/docs/standard/python/mail/sendgrid?hl=zh-cn) instead. 

##  March 24, 2016

**FEATURE:**

Version 1.9.35

**CHANGED:**

  * App Engine Managed VMs is renamed to [ App Engine flexible environment ](https://cloud.google.com/appengine/docs/flexible/?hl=zh-cn) . 

**FIXED:**

  * Fixes trace timestamps to match log timestamps. 

##  March 04, 2016

**FEATURE:**

Version 1.9.34

**FEATURE:**

  * Increases default quota for URL fetch for billed apps. Refer to the [ Quotas page ](https://cloud.google.com/appengine/docs/quotas?hl=zh-cn#UrlFetch) for details. 

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
Cloud Build ](https://cloud.google.com/cloud-build/docs/?hl=zh-cn) service. To
use the Cloud Build service, follow these steps:

    1. [ Activate the Cloud Build API ](https://support.google.com/cloud/answer/6158841?hl=zh-cn) for your project. 
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

**Python runtime notes**

  * Stackdriver Debugger is enabled automatically for Python applications running on App Engine. [ Try it ](https://cloud.google.com/debugger/docs/setting-up-python-on-app-engine?hl=zh-cn) . 

**FEATURE:**

Version 1.9.29

**FEATURE:**

  * Stop calculating and storing queue depth for non-existent queues, queues marked for deletion, and in the case of queue table outages. 

**FEATURE:**

  * For developers using the [ endpoints API ](https://cloud.google.com/appengine/docs/standard/python/endpoints/create_api?hl=zh-cn#defining_the_api_endpointsapi) , added a discoverable boolean parameter to the @Api annotation to allow users to disable API discovery. Using this feature will prevent some client libraries (e.g. JavaScript) and the API Explorer from working, as they depend on discovery. 

##  October 29, 2015

**FEATURE:**

Version 1.9.28

**BREAKING:**

The Prospective Search API, which was deprecated on July 14, 2015, is now
restricted to existing users. It will fully shutdown on December 1, 2015. *
Improved accuracy of Geo filtering in Search queries.

**FEATURE:**

**Python runtime notes**

  * Allow use of quoted numbers within comparison clauses of Search queries. [ https://issuetracker.google.com/issues/35899722 ](https://issuetracker.google.com/issues/35899722?hl=zh-cn)

##  September 25, 2015

**FEATURE:**

Version 1.9.27

**FEATURE:**

Applications that are newly enabled for billing now default to an unlimited
daily budget, and no longer default to a maximum daily budget of $0. This
prevents unwanted outages due to running out of budget. To set a ceiling on
your application's daily cost, after you enable billing, set a budget in the [
app engine settings
](https://console.cloud.google.com/project/_/appengine/settings?hl=zh-cn) .
For more information, see [ Setting a daily budget
](https://cloud.google.com/appengine/docs/developers-console/?hl=zh-
cn#setting_a_daily_budget) .

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

