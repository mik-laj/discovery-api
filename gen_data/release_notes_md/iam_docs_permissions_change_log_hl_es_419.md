#  Registro de cambios de permisos de IAM

En esta página se describen los cambios en los permisos públicos de Cloud IAM
para todos los servicios Beta y de disponibilidad general en Google Cloud.
Este registro de cambios puede servirte de ayuda para mantener y solucionar
problemas en tus [ funciones personalizadas
](https://cloud.google.com/iam/docs/understanding-custom-roles?hl=es_419) .

Cuando se quita un permiso o deja de ser compatible con las funciones
personalizadas, Cloud IAM lo quita automáticamente de estas. En cambio, cuando
se agrega un permiso, Cloud IAM _no_ lo agrega automáticamente a tus funciones
personalizadas.

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) o agrega
directamente la URL del feed: ` https://cloud.google.com/feeds/cloud-iam-
permissions-change-log.xml ` .

Registro de cambios de permisos de IAM

##  Próximos cambios que se aplicarán en Cloud IAM la semana del 02/03/2020

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/compute.networkAdmin
` (Administrador de red de Compute):

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/compute.networkViewer ` (Compute Network Viewer):

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/editor ` (Editor):

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
  
Cloud Identity and Access Management  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/iam.securityAdmin `
(Administrador de seguridad):

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
Cloud Identity and Access Management  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/iam.securityReviewer
` (Revisor de seguridad):

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
Identity Platform  |  Se agregó una función  |

La función ` roles/identityplatform.admin ` (Administrador de plataforma de
Identity) se agregó con los siguientes permisos:

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
  
Identity Platform  |  Se agregó una función  |

La función ` roles/identityplatform.viewer ` (Identity Platform Viewer) se
agregó con los siguientes permisos:

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
  
API de administración de redes  |  Ahora en etapa de disponibilidad general  |

La función ` roles/networkmanagement.admin ` (Administrador de administración
de red) ahora es Google Analytics.  
  
API de administración de redes  |  Ahora en etapa de disponibilidad general  |

La función ` roles/networkmanagement.viewer ` (Visor de administración de red)
ahora es Google Analytics.  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/owner `
(Propietario):

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
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/viewer `
(Visualizador):

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.get `  
` servicedirectory.locations.list `  
  
BigQuery  |  Agregado  |  ` bigquery.bireservations.get `  
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
  
BigQuery  |  Compatible con funciones personalizadas  |  `
bigquery.bireservations.get `  
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
  
Identity Platform  |  Agregado  |  `
identityplatform.workloadPoolProviders.create `  
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
  
API de administración de redes  |  Ahora en etapa de disponibilidad general  |
` networkmanagement.connectivitytests.create `  
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
  
Memorystore for Redis  |  Agregado  |  ` redis.instances.failover `  
` redis.instances.upgrade `  
  
Memorystore for Redis  |  Compatible con funciones personalizadas  |  `
redis.instances.failover `  
` redis.instances.upgrade `  
  
Directorio de servicios  |  Agregado  |  ` servicedirectory.endpoints.create `  
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
  
Directorio de servicios  |  Compatible con funciones personalizadas  |  `
servicedirectory.endpoints.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 27/02/2020

Servicio  |  Cambio  |  Descripción  
---|---|---  
BigQuery  |  Ahora en etapa de disponibilidad general  |

La función ` roles/bigquery.readSessionUser ` (usuario de la sesión de lectura
de BigQuery) ahora es Google Analytics.  
  
Data Catalog  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/datacatalog.entryGroupCreator ` (DataCatalog EntryGroup Creator):

` datacatalog.entryGroups.list `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/editor ` (Editor):

` dlp.jobs.create `  
` dlp.jobs.get `  
` dlp.jobs.list `  
  
Administrador de secretos  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/secretmanager.secretAccessor ` (Administrador y descriptor de acceso a
secretos):

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Security Command Center  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/securitycenter.adminEditor ` (Editor administrador del centro de
seguridad):

` securitycenter.organizationsettings.get `  
  
Security Command Center  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/securitycenter.adminViewer ` (Visualizador administrador del centro de
seguridad):

` securitycenter.organizationsettings.get `  
  
Cloud Spanner  |  Ahora en etapa de disponibilidad general  |

La función ` roles/spanner.backupAdmin ` (Administrador de copia de seguridad
de Cloud Spanner) ahora es Google Analytics.  
  
Cloud Spanner  |  Ahora en etapa de disponibilidad general  |

La función ` roles/spanner.backupWriter ` (escritor de copia de seguridad de
Cloud Spanner) ahora es Google Analytics.  
  
Cloud Spanner  |  Ahora en etapa de disponibilidad general  |

La función ` roles/spanner.restoreAdmin ` (Administrador de restauración de
Cloud Spanner) ahora es Google Analytics.  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/viewer `
(Visualizador):

` dlp.jobs.get `  
` dlp.jobs.list `  
  
BigQuery  |  Agregado  |  ` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  Compatible con funciones personalizadas  |  `
bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  Ahora en etapa de disponibilidad general  |  `
bigquery.readsessions.create `  
` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
Data Catalog  |  Agregado  |  ` datacatalog.entryGroups.list `  
  
Data Catalog  |  Compatible con funciones personalizadas  |  `
datacatalog.entryGroups.list `  
  
Cloud Healthcare API  |  Compatible con funciones personalizadas  |  `
healthcare.fhirStores.executeBundle `  
  
Cloud Identity and Access Management  |  Compatible con funciones
personalizadas  |  ` iam.serviceAccounts.getOpenIdToken `  
  
Cloud Spanner  |  Agregado  |  ` spanner.backupOperations.cancel `  
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
  
Cloud Spanner  |  Compatible con funciones personalizadas  |  `
spanner.backupOperations.cancel `  
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
  
Cloud Spanner  |  Ahora en etapa de disponibilidad general  |  `
spanner.backupOperations.cancel `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 21/02/2020

Servicio  |  Cambio  |  Descripción  
---|---|---  
Access Context Manager  |  Agregado  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Access Context Manager  |  Ahora en etapa de disponibilidad general  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Compute Engine  |  Agregado  |  ` compute.regionHealthCheckServices.create `  
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
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.regionHealthCheckServices.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 14/02/2020

Servicio  |  Cambio  |  Descripción  
---|---|---  
Asistencia de Google Cloud  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudsupport.techSupportEditor ` (Editor de asistencia
técnica) ahora es Google Analytics.  
  
Asistencia de Google Cloud  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudsupport.techSupportViewer ` (Visor de asistencia
técnica) ahora es Google Analytics.  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/editor ` (Editor):

` healthcare.fhirStores.executeBundle `  
  
Cloud Healthcare API  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/healthcare.fhirResourceEditor ` (Editor de recursos FHIR de Healthcare):

` healthcare.fhirStores.executeBundle `  
  
Cloud Healthcare API  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/healthcare.fhirResourceReader ` (Lector de recursos FHIR de Healthcare):

` healthcare.fhirStores.executeBundle `  
  
Cloud Logging  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/logging.privateLogViewer ` (Visualizador de registros privados):

` logging.buckets.get `  
` logging.buckets.list `  
  
Cloud Logging  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/logging.viewer `
(Visualizador de registros):

` logging.buckets.get `  
` logging.buckets.list `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/owner `
(Propietario):

` healthcare.fhirStores.executeBundle `  
  
Security Command Center  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/securitycenter.admin
` (Administrador del centro de seguridad):

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
  
Security Command Center  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/securitycenter.adminEditor ` (Editor administrador del centro de
seguridad):

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
  
Security Command Center  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/securitycenter.adminViewer ` (Visualizador administrador del centro de
seguridad):

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
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/viewer `
(Visualizador):

` healthcare.fhirStores.executeBundle `  
  
Asistencia de Google Cloud  |  Agregado  |  ` cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Asistencia de Google Cloud  |  Compatible con funciones personalizadas  |  `
cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Asistencia de Google Cloud  |  Ahora en etapa de disponibilidad general  |  `
cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Cloud Healthcare API  |  Agregado  |  ` healthcare.fhirStores.executeBundle `  
  
Cloud Logging  |  Agregado  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud Logging  |  Compatible con funciones personalizadas  |  `
logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud Logging  |  Ahora en etapa de disponibilidad general  |  `
logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 07/02/2020

Servicio  |  Cambio  |  Descripción  
---|---|---  
Administrador de secretos  |  Ahora en etapa de disponibilidad general  |

La función ` roles/secretmanager.admin ` (Administrador del administrador de
secretos) ahora es Google Analytics.  
  
Administrador de secretos  |  Ahora en etapa de disponibilidad general  |

La función ` roles/secretmanager.secretAccessor ` (Administrador y descriptor
de acceso a secretos) ahora es Google Analytics.  
  
Administrador de secretos  |  Ahora en etapa de disponibilidad general  |

La función ` roles/secretmanager.viewer ` (Visualizador del administrador de
secretos) ahora es Google Analytics.  
  
Cloud Healthcare API  |  Compatible con funciones personalizadas  |  `
healthcare.datasets.create `  
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
  
reCAPTCHA Enterprise  |  Agregado  |  `
recaptchaenterprise.assessments.annotate `  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
reCAPTCHA Enterprise  |  Compatible con funciones personalizadas  |  `
recaptchaenterprise.assessments.annotate `  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
Administrador de secretos  |  Compatible con funciones personalizadas  |  `
secretmanager.locations.get `  
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
  
Administrador de secretos  |  Ahora en etapa de disponibilidad general  |  `
secretmanager.locations.get `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 31/01/2020

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Build  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudbuild.builds.builder ` (cuenta de servicio de Cloud Build):

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
  
Cloud Composer  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/composer.worker `
(Composer Worker):

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
  
Google Cloud Game Servers  |  Agregado  |  `
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
  
Google Cloud Game Servers  |  Compatible con funciones personalizadas  |  `
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
  
Paquete de operaciones de Google Cloud  |  Agregado  |  `
opsconfigmonitoring.resourceMetadata.write `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 24/01/2020

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Scheduler  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/cloudscheduler.admin
` (Administrador de Cloud Scheduler):

` serviceusage.services.list `  
  
Cloud Scheduler  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudscheduler.jobRunner ` (Ejecutor de trabajos de Cloud Scheduler):

` serviceusage.services.list `  
  
Cloud Scheduler  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudscheduler.viewer ` (Visualizador de Cloud Scheduler):

` serviceusage.services.list `  
  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/compute.networkAdmin
` (Administrador de red de Compute):

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/compute.networkViewer ` (Visualizador de red de Compute):

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.notificationConfigEditor ` (Editor de
configuración de notificaciones del centro de seguridad) ahora es Google
Analytics.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.notificationConfigViewer ` (Visor de
configuraciones de notificaciones del Centro de seguridad) ahora es Google
Analytics.  
  
Artifact Registry  |  Agregado  |  ` artifactregistry.files.get `  
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
  
Artifact Registry  |  Compatible con funciones personalizadas  |  `
artifactregistry.files.get `  
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
  
Cloud Identity and Access Management  |  Agregado  |  `
iam.serviceAccounts.getOpenIdToken `  
  
Security Command Center  |  Agregado  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
Security Command Center  |  Compatible con funciones personalizadas  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 10/01/2020

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Asset Inventory  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudasset.owner ` (Propietario de recursos de Cloud) pasó
a la etapa de disponibilidad general.  
  
Migrate for Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudmigration.inframanager ` (Administrador de Velostrata):

` compute.globalOperations.get `  
  
Cloud Spanner  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/spanner.databaseReader ` (Lector de bases de datos de Cloud Spanner):

` spanner.instances.get `  
  
Cloud Spanner  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/spanner.databaseUser
` (Usuario de bases de datos de Cloud Spanner):

` spanner.instances.get `  
  
Cloud Asset Inventory  |  Ahora en etapa de disponibilidad general  |  `
cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Compute Engine  |  Agregado  |  ` compute.networks.listPeeringRoutes `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.networks.listPeeringRoutes `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.networks.listPeeringRoutes `  
  
API de administración de redes  |  Agregado  |  `
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
  
API de administración de redes  |  Compatible con funciones personalizadas  |
` networkmanagement.connectivitytests.create `  
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
  
  
##  Cambios que se realizaron Cloud IAM hasta el 20/12/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Migrate for Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudmigration.inframanager ` (Administrador de Velostrata):

` compute.disks.createSnapshot `  
` compute.snapshots.create `  
` compute.snapshots.delete `  
` compute.snapshots.get `  
` compute.snapshots.setLabels `  
` compute.snapshots.useReadOnly `  
  
Cloud Scheduler  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/cloudscheduler.admin
` (Administrador de Cloud Scheduler):

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud Scheduler  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudscheduler.jobRunner ` (Ejecutor de trabajos de Cloud Scheduler):

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud Scheduler  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudscheduler.viewer ` (Visualizador de Cloud Scheduler):

` appengine.applications.get `  
` serviceusage.services.get `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |

La función ` roles/compute.packetMirroringAdmin ` (Administrador de
duplicación de paquetes de Compute) pasó a la etapa de disponibilidad general.  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |

La función ` roles/compute.packetMirroringUser ` (Usuario de duplicación de
paquetes de Compute) pasó a la etapa de disponibilidad general.  
  
Cloud DNS  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dns.peer ` (Par de DNS) pasó a la etapa de disponibilidad
general.  
  
Función básica  |  Se actualizó una función  |

Se quitaron los siguientes permisos de la función ` roles/editor ` (Editor):

` datacatalog.taxonomies.create `  
  
Recommender  |  Ahora en etapa de disponibilidad general  |

La función ` roles/recommender.computeAdmin ` (Administrador del recomendador
de Compute) pasó a la etapa de disponibilidad general.  
  
Recommender  |  Ahora en etapa de disponibilidad general  |

La función ` roles/recommender.computeViewer ` (Visualizador del recomendador
de Compute) pasó a la etapa de disponibilidad general.  
  
Recommender  |  Ahora en etapa de disponibilidad general  |

La función ` roles/recommender.iamAdmin ` (Administrador del recomendador de
IAM) pasó a la etapa de disponibilidad general.  
  
Recommender  |  Ahora en etapa de disponibilidad general  |

La función ` roles/recommender.iamViewer ` (Visualizador del recomendador de
IAM) pasó a la etapa de disponibilidad general.  
  
Ejecución de compilación remota  |  Se agregó una función  |

Se agregó la función ` roles/remotebuildexecution.reservationAdmin `
(Administrador de reservas de ejecución de compilación remota) con los
siguientes permisos:

` remotebuildexecution.actions.create `  
` remotebuildexecution.actions.delete `  
` remotebuildexecution.actions.get `  
  
Cloud Bigtable  |  Agregado  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  Compatible con funciones personalizadas  |  `
bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  Ahora en etapa de disponibilidad general  |  `
bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Compute Engine  |  Agregado  |  ` compute.nodeGroups.update `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.nodeGroups.update `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Data Catalog  |  Agregado  |  ` datacatalog.entries.list `  
` datacatalog.entries.updateTag `  
` datacatalog.entryGroups.update `  
  
Dataproc  |  Agregado  |  ` dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
Dataproc  |  Ahora en etapa de disponibilidad general  |  `
dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
Cloud DNS  |  Ahora en etapa de disponibilidad general  |  `
dns.networks.targetWithPeeringZone `  
  
Cloud Logging  |  Agregado  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud Logging  |  Compatible con funciones personalizadas  |  `
logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud Logging  |  Ahora en etapa de disponibilidad general  |  `
logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Recommender  |  Ahora en etapa de disponibilidad general  |  `
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 22/11/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Data Catalog  |  Se actualizó una función  |

Se quitaron los siguientes permisos de la función ` roles/datacatalog.admin `
(Administrador de Data Catalog):

` datacatalog.categories.fineGrainedGet `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/editor ` (Editor):

` remotebuildexecution.actions.delete `  
  
API de Identity Toolkit  |  Ahora en etapa de disponibilidad general  |

La función ` roles/identitytoolkit.admin ` (Administrador de Identity Toolkit)
pasó a la etapa de disponibilidad general.  
  
API de Identity Toolkit  |  Ahora en etapa de disponibilidad general  |

La función ` roles/identitytoolkit.viewer ` (Visualizador de Identity Toolkit)
pasó a la etapa de disponibilidad general.  
  
API de Apigee  |  Agregado  |  ` apigee.apiproductattributes.createOrUpdateAll
`  
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
  
API de Apigee  |  Compatible con funciones personalizadas  |  `
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
  
BigQuery  |  Agregado  |  ` bigquery.tables.setCategory `  
  
Compute Engine  |  Agregado  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Ejecución de compilación remota  |  Agregado  |  `
remotebuildexecution.actions.delete `  
  
Ejecución de compilación remota  |  Compatible con funciones personalizadas  |
` remotebuildexecution.actions.delete `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 14/11/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Aprobación de acceso  |  Agregado  |  ` accessapproval.settings.delete `  
  
AI Platform Notebooks  |  Agregado  |  ` notebooks.environments.create `  
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
  
AI Platform Notebooks  |  Compatible con funciones personalizadas  |  `
notebooks.environments.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 01/11/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
API de Hangouts Chat  |  Ahora en etapa de disponibilidad general  |

La función ` roles/chat.owner ` (Propietario de chat bots) pasó a la etapa de
disponibilidad general.  
  
API de Hangouts Chat  |  Ahora en etapa de disponibilidad general  |

La función ` roles/chat.reader ` (Visualizador de chat bots) pasó a la etapa
de disponibilidad general.  
  
API de Hangouts Chat  |  Ahora en etapa de disponibilidad general  |  `
chat.bots.get `  
` chat.bots.update `  
  
Cloud Asset Inventory  |  Agregado  |  `
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
  
Data Catalog  |  Agregado  |  ` datacatalog.categories.fineGrainedGet `  
` datacatalog.categories.getIamPolicy `  
` datacatalog.categories.setIamPolicy `  
` datacatalog.taxonomies.create `  
` datacatalog.taxonomies.delete `  
` datacatalog.taxonomies.get `  
` datacatalog.taxonomies.getIamPolicy `  
` datacatalog.taxonomies.list `  
` datacatalog.taxonomies.setIamPolicy `  
` datacatalog.taxonomies.update `  
  
Identity-Aware Proxy  |  Agregado  |  ` iap.projects.getSettings `  
` iap.projects.updateSettings `  
  
NetApp Cloud Volumes Service  |  Agregado  |  ` netappcloudvolumes.jobs.get `  
` netappcloudvolumes.jobs.list `  
  
Redis Enterprise Cloud  |  Agregado  |  `
redisenterprisecloud.databases.create `  
` redisenterprisecloud.databases.delete `  
` redisenterprisecloud.databases.get `  
` redisenterprisecloud.databases.list `  
` redisenterprisecloud.databases.update `  
` redisenterprisecloud.subscriptions.create `  
` redisenterprisecloud.subscriptions.delete `  
` redisenterprisecloud.subscriptions.get `  
` redisenterprisecloud.subscriptions.list `  
` redisenterprisecloud.subscriptions.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 25/10/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Identity-Aware Proxy  |  Ahora en etapa de disponibilidad general  |

La función ` roles/iap.tunnelResourceAccessor ` (Usuario de túnel protegido
con IAP) pasó a la etapa de disponibilidad general.  
  
Servicio administrado para Microsoft Active Directory  |  Ahora en etapa de
disponibilidad general  |

La función ` roles/managedidentities.admin ` (Administrador de identidades
administradas de Google Cloud) pasó a la etapa de disponibilidad general.  
  
Servicio administrado para Microsoft Active Directory  |  Ahora en etapa de
disponibilidad general  |

La función ` roles/managedidentities.domainAdmin ` (Administrador de dominios
de identidades administradas de Google Cloud) pasó a la etapa de
disponibilidad general.  
  
Servicio administrado para Microsoft Active Directory  |  Ahora en etapa de
disponibilidad general  |

La función ` roles/managedidentities.viewer ` (Visualizador de identidades
administradas de Google Cloud) pasó a la etapa de disponibilidad general.  
  
API de acciones  |  Agregado  |  ` actions.agentVersions.get `  
  
API de acciones  |  Compatible con funciones personalizadas  |  `
actions.agentVersions.get `  
  
API de acciones  |  Ahora en etapa de disponibilidad general  |  `
actions.agentVersions.get `  
  
Dialogflow  |  Agregado  |  ` dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
Dialogflow  |  Ahora en etapa de disponibilidad general  |  `
dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
Identity-Aware Proxy  |  Ahora en etapa de disponibilidad general  |  `
iap.tunnel.getIamPolicy `  
` iap.tunnel.setIamPolicy `  
` iap.tunnelInstances.accessViaIAP `  
` iap.tunnelInstances.getIamPolicy `  
` iap.tunnelInstances.setIamPolicy `  
` iap.tunnelZones.getIamPolicy `  
` iap.tunnelZones.setIamPolicy `  
  
Servicio administrado para Microsoft Active Directory  |  Ahora en etapa de
disponibilidad general  |  ` managedidentities.domains.attachTrust `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 18/10/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Identity-Aware Proxy  |  Ahora en etapa de disponibilidad general  |

La función ` roles/iap.settingsAdmin ` (Administrador de configuración de IAP)
pasó a la etapa de disponibilidad general.  
  
Identity-Aware Proxy  |  Agregado  |  ` iap.web.getSettings `  
` iap.web.updateSettings `  
` iap.webServiceVersions.getSettings `  
` iap.webServiceVersions.updateSettings `  
` iap.webServices.getSettings `  
` iap.webServices.updateSettings `  
` iap.webTypes.getSettings `  
` iap.webTypes.updateSettings `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 11/10/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Reglas de seguridad de Firebase  |  Ahora en etapa de disponibilidad general
|

La función ` roles/firebaserules.admin ` (Administrador de reglas de Firebase)
pasó a la etapa de disponibilidad general.  
  
Reglas de seguridad de Firebase  |  Ahora en etapa de disponibilidad general
|

La función ` roles/firebaserules.viewer ` (Visualizador de reglas de Firebase)
pasó a la etapa de disponibilidad general.  
  
BigQuery  |  Compatible con funciones personalizadas  |  `
bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Google Kubernetes Engine  |  Agregado  |  ` container.csiDrivers.create `  
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
  
Google Kubernetes Engine  |  Compatible con funciones personalizadas  |  `
container.csiDrivers.create `  
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
  
Google Kubernetes Engine  |  Ahora en etapa de disponibilidad general  |  `
container.csiDrivers.create `  
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
  
Reglas de seguridad de Firebase  |  Ahora en etapa de disponibilidad general
|  ` firebaserules.releases.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 04/10/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
API de acciones  |  Agregado  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
API de acciones  |  Compatible con funciones personalizadas  |  `
actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
API de acciones  |  Ahora en etapa de disponibilidad general  |  `
actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Cloud Identity and Access Management  |  Compatible con funciones
personalizadas  |  ` iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 27/09/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
API de Hangouts Chat  |  Agregado  |  ` chat.bots.get `  
` chat.bots.update `  
  
API de Hangouts Chat  |  Compatible con funciones personalizadas  |  `
chat.bots.get `  
` chat.bots.update `  
  
Cloud Asset Inventory  |  Agregado  |  ` cloudasset.assets.exportAccessLevel `  
` cloudasset.assets.exportAccessPolicy `  
` cloudasset.assets.exportAllAccessPolicy `  
` cloudasset.assets.exportOrgPolicy `  
` cloudasset.assets.exportServicePerimeter `  
` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Cloud Asset Inventory  |  Compatible con funciones personalizadas  |  `
cloudasset.assets.exportAccessPolicy `  
` cloudasset.assets.exportOrgPolicy `  
` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Cloud Identity and Access Management  |  Compatible con funciones
personalizadas  |  ` iam.serviceAccountKeys.create `  
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
  
API de VM Migration  |  Agregado  |  ` vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
API de VM Migration  |  Compatible con funciones personalizadas  |  `
vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 20/09/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Key Management Service  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudkms.importer ` (Importador de Cloud KMS) pasó a la
etapa de disponibilidad general.  
  
Cloud Key Management Service  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudkms.publicKeyViewer ` (Visualizador de CryptoKeys
públicas de Cloud KMS) pasó a la etapa de disponibilidad general.  
  
Cloud Key Management Service  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudkms.signer ` (Firmante de CryptoKeys de Cloud KMS)
pasó a la etapa de disponibilidad general.  
  
Cloud Key Management Service  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudkms.signerVerifier ` (Verificador y firmante de
CryptoKeys de Cloud KMS) pasó a la etapa de disponibilidad general.  
  
Cloud Key Management Service  |  Agregado  |  ` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  Compatible con funciones personalizadas  |  `
cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  Ahora en etapa de disponibilidad general  |
` cloudkms.cryptoKeyVersions.useToSign `  
` cloudkms.cryptoKeyVersions.viewPublicKey `  
` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 13/09/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Firebase Remote Config  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudconfig.admin ` (Administrador de Firebase Remote
Config) pasó a la etapa de disponibilidad general.  
  
Firebase Remote Config  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudconfig.viewer ` (Visualizador de Firebase Remote
Config) pasó a la etapa de disponibilidad general.  
  
Firebase  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebase.admin ` (Administrador de Firebase) pasó a la
etapa de disponibilidad general.  
  
Firebase  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebase.analyticsAdmin ` (Administrador de Firebase
Analytics) pasó a la etapa de disponibilidad general.  
  
Firebase  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebase.analyticsViewer ` (Visualizador de Firebase
Analytics) pasó a la etapa de disponibilidad general.  
  
Firebase  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebase.developAdmin ` (Administrador de desarrollo de
Firebase) pasó a la etapa de disponibilidad general.  
  
Firebase  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebase.developViewer ` (Visualizador de desarrollo de
Firebase) pasó a la etapa de disponibilidad general.  
  
Firebase  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebase.growthAdmin ` (Administrador de Firebase Grow)
pasó a la etapa de disponibilidad general.  
  
Firebase  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebase.growthViewer ` (Visualizador de Firebase Grow)
pasó a la etapa de disponibilidad general.  
  
Firebase  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebase.qualityAdmin ` (Administrador de calidad de
Firebase) pasó a la etapa de disponibilidad general.  
  
Firebase  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebase.qualityViewer ` (Visualizador de calidad de
Firebase) pasó a la etapa de disponibilidad general.  
  
Firebase  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebase.viewer ` (Visualizador de Firebase) pasó a la
etapa de disponibilidad general.  
  
Firebase Authentication  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebaseauth.admin ` (Administrador de Firebase
Authentication) pasó a la etapa de disponibilidad general.  
  
Firebase Authentication  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebaseauth.viewer ` (Visualizador de Firebase
Authentication) pasó a la etapa de disponibilidad general.  
  
Firebase Crashlytics  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasecrashlytics.admin ` (Administrador de Firebase
Crashlytics) pasó a la etapa de disponibilidad general.  
  
Firebase Crashlytics  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasecrashlytics.viewer ` (Visualizador de Firebase
Crashlytics) pasó a la etapa de disponibilidad general.  
  
Firebase Realtime Database  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasedatabase.admin ` (Administrador de Firebase
Realtime Database) pasó a la etapa de disponibilidad general.  
  
Firebase Realtime Database  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasedatabase.viewer ` (Visualizador de Firebase
Realtime Database) pasó a la etapa de disponibilidad general.  
  
Firebase Dynamic Links  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasedynamiclinks.admin ` (Administrador de Firebase
Dynamic Links) pasó a la etapa de disponibilidad general.  
  
Firebase Dynamic Links  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasedynamiclinks.viewer ` (Visualizador de Firebase
Dynamic Links) pasó a la etapa de disponibilidad general.  
  
Firebase Hosting  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasehosting.admin ` (Administrador de Firebase Hosting)
pasó a la etapa de disponibilidad general.  
  
Firebase Hosting  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasehosting.viewer ` (Visualizador de Firebase Hosting)
pasó a la etapa de disponibilidad general.  
  
Firebase Cloud Messaging  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasenotifications.admin ` (Administrador de Firebase
Cloud Messaging) pasó a la etapa de disponibilidad general.  
  
Firebase Cloud Messaging  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasenotifications.viewer ` (Visualizador de Firebase
Cloud Messaging) pasó a la etapa de disponibilidad general.  
  
Firebase Performance Monitoring  |  Ahora en etapa de disponibilidad general
|

La función ` roles/firebaseperformance.admin ` (Administrador de informes de
rendimiento de Firebase) pasó a la etapa de disponibilidad general.  
  
Firebase Performance Monitoring  |  Ahora en etapa de disponibilidad general
|

La función ` roles/firebaseperformance.viewer ` (Visualizador de informes de
rendimiento de Firebase) pasó a la etapa de disponibilidad general.  
  
Firebase Predictions  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasepredictions.admin ` (Administrador de Firebase
Predictions) pasó a la etapa de disponibilidad general.  
  
Firebase Predictions  |  Ahora en etapa de disponibilidad general  |

La función ` roles/firebasepredictions.viewer ` (Visualizador de Firebase
Predictions) pasó a la etapa de disponibilidad general.  
  
Firebase Remote Config  |  Ahora en etapa de disponibilidad general  |  `
cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Cloud DNS  |  Ahora en etapa de disponibilidad general  |  `
dns.networks.bindPrivateDNSPolicy `  
` dns.policies.create `  
` dns.policies.delete `  
` dns.policies.get `  
` dns.policies.getIamPolicy `  
` dns.policies.list `  
` dns.policies.setIamPolicy `  
` dns.policies.update `  
  
Firebase  |  Ahora en etapa de disponibilidad general  |  `
firebase.billingPlans.get `  
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
  
Firebase Authentication  |  Ahora en etapa de disponibilidad general  |  `
firebaseauth.configs.create `  
` firebaseauth.configs.get `  
` firebaseauth.configs.getHashConfig `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Crashlytics  |  Ahora en etapa de disponibilidad general  |  `
firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase Realtime Database  |  Ahora en etapa de disponibilidad general  |  `
firebasedatabase.instances.create `  
` firebasedatabase.instances.get `  
` firebasedatabase.instances.list `  
` firebasedatabase.instances.update `  
  
Firebase Dynamic Links  |  Ahora en etapa de disponibilidad general  |  `
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
  
Firebase Hosting  |  Ahora en etapa de disponibilidad general  |  `
firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase Cloud Messaging  |  Ahora en etapa de disponibilidad general  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Performance Monitoring  |  Ahora en etapa de disponibilidad general
|  ` firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Predictions  |  Ahora en etapa de disponibilidad general  |  `
firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
NetApp Cloud Volumes Service  |  Agregado  |  `
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
  
Event Threat Detection  |  Compatible con funciones personalizadas  |  `
threatdetection.detectorSettings.clear `  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 06/09/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/owner `
(Propietario):

` dataprocessing.iamaccesshistory.exportData `  
  
Acceso a VPC sin servidores  |  Ahora en etapa de disponibilidad general  |

La función ` roles/vpaccess.user ` (Usuario de Acceso a VPC sin servidores)
pasó a la etapa de disponibilidad general.  
  
Acceso a VPC sin servidores  |  Ahora en etapa de disponibilidad general  |

La función ` roles/vpaccess.viewer ` (Visualizador de Acceso a VPC sin
servidores) pasó a la etapa de disponibilidad general.  
  
Acceso a VPC sin servidores  |  Ahora en etapa de disponibilidad general  |

La función ` roles/vpcaccess.admin ` (Administrador de Acceso a VPC sin
servidores) pasó a la etapa de disponibilidad general.  
  
Compute Engine  |  Agregado  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Acceso a VPC sin servidores  |  Ahora en etapa de disponibilidad general  |  `
vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 30/08/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Firebase Test Lab  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudtestservice.testAdmin ` (Administrador de Firebase Test Lab):

` firebase.clients.get `  
` firebase.projects.get `  
  
Firebase Test Lab  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudtestservice.testViewer ` (Visualizador de Firebase Test Lab):

` firebase.clients.get `  
` firebase.projects.get `  
  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/compute.orgSecurityPolicyAdmin ` (Administrador de políticas de
seguridad de Compute para la organización):

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/compute.orgSecurityPolicyUser ` (Usuario de políticas de seguridad de
Compute para la organización):

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/compute.orgSecurityResourceAdmin ` (Administrador de recursos de Compute
en la organización):

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 23/08/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Traducción  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudtranslate.admin ` (Administrador de la API de Cloud
Translation) pasó a la etapa de disponibilidad general.  
  
Traducción  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudtranslate.editor ` (Editor de la API de Cloud
Translation) pasó a la etapa de disponibilidad general.  
  
Traducción  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudtranslate.user ` (Usuario de la API de Cloud
Translation) pasó a la etapa de disponibilidad general.  
  
Traducción  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudtranslate.viewer ` (Visualizador de la API de Cloud
Translation) pasó a la etapa de disponibilidad general.  
  
Cloud Healthcare API  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/healthcare.dicomEditor ` (Editor de imágenes DICOM de Healthcare):

` healthcare.dicomStores.dicomWebDelete `  
  
Traducción  |  Ahora en etapa de disponibilidad general  |  `
cloudtranslate.generalModels.batchPredict `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 16/08/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Traducción  |  Compatible con funciones personalizadas  |  `
cloudtranslate.locations.get `  
` cloudtranslate.locations.list `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.networks.updatePeering `  
  
Data Catalog  |  Agregado  |  ` datacatalog.entries.create `  
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
  
Data Catalog  |  Compatible con funciones personalizadas  |  `
datacatalog.entries.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 09/08/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/compute.orgSecurityPolicyAdmin ` (Administrador de políticas de
seguridad de Compute para la organización):

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/compute.orgSecurityPolicyUser ` (Usuario de políticas de seguridad de
Compute para la organización):

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/compute.orgSecurityResourceAdmin ` (Administrador de recursos de Compute
en la organización):

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Cloud Storage  |  Ahora en etapa de disponibilidad general  |

La función ` roles/storage.hmacKeyAdmin ` (Administrador de claves HMAC de
Storage) pasó a la etapa de disponibilidad general.  
  
Cloud Storage  |  Agregado  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
Cloud Storage  |  Compatible con funciones personalizadas  |  `
storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
Cloud Storage  |  Ahora en etapa de disponibilidad general  |  `
storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 28/06/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/viewer `
(Visualizador):

` pubsub.snapshots.seek `  
  
Firebase Crashlytics  |  Agregado  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase Crashlytics  |  Compatible con funciones personalizadas  |  `
firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Memorystore for Redis  |  Agregado  |  ` redis.instances.export `  
` redis.instances.import `  
  
Memorystore for Redis  |  Compatible con funciones personalizadas  |  `
redis.instances.export `  
` redis.instances.import `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 21/06/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Migrate for Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudmigration.inframanager ` (Administrador de Velostrata):

` compute.instances.updateShieldedInstanceConfig `  
  
Traducción  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudtranslate.viewer ` (Visualizador de la API de Cloud Translation):

` cloudtranslate.operations.wait `  
  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/compute.networkUser
` (Usuario de red de Compute):

` compute.vpnGateways.use `  
  
Firebase  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/firebase.admin `
(Administrador de Firebase):

` cloudmessaging.messages.create `  
  
Firebase  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/firebase.growthAdmin
` (Administrador de Firebase Grow):

` cloudmessaging.messages.create `  
  
Resource Manager  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/resourcemanager.projectMover ` (Migrador de proyectos):

` resourcemanager.projects.move `  
  
Security Command Center  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/securitycenter.adminEditor ` (Editor administrador del centro de
seguridad):

` securitycenter.assets.group `  
` securitycenter.assets.list `  
` securitycenter.assets.listAssetPropertyNames `  
  
BigQuery  |  Agregado  |  ` bigquery.connections.create `  
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
  
BigQuery  |  Compatible con funciones personalizadas  |  `
bigquery.routines.create `  
` bigquery.routines.delete `  
` bigquery.routines.get `  
` bigquery.routines.list `  
` bigquery.routines.update `  
  
Traducción  |  Compatible con funciones personalizadas  |  `
cloudtranslate.generalModels.batchPredict `  
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
  
Cloud Composer  |  Agregado  |  ` composer.imageversions.list `  
  
Cloud Composer  |  Compatible con funciones personalizadas  |  `
composer.imageversions.list `  
  
Cloud Composer  |  Ahora en etapa de disponibilidad general  |  `
composer.imageversions.list `  
  
Compute Engine  |  Agregado  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 14/06/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Identity and Access Management  |  Ahora en etapa de disponibilidad
general  |

La función ` roles/iam.workloadIdentityUser ` (Usuario de identidades de
cargas de trabajo) pasó a la etapa de disponibilidad general.  
  
Cloud Functions  |  Agregado  |  ` cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Cloud Functions  |  Compatible con funciones personalizadas  |  `
cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 31/05/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Data Catalog  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/datacatalog.admin `
(Administrador de Data Catalog):

` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
` pubsub.topics.updateTag `  
  
Migrate for Compute Engine  |  Agregado  |  `
cloudmigration.velostrataendpoints.connect `  
  
Cloud Identity and Access Management  |  Disponible con funciones
personalizadas  |  ` iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 24/05/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/viewer `
(Visualizador):

` managedidentities.domains.validateTrust `  
  
Recomendaciones IA  |  Compatible con funciones personalizadas  |  `
automlrecommendations.apiKeys.create `  
` automlrecommendations.apiKeys.delete `  
` automlrecommendations.apiKeys.list `  
` automlrecommendations.catalogItems.create `  
` automlrecommendations.catalogItems.delete `  
` automlrecommendations.catalogItems.get `  
` automlrecommendations.catalogItems.list `  
` automlrecommendations.catalogItems.update `  
` automlrecommendations.events.list `  
` automlrecommendations.events.purge `  
  
BigQuery  |  Agregado  |  ` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
BigQuery  |  Compatible con funciones personalizadas  |  `
bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
Data Catalog  |  Agregado  |  ` datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
Data Catalog  |  Compatible con funciones personalizadas  |  `
datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
Filestore  |  Agregado  |  ` file.snapshots.update `  
  
Filestore  |  Compatible con funciones personalizadas  |  `
file.snapshots.update `  
  
Pub/Sub  |  Agregado  |  ` pubsub.topics.updateTag `  
  
Pub/Sub  |  Compatible con funciones personalizadas  |  `
pubsub.topics.updateTag `  
  
  
##  Cambios de IAM a partir del 17/05/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Dialogflow  |  Agregado  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  Compatible con funciones personalizadas  |  `
dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  Ahora en etapa de disponibilidad general  |  `
dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 10/05/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Identity and Access Management  |  Ahora en etapa de disponibilidad
general  |

La función ` roles/iam.securityAdmin ` (Administrador de seguridad) pasó a la
etapa de disponibilidad general.  
  
Cloud IoT  |  Agregado  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  Compatible con funciones personalizadas  |  `
cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  Ahora en etapa de disponibilidad general  |  `
cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.healthChecks.create `  
` compute.healthChecks.delete `  
` compute.healthChecks.get `  
` compute.healthChecks.list `  
` compute.healthChecks.update `  
` compute.healthChecks.use `  
` compute.healthChecks.useReadOnly `  
` compute.instanceGroups.use `  
  
API de Cloud Healthcare  |  Agregado  |  ` healthcare.fhirResources.purge `  
  
Servicio administrado para Microsoft Active Directory  |  Agregado  |  `
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
  
Servicio administrado para Microsoft Active Directory  |  Compatible con
funciones personalizadas  |  ` managedidentities.domains.attachTrust `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 03/05/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.admin ` (Administrador del centro de
seguridad) pasó a la etapa de disponibilidad general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.adminEditor ` (Editor administrador del
centro de seguridad) pasó a la etapa de disponibilidad general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.adminViewer ` (Visualizador administrador
del centro de seguridad) pasó a la etapa de disponibilidad general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.assetsDiscoveryRunner ` (Ejecutor de
detección de activos del centro de seguridad) pasó a la etapa de
disponibilidad general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.assetSecurityMarksWriter ` (Escritor de
marcas de seguridad de activos del centro de seguridad) pasó a la etapa de
disponibilidad general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.assetsViewer ` (Visualizador de activos del
centro de seguridad) pasó a la etapa de disponibilidad general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.findingSecurityMarksWriter ` (Escritor de
marcas de seguridad de hallazgos del centro de seguridad) pasó a la etapa de
disponibilidad general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.findingsEditor ` (Editor de hallazgos del
centro de seguridad) pasó a la etapa de disponibilidad general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.findingsStateSetter ` (Definidor de estado
de hallazgos del centro de seguridad) pasó a la etapa de disponibilidad
general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.findingsViewer ` (Visualizador de hallazgos
del centro de seguridad) pasó a la etapa de disponibilidad general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.sourcesAdmin ` (Administrador de fuentes del
centro de seguridad) pasó a la etapa de disponibilidad general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.sourcesEditor ` (Editor de fuentes del
centro de seguridad) pasó a la etapa de disponibilidad general.  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |

La función ` roles/securitycenter.sourcesViewer ` (Visualizador de fuentes del
centro de seguridad) pasó a la etapa de disponibilidad general.  
  
Recomendaciones IA  |  Agregado  |  ` automlrecommendations.apiKeys.create `  
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
  
BigQuery  |  Agregado  |  ` bigquery.models.create `  
` bigquery.models.delete `  
` bigquery.models.getData `  
` bigquery.models.getMetadata `  
` bigquery.models.list `  
` bigquery.models.updateData `  
` bigquery.models.updateMetadata `  
  
Firebase Cloud Messaging  |  Agregado  |  ` cloudmessaging.messages.create `  
  
Firebase Cloud Messaging  |  Compatible con funciones personalizadas  |  `
cloudmessaging.messages.create `  
  
Firebase Cloud Messaging  |  Ahora en etapa de disponibilidad general  |  `
cloudmessaging.messages.create `  
  
Security Command Center  |  Ahora en etapa de disponibilidad general  |  `
securitycenter.assets.group `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 19/04/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Función básica  |  Se actualizó una función  |

Se quitaron los siguientes permisos de la función ` roles/editor ` (Editor):

` firebasedynamiclinks.domains.delete `  
  
Security Command Center  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/securitycenter.admin
` (Administrador del centro de seguridad):

` securitycenter.findings.setState `  
  
Security Command Center  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/securitycenter.adminEditor ` (Editor administrador del centro de
seguridad):

` securitycenter.findings.setState `  
  
Security Command Center  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/securitycenter.findingsEditor ` (Editor de hallazgos del centro de
seguridad):

` securitycenter.findings.setState `  
  
Aprobación de acceso  |  Agregado  |  ` accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
Aprobación de acceso  |  Compatible con funciones personalizadas  |  `
accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
Cloud Bigtable  |  Agregado  |  ` bigtable.locations.list `  
  
Cloud Bigtable  |  Compatible con funciones personalizadas  |  `
bigtable.locations.list `  
  
Cloud Bigtable  |  Ahora en etapa de disponibilidad general  |  `
bigtable.locations.list `  
  
Cloud Scheduler  |  Agregado  |  ` cloudscheduler.locations.get `  
` cloudscheduler.locations.list `  
  
Compute Engine  |  Agregado  |  `
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
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
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
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.networkEndpointGroups.attachNetworkEndpoints `  
` compute.networkEndpointGroups.create `  
` compute.networkEndpointGroups.delete `  
` compute.networkEndpointGroups.detachNetworkEndpoints `  
` compute.networkEndpointGroups.get `  
` compute.networkEndpointGroups.getIamPolicy `  
` compute.networkEndpointGroups.list `  
` compute.networkEndpointGroups.setIamPolicy `  
` compute.networkEndpointGroups.use `  
  
Ejecución de compilación remota  |  Agregado  |  `
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
  
Ejecución de compilación remota  |  Compatible con funciones personalizadas  |
` remotebuildexecution.actions.create `  
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
  
Acceso a VPC sin servidores  |  Agregado  |  ` vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 29/03/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/compute.networkUser
` (Usuario de red de Compute):

` servicenetworking.services.get `  
  
Cloud Monitoring  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/monitoring.admin `
(Administrador de Monitoring):

` serviceusage.services.enable `  
  
Cloud Monitoring  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/monitoring.editor `
(Editor de Monitoring):

` serviceusage.services.enable `  
  
Paquete de operaciones de Google Cloud  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/stackdriver.accounts.editor ` (Editor de cuentas de Stackdriver):

` serviceusage.services.enable `  
  
Cloud SQL  |  Agregado  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  Compatible con funciones personalizadas  |  `
cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  Ahora en etapa de disponibilidad general  |  `
cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Traducción  |  Agregado  |  ` cloudtranslate.generalModels.batchPredict `  
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
  
Cloud DNS  |  Agregado  |  ` dns.networks.targetWithPeeringZone `  
  
Cloud DNS  |  Compatible con funciones personalizadas  |  `
dns.networks.targetWithPeeringZone `  
  
Event Threat Detection  |  Agregado  |  `
threatdetection.detectorSettings.clear `  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 22/03/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Talent Solution  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudjobdiscovery.admin ` (Administrador) pasó a la etapa
de disponibilidad general.  
  
Talent Solution  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudjobdiscovery.jobsEditor ` (Editor de trabajos) pasó a
la etapa de disponibilidad general.  
  
Talent Solution  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudjobdiscovery.jobsViewer ` (Visualizador de trabajos)
pasó a la etapa de disponibilidad general.  
  
Talent Solution  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudjobdiscovery.profilesEditor ` (Editor de perfiles)
pasó a la etapa de disponibilidad general.  
  
Talent Solution  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudjobdiscovery.profilesViewer ` (Visualizador de
perfiles) pasó a la etapa de disponibilidad general.  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/editor ` (Editor):

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Filestore  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/file.editor `
(Editor de Cloud Filestore):

` file.instances.restore `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/owner `
(Propietario):

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Talent Solution  |  Ahora en etapa de disponibilidad general  |  `
cloudjobdiscovery.companies.create `  
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
  
Compute Engine  |  Agregado  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Filestore  |  Agregado  |  ` file.instances.restore `  
  
Firebase Authentication  |  Agregado  |  ` firebaseauth.configs.getHashConfig
`  
  
Firebase Authentication  |  Compatible con funciones personalizadas  |  `
firebaseauth.configs.getHashConfig `  
  
API de Cloud Healthcare  |  Agregado  |  ` healthcare.datasets.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 15/03/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Talent Solution  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudjobdiscovery.profilesEditor ` (Editor de perfiles):

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Talent Solution  |  Se actualizó una función  |

Se quitaron los siguientes permisos de la función `
roles/cloudjobdiscovery.profilesEditor ` (Editor de perfiles):

` cloudjobdiscovery.companies.create `  
` cloudjobdiscovery.companies.delete `  
` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.companies.update `  
  
Talent Solution  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/cloudjobdiscovery.profilesViewer ` (Visualizador de perfiles):

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  Se actualizó una función  |

Se quitaron los siguientes permisos de la función `
roles/cloudjobdiscovery.profilesViewer ` (Visualizador de perfiles):

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/editor ` (Editor):

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/owner `
(Propietario):

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Storage Transfer Service  |  Ahora en etapa de disponibilidad general  |

La función ` roles/storagetransfer.admin ` (Administrador de transferencia de
almacenamiento) pasó a la etapa de disponibilidad general.  
  
Storage Transfer Service  |  Ahora en etapa de disponibilidad general  |

La función ` roles/storagetransfer.user ` (Usuario de transferencia de
almacenamiento) pasó a la etapa de disponibilidad general.  
  
Storage Transfer Service  |  Ahora en etapa de disponibilidad general  |

La función ` roles/storagetransfer.viewer ` (Visualizador de transferencia de
almacenamiento) pasó a la etapa de disponibilidad general.  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/viewer `
(Visualizador):

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  Agregado  |  ` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Cloud DNS  |  Ahora en etapa de disponibilidad general  |  `
dns.networks.bindPrivateDNSZone `  
  
Cloud Run  |  Agregado  |  ` run.configurations.get `  
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
  
Cloud Run  |  No compatible con funciones personalizadas  |  `
run.routes.invoke `  
  
Cloud Run  |  Compatible con funciones personalizadas  |  `
run.configurations.get `  
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
  
Storage Transfer Service  |  Agregado  |  ` storagetransfer.jobs.create `  
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
  
Storage Transfer Service  |  Compatible con funciones personalizadas  |  `
storagetransfer.jobs.create `  
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
  
Storage Transfer Service  |  Ahora en etapa de disponibilidad general  |  `
storagetransfer.jobs.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 07/03/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
BigQuery  |  Se agregó una función  |

Se agregó la función ` roles/bigquery.connectionAdmin ` (Administrador de
conexión de BigQuery) con los siguientes permisos:

` bigquery.connections.create `  
` bigquery.connections.delete `  
` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.setIamPolicy `  
` bigquery.connections.update `  
` bigquery.connections.use `  
  
BigQuery  |  Se agregó una función  |

Se agregó la función ` roles/bigquery.connectionUser ` (Usuario de conexión de
BigQuery) con los siguientes permisos:

` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.use `  
  
Dialogflow  |  Se actualizó una función  |

Se han agregado los siguientes permisos a la función ` roles/dialogflow.admin
` (Administrador de la API de Dialogflow):

` dialogflow.agents.update `  
  
Dialogflow  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/dialogflow.consoleAgentEditor ` (Editor de agentes de la consola de
Dialogflow):

` dialogflow.agents.update `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/editor ` (Editor):

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/file.editor `
(Editor de Cloud Filestore):

` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/file.viewer `
(Visualizador de Cloud Filestore):

` file.snapshots.get `  
` file.snapshots.list `  
  
Cloud Identity and Access Management  |  Ahora en etapa de disponibilidad
general  |

La función ` roles/iam.serviceAccountCreator ` (Creador de cuentas de
servicio) pasó a la etapa de disponibilidad general.  
  
Cloud Identity and Access Management  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/iam.securityReviewer
` (Revisor de seguridad):

` file.snapshots.list `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/owner `
(Propietario):

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Service Usage  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/serviceusage.apiKeysAdmin ` (Administrador de claves de API):

` serviceusage.operations.get `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/viewer `
(Visualizador):

` file.snapshots.get `  
` file.snapshots.list `  
  
Servicio de etiquetado de datos de AI Platform  |  Agregado  |  `
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
  
Servicio de etiquetado de datos de AI Platform  |  Compatible con funciones
personalizadas  |  ` datalabeling.annotateddatasets.delete `  
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
  
Dialogflow  |  Agregado  |  ` dialogflow.agents.update `  
  
Filestore  |  Agregado  |  ` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 01/03/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/compute.instanceAdmin.v1 ` (Administrador de instancias de Compute
[v1]):

` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Dataproc  |  Se agregó una función  |

Se agregó la función ` roles/dataproc.admin ` (Administrador de Dataproc) con
los siguientes permisos:

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
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/editor ` (Editor):

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
Cloud Identity and Access Management  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/iam.serviceAccountDeleter ` (Eliminador de cuentas de servicio):

` iam.serviceAccounts.get `  
` iam.serviceAccounts.list `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/viewer `
(Visualizador):

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
AutoML  |  Agregado  |  ` automl.columnSpecs.get `  
` automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.export `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
AutoML  |  Compatible con funciones personalizadas  |  `
automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.deploy `  
` automl.models.export `  
` automl.models.undeploy `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
Compute Engine  |  Agregado  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 15/02/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Access Context Manager  |  Ahora en etapa de disponibilidad general  |

La función ` roles/accesscontextmanager.policyAdmin ` (Administrador de Access
Context Manager) pasó a la etapa de disponibilidad general.  
  
Access Context Manager  |  Ahora en etapa de disponibilidad general  |

La función ` roles/accesscontextmanager.policyEditor ` (Editor de Access
Context Manager) pasó a la etapa de disponibilidad general.  
  
Access Context Manager  |  Ahora en etapa de disponibilidad general  |

La función ` roles/accesscontextmanager.policyReader ` (Lector de Access
Context Manager) pasó a la etapa de disponibilidad general.  
  
Talent Solution  |  Se agregó una función  |

Se agregó la función ` roles/cloudjobdiscovery.profilesEditor ` (Editor de
perfiles) con los siguientes permisos:

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
  
Talent Solution  |  Se agregó una función  |

Se agregó la función ` roles/cloudjobdiscovery.profilesViewer ` (Visualizador
de perfiles) con los siguientes permisos:

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/editor ` (Editor):

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/owner `
(Propietario):

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
Función básica  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función ` roles/viewer `
(Visualizador):

` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
  
Paquete de operaciones de Google Cloud  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/stackdriver.accounts.editor ` (Editor de cuentas de Stackdriver):

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Paquete de operaciones de Google Cloud  |  Se actualizó una función  |

Se agregaron los siguientes permisos a la función `
roles/stackdriver.accounts.viewer ` (Visualizador de cuentas de Stackdriver):

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Access Context Manager  |  Compatible con funciones personalizadas  |  `
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
  
Access Context Manager  |  Ahora en etapa de disponibilidad general  |  `
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
  
Talent Solution  |  Agregado  |  ` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 08/02/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Security Command Center  |  Compatible con funciones personalizadas  |  `
securitycenter.assets.group `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 01/02/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Dialogflow  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dialogflow.admin ` (Administrador de la API de Dialogflow)
pasó a la etapa de disponibilidad general.  
  
Dialogflow  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dialogflow.client ` (Cliente de la API de Dialogflow) pasó
a la etapa de disponibilidad general.  
  
Dialogflow  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dialogflow.consoleAgentEditor ` (Editor de agentes de la
consola de Dialogflow) pasó a la etapa de disponibilidad general.  
  
Dialogflow  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dialogflow.reader ` (Lector de la API de Dialogflow) pasó a
la etapa de disponibilidad general.  
  
Cloud Asset Inventory  |  Agregado  |  ` cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Cloud Asset Inventory  |  Compatible con funciones personalizadas  |  `
cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Cloud Asset Inventory  |  Ahora en etapa de disponibilidad general  |  `
cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Dialogflow  |  Compatible con funciones personalizadas  |  `
dialogflow.agents.search `  
` dialogflow.agents.train `  
  
Dialogflow  |  Ahora en etapa de disponibilidad general  |  `
dialogflow.agents.export `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 25/01/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Agregado  |  ` compute.instances.updateDisplayDevice `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 11/01/2019

Servicio  |  Cambio  |  Descripción  
---|---|---  
Identity-Aware Proxy  |  Ahora en etapa de disponibilidad general  |

La función ` roles/iap.admin ` (Administrador de políticas de IAP) pasó a la
etapa de disponibilidad general.  
  
Identity-Aware Proxy  |  Compatible con funciones personalizadas  |  `
iap.web.getIamPolicy `  
` iap.web.setIamPolicy `  
` iap.webServiceVersions.accessViaIAP `  
` iap.webServiceVersions.getIamPolicy `  
` iap.webServiceVersions.setIamPolicy `  
` iap.webServices.getIamPolicy `  
` iap.webServices.setIamPolicy `  
` iap.webTypes.getIamPolicy `  
` iap.webTypes.setIamPolicy `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 21/12/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud DNS  |  Agregado  |  ` dns.networks.bindPrivateDNSZone `  
  
Cloud DNS  |  Compatible con funciones personalizadas  |  `
dns.networks.bindPrivateDNSZone `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 14/12/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Firebase Authentication  |  Agregado  |  ` firebaseauth.configs.create `  
  
Firebase Authentication  |  Compatible con funciones personalizadas  |  `
firebaseauth.configs.create `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 07/12/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
BigQuery  |  Agregado  |  ` bigquery.readsessions.create `  
  
BigQuery  |  Compatible con funciones personalizadas  |  `
bigquery.readsessions.create `  
  
Google Kubernetes Engine  |  Compatible con funciones personalizadas  |  `
container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
Google Kubernetes Engine  |  Ahora en etapa de disponibilidad general  |  `
container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 30/11/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Asset Inventory  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudasset.viewer ` (Visualizador de recursos de Cloud)
pasó a la etapa de disponibilidad general.  
  
Cloud Asset Inventory  |  Ahora en etapa de disponibilidad general  |  `
cloudasset.assets.exportAll `  
  
Compute Engine  |  Agregado  |  ` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.disks.getIamPolicy `  
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
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
` compute.subnetworks.getIamPolicy `  
` compute.subnetworks.setIamPolicy `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 16/11/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
AutoML  |  Agregado  |  ` automl.locations.getIamPolicy `  
` automl.locations.setIamPolicy `  
  
AutoML  |  Compatible con funciones personalizadas  |  `
automl.locations.getIamPolicy `  
` automl.locations.setIamPolicy `  
  
Talent Solution  |  Agregado  |  ` cloudjobdiscovery.events.create `  
` cloudjobdiscovery.events.delete `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.events.update `  
  
Compute Engine  |  Agregado  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Google Kubernetes Engine  |  Agregado  |  ` container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 09/11/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Google Analytics  |  Agregado  |  `
firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
Google Analytics  |  Compatible con funciones personalizadas  |  `
firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 02/11/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  Compatible con funciones personalizadas  |  `
file.instances.create `  
` file.instances.delete `  
` file.instances.get `  
` file.instances.list `  
` file.instances.update `  
` file.locations.get `  
` file.locations.list `  
` file.operations.get `  
` file.operations.list `  
  
Paquete de operaciones de Google Cloud  |  Agregado  |  `
stackdriver.resourceMetadata.write `  
  
Paquete de operaciones de Google Cloud  |  Compatible con funciones
personalizadas  |  ` stackdriver.resourceMetadata.write `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 26/10/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
BigQuery  |  Ahora en etapa de disponibilidad general  |

La función ` roles/bigquery.metadataViewer ` (Visualizador de metadatos de
BigQuery) pasó a la etapa de disponibilidad general.  
  
Cloud Identity and Access Management  |  Ahora en etapa de disponibilidad
general  |

La función ` roles/iam.serviceAccountDeleter ` (Eliminador de cuentas de
servicio) pasó a la etapa de disponibilidad general.  
  
Firebase Realtime Database  |  Agregado  |  `
firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
Firebase Realtime Database  |  Compatible con funciones personalizadas  |  `
firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
Integraciones de Firebase con servicios externos  |  Agregado  |  `
firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
Integraciones de Firebase con servicios externos  |  Compatible con funciones
personalizadas  |  ` firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 19/10/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Asistencia de Google Cloud  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudsupport.admin ` (Administrador de cuentas de
asistencia) pasó a la etapa de disponibilidad general.  
  
Asistencia de Google Cloud  |  Ahora en etapa de disponibilidad general  |

La función ` roles/cloudsupport.viewer ` (Visualizador de cuentas del servicio
de asistencia) pasó a la etapa de disponibilidad general.  
  
Firebase Remote Config  |  Agregado  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Firebase Remote Config  |  Compatible con funciones personalizadas  |  `
cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Asistencia de Google Cloud  |  Compatible con funciones personalizadas  |  `
cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Asistencia de Google Cloud  |  Ahora en etapa de disponibilidad general  |  `
cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Compute Engine  |  Agregado  |  ` compute.networks.updatePeering `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.networks.updatePeering `  
  
Firebase Crashlytics  |  Agregado  |  ` firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase Crashlytics  |  Compatible con funciones personalizadas  |  `
firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase Dynamic Links  |  Agregado  |  `
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
  
Firebase Dynamic Links  |  Compatible con funciones personalizadas  |  `
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
  
Firebase In-App Messaging  |  Agregado  |  `
firebaseinappmessaging.campaigns.create `  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Firebase In-App Messaging  |  Compatible con funciones personalizadas  |  `
firebaseinappmessaging.campaigns.create `  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Firebase Cloud Messaging  |  Agregado  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Cloud Messaging  |  Compatible con funciones personalizadas  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Performance Monitoring  |  Agregado  |  `
firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Performance Monitoring  |  Compatible con funciones personalizadas  |
` firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Predictions  |  Agregado  |  ` firebasepredictions.predictions.create
`  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
Firebase Predictions  |  Compatible con funciones personalizadas  |  `
firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
Security Command Center  |  Agregado  |  ` securitycenter.assets.get `  
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
  
Administración de consumidores de servicios  |  Agregado  |  `
serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
Administración de consumidores de servicios  |  Compatible con funciones
personalizadas  |  ` serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 12/10/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.admin ` (Administrador de DLP) pasó a la etapa de
disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.analyzeRiskTemplatesEditor ` (Editor de plantillas de
riesgo del análisis de DLP) pasó a la etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.analyzeRiskTemplatesReader ` (Lector de plantillas de
riesgo del análisis de DLP) pasó a la etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.deidentifyTemplatesEditor ` (Editor de plantillas de
desidentificación de DLP) pasó a la etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.deidentifyTemplatesReader ` (Lector de plantillas de
desidentificación para DLP) pasó a la etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.inspectTemplatesEditor ` (Editor de plantillas de
inspección de DLP) pasó a la etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.inspectTemplatesReader ` (Lector de plantillas de
inspección de DLP) pasó a la etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.jobsEditor ` (Editor de trabajos de DLP) pasó a la
etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.jobsReader ` (Lector de trabajos de DLP) pasó a la
etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.jobTriggersEditor ` (Editor de activadores de trabajo
de DLP) pasó a la etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.jobTriggersReader ` (Lector de activadores de trabajo
de DLP) pasó a la etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.reader ` (Lector de DLP) pasó a la etapa de
disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.storedInfoTypesEditor ` (Editor de infotipos
almacenados en DLP) pasó a la etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.storedInfoTypesReader ` (Lector de infotipos
almacenados en DLP) pasó a la etapa de disponibilidad general.  
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |

La función ` roles/dlp.user ` (Usuario de DLP) pasó a la etapa de
disponibilidad general.  
  
Google Kubernetes Engine  |  Compatible con funciones personalizadas  |  `
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
  
Cloud Data Loss Prevention  |  Compatible con funciones personalizadas  |  `
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
  
Cloud Data Loss Prevention  |  Ahora en etapa de disponibilidad general  |  `
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
` dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud DNS  |  Compatible con funciones personalizadas  |  ` dns.dnsKeys.get `  
` dns.dnsKeys.list `  
` dns.managedZoneOperations.get `  
` dns.managedZoneOperations.list `  
` dns.managedZones.update `  
  
Firebase  |  Agregado  |  ` firebase.billingPlans.get `  
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
  
Firebase  |  Compatible con funciones personalizadas  |  `
firebase.billingPlans.get `  
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
  
Firebase A/B Testing  |  Agregado  |  ` firebaseabt.experimentresults.get `  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Firebase A/B Testing  |  Compatible con funciones personalizadas  |  `
firebaseabt.experimentresults.get `  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Firebase Authentication  |  Agregado  |  ` firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Authentication  |  Compatible con funciones personalizadas  |  `
firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Realtime Database  |  Agregado  |  ` firebasedatabase.instances.get `  
` firebasedatabase.instances.update `  
  
Firebase Realtime Database  |  Compatible con funciones personalizadas  |  `
firebasedatabase.instances.get `  
` firebasedatabase.instances.update `  
  
Firebase Hosting  |  Agregado  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase Hosting  |  Compatible con funciones personalizadas  |  `
firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Kit de AA para Firebase  |  Agregado  |  ` firebaseml.compressionjobs.create `  
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
  
Kit de AA para Firebase  |  Compatible con funciones personalizadas  |  `
firebaseml.compressionjobs.create `  
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
  
Reglas de seguridad de Firebase  |  Agregado  |  `
firebaserules.releases.create `  
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
  
Reglas de seguridad de Firebase  |  Compatible con funciones personalizadas  |
` firebaserules.releases.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 05/10/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Agregado  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.instances.resume `  
` compute.instances.suspend `  
  
Google Kubernetes Engine  |  Compatible con funciones personalizadas  |  `
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
  
Google Kubernetes Engine  |  Ahora en etapa de disponibilidad general  |  `
container.cronJobs.getStatus `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 21/09/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
AutoML  |  Agregado  |  ` automl.datasets.getIamPolicy `  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
AutoML  |  Compatible con funciones personalizadas  |  `
automl.datasets.getIamPolicy `  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
Cloud Asset Inventory  |  Agregado  |  ` cloudasset.assets.exportAll `  
  
Cloud Asset Inventory  |  Compatible con funciones personalizadas  |  `
cloudasset.assets.exportAll `  
  
Compute Engine  |  Agregado  |  ` compute.licenses.delete `  
  
Google Kubernetes Engine  |  Compatible con funciones personalizadas  |  `
container.apiServices.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 07/09/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Memorystore for Redis  |  Compatible con funciones personalizadas  |  `
redis.operations.cancel `  
` redis.operations.delete `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 31/08/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Google Kubernetes Engine  |  Agregado  |  ` container.cronJobs.getStatus `  
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
  
Cloud Data Loss Prevention  |  Agregado  |  ` dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud Data Loss Prevention  |  Compatible con funciones personalizadas  |  `
dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud Source Repositories  |  Agregado  |  ` source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud Source Repositories  |  Compatible con funciones personalizadas  |  `
source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud Source Repositories  |  Ahora en etapa de disponibilidad general  |  `
source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 10/08/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Autorización binaria  |  Agregado  |  `
binaryauthorization.attestors.verifyImageAttested `  
  
Autorización binaria  |  Compatible con funciones personalizadas  |  `
binaryauthorization.attestors.verifyImageAttested `  
  
Compute Engine  |  Agregado  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  Agregado  |  ` file.instances.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 03/08/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
API de administración de Android  |  Compatible con funciones personalizadas
|  ` androidmanagement.enterprises.manage `  
  
API de administración de Android  |  Ahora en etapa de disponibilidad general
|  ` androidmanagement.enterprises.manage `  
  
Cloud Billing  |  Compatible con funciones personalizadas  |  `
billing.resourceCosts.get `  
  
Autorización binaria  |  Agregado  |  ` binaryauthorization.policy.get `  
` binaryauthorization.policy.getIamPolicy `  
` binaryauthorization.policy.setIamPolicy `  
` binaryauthorization.policy.update `  
  
Cloud Composer  |  Ahora en etapa de disponibilidad general  |  `
composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.nodeGroups.addNodes `  
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
  
Google Kubernetes Engine  |  Ahora en etapa de disponibilidad general  |  `
container.hostServiceAgent.use `  
  
Memorystore for Redis  |  Agregado  |  ` redis.operations.cancel `  
  
Memorystore for Redis  |  Compatible con funciones personalizadas  |  `
redis.instances.create `  
` redis.instances.delete `  
` redis.instances.get `  
` redis.instances.list `  
` redis.instances.update `  
` redis.locations.get `  
` redis.locations.list `  
` redis.operations.get `  
` redis.operations.list `  
  
Suscríbete con Google  |  Agregado  |  `
subscribewithgoogledeveloper.tools.get `  
  
Suscríbete con Google  |  Compatible con funciones personalizadas  |  `
subscribewithgoogledeveloper.tools.get `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 20/07/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Access Context Manager  |  Agregado  |  `
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
  
AutoML  |  Agregado  |  ` automl.annotationSpecs.create `  
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
  
AutoML  |  Compatible con funciones personalizadas  |  `
automl.annotationSpecs.create `  
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
  
Autorización binaria  |  Agregado  |  ` binaryauthorization.attestors.create `  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
Autorización binaria  |  Compatible con funciones personalizadas  |  `
binaryauthorization.attestors.create `  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
Cloud DNS  |  Compatible con funciones personalizadas  |  ` dns.changes.create
`  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 13/07/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
BigQuery  |  Agregado  |  ` bigquery.datasets.getIamPolicy `  
` bigquery.datasets.setIamPolicy `  
  
Datastore  |  Agregado  |  ` datastore.locations.get `  
` datastore.locations.list `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 06/07/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Composer  |  Compatible con funciones personalizadas  |  `
composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Endpoints  |  Agregado  |  ` endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud Endpoints  |  Compatible con funciones personalizadas  |  `
endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud TPU  |  Agregado  |  ` tpu.acceleratortypes.get `  
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
  
Cloud TPU  |  Compatible con funciones personalizadas  |  `
tpu.acceleratortypes.get `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 29/06/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Identity and Access Management  |  Ahora en etapa de disponibilidad
general  |  ` iam.serviceAccounts.implicitDelegation `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 15/06/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.backendServices.create `  
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
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.regionBackendServices.create `  
` compute.regionBackendServices.delete `  
` compute.regionBackendServices.get `  
` compute.regionBackendServices.list `  
` compute.regionBackendServices.setSecurityPolicy `  
` compute.regionBackendServices.update `  
` compute.regionBackendServices.use `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 08/06/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Agregado  |  ` compute.nodeGroups.addNodes `  
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
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.nodeGroups.addNodes `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 11/05/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
BigQuery  |  Compatible con funciones personalizadas  |  `
bigquery.jobs.listAll `  
  
Cloud Bigtable  |  Compatible con funciones personalizadas  |  `
bigtable.appProfiles.create `  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.clusters.create `  
` bigtable.clusters.delete `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Bigtable  |  Ahora en etapa de disponibilidad general  |  `
bigtable.appProfiles.create `  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Composer  |  Pasó a la etapa Beta.  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Life Sciences  |  Compatible con funciones personalizadas  |  `
genomics.operations.cancel `  
` genomics.operations.create `  
` genomics.operations.get `  
` genomics.operations.list `  
  
Cloud Monitoring  |  Compatible con funciones personalizadas  |  `
monitoring.dashboards.create `  
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
  
Cloud Monitoring  |  Ahora en etapa de disponibilidad general  |  `
monitoring.dashboards.create `  
` monitoring.dashboards.delete `  
` monitoring.dashboards.get `  
` monitoring.dashboards.list `  
` monitoring.dashboards.update `  
` monitoring.publicWidgets.create `  
` monitoring.publicWidgets.delete `  
` monitoring.publicWidgets.get `  
` monitoring.publicWidgets.list `  
` monitoring.publicWidgets.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 04/05/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
BigQuery  |  Disponible con funciones personalizadas  |  `
bigquery.jobs.listAll `  
  
Cloud Bigtable  |  Agregado  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  Compatible con funciones personalizadas  |  `
bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  Ahora en etapa de disponibilidad general  |  `
bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.oslogin.updateExternalUser `  
  
Service Management  |  Compatible con funciones personalizadas  |  `
servicemanagement.services.bind `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 06/04/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.instances.setShieldedVmIntegrityPolicy `  
` compute.instances.updateShieldedVmConfig `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.instances.setShieldedVmIntegrityPolicy `  
  
Google Kubernetes Engine  |  Compatible con funciones personalizadas  |  `
container.hostServiceAgent.use `  
  
Dataproc  |  Compatible con funciones personalizadas  |  `
dataproc.jobs.getIamPolicy `  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
Dataproc  |  Ahora en etapa de disponibilidad general  |  `
dataproc.jobs.getIamPolicy `  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 30/03/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud IoT  |  Ahora en etapa de disponibilidad general  |  `
cloudiot.devices.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 23/03/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Life Sciences  |  Compatible con funciones personalizadas  |  `
genomics.datasets.create `  
` genomics.datasets.delete `  
` genomics.datasets.get `  
` genomics.datasets.getIamPolicy `  
` genomics.datasets.list `  
` genomics.datasets.setIamPolicy `  
` genomics.datasets.update `  
  
Pub/Sub  |  Compatible con funciones personalizadas  |  `
pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.list `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 09/03/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Talent Solution  |  Agregado  |  ` cloudjobdiscovery.companies.create `  
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
  
Talent Solution  |  Compatible con funciones personalizadas  |  `
cloudjobdiscovery.companies.create `  
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
  
Cloud Profiler  |  Agregado  |  ` cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
Cloud Profiler  |  Compatible con funciones personalizadas  |  `
cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 02/03/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Agente de servicio abierto para Google Cloud  |  Agregado  |  `
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
  
Agente de servicio abierto para Google Cloud  |  Compatible con funciones
personalizadas  |  ` servicebroker.bindingoperations.get `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 23/02/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Resource Manager  |  Compatible con funciones personalizadas  |  `
resourcemanager.projects.list `  
` resourcemanager.projects.move `  
  
Service Management  |  Agregado  |  ` servicemanagement.services.quota `  
  
Service Management  |  Compatible con funciones personalizadas  |  `
servicemanagement.services.quota `  
  
Cloud Source Repositories  |  Compatible con funciones personalizadas  |  `
source.repos.create `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 16/02/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
BigQuery  |  Compatible con funciones personalizadas  |  `
bigquery.tables.update `  
` bigquery.tables.updateData `  
  
Cloud IoT  |  Compatible con funciones personalizadas  |  `
cloudiot.devices.create `  
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
  
Cloud SQL  |  Compatible con funciones personalizadas  |  `
cloudsql.instances.demoteMaster `  
  
Asistencia de Google Cloud  |  Agregado  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Compute Engine  |  Agregado  |  ` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.addresses.create `  
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
  
Dataproc  |  Compatible con funciones personalizadas  |  `
dataproc.agents.create `  
` dataproc.agents.delete `  
` dataproc.agents.get `  
` dataproc.agents.list `  
` dataproc.agents.update `  
` dataproc.tasks.lease `  
` dataproc.tasks.listInvalidatedLeases `  
` dataproc.tasks.reportStatus `  
` dataproc.workflowTemplates.instantiateInline `  
  
Cloud DNS  |  Agregado  |  ` dns.changes.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 02/02/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Disponible con funciones personalizadas  |  `
compute.interconnectAttachments.create `  
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
  
Cloud Data Loss Prevention  |  Agregado  |  ` dlp.jobTriggers.create `  
` dlp.jobTriggers.delete `  
` dlp.jobTriggers.get `  
` dlp.jobTriggers.list `  
` dlp.jobTriggers.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 26/01/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
BigQuery  |  Agregado  |  ` bigquery.jobs.listAll `  
  
Google Kubernetes Engine  |  Agregado  |  `
container.podSecurityPolicies.create `  
` container.podSecurityPolicies.delete `  
` container.podSecurityPolicies.get `  
` container.podSecurityPolicies.list `  
` container.podSecurityPolicies.update `  
` container.podSecurityPolicies.use `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 19/01/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Agregado  |  ` compute.addresses.createInternal `  
` compute.addresses.deleteInternal `  
` compute.addresses.useInternal `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 12/01/2018

Servicio  |  Cambio  |  Descripción  
---|---|---  
App Engine  |  No se admite en funciones personalizadas.  |  `
appengine.runtimes.actAsAdmin `  
  
Compute Engine  |  Agregado  |  ` compute.backendServices.setSecurityPolicy `  
` compute.securityPolicies.create `  
` compute.securityPolicies.delete `  
` compute.securityPolicies.get `  
` compute.securityPolicies.getIamPolicy `  
` compute.securityPolicies.list `  
` compute.securityPolicies.setIamPolicy `  
` compute.securityPolicies.update `  
` compute.securityPolicies.use `  
  
Compute Engine  |  No se admite en funciones personalizadas.  |  `
compute.organizations.administerXpn `  
` compute.targetHttpProxies.create `  
` compute.targetHttpProxies.setUrlMap `  
` compute.targetHttpsProxies.create `  
` compute.targetHttpsProxies.setUrlMap `  
` compute.targetSslProxies.create `  
` compute.targetSslProxies.setBackendService `  
` compute.targetTcpProxies.create `  
` compute.targetTcpProxies.update `  
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 22/12/2017

Servicio  |  Cambio  |  Descripción  
---|---|---  
App Engine  |  Compatible con funciones personalizadas  |  `
appengine.applications.create `  
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
  
App Engine  |  No se admite en funciones personalizadas.  |  `
appengine.applications.list `  
` appengine.operations.cancel `  
` appengine.operations.delete `  
` appengine.services.create `  
  
Cloud Billing  |  Compatible con funciones personalizadas  |  `
billing.accounts.close `  
` billing.accounts.reopen `  
` billing.budgets.delete `  
` billing.budgets.update `  
  
Depurador de Cloud  |  Compatible con funciones personalizadas  |  `
clouddebugger.breakpoints.create `  
` clouddebugger.breakpoints.delete `  
` clouddebugger.breakpoints.get `  
` clouddebugger.breakpoints.list `  
` clouddebugger.breakpoints.listActive `  
` clouddebugger.breakpoints.update `  
` clouddebugger.debuggees.create `  
` clouddebugger.debuggees.list `  
  
Cloud Key Management Service  |  Compatible con funciones personalizadas  |  `
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
  
Cloud SQL  |  Compatible con funciones personalizadas  |  `
cloudsql.backupRuns.create `  
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
  
Cloud SQL  |  No se admite en funciones personalizadas.  |  `
cloudsql.databases.getIamPolicy `  
` cloudsql.databases.setIamPolicy `  
` cloudsql.instances.demoteMaster `  
` cloudsql.instances.getIamPolicy `  
` cloudsql.instances.migrate `  
` cloudsql.instances.setIamPolicy `  
` cloudsql.sslCerts.createEphemeral `  
  
Cloud Trace  |  Compatible con funciones personalizadas  |  `
cloudtrace.insights.get `  
` cloudtrace.insights.list `  
` cloudtrace.stats.get `  
` cloudtrace.tasks.create `  
` cloudtrace.tasks.delete `  
` cloudtrace.tasks.get `  
` cloudtrace.tasks.list `  
` cloudtrace.traces.get `  
` cloudtrace.traces.list `  
` cloudtrace.traces.patch `  
  
Compute Engine  |  Agregado  |  ` compute.instances.setMachineResources `  
` compute.instances.setMinCpuPlatform `  
` compute.instances.setServiceAccount `  
` compute.instances.updateAccessConfig `  
` compute.instances.updateNetworkInterface `  
` compute.licenseCodes.get `  
` compute.licenseCodes.list `  
` compute.licenseCodes.update `  
` compute.licenseCodes.use `  
  
Compute Engine  |  Compatible con funciones personalizadas  |  `
compute.acceleratorTypes.get `  
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
  
Compute Engine  |  No se admite en funciones personalizadas.  |  `
compute.backendServices.create `  
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
  
Google Kubernetes Engine  |  Agregado  |  ` container.services.updateStatus `  
  
Google Kubernetes Engine  |  Compatible con funciones personalizadas  |  `
container.clusters.create `  
` container.clusters.delete `  
` container.clusters.get `  
` container.clusters.getCredentials `  
` container.clusters.list `  
` container.clusters.update `  
` container.operations.get `  
` container.operations.list `  
  
Dataproc  |  Compatible con funciones personalizadas  |  `
dataproc.clusters.create `  
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
  
Datastore  |  No se admite en funciones personalizadas.  |  `
datastore.databases.create `  
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
  
Cloud Deployment Manager  |  Compatible con funciones personalizadas  |  `
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
  
Dialogflow  |  Compatible con funciones personalizadas  |  `
dialogflow.agents.export `  
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
  
Error Reporting  |  Compatible con funciones personalizadas  |  `
errorreporting.applications.list `  
` errorreporting.errorEvents.create `  
` errorreporting.errorEvents.delete `  
` errorreporting.errorEvents.list `  
` errorreporting.groupMetadata.get `  
` errorreporting.groupMetadata.update `  
` errorreporting.groups.list `  
  
Cloud Identity and Access Management  |  No se admite en funciones
personalizadas.  |  ` iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
Cloud Logging  |  Compatible con funciones personalizadas  |  `
logging.exclusions.create `  
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
  
AI Platform  |  Compatible con funciones personalizadas  |  ` ml.jobs.cancel `  
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
  
Cloud Monitoring  |  Compatible con funciones personalizadas  |  `
monitoring.groups.create `  
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
  
Pub/Sub  |  Compatible con funciones personalizadas  |  `
pubsub.topics.setIamPolicy `  
  
Service Management  |  Compatible con funciones personalizadas  |  `
servicemanagement.services.check `  
` servicemanagement.services.report `  
  
Service Management  |  No se admite en funciones personalizadas.  |  `
servicemanagement.consumerSettings.get `  
` servicemanagement.consumerSettings.getIamPolicy `  
` servicemanagement.consumerSettings.list `  
` servicemanagement.consumerSettings.setIamPolicy `  
` servicemanagement.consumerSettings.update `  
  
Cloud Source Repositories  |  Compatible con funciones personalizadas  |  `
source.repos.delete `  
` source.repos.get `  
` source.repos.getIamPolicy `  
` source.repos.list `  
` source.repos.setIamPolicy `  
  
Cloud Source Repositories  |  No compatible con funciones personalizadas  |  `
source.repos.update `  
  
Cloud Spanner  |  Compatible con funciones personalizadas  |  `
spanner.databaseOperations.cancel `  
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
  
Cloud Spanner  |  No se admite en funciones personalizadas.  |  `
spanner.databaseOperations.delete `  
` spanner.databases.update `  
  
Cloud Storage  |  Compatible con funciones personalizadas  |  `
storage.buckets.create `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 08/12/2017

Servicio  |  Cambio  |  Descripción  
---|---|---  
BigQuery  |  Compatible con funciones personalizadas  |  `
bigquery.datasets.create `  
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
  
BigQuery  |  No se admite en funciones personalizadas.  |  `
bigquery.config.get `  
` bigquery.config.update `  
` bigquery.service.actAsSuperuser `  
` bigquery.tables.update `  
` bigquery.tables.updateData `  
` bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Cloud Bigtable  |  Compatible con funciones personalizadas  |  `
bigtable.clusters.get `  
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
  
Compute Engine  |  Agregado  |  ` compute.disks.getIamPolicy `  
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
  
Dataflow  |  Compatible con funciones personalizadas  |  `
dataflow.jobs.cancel `  
` dataflow.jobs.create `  
` dataflow.jobs.get `  
` dataflow.jobs.list `  
` dataflow.jobs.updateContents `  
` dataflow.messages.list `  
` dataflow.metrics.get `  
  
Dataproc  |  Agregado  |  ` dataproc.workflowTemplates.instantiateInline `  
  
Cloud Data Loss Prevention  |  Agregado  |  ` dlp.analyzeRiskTemplates.create
`  
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
  
Pub/Sub  |  Agregado  |  ` pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.get `  
` pubsub.snapshots.getIamPolicy `  
` pubsub.snapshots.list `  
` pubsub.snapshots.seek `  
` pubsub.snapshots.setIamPolicy `  
` pubsub.snapshots.update `  
  
Pub/Sub  |  Compatible con funciones personalizadas  |  `
pubsub.subscriptions.consume `  
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
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 01/12/2017

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Build  |  Compatible con funciones personalizadas  |  `
cloudbuild.builds.create `  
` cloudbuild.builds.get `  
` cloudbuild.builds.list `  
` cloudbuild.builds.update `  
  
Resultados de herramientas de Cloud  |  Ahora en etapa de disponibilidad
general  |  ` cloudtoolresults.executions.create `  
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
  
Compute Engine  |  Ahora en etapa de disponibilidad general  |  `
compute.instances.addMaintenancePolicies `  
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
  
Google Kubernetes Engine  |  Agregado  |  `
container.initializerConfigurations.create `  
` container.initializerConfigurations.delete `  
` container.initializerConfigurations.get `  
` container.initializerConfigurations.list `  
` container.initializerConfigurations.update `  
` container.pods.initialize `  
  
Google Kubernetes Engine  |  Ahora en etapa de disponibilidad general  |  `
container.deployments.getScale `  
` container.deployments.updateScale `  
  
Dataprep de Trifacta  |  Compatible con funciones personalizadas  |  `
dataprep.projects.use `  
  
Cloud Identity and Access Management  |  Compatible con funciones
personalizadas  |  ` iam.roles.create `  
` iam.roles.delete `  
` iam.roles.get `  
` iam.roles.list `  
` iam.roles.undelete `  
` iam.roles.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 10/11/2017

Servicio  |  Cambio  |  Descripción  
---|---|---  
Google Kubernetes Engine  |  Agregado  |  ` container.clusters.getIamPolicy `  
` container.clusters.setIamPolicy `  
  
AI Platform  |  Agregado  |  ` ml.locations.get `  
` ml.locations.list `  
  
Cloud Monitoring  |  Agregado  |  ` monitoring.metricDescriptors.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 27/10/2017

Servicio  |  Cambio  |  Descripción  
---|---|---  
Compute Engine  |  Agregado  |  ` compute.instances.updateShieldedVmConfig `  
  
Identity-Aware Proxy  |  Agregado  |  ` iap.web.getIamPolicy `  
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
  
Service Management  |  Compatible con funciones personalizadas  |  `
servicemanagement.services.create `  
` servicemanagement.services.delete `  
` servicemanagement.services.get `  
` servicemanagement.services.getIamPolicy `  
` servicemanagement.services.list `  
` servicemanagement.services.setIamPolicy `  
` servicemanagement.services.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 06/10/2017

Servicio  |  Cambio  |  Descripción  
---|---|---  
Dataproc  |  Ahora en etapa de disponibilidad general  |  `
dataproc.workflowTemplates.create `  
` dataproc.workflowTemplates.delete `  
` dataproc.workflowTemplates.get `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.instantiate `  
` dataproc.workflowTemplates.list `  
` dataproc.workflowTemplates.setIamPolicy `  
` dataproc.workflowTemplates.update `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 22/09/2017

Servicio  |  Cambio  |  Descripción  
---|---|---  
App Engine  |  Agregado  |  ` appengine.memcache.addKey `  
` appengine.memcache.flush `  
` appengine.memcache.get `  
` appengine.memcache.getKey `  
` appengine.memcache.list `  
` appengine.memcache.update `  
  
Cloud SQL  |  Agregado  |  ` cloudsql.instances.demoteMaster `  
  
Cloud SQL  |  Ahora en etapa de disponibilidad general  |  `
cloudsql.instances.demoteMaster `  
  
  
##  Cambios que se realizaron en Cloud IAM hasta el 08/09/2017

Servicio  |  Cambio  |  Descripción  
---|---|---  
Cloud Functions  |  Agregado  |  ` cloudfunctions.functions.call `  
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
  
Compute Engine  |  Agregado  |  ` compute.instances.setDeletionProtection `  
` compute.targetHttpsProxies.setUrlMap `  
  
Google Kubernetes Engine  |  Agregado  |  ` container.statefulSets.getScale `  
` container.statefulSets.updateScale `  
  
Google Kubernetes Engine  |  Ahora en etapa de disponibilidad general  |  `
container.statefulSets.getScale `  
` container.statefulSets.updateScale `  
  
Cloud Functions  |  Agregado  |  ` dlp.kms.encrypt `  
` dlp.riskAnalysisOperations.cancel `  
` dlp.riskAnalysisOperations.create `  
` dlp.riskAnalysisOperations.get `  
` dlp.riskAnalysisOperations.list `  

