#  IAM 권한 변경 로그

이 페이지에서는 Google Cloud에서 일반 안정화 버전 서비스 및 베타 버전 서비스에 대한 퍼블릭 Cloud IAM 권한의 변경사항을
설명합니다. 이 변경 로그는 [ 커스텀 역할 ](https://cloud.google.com/iam/docs/understanding-
custom-roles?hl=ko) 을 유지관리하고 문제를 해결하는 데 유용합니다.

권한이 사용되지 않거나 커스텀 역할에서 더 이상 지원되지 않으면 Cloud IAM은 권한을 커스텀 역할에서 자동으로 삭제합니다. 하지만
권한을 추가하면 Cloud IAM이 권한을 커스텀 역할에 자동으로 추가하지 _않습니다_ .

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL을 다음과 같이 직접 추가하세요. ` https://cloud.google.com/feeds/cloud-iam-
permissions-change-log.xml `

IAM 권한 변경 로그

##  2020년 3월 2일이 속한 주에 예정된 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.networkAdmin ` (Compute 네트워크 관리자) 역할에 다음 권한이 추가되었습니다.

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.networkViewer ` (Compute Network 뷰어) 역할에 다음 권한이 추가되었습니다.

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
기본 역할  |  역할 업데이트됨  |

` roles/editor ` (편집자) 역할에 다음 권한이 추가되었습니다.

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
  
Cloud ID 및 액세스 관리  |  역할 업데이트됨  |

` roles/iam.securityAdmin ` (보안 관리자) 역할에 다음 권한이 추가되었습니다.

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
Cloud ID 및 액세스 관리  |  역할 업데이트됨  |

` roles/iam.securityReviewer ` (보안 검토자) 역할에 다음 권한이 추가되었습니다.

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
Identity Platform  |  역할 추가됨  |

` roles/identityplatform.admin ` (Identity Platform 관리자) 역할에 다음 권한이 추가되었습니다.

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
  
Identity Platform  |  역할 추가됨  |

` roles/identityplatform.viewer ` (Identity Platform 뷰어) 역할에 다음 권한이 추가되었습니다.

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
  
Network Management API  |  현재 GA  |

` roles/networkmanagement.admin ` (네트워크 관리 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Network Management API  |  현재 GA  |

` roles/networkmanagement.viewer ` (네트워크 관리 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
기본 역할  |  역할 업데이트됨  |

` roles/owner ` (소유자) 역할에 다음 권한이 추가되었습니다.

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
  
기본 역할  |  역할 업데이트됨  |

` roles/viewer ` (뷰어) 역할에 다음 권한이 추가되었습니다.

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.get `  
` servicedirectory.locations.list `  
  
BigQuery  |  추가됨  |  ` bigquery.bireservations.get `  
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
  
BigQuery  |  커스텀 역할에서 지원됨  |  ` bigquery.bireservations.get `  
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
  
Identity Platform  |  추가됨  |  ` identityplatform.workloadPoolProviders.create
`  
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
  
Network Management API  |  현재 GA  |  `
networkmanagement.connectivitytests.create `  
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
  
Redis용 Memorystore  |  추가됨  |  ` redis.instances.failover `  
` redis.instances.upgrade `  
  
Redis용 Memorystore  |  커스텀 역할에서 지원됨  |  ` redis.instances.failover `  
` redis.instances.upgrade `  
  
서비스 디렉터리  |  추가됨  |  ` servicedirectory.endpoints.create `  
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
  
서비스 디렉터리  |  커스텀 역할에서 지원됨  |  ` servicedirectory.endpoints.create `  
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
  
  
##  2020년 2월 27일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
BigQuery  |  현재 GA  |

` roles/bigquery.readSessionUser ` (BigQuery 읽기 세션 사용자) 역할 일반 안정화 버전이 출시되었습니다.  
  
데이터 카탈로그  |  역할 업데이트됨  |

` roles/datacatalog.entryGroupCreator ` (DataCatalog EntryGroup 생성자) 역할에 다음
권한이 추가되었습니다.

` datacatalog.entryGroups.list `  
  
기본 역할  |  역할 업데이트됨  |

` roles/editor ` (편집자) 역할에 다음 권한이 추가되었습니다.

` dlp.jobs.create `  
` dlp.jobs.get `  
` dlp.jobs.list `  
  
보안 비밀 관리자  |  역할 업데이트됨  |

` roles/secretmanager.secretAccessor ` (보안 비밀 관리자 보안 비밀 접근자) 역할에 다음 권한이
추가되었습니다.

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
보안센터  |  역할 업데이트됨  |

` roles/securitycenter.adminEditor ` (보안 센터 관리자 편집자) 역할에 다음 권한이 추가되었습니다.

` securitycenter.organizationsettings.get `  
  
보안센터  |  역할 업데이트됨  |

` roles/securitycenter.adminViewer ` (보안 센터 관리자 뷰어) 역할에 다음 권한이 추가되었습니다.

` securitycenter.organizationsettings.get `  
  
Cloud Spanner  |  현재 GA  |

` roles/spanner.backupAdmin ` (Cloud Spanner 백업 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Spanner  |  현재 GA  |

` roles/spanner.backupWriter ` (Cloud Spanner 백업 작성자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Spanner  |  현재 GA  |

` roles/spanner.restoreAdmin ` (Cloud Spanner 복원 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
기본 역할  |  역할 업데이트됨  |

` roles/viewer ` (뷰어) 역할에 다음 권한이 추가되었습니다.

` dlp.jobs.get `  
` dlp.jobs.list `  
  
BigQuery  |  추가됨  |  ` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  커스텀 역할에서 지원됨  |  ` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  현재 GA  |  ` bigquery.readsessions.create `  
` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
데이터 카탈로그  |  추가됨  |  ` datacatalog.entryGroups.list `  
  
데이터 카탈로그  |  커스텀 역할에서 지원됨  |  ` datacatalog.entryGroups.list `  
  
Cloud Healthcare API  |  커스텀 역할에서 지원됨  |  `
healthcare.fhirStores.executeBundle `  
  
Cloud Identity and Access Management  |  커스텀 역할에서 지원됨  |  `
iam.serviceAccounts.getOpenIdToken `  
  
Cloud Spanner  |  추가됨  |  ` spanner.backupOperations.cancel `  
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
  
Cloud Spanner  |  커스텀 역할에서 지원됨  |  ` spanner.backupOperations.cancel `  
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
  
Cloud Spanner  |  현재 GA  |  ` spanner.backupOperations.cancel `  
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
  
  
##  2020년 2월 21일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Access Context Manager  |  추가됨  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Access Context Manager  |  현재 GA  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Compute Engine  |  추가됨  |  ` compute.regionHealthCheckServices.create `  
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
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.regionHealthCheckServices.create
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
  
  
##  2020년 2월 14일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Google Cloud 지원  |  현재 GA  |

` roles/cloudsupport.techSupportEditor ` (기술 지원 편집자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Google Cloud 지원  |  현재 GA  |

` roles/cloudsupport.techSupportViewer ` (기술 지원 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
기본 역할  |  역할 업데이트됨  |

` roles/editor ` (편집자) 역할에 다음 권한이 추가되었습니다.

` healthcare.fhirStores.executeBundle `  
  
Cloud Healthcare API  |  역할 업데이트됨  |

` roles/healthcare.fhirResourceEditor ` (Healthcare FHIR 리소스 편집자) 역할에 다음 권한이
추가되었습니다.

` healthcare.fhirStores.executeBundle `  
  
Cloud Healthcare API  |  역할 업데이트됨  |

` roles/healthcare.fhirResourceReader ` (Healthcare FHIR 리소스 리더) 역할에 다음 권한이
추가되었습니다.

` healthcare.fhirStores.executeBundle `  
  
Cloud 로깅  |  역할 업데이트됨  |

` roles/logging.privateLogViewer ` (비공개 로그 뷰어) 역할에 다음 권한이 추가되었습니다.

` logging.buckets.get `  
` logging.buckets.list `  
  
Cloud 로깅  |  역할 업데이트됨  |

` roles/logging.viewer ` (로그 뷰어) 역할에 다음 권한이 추가되었습니다.

` logging.buckets.get `  
` logging.buckets.list `  
  
기본 역할  |  역할 업데이트됨  |

` roles/owner ` (소유자) 역할에 다음 권한이 추가되었습니다.

` healthcare.fhirStores.executeBundle `  
  
보안센터  |  역할 업데이트됨  |

` roles/securitycenter.admin ` (보안 센터 관리자) 역할에 다음 권한이 추가되었습니다.

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
  
보안센터  |  역할 업데이트됨  |

` roles/securitycenter.adminEditor ` (보안 센터 관리자 편집자) 역할에 다음 권한이 추가되었습니다.

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
  
보안센터  |  역할 업데이트됨  |

` roles/securitycenter.adminViewer ` (보안 센터 관리자 뷰어) 역할에 다음 권한이 추가되었습니다.

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
  
기본 역할  |  역할 업데이트됨  |

` roles/viewer ` (뷰어) 역할에 다음 권한이 추가되었습니다.

` healthcare.fhirStores.executeBundle `  
  
Google Cloud 지원  |  추가됨  |  ` cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Google Cloud 지원  |  커스텀 역할에서 지원됨  |  ` cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Google Cloud 지원  |  현재 GA  |  ` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Cloud Healthcare API  |  추가됨  |  ` healthcare.fhirStores.executeBundle `  
  
Cloud 로깅  |  추가됨  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud 로깅  |  커스텀 역할에서 지원됨  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud 로깅  |  현재 GA  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
  
##  2020년 2월 7일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
보안 비밀 관리자  |  현재 GA  |

` roles/secretmanager.admin ` (보안 비밀 관리자 관리) 역할 일반 안정화 버전이 출시되었습니다.  
  
보안 비밀 관리자  |  현재 GA  |

` roles/secretmanager.secretAccessor ` (보안 비밀 관리자 보안 비밀 접근자) 역할 일반 안정화 버전이
출시되었습니다.  
  
보안 비밀 관리자  |  현재 GA  |

` roles/secretmanager.viewer ` (보안 비밀 관리자 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Healthcare API  |  커스텀 역할에서 지원됨  |  ` healthcare.datasets.create `  
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
  
reCAPTCHA Enterprise  |  추가됨  |  ` recaptchaenterprise.assessments.annotate `  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
reCAPTCHA Enterprise  |  커스텀 역할에서 지원됨  |  `
recaptchaenterprise.assessments.annotate `  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
보안 비밀 관리자  |  커스텀 역할에서 지원됨  |  ` secretmanager.locations.get `  
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
  
보안 비밀 관리자  |  현재 GA  |  ` secretmanager.locations.get `  
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
  
  
##  2020년 1월 31일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud 빌드  |  역할 업데이트됨  |

` roles/cloudbuild.builds.builder ` (Cloud Build 서비스 계정) 역할에 다음 권한이 추가되었습니다.

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
  
Cloud Composer  |  역할 업데이트됨  |

` roles/composer.worker ` (Composer 작업자) 역할에 다음 권한이 추가되었습니다.

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
  
Google Cloud Game Servers  |  추가됨  |  ` gameservices.gameServerClusters.create
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
  
Google Cloud Game Servers  |  커스텀 역할에서 지원됨  |  `
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
  
Google Cloud 작업 도구 모음  |  추가됨  |  ` opsconfigmonitoring.resourceMetadata.write
`  
  
  
##  2020년 1월 24일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud 스케줄러  |  역할 업데이트됨  |

` roles/cloudscheduler.admin ` (Cloud Scheduler 관리자) 역할에 다음 권한이 추가되었습니다.

` serviceusage.services.list `  
  
Cloud 스케줄러  |  역할 업데이트됨  |

` roles/cloudscheduler.jobRunner ` (Cloud Scheduler 작업 실행자) 역할에 다음 권한이
추가되었습니다.

` serviceusage.services.list `  
  
Cloud 스케줄러  |  역할 업데이트됨  |

` roles/cloudscheduler.viewer ` (Cloud Scheduler 뷰어) 역할에 다음 권한이 추가되었습니다.

` serviceusage.services.list `  
  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.networkAdmin ` (Compute 네트워크 관리자) 역할에 다음 권한이 추가되었습니다.

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.networkViewer ` (Compute Network 뷰어) 역할에 다음 권한이 추가되었습니다.

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
보안센터  |  현재 GA  |

` roles/securitycenter.notificationConfigEditor ` (보안 센터 알림 구성 편집자) 역할 일반 안정화
버전이 출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.notificationConfigViewer ` (보안 센터 알림 구성 뷰어) 역할 일반 안정화
버전이 출시되었습니다.  
  
Artifact Registry  |  추가됨  |  ` artifactregistry.files.get `  
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
  
Artifact Registry  |  커스텀 역할에서 지원됨  |  ` artifactregistry.files.get `  
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
  
Cloud ID 및 액세스 관리  |  추가됨  |  ` iam.serviceAccounts.getOpenIdToken `  
  
보안센터  |  추가됨  |  ` securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
보안센터  |  커스텀 역할에서 지원됨  |  ` securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
보안센터  |  현재 GA  |  ` securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
  
##  2020년 1월 10일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
클라우드 애셋 인벤토리  |  현재 GA  |

` roles/cloudasset.owner ` (클라우드 애셋 소유자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Compute Engine용 이전  |  역할 업데이트됨  |

` roles/cloudmigration.inframanager ` (Velostrata 관리자) 역할에 다음 권한이 추가되었습니다.

` compute.globalOperations.get `  
  
Cloud Spanner  |  역할 업데이트됨  |

` roles/spanner.databaseReader ` (Cloud Spanner 데이터베이스 리더) 역할에 다음 권한이 추가되었습니다.

` spanner.instances.get `  
  
Cloud Spanner  |  역할 업데이트됨  |

` roles/spanner.databaseUser ` (Cloud Spanner 데이터베이스 사용자) 역할에 다음 권한이 추가되었습니다.

` spanner.instances.get `  
  
클라우드 애셋 인벤토리  |  현재 GA  |  ` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Compute Engine  |  추가됨  |  ` compute.networks.listPeeringRoutes `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.networks.listPeeringRoutes `  
  
Compute Engine  |  현재 GA  |  ` compute.networks.listPeeringRoutes `  
  
Network Management API  |  추가됨  |  `
networkmanagement.connectivitytests.create `  
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
  
Network Management API  |  커스텀 역할에서 지원됨  |  `
networkmanagement.connectivitytests.create `  
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
  
  
##  2019년 12월 20일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine용 이전  |  역할 업데이트됨  |

` roles/cloudmigration.inframanager ` (Velostrata 관리자) 역할에 다음 권한이 추가되었습니다.

` compute.disks.createSnapshot `  
` compute.snapshots.create `  
` compute.snapshots.delete `  
` compute.snapshots.get `  
` compute.snapshots.setLabels `  
` compute.snapshots.useReadOnly `  
  
Cloud 스케줄러  |  역할 업데이트됨  |

` roles/cloudscheduler.admin ` (Cloud Scheduler 관리자) 역할에 다음 권한이 추가되었습니다.

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud 스케줄러  |  역할 업데이트됨  |

` roles/cloudscheduler.jobRunner ` (Cloud Scheduler 작업 실행자) 역할에 다음 권한이
추가되었습니다.

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud 스케줄러  |  역할 업데이트됨  |

` roles/cloudscheduler.viewer ` (Cloud Scheduler 뷰어) 역할에 다음 권한이 추가되었습니다.

` appengine.applications.get `  
` serviceusage.services.get `  
  
Compute Engine  |  현재 GA  |

` roles/compute.packetMirroringAdmin ` (Compute 패킷 미러링 관리자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Compute Engine  |  현재 GA  |

` roles/compute.packetMirroringUser ` (Compute 패킷 미러링 사용자) 역할 일반 안정화 버전이
출시되었습니다.  
  
클라우드 DNS  |  현재 GA  |

` roles/dns.peer ` (DNS 피어) 역할 일반 안정화 버전이 출시되었습니다.  
  
기본 역할  |  역할 업데이트됨  |

` roles/editor ` (편집자) 역할에서 다음 권한이 삭제되었습니다.

` datacatalog.taxonomies.create `  
  
추천자  |  현재 GA  |

` roles/recommender.computeAdmin ` (Compute 추천자 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
추천자  |  현재 GA  |

` roles/recommender.computeViewer ` (Compute 추천자 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
추천자  |  현재 GA  |

` roles/recommender.iamAdmin ` (IAM 추천자 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
추천자  |  현재 GA  |

` roles/recommender.iamViewer ` (IAM 추천자 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
원격 빌드 실행  |  역할 추가됨  |

` roles/remotebuildexecution.reservationAdmin ` (원격 빌드 실행 예약 관리자) 역할에 다음 권한이
추가되었습니다.

` remotebuildexecution.actions.create `  
` remotebuildexecution.actions.delete `  
` remotebuildexecution.actions.get `  
  
Cloud Bigtable  |  추가됨  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  커스텀 역할에서 지원됨  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  현재 GA  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Compute Engine  |  추가됨  |  ` compute.nodeGroups.update `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.nodeGroups.update `  
  
Compute Engine  |  현재 GA  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
데이터 카탈로그  |  추가됨  |  ` datacatalog.entries.list `  
` datacatalog.entries.updateTag `  
` datacatalog.entryGroups.update `  
  
Dataproc  |  추가됨  |  ` dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
Dataproc  |  현재 GA  |  ` dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
클라우드 DNS  |  현재 GA  |  ` dns.networks.targetWithPeeringZone `  
  
Cloud 로깅  |  추가됨  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud 로깅  |  커스텀 역할에서 지원됨  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud 로깅  |  현재 GA  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
추천자  |  현재 GA  |  `
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
  
  
##  2019년 11월 22일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
데이터 카탈로그  |  역할 업데이트됨  |

` roles/datacatalog.admin ` (Data Catalog 관리자) 역할에서 다음 권한이 삭제되었습니다.

` datacatalog.categories.fineGrainedGet `  
  
기본 역할  |  역할 업데이트됨  |

` roles/editor ` (편집자) 역할에 다음 권한이 추가되었습니다.

` remotebuildexecution.actions.delete `  
  
Identity Toolkit API  |  현재 GA  |

` roles/identitytoolkit.admin ` (Identity Toolkit 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Identity Toolkit API  |  현재 GA  |

` roles/identitytoolkit.viewer ` (Identity Toolkit 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Apigee API  |  추가됨  |  ` apigee.apiproductattributes.createOrUpdateAll `  
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
  
Apigee API  |  커스텀 역할에서 지원됨  |  `
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
  
BigQuery  |  추가됨  |  ` bigquery.tables.setCategory `  
  
Compute Engine  |  추가됨  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
원격 빌드 실행  |  추가됨  |  ` remotebuildexecution.actions.delete `  
  
원격 빌드 실행  |  커스텀 역할에서 지원됨  |  ` remotebuildexecution.actions.delete `  
  
  
##  2019년 11월 14일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
액세스 승인  |  추가됨  |  ` accessapproval.settings.delete `  
  
AI Platform Notebooks  |  추가됨  |  ` notebooks.environments.create `  
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
  
AI Platform Notebooks  |  커스텀 역할에서 지원됨  |  ` notebooks.environments.create `  
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
  
  
##  2019년 11월 1일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Hangouts Chat API  |  현재 GA  |

` roles/chat.owner ` (채팅 봇 소유자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Hangouts Chat API  |  현재 GA  |

` roles/chat.reader ` (채팅 봇 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Hangouts Chat API  |  현재 GA  |  ` chat.bots.get `  
` chat.bots.update `  
  
클라우드 애셋 인벤토리  |  추가됨  |  ` cloudasset.assets.exportAppengineApplications `  
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
  
데이터 카탈로그  |  추가됨  |  ` datacatalog.categories.fineGrainedGet `  
` datacatalog.categories.getIamPolicy `  
` datacatalog.categories.setIamPolicy `  
` datacatalog.taxonomies.create `  
` datacatalog.taxonomies.delete `  
` datacatalog.taxonomies.get `  
` datacatalog.taxonomies.getIamPolicy `  
` datacatalog.taxonomies.list `  
` datacatalog.taxonomies.setIamPolicy `  
` datacatalog.taxonomies.update `  
  
IAP(Identity-Aware Proxy)  |  추가됨  |  ` iap.projects.getSettings `  
` iap.projects.updateSettings `  
  
NetApp Cloud Volumes 서비스  |  추가됨  |  ` netappcloudvolumes.jobs.get `  
` netappcloudvolumes.jobs.list `  
  
Redis Enterprise Cloud  |  추가됨  |  ` redisenterprisecloud.databases.create `  
` redisenterprisecloud.databases.delete `  
` redisenterprisecloud.databases.get `  
` redisenterprisecloud.databases.list `  
` redisenterprisecloud.databases.update `  
` redisenterprisecloud.subscriptions.create `  
` redisenterprisecloud.subscriptions.delete `  
` redisenterprisecloud.subscriptions.get `  
` redisenterprisecloud.subscriptions.list `  
` redisenterprisecloud.subscriptions.update `  
  
  
##  2019년 10월 25일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
IAP(Identity-Aware Proxy)  |  현재 GA  |

` roles/iap.tunnelResourceAccessor ` (IAP 보안 터널 사용자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Microsoft Active Directory의 관리형 서비스  |  현재 GA  |

` roles/managedidentities.admin ` (Google Cloud 관리형 ID 관리자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Microsoft Active Directory의 관리형 서비스  |  현재 GA  |

` roles/managedidentities.domainAdmin ` (Google Cloud 관리형 ID 도메인 관리자) 역할 일반
안정화 버전이 출시되었습니다.  
  
Microsoft Active Directory의 관리형 서비스  |  현재 GA  |

` roles/managedidentities.viewer ` (Google Cloud 관리형 ID 뷰어) 역할 일반 안정화 버전이
출시되었습니다.  
  
Actions API  |  추가됨  |  ` actions.agentVersions.get `  
  
Actions API  |  커스텀 역할에서 지원됨  |  ` actions.agentVersions.get `  
  
Actions API  |  현재 GA  |  ` actions.agentVersions.get `  
  
Dialogflow  |  추가됨  |  ` dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
Dialogflow  |  현재 GA  |  ` dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
IAP(Identity-Aware Proxy)  |  현재 GA  |  ` iap.tunnel.getIamPolicy `  
` iap.tunnel.setIamPolicy `  
` iap.tunnelInstances.accessViaIAP `  
` iap.tunnelInstances.getIamPolicy `  
` iap.tunnelInstances.setIamPolicy `  
` iap.tunnelZones.getIamPolicy `  
` iap.tunnelZones.setIamPolicy `  
  
Microsoft Active Directory의 관리형 서비스  |  현재 GA  |  `
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
  
  
##  2019년 10월 18일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
IAP(Identity-Aware Proxy)  |  현재 GA  |

` roles/iap.settingsAdmin ` (IAP 설정 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
IAP(Identity-Aware Proxy)  |  추가됨  |  ` iap.web.getSettings `  
` iap.web.updateSettings `  
` iap.webServiceVersions.getSettings `  
` iap.webServiceVersions.updateSettings `  
` iap.webServices.getSettings `  
` iap.webServices.updateSettings `  
` iap.webTypes.getSettings `  
` iap.webTypes.updateSettings `  
  
  
##  2019년 10월 11일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Firebase 보안 규칙  |  현재 GA  |

` roles/firebaserules.admin ` (Firebase 규칙 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase 보안 규칙  |  현재 GA  |

` roles/firebaserules.viewer ` (Firebase 규칙 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
BigQuery  |  커스텀 역할에서 지원됨  |  ` bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Google Kubernetes Engine  |  추가됨  |  ` container.csiDrivers.create `  
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
  
Google Kubernetes Engine  |  커스텀 역할에서 지원됨  |  ` container.csiDrivers.create `  
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
  
Google Kubernetes Engine  |  현재 GA  |  ` container.csiDrivers.create `  
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
  
Firebase 보안 규칙  |  현재 GA  |  ` firebaserules.releases.create `  
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
  
  
##  2019년 10월 4일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Actions API  |  추가됨  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Actions API  |  커스텀 역할에서 지원됨  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Actions API  |  현재 GA  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Cloud ID 및 액세스 관리  |  커스텀 역할에서 지원됨  |  ` iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
  
  
##  2019년 9월 27일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Hangouts Chat API  |  추가됨  |  ` chat.bots.get `  
` chat.bots.update `  
  
Hangouts Chat API  |  커스텀 역할에서 지원됨  |  ` chat.bots.get `  
` chat.bots.update `  
  
클라우드 애셋 인벤토리  |  추가됨  |  ` cloudasset.assets.exportAccessLevel `  
` cloudasset.assets.exportAccessPolicy `  
` cloudasset.assets.exportAllAccessPolicy `  
` cloudasset.assets.exportOrgPolicy `  
` cloudasset.assets.exportServicePerimeter `  
` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
클라우드 애셋 인벤토리  |  커스텀 역할에서 지원됨  |  ` cloudasset.assets.exportAccessPolicy `  
` cloudasset.assets.exportOrgPolicy `  
` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Cloud Identity and Access Management  |  커스텀 역할에서 지원됨  |  `
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
  
VM Migration API  |  추가됨  |  ` vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
VM Migration API  |  커스텀 역할에서 지원됨  |  ` vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
  
##  2019년 9월 20일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud Key Management Service  |  현재 GA  |

` roles/cloudkms.importer ` (Cloud KMS 가져오기 작업자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Key Management Service  |  현재 GA  |

` roles/cloudkms.publicKeyViewer ` (Cloud KMS CryptoKey 공개 키 뷰어) 역할 일반 안정화 버전이
출시되었습니다.  
  
Cloud Key Management Service  |  현재 GA  |

` roles/cloudkms.signer ` (Cloud KMS CryptoKey 서명자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Key Management Service  |  현재 GA  |

` roles/cloudkms.signerVerifier ` (Cloud KMS CryptoKey 서명자/검증자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Cloud Key Management Service  |  추가됨  |  ` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  커스텀 역할에서 지원됨  |  ` cloudkms.importJobs.create
`  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  현재 GA  |  `
cloudkms.cryptoKeyVersions.useToSign `  
` cloudkms.cryptoKeyVersions.viewPublicKey `  
` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
  
##  2019년 9월 13일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Firebase 원격 구성  |  현재 GA  |

` roles/cloudconfig.admin ` (Firebase 원격 구성 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase 원격 구성  |  현재 GA  |

` roles/cloudconfig.viewer ` (Firebase 원격 구성 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase  |  현재 GA  |

` roles/firebase.admin ` (Firebase 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase  |  현재 GA  |

` roles/firebase.analyticsAdmin ` (Firebase 애널리틱스 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase  |  현재 GA  |

` roles/firebase.analyticsViewer ` (Firebase 애널리틱스 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase  |  현재 GA  |

` roles/firebase.developAdmin ` (Firebase 개발 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase  |  현재 GA  |

` roles/firebase.developViewer ` (Firebase 개발 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase  |  현재 GA  |

` roles/firebase.growthAdmin ` (Firebase Grow Admin) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase  |  현재 GA  |

` roles/firebase.growthViewer ` (Firebase 확장 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase  |  현재 GA  |

` roles/firebase.qualityAdmin ` (Firebase 품질 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase  |  현재 GA  |

` roles/firebase.qualityViewer ` (Firebase 품질 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase  |  현재 GA  |

` roles/firebase.viewer ` (Firebase 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase 인증  |  현재 GA  |

` roles/firebaseauth.admin ` (Firebase 인증 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase 인증  |  현재 GA  |

` roles/firebaseauth.viewer ` (Firebase 인증 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase Crashlytics  |  현재 GA  |

` roles/firebasecrashlytics.admin ` (Firebase Crashlytics 관리자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Firebase Crashlytics  |  현재 GA  |

` roles/firebasecrashlytics.viewer ` (Firebase Crashlytics 뷰어) 역할 일반 안정화 버전이
출시되었습니다.  
  
Firebase 실시간 데이터베이스  |  현재 GA  |

` roles/firebasedatabase.admin ` (Firebase 실시간 데이터베이스 관리자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Firebase 실시간 데이터베이스  |  현재 GA  |

` roles/firebasedatabase.viewer ` (Firebase 실시간 데이터베이스 뷰어) 역할 일반 안정화 버전이
출시되었습니다.  
  
Firebase 동적 링크  |  현재 GA  |

` roles/firebasedynamiclinks.admin ` (Firebase 동적 링크 관리자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Firebase 동적 링크  |  현재 GA  |

` roles/firebasedynamiclinks.viewer ` (Firebase 동적 링크 뷰어) 역할 일반 안정화 버전이
출시되었습니다.  
  
Firebase 호스팅  |  현재 GA  |

` roles/firebasehosting.admin ` (Firebase 호스팅 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase 호스팅  |  현재 GA  |

` roles/firebasehosting.viewer ` (Firebase 호스팅 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase 클라우드 메시징  |  현재 GA  |

` roles/firebasenotifications.admin ` (Firebase 클라우드 메시징 관리자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Firebase 클라우드 메시징  |  현재 GA  |

` roles/firebasenotifications.viewer ` (Firebase 클라우드 메시징 뷰어) 역할 일반 안정화 버전이
출시되었습니다.  
  
Firebase 성능 모니터링  |  현재 GA  |

` roles/firebaseperformance.admin ` (Firebase 성능 보고 관리자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Firebase 성능 모니터링  |  현재 GA  |

` roles/firebaseperformance.viewer ` (Firebase 성능 보고 뷰어) 역할 일반 안정화 버전이
출시되었습니다.  
  
Firebase 예측  |  현재 GA  |

` roles/firebasepredictions.admin ` (Firebase 예측 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase 예측  |  현재 GA  |

` roles/firebasepredictions.viewer ` (Firebase 예측 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase 원격 구성  |  현재 GA  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
클라우드 DNS  |  현재 GA  |  ` dns.networks.bindPrivateDNSPolicy `  
` dns.policies.create `  
` dns.policies.delete `  
` dns.policies.get `  
` dns.policies.getIamPolicy `  
` dns.policies.list `  
` dns.policies.setIamPolicy `  
` dns.policies.update `  
  
Firebase  |  현재 GA  |  ` firebase.billingPlans.get `  
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
  
Firebase 인증  |  현재 GA  |  ` firebaseauth.configs.create `  
` firebaseauth.configs.get `  
` firebaseauth.configs.getHashConfig `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Crashlytics  |  현재 GA  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase 실시간 데이터베이스  |  현재 GA  |  ` firebasedatabase.instances.create `  
` firebasedatabase.instances.get `  
` firebasedatabase.instances.list `  
` firebasedatabase.instances.update `  
  
Firebase 동적 링크  |  현재 GA  |  ` firebasedynamiclinks.destinations.list `  
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
  
Firebase 호스팅  |  현재 GA  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase 클라우드 메시징  |  현재 GA  |  ` firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase 성능 모니터링  |  현재 GA  |  ` firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase 예측  |  현재 GA  |  ` firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
NetApp Cloud Volumes 서비스  |  추가됨  |  `
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
  
이벤트 위협 감지  |  커스텀 역할에서 지원됨  |  ` threatdetection.detectorSettings.clear `  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  2019년 9월 6일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
기본 역할  |  역할 업데이트됨  |

` roles/owner ` (소유자) 역할에 다음 권한이 추가되었습니다.

` dataprocessing.iamaccesshistory.exportData `  
  
서버리스 VPC 액세스  |  현재 GA  |

` roles/vpaccess.user ` (서버리스 VPC 액세스 사용자) 역할 일반 안정화 버전이 출시되었습니다.  
  
서버리스 VPC 액세스  |  현재 GA  |

` roles/vpaccess.viewer ` (서버리스 VPC 액세스 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
서버리스 VPC 액세스  |  현재 GA  |

` roles/vpcaccess.admin ` (서버리스 VPC 액세스 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Compute Engine  |  추가됨  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  현재 GA  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
서버리스 VPC 액세스  |  현재 GA  |  ` vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  2019년 8월 30일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Firebase Test Lab  |  역할 업데이트됨  |

` roles/cloudtestservice.testAdmin ` (Firebase Test Lab 관리자) 역할에 다음 권한이
추가되었습니다.

` firebase.clients.get `  
` firebase.projects.get `  
  
Firebase Test Lab  |  역할 업데이트됨  |

` roles/cloudtestservice.testViewer ` (Firebase Test Lab 뷰어) 역할에 다음 권한이
추가되었습니다.

` firebase.clients.get `  
` firebase.projects.get `  
  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.orgSecurityPolicyAdmin ` (Compute 조직 보안 정책 관리자) 역할에 다음 권한이
추가되었습니다.

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.orgSecurityPolicyUser ` (Compute 조직 보안 정책 사용자) 역할에 다음 권한이
추가되었습니다.

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.orgSecurityResourceAdmin ` (Compute 조직 리소스 관리자) 역할에 다음 권한이
추가되었습니다.

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
  
##  2019년 8월 23일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
번역  |  현재 GA  |

` roles/cloudtranslate.admin ` (Cloud Translation API 관리자) 역할 일반 안정화 버전이
출시되었습니다.  
  
번역  |  현재 GA  |

` roles/cloudtranslate.editor ` (Cloud Translation API 편집자) 역할 일반 안정화 버전이
출시되었습니다.  
  
번역  |  현재 GA  |

` roles/cloudtranslate.user ` (Cloud Translation API 사용자) 역할 일반 안정화 버전이
출시되었습니다.  
  
번역  |  현재 GA  |

` roles/cloudtranslate.viewer ` (Cloud Translation API 뷰어) 역할 일반 안정화 버전이
출시되었습니다.  
  
Cloud Healthcare API  |  역할 업데이트됨  |

` roles/healthcare.dicomEditor ` (Healthcare DICOM 편집자) 역할에 다음 권한이 추가되었습니다.

` healthcare.dicomStores.dicomWebDelete `  
  
번역  |  현재 GA  |  ` cloudtranslate.generalModels.batchPredict `  
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
  
  
##  2019년 8월 16일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
번역  |  커스텀 역할에서 지원됨  |  ` cloudtranslate.locations.get `  
` cloudtranslate.locations.list `  
  
Compute Engine  |  현재 GA  |  ` compute.networks.updatePeering `  
  
데이터 카탈로그  |  추가됨  |  ` datacatalog.entries.create `  
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
  
데이터 카탈로그  |  커스텀 역할에서 지원됨  |  ` datacatalog.entries.create `  
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
  
  
##  2019년 8월 9일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.orgSecurityPolicyAdmin ` (Compute 조직 보안 정책 관리자) 역할에 다음 권한이
추가되었습니다.

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.orgSecurityPolicyUser ` (Compute 조직 보안 정책 사용자) 역할에 다음 권한이
추가되었습니다.

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.orgSecurityResourceAdmin ` (Compute 조직 리소스 관리자) 역할에 다음 권한이
추가되었습니다.

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Cloud Storage  |  현재 GA  |

` roles/storage.hmacKeyAdmin ` (스토리지 HMAC 키 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Storage  |  추가됨  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
Cloud Storage  |  커스텀 역할에서 지원됨  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
Cloud Storage  |  현재 GA  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
  
##  2019년 6월 28일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
기본 역할  |  역할 업데이트됨  |

` roles/viewer ` (뷰어) 역할에 다음 권한이 추가되었습니다.

` pubsub.snapshots.seek `  
  
Firebase Crashlytics  |  추가됨  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase Crashlytics  |  커스텀 역할에서 지원됨  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Redis용 Memorystore  |  추가됨  |  ` redis.instances.export `  
` redis.instances.import `  
  
Redis용 Memorystore  |  커스텀 역할에서 지원됨  |  ` redis.instances.export `  
` redis.instances.import `  
  
  
##  2019년 6월 21일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine용 이전  |  역할 업데이트됨  |

` roles/cloudmigration.inframanager ` (Velostrata 관리자) 역할에 다음 권한이 추가되었습니다.

` compute.instances.updateShieldedInstanceConfig `  
  
번역  |  역할 업데이트됨  |

` roles/cloudtranslate.viewer ` (Cloud Translation API 뷰어) 역할에 다음 권한이 추가되었습니다.

` cloudtranslate.operations.wait `  
  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.networkUser ` (Compute 네트워크 사용자) 역할에 다음 권한이 추가되었습니다.

` compute.vpnGateways.use `  
  
Firebase  |  역할 업데이트됨  |

` roles/firebase.admin ` (Firebase 관리자) 역할에 다음 권한이 추가되었습니다.

` cloudmessaging.messages.create `  
  
Firebase  |  역할 업데이트됨  |

` roles/firebase.growthAdmin ` (Firebase Grow Admin) 역할에 다음 권한이 추가되었습니다.

` cloudmessaging.messages.create `  
  
리소스 관리자  |  역할 업데이트됨  |

` roles/resourcemanager.projectMover ` (프로젝트 이동자) 역할에 다음 권한이 추가되었습니다.

` resourcemanager.projects.move `  
  
보안센터  |  역할 업데이트됨  |

` roles/securitycenter.adminEditor ` (보안 센터 관리자 편집자) 역할에 다음 권한이 추가되었습니다.

` securitycenter.assets.group `  
` securitycenter.assets.list `  
` securitycenter.assets.listAssetPropertyNames `  
  
BigQuery  |  추가됨  |  ` bigquery.connections.create `  
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
  
BigQuery  |  커스텀 역할에서 지원됨  |  ` bigquery.routines.create `  
` bigquery.routines.delete `  
` bigquery.routines.get `  
` bigquery.routines.list `  
` bigquery.routines.update `  
  
번역  |  커스텀 역할에서 지원됨  |  ` cloudtranslate.generalModels.batchPredict `  
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
  
Cloud Composer  |  추가됨  |  ` composer.imageversions.list `  
  
Cloud Composer  |  커스텀 역할에서 지원됨  |  ` composer.imageversions.list `  
  
Cloud Composer  |  현재 GA  |  ` composer.imageversions.list `  
  
Compute Engine  |  추가됨  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  현재 GA  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
  
##  2019년 6월 14일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud Identity and Access Management  |  현재 GA  |

` roles/iam.workloadIdentityUser ` (워크로드 아이덴티티 사용자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud 함수  |  추가됨  |  ` cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Cloud 함수  |  커스텀 역할에서 지원됨  |  ` cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Compute Engine  |  현재 GA  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  2019년 5월 31일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
데이터 카탈로그  |  역할 업데이트됨  |

` roles/datacatalog.admin ` (Data Catalog 관리자) 역할에 다음 권한이 추가되었습니다.

` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
` pubsub.topics.updateTag `  
  
Compute Engine용 이전  |  추가됨  |  ` cloudmigration.velostrataendpoints.connect `  
  
Cloud ID 및 액세스 관리  |  커스텀 역할에서 사용 가능  |  ` iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
  
##  2019년 5월 24일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
기본 역할  |  역할 업데이트됨  |

` roles/viewer ` (뷰어) 역할에 다음 권한이 추가되었습니다.

` managedidentities.domains.validateTrust `  
  
Recommendations AI  |  커스텀 역할에서 지원됨  |  ` automlrecommendations.apiKeys.create
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
  
BigQuery  |  추가됨  |  ` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
BigQuery  |  커스텀 역할에서 지원됨  |  ` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
데이터 카탈로그  |  추가됨  |  ` datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
데이터 카탈로그  |  커스텀 역할에서 지원됨  |  ` datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
Filestore  |  추가됨  |  ` file.snapshots.update `  
  
Filestore  |  커스텀 역할에서 지원됨  |  ` file.snapshots.update `  
  
게시/구독  |  추가됨  |  ` pubsub.topics.updateTag `  
  
게시/구독  |  커스텀 역할에서 지원됨  |  ` pubsub.topics.updateTag `  
  
  
##  2019년 5월 17일 기준 IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Dialogflow  |  추가됨  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  커스텀 역할에서 지원됨  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  현재 GA  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
  
##  2019년 5월 10일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud Identity and Access Management  |  현재 GA  |

` roles/iam.securityAdmin ` (보안 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud IoT  |  추가됨  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  커스텀 역할에서 지원됨  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  현재 GA  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.healthChecks.create `  
` compute.healthChecks.delete `  
` compute.healthChecks.get `  
` compute.healthChecks.list `  
` compute.healthChecks.update `  
` compute.healthChecks.use `  
` compute.healthChecks.useReadOnly `  
` compute.instanceGroups.use `  
  
Cloud Healthcare API  |  추가됨  |  ` healthcare.fhirResources.purge `  
  
Microsoft Active Directory의 관리형 서비스  |  추가됨  |  `
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
  
Microsoft Active Directory의 관리형 서비스  |  커스텀 역할에서 지원됨  |  `
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
  
  
##  2019년 5월 3일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
보안센터  |  현재 GA  |

` roles/securitycenter.admin ` (보안 센터 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.adminEditor ` (보안 센터 관리자 편집자) 역할 일반 안정화 버전이 출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.adminViewer ` (보안 센터 관리자 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.assetsDiscoveryRunner ` (보안 센터 애셋 검색 실행자) 역할 일반 안정화 버전이
출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.assetSecurityMarksWriter ` (보안 센터 애셋 보안 표시 작성자) 역할 일반
안정화 버전이 출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.assetsViewer ` (보안 센터 애셋 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.findingSecurityMarksWriter ` (보안 센터 발견 항목 보안 표시 작성자) 역할
일반 안정화 버전이 출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.findingsEditor ` (보안 센터 발견 항목 편집자) 역할 일반 안정화 버전이
출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.findingsStateSetter ` (보안 센터 발견 항목 상태 설정자) 역할 일반 안정화
버전이 출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.findingsViewer ` (보안 센터 발견 항목 뷰어) 역할 일반 안정화 버전이
출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.sourcesAdmin ` (보안 센터 소스 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.sourcesEditor ` (보안 센터 소스 편집자) 역할 일반 안정화 버전이 출시되었습니다.  
  
보안센터  |  현재 GA  |

` roles/securitycenter.sourcesViewer ` (보안 센터 소스 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Recommendations AI  |  추가됨  |  ` automlrecommendations.apiKeys.create `  
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
  
BigQuery  |  추가됨  |  ` bigquery.models.create `  
` bigquery.models.delete `  
` bigquery.models.getData `  
` bigquery.models.getMetadata `  
` bigquery.models.list `  
` bigquery.models.updateData `  
` bigquery.models.updateMetadata `  
  
Firebase 클라우드 메시징  |  추가됨  |  ` cloudmessaging.messages.create `  
  
Firebase 클라우드 메시징  |  커스텀 역할에서 지원됨  |  ` cloudmessaging.messages.create `  
  
Firebase 클라우드 메시징  |  현재 GA  |  ` cloudmessaging.messages.create `  
  
보안센터  |  현재 GA  |  ` securitycenter.assets.group `  
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
  
  
##  2019년 4월 19일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
기본 역할  |  역할 업데이트됨  |

` roles/editor ` (편집자) 역할에서 다음 권한이 삭제되었습니다.

` firebasedynamiclinks.domains.delete `  
  
보안센터  |  역할 업데이트됨  |

` roles/securitycenter.admin ` (보안 센터 관리자) 역할에 다음 권한이 추가되었습니다.

` securitycenter.findings.setState `  
  
보안센터  |  역할 업데이트됨  |

` roles/securitycenter.adminEditor ` (보안 센터 관리자 편집자) 역할에 다음 권한이 추가되었습니다.

` securitycenter.findings.setState `  
  
보안센터  |  역할 업데이트됨  |

` roles/securitycenter.findingsEditor ` (보안 센터 발견 항목 편집자) 역할에 다음 권한이 추가되었습니다.

` securitycenter.findings.setState `  
  
액세스 승인  |  추가됨  |  ` accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
액세스 승인  |  커스텀 역할에서 지원됨  |  ` accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
Cloud Bigtable  |  추가됨  |  ` bigtable.locations.list `  
  
Cloud Bigtable  |  커스텀 역할에서 지원됨  |  ` bigtable.locations.list `  
  
Cloud Bigtable  |  현재 GA  |  ` bigtable.locations.list `  
  
Cloud 스케줄러  |  추가됨  |  ` cloudscheduler.locations.get `  
` cloudscheduler.locations.list `  
  
Compute Engine  |  추가됨  |  `
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
  
Compute Engine  |  커스텀 역할에서 지원됨  |  `
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
  
Compute Engine  |  현재 GA  |  `
compute.networkEndpointGroups.attachNetworkEndpoints `  
` compute.networkEndpointGroups.create `  
` compute.networkEndpointGroups.delete `  
` compute.networkEndpointGroups.detachNetworkEndpoints `  
` compute.networkEndpointGroups.get `  
` compute.networkEndpointGroups.getIamPolicy `  
` compute.networkEndpointGroups.list `  
` compute.networkEndpointGroups.setIamPolicy `  
` compute.networkEndpointGroups.use `  
  
원격 빌드 실행  |  추가됨  |  ` remotebuildexecution.actions.create `  
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
  
원격 빌드 실행  |  커스텀 역할에서 지원됨  |  ` remotebuildexecution.actions.create `  
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
  
서버리스 VPC 액세스  |  추가됨  |  ` vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  2019년 3월 29일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.networkUser ` (Compute 네트워크 사용자) 역할에 다음 권한이 추가되었습니다.

` servicenetworking.services.get `  
  
Cloud Monitoring  |  역할 업데이트됨  |

` roles/monitoring.admin ` (모니터링 관리자) 역할에 다음 권한이 추가되었습니다.

` serviceusage.services.enable `  
  
Cloud Monitoring  |  역할 업데이트됨  |

` roles/monitoring.editor ` (모니터링 편집자) 역할에 다음 권한이 추가되었습니다.

` serviceusage.services.enable `  
  
Google Cloud 작업 도구 모음  |  역할 업데이트됨  |

` roles/stackdriver.accounts.editor ` (Stackdriver 계정 편집자) 역할에 다음 권한이 추가되었습니다.

` serviceusage.services.enable `  
  
Cloud SQL  |  추가됨  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  커스텀 역할에서 지원됨  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  현재 GA  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
번역  |  추가됨  |  ` cloudtranslate.generalModels.batchPredict `  
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
  
클라우드 DNS  |  추가됨  |  ` dns.networks.targetWithPeeringZone `  
  
클라우드 DNS  |  커스텀 역할에서 지원됨  |  ` dns.networks.targetWithPeeringZone `  
  
이벤트 위협 감지  |  추가됨  |  ` threatdetection.detectorSettings.clear `  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  2019년 3월 22일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Talent Solution  |  현재 GA  |

` roles/cloudjobdiscovery.admin ` (관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Talent Solution  |  현재 GA  |

` roles/cloudjobdiscovery.jobsEditor ` (작업 편집자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Talent Solution  |  현재 GA  |

` roles/cloudjobdiscovery.jobsViewer ` (작업 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Talent Solution  |  현재 GA  |

` roles/cloudjobdiscovery.profilesEditor ` (프로필 편집자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Talent Solution  |  현재 GA  |

` roles/cloudjobdiscovery.profilesViewer ` (프로필 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
기본 역할  |  역할 업데이트됨  |

` roles/editor ` (편집자) 역할에 다음 권한이 추가되었습니다.

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Filestore  |  역할 업데이트됨  |

` roles/file.editor ` (Cloud Filestore 편집자) 역할에 다음 권한이 추가되었습니다.

` file.instances.restore `  
  
기본 역할  |  역할 업데이트됨  |

` roles/owner ` (소유자) 역할에 다음 권한이 추가되었습니다.

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Talent Solution  |  현재 GA  |  ` cloudjobdiscovery.companies.create `  
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
  
Compute Engine  |  추가됨  |  ` compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  현재 GA  |  ` compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Filestore  |  추가됨  |  ` file.instances.restore `  
  
Firebase 인증  |  추가됨  |  ` firebaseauth.configs.getHashConfig `  
  
Firebase 인증  |  커스텀 역할에서 지원됨  |  ` firebaseauth.configs.getHashConfig `  
  
Cloud Healthcare API  |  추가됨  |  ` healthcare.datasets.create `  
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
  
  
##  2019년 3월 15일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Talent Solution  |  역할 업데이트됨  |

` roles/cloudjobdiscovery.profilesEditor ` (프로필 편집자) 역할에 다음 권한이 추가되었습니다.

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Talent Solution  |  역할 업데이트됨  |

` roles/cloudjobdiscovery.profilesEditor ` (프로필 편집자) 역할에서 다음 권한이 삭제되었습니다.

` cloudjobdiscovery.companies.create `  
` cloudjobdiscovery.companies.delete `  
` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.companies.update `  
  
Talent Solution  |  역할 업데이트됨  |

` roles/cloudjobdiscovery.profilesViewer ` (프로필 뷰어) 역할에 다음 권한이 추가되었습니다.

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  역할 업데이트됨  |

` roles/cloudjobdiscovery.profilesViewer ` (프로필 뷰어) 역할에서 다음 권한이 삭제되었습니다.

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
  
기본 역할  |  역할 업데이트됨  |

` roles/editor ` (편집자) 역할에 다음 권한이 추가되었습니다.

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
기본 역할  |  역할 업데이트됨  |

` roles/owner ` (소유자) 역할에 다음 권한이 추가되었습니다.

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
저장소 전송 서비스  |  현재 GA  |

` roles/storagetransfer.admin ` (스토리지 전송 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
저장소 전송 서비스  |  현재 GA  |

` roles/storagetransfer.user ` (스토리지 전송 사용자) 역할 일반 안정화 버전이 출시되었습니다.  
  
저장소 전송 서비스  |  현재 GA  |

` roles/storagetransfer.viewer ` (스토리지 전송 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
기본 역할  |  역할 업데이트됨  |

` roles/viewer ` (뷰어) 역할에 다음 권한이 추가되었습니다.

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  추가됨  |  ` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
클라우드 DNS  |  현재 GA  |  ` dns.networks.bindPrivateDNSZone `  
  
Cloud Run  |  추가됨  |  ` run.configurations.get `  
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
  
Cloud Run  |  커스텀 역할에서 지원되지 않음  |  ` run.routes.invoke `  
  
Cloud Run  |  커스텀 역할에서 지원됨  |  ` run.configurations.get `  
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
  
저장소 전송 서비스  |  추가됨  |  ` storagetransfer.jobs.create `  
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
  
저장소 전송 서비스  |  커스텀 역할에서 지원됨  |  ` storagetransfer.jobs.create `  
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
  
저장소 전송 서비스  |  현재 GA  |  ` storagetransfer.jobs.create `  
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
  
  
##  2019년 3월 7일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
BigQuery  |  역할 추가됨  |

` roles/bigquery.connectionAdmin ` (BigQuery 연결 관리자) 역할에 다음 권한이 추가되었습니다.

` bigquery.connections.create `  
` bigquery.connections.delete `  
` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.setIamPolicy `  
` bigquery.connections.update `  
` bigquery.connections.use `  
  
BigQuery  |  역할 추가됨  |

` roles/bigquery.connectionUser ` (BigQuery 연결 사용자) 역할에 다음 권한이 추가되었습니다.

` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.use `  
  
Dialogflow  |  역할 업데이트됨  |

` roles/dialogflow.admin ` (Dialogflow API 관리자) 역할에 다음 권한이 추가되었습니다.

` dialogflow.agents.update `  
  
Dialogflow  |  역할 업데이트됨  |

` roles/dialogflow.consoleAgentEditor ` (Dialogflow 콘솔 에이전트 편집자) 역할에 다음 권한이
추가되었습니다.

` dialogflow.agents.update `  
  
기본 역할  |  역할 업데이트됨  |

` roles/editor ` (편집자) 역할에 다음 권한이 추가되었습니다.

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  역할 업데이트됨  |

` roles/file.editor ` (Cloud Filestore 편집자) 역할에 다음 권한이 추가되었습니다.

` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  역할 업데이트됨  |

` roles/file.viewer ` (Cloud Filestore 뷰어) 역할에 다음 권한이 추가되었습니다.

` file.snapshots.get `  
` file.snapshots.list `  
  
Cloud ID 및 액세스 관리  |  현재 GA  |

` roles/iam.serviceAccountCreator ` (서비스 계정 만들기) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud ID 및 액세스 관리  |  역할 업데이트됨  |

` roles/iam.securityReviewer ` (보안 검토자) 역할에 다음 권한이 추가되었습니다.

` file.snapshots.list `  
  
기본 역할  |  역할 업데이트됨  |

` roles/owner ` (소유자) 역할에 다음 권한이 추가되었습니다.

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
서비스 사용량  |  역할 업데이트됨  |

` roles/serviceusage.apiKeysAdmin ` (API 키 관리자) 역할에 다음 권한이 추가되었습니다.

` serviceusage.operations.get `  
  
기본 역할  |  역할 업데이트됨  |

` roles/viewer ` (뷰어) 역할에 다음 권한이 추가되었습니다.

` file.snapshots.get `  
` file.snapshots.list `  
  
AI Platform 데이터 라벨링 서비스  |  추가됨  |  ` datalabeling.annotateddatasets.delete `  
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
  
AI Platform 데이터 라벨링 서비스  |  커스텀 역할에서 지원됨  |  `
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
  
Dialogflow  |  추가됨  |  ` dialogflow.agents.update `  
  
Filestore  |  추가됨  |  ` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
  
##  2019년 3월 1일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  역할 업데이트됨  |

` roles/compute.instanceAdmin.v1 ` (Compute 인스턴스 관리자(v1)) 역할에 다음 권한이 추가되었습니다.

` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Dataproc  |  역할 추가됨  |

` roles/dataproc.admin ` (Dataproc 관리자) 역할에 다음 권한이 추가되었습니다.

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
  
기본 역할  |  역할 업데이트됨  |

` roles/editor ` (편집자) 역할에 다음 권한이 추가되었습니다.

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
Cloud ID 및 액세스 관리  |  역할 업데이트됨  |

` roles/iam.serviceAccountDeleter ` (서비스 계정 삭제) 역할에 다음 권한이 추가되었습니다.

` iam.serviceAccounts.get `  
` iam.serviceAccounts.list `  
  
기본 역할  |  역할 업데이트됨  |

` roles/viewer ` (뷰어) 역할에 다음 권한이 추가되었습니다.

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
자동 ML  |  추가됨  |  ` automl.columnSpecs.get `  
` automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.export `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
자동 ML  |  커스텀 역할에서 지원됨  |  ` automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.deploy `  
` automl.models.export `  
` automl.models.undeploy `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
Compute Engine  |  추가됨  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  2019년 2월 15일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Access Context Manager  |  현재 GA  |

` roles/accesscontextmanager.policyAdmin ` (Access Context Manager 관리자) 역할 일반
안정화 버전이 출시되었습니다.  
  
Access Context Manager  |  현재 GA  |

` roles/accesscontextmanager.policyEditor ` (Access Context Manager 편집자) 역할 일반
안정화 버전이 출시되었습니다.  
  
Access Context Manager  |  현재 GA  |

` roles/accesscontextmanager.policyReader ` (Access Context Manager 리더) 역할 일반
안정화 버전이 출시되었습니다.  
  
Talent Solution  |  역할 추가됨  |

` roles/cloudjobdiscovery.profilesEditor ` (프로필 편집자) 역할에 다음 권한이 추가되었습니다.

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
  
Talent Solution  |  역할 추가됨  |

` roles/cloudjobdiscovery.profilesViewer ` (프로필 뷰어) 역할에 다음 권한이 추가되었습니다.

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
기본 역할  |  역할 업데이트됨  |

` roles/editor ` (편집자) 역할에 다음 권한이 추가되었습니다.

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
기본 역할  |  역할 업데이트됨  |

` roles/owner ` (소유자) 역할에 다음 권한이 추가되었습니다.

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
기본 역할  |  역할 업데이트됨  |

` roles/viewer ` (뷰어) 역할에 다음 권한이 추가되었습니다.

` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
  
Google Cloud 작업 도구 모음  |  역할 업데이트됨  |

` roles/stackdriver.accounts.editor ` (Stackdriver 계정 편집자) 역할에 다음 권한이 추가되었습니다.

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Google Cloud 작업 도구 모음  |  역할 업데이트됨  |

` roles/stackdriver.accounts.viewer ` (Stackdriver 계정 뷰어) 역할에 다음 권한이 추가되었습니다.

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Access Context Manager  |  커스텀 역할에서 지원됨  |  `
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
  
Access Context Manager  |  현재 GA  |  `
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
  
Talent Solution  |  추가됨  |  ` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
  
##  2019년 2월 8일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
보안센터  |  커스텀 역할에서 지원됨  |  ` securitycenter.assets.group `  
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
  
  
##  2019년 2월 1일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Dialogflow  |  현재 GA  |

` roles/dialogflow.admin ` (Dialogflow API 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Dialogflow  |  현재 GA  |

` roles/dialogflow.client ` (Dialogflow API 클라이언트) 역할 일반 안정화 버전이 출시되었습니다.  
  
Dialogflow  |  현재 GA  |

` roles/dialogflow.consoleAgentEditor ` (Dialogflow 콘솔 에이전트 편집자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Dialogflow  |  현재 GA  |

` roles/dialogflow.reader ` (Dialogflow API 리더) 역할 일반 안정화 버전이 출시되었습니다.  
  
클라우드 애셋 인벤토리  |  추가됨  |  ` cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
클라우드 애셋 인벤토리  |  커스텀 역할에서 지원됨  |  ` cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
클라우드 애셋 인벤토리  |  현재 GA  |  ` cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Dialogflow  |  커스텀 역할에서 지원됨  |  ` dialogflow.agents.search `  
` dialogflow.agents.train `  
  
Dialogflow  |  현재 GA  |  ` dialogflow.agents.export `  
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
  
  
##  2019년 1월 25일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  추가됨  |  ` compute.instances.updateDisplayDevice `  
  
  
##  2019년 1월 11일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
IAP(Identity-Aware Proxy)  |  현재 GA  |

` roles/iap.admin ` (IAP 정책 관리자)가 역할 일반 안정화 버전이 출시되었습니다.  
  
IAP(Identity-Aware Proxy)  |  커스텀 역할에서 지원됨  |  ` iap.web.getIamPolicy `  
` iap.web.setIamPolicy `  
` iap.webServiceVersions.accessViaIAP `  
` iap.webServiceVersions.getIamPolicy `  
` iap.webServiceVersions.setIamPolicy `  
` iap.webServices.getIamPolicy `  
` iap.webServices.setIamPolicy `  
` iap.webTypes.getIamPolicy `  
` iap.webTypes.setIamPolicy `  
  
  
##  2018년 12월 21일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
클라우드 DNS  |  추가됨  |  ` dns.networks.bindPrivateDNSZone `  
  
클라우드 DNS  |  커스텀 역할에서 지원됨  |  ` dns.networks.bindPrivateDNSZone `  
  
  
##  2018년 12월 14일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Firebase 인증  |  추가됨  |  ` firebaseauth.configs.create `  
  
Firebase 인증  |  커스텀 역할에서 지원됨  |  ` firebaseauth.configs.create `  
  
  
##  2018년 12월 7일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
BigQuery  |  추가됨  |  ` bigquery.readsessions.create `  
  
BigQuery  |  커스텀 역할에서 지원됨  |  ` bigquery.readsessions.create `  
  
Google Kubernetes Engine  |  커스텀 역할에서 지원됨  |  `
container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
Google Kubernetes Engine  |  현재 GA  |  ` container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  2018년 11월 30일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
클라우드 애셋 인벤토리  |  현재 GA  |

` roles/cloudasset.viewer ` (Cloud 애셋 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
클라우드 애셋 인벤토리  |  현재 GA  |  ` cloudasset.assets.exportAll `  
  
Compute Engine  |  추가됨  |  ` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.disks.getIamPolicy `  
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
  
Compute Engine  |  현재 GA  |  ` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
` compute.subnetworks.getIamPolicy `  
` compute.subnetworks.setIamPolicy `  
  
  
##  2018년 11월 16일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
자동 ML  |  추가됨  |  ` automl.locations.getIamPolicy `  
` automl.locations.setIamPolicy `  
  
자동 ML  |  커스텀 역할에서 지원됨  |  ` automl.locations.getIamPolicy `  
` automl.locations.setIamPolicy `  
  
Talent Solution  |  추가됨  |  ` cloudjobdiscovery.events.create `  
` cloudjobdiscovery.events.delete `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.events.update `  
  
Compute Engine  |  추가됨  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  현재 GA  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Google Kubernetes Engine  |  추가됨  |  ` container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  2018년 11월 9일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Google 애널리틱스  |  추가됨  |  ` firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
Google 애널리틱스  |  커스텀 역할에서 지원됨  |  `
firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
  
##  2018년 11월 2일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  현재 GA  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  커스텀 역할에서 지원됨  |  ` file.instances.create `  
` file.instances.delete `  
` file.instances.get `  
` file.instances.list `  
` file.instances.update `  
` file.locations.get `  
` file.locations.list `  
` file.operations.get `  
` file.operations.list `  
  
Google Cloud 작업 도구 모음  |  추가됨  |  ` stackdriver.resourceMetadata.write `  
  
Google Cloud 작업 도구 모음  |  커스텀 역할에서 지원됨  |  `
stackdriver.resourceMetadata.write `  
  
  
##  2018년 10월 26일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
BigQuery  |  현재 GA  |

` roles/bigquery.metadataViewer ` (BigQuery 메타데이터 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud ID 및 액세스 관리  |  현재 GA  |

` roles/iam.serviceAccountDeleter ` (서비스 계정 삭제) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase 실시간 데이터베이스  |  추가됨  |  ` firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
Firebase 실시간 데이터베이스  |  커스텀 역할에서 지원됨  |  ` firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
외부 서비스와 Firebase 통합  |  추가됨  |  ` firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
외부 서비스와 Firebase 통합  |  커스텀 역할에서 지원됨  |  ` firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
  
##  2018년 10월 19일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Google Cloud 지원  |  현재 GA  |

` roles/cloudsupport.admin ` (지원 계정 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Google Cloud 지원  |  현재 GA  |

` roles/cloudsupport.viewer ` (지원 계정 뷰어) 역할 일반 안정화 버전이 출시되었습니다.  
  
Firebase 원격 구성  |  추가됨  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Firebase 원격 구성  |  커스텀 역할에서 지원됨  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Google Cloud 지원  |  커스텀 역할에서 지원됨  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Google Cloud 지원  |  현재 GA  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Compute Engine  |  추가됨  |  ` compute.networks.updatePeering `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.networks.updatePeering `  
  
Firebase Crashlytics  |  추가됨  |  ` firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase Crashlytics  |  커스텀 역할에서 지원됨  |  ` firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase 동적 링크  |  추가됨  |  ` firebasedynamiclinks.destinations.list `  
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
  
Firebase 동적 링크  |  커스텀 역할에서 지원됨  |  ` firebasedynamiclinks.destinations.list `  
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
  
Firebase 인앱 메시지  |  추가됨  |  ` firebaseinappmessaging.campaigns.create `  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Firebase 인앱 메시지  |  커스텀 역할에서 지원됨  |  ` firebaseinappmessaging.campaigns.create
`  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Firebase 클라우드 메시징  |  추가됨  |  ` firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase 클라우드 메시징  |  커스텀 역할에서 지원됨  |  ` firebasenotifications.messages.create
`  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase 성능 모니터링  |  추가됨  |  ` firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase 성능 모니터링  |  커스텀 역할에서 지원됨  |  ` firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase 예측  |  추가됨  |  ` firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
Firebase 예측  |  커스텀 역할에서 지원됨  |  ` firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
보안센터  |  추가됨  |  ` securitycenter.assets.get `  
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
  
서비스 소비자 관리  |  추가됨  |  ` serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
서비스 소비자 관리  |  커스텀 역할에서 지원됨  |  `
serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
  
##  2018년 10월 12일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.admin ` (DLP 관리자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.analyzeRiskTemplatesEditor ` (DLP 위험 분석 템플릿 편집자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.analyzeRiskTemplatesReader ` (DLP 위험 관리 템플릿 리더) 역할 일반 안정화 버전이
출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.deidentifyTemplatesEditor ` (DLP 익명화 템플릿 편집자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.deidentifyTemplatesReader ` (DLP 익명화 템플릿 리더) 역할 일반 안정화 버전이
출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.inspectTemplatesEditor ` (DLP 검사 템플릿 편집자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.inspectTemplatesReader ` (DLP 검사 템플릿 리더) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.jobsEditor ` (DLP 작업 편집자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.jobsReader ` (DLP 작업 리더) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.jobTriggersEditor ` (DLP 작업 트리거 편집자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.jobTriggersReader ` (DLP 작업 트리거 리더) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.reader ` (DLP 리더) 역할 일반 안정화 버전이 출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.storedInfoTypesEditor ` (DLP 저장 InfoType 편집자) 역할 일반 안정화 버전이
출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.storedInfoTypesReader ` (DLP 저장 InfoType 리더) 역할 일반 안정화 버전이
출시되었습니다.  
  
Cloud Data Loss Prevention  |  현재 GA  |

` roles/dlp.user ` (DLP 사용자) 역할 일반 안정화 버전이 출시되었습니다.  
  
Google Kubernetes Engine  |  커스텀 역할에서 지원됨  |  `
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
  
Cloud Data Loss Prevention  |  커스텀 역할에서 지원됨  |  `
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
  
Cloud Data Loss Prevention  |  현재 GA  |  ` dlp.analyzeRiskTemplates.create `  
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
  
클라우드 DNS  |  커스텀 역할에서 지원됨  |  ` dns.dnsKeys.get `  
` dns.dnsKeys.list `  
` dns.managedZoneOperations.get `  
` dns.managedZoneOperations.list `  
` dns.managedZones.update `  
  
Firebase  |  추가됨  |  ` firebase.billingPlans.get `  
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
  
Firebase  |  커스텀 역할에서 지원됨  |  ` firebase.billingPlans.get `  
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
  
Firebase A/B 테스팅  |  추가됨  |  ` firebaseabt.experimentresults.get `  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Firebase A/B 테스팅  |  커스텀 역할에서 지원됨  |  ` firebaseabt.experimentresults.get `  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Firebase 인증  |  추가됨  |  ` firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase 인증  |  커스텀 역할에서 지원됨  |  ` firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase 실시간 데이터베이스  |  추가됨  |  ` firebasedatabase.instances.get `  
` firebasedatabase.instances.update `  
  
Firebase 실시간 데이터베이스  |  커스텀 역할에서 지원됨  |  ` firebasedatabase.instances.get `  
` firebasedatabase.instances.update `  
  
Firebase 호스팅  |  추가됨  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase 호스팅  |  커스텀 역할에서 지원됨  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase용 ML Kit  |  추가됨  |  ` firebaseml.compressionjobs.create `  
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
  
Firebase용 ML Kit  |  커스텀 역할에서 지원됨  |  ` firebaseml.compressionjobs.create `  
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
  
Firebase 보안 규칙  |  추가됨  |  ` firebaserules.releases.create `  
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
  
Firebase 보안 규칙  |  커스텀 역할에서 지원됨  |  ` firebaserules.releases.create `  
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
  
  
##  2018년 10월 5일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  추가됨  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  현재 GA  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Google Kubernetes Engine  |  커스텀 역할에서 지원됨  |  `
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
  
Google Kubernetes Engine  |  현재 GA  |  ` container.cronJobs.getStatus `  
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
  
  
##  2018년 9월 21일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
자동 ML  |  추가됨  |  ` automl.datasets.getIamPolicy `  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
자동 ML  |  커스텀 역할에서 지원됨  |  ` automl.datasets.getIamPolicy `  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
클라우드 애셋 인벤토리  |  추가됨  |  ` cloudasset.assets.exportAll `  
  
클라우드 애셋 인벤토리  |  커스텀 역할에서 지원됨  |  ` cloudasset.assets.exportAll `  
  
Compute Engine  |  추가됨  |  ` compute.licenses.delete `  
  
Google Kubernetes Engine  |  커스텀 역할에서 지원됨  |  ` container.apiServices.create `  
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
  
  
##  2018년 9월 7일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Redis용 Memorystore  |  커스텀 역할에서 지원됨  |  ` redis.operations.cancel `  
` redis.operations.delete `  
  
  
##  2018년 8월 31일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Google Kubernetes Engine  |  추가됨  |  ` container.cronJobs.getStatus `  
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
  
Cloud Data Loss Prevention  |  추가됨  |  ` dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud Data Loss Prevention  |  커스텀 역할에서 지원됨  |  ` dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud Source Repositories  |  추가됨  |  ` source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud Source Repositories  |  커스텀 역할에서 지원됨  |  ` source.repos.getProjectConfig
`  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud Source Repositories  |  현재 GA  |  ` source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
  
##  2018년 8월 10일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
바이너리 승인  |  추가됨  |  ` binaryauthorization.attestors.verifyImageAttested `  
  
바이너리 승인  |  커스텀 역할에서 지원됨  |  `
binaryauthorization.attestors.verifyImageAttested `  
  
Compute Engine  |  추가됨  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  추가됨  |  ` file.instances.create `  
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
  
  
##  2018년 8월 3일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Android Management API  |  커스텀 역할에서 지원됨  |  `
androidmanagement.enterprises.manage `  
  
Android Management API  |  현재 GA  |  ` androidmanagement.enterprises.manage `  
  
클라우드 결제  |  커스텀 역할에서 지원됨  |  ` billing.resourceCosts.get `  
  
바이너리 승인  |  추가됨  |  ` binaryauthorization.policy.get `  
` binaryauthorization.policy.getIamPolicy `  
` binaryauthorization.policy.setIamPolicy `  
` binaryauthorization.policy.update `  
  
Cloud Composer  |  현재 GA  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Compute Engine  |  현재 GA  |  ` compute.nodeGroups.addNodes `  
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
  
Google Kubernetes Engine  |  현재 GA  |  ` container.hostServiceAgent.use `  
  
Redis용 Memorystore  |  추가됨  |  ` redis.operations.cancel `  
  
Redis용 Memorystore  |  커스텀 역할에서 지원됨  |  ` redis.instances.create `  
` redis.instances.delete `  
` redis.instances.get `  
` redis.instances.list `  
` redis.instances.update `  
` redis.locations.get `  
` redis.locations.list `  
` redis.operations.get `  
` redis.operations.list `  
  
Google을 통한 구독  |  추가됨  |  ` subscribewithgoogledeveloper.tools.get `  
  
Google을 통한 구독  |  커스텀 역할에서 지원됨  |  ` subscribewithgoogledeveloper.tools.get `  
  
  
##  2018년 7월 20일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Access Context Manager  |  추가됨  |  ` accesscontextmanager.accessLevels.create
`  
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
  
자동 ML  |  추가됨  |  ` automl.annotationSpecs.create `  
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
  
자동 ML  |  커스텀 역할에서 지원됨  |  ` automl.annotationSpecs.create `  
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
  
바이너리 승인  |  추가됨  |  ` binaryauthorization.attestors.create `  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
바이너리 승인  |  커스텀 역할에서 지원됨  |  ` binaryauthorization.attestors.create `  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
클라우드 DNS  |  커스텀 역할에서 지원됨  |  ` dns.changes.create `  
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
  
  
##  2018년 7월 13일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
BigQuery  |  추가됨  |  ` bigquery.datasets.getIamPolicy `  
` bigquery.datasets.setIamPolicy `  
  
데이터 저장소  |  추가됨  |  ` datastore.locations.get `  
` datastore.locations.list `  
  
  
##  2018년 7월 6일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud Composer  |  커스텀 역할에서 지원됨  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Endpoints  |  추가됨  |  ` endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud Endpoints  |  커스텀 역할에서 지원됨  |  ` endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud TPU  |  추가됨  |  ` tpu.acceleratortypes.get `  
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
  
Cloud TPU  |  커스텀 역할에서 지원됨  |  ` tpu.acceleratortypes.get `  
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
  
  
##  2018년 6월 29일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud Identity and Access Management  |  현재 GA  |  `
iam.serviceAccounts.implicitDelegation `  
  
  
##  2018년 6월 15일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.backendServices.create `  
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
  
Compute Engine  |  현재 GA  |  ` compute.regionBackendServices.create `  
` compute.regionBackendServices.delete `  
` compute.regionBackendServices.get `  
` compute.regionBackendServices.list `  
` compute.regionBackendServices.setSecurityPolicy `  
` compute.regionBackendServices.update `  
` compute.regionBackendServices.use `  
  
  
##  2018년 6월 8일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  추가됨  |  ` compute.nodeGroups.addNodes `  
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
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.nodeGroups.addNodes `  
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
  
  
##  2018년 5월 11일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
BigQuery  |  커스텀 역할에서 지원됨  |  ` bigquery.jobs.listAll `  
  
Cloud Bigtable  |  커스텀 역할에서 지원됨  |  ` bigtable.appProfiles.create `  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.clusters.create `  
` bigtable.clusters.delete `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Bigtable  |  현재 GA  |  ` bigtable.appProfiles.create `  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Composer  |  현재 베타  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Life Sciences  |  커스텀 역할에서 지원됨  |  ` genomics.operations.cancel `  
` genomics.operations.create `  
` genomics.operations.get `  
` genomics.operations.list `  
  
Cloud Monitoring  |  커스텀 역할에서 지원됨  |  ` monitoring.dashboards.create `  
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
  
Cloud Monitoring  |  현재 GA  |  ` monitoring.dashboards.create `  
` monitoring.dashboards.delete `  
` monitoring.dashboards.get `  
` monitoring.dashboards.list `  
` monitoring.dashboards.update `  
` monitoring.publicWidgets.create `  
` monitoring.publicWidgets.delete `  
` monitoring.publicWidgets.get `  
` monitoring.publicWidgets.list `  
` monitoring.publicWidgets.update `  
  
  
##  2018년 5월 4일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
BigQuery  |  커스텀 역할에서 사용 가능  |  ` bigquery.jobs.listAll `  
  
Cloud Bigtable  |  추가됨  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  커스텀 역할에서 지원됨  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  현재 GA  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  현재 GA  |  ` compute.oslogin.updateExternalUser `  
  
서비스 관리  |  커스텀 역할에서 지원됨  |  ` servicemanagement.services.bind `  
  
  
##  2018년 4월 6일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  커스텀 역할에서 지원됨  |  `
compute.instances.setShieldedVmIntegrityPolicy `  
` compute.instances.updateShieldedVmConfig `  
  
Compute Engine  |  현재 GA  |  ` compute.instances.setShieldedVmIntegrityPolicy
`  
  
Google Kubernetes Engine  |  커스텀 역할에서 지원됨  |  ` container.hostServiceAgent.use
`  
  
Dataproc  |  커스텀 역할에서 지원됨  |  ` dataproc.jobs.getIamPolicy `  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
Dataproc  |  현재 GA  |  ` dataproc.jobs.getIamPolicy `  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
  
##  2018년 3월 30일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud IoT  |  현재 GA  |  ` cloudiot.devices.create `  
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
  
  
##  2018년 3월 23일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud Life Sciences  |  커스텀 역할에서 지원됨  |  ` genomics.datasets.create `  
` genomics.datasets.delete `  
` genomics.datasets.get `  
` genomics.datasets.getIamPolicy `  
` genomics.datasets.list `  
` genomics.datasets.setIamPolicy `  
` genomics.datasets.update `  
  
게시/구독  |  커스텀 역할에서 지원됨  |  ` pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.list `  
  
  
##  2018년 3월 9일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Talent Solution  |  추가됨  |  ` cloudjobdiscovery.companies.create `  
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
  
Talent Solution  |  커스텀 역할에서 지원됨  |  ` cloudjobdiscovery.companies.create `  
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
  
Cloud Profiler  |  추가됨  |  ` cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
Cloud Profiler  |  커스텀 역할에서 지원됨  |  ` cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
  
##  2018년 3월 2일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Google Cloud용 서비스 브로커 열기  |  추가됨  |  ` servicebroker.bindingoperations.get `  
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
  
Google Cloud용 서비스 브로커 열기  |  커스텀 역할에서 지원됨  |  `
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
  
  
##  2018년 2월 23일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
리소스 관리자  |  커스텀 역할에서 지원됨  |  ` resourcemanager.projects.list `  
` resourcemanager.projects.move `  
  
서비스 관리  |  추가됨  |  ` servicemanagement.services.quota `  
  
서비스 관리  |  커스텀 역할에서 지원됨  |  ` servicemanagement.services.quota `  
  
Cloud Source Repositories  |  커스텀 역할에서 지원됨  |  ` source.repos.create `  
  
  
##  2018년 2월 16일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
BigQuery  |  커스텀 역할에서 지원됨  |  ` bigquery.tables.update `  
` bigquery.tables.updateData `  
  
Cloud IoT  |  커스텀 역할에서 지원됨  |  ` cloudiot.devices.create `  
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
  
Cloud SQL  |  커스텀 역할에서 지원됨  |  ` cloudsql.instances.demoteMaster `  
  
Google Cloud 지원  |  추가됨  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Compute Engine  |  추가됨  |  ` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.addresses.create `  
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
  
Dataproc  |  커스텀 역할에서 지원됨  |  ` dataproc.agents.create `  
` dataproc.agents.delete `  
` dataproc.agents.get `  
` dataproc.agents.list `  
` dataproc.agents.update `  
` dataproc.tasks.lease `  
` dataproc.tasks.listInvalidatedLeases `  
` dataproc.tasks.reportStatus `  
` dataproc.workflowTemplates.instantiateInline `  
  
클라우드 DNS  |  추가됨  |  ` dns.changes.create `  
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
  
  
##  2018년 2월 2일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  커스텀 역할에서 사용 가능  |  ` compute.interconnectAttachments.create
`  
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
  
Cloud Data Loss Prevention  |  추가됨  |  ` dlp.jobTriggers.create `  
` dlp.jobTriggers.delete `  
` dlp.jobTriggers.get `  
` dlp.jobTriggers.list `  
` dlp.jobTriggers.update `  
  
  
##  2018년 1월 26일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
BigQuery  |  추가됨  |  ` bigquery.jobs.listAll `  
  
Google Kubernetes Engine  |  추가됨  |  ` container.podSecurityPolicies.create `  
` container.podSecurityPolicies.delete `  
` container.podSecurityPolicies.get `  
` container.podSecurityPolicies.list `  
` container.podSecurityPolicies.update `  
` container.podSecurityPolicies.use `  
  
  
##  2018년 1월 19일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  추가됨  |  ` compute.addresses.createInternal `  
` compute.addresses.deleteInternal `  
` compute.addresses.useInternal `  
  
  
##  2018년 1월 12일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
App Engine  |  커스텀 역할에서 지원되지 않음  |  ` appengine.runtimes.actAsAdmin `  
  
Compute Engine  |  추가됨  |  ` compute.backendServices.setSecurityPolicy `  
` compute.securityPolicies.create `  
` compute.securityPolicies.delete `  
` compute.securityPolicies.get `  
` compute.securityPolicies.getIamPolicy `  
` compute.securityPolicies.list `  
` compute.securityPolicies.setIamPolicy `  
` compute.securityPolicies.update `  
` compute.securityPolicies.use `  
  
Compute Engine  |  커스텀 역할에서 지원되지 않음  |  ` compute.organizations.administerXpn
`  
` compute.targetHttpProxies.create `  
` compute.targetHttpProxies.setUrlMap `  
` compute.targetHttpsProxies.create `  
` compute.targetHttpsProxies.setUrlMap `  
` compute.targetSslProxies.create `  
` compute.targetSslProxies.setBackendService `  
` compute.targetTcpProxies.create `  
` compute.targetTcpProxies.update `  
  
Compute Engine  |  현재 GA  |  ` compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
  
  
##  2017년 12월 22일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
App Engine  |  커스텀 역할에서 지원됨  |  ` appengine.applications.create `  
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
  
App Engine  |  커스텀 역할에서 지원되지 않음  |  ` appengine.applications.list `  
` appengine.operations.cancel `  
` appengine.operations.delete `  
` appengine.services.create `  
  
클라우드 결제  |  커스텀 역할에서 지원됨  |  ` billing.accounts.close `  
` billing.accounts.reopen `  
` billing.budgets.delete `  
` billing.budgets.update `  
  
Cloud 디버거  |  커스텀 역할에서 지원됨  |  ` clouddebugger.breakpoints.create `  
` clouddebugger.breakpoints.delete `  
` clouddebugger.breakpoints.get `  
` clouddebugger.breakpoints.list `  
` clouddebugger.breakpoints.listActive `  
` clouddebugger.breakpoints.update `  
` clouddebugger.debuggees.create `  
` clouddebugger.debuggees.list `  
  
Cloud Key Management Service  |  커스텀 역할에서 지원됨  |  `
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
  
Cloud SQL  |  커스텀 역할에서 지원됨  |  ` cloudsql.backupRuns.create `  
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
  
Cloud SQL  |  커스텀 역할에서 지원되지 않음  |  ` cloudsql.databases.getIamPolicy `  
` cloudsql.databases.setIamPolicy `  
` cloudsql.instances.demoteMaster `  
` cloudsql.instances.getIamPolicy `  
` cloudsql.instances.migrate `  
` cloudsql.instances.setIamPolicy `  
` cloudsql.sslCerts.createEphemeral `  
  
Cloud Trace  |  커스텀 역할에서 지원됨  |  ` cloudtrace.insights.get `  
` cloudtrace.insights.list `  
` cloudtrace.stats.get `  
` cloudtrace.tasks.create `  
` cloudtrace.tasks.delete `  
` cloudtrace.tasks.get `  
` cloudtrace.tasks.list `  
` cloudtrace.traces.get `  
` cloudtrace.traces.list `  
` cloudtrace.traces.patch `  
  
Compute Engine  |  추가됨  |  ` compute.instances.setMachineResources `  
` compute.instances.setMinCpuPlatform `  
` compute.instances.setServiceAccount `  
` compute.instances.updateAccessConfig `  
` compute.instances.updateNetworkInterface `  
` compute.licenseCodes.get `  
` compute.licenseCodes.list `  
` compute.licenseCodes.update `  
` compute.licenseCodes.use `  
  
Compute Engine  |  커스텀 역할에서 지원됨  |  ` compute.acceleratorTypes.get `  
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
  
Compute Engine  |  커스텀 역할에서 지원되지 않음  |  ` compute.backendServices.create `  
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
  
Google Kubernetes Engine  |  추가됨  |  ` container.services.updateStatus `  
  
Google Kubernetes Engine  |  커스텀 역할에서 지원됨  |  ` container.clusters.create `  
` container.clusters.delete `  
` container.clusters.get `  
` container.clusters.getCredentials `  
` container.clusters.list `  
` container.clusters.update `  
` container.operations.get `  
` container.operations.list `  
  
Dataproc  |  커스텀 역할에서 지원됨  |  ` dataproc.clusters.create `  
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
  
데이터 저장소  |  커스텀 역할에서 지원되지 않음  |  ` datastore.databases.create `  
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
  
Cloud Deployment Manager  |  커스텀 역할에서 지원됨  |  `
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
  
Dialogflow  |  커스텀 역할에서 지원됨  |  ` dialogflow.agents.export `  
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
  
오류 보고  |  커스텀 역할에서 지원됨  |  ` errorreporting.applications.list `  
` errorreporting.errorEvents.create `  
` errorreporting.errorEvents.delete `  
` errorreporting.errorEvents.list `  
` errorreporting.groupMetadata.get `  
` errorreporting.groupMetadata.update `  
` errorreporting.groups.list `  
  
Cloud Identity and Access Management  |  커스텀 역할에서 지원되지 않음  |  `
iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
Cloud 로깅  |  커스텀 역할에서 지원됨  |  ` logging.exclusions.create `  
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
  
AI 플랫폼  |  커스텀 역할에서 지원됨  |  ` ml.jobs.cancel `  
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
  
Cloud Monitoring  |  커스텀 역할에서 지원됨  |  ` monitoring.groups.create `  
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
  
게시/구독  |  커스텀 역할에서 지원됨  |  ` pubsub.topics.setIamPolicy `  
  
서비스 관리  |  커스텀 역할에서 지원됨  |  ` servicemanagement.services.check `  
` servicemanagement.services.report `  
  
서비스 관리  |  커스텀 역할에서 지원되지 않음  |  ` servicemanagement.consumerSettings.get `  
` servicemanagement.consumerSettings.getIamPolicy `  
` servicemanagement.consumerSettings.list `  
` servicemanagement.consumerSettings.setIamPolicy `  
` servicemanagement.consumerSettings.update `  
  
Cloud Source Repositories  |  커스텀 역할에서 지원됨  |  ` source.repos.delete `  
` source.repos.get `  
` source.repos.getIamPolicy `  
` source.repos.list `  
` source.repos.setIamPolicy `  
  
Cloud Source Repositories  |  커스텀 역할에서 지원되지 않음  |  ` source.repos.update `  
  
Cloud Spanner  |  커스텀 역할에서 지원됨  |  ` spanner.databaseOperations.cancel `  
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
  
Cloud Spanner  |  커스텀 역할에서 지원되지 않음  |  ` spanner.databaseOperations.delete `  
` spanner.databases.update `  
  
Cloud Storage  |  커스텀 역할에서 지원됨  |  ` storage.buckets.create `  
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
  
  
##  2017년 12월 8일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
BigQuery  |  커스텀 역할에서 지원됨  |  ` bigquery.datasets.create `  
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
  
BigQuery  |  커스텀 역할에서 지원되지 않음  |  ` bigquery.config.get `  
` bigquery.config.update `  
` bigquery.service.actAsSuperuser `  
` bigquery.tables.update `  
` bigquery.tables.updateData `  
` bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Cloud Bigtable  |  커스텀 역할에서 지원됨  |  ` bigtable.clusters.get `  
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
  
Compute Engine  |  추가됨  |  ` compute.disks.getIamPolicy `  
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
  
Dataflow  |  커스텀 역할에서 지원됨  |  ` dataflow.jobs.cancel `  
` dataflow.jobs.create `  
` dataflow.jobs.get `  
` dataflow.jobs.list `  
` dataflow.jobs.updateContents `  
` dataflow.messages.list `  
` dataflow.metrics.get `  
  
Dataproc  |  추가됨  |  ` dataproc.workflowTemplates.instantiateInline `  
  
Cloud Data Loss Prevention  |  추가됨  |  ` dlp.analyzeRiskTemplates.create `  
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
  
게시/구독  |  추가됨  |  ` pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.get `  
` pubsub.snapshots.getIamPolicy `  
` pubsub.snapshots.list `  
` pubsub.snapshots.seek `  
` pubsub.snapshots.setIamPolicy `  
` pubsub.snapshots.update `  
  
게시/구독  |  커스텀 역할에서 지원됨  |  ` pubsub.subscriptions.consume `  
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
  
  
##  2017년 12월 1일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud 빌드  |  커스텀 역할에서 지원됨  |  ` cloudbuild.builds.create `  
` cloudbuild.builds.get `  
` cloudbuild.builds.list `  
` cloudbuild.builds.update `  
  
Cloud 도구 결과  |  현재 GA  |  ` cloudtoolresults.executions.create `  
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
  
Compute Engine  |  현재 GA  |  ` compute.instances.addMaintenancePolicies `  
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
  
Google Kubernetes Engine  |  추가됨  |  `
container.initializerConfigurations.create `  
` container.initializerConfigurations.delete `  
` container.initializerConfigurations.get `  
` container.initializerConfigurations.list `  
` container.initializerConfigurations.update `  
` container.pods.initialize `  
  
Google Kubernetes Engine  |  현재 GA  |  ` container.deployments.getScale `  
` container.deployments.updateScale `  
  
Trifacta 제공 Dataprep  |  커스텀 역할에서 지원됨  |  ` dataprep.projects.use `  
  
Cloud Identity and Access Management  |  커스텀 역할에서 지원됨  |  ` iam.roles.create `  
` iam.roles.delete `  
` iam.roles.get `  
` iam.roles.list `  
` iam.roles.undelete `  
` iam.roles.update `  
  
  
##  2017년 11월 10일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Google Kubernetes Engine  |  추가됨  |  ` container.clusters.getIamPolicy `  
` container.clusters.setIamPolicy `  
  
AI 플랫폼  |  추가됨  |  ` ml.locations.get `  
` ml.locations.list `  
  
Cloud Monitoring  |  추가됨  |  ` monitoring.metricDescriptors.update `  
  
  
##  2017년 10월 27일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Compute Engine  |  추가됨  |  ` compute.instances.updateShieldedVmConfig `  
  
IAP(Identity-Aware Proxy)  |  추가됨  |  ` iap.web.getIamPolicy `  
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
  
서비스 관리  |  커스텀 역할에서 지원됨  |  ` servicemanagement.services.create `  
` servicemanagement.services.delete `  
` servicemanagement.services.get `  
` servicemanagement.services.getIamPolicy `  
` servicemanagement.services.list `  
` servicemanagement.services.setIamPolicy `  
` servicemanagement.services.update `  
  
  
##  2017년 10월 6일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Dataproc  |  현재 GA  |  ` dataproc.workflowTemplates.create `  
` dataproc.workflowTemplates.delete `  
` dataproc.workflowTemplates.get `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.instantiate `  
` dataproc.workflowTemplates.list `  
` dataproc.workflowTemplates.setIamPolicy `  
` dataproc.workflowTemplates.update `  
  
  
##  2017년 9월 22일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
App Engine  |  추가됨  |  ` appengine.memcache.addKey `  
` appengine.memcache.flush `  
` appengine.memcache.get `  
` appengine.memcache.getKey `  
` appengine.memcache.list `  
` appengine.memcache.update `  
  
Cloud SQL  |  추가됨  |  ` cloudsql.instances.demoteMaster `  
  
Cloud SQL  |  현재 GA  |  ` cloudsql.instances.demoteMaster `  
  
  
##  2017년 9월 8일 기준 Cloud IAM 변경사항

서비스  |  변경  |  설명  
---|---|---  
Cloud 함수  |  추가됨  |  ` cloudfunctions.functions.call `  
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
  
Compute Engine  |  추가됨  |  ` compute.instances.setDeletionProtection `  
` compute.targetHttpsProxies.setUrlMap `  
  
Google Kubernetes Engine  |  추가됨  |  ` container.statefulSets.getScale `  
` container.statefulSets.updateScale `  
  
Google Kubernetes Engine  |  현재 GA  |  ` container.statefulSets.getScale `  
` container.statefulSets.updateScale `  
  
Cloud 함수  |  추가됨  |  ` dlp.kms.encrypt `  
` dlp.riskAnalysisOperations.cancel `  
` dlp.riskAnalysisOperations.create `  
` dlp.riskAnalysisOperations.get `  
` dlp.riskAnalysisOperations.list `  

