#  Release notes

This page documents production updates to Cloud SQL. You can check this page
for announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/cloud-sql-mysql-release-
notes.xml `

##  June 23, 2020

**FEATURE:**

Committed use discounts (CUDs) are now available to purchase for Cloud SQL.
CUDs provide discounted prices in exchange for your commitment to use a
minimum level of resources for a specified term. With committed use discounts
for Cloud SQL, you can earn a deep discount off your cost of use in exchange
for committing to continuously use database instances in a particular region
for a 1- or 3-year term. See the [ documentation
](https://cloud.google.com/sql/docs/mysql/cud) for more details.

##  June 08, 2020

**FEATURE:**

Support for [ asia-southeast2
](https://cloud.google.com/sql/docs/mysql/locations) region (Jakarta).

##  May 18, 2020

**FEATURE:**

MySQL 5.6 minor version is upgraded to 5.6.42. MySQL 5.7 minor version is
upgraded to 5.7.25.

##  May 04, 2020

**DEPRECATED:**

As [ previously announced ](https://cloud.google.com/sql/docs/mysql/release-
notes#January_29_2019) , Cloud SQL First Generation was deprecated on January
29, 2019. All First Generation instances have been migrated to Second
Generation. In the documentation and in the Google Cloud Console, "MySQL
Second Generation instances" are now referred to simply as "MySQL instances."
For general information about this deprecation, see the existing [ deprecation
notice ](https://cloud.google.com/sql/docs/mysql/deprecation-notice) .

##  April 20, 2020

**FEATURE:**

Support for [ us-west4 ](https://cloud.google.com/sql/docs/mysql/locations)
region (Las Vegas).

##  March 24, 2020

**FEATURE:**

Cloud SQL now supports 96-core machine types for MySQL, Postgres, and SQL
Server instances. For pricing-related information, see the [ Pricing page
](https://cloud.google.com/sql/pricing) .

##  March 16, 2020

**FEATURE:**

Cloud SQL now supports read replicas in a different region than that of the
primary instance, providing additional protection against regional outages and
improving read performance by making replicas available closer to your
application. To get started, see [ Cross-region replicas
](https://cloud.google.com/sql/docs/mysql/replication/cross-region-replicas) .

Cloud SQL instances using [ private IP
](https://cloud.google.com/sql/docs/mysql/private-ip) are now accessible
across regions, at the regular cross-region network egress cost.

##  February 27, 2020

**FEATURE:**

MySQL 5.6.42 is now generally available in Cloud SQL. To start using MySQL
5.6.42, see [ Creating Instances
](https://cloud.google.com/sql/docs/mysql/create-instance) .

##  February 24, 2020

**FEATURE:**

Support for us-west3 region (Salt Lake City).

##  February 06, 2020

**DEPRECATED:**

First Generation instances no longer can be created. As [ previously announced
](https://cloud.google.com/sql/docs/mysql/release-notes#January_29_2019) ,
Cloud SQL First Generation was deprecated on January 29, 2019. To improve
performance, availability, and storage capacity, Cloud SQL Second Generation
has replaced First Generation. For more information, see the existing [
deprecation notice ](https://cloud.google.com/sql/docs/mysql/deprecation-
notice) and, if necessary, the [ information about upgrading an instance
](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen) .

##  January 24, 2020

**FEATURE:**

Support for [ asia-northeast3
](https://cloud.google.com/sql/docs/mysql/locations) region (Seoul).

##  December 17, 2019

**FEATURE:**

Cloud SQL now supports VPC Service Controls, which let you add a service
perimeter around the Cloud SQL Admin API and host project for Cloud SQL
instances to reduce the risk of data exfiltration. To learn more about using
VPC Service Controls with Cloud SQL, see [ Configuring VPC Service Controls
](https://cloud.google.com/sql/docs/postgres/admin-api/configure-service-
controls) .

##  December 13, 2019

**FEATURE:**

You can now use Cloud VPN with Cloud SQL. To get started, see [ Using a VPN
with Cloud SQL ](https://cloud.google.com/sql/docs/postgres/configure-private-
ip#vpn) .

**FEATURE:**

Connection organization policies for Cloud SQL give you the ability to set
policies that control access to and from Cloud SQL instances. To learn more
about this feature, see [ Connection organization policies
](https://cloud.google.com/sql/docs/postgres/connection-org-policy) . To use
this feature, see [ Setting organization policies for Cloud SQL
](https://cloud.google.com/sql/docs/postgres/configure-org-policy) .

##  December 10, 2019

**FEATURE:**

Cloud SQL now offers notifications for upcoming maintenance. See the [
Overview of maintenance on Cloud SQL instances
](https://cloud.google.com/sql/docs/sqlserver/maintenance) . To find out how
to sign up for notifications and check your instances for upcoming
maintenance, see [ Finding and setting maintenance windows
](https://cloud.google.com/sql/docs/sqlserver/set-maintenance-window) .

##  November 25, 2019

**FEATURE:**

Cloud SQL now supports Access Transparency. As part of Google's long-term
commitment to security and transparency, you can use Access Transparency,
which provides you with logs of actions that Google staff have taken when
accessing your data. To learn more about Access Transparency, see the [
Overview of Access Transparency
](https://cloud.google.com/logging/docs/audit/access-transparency-
overview#overview) .

##  November 19, 2019

**FEATURE:**

Cloud SQL now supports customer-managed encryption keys (CMEK). With CMEK, you
can encrypt Cloud SQL instances using a key you manage. To learn more about
CMEK, see the [ Overview of customer managed encryption keys (CMEK)
](https://cloud.google.com/sql/docs/mysql/cmek) . To start using CMEK, see [
Using customer-managed encryption keys (CMEK)
](https://cloud.google.com/sql/docs/mysql/configure-cmek) .

##  October 18, 2019

**FEATURE:**

Cloud SQL Second Generation MySQL instances have a new high availability (HA)
configuration. The new HA configuration, based on Google's [ Regional Disks
](https://cloud.google.com/compute/docs/disks/#repds) , eliminates replication
lag and, combined with automatic failover, provides isolation from many types
of infrastructure, hardware, and software failures. Regional disks also ensure
that all previously committed database transactions are persisted and
available after failover, right up to the time of the failure.

The new high availability configuration is the default. You can continue to
use the API to create instances with the legacy high availability
configuration (using failover replicas) until the upgrade of existing
instances occurs in early 2020. To learn how high availability now works for
Second Generation MySQL instances, see the [ Overview of the high availability
configuration ](https://cloud.google.com/sql/docs/mysql/high-availability) .
To enable high availability on existing instances, or to create new instances
with high availability, see [ Enabling and disabling high availability on an
instance ](https://cloud.google.com/sql/docs/mysql/configure-ha#ha-existing) .

##  June 25, 2019

**FEATURE:**

This release increases the maximum data storage for instances of MySQL (MySQL
Second Generation) and PostgreSQL. The maximum data storage is increased from
10,230 GB to 30,720 GB. For Cloud SQL storage limits, see [ Limits
](https://cloud.google.com/sql/docs/mysql/quotas#limits) . You can limit your
automatic storage increases; see [ Automatic storage increase limit
](https://cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-
increase-limit-2ndgen) .

##  May 24, 2019

**FEATURE:**

Cloud SQL now allows you to specify a location for backups, and to restrict
data to a single region. To learn about custom backup locations, see [ Custom
backup locations ](https://cloud.google.com/sql/docs/mysql/backup-
recovery/backups#custom-backup-location) . To learn how to set a custom
location for a backup, see [ Setting and viewing a custom location for backups
](https://cloud.google.com/sql/docs/mysql/backup-recovery/backing-
up#locationbackups) .

##  April 18, 2019

**FEATURE:**

Support for [ asia-northeast2
](https://cloud.google.com/sql/docs/mysql/locations) region (Osaka, Japan).

##  April 03, 2019

**FEATURE:**

Support added for 122 MySQL flags and 96 PostgreSQL flags. See [ Supported
PostgreSQL Flags ](https://cloud.google.com/sql/docs/postgres/flags#list-
flags-postgres) and [ Supported MySQL Flags
](https://cloud.google.com/sql/docs/mysql/flags#list-flags-mysql) .

##  March 11, 2019

**FEATURE:**

Support for [ europe-west6
](https://cloud.google.com/sql/docs/mysql/locations) region (Zürich,
Switzerland).

##  January 29, 2019

**FEATURE:**

Cloud SQL Second Generation [ is replacing
](https://cloud.google.com/sql/docs/mysql/deprecation-notice) First
Generation. Support for First Generation instances for MySQL is ending March
25th, 2020.

##  December 06, 2018

**FEATURE:**

GA support for [ Private IP connectivity
](https://cloud.google.com/sql/docs/mysql/private-ip) .

##  October 01, 2018

**FEATURE:**

Support for [ asia-east2 region
](https://cloud.google.com/sql/docs/mysql/locations) (Hong Kong).

**FEATURE:**

[ Upgrade to Second Generation
](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen) generally available
for eligible First Generation MySQL instances.

##  September 01, 2018

**FEATURE:**

Beta support for [ private IP
](https://cloud.google.com/sql/docs/mysql/private-ip) (private services
access) connectivity.

**CHANGED:**

[ Proxy version 1.12 ](https://github.com/GoogleCloudPlatform/cloudsql-
proxy/releases/tag/1.12) released.

##  July 01, 2018

**FEATURE:**

Support for [ replication from an external MySQL server to a Cloud SQL Second
Generation replica
](https://cloud.google.com/sql/docs/mysql/replication/replication-from-
external) .

**FEATURE:**

Support for [ us-west2 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (Los Angeles).

##  June 01, 2018

**FEATURE:**

Support for connecting from [ Cloud Functions
](https://cloud.google.com/sql/docs/mysql/connect-functions) Beta  .

**FEATURE:**

Support for [ europe-north1 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (Finland).

**FEATURE:**

Support for [ rotating SSL certificates
](https://cloud.google.com/sql/docs/mysql/configure-ssl-instance#how-rotation-
works) .

##  May 01, 2018

**FEATURE:**

Support for [ asia-southeast1 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (Singapore).

##  March 01, 2018

**FEATURE:**

Support for [ europe-west4 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (Netherlands).

##  February 01, 2018

**CHANGED:**

[ Maximum concurrent connections to App Engine
](https://cloud.google.com/sql/docs/mysql/faq#sizeqps) updated from 12 to 60.

##  January 01, 2018

**CHANGED:**

MySQL 5.6 minor version upgraded to 5.6.36.

**FEATURE:**

Support for [ northamerica-northeast1 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (Montréal).

**CHANGED:**

Connection limits for PostgreSQL instances changed. [ Learn more
](https://cloud.google.com/sql/docs/mysql/faq#sizeqps) .

##  November 01, 2017

**FEATURE:**

Beta support for [ the high availability configuration
](https://cloud.google.com/sql/docs/postgres/high-availability) and [
replication ](https://cloud.google.com/sql/docs/postgres/replication/create-
replica) for PostgreSQL instances.

##  October 01, 2017

**FEATURE:**

Support for [ asia-south1 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (Mumbai).

**CHANGED:**

[ Proxy version 1.11 ](https://github.com/GoogleCloudPlatform/cloudsql-
proxy/releases/tag/1.11) released.

##  September 01, 2017

**FEATURE:**

Support for 64-core [ machine types
](https://cloud.google.com/sql/docs/mysql/instance-settings#machine-
type-2ndgen) for MySQL instances and 64 cores for PostgreSQL instances.

**FEATURE:**

Support for [ southamerica-east1 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (São Paulo).

##  August 01, 2017

**FEATURE:**

Support for [ europe-west3 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (Frankfurt).

##  June 01, 2017

**FEATURE:**

Support for [ labels ](https://cloud.google.com/sql/docs/mysql/label-instance)
.

**CHANGED:**

[ Proxy version 1.10 ](https://github.com/GoogleCloudPlatform/cloudsql-
proxy/releases) released.

**FEATURE:**

Support for the [ JDBC Socket Library for PostgreSQL
](https://cloud.google.com/sql/docs/mysql/connect-external-app#java) .

**FEATURE:**

Support for [ australia-southeast1 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (Sydney).

**FEATURE:**

Support for [ europe-west2 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (London).

**FEATURE:**

Support for the following PostgreSQL [ extensions
](https://cloud.google.com/sql/docs/postgres/extensions) : ` btree-gin ` , `
btree-gist ` , ` chkpass ` , ` citext ` , ` cube ` , ` dict_int ` , `
dict_xsyn ` , ` earthdistance ` , ` intagg ` , ` intarray ` , ` isn ` , `
ltree ` , ` pgstattuple ` , ` pg_trgm ` , ` tablefunc ` , ` tsm_system_rows `
, ` tsm_system_time ` , ` unaccent ` , ` uuid-ossp ` .

##  May 01, 2017

**FEATURE:**

GA support for Second Generation and PostgreSQL instances in version 157.0.0
of the ` gcloud ` command-line tool. The ` beta ` version is no longer
required for these instances.

**FEATURE:**

Support for [ us-west1 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (Oregon).

**FEATURE:**

Support for [ us-east4 region
](https://cloud.google.com/sql/docs/mysql/instance-locations) (Northern
Virginia).

##  April 01, 2017

**CHANGED:**

[ Proxy version 1.09 ](https://github.com/GoogleCloudPlatform/cloudsql-
proxy/releases) released.

##  March 01, 2017

**FEATURE:**

[ Cloud SQL for PostgreSQL
](https://cloud.google.com/sql/docs/postgres/features/#postgres) Beta
availability.

To provide feedback on the beta release, go to [ our Cloud SQL user forum
](https://googlecloudplatform.uservoice.com/forums/302613-cloud-sql) .

**FEATURE:**

Support for 32-core [ machine types
](https://cloud.google.com/sql/docs/mysql/instance-settings#machine-
type-2ndgen) for MySQL instances.

**FEATURE:**

Support for making MySQL general and slow query log files [ available through
the Stackdriver Log Viewer
](https://cloud.google.com/sql/docs/mysql/flags#tips-general-log) .

##  February 01, 2017

**FEATURE:**

Support for [ Identity and Access Management ](https://cloud.google.com/iam/)
(IAM) [ predefined roles ](https://cloud.google.com/sql/docs/mysql/project-
access-control) .

##  December 01, 2016

**FEATURE:**

Support for administration of [ users
](https://cloud.google.com/sql/docs/mysql/create-manage-users) and [ databases
](https://cloud.google.com/sql/docs/mysql/create-manage-databases) for Second
Generation instances in the Google Cloud Console and the Cloud SQL API.

##  November 01, 2016

**FEATURE:**

Support for [ Northeastern Asia Pacific region
](https://cloud.google.com/sql/docs/mysql/instance-locations) ( ` asia-
northeast1 ` ).

**CHANGED:**

MySQL 5.7 minor version upgraded to 5.7.14.

##  August 01, 2016

**FEATURE:**

[ Cloud SQL Second Generation
](https://cloud.google.com/sql/docs/mysql/1st-2nd-gen-differences) General
Availability.

  * Up to [ 16 cores and 104 GB RAM ](https://cloud.google.com/sql/pricing/#machine-types-pricing) . 
  * [ SSD or HDD storage option ](https://cloud.google.com/sql/docs/mysql/instance-settings#storage-type-2ndgen) with optional [ automatic storage increase capability ](https://cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen) . 
  * Optional [ high availability configuration ](https://cloud.google.com/sql/docs/mysql/high-availability) (recommended for all production instances). 
  * Configurable [ maintenance window ](https://cloud.google.com/sql/docs/mysql/instance-settings#maintenance-window-2ndgen) and [ maintenance timing ](https://cloud.google.com/sql/docs/mysql/instance-settings#maintenance-timing-2ndgen) . 
  * MySQL compatibility: 
    * MySQL 5.6 (5.6.31) and 5.7 (5.7.11) 
    * [ InnoDB storage engine ](https://dev.mysql.com/doc/refman/5.7/en/innodb-storage-engine.html)
    * [ GTID support ](https://dev.mysql.com/doc/refman/5.7/en/replication-gtids.html)

