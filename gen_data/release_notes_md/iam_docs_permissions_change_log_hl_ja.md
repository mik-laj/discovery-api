#  IAM 権限変更ログ

このページでは、Google Cloud の一般提供およびベータ版のすべてのサービスにおいて、公開 Cloud IAM
権限に関して行われた変更について説明します。こうした変更ログは、 [ カスタム役割
](https://cloud.google.com/iam/docs/understanding-custom-roles?hl=ja)
の保守とトラブルシューティングに役立ちます。

廃止された権限、カスタム役割でサポートされなくなった権限は、Cloud IAM
がカスタム役割から自動的に削除します。これとは対照的に、権限が追加された場合、Cloud IAM が自動的にカスタム役割に権限を追加することはありません
__ 。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/cloud-iam-permissions-change-
log.xml ` を直接追加します。

IAM 権限変更ログ

##  2020-03-02 の週の Cloud IAM の変更予定

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.networkAdmin ` （Compute ネットワーク 管理者）に追加されました。

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.networkViewer ` （Compute ネットワーク 閲覧者）に追加されました。

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/editor ` （編集者）に追加されました。

` bigquery.bireservations.update `  
` bigquery.reservationAssignments.create `  
` bigquery.reservationAssignments.delete `  
` bigquery.reservations.create `  
` bigquery.reservations.delete `  
` bigquery.reservations.update `  
` identityplatform.workloadPoolProviders.create `  
` identityplatform.workloadPoolProviders.delete `  
` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPoolProviders.undelete `  
` identityplatform.workloadPoolProviders.update `  
` identityplatform.workloadPools.create `  
` identityplatform.workloadPools.delete `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
` identityplatform.workloadPools.undelete `  
` identityplatform.workloadPools.update `  
` servicedirectory.locations.get `  
` servicedirectory.locations.list `  
  
Cloud Identity and Access Management  |  役割の更新  |

以下の権限が役割 ` roles/iam.securityAdmin ` （セキュリティ管理者）に追加されました。

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
Cloud Identity and Access Management  |  役割の更新  |

次の権限が役割 ` roles/iam.securityReviewer ` （セキュリティ審査担当者）に追加されました。

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
ID プラットフォーム  |  役割の追加  |

次の権限を持つ役割 ` roles/identityplatform.admin ` （Identity Platform 管理者）が追加されました。

` identityplatform.workloadPoolProviders.create `  
` identityplatform.workloadPoolProviders.delete `  
` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPoolProviders.undelete `  
` identityplatform.workloadPoolProviders.update `  
` identityplatform.workloadPools.create `  
` identityplatform.workloadPools.delete `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
` identityplatform.workloadPools.undelete `  
` identityplatform.workloadPools.update `  
  
ID プラットフォーム  |  役割の追加  |

次の権限を持つ役割 ` roles/identityplatform.viewer ` （Identity Platform 閲覧者）が追加されました。

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
  
ネットワーク管理 API  |  一般提供開始  |

役割 ` roles/networkmanagement.admin ` （Network Management 管理者）の一般提供を開始しました。  
  
ネットワーク管理 API  |  一般提供開始  |

役割 ` roles/networkmanagement.viewer ` （Network Management 閲覧者）の一般提供を開始しました。  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/owner ` （オーナー）に追加されました。

` identityplatform.workloadPoolProviders.create `  
` identityplatform.workloadPoolProviders.delete `  
` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPoolProviders.undelete `  
` identityplatform.workloadPoolProviders.update `  
` identityplatform.workloadPools.create `  
` identityplatform.workloadPools.delete `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
` identityplatform.workloadPools.undelete `  
` identityplatform.workloadPools.update `  
` servicedirectory.locations.get `  
` servicedirectory.locations.list `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/viewer ` （閲覧者）に追加されました。

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.get `  
` servicedirectory.locations.list `  
  
BigQuery  |  追加  |  ` bigquery.bireservations.get `  
` bigquery.bireservations.update `  
` bigquery.capacityCommitments.create `  
` bigquery.capacityCommitments.delete `  
` bigquery.capacityCommitments.get `  
` bigquery.capacityCommitments.list `  
` bigquery.reservationAssignments.create `  
` bigquery.reservationAssignments.delete `  
` bigquery.reservationAssignments.list `  
` bigquery.reservationAssignments.search `  
` bigquery.reservations.create `  
` bigquery.reservations.delete `  
` bigquery.reservations.get `  
` bigquery.reservations.list `  
` bigquery.reservations.update `  
  
BigQuery  |  カスタムの役割でサポート  |  ` bigquery.bireservations.get `  
` bigquery.bireservations.update `  
` bigquery.capacityCommitments.create `  
` bigquery.capacityCommitments.delete `  
` bigquery.capacityCommitments.get `  
` bigquery.capacityCommitments.list `  
` bigquery.reservationAssignments.create `  
` bigquery.reservationAssignments.delete `  
` bigquery.reservationAssignments.list `  
` bigquery.reservationAssignments.search `  
` bigquery.reservations.create `  
` bigquery.reservations.delete `  
` bigquery.reservations.get `  
` bigquery.reservations.list `  
` bigquery.reservations.update `  
  
ID プラットフォーム  |  追加  |  ` identityplatform.workloadPoolProviders.create `  
` identityplatform.workloadPoolProviders.delete `  
` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPoolProviders.undelete `  
` identityplatform.workloadPoolProviders.update `  
` identityplatform.workloadPools.create `  
` identityplatform.workloadPools.delete `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
` identityplatform.workloadPools.undelete `  
` identityplatform.workloadPools.update `  
  
ネットワーク管理 API  |  一般提供開始  |  ` networkmanagement.connectivitytests.create `  
` networkmanagement.connectivitytests.delete `  
` networkmanagement.connectivitytests.get `  
` networkmanagement.connectivitytests.getIamPolicy `  
` networkmanagement.connectivitytests.list `  
` networkmanagement.connectivitytests.rerun `  
` networkmanagement.connectivitytests.setIamPolicy `  
` networkmanagement.connectivitytests.update `  
` networkmanagement.locations.get `  
` networkmanagement.locations.list `  
` networkmanagement.operations.get `  
` networkmanagement.operations.list `  
  
Memorystore for Redis  |  追加  |  ` redis.instances.failover `  
` redis.instances.upgrade `  
  
Memorystore for Redis  |  カスタムの役割でサポート  |  ` redis.instances.failover `  
` redis.instances.upgrade `  
  
Service Directory  |  追加  |  ` servicedirectory.endpoints.create `  
` servicedirectory.endpoints.delete `  
` servicedirectory.endpoints.get `  
` servicedirectory.endpoints.getIamPolicy `  
` servicedirectory.endpoints.list `  
` servicedirectory.endpoints.setIamPolicy `  
` servicedirectory.endpoints.update `  
` servicedirectory.locations.get `  
` servicedirectory.locations.list `  
` servicedirectory.namespaces.associatePrivateZone `  
` servicedirectory.namespaces.create `  
` servicedirectory.namespaces.delete `  
` servicedirectory.namespaces.get `  
` servicedirectory.namespaces.getIamPolicy `  
` servicedirectory.namespaces.list `  
` servicedirectory.namespaces.setIamPolicy `  
` servicedirectory.namespaces.update `  
` servicedirectory.services.create `  
` servicedirectory.services.delete `  
` servicedirectory.services.get `  
` servicedirectory.services.getIamPolicy `  
` servicedirectory.services.list `  
` servicedirectory.services.resolve `  
` servicedirectory.services.setIamPolicy `  
` servicedirectory.services.update `  
  
Service Directory  |  カスタムの役割でサポート  |  ` servicedirectory.endpoints.create `  
` servicedirectory.endpoints.delete `  
` servicedirectory.endpoints.get `  
` servicedirectory.endpoints.getIamPolicy `  
` servicedirectory.endpoints.list `  
` servicedirectory.endpoints.setIamPolicy `  
` servicedirectory.endpoints.update `  
` servicedirectory.namespaces.associatePrivateZone `  
` servicedirectory.namespaces.create `  
` servicedirectory.namespaces.delete `  
` servicedirectory.namespaces.get `  
` servicedirectory.namespaces.getIamPolicy `  
` servicedirectory.namespaces.list `  
` servicedirectory.namespaces.setIamPolicy `  
` servicedirectory.namespaces.update `  
` servicedirectory.services.create `  
` servicedirectory.services.delete `  
` servicedirectory.services.get `  
` servicedirectory.services.getIamPolicy `  
` servicedirectory.services.list `  
` servicedirectory.services.resolve `  
` servicedirectory.services.setIamPolicy `  
` servicedirectory.services.update `  
  
  
##  2020-02-27 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
BigQuery  |  一般提供開始  |

役割 ` roles/bigquery.readSessionUser ` （BigQuery 読み取りセッション ユーザー）の一般提供を開始しました。  
  
データカタログ  |  役割の更新  |

次の権限が役割 ` roles/datacatalog.entryGroupCreator ` （DataCatalog EntryGroup
作成者）に追加されました。

` datacatalog.entryGroups.list `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/editor ` （編集者）に追加されました。

` dlp.jobs.create `  
` dlp.jobs.get `  
` dlp.jobs.list `  
  
シークレット マネージャー  |  役割の更新  |

次の権限が役割 ` roles/secretmanager.secretAccessor ` （Secret Manager のシークレット
アクセサー）に追加されました。

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
セキュリティ コマンド センター  |  役割の更新  |

次の権限が役割 ` roles/securitycenter.adminEditor ` （セキュリティ センター管理編集者）に追加されました。

` securitycenter.organizationsettings.get `  
  
セキュリティ コマンド センター  |  役割の更新  |

次の権限が役割 ` roles/securitycenter.adminViewer ` （セキュリティ センター管理閲覧者）に追加されました。

` securitycenter.organizationsettings.get `  
  
Cloud Spanner  |  一般提供開始  |

役割 ` roles/spanner.backupAdmin ` （Cloud Spanner バックアップ管理者）の一般提供を開始しました。  
  
Cloud Spanner  |  一般提供開始  |

役割 ` roles/spanner.backupWriter ` （Cloud Spanner バックアップ書き込み）の一般提供を開始しました。  
  
Cloud Spanner  |  一般提供開始  |

役割 ` roles/spanner.restoreAdmin ` （Cloud Spanner 復元の管理者）の一般提供を開始しました。  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/viewer ` （閲覧者）に追加されました。

` dlp.jobs.get `  
` dlp.jobs.list `  
  
BigQuery  |  追加  |  ` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  カスタムの役割でサポート  |  ` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  一般提供開始  |  ` bigquery.readsessions.create `  
` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
データカタログ  |  追加  |  ` datacatalog.entryGroups.list `  
  
データカタログ  |  カスタムの役割でサポート  |  ` datacatalog.entryGroups.list `  
  
Cloud Healthcare API  |  カスタムの役割でサポート  |  `
healthcare.fhirStores.executeBundle `  
  
Cloud Identity and Access Management  |  カスタムの役割でサポート  |  `
iam.serviceAccounts.getOpenIdToken `  
  
Cloud Spanner  |  追加  |  ` spanner.backupOperations.cancel `  
` spanner.backupOperations.get `  
` spanner.backupOperations.list `  
` spanner.backups.create `  
` spanner.backups.delete `  
` spanner.backups.get `  
` spanner.backups.getIamPolicy `  
` spanner.backups.list `  
` spanner.backups.restoreDatabase `  
` spanner.backups.setIamPolicy `  
` spanner.backups.update `  
` spanner.databases.createBackup `  
  
Cloud Spanner  |  カスタムの役割でサポート  |  ` spanner.backupOperations.cancel `  
` spanner.backupOperations.get `  
` spanner.backupOperations.list `  
` spanner.backups.create `  
` spanner.backups.delete `  
` spanner.backups.get `  
` spanner.backups.getIamPolicy `  
` spanner.backups.list `  
` spanner.backups.restoreDatabase `  
` spanner.backups.setIamPolicy `  
` spanner.backups.update `  
` spanner.databases.createBackup `  
  
Cloud Spanner  |  一般提供開始  |  ` spanner.backupOperations.cancel `  
` spanner.backupOperations.get `  
` spanner.backupOperations.list `  
` spanner.backups.create `  
` spanner.backups.delete `  
` spanner.backups.get `  
` spanner.backups.getIamPolicy `  
` spanner.backups.list `  
` spanner.backups.restoreDatabase `  
` spanner.backups.setIamPolicy `  
` spanner.backups.update `  
` spanner.databases.createBackup `  
  
  
##  2020-02-21 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Access Context Manager  |  追加  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Access Context Manager  |  一般提供開始  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Compute Engine  |  追加  |  ` compute.regionHealthCheckServices.create `  
` compute.regionHealthCheckServices.delete `  
` compute.regionHealthCheckServices.get `  
` compute.regionHealthCheckServices.list `  
` compute.regionHealthCheckServices.update `  
` compute.regionHealthCheckServices.use `  
` compute.regionNotificationEndpoints.create `  
` compute.regionNotificationEndpoints.delete `  
` compute.regionNotificationEndpoints.get `  
` compute.regionNotificationEndpoints.list `  
` compute.regionNotificationEndpoints.update `  
` compute.regionNotificationEndpoints.use `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.regionHealthCheckServices.create
`  
` compute.regionHealthCheckServices.delete `  
` compute.regionHealthCheckServices.get `  
` compute.regionHealthCheckServices.list `  
` compute.regionHealthCheckServices.update `  
` compute.regionHealthCheckServices.use `  
` compute.regionNotificationEndpoints.create `  
` compute.regionNotificationEndpoints.delete `  
` compute.regionNotificationEndpoints.get `  
` compute.regionNotificationEndpoints.list `  
` compute.regionNotificationEndpoints.update `  
` compute.regionNotificationEndpoints.use `  
  
  
##  2020-02-14 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Google Cloud サポート  |  一般提供開始  |

役割 ` roles/cloudsupport.techSupportEditor ` （テクニカル サポート編集者）の一般提供を開始しました。  
  
Google Cloud サポート  |  一般提供開始  |

役割 ` roles/cloudsupport.techSupportViewer ` （テクニカル サポート閲覧者）の一般提供を開始しました。  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/editor ` （編集者）に追加されました。

` healthcare.fhirStores.executeBundle `  
  
Cloud Healthcare API  |  役割の更新  |

次の権限が役割 ` roles/healthcare.fhirResourceEditor ` （Healthcare FHIR
リソース編集者）に追加されました。

` healthcare.fhirStores.executeBundle `  
  
Cloud Healthcare API  |  役割の更新  |

次の権限が役割 ` roles/healthcare.fhirResourceReader ` （Healthcare FHIR
リソース読み取り）に追加されました。

` healthcare.fhirStores.executeBundle `  
  
Cloud Logging  |  役割の更新  |

次の権限が役割 ` roles/logging.privateLogViewer ` （プライベート ログ閲覧者）に追加されました。

` logging.buckets.get `  
` logging.buckets.list `  
  
Cloud Logging  |  役割の更新  |

次の権限が役割 ` roles/logging.viewer ` （ログ閲覧者）に追加されました。

` logging.buckets.get `  
` logging.buckets.list `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/owner ` （オーナー）に追加されました。

` healthcare.fhirStores.executeBundle `  
  
セキュリティ コマンド センター  |  役割の更新  |

次の権限が役割 ` roles/securitycenter.admin ` （セキュリティ センター管理者）に追加されました。

` appengine.applications.get `  
` cloudsecurityscanner.crawledurls.list `  
` cloudsecurityscanner.results.get `  
` cloudsecurityscanner.results.list `  
` cloudsecurityscanner.scanruns.get `  
` cloudsecurityscanner.scanruns.getSummary `  
` cloudsecurityscanner.scanruns.list `  
` cloudsecurityscanner.scanruns.stop `  
` cloudsecurityscanner.scans.create `  
` cloudsecurityscanner.scans.delete `  
` cloudsecurityscanner.scans.get `  
` cloudsecurityscanner.scans.list `  
` cloudsecurityscanner.scans.run `  
` cloudsecurityscanner.scans.update `  
` compute.addresses.list `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
セキュリティ コマンド センター  |  役割の更新  |

次の権限が役割 ` roles/securitycenter.adminEditor ` （セキュリティ センター管理編集者）に追加されました。

` appengine.applications.get `  
` cloudsecurityscanner.crawledurls.list `  
` cloudsecurityscanner.results.get `  
` cloudsecurityscanner.results.list `  
` cloudsecurityscanner.scanruns.get `  
` cloudsecurityscanner.scanruns.getSummary `  
` cloudsecurityscanner.scanruns.list `  
` cloudsecurityscanner.scanruns.stop `  
` cloudsecurityscanner.scans.create `  
` cloudsecurityscanner.scans.delete `  
` cloudsecurityscanner.scans.get `  
` cloudsecurityscanner.scans.list `  
` cloudsecurityscanner.scans.run `  
` cloudsecurityscanner.scans.update `  
` compute.addresses.list `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
セキュリティ コマンド センター  |  役割の更新  |

次の権限が役割 ` roles/securitycenter.adminViewer ` （セキュリティ センター管理閲覧者）に追加されました。

` cloudsecurityscanner.crawledurls.list `  
` cloudsecurityscanner.results.get `  
` cloudsecurityscanner.results.list `  
` cloudsecurityscanner.scanruns.get `  
` cloudsecurityscanner.scanruns.getSummary `  
` cloudsecurityscanner.scanruns.list `  
` cloudsecurityscanner.scans.get `  
` cloudsecurityscanner.scans.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/viewer ` （閲覧者）に追加されました。

` healthcare.fhirStores.executeBundle `  
  
Google Cloud サポート  |  追加  |  ` cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Google Cloud サポート  |  カスタムの役割でサポート  |  ` cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Google Cloud サポート  |  一般提供開始  |  ` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Cloud Healthcare API  |  追加  |  ` healthcare.fhirStores.executeBundle `  
  
Cloud Logging  |  追加  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud Logging  |  カスタムの役割でサポート  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud Logging  |  一般提供開始  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
  
##  2020-02-07 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
シークレット マネージャー  |  一般提供開始  |

役割 ` roles/secretmanager.admin ` （Secret Manager 管理者）の一般提供を開始しました。  
  
シークレット マネージャー  |  一般提供開始  |

役割 ` roles/secretmanager.secretAccessor ` （Secret Manager のシークレット
アクセサー）の一般提供を開始しました。  
  
シークレット マネージャー  |  一般提供開始  |

役割 ` roles/secretmanager.viewer ` （Secret Manager 閲覧者）の一般提供を開始しました。  
  
Cloud Healthcare API  |  カスタムの役割でサポート  |  ` healthcare.datasets.create `  
` healthcare.datasets.deidentify `  
` healthcare.datasets.delete `  
` healthcare.datasets.get `  
` healthcare.datasets.getIamPolicy `  
` healthcare.datasets.list `  
` healthcare.datasets.setIamPolicy `  
` healthcare.datasets.update `  
` healthcare.dicomStores.create `  
` healthcare.dicomStores.delete `  
` healthcare.dicomStores.dicomWebDelete `  
` healthcare.dicomStores.dicomWebRead `  
` healthcare.dicomStores.dicomWebWrite `  
` healthcare.dicomStores.export `  
` healthcare.dicomStores.get `  
` healthcare.dicomStores.getIamPolicy `  
` healthcare.dicomStores.import `  
` healthcare.dicomStores.list `  
` healthcare.dicomStores.setIamPolicy `  
` healthcare.dicomStores.update `  
` healthcare.fhirResources.create `  
` healthcare.fhirResources.delete `  
` healthcare.fhirResources.get `  
` healthcare.fhirResources.patch `  
` healthcare.fhirResources.purge `  
` healthcare.fhirResources.update `  
` healthcare.fhirStores.create `  
` healthcare.fhirStores.delete `  
` healthcare.fhirStores.export `  
` healthcare.fhirStores.get `  
` healthcare.fhirStores.getIamPolicy `  
` healthcare.fhirStores.import `  
` healthcare.fhirStores.list `  
` healthcare.fhirStores.searchResources `  
` healthcare.fhirStores.setIamPolicy `  
` healthcare.fhirStores.update `  
` healthcare.hl7V2Messages.create `  
` healthcare.hl7V2Messages.delete `  
` healthcare.hl7V2Messages.get `  
` healthcare.hl7V2Messages.ingest `  
` healthcare.hl7V2Messages.list `  
` healthcare.hl7V2Messages.update `  
` healthcare.hl7V2Stores.create `  
` healthcare.hl7V2Stores.delete `  
` healthcare.hl7V2Stores.get `  
` healthcare.hl7V2Stores.getIamPolicy `  
` healthcare.hl7V2Stores.list `  
` healthcare.hl7V2Stores.setIamPolicy `  
` healthcare.hl7V2Stores.update `  
` healthcare.operations.get `  
` healthcare.operations.list `  
  
reCAPTCHA Enterprise  |  追加  |  ` recaptchaenterprise.assessments.annotate `  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
reCAPTCHA Enterprise  |  カスタムの役割でサポート  |  `
recaptchaenterprise.assessments.annotate `  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
シークレット マネージャー  |  カスタムの役割でサポート  |  ` secretmanager.locations.get `  
` secretmanager.locations.list `  
` secretmanager.secrets.create `  
` secretmanager.secrets.delete `  
` secretmanager.secrets.get `  
` secretmanager.secrets.getIamPolicy `  
` secretmanager.secrets.list `  
` secretmanager.secrets.setIamPolicy `  
` secretmanager.secrets.update `  
` secretmanager.versions.access `  
` secretmanager.versions.add `  
` secretmanager.versions.destroy `  
` secretmanager.versions.disable `  
` secretmanager.versions.enable `  
` secretmanager.versions.get `  
` secretmanager.versions.list `  
  
シークレット マネージャー  |  一般提供開始  |  ` secretmanager.locations.get `  
` secretmanager.locations.list `  
` secretmanager.secrets.create `  
` secretmanager.secrets.delete `  
` secretmanager.secrets.get `  
` secretmanager.secrets.getIamPolicy `  
` secretmanager.secrets.list `  
` secretmanager.secrets.setIamPolicy `  
` secretmanager.secrets.update `  
` secretmanager.versions.access `  
` secretmanager.versions.add `  
` secretmanager.versions.destroy `  
` secretmanager.versions.disable `  
` secretmanager.versions.enable `  
` secretmanager.versions.get `  
` secretmanager.versions.list `  
  
  
##  2020-01-31 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Build  |  役割の更新  |

次の権限が役割 ` roles/cloudbuild.builds.builder ` （Cloud Build サービス アカウント）に追加されました。

` artifactregistry.files.get `  
` artifactregistry.files.list `  
` artifactregistry.packages.get `  
` artifactregistry.packages.list `  
` artifactregistry.repositories.downloadArtifacts `  
` artifactregistry.repositories.get `  
` artifactregistry.repositories.list `  
` artifactregistry.repositories.uploadArtifacts `  
` artifactregistry.tags.create `  
` artifactregistry.tags.get `  
` artifactregistry.tags.list `  
` artifactregistry.tags.update `  
` artifactregistry.versions.get `  
` artifactregistry.versions.list `  
  
Cloud Composer  |  役割の更新  |

次の権限が役割 ` roles/composer.worker ` （Composer ワーカー）に追加されました。

` artifactregistry.files.get `  
` artifactregistry.files.list `  
` artifactregistry.packages.get `  
` artifactregistry.packages.list `  
` artifactregistry.repositories.downloadArtifacts `  
` artifactregistry.repositories.get `  
` artifactregistry.repositories.list `  
` artifactregistry.repositories.uploadArtifacts `  
` artifactregistry.tags.create `  
` artifactregistry.tags.get `  
` artifactregistry.tags.list `  
` artifactregistry.tags.update `  
` artifactregistry.versions.get `  
` artifactregistry.versions.list `  
  
Google Cloud Game Servers  |  追加  |  ` gameservices.gameServerClusters.create
`  
` gameservices.gameServerClusters.delete `  
` gameservices.gameServerClusters.get `  
` gameservices.gameServerClusters.list `  
` gameservices.gameServerClusters.update `  
` gameservices.gameServerConfigs.create `  
` gameservices.gameServerConfigs.delete `  
` gameservices.gameServerConfigs.get `  
` gameservices.gameServerConfigs.list `  
` gameservices.gameServerDeployments.create `  
` gameservices.gameServerDeployments.delete `  
` gameservices.gameServerDeployments.get `  
` gameservices.gameServerDeployments.list `  
` gameservices.gameServerDeployments.rollout `  
` gameservices.gameServerDeployments.update `  
` gameservices.locations.get `  
` gameservices.locations.list `  
` gameservices.operations.cancel `  
` gameservices.operations.delete `  
` gameservices.operations.get `  
` gameservices.operations.list `  
` gameservices.realms.create `  
` gameservices.realms.delete `  
` gameservices.realms.get `  
` gameservices.realms.list `  
` gameservices.realms.update `  
  
Google Cloud Game Servers  |  カスタムの役割でサポート  |  `
gameservices.gameServerClusters.create `  
` gameservices.gameServerClusters.delete `  
` gameservices.gameServerClusters.get `  
` gameservices.gameServerClusters.list `  
` gameservices.gameServerClusters.update `  
` gameservices.gameServerConfigs.create `  
` gameservices.gameServerConfigs.delete `  
` gameservices.gameServerConfigs.get `  
` gameservices.gameServerConfigs.list `  
` gameservices.gameServerDeployments.create `  
` gameservices.gameServerDeployments.delete `  
` gameservices.gameServerDeployments.get `  
` gameservices.gameServerDeployments.list `  
` gameservices.gameServerDeployments.rollout `  
` gameservices.gameServerDeployments.update `  
` gameservices.locations.get `  
` gameservices.locations.list `  
` gameservices.operations.cancel `  
` gameservices.operations.delete `  
` gameservices.operations.get `  
` gameservices.operations.list `  
` gameservices.realms.create `  
` gameservices.realms.delete `  
` gameservices.realms.get `  
` gameservices.realms.list `  
` gameservices.realms.update `  
  
Google Cloud オペレーションスイート  |  追加  |  `
opsconfigmonitoring.resourceMetadata.write `  
  
  
##  2020-01-24 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Scheduler  |  役割の更新  |

次の権限が役割 ` roles/cloudscheduler.admin ` （Cloud Scheduler 管理者）に追加されました。

` serviceusage.services.list `  
  
Cloud Scheduler  |  役割の更新  |

次の権限が役割 ` roles/cloudscheduler.jobRunner ` （Cloud Scheduler ジョブ実行者）に追加されました。

` serviceusage.services.list `  
  
Cloud Scheduler  |  役割の更新  |

次の権限が役割 ` roles/cloudscheduler.viewer ` （Cloud Scheduler 閲覧者）に追加されました。

` serviceusage.services.list `  
  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.networkAdmin ` （Compute ネットワーク 管理者）に追加されました。

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.networkViewer ` （Compute ネットワーク 閲覧者）に追加されました。

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.notificationConfigEditor ` （セキュリティ
センター通知構成編集者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.notificationConfigViewer ` （セキュリティ
センター通知構成閲覧者）の一般提供を開始しました。  
  
Artifact Registry  |  追加  |  ` artifactregistry.files.get `  
` artifactregistry.files.list `  
` artifactregistry.packages.delete `  
` artifactregistry.packages.get `  
` artifactregistry.packages.list `  
` artifactregistry.repositories.create `  
` artifactregistry.repositories.delete `  
` artifactregistry.repositories.deleteArtifacts `  
` artifactregistry.repositories.downloadArtifacts `  
` artifactregistry.repositories.get `  
` artifactregistry.repositories.getIamPolicy `  
` artifactregistry.repositories.list `  
` artifactregistry.repositories.setIamPolicy `  
` artifactregistry.repositories.update `  
` artifactregistry.repositories.uploadArtifacts `  
` artifactregistry.tags.create `  
` artifactregistry.tags.delete `  
` artifactregistry.tags.get `  
` artifactregistry.tags.list `  
` artifactregistry.tags.update `  
` artifactregistry.versions.delete `  
` artifactregistry.versions.get `  
` artifactregistry.versions.list `  
  
Artifact Registry  |  カスタムの役割でサポート  |  ` artifactregistry.files.get `  
` artifactregistry.files.list `  
` artifactregistry.packages.delete `  
` artifactregistry.packages.get `  
` artifactregistry.packages.list `  
` artifactregistry.repositories.create `  
` artifactregistry.repositories.delete `  
` artifactregistry.repositories.deleteArtifacts `  
` artifactregistry.repositories.downloadArtifacts `  
` artifactregistry.repositories.get `  
` artifactregistry.repositories.getIamPolicy `  
` artifactregistry.repositories.list `  
` artifactregistry.repositories.setIamPolicy `  
` artifactregistry.repositories.update `  
` artifactregistry.repositories.uploadArtifacts `  
` artifactregistry.tags.create `  
` artifactregistry.tags.delete `  
` artifactregistry.tags.get `  
` artifactregistry.tags.list `  
` artifactregistry.tags.update `  
` artifactregistry.versions.delete `  
` artifactregistry.versions.get `  
` artifactregistry.versions.list `  
  
Cloud Identity and Access Management  |  追加  |  `
iam.serviceAccounts.getOpenIdToken `  
  
セキュリティ コマンド センター  |  追加  |  ` securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
セキュリティ コマンド センター  |  カスタムの役割でサポート  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
セキュリティ コマンド センター  |  一般提供開始  |  ` securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
  
##  2020-01-10 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Asset Inventory  |  一般提供開始  |

役割 ` roles/cloudasset.owner ` （Cloud Asset オーナー）の一般提供を開始しました。  
  
Compute Engine の移行  |  役割の更新  |

次の権限が役割 ` roles/cloudmigration.inframanager ` （Velostrata Manager）に追加されました。

` compute.globalOperations.get `  
  
Cloud Spanner  |  役割の更新  |

次の権限が役割 ` roles/spanner.databaseReader ` （Cloud Spanner データベース読み取り）に追加されました。

` spanner.instances.get `  
  
Cloud Spanner  |  役割の更新  |

次の権限が役割 ` roles/spanner.databaseUser ` （Cloud Spanner データベース ユーザー）に追加されました。

` spanner.instances.get `  
  
Cloud Asset Inventory  |  一般提供開始  |  ` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Compute Engine  |  追加  |  ` compute.networks.listPeeringRoutes `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.networks.listPeeringRoutes `  
  
Compute Engine  |  一般提供開始  |  ` compute.networks.listPeeringRoutes `  
  
ネットワーク管理 API  |  追加  |  ` networkmanagement.connectivitytests.create `  
` networkmanagement.connectivitytests.delete `  
` networkmanagement.connectivitytests.get `  
` networkmanagement.connectivitytests.getIamPolicy `  
` networkmanagement.connectivitytests.list `  
` networkmanagement.connectivitytests.rerun `  
` networkmanagement.connectivitytests.setIamPolicy `  
` networkmanagement.connectivitytests.update `  
` networkmanagement.locations.get `  
` networkmanagement.locations.list `  
` networkmanagement.operations.get `  
` networkmanagement.operations.list `  
  
ネットワーク管理 API  |  カスタムの役割でサポート  |  ` networkmanagement.connectivitytests.create
`  
` networkmanagement.connectivitytests.delete `  
` networkmanagement.connectivitytests.get `  
` networkmanagement.connectivitytests.getIamPolicy `  
` networkmanagement.connectivitytests.list `  
` networkmanagement.connectivitytests.rerun `  
` networkmanagement.connectivitytests.setIamPolicy `  
` networkmanagement.connectivitytests.update `  
` networkmanagement.locations.get `  
` networkmanagement.locations.list `  
` networkmanagement.operations.get `  
` networkmanagement.operations.list `  
  
  
##  2019-12-20 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine の移行  |  役割の更新  |

次の権限が役割 ` roles/cloudmigration.inframanager ` （Velostrata Manager）に追加されました。

` compute.disks.createSnapshot `  
` compute.snapshots.create `  
` compute.snapshots.delete `  
` compute.snapshots.get `  
` compute.snapshots.setLabels `  
` compute.snapshots.useReadOnly `  
  
Cloud Scheduler  |  役割の更新  |

次の権限が役割 ` roles/cloudscheduler.admin ` （Cloud Scheduler 管理者）に追加されました。

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud Scheduler  |  役割の更新  |

次の権限が役割 ` roles/cloudscheduler.jobRunner ` （Cloud Scheduler ジョブ実行者）に追加されました。

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud Scheduler  |  役割の更新  |

次の権限が役割 ` roles/cloudscheduler.viewer ` （Cloud Scheduler 閲覧者）に追加されました。

` appengine.applications.get `  
` serviceusage.services.get `  
  
Compute Engine  |  一般提供開始  |

役割 ` roles/compute.packetMirroringAdmin ` （コンピューティング パケット
ミラーリング管理者）の一般提供を開始しました。  
  
Compute Engine  |  一般提供開始  |

役割 ` roles/compute.packetMirroringUser ` （コンピューティング パケット ミラーリング
ユーザー）の一般提供を開始しました。  
  
Cloud DNS  |  一般提供開始  |

役割 ` roles/dns.peer ` （DNS ピア）の一般提供を開始しました。  
  
基本の役割  |  役割の更新  |

役割 ` roles/editor ` （編集者）から次の権限が削除されました。

` datacatalog.taxonomies.create `  
  
推薦者  |  一般提供開始  |

役割 ` roles/recommender.computeAdmin ` （コンピューティング推奨事項の管理者）の一般提供を開始しました。  
  
推薦者  |  一般提供開始  |

役割 ` roles/recommender.computeViewer ` （コンピューティング推奨事項の閲覧者）の一般提供を開始しました。  
  
推薦者  |  一般提供開始  |

役割 ` roles/recommender.iamAdmin ` （IAM 推奨事項の管理者）の一般提供を開始しました。  
  
推薦者  |  一般提供開始  |

役割 ` roles/recommender.iamViewer ` （IAM 推奨事項の閲覧者）の一般提供を開始しました。  
  
Remote Build Execution  |  役割の追加  |

以下の権限を持つ役割 ` roles/remotebuildexecution.reservationAdmin ` （Remote Build
Execution 予約管理者）が次の権限で追加されました。

` remotebuildexecution.actions.create `  
` remotebuildexecution.actions.delete `  
` remotebuildexecution.actions.get `  
  
Cloud Bigtable  |  追加  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  カスタムの役割でサポート  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  一般提供開始  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Compute Engine  |  追加  |  ` compute.nodeGroups.update `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.nodeGroups.update `  
  
Compute Engine  |  一般提供開始  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
データカタログ  |  追加  |  ` datacatalog.entries.list `  
` datacatalog.entries.updateTag `  
` datacatalog.entryGroups.update `  
  
Dataproc  |  追加  |  ` dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
Dataproc  |  一般提供開始  |  ` dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
Cloud DNS  |  一般提供開始  |  ` dns.networks.targetWithPeeringZone `  
  
Cloud Logging  |  追加  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud Logging  |  カスタムの役割でサポート  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud Logging  |  一般提供開始  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
推薦者  |  一般提供開始  |  `
recommender.computeInstanceGroupManagerMachineTypeRecommendations.get `  
` recommender.computeInstanceGroupManagerMachineTypeRecommendations.list `  
` recommender.computeInstanceGroupManagerMachineTypeRecommendations.update `  
` recommender.computeInstanceMachineTypeRecommendations.get `  
` recommender.computeInstanceMachineTypeRecommendations.list `  
` recommender.computeInstanceMachineTypeRecommendations.update `  
` recommender.iamPolicyRecommendations.get `  
` recommender.iamPolicyRecommendations.list `  
` recommender.iamPolicyRecommendations.update `  
` recommender.locations.get `  
` recommender.locations.list `  
  
  
##  2019-11-22 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
データカタログ  |  役割の更新  |

次の権限が役割 ` roles/datacatalog.admin ` （Data Catalog 管理者）から削除されました。

` datacatalog.categories.fineGrainedGet `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/editor ` （編集者）に追加されました。

` remotebuildexecution.actions.delete `  
  
Identity Toolkit API  |  一般提供開始  |

役割 ` roles/identitytoolkit.admin ` （Identity Toolkit 管理者）の一般提供を開始しました。  
  
Identity Toolkit API  |  一般提供開始  |

役割 ` roles/identitytoolkit.viewer ` （Identity Toolkit 閲覧者）の一般提供を開始しました。  
  
Apigee API  |  追加  |  ` apigee.apiproductattributes.createOrUpdateAll `  
` apigee.apiproductattributes.delete `  
` apigee.apiproductattributes.get `  
` apigee.apiproductattributes.list `  
` apigee.apiproductattributes.update `  
` apigee.apiproducts.create `  
` apigee.apiproducts.delete `  
` apigee.apiproducts.get `  
` apigee.apiproducts.list `  
` apigee.apiproducts.update `  
` apigee.appkeys.create `  
` apigee.appkeys.delete `  
` apigee.appkeys.get `  
` apigee.appkeys.manage `  
` apigee.apps.get `  
` apigee.apps.list `  
` apigee.deployments.create `  
` apigee.deployments.delete `  
` apigee.deployments.get `  
` apigee.deployments.list `  
` apigee.deployments.update `  
` apigee.developerappattributes.createOrUpdateAll `  
` apigee.developerappattributes.delete `  
` apigee.developerappattributes.get `  
` apigee.developerappattributes.list `  
` apigee.developerappattributes.update `  
` apigee.developerapps.create `  
` apigee.developerapps.delete `  
` apigee.developerapps.get `  
` apigee.developerapps.list `  
` apigee.developerapps.manage `  
` apigee.developerattributes.createOrUpdateAll `  
` apigee.developerattributes.delete `  
` apigee.developerattributes.get `  
` apigee.developerattributes.list `  
` apigee.developerattributes.update `  
` apigee.developers.create `  
` apigee.developers.delete `  
` apigee.developers.get `  
` apigee.developers.list `  
` apigee.developers.update `  
` apigee.environments.create `  
` apigee.environments.delete `  
` apigee.environments.get `  
` apigee.environments.getDataLocation `  
` apigee.environments.getIamPolicy `  
` apigee.environments.getStats `  
` apigee.environments.list `  
` apigee.environments.manageRuntime `  
` apigee.environments.setIamPolicy `  
` apigee.environments.update `  
` apigee.flowhooks.attachSharedFlow `  
` apigee.flowhooks.detachSharedFlow `  
` apigee.flowhooks.getSharedFlow `  
` apigee.flowhooks.list `  
` apigee.keystorealiases.create `  
` apigee.keystorealiases.delete `  
` apigee.keystorealiases.exportCertificate `  
` apigee.keystorealiases.generateCSR `  
` apigee.keystorealiases.get `  
` apigee.keystorealiases.list `  
` apigee.keystorealiases.update `  
` apigee.keystores.create `  
` apigee.keystores.delete `  
` apigee.keystores.export `  
` apigee.keystores.get `  
` apigee.keystores.list `  
` apigee.keyvaluemaps.create `  
` apigee.keyvaluemaps.delete `  
` apigee.keyvaluemaps.list `  
` apigee.maskconfigs.get `  
` apigee.maskconfigs.update `  
` apigee.organizations.create `  
` apigee.organizations.get `  
` apigee.organizations.list `  
` apigee.organizations.update `  
` apigee.proxies.create `  
` apigee.proxies.delete `  
` apigee.proxies.get `  
` apigee.proxies.list `  
` apigee.proxyrevisions.delete `  
` apigee.proxyrevisions.deploy `  
` apigee.proxyrevisions.get `  
` apigee.proxyrevisions.list `  
` apigee.proxyrevisions.undeploy `  
` apigee.proxyrevisions.update `  
` apigee.queries.create `  
` apigee.queries.get `  
` apigee.queries.list `  
` apigee.references.create `  
` apigee.references.delete `  
` apigee.references.get `  
` apigee.references.list `  
` apigee.references.update `  
` apigee.reports.create `  
` apigee.reports.delete `  
` apigee.reports.get `  
` apigee.reports.list `  
` apigee.reports.update `  
` apigee.resourcefiles.create `  
` apigee.resourcefiles.delete `  
` apigee.resourcefiles.get `  
` apigee.resourcefiles.list `  
` apigee.resourcefiles.update `  
` apigee.sharedflowrevisions.delete `  
` apigee.sharedflowrevisions.deploy `  
` apigee.sharedflowrevisions.get `  
` apigee.sharedflowrevisions.list `  
` apigee.sharedflowrevisions.undeploy `  
` apigee.sharedflowrevisions.update `  
` apigee.sharedflows.create `  
` apigee.sharedflows.delete `  
` apigee.sharedflows.get `  
` apigee.sharedflows.list `  
` apigee.targetservers.create `  
` apigee.targetservers.delete `  
` apigee.targetservers.get `  
` apigee.targetservers.list `  
` apigee.targetservers.update `  
` apigee.tracesessions.create `  
` apigee.tracesessions.delete `  
` apigee.tracesessions.get `  
` apigee.tracesessions.list `  
  
Apigee API  |  カスタムの役割でサポート  |  `
apigee.apiproductattributes.createOrUpdateAll `  
` apigee.apiproductattributes.delete `  
` apigee.apiproductattributes.get `  
` apigee.apiproductattributes.list `  
` apigee.apiproductattributes.update `  
` apigee.apiproducts.create `  
` apigee.apiproducts.delete `  
` apigee.apiproducts.get `  
` apigee.apiproducts.list `  
` apigee.apiproducts.update `  
` apigee.appkeys.create `  
` apigee.appkeys.delete `  
` apigee.appkeys.get `  
` apigee.appkeys.manage `  
` apigee.apps.get `  
` apigee.apps.list `  
` apigee.deployments.create `  
` apigee.deployments.delete `  
` apigee.deployments.get `  
` apigee.deployments.list `  
` apigee.deployments.update `  
` apigee.developerappattributes.createOrUpdateAll `  
` apigee.developerappattributes.delete `  
` apigee.developerappattributes.get `  
` apigee.developerappattributes.list `  
` apigee.developerappattributes.update `  
` apigee.developerapps.create `  
` apigee.developerapps.delete `  
` apigee.developerapps.get `  
` apigee.developerapps.list `  
` apigee.developerapps.manage `  
` apigee.developerattributes.createOrUpdateAll `  
` apigee.developerattributes.delete `  
` apigee.developerattributes.get `  
` apigee.developerattributes.list `  
` apigee.developerattributes.update `  
` apigee.developers.create `  
` apigee.developers.delete `  
` apigee.developers.get `  
` apigee.developers.list `  
` apigee.developers.update `  
` apigee.environments.create `  
` apigee.environments.delete `  
` apigee.environments.get `  
` apigee.environments.getDataLocation `  
` apigee.environments.getIamPolicy `  
` apigee.environments.getStats `  
` apigee.environments.list `  
` apigee.environments.manageRuntime `  
` apigee.environments.setIamPolicy `  
` apigee.environments.update `  
` apigee.flowhooks.attachSharedFlow `  
` apigee.flowhooks.detachSharedFlow `  
` apigee.flowhooks.getSharedFlow `  
` apigee.flowhooks.list `  
` apigee.keystorealiases.create `  
` apigee.keystorealiases.delete `  
` apigee.keystorealiases.exportCertificate `  
` apigee.keystorealiases.generateCSR `  
` apigee.keystorealiases.get `  
` apigee.keystorealiases.list `  
` apigee.keystorealiases.update `  
` apigee.keystores.create `  
` apigee.keystores.delete `  
` apigee.keystores.export `  
` apigee.keystores.get `  
` apigee.keystores.list `  
` apigee.keyvaluemaps.create `  
` apigee.keyvaluemaps.delete `  
` apigee.keyvaluemaps.list `  
` apigee.maskconfigs.get `  
` apigee.maskconfigs.update `  
` apigee.organizations.create `  
` apigee.organizations.get `  
` apigee.organizations.list `  
` apigee.organizations.update `  
` apigee.proxies.create `  
` apigee.proxies.delete `  
` apigee.proxies.get `  
` apigee.proxies.list `  
` apigee.proxyrevisions.delete `  
` apigee.proxyrevisions.deploy `  
` apigee.proxyrevisions.get `  
` apigee.proxyrevisions.list `  
` apigee.proxyrevisions.undeploy `  
` apigee.proxyrevisions.update `  
` apigee.queries.create `  
` apigee.queries.get `  
` apigee.queries.list `  
` apigee.references.create `  
` apigee.references.delete `  
` apigee.references.get `  
` apigee.references.list `  
` apigee.references.update `  
` apigee.reports.create `  
` apigee.reports.delete `  
` apigee.reports.get `  
` apigee.reports.list `  
` apigee.reports.update `  
` apigee.resourcefiles.create `  
` apigee.resourcefiles.delete `  
` apigee.resourcefiles.get `  
` apigee.resourcefiles.list `  
` apigee.resourcefiles.update `  
` apigee.sharedflowrevisions.delete `  
` apigee.sharedflowrevisions.deploy `  
` apigee.sharedflowrevisions.get `  
` apigee.sharedflowrevisions.list `  
` apigee.sharedflowrevisions.undeploy `  
` apigee.sharedflowrevisions.update `  
` apigee.sharedflows.create `  
` apigee.sharedflows.delete `  
` apigee.sharedflows.get `  
` apigee.sharedflows.list `  
` apigee.targetservers.create `  
` apigee.targetservers.delete `  
` apigee.targetservers.get `  
` apigee.targetservers.list `  
` apigee.targetservers.update `  
` apigee.tracesessions.create `  
` apigee.tracesessions.delete `  
` apigee.tracesessions.get `  
` apigee.tracesessions.list `  
  
BigQuery  |  追加  |  ` bigquery.tables.setCategory `  
  
Compute Engine  |  追加  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Remote Build Execution  |  追加  |  ` remotebuildexecution.actions.delete `  
  
Remote Build Execution  |  カスタムの役割でサポート  |  `
remotebuildexecution.actions.delete `  
  
  
##  2019-11-14 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
アクセス承認  |  追加  |  ` accessapproval.settings.delete `  
  
AI Platform ノートブック  |  追加  |  ` notebooks.environments.create `  
` notebooks.environments.delete `  
` notebooks.environments.get `  
` notebooks.environments.getIamPolicy `  
` notebooks.environments.list `  
` notebooks.environments.setIamPolicy `  
` notebooks.instances.create `  
` notebooks.instances.delete `  
` notebooks.instances.get `  
` notebooks.instances.getIamPolicy `  
` notebooks.instances.list `  
` notebooks.instances.setIamPolicy `  
` notebooks.instances.update `  
` notebooks.locations.get `  
` notebooks.locations.list `  
` notebooks.operations.cancel `  
` notebooks.operations.delete `  
` notebooks.operations.get `  
` notebooks.operations.list `  
  
AI Platform ノートブック  |  カスタムの役割でサポート  |  ` notebooks.environments.create `  
` notebooks.environments.delete `  
` notebooks.environments.get `  
` notebooks.environments.getIamPolicy `  
` notebooks.environments.list `  
` notebooks.environments.setIamPolicy `  
` notebooks.instances.create `  
` notebooks.instances.delete `  
` notebooks.instances.get `  
` notebooks.instances.getIamPolicy `  
` notebooks.instances.list `  
` notebooks.instances.setIamPolicy `  
` notebooks.instances.update `  
` notebooks.locations.get `  
` notebooks.locations.list `  
` notebooks.operations.cancel `  
` notebooks.operations.delete `  
` notebooks.operations.get `  
` notebooks.operations.list `  
  
  
##  2019-11-01 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Hangouts Chat API  |  一般提供開始  |

役割 ` roles/chat.owner ` （チャットボット オーナー）の一般提供を開始しました。  
  
Hangouts Chat API  |  一般提供開始  |

役割 ` roles/chat.reader ` （チャットボット閲覧者）の一般提供を開始しました。  
  
Hangouts Chat API  |  一般提供開始  |  ` chat.bots.get `  
` chat.bots.update `  
  
Cloud Asset Inventory  |  追加  |  `
cloudasset.assets.exportAppengineApplications `  
` cloudasset.assets.exportAppengineServices `  
` cloudasset.assets.exportAppengineVersions `  
` cloudasset.assets.exportBigqueryDatasets `  
` cloudasset.assets.exportBigqueryTables `  
` cloudasset.assets.exportBigtableCluster `  
` cloudasset.assets.exportBigtableInstance `  
` cloudasset.assets.exportBigtableTable `  
` cloudasset.assets.exportCloudbillingBillingAccounts `  
` cloudasset.assets.exportCloudkmsCryptoKeyVersions `  
` cloudasset.assets.exportCloudkmsCryptoKeys `  
` cloudasset.assets.exportCloudkmsKeyRings `  
` cloudasset.assets.exportCloudresourcemanagerFolders `  
` cloudasset.assets.exportCloudresourcemanagerOrganizations `  
` cloudasset.assets.exportCloudresourcemanagerProjects `  
` cloudasset.assets.exportComputeAddress `  
` cloudasset.assets.exportComputeAutoscalers `  
` cloudasset.assets.exportComputeBackendBuckets `  
` cloudasset.assets.exportComputeBackendServices `  
` cloudasset.assets.exportComputeDisks `  
` cloudasset.assets.exportComputeFirewalls `  
` cloudasset.assets.exportComputeForwardingRules `  
` cloudasset.assets.exportComputeGlobalAddress `  
` cloudasset.assets.exportComputeGlobalForwardingRules `  
` cloudasset.assets.exportComputeHealthChecks `  
` cloudasset.assets.exportComputeHttpHealthChecks `  
` cloudasset.assets.exportComputeHttpsHealthChecks `  
` cloudasset.assets.exportComputeImages `  
` cloudasset.assets.exportComputeInstanceGroupManagers `  
` cloudasset.assets.exportComputeInstanceGroups `  
` cloudasset.assets.exportComputeInstanceTemplates `  
` cloudasset.assets.exportComputeInstances `  
` cloudasset.assets.exportComputeInterconnect `  
` cloudasset.assets.exportComputeInterconnectAttachment `  
` cloudasset.assets.exportComputeLicenses `  
` cloudasset.assets.exportComputeNetworks `  
` cloudasset.assets.exportComputeProjects `  
` cloudasset.assets.exportComputeRegionAutoscaler `  
` cloudasset.assets.exportComputeRegionBackendServices `  
` cloudasset.assets.exportComputeRegionDisk `  
` cloudasset.assets.exportComputeRegionInstanceGroup `  
` cloudasset.assets.exportComputeRegionInstanceGroupManager `  
` cloudasset.assets.exportComputeRouters `  
` cloudasset.assets.exportComputeRoutes `  
` cloudasset.assets.exportComputeSecurityPolicy `  
` cloudasset.assets.exportComputeSnapshots `  
` cloudasset.assets.exportComputeSslCertificates `  
` cloudasset.assets.exportComputeSubnetworks `  
` cloudasset.assets.exportComputeTargetHttpProxies `  
` cloudasset.assets.exportComputeTargetHttpsProxies `  
` cloudasset.assets.exportComputeTargetInstances `  
` cloudasset.assets.exportComputeTargetPools `  
` cloudasset.assets.exportComputeTargetSslProxies `  
` cloudasset.assets.exportComputeTargetTcpProxies `  
` cloudasset.assets.exportComputeTargetVpnGateways `  
` cloudasset.assets.exportComputeUrlMaps `  
` cloudasset.assets.exportComputeVpnTunnels `  
` cloudasset.assets.exportContainerClusterrole `  
` cloudasset.assets.exportContainerClusterrolebinding `  
` cloudasset.assets.exportContainerClusters `  
` cloudasset.assets.exportContainerNamespace `  
` cloudasset.assets.exportContainerNode `  
` cloudasset.assets.exportContainerNodepool `  
` cloudasset.assets.exportContainerPod `  
` cloudasset.assets.exportContainerRole `  
` cloudasset.assets.exportContainerRolebinding `  
` cloudasset.assets.exportContainerregistryImage `  
` cloudasset.assets.exportDatafusionInstance `  
` cloudasset.assets.exportDataprocClusters `  
` cloudasset.assets.exportDataprocJobs `  
` cloudasset.assets.exportDnsManagedZones `  
` cloudasset.assets.exportDnsPolicies `  
` cloudasset.assets.exportIamRoles `  
` cloudasset.assets.exportIamServiceAccountKeys `  
` cloudasset.assets.exportIamServiceAccounts `  
` cloudasset.assets.exportManagedidentitiesDomain `  
` cloudasset.assets.exportPubsubSubscriptions `  
` cloudasset.assets.exportPubsubTopics `  
` cloudasset.assets.exportServicemanagementServices `  
` cloudasset.assets.exportSpannerDatabases `  
` cloudasset.assets.exportSpannerInstances `  
` cloudasset.assets.exportSqladminInstances `  
` cloudasset.assets.exportStorageBuckets `  
  
データカタログ  |  追加  |  ` datacatalog.categories.fineGrainedGet `  
` datacatalog.categories.getIamPolicy `  
` datacatalog.categories.setIamPolicy `  
` datacatalog.taxonomies.create `  
` datacatalog.taxonomies.delete `  
` datacatalog.taxonomies.get `  
` datacatalog.taxonomies.getIamPolicy `  
` datacatalog.taxonomies.list `  
` datacatalog.taxonomies.setIamPolicy `  
` datacatalog.taxonomies.update `  
  
Identity-Aware Proxy  |  追加  |  ` iap.projects.getSettings `  
` iap.projects.updateSettings `  
  
NetApp Cloud Volumes Service  |  追加  |  ` netappcloudvolumes.jobs.get `  
` netappcloudvolumes.jobs.list `  
  
Redis Enterprise Cloud  |  追加  |  ` redisenterprisecloud.databases.create `  
` redisenterprisecloud.databases.delete `  
` redisenterprisecloud.databases.get `  
` redisenterprisecloud.databases.list `  
` redisenterprisecloud.databases.update `  
` redisenterprisecloud.subscriptions.create `  
` redisenterprisecloud.subscriptions.delete `  
` redisenterprisecloud.subscriptions.get `  
` redisenterprisecloud.subscriptions.list `  
` redisenterprisecloud.subscriptions.update `  
  
  
##  2019-10-25 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Identity-Aware Proxy  |  一般提供開始  |

役割 ` roles/iap.tunnelResourceAccessor ` （IAP で保護されたトンネル ユーザー）の一般提供を開始しました。  
  
Microsoft Active Directory のマネージド サービス  |  一般提供開始  |

役割 ` roles/managedidentities.admin ` （Google Cloud Managed Identities
管理者）の一般提供を開始しました。  
  
Microsoft Active Directory のマネージド サービス  |  一般提供開始  |

役割 ` roles/managedidentities.domainAdmin ` （Google Cloud Managed Identities
ドメイン管理者）の一般提供を開始しました。  
  
Microsoft Active Directory のマネージド サービス  |  一般提供開始  |

役割 ` roles/managedidentities.viewer ` （Google Cloud Managed Identities
閲覧者）の一般提供を開始しました。  
  
Actions API  |  追加  |  ` actions.agentVersions.get `  
  
Actions API  |  カスタムの役割でサポート  |  ` actions.agentVersions.get `  
  
Actions API  |  一般提供開始  |  ` actions.agentVersions.get `  
  
Dialogflow  |  追加  |  ` dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
Dialogflow  |  一般提供開始  |  ` dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
Identity-Aware Proxy  |  一般提供開始  |  ` iap.tunnel.getIamPolicy `  
` iap.tunnel.setIamPolicy `  
` iap.tunnelInstances.accessViaIAP `  
` iap.tunnelInstances.getIamPolicy `  
` iap.tunnelInstances.setIamPolicy `  
` iap.tunnelZones.getIamPolicy `  
` iap.tunnelZones.setIamPolicy `  
  
Microsoft Active Directory のマネージド サービス  |  一般提供開始  |  `
managedidentities.domains.attachTrust `  
` managedidentities.domains.create `  
` managedidentities.domains.delete `  
` managedidentities.domains.detachTrust `  
` managedidentities.domains.get `  
` managedidentities.domains.getIamPolicy `  
` managedidentities.domains.list `  
` managedidentities.domains.reconfigureTrust `  
` managedidentities.domains.resetpassword `  
` managedidentities.domains.setIamPolicy `  
` managedidentities.domains.update `  
` managedidentities.domains.validateTrust `  
` managedidentities.locations.get `  
` managedidentities.locations.list `  
` managedidentities.operations.cancel `  
` managedidentities.operations.delete `  
` managedidentities.operations.get `  
` managedidentities.operations.list `  
  
  
##  2019-10-18 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Identity-Aware Proxy  |  一般提供開始  |

役割 ` roles/iap.settingsAdmin ` （IAP 設定管理者）の一般提供を開始しました。  
  
Identity-Aware Proxy  |  追加  |  ` iap.web.getSettings `  
` iap.web.updateSettings `  
` iap.webServiceVersions.getSettings `  
` iap.webServiceVersions.updateSettings `  
` iap.webServices.getSettings `  
` iap.webServices.updateSettings `  
` iap.webTypes.getSettings `  
` iap.webTypes.updateSettings `  
  
  
##  2019-10-11 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Firebase セキュリティ ルール  |  一般提供開始  |

役割 ` roles/firebaserules.admin ` （Firebase ルール管理者）の一般提供を開始しました。  
  
Firebase セキュリティ ルール  |  一般提供開始  |

役割 ` roles/firebaserules.viewer ` （Firebase Rules 閲覧者）の一般提供を開始しました。  
  
BigQuery  |  カスタムの役割でサポート  |  ` bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Google Kubernetes Engine  |  追加  |  ` container.csiDrivers.create `  
` container.csiDrivers.delete `  
` container.csiDrivers.get `  
` container.csiDrivers.list `  
` container.csiDrivers.update `  
` container.csiNodes.create `  
` container.csiNodes.delete `  
` container.csiNodes.get `  
` container.csiNodes.list `  
` container.csiNodes.update `  
` container.runtimeClasses.create `  
` container.runtimeClasses.delete `  
` container.runtimeClasses.get `  
` container.runtimeClasses.list `  
` container.runtimeClasses.update `  
  
Google Kubernetes Engine  |  カスタムの役割でサポート  |  ` container.csiDrivers.create `  
` container.csiDrivers.delete `  
` container.csiDrivers.get `  
` container.csiDrivers.list `  
` container.csiDrivers.update `  
` container.csiNodes.create `  
` container.csiNodes.delete `  
` container.csiNodes.get `  
` container.csiNodes.list `  
` container.csiNodes.update `  
` container.runtimeClasses.create `  
` container.runtimeClasses.delete `  
` container.runtimeClasses.get `  
` container.runtimeClasses.list `  
` container.runtimeClasses.update `  
  
Google Kubernetes Engine  |  一般提供開始  |  ` container.csiDrivers.create `  
` container.csiDrivers.delete `  
` container.csiDrivers.get `  
` container.csiDrivers.list `  
` container.csiDrivers.update `  
` container.csiNodes.create `  
` container.csiNodes.delete `  
` container.csiNodes.get `  
` container.csiNodes.list `  
` container.csiNodes.update `  
` container.runtimeClasses.create `  
` container.runtimeClasses.delete `  
` container.runtimeClasses.get `  
` container.runtimeClasses.list `  
` container.runtimeClasses.update `  
  
Firebase セキュリティ ルール  |  一般提供開始  |  ` firebaserules.releases.create `  
` firebaserules.releases.delete `  
` firebaserules.releases.get `  
` firebaserules.releases.getExecutable `  
` firebaserules.releases.list `  
` firebaserules.releases.update `  
` firebaserules.rulesets.create `  
` firebaserules.rulesets.delete `  
` firebaserules.rulesets.get `  
` firebaserules.rulesets.list `  
` firebaserules.rulesets.test `  
  
  
##  2019-10-04 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Actions API  |  追加  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Actions API  |  カスタムの役割でサポート  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Actions API  |  一般提供開始  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Cloud Identity and Access Management  |  カスタムの役割でサポート  |  `
iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
  
  
##  2019-09-27 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Hangouts Chat API  |  追加  |  ` chat.bots.get `  
` chat.bots.update `  
  
Hangouts Chat API  |  カスタムの役割でサポート  |  ` chat.bots.get `  
` chat.bots.update `  
  
Cloud Asset Inventory  |  追加  |  ` cloudasset.assets.exportAccessLevel `  
` cloudasset.assets.exportAccessPolicy `  
` cloudasset.assets.exportAllAccessPolicy `  
` cloudasset.assets.exportOrgPolicy `  
` cloudasset.assets.exportServicePerimeter `  
` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Cloud Asset Inventory  |  カスタムの役割でサポート  |  `
cloudasset.assets.exportAccessPolicy `  
` cloudasset.assets.exportOrgPolicy `  
` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Cloud Identity and Access Management  |  カスタムの役割でサポート  |  `
iam.serviceAccountKeys.create `  
` iam.serviceAccountKeys.delete `  
` iam.serviceAccountKeys.get `  
` iam.serviceAccountKeys.list `  
` iam.serviceAccounts.create `  
` iam.serviceAccounts.delete `  
` iam.serviceAccounts.get `  
` iam.serviceAccounts.getIamPolicy `  
` iam.serviceAccounts.list `  
` iam.serviceAccounts.setIamPolicy `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
` iam.serviceAccounts.update `  
  
VM Migration API  |  追加  |  ` vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
VM Migration API  |  カスタムの役割でサポート  |  ` vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
  
##  2019-09-20 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Key Management Service  |  一般提供開始  |

役割 ` roles/cloudkms.importer ` （Cloud KMS インポータ）の一般提供を開始しました。  
  
Cloud Key Management Service  |  一般提供開始  |

役割 ` roles/cloudkms.publicKeyViewer ` （Cloud KMS 暗号鍵の公開鍵閲覧者）の一般提供を開始しました。  
  
Cloud Key Management Service  |  一般提供開始  |

役割 ` roles/cloudkms.signer ` （Cloud KMS 暗号鍵の署名者）の一般提供を開始しました。  
  
Cloud Key Management Service  |  一般提供開始  |

役割 ` roles/cloudkms.signerVerifier ` （Cloud KMS 暗号鍵の署名者 / 検証者）の一般提供を開始しました。  
  
Cloud Key Management Service  |  追加  |  ` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  カスタムの役割でサポート  |  ` cloudkms.importJobs.create
`  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  一般提供開始  |  `
cloudkms.cryptoKeyVersions.useToSign `  
` cloudkms.cryptoKeyVersions.viewPublicKey `  
` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
  
##  2019-09-13 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Firebase Remote Config  |  一般提供開始  |

役割 ` roles/cloudconfig.admin ` （Firebase Remote Config 管理者）の一般提供を開始しました。  
  
Firebase Remote Config  |  一般提供開始  |

役割 ` roles/cloudconfig.viewer ` （Firebase Remote Config 閲覧者）の一般提供を開始しました。  
  
Firebase  |  一般提供開始  |

役割 ` roles/firebase.admin ` （Firebase 管理者）の一般提供を開始しました。  
  
Firebase  |  一般提供開始  |

役割 ` roles/firebase.analyticsAdmin ` （Firebase 向け Google
アナリティクス管理者）の一般提供を開始しました。  
  
Firebase  |  一般提供開始  |

役割 ` roles/firebase.analyticsViewer ` （Firebase 向け Google
アナリティクス閲覧者）の一般提供を開始しました。  
  
Firebase  |  一般提供開始  |

役割 ` roles/firebase.developAdmin ` （Firebase Develop 管理者）の一般提供を開始しました。  
  
Firebase  |  一般提供開始  |

役割 ` roles/firebase.developViewer ` （Firebase Develop 閲覧者）の一般提供を開始しました。  
  
Firebase  |  一般提供開始  |

役割 ` roles/firebase.growthAdmin ` （Firebase Grow 管理者）の一般提供を開始しました。  
  
Firebase  |  一般提供開始  |

役割 ` roles/firebase.growthViewer ` （Firebase Grow 閲覧者）の一般提供を開始しました。  
  
Firebase  |  一般提供開始  |

役割 ` roles/firebase.qualityAdmin ` （Firebase Quality 管理者）の一般提供を開始しました。  
  
Firebase  |  一般提供開始  |

役割 ` roles/firebase.qualityViewer ` （Firebase Quality 閲覧者）の一般提供を開始しました。  
  
Firebase  |  一般提供開始  |

役割 ` roles/firebase.viewer ` （Firebase 閲覧者）の一般提供を開始しました。  
  
Firebase 認証  |  一般提供開始  |

役割 ` roles/firebaseauth.admin ` （Firebase Authentication 管理者）の一般提供を開始しました。  
  
Firebase 認証  |  一般提供開始  |

役割 ` roles/firebaseauth.viewer ` （Firebase Authentication 閲覧者）の一般提供を開始しました。  
  
Firebase Crashlytics  |  一般提供開始  |

役割 ` roles/firebasecrashlytics.admin ` （Firebase Crashlytics 管理者）の一般提供を開始しました。  
  
Firebase Crashlytics  |  一般提供開始  |

役割 ` roles/firebasecrashlytics.viewer ` （Firebase Crashlytics
閲覧者）の一般提供を開始しました。  
  
Firebase Realtime Database  |  一般提供開始  |

役割 ` roles/firebasedatabase.admin ` （Firebase Realtime Database
管理者）の一般提供を開始しました。  
  
Firebase Realtime Database  |  一般提供開始  |

役割 ` roles/firebasedatabase.viewer ` （Firebase Realtime Database
閲覧者）の一般提供を開始しました。  
  
Firebase Dynamic Links  |  一般提供開始  |

役割 ` roles/firebasedynamiclinks.admin ` （Firebase Dynamic Links
管理者）の一般提供を開始しました。  
  
Firebase Dynamic Links  |  一般提供開始  |

役割 ` roles/firebasedynamiclinks.viewer ` （Firebase Dynamic Links
閲覧者）の一般提供を開始しました。  
  
Firebase Hosting  |  一般提供開始  |

役割 ` roles/firebasehosting.admin ` （Firebase Hosting 管理者）の一般提供を開始しました。  
  
Firebase Hosting  |  一般提供開始  |

役割 ` roles/firebasehosting.viewer ` （Firebase Hosting 閲覧者）の一般提供を開始しました。  
  
Firebase Cloud Messaging  |  一般提供開始  |

役割 ` roles/firebasenotifications.admin ` （Firebase Cloud Messaging
管理者）の一般提供を開始しました。  
  
Firebase Cloud Messaging  |  一般提供開始  |

役割 ` roles/firebasenotifications.viewer ` （Firebase Cloud Messaging
閲覧者）の一般提供を開始しました。  
  
Firebase Performance Monitoring  |  一般提供開始  |

役割 ` roles/firebaseperformance.admin ` （Firebase Performance Reporting
管理者）の一般提供を開始しました。  
  
Firebase Performance Monitoring  |  一般提供開始  |

役割 ` roles/firebaseperformance.viewer ` （Firebase Performance Reporting
閲覧者）の一般提供を開始しました。  
  
Firebase Predictions  |  一般提供開始  |

役割 ` roles/firebasepredictions.admin ` （Firebase Predictions 管理者）の一般提供を開始しました。  
  
Firebase Predictions  |  一般提供開始  |

役割 ` roles/firebasepredictions.viewer ` （Firebase Predictions
閲覧者）の一般提供を開始しました。  
  
Firebase Remote Config  |  一般提供開始  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Cloud DNS  |  一般提供開始  |  ` dns.networks.bindPrivateDNSPolicy `  
` dns.policies.create `  
` dns.policies.delete `  
` dns.policies.get `  
` dns.policies.getIamPolicy `  
` dns.policies.list `  
` dns.policies.setIamPolicy `  
` dns.policies.update `  
  
Firebase  |  一般提供開始  |  ` firebase.billingPlans.get `  
` firebase.billingPlans.update `  
` firebase.clients.create `  
` firebase.clients.delete `  
` firebase.clients.get `  
` firebase.links.create `  
` firebase.links.delete `  
` firebase.links.list `  
` firebase.links.update `  
` firebase.projects.delete `  
` firebase.projects.get `  
` firebase.projects.update `  
  
Firebase 認証  |  一般提供開始  |  ` firebaseauth.configs.create `  
` firebaseauth.configs.get `  
` firebaseauth.configs.getHashConfig `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Crashlytics  |  一般提供開始  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase Realtime Database  |  一般提供開始  |  ` firebasedatabase.instances.create
`  
` firebasedatabase.instances.get `  
` firebasedatabase.instances.list `  
` firebasedatabase.instances.update `  
  
Firebase Dynamic Links  |  一般提供開始  |  ` firebasedynamiclinks.destinations.list
`  
` firebasedynamiclinks.destinations.update `  
` firebasedynamiclinks.domains.create `  
` firebasedynamiclinks.domains.delete `  
` firebasedynamiclinks.domains.get `  
` firebasedynamiclinks.domains.list `  
` firebasedynamiclinks.domains.update `  
` firebasedynamiclinks.links.create `  
` firebasedynamiclinks.links.get `  
` firebasedynamiclinks.links.list `  
` firebasedynamiclinks.links.update `  
` firebasedynamiclinks.stats.get `  
  
Firebase Hosting  |  一般提供開始  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase Cloud Messaging  |  一般提供開始  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Performance Monitoring  |  一般提供開始  |  `
firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Predictions  |  一般提供開始  |  ` firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
NetApp Cloud Volumes Service  |  追加  |  `
netappcloudvolumes.activeDirectories.create `  
` netappcloudvolumes.activeDirectories.delete `  
` netappcloudvolumes.activeDirectories.get `  
` netappcloudvolumes.activeDirectories.list `  
` netappcloudvolumes.activeDirectories.update `  
` netappcloudvolumes.ipRanges.list `  
` netappcloudvolumes.regions.list `  
` netappcloudvolumes.serviceLevels.list `  
` netappcloudvolumes.snapshots.create `  
` netappcloudvolumes.snapshots.delete `  
` netappcloudvolumes.snapshots.get `  
` netappcloudvolumes.snapshots.list `  
` netappcloudvolumes.snapshots.update `  
` netappcloudvolumes.volumes.create `  
` netappcloudvolumes.volumes.delete `  
` netappcloudvolumes.volumes.get `  
` netappcloudvolumes.volumes.list `  
` netappcloudvolumes.volumes.update `  
  
イベント脅威検出  |  カスタムの役割でサポート  |  ` threatdetection.detectorSettings.clear `  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  2019-09-06 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/owner ` （オーナー）に追加されました。

` dataprocessing.iamaccesshistory.exportData `  
  
サーバーレス VPC アクセス  |  一般提供開始  |

役割 ` roles/vpaccess.user ` （サーバーレス VPC アクセス ユーザー）の一般提供を開始しました。  
  
サーバーレス VPC アクセス  |  一般提供開始  |

役割 ` roles/vpaccess.viewer ` （サーバーレス VPC アクセス閲覧者）の一般提供を開始しました。  
  
サーバーレス VPC アクセス  |  一般提供開始  |

役割 ` roles/vpcaccess.admin ` （サーバーレス VPC アクセス管理者）の一般提供を開始しました。  
  
Compute Engine  |  追加  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  一般提供開始  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
サーバーレス VPC アクセス  |  一般提供開始  |  ` vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  2019-08-30 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Firebase Test Lab  |  役割の更新  |

次の権限が役割 ` roles/cloudtestservice.testAdmin ` （Firebase Test Lab 管理者）に追加されました。

` firebase.clients.get `  
` firebase.projects.get `  
  
Firebase Test Lab  |  役割の更新  |

次の権限が役割 ` roles/cloudtestservice.testViewer ` （Firebase Test Lab 閲覧者）に追加されました。

` firebase.clients.get `  
` firebase.projects.get `  
  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.orgSecurityPolicyAdmin ` （コンピューティング組織セキュリティ
ポリシー管理者）に追加されました。

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.orgSecurityPolicyUser ` （コンピューティング組織セキュリティ ポリシー
ユーザー）に追加されました。

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.orgSecurityResourceAdmin `
（コンピューティング組織リソース管理者）に追加されました。

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
  
##  2019-08-23 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
翻訳  |  一般提供開始  |

役割 ` roles/cloudtranslate.admin ` （Cloud Translation API 管理者）の一般提供を開始しました。  
  
翻訳  |  一般提供開始  |

役割 ` roles/cloudtranslate.editor ` （Cloud Translation API 編集者）の一般提供を開始しました。  
  
翻訳  |  一般提供開始  |

役割 ` roles/cloudtranslate.user ` （Cloud Translation API ユーザー）の一般提供を開始しました。  
  
翻訳  |  一般提供開始  |

役割 ` roles/cloudtranslate.viewer ` （Cloud Translation API 閲覧者）の一般提供を開始しました。  
  
Cloud Healthcare API  |  役割の更新  |

次の権限が役割 ` roles/healthcare.dicomEditor ` （Healthcare DICOM 編集者）に追加されました。

` healthcare.dicomStores.dicomWebDelete `  
  
翻訳  |  一般提供開始  |  ` cloudtranslate.generalModels.batchPredict `  
` cloudtranslate.generalModels.get `  
` cloudtranslate.generalModels.predict `  
` cloudtranslate.glossaries.batchPredict `  
` cloudtranslate.glossaries.create `  
` cloudtranslate.glossaries.delete `  
` cloudtranslate.glossaries.get `  
` cloudtranslate.glossaries.list `  
` cloudtranslate.glossaries.predict `  
` cloudtranslate.languageDetectionModels.predict `  
` cloudtranslate.locations.get `  
` cloudtranslate.locations.list `  
` cloudtranslate.operations.cancel `  
` cloudtranslate.operations.delete `  
` cloudtranslate.operations.get `  
` cloudtranslate.operations.list `  
` cloudtranslate.operations.wait `  
  
  
##  2019-08-16 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
翻訳  |  カスタムの役割でサポート  |  ` cloudtranslate.locations.get `  
` cloudtranslate.locations.list `  
  
Compute Engine  |  一般提供開始  |  ` compute.networks.updatePeering `  
  
データカタログ  |  追加  |  ` datacatalog.entries.create `  
` datacatalog.entries.delete `  
` datacatalog.entries.get `  
` datacatalog.entries.getIamPolicy `  
` datacatalog.entries.setIamPolicy `  
` datacatalog.entries.update `  
` datacatalog.entryGroups.create `  
` datacatalog.entryGroups.delete `  
` datacatalog.entryGroups.get `  
` datacatalog.entryGroups.getIamPolicy `  
` datacatalog.entryGroups.setIamPolicy `  
  
データカタログ  |  カスタムの役割でサポート  |  ` datacatalog.entries.create `  
` datacatalog.entries.delete `  
` datacatalog.entries.get `  
` datacatalog.entries.getIamPolicy `  
` datacatalog.entries.setIamPolicy `  
` datacatalog.entries.update `  
` datacatalog.entryGroups.create `  
` datacatalog.entryGroups.delete `  
` datacatalog.entryGroups.get `  
` datacatalog.entryGroups.getIamPolicy `  
` datacatalog.entryGroups.setIamPolicy `  
  
  
##  2019-08-09 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.orgSecurityPolicyAdmin ` （コンピューティング組織セキュリティ
ポリシー管理者）に追加されました。

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.orgSecurityPolicyUser ` （コンピューティング組織セキュリティ ポリシー
ユーザー）に追加されました。

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.orgSecurityResourceAdmin `
（コンピューティング組織リソース管理者）に追加されました。

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
クラウド ストレージ  |  一般提供開始  |

役割 ` roles/storage.hmacKeyAdmin ` （Storage HMAC キー管理者）の一般提供を開始しました。  
  
クラウド ストレージ  |  追加  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
クラウド ストレージ  |  カスタムの役割でサポート  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
クラウド ストレージ  |  一般提供開始  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
  
##  2019-06-28 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/viewer ` （閲覧者）に追加されました。

` pubsub.snapshots.seek `  
  
Firebase Crashlytics  |  追加  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase Crashlytics  |  カスタムの役割でサポート  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Memorystore for Redis  |  追加  |  ` redis.instances.export `  
` redis.instances.import `  
  
Memorystore for Redis  |  カスタムの役割でサポート  |  ` redis.instances.export `  
` redis.instances.import `  
  
  
##  2019-06-21 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine の移行  |  役割の更新  |

次の権限が役割 ` roles/cloudmigration.inframanager ` （Velostrata Manager）に追加されました。

` compute.instances.updateShieldedInstanceConfig `  
  
翻訳  |  役割の更新  |

次の権限が役割 ` roles/cloudtranslate.viewer ` （Cloud Translation API 閲覧者）に追加されました。

` cloudtranslate.operations.wait `  
  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.networkUser ` （Compute ネットワーク ユーザー）に追加されました。

` compute.vpnGateways.use `  
  
Firebase  |  役割の更新  |

次の権限が役割 ` roles/firebase.admin ` （Firebase 管理者）に追加されました。

` cloudmessaging.messages.create `  
  
Firebase  |  役割の更新  |

次の権限が役割 ` roles/firebase.growthAdmin ` （Firebase Grow 管理者）に追加されました。

` cloudmessaging.messages.create `  
  
Resource Manager  |  役割の更新  |

次の権限が役割 ` roles/resourcemanager.projectMover ` （プロジェクト移動）に追加されました。

` resourcemanager.projects.move `  
  
セキュリティ コマンド センター  |  役割の更新  |

次の権限が役割 ` roles/securitycenter.adminEditor ` （セキュリティ センター管理編集者）に追加されました。

` securitycenter.assets.group `  
` securitycenter.assets.list `  
` securitycenter.assets.listAssetPropertyNames `  
  
BigQuery  |  追加  |  ` bigquery.connections.create `  
` bigquery.connections.delete `  
` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.setIamPolicy `  
` bigquery.connections.update `  
` bigquery.connections.use `  
` bigquery.routines.create `  
` bigquery.routines.delete `  
` bigquery.routines.get `  
` bigquery.routines.list `  
` bigquery.routines.update `  
  
BigQuery  |  カスタムの役割でサポート  |  ` bigquery.routines.create `  
` bigquery.routines.delete `  
` bigquery.routines.get `  
` bigquery.routines.list `  
` bigquery.routines.update `  
  
翻訳  |  カスタムの役割でサポート  |  ` cloudtranslate.generalModels.batchPredict `  
` cloudtranslate.generalModels.get `  
` cloudtranslate.generalModels.predict `  
` cloudtranslate.glossaries.batchPredict `  
` cloudtranslate.glossaries.create `  
` cloudtranslate.glossaries.delete `  
` cloudtranslate.glossaries.get `  
` cloudtranslate.glossaries.list `  
` cloudtranslate.glossaries.predict `  
` cloudtranslate.languageDetectionModels.predict `  
` cloudtranslate.operations.cancel `  
` cloudtranslate.operations.delete `  
` cloudtranslate.operations.get `  
` cloudtranslate.operations.list `  
` cloudtranslate.operations.wait `  
  
Cloud Composer  |  追加  |  ` composer.imageversions.list `  
  
Cloud Composer  |  カスタムの役割でサポート  |  ` composer.imageversions.list `  
  
Cloud Composer  |  一般提供開始  |  ` composer.imageversions.list `  
  
Compute Engine  |  追加  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  一般提供開始  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
  
##  2019-06-14 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Identity and Access Management  |  一般提供開始  |

役割 ` roles/iam.workloadIdentityUser ` （Workload Identity ユーザー）の一般提供を開始しました。  
  
Cloud Functions  |  追加  |  ` cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Cloud Functions  |  カスタムの役割でサポート  |  ` cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Compute Engine  |  一般提供開始  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  2019-05-31 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
データカタログ  |  役割の更新  |

次の権限が役割 ` roles/datacatalog.admin ` （Data Catalog 管理者）に追加されました。

` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
` pubsub.topics.updateTag `  
  
Compute Engine の移行  |  追加  |  ` cloudmigration.velostrataendpoints.connect `  
  
Cloud Identity and Access Management  |  カスタムの役割で使用可能  |  `
iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
  
##  2019-05-24 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/viewer ` （閲覧者）に追加されました。

` managedidentities.domains.validateTrust `  
  
Recommendations AI  |  カスタムの役割でサポート  |  ` automlrecommendations.apiKeys.create
`  
` automlrecommendations.apiKeys.delete `  
` automlrecommendations.apiKeys.list `  
` automlrecommendations.catalogItems.create `  
` automlrecommendations.catalogItems.delete `  
` automlrecommendations.catalogItems.get `  
` automlrecommendations.catalogItems.list `  
` automlrecommendations.catalogItems.update `  
` automlrecommendations.events.list `  
` automlrecommendations.events.purge `  
  
BigQuery  |  追加  |  ` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
BigQuery  |  カスタムの役割でサポート  |  ` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
データカタログ  |  追加  |  ` datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
データカタログ  |  カスタムの役割でサポート  |  ` datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
Filestore  |  追加  |  ` file.snapshots.update `  
  
Filestore  |  カスタムの役割でサポート  |  ` file.snapshots.update `  
  
Pub/Sub  |  追加  |  ` pubsub.topics.updateTag `  
  
Pub/Sub  |  カスタムの役割でサポート  |  ` pubsub.topics.updateTag `  
  
  
##  2019-05-17 現在の IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Dialogflow  |  追加  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  カスタムの役割でサポート  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  一般提供開始  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
  
##  2019-05-10 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Identity and Access Management  |  一般提供開始  |

役割 ` roles/iam.securityAdmin ` （セキュリティ管理者）の一般提供を開始しました。  
  
Cloud IoT  |  追加  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  カスタムの役割でサポート  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  一般提供開始  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.healthChecks.create `  
` compute.healthChecks.delete `  
` compute.healthChecks.get `  
` compute.healthChecks.list `  
` compute.healthChecks.update `  
` compute.healthChecks.use `  
` compute.healthChecks.useReadOnly `  
` compute.instanceGroups.use `  
  
Cloud Healthcare API  |  追加  |  ` healthcare.fhirResources.purge `  
  
Microsoft Active Directory のマネージド サービス  |  追加  |  `
managedidentities.domains.attachTrust `  
` managedidentities.domains.create `  
` managedidentities.domains.delete `  
` managedidentities.domains.detachTrust `  
` managedidentities.domains.get `  
` managedidentities.domains.getIamPolicy `  
` managedidentities.domains.list `  
` managedidentities.domains.reconfigureTrust `  
` managedidentities.domains.resetpassword `  
` managedidentities.domains.setIamPolicy `  
` managedidentities.domains.update `  
` managedidentities.domains.validateTrust `  
` managedidentities.locations.get `  
` managedidentities.locations.list `  
` managedidentities.operations.cancel `  
` managedidentities.operations.delete `  
` managedidentities.operations.get `  
` managedidentities.operations.list `  
  
Microsoft Active Directory のマネージド サービス  |  カスタムの役割でサポート  |  `
managedidentities.domains.attachTrust `  
` managedidentities.domains.create `  
` managedidentities.domains.delete `  
` managedidentities.domains.detachTrust `  
` managedidentities.domains.get `  
` managedidentities.domains.getIamPolicy `  
` managedidentities.domains.list `  
` managedidentities.domains.reconfigureTrust `  
` managedidentities.domains.resetpassword `  
` managedidentities.domains.setIamPolicy `  
` managedidentities.domains.update `  
` managedidentities.domains.validateTrust `  
` managedidentities.locations.get `  
` managedidentities.locations.list `  
` managedidentities.operations.cancel `  
` managedidentities.operations.delete `  
` managedidentities.operations.get `  
` managedidentities.operations.list `  
  
  
##  2019-05-03 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.admin ` （セキュリティ センター管理者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.adminEditor ` （セキュリティ センター管理者編集者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.adminViewer ` （セキュリティ センター管理者閲覧者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.assetsDiscoveryRunner ` （セキュリティ センターのアセット
ディスカバリ実行者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.assetSecurityMarksWriter ` （セキュリティ センターのアセット セキュリティ
マーク編集者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.assetsViewer ` （セキュリティ センターのアセット閲覧者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.findingSecurityMarksWriter ` （セキュリティ センターの検出セキュリティ
マーク編集者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.findingsEditor ` （セキュリティ センターの検出編集者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.findingsStateSetter ` （セキュリティ
センターの検出状態設定者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.findingsViewer ` （セキュリティ センターの検出閲覧者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.sourcesAdmin ` （セキュリティ センターのソース管理者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.sourcesEditor ` （セキュリティ センターのソース編集者）の一般提供を開始しました。  
  
セキュリティ コマンド センター  |  一般提供開始  |

役割 ` roles/securitycenter.sourcesViewer ` （セキュリティ センターのソース閲覧者）の一般提供を開始しました。  
  
Recommendations AI  |  追加  |  ` automlrecommendations.apiKeys.create `  
` automlrecommendations.apiKeys.delete `  
` automlrecommendations.apiKeys.get `  
` automlrecommendations.apiKeys.list `  
` automlrecommendations.catalogItems.create `  
` automlrecommendations.catalogItems.delete `  
` automlrecommendations.catalogItems.get `  
` automlrecommendations.catalogItems.list `  
` automlrecommendations.catalogItems.update `  
` automlrecommendations.catalogs.get `  
` automlrecommendations.catalogs.getStats `  
` automlrecommendations.catalogs.list `  
` automlrecommendations.eventStores.get `  
` automlrecommendations.eventStores.getStats `  
` automlrecommendations.eventStores.list `  
` automlrecommendations.events.create `  
` automlrecommendations.events.delete `  
` automlrecommendations.events.get `  
` automlrecommendations.events.list `  
` automlrecommendations.events.purge `  
` automlrecommendations.events.update `  
` automlrecommendations.placements.get `  
` automlrecommendations.placements.getStats `  
` automlrecommendations.placements.list `  
` automlrecommendations.recommendations.get `  
` automlrecommendations.recommendations.list `  
  
BigQuery  |  追加  |  ` bigquery.models.create `  
` bigquery.models.delete `  
` bigquery.models.getData `  
` bigquery.models.getMetadata `  
` bigquery.models.list `  
` bigquery.models.updateData `  
` bigquery.models.updateMetadata `  
  
Firebase Cloud Messaging  |  追加  |  ` cloudmessaging.messages.create `  
  
Firebase Cloud Messaging  |  カスタムの役割でサポート  |  ` cloudmessaging.messages.create
`  
  
Firebase Cloud Messaging  |  一般提供開始  |  ` cloudmessaging.messages.create `  
  
セキュリティ コマンド センター  |  一般提供開始  |  ` securitycenter.assets.group `  
` securitycenter.assets.list `  
` securitycenter.assets.listAssetPropertyNames `  
` securitycenter.assets.runDiscovery `  
` securitycenter.assetsecuritymarks.update `  
` securitycenter.findings.group `  
` securitycenter.findings.list `  
` securitycenter.findings.listFindingPropertyNames `  
` securitycenter.findings.setState `  
` securitycenter.findings.update `  
` securitycenter.findingsecuritymarks.update `  
` securitycenter.organizationsettings.get `  
` securitycenter.organizationsettings.update `  
` securitycenter.sources.get `  
` securitycenter.sources.getIamPolicy `  
` securitycenter.sources.list `  
` securitycenter.sources.setIamPolicy `  
` securitycenter.sources.update `  
  
  
##  2019-04-19 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
基本の役割  |  役割の更新  |

役割 ` roles/editor ` （編集者）から次の権限が削除されました。

` firebasedynamiclinks.domains.delete `  
  
セキュリティ コマンド センター  |  役割の更新  |

次の権限が役割 ` roles/securitycenter.admin ` （セキュリティ センター管理者）に追加されました。

` securitycenter.findings.setState `  
  
セキュリティ コマンド センター  |  役割の更新  |

次の権限が役割 ` roles/securitycenter.adminEditor ` （セキュリティ センター管理編集者）に追加されました。

` securitycenter.findings.setState `  
  
セキュリティ コマンド センター  |  役割の更新  |

次の権限が役割 ` roles/securitycenter.findingsEditor ` （セキュリティ センターの検出編集者）に追加されました。

` securitycenter.findings.setState `  
  
アクセス承認  |  追加  |  ` accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
アクセス承認  |  カスタムの役割でサポート  |  ` accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
Cloud Bigtable  |  追加  |  ` bigtable.locations.list `  
  
Cloud Bigtable  |  カスタムの役割でサポート  |  ` bigtable.locations.list `  
  
Cloud Bigtable  |  一般提供開始  |  ` bigtable.locations.list `  
  
Cloud Scheduler  |  追加  |  ` cloudscheduler.locations.get `  
` cloudscheduler.locations.list `  
  
Compute Engine  |  追加  |  `
compute.networkEndpointGroups.attachNetworkEndpoints `  
` compute.networkEndpointGroups.create `  
` compute.networkEndpointGroups.delete `  
` compute.networkEndpointGroups.detachNetworkEndpoints `  
` compute.networkEndpointGroups.get `  
` compute.networkEndpointGroups.getIamPolicy `  
` compute.networkEndpointGroups.list `  
` compute.networkEndpointGroups.setIamPolicy `  
` compute.networkEndpointGroups.use `  
` compute.reservations.create `  
` compute.reservations.delete `  
` compute.reservations.get `  
` compute.reservations.list `  
` compute.reservations.resize `  
  
Compute Engine  |  カスタムの役割でサポート  |  `
compute.networkEndpointGroups.attachNetworkEndpoints `  
` compute.networkEndpointGroups.create `  
` compute.networkEndpointGroups.delete `  
` compute.networkEndpointGroups.detachNetworkEndpoints `  
` compute.networkEndpointGroups.get `  
` compute.networkEndpointGroups.getIamPolicy `  
` compute.networkEndpointGroups.list `  
` compute.networkEndpointGroups.setIamPolicy `  
` compute.networkEndpointGroups.use `  
` compute.reservations.create `  
` compute.reservations.delete `  
` compute.reservations.get `  
` compute.reservations.list `  
` compute.reservations.resize `  
  
Compute Engine  |  一般提供開始  |  `
compute.networkEndpointGroups.attachNetworkEndpoints `  
` compute.networkEndpointGroups.create `  
` compute.networkEndpointGroups.delete `  
` compute.networkEndpointGroups.detachNetworkEndpoints `  
` compute.networkEndpointGroups.get `  
` compute.networkEndpointGroups.getIamPolicy `  
` compute.networkEndpointGroups.list `  
` compute.networkEndpointGroups.setIamPolicy `  
` compute.networkEndpointGroups.use `  
  
Remote Build Execution  |  追加  |  ` remotebuildexecution.actions.create `  
` remotebuildexecution.actions.get `  
` remotebuildexecution.actions.set `  
` remotebuildexecution.actions.update `  
` remotebuildexecution.blobs.create `  
` remotebuildexecution.blobs.get `  
` remotebuildexecution.botsessions.create `  
` remotebuildexecution.botsessions.update `  
` remotebuildexecution.instances.create `  
` remotebuildexecution.instances.delete `  
` remotebuildexecution.instances.get `  
` remotebuildexecution.instances.list `  
` remotebuildexecution.logstreams.create `  
` remotebuildexecution.logstreams.get `  
` remotebuildexecution.logstreams.update `  
` remotebuildexecution.workerpools.create `  
` remotebuildexecution.workerpools.delete `  
` remotebuildexecution.workerpools.get `  
` remotebuildexecution.workerpools.list `  
` remotebuildexecution.workerpools.update `  
  
Remote Build Execution  |  カスタムの役割でサポート  |  `
remotebuildexecution.actions.create `  
` remotebuildexecution.actions.get `  
` remotebuildexecution.actions.set `  
` remotebuildexecution.actions.update `  
` remotebuildexecution.blobs.create `  
` remotebuildexecution.blobs.get `  
` remotebuildexecution.botsessions.create `  
` remotebuildexecution.botsessions.update `  
` remotebuildexecution.instances.create `  
` remotebuildexecution.instances.delete `  
` remotebuildexecution.instances.get `  
` remotebuildexecution.instances.list `  
` remotebuildexecution.logstreams.create `  
` remotebuildexecution.logstreams.get `  
` remotebuildexecution.logstreams.update `  
` remotebuildexecution.workerpools.create `  
` remotebuildexecution.workerpools.delete `  
` remotebuildexecution.workerpools.get `  
` remotebuildexecution.workerpools.list `  
` remotebuildexecution.workerpools.update `  
  
サーバーレス VPC アクセス  |  追加  |  ` vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  2019-03-29 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.networkUser ` （Compute ネットワーク ユーザー）に追加されました。

` servicenetworking.services.get `  
  
Cloud Monitoring  |  役割の更新  |

次の権限が役割 ` roles/monitoring.admin ` （モニタリング管理者）に追加されました。

` serviceusage.services.enable `  
  
Cloud Monitoring  |  役割の更新  |

次の権限が役割 ` roles/monitoring.editor ` （モニタリング編集者）に追加されました。

` serviceusage.services.enable `  
  
Google Cloud オペレーションスイート  |  役割の更新  |

次の権限が役割 ` roles/stackdriver.accounts.editor ` （Stackdriver アカウント編集者）に追加されました。

` serviceusage.services.enable `  
  
Cloud SQL  |  追加  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  カスタムの役割でサポート  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  一般提供開始  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
翻訳  |  追加  |  ` cloudtranslate.generalModels.batchPredict `  
` cloudtranslate.generalModels.get `  
` cloudtranslate.generalModels.getIamPolicy `  
` cloudtranslate.generalModels.predict `  
` cloudtranslate.generalModels.setIamPolicy `  
` cloudtranslate.glossaries.batchPredict `  
` cloudtranslate.glossaries.create `  
` cloudtranslate.glossaries.delete `  
` cloudtranslate.glossaries.get `  
` cloudtranslate.glossaries.getIamPolicy `  
` cloudtranslate.glossaries.list `  
` cloudtranslate.glossaries.predict `  
` cloudtranslate.glossaries.setIamPolicy `  
` cloudtranslate.languageDetectionModels.getIamPolicy `  
` cloudtranslate.languageDetectionModels.predict `  
` cloudtranslate.languageDetectionModels.setIamPolicy `  
` cloudtranslate.locations.get `  
` cloudtranslate.locations.getIamPolicy `  
` cloudtranslate.locations.list `  
` cloudtranslate.locations.setIamPolicy `  
` cloudtranslate.operations.cancel `  
` cloudtranslate.operations.delete `  
` cloudtranslate.operations.get `  
` cloudtranslate.operations.getIamPolicy `  
` cloudtranslate.operations.list `  
` cloudtranslate.operations.setIamPolicy `  
` cloudtranslate.operations.wait `  
  
Cloud DNS  |  追加  |  ` dns.networks.targetWithPeeringZone `  
  
Cloud DNS  |  カスタムの役割でサポート  |  ` dns.networks.targetWithPeeringZone `  
  
イベント脅威検出  |  追加  |  ` threatdetection.detectorSettings.clear `  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  2019-03-22 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Talent Solution  |  一般提供開始  |

役割 ` roles/cloudjobdiscovery.admin ` （管理者）の一般提供を開始しました。  
  
Talent Solution  |  一般提供開始  |

役割 ` roles/cloudjobdiscovery.jobsEditor ` （ジョブ編集者）の一般提供を開始しました。  
  
Talent Solution  |  一般提供開始  |

役割 ` roles/cloudjobdiscovery.jobsViewer ` （ジョブ閲覧者）の一般提供を開始しました。  
  
Talent Solution  |  一般提供開始  |

役割 ` roles/cloudjobdiscovery.profilesEditor ` （プロファイル編集者）の一般提供を開始しました。  
  
Talent Solution  |  一般提供開始  |

役割 ` roles/cloudjobdiscovery.profilesViewer ` （プロファイル閲覧者）の一般提供を開始しました。  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/editor ` （編集者）に追加されました。

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Filestore  |  役割の更新  |

次の権限が役割 ` roles/file.editor ` （Cloud Filestore 編集者）に追加されました。

` file.instances.restore `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/owner ` （オーナー）に追加されました。

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Talent Solution  |  一般提供開始  |  ` cloudjobdiscovery.companies.create `  
` cloudjobdiscovery.companies.delete `  
` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.companies.update `  
` cloudjobdiscovery.events.create `  
` cloudjobdiscovery.jobs.create `  
` cloudjobdiscovery.jobs.delete `  
` cloudjobdiscovery.jobs.get `  
` cloudjobdiscovery.jobs.search `  
` cloudjobdiscovery.jobs.update `  
` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
` cloudjobdiscovery.tools.access `  
  
Compute Engine  |  追加  |  ` compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  カスタムの役割でサポート  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  一般提供開始  |  ` compute.instances.getShieldedInstanceIdentity
`  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Filestore  |  追加  |  ` file.instances.restore `  
  
Firebase 認証  |  追加  |  ` firebaseauth.configs.getHashConfig `  
  
Firebase 認証  |  カスタムの役割でサポート  |  ` firebaseauth.configs.getHashConfig `  
  
Cloud Healthcare API  |  追加  |  ` healthcare.datasets.create `  
` healthcare.datasets.deidentify `  
` healthcare.datasets.delete `  
` healthcare.datasets.get `  
` healthcare.datasets.getIamPolicy `  
` healthcare.datasets.list `  
` healthcare.datasets.setIamPolicy `  
` healthcare.datasets.update `  
` healthcare.dicomStores.create `  
` healthcare.dicomStores.delete `  
` healthcare.dicomStores.dicomWebDelete `  
` healthcare.dicomStores.dicomWebRead `  
` healthcare.dicomStores.dicomWebWrite `  
` healthcare.dicomStores.export `  
` healthcare.dicomStores.get `  
` healthcare.dicomStores.getIamPolicy `  
` healthcare.dicomStores.import `  
` healthcare.dicomStores.list `  
` healthcare.dicomStores.setIamPolicy `  
` healthcare.dicomStores.update `  
` healthcare.fhirResources.create `  
` healthcare.fhirResources.delete `  
` healthcare.fhirResources.get `  
` healthcare.fhirResources.patch `  
` healthcare.fhirResources.update `  
` healthcare.fhirSecurityLabels.getIamPolicy `  
` healthcare.fhirSecurityLabels.setIamPolicy `  
` healthcare.fhirStores.create `  
` healthcare.fhirStores.delete `  
` healthcare.fhirStores.export `  
` healthcare.fhirStores.get `  
` healthcare.fhirStores.getIamPolicy `  
` healthcare.fhirStores.import `  
` healthcare.fhirStores.list `  
` healthcare.fhirStores.searchResources `  
` healthcare.fhirStores.setIamPolicy `  
` healthcare.fhirStores.update `  
` healthcare.hl7V2Messages.create `  
` healthcare.hl7V2Messages.delete `  
` healthcare.hl7V2Messages.get `  
` healthcare.hl7V2Messages.ingest `  
` healthcare.hl7V2Messages.list `  
` healthcare.hl7V2Messages.update `  
` healthcare.hl7V2Stores.create `  
` healthcare.hl7V2Stores.delete `  
` healthcare.hl7V2Stores.get `  
` healthcare.hl7V2Stores.getIamPolicy `  
` healthcare.hl7V2Stores.list `  
` healthcare.hl7V2Stores.setIamPolicy `  
` healthcare.hl7V2Stores.update `  
` healthcare.operations.cancel `  
` healthcare.operations.get `  
` healthcare.operations.list `  
  
  
##  2019-03-15 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Talent Solution  |  役割の更新  |

次の権限が役割 ` roles/cloudjobdiscovery.profilesEditor ` （プロファイル編集者）に追加されました。

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Talent Solution  |  役割の更新  |

次の権限が役割 ` roles/cloudjobdiscovery.profilesEditor ` （プロファイル編集者）から削除されました。

` cloudjobdiscovery.companies.create `  
` cloudjobdiscovery.companies.delete `  
` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.companies.update `  
  
Talent Solution  |  役割の更新  |

次の権限が役割 ` roles/cloudjobdiscovery.profilesViewer ` （プロファイル閲覧者）に追加されました。

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  役割の更新  |

次の権限が役割 ` roles/cloudjobdiscovery.profilesViewer ` （プロファイル閲覧者）から削除されました。

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/editor ` （編集者）に追加されました。

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/owner ` （オーナー）に追加されました。

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Storage Transfer Service  |  一般提供開始  |

役割 ` roles/storagetransfer.admin ` （Storage Transfer 管理者）の一般提供を開始しました。  
  
Storage Transfer Service  |  一般提供開始  |

役割 ` roles/storagetransfer.user ` （Storage Transfer ユーザー）の一般提供を開始しました。  
  
Storage Transfer Service  |  一般提供開始  |

役割 ` roles/storagetransfer.viewer ` （Storage Transfer 閲覧者）の一般提供を開始しました。  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/viewer ` （閲覧者）に追加されました。

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  追加  |  ` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Cloud DNS  |  一般提供開始  |  ` dns.networks.bindPrivateDNSZone `  
  
Cloud Run  |  追加  |  ` run.configurations.get `  
` run.configurations.list `  
` run.locations.list `  
` run.revisions.delete `  
` run.revisions.get `  
` run.revisions.list `  
` run.routes.get `  
` run.routes.invoke `  
` run.routes.list `  
` run.services.create `  
` run.services.delete `  
` run.services.get `  
` run.services.getIamPolicy `  
` run.services.list `  
` run.services.setIamPolicy `  
` run.services.update `  
  
Cloud Run  |  カスタムの役割でサポートされない  |  ` run.routes.invoke `  
  
Cloud Run  |  カスタムの役割でサポート  |  ` run.configurations.get `  
` run.configurations.list `  
` run.locations.list `  
` run.revisions.delete `  
` run.revisions.get `  
` run.revisions.list `  
` run.routes.get `  
` run.routes.list `  
` run.services.create `  
` run.services.delete `  
` run.services.get `  
` run.services.getIamPolicy `  
` run.services.list `  
` run.services.setIamPolicy `  
` run.services.update `  
  
Storage Transfer Service  |  追加  |  ` storagetransfer.jobs.create `  
` storagetransfer.jobs.delete `  
` storagetransfer.jobs.get `  
` storagetransfer.jobs.list `  
` storagetransfer.jobs.update `  
` storagetransfer.operations.cancel `  
` storagetransfer.operations.get `  
` storagetransfer.operations.list `  
` storagetransfer.operations.pause `  
` storagetransfer.operations.resume `  
` storagetransfer.projects.getServiceAccount `  
  
Storage Transfer Service  |  カスタムの役割でサポート  |  ` storagetransfer.jobs.create `  
` storagetransfer.jobs.delete `  
` storagetransfer.jobs.get `  
` storagetransfer.jobs.list `  
` storagetransfer.jobs.update `  
` storagetransfer.operations.cancel `  
` storagetransfer.operations.get `  
` storagetransfer.operations.list `  
` storagetransfer.operations.pause `  
` storagetransfer.operations.resume `  
` storagetransfer.projects.getServiceAccount `  
  
Storage Transfer Service  |  一般提供開始  |  ` storagetransfer.jobs.create `  
` storagetransfer.jobs.delete `  
` storagetransfer.jobs.get `  
` storagetransfer.jobs.list `  
` storagetransfer.jobs.update `  
` storagetransfer.operations.cancel `  
` storagetransfer.operations.get `  
` storagetransfer.operations.list `  
` storagetransfer.operations.pause `  
` storagetransfer.operations.resume `  
` storagetransfer.projects.getServiceAccount `  
  
  
##  2019-03-07 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
BigQuery  |  役割の追加  |

次の権限を持つ役割 ` roles/bigquery.connectionAdmin ` （BigQuery Connection
管理者）が追加されました。

` bigquery.connections.create `  
` bigquery.connections.delete `  
` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.setIamPolicy `  
` bigquery.connections.update `  
` bigquery.connections.use `  
  
BigQuery  |  役割の追加  |

次の権限を持つ役割 ` roles/bigquery.connectionUser ` （BigQuery Connection
ユーザー）が追加されました。

` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.use `  
  
Dialogflow  |  役割の更新  |

次の権限が役割 ` roles/dialogflow.admin ` （Dialogflow API 管理者）に追加されました。

` dialogflow.agents.update `  
  
Dialogflow  |  役割の更新  |

次の権限が役割 ` roles/dialogflow.consoleAgentEditor ` （Dialogflow コンソール
エージェント編集者）に追加されました。

` dialogflow.agents.update `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/editor ` （編集者）に追加されました。

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  役割の更新  |

次の権限が役割 ` roles/file.editor ` （Cloud Filestore 編集者）に追加されました。

` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  役割の更新  |

次の権限が役割 ` roles/file.viewer ` （Cloud Filestore 閲覧者）に追加されました。

` file.snapshots.get `  
` file.snapshots.list `  
  
Cloud Identity and Access Management  |  一般提供開始  |

役割 ` roles/iam.serviceAccountCreator ` （サービス アカウントの作成）の一般提供を開始しました。  
  
Cloud Identity and Access Management  |  役割の更新  |

次の権限が役割 ` roles/iam.securityReviewer ` （セキュリティ審査担当者）に追加されました。

` file.snapshots.list `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/owner ` （オーナー）に追加されました。

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
サービスの使用状況  |  役割の更新  |

次の権限が役割 ` roles/serviceusage.apiKeysAdmin ` （API キー管理者）に追加されました。

` serviceusage.operations.get `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/viewer ` （閲覧者）に追加されました。

` file.snapshots.get `  
` file.snapshots.list `  
  
AI Platform Data Labeling Service  |  追加  |  `
datalabeling.annotateddatasets.delete `  
` datalabeling.annotateddatasets.get `  
` datalabeling.annotateddatasets.label `  
` datalabeling.annotateddatasets.list `  
` datalabeling.annotationspecsets.create `  
` datalabeling.annotationspecsets.delete `  
` datalabeling.annotationspecsets.get `  
` datalabeling.annotationspecsets.list `  
` datalabeling.dataitems.get `  
` datalabeling.dataitems.list `  
` datalabeling.datasets.create `  
` datalabeling.datasets.delete `  
` datalabeling.datasets.export `  
` datalabeling.datasets.get `  
` datalabeling.datasets.import `  
` datalabeling.datasets.list `  
` datalabeling.examples.get `  
` datalabeling.examples.list `  
` datalabeling.instructions.create `  
` datalabeling.instructions.delete `  
` datalabeling.instructions.get `  
` datalabeling.instructions.list `  
` datalabeling.operations.cancel `  
` datalabeling.operations.get `  
` datalabeling.operations.list `  
  
AI Platform Data Labeling Service  |  カスタムの役割でサポート  |  `
datalabeling.annotateddatasets.delete `  
` datalabeling.annotateddatasets.get `  
` datalabeling.annotateddatasets.label `  
` datalabeling.annotateddatasets.list `  
` datalabeling.annotationspecsets.create `  
` datalabeling.annotationspecsets.delete `  
` datalabeling.annotationspecsets.get `  
` datalabeling.annotationspecsets.list `  
` datalabeling.dataitems.get `  
` datalabeling.dataitems.list `  
` datalabeling.datasets.create `  
` datalabeling.datasets.delete `  
` datalabeling.datasets.export `  
` datalabeling.datasets.get `  
` datalabeling.datasets.import `  
` datalabeling.datasets.list `  
` datalabeling.examples.get `  
` datalabeling.examples.list `  
` datalabeling.instructions.create `  
` datalabeling.instructions.delete `  
` datalabeling.instructions.get `  
` datalabeling.instructions.list `  
` datalabeling.operations.cancel `  
` datalabeling.operations.get `  
` datalabeling.operations.list `  
  
Dialogflow  |  追加  |  ` dialogflow.agents.update `  
  
Filestore  |  追加  |  ` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
  
##  2019-03-01 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  役割の更新  |

次の権限が役割 ` roles/compute.instanceAdmin.v1 ` （Compute インスタンス管理者 v1）に追加されました。

` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Dataproc  |  役割の追加  |

次の権限を持つ役割 ` roles/dataproc.admin ` （Dataproc 管理者）が追加されました。

` compute.machineTypes.get `  
` compute.machineTypes.list `  
` compute.networks.get `  
` compute.networks.list `  
` compute.projects.get `  
` compute.regions.get `  
` compute.regions.list `  
` compute.zones.get `  
` compute.zones.list `  
` dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
` dataproc.clusters.create `  
` dataproc.clusters.delete `  
` dataproc.clusters.get `  
` dataproc.clusters.getIamPolicy `  
` dataproc.clusters.list `  
` dataproc.clusters.setIamPolicy `  
` dataproc.clusters.update `  
` dataproc.clusters.use `  
` dataproc.jobs.cancel `  
` dataproc.jobs.create `  
` dataproc.jobs.delete `  
` dataproc.jobs.get `  
` dataproc.jobs.getIamPolicy `  
` dataproc.jobs.list `  
` dataproc.jobs.setIamPolicy `  
` dataproc.jobs.update `  
` dataproc.operations.cancel `  
` dataproc.operations.delete `  
` dataproc.operations.get `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.list `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.create `  
` dataproc.workflowTemplates.delete `  
` dataproc.workflowTemplates.get `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.instantiate `  
` dataproc.workflowTemplates.instantiateInline `  
` dataproc.workflowTemplates.list `  
` dataproc.workflowTemplates.setIamPolicy `  
` dataproc.workflowTemplates.update `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/editor ` （編集者）に追加されました。

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
Cloud Identity and Access Management  |  役割の更新  |

次の権限が役割 ` roles/iam.serviceAccountDeleter ` （サービス アカウントの削除）に追加されました。

` iam.serviceAccounts.get `  
` iam.serviceAccounts.list `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/viewer ` （閲覧者）に追加されました。

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
AutoML  |  追加  |  ` automl.columnSpecs.get `  
` automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.export `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
AutoML  |  カスタムの役割でサポート  |  ` automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.deploy `  
` automl.models.export `  
` automl.models.undeploy `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
Compute Engine  |  追加  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  2019-02-15 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Access Context Manager  |  一般提供開始  |

役割 ` roles/accesscontextmanager.policyAdmin ` （Access Context Manager
管理者）の一般提供を開始しました。  
  
Access Context Manager  |  一般提供開始  |

役割 ` roles/accesscontextmanager.policyEditor ` （Access Context Manager
編集者）の一般提供を開始しました。  
  
Access Context Manager  |  一般提供開始  |

役割 ` roles/accesscontextmanager.policyReader ` （Access Context Manager
読み取り）の一般提供を開始しました。  
  
Talent Solution  |  役割の追加  |

次の権限を持つ役割 ` roles/cloudjobdiscovery.profilesEditor ` （プロファイル編集者）が追加されました。

` cloudjobdiscovery.companies.create `  
` cloudjobdiscovery.companies.delete `  
` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.companies.update `  
` cloudjobdiscovery.events.create `  
` cloudjobdiscovery.events.delete `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.events.update `  
` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Talent Solution  |  役割の追加  |

次の権限を持つ役割 ` roles/cloudjobdiscovery.profilesViewer ` （プロファイル閲覧者）が追加されました。

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/editor ` （編集者）に追加されました。

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/owner ` （オーナー）に追加されました。

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
基本の役割  |  役割の更新  |

次の権限が役割 ` roles/viewer ` （閲覧者）に追加されました。

` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
  
Google Cloud オペレーションスイート  |  役割の更新  |

次の権限が役割 ` roles/stackdriver.accounts.editor ` （Stackdriver アカウント編集者）に追加されました。

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Google Cloud オペレーションスイート  |  役割の更新  |

次の権限が役割 ` roles/stackdriver.accounts.viewer ` （Stackdriver アカウント閲覧者）に追加されました。

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Access Context Manager  |  カスタムの役割でサポート  |  `
accesscontextmanager.accessLevels.create `  
` accesscontextmanager.accessLevels.delete `  
` accesscontextmanager.accessLevels.get `  
` accesscontextmanager.accessLevels.list `  
` accesscontextmanager.accessLevels.update `  
` accesscontextmanager.accessPolicies.create `  
` accesscontextmanager.accessPolicies.delete `  
` accesscontextmanager.accessPolicies.get `  
` accesscontextmanager.accessPolicies.getIamPolicy `  
` accesscontextmanager.accessPolicies.list `  
` accesscontextmanager.accessPolicies.setIamPolicy `  
` accesscontextmanager.accessPolicies.update `  
` accesscontextmanager.accessZones.create `  
` accesscontextmanager.accessZones.delete `  
` accesscontextmanager.accessZones.get `  
` accesscontextmanager.accessZones.list `  
` accesscontextmanager.accessZones.update `  
` accesscontextmanager.policies.create `  
` accesscontextmanager.policies.delete `  
` accesscontextmanager.policies.get `  
` accesscontextmanager.policies.getIamPolicy `  
` accesscontextmanager.policies.list `  
` accesscontextmanager.policies.setIamPolicy `  
` accesscontextmanager.policies.update `  
` accesscontextmanager.servicePerimeters.create `  
` accesscontextmanager.servicePerimeters.delete `  
` accesscontextmanager.servicePerimeters.get `  
` accesscontextmanager.servicePerimeters.list `  
` accesscontextmanager.servicePerimeters.update `  
  
Access Context Manager  |  一般提供開始  |  `
accesscontextmanager.accessLevels.create `  
` accesscontextmanager.accessLevels.delete `  
` accesscontextmanager.accessLevels.get `  
` accesscontextmanager.accessLevels.list `  
` accesscontextmanager.accessLevels.update `  
` accesscontextmanager.accessPolicies.create `  
` accesscontextmanager.accessPolicies.delete `  
` accesscontextmanager.accessPolicies.get `  
` accesscontextmanager.accessPolicies.getIamPolicy `  
` accesscontextmanager.accessPolicies.list `  
` accesscontextmanager.accessPolicies.setIamPolicy `  
` accesscontextmanager.accessPolicies.update `  
` accesscontextmanager.accessZones.create `  
` accesscontextmanager.accessZones.delete `  
` accesscontextmanager.accessZones.get `  
` accesscontextmanager.accessZones.list `  
` accesscontextmanager.accessZones.update `  
` accesscontextmanager.policies.create `  
` accesscontextmanager.policies.delete `  
` accesscontextmanager.policies.get `  
` accesscontextmanager.policies.getIamPolicy `  
` accesscontextmanager.policies.list `  
` accesscontextmanager.policies.setIamPolicy `  
` accesscontextmanager.policies.update `  
` accesscontextmanager.servicePerimeters.create `  
` accesscontextmanager.servicePerimeters.delete `  
` accesscontextmanager.servicePerimeters.get `  
` accesscontextmanager.servicePerimeters.list `  
` accesscontextmanager.servicePerimeters.update `  
  
Talent Solution  |  追加  |  ` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
  
##  2019-02-08 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
セキュリティ コマンド センター  |  カスタムの役割でサポート  |  ` securitycenter.assets.group `  
` securitycenter.assets.list `  
` securitycenter.assets.listAssetPropertyNames `  
` securitycenter.assets.runDiscovery `  
` securitycenter.assetsecuritymarks.update `  
` securitycenter.findings.group `  
` securitycenter.findings.list `  
` securitycenter.findings.listFindingPropertyNames `  
` securitycenter.findings.setState `  
` securitycenter.findings.update `  
` securitycenter.findingsecuritymarks.update `  
` securitycenter.organizationsettings.get `  
` securitycenter.organizationsettings.update `  
` securitycenter.sources.get `  
` securitycenter.sources.getIamPolicy `  
` securitycenter.sources.list `  
` securitycenter.sources.setIamPolicy `  
` securitycenter.sources.update `  
  
  
##  2019-02-01 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Dialogflow  |  一般提供開始  |

役割 ` roles/dialogflow.admin ` （Dialogflow API 管理者）の一般提供を開始しました。  
  
Dialogflow  |  一般提供開始  |

役割 ` roles/dialogflow.client ` （Dialogflow API クライアント）の一般提供を開始しました。  
  
Dialogflow  |  一般提供開始  |

役割 ` roles/dialogflow.consoleAgentEditor ` （Dialogflow コンソール
エージェント編集者）の一般提供を開始しました。  
  
Dialogflow  |  一般提供開始  |

役割 ` roles/dialogflow.reader ` （Dialogflow API 読み取り）の一般提供を開始しました。  
  
Cloud Asset Inventory  |  追加  |  ` cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Cloud Asset Inventory  |  カスタムの役割でサポート  |  ` cloudasset.assets.exportIamPolicy
`  
` cloudasset.assets.exportResource `  
  
Cloud Asset Inventory  |  一般提供開始  |  ` cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Dialogflow  |  カスタムの役割でサポート  |  ` dialogflow.agents.search `  
` dialogflow.agents.train `  
  
Dialogflow  |  一般提供開始  |  ` dialogflow.agents.export `  
` dialogflow.agents.get `  
` dialogflow.agents.import `  
` dialogflow.agents.restore `  
` dialogflow.agents.search `  
` dialogflow.agents.train `  
` dialogflow.contexts.create `  
` dialogflow.contexts.delete `  
` dialogflow.contexts.get `  
` dialogflow.contexts.list `  
` dialogflow.contexts.update `  
` dialogflow.entityTypes.create `  
` dialogflow.entityTypes.createEntity `  
` dialogflow.entityTypes.delete `  
` dialogflow.entityTypes.deleteEntity `  
` dialogflow.entityTypes.get `  
` dialogflow.entityTypes.list `  
` dialogflow.entityTypes.update `  
` dialogflow.entityTypes.updateEntity `  
` dialogflow.intents.create `  
` dialogflow.intents.delete `  
` dialogflow.intents.get `  
` dialogflow.intents.list `  
` dialogflow.intents.update `  
` dialogflow.operations.get `  
` dialogflow.sessionEntityTypes.create `  
` dialogflow.sessionEntityTypes.delete `  
` dialogflow.sessionEntityTypes.get `  
` dialogflow.sessionEntityTypes.list `  
` dialogflow.sessionEntityTypes.update `  
` dialogflow.sessions.detectIntent `  
` dialogflow.sessions.streamingDetectIntent `  
  
  
##  2019-01-25 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  追加  |  ` compute.instances.updateDisplayDevice `  
  
  
##  2019-01-11 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Identity-Aware Proxy  |  一般提供開始  |

役割 ` roles/iap.admin ` （IAP ポリシー管理者）の一般提供を開始しました。  
  
Identity-Aware Proxy  |  カスタムの役割でサポート  |  ` iap.web.getIamPolicy `  
` iap.web.setIamPolicy `  
` iap.webServiceVersions.accessViaIAP `  
` iap.webServiceVersions.getIamPolicy `  
` iap.webServiceVersions.setIamPolicy `  
` iap.webServices.getIamPolicy `  
` iap.webServices.setIamPolicy `  
` iap.webTypes.getIamPolicy `  
` iap.webTypes.setIamPolicy `  
  
  
##  2018-12-21 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud DNS  |  追加  |  ` dns.networks.bindPrivateDNSZone `  
  
Cloud DNS  |  カスタムの役割でサポート  |  ` dns.networks.bindPrivateDNSZone `  
  
  
##  2018-12-14 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Firebase 認証  |  追加  |  ` firebaseauth.configs.create `  
  
Firebase 認証  |  カスタムの役割でサポート  |  ` firebaseauth.configs.create `  
  
  
##  2018-12-07 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
BigQuery  |  追加  |  ` bigquery.readsessions.create `  
  
BigQuery  |  カスタムの役割でサポート  |  ` bigquery.readsessions.create `  
  
Google Kubernetes Engine  |  カスタムの役割でサポート  |  `
container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
Google Kubernetes Engine  |  一般提供開始  |  ` container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  2018-11-30 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Asset Inventory  |  一般提供開始  |

役割 ` roles/cloudasset.viewer ` （クラウド アセット閲覧者）の一般提供を開始しました。  
  
Cloud Asset Inventory  |  一般提供開始  |  ` cloudasset.assets.exportAll `  
  
Compute Engine  |  追加  |  ` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.disks.getIamPolicy `  
` compute.disks.setIamPolicy `  
` compute.images.getIamPolicy `  
` compute.instances.getIamPolicy `  
` compute.instances.setIamPolicy `  
` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.licenses.getIamPolicy `  
` compute.licenses.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
` compute.snapshots.getIamPolicy `  
` compute.snapshots.setIamPolicy `  
` compute.subnetworks.getIamPolicy `  
` compute.subnetworks.setIamPolicy `  
  
Compute Engine  |  一般提供開始  |  ` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
` compute.subnetworks.getIamPolicy `  
` compute.subnetworks.setIamPolicy `  
  
  
##  2018-11-16 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
AutoML  |  追加  |  ` automl.locations.getIamPolicy `  
` automl.locations.setIamPolicy `  
  
AutoML  |  カスタムの役割でサポート  |  ` automl.locations.getIamPolicy `  
` automl.locations.setIamPolicy `  
  
Talent Solution  |  追加  |  ` cloudjobdiscovery.events.create `  
` cloudjobdiscovery.events.delete `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.events.update `  
  
Compute Engine  |  追加  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  一般提供開始  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Google Kubernetes Engine  |  追加  |  ` container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  2018-11-09 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Google アナリティクス  |  追加  |  ` firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
Google アナリティクス  |  カスタムの役割でサポート  |  `
firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
  
##  2018-11-02 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  一般提供開始  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  カスタムの役割でサポート  |  ` file.instances.create `  
` file.instances.delete `  
` file.instances.get `  
` file.instances.list `  
` file.instances.update `  
` file.locations.get `  
` file.locations.list `  
` file.operations.get `  
` file.operations.list `  
  
Google Cloud オペレーションスイート  |  追加  |  ` stackdriver.resourceMetadata.write `  
  
Google Cloud オペレーションスイート  |  カスタムの役割でサポート  |  `
stackdriver.resourceMetadata.write `  
  
  
##  2018-10-26 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
BigQuery  |  一般提供開始  |

役割 ` roles/bigquery.metadataViewer ` （BigQuery メタデータ閲覧者）の一般提供を開始しました。  
  
Cloud Identity and Access Management  |  一般提供開始  |

役割 ` roles/iam.serviceAccountDeleter ` （サービス アカウントの削除）の一般提供を開始しました。  
  
Firebase Realtime Database  |  追加  |  ` firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
Firebase Realtime Database  |  カスタムの役割でサポート  |  `
firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
Firebase と外部サービスの統合  |  追加  |  ` firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
Firebase と外部サービスの統合  |  カスタムの役割でサポート  |  ` firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
  
##  2018-10-19 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Google Cloud サポート  |  一般提供開始  |

役割 ` roles/cloudsupport.admin ` （サポート アカウント管理者）の一般提供を開始しました。  
  
Google Cloud サポート  |  一般提供開始  |

役割 ` roles/cloudsupport.viewer ` （サポート アカウント閲覧者）の一般提供を開始しました。  
  
Firebase Remote Config  |  追加  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Firebase Remote Config  |  カスタムの役割でサポート  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Google Cloud サポート  |  カスタムの役割でサポート  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Google Cloud サポート  |  一般提供開始  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Compute Engine  |  追加  |  ` compute.networks.updatePeering `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.networks.updatePeering `  
  
Firebase Crashlytics  |  追加  |  ` firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase Crashlytics  |  カスタムの役割でサポート  |  ` firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase Dynamic Links  |  追加  |  ` firebasedynamiclinks.destinations.list `  
` firebasedynamiclinks.destinations.update `  
` firebasedynamiclinks.domains.create `  
` firebasedynamiclinks.domains.delete `  
` firebasedynamiclinks.domains.get `  
` firebasedynamiclinks.domains.list `  
` firebasedynamiclinks.domains.update `  
` firebasedynamiclinks.links.create `  
` firebasedynamiclinks.links.get `  
` firebasedynamiclinks.links.list `  
` firebasedynamiclinks.links.update `  
` firebasedynamiclinks.stats.get `  
  
Firebase Dynamic Links  |  カスタムの役割でサポート  |  `
firebasedynamiclinks.destinations.list `  
` firebasedynamiclinks.destinations.update `  
` firebasedynamiclinks.domains.create `  
` firebasedynamiclinks.domains.delete `  
` firebasedynamiclinks.domains.get `  
` firebasedynamiclinks.domains.list `  
` firebasedynamiclinks.domains.update `  
` firebasedynamiclinks.links.create `  
` firebasedynamiclinks.links.get `  
` firebasedynamiclinks.links.list `  
` firebasedynamiclinks.links.update `  
` firebasedynamiclinks.stats.get `  
  
Firebase アプリ内メッセージング  |  追加  |  ` firebaseinappmessaging.campaigns.create `  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Firebase アプリ内メッセージング  |  カスタムの役割でサポート  |  `
firebaseinappmessaging.campaigns.create `  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Firebase Cloud Messaging  |  追加  |  ` firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Cloud Messaging  |  カスタムの役割でサポート  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Performance Monitoring  |  追加  |  ` firebaseperformance.config.create
`  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Performance Monitoring  |  カスタムの役割でサポート  |  `
firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Predictions  |  追加  |  ` firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
Firebase Predictions  |  カスタムの役割でサポート  |  `
firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
セキュリティ コマンド センター  |  追加  |  ` securitycenter.assets.get `  
` securitycenter.assets.getFieldNames `  
` securitycenter.assets.group `  
` securitycenter.assets.list `  
` securitycenter.assets.listAssetPropertyNames `  
` securitycenter.assets.runDiscovery `  
` securitycenter.assets.triggerDiscovery `  
` securitycenter.assets.update `  
` securitycenter.assetsecuritymarks.update `  
` securitycenter.configs.get `  
` securitycenter.configs.getIamPolicy `  
` securitycenter.configs.setIamPolicy `  
` securitycenter.configs.update `  
` securitycenter.findings.group `  
` securitycenter.findings.list `  
` securitycenter.findings.listFindingPropertyNames `  
` securitycenter.findings.setState `  
` securitycenter.findings.update `  
` securitycenter.findingsecuritymarks.update `  
` securitycenter.organizationsettings.get `  
` securitycenter.organizationsettings.update `  
` securitycenter.scans.get `  
` securitycenter.scans.list `  
` securitycenter.sources.get `  
` securitycenter.sources.getIamPolicy `  
` securitycenter.sources.list `  
` securitycenter.sources.setIamPolicy `  
` securitycenter.sources.update `  
  
Service Consumer Management  |  追加  |  `
serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
Service Consumer Management  |  カスタムの役割でサポート  |  `
serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
  
##  2018-10-12 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.admin ` （DLP 管理者）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.analyzeRiskTemplatesEditor ` （DLP リスク分析テンプレート編集者）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.analyzeRiskTemplatesReader ` （DLP リスク分析テンプレート読み取り）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.deidentifyTemplatesEditor ` （DLP 匿名化テンプレート編集者）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.deidentifyTemplatesReader ` （DLP 匿名化テンプレート読み取り）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.inspectTemplatesEditor ` （DLP 検査テンプレート編集者）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.inspectTemplatesReader ` （DLP 検査テンプレート読み取り）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.jobsEditor ` （DLP ジョブ編集者）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.jobsReader ` （DLP ジョブ読み取り）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.jobTriggersEditor ` （DLP ジョブトリガー編集者）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.jobTriggersReader ` （DLP ジョブトリガー読み取り）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.reader ` （DLP リーダー）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.storedInfoTypesEditor ` （DLP Stored InfoTypes 編集者）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.storedInfoTypesReader ` （DLP Stored InfoTypes
読み取り）の一般提供を開始しました。  
  
Cloud Data Loss Prevention  |  一般提供開始  |

役割 ` roles/dlp.user ` （DLP ユーザー）の一般提供を開始しました。  
  
Google Kubernetes Engine  |  カスタムの役割でサポート  |  `
container.certificateSigningRequests.approve `  
` container.clusterRoles.bind `  
` container.deployments.rollback `  
` container.nodes.proxy `  
` container.pods.attach `  
` container.pods.evict `  
` container.pods.exec `  
` container.pods.getLogs `  
` container.pods.portForward `  
` container.pods.proxy `  
` container.roles.bind `  
` container.services.proxy `  
` container.thirdPartyObjects.create `  
` container.thirdPartyObjects.delete `  
` container.thirdPartyObjects.get `  
` container.thirdPartyObjects.list `  
` container.thirdPartyObjects.update `  
  
Cloud Data Loss Prevention  |  カスタムの役割でサポート  |  `
dlp.analyzeRiskTemplates.create `  
` dlp.analyzeRiskTemplates.delete `  
` dlp.analyzeRiskTemplates.get `  
` dlp.analyzeRiskTemplates.list `  
` dlp.analyzeRiskTemplates.update `  
` dlp.deidentifyTemplates.create `  
` dlp.deidentifyTemplates.delete `  
` dlp.deidentifyTemplates.get `  
` dlp.deidentifyTemplates.list `  
` dlp.deidentifyTemplates.update `  
` dlp.inspectTemplates.create `  
` dlp.inspectTemplates.delete `  
` dlp.inspectTemplates.get `  
` dlp.inspectTemplates.list `  
` dlp.inspectTemplates.update `  
` dlp.jobTriggers.create `  
` dlp.jobTriggers.delete `  
` dlp.jobTriggers.get `  
` dlp.jobTriggers.list `  
` dlp.jobTriggers.update `  
` dlp.jobs.cancel `  
` dlp.jobs.create `  
` dlp.jobs.delete `  
` dlp.jobs.get `  
` dlp.jobs.list `  
` dlp.kms.encrypt `  
  
Cloud Data Loss Prevention  |  一般提供開始  |  ` dlp.analyzeRiskTemplates.create `  
` dlp.analyzeRiskTemplates.delete `  
` dlp.analyzeRiskTemplates.get `  
` dlp.analyzeRiskTemplates.list `  
` dlp.analyzeRiskTemplates.update `  
` dlp.deidentifyTemplates.create `  
` dlp.deidentifyTemplates.delete `  
` dlp.deidentifyTemplates.get `  
` dlp.deidentifyTemplates.list `  
` dlp.deidentifyTemplates.update `  
` dlp.inspectTemplates.create `  
` dlp.inspectTemplates.delete `  
` dlp.inspectTemplates.get `  
` dlp.inspectTemplates.list `  
` dlp.inspectTemplates.update `  
` dlp.jobTriggers.create `  
` dlp.jobTriggers.delete `  
` dlp.jobTriggers.get `  
` dlp.jobTriggers.list `  
` dlp.jobTriggers.update `  
` dlp.jobs.cancel `  
` dlp.jobs.create `  
` dlp.jobs.delete `  
` dlp.jobs.get `  
` dlp.jobs.list `  
` dlp.kms.encrypt `  
` dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud DNS  |  カスタムの役割でサポート  |  ` dns.dnsKeys.get `  
` dns.dnsKeys.list `  
` dns.managedZoneOperations.get `  
` dns.managedZoneOperations.list `  
` dns.managedZones.update `  
  
Firebase  |  追加  |  ` firebase.billingPlans.get `  
` firebase.billingPlans.update `  
` firebase.clients.create `  
` firebase.clients.delete `  
` firebase.clients.get `  
` firebase.links.create `  
` firebase.links.delete `  
` firebase.links.list `  
` firebase.links.update `  
` firebase.projects.delete `  
` firebase.projects.get `  
` firebase.projects.update `  
  
Firebase  |  カスタムの役割でサポート  |  ` firebase.billingPlans.get `  
` firebase.billingPlans.update `  
` firebase.clients.create `  
` firebase.clients.delete `  
` firebase.clients.get `  
` firebase.links.create `  
` firebase.links.delete `  
` firebase.links.list `  
` firebase.links.update `  
` firebase.projects.delete `  
` firebase.projects.get `  
` firebase.projects.update `  
  
Firebase A/B テスト  |  追加  |  ` firebaseabt.experimentresults.get `  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Firebase A/B テスト  |  カスタムの役割でサポート  |  ` firebaseabt.experimentresults.get `  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Firebase 認証  |  追加  |  ` firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase 認証  |  カスタムの役割でサポート  |  ` firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Realtime Database  |  追加  |  ` firebasedatabase.instances.get `  
` firebasedatabase.instances.update `  
  
Firebase Realtime Database  |  カスタムの役割でサポート  |  `
firebasedatabase.instances.get `  
` firebasedatabase.instances.update `  
  
Firebase Hosting  |  追加  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase Hosting  |  カスタムの役割でサポート  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase 向け ML Kit  |  追加  |  ` firebaseml.compressionjobs.create `  
` firebaseml.compressionjobs.delete `  
` firebaseml.compressionjobs.get `  
` firebaseml.compressionjobs.list `  
` firebaseml.compressionjobs.start `  
` firebaseml.compressionjobs.update `  
` firebaseml.models.create `  
` firebaseml.models.delete `  
` firebaseml.models.get `  
` firebaseml.models.list `  
` firebaseml.modelversions.create `  
` firebaseml.modelversions.get `  
` firebaseml.modelversions.list `  
` firebaseml.modelversions.update `  
  
Firebase 向け ML Kit  |  カスタムの役割でサポート  |  ` firebaseml.compressionjobs.create `  
` firebaseml.compressionjobs.delete `  
` firebaseml.compressionjobs.get `  
` firebaseml.compressionjobs.list `  
` firebaseml.compressionjobs.start `  
` firebaseml.compressionjobs.update `  
` firebaseml.models.create `  
` firebaseml.models.delete `  
` firebaseml.models.get `  
` firebaseml.models.list `  
` firebaseml.modelversions.create `  
` firebaseml.modelversions.get `  
` firebaseml.modelversions.list `  
` firebaseml.modelversions.update `  
  
Firebase セキュリティ ルール  |  追加  |  ` firebaserules.releases.create `  
` firebaserules.releases.delete `  
` firebaserules.releases.get `  
` firebaserules.releases.getExecutable `  
` firebaserules.releases.list `  
` firebaserules.releases.update `  
` firebaserules.rulesets.create `  
` firebaserules.rulesets.delete `  
` firebaserules.rulesets.get `  
` firebaserules.rulesets.list `  
` firebaserules.rulesets.test `  
  
Firebase セキュリティ ルール  |  カスタムの役割でサポート  |  ` firebaserules.releases.create `  
` firebaserules.releases.delete `  
` firebaserules.releases.get `  
` firebaserules.releases.getExecutable `  
` firebaserules.releases.list `  
` firebaserules.releases.update `  
` firebaserules.rulesets.create `  
` firebaserules.rulesets.delete `  
` firebaserules.rulesets.get `  
` firebaserules.rulesets.list `  
` firebaserules.rulesets.test `  
  
  
##  2018-10-05 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  追加  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  一般提供開始  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Google Kubernetes Engine  |  カスタムの役割でサポート  |  `
container.apiServices.updateStatus `  
` container.certificateSigningRequests.updateStatus `  
` container.cronJobs.getStatus `  
` container.cronJobs.updateStatus `  
` container.customResourceDefinitions.updateStatus `  
` container.daemonSets.getStatus `  
` container.daemonSets.updateStatus `  
` container.deployments.getScale `  
` container.deployments.getStatus `  
` container.deployments.updateScale `  
` container.deployments.updateStatus `  
` container.horizontalPodAutoscalers.getStatus `  
` container.horizontalPodAutoscalers.updateStatus `  
` container.ingresses.getStatus `  
` container.ingresses.updateStatus `  
` container.jobs.getStatus `  
` container.jobs.updateStatus `  
` container.namespaces.getStatus `  
` container.namespaces.updateStatus `  
` container.nodes.getStatus `  
` container.nodes.updateStatus `  
` container.persistentVolumeClaims.getStatus `  
` container.persistentVolumeClaims.updateStatus `  
` container.persistentVolumes.getStatus `  
` container.persistentVolumes.updateStatus `  
` container.podDisruptionBudgets.getStatus `  
` container.podDisruptionBudgets.updateStatus `  
` container.pods.getStatus `  
` container.pods.updateStatus `  
` container.replicaSets.getScale `  
` container.replicaSets.getStatus `  
` container.replicaSets.updateScale `  
` container.replicaSets.updateStatus `  
` container.replicationControllers.getScale `  
` container.replicationControllers.getStatus `  
` container.replicationControllers.updateScale `  
` container.replicationControllers.updateStatus `  
` container.resourceQuotas.getStatus `  
` container.resourceQuotas.updateStatus `  
` container.services.getStatus `  
` container.services.updateStatus `  
` container.statefulSets.getScale `  
` container.statefulSets.getStatus `  
` container.statefulSets.updateScale `  
` container.statefulSets.updateStatus `  
  
Google Kubernetes Engine  |  一般提供開始  |  ` container.cronJobs.getStatus `  
` container.daemonSets.getStatus `  
` container.deployments.getStatus `  
` container.horizontalPodAutoscalers.getStatus `  
` container.ingresses.getStatus `  
` container.jobs.getStatus `  
` container.namespaces.getStatus `  
` container.nodes.getStatus `  
` container.persistentVolumeClaims.getStatus `  
` container.persistentVolumes.getStatus `  
` container.podDisruptionBudgets.getStatus `  
` container.pods.getStatus `  
` container.replicaSets.getScale `  
` container.replicaSets.getStatus `  
` container.replicaSets.updateScale `  
` container.replicationControllers.getScale `  
` container.replicationControllers.getStatus `  
` container.replicationControllers.updateScale `  
` container.resourceQuotas.getStatus `  
` container.services.getStatus `  
` container.statefulSets.getStatus `  
  
  
##  2018-09-21 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
AutoML  |  追加  |  ` automl.datasets.getIamPolicy `  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
AutoML  |  カスタムの役割でサポート  |  ` automl.datasets.getIamPolicy `  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
Cloud Asset Inventory  |  追加  |  ` cloudasset.assets.exportAll `  
  
Cloud Asset Inventory  |  カスタムの役割でサポート  |  ` cloudasset.assets.exportAll `  
  
Compute Engine  |  追加  |  ` compute.licenses.delete `  
  
Google Kubernetes Engine  |  カスタムの役割でサポート  |  ` container.apiServices.create `  
` container.apiServices.delete `  
` container.apiServices.get `  
` container.apiServices.list `  
` container.apiServices.update `  
` container.bindings.create `  
` container.certificateSigningRequests.create `  
` container.certificateSigningRequests.delete `  
` container.certificateSigningRequests.get `  
` container.certificateSigningRequests.list `  
` container.certificateSigningRequests.update `  
` container.clusterRoleBindings.create `  
` container.clusterRoleBindings.delete `  
` container.clusterRoleBindings.get `  
` container.clusterRoleBindings.list `  
` container.clusterRoleBindings.update `  
` container.clusterRoles.create `  
` container.clusterRoles.delete `  
` container.clusterRoles.get `  
` container.clusterRoles.list `  
` container.clusterRoles.update `  
` container.componentStatuses.get `  
` container.componentStatuses.list `  
` container.configMaps.create `  
` container.configMaps.delete `  
` container.configMaps.get `  
` container.configMaps.list `  
` container.configMaps.update `  
` container.controllerRevisions.create `  
` container.controllerRevisions.delete `  
` container.controllerRevisions.get `  
` container.controllerRevisions.list `  
` container.controllerRevisions.update `  
` container.cronJobs.create `  
` container.cronJobs.delete `  
` container.cronJobs.get `  
` container.cronJobs.list `  
` container.cronJobs.update `  
` container.customResourceDefinitions.create `  
` container.customResourceDefinitions.delete `  
` container.customResourceDefinitions.get `  
` container.customResourceDefinitions.list `  
` container.customResourceDefinitions.update `  
` container.daemonSets.create `  
` container.daemonSets.delete `  
` container.daemonSets.get `  
` container.daemonSets.list `  
` container.daemonSets.update `  
` container.deployments.create `  
` container.deployments.delete `  
` container.deployments.get `  
` container.deployments.list `  
` container.deployments.update `  
` container.endpoints.create `  
` container.endpoints.delete `  
` container.endpoints.get `  
` container.endpoints.list `  
` container.endpoints.update `  
` container.events.create `  
` container.events.delete `  
` container.events.get `  
` container.events.list `  
` container.events.update `  
` container.horizontalPodAutoscalers.create `  
` container.horizontalPodAutoscalers.delete `  
` container.horizontalPodAutoscalers.get `  
` container.horizontalPodAutoscalers.list `  
` container.horizontalPodAutoscalers.update `  
` container.ingresses.create `  
` container.ingresses.delete `  
` container.ingresses.get `  
` container.ingresses.list `  
` container.ingresses.update `  
` container.jobs.create `  
` container.jobs.delete `  
` container.jobs.get `  
` container.jobs.list `  
` container.jobs.update `  
` container.limitRanges.create `  
` container.limitRanges.delete `  
` container.limitRanges.get `  
` container.limitRanges.list `  
` container.limitRanges.update `  
` container.localSubjectAccessReviews.create `  
` container.namespaces.create `  
` container.namespaces.delete `  
` container.namespaces.get `  
` container.namespaces.list `  
` container.namespaces.update `  
` container.networkPolicies.create `  
` container.networkPolicies.delete `  
` container.networkPolicies.get `  
` container.networkPolicies.list `  
` container.networkPolicies.update `  
` container.nodes.create `  
` container.nodes.delete `  
` container.nodes.get `  
` container.nodes.list `  
` container.nodes.update `  
` container.persistentVolumeClaims.create `  
` container.persistentVolumeClaims.delete `  
` container.persistentVolumeClaims.get `  
` container.persistentVolumeClaims.list `  
` container.persistentVolumeClaims.update `  
` container.persistentVolumes.create `  
` container.persistentVolumes.delete `  
` container.persistentVolumes.get `  
` container.persistentVolumes.list `  
` container.persistentVolumes.update `  
` container.podDisruptionBudgets.create `  
` container.podDisruptionBudgets.delete `  
` container.podDisruptionBudgets.get `  
` container.podDisruptionBudgets.list `  
` container.podDisruptionBudgets.update `  
` container.podSecurityPolicies.create `  
` container.podSecurityPolicies.delete `  
` container.podSecurityPolicies.get `  
` container.podSecurityPolicies.list `  
` container.podSecurityPolicies.update `  
` container.podTemplates.create `  
` container.podTemplates.delete `  
` container.podTemplates.get `  
` container.podTemplates.list `  
` container.podTemplates.update `  
` container.pods.create `  
` container.pods.delete `  
` container.pods.get `  
` container.pods.list `  
` container.pods.update `  
` container.replicaSets.create `  
` container.replicaSets.delete `  
` container.replicaSets.get `  
` container.replicaSets.list `  
` container.replicaSets.update `  
` container.replicationControllers.create `  
` container.replicationControllers.delete `  
` container.replicationControllers.get `  
` container.replicationControllers.list `  
` container.replicationControllers.update `  
` container.resourceQuotas.create `  
` container.resourceQuotas.delete `  
` container.resourceQuotas.get `  
` container.resourceQuotas.list `  
` container.resourceQuotas.update `  
` container.roleBindings.create `  
` container.roleBindings.delete `  
` container.roleBindings.get `  
` container.roleBindings.list `  
` container.roleBindings.update `  
` container.roles.create `  
` container.roles.delete `  
` container.roles.get `  
` container.roles.list `  
` container.roles.update `  
` container.secrets.create `  
` container.secrets.delete `  
` container.secrets.get `  
` container.secrets.list `  
` container.secrets.update `  
` container.selfSubjectAccessReviews.create `  
` container.serviceAccounts.create `  
` container.serviceAccounts.delete `  
` container.serviceAccounts.get `  
` container.serviceAccounts.list `  
` container.serviceAccounts.update `  
` container.services.create `  
` container.services.delete `  
` container.services.get `  
` container.services.list `  
` container.services.update `  
` container.statefulSets.create `  
` container.statefulSets.delete `  
` container.statefulSets.get `  
` container.statefulSets.list `  
` container.statefulSets.update `  
` container.storageClasses.create `  
` container.storageClasses.delete `  
` container.storageClasses.get `  
` container.storageClasses.list `  
` container.storageClasses.update `  
` container.subjectAccessReviews.create `  
  
  
##  2018-09-07 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Memorystore for Redis  |  カスタムの役割でサポート  |  ` redis.operations.cancel `  
` redis.operations.delete `  
  
  
##  2018-08-31 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Google Kubernetes Engine  |  追加  |  ` container.cronJobs.getStatus `  
` container.daemonSets.getStatus `  
` container.deployments.getStatus `  
` container.horizontalPodAutoscalers.getStatus `  
` container.ingresses.getStatus `  
` container.jobs.getStatus `  
` container.namespaces.getStatus `  
` container.nodes.getStatus `  
` container.persistentVolumeClaims.getStatus `  
` container.persistentVolumes.getStatus `  
` container.podDisruptionBudgets.getStatus `  
` container.pods.getStatus `  
` container.replicaSets.getScale `  
` container.replicaSets.getStatus `  
` container.replicaSets.updateScale `  
` container.replicationControllers.getScale `  
` container.replicationControllers.getStatus `  
` container.replicationControllers.updateScale `  
` container.resourceQuotas.getStatus `  
` container.services.getStatus `  
` container.statefulSets.getStatus `  
  
Cloud Data Loss Prevention  |  追加  |  ` dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud Data Loss Prevention  |  カスタムの役割でサポート  |  ` dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud ソース レポジトリ  |  追加  |  ` source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud ソース レポジトリ  |  カスタムの役割でサポート  |  ` source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud ソース レポジトリ  |  一般提供開始  |  ` source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
  
##  2018-08-10 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Binary Authorization  |  追加  |  `
binaryauthorization.attestors.verifyImageAttested `  
  
Binary Authorization  |  カスタムの役割でサポート  |  `
binaryauthorization.attestors.verifyImageAttested `  
  
Compute Engine  |  追加  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  追加  |  ` file.instances.create `  
` file.instances.delete `  
` file.instances.get `  
` file.instances.list `  
` file.instances.update `  
` file.locations.get `  
` file.locations.list `  
` file.operations.cancel `  
` file.operations.delete `  
` file.operations.get `  
` file.operations.list `  
  
  
##  2018-08-03 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Android Management API  |  カスタムの役割でサポート  |  `
androidmanagement.enterprises.manage `  
  
Android Management API  |  一般提供開始  |  ` androidmanagement.enterprises.manage `  
  
クラウドのお支払いとご請求  |  カスタムの役割でサポート  |  ` billing.resourceCosts.get `  
  
Binary Authorization  |  追加  |  ` binaryauthorization.policy.get `  
` binaryauthorization.policy.getIamPolicy `  
` binaryauthorization.policy.setIamPolicy `  
` binaryauthorization.policy.update `  
  
Cloud Composer  |  一般提供開始  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Compute Engine  |  一般提供開始  |  ` compute.nodeGroups.addNodes `  
` compute.nodeGroups.create `  
` compute.nodeGroups.delete `  
` compute.nodeGroups.deleteNodes `  
` compute.nodeGroups.get `  
` compute.nodeGroups.list `  
` compute.nodeGroups.setNodeTemplate `  
` compute.nodeTemplates.create `  
` compute.nodeTemplates.delete `  
` compute.nodeTemplates.get `  
` compute.nodeTemplates.list `  
` compute.nodeTypes.get `  
` compute.nodeTypes.list `  
  
Google Kubernetes Engine  |  一般提供開始  |  ` container.hostServiceAgent.use `  
  
Memorystore for Redis  |  追加  |  ` redis.operations.cancel `  
  
Memorystore for Redis  |  カスタムの役割でサポート  |  ` redis.instances.create `  
` redis.instances.delete `  
` redis.instances.get `  
` redis.instances.list `  
` redis.instances.update `  
` redis.locations.get `  
` redis.locations.list `  
` redis.operations.get `  
` redis.operations.list `  
  
Google で購読  |  追加  |  ` subscribewithgoogledeveloper.tools.get `  
  
Google で購読  |  カスタムの役割でサポート  |  ` subscribewithgoogledeveloper.tools.get `  
  
  
##  2018-07-20 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Access Context Manager  |  追加  |  ` accesscontextmanager.accessLevels.create `  
` accesscontextmanager.accessLevels.delete `  
` accesscontextmanager.accessLevels.get `  
` accesscontextmanager.accessLevels.list `  
` accesscontextmanager.accessLevels.update `  
` accesscontextmanager.accessPolicies.create `  
` accesscontextmanager.accessPolicies.delete `  
` accesscontextmanager.accessPolicies.get `  
` accesscontextmanager.accessPolicies.getIamPolicy `  
` accesscontextmanager.accessPolicies.list `  
` accesscontextmanager.accessPolicies.setIamPolicy `  
` accesscontextmanager.accessPolicies.update `  
` accesscontextmanager.accessZones.create `  
` accesscontextmanager.accessZones.delete `  
` accesscontextmanager.accessZones.get `  
` accesscontextmanager.accessZones.list `  
` accesscontextmanager.accessZones.update `  
` accesscontextmanager.policies.create `  
` accesscontextmanager.policies.delete `  
` accesscontextmanager.policies.get `  
` accesscontextmanager.policies.getIamPolicy `  
` accesscontextmanager.policies.list `  
` accesscontextmanager.policies.setIamPolicy `  
` accesscontextmanager.policies.update `  
` accesscontextmanager.servicePerimeters.create `  
` accesscontextmanager.servicePerimeters.delete `  
` accesscontextmanager.servicePerimeters.get `  
` accesscontextmanager.servicePerimeters.list `  
` accesscontextmanager.servicePerimeters.update `  
  
AutoML  |  追加  |  ` automl.annotationSpecs.create `  
` automl.annotationSpecs.delete `  
` automl.annotationSpecs.get `  
` automl.annotationSpecs.list `  
` automl.annotationSpecs.update `  
` automl.annotations.approve `  
` automl.annotations.create `  
` automl.annotations.list `  
` automl.annotations.manipulate `  
` automl.annotations.reject `  
` automl.datasets.create `  
` automl.datasets.delete `  
` automl.datasets.export `  
` automl.datasets.get `  
` automl.datasets.import `  
` automl.datasets.list `  
` automl.examples.delete `  
` automl.examples.get `  
` automl.examples.list `  
` automl.humanAnnotationTasks.create `  
` automl.humanAnnotationTasks.delete `  
` automl.humanAnnotationTasks.get `  
` automl.humanAnnotationTasks.list `  
` automl.locations.get `  
` automl.locations.list `  
` automl.modelEvaluations.create `  
` automl.modelEvaluations.get `  
` automl.modelEvaluations.list `  
` automl.models.create `  
` automl.models.delete `  
` automl.models.deploy `  
` automl.models.get `  
` automl.models.list `  
` automl.models.predict `  
` automl.models.undeploy `  
` automl.operations.cancel `  
` automl.operations.delete `  
` automl.operations.get `  
` automl.operations.list `  
  
AutoML  |  カスタムの役割でサポート  |  ` automl.annotationSpecs.create `  
` automl.annotationSpecs.delete `  
` automl.annotationSpecs.get `  
` automl.annotationSpecs.list `  
` automl.annotationSpecs.update `  
` automl.annotations.approve `  
` automl.annotations.create `  
` automl.annotations.list `  
` automl.annotations.manipulate `  
` automl.annotations.reject `  
` automl.datasets.create `  
` automl.datasets.delete `  
` automl.datasets.export `  
` automl.datasets.get `  
` automl.datasets.import `  
` automl.datasets.list `  
` automl.examples.delete `  
` automl.examples.get `  
` automl.examples.list `  
` automl.humanAnnotationTasks.create `  
` automl.humanAnnotationTasks.get `  
` automl.humanAnnotationTasks.list `  
` automl.locations.get `  
` automl.locations.list `  
` automl.modelEvaluations.get `  
` automl.modelEvaluations.list `  
` automl.models.create `  
` automl.models.delete `  
` automl.models.get `  
` automl.models.list `  
` automl.models.predict `  
` automl.operations.cancel `  
` automl.operations.delete `  
` automl.operations.get `  
` automl.operations.list `  
  
Binary Authorization  |  追加  |  ` binaryauthorization.attestors.create `  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
Binary Authorization  |  カスタムの役割でサポート  |  `
binaryauthorization.attestors.create `  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
Cloud DNS  |  カスタムの役割でサポート  |  ` dns.changes.create `  
` dns.changes.get `  
` dns.changes.list `  
` dns.managedZones.create `  
` dns.managedZones.delete `  
` dns.managedZones.get `  
` dns.managedZones.list `  
` dns.projects.get `  
` dns.resourceRecordSets.create `  
` dns.resourceRecordSets.delete `  
` dns.resourceRecordSets.list `  
` dns.resourceRecordSets.update `  
  
  
##  2018-07-13 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
BigQuery  |  追加  |  ` bigquery.datasets.getIamPolicy `  
` bigquery.datasets.setIamPolicy `  
  
データストア  |  追加  |  ` datastore.locations.get `  
` datastore.locations.list `  
  
  
##  2018-07-06 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Composer  |  カスタムの役割でサポート  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Endpoints  |  追加  |  ` endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud Endpoints  |  カスタムの役割でサポート  |  ` endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud TPU  |  追加  |  ` tpu.acceleratortypes.get `  
` tpu.acceleratortypes.list `  
` tpu.locations.get `  
` tpu.locations.list `  
` tpu.nodes.create `  
` tpu.nodes.delete `  
` tpu.nodes.get `  
` tpu.nodes.list `  
` tpu.nodes.reimage `  
` tpu.nodes.reset `  
` tpu.nodes.start `  
` tpu.nodes.stop `  
` tpu.operations.get `  
` tpu.operations.list `  
` tpu.tensorflowversions.get `  
` tpu.tensorflowversions.list `  
  
Cloud TPU  |  カスタムの役割でサポート  |  ` tpu.acceleratortypes.get `  
` tpu.acceleratortypes.list `  
` tpu.locations.get `  
` tpu.locations.list `  
` tpu.nodes.create `  
` tpu.nodes.delete `  
` tpu.nodes.get `  
` tpu.nodes.list `  
` tpu.nodes.reimage `  
` tpu.nodes.reset `  
` tpu.nodes.start `  
` tpu.nodes.stop `  
` tpu.operations.get `  
` tpu.operations.list `  
` tpu.tensorflowversions.get `  
` tpu.tensorflowversions.list `  
  
  
##  2018-06-29 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Identity and Access Management  |  一般提供開始  |  `
iam.serviceAccounts.implicitDelegation `  
  
  
##  2018-06-15 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.backendServices.create `  
` compute.backendServices.delete `  
` compute.backendServices.get `  
` compute.backendServices.list `  
` compute.backendServices.setSecurityPolicy `  
` compute.backendServices.update `  
` compute.backendServices.use `  
` compute.regionBackendServices.create `  
` compute.regionBackendServices.delete `  
` compute.regionBackendServices.get `  
` compute.regionBackendServices.list `  
` compute.regionBackendServices.setSecurityPolicy `  
` compute.regionBackendServices.update `  
` compute.regionBackendServices.use `  
` compute.targetHttpProxies.create `  
` compute.targetHttpProxies.setUrlMap `  
` compute.targetHttpsProxies.create `  
` compute.targetHttpsProxies.setUrlMap `  
` compute.targetSslProxies.create `  
` compute.targetSslProxies.setBackendService `  
` compute.targetTcpProxies.create `  
` compute.targetTcpProxies.update `  
  
Compute Engine  |  一般提供開始  |  ` compute.regionBackendServices.create `  
` compute.regionBackendServices.delete `  
` compute.regionBackendServices.get `  
` compute.regionBackendServices.list `  
` compute.regionBackendServices.setSecurityPolicy `  
` compute.regionBackendServices.update `  
` compute.regionBackendServices.use `  
  
  
##  2018-06-08 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  追加  |  ` compute.nodeGroups.addNodes `  
` compute.nodeGroups.create `  
` compute.nodeGroups.delete `  
` compute.nodeGroups.deleteNodes `  
` compute.nodeGroups.get `  
` compute.nodeGroups.list `  
` compute.nodeGroups.setNodeTemplate `  
` compute.nodeTemplates.create `  
` compute.nodeTemplates.delete `  
` compute.nodeTemplates.get `  
` compute.nodeTemplates.list `  
` compute.nodeTypes.get `  
` compute.nodeTypes.list `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.nodeGroups.addNodes `  
` compute.nodeGroups.create `  
` compute.nodeGroups.delete `  
` compute.nodeGroups.deleteNodes `  
` compute.nodeGroups.get `  
` compute.nodeGroups.list `  
` compute.nodeGroups.setNodeTemplate `  
` compute.nodeTemplates.create `  
` compute.nodeTemplates.delete `  
` compute.nodeTemplates.get `  
` compute.nodeTemplates.list `  
` compute.nodeTypes.get `  
` compute.nodeTypes.list `  
  
  
##  2018-05-11 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
BigQuery  |  カスタムの役割でサポート  |  ` bigquery.jobs.listAll `  
  
Cloud Bigtable  |  カスタムの役割でサポート  |  ` bigtable.appProfiles.create `  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.clusters.create `  
` bigtable.clusters.delete `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Bigtable  |  一般提供開始  |  ` bigtable.appProfiles.create `  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Composer  |  現在ベータ版  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Life Sciences  |  カスタムの役割でサポート  |  ` genomics.operations.cancel `  
` genomics.operations.create `  
` genomics.operations.get `  
` genomics.operations.list `  
  
Cloud Monitoring  |  カスタムの役割でサポート  |  ` monitoring.dashboards.create `  
` monitoring.dashboards.delete `  
` monitoring.dashboards.get `  
` monitoring.dashboards.list `  
` monitoring.dashboards.update `  
` monitoring.publicWidgets.create `  
` monitoring.publicWidgets.delete `  
` monitoring.publicWidgets.get `  
` monitoring.publicWidgets.list `  
` monitoring.publicWidgets.update `  
` monitoring.uptimeCheckConfigs.create `  
` monitoring.uptimeCheckConfigs.delete `  
` monitoring.uptimeCheckConfigs.get `  
` monitoring.uptimeCheckConfigs.list `  
` monitoring.uptimeCheckConfigs.update `  
  
Cloud Monitoring  |  一般提供開始  |  ` monitoring.dashboards.create `  
` monitoring.dashboards.delete `  
` monitoring.dashboards.get `  
` monitoring.dashboards.list `  
` monitoring.dashboards.update `  
` monitoring.publicWidgets.create `  
` monitoring.publicWidgets.delete `  
` monitoring.publicWidgets.get `  
` monitoring.publicWidgets.list `  
` monitoring.publicWidgets.update `  
  
  
##  2018-05-04 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
BigQuery  |  カスタムの役割で使用可能  |  ` bigquery.jobs.listAll `  
  
Cloud Bigtable  |  追加  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  カスタムの役割でサポート  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  一般提供開始  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  一般提供開始  |  ` compute.oslogin.updateExternalUser `  
  
サービス管理  |  カスタムの役割でサポート  |  ` servicemanagement.services.bind `  
  
  
##  2018-04-06 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  カスタムの役割でサポート  |  `
compute.instances.setShieldedVmIntegrityPolicy `  
` compute.instances.updateShieldedVmConfig `  
  
Compute Engine  |  一般提供開始  |  ` compute.instances.setShieldedVmIntegrityPolicy
`  
  
Google Kubernetes Engine  |  カスタムの役割でサポート  |  ` container.hostServiceAgent.use
`  
  
Dataproc  |  カスタムの役割でサポート  |  ` dataproc.jobs.getIamPolicy `  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
Dataproc  |  一般提供開始  |  ` dataproc.jobs.getIamPolicy `  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
  
##  2018-03-30 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud IoT  |  一般提供開始  |  ` cloudiot.devices.create `  
` cloudiot.devices.delete `  
` cloudiot.devices.get `  
` cloudiot.devices.list `  
` cloudiot.devices.update `  
` cloudiot.devices.updateConfig `  
` cloudiot.registries.create `  
` cloudiot.registries.delete `  
` cloudiot.registries.get `  
` cloudiot.registries.getIamPolicy `  
` cloudiot.registries.list `  
` cloudiot.registries.setIamPolicy `  
` cloudiot.registries.update `  
  
  
##  2018-03-23 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Life Sciences  |  カスタムの役割でサポート  |  ` genomics.datasets.create `  
` genomics.datasets.delete `  
` genomics.datasets.get `  
` genomics.datasets.getIamPolicy `  
` genomics.datasets.list `  
` genomics.datasets.setIamPolicy `  
` genomics.datasets.update `  
  
Pub/Sub  |  カスタムの役割でサポート  |  ` pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.list `  
  
  
##  2018-03-09 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Talent Solution  |  追加  |  ` cloudjobdiscovery.companies.create `  
` cloudjobdiscovery.companies.delete `  
` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.companies.update `  
` cloudjobdiscovery.jobs.create `  
` cloudjobdiscovery.jobs.delete `  
` cloudjobdiscovery.jobs.deleteByFilter `  
` cloudjobdiscovery.jobs.get `  
` cloudjobdiscovery.jobs.search `  
` cloudjobdiscovery.jobs.update `  
` cloudjobdiscovery.tools.access `  
  
Talent Solution  |  カスタムの役割でサポート  |  ` cloudjobdiscovery.companies.create `  
` cloudjobdiscovery.companies.delete `  
` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.companies.update `  
` cloudjobdiscovery.jobs.create `  
` cloudjobdiscovery.jobs.delete `  
` cloudjobdiscovery.jobs.deleteByFilter `  
` cloudjobdiscovery.jobs.get `  
` cloudjobdiscovery.jobs.search `  
` cloudjobdiscovery.jobs.update `  
` cloudjobdiscovery.tools.access `  
  
Cloud Profiler  |  追加  |  ` cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
Cloud Profiler  |  カスタムの役割でサポート  |  ` cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
  
##  2018-03-02 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Open Service Broker for Google Cloud  |  追加  |  `
servicebroker.bindingoperations.get `  
` servicebroker.bindingoperations.list `  
` servicebroker.bindings.create `  
` servicebroker.bindings.delete `  
` servicebroker.bindings.get `  
` servicebroker.bindings.getIamPolicy `  
` servicebroker.bindings.list `  
` servicebroker.bindings.setIamPolicy `  
` servicebroker.catalogs.create `  
` servicebroker.catalogs.delete `  
` servicebroker.catalogs.get `  
` servicebroker.catalogs.getIamPolicy `  
` servicebroker.catalogs.list `  
` servicebroker.catalogs.setIamPolicy `  
` servicebroker.catalogs.validate `  
` servicebroker.instanceoperations.get `  
` servicebroker.instanceoperations.list `  
` servicebroker.instances.create `  
` servicebroker.instances.delete `  
` servicebroker.instances.get `  
` servicebroker.instances.getIamPolicy `  
` servicebroker.instances.list `  
` servicebroker.instances.setIamPolicy `  
` servicebroker.instances.update `  
  
Open Service Broker for Google Cloud  |  カスタムの役割でサポート  |  `
servicebroker.bindingoperations.get `  
` servicebroker.bindingoperations.list `  
` servicebroker.bindings.create `  
` servicebroker.bindings.delete `  
` servicebroker.bindings.get `  
` servicebroker.bindings.getIamPolicy `  
` servicebroker.bindings.list `  
` servicebroker.bindings.setIamPolicy `  
` servicebroker.catalogs.create `  
` servicebroker.catalogs.delete `  
` servicebroker.catalogs.get `  
` servicebroker.catalogs.getIamPolicy `  
` servicebroker.catalogs.list `  
` servicebroker.catalogs.setIamPolicy `  
` servicebroker.catalogs.validate `  
` servicebroker.instanceoperations.get `  
` servicebroker.instanceoperations.list `  
` servicebroker.instances.create `  
` servicebroker.instances.delete `  
` servicebroker.instances.get `  
` servicebroker.instances.getIamPolicy `  
` servicebroker.instances.list `  
` servicebroker.instances.setIamPolicy `  
` servicebroker.instances.update `  
  
  
##  2018-02-23 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Resource Manager  |  カスタムの役割でサポート  |  ` resourcemanager.projects.list `  
` resourcemanager.projects.move `  
  
サービス管理  |  追加  |  ` servicemanagement.services.quota `  
  
サービス管理  |  カスタムの役割でサポート  |  ` servicemanagement.services.quota `  
  
Cloud ソース レポジトリ  |  カスタムの役割でサポート  |  ` source.repos.create `  
  
  
##  2018-02-16 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
BigQuery  |  カスタムの役割でサポート  |  ` bigquery.tables.update `  
` bigquery.tables.updateData `  
  
Cloud IoT  |  カスタムの役割でサポート  |  ` cloudiot.devices.create `  
` cloudiot.devices.delete `  
` cloudiot.devices.get `  
` cloudiot.devices.list `  
` cloudiot.devices.update `  
` cloudiot.devices.updateConfig `  
` cloudiot.registries.create `  
` cloudiot.registries.delete `  
` cloudiot.registries.get `  
` cloudiot.registries.getIamPolicy `  
` cloudiot.registries.list `  
` cloudiot.registries.setIamPolicy `  
` cloudiot.registries.update `  
  
Cloud SQL  |  カスタムの役割でサポート  |  ` cloudsql.instances.demoteMaster `  
  
Google Cloud サポート  |  追加  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Compute Engine  |  追加  |  ` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.addresses.create `  
` compute.disks.create `  
` compute.disks.setLabels `  
` compute.forwardingRules.create `  
` compute.globalAddresses.create `  
` compute.globalForwardingRules.create `  
` compute.images.create `  
` compute.images.setLabels `  
` compute.snapshots.create `  
` compute.snapshots.setLabels `  
` compute.targetVpnGateways.create `  
` compute.vpnTunnels.create `  
  
Dataproc  |  カスタムの役割でサポート  |  ` dataproc.agents.create `  
` dataproc.agents.delete `  
` dataproc.agents.get `  
` dataproc.agents.list `  
` dataproc.agents.update `  
` dataproc.tasks.lease `  
` dataproc.tasks.listInvalidatedLeases `  
` dataproc.tasks.reportStatus `  
` dataproc.workflowTemplates.instantiateInline `  
  
Cloud DNS  |  追加  |  ` dns.changes.create `  
` dns.changes.get `  
` dns.changes.list `  
` dns.dnsKeys.create `  
` dns.dnsKeys.delete `  
` dns.dnsKeys.get `  
` dns.dnsKeys.list `  
` dns.dnsKeys.update `  
` dns.managedZoneOperations.get `  
` dns.managedZoneOperations.list `  
` dns.managedZones.create `  
` dns.managedZones.delete `  
` dns.managedZones.get `  
` dns.managedZones.list `  
` dns.managedZones.update `  
` dns.projects.get `  
` dns.resourceRecordSets.create `  
` dns.resourceRecordSets.delete `  
` dns.resourceRecordSets.get `  
` dns.resourceRecordSets.list `  
` dns.resourceRecordSets.update `  
  
  
##  2018-02-02 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  カスタムの役割で使用可能  |  ` compute.interconnectAttachments.create `  
` compute.interconnectAttachments.delete `  
` compute.interconnectAttachments.get `  
` compute.interconnectAttachments.list `  
` compute.interconnectAttachments.setLabels `  
` compute.interconnectAttachments.update `  
` compute.interconnectAttachments.use `  
` compute.interconnectLocations.get `  
` compute.interconnectLocations.list `  
` compute.interconnects.create `  
` compute.interconnects.delete `  
` compute.interconnects.get `  
` compute.interconnects.list `  
` compute.interconnects.setLabels `  
` compute.interconnects.update `  
` compute.interconnects.use `  
  
Cloud Data Loss Prevention  |  追加  |  ` dlp.jobTriggers.create `  
` dlp.jobTriggers.delete `  
` dlp.jobTriggers.get `  
` dlp.jobTriggers.list `  
` dlp.jobTriggers.update `  
  
  
##  2018-01-26 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
BigQuery  |  追加  |  ` bigquery.jobs.listAll `  
  
Google Kubernetes Engine  |  追加  |  ` container.podSecurityPolicies.create `  
` container.podSecurityPolicies.delete `  
` container.podSecurityPolicies.get `  
` container.podSecurityPolicies.list `  
` container.podSecurityPolicies.update `  
` container.podSecurityPolicies.use `  
  
  
##  2018-01-19 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  追加  |  ` compute.addresses.createInternal `  
` compute.addresses.deleteInternal `  
` compute.addresses.useInternal `  
  
  
##  2018-01-12 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
App Engine  |  カスタムの役割でサポートされない  |  ` appengine.runtimes.actAsAdmin `  
  
Compute Engine  |  追加  |  ` compute.backendServices.setSecurityPolicy `  
` compute.securityPolicies.create `  
` compute.securityPolicies.delete `  
` compute.securityPolicies.get `  
` compute.securityPolicies.getIamPolicy `  
` compute.securityPolicies.list `  
` compute.securityPolicies.setIamPolicy `  
` compute.securityPolicies.update `  
` compute.securityPolicies.use `  
  
Compute Engine  |  カスタムの役割でサポートされない  |  ` compute.organizations.administerXpn
`  
` compute.targetHttpProxies.create `  
` compute.targetHttpProxies.setUrlMap `  
` compute.targetHttpsProxies.create `  
` compute.targetHttpsProxies.setUrlMap `  
` compute.targetSslProxies.create `  
` compute.targetSslProxies.setBackendService `  
` compute.targetTcpProxies.create `  
` compute.targetTcpProxies.update `  
  
Compute Engine  |  一般提供開始  |  ` compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
  
  
##  2017-12-22 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
App Engine  |  カスタムの役割でサポート  |  ` appengine.applications.create `  
` appengine.applications.get `  
` appengine.applications.update `  
` appengine.instances.delete `  
` appengine.instances.get `  
` appengine.instances.list `  
` appengine.operations.get `  
` appengine.operations.list `  
` appengine.services.delete `  
` appengine.services.get `  
` appengine.services.list `  
` appengine.services.update `  
` appengine.versions.create `  
` appengine.versions.delete `  
` appengine.versions.get `  
` appengine.versions.list `  
` appengine.versions.update `  
  
App Engine  |  カスタムの役割でサポートされない  |  ` appengine.applications.list `  
` appengine.operations.cancel `  
` appengine.operations.delete `  
` appengine.services.create `  
  
クラウドのお支払いとご請求  |  カスタムの役割でサポート  |  ` billing.accounts.close `  
` billing.accounts.reopen `  
` billing.budgets.delete `  
` billing.budgets.update `  
  
Cloud デバッガ  |  カスタムの役割でサポート  |  ` clouddebugger.breakpoints.create `  
` clouddebugger.breakpoints.delete `  
` clouddebugger.breakpoints.get `  
` clouddebugger.breakpoints.list `  
` clouddebugger.breakpoints.listActive `  
` clouddebugger.breakpoints.update `  
` clouddebugger.debuggees.create `  
` clouddebugger.debuggees.list `  
  
Cloud Key Management Service  |  カスタムの役割でサポート  |  `
cloudkms.cryptoKeyVersions.create `  
` cloudkms.cryptoKeyVersions.destroy `  
` cloudkms.cryptoKeyVersions.get `  
` cloudkms.cryptoKeyVersions.list `  
` cloudkms.cryptoKeyVersions.restore `  
` cloudkms.cryptoKeyVersions.update `  
` cloudkms.cryptoKeyVersions.useToDecrypt `  
` cloudkms.cryptoKeyVersions.useToEncrypt `  
` cloudkms.cryptoKeys.create `  
` cloudkms.cryptoKeys.get `  
` cloudkms.cryptoKeys.getIamPolicy `  
` cloudkms.cryptoKeys.list `  
` cloudkms.cryptoKeys.setIamPolicy `  
` cloudkms.cryptoKeys.update `  
` cloudkms.keyRings.create `  
` cloudkms.keyRings.get `  
` cloudkms.keyRings.getIamPolicy `  
` cloudkms.keyRings.list `  
` cloudkms.keyRings.setIamPolicy `  
  
Cloud SQL  |  カスタムの役割でサポート  |  ` cloudsql.backupRuns.create `  
` cloudsql.backupRuns.delete `  
` cloudsql.backupRuns.get `  
` cloudsql.backupRuns.list `  
` cloudsql.databases.create `  
` cloudsql.databases.delete `  
` cloudsql.databases.get `  
` cloudsql.databases.list `  
` cloudsql.databases.update `  
` cloudsql.instances.clone `  
` cloudsql.instances.connect `  
` cloudsql.instances.create `  
` cloudsql.instances.delete `  
` cloudsql.instances.export `  
` cloudsql.instances.failover `  
` cloudsql.instances.get `  
` cloudsql.instances.import `  
` cloudsql.instances.list `  
` cloudsql.instances.promoteReplica `  
` cloudsql.instances.resetSslConfig `  
` cloudsql.instances.restart `  
` cloudsql.instances.restoreBackup `  
` cloudsql.instances.startReplica `  
` cloudsql.instances.stopReplica `  
` cloudsql.instances.truncateLog `  
` cloudsql.instances.update `  
` cloudsql.sslCerts.create `  
` cloudsql.sslCerts.delete `  
` cloudsql.sslCerts.get `  
` cloudsql.sslCerts.list `  
` cloudsql.users.create `  
` cloudsql.users.delete `  
` cloudsql.users.list `  
` cloudsql.users.update `  
  
Cloud SQL  |  カスタムの役割でサポートされない  |  ` cloudsql.databases.getIamPolicy `  
` cloudsql.databases.setIamPolicy `  
` cloudsql.instances.demoteMaster `  
` cloudsql.instances.getIamPolicy `  
` cloudsql.instances.migrate `  
` cloudsql.instances.setIamPolicy `  
` cloudsql.sslCerts.createEphemeral `  
  
Cloud Trace  |  カスタムの役割でサポート  |  ` cloudtrace.insights.get `  
` cloudtrace.insights.list `  
` cloudtrace.stats.get `  
` cloudtrace.tasks.create `  
` cloudtrace.tasks.delete `  
` cloudtrace.tasks.get `  
` cloudtrace.tasks.list `  
` cloudtrace.traces.get `  
` cloudtrace.traces.list `  
` cloudtrace.traces.patch `  
  
Compute Engine  |  追加  |  ` compute.instances.setMachineResources `  
` compute.instances.setMinCpuPlatform `  
` compute.instances.setServiceAccount `  
` compute.instances.updateAccessConfig `  
` compute.instances.updateNetworkInterface `  
` compute.licenseCodes.get `  
` compute.licenseCodes.list `  
` compute.licenseCodes.update `  
` compute.licenseCodes.use `  
  
Compute Engine  |  カスタムの役割でサポート  |  ` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
` compute.addresses.delete `  
` compute.addresses.get `  
` compute.addresses.list `  
` compute.addresses.use `  
` compute.autoscalers.create `  
` compute.autoscalers.delete `  
` compute.autoscalers.get `  
` compute.autoscalers.list `  
` compute.autoscalers.update `  
` compute.backendBuckets.create `  
` compute.backendBuckets.delete `  
` compute.backendBuckets.get `  
` compute.backendBuckets.list `  
` compute.backendBuckets.update `  
` compute.commitments.list `  
` compute.diskTypes.get `  
` compute.diskTypes.list `  
` compute.disks.createSnapshot `  
` compute.disks.delete `  
` compute.disks.get `  
` compute.disks.list `  
` compute.disks.resize `  
` compute.disks.update `  
` compute.disks.use `  
` compute.disks.useReadOnly `  
` compute.firewalls.create `  
` compute.firewalls.delete `  
` compute.firewalls.get `  
` compute.firewalls.list `  
` compute.firewalls.update `  
` compute.forwardingRules.delete `  
` compute.forwardingRules.get `  
` compute.forwardingRules.list `  
` compute.forwardingRules.setTarget `  
` compute.globalAddresses.delete `  
` compute.globalAddresses.get `  
` compute.globalAddresses.list `  
` compute.globalAddresses.use `  
` compute.globalForwardingRules.delete `  
` compute.globalForwardingRules.get `  
` compute.globalForwardingRules.list `  
` compute.globalOperations.delete `  
` compute.globalOperations.get `  
` compute.globalOperations.list `  
` compute.httpHealthChecks.create `  
` compute.httpHealthChecks.delete `  
` compute.httpHealthChecks.get `  
` compute.httpHealthChecks.list `  
` compute.httpHealthChecks.update `  
` compute.httpHealthChecks.useReadOnly `  
` compute.httpsHealthChecks.create `  
` compute.httpsHealthChecks.delete `  
` compute.httpsHealthChecks.get `  
` compute.httpsHealthChecks.list `  
` compute.httpsHealthChecks.update `  
` compute.httpsHealthChecks.useReadOnly `  
` compute.images.delete `  
` compute.images.deprecate `  
` compute.images.get `  
` compute.images.getFromFamily `  
` compute.images.list `  
` compute.instanceGroupManagers.create `  
` compute.instanceGroupManagers.delete `  
` compute.instanceGroupManagers.get `  
` compute.instanceGroupManagers.list `  
` compute.instanceGroupManagers.update `  
` compute.instanceGroupManagers.use `  
` compute.instanceGroups.create `  
` compute.instanceGroups.delete `  
` compute.instanceGroups.get `  
` compute.instanceGroups.list `  
` compute.instanceGroups.update `  
` compute.instanceTemplates.create `  
` compute.instanceTemplates.delete `  
` compute.instanceTemplates.get `  
` compute.instanceTemplates.list `  
` compute.instanceTemplates.useReadOnly `  
` compute.instances.addAccessConfig `  
` compute.instances.attachDisk `  
` compute.instances.create `  
` compute.instances.delete `  
` compute.instances.deleteAccessConfig `  
` compute.instances.detachDisk `  
` compute.instances.get `  
` compute.instances.getSerialPortOutput `  
` compute.instances.list `  
` compute.instances.listReferrers `  
` compute.instances.reset `  
` compute.instances.setDiskAutoDelete `  
` compute.instances.setLabels `  
` compute.instances.setMachineType `  
` compute.instances.setMetadata `  
` compute.instances.setScheduling `  
` compute.instances.setTags `  
` compute.instances.start `  
` compute.instances.stop `  
` compute.instances.use `  
` compute.machineTypes.get `  
` compute.machineTypes.list `  
` compute.networks.create `  
` compute.networks.delete `  
` compute.networks.get `  
` compute.networks.list `  
` compute.networks.updatePolicy `  
` compute.organizations.disableXpnHost `  
` compute.organizations.disableXpnResource `  
` compute.organizations.enableXpnHost `  
` compute.organizations.enableXpnResource `  
` compute.projects.get `  
` compute.projects.setCommonInstanceMetadata `  
` compute.projects.setUsageExportBucket `  
` compute.regionOperations.delete `  
` compute.regionOperations.get `  
` compute.regionOperations.list `  
` compute.regions.get `  
` compute.regions.list `  
` compute.routers.create `  
` compute.routers.delete `  
` compute.routers.get `  
` compute.routers.list `  
` compute.routers.update `  
` compute.routers.use `  
` compute.routes.create `  
` compute.routes.delete `  
` compute.routes.get `  
` compute.routes.list `  
` compute.snapshots.delete `  
` compute.snapshots.get `  
` compute.snapshots.list `  
` compute.snapshots.useReadOnly `  
` compute.sslCertificates.create `  
` compute.sslCertificates.delete `  
` compute.sslCertificates.get `  
` compute.sslCertificates.list `  
` compute.subnetworks.use `  
` compute.subnetworks.useExternalIp `  
` compute.targetHttpProxies.create `  
` compute.targetHttpProxies.delete `  
` compute.targetHttpProxies.get `  
` compute.targetHttpProxies.list `  
` compute.targetHttpProxies.setUrlMap `  
` compute.targetHttpProxies.use `  
` compute.targetHttpsProxies.create `  
` compute.targetHttpsProxies.delete `  
` compute.targetHttpsProxies.get `  
` compute.targetHttpsProxies.list `  
` compute.targetHttpsProxies.setSslCertificates `  
` compute.targetHttpsProxies.setUrlMap `  
` compute.targetHttpsProxies.use `  
` compute.targetInstances.create `  
` compute.targetInstances.delete `  
` compute.targetInstances.get `  
` compute.targetInstances.list `  
` compute.targetInstances.use `  
` compute.targetPools.addHealthCheck `  
` compute.targetPools.addInstance `  
` compute.targetPools.create `  
` compute.targetPools.delete `  
` compute.targetPools.get `  
` compute.targetPools.list `  
` compute.targetPools.removeHealthCheck `  
` compute.targetPools.removeInstance `  
` compute.targetPools.update `  
` compute.targetPools.use `  
` compute.targetSslProxies.create `  
` compute.targetSslProxies.delete `  
` compute.targetSslProxies.get `  
` compute.targetSslProxies.list `  
` compute.targetSslProxies.setBackendService `  
` compute.targetSslProxies.setProxyHeader `  
` compute.targetSslProxies.setSslCertificates `  
` compute.targetSslProxies.use `  
` compute.targetTcpProxies.create `  
` compute.targetTcpProxies.delete `  
` compute.targetTcpProxies.get `  
` compute.targetTcpProxies.list `  
` compute.targetTcpProxies.update `  
` compute.targetTcpProxies.use `  
` compute.targetVpnGateways.delete `  
` compute.targetVpnGateways.get `  
` compute.targetVpnGateways.list `  
` compute.targetVpnGateways.use `  
` compute.vpnTunnels.delete `  
` compute.vpnTunnels.get `  
` compute.vpnTunnels.list `  
` compute.zoneOperations.delete `  
` compute.zoneOperations.get `  
` compute.zoneOperations.list `  
` compute.zones.get `  
` compute.zones.list `  
  
Compute Engine  |  カスタムの役割でサポートされない  |  ` compute.backendServices.create `  
` compute.backendServices.delete `  
` compute.backendServices.get `  
` compute.backendServices.list `  
` compute.backendServices.update `  
` compute.backendServices.use `  
` compute.healthChecks.create `  
` compute.healthChecks.delete `  
` compute.healthChecks.get `  
` compute.healthChecks.list `  
` compute.healthChecks.update `  
` compute.healthChecks.use `  
` compute.healthChecks.useReadOnly `  
` compute.interconnectAttachments.create `  
` compute.interconnectAttachments.delete `  
` compute.interconnectAttachments.get `  
` compute.interconnectAttachments.list `  
` compute.interconnectAttachments.setLabels `  
` compute.interconnectAttachments.update `  
` compute.interconnectAttachments.use `  
` compute.interconnectLocations.get `  
` compute.interconnectLocations.list `  
` compute.interconnects.create `  
` compute.interconnects.delete `  
` compute.interconnects.get `  
` compute.interconnects.list `  
` compute.interconnects.setLabels `  
` compute.interconnects.update `  
` compute.interconnects.use `  
` compute.urlMaps.create `  
` compute.urlMaps.delete `  
` compute.urlMaps.get `  
` compute.urlMaps.invalidateCache `  
` compute.urlMaps.list `  
` compute.urlMaps.update `  
` compute.urlMaps.use `  
` compute.urlMaps.validate `  
  
Google Kubernetes Engine  |  追加  |  ` container.services.updateStatus `  
  
Google Kubernetes Engine  |  カスタムの役割でサポート  |  ` container.clusters.create `  
` container.clusters.delete `  
` container.clusters.get `  
` container.clusters.getCredentials `  
` container.clusters.list `  
` container.clusters.update `  
` container.operations.get `  
` container.operations.list `  
  
Dataproc  |  カスタムの役割でサポート  |  ` dataproc.clusters.create `  
` dataproc.clusters.delete `  
` dataproc.clusters.get `  
` dataproc.clusters.getIamPolicy `  
` dataproc.clusters.list `  
` dataproc.clusters.setIamPolicy `  
` dataproc.clusters.update `  
` dataproc.clusters.use `  
` dataproc.jobs.cancel `  
` dataproc.jobs.create `  
` dataproc.jobs.delete `  
` dataproc.jobs.get `  
` dataproc.jobs.list `  
` dataproc.jobs.update `  
` dataproc.operations.cancel `  
` dataproc.operations.delete `  
` dataproc.operations.get `  
` dataproc.operations.list `  
` dataproc.workflowTemplates.create `  
` dataproc.workflowTemplates.delete `  
` dataproc.workflowTemplates.get `  
` dataproc.workflowTemplates.instantiate `  
` dataproc.workflowTemplates.list `  
` dataproc.workflowTemplates.update `  
  
データストア  |  カスタムの役割でサポートされない  |  ` datastore.databases.create `  
` datastore.databases.delete `  
` datastore.databases.export `  
` datastore.databases.get `  
` datastore.databases.getIamPolicy `  
` datastore.databases.import `  
` datastore.databases.list `  
` datastore.databases.setIamPolicy `  
` datastore.databases.update `  
` datastore.entities.allocateIds `  
` datastore.entities.create `  
` datastore.entities.delete `  
` datastore.entities.get `  
` datastore.entities.list `  
` datastore.entities.update `  
` datastore.indexes.create `  
` datastore.indexes.delete `  
` datastore.indexes.get `  
` datastore.indexes.list `  
` datastore.indexes.update `  
` datastore.namespaces.get `  
` datastore.namespaces.getIamPolicy `  
` datastore.namespaces.list `  
` datastore.namespaces.setIamPolicy `  
` datastore.operations.cancel `  
` datastore.operations.delete `  
` datastore.operations.get `  
` datastore.operations.list `  
` datastore.statistics.get `  
` datastore.statistics.list `  
  
Cloud Deployment Manager  |  カスタムの役割でサポート  |  `
deploymentmanager.compositeTypes.create `  
` deploymentmanager.compositeTypes.delete `  
` deploymentmanager.compositeTypes.get `  
` deploymentmanager.compositeTypes.list `  
` deploymentmanager.compositeTypes.update `  
` deploymentmanager.deployments.cancelPreview `  
` deploymentmanager.deployments.create `  
` deploymentmanager.deployments.delete `  
` deploymentmanager.deployments.get `  
` deploymentmanager.deployments.getIamPolicy `  
` deploymentmanager.deployments.list `  
` deploymentmanager.deployments.setIamPolicy `  
` deploymentmanager.deployments.stop `  
` deploymentmanager.deployments.update `  
` deploymentmanager.manifests.get `  
` deploymentmanager.manifests.list `  
` deploymentmanager.operations.get `  
` deploymentmanager.operations.list `  
` deploymentmanager.resources.get `  
` deploymentmanager.resources.list `  
` deploymentmanager.typeProviders.create `  
` deploymentmanager.typeProviders.delete `  
` deploymentmanager.typeProviders.get `  
` deploymentmanager.typeProviders.list `  
` deploymentmanager.typeProviders.update `  
` deploymentmanager.types.list `  
  
Dialogflow  |  カスタムの役割でサポート  |  ` dialogflow.agents.export `  
` dialogflow.agents.get `  
` dialogflow.agents.import `  
` dialogflow.agents.restore `  
` dialogflow.contexts.create `  
` dialogflow.contexts.delete `  
` dialogflow.contexts.get `  
` dialogflow.contexts.list `  
` dialogflow.contexts.update `  
` dialogflow.entityTypes.create `  
` dialogflow.entityTypes.createEntity `  
` dialogflow.entityTypes.delete `  
` dialogflow.entityTypes.deleteEntity `  
` dialogflow.entityTypes.get `  
` dialogflow.entityTypes.list `  
` dialogflow.entityTypes.update `  
` dialogflow.entityTypes.updateEntity `  
` dialogflow.intents.create `  
` dialogflow.intents.delete `  
` dialogflow.intents.get `  
` dialogflow.intents.list `  
` dialogflow.intents.update `  
` dialogflow.operations.get `  
` dialogflow.sessionEntityTypes.create `  
` dialogflow.sessionEntityTypes.delete `  
` dialogflow.sessionEntityTypes.get `  
` dialogflow.sessionEntityTypes.list `  
` dialogflow.sessionEntityTypes.update `  
` dialogflow.sessions.detectIntent `  
` dialogflow.sessions.streamingDetectIntent `  
  
エラーレポート  |  カスタムの役割でサポート  |  ` errorreporting.applications.list `  
` errorreporting.errorEvents.create `  
` errorreporting.errorEvents.delete `  
` errorreporting.errorEvents.list `  
` errorreporting.groupMetadata.get `  
` errorreporting.groupMetadata.update `  
` errorreporting.groups.list `  
  
Cloud Identity and Access Management  |  カスタムの役割でサポートされない  |  `
iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
Cloud Logging  |  カスタムの役割でサポート  |  ` logging.exclusions.create `  
` logging.exclusions.delete `  
` logging.exclusions.get `  
` logging.exclusions.list `  
` logging.exclusions.update `  
` logging.logEntries.create `  
` logging.logEntries.list `  
` logging.logMetrics.create `  
` logging.logMetrics.delete `  
` logging.logMetrics.get `  
` logging.logMetrics.list `  
` logging.logMetrics.update `  
` logging.logServiceIndexes.list `  
` logging.logServices.list `  
` logging.logs.delete `  
` logging.logs.list `  
` logging.privateLogEntries.list `  
` logging.sinks.create `  
` logging.sinks.delete `  
` logging.sinks.get `  
` logging.sinks.list `  
` logging.sinks.update `  
` logging.usage.get `  
  
AI Platform  |  カスタムの役割でサポート  |  ` ml.jobs.cancel `  
` ml.jobs.create `  
` ml.jobs.get `  
` ml.jobs.getIamPolicy `  
` ml.jobs.list `  
` ml.jobs.setIamPolicy `  
` ml.jobs.update `  
` ml.locations.get `  
` ml.locations.list `  
` ml.models.create `  
` ml.models.delete `  
` ml.models.get `  
` ml.models.getIamPolicy `  
` ml.models.list `  
` ml.models.predict `  
` ml.models.setIamPolicy `  
` ml.models.update `  
` ml.operations.cancel `  
` ml.operations.get `  
` ml.operations.list `  
` ml.projects.getConfig `  
` ml.versions.create `  
` ml.versions.delete `  
` ml.versions.get `  
` ml.versions.list `  
` ml.versions.predict `  
` ml.versions.update `  
  
Cloud Monitoring  |  カスタムの役割でサポート  |  ` monitoring.groups.create `  
` monitoring.groups.delete `  
` monitoring.groups.get `  
` monitoring.groups.list `  
` monitoring.groups.update `  
` monitoring.metricDescriptors.create `  
` monitoring.metricDescriptors.delete `  
` monitoring.metricDescriptors.get `  
` monitoring.metricDescriptors.list `  
` monitoring.monitoredResourceDescriptors.get `  
` monitoring.monitoredResourceDescriptors.list `  
` monitoring.timeSeries.create `  
` monitoring.timeSeries.list `  
  
Pub/Sub  |  カスタムの役割でサポート  |  ` pubsub.topics.setIamPolicy `  
  
サービス管理  |  カスタムの役割でサポート  |  ` servicemanagement.services.check `  
` servicemanagement.services.report `  
  
サービス管理  |  カスタムの役割でサポートされない  |  ` servicemanagement.consumerSettings.get `  
` servicemanagement.consumerSettings.getIamPolicy `  
` servicemanagement.consumerSettings.list `  
` servicemanagement.consumerSettings.setIamPolicy `  
` servicemanagement.consumerSettings.update `  
  
Cloud ソース レポジトリ  |  カスタムの役割でサポート  |  ` source.repos.delete `  
` source.repos.get `  
` source.repos.getIamPolicy `  
` source.repos.list `  
` source.repos.setIamPolicy `  
  
Cloud ソース レポジトリ  |  カスタムの役割でサポートされない  |  ` source.repos.update `  
  
Cloud Spanner  |  カスタムの役割でサポート  |  ` spanner.databaseOperations.cancel `  
` spanner.databaseOperations.get `  
` spanner.databaseOperations.list `  
` spanner.databases.beginOrRollbackReadWriteTransaction `  
` spanner.databases.beginReadOnlyTransaction `  
` spanner.databases.create `  
` spanner.databases.drop `  
` spanner.databases.get `  
` spanner.databases.getDdl `  
` spanner.databases.getIamPolicy `  
` spanner.databases.list `  
` spanner.databases.read `  
` spanner.databases.select `  
` spanner.databases.setIamPolicy `  
` spanner.databases.updateDdl `  
` spanner.databases.write `  
` spanner.instanceConfigs.get `  
` spanner.instanceConfigs.list `  
` spanner.instanceOperations.cancel `  
` spanner.instanceOperations.delete `  
` spanner.instanceOperations.get `  
` spanner.instanceOperations.list `  
` spanner.instances.create `  
` spanner.instances.delete `  
` spanner.instances.get `  
` spanner.instances.getIamPolicy `  
` spanner.instances.list `  
` spanner.instances.setIamPolicy `  
` spanner.instances.update `  
` spanner.sessions.create `  
` spanner.sessions.delete `  
` spanner.sessions.get `  
` spanner.sessions.list `  
  
Cloud Spanner  |  カスタムの役割でサポートされない  |  ` spanner.databaseOperations.delete `  
` spanner.databases.update `  
  
クラウド ストレージ  |  カスタムの役割でサポート  |  ` storage.buckets.create `  
` storage.buckets.delete `  
` storage.buckets.get `  
` storage.buckets.getIamPolicy `  
` storage.buckets.list `  
` storage.buckets.setIamPolicy `  
` storage.buckets.update `  
` storage.objects.create `  
` storage.objects.delete `  
` storage.objects.get `  
` storage.objects.getIamPolicy `  
` storage.objects.list `  
` storage.objects.setIamPolicy `  
` storage.objects.update `  
  
  
##  2017-12-08 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
BigQuery  |  カスタムの役割でサポート  |  ` bigquery.datasets.create `  
` bigquery.datasets.delete `  
` bigquery.datasets.get `  
` bigquery.datasets.update `  
` bigquery.jobs.create `  
` bigquery.jobs.get `  
` bigquery.jobs.list `  
` bigquery.jobs.update `  
` bigquery.savedqueries.create `  
` bigquery.savedqueries.delete `  
` bigquery.savedqueries.get `  
` bigquery.savedqueries.list `  
` bigquery.savedqueries.update `  
` bigquery.tables.create `  
` bigquery.tables.delete `  
` bigquery.tables.export `  
` bigquery.tables.get `  
` bigquery.tables.getData `  
` bigquery.tables.list `  
  
BigQuery  |  カスタムの役割でサポートされない  |  ` bigquery.config.get `  
` bigquery.config.update `  
` bigquery.service.actAsSuperuser `  
` bigquery.tables.update `  
` bigquery.tables.updateData `  
` bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Cloud Bigtable  |  カスタムの役割でサポート  |  ` bigtable.clusters.get `  
` bigtable.clusters.list `  
` bigtable.clusters.update `  
` bigtable.instances.create `  
` bigtable.instances.delete `  
` bigtable.instances.get `  
` bigtable.instances.list `  
` bigtable.instances.update `  
` bigtable.tables.create `  
` bigtable.tables.delete `  
` bigtable.tables.get `  
` bigtable.tables.list `  
` bigtable.tables.mutateRows `  
` bigtable.tables.readRows `  
` bigtable.tables.sampleRowKeys `  
` bigtable.tables.update `  
  
Compute Engine  |  追加  |  ` compute.disks.getIamPolicy `  
` compute.disks.setIamPolicy `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.setIamPolicy `  
` compute.images.getIamPolicy `  
` compute.images.setIamPolicy `  
` compute.instances.getIamPolicy `  
` compute.instances.setIamPolicy `  
` compute.licenses.getIamPolicy `  
` compute.licenses.setIamPolicy `  
` compute.organizations.administerXpn `  
` compute.organizations.disableXpnHost `  
` compute.organizations.disableXpnResource `  
` compute.organizations.enableXpnHost `  
` compute.organizations.enableXpnResource `  
` compute.regionOperations.getIamPolicy `  
` compute.regionOperations.setIamPolicy `  
` compute.snapshots.getIamPolicy `  
` compute.snapshots.setIamPolicy `  
` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
` compute.zoneOperations.getIamPolicy `  
` compute.zoneOperations.setIamPolicy `  
  
Dataflow  |  カスタムの役割でサポート  |  ` dataflow.jobs.cancel `  
` dataflow.jobs.create `  
` dataflow.jobs.get `  
` dataflow.jobs.list `  
` dataflow.jobs.updateContents `  
` dataflow.messages.list `  
` dataflow.metrics.get `  
  
Dataproc  |  追加  |  ` dataproc.workflowTemplates.instantiateInline `  
  
Cloud Data Loss Prevention  |  追加  |  ` dlp.analyzeRiskTemplates.create `  
` dlp.analyzeRiskTemplates.delete `  
` dlp.analyzeRiskTemplates.get `  
` dlp.analyzeRiskTemplates.list `  
` dlp.analyzeRiskTemplates.update `  
` dlp.deidentifyTemplates.create `  
` dlp.deidentifyTemplates.delete `  
` dlp.deidentifyTemplates.get `  
` dlp.deidentifyTemplates.list `  
` dlp.deidentifyTemplates.update `  
` dlp.inspectTemplates.create `  
` dlp.inspectTemplates.delete `  
` dlp.inspectTemplates.get `  
` dlp.inspectTemplates.list `  
` dlp.inspectTemplates.update `  
` dlp.jobs.cancel `  
` dlp.jobs.create `  
` dlp.jobs.delete `  
` dlp.jobs.get `  
` dlp.jobs.list `  
  
Pub/Sub  |  追加  |  ` pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.get `  
` pubsub.snapshots.getIamPolicy `  
` pubsub.snapshots.list `  
` pubsub.snapshots.seek `  
` pubsub.snapshots.setIamPolicy `  
` pubsub.snapshots.update `  
  
Pub/Sub  |  カスタムの役割でサポート  |  ` pubsub.subscriptions.consume `  
` pubsub.subscriptions.create `  
` pubsub.subscriptions.delete `  
` pubsub.subscriptions.get `  
` pubsub.subscriptions.getIamPolicy `  
` pubsub.subscriptions.list `  
` pubsub.subscriptions.setIamPolicy `  
` pubsub.subscriptions.update `  
` pubsub.topics.attachSubscription `  
` pubsub.topics.create `  
` pubsub.topics.delete `  
` pubsub.topics.get `  
` pubsub.topics.getIamPolicy `  
` pubsub.topics.list `  
` pubsub.topics.publish `  
  
  
##  2017-12-01 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Build  |  カスタムの役割でサポート  |  ` cloudbuild.builds.create `  
` cloudbuild.builds.get `  
` cloudbuild.builds.list `  
` cloudbuild.builds.update `  
  
Cloud Tool Results  |  一般提供開始  |  ` cloudtoolresults.executions.create `  
` cloudtoolresults.executions.get `  
` cloudtoolresults.executions.list `  
` cloudtoolresults.executions.update `  
` cloudtoolresults.histories.create `  
` cloudtoolresults.histories.get `  
` cloudtoolresults.histories.list `  
` cloudtoolresults.settings.create `  
` cloudtoolresults.settings.get `  
` cloudtoolresults.settings.update `  
` cloudtoolresults.steps.create `  
` cloudtoolresults.steps.get `  
` cloudtoolresults.steps.list `  
` cloudtoolresults.steps.update `  
  
Compute Engine  |  一般提供開始  |  ` compute.instances.addMaintenancePolicies `  
` compute.instances.removeMaintenancePolicies `  
` compute.maintenancePolicies.create `  
` compute.maintenancePolicies.delete `  
` compute.maintenancePolicies.get `  
` compute.maintenancePolicies.getIamPolicy `  
` compute.maintenancePolicies.list `  
` compute.maintenancePolicies.setIamPolicy `  
` compute.maintenancePolicies.use `  
` compute.targetTcpProxies.create `  
` compute.targetTcpProxies.delete `  
` compute.targetTcpProxies.get `  
` compute.targetTcpProxies.getIamPolicy `  
` compute.targetTcpProxies.list `  
` compute.targetTcpProxies.setIamPolicy `  
` compute.targetTcpProxies.update `  
` compute.targetTcpProxies.use `  
  
Google Kubernetes Engine  |  追加  |  `
container.initializerConfigurations.create `  
` container.initializerConfigurations.delete `  
` container.initializerConfigurations.get `  
` container.initializerConfigurations.list `  
` container.initializerConfigurations.update `  
` container.pods.initialize `  
  
Google Kubernetes Engine  |  一般提供開始  |  ` container.deployments.getScale `  
` container.deployments.updateScale `  
  
Dataprep by Trifacta  |  カスタムの役割でサポート  |  ` dataprep.projects.use `  
  
Cloud Identity and Access Management  |  カスタムの役割でサポート  |  ` iam.roles.create `  
` iam.roles.delete `  
` iam.roles.get `  
` iam.roles.list `  
` iam.roles.undelete `  
` iam.roles.update `  
  
  
##  2017-11-10 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Google Kubernetes Engine  |  追加  |  ` container.clusters.getIamPolicy `  
` container.clusters.setIamPolicy `  
  
AI Platform  |  追加  |  ` ml.locations.get `  
` ml.locations.list `  
  
Cloud Monitoring  |  追加  |  ` monitoring.metricDescriptors.update `  
  
  
##  2017-10-27 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Compute Engine  |  追加  |  ` compute.instances.updateShieldedVmConfig `  
  
Identity-Aware Proxy  |  追加  |  ` iap.web.getIamPolicy `  
` iap.web.setIamPolicy `  
` iap.webServiceVersions.accessViaIAP `  
` iap.webServiceVersions.getIamPolicy `  
` iap.webServiceVersions.setIamPolicy `  
` iap.webServiceVersions.updateIAP `  
` iap.webServices.getIamPolicy `  
` iap.webServices.setIamPolicy `  
` iap.webServices.updateIAP `  
` iap.webTypes.getIamPolicy `  
` iap.webTypes.setIamPolicy `  
` iap.webTypes.updateIAP `  
  
サービス管理  |  カスタムの役割でサポート  |  ` servicemanagement.services.create `  
` servicemanagement.services.delete `  
` servicemanagement.services.get `  
` servicemanagement.services.getIamPolicy `  
` servicemanagement.services.list `  
` servicemanagement.services.setIamPolicy `  
` servicemanagement.services.update `  
  
  
##  2017-10-06 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Dataproc  |  一般提供開始  |  ` dataproc.workflowTemplates.create `  
` dataproc.workflowTemplates.delete `  
` dataproc.workflowTemplates.get `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.instantiate `  
` dataproc.workflowTemplates.list `  
` dataproc.workflowTemplates.setIamPolicy `  
` dataproc.workflowTemplates.update `  
  
  
##  2017-09-22 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
App Engine  |  追加  |  ` appengine.memcache.addKey `  
` appengine.memcache.flush `  
` appengine.memcache.get `  
` appengine.memcache.getKey `  
` appengine.memcache.list `  
` appengine.memcache.update `  
  
Cloud SQL  |  追加  |  ` cloudsql.instances.demoteMaster `  
  
Cloud SQL  |  一般提供開始  |  ` cloudsql.instances.demoteMaster `  
  
  
##  2017-09-08 現在の Cloud IAM 変更

サービス  |  変更  |  説明  
---|---|---  
Cloud Functions  |  追加  |  ` cloudfunctions.functions.call `  
` cloudfunctions.functions.create `  
` cloudfunctions.functions.delete `  
` cloudfunctions.functions.get `  
` cloudfunctions.functions.list `  
` cloudfunctions.functions.sourceCodeGet `  
` cloudfunctions.functions.sourceCodeSet `  
` cloudfunctions.functions.update `  
` cloudfunctions.locations.list `  
` cloudfunctions.operations.get `  
` cloudfunctions.operations.list `  
  
Compute Engine  |  追加  |  ` compute.instances.setDeletionProtection `  
` compute.targetHttpsProxies.setUrlMap `  
  
Google Kubernetes Engine  |  追加  |  ` container.statefulSets.getScale `  
` container.statefulSets.updateScale `  
  
Google Kubernetes Engine  |  一般提供開始  |  ` container.statefulSets.getScale `  
` container.statefulSets.updateScale `  
  
Cloud Functions  |  追加  |  ` dlp.kms.encrypt `  
` dlp.riskAnalysisOperations.cancel `  
` dlp.riskAnalysisOperations.create `  
` dlp.riskAnalysisOperations.get `  
` dlp.riskAnalysisOperations.list `  

