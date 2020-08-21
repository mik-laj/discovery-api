#  Notas de la versión de Java

Puedes ver las actualizaciones más recientes de todos los productos de Google
Cloud en la página de [ notas de la versión de Google Cloud
](https://cloud.google.com/release-notes?hl=es-419) .

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , o agrega
directamente la URL del feed: ` https://cloud.google.com/feeds/gaestd-java-
release-notes.xml `

##  August 20, 2020

**CHANGED:**

Updated Java SDK to version 1.9.82.

##  July 23, 2020

**FEATURE:**

[ Serverless VPC Access support for Shared VPC
](https://cloud.google.com/appengine/docs/standard/java/connecting-
vpc?hl=es-419#shared-vpc) is now available in Beta.

##  July 17, 2020

**CHANGED:**

  * Updated Java SDK to version 1.9.81 

##  July 08, 2020

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs?hl=es-419) . Notably, this
feature allows you to use [ Cloud CDN
](https://cloud.google.com/cdn?hl=es-419) with App Engine.  
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
](https://cloud.google.com/appengine/docs/standard/java/labeling-
resources?hl=es-419) .

##  April 20, 2020

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**CHANGED:**

  * Updated Java SDK to Version 1.9.80 
  * Fixed deployment of cron.yaml file with retry_parameters configured 
  * Fixed class LocalTaskQueueTestConfig to support custom paths for queue.yaml files ( [ public issue 138528920 ](https://issuetracker.google.com/138528920?hl=es-419) ) 

##  April 13, 2020

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data your Java 8 app can send and
receive through a socket.

##  March 20, 2020

**CHANGED:**

  * Updated Java SDK to version 1.9.79. 
  * Updated Jetty to version 9.4.27. 

##  March 13, 2020

**FEATURE:**

App Engine is now available in the ` asia-northeast3 ` region (Seoul).

##  March 06, 2020

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

##  February 06, 2020

**DEPRECATED:**

  * You can no longer apply new spending limits to projects. Existing spending limits will continue to work. For more information on how you can limit app costs, see [ Limiting Costs ](https://cloud.google.com/appengine/docs/managing-costs?hl=es-419) . 

##  December 11, 2019

**FEATURE:**

  * [ Serverless VPC Access ](https://cloud.google.com/appengine/docs/standard/java/connecting-vpc?hl=es-419) is now GA. 

##  December 07, 2019

**FEATURE:**

  * Updated Java SDK to version 1.9.77. 

**FEATURE:**

  * Upgrade Jarkata Jasper JSP compiler to version 9.0.24. 

##  October 17, 2019

**FEATURE:**

  * The [ Java 11 runtime ](https://cloud.google.com/appengine/docs/standard/java11/runtime?hl=es-419) for the App Engine standard environment is now GA. 

##  July 30, 2019

**DEPRECATED:**

  * The AppCfg tooling and the legacy standalone App Engine SDK, delivered through the ` GoogleAppEngineLauncher.dmg ` , ` GoogleAppEngine.msi ` , and ` google_appengine.zip ` files, are now deprecated. Google will shut down and remove support on July 30, 2020. 

**FEATURE:**

  * The functionalities of the App Engine SDK is delivered exclusively through [ Cloud SDK ](https://cloud.google.com/sdk/docs?hl=es-419) . For more information, see [ Migrating to Cloud SDK ](https://cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration?hl=es-419) . 

##  June 24, 2019

**FEATURE:**

  * Updated Java SDK to version 1.9.76. 

##  June 05, 2019

**FEATURE:**

  * The [ Java 11 runtime ](https://cloud.google.com/appengine/docs/standard/java11/runtime?hl=es-419) for the App Engine standard environment is now Beta. 

##  June 03, 2019

**FEATURE:**

  * Updated Java SDK to version 1.9.75. 

**FEATURE:**

  * The Google App Engine API jar is now compiled as a Java 8 target. 

**FIXED:**

  * Fixed performance issue for large batch GETs from Memcache. 

##  April 30, 2019

**FEATURE:**

  * Updated Java SDK to version 1.9.74. 

##  April 18, 2019

**FEATURE:**

  * App Engine is now available in the ` asia-northeast2 ` region (Osaka, Japan). 

##  April 15, 2019

**FEATURE:**

  * App Engine is now available in the ` europe-west6 ` region (Zürich, Switzerland). 

##  April 09, 2019

**FEATURE:**

  * [ Serverless VPC Access ](https://cloud.google.com/appengine/docs/standard/java/connecting-vpc?hl=es-419) is now in beta. Serverless VPC Access enables your app to connect to internal resources in your VPC network, such as Compute Engine VM instances, Memorystore instances, and more. 

##  March 26, 2019

**FEATURE:**

  * Updated Java SDK to version 1.9.73. 

##  February 13, 2019

**FEATURE:**

  * Updated Java SDK to version 1.9.72. 

**DEPRECATED:**

  * You can no longer build Java 7 apps. Java 7 app deployment was blocked on January 25. 

##  January 25, 2019

**DEPRECATED:**

  * App deployments on the Java 7 runtime are now blocked. If your app is currently using the Java 7 runtime, it will be automatically migrated to the [ Java 8 runtime ](https://cloud.google.com/appengine/docs/standard/java/runtime?hl=es-419) . 

##  January 21, 2019

**FEATURE:**

  * Updated Java SDK to version 1.9.78. 

##  December 28, 2018

**FEATURE:**

  * Updated Java SDK to version 1.9.69. 

**FEATURE:**

  * Upgrade the ASM library to improve handling of Java 11 bytecode. 

**FEATURE:**

  * Stop bundling the ECJ (Eclipse compiler) in the JSP compilation classpath. 

##  December 19, 2018

**FEATURE:**

  * Updated Java SDK to version 1.9.71. 

**FEATURE:**

  * [ ` DeleteSchema ` method ](https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/search/Index.html?hl=es-419#deleteSchema--) in ` com.google.appengine.api.search.Index ` is now supported. To completely delete an index, you need to delete the index's documents and schema. 

##  December 06, 2018

**FEATURE:**

  * Updated Java SDK to version 1.9.70. 

**FEATURE:**

  * Updated Jetty to version 9.4.14.v20181114. 

##  October 25, 2018

**FEATURE:**

  * Updated Java SDK to version 1.9.68. 

**FIXED:**

  * Minor bug fixes. 

##  October 22, 2018

**FEATURE:**

  * App Engine is now available in the ` asia-east2 ` region (Hong Kong). 

##  October 18, 2018

**FEATURE:**

  * Updated Java SDK to version 1.9.67. 

**FIXED:**

  * ` AppEngineSession.setAttribute ` supports null values, [ fixing a bug ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2283) that would previously throw null pointer exceptions. 

##  October 03, 2018

**FEATURE:**

  * Updated Java SDK to version 1.9.66. 

**FEATURE:**

  * Updated Jetty to version 9.4.12.v20180830. 

##  September 19, 2018

**FEATURE:**

**Java runtime notes**

**FEATURE:**

  * Updated Java SDK to version 1.9.65. 

**FEATURE:**

  * ` enhance_jdos ` will fail if it raises an exception. 

**FEATURE:**

  * ` DatastoreType ` always returns high replication. 

**FIXED:**

  * Fixed grammar in staging option defaults help. 

**FIXED:**

  * Fixed LocalMailService javadoc. 

**FEATURE:**

  * ` min-instances ` can be set to 0 in ` appengine-web.xml ` . 

**FEATURE:**

  * Improved support for using Java 11 to develop and deploy apps on the Java 8 runtime. 

##  August 24, 2018

**DEPRECATED:**

**Shutdown of Cloud Endpoints Frameworks v1 is approaching**

Cloud Endpoints Frameworks v1 for the App Engine standard environment was
deprecated on August 2, 2017. The [ service is scheduled to be shutdown
](https://cloud.google.com/appengine/docs/deprecations/endpoints-v1?hl=es-419)
on September 3, 2018, and the documentation will be removed. To avoid an
outage, you must migrate your v1 application. For information on migrating
your application to Endpoints Frameworks v2, see the following:

  * [ Java Migration Guide ](https://cloud.google.com/endpoints/docs/frameworks/java/migrating?hl=es-419)
  * [ Migrating Android Projects ](https://cloud.google.com/endpoints/docs/frameworks/java/migrating-android?hl=es-419)

##  July 10, 2018

**FEATURE:**

  * App Engine is now available in the ` us-west2 ` region (Los Angeles). 

##  July 02, 2018

**FIXED:**

Fixed a bug in [ auto scaling configuration
](https://cloud.google.com/appengine/docs/standard/java/config/appref?hl=es-419#scaling_elements)
where App Engine was aggressively shutting down instances when the ` max-
instances ` setting was used.

##  May 31, 2018

**FEATURE:**

**Java runtime notes**

**FEATURE:**

  * Updated Java SDK to version 1.9.64. 

**FIXED:**

  * Fixes issues where the [ Java runtime does not support ` <min-instances>0</min-instances> ` ](https://issuetracker.google.com/80273043?hl=es-419) . 

**FEATURE:**

  * Adds --application flag to ` dev_appserver.py ` . 

**FEATURE:**

  * Prevent deployment with filenames containing carriage returns. 

**FIXED:**

  * Fixes a problem where environment variables set in the ` appengine-web.xml ` file were not passed through the staging process and available to the app. 

##  May 15, 2018

**FEATURE:**

  * Completed a gradual rollout of an upgrade to the automatic scaling system: 
    * Improved efficiency resulting generally in lower instance cost (up to 6% reduction for many users) and up to 30% reduction for _loading requests_ , which are the first request to a new instance. 
    * New max instances setting allows you to cap the total number of instances to be scheduled. 
    * New min instances setting allows you to specify a minimum number of instance to keep running for your app. 
    * New target CPU utilization setting lets you optimize between latency and cost. 
    * New target throughput utilization setting lets you optimize for the number of concurrent requests at which new instances are started. 
    * No more resident instances in auto scaling. Previously, if you used the ` min_idle_instances ` setting, the minimum idle instances were labelled as _Resident_ in the Cloud Console, with the remainder of the instances labelled as _Dynamic_ . The new scheduler simply labels all instances as _Dynamic_ with auto scaling. However, the underlying behavior remains similar to previous behavior. If you use ` min_idle_instances ` and enable warmup requests, you will see at least that many dynamic instances running even during periods with no traffic. 
    * For more details, see the [ auto scaling documentation ](https://cloud.google.com/appengine/docs/standard/java/config/appref?hl=es-419#scaling_elements) . 

##  February 27, 2018

**FEATURE:**

**Java runtime notes**

  * Updated Java SDK to version 1.9.63. 

##  February 07, 2018

**FEATURE:**

**Java runtime notes**

**FEATURE:**

  * Updated Java SDK to version 1.9.62. 

**FIXED:**

  * Fixed a [ Cloud SDK issue ](https://issuetracker.google.com/issues/72808542?hl=es-419) where the Java 8 Servlet 3.1 quickstart processing failed during deployment. 

##  January 22, 2018

**FEATURE:**

**Java runtime notes**

  * Java SDK version 1.9.61 was patched. If you have previously installed this version, [ download ](https://cloud.google.com/appengine/docs/standard/java/download?hl=es-419) and reinstall the SDK. 

##  January 18, 2018

**FEATURE:**

**Java runtime notes**

  * Updated Java SDK to version 1.9.61. 

##  December 20, 2017

**FEATURE:**

**Java runtime notes**

**FEATURE:**

  * Updated Java SDK to version 1.9.60. 

**FEATURE:**

  * Added a deprecation warning when deploying or locally running a Java 7 application. 

**FIXED:**

  * Fixed a bug when using the appcfg flag 'use_google_application_default_credentials' did not work correctly on Google Compute Engine VMs. 

**FEATURE:**

  * Added a new flag to the ` appcfg ` command called ` enable_new_staging_defaults ` to prepare for future Cloud SDK integration to provide better default values for Java application deployment flags. 

**FEATURE:**

  * Changed the default character encoding to ` UTF-8 ` in the local development server when the runtime is Java 8. Also, allow the character encoding to be set explicitly using the ` appengine.file.encoding ` system property. These changes mimic what happens in production. 

**FIXED:**

  * Fixed issue where the [ Development server filter running on Windows fails to parse some servlet URL ](https://issuetracker.google.com/63595917?hl=es-419) . 

##  December 14, 2017

**FEATURE:**

  * Improved access control documentation around deploying apps with IAM roles and service accounts: 

    * [ Predefined App Engine roles ](https://cloud.google.com/appengine/docs/standard/java/access-control?hl=es-419#predefined_app_engine_roles)
    * [ Deploying using IAM roles ](https://cloud.google.com/appengine/docs/standard/java/granting-project-access?hl=es-419#deploying_using_iam_roles)
    * [ Require permissions ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=es-419#required_permissions)

**FEATURE:**

**Java runtime notes**

**FEATURE:**

  * Updated Java SDK to version 1.9.59. 

**FEATURE:**

  * Updated the local development server to set the ` url-stream-handler ` configuration parameter to ` native ` by default. This change reflects the behavior of the Java 8 runtime in production. For more information on ` url-stream-handler ` , see the [ ` appengine-web.xml ` ](https://cloud.google.com/appengine/docs/standard/java/config/appref?hl=es-419#url-stream-handler) reference. 

**FIXED:**

  * Fixed the [ ` NoClassDefFoundError ` ](https://github.com/GoogleCloudPlatform/endpoints-framework-gradle-plugin/issues/53) error that occurs when using the local development server with the Java 8 runtime and Endpoints Framework Gradle Plugin. 

**FIXED:**

  * Fixed a [ local development server bug ](https://issuetracker.google.com/63595917?hl=es-419) to resolve issues with servlet URLs that contain the colon character. 

##  October 31, 2017

**FEATURE:**

  * App Engine is now available in the ` asia-south1 ` region (Mumbai, India). 

##  October 11, 2017

**FEATURE:**

  * Announced general availability of [ App Engine firewall ](https://cloud.google.com/appengine/docs/standard/java/creating-firewalls?hl=es-419) . 

**FEATURE:**

**Java runtime notes**

**FEATURE:**

  * Updated Java SDK to version 1.9.58 

**FIXED:**

  * Fix the [ Jetty quickstart module for annotations ](https://webtide.com/jetty-9-quick-start/) in the App Engine flexible environment. 

**FIXED:**

  * Fixed [ local development server bug ](https://issuetracker.google.com/63595917?hl=es-419) where certain characters caused problems with URL parsing. 

**FEATURE:**

  * Use 1.8 target for the Jetty 9 JSP compiler when using JDK 9. 

##  September 25, 2017

**FEATURE:**

**Java runtime notes**

**FEATURE:**

  * [ The Java 8 runtime is now generally available ](https://cloudplatform.googleblog.com/2017/09/Java-8-on-App-Engine-Standard-environment-is-now-generally-available.html) . 

**FEATURE:**

  * Updated Java SDK to version 1.9.57 

**DEPRECATED:**

  * The local development server no longer supports ` -Xbootclasspath/p ` and ` google_sql.jar ` in the path. 

**DEPRECATED:**

  * The Java 8 runtime no longer supports JDK9 JARs that contain ` module-info.class ` . 

**DEPRECATED:**

  * Cloud Endpoints v1 is no longer supported on the Java 8 runtime. 

**FIXED:**

  * Fixed ` NoClassDefFoundError ` exception on the local development server when using Cloud Endpoints v2 on the Java 8 runtime. 

##  September 18, 2017

**FEATURE:**

**Java runtime notes**

**FEATURE:**

  * Release 1.3.3 for ` com.google.cloud.tools:appengine-gradle-plugin `

**FEATURE:**

  * The local development server now logs output to ` dev_appserver.out ` . ( [ #156 ](https://github.com/GoogleCloudPlatform/app-gradle-plugin/pull/156) ) 

**FEATURE:**

  * ` datastore-indexes-auto.xml ` is no longer removed during non-clean rebuilds. ( [ #165 ](https://github.com/GoogleCloudPlatform/app-gradle-plugin/issues/165) ) 

**FEATURE:**

  * Switched to use sync instead of copy on the explodeWar task. ( [ #162 ](https://github.com/GoogleCloudPlatform/app-gradle-plugin/pull/162) ) 

##  September 13, 2017

**FEATURE:**

  * You can now use managed certificates to add SSL to your custom domain. Once you map your custom domain to your application, App Engine provisions an SSL certificate automatically and handles renewing the certificate before it expires and revoking it if you remove the custom domain. Managed certificates are in beta. For more information, see [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/standard/java/securing-custom-domains-with-ssl?hl=es-419) . 

**FEATURE:**

  * If you have an existing domain mapping and SSL certificate, then it continues to function as expected. You can also [ upgrade to managed SSL certificates ](https://cloud.google.com/appengine/docs/standard/java/securing-custom-domains-with-ssl?hl=es-419#updating_to_managed_ssl_certificates) . 

**FEATURE:**

  * The ` gcloud ` commands and Admin API methods used to [ map custom domains ](https://cloud.google.com/appengine/docs/standard/java/mapping-custom-domains?hl=es-419) are now generally available. This includes [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains/?hl=es-419) and [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=es-419) . However, if you want to use managed SSL certificates, use the beta commands and methods that are specified in [ Securing Custom Domains with SSL ](https://cloud.google.com/appengine/docs/standard/java/securing-custom-domains-with-ssl?hl=es-419) . 

##  September 11, 2017

**FEATURE:**

**Java runtime notes**

**FEATURE:**

  * Updated Java SDK to version 1.9.56 

**FEATURE:**

  * For flexible runtimes compatible with the App Engine standard environment APIs ( ` compat ` runtimes), this SDK version includes updates to the ` appengine-web.xml ` file configuration to add support for ` subnetwork_name ` , ` session_affinity ` , and updated liveness and readiness health checks. 

**FEATURE:**

  * Added support for the environment variables ` GAE_RUNTIME ` ( ` java 7 ` or ` java 8 ` ) and GAE_ENV ( ` standard ` ) in the Google App Engine SDK. 

##  September 05, 2017

**FEATURE:**

  * App Engine is now available in the ` southamerica-east1 ` region (São Paulo, Brazil). 

**FEATURE:**

  * Updated Java SDK to version 1.9.55 

**FIXED:**

  * Fixed bug where security manager was being used for the SDK even when the app was using Java 8/Jetty 9. 

**FEATURE:**

  * Emit error message when using the [ appstats ](https://cloud.google.com/appengine/docs/standard/java/tools/appstats?hl=es-419) filter with Java8. 

**FIXED:**

  * Fixed [ Issue 63123716: Url fetching with Google Java HTTP Client not working on dev-server ](https://issuetracker.google.com/issues/63123716?hl=es-419)

##  August 01, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west3 ` region (Frankfurt, Germany). 

##  July 18, 2017

**FEATURE:**

  * App Engine is now available in the ` australia-southeast1 ` region (Sydney, Australia). 

##  June 28, 2017

**FEATURE:**

**What's New**

  * [ Java 8 runtime for App Engine standard environment ](https://cloud.google.com/appengine/docs/standard/java/runtime-java8?hl=es-419) is in Beta. 
  * Just add ` <runtime>java8</runtime> ` in the ` appengine-web.xml ` file. 
  * Based on OpenJDK 8, Servlet 3.1 and Jetty 9.3. 
  * Feature compatibility with Java 7 on App Engine and the built-in App Engine APIs. 
  * Supports all Google Cloud-based APIs accessible from the [ Google Cloud Client Library for Java ](https://googleapis.github.io/google-cloud-java/google-cloud-clients/) . 
  * All public Java 8 APIs are available, [ class whitelisting ](https://cloud.google.com/appengine/docs/standard/java/jrewhitelist?hl=es-419) has been removed. 
  * The [ Java security manager ](https://docs.oracle.com/javase/7/docs/api/java/lang/SecurityManager.html) is removed for the Java 8 runtime. 
  * Support for read only [ GCP Metadata server ](https://cloud.google.com/compute/docs/storing-retrieving-metadata?hl=es-419) project and service accounts values. 
  * Java SDK 1.9.54 supports the Java 8 runtime. 

**BREAKING:**

**Known Java 8 Runtime Limitations**

  * The ` /tmp ` directory is writable. Files in ` /tmp ` will consume memory allocated to your instance. 
  * Async Servlet 3.1 is not supported. 
  * WebSocket is not supported. 
  * The Jetty 9 configuration cannot be modified. 
  * App Engine APIs can only be called from the thread that handles a web request or from threads created using [ ThreadManager ](https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/ThreadManager?hl=es-419)
  * ` WEB-INF/appengine-web.xml ` must be used for configuration, ` app.yaml ` is not currently supported. 
  * Deployment must be done through the Maven, Gradle, or IDE plugins. 
  * If you create a thread pool using for example ` ExecutorService pool = Executors.newCachedThreadPool(ThreadManager.currentRequestThreadFactory()) ` then it must be shutdown down explicitly using ` pool.shutdown() ` before the current request terminates. 
  * Previously it was possible to reference vendored classes like ` com.google.appengine.repackaged.org.joda.Instant ` inadvertently when just ` org.joda.Instant ` was intended. The vendoring scheme has changed so code that did that no longer works. 
  * Native network APIs (for example ` HttpURLConnection ` ) are enabled for billed applications, but will return an exception ( ` java.net.SocketTimeoutException ` or ` java.io.IOException ` ) when used in free applications. Free applications can access ` *.googleapis.com ` and ` accounts.google.com ` , and they can also be [ configured ](https://cloud.google.com/appengine/docs/standard/java/config/appref?hl=es-419#url-stream-handler) to use the URLFetch service. 
  * The ` google-cloud-java ` APIs need to be wrapped in an ` executor ` . See [ Pub/Sub Publisher hangs unless submitted through an executor ](https://github.com/googleapis/google-cloud-java/issues/2150) . 
  * Cloud Endpoints must be [ migrated ](https://cloud.google.com/endpoints/docs/frameworks/legacy/v1/java/migrating?hl=es-419) from v1 to v2. 
  * Channels and XMPP APIs are not supported. 
  * ` appengine-labs-api.jar ` APIs are not supported resulting in [ Appstats for Java ](https://cloud.google.com/appengine/docs/standard/java/tools/appstats?hl=es-419) not being supported. 
  * The Java 8 runtime default is to use the native Java HTTP(S) transport, not the URL Fetch transport, as is the case for Java 7 runtime. For more information, see [ url-stream-handler ](https://cloud.google.com/appengine/docs/standard/java/config/appref?hl=es-419#url-stream-handler) . 

##  June 15, 2017

**FEATURE:**

  * Updated Java SDK to version 1.9.54. 

##  June 06, 2017

**FEATURE:**

  * App Engine is now available in the ` europe-west2 ` region (London). 

**FEATURE:**

  * You can now use the beta-level features in the Admin API and ` gcloud ` command-line tool to [ create and manage your custom domains and SSL certificates ](https://cloud.google.com/appengine/docs/standard/java/mapping-custom-domains?hl=es-419) . 

##  May 09, 2017

**FEATURE:**

  * App Engine is now available in the ` us-east4 ` region (North Virginia). 

**FEATURE:**

  * Updated Java SDK to version 1.9.53. 

**FIXED:**

  * Fixed a Java SDK issue where JSP tag library usage would not work with a Java 8 SpringBoot application. 

##  May 08, 2017

**FEATURE:**

  * Release 1.3.1 for ` com.google.cloud.tools:appengine-(gradle/maven)-plugin `

**FEATURE:**

  * Running locally on development server will read and include environment variables from the ` appengine-web.xml ` configuration file. 

**FEATURE:**

  * Expose ` environment ` parameter for including additional environment variables through the maven/gradle configuration. 

##  May 02, 2017

**FEATURE:**

  * Release 1.3.0 for ` com.google.cloud.tools.appengine-(gradle/maven)-plugin `

**CHANGED:**

  * Default development server is Dev App Server v1 (only java modules) 

**FEATURE:**

  * New gradle tasks for configuration deployment : ` appengineDeployCron ` , ` appengineDeployDispatch ` , ` appengineDeployDos ` , ` appengineDeployIndex ` , ` appengineDeployQueue `

**FEATURE:**

  * New maven goals for configuration deployment : ` appengine:deployCron ` , ` appengine:deployDispatch ` , ` appengine:deployDos ` , ` appengine:deployIndex ` , ` appengine:deployQueue `

**FEATURE:**

  * Staging flexible apps with maven/gradle only copies ` app.yaml ` into build/target directory. For deployment of configuration files, use ` src/main/appengine ` . 

**CHANGED:**

  * Gradle exploded app directory default changed from ` build/exploded-app ` to ` build/exploded-<module-name> `

##  April 19, 2017

**FEATURE:**

  * Updated Java SDK to version 1.9.52. 

**FEATURE:**

  * Better support for Java 8 standard environment alpha runtime. 

**FEATURE:**

  * Upgrade to Jetty 9.3.18 for the [ Java 8 alpha ](https://docs.google.com/a/google.com/forms/d/1MDzykTWp77YzRgFs5R6ONOuKWYnKEhfy5VhSJYbDvmo/viewform?hl=es-419) standard environment runtime. 

**FEATURE:**

  * Update the ` quickstart-web.xml ` processing to use the latest Jetty capabilities to better support Java 8 SpringBoot applications. 

**FIXED:**

  * Fix local execution of multiple services located in directories ending with the same name. 

**FIXED:**

  * Fix SDK error when booting a SpringBoot application. 

##  March 29, 2017

**FEATURE:**

  * Updated Java SDK to version 1.9.51. 

**FEATURE:**

  * [ Java 8 alpha ](https://docs.google.com/a/google.com/forms/d/1MDzykTWp77YzRgFs5R6ONOuKWYnKEhfy5VhSJYbDvmo/viewform?hl=es-419) applications without a ` web.xml ` file can now run in the [ local development server ](https://cloud.google.com/appengine/docs/standard/java/tools/using-local-server?hl=es-419) . 

##  March 21, 2017

**FEATURE:**

  * Updated the ` com.google.cloud.tools:appengine-gradle-plugin ` to 1.1.1. 

**FIXED:**

  * Fixed [ issue 108 ](https://github.com/GoogleCloudPlatform/app-gradle-plugin/issues/108) with flexible environment deployments in multi-module Gradle projects failing. 

##  March 06, 2017

**FEATURE:**

  * Updated the ` com.google.cloud.tools:appengine-maven-plugin ` to 1.2.1. 

**FIXED:**

  * Fixed [ issue 144 ](https://github.com/GoogleCloudPlatform/app-maven-plugin/issues/144) with custom deployable parameters incorrectly adding in extra directory. 

##  March 01, 2017

**FEATURE:**

  * Updated Java SDK to version 1.9.50. 

**FEATURE:**

  * Added support for testing multiple services with the local development server. 

**FEATURE:**

  * Stop generating a web.xml file for apps that use the Java 7 runtime and include a ` web.xml ` that specifies the servlet 3.1 schema. 

**FEATURE:**

  * Package Java class files in the .zip files even if the application does not have JSPs. 

##  February 17, 2017

**FEATURE:**

Updated the ` com.google.cloud.tools ` [ maven
](https://cloud.google.com/appengine/docs/java/tools/maven-
reference?hl=es-419) (1.2.0) and [ gradle
](https://cloud.google.com/appengine/docs/java/tools/gradle-
reference?hl=es-419) (1.1.0) plugins for App Engine:

  * Added ` clearDatastore ` flag for clearing the local datastore upon startup. 
  * Added source-context tasks/goals. 

##  January 30, 2017

**FEATURE:**

  * Updated Java SDK to version 1.9.49. 

##  December 01, 2016

**FEATURE:**

  * Updated Java SDK to version 1.9.48. 

##  November 03, 2016

**CHANGED:**

  * Version 1.9.45 was skipped. 

**FEATURE:**

  * Updated Java Runtime and SDK to version 1.9.46. 

##  October 27, 2016

**DEPRECATED:**

  * The Channel and XMPP services are now [ deprecated ](https://cloud.google.com/appengine/docs/deprecations/?hl=es-419) . These services will be turned down on October 31, 2017. 

##  October 17, 2016

**FEATURE:**

  * Updated Java Runtime and SDK to version 1.9.44. 

**FEATURE:**

  * Add new BlobInfo property, which is set when a Blobstore blob is stored in a Cloud Storage bucket. 

##  August 01, 2016

**FEATURE:**

**Admin API notes**

  * Version 1 of the [ Admin API ](https://cloud.google.com/appengine/docs/admin-api/?hl=es-419) is now generally available. 

**FEATURE:**

Version 1.9.42

**CHANGED:**

  * Version 1.9.41 was skipped. 

**FIXED:**

  * Version 1.9.42 includes general bug fixes and improvements. 

##  July 21, 2016

**FIXED:**

**Java 8 runtime notes**

  * Fixes potentially incorrect reported memory usage in the App Engine dashboard (the values under Instance "Average Memory" and the "Memory Usage" graph). This issue does not affect billing. 

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

  * New [ App Engine guided walkthrough ](https://console.cloud.google.com/start/appengine?hl=es-419) in the Cloud Console. Pick your preferred language and launch an interactive tutorial directly in the console. 

**FEATURE:**

  * Increases the maximum cron tasks limit to 250. 

**FEATURE:**

**Java runtime notes**

  * All Java applications will be automatically upgraded to use the 64-bit version of the Java runtime. This rolling upgrade will start on July 20, 2016. 

##  July 01, 2016

**FEATURE:**

**Cloud Datastore**

  * New [ Cloud Datastore Pricing ](https://cloud.google.com/appengine/pricing?hl=es-419#costs-for-datastore-calls) is now in effect. 

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

##  May 02, 2016

**FEATURE:**

**App Engine flexible environment**

  * The [ Ruby runtime ](https://cloud.google.com/appengine/docs/flexible/ruby/?hl=es-419) is now available for the App Engine flexible environment. 

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

**Java runtime notes**

  * Google no longer accepts quota increase requests for the mail service. Customers should use [ Sendgrid ](https://cloud.google.com/appengine/docs/standard/java/mail/sendgrid?hl=es-419) instead. 

##  March 24, 2016

**CHANGED:**

Version 1.9.35

  * App Engine Managed VMs is renamed to [ App Engine flexible environment ](https://cloud.google.com/appengine/docs/flexible/?hl=es-419) . 

**FIXED:**

  * Fixes trace timestamps to match log timestamps. 

**CHANGED:**

**Java runtime notes**

  * This release does not include a new Java SDK. Java users should continue to use the 1.9.34 SDK. 

##  March 16, 2016

**FEATURE:**

**Java runtime notes**

  * Version 1.9.34 of the Java SDK is available. 

##  March 04, 2016

**FEATURE:**

Version 1.9.34

  * Increases default quota for URL fetch for billed apps. Refer to the [ Quotas page ](https://cloud.google.com/appengine/docs/quotas?hl=es-419#UrlFetch) for details. 

**FEATURE:**

**Java runtime notes**

  * This release does not include a new Java SDK. Java users should continue to use the 1.9.32 SDK. 

##  February 17, 2016

**FEATURE:**

Version 1.9.33

  * The URL path "/form" is now allowed and will be forwarded to applications. Previously, this path was blocked. 

**CHANGED:**

**Java runtime notes**

  * This release does not include a new Java SDK. Java users should continue to use the 1.9.32 SDK. 

##  February 03, 2016

**FEATURE:**

Version 1.9.32

  * Container construction choices for Managed VMs 

The ` gcloud preview app deploy ` (and ` mvn gcloud:deploy ` ) commands upload
your artifacts to our servers and build a container to deploy your app to the
Managed VM environment.

There are two mechanisms for building the container image remotely. The
default behavior is to build the container on a transient Compute Engine
Virtual Machine which has Docker installed. Alternatively, you can use the [
Cloud Build ](https://cloud.google.com/cloud-build/docs/?hl=es-419) service.
To use the Cloud Build service, follow these steps:

    1. [ Activate the Cloud Build API ](https://support.google.com/cloud/answer/6158841?hl=es-419) for your project. 
    2. Use the command ` gcloud config set app/use_cloud_build True ` . This will cause all invocations of ` gcloud preview app deploy ` to use the service. (To return to the default behavior, use the command ` gcloud config set app/use_cloud_build False ` . 

**FEATURE:**

**Java runtime notes**

  * Improved exception handling for the low-level API for Datastore, ` Transaction.rollback() ` . Instead of an exception, it generates an ` INFO ` log message when an operation associated with the transaction has failed. 

##  January 14, 2016

**FEATURE:**

Version 1.9.31

**FEATURE:**

App Engine now supports Google Groups: Adding a Google Group as a member of a
project grants the members of the group access to App Engine. For example, if
a Google Group is an Editor on a project, all members of the group now have
Editor access to the App Engine application.

##  December 30, 2015

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

  * For developers using the [ endpoints API ](https://cloud.google.com/appengine/docs/standard/python/endpoints/create_api?hl=es-419#defining_the_api_endpointsapi) , added a discoverable boolean parameter to the @Api annotation to allow users to disable API discovery. Using this feature will prevent some client libraries (e.g. JavaScript) and the API Explorer from working, as they depend on discovery. 

##  October 29, 2015

**FEATURE:**

Version 1.9.28

**BREAKING:**

The Prospective Search API, which was deprecated on July 14, 2015, is now
restricted to existing users. It will fully shutdown on December 1, 2015.

**FEATURE:**

Improved accuracy of Geo filtering in Search queries.

**FEATURE:**

**Java runtime notes**

  * Disabled Files API in the Java DevAppServer. 

##  September 25, 2015

**FEATURE:**

Version 1.9.27

**FEATURE:**

Applications that are newly enabled for billing now default to an unlimited
daily budget, and no longer default to a maximum daily budget of $0. This
prevents unwanted outages due to running out of budget. To set a ceiling on
your application's daily cost, after you enable billing, set a budget in the [
app engine settings
](https://console.cloud.google.com/project/_/appengine/settings?hl=es-419) .
For more information, see [ Setting a daily budget
](https://cloud.google.com/appengine/docs/developers-
console/?hl=es-419#setting_a_daily_budget) .

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

**FEATURE:**

**Java runtime notes**

  * Java's URLFetch API gains a property to specify default fetch deadline. ` appengine.api.urlfetch.defaultDeadline ` is a floating point number in seconds that can be used to specify a default URLFetch timeout for Java in appengine-web.xml. 

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

