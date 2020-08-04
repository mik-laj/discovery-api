#  Release notes

These release notes apply to the Cloud Composer service. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/composer-release-notes.xml `

##  August 03, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.11.1-airflow-1.10.3 ` , ` composer-1.11.1-airflow-1.10.6 ` , and ` composer-1.11.1-airflow-1.10.9 ` . The default is ` composer-1.11.1-airflow-1.10.6 ` . Upgrade your Cloud SDK to use features in this release. 
  * Composer now enforces ` iam.serviceAccounts.actAs ` permission checks on the service account specified during Composer environment creation. See [ Creating environments ](https://cloud.google.com/composer/docs/how-to/managing/creating#access-control) for details. 

**FEATURE:**

  * Private IP environments can now be creating using non-rfc 1918 CGN ranges (100.64.0.0/10) 
  * New PyPi packages have been added for Composer version composer-1.11.0-airflow-1.10.6. These make it possible to install apache-airflow-backport-providers-google with no additional package upgrades. 
  * The PyPi package ` google-cloud-datacatalog ` can now be installed on Composer environments running Airflow 1.10.6 and Python 3. 
  * Cloud Composer 1.11.1+: Backport providers are installed by default for Airflow 1.10.6 and 1.10.9. 
  * You can now use the ` label.worker_id ` filter in Cloud Monitoring logs to see logs sent out of a specific Airflow worker Pod. 
  * With the Composer Beta API, you can now upgrade an environment to any of the three latest Composer versions (instead of just the latest). 
  * You can now modify these previously blocked Airflow configurations: ` [scheduler] scheduler_heartbeat_sec ` , ` [scheduler] job_heartbeat_sec ` , ` [scheduler] run_duration `

**FIXED:**

  * A more informative error message was added for environment creation failures caused by issues with Cloud SQL instance creation. 
  * Improved error reporting has been added for update operations that change the web server image in cases where the error occurs before the new web server image is created. 
  * The Airflow-worker liveness check has been changed so that a task just added to a queue will not fire an alert. 
  * Reduced the amount of non-informative logs thrown by the environment in Composer 1.10.6. 
  * Improved the syncing procedure for env_var.json in Airflow 1.10.9 (it should no longer throw "missing file:" errors). 
  * Airflow-worker and airflow-scheduler will no longer throw "missing env_var.json" errors in Airflow 1.10.6. 
  * Added validation in the v1 API to provide meaningful error messages when creating an environment with domain restricted sharing. 

##  July 30, 2020

**FEATURE:**

Cloud Composer is now available in Osaka ( ` asia-northeast2 ` ).

##  July 24, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.11.0-airflow-1.10.2 ` , ` composer-1.11.0-airflow-1.10.3 ` , ` composer-1.11.0-airflow-1.10.6 ` , and ` composer-1.11.0-airflow-1.10.9 ` . The default is ` composer-1.11.0-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * Airflow 1.10.9 is now supported. 
  * Environment upgrades have been enabled for the latest two Composer versions (1.11.0 and 1.10.6). 
  * Added a retry feature to the Airflow CeleryExecutor (disabled by default). You can configure the number of times Celery will attempt to execute a task by setting the ` [celery] max_command_attempts ` property. The delay between each retry can also be adjusted with ` [celery] command_retry_wait_duration ` (default: 5 seconds). 

**FIXED:**

  * New PyPi packages have been added for Composer version ` composer-1.11.0-airflow-1.10.6 ` . These make it possible to install ` apache-airflow-backport-providers-google ` with no additional package upgrades. 
  * The PyPi package ` google-cloud-datacatalog ` can now be installed on Composer environments running Airflow 1.10.6 and Python 3. 
  * Fixed synchronization of environment variables to the web server. 
  * Improved error reporting when PyPI package installation fails. 

**DEPRECATED:**

  * Composer versions 1.6.1, 1.7.0, and 1.7.1 are now deprecated. 

##  July 07, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.6-airflow-1.10.2 ` , ` composer-1.10.6-airflow-1.10.3 ` and ` composer-1.10.6-airflow-1.10.6 ` . The default is ` composer-1.10.6-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 

  * **For Airflow 1.10.6 and later:** The Airflow config property ` [celery] pool ` is now blocked. 

  * The ` [core]sql_alchemy_pool_recycle ` Airflow setting has been modified to improve SQL connection reliability. 

**FIXED:**

  * Fixed an issue with Airflow 1.10.6 environments where task logs were not visible in the UI when DAG serialization was enabled. 
  * It is now possible to upgrade from Composer versions 1.1.1, 1.2.0, 1.3.0, 1.4.0, 1.4.1, 1.4.2, 1.5.0, and 1.5.2 to the newest version. 

##  June 30, 2020

**FEATURE:**

Cloud Composer support for [ VPC Service Controls
](https://cloud.google.com/composer/docs/configuring-vpc-sc) is now in Beta.

##  June 24, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.5-airflow-1.10.2 ` , ` composer-1.10.5-airflow-1.10.3 ` and ` composer-1.10.5-airflow-1.10.6 ` . The default is ` composer-1.10.5-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * Composer now uses the Kubernetes v1 API, and is compatible with GKE 1.16 
  * An updated haproxy configuration for Composer increases the maximum number of connections to 2000, and changes load balancing to be based on the number of connections. These settings can be configured with environment variables. 

**FIXED:**

  * Error messages for ` TP_APP_ENGINE_CREATING ` timeout and RPC delivery issues have been expanded. 
  * Airflow Providers can now be installed inside Cloud Composer. 
  * Error handling for rendering templates in the Airflow web server UI has been improved. 
  * Fixed an issue with rendering task instance details (logs, task instance template, params) in the Airflow web server UI when DAG serialization is enabled. 
  * Fixed an issue with ` DataFlowJavaOperator ` , so it can now be used with Apache Beam 2.20. 
  * Improved error reporting for failing operations. 
  * Memory consumption of the ` gcs-syncd ` container is now constrained to prevent system instability. 

##  May 31, 2020

**FEATURE:**

Cloud Composer is now available in Seoul ( ` asia-northeast3 ` ).

##  May 30, 2020

**FEATURE:**

Domain restricted sharing is now generally available (GA). The v1 Composer API
and GCP Console now support [ domain restricted sharing
](https://cloud.google.com/resource-manager/docs/organization-
policy/restricting-domains) for Composer environments.

##  May 26, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.4-airflow-1.10.2 ` , ` composer-1.10.4-airflow-1.10.3 ` and ` composer-1.10.4-airflow-1.10.6 ` . The default is ` composer-1.10.4-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 
  * **For Airflow 1.10.6 and later:** The Airflow config property ` [celery] pool ` is now blocked. 

**FIXED:**

  * Fixed an issue with Airflow 1.10.6 environments where task logs were not visible in the UI when DAG serialization was enabled. 

##  May 15, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.3-airflow-1.10.2 ` , ` composer-1.10.3-airflow-1.10.3 ` and ` composer-1.10.3-airflow-1.10.6 ` . The default is ` composer-1.10.3-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * Resource quota limits have been updated, allowing environment administrators to set quotas with more granularity. The default quotas for read and write operations have also changed; see [ Cloud Composer resource quotas ](https://cloud.google.com/composer/quotas) for details. The old limits are deprecated, but will not be removed from the Cloud Console Quotas page until a future release. 

**CHANGED:**

  * The machine type of the Airflow web server will now be preserved during Composer environment updates, including cases like new PyPi module installations, or adding new environment variables. 
  * Synchronization of log files between the Airflow scheduler, web server and workers has been improved. 
  * More useful error messages have been added for Composer environment upgrade failures. 
  * _Future change:_ Airflow 1.10.6 will become the default Airflow version for Composer environments in an upcoming release. 

**DEPRECATED:**

  * Composer version 1.6.1 has been deprecated. 

##  May 08, 2020

**FEATURE:**

Cloud Composer is now available in Hong Kong ( ` asia-east2 ` ).

**FEATURE:**

Cloud Composer is now available in Las Vegas ( ` us-west4 ` ).

##  April 27, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.2-airflow-1.10.2 ` , ` composer-1.10.2-airflow-1.10.3 ` and ` composer-1.10.2-airflow-1.10.6 ` . The default is ` composer-1.10.2-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 

**FIXED:**

  * Fixed an issue with the CloudSQL Proxy HealthCheck that caused the Proxy Pod to restart repeatedly. 
  * The fluentd spec for in-cluster build log exporting now correctly points to the production fluentd image from ` cloud-airflow-releaser ` . This fix is required for Composer to correctly perform in-cluster builds for VPC SC configuration. 
  * Adjusted ImageBuilder to fix PyPI package installation issues when using VPC SC. 
  * Fixed intermittent issues with ` airflow-monitoring ` during the initialization phase. 
  * Fixed an issue that caused the Airflow scheduler and worker pods to take ~10 minutes to terminate. 
  * Fixed an issue with upgrading the image version and improved error handling during Composer environment upgrades. 

**DEPRECATED:**

  * The oldest supported version of Composer is now ` composer-1.6.0-airflow-x.x.x `

##  April 17, 2020

**BREAKING:**

Composer version 1.10.1 has been rolled back. If you created an environment
with ` composer-1.10.1-airflow-* ` , you can retrieve and delete the
environment, but not update it. We recommend that you delete the environment
and create a new environment with the latest image version. Refer to the March
20, 2020 release notes for default version.

##  April 10, 2020

**FEATURE:**

[ Private IP Composer environments
](https://cloud.google.com/composer/docs/concepts/private-ip) are now
generally available (GA). See [ Configuring private IP
](https://cloud.google.com/composer/docs/how-to/managing/configuring-private-
ip) to learn how to use this feature.

**FEATURE:**

Support for [ Shared VPC networks
](https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-
vpc) is now generally available (GA).

##  April 05, 2020

**FEATURE:**

Cloud Composer is now available in Salt Lake City ( ` us-west3 ` ).

##  March 31, 2020

**FEATURE:**

The new [ Composer monitoring dashboard
](https://cloud.google.com/composer/docs/monitoring-dashboard) is now in beta.

##  March 23, 2020

**FEATURE:**

Cloud Composer is now available in Sao Paulo ( ` southamerica-east1 ` ).

##  March 20, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.0-airflow-1.10.2 ` , ` composer-1.10.0-airflow-1.10.3 ` and ` composer-1.10.0-airflow-1.10.6 ` . The default is ` composer-1.10.0-airflow-1.10.2 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * Improved Composer logs: Composer Agent adds more detailed logs in Cloud Monitoring to describe the current stage of environment creation and provide better error messages if an operation fails. 
  * MySQL passwords are now stored in Kubernetes Secrets instead of the config map. 
  * You can now set the ` core.store_serialized_dags ` property to ` False ` after setting it to ` True ` . (Previously it was not possible to switch back.) 
  * Composer now uses Pip version 19.0.2 for both Python 2 and Python 3 Airflow environments. 
  * Added the Airflow property ` core.store_dag_code ` , which lets you see DAG code in the web UI while VPC-SC is enabled. 
  * New metrics have been added to the monitoring API. [ See the full list here ](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-composer) . 

**FIXED:**

  * Fixed an issue where Airflow database connection errors did not propagate correctly. 
  * Logs from the Composer Agent will now show the correct severity level in Cloud Monitoring. 
  * Fixed an issue where network tags added to environments did not propagate to the node pools created during the in-cluster image building. 
  * The Composer Agent will now wait for ` env_vars ` to be sent before starting the web server. 
  * Backported a fix for SQL proxy, which improves the stability of SQL connections inside workers. 
  * Added new scripts to handle synchronization of files from Customer Project buckets with tenant project buckets in DRS mode, so that DAG synchronization is not affected by long-running logs synchronization. 
  * Fixed an issue that prevented the creation of environments in the same VPC but different regions. 
  * Fixed an issue with updating the node count for Composer environments running versions 1.6.0 to 1.8.2. 
  * Installing PyPI packages from private repositories in the public Internet (specified in the pip.conf file) now works in private IP Composer environments without having to configure Cloud NAT. 

##  March 09, 2020

**FEATURE:**

You can now control access to the Airflow web server, either allowing access
from any IP address (default), or specifying which IP ranges have access. For
details, see [ Creating environments
](https://cloud.google.com/composer/docs/how-
to/managing/creating#creating_a_new_environment) .

##  February 28, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.9.2-airflow-1.10.1 ` , ` composer-1.9.2-airflow-1.10.2 ` , ` composer-1.9.2-airflow-1.10.3 ` and ` composer-1.9.2-airflow-1.10.6 ` . The default is ` composer-1.9.2-airflow-1.10.2 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * (Beta) You can now create private IP Cloud Composer environments that are configured for [ Shared VPC ](https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-vpc) . 

**FIXED:**

  * Fixed an issue with updating Composer environments running versions 1.6.0 to 1.8.2. Updating the node count for an environment is still broken, and will be fixed in a future version. 

    * Workaround: To resize the cluster for an environment using version 1.6.0 - 1.8.2, resize the default node pool in the cluster directly through GKE interface, or delete the Composer environment and recreate it with a different node count. 
  * Fixed an issue with the Dataflow Python hook for Airflow 1.10.6 that restricted it to using Python 2. Dataflow will now use the same Python version as the Composer environment. 

##  February 25, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.9.1-airflow-1.10.1 ` , ` composer-1.9.1-airflow-1.10.2 ` , ` composer-1.9.1-airflow-1.10.3 ` and ` composer-1.9.1-airflow-1.10.6 ` . The default is ` composer-1.9.1-airflow-1.10.2 ` . Upgrade your Cloud SDK to use features in this release. 

**FIXED:**

  * Fixed an issue where updating environment variables cleared the stored Fernet key. 
  * Fixed an issue with running DAGs via the Airflow 1.10.2 REST API when ` dag_serialization ` is turned on. 
  * Fixed an issue with environment creation for Composer versions 1.6.0 to 1.8.2 when using GKE version 1.14. 
  * Improved the health check functionality for SQLProxy. 

##  February 13, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.9.0-airflow-1.10.1 ` , ` composer-1.9.0-airflow-1.10.2 ` , ` composer-1.9.0-airflow-1.10.3 ` and ` composer-1.9.0-airflow-1.10.6 ` . The default is ` composer-1.9.0-airflow-1.10.2 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * [ Airflow 1.10.6 ](https://airflow.apache.org/docs/stable/changelog.html#airflow-1-10-6-2019-10-28) is now available for Composer. 

**CHANGED:**

  * Python 3 is now the default version for new Composer environments. 
  * Airflow 1.9.0 is no longer supported for new Composer environments. 

**FIXED:**

  * Fixed BigQuery operators for Python 3 in Airflow 1.10.6. 
  * Fixed a bug where some deserialized tasks had no ` start_date ` in Airflow 1.10.6. 
  * The Fernet Key is now stored in Kubernetes Secrets instead of the Config Map. 
  * Workers now wait until they have synced with the ` dags ` folder before executing tasks. 
  * New items have been added to the Airflow security properties blacklist in airflow.cfg: ` webserver-auth_backend ` and ` scheduler-auth_backend ` . 
  * Fixed a rare bug where Airflow workers tried to execute tasks before the DAG code was synced to the Airflow worker volume. 

**DEPRECATED:**

  * Composer is planning to deprecate support for Airflow 1.10.1. 
  * In the near future it will not be possible to create Composer environments for Python 2 from the user interface. You will still be able to create Python 2 environments using gcloud. 

##  January 31, 2020

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.8.4-airflow-1.9.0 ` , ` composer-1.8.4-airflow-1.10.1 ` , ` composer-1.8.4-airflow-1.10.2 ` , and ` composer-1.8.4-airflow-1.10.3 ` . The default is ` composer-1.8.4-airflow-1.9.0 ` . Upgrade your Cloud SDK to use features in this release. 

**FIXED:**

  * Deprecation policy update: It is no longer possible to create environments with image versions older than 1 year. Currently the oldest version allowed is composer-1.4.1. 
  * The Python version for Dataflow Operators is no longer hard-coded. Composer users can now use Dataflow Operators with Python 2 and 3. (Airflow 1.10.3 only.) 
  * Fixed an issue with App Engine health check errors when creating environments with Composer version 1.7.5 or lower. 
  * The ` airflow_home configuration ` parameter is no longer added to ` airflow.cfg ` if using Airflow version 1.10.3 or greater. 
  * Airflow 1.10.2 is now the default version used for new Composer environments when Airflow version is not specified. 

##  December 16, 2019

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.8.3-airflow-1.9.0 ` , ` composer-1.8.3-airflow-1.10.1 ` , ` composer-1.8.3-airflow-1.10.2 ` , and ` composer-1.8.3-airflow-1.10.3 ` . The default is ` composer-1.8.3-airflow-1.9.0 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * Composer now uses OpenAPI to manage components running on GKE clusters. This ensures Composer will be compatible with future versions of GKE. 

**FIXED:**

  * Fixed the formatting for validation errors returned by the ` projects.locations.environments.create ` API method. 

##  November 25, 2019

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.8.2-airflow-1.9.0 ` , ` composer-1.8.2-airflow-1.10.1 ` , ` composer-1.8.2-airflow-1.10.2 ` , and ` composer-1.8.2-airflow-1.10.3 ` . The default is ` composer-1.8.2-airflow-1.9.0 ` . Upgrade your Cloud SDK to use features in this release. 

**FIXED:**

  * Fixed an issue with triggering DAGs from the Web UI while DAG serialization is turned on (for Airflow 1.10.3). 
  * CloudSQL Proxy should now use less CPU power. 

##  November 18, 2019

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.8.1-airflow-1.9.0 ` , ` composer-1.8.1-airflow-1.10.1 ` , ` composer-1.8.1-airflow-1.10.2 ` , and ` composer-1.8.1-airflow-1.10.3 ` . The default is ` composer-1.8.1-airflow-1.9.0 ` . Upgrade your Cloud SDK to use features in this release. 

**FIXED:**

  * Fixed an issue that prevented upgrades from Airflow 1.10.2 to 1.10.3. 
  * Fixed an issue with triggering DAGs from the Web UI while DAG serialization is turned on. 

##  October 31, 2019

**FEATURE:**

Cloud Composer is now available in Frankfurt ( ` europe-west3 ` ).

##  October 30, 2019

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.8.0-airflow-1.9.0 ` , ` composer-1.8.0-airflow-1.10.1 ` , ` composer-1.8.0-airflow-1.10.2 ` , and ` composer-1.8.0-airflow-1.10.3 ` . The default is ` composer-1.8.0-airflow-1.9.0 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * Added support for Apache Airflow 1.10.3. 

**FIXED:**

  * Fixed a DAG serialization issue in Airflow 1.10.2. 
  * Fixed an issue with domain restricted sharing support. 

##  October 18, 2019

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.7.9-airflow-1.9.0 ` , ` composer-1.7.9-airflow-1.10.1 ` , and ` composer-1.7.9-airflow-1.10.2 ` . The default is ` composer-1.7.9-airflow-1.9.0 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * Bucket Policy Only is now supported, and you will no longer need to disable it during Cloud Composer environment creation. 
  * Support for [ Domain restricted sharing ](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) is now in Beta. See [ Creating environments ](https://cloud.google.com/composer/docs/how-to/managing/creating#access-control) to learn how to enable this feature. 

**FIXED:**

  * Improved automatic zone selection during environment creation. 
  * Fixed an issue with Private IP setup during environment creation. 

##  October 08, 2019

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.7.7-airflow-1.9.0 ` , ` composer-1.7.7-airflow-1.10.1 ` , and ` composer-1.7.7-airflow-1.10.2 ` . The default is ` composer-1.7.7-airflow-1.9.0 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * The ODBC Linux driver ( ` unixodbc-dev ` ) is now included by default in the Cloud Composer images. 
  * ` jsonschema ` is now available as a Python dependency for DAG serialization. 
  * Composer now ensures that you can only change the Airflow config ` [core] store_serialized_dags ` one way (from false to true). 
  * Added default Airflow config and environment variables for DAG serialization. 
  * Environment update timeout has been extended to facilitate migrating large databases. 

**FIXED:**

  * New environments will use regional buckets instead of multi-regional. Previously-created environments will continue to use multi-regional buckets. 
  * Fixed an issue that sporadically caused Cloud Storage bucket synchronization to hang. 
  * Fixed an issue where service account permission errors would overwrite other errors. 
  * Fixed an issue that caused extraneous disk usage in the Airflow webserver. 

##  September 20, 2019

**FEATURE:**

Cloud Composer is now available in Zurich ( ` europe-west6 ` ).

##  September 12, 2019

**CHANGED:** **Note:** This release has been rolled back. If you created an
environment with composer-1.7.6-airflow-*, you can retrieve and delete the
environment, but not update. We recommend that you delete the environment and
create a new environment with the latest image version. Refer to the August
28, 2019, release note for default version.

**FEATURE:**

  * The ODBC Linux driver ( ` unixodbc-dev ` ) is now included by default in the Cloud Composer images. 
  * ` jsonschema ` is now available as a Python dependency for DAG serialization. 

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.7.6-airflow-1.9.0 ` , ` composer-1.7.6-airflow-1.10.1 ` , and ` composer-1.7.6-airflow-1.10.2 ` . The default is ` composer-1.7.6-airflow-1.9.0 ` . Upgrade your Cloud SDK to use features in this release. 

**FIXED:**

  * New environments will use regional buckets instead of multi-regional. Previously-created environments will continue to use multi-regional buckets. 
  * Fixed an issue that sporadically caused Cloud Storage bucket synchronization to hang. 
  * Fixed an issue where service account permission errors would overwrite other errors. 
  * Fixed an issue that caused extraneous disk usage in the Airflow webserver. 

##  August 30, 2019

**FEATURE:**

Cloud Composer is now available in Sydney ( ` australia-southeast1 ` ) and
Montreal ( ` northamerica-northeast1 ` ).

##  August 28, 2019

**CHANGED:** **Note:** This Cloud Composer release has begun rolling out to [
supported regions ](https://cloud.google.com/about/locations/) . The rollout
is scheduled to be completed on September 3, 2019, at which time
composer-1.7.5-airflow-1.9.0 becomes the default Cloud Composer release for
newly created environments in all regions.

**CHANGED:** **Note:** The  August 22, 2019  , release has been rolled back,
so this release supersedes the rollout dates and default version previously
stated.

**CHANGED:**

[ New versions
](https://cloud.google.com/composer/docs/concepts/versioning/composer-
versions) of Cloud Composer images: ` composer-1.7.5-airflow-1.9.0 ` , `
composer-1.7.5-airflow-1.10.1 ` , and ` composer-1.7.5-airflow-1.10.2 ` . The
default is ` composer-1.7.5-airflow-1.9.0 ` . Upgrade your Cloud SDK to use
features in this release.

**FEATURE:**

  * Fixed unwanted error output from scheduler pod in Private IP Composer environments. 
  * Improved reliability of Private IP environment creation in crowded IP address spaces. 
  * Fixed an issue with asynchronous DAG loading when handling Unicode strings. 
  * Fixed an issue that caused some environment deletion operations to fail. 
  * Fixed an issue that sometimes prevented the liveness DAG from running when there were failed scheduler pods. 
  * Improved error messages when corrupted Cloud Storage bucket permissions prevent operations from succeeding. 
  * Reduced the latency of failed Python package updates when invalid packages are selected. 
  * Backported [ AIRFLOW-4015 ](https://issues.apache.org/jira/browse/AIRFLOW-4015) to support the ` GET dag_runs ` endpoint in Airflow 1.10.2. 
  * Fixed an issue that caused image version upgrades to fail when the Airflow database was too large. 

##  August 22, 2019

**CHANGED:** **Note:** This release has been rolled back. If you created an
environment with ` composer-1.7.4-airflow-* ` , you can retrieve and delete
the environment, but not update. We recommend that you delete the environment
and create a new environment with the latest image version. Refer to the
August 28, 2019, release note for the rollout dates and default version.

**CHANGED:**

[ New versions
](https://cloud.google.com/composer/docs/concepts/versioning/composer-
versions) of Cloud Composer images: ` composer-1.7.4-airflow-1.9.0 ` , `
composer-1.7.4-airflow-1.10.1 ` , and ` composer-1.7.4-airflow-1.10.2 ` . The
default is ` composer-1.7.4-airflow-1.9.0 ` . Upgrade your Cloud SDK to use
features in this release.

**FEATURE:**

  * Fixed unwanted error output from scheduler pod in Private IP Composer environments. 
  * Improved reliability of Private IP environment creation in crowded IP address spaces. 
  * Fixed an issue with asynchronous DAG loading when handling Unicode strings. 
  * Fixed an issue that caused some environment deletion operations to fail. 
  * Fixed an issue that sometimes prevented the liveness DAG from running when there were failed scheduler pods. 
  * Improved error messages when corrupted Cloud Storage bucket permissions prevent operations from succeeding. 
  * Reduced the latency of failed Python package updates when invalid packages are selected. 
  * Backported [ AIRFLOW-4015 ](https://issues.apache.org/jira/browse/AIRFLOW-4015) to support the ` GET dag_runs ` endpoint in Airflow 1.10.2. 
  * Fixed an issue that caused image version upgrades to fail when the Airflow database was too large. 

##  August 14, 2019

**CHANGED:** **Note:** This Cloud Composer release has begun rolling out to [
supported regions ](https://cloud.google.com/about/locations/) . The rollout
is scheduled to be completed on August 15, 2019, at which time
composer-1.7.3-airflow-1.9.0 becomes the default Cloud Composer release for
newly created environments in all regions.

**CHANGED:**

[ New versions
](https://cloud.google.com/composer/docs/concepts/versioning/composer-
versions) of Cloud Composer images: ` composer-1.7.3-airflow-1.9.0 ` , `
composer-1.7.3-airflow-1.10.1 ` , and ` composer-1.7.3-airflow-1.10.2 ` . The
default is ` composer-1.7.3-airflow-1.9.0 ` . Upgrade your Cloud SDK to use
features in this release.

**FEATURE:**

This release contains only internal reliability improvements.

##  June 21, 2019

**FEATURE:**

Cloud Composer is now available in London ( ` europe-west2 ` ).

##  June 14, 2019

**CHANGED:** **Note:** This Cloud Composer release has begun rolling out to [
supported regions ](https://cloud.google.com/about/locations/) . The rollout
is scheduled to be completed on June 19, 2019, at which time
composer-1.7.2-airflow-1.9.0 becomes the default Cloud Composer release for
newly created environments in all regions.

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.7.2-airflow-1.9.0 ` , ` composer-1.7.2-airflow-1.10.1 ` , and ` composer-1.7.2-airflow-1.10.2 ` . The default is ` composer-1.7.2-airflow-1.9.0 ` . Upgrade your Cloud SDK to use features in this release. 
  * The [ Airflow configuration ](https://cloud.google.com/composer/docs/concepts/airflow-configurations) ` webserver-workers ` is now updatable. Available only in Airflow 1.10.2 and later. 

**FEATURE:**

  * Fixed an asynchronous DAG loading issue that prevented the Airflow web server from loading some DAGs. Available only in ` composer-1.7.2-airflow-1.10.2 ` versions and later. 
  * Fixed an issue that caused image version upgrades to fail when migrating particularly large Airflow databases. 
  * Fixed an issue that sometimes prevented data plane monitoring metrics from being reported in Stackdriver. 
  * Fixed an issue that caused PyPI package installation to sometimes time out and fail. 

##  May 28, 2019

**FEATURE:**

To display DAGs faster and reduce potential downtime due to heavy DAG
processing, Cloud Composer now supports [ asynchronous DAG loading
](https://cloud.google.com/composer/docs/how-to/accessing/airflow-web-
interface) in the Airflow web server. To enable, set the following [ Airflow
configurations ](https://cloud.google.com/composer/docs/concepts/airflow-
configurations) : ` [webserver]async_dagbag_loader=True ` and `
[webserver]worker_refresh_interval=3600 ` . Available only in `
composer-1.7.1-Airflow-1.10.2 ` versions and later.

**CHANGED:**

[ New versions
](https://cloud.google.com/composer/docs/concepts/versioning/composer-
versions) of Cloud Composer images: ` composer-1.7.1-airflow-1.9.0 ` , `
composer-1.7.1-airflow-1.10.1 ` , and ` composer-1.7.1-airflow-1.10.2 ` . The
default is ` composer-1.7.1-airflow-1.9.0 ` . Upgrade your Cloud SDK to use
features in this release.

**FEATURE:**

  * Backported [ AIRFLOW-3143 ](https://issues.apache.org/jira/browse/AIRFLOW-3143) to support auto-zone in DataprocClusterCreateOperator. Available only in ` composer-1.7.1-airflow-1.10.2 ` versions and later. 
  * Added back the list of [ blocked Airflow configurations ](https://cloud.google.com/composer/docs/concepts/airflow-configurations) for Airflow 1.10.2. 

##  May 16, 2019

**FEATURE:**

  * Cloud Composer now supports [ Private Python package repositories ](https://cloud.google.com/composer/docs/how-to/using/installing-python-dependencies#install-private) . Available only in ` composer-1.7.0-* ` and later versions. 
  * Added support for Apache Airflow 1.10.2. 
  * Added new health metrics in [ Stackdriver ](https://cloud.google.com/composer/docs/how-to/managing/monitoring-environments) to monitor your environment: ` composer.googleapis.com/environment/healthy ` and ` composer.googleapis.com/environment/database_health `
  * [ VPC Native support ](https://cloud.google.com/composer/docs/how-to/managing/configuring-private-ip#secondary-range) is now in beta. 
  * Backported [ AIRFLOW-2747 ](https://issues.apache.org/jira/browse/AIRFLOW-2747) to support explicit rescheduling of Airflow sensors. Available only in Airflow 1.10.2 versions and later. 

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.7.0-airflow-1.9.0 ` , ` composer-1.7.0-airflow-1.10.1 ` , and ` composer-1.7.0-airflow-1.10.2 ` . The default is ` composer-1.7.0-airflow-1.9.0 ` . Upgrade your Cloud SDK to use features in this release. 
  * To prevent co-locating workers on the same node, improved Airflow worker pods scheduling. 
  * When creating a Private IP Cloud Composer environment, the GKE master IP CIDR block no longer needs to be specified. 
  * Starting from ` composer-1.7.0-* ` , Apache Airflow version 1.10.0 is no longer available for environment creation or in-place upgrade. 

To protect your environment from security vulnerabilities, we recommend that
you upgrade to the latest Cloud Composer version:
composer-1.7.0-airflow.-1.x.y. Because Airflow 1.10.0 is no longer supported,
also consider upgrading to Airflow 1.10.1.

**FEATURE:**

  * Added back the ` ping ` command-line utility to the default Cloud Composer managed Docker images. 
  * Backported AIRFLOW-2715 [ AIRFLOW-2715 ](https://issues.apache.org/jira/browse/AIRFLOW-2715) to fix the ` DataflowTemplateOperator ` region support issue. Available only in Airflow 1.10.2 versions and later. 
  * Fixed an issue that prevented in-place upgrades when the environment service account had only the ` roles/composer.worker ` role. 
  * Backported fixes for [ CVE-2019-0216 ](https://nvd.nist.gov/vuln/detail/CVE-2019-0216) and [ CVE-2019-0229 ](https://nvd.nist.gov/vuln/detail/CVE-2019-0229) . 
  * Fixed an issue that caused some environment deletion operations to fail. 
  * Fixed an issue that could cause Cloud Composer workloads to leak into the node pools added for ` KubernetesPodOperator ` workloads. 
  * Fixed an issue in which the ` airflow_db ` connection did not work correctly for some environments. 
  * Fixed an issue that prevented upgrading a Private IP Cloud Composer environment. 

##  April 04, 2019

**FEATURE:**

[ Stackdriver metrics for Cloud Composer
](https://cloud.google.com/composer/docs/how-to/managing/monitoring-
environments) is in beta. You can now use Stackdriver Monitoring to understand
the performance and health of your Cloud Composer environments and examine
Airflow metrics. Stackdriver is available for ` composer-1.6.0-airflow-1.9.0 `
and later versions.

**CHANGED:**

[ New versions
](https://cloud.google.com/composer/docs/concepts/versioning/composer-
versions) of Cloud Composer images: ` composer-1.6.1-airflow-1.9.0 ` , `
composer-1.6.1-airflow-1.10.0 ` , and ` composer-1.6.1-airflow-1.10.1 ` . The
default is ` composer-1.6.1-airflow-1.9.0 ` . Upgrade your Cloud SDK to use
features in this release.

**ISSUE:**

Stackdriver Monitoring: In rare cases, a ` TRANSIENT_FAILURE ` connection
error occurs when Cloud Composer writes metrics to Stackdriver Monitoring.
Typically, the automatic retry is successful, but occasionally, the failure
state persists for an extended period of time.

##  April 03, 2019

**FEATURE:**

  * [ Private IP Cloud Composer environment ](https://cloud.google.com/composer/docs/concepts/private-ip) is in beta. To isolate your workflows from the public internet, you can now assign only private IP ( [ RFC 1918 ](https://tools.ietf.org/html/rfc1918) ) addresses to the managed Google Kubernetes Engine and Cloud SQL VMs in your Cloud Composer environment. 
  * [ Image version upgrade ](https://cloud.google.com/composer/docs/how-to/managing/upgrading) is in beta. You can now perform an in-place upgrade on the Airflow version or Cloud Composer version that your environment runs. 

**CHANGED:**

[ New versions
](https://cloud.google.com/composer/docs/concepts/versioning/composer-
versions) of Cloud Composer images: ` composer-1.6.0-airflow-1.9.0 ` , `
composer-1.6.0-airflow-1.10.0 ` , and ` composer-1.6.0-airflow-1.10.1 ` . The
default is ` composer-1.6.0-airflow-1.9.0 ` . Upgrade your Cloud SDK to use
features in this release.

**FEATURE:**

Increased the operation timeout from 20 to 30 minutes to fix the sporadic,
premature PyPI dependency update timeout issue.

**ISSUE:**

  * Currently, you cannot perform an image version upgrade. 
  * Currently, you cannot simultaneously create or delete two Cloud Composer environments on the same subnetwork if one of the two environments is a Private IP Cloud Composer environment. 
    * You must wait until the first Cloud Composer environment is created before creating the second environment to avoid environment creation failures. 
    * You must wait until the first Cloud Composer environment is deleted before deleting the second environment to avoid a GKE cluster resource leak. If the leak occurs, manually delete the GKE cluster for the Cloud Composer environment. 

` airflow_db ` connection: The ` airflow_db ` connection works only for the
Airflow webserver. Workarounds are as follows:

  * Update the ` airflow_db ` connection's Host component to ` airflow-sqlproxy-service.default ` . This update breaks the ability to use the connection in the Airflow webserver's Ad Hoc Query page but is preferred for DAGs that rely on the ` airflow_db ` connection. 
  * Create a new connection that mirrors the ` airflow_db ` connection but uses ` airflow-sqlproxy-service.default ` for the Host. 

**CHANGED:**

[ New versions
](https://cloud.google.com/composer/docs/concepts/versioning/composer-
versions) of Cloud Composer images: ` composer-1.4.2-airflow-1.9.0 ` and `
composer-1.4.2-airflow-1.10.0 ` .

**FEATURE:**

  * Fixed the issue where ` max_active_runs ` and ` concurrency ` are not updated in the Airflow web UI **DAG Details** page when configurations are updated. 
  * Fixed the failed ` KubernetesPodOperator ` and ` GkePodOperator ` when a task a runs longer than 1 hour due to authentication issues in the Kuberentes client. 

##  March 20, 2019

**CHANGED:**

You can now [ configure Shared VPC
](https://cloud.google.com/composer/docs/how-to/managing/creating) in the GCP
Console.

##  March 11, 2019

**CHANGED:** **Note:** The March 7, 2019, release has been rolled back, so
this release supersedes the rollout dates and default version previously
stated.

**FEATURE:**

You can now [ access the Airflow web interface logs
](https://cloud.google.com/composer/docs/concepts/logs) in Stackdriver Logging
for Cloud Composer under ` airflow-webserver ` .

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.5.2-airflow-1.9.0 ` , ` composer-1.5.2-airflow-1.10.0 ` , and ` composer-1.5.2-airflow-1.10.1 ` . The default is ` composer-1.5.2-airflow-1.9.0 ` . 
  * For the Cloud SQL instance for Cloud Composer, the [ ` wait_timeout ` ](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_wait_timeout) and [ ` interactive_timeout ` ](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_interactive_timeout) are reduced to 1800 seconds to enable a faster deadlock recovery if an idle SQL connection holds a database lock. 
  * Added back the openssh-client package to the default Cloud Composer managed docker images. 

**FEATURE:**

  * Backported the Apache Airflow [ fix for the SubDag failed by scheduler deadlock issue ](https://github.com/apache/airflow/pull/4769) . 
  * Fixed an issue where a DAG backfill could not be disabled on a per-DAG basis. 

##  March 07, 2019

**CHANGED:** **Note:** This release has been rolled back. If you created an
environment with ` composer-1.5.1-airflow-* ` , you can retrieve and delete
the environment, but not update. We recommend that you delete the environment
and create a new environment with the latest image version. Refer to the March
11, 2019, release note for the rollout dates and default version.

**FEATURE:**

You can now [ access the Airflow web interface logs
](https://cloud.google.com/composer/docs/concepts/logs) in Stackdriver Logging
for Cloud Composer under ` airflow-webserver ` .

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.5.1-airflow-1.9.0 ` , ` composer-1.5.1-airflow-1.10.0 ` , and ` composer-1.5.1-airflow-1.10.1 ` . The default is ` composer-1.5.1-airflow-1.9.0 ` . 
  * For the Cloud SQL instance for Cloud Composer, the [ ` wait_timeout ` ](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_wait_timeout) and [ ` interactive_timeout ` ](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_interactive_timeout) are reduced to 1800 seconds to enable a faster deadlock recovery if an idle SQL connection holds a database lock. 
  * Added back the openssh-client package to the default Cloud Composer managed docker images. 

**FEATURE:**

  * Backported the Apache Airflow [ fix for the SubDag failed by scheduler deadlock issue ](https://github.com/apache/airflow/pull/4769) . 
  * Fixed an issue where a DAG backfill could not be disabled on a per-DAG basis. 

##  February 06, 2019

**FEATURE:**

  * Multi-version Apache Airflow support [ is now ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versioning-overview) [ General Availability ](https://cloud.google.com/terms/launch-stages#launch-stages) . You can select the [ Cloud Composer image version ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versioning-overview) when you [ create a new environment ](https://cloud.google.com/composer/docs/how-to/managing/creating) without enabling Beta feature support. 
  * You can now [ view available Cloud Composer image versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versioning-overview#version_selection) in all Cloud Composer interfaces. 
  * Added support for Apache Airflow 1.10.1. 

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.5.0-airflow-1.9.0 ` , ` composer-1.5.0-airflow-1.10.0 ` , and ` composer-1.5.0-airflow-1.10.1 `
  * [ Increased the disk size ](https://cloud.google.com/composer/pricing) for the Apache Airflow webserver from 10 to 20 GB. 
  * We now install Airflow dependencies of "mysql" instead of "devel". 

If your DAG uses dependencies that are available only in "devel", add the
dependencies to your DAG as PyPI dependencies.

**FEATURE:**

  * Backported Airflow upstream fix for the broken GCP connection in the ` DataflowJavaOperator ` and ` DataflowPythonOperator ` [ AIRFLOW-2009 ](https://issues.apache.org/jira/browse/AIRFLOW-2009) in all Cloud Composer managed Airflow versions. 
  * Backported Airflow upstream fixes for [ CVE-2018-20244: Stored XSS in Apache Airflow ](https://lists.apache.org/thread.html/f656fddf9c49293b3ec450437c46709eb01a12d1645136b2f1b8573b@%3Cdev.airflow.apache.org%3E) in all Cloud Composer managed Airflow versions (1.9.0, 1.10.0, 1.10.1). 

Due to this vulnerability, we recommend that you upgrade to the latest Cloud
Composer version.

##  January 10, 2019

**FEATURE:**

Added a Kubernetes pod liveness checker for the ` airflow-sqlproxy ` service
to recover from the ` cloudsqlproxy ` process error.

##  December 19, 2018

**FEATURE:**

Cloud Composer is now available in the Northern Virginia ( ` us-east4 ` )
region.

##  December 17, 2018

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.4.1-airflow-1.9.0 ` and ` composer-1.4.1-airflow-1.10.0 ` . 
  * The Airflow workers restart when a Celery concurrency configuration change is requested so that the change takes effect automatically. 
  * The ` logs/ ` and ` data/ ` directories in Cloud Storage are mounted with file mode 755, enabling binaries to be placed in these directories and executed from Airflow. 
  * The GCP_PROJECT environment variable is set to the Google Cloud Platform project ID in the Airflow webserver. 

**FEATURE:**

  * Fixed the broken Airflow webserver when DAG parsing times out on the webserver side. 
  * Pinned the Airflow base Docker image tag for initial environment creation and future PyPI dependency installations. 

##  November 26, 2018

**FEATURE:**

GA launch of [ Python 3 support
](https://cloud.google.com/composer/docs/concepts/python-version) . Currently,
the ` v1 ` [ API ](https://cloud.google.com/composer/docs/apis) and the GCP
Console support GA [ Python 3 environment creation
](https://cloud.google.com/composer/docs/how-to/managing/creating) .

**CHANGED:**

[ New versions
](https://cloud.google.com/composer/docs/concepts/versioning/composer-
versions) of Cloud Composer images: ` composer-1.4.0-airflow-1.9.0 ` and `
composer-1.4.0-airflow-1.10.0 ` .

**FEATURE:**

  * Fixed the Stackdriver logging severity level for ` airflow-sqlproxy ` and improved the labeling of logs. 
  * Fixed boundless HTTP header growth in the ` set_user_agent googleapiclient ` methods in 1.10.0 images. 

##  October 24, 2018

**FEATURE:**

  * Multi-version Apache Airflow support [ is now in Beta ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versioning-overview) . You can choose from multiple versions of Airflow when creating a new Cloud Composer environment. Multiple versions of Airflow can run in the same GCP project simultaneously. 
  * Cloud Composer is now available in the Mumbai ( ` asia-south1 ` ) region. 
  * The Cloud Composer now displays in the top-right banner of the Airflow webserver UI. 

**CHANGED:**

[ New versions
](https://cloud.google.com/composer/docs/concepts/versioning/composer-
versions) of Cloud Composer images: ` composer-1.3.0-airflow-1.9.0 ` and `
composer-1.3.0-airflow-1.10.0 ` .

##  October 02, 2018

**FEATURE:**

Support for [ Python 3 is now in Beta
](https://cloud.google.com/composer/docs/concepts/python-version) You can
create Python 3 Cloud Composer environments and run Python 2 and Python 3
environments in the same GCP project simultaneously. Currently, the v1beta1 [
API ](https://cloud.google.com/composer/docs/apis) and GCP Console support
Python 3 environment creation.

For composer-1.2.0 environments, some commands in Python 2 Composer
environments might run under the Python 3 runtime. Operators should explicitly
specify ` python2 ` to ensure that commands run under Python 2. For more info,
see [ PEP 394. ](https://www.python.org/dev/peps/pep-0394/)

**CHANGED:**

  * [ New version ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of the Cloud Composer image: ` composer-1.2.0-airflow-1.9.0 ` . 
  * To reduce potential scheduling delays due to DAG processing, the scheduler restart behavior is now time based (every 600 seconds), not run based. 

##  September 17, 2018

**CHANGED:**

  * [ New version ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of the Cloud Composer image: ` composer-1.1.1-airflow-1.9.0 ` . 
  * The following [ Airflow configurations ](https://cloud.google.com/composer/docs/concepts/airflow-configurations) are now updatable: core-dag_concurrency, core-parallelism, core-max_active_runs_per_dag, and scheduler-max_threads. 

##  August 17, 2018

**FEATURE:**

  * Support for [ GKE Shared VPC ](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc) is now in Beta. For information about Cloud Composer configuration, see [ Creating Environments ](https://cloud.google.com/composer/docs/how-to/managing/creating) . 
  * Added the following Airflow updates: 
    * Backported network, subnetwork, and tags support in ` DataprocClusterCreateOperator ` to create Cloud Dataproc clusters in user-specified subnetworks. 
    * Backported ` GKEPodOperator ` to enable launching Kubernetes pods in GKE clusters that are accessible from GCP connections. 

**CHANGED:**

  * [ New version ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of the Cloud Composer image: ` composer-1.1.0-airflow-1.9.0 ` . 
  * Cloud Composer environments running composer-1.0.0 or later now have GKE cluster [ auto-upgrade ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) enabled by default. 
  * Introduced additional liveness monitoring for the Cloud Composer Stackdriver fluentd agent. 

**FEATURE:**

Fixed the following Airflow issues:

  * Fixed the issue where the ` DataFlowJavaOperator ` and the ` DataFlowPythonOperator ` might run continually due to a job name mismatch. 
  * Fixed a rare scheduler bug where the Airflow scheduler freezes by restarting the scheduler if its Stackdriver logs are old. 

##  July 19, 2018

**FEATURE:**

  * **GA launch** of Cloud Composer. 
  * Cloud Composer is now available in the following regions: 
    * ` asia-northeast1 `
    * ` us-east1 `
  * Revamped Stackdriver Logging as follows: 
    * Stackdriver Logging now based on fluentd and now includes ` composer-agent ` , ` airflow-redis ` , and ` airflow-sqlproxy ` logs. 
    * Exposed the Airflow worker and scheduler container logs in Stackdriver Logging, including exceptions and stderr. 
    * Disabled Logging for Google Kubernetes Engine to avoid duplicate logging in Stackdriver Logging. 
    * The log format for some raw Airflow logs stored in Cloud Storage now include the delimiter string, dag-id, task-id, and execution date. 
  * Added new [ Cloud Identity and Access Management roles ](https://cloud.google.com/composer/docs/how-to/access-control#roles) . 
    * The ` composer.environmentAndStorageObjectAdmin ` and ` composer.environmentAndStorageObjectViewer ` roles provide users the permissions necessary to access environments and objects in Cloud Storage buckets. 
    * The ` composer.worker ` role provides service accounts the permissions necessary to run a Cloud Composer VM. 
  * Added the following Airflow updates: 
    * Backported the ` KubernetesPodOperator ` to enable launching Docker containers in Cloud Composer. 
    * Added ` PARQUET ` source format support in ` bigquery_hook ` . 
    * Backported the JDBC/DBAPI autocommit issue fix. 
    * Fixed the Airflow documentation link in the Airflow web interface. 

**CHANGED:**

  * [ New version ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of the Cloud Composer image: ` composer-1.0.0-airflow-1.9.0 ` . 
  * Cloud Composer environments running composer-1.0.0 or later can now launch Cloud Dataflow jobs in [ supported Cloud Dataflow regions ](https://cloud.google.com/about/locations/) . 
  * Added the option to modify some [ celery configurations ](https://cloud.google.com/composer/docs/concepts/airflow-configurations) . 

**FEATURE:**

Fixed the following Airflow issues:

  * Fixed the issue where Airflow tasks were stuck in queued or running states for extended periods of time before failing. 
  * Fixed the Airflow web interface crashlooping issue that resulted from statsd exceptions. 
  * Revised the Airflow web interface message when the TaskInstance RUN button is clicked. Note that the task instance restarts automatically if the DAG is running and its dependencies are met. 

##  June 27, 2018

**CHANGED:**

  * [ New version ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of the Cloud Composer image: ` composer-0.5.3-airflow-1.9.0 ` . 
  * Added requirement to include ` https://www.googleapis.com/auth/cloud-platform ` when specifying OAuth scopes during [ environment creation ](https://cloud.google.com/composer/docs/how-to/managing/creating) . 
  * Improved health checking on Airflow to restart scheduler and worker pods if scheduled tasks are not queued or executed. 
  * Improved messaging for create and update environment failures. 

##  June 15, 2018

**FEATURE:**

[ Audit logging ](https://cloud.google.com/composer/docs/how-to/audit-logging)
is now available in Beta.

**CHANGED:**

  * [ New version ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of the Cloud Composer image: ` composer-0.5.2-airflow-1.9.0 ` . 
  * [ Added OAuth scope configuration ](https://cloud.google.com/composer/docs/how-to/managing/creating) on the Google Cloud Platform Console **Environment creation** page 
  * Increased the minimum disk size from 10 GB to 20 GB. 
  * Improved error reporting. 
  * Improved stability of the CeleryExecutor Redis message backend. 

**FEATURE:**

Fixed the ` BAD REQUEST ` error message for environment creation or deletion
failures to provide information about the failures.

##  May 17, 2018

**CHANGED:**

[ New version
](https://cloud.google.com/composer/docs/concepts/versioning/composer-
versions) of the Cloud Composer image: ` composer-0.5.1-airflow-1.9.0 ` .

**FEATURE:**

  * Fixed permanent environment ` DELETE ` error that occurred when the Google Kubernetes Engine cluster is deleted or that occurred when in an error state prior to environment deletion. 
  * Removed inapplicable "Failed to update environment from json" error message from worker/scheduler logs. 

##  May 01, 2018

**FEATURE:**

**Beta launch** of Cloud Composer ( ` composer-0.5.0-airflow-1.9.0 ` ). This
release includes [ Apache Airflow ](https://airflow.apache.org) 1.9.0.

