#  Notas da versão

Nesta página, você encontra as atualizações de produção do Datastore. Acesse-a
periodicamente para ver avisos de recursos novos ou atualizados, correções de
bugs, problemas conhecidos e recursos obsoletos.

É possível ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas da versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt-br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/datastore-release-
notes.xml `

##  June 08, 2020

**FEATURE:**

Support for the [ ` asia-southeast2 ` (Jakarta)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  April 20, 2020

**FEATURE:**

Support for [ ` us-west4 ` region (Las Vegas)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  March 11, 2020

**FEATURE:**

Support for [ ` us-west3 ` (Salt Lake City) and ` asia-northeast3 ` (Seoul)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  February 13, 2020

**FEATURE:**

You can now [ configure indexes with the REST API
](https://cloud.google.com/datastore/docs/configure-indexes-rest-api?hl=pt-br)
.

##  November 18, 2019

**FEATURE:**

You can now [ start managed export and import operations from the Google Cloud
Console ](https://cloud.google.com/datastore/docs/export-import-
entities?hl=pt-br#exporting_all_entities) .

##  April 18, 2019

**FEATURE:**

Support for [ ` asia-northeast2 ` region (Osaka)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  April 15, 2019

**FEATURE:**

Support for [ ` europe-west6 ` region (Zürich)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  January 31, 2019

**FEATURE:**

[ Cloud Firestore is now Generally Available.
](https://cloud.google.com/firestore/docs/release-notes?hl=pt-
br#january_31_2019) Cloud Firestore is the new version of Cloud Datastore and
includes a backwards-compatible [ Datastore mode
](https://cloud.google.com/firestore/docs/firestore-or-datastore?hl=pt-
br#in_datastore_mode) .

If you intend to use the Cloud Datastore API in a new project, use Cloud
Firestore in Datastore mode. Existing Cloud Datastore databases will be [
automatically upgraded to Cloud Firestore in Datastore mode
](https://cloud.google.com/datastore/docs/upgrade-to-firestore?hl=pt-br) .

Except where noted, the Cloud Datastore documentation now describes behavior
for Cloud Firestore in Datastore mode.

##  October 22, 2018

**FEATURE:**

Support for [ ` asia-east2 ` region (Hong Kong)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

**CHANGED:**

Cloud Datastore will soon enforce IAM requirements for all App Engine apps,
see [ Cloud Datastore permissions for App Engine
](https://cloud.google.com/datastore/docs/activate?hl=pt-br#datastore-
permissions-for-app-engine) . Previously, App Engine apps could always access
Cloud Datastore instances in the same project.

Cloud Datastore IAM requirements for App Engine will apply to projects created
after 09/03/2018 and will gradually rollout to existing projects. At a future
date, all projects will enforce Cloud Datastore IAM requirements for App
Engine.

##  October 08, 2018

**FEATURE:**

You can now create a [ Cloud Firestore database in Datastore mode
](https://cloud.google.com/datastore/docs/firestore-or-datastore?hl=pt-
br#choosing_a_database) . Datastore mode allows you to use Cloud Datastore
client libraries with an improved Cloud Firestore storage layer, removing
eventual consistency limitations.

If you have an existing Cloud Datastore project, see this page on the [
automatic upgrade to Cloud Firestore
](https://cloud.google.com/datastore/docs/upgrade-to-firestore?hl=pt-br) .

##  July 10, 2018

**FEATURE:**

Support for [ ` us-west2 ` region (Los Angeles)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  February 28, 2018

**FEATURE:**

General Availability release of the [ Cloud Datastore Administration API v1
](https://cloud.google.com/datastore/docs/reference/admin/rest/v1/projects?hl=pt-
br) , previously in Beta. To learn more about using this service, see:

  * [ Exporting and Importing Entities ](https://cloud.google.com/datastore/docs/export-import-entities?hl=pt-br)
  * [ Scheduling an Export ](https://cloud.google.com/datastore/docs/schedule-export?hl=pt-br)

**DEPRECATED:**

The Cloud Datastore Administration API v1beta1 is now deprecated.

**DEPRECATED:**

The Cloud Datastore Admin backup feature is being phased out in favor of the [
managed export and import ](https://cloud.google.com/datastore/docs/export-
import-entities?hl=pt-br) for Cloud Datastore. Please migrate to the managed
export and import functionality at your earliest convenience. To help you make
the transition, the Datastore Admin backup feature will continue to be
available until February 28, 2019.

##  January 30, 2018

**FEATURE:**

When you begin a transaction with the Cloud Datastore Data API, you can now
use a [ ` TransactionOptions `
](https://cloud.google.com/datastore/docs/reference/data/rest/v1/projects/beginTransaction?hl=pt-
br#TransactionOptions) object to specify whether the transaction is read-only
or read-write.

**FEATURE:**

When you begin a read-write transaction with the Cloud Datastore Data API, you
can now specify a [ ` previousTransaction `
](https://cloud.google.com/datastore/docs/reference/data/rest/v1/projects/beginTransaction?hl=pt-
br#ReadWrite) that you are retrying.

**CHANGED:**

Message [ ` BeginTransactionRequest `
](https://cloud.google.com/datastore/docs/reference/data/rest/v1/projects/beginTransaction?hl=pt-
br) adds field ` transactionOptions ` as part of the Data API.

##  January 10, 2018

**FEATURE:**

Support for [ ` northamerica-northeast1 ` region (Montréal)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  October 31, 2017

**FEATURE:**

Support for [ ` asia-south1 ` region (Mumbai)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  September 05, 2017

**FEATURE:**

Support for [ ` southamerica-east1 ` region (São Paulo)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  August 30, 2017

**FEATURE:**

Initial Beta release of the Cloud Datastore Administration API v1.

Additions to the API definition:

  * Methods for exporting and importing entities. 
    * [ export ](https://cloud.google.com/datastore/docs/reference/admin/rest/v1beta1/projects/export?hl=pt-br)
    * [ import ](https://cloud.google.com/datastore/docs/reference/admin/rest/v1beta1/projects/import?hl=pt-br)
  * Methods for managing long-running operations. 
    * [ cancel ](https://cloud.google.com/datastore/docs/reference/rest/v1/projects.operations/cancel?hl=pt-br)
    * [ delete ](https://cloud.google.com/datastore/docs/reference/rest/v1/projects.operations/delete?hl=pt-br)
    * [ get ](https://cloud.google.com/datastore/docs/reference/rest/v1/projects.operations/get?hl=pt-br)
    * [ list ](https://cloud.google.com/datastore/docs/reference/rest/v1/projects.operations/list?hl=pt-br)

Additions to the ` gcloud ` command-line tool effective in [ version 169.0.0
](https://cloud.google.com/sdk/docs/release-notes?hl=pt-br#16900_2017-08-30) :

  * ` gcloud beta datastore export ` has been added to support exporting entities 
  * ` gcloud beta datastore import ` has been added to support importing entities 
  * ` gcloud beta datastore operations cancel ` has been added to support canceling long-running operations 
  * ` gcloud beta datastore operations delete ` has been added to support deleting long-running operations 
  * ` gcloud beta datastore operations describe ` has been added to support describing a completed long-running operation 
  * ` gcloud beta datastore operations list ` has been added to support listing active long-running operations 

##  August 01, 2017

**FEATURE:**

Support for [ ` europe-west3 ` region (Frankfurt)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  July 18, 2017

**FEATURE:**

Support for [ ` australia-southeast1 ` region (Sydney)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  June 06, 2017

**FEATURE:**

Support for [ ` europe-west2 ` region (London)
](https://cloud.google.com/datastore/docs/locations?hl=pt-br) .

##  August 16, 2016

**FEATURE:**

Initial release of Cloud Datastore API v1.

**CHANGED:**

Message ` EntityResult ` adds field ` version ` as part of API v1 and API
v1beta3.

**CHANGED:**

Error handling in Cloud Datastore API v1:

  * Attempting to insert an entity that already exists will return error code ` ALREADY_EXISTS ` . In v1beta3, it returned ` INVALID_ARGUMENT ` . 
  * Attempting to update an entity that does not exist will return error code ` NOT_FOUND ` . In v1beta3, it returned ` INVALID_ARGUMENT ` . 

**DEPRECATED:**

Because Cloud Datastore API v1 is released, Cloud Datastore API v1beta3 is now
deprecated.

##  April 01, 2016

**CHANGED:**

  * Initial release of Cloud Datastore API v1beta3. 
  * Changes to the API definition: 
    * The API is now defined in three proto files: ` entity.proto ` , ` query.proto ` , and ` datastore.proto ` . 
    * The proto files now use proto3 syntax: 
      * Maps are used for several fields (see below for details). 
      * All enums add a value with suffix ` _UNSPECIFIED ` that is equal to 0. 
      * ` oneof ` is used to prevent setting mutually-exclusive fields: 
        * Fields ` id ` and ` name ` in message ` PathElement ` . 
        * The value fields in message ` Value ` . 
        * Fields ` composite_filter ` and ` property_filter ` in type ` Filter ` . 
        * Fields ` value ` and ` cursor ` in message ` GqlQueryParameter ` . 
        * Fields ` upsert ` , ` update ` , ` upsert ` , and ` delete ` in message ` Mutation ` . 
    * All request messages add a top-level field ` project_id ` . This field is populated automatically for requests made over HTTP. 
    * Several repeated fields now have plural names: 
      * In message ` CompositeFilter ` , ` filter ` is now ` filters ` . 
      * In message ` QueryResultBatch ` , ` entity_result ` is now ` entity_results ` . 
      * In message ` LookupRequest ` , ` key ` is now ` keys ` . 
      * In message ` AllocateIdsRequest ` , ` key ` is now ` keys ` . 
      * In message ` AllocateIdsResponse ` , ` key ` is now ` keys ` . 
    * The proto package name now includes the API version. 
    * In message ` PartitionId ` : 
      * Field ` dataset_id ` is now ` project_id ` . ` project_id ` never includes the app/project ID "prefix" (e.g. "s~"). This fixes [ https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/59 ](https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/59) . 
      * Field ` namespace ` is now ` namespace_id ` . 
    * In message ` Key ` , field ` path_element ` is now ` path ` . 
    * In message ` Value ` : 
      * Null values are represented by explicitly setting field ` null_value ` with type ` com.protobuf.NullValue ` . This fixes [ https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/41 ](https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/41) . 
      * Field ` timestamp_microseconds_value ` is now ` timestamp_value ` with type ` google.protobuf.Timestamp ` . In JSON, the field ` dateTimeValue ` is now ` timestampValue ` . This field is still limited to microsecond precision. 
      * Field ` blob_key_value ` is removed. Values that previously populated that field in the v1beta1 or v1beta2 APIs will instead populate field ` string_value ` in the v1beta3 API. 
      * Field ` geo_point_value ` of type ` google.type.LatLng ` is added. 
      * Repeated field ` list_value ` is replaced with ` array_value ` of type ` ArrayValue ` . 
      * Field ` indexed ` , which defaulted to true, is now ` exclude_from_indexes ` , which defaults to false. 
    * Message ` Property ` is removed. In message ` Entity ` , repeated field ` property ` is now field ` properties ` which is a map from ` string ` to ` Value ` . 
    * Message ` PropertyExpression ` is now ` Projection ` . 
    * Message ` EntityResult ` adds a field ` cursor ` of type ` bytes ` . 
    * In message ` Query ` : 
      * Field ` group_by ` is now ` distinct_on ` . 
      * Field ` limit ` is now of type ` google.protobuf.Int32Value ` . 
    * In message ` PropertyExpression ` , enum ` AggregationFunction ` and field ` aggregation_function ` are removed. 
    * In messages ` CompositeFilter ` and ` PropertyFilter ` , field ` operator ` is now ` op ` . 
    * In message ` GqlQuery ` : 
      * Field ` allow_literal ` is now ` allow_literals ` . 
      * Repeated field ` name_arg ` is now map field ` named_bindings ` . 
      * Field ` number_arg ` is now ` positional_bindings ` . 
    * Message ` GqlQueryArg ` is now ` GqlQueryParameter ` . Field ` name ` is removed. 
    * Enum ` MoreResultsType ` adds a new value ` MORE_RESULTS_AFTER_CURSOR ` . 
    * Message ` QueryResultBatch ` adds field ` skipped_cursor ` . 
    * In message ` Mutation ` : 
      * A ` Mutation ` now describes one change to one single entity. Its fields are no longer repeated. 
      * Field ` insert_auto_id ` is removed. ` insert ` and ` update ` mutations now support auto ID allocation. 
      * Field ` force ` is removed. 
    * In message ` MutationResult ` : 
      * Field ` index_updates ` is moved to message ` CommitResponse ` . 
      * Repeated field ` insert_auto_id_key ` is now ` key ` and is no longer repeated. 
    * Message ` RunQueryResponse ` adds field ` query ` . When a ` RunQueryRequest ` message sets field ` gql_query ` , the ` RunQueryResponse ` message sets field ` query ` to the parsed form of the ` GqlQuery ` message from the request. 
    * In message ` BeginTransactionRequest ` , enum ` IsolationLevel ` and field ` isolation_level ` are removed. All transactions are now serializable. 
    * In message ` CommitRequest ` , field ` mutation ` is now repeated field ` mutations ` . 
    * In message ` CommitResponse ` , field ` mutation_result ` is now repeated field ` mutation_results ` . 
  * Changes to the JSON API: 
    * Null values are now supported. This fixes [ https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/41 ](https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/41) . 
    * Fields set to their default values are not included in responses, for example: 
      * Fields ` found ` , ` missing ` , and ` deferred ` in message to ` LookupResponse ` are not included when they are empty. 
      * Field ` entity_result ` in message ` QueryResultBatch ` is not included when it is empty. 
      * Field ` skipped_results ` in message ` QueryResultBatch ` is not included when it is 0. 
  * The API endpoint format has changed. For example, in v1beta2, a ` RunQuery ` is sent to: ` https://www.googleapis.com/datastore/v1beta2/datasets/<dataset-id>/runQuery ` In v1beta3, it is sent to: ` https://datastore.googleapis.com/v1beta3/projects/<project-id>:runQuery `
  * Account domain restrictions no longer apply when accessing the API. This fixes [ https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/19 ](https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/19) . 
  * Errors: 
    * JSON errors add a ` status ` field and remove the ` errors ` list. 
    * Errors resulting from requests with a content type of ` application/x-protobuf ` are now a serialized ` google.rpc.Status ` message. 
  * Changes to GQL: 
    * In synthetic literal ` KEY ` , ` DATASET ` is now ` PROJECT ` . 
    * The ` BLOBKEY ` synthetic literal is removed. 
    * The ` FIRST ` aggregator is removed. 
    * The ` GROUP BY ` clause is replaced with ` DISTINCT ON ` . 
    * Fully-qualified property names are now supported. 
    * Query filters on timestamps prior to the epoch are now supported. 
  * Empty array values are now supported. 
  * Indexing and querying properties inside of entity values is now supported. Values inside entity values are indexed by default. 
  * Key normalization: 
    * In ` Key ` objects in ` RunQueryRequest ` s, key normalization will never set ` partition_id.namespace_id ` , as it previously did under some circumstances. If a key should reference that partition its ` partition_id.namespace_id ` must be explicitly set. 
    * ` Key ` objects with empty ` path ` and empty or unset ` partition_id ` are no longer normalized. 
  * Writes of foreign partition IDs may now fail if the foreign project is not in an active state. For this reason, use of foreign partition IDs is discouraged. 
  * In a non-transactional ` Commit ` requests, no two mutations may affect the same entity. 
  * In transactional ` Commit ` requests, mutations affecting the same entity are applied in the order in which they appear in the request. Certain sequences of mutations affecting the same entity are not permitted. 
  * Field ` more_results ` in message ` QueryResultBatch ` is accurate in more cases. This fixes [ https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/48 ](https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/48) . 
  * The typical number of results returned by a call to ` RunQuery ` is smaller due to a change in server-side batching. As before, clients should not rely on the batch size and instead use cursors to continue queries. 
  * Scope ` https://www.googleapis.com/auth/userinfo.email ` is no longer required. 
  * The API works for projects that have an App Engine domain restriction. This fixes [ https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/19 ](https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/19) . 
  * ` gcd ` tool: 
    * Options ` -d ` , ` --dataset_id ` , and ` --dataset_id_override ` are now ` -p ` , ` --project_id ` , and ` --project_id_override ` , respectively. 
    * Option ` --auth_mode ` is removed. The ` updateindexes ` and ` vacuumindexes ` commands always use OAuth 2.0. 
    * Option ` --auto_generate_indexes ` is now ` --store_index_configuration_on_disk ` . 
    * Index configuration for new projects is now stored in a YAML file: ` <directory>/WEB-INF/index.yaml ` . Index configuration for projects that previously used XML will continue to do so. 

##  September 01, 2013

**CHANGED:**

  * Initial release of Cloud Datastore API v1beta2. 
  * Changes to the API: 
    * ` BlindWrite ` method merged into ` Commit ` . 
    * Added ` list_value ` to ` Value ` and changed ` value ` to a non-repeated field in ` Property ` . 
    * In the JSON API, string constants are now uppercase and underscore-separated instead of camel-cased (e.g. ` LESS_THAN_OR_EQUAL ` instead of ` lessThanOrEqual ` ). 
  * Changes to GQL: 
    * New synthetic literals: ` BLOB ` , ` BLOBKEY ` , ` DATETIME ` , ` KEY ` . 
    * Support for ` IS NULL ` . 
    * Fixed partition ID handling for binding arguments. 
  * Fixed partition ID handling for query requests that include an explicit partition ID. 
  * Fixed scopes in discovery document. This fixes [ https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/9 ](https://github.com/GoogleCloudPlatform/google-cloud-datastore/issues/9) . 

##  July 01, 2013

**CHANGED:**

  * GQL support. 
  * Metadata query support. 
  * ` gcd ` tool: 
    * Microsoft Windows support ( ` gcd.cmd ` ). 
    * Added testing mode option ` --testing ` , which doesn't store data or index configuration on disk and supports fully-consistent non-ancestor queries. This option is useful for unit and integration tests. 
    * More intuitive ` update_indexes ` command (renamed to ` updateindexes ` ). 
    * New ` create ` command and simplified ` start ` command. 
    * Improved integration with existing App Engine applications. 

##  May 01, 2013

**CHANGED:**

  * Initial public beta release (v1beta1) of the Cloud Datastore API. 

