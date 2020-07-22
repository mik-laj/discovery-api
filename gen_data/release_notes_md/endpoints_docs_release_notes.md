#  Release notes

This page contains release notes for features and updates to Cloud Endpoints.
For information about updates to the Extensible Service Proxy (ESP), see the [
Endpoints runtime release notes
](https://github.com/cloudendpoints/esp/releases) on GitHub.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/cloud-endpoints-release-
notes.xml `

##  January 2020

###  gRPC support for Cloud Run added (Beta)

Added support for gRPC for [ Cloud Run ](/run/docs) to Cloud Endpoints. This
feature requires you to use [ Extensible Service Proxy V2 Beta (ESPv2 Beta)
](/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) as the
Endpoints [ API gateway ](https://wikipedia.org/wiki/API_management) .

Endpoints support for gRPC with [ Cloud Run ](/run/docs) and Endpoints support
for ESPv2 Beta are currently in Beta.

See [ Getting Started with Endpoints for Cloud Run ](/endpoints/docs/grpc/get-
started-cloud-run) for more.

##  December 2019

###  Extensible Service Proxy V2 Beta support added

[ Extensible Service Proxy V2 Beta (ESPv2 Beta)
](/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) support added
as an Endpoints [ API gateway ](https://wikipedia.org/wiki/API_management) for
[ Cloud Functions ](/endpoints/docs/openapi/get-started-cloud-functions) and [
Cloud Run ](/endpoints/docs/openapi/get-started-cloud-run) . ESPv2 Beta is an
[ Envoy ](https://www.envoyproxy.io/docs/envoy/latest/) -based high-
performance, scalable proxy that runs in front of an OpenAPI API backend.

ESPv2 Beta supports version 2 of the [ OpenAPI Specification
](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) .
ESPv2 Beta does not currently support [ gRPC ](http://www.grpc.io) .

ESPv2 Beta is only supported for use for the Beta versions of Endpoints for [
Cloud Functions ](/endpoints/docs/openapi/get-started-cloud-functions) and for
[ Cloud Run ](/endpoints/docs/openapi/get-started-cloud-run) . ESPv2 Beta is
not supported for Endpoints for App Engine, GKE, Compute Engine, or
Kubernetes.

ESPv2 Beta supports all other features of [ Extensible Service Proxy (ESP)
](/endpoints/docs/openapi/glossary#extensible_service_proxy) , such as trace
and logging, unless explicitly specified in the documentation.

APIs deployed on Endpoints for Cloud Functions and Cloud Run using ESP will
continue to function. However, we recommend that you migrate your APIs to
ESPv2 Beta. Technical support will instruct you to move to ESPv2 Beta rather
than attempting to troubleshoot issues with ESP.

See [ Migrate to Extensible Service Proxy V2 Beta
](/endpoints/docs/openapi/migrate-to-esp-v2) for more.

##  September 2018

###  Cloud Endpoints Frameworks v1 has been shutdown

Cloud Endpoints Frameworks v1 for the App Engine standard environment was
deprecated on August 2, 2017. The [ service was shutdown
](/appengine/docs/deprecations/endpoints-v1) on September 13, 2018, and the
documentation has been removed.

###  Endpoints Frameworks Python: Changing the default logging level

The ability to the change the default logging level was added to Endpoints
Frameworks Python. For more information, see [ Logging in Endpoints Framework
for Python
](/endpoints/docs/frameworks/python/api_server#logging_in_endpoints_framework_for_python)
.

##  August 2018

###  Cloud Endpoints Portal updates

Endpoints Portal is now now generally available. This release includes the
following new features and enhancements:

####  Sync custom documentation through an API

An API that allows you to sync custom documentation to your portal is now
available. To learn more, see the documentation for your API implementation:

  * [ Endpoints OpenAPI: Sync the Custom Documentation through an API ](/endpoints/docs/openapi/dev-portal-sync-custom-api)
  * [ Endpoints gRPC: Sync the Custom Documentation through an API ](/endpoints/docs/grpc/dev-portal-sync-custom-api)
  * [ Endpoints Frameworks: Sync the Custom Documentation through an API ](/endpoints/docs/frameworks/dev-portal-sync-custom-api)

####  Include images in custom documentation

You can add images to the custom content Git repository and reference them in
your Markdown files. To learn more, see the documentation for your API
implementation:

  * [ Endpoints OpenAPI: Adding images ](/endpoints/docs/openapi/dev-portal-add-custom-docs#add_images)
  * [ Endpoints gRPC: Adding images ](/endpoints/docs/grpc/dev-portal-add-custom-docs#add_images)
  * [ Endpoints Frameworks: Adding images ](/endpoints/docs/frameworks/dev-portal-add-custom-docs#add_images)

####  Introducing SmartDocs API reference documentation

The component that displays API reference documentation in your portal and
provides the **Try this API** panel has a name: _SmartDocs API reference
documentation_ . Originally developed for the Endpoints Portal, SmartDocs is
also available in [ Apigee’s integrated developer portal ](https://docs-
new.apigee.com/whats-new#api-doc-ui) .

###  Shutdown of Cloud Endpoints Frameworks v1 is approaching

Cloud Endpoints Frameworks v1 for the App Engine standard environment was
deprecated on August 2, 2017. The [ service is scheduled to be shutdown
](/appengine/docs/deprecations/endpoints-v1) on September 3, 2018, and the
documentation will be removed. To avoid an outage, you must migrate your v1
application. For information on migrating your application to Endpoints
Frameworks v2, see the following:

  * [ Java: Migration Guide ](/endpoints/docs/frameworks/java/migrating)
  * [ Java: Migrating Android Projects ](/endpoints/docs/frameworks/java/migrating-android)
  * [ Python: Migration Guide ](/endpoints/docs/frameworks/python/migrating)

###  Disable trace sampling in ESP

By default, ESP samples a small number of requests to your API and sends
traces to [ Stackdriver Trace ](/trace/docs/overview) . The ESP startup option
to disable trace sampling was added in ESP release 1.19.0. This option is now
available for deployments on the App Engine flexible environment.

To learn more, see "Tracing your API" in the documentation for your API
implementation:

  * [ Endpoints OpenAPI documentation ](/endpoints/docs/openapi/tracing)
  * [ Endpoints gRPC documentation ](/endpoints/docs/grpc/tracing)

Endpoints Frameworks, which is used on the App Engine standard environment
does not use ESP for API management and does not send trace data to
Stackdriver Trace.

##  July 2018

###  New role and permissions for Endpoints Portal

The [ Identity and Access Management (IAM) ](/iam/docs) role, **Endpoints
Portal Admin** , and several new IAM permissions are now available. The new
role and permissions allow you to control the degree of access that project
members have to Endpoints Portal.

To learn more, see "Endpoints Portal permissions" in the documentation for
your API implementation:

  * [ Endpoints OpenAPI documentation ](/endpoints/docs/openapi/api-access-overview#endpoints_portal_permissions)
  * [ Endpoints gRPC documentation ](/endpoints/docs/grpc/api-access-overview#endpoints_portal_permissions)
  * [ Endpoints Frameworks documentation ](/endpoints/docs/frameworks/api-access-overview#endpoints_portal_permissions)

##  June 2018

###  Library and Plugin Updates

  * The Endpoints Frameworks for Python library, version [ 4.4.0 ](https://pypi.python.org/pypi/google-endpoints) , has been enhanced such that you can import the ` message_types ` , ` messages ` , and the ` remote ` classes from the ` endpoints ` library instead of the ` protorpc ` library. In the file where you [ define your API ](/endpoints/docs/frameworks/python/create_api) , we recommend that you change your import statements from: 
    
        import endpoints
    from protorpc import message_types
    from protorpc import messages
    from protorpc import remote
    

to:

    
        from endpoints import message_types
    from endpoints import messages
    from endpoints import remote
    

This optional change in your import statements streamlines code in the
Endpoints Frameworks library.

  * The Endpoints Frameworks for Java libraries, version [ 2.1.0 ](http://search.maven.org/#search%7Cga%7C1%7Cendpoints-framework) , now validates that requests have required parameters. If a required parameter is omitted in a request, Endpoints Frameworks returns the status code HTTP 400, Bad Request. 

###  Beta launch of Endpoints Portal

You use Endpoints Portal to create a developer portal, a website that users of
your Cloud Endpoints API can access to read documentation and to interact with
your API.

To learn more, see "Cloud Endpoints Portal Overview" in the documentation for
your API implementation:

  * [ Endpoints OpenAPI documentation ](/endpoints/docs/openapi/dev-portal-overview)
  * [ Endpoints gRPC documentation ](/endpoints/docs/grpc/dev-portal-overview)
  * [ Endpoints Frameworks documentation ](/endpoints/docs/frameworks/dev-portal-overview)

##  March 2018

###  ESP managed rollout option

The ESP ` --rollout_strategy=managed ` option is now available for APIs
described with OpenAPI or gRPC. This option configures ESP to use the latest
deployed service configuration. When you specify this option, up to 5 minutes
after you deploy a new service configuration, ESP detects the change and
automatically begins using it. We recommend that you specify this option
instead of a specific configuration ID for ESP to use.

This option is not available in Endpoints Frameworks.

Although the managed rollout option has been available in ESP since version
1.7.0, the ` gcloud ` command line tool has now been updated to make the
option available on the App Engine flexible environment. Currently, the option
is available only in the beta version of the ` gcloud ` command line tool.
After you add the option to your ` app.yaml ` , you will need to use the `
gcloud beta app deploy ` command to deploy your API and ESP.

For information on deploying ESP with this new option, see the documentation
for your API implementation:

  * [ Endpoints OpenAPI documentation ](/endpoints/docs/openapi/deploy-api-backend#deploying_your_api_and_esp)
  * [ Endpoints gRPC documentation ](/endpoints/docs/grpc/deploy-api-backend#deploying_your_api_and_esp)

###  Library and Plugin Updates

  * The Endpoints Frameworks for Python library, version [ 3.0.0 ](https://pypi.python.org/pypi/google-endpoints) , contains potentially breaking changes. 
    * It is now possible to deploy a single service comprising multiple APIs. However, there are additional restrictions on API names when using this functionality. See [ Deploying and Testing an API ](/endpoints/docs/frameworks/python/test-deploy#generating_and_deploying_an_api_configuration_file) for more details. 
    * Previously, API version strings were embedded in the path as-is. For example, an API ` echo ` with version ` v1 ` would have a path like ` /echo/v1 ` . This continues to be the case for API version strings that are not compatible with the [ SemVer standard ](https://semver.org/spec/v2.0.0.html) . If the string is compatible with the SemVer standard, the major version number will be extracted and embedded in the path when you deploy your API. So, for example, an API called ` echo ` with version ` 2.1.0 ` would have a path like ` /echo/v2 ` . If you update the ` echo ` API to version ` 2.2.0 ` and deploy a backwards-compatible change, the path remains ` /echo/v2 ` . This allows you to update the API version number when you make a backwards-compatible change without breaking existing paths for your clients. But if you update the ` echo ` API to version ` 3.0.0 ` (because you are deploying a breaking change), the path is changed to ` /echo/v3 ` . 

##  January 2018

The Endpoints dashboard now provides the ability to compare a configuration
file with the previous version. Viewing the differences in your configuration
files might be helpful when troubleshooting a problem with a particular
deployment. To learn more, see the documentation for your API implementation:

  * [ Endpoints OpenAPI documentation ](/endpoints/docs/openapi/config-file-compare)
  * [ Endpoints gRPC documentation ](/endpoints/docs/grpc/config-file-compare)
  * [ Endpoints Frameworks documentation ](/endpoints/docs/frameworks/config-file-compare)

###  Library and Plugin Updates

  * The Endpoints Frameworks for Python library, version [ 2.5.0 ](https://pypi.python.org/pypi/google-endpoints)

##  December 2017

###  Endpoints DNS

The Endpoints DNS feature is now generally available. You can configure
Endpoints to register a URL that you can use to call your APIs. For people not
using App Engine, this provides a convenient way to call APIs without using
your IP address or registering a domain name. The API can be called with a URL
such as:

    
    
    echo-api.endpoints.my-project-id.cloud.goog
    

To learn more, see the "Configuring DNS on the cloud.goog domain" page in the
documentation for your API implementation:

  * [ Endpoints OpenAPI documentation ](https://cloud.google.com/endpoints/docs/openapi/cloud-goog-dns-configure)
  * [ Endpoints gRPC documentation ](https://cloud.google.com/endpoints/docs/grpc/cloud-goog-dns-configure) . 

###  Endpoints DNS with SSL

A sample that shows how to enable SSL for APIs configured to use the `
cloud.goog ` domain is now available. To learn more, see the documentation for
your API implementation:

  * [ Endpoints OpenAPI documentation ](/endpoints/docs/openapi/enabling-ssl#enabling_ssl_using_lets_encrypt)
  * [ Endpoints gRPC documentation ](/endpoints/docs/grpc/enabling-ssl#enabling_ssl_using_lets_encrypt)

##  November 2017

###  Filter for a specific consumer project

The ability to filter metrics for a specific consumer project is now available
as an Alpha feature in the Endpoints dashboard. To learn more, see the
documentation for your API implementation:

  * [ Endpoints OpenAPI documentation ](/endpoints/docs/openapi/monitoring-your-api#filter_for_a_specific_consumer_project)
  * [ Endpoints gRPC documentation ](/endpoints/docs/grpc/monitoring-your-api#filter_for_a_specific_consumer_project)
  * [ Endpoints Frameworks documentation ](/endpoints/docs/frameworks/monitoring-your-api#filter_for_a_specific_consumer_project)

###  Library and Plugin Updates

  * The Endpoints Frameworks for Python library, version [ 2.4.5 ](https://pypi.python.org/pypi/google-endpoints)

  * The Endpoints Framework Gradle plugin, version [ 1.0.3 ](https://github.com/GoogleCloudPlatform/endpoints-framework-gradle-plugin/blob/master/CHANGELOG.md)

  * The Endpoints Framework Maven plugin, version [ 1.0.3 ](https://github.com/GoogleCloudPlatform/endpoints-framework-maven-plugin/blob/master/CHANGELOG.md)

##  October 2017

###  Beta Launch of Quotas

Quotas let you specify usage limits to protect your API from an excessive
number of requests. To learn more about quotas, see the "About Quotas" page in
the documentation for your API implementation:

  * [ Endpoints OpenAPI documentation ](/endpoints/docs/openapi/quotas-overview)
  * [ Endpoints gRPC documentation ](/endpoints/docs/grpc/quotas-overview)
  * [ Endpoints Frameworks documentation ](/endpoints/docs/frameworks/quotas-overview)

###  gcloud endpoints and gcloud services

The Cloud SDK command groups [ gcloud endpoints
](/sdk/gcloud/reference/endpoints) and [ gcloud services
](/sdk/gcloud/reference/services) are now generally available. The gcloud
endpoints and gcloud services command groups are a replacement for gcloud
service-management, which is deprecated.

###  Library Updates

  * The Endpoints Frameworks for Python library, version [ 2.4.1 ](https://pypi.python.org/pypi/google-endpoints) is available. 

  * The Endpoints Frameworks for Java libraries, version [ 2.0.9 ](http://search.maven.org/#search%7Cga%7C1%7Cendpoints-framework) are available. 

##  August 2017

API metrics are now published in Stackdriver. You can monitor request rates,
latencies and much more. For information on setting up alerts, see the
"Monitoring your API" page in the documentation for your API implementation:

  * [ Endpoints OpenAPI documentation ](/endpoints/docs/openapi/monitoring-your-api)
  * [ Endpoints gRPC documentation ](/endpoints/docs/grpc/monitoring-your-api)
  * [ Endpoints Frameworks documentation ](/endpoints/docs/frameworks/monitoring-your-api) , 

You will find a complete list of metrics in the [ Stackdriver metrics list
](/monitoring/api/metrics_gcp#gcp-serviceruntime) .

##  July 2017

You can now programmatically grant access to individual APIs via the IAM API.
See the "API Access Overview" page for your API implementation to find
details.

  * [ Endpoints OpenAPI documentation ](/endpoints/docs/openapi/api-access-overview)
  * [ Endpoints gRPC documentation ](/endpoints/docs/grpc/api-access-overview)
  * [ Endpoints Frameworks documentation ](/endpoints/docs/frameworks/api-access-overview)

##  May 2017

Endpoints now attributes calls to the Producer project if no API key is
provided and reports the protocol used by the backend (gRPC, HTTP).

##  April 2017

Endpoints can now optionally register a URL that you can use to call your
APIs. For people not using App Engine, this gives a convenient way to call
APIs without using your IP address. The API can be called with a URL such as

    
    
    echo-api.endpoints.my-project-id.cloud.goog
    

For details, see the [ OpenAPI configuration page
](https://cloud.google.com/endpoints/docs/openapi/cloud-goog-dns-configure) or
the [ gRPC configuration page
](https://cloud.google.com/endpoints/docs/grpc/cloud-goog-dns-configure) .

##  February 2017

API Deployment History is now available in the Google Cloud Console, allowing
you to view the history of API config deployments. This functionality is
currently in Beta.

The API deployment history shows you who uploaded a particular configuration,
when it was uploaded, and what its configuration ID is. This is helpful for
finding configuration IDs and attribution of configuration changes for your
API.

To see the new screen, navigate to your API in the Endpoints UI section of the
[ Cloud Console ](https://console.cloud.google.com/endpoints) and click on the
Deployment History tab.

##  January 2017

We are changing the behavior of the Extensible Service Proxy (ESP) to deny
cross-origin resource sharing (CORS) requests by default; if you rely on CORS
requests, you must change your configuration to explicitly allow them and
redeploy by January 2, 2017.

**Important:** This announcements affects CORS requests. If you are NOT using
CORS requests to your APIs, please ignore this announcement.  **Important:**
The changes in this release do not effect deployments on Google App Engine
Standard.

###  Background & Current Behavior

With the CORS standard, a browser inserts an extra ` OPTIONS ` request to the
server to determine whether it has permission to perform a cross-origin
request. Currently the ESP always accepts ` OPTIONS ` requests. This means
that currently ESP always allows cross-origin requests through CORS.

###  Upcoming Changes

ESP will allow service producers to specify whether or not to allow cross-
origin traffic. By default, ESP will **block** cross-origin requests by
rejecting all ` OPTIONS ` requests. If you want to allow cross-origin requests
for your API, you will need to add the following snippet to the service's
OpenAPI configuration.

    
    
    ...
    "host": "echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog",
    "x-google-endpoints": [
      {
        "name": "echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog",
        "allowCors": true
      }
    ],
    ...
    

**Important:** This is **a breaking change** . By default ESP will now reject
cross-origin calls unless the above ` "allowCors" ` setting is applied.

###  What You Need to Do

**Note:** This change does not apply to App Engine Standard Environment.
Standard Environment uses Endpoints Frameworks. CORS traffic is allowed on
this platform.

Follow the instructions in the appropriate tab below.

###  App Engine Flex

After ESP 1.0 is released on January 2, 2017, all Flexible Environment API
deployments will feature the new version of ESP and will automatically
disallow CORS requests by default. App Engine applications are automatically
redeployed every 7 days, so sometime in the 7 days following the release of
ESP 1.0, your app will be restarted with the latest version and will
automatically be protected from unintended cross origin sharing.

If you are using Flexible Environments and would like to continue to allow
CORS requests, you must add the "x-google-endpoints" snippet above to your API
configuration (aka OpenAPI specification aka Swagger file). If you are relying
on CORS, we recommend that you add the snippet as soon as possible and
redeploy your service using the following command to avoid service
interruption. Then you will not see changed behavior when the new version of
ESP rolls out.

    
    
    gcloud app deploy app.yaml
    

###  Kubernetes Engine

We plan to introduce this change in the version 1.0 release of ESP on January
2, 2017.

**Note:** If you do not use CORS to allow cross-origin traffic to your API,
you do not need to change your API configuration. You may wish to upgrade your
ESP to block any CORS requests.

If you are currently using CORS to enable cross-origin traffic to your API,
you will need to make changes to your API configuration (aka OpenAPI
specification aka Swagger file) when you upgrade ESP to version 1.0 after
January 2. Add the above "x-google-endpoints" snippets to the OpenAPI config
for your API, and re-deploy your API configuration using the following
command.

    
    
    gcloud service-management deploy openapi.yaml
    

Note that the above step pushed your new service config to the service
manager. Note the new ` SERVICE_CONFIG_ID ` , you will need it in the next
step.

Now you need to redeploy your service. You can use the following command,
replacing ESP-DEPLOYMENT with the deployment name for your service.

    
    
    kubectl edit deployment/ESP-DEPLOYMENT
    

This command opens up your GKE configuration YAML and let you update the
deployment. Make sure to change your version of ESP to 1.0 and update the
SERVICE_CONFIG_ID to the new SERVICE_CONFIG_ID, and save the deployment.

    
    
    containers:
        - name: esp
          image: gcr.io/endpoints-release/endpoints-runtime:1.0
          args: [
            "--http_port", "8080",
            "--backend", "localhost:8081",
            "--service", "SERVICE_NAME",
            "--version", "SERVICE_CONFIG_ID",
          ]
    

###  Compute Engine

We plan to introduce this change in the ESP version 1.0 release on January 2,
2017.

**Note:** If you do not use CORS to allow cross-origin traffic to your API,
you do not need to change your API configuration. You may wish to upgrade your
ESP to block any CORS requests.

If you are currently using CORS to enable cross-origin traffic to your API,
you will need to make changes to your API configuration (aka OpenAPI
specification aka Swagger file) when you upgrade ESP to version 1.0. Add the
above "x-google-endpoints" snippets to the OpenAPI config for your API, and
re-deploy your API configuration using the following command.

gcloud service-management deploy openapi.yaml

Note that the above step pushed your new service config to the service
manager. Note the new ` SERVICE_CONFIG_ID ` , you will need it in the next
step.

Before redeploying your service, you need to update the metadata entries on
the VM with the following command:

    
    
    gcloud compute instances add-metadata --metadata=endpoints-service-name=SERVICE_NAME,endpoints-service-config-id=SERVICE_CONFIG_ID
    

Then you need to SSH to the VM and run the following command to restart ESP.

    
    
    sudo /etc/init.d/nginx restart
    

Alternatively, if you use the start_esp.py script to start ESP (instead of the
init.d script), you can stop ESP and re-run the start_esp.py command with the
updated SERVICE_CONFIG_ID.

###  Compute Engine + Docker

We plan to introduce this change in the version 1.0 release of ESP on January
2, 2017.

**Note:** If you do not use CORS to allow cross-origin traffic to your API,
you do not need to change your API configuration. You may wish to upgrade your
ESP to block any CORS requests.

If you are currently using CORS to enable cross-origin traffic to your API,
you will need to make changes to your API configuration (known as the OpenAPI
specification or Swagger file) when you upgrade ESP to version 1.0. Add the
above ` x-google-endpoints ` snippets to the OpenAPI config for your API, and
re-deploy your API configuration using the following command.

    
    
    gcloud service-management deploy openapi.yaml
    

This pushes your new service config to Google Service Management. That command
will return a new ` SERVICE_CONFIG_ID ` for your API. Note it down because you
will need it in the next step.

Next, redeploy your service. First stop and remove the current ESP instance
(e.g., "esp") using the following commands. You can use ` sudo docker ps `
command to find out the current ESP instance.

    
    
    sudo docker stop esp
    sudo docker rm esp
    

Then, run the following command to redeploy ESP. Make sure to use the new `
SERVICE_CONFIG_ID ` for ` -v ` option.

    
    
    sudo docker run --name=esp -d -p 80:8080 --link=echo:echo gcr.io/endpoints-release/endpoints-runtime:1.0 -s [SERVICE_NAME] -v [SERVICE_CONFIG_ID] -a echo:8081
    

