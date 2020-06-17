#  Notas de la versión

Esta página contiene actualizaciones de producción y anuncios de funciones
para el servicio de Pub/Sub. Si quieres obtener actualizaciones de
lanzamientos de [ bibliotecas cliente
](https://cloud.google.com/pubsub/docs/reference/libraries?hl=es-419) de
Pub/Sub para lenguajes específicos, usa los vínculos siguientes: [ C#
](https://github.com/googleapis/google-cloud-dotnet/releases) , [ Go
](https://github.com/googleapis/google-cloud-go/releases) , [ Java
](https://github.com/googleapis/java-pubsub/releases) , [ Node.js
](https://github.com/googleapis/nodejs-pubsub/releases) , [ PHP
](https://github.com/googleapis/google-cloud-php/releases) , [ Python
](https://github.com/googleapis/python-pubsub/releases) y [ Ruby
](https://github.com/googleapis/google-cloud-ruby/releases) .

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) o agrega
directamente la URL del feed: ` https://cloud.google.com/feeds/pubsub-release-
notes.xml ` .

##  June 16, 2020

**FEATURE:**

[ Retry policies for Pub/Sub subscriptions
](https://cloud.google.com/pubsub/docs/admin?hl=es-419#creating_subscriptions)
are now available at the GA launch stage.

##  June 08, 2020

**FEATURE:**

Pub/Sub is now available in the ` asia-southeast2 ` region (Jakarta).

**FEATURE:**

Pub/Sub [ message filtering
](https://cloud.google.com/pubsub/docs/filtering?hl=es-419) is now available
at the [ beta launch stage
](https://cloud.google.com/products/?hl=es-419#product-launch-stages) .

##  May 26, 2020

**FEATURE:**

[ Pub/Sub Lite ](https://cloud.google.com/pubsub/docs/choosing-pubsub-or-
lite?hl=es-419) is now available at the [ beta launch stage
](https://cloud.google.com/products/?hl=es-419#product-launch-stages) .

##  April 20, 2020

**FEATURE:**

Pub/Sub is now available in the ` us-west4 ` region (Las Vegas).

**FEATURE:**

[ Dead-letter topics ](https://cloud.google.com/pubsub/docs/dead-letter-
topics?hl=es-419) for Pub/Sub are now available at the [ General Availability
release level ](https://cloud.google.com/products/?hl=es-419#product-launch-
stages) .

##  February 24, 2020

**FEATURE:**

Cloud Pub/Sub is now available in the ` us-west3 ` region (Salt Lake City).

##  January 24, 2020

**FEATURE:**

Cloud Pub/Sub is now available in the ` asia-northeast3 ` region (Seoul).

##  December 12, 2019

**CHANGED:**

[ Push subscriptions ](https://cloud.google.com/pubsub/docs/push?hl=es-419)
can now send HTTP POST requests to webhook URLs without proof of domain
ownership.

##  September 23, 2019

**FEATURE:**

[ Resource location restrictions
](https://cloud.google.com/pubsub/docs/resource-location-
restriction?hl=es-419) are available for Cloud Pub/Sub at the [ General
Availability release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) . This
feature allows you to manage the location in which your topics' messages are
stored.

##  September 05, 2019

**FEATURE:**

[ Custom-managed encryption keys (CMEK)
](https://cloud.google.com/pubsub/docs/cmek?hl=es-419) are available at the [
General Availability release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) .

##  August 29, 2019

**FEATURE:**

The [ Cloud Pub/Sub Python client library
](https://github.com/googleapis/python-pubsub/tree/master) is available at the
[ General Availability release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) .

##  July 17, 2019

**FEATURE:**

[ Authentication for push subscriptions
](https://cloud.google.com/pubsub/docs/push?hl=es-419#setting_up_for_push_authentication)
is available at the [ General Availability release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) .

**FEATURE:**

[ Resource location restrictions
](https://cloud.google.com/pubsub/docs/resource-location-
restriction?hl=es-419) are available for Cloud Pub/Sub at the [ beta release
level ](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) . This
feature allows you to manage the location in which your topics' messages are
stored.

##  June 26, 2019

**FEATURE:**

[ Custom-managed encryption keys (CMEK)
](https://cloud.google.com/pubsub/docs/cmek?hl=es-419) are in the process of
being rolled out at the [ beta release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) . This
feature will be fully available to Cloud Pub/Sub users as of June 28, 2019.

##  May 16, 2019

**FEATURE:**

The ability to [ modify subscription expiration policies
](https://cloud.google.com/pubsub/docs/admin?hl=es-419#modifying_subscription_expiration_policies)
is now available at the [ General Availability release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) .

##  April 15, 2019

**FEATURE:**

Cloud Pub/Sub is now available in the ` asia-northeast2 ` region (Osaka,
Japan).

##  April 09, 2019

**FEATURE:**

[ Authentication for push subscriptions
](https://cloud.google.com/pubsub/docs/push?hl=es-419#setting_up_for_push_authentication)
is available at the [ beta release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) .

##  March 20, 2019

**FEATURE:**

[ New pricing ](https://cloud.google.com/pubsub/pricing?hl=es-419) has been
announced. The announcement includes a lower base price for in-region users
and new region egress fees.

##  March 11, 2019

**FEATURE:**

Cloud Pub/Sub is now available in the ` europe-west6 ` region (Zürich,
Switzerland).

##  February 05, 2019

**FEATURE:**

[ Seek ](https://cloud.google.com/pubsub/docs/replay-overview?hl=es-419) for
Cloud Pub/Sub is available at the [ General Availability release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) and is
recommended for production loads. The Seek feature extends subscriber
functionality by allowing you to to alter the acknowledgement state of
messages in bulk. For example, you can replay previously acknowledged messages
or discard obsolete messages.

##  October 29, 2018

**FEATURE:**

[ Seek ](https://cloud.google.com/pubsub/docs/replay-overview?hl=es-419) for
Cloud Pub/Sub is available at the [ beta release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) .

##  October 22, 2018

**FEATURE:**

Cloud Pub/Sub is now available in the ` asia-east2 ` region (Hong Kong).

##  September 19, 2018

**FEATURE:**

[ Labels ](https://cloud.google.com/pubsub/docs/labels?hl=es-419) for Cloud
Pub/Sub are available at the [ General Availability release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) and are
recommended for production loads.

##  July 31, 2018

**FEATURE:**

[ Labels ](https://cloud.google.com/pubsub/docs/labels?hl=es-419) for Cloud
Pub/Sub are available at the [ beta release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) .

##  July 10, 2018

**FEATURE:**

Cloud Pub/Sub is now available in the ` us-west2 ` region (Los Angeles).

##  June 11, 2018

**FEATURE:**

Cloud Pub/Sub is now available in the ` europe-north1 ` region (Finland).

##  May 31, 2018

**FEATURE:**

The C#, GO, and Java [ client libraries
](https://cloud.google.com/pubsub/docs/reference/libraries?hl=es-419) are now
at the [ General Availability release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) and are
recommended for production loads.

##  May 23, 2018

**FEATURE:**

[ Audit Logging ](https://cloud.google.com/pubsub/docs/audit-
logging?hl=es-419) for Cloud Pub/Sub is now at the [ General Availability
release level ](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels)
and is recommended for production loads.

##  April 20, 2018

**FEATURE:**

The gRPC service APIs, including StreamingPull, are now available at the [
General Availability release level
](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels) and are
recommended for production loads. Note that the [ Cloud Client Libraries
](https://cloud.google.com/pubsub/docs/reference/libraries?hl=es-419) for
Cloud Pub/Sub already use these APIs.

##  February 20, 2018

**FEATURE:**

Added support for [ generating Google Cloud Audit logs
](https://cloud.google.com/pubsub/docs/audit-logging?hl=es-419) that enable
you to track usage and access.

##  January 24, 2018

**FEATURE:**

The Cloud Pub/Sub ` gcloud ` commands are now at the [ General Availability
release level ](https://cloud.google.com/sdk/gcloud/?hl=es-419#release_levels)
. The ` beta ` label is no longer required.

##  January 10, 2018

**FEATURE:**

Cloud Pub/Sub is now available in the ` europe-west4 ` region (Netherlands).

**FEATURE:**

Cloud Pub/Sub is now available in the ` northamerica-northeast1 ` region
(Montréal).

##  August 30, 2017

**FEATURE:**

The [ StreamingPull API
](https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1?hl=es-419)
is now in Beta. Users of client libraries should see improvements in end-to-
end message latency and CPU utilization without any changes in code after
updating to the most recent version of the client library.

##  August 01, 2017

**FEATURE:**

Cloud Pub/Sub is now available in the ` europe-west3 ` region (Frankfurt).

##  June 20, 2017

**FEATURE:**

Cloud Pub/Sub is now available in the ` australia-southeast1 ` region
(Sydney).

##  June 06, 2017

**FEATURE:**

Cloud Pub/Sub is now available in the ` europe-west2 ` region (London).

##  April 19, 2017

**FEATURE:**

Announced beta availability of [ gRPC
](https://cloud.google.com/pubsub/docs/reference/rpc/?hl=es-419) .

##  January 20, 2017

**CHANGED:**

Published changes to the Cloud Pub/Sub [ pricing model
](https://cloud.google.com/pubsub/pricing?hl=es-419) .

##  December 01, 2015

**FEATURE:**

Support added for quota metrics per topic and subscription ( `
pubsub.googleapis.com/topic/byte_cost ` and `
pubsub.googleapis.com/subscription/byte_cost ` , respectively).

##  November 01, 2015

**FEATURE:**

Added publish timestamp field on pulled messages.

##  June 01, 2015

**FEATURE:**

**Stable API suitable for production development** \- v1 released.

##  February 01, 2015

**FEATURE:**

**Beta release** \- v1beta2 released.

##  November 01, 2014

**FEATURE:**

**Batch request support added** \- Support added for batch Publish and Pull
requests.

##  June 01, 2014

**FEATURE:**

**Initial release** \- v1beta1 released.

