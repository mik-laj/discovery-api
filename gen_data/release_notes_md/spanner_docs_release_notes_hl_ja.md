#  リリースノート

このページには Cloud Spanner
に関する本番環境の更新内容が記載されています。このページを定期的にチェックして、新機能や更新された機能、バグ修正、既知の問題、非推奨になった機能に関するお知らせを確認してください。

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/spanner-release-notes.xml `
を直接追加します。

##  June 08, 2020

**FEATURE:**

A second [ multi-region instance configuration
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-multi-region) is now available in Europe - ` eur5 `
(London/Belgium).

**FEATURE:**

A [ multi-region instance configuration
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-multi-region) is now available in Asia - ` asia1 `
(Tokyo/Osaka).

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Jakarta (asia-southeast2).

##  June 03, 2020

**CHANGED:**

Cloud Spanner SQL now supports the following statistical aggregate functions -
STDDEV, VARIANCE. For more information, see [ Statistical Aggregate Functions
](https://cloud.google.com/spanner/docs/statistical_aggregate_functions?hl=ja)
.

##  May 18, 2020

**FEATURE:**

You can now run SQL queries to retrieve [ transaction statistics
](https://cloud.google.com/spanner/docs/transaction-stats-tables?hl=ja) for
your database over recent one-minute, 10-minute, and one-hour time periods.

##  April 20, 2020

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Las Vegas (us-west4).

##  April 17, 2020

**FEATURE:**

Cloud Spanner Backup and Restore is now [ generally available
](https://cloud.google.com/products?hl=ja#product-launch-stages) , enabling
you to create backups of Cloud Spanner databases on demand, and restore them.
For more information, see [ Backup and Restore
](https://cloud.google.com/spanner/docs/backup?hl=ja) .

**FEATURE:**

Query Optimizer Versioning is now [ generally available
](https://cloud.google.com/products?hl=ja#product-launch-stages) , enabling
you to select which version of the optimizer to use for your database,
application or query. For more information, see [ Query optimizer
](https://cloud.google.com/spanner/docs/query-optimizer/overview?hl=ja) .

##  April 01, 2020

**FEATURE:**

A [ beta ](https://cloud.google.com/products/?hl=ja#product-launch-stages)
version of the Cloud Spanner emulator is now available, enabling you to
develop and test Cloud Spanner applications locally. For more information, see
[ Using the Cloud Spanner Emulator
](https://cloud.google.com/spanner/docs/emulator?hl=ja) .

##  March 19, 2020

**FEATURE:**

The open-source [ C++ client library for Cloud Spanner
](https://github.com/googleapis/google-cloud-cpp-spanner) is now available. To
get started using C++ with Cloud Spanner, [ see this tutorial
](https://cloud.google.com/spanner/docs/getting-started/cpp?hl=ja) .

##  March 05, 2020

**FEATURE:**

Foreign keys is now [ generally available
](https://cloud.google.com/terms/launch-stages?hl=ja) . For more information,
see [ Foreign keys overview ](https://cloud.google.com/spanner/docs/foreign-
keys/overview?hl=ja) .

##  February 24, 2020

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Salt Lake City (us-west3).

##  January 24, 2020

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Seoul (asia-northeast3).

##  December 18, 2019

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Frankfurt ( ` europe-west3 ` ).

##  November 25, 2019

**FEATURE:**

SQL queries now support the [ ` WITH ` clause
](https://cloud.google.com/spanner/docs/query-syntax?hl=ja#with-clause) . This
clause lets you bind the results of subqueries to temporary tables which makes
it easier to structure complex queries and optimize them for a faster
execution time.

##  October 16, 2019

**FEATURE:**

If you would like to use [ Hibernate ORM ](https://hibernate.org/orm/) with
Cloud Spanner, we now provide a guide to [ help you connect Hibernate ORM to
Cloud Spanner ](https://cloud.google.com/spanner/docs/use-hibernate?hl=ja) .

##  September 25, 2019

**CHANGED:**

All Cloud Spanner instances, including 1-node and 2-node instances, are now
covered under the [ Service Level Agreement (SLA)
](https://cloud.google.com/spanner/sla?hl=ja) . Cloud Spanner now supports
99.99% monthly uptime percentage for all regional instances and 99.999%
monthly uptime percentage for all multi-region instances under the Cloud
Spanner SLA, regardless of instance size.

##  August 09, 2019

**CHANGED:**

The Google Cloud Platform Console no longer provides a chart that shows the
stacked throughput, by region, for instances with multi-region configurations.
Instead, you can use the chart that shows total throughput for all regions. [
Learn more about monitoring with the GCP Console
](https://cloud.google.com/spanner/docs/monitoring-console?hl=ja) .

##  August 07, 2019

**FEATURE:**

An [ open-source JDBC driver ](https://cloud.google.com/spanner/docs/open-
source-jdbc?hl=ja) for Cloud Spanner is now available. This open-source driver
enables Java applications to access Cloud Spanner through the Java Database
Connectivity (JDBC) API.

##  July 31, 2019

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in São Paulo ( ` southamerica-
east1 ` ).

##  June 26, 2019

**FEATURE:**

You can now [ import and export Cloud Spanner data in CSV format
](https://cloud.google.com/spanner/docs/import-export-csv?hl=ja) . You can use
this feature to copy CSV data between Cloud Spanner and traditional relational
database management systems, in combination with tools such as the ` mysqldump
` tool for MySQL, the ` COPY ` statement for PostgreSQL, or the ` bcp ` tool
for Microsoft SQL Server.

**CHANGED:**

If you write your applications in Java with the [ Spring Framework
](https://spring.io/projects/spring-framework) , we now provide a guide to
help you [ add Spring Data Cloud Spanner to your application
](https://cloud.google.com/spanner/docs/adding-spring?hl=ja) . Spring Data
Cloud Spanner can make it easier and more efficient to work with Cloud
Spanner.

##  June 21, 2019

**FEATURE:**

For SQL queries, Cloud Spanner now automatically uses any [ secondary indexes
](https://cloud.google.com/spanner/docs/secondary-indexes?hl=ja) that are
likely to make the query more efficient.

If you notice a performance regression in an existing query, [ follow these
troubleshooting steps ](https://cloud.google.com/spanner/docs/troubleshooting-
performance-regressions?hl=ja) , and [ get support
](https://cloud.google.com/spanner/docs/getting-support?hl=ja) if you cannot
resolve the issue.

##  May 15, 2019

**FEATURE:**

The Google Cloud Platform Console and the Stackdriver Monitoring console now
provide [ latency charts
](https://cloud.google.com/spanner/docs/latency?hl=ja) for Cloud Spanner. Use
these charts to help you troubleshoot performance issues.

##  April 30, 2019

**FEATURE:**

The Google Cloud Platform Console and the Stackdriver Monitoring console now
provide [ CPU utilization charts ](https://cloud.google.com/spanner/docs/cpu-
utilization?hl=ja) for additional CPU utilization metrics. You can also [ set
up alerts in Stackdriver Monitoring
](https://cloud.google.com/spanner/docs/monitoring-stackdriver?hl=ja#create-
alert) to track these metrics.

##  April 18, 2019

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Osaka ( ` asia-northeast2 ` ).

##  March 14, 2019

**FEATURE:**

Cloud Spanner now allows you to send multiple DML statements in one
transaction using [ batch DML ](https://cloud.google.com/spanner/docs/dml-
tasks?hl=ja#use-batch) .

##  March 11, 2019

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Zürich ( ` europe-west6 ` ).

##  February 01, 2019

**FEATURE:**

Published new documentation for migrating data to Cloud Spanner:

  * [ Migrating from DynamoDB to Cloud Spanner ](https://cloud.google.com/solutions/migrating-dynamodb-to-cloud-spanner?hl=ja)
  * [ Migrating from MySQL to Cloud Spanner ](https://cloud.google.com/solutions/migrating-mysql-to-spanner?hl=ja)
  * [ Migrating from an Oracle OLTP system to Cloud Spanner ](https://cloud.google.com/solutions/migrating-oracle-to-cloud-spanner?hl=ja)
  * [ Migrating from PostgreSQL to Cloud Spanner ](https://cloud.google.com/spanner/docs/migrating-postgres-spanner?hl=ja)

##  January 17, 2019

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in London ( ` europe-west2 ` ).

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Sydney ( ` australia-southeast1
` ).

##  January 11, 2019

**FEATURE:**

Cloud Spanner now supports [ importing data from other databases
](https://cloud.google.com/spanner/docs/import-non-spanner?hl=ja) using the [
Avro to Cloud Spanner template
](https://cloud.google.com/dataflow/docs/guides/templates/provided-
batch?hl=ja#gcsavrotocloudspanner) .

##  December 06, 2018

**FEATURE:**

Announced general availability of the [ Java client library
](https://cloud.google.com/spanner/docs/reference/libraries?hl=ja) for Cloud
Spanner.

##  November 26, 2018

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Hong Kong ( ` asia-east2 ` ).

##  November 13, 2018

**FEATURE:**

The GCP Console now displays [ query statistics
](https://cloud.google.com/spanner/docs/query-statistics?hl=ja) , as measured
by CPU usage, for Cloud Spanner queries over recent one-minute, 10-minute,
one-hour, and one-day time periods. You can also run SQL queries over the [
SPANNER_SYS ](https://cloud.google.com/spanner/docs/query-stats-tables?hl=ja)
tables to retrieve recent query statistics.

##  October 29, 2018

**FEATURE:**

Cloud Spanner [ multi-region instance configurations
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-multi-region) can now be created in Europe ( ` eur3 ` ).

##  October 26, 2018

**FEATURE:**

The gcloud command-line tool includes beta support for [ inserting, updating,
and deleting table rows ](https://cloud.google.com/spanner/docs/modify-
gcloud?hl=ja#modifying_data_using_dml) using Partitioned DML.

##  October 22, 2018

**FEATURE:**

Cloud Spanner [ multi-region instance configurations
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-multi-region) can now be created in a second multi-region
instance configuration in North America ( ` nam6 ` ).

##  October 10, 2018

**FEATURE:**

Cloud Spanner now supports [ Data Manipulation Language (DML)
](https://cloud.google.com/spanner/docs/dml-tasks?hl=ja) statements, including
[ Partitioned DML ](https://cloud.google.com/spanner/docs/dml-
partitioned?hl=ja) .

##  August 17, 2018

**FEATURE:**

You can now use the REST API or the ` gcloud ` command-line tool to [ export
](https://cloud.google.com/dataflow/docs/guides/templates/provided-
batch?hl=ja#cloudspannertogcsavro) and [ import
](https://cloud.google.com/dataflow/docs/guides/templates/provided-
batch?hl=ja#gcsavrotocloudspanner) Cloud Spanner databases.

##  July 12, 2018

**FEATURE:**

Cloud Spanner now supports [ exporting
](https://cloud.google.com/spanner/docs/export?hl=ja) and [ importing
](https://cloud.google.com/spanner/docs/import?hl=ja) databases using the GCP
Console.

##  July 10, 2018

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Los Angeles ( ` us-west2 ` ).

##  June 11, 2018

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Finland ( ` europe-north1 ` ).

##  June 06, 2018

**CHANGED:**

Published new and updated documentation for designing and updating schemas:

  * [ Schema and data model ](https://cloud.google.com/spanner/docs/schema-and-data-model?hl=ja)
  * [ Schema design ](https://cloud.google.com/spanner/docs/schema-design?hl=ja)
  * [ Schema updates ](https://cloud.google.com/spanner/docs/schema-updates?hl=ja)

##  May 10, 2018

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Singapore ( ` asia-southeast1 `
).

##  April 26, 2018

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Oregon ( ` us-west1 ` ).

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in South Carolina ( ` us-east1 `
).

##  April 24, 2018

**FEATURE:**

The gcloud command-line tool includes beta support for [ inserting, updating,
and deleting rows ](https://cloud.google.com/spanner/docs/modify-gcloud?hl=ja)
in a table.

##  March 28, 2018

**FEATURE:**

Cloud Spanner now supports the [ commit timestamp column option
](https://cloud.google.com/spanner/docs/commit-timestamp?hl=ja) that you can
use to automatically write the commit timestamp of a transaction into a
column.

##  March 15, 2018

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in the Netherlands ( ` europe-
west4 ` ).

##  March 02, 2018

**FEATURE:**

Cloud Spanner now supports [ reading and querying data in parallel
](https://cloud.google.com/spanner/docs/reads?hl=ja#read_data_in_parallel)
with multiple workers using the client libraries for Node.js and Ruby.

##  February 27, 2018

**FEATURE:**

Cloud Spanner now supports [ reading and querying data in parallel
](https://cloud.google.com/spanner/docs/reads?hl=ja#read_data_in_parallel)
with multiple workers using the client libraries for C#, Go, Java, and PHP.

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Montréal ( ` northamerica-
northeast1 ` ).

##  February 20, 2018

**FEATURE:**

Cloud Spanner now supports both Admin Activity and Data Access [ audit logs
](https://cloud.google.com/spanner/docs/audit-logging?hl=ja) as a part of
Stackdriver Logging.

##  January 31, 2018

**FEATURE:**

Announced general availability of [ IAM custom roles
](https://cloud.google.com/spanner/docs/iam?hl=ja#custom-roles) for Cloud
Spanner.

##  January 18, 2018

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Northern Virginia ( ` us-east4
` ) and Mumbai ( ` asia-south1 ` ).

##  November 14, 2017

**FEATURE:**

Cloud Spanner [ multi-region instance configurations
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-multi-region) are now available. Multi-region instances can now
be created in one continent (nam3) or three continents (nam-eur-asia1).

##  June 15, 2017

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances?hl=ja#available-
configurations-regional) can now be created in Tokyo ( ` asia-northeast1 ` ).

##  May 16, 2017

**FEATURE:**

Announced general availability of the Cloud Spanner API.

**FEATURE:**

Newly published documentation: [ SQL best practices
](https://cloud.google.com/spanner/docs/sql-best-practices?hl=ja) , [ Working
with arrays in SQL ](https://cloud.google.com/spanner/docs/arrays?hl=ja) , [
Using Cloud Spanner with Cloud Functions
](https://cloud.google.com/spanner/docs/use-cloud-functions?hl=ja) , [
Monitoring using Stackdriver
](https://cloud.google.com/spanner/docs/monitoring?hl=ja) , [ Applying IAM
Roles for databases, instances, and projects
](https://cloud.google.com/spanner/docs/grant-permissions?hl=ja) , [
Integrating with other Google Cloud Platform services
](https://cloud.google.com/spanner/docs/integrate-google-cloud-platform?hl=ja)
.

##  February 14, 2017

**FEATURE:**

Initial Beta release of Cloud Spanner API.

**ISSUE:**

The version of the gcloud command-line tool that supports Cloud Spanner is
being rolled out. It is expected to be completely available by February 16,
2017.

**ISSUE:**

The Cloud Spanner UI in the Google Cloud Platform Console is being rolled out
and will be available shortly.

