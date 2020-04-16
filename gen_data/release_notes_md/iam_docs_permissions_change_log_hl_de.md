#  Änderungslog der IAM-Berechtigungen

Auf dieser Seite werden Änderungen an den öffentlichen Cloud IAM-
Berechtigungen für alle allgemein verfügbaren Dienste und Betadienste in
Google Cloud beschrieben. Dieses Änderungslog unterstützt Sie dabei, Ihre [
benutzerdefinierten Rollen ](https://cloud.google.com/iam/docs/understanding-
custom-roles?hl=de) zu verwalten und Fehler zu beheben.

Wenn eine Berechtigung für benutzerdefinierte Rollen eingestellt wurde oder
nicht mehr unterstützt wird, entfernt Cloud IAM die Berechtigung automatisch
aus Ihren benutzerdefinierten Rollen. Wird dagegen eine Berechtigung
hinzugefügt, fügt Cloud IAM die Berechtigung _nicht_ automatisch Ihren
benutzerdefinierten Rollen hinzu.

Für neueste Produktaktualisierungen können Sie die URL dieser Seite in einen [
Feedreader ](https://wikipedia.org/wiki/Comparison_of_feed_aggregators)
einfügen oder die Feed-URL direkt hinzufügen: `
https://cloud.google.com/feeds/cloud-iam-permissions-change-log.xml `

Änderungslog der IAM-Berechtigungen

##  Cloud IAM-Änderungen mit Wirkung ab der Woche vom 02.03.2020

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  Rolle aktualisiert  |

Der Rolle ` roles/compute.networkAdmin ` (Compute Network Admin) wurden die
folgenden Berechtigungen hinzugefügt:

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
Compute Engine  |  Rolle aktualisiert  |

Die folgenden Berechtigungen wurden der Rolle ` roles/compute.networkViewer `
hinzugefügt (Compute Network Viewer):

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/editor ` (Bearbeiter) wurden folgende Berechtigungen
hinzugefügt:

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
  
Cloud Identity and Access Management  |  Rolle aktualisiert  |

Der Rolle ` roles/iam.securityAdmin ` (Sicherheitsadministrator) wurden die
folgenden Berechtigungen hinzugefügt:

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
Cloud Identity and Access Management  |  Rolle aktualisiert  |

Zur Rolle ` roles/iam.securityReviewer ` (Sicherheitsprüfer) wurden folgende
Berechtigungen hinzugefügt:

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
Identity Platform  |  Rolle hinzugefügt  |

Die Rolle ` roles/identityplatform.admin ` (Identity Platform Admin) wurde mit
den folgenden Berechtigungen hinzugefügt:

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
  
Identity Platform  |  Rolle hinzugefügt  |

Die Rolle ` roles/identityplatform.viewer ` (Identity Platform Viewer) wurde
mit den folgenden Berechtigungen hinzugefügt:

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
  
Network Management API  |  Jetzt GA  |

Die Rolle ` roles/networkmanagement.admin ` (Network Management Admin) ist
jetzt GA.  
  
Network Management API  |  Jetzt GA  |

Die Rolle ` roles/networkmanagement.viewer ` (Network Management Viewer) ist
jetzt GA.  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/owner ` (Inhaber) wurden folgende Berechtigungen
hinzugefügt:

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
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/viewer ` (Betrachter) wurden folgende Berechtigungen
hinzugefügt:

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.get `  
` servicedirectory.locations.list `  
  
BigQuery  |  Hinzugefügt:  |  ` bigquery.bireservations.get `  
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
  
BigQuery  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Identity Platform  |  Hinzugefügt:  |  `
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
  
Network Management API  |  Jetzt GA  |  `
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
  
Memorystore for Redis  |  Hinzugefügt:  |  ` redis.instances.failover `  
` redis.instances.upgrade `  
  
Memorystore for Redis  |  In benutzerdefinierten Rollen unterstützt  |  `
redis.instances.failover `  
` redis.instances.upgrade `  
  
Service Directory  |  Hinzugefügt:  |  ` servicedirectory.endpoints.create `  
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
  
Service Directory  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 27.02.2020

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
BigQuery  |  Jetzt GA  |

Die Rolle ` roles/bigquery.readSessionUser ` (BigQuery Read Session User) ist
jetzt GA.  
  
Data Catalog  |  Rolle aktualisiert  |

Die folgenden Berechtigungen wurden zur Rolle `
roles/datacatalog.entryGroupCreator ` hinzugefügt (DataCatalog EntryGroup
Creator):

` datacatalog.entryGroups.list `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/editor ` (Bearbeiter) wurden folgende Berechtigungen
hinzugefügt:

` dlp.jobs.create `  
` dlp.jobs.get `  
` dlp.jobs.list `  
  
Secret Manager  |  Rolle aktualisiert  |

Die folgenden Berechtigungen wurden der Rolle `
roles/secretmanager.secretAccessor ` (Secret Manager Secret Accessor)
hinzugefügt:

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Security Command Center  |  Rolle aktualisiert  |

Zur Rolle ` roles/securitycenter.adminEditor ` (Sicherheitscenter-
Administratorbearbeiter) wurden folgende Berechtigungen hinzugefügt:

` securitycenter.organizationsettings.get `  
  
Security Command Center  |  Rolle aktualisiert  |

Die folgenden Berechtigungen wurden der Rolle `
roles/securitycenter.adminViewer ` hinzugefügt (Sicherheitscenter-Admin-
Betrachter):

` securitycenter.organizationsettings.get `  
  
Cloud Spanner  |  Jetzt GA  |

Die Rolle ` roles/spanner.backupAdmin ` (Cloud Spanner Backup Admin) ist jetzt
GA.  
  
Cloud Spanner  |  Jetzt GA  |

Die Rolle ` roles/spanner.backupWriter ` (Cloud Spanner Backup Writer) ist
jetzt GA.  
  
Cloud Spanner  |  Jetzt GA  |

Die Rolle ` roles/spanner.restoreAdmin ` (Cloud Spanner Restore Admin) ist
jetzt GA.  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/viewer ` (Betrachter) wurden folgende Berechtigungen
hinzugefügt:

` dlp.jobs.get `  
` dlp.jobs.list `  
  
BigQuery  |  Hinzugefügt:  |  ` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  In benutzerdefinierten Rollen unterstützt  |  `
bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  Jetzt GA  |  ` bigquery.readsessions.create `  
` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
Data Catalog  |  Hinzugefügt:  |  ` datacatalog.entryGroups.list `  
  
Data Catalog  |  In benutzerdefinierten Rollen unterstützt  |  `
datacatalog.entryGroups.list `  
  
Cloud Healthcare API  |  In benutzerdefinierten Rollen unterstützt  |  `
healthcare.fhirStores.executeBundle `  
  
Cloud Identity and Access Management  |  In benutzerdefinierten Rollen
unterstützt  |  ` iam.serviceAccounts.getOpenIdToken `  
  
Cloud Spanner  |  Hinzugefügt:  |  ` spanner.backupOperations.cancel `  
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
  
Cloud Spanner  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Cloud Spanner  |  Jetzt GA  |  ` spanner.backupOperations.cancel `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 21.02.2020

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Access Context Manager  |  Hinzugefügt:  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Access Context Manager  |  Jetzt GA  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.regionHealthCheckServices.create
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
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 14.02.2020

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Google Cloud-Support  |  Jetzt GA  |

Die Rolle ` roles/cloudsupport.techSupportEditor ` (Tech Support Editor) ist
jetzt GA.  
  
Google Cloud-Support  |  Jetzt GA  |

Die Rolle ` roles/cloudsupport.techSupportViewer ` (Tech Support Viewer) ist
jetzt GA.  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/editor ` (Bearbeiter) wurden folgende Berechtigungen
hinzugefügt:

` healthcare.fhirStores.executeBundle `  
  
Cloud Healthcare API  |  Rolle aktualisiert  |

Die folgenden Berechtigungen wurden der Rolle `
roles/healthcare.fhirResourceEditor ` (Healthcare FHIR Resource Editor)
hinzugefügt:

` healthcare.fhirStores.executeBundle `  
  
Cloud Healthcare API  |  Rolle aktualisiert  |

Die folgenden Berechtigungen wurden zur Rolle `
roles/healthcare.fhirResourceReader ` (Healthcare FHIR Resource Reader)
hinzugefügt:

` healthcare.fhirStores.executeBundle `  
  
Cloud Logging  |  Rolle aktualisiert  |

Der Rolle ` roles/logging.privateLogViewer ` (Private Logs Viewer) wurden die
folgenden Berechtigungen hinzugefügt:

` logging.buckets.get `  
` logging.buckets.list `  
  
Cloud Logging  |  Rolle aktualisiert  |

Der Rolle ` roles/logging.viewer ` (Log-Betrachter) wurden die folgenden
Berechtigungen hinzugefügt:

` logging.buckets.get `  
` logging.buckets.list `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/owner ` (Inhaber) wurden folgende Berechtigungen
hinzugefügt:

` healthcare.fhirStores.executeBundle `  
  
Security Command Center  |  Rolle aktualisiert  |

Zur Rolle ` roles/securitycenter.admin ` (Sicherheitscenter-Administrator)
wurden folgende Berechtigungen hinzugefügt:

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
  
Security Command Center  |  Rolle aktualisiert  |

Zur Rolle ` roles/securitycenter.adminEditor ` (Sicherheitscenter-
Administratorbearbeiter) wurden folgende Berechtigungen hinzugefügt:

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
  
Security Command Center  |  Rolle aktualisiert  |

Die folgenden Berechtigungen wurden der Rolle `
roles/securitycenter.adminViewer ` hinzugefügt (Sicherheitscenter-Admin-
Betrachter):

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
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/viewer ` (Betrachter) wurden folgende Berechtigungen
hinzugefügt:

` healthcare.fhirStores.executeBundle `  
  
Google Cloud-Support  |  Hinzugefügt:  |  ` cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Google Cloud-Support  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Google Cloud-Support  |  Jetzt GA  |  ` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Cloud Healthcare API  |  Hinzugefügt:  |  `
healthcare.fhirStores.executeBundle `  
  
Cloud Logging  |  Hinzugefügt:  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud Logging  |  In benutzerdefinierten Rollen unterstützt  |  `
logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud Logging  |  Jetzt GA  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 07.02.2020

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Secret Manager  |  Jetzt GA  |

Die Rolle ` roles/secretmanager.admin ` (Secret Manager-Administrator) ist
jetzt GA.  
  
Secret Manager  |  Jetzt GA  |

Die Rolle ` roles/secretmanager.secretAccessor ` (Secret Manager Secret
Accessor) ist jetzt GA.  
  
Secret Manager  |  Jetzt GA  |

Die Rolle ` roles/secretmanager.viewer ` (Secret Manager Viewer) ist jetzt GA.  
  
Cloud Healthcare API  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
reCAPTCHA Enterprise  |  Hinzugefügt:  |  `
recaptchaenterprise.assessments.annotate `  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
reCAPTCHA Enterprise  |  In benutzerdefinierten Rollen unterstützt  |  `
recaptchaenterprise.assessments.annotate `  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
Secret Manager  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Secret Manager  |  Jetzt GA  |  ` secretmanager.locations.get `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 31.01.2020

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Build  |  Rolle aktualisiert  |

Die folgenden Berechtigungen wurden der Rolle `
roles/cloudbuild.builds.builder ` (Cloud Build-Dienstkonto) hinzugefügt:

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
  
Cloud Composer  |  Rolle aktualisiert  |

Der Rolle ` roles/composer.worker ` (Composer Worker) wurden die folgenden
Berechtigungen hinzugefügt:

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
  
Google Cloud Game Servers  |  Hinzugefügt:  |  `
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
  
Google Cloud Game Servers  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Google Cloud Operations Suite  |  Hinzugefügt:  |  `
opsconfigmonitoring.resourceMetadata.write `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 24.01.2020

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Scheduler  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudscheduler.admin ` (Cloud Scheduler-Administrator)
wurden folgende Berechtigungen hinzugefügt:

` serviceusage.services.list `  
  
Cloud Scheduler  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudscheduler.jobRunner ` (Cloud Scheduler-Jobinitiator)
wurden folgende Berechtigungen hinzugefügt:

` serviceusage.services.list `  
  
Cloud Scheduler  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudscheduler.viewer ` (Cloud Scheduler-Betrachter) wurden
folgende Berechtigungen hinzugefügt:

` serviceusage.services.list `  
  
Compute Engine  |  Rolle aktualisiert  |

Der Rolle ` roles/compute.networkAdmin ` (Compute Network Admin) wurden die
folgenden Berechtigungen hinzugefügt:

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
Compute Engine  |  Rolle aktualisiert  |

Die folgenden Berechtigungen wurden der Rolle ` roles/compute.networkViewer `
hinzugefügt (Compute Network Viewer):

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.notificationConfigEditor ` (Security Center
Notification Configurations Editor) ist jetzt GA.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.notificationConfigViewer ` (Security Center
Notifications Configurations Viewer) ist jetzt GA.  
  
Artifact Registry  |  Hinzugefügt:  |  ` artifactregistry.files.get `  
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
  
Artifact Registry  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Cloud Identity and Access Management  |  Hinzugefügt:  |  `
iam.serviceAccounts.getOpenIdToken `  
  
Security Command Center  |  Hinzugefügt:  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
Security Command Center  |  In benutzerdefinierten Rollen unterstützt  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
Security Command Center  |  Jetzt GA  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 10.01.2020

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Asset Inventory  |  Jetzt GA  |

Die Rolle ` roles/cloudasset.owner ` (Cloud Asset-Inhaber) ist jetzt allgemein
verfügbar.  
  
Migrate for Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudmigration.inframanager ` (Velostrata Manager) wurden
folgende Berechtigungen hinzugefügt:

` compute.globalOperations.get `  
  
Cloud Spanner  |  Rolle aktualisiert  |

Zur Rolle ` roles/spanner.databaseReader ` (Cloud Spanner-Datenbank-Leser)
wurden folgende Berechtigungen hinzugefügt:

` spanner.instances.get `  
  
Cloud Spanner  |  Rolle aktualisiert  |

Zur Rolle ` roles/spanner.databaseUser ` (Cloud Spanner-Datenbank-Nutzer)
wurden folgende Berechtigungen hinzugefügt:

` spanner.instances.get `  
  
Cloud Asset Inventory  |  Jetzt GA  |  ` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.networks.listPeeringRoutes `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.networks.listPeeringRoutes `  
  
Compute Engine  |  Jetzt GA  |  ` compute.networks.listPeeringRoutes `  
  
Network Management API  |  Hinzugefügt:  |  `
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
  
Network Management API  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 20.12.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Migrate for Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudmigration.inframanager ` (Velostrata Manager) wurden
folgende Berechtigungen hinzugefügt:

` compute.disks.createSnapshot `  
` compute.snapshots.create `  
` compute.snapshots.delete `  
` compute.snapshots.get `  
` compute.snapshots.setLabels `  
` compute.snapshots.useReadOnly `  
  
Cloud Scheduler  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudscheduler.admin ` (Cloud Scheduler-Administrator)
wurden folgende Berechtigungen hinzugefügt:

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud Scheduler  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudscheduler.jobRunner ` (Cloud Scheduler-Jobinitiator)
wurden folgende Berechtigungen hinzugefügt:

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud Scheduler  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudscheduler.viewer ` (Cloud Scheduler-Betrachter) wurden
folgende Berechtigungen hinzugefügt:

` appengine.applications.get `  
` serviceusage.services.get `  
  
Compute Engine  |  Jetzt GA  |

Die Rolle ` roles/compute.packetMirroringAdmin ` (Administrator der Compute-
Paketspiegelung) ist jetzt allgemein verfügbar.  
  
Compute Engine  |  Jetzt GA  |

Die Rolle ` roles/compute.packetMirroringUser ` (Nutzer der Compute-
Paketspiegelung) ist jetzt allgemein verfügbar.  
  
Cloud DNS  |  Jetzt GA  |

Die Rolle ` roles/dns.peer ` (DNS-Peer) ist jetzt allgemein verfügbar.  
  
Einfache Rolle  |  Rolle aktualisiert  |

Aus der Rolle ` roles/editor ` (Bearbeiter) wurden folgende Berechtigungen
entfernt:

` datacatalog.taxonomies.create `  
  
Recommender  |  Jetzt GA  |

Die Rolle ` roles/recommender.computeAdmin ` (Compute Recommender-
Administrator) ist jetzt allgemein verfügbar.  
  
Recommender  |  Jetzt GA  |

Die Rolle ` roles/recommender.computeViewer ` (Compute Recommender-Betrachter)
ist jetzt allgemein verfügbar.  
  
Recommender  |  Jetzt GA  |

Die Rolle ` roles/recommender.iamAdmin ` (IAM Recommender-Administrator) ist
jetzt allgemein verfügbar.  
  
Recommender  |  Jetzt GA  |

Die Rolle ` roles/recommender.iamViewer ` (IAM Recommender-Betrachter) ist
jetzt allgemein verfügbar.  
  
Remote Build Execution  |  Rolle hinzugefügt  |

Die Rolle ` roles/remotebuildexecution.reservationAdmin ` (Remote Build
Execution Reservation-Administrator) wurde mit den folgenden Berechtigungen
hinzugefügt:

` remotebuildexecution.actions.create `  
` remotebuildexecution.actions.delete `  
` remotebuildexecution.actions.get `  
  
Cloud Bigtable  |  Hinzugefügt:  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  In benutzerdefinierten Rollen unterstützt  |  `
bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  Jetzt GA  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.nodeGroups.update `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.nodeGroups.update `  
  
Compute Engine  |  Jetzt GA  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Data Catalog  |  Hinzugefügt:  |  ` datacatalog.entries.list `  
` datacatalog.entries.updateTag `  
` datacatalog.entryGroups.update `  
  
Dataproc  |  Hinzugefügt:  |  ` dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
Dataproc  |  Jetzt GA  |  ` dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
Cloud DNS  |  Jetzt GA  |  ` dns.networks.targetWithPeeringZone `  
  
Cloud Logging  |  Hinzugefügt:  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud Logging  |  In benutzerdefinierten Rollen unterstützt  |  `
logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud Logging  |  Jetzt GA  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Recommender  |  Jetzt GA  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 22.11.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Data Catalog  |  Rolle aktualisiert  |

Aus der Rolle ` roles/datacatalog.admin ` (Data Catalog-Administrator) wurden
folgende Berechtigungen entfernt:

` datacatalog.categories.fineGrainedGet `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/editor ` (Bearbeiter) wurden folgende Berechtigungen
hinzugefügt:

` remotebuildexecution.actions.delete `  
  
Identity Toolkit API  |  Jetzt GA  |

Die Rolle ` roles/identitytoolkit.admin ` (Identity Toolkit-Administrator) ist
jetzt allgemein verfügbar.  
  
Identity Toolkit API  |  Jetzt GA  |

Die Rolle ` roles/identitytoolkit.viewer ` (Identity Toolkit-Betrachter) ist
jetzt allgemein verfügbar.  
  
Apigee API  |  Hinzugefügt:  |  `
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
  
Apigee API  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
BigQuery  |  Hinzugefügt:  |  ` bigquery.tables.setCategory `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Remote Build Execution  |  Hinzugefügt:  |  `
remotebuildexecution.actions.delete `  
  
Remote Build Execution  |  In benutzerdefinierten Rollen unterstützt  |  `
remotebuildexecution.actions.delete `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 14.11.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Zugriffsgenehmigung  |  Hinzugefügt:  |  ` accessapproval.settings.delete `  
  
AI Platform Notebooks  |  Hinzugefügt:  |  ` notebooks.environments.create `  
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
  
AI Platform Notebooks  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 01.11.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Hangouts Chat API  |  Jetzt GA  |

Die Rolle ` roles/chat.owner ` (Chatbots-Inhaber) ist jetzt allgemein
verfügbar.  
  
Hangouts Chat API  |  Jetzt GA  |

Die Rolle ` roles/chat.reader ` (Chatbots-Betrachter) ist jetzt allgemein
verfügbar.  
  
Hangouts Chat API  |  Jetzt GA  |  ` chat.bots.get `  
` chat.bots.update `  
  
Cloud Asset Inventory  |  Hinzugefügt:  |  `
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
  
Data Catalog  |  Hinzugefügt:  |  ` datacatalog.categories.fineGrainedGet `  
` datacatalog.categories.getIamPolicy `  
` datacatalog.categories.setIamPolicy `  
` datacatalog.taxonomies.create `  
` datacatalog.taxonomies.delete `  
` datacatalog.taxonomies.get `  
` datacatalog.taxonomies.getIamPolicy `  
` datacatalog.taxonomies.list `  
` datacatalog.taxonomies.setIamPolicy `  
` datacatalog.taxonomies.update `  
  
Identity-Aware Proxy  |  Hinzugefügt:  |  ` iap.projects.getSettings `  
` iap.projects.updateSettings `  
  
NetApp Cloud Volumes-Dienst  |  Hinzugefügt:  |  ` netappcloudvolumes.jobs.get
`  
` netappcloudvolumes.jobs.list `  
  
Redis Enterprise Cloud  |  Hinzugefügt:  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 25.10.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Identity-Aware Proxy  |  Jetzt GA  |

Die Rolle ` roles/iap.tunnelResourceAccessor ` (Nutzer IAP-gesicherter Tunnel)
ist jetzt allgemein verfügbar.  
  
Managed Service for Microsoft Active Directory  |  Jetzt GA  |

Die Rolle ` roles/managedidentities.admin ` (Google Cloud Managed Identities-
Administrator) ist jetzt allgemein verfügbar.  
  
Managed Service for Microsoft Active Directory  |  Jetzt GA  |

Die Rolle ` roles/managedidentities.domainAdmin ` (Google Cloud Managed
Identities-Domainadministrator) ist jetzt allgemein verfügbar.  
  
Managed Service for Microsoft Active Directory  |  Jetzt GA  |

Die Rolle ` roles/managedidentities.viewer ` (Google Cloud Managed Identities-
Betrachter) ist jetzt allgemein verfügbar.  
  
Actions API  |  Hinzugefügt:  |  ` actions.agentVersions.get `  
  
Actions API  |  In benutzerdefinierten Rollen unterstützt  |  `
actions.agentVersions.get `  
  
Actions API  |  Jetzt GA  |  ` actions.agentVersions.get `  
  
Dialogflow  |  Hinzugefügt:  |  ` dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
Dialogflow  |  Jetzt GA  |  ` dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
Identity-Aware Proxy  |  Jetzt GA  |  ` iap.tunnel.getIamPolicy `  
` iap.tunnel.setIamPolicy `  
` iap.tunnelInstances.accessViaIAP `  
` iap.tunnelInstances.getIamPolicy `  
` iap.tunnelInstances.setIamPolicy `  
` iap.tunnelZones.getIamPolicy `  
` iap.tunnelZones.setIamPolicy `  
  
Managed Service for Microsoft Active Directory  |  Jetzt GA  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 18.10.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Identity-Aware Proxy  |  Jetzt GA  |

Die Rolle ` roles/iap.settingsAdmin ` (Administrator IAP-Einstellungen) ist
jetzt allgemein verfügbar.  
  
Identity-Aware Proxy  |  Hinzugefügt:  |  ` iap.web.getSettings `  
` iap.web.updateSettings `  
` iap.webServiceVersions.getSettings `  
` iap.webServiceVersions.updateSettings `  
` iap.webServices.getSettings `  
` iap.webServices.updateSettings `  
` iap.webTypes.getSettings `  
` iap.webTypes.updateSettings `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 11.10.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Firebase-Sicherheitsregeln  |  Jetzt GA  |

Die Rolle ` roles/firebaserules.admin ` (Administrator von Firebase-Regeln)
ist jetzt allgemein verfügbar.  
  
Firebase-Sicherheitsregeln  |  Jetzt GA  |

Die Rolle ` roles/firebaserules.viewer ` (Betrachter von Firebase-Regeln) ist
jetzt allgemein verfügbar.  
  
BigQuery  |  In benutzerdefinierten Rollen unterstützt  |  `
bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Google Kubernetes Engine  |  Hinzugefügt  |  ` container.csiDrivers.create `  
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
  
Google Kubernetes Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Google Kubernetes Engine  |  Jetzt GA  |  ` container.csiDrivers.create `  
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
  
Firebase-Sicherheitsregeln  |  Jetzt GA  |  ` firebaserules.releases.create `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 04.10.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Actions API  |  Hinzugefügt:  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Actions API  |  In benutzerdefinierten Rollen unterstützt  |  `
actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Actions API  |  Jetzt GA  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Cloud Identity and Access Management  |  In benutzerdefinierten Rollen
unterstützt  |  ` iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 27.09.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Hangouts Chat API  |  Hinzugefügt:  |  ` chat.bots.get `  
` chat.bots.update `  
  
Hangouts Chat API  |  In benutzerdefinierten Rollen unterstützt  |  `
chat.bots.get `  
` chat.bots.update `  
  
Cloud Asset Inventory  |  Hinzugefügt  |  `
cloudasset.assets.exportAccessLevel `  
` cloudasset.assets.exportAccessPolicy `  
` cloudasset.assets.exportAllAccessPolicy `  
` cloudasset.assets.exportOrgPolicy `  
` cloudasset.assets.exportServicePerimeter `  
` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Cloud Asset Inventory  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudasset.assets.exportAccessPolicy `  
` cloudasset.assets.exportOrgPolicy `  
` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Cloud Identity and Access Management  |  In benutzerdefinierten Rollen
unterstützt  |  ` iam.serviceAccountKeys.create `  
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
  
VM Migration API  |  Hinzugefügt:  |  ` vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
VM Migration API  |  In benutzerdefinierten Rollen unterstützt  |  `
vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 20.09.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Key Management Service  |  Jetzt GA  |

Die Rolle ` roles/cloudkms.importer ` (Cloud KMS-Importeur) ist jetzt
allgemein verfügbar.  
  
Cloud Key Management Service  |  Jetzt GA  |

Die Rolle ` roles/cloudkms.publicKeyViewer ` (PublicKey-Betrachter für Cloud
KMS CryptoKeys) ist jetzt allgemein verfügbar.  
  
Cloud Key Management Service  |  Jetzt GA  |

Die Rolle ` roles/cloudkms.signer ` (Cloud KMS CryptoKey-Signer) ist jetzt
allgemein verfügbar.  
  
Cloud Key Management Service  |  Jetzt GA  |

Die Rolle ` roles/cloudkms.signerVerifier ` (Cloud KMS CryptoKey-
Signer/Prüffunktion) ist jetzt allgemein verfügbar.  
  
Cloud Key Management Service  |  Hinzugefügt:  |  ` cloudkms.importJobs.create
`  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  In benutzerdefinierten Rollen unterstützt  |
` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  Jetzt GA  |  `
cloudkms.cryptoKeyVersions.useToSign `  
` cloudkms.cryptoKeyVersions.viewPublicKey `  
` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 13.09.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Firebase Remote Config  |  Jetzt GA  |

Die Rolle ` roles/cloudconfig.admin ` (Firebase Remote Config-Administrator)
ist jetzt allgemein verfügbar.  
  
Firebase Remote Config  |  Jetzt GA  |

Die Rolle ` roles/cloudconfig.viewer ` (Firebase Remote Config-Betrachter) ist
jetzt allgemein verfügbar.  
  
Firebase  |  Jetzt GA  |

Die Rolle ` roles/firebase.admin ` (Firebase-Administrator) ist jetzt
allgemein verfügbar.  
  
Firebase  |  Jetzt GA  |

Die Rolle ` roles/firebase.analyticsAdmin ` (Firebase Analytics-Administrator)
ist jetzt allgemein verfügbar.  
  
Firebase  |  Jetzt GA  |

Die Rolle ` roles/firebase.analyticsViewer ` (Firebase Analytics-Betrachter)
ist jetzt allgemein verfügbar.  
  
Firebase  |  Jetzt GA  |

Die Rolle ` roles/firebase.developAdmin ` (Firebase Develop-Administrator) ist
jetzt allgemein verfügbar.  
  
Firebase  |  Jetzt GA  |

Die Rolle ` roles/firebase.developViewer ` (Firebase Develop-Betrachter) ist
jetzt allgemein verfügbar.  
  
Firebase  |  Jetzt GA  |

Die Rolle ` roles/firebase.growthAdmin ` (Firebase Growth-Administrator) ist
jetzt allgemein verfügbar.  
  
Firebase  |  Jetzt GA  |

Die Rolle ` roles/firebase.growthViewer ` (Firebase Growth-Betrachter) ist
jetzt allgemein verfügbar.  
  
Firebase  |  Jetzt GA  |

Die Rolle ` roles/firebase.qualityAdmin ` (Firebase Quality-Administrator) ist
jetzt allgemein verfügbar.  
  
Firebase  |  Jetzt GA  |

Die Rolle ` roles/firebase.qualityViewer ` (Firebase Quality-Betrachter) ist
jetzt allgemein verfügbar.  
  
Firebase  |  Jetzt GA  |

Die Rolle ` roles/firebase.viewer ` (Firebase-Betrachter) ist jetzt allgemein
verfügbar.  
  
Firebase Authentication  |  Jetzt GA  |

Die Rolle ` roles/firebaseauth.admin ` (Firebase Authentication-Administrator)
ist jetzt allgemein verfügbar.  
  
Firebase Authentication  |  Jetzt GA  |

Die Rolle ` roles/firebaseauth.viewer ` (Firebase Authentication-Betrachter)
ist jetzt allgemein verfügbar.  
  
Firebase Crashlytics  |  Jetzt GA  |

Die Rolle ` roles/firebasecrashlytics.admin ` (Firebase Crashlytics-
Administrator) ist jetzt allgemein verfügbar.  
  
Firebase Crashlytics  |  Jetzt GA  |

Die Rolle ` roles/firebasecrashlytics.viewer ` (Firebase Crashlytics-
Betrachter) ist jetzt allgemein verfügbar.  
  
Firebase Realtime Database  |  Jetzt GA  |

Die Rolle ` roles/firebasedatabase.admin ` (Firebase Realtime Database-
Administrator) ist jetzt allgemein verfügbar.  
  
Firebase Realtime Database  |  Jetzt GA  |

Die Rolle ` roles/firebasedatabase.viewer ` (Firebase Realtime Database-
Betrachter) ist jetzt allgemein verfügbar.  
  
Firebase Dynamic Links  |  Jetzt GA  |

Die Rolle ` roles/firebasedynamiclinks.admin ` (Firebase Dynamic Links-
Administrator) ist jetzt allgemein verfügbar.  
  
Firebase Dynamic Links  |  Jetzt GA  |

Die Rolle ` roles/firebasedynamiclinks.viewer ` (Firebase Dynamic Links-
Betrachter) ist jetzt allgemein verfügbar.  
  
Firebase Hosting  |  Jetzt GA  |

Die Rolle ` roles/firebasehosting.admin ` (Firebase Hosting-Administrator) ist
jetzt allgemein verfügbar.  
  
Firebase Hosting  |  Jetzt GA  |

Die Rolle ` roles/firebasehosting.viewer ` (Firebase Hosting-Betrachter) ist
jetzt allgemein verfügbar.  
  
Firebase Cloud Messaging  |  Jetzt GA  |

Die Rolle ` roles/firebasenotifications.admin ` (Firebase Cloud Messaging-
Administrator) ist jetzt allgemein verfügbar.  
  
Firebase Cloud Messaging  |  Jetzt GA  |

Die Rolle ` roles/firebasenotifications.viewer ` (Firebase Cloud Messaging-
Betrachter) ist jetzt allgemein verfügbar.  
  
Firebase Performance Monitoring  |  Jetzt GA  |

Die Rolle ` roles/firebaseperformance.admin ` (Firebase Performance Reporting-
Administrator) ist jetzt allgemein verfügbar.  
  
Firebase Performance Monitoring  |  Jetzt GA  |

Die Rolle ` roles/firebaseperformance.viewer ` (Firebase Performance
Reporting-Betrachter) ist jetzt allgemein verfügbar.  
  
Firebase Predictions  |  Jetzt GA  |

Die Rolle ` roles/firebasepredictions.admin ` (Firebase Predictions-
Administrator) ist jetzt allgemein verfügbar.  
  
Firebase Predictions  |  Jetzt GA  |

Die Rolle ` roles/firebasepredictions.viewer ` (Firebase Predictions-
Betrachter) ist jetzt allgemein verfügbar.  
  
Firebase Remote Config  |  Jetzt GA  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Cloud DNS  |  Jetzt GA  |  ` dns.networks.bindPrivateDNSPolicy `  
` dns.policies.create `  
` dns.policies.delete `  
` dns.policies.get `  
` dns.policies.getIamPolicy `  
` dns.policies.list `  
` dns.policies.setIamPolicy `  
` dns.policies.update `  
  
Firebase  |  Jetzt GA  |  ` firebase.billingPlans.get `  
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
  
Firebase Authentication  |  Jetzt GA  |  ` firebaseauth.configs.create `  
` firebaseauth.configs.get `  
` firebaseauth.configs.getHashConfig `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Crashlytics  |  Jetzt GA  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase Realtime Database  |  Jetzt GA  |  `
firebasedatabase.instances.create `  
` firebasedatabase.instances.get `  
` firebasedatabase.instances.list `  
` firebasedatabase.instances.update `  
  
Firebase Dynamic Links  |  Jetzt GA  |  `
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
  
Firebase Hosting  |  Jetzt GA  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase Cloud Messaging  |  Jetzt GA  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Performance Monitoring  |  Jetzt GA  |  `
firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Predictions  |  Jetzt GA  |  ` firebasepredictions.predictions.create
`  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
NetApp Cloud Volumes-Dienst  |  Hinzugefügt:  |  `
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
  
Event Threat Detection  |  In benutzerdefinierten Rollen unterstützt  |  `
threatdetection.detectorSettings.clear `  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 06.09.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/owner ` (Inhaber) wurden folgende Berechtigungen
hinzugefügt:

` dataprocessing.iamaccesshistory.exportData `  
  
Serverless VPC Access  |  Jetzt GA  |

Die Rolle ` roles/vpaccess.user ` (Nutzer von serverlosem VPC-Zugriff) ist
jetzt allgemein verfügbar.  
  
Serverless VPC Access  |  Jetzt GA  |

Die Rolle ` roles/vpaccess.viewer ` (Betrachter von serverlosem VPC-Zugriff)
ist jetzt allgemein verfügbar.  
  
Serverless VPC Access  |  Jetzt GA  |

Die Rolle ` roles/vpcaccess.admin ` (Administrator von serverlosem VPC-
Zugriff) ist jetzt allgemein verfügbar.  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  Jetzt GA  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Serverless VPC Access  |  Jetzt GA  |  ` vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 30.08.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Firebase Test Lab  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudtestservice.testAdmin ` (Firebase Test Lab-
Administrator) wurden folgende Berechtigungen hinzugefügt:

` firebase.clients.get `  
` firebase.projects.get `  
  
Firebase Test Lab  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudtestservice.testViewer ` (Firebase Test Lab-Betrachter)
wurden folgende Berechtigungen hinzugefügt:

` firebase.clients.get `  
` firebase.projects.get `  
  
Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/compute.orgSecurityPolicyAdmin ` (Administrator von Compute
Engine-Sicherheitsrichtlinien für die Organisation) wurden folgende
Berechtigungen hinzugefügt:

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/compute.orgSecurityPolicyUser ` (Nutzer von Compute Engine-
Sicherheitsrichtlinien für die Organisation) wurden folgende Berechtigungen
hinzugefügt:

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/compute.orgSecurityResourceAdmin ` (Administrator für
Compute Engine-Organisationsressourcen) wurden folgende Berechtigungen
hinzugefügt:

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 23.08.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Übersetzung  |  Jetzt GA  |

Die Rolle ` roles/cloudtranslate.admin ` (Cloud Translation API-Administrator)
ist jetzt allgemein verfügbar.  
  
Übersetzung  |  Jetzt GA  |

Die Rolle ` roles/cloudtranslate.editor ` (Cloud Translation API-Bearbeiter)
ist jetzt allgemein verfügbar.  
  
Übersetzung  |  Jetzt GA  |

Die Rolle ` roles/cloudtranslate.user ` (Cloud Translation API-Nutzer) ist
jetzt allgemein verfügbar.  
  
Übersetzung  |  Jetzt GA  |

Die Rolle ` roles/cloudtranslate.viewer ` (Cloud Translation API-Betrachter)
ist jetzt allgemein verfügbar.  
  
Cloud Healthcare API  |  Rolle aktualisiert  |

Zur Rolle ` roles/healthcare.dicomEditor ` (Healthcare DICOM-Bearbeiter)
wurden folgende Berechtigungen hinzugefügt:

` healthcare.dicomStores.dicomWebDelete `  
  
Übersetzung  |  Jetzt GA  |  ` cloudtranslate.generalModels.batchPredict `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 16.08.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Übersetzung  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudtranslate.locations.get `  
` cloudtranslate.locations.list `  
  
Compute Engine  |  Jetzt GA  |  ` compute.networks.updatePeering `  
  
Data Catalog  |  Hinzugefügt:  |  ` datacatalog.entries.create `  
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
  
Data Catalog  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 09.08.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/compute.orgSecurityPolicyAdmin ` (Administrator von Compute
Engine-Sicherheitsrichtlinien für die Organisation) wurden folgende
Berechtigungen hinzugefügt:

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/compute.orgSecurityPolicyUser ` (Nutzer von Compute Engine-
Sicherheitsrichtlinien für die Organisation) wurden folgende Berechtigungen
hinzugefügt:

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/compute.orgSecurityResourceAdmin ` (Administrator für
Compute Engine-Organisationsressourcen) wurden folgende Berechtigungen
hinzugefügt:

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
cl  |  Jetzt GA  |

Die Rolle ` roles/storage.hmacKeyAdmin ` (Storage HMAC-Schlüssel-
Administrator) ist jetzt allgemein verfügbar.  
  
cl  |  Hinzugefügt:  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
cl  |  In benutzerdefinierten Rollen unterstützt  |  ` storage.hmacKeys.create
`  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
cl  |  Jetzt GA  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 28.06.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/viewer ` (Betrachter) wurden folgende Berechtigungen
hinzugefügt:

` pubsub.snapshots.seek `  
  
Firebase Crashlytics  |  Hinzugefügt:  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase Crashlytics  |  In benutzerdefinierten Rollen unterstützt  |  `
firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Memorystore for Redis  |  Hinzugefügt:  |  ` redis.instances.export `  
` redis.instances.import `  
  
Memorystore for Redis  |  In benutzerdefinierten Rollen unterstützt  |  `
redis.instances.export `  
` redis.instances.import `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 21.06.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Migrate for Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudmigration.inframanager ` (Velostrata Manager) wurden
folgende Berechtigungen hinzugefügt:

` compute.instances.updateShieldedInstanceConfig `  
  
Übersetzung  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudtranslate.viewer ` (Cloud Translation API-Betrachter)
wurden folgende Berechtigungen hinzugefügt:

` cloudtranslate.operations.wait `  
  
Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/compute.networkUser ` (Compute-Netzwerknutzer) wurden
folgende Berechtigungen hinzugefügt:

` compute.vpnGateways.use `  
  
Firebase  |  Rolle aktualisiert  |

Zur Rolle ` roles/firebase.admin ` (Firebase-Administrator) wurden folgende
Berechtigungen hinzugefügt:

` cloudmessaging.messages.create `  
  
Firebase  |  Rolle aktualisiert  |

Zur Rolle ` roles/firebase.growthAdmin ` (Firebase Growth-Administrator)
wurden folgende Berechtigungen hinzugefügt:

` cloudmessaging.messages.create `  
  
Resource Manager  |  Rolle aktualisiert  |

Zur Rolle ` roles/resourcemanager.projectMover ` (Projektverschieber) wurden
folgende Berechtigungen hinzugefügt:

` resourcemanager.projects.move `  
  
Security Command Center  |  Rolle aktualisiert  |

Zur Rolle ` roles/securitycenter.adminEditor ` (Sicherheitscenter-
Administratorbearbeiter) wurden folgende Berechtigungen hinzugefügt:

` securitycenter.assets.group `  
` securitycenter.assets.list `  
` securitycenter.assets.listAssetPropertyNames `  
  
BigQuery  |  Hinzugefügt:  |  ` bigquery.connections.create `  
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
  
BigQuery  |  In benutzerdefinierten Rollen unterstützt  |  `
bigquery.routines.create `  
` bigquery.routines.delete `  
` bigquery.routines.get `  
` bigquery.routines.list `  
` bigquery.routines.update `  
  
Übersetzung  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Cloud Composer  |  Hinzugefügt:  |  ` composer.imageversions.list `  
  
Cloud Composer  |  In benutzerdefinierten Rollen unterstützt  |  `
composer.imageversions.list `  
  
Cloud Composer  |  Jetzt GA  |  ` composer.imageversions.list `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  Jetzt GA  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 14.06.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Identity and Access Management  |  Jetzt GA  |

Die Rolle ` roles/iam.workloadIdentityUser ` (Arbeitslastidentität-Nutzer) ist
jetzt allgemein verfügbar.  
  
Cloud Functions  |  Hinzugefügt:  |  ` cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Cloud Functions  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Compute Engine  |  Jetzt GA  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 31.05.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Data Catalog  |  Rolle aktualisiert  |

Zur Rolle ` roles/datacatalog.admin ` (Data Catalog-Administrator) wurden
folgende Berechtigungen hinzugefügt:

` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
` pubsub.topics.updateTag `  
  
Migrate for Compute Engine  |  Hinzugefügt:  |  `
cloudmigration.velostrataendpoints.connect `  
  
Cloud Identity and Access Management  |  In benutzerdefinierten Rollen
verfügbar  |  ` iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 24.05.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/viewer ` (Betrachter) wurden folgende Berechtigungen
hinzugefügt:

` managedidentities.domains.validateTrust `  
  
Empfehlungs-KI  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
BigQuery  |  Hinzugefügt:  |  ` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
BigQuery  |  In benutzerdefinierten Rollen unterstützt  |  `
bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
Data Catalog  |  Hinzugefügt:  |  ` datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
Data Catalog  |  In benutzerdefinierten Rollen unterstützt  |  `
datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
Filestore  |  Hinzugefügt:  |  ` file.snapshots.update `  
  
Filestore  |  In benutzerdefinierten Rollen unterstützt  |  `
file.snapshots.update `  
  
Pub/Sub  |  Hinzugefügt:  |  ` pubsub.topics.updateTag `  
  
Pub/Sub  |  In benutzerdefinierten Rollen unterstützt  |  `
pubsub.topics.updateTag `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 17.05.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Dialogflow  |  Hinzugefügt:  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  In benutzerdefinierten Rollen unterstützt  |  `
dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  Jetzt GA  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 10.05.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Identity and Access Management  |  Jetzt GA  |

Die Rolle ` roles/iam.securityAdmin ` (Sicherheitsadministrator) ist jetzt
allgemein verfügbar.  
  
Cloud IoT  |  Hinzugefügt:  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  Jetzt GA  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.healthChecks.create `  
` compute.healthChecks.delete `  
` compute.healthChecks.get `  
` compute.healthChecks.list `  
` compute.healthChecks.update `  
` compute.healthChecks.use `  
` compute.healthChecks.useReadOnly `  
` compute.instanceGroups.use `  
  
Cloud Healthcare API  |  Hinzugefügt:  |  ` healthcare.fhirResources.purge `  
  
Managed Service for Microsoft Active Directory  |  Hinzugefügt:  |  `
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
  
Managed Service for Microsoft Active Directory  |  In benutzerdefinierten
Rollen unterstützt  |  ` managedidentities.domains.attachTrust `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 03.05.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.admin ` (Sicherheitscenter-Administrator) ist
jetzt allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.adminEditor ` (Sicherheitscenter-
Administratorbearbeiter) ist jetzt allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.adminViewer ` (Sicherheitscenter-Admin-
Betrachter) ist jetzt allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.assetsDiscoveryRunner ` (Sicherheitscenter-
Asset-Erkennungs-Initiator) ist jetzt allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.assetSecurityMarksWriter `
(Sicherheitscenter-Autor für Asset-Sicherheitsmarkierungen) ist jetzt
allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.assetsViewer ` (Betrachter von
Sicherheitscenter-Assets) ist jetzt allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.findingSecurityMarksWriter `
(Sicherheitscenter-Autor für Ergebnis-Sicherheitsmarkierungen) ist jetzt
allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.findingsEditor ` (Sicherheitscenter-
Ergebnisbearbeiter) ist jetzt allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.findingsStateSetter ` (Sicherheitscenter-
Ergebniszustand-Festleger) ist jetzt allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.findingsViewer ` (Sicherheitscenter-
Ergebnisbetrachter) ist jetzt allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.sourcesAdmin ` (Sicherheitscenter-
Quellenadministrator) ist jetzt allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.sourcesEditor ` (Sicherheitscenter-
Quellenbearbeiter) ist jetzt allgemein verfügbar.  
  
Security Command Center  |  Jetzt GA  |

Die Rolle ` roles/securitycenter.sourcesViewer ` (Sicherheitscenter-
Quellenbetrachter) ist jetzt allgemein verfügbar.  
  
Empfehlungs-KI  |  Hinzugefügt:  |  ` automlrecommendations.apiKeys.create `  
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
  
BigQuery  |  Hinzugefügt:  |  ` bigquery.models.create `  
` bigquery.models.delete `  
` bigquery.models.getData `  
` bigquery.models.getMetadata `  
` bigquery.models.list `  
` bigquery.models.updateData `  
` bigquery.models.updateMetadata `  
  
Firebase Cloud Messaging  |  Hinzugefügt:  |  ` cloudmessaging.messages.create
`  
  
Firebase Cloud Messaging  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudmessaging.messages.create `  
  
Firebase Cloud Messaging  |  Jetzt GA  |  ` cloudmessaging.messages.create `  
  
Security Command Center  |  Jetzt GA  |  ` securitycenter.assets.group `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 19.04.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Einfache Rolle  |  Rolle aktualisiert  |

Aus der Rolle ` roles/editor ` (Bearbeiter) wurden folgende Berechtigungen
entfernt:

` firebasedynamiclinks.domains.delete `  
  
Security Command Center  |  Rolle aktualisiert  |

Zur Rolle ` roles/securitycenter.admin ` (Sicherheitscenter-Administrator)
wurden folgende Berechtigungen hinzugefügt:

` securitycenter.findings.setState `  
  
Security Command Center  |  Rolle aktualisiert  |

Zur Rolle ` roles/securitycenter.adminEditor ` (Sicherheitscenter-
Administratorbearbeiter) wurden folgende Berechtigungen hinzugefügt:

` securitycenter.findings.setState `  
  
Security Command Center  |  Rolle aktualisiert  |

Zur Rolle ` roles/securitycenter.findingsEditor ` (Sicherheitscenter-
Ergebnisbearbeiter) wurden folgende Berechtigungen hinzugefügt:

` securitycenter.findings.setState `  
  
Zugriffsgenehmigung  |  Hinzugefügt:  |  ` accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
Zugriffsgenehmigung  |  In benutzerdefinierten Rollen unterstützt  |  `
accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
Cloud Bigtable  |  Hinzugefügt:  |  ` bigtable.locations.list `  
  
Cloud Bigtable  |  In benutzerdefinierten Rollen unterstützt  |  `
bigtable.locations.list `  
  
Cloud Bigtable  |  Jetzt GA  |  ` bigtable.locations.list `  
  
Cloud Scheduler  |  Hinzugefügt:  |  ` cloudscheduler.locations.get `  
` cloudscheduler.locations.list `  
  
Compute Engine  |  Hinzugefügt:  |  `
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
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Compute Engine  |  Jetzt GA  |  `
compute.networkEndpointGroups.attachNetworkEndpoints `  
` compute.networkEndpointGroups.create `  
` compute.networkEndpointGroups.delete `  
` compute.networkEndpointGroups.detachNetworkEndpoints `  
` compute.networkEndpointGroups.get `  
` compute.networkEndpointGroups.getIamPolicy `  
` compute.networkEndpointGroups.list `  
` compute.networkEndpointGroups.setIamPolicy `  
` compute.networkEndpointGroups.use `  
  
Remote Build Execution  |  Hinzugefügt:  |  `
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
  
Remote Build Execution  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Serverless VPC Access  |  Hinzugefügt:  |  ` vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 29.03.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/compute.networkUser ` (Compute-Netzwerknutzer) wurden
folgende Berechtigungen hinzugefügt:

` servicenetworking.services.get `  
  
Cloud Monitoring  |  Rolle aktualisiert  |

Zur Rolle ` roles/monitoring.admin ` (Monitoring-Administrator) wurden
folgende Berechtigungen hinzugefügt:

` serviceusage.services.enable `  
  
Cloud Monitoring  |  Rolle aktualisiert  |

Zur Rolle ` roles/monitoring.editor ` (Monitoring-Bearbeiter) wurden folgende
Berechtigungen hinzugefügt:

` serviceusage.services.enable `  
  
Google Cloud Operations Suite  |  Rolle aktualisiert  |

Zur Rolle ` roles/stackdriver.accounts.editor ` (Bearbeiter von Stackdriver-
Konten) wurden folgende Berechtigungen hinzugefügt:

` serviceusage.services.enable `  
  
Cloud SQL  |  Hinzugefügt:  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  Jetzt GA  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Übersetzung  |  Hinzugefügt:  |  ` cloudtranslate.generalModels.batchPredict `  
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
  
Cloud DNS  |  Hinzugefügt:  |  ` dns.networks.targetWithPeeringZone `  
  
Cloud DNS  |  In benutzerdefinierten Rollen unterstützt  |  `
dns.networks.targetWithPeeringZone `  
  
Event Threat Detection  |  Hinzugefügt:  |  `
threatdetection.detectorSettings.clear `  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 22.03.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Talent Solution  |  Jetzt GA  |

Die Rolle ` roles/cloudjobdiscovery.admin ` (Administrator) ist jetzt
allgemein verfügbar.  
  
Talent Solution  |  Jetzt GA  |

Die Rolle ` roles/cloudjobdiscovery.jobsEditor ` (Jobbearbeiter) ist jetzt
allgemein verfügbar.  
  
Talent Solution  |  Jetzt GA  |

Die Rolle ` roles/cloudjobdiscovery.jobsViewer ` (Jobbetrachter) ist jetzt
allgemein verfügbar.  
  
Talent Solution  |  Jetzt GA  |

Die Rolle ` roles/cloudjobdiscovery.profilesEditor ` (Profilbearbeiter) ist
jetzt allgemein verfügbar.  
  
Talent Solution  |  Jetzt GA  |

Die Rolle ` roles/cloudjobdiscovery.profilesViewer ` (Profilbetrachter) ist
jetzt allgemein verfügbar.  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/editor ` (Bearbeiter) wurden folgende Berechtigungen
hinzugefügt:

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Filestore  |  Rolle aktualisiert  |

Zur Rolle ` roles/file.editor ` (Cloud Filestore-Bearbeiter) wurden folgende
Berechtigungen hinzugefügt:

` file.instances.restore `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/owner ` (Inhaber) wurden folgende Berechtigungen
hinzugefügt:

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Talent Solution  |  Jetzt GA  |  ` cloudjobdiscovery.companies.create `  
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
  
Compute Engine  |  Hinzugefügt:  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  Jetzt GA  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Filestore  |  Hinzugefügt:  |  ` file.instances.restore `  
  
Firebase Authentication  |  Hinzugefügt:  |  `
firebaseauth.configs.getHashConfig `  
  
Firebase Authentication  |  In benutzerdefinierten Rollen unterstützt  |  `
firebaseauth.configs.getHashConfig `  
  
Cloud Healthcare API  |  Hinzugefügt  |  ` healthcare.datasets.create `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 15.03.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Talent Solution  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudjobdiscovery.profilesEditor ` (Profilbearbeiter) wurden
folgende Berechtigungen hinzugefügt:

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Talent Solution  |  Rolle aktualisiert  |

Aus der Rolle ` roles/cloudjobdiscovery.profilesEditor ` (Profilbearbeiter)
wurden folgende Berechtigungen entfernt:

` cloudjobdiscovery.companies.create `  
` cloudjobdiscovery.companies.delete `  
` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.companies.update `  
  
Talent Solution  |  Rolle aktualisiert  |

Zur Rolle ` roles/cloudjobdiscovery.profilesViewer ` (Profilbetrachter) wurden
folgende Berechtigungen hinzugefügt:

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  Rolle aktualisiert  |

Aus der Rolle ` roles/cloudjobdiscovery.profilesViewer ` (Profilbetrachter)
wurden folgende Berechtigungen entfernt:

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/editor ` (Bearbeiter) wurden folgende Berechtigungen
hinzugefügt:

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/owner ` (Inhaber) wurden folgende Berechtigungen
hinzugefügt:

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Storage Transfer Service  |  Jetzt GA  |

Die Rolle ` roles/storagetransfer.admin ` (Storage Transfer-Administrator) ist
jetzt allgemein verfügbar.  
  
Storage Transfer Service  |  Jetzt GA  |

Die Rolle ` roles/storagetransfer.user ` (Storage Transfer-Nutzer) ist jetzt
allgemein verfügbar.  
  
Storage Transfer Service  |  Jetzt GA  |

Die Rolle ` roles/storagetransfer.viewer ` (Storage Transfer-Betrachter) ist
jetzt allgemein verfügbar.  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/viewer ` (Betrachter) wurden folgende Berechtigungen
hinzugefügt:

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  Hinzugefügt:  |  ` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Cloud DNS  |  Jetzt GA  |  ` dns.networks.bindPrivateDNSZone `  
  
Cloud Run  |  Hinzugefügt  |  ` run.configurations.get `  
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
  
Cloud Run  |  In benutzerdefinierten Rollen nicht unterstützt  |  `
run.routes.invoke `  
  
Cloud Run  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Storage Transfer Service  |  Hinzugefügt:  |  ` storagetransfer.jobs.create `  
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
  
Storage Transfer Service  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Storage Transfer Service  |  Jetzt GA  |  ` storagetransfer.jobs.create `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 07.03.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
BigQuery  |  Rolle hinzugefügt  |

Die Rolle ` roles/bigquery.connectionAdmin ` (BigQuery-
Verbindungsadministrator) wurde mit den folgenden Berechtigungen hinzugefügt:

` bigquery.connections.create `  
` bigquery.connections.delete `  
` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.setIamPolicy `  
` bigquery.connections.update `  
` bigquery.connections.use `  
  
BigQuery  |  Rolle hinzugefügt  |

Die Rolle ` roles/bigquery.connectionUser ` (BigQuery-Verbindungsnutzer) wurde
mit den folgenden Berechtigungen hinzugefügt:

` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.use `  
  
Dialogflow  |  Rolle aktualisiert  |

Zur Rolle ` roles/dialogflow.admin ` (Dialogflow API-Administrator) wurden
folgende Berechtigungen hinzugefügt:

` dialogflow.agents.update `  
  
Dialogflow  |  Rolle aktualisiert  |

Zur Rolle ` roles/dialogflow.consoleAgentEditor ` (Agent-Bearbeiter in
Dialogflow-Konsole) wurden folgende Berechtigungen hinzugefügt:

` dialogflow.agents.update `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/editor ` (Bearbeiter) wurden folgende Berechtigungen
hinzugefügt:

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  Rolle aktualisiert  |

Zur Rolle ` roles/file.editor ` (Cloud Filestore-Bearbeiter) wurden folgende
Berechtigungen hinzugefügt:

` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  Rolle aktualisiert  |

Zur Rolle ` roles/file.viewer ` (Cloud Filestore-Betrachter) wurden folgende
Berechtigungen hinzugefügt:

` file.snapshots.get `  
` file.snapshots.list `  
  
Cloud Identity and Access Management  |  Jetzt GA  |

Die Rolle ` roles/iam.serviceAccountCreator ` (Dienstkonten erstellen) ist
jetzt allgemein verfügbar.  
  
Cloud Identity and Access Management  |  Rolle aktualisiert  |

Zur Rolle ` roles/iam.securityReviewer ` (Sicherheitsprüfer) wurden folgende
Berechtigungen hinzugefügt:

` file.snapshots.list `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/owner ` (Inhaber) wurden folgende Berechtigungen
hinzugefügt:

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Service Usage  |  Rolle aktualisiert  |

Zur Rolle ` roles/serviceusage.apiKeysAdmin ` (API-Schlüsseladministrator)
wurden folgende Berechtigungen hinzugefügt:

` serviceusage.operations.get `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/viewer ` (Betrachter) wurden folgende Berechtigungen
hinzugefügt:

` file.snapshots.get `  
` file.snapshots.list `  
  
AI Platform Data Labeling Service  |  Hinzugefügt:  |  `
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
  
AI Platform Data Labeling Service  |  In benutzerdefinierten Rollen
unterstützt  |  ` datalabeling.annotateddatasets.delete `  
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
  
Dialogflow  |  Hinzugefügt:  |  ` dialogflow.agents.update `  
  
Filestore  |  Hinzugefügt:  |  ` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 01.03.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  Rolle aktualisiert  |

Zur Rolle ` roles/compute.instanceAdmin.v1 ` (Compute-Instanzadministrator
(Version 1)) wurden folgende Berechtigungen hinzugefügt:

` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Dataproc  |  Rolle hinzugefügt  |

Die Rolle ` roles/dataproc.admin ` (Dataproc-Administrator) wurde mit den
folgenden Berechtigungen hinzugefügt:

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
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/editor ` (Bearbeiter) wurden folgende Berechtigungen
hinzugefügt:

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
Cloud Identity and Access Management  |  Rolle aktualisiert  |

Zur Rolle ` roles/iam.serviceAccountDeleter ` (Dienstkonten löschen) wurden
folgende Berechtigungen hinzugefügt:

` iam.serviceAccounts.get `  
` iam.serviceAccounts.list `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/viewer ` (Betrachter) wurden folgende Berechtigungen
hinzugefügt:

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
AutoML  |  Hinzugefügt:  |  ` automl.columnSpecs.get `  
` automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.export `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
AutoML  |  In benutzerdefinierten Rollen unterstützt  |  `
automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.deploy `  
` automl.models.export `  
` automl.models.undeploy `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 15.02.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Access Context Manager  |  Jetzt GA  |

Die Rolle ` roles/accesscontextmanager.policyAdmin ` (Access Context Manager-
Administrator) ist jetzt allgemein verfügbar.  
  
Access Context Manager  |  Jetzt GA  |

Die Rolle ` roles/accesscontextmanager.policyEditor ` (Access Context Manager-
Bearbeiter) ist jetzt allgemein verfügbar.  
  
Access Context Manager  |  Jetzt GA  |

Die Rolle ` roles/accesscontextmanager.policyReader ` (Access Context Manager-
Leser) ist jetzt allgemein verfügbar.  
  
Talent Solution  |  Rolle hinzugefügt  |

Die Rolle ` roles/cloudjobdiscovery.profilesEditor ` (Profilbearbeiter) wurde
mit den folgenden Berechtigungen hinzugefügt:

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
  
Talent Solution  |  Rolle hinzugefügt  |

Die Rolle ` roles/cloudjobdiscovery.profilesViewer ` (Profilbetrachter) wurde
mit den folgenden Berechtigungen hinzugefügt:

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/editor ` (Bearbeiter) wurden folgende Berechtigungen
hinzugefügt:

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/owner ` (Inhaber) wurden folgende Berechtigungen
hinzugefügt:

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
Einfache Rolle  |  Rolle aktualisiert  |

Zur Rolle ` roles/viewer ` (Betrachter) wurden folgende Berechtigungen
hinzugefügt:

` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
  
Google Cloud Operations Suite  |  Rolle aktualisiert  |

Zur Rolle ` roles/stackdriver.accounts.editor ` (Bearbeiter von Stackdriver-
Konten) wurden folgende Berechtigungen hinzugefügt:

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Google Cloud Operations Suite  |  Rolle aktualisiert  |

Zur Rolle ` roles/stackdriver.accounts.viewer ` (Betrachter von Stackdriver-
Konten) wurden folgende Berechtigungen hinzugefügt:

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Access Context Manager  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Access Context Manager  |  Jetzt GA  |  `
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
  
Talent Solution  |  Hinzugefügt:  |  ` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 08.02.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Security Command Center  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 01.02.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Dialogflow  |  Jetzt GA  |

Die Rolle ` roles/dialogflow.admin ` (Dialogflow API-Administrator) ist jetzt
allgemein verfügbar.  
  
Dialogflow  |  Jetzt GA  |

Die Rolle ` roles/dialogflow.client ` (Dialogflow API-Client) ist jetzt
allgemein verfügbar.  
  
Dialogflow  |  Jetzt GA  |

Die Rolle ` roles/dialogflow.consoleAgentEditor ` (Agent-Bearbeiter in
Dialogflow-Konsole) ist jetzt allgemein verfügbar.  
  
Dialogflow  |  Jetzt GA  |

Die Rolle ` roles/dialogflow.reader ` (Dialogflow API-Leser) ist jetzt
allgemein verfügbar.  
  
Cloud Asset Inventory  |  Hinzugefügt  |  ` cloudasset.assets.exportIamPolicy
`  
` cloudasset.assets.exportResource `  
  
Cloud Asset Inventory  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Cloud Asset Inventory  |  Jetzt allgemein verfügbar  |  `
cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Dialogflow  |  In benutzerdefinierten Rollen unterstützt  |  `
dialogflow.agents.search `  
` dialogflow.agents.train `  
  
Dialogflow  |  Jetzt allgemein verfügbar  |  ` dialogflow.agents.export `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 25.01.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  Hinzugefügt:  |  ` compute.instances.updateDisplayDevice `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 11.01.2019

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Identity-Aware Proxy  |  Jetzt GA  |

Die Rolle ` roles/iap.admin ` (IAP-Richtlinienadministrator) ist jetzt
allgemein verfügbar.  
  
Identity-Aware Proxy  |  In benutzerdefinierten Rollen unterstützt  |  `
iap.web.getIamPolicy `  
` iap.web.setIamPolicy `  
` iap.webServiceVersions.accessViaIAP `  
` iap.webServiceVersions.getIamPolicy `  
` iap.webServiceVersions.setIamPolicy `  
` iap.webServices.getIamPolicy `  
` iap.webServices.setIamPolicy `  
` iap.webTypes.getIamPolicy `  
` iap.webTypes.setIamPolicy `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 21.12.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud DNS  |  Hinzugefügt:  |  ` dns.networks.bindPrivateDNSZone `  
  
Cloud DNS  |  In benutzerdefinierten Rollen unterstützt  |  `
dns.networks.bindPrivateDNSZone `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 14.12.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Firebase Authentication  |  Hinzugefügt:  |  ` firebaseauth.configs.create `  
  
Firebase Authentication  |  In benutzerdefinierten Rollen unterstützt  |  `
firebaseauth.configs.create `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 07.12.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
BigQuery  |  Hinzugefügt:  |  ` bigquery.readsessions.create `  
  
BigQuery  |  In benutzerdefinierten Rollen unterstützt  |  `
bigquery.readsessions.create `  
  
Google Kubernetes Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
Google Kubernetes Engine  |  Jetzt allgemein verfügbar  |  `
container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 30.11.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Asset Inventory  |  Jetzt GA  |

Die Rolle ` roles/cloudasset.viewer ` (Betrachter von Cloudassets) ist jetzt
allgemein verfügbar.  
  
Cloud Asset Inventory  |  Jetzt GA  |  ` cloudasset.assets.exportAll `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Compute Engine  |  Jetzt GA  |  ` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
` compute.subnetworks.getIamPolicy `  
` compute.subnetworks.setIamPolicy `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 16.11.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
AutoML  |  Hinzugefügt:  |  ` automl.locations.getIamPolicy `  
` automl.locations.setIamPolicy `  
  
AutoML  |  In benutzerdefinierten Rollen unterstützt  |  `
automl.locations.getIamPolicy `  
` automl.locations.setIamPolicy `  
  
Talent Solution  |  Hinzugefügt:  |  ` cloudjobdiscovery.events.create `  
` cloudjobdiscovery.events.delete `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.events.update `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  Jetzt GA  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Google Kubernetes Engine  |  Hinzugefügt  |  ` container.backendConfigs.create
`  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 09.11.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Google Analytics  |  Hinzugefügt:  |  `
firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
Google Analytics  |  In benutzerdefinierten Rollen unterstützt  |  `
firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 02.11.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  Jetzt GA  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  In benutzerdefinierten Rollen unterstützt  |  `
file.instances.create `  
` file.instances.delete `  
` file.instances.get `  
` file.instances.list `  
` file.instances.update `  
` file.locations.get `  
` file.locations.list `  
` file.operations.get `  
` file.operations.list `  
  
Google Cloud Operations Suite  |  Hinzugefügt:  |  `
stackdriver.resourceMetadata.write `  
  
Google Cloud Operations Suite  |  In benutzerdefinierten Rollen unterstützt  |
` stackdriver.resourceMetadata.write `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 26.10.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
BigQuery  |  Jetzt GA  |

Die Rolle ` roles/bigquery.metadataViewer ` (BigQuery-Metadaten-Betrachter)
ist jetzt allgemein verfügbar.  
  
Cloud Identity and Access Management  |  Jetzt GA  |

Die Rolle ` roles/iam.serviceAccountDeleter ` (Dienstkonten löschen) ist jetzt
allgemein verfügbar.  
  
Firebase Realtime Database  |  Hinzugefügt:  |  `
firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
Firebase Realtime Database  |  In benutzerdefinierten Rollen unterstützt  |  `
firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
Firebase-Integrationen mit externen Diensten  |  Hinzugefügt:  |  `
firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
Firebase-Integrationen mit externen Diensten  |  In benutzerdefinierten Rollen
unterstützt  |  ` firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 19.10.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Google Cloud-Support  |  Jetzt GA  |

Die Rolle ` roles/cloudsupport.admin ` (Supportkontoadministrator) ist jetzt
allgemein verfügbar.  
  
Google Cloud-Support  |  Jetzt GA  |

Die Rolle ` roles/cloudsupport.viewer ` (Supportkontobetrachter) ist jetzt
allgemein verfügbar.  
  
Firebase Remote Config  |  Hinzugefügt  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Firebase Remote Config  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Google Cloud-Support  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Google Cloud-Support  |  Jetzt GA  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.networks.updatePeering `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.networks.updatePeering `  
  
Firebase Crashlytics  |  Hinzugefügt:  |  ` firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase Crashlytics  |  In benutzerdefinierten Rollen unterstützt  |  `
firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase Dynamic Links  |  Hinzugefügt:  |  `
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
  
Firebase Dynamic Links  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Firebase In-App Messaging  |  Hinzugefügt:  |  `
firebaseinappmessaging.campaigns.create `  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Firebase In-App Messaging  |  In benutzerdefinierten Rollen unterstützt  |  `
firebaseinappmessaging.campaigns.create `  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Firebase Cloud Messaging  |  Hinzugefügt:  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Cloud Messaging  |  In benutzerdefinierten Rollen unterstützt  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Performance Monitoring  |  Hinzugefügt:  |  `
firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Performance Monitoring  |  In benutzerdefinierten Rollen unterstützt
|  ` firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Predictions  |  Hinzugefügt:  |  `
firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
Firebase Predictions  |  In benutzerdefinierten Rollen unterstützt  |  `
firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
Security Command Center  |  Hinzugefügt:  |  ` securitycenter.assets.get `  
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
  
Dienstnutzerverwaltung  |  Hinzugefügt  |  `
serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
Dienstnutzerverwaltung  |  In benutzerdefinierten Rollen unterstützt  |  `
serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 12.10.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.admin ` (DLP-Administrator) ist jetzt allgemein
verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.analyzeRiskTemplatesEditor ` (Bearbeiter von DLP-
Risikoanalysevorlagen) ist jetzt allgemein verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.analyzeRiskTemplatesReader ` (Leser von DLP-
Risikoanalysevorlagen) ist jetzt allgemein verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.deidentifyTemplatesEditor ` (Bearbeiter von DLP-De-
identify-Vorlagen) ist jetzt allgemein verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.deidentifyTemplatesReader ` (Leser von DLP-De-identify-
Vorlagen) ist jetzt allgemein verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.inspectTemplatesEditor ` (Bearbeiter von DLP-
Prüfungsvorlagen) ist jetzt allgemein verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.inspectTemplatesReader ` (Leser von DLP-
Prüfungsvorlagen) ist jetzt allgemein verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.jobsEditor ` (DLP-Jobs-Bearbeiter) ist jetzt allgemein
verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.jobsReader ` (DLP-Jobs-Leser) ist jetzt allgemein
verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.jobTriggersEditor ` (DLP-Job-Trigger-Bearbeiter) ist
jetzt allgemein verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.jobTriggersReader ` (DLP-Job-Trigger-Leser) ist jetzt
allgemein verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.reader ` (DLP-Leser) ist jetzt allgemein verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.storedInfoTypesEditor ` (Bearbeiter von für DLP
gespeicherten InfoTypes) ist jetzt allgemein verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.storedInfoTypesReader ` (Leser von für DLP gespeicherten
InfoTypes) ist jetzt allgemein verfügbar.  
  
Cloud Data Loss Prevention  |  Jetzt GA  |

Die Rolle ` roles/dlp.user ` (DLP-Nutzer) ist jetzt allgemein verfügbar.  
  
Google Kubernetes Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Cloud Data Loss Prevention  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Cloud Data Loss Prevention  |  Jetzt GA  |  ` dlp.analyzeRiskTemplates.create
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
  
Cloud DNS  |  In benutzerdefinierten Rollen unterstützt  |  ` dns.dnsKeys.get
`  
` dns.dnsKeys.list `  
` dns.managedZoneOperations.get `  
` dns.managedZoneOperations.list `  
` dns.managedZones.update `  
  
Firebase  |  Hinzugefügt:  |  ` firebase.billingPlans.get `  
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
  
Firebase  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Firebase A/B Testing  |  Hinzugefügt:  |  ` firebaseabt.experimentresults.get
`  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Firebase A/B Testing  |  In benutzerdefinierten Rollen unterstützt  |  `
firebaseabt.experimentresults.get `  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Firebase Authentication  |  Hinzugefügt:  |  ` firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Authentication  |  In benutzerdefinierten Rollen unterstützt  |  `
firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Realtime Database  |  Hinzugefügt:  |  `
firebasedatabase.instances.get `  
` firebasedatabase.instances.update `  
  
Firebase Realtime Database  |  In benutzerdefinierten Rollen unterstützt  |  `
firebasedatabase.instances.get `  
` firebasedatabase.instances.update `  
  
Firebase Hosting  |  Hinzugefügt:  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase Hosting  |  In benutzerdefinierten Rollen unterstützt  |  `
firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
ML Kit for Firebase  |  Hinzugefügt:  |  ` firebaseml.compressionjobs.create `  
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
  
ML Kit for Firebase  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Firebase-Sicherheitsregeln  |  Hinzugefügt:  |  `
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
  
Firebase-Sicherheitsregeln  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 05.10.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  Hinzugefügt:  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  Jetzt GA  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Google Kubernetes Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Google Kubernetes Engine  |  Jetzt allgemein verfügbar  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 21.09.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
AutoML  |  Hinzugefügt:  |  ` automl.datasets.getIamPolicy `  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
AutoML  |  In benutzerdefinierten Rollen unterstützt  |  `
automl.datasets.getIamPolicy `  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
Cloud Asset Inventory  |  Hinzugefügt  |  ` cloudasset.assets.exportAll `  
  
Cloud Asset Inventory  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudasset.assets.exportAll `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.licenses.delete `  
  
Google Kubernetes Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 07.09.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Memorystore for Redis  |  In benutzerdefinierten Rollen unterstützt  |  `
redis.operations.cancel `  
` redis.operations.delete `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 31.08.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Google Kubernetes Engine  |  Hinzugefügt:  |  ` container.cronJobs.getStatus `  
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
  
Cloud Data Loss Prevention  |  Hinzugefügt:  |  ` dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud Data Loss Prevention  |  In benutzerdefinierten Rollen unterstützt  |  `
dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud Source Repositories  |  Hinzugefügt  |  ` source.repos.getProjectConfig
`  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud Source Repositories  |  In benutzerdefinierten Rollen unterstützt  |  `
source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud Source Repositories  |  Jetzt allgemein verfügbar  |  `
source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 10.08.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Binärautorisierung  |  Hinzugefügt  |  `
binaryauthorization.attestors.verifyImageAttested `  
  
Binärautorisierung  |  In benutzerdefinierten Rollen unterstützt  |  `
binaryauthorization.attestors.verifyImageAttested `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  Hinzugefügt:  |  ` file.instances.create `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 03.08.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Android Management API  |  In benutzerdefinierten Rollen unterstützt  |  `
androidmanagement.enterprises.manage `  
  
Android Management API  |  Jetzt GA  |  ` androidmanagement.enterprises.manage
`  
  
Cloud Billing  |  In benutzerdefinierten Rollen unterstützt  |  `
billing.resourceCosts.get `  
  
Binärautorisierung  |  Hinzugefügt  |  ` binaryauthorization.policy.get `  
` binaryauthorization.policy.getIamPolicy `  
` binaryauthorization.policy.setIamPolicy `  
` binaryauthorization.policy.update `  
  
Cloud Composer  |  Jetzt GA  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Compute Engine  |  Jetzt GA  |  ` compute.nodeGroups.addNodes `  
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
  
Google Kubernetes Engine  |  Jetzt GA  |  ` container.hostServiceAgent.use `  
  
Memorystore for Redis  |  Hinzugefügt:  |  ` redis.operations.cancel `  
  
Memorystore for Redis  |  In benutzerdefinierten Rollen unterstützt  |  `
redis.instances.create `  
` redis.instances.delete `  
` redis.instances.get `  
` redis.instances.list `  
` redis.instances.update `  
` redis.locations.get `  
` redis.locations.list `  
` redis.operations.get `  
` redis.operations.list `  
  
Abonnieren mit Google  |  Hinzugefügt:  |  `
subscribewithgoogledeveloper.tools.get `  
  
Abonnieren mit Google  |  In benutzerdefinierten Rollen unterstützt  |  `
subscribewithgoogledeveloper.tools.get `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 20.07.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Access Context Manager  |  Hinzugefügt:  |  `
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
  
AutoML  |  Hinzugefügt:  |  ` automl.annotationSpecs.create `  
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
  
AutoML  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Binärautorisierung  |  Hinzugefügt  |  ` binaryauthorization.attestors.create
`  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
Binärautorisierung  |  In benutzerdefinierten Rollen unterstützt  |  `
binaryauthorization.attestors.create `  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
Cloud DNS  |  In benutzerdefinierten Rollen unterstützt  |  `
dns.changes.create `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 13.07.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
BigQuery  |  Hinzugefügt:  |  ` bigquery.datasets.getIamPolicy `  
` bigquery.datasets.setIamPolicy `  
  
Datastore  |  Hinzugefügt:  |  ` datastore.locations.get `  
` datastore.locations.list `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 06.07.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Composer  |  In benutzerdefinierten Rollen unterstützt  |  `
composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Endpoints  |  Hinzugefügt  |  ` endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud Endpoints  |  In benutzerdefinierten Rollen unterstützt  |  `
endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud TPU  |  Hinzugefügt  |  ` tpu.acceleratortypes.get `  
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
  
Cloud TPU  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 29.06.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Identity and Access Management  |  Jetzt allgemein verfügbar  |  `
iam.serviceAccounts.implicitDelegation `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 15.06.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Compute Engine  |  Jetzt GA  |  ` compute.regionBackendServices.create `  
` compute.regionBackendServices.delete `  
` compute.regionBackendServices.get `  
` compute.regionBackendServices.list `  
` compute.regionBackendServices.setSecurityPolicy `  
` compute.regionBackendServices.update `  
` compute.regionBackendServices.use `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 08.06.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  Hinzugefügt:  |  ` compute.nodeGroups.addNodes `  
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
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 11.05.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
BigQuery  |  In benutzerdefinierten Rollen unterstützt  |  `
bigquery.jobs.listAll `  
  
Cloud Bigtable  |  In benutzerdefinierten Rollen unterstützt  |  `
bigtable.appProfiles.create `  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.clusters.create `  
` bigtable.clusters.delete `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Bigtable  |  Jetzt GA  |  ` bigtable.appProfiles.create `  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Composer  |  Jetzt Beta  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Life Sciences  |  In benutzerdefinierten Rollen unterstützt  |  `
genomics.operations.cancel `  
` genomics.operations.create `  
` genomics.operations.get `  
` genomics.operations.list `  
  
Cloud Monitoring  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Cloud Monitoring  |  Jetzt GA  |  ` monitoring.dashboards.create `  
` monitoring.dashboards.delete `  
` monitoring.dashboards.get `  
` monitoring.dashboards.list `  
` monitoring.dashboards.update `  
` monitoring.publicWidgets.create `  
` monitoring.publicWidgets.delete `  
` monitoring.publicWidgets.get `  
` monitoring.publicWidgets.list `  
` monitoring.publicWidgets.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 04.05.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
BigQuery  |  In benutzerdefinierten Rollen verfügbar  |  `
bigquery.jobs.listAll `  
  
Cloud Bigtable  |  Hinzugefügt:  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  In benutzerdefinierten Rollen unterstützt  |  `
bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  Jetzt GA  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  Jetzt GA  |  ` compute.oslogin.updateExternalUser `  
  
Dienstverwaltung  |  In benutzerdefinierten Rollen unterstützt  |  `
servicemanagement.services.bind `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 06.04.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
compute.instances.setShieldedVmIntegrityPolicy `  
` compute.instances.updateShieldedVmConfig `  
  
Compute Engine  |  Jetzt GA  |  `
compute.instances.setShieldedVmIntegrityPolicy `  
  
Google Kubernetes Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
container.hostServiceAgent.use `  
  
Dataproc  |  In benutzerdefinierten Rollen unterstützt  |  `
dataproc.jobs.getIamPolicy `  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
Dataproc  |  Jetzt GA  |  ` dataproc.jobs.getIamPolicy `  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 30.03.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud IoT  |  Jetzt GA  |  ` cloudiot.devices.create `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 23.03.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Life Sciences  |  In benutzerdefinierten Rollen unterstützt  |  `
genomics.datasets.create `  
` genomics.datasets.delete `  
` genomics.datasets.get `  
` genomics.datasets.getIamPolicy `  
` genomics.datasets.list `  
` genomics.datasets.setIamPolicy `  
` genomics.datasets.update `  
  
Pub/Sub  |  In benutzerdefinierten Rollen unterstützt  |  `
pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.list `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 09.03.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Talent Solution  |  Hinzugefügt:  |  ` cloudjobdiscovery.companies.create `  
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
  
Talent Solution  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Cloud Profiler  |  Hinzugefügt:  |  ` cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
Cloud Profiler  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 02.03.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Open Service Broker for Google Cloud  |  Hinzugefügt:  |  `
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
  
Open Service Broker for Google Cloud  |  In benutzerdefinierten Rollen
unterstützt  |  ` servicebroker.bindingoperations.get `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 23.02.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Resource Manager  |  In benutzerdefinierten Rollen unterstützt  |  `
resourcemanager.projects.list `  
` resourcemanager.projects.move `  
  
Dienstverwaltung  |  Hinzugefügt:  |  ` servicemanagement.services.quota `  
  
Dienstverwaltung  |  In benutzerdefinierten Rollen unterstützt  |  `
servicemanagement.services.quota `  
  
Cloud Source Repositories  |  In benutzerdefinierten Rollen unterstützt  |  `
source.repos.create `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 16.02.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
BigQuery  |  In benutzerdefinierten Rollen unterstützt  |  `
bigquery.tables.update `  
` bigquery.tables.updateData `  
  
Cloud IoT  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Cloud SQL  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudsql.instances.demoteMaster `  
  
Google Cloud-Support  |  Hinzugefügt:  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Compute Engine  |  Hinzugefügt:  |  ` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Dataproc  |  In benutzerdefinierten Rollen unterstützt  |  `
dataproc.agents.create `  
` dataproc.agents.delete `  
` dataproc.agents.get `  
` dataproc.agents.list `  
` dataproc.agents.update `  
` dataproc.tasks.lease `  
` dataproc.tasks.listInvalidatedLeases `  
` dataproc.tasks.reportStatus `  
` dataproc.workflowTemplates.instantiateInline `  
  
Cloud DNS  |  Hinzugefügt:  |  ` dns.changes.create `  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 02.02.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  In benutzerdefinierten Rollen verfügbar  |  `
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
  
Cloud Data Loss Prevention  |  Hinzugefügt:  |  ` dlp.jobTriggers.create `  
` dlp.jobTriggers.delete `  
` dlp.jobTriggers.get `  
` dlp.jobTriggers.list `  
` dlp.jobTriggers.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 26.01.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
BigQuery  |  Hinzugefügt:  |  ` bigquery.jobs.listAll `  
  
Google Kubernetes Engine  |  Hinzugefügt  |  `
container.podSecurityPolicies.create `  
` container.podSecurityPolicies.delete `  
` container.podSecurityPolicies.get `  
` container.podSecurityPolicies.list `  
` container.podSecurityPolicies.update `  
` container.podSecurityPolicies.use `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 19.01.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  Hinzugefügt:  |  ` compute.addresses.createInternal `  
` compute.addresses.deleteInternal `  
` compute.addresses.useInternal `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 12.01.2018

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
App Engine  |  In benutzerdefinierten Rollen nicht unterstützt  |  `
appengine.runtimes.actAsAdmin `  
  
Compute Engine  |  Hinzugefügt:  |  `
compute.backendServices.setSecurityPolicy `  
` compute.securityPolicies.create `  
` compute.securityPolicies.delete `  
` compute.securityPolicies.get `  
` compute.securityPolicies.getIamPolicy `  
` compute.securityPolicies.list `  
` compute.securityPolicies.setIamPolicy `  
` compute.securityPolicies.update `  
` compute.securityPolicies.use `  
  
Compute Engine  |  In benutzerdefinierten Rollen nicht unterstützt  |  `
compute.organizations.administerXpn `  
` compute.targetHttpProxies.create `  
` compute.targetHttpProxies.setUrlMap `  
` compute.targetHttpsProxies.create `  
` compute.targetHttpsProxies.setUrlMap `  
` compute.targetSslProxies.create `  
` compute.targetSslProxies.setBackendService `  
` compute.targetTcpProxies.create `  
` compute.targetTcpProxies.update `  
  
Compute Engine  |  Jetzt GA  |  ` compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 22.12.2017

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
App Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
App Engine  |  In benutzerdefinierten Rollen nicht unterstützt  |  `
appengine.applications.list `  
` appengine.operations.cancel `  
` appengine.operations.delete `  
` appengine.services.create `  
  
Cloud Billing  |  In benutzerdefinierten Rollen unterstützt  |  `
billing.accounts.close `  
` billing.accounts.reopen `  
` billing.budgets.delete `  
` billing.budgets.update `  
  
Cloud Debugger  |  In benutzerdefinierten Rollen unterstützt  |  `
clouddebugger.breakpoints.create `  
` clouddebugger.breakpoints.delete `  
` clouddebugger.breakpoints.get `  
` clouddebugger.breakpoints.list `  
` clouddebugger.breakpoints.listActive `  
` clouddebugger.breakpoints.update `  
` clouddebugger.debuggees.create `  
` clouddebugger.debuggees.list `  
  
Cloud Key Management Service  |  In benutzerdefinierten Rollen unterstützt  |
` cloudkms.cryptoKeyVersions.create `  
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
  
Cloud SQL  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Cloud SQL  |  In benutzerdefinierten Rollen nicht unterstützt  |  `
cloudsql.databases.getIamPolicy `  
` cloudsql.databases.setIamPolicy `  
` cloudsql.instances.demoteMaster `  
` cloudsql.instances.getIamPolicy `  
` cloudsql.instances.migrate `  
` cloudsql.instances.setIamPolicy `  
` cloudsql.sslCerts.createEphemeral `  
  
Cloud Trace  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Compute Engine  |  Hinzugefügt:  |  ` compute.instances.setMachineResources `  
` compute.instances.setMinCpuPlatform `  
` compute.instances.setServiceAccount `  
` compute.instances.updateAccessConfig `  
` compute.instances.updateNetworkInterface `  
` compute.licenseCodes.get `  
` compute.licenseCodes.list `  
` compute.licenseCodes.update `  
` compute.licenseCodes.use `  
  
Compute Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Compute Engine  |  In benutzerdefinierten Rollen nicht unterstützt  |  `
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
  
Google Kubernetes Engine  |  Hinzugefügt  |  ` container.services.updateStatus
`  
  
Google Kubernetes Engine  |  In benutzerdefinierten Rollen unterstützt  |  `
container.clusters.create `  
` container.clusters.delete `  
` container.clusters.get `  
` container.clusters.getCredentials `  
` container.clusters.list `  
` container.clusters.update `  
` container.operations.get `  
` container.operations.list `  
  
Dataproc  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Datastore  |  In benutzerdefinierten Rollen nicht unterstützt  |  `
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
  
Cloud Deployment Manager  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Dialogflow  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Fehlerberichte  |  In benutzerdefinierten Rollen unterstützt  |  `
errorreporting.applications.list `  
` errorreporting.errorEvents.create `  
` errorreporting.errorEvents.delete `  
` errorreporting.errorEvents.list `  
` errorreporting.groupMetadata.get `  
` errorreporting.groupMetadata.update `  
` errorreporting.groups.list `  
  
Cloud Identity and Access Management  |  In benutzerdefinierten Rollen nicht
unterstützt  |  ` iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
Cloud Logging  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
AI Platform  |  In benutzerdefinierten Rollen unterstützt  |  ` ml.jobs.cancel
`  
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
  
Cloud Monitoring  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Pub/Sub  |  In benutzerdefinierten Rollen unterstützt  |  `
pubsub.topics.setIamPolicy `  
  
Dienstverwaltung  |  In benutzerdefinierten Rollen unterstützt  |  `
servicemanagement.services.check `  
` servicemanagement.services.report `  
  
Dienstverwaltung  |  In benutzerdefinierten Rollen nicht unterstützt  |  `
servicemanagement.consumerSettings.get `  
` servicemanagement.consumerSettings.getIamPolicy `  
` servicemanagement.consumerSettings.list `  
` servicemanagement.consumerSettings.setIamPolicy `  
` servicemanagement.consumerSettings.update `  
  
Cloud Source Repositories  |  In benutzerdefinierten Rollen unterstützt  |  `
source.repos.delete `  
` source.repos.get `  
` source.repos.getIamPolicy `  
` source.repos.list `  
` source.repos.setIamPolicy `  
  
Cloud Source Repositories  |  In benutzerdefinierten Rollen nicht unterstützt
|  ` source.repos.update `  
  
Cloud Spanner  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Cloud Spanner  |  In benutzerdefinierten Rollen nicht unterstützt  |  `
spanner.databaseOperations.delete `  
` spanner.databases.update `  
  
cl  |  In benutzerdefinierten Rollen unterstützt  |  ` storage.buckets.create
`  
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 08.12.2017

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
BigQuery  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
BigQuery  |  In benutzerdefinierten Rollen nicht unterstützt  |  `
bigquery.config.get `  
` bigquery.config.update `  
` bigquery.service.actAsSuperuser `  
` bigquery.tables.update `  
` bigquery.tables.updateData `  
` bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Cloud Bigtable  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
Compute Engine  |  Hinzugefügt:  |  ` compute.disks.getIamPolicy `  
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
  
Dataflow  |  In benutzerdefinierten Rollen unterstützt  |  `
dataflow.jobs.cancel `  
` dataflow.jobs.create `  
` dataflow.jobs.get `  
` dataflow.jobs.list `  
` dataflow.jobs.updateContents `  
` dataflow.messages.list `  
` dataflow.metrics.get `  
  
Dataproc  |  Hinzugefügt:  |  ` dataproc.workflowTemplates.instantiateInline `  
  
Cloud Data Loss Prevention  |  Hinzugefügt:  |  `
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
` dlp.jobs.cancel `  
` dlp.jobs.create `  
` dlp.jobs.delete `  
` dlp.jobs.get `  
` dlp.jobs.list `  
  
Pub/Sub  |  Hinzugefügt:  |  ` pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.get `  
` pubsub.snapshots.getIamPolicy `  
` pubsub.snapshots.list `  
` pubsub.snapshots.seek `  
` pubsub.snapshots.setIamPolicy `  
` pubsub.snapshots.update `  
  
Pub/Sub  |  In benutzerdefinierten Rollen unterstützt  |  `
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
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 01.12.2017

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Build  |  In benutzerdefinierten Rollen unterstützt  |  `
cloudbuild.builds.create `  
` cloudbuild.builds.get `  
` cloudbuild.builds.list `  
` cloudbuild.builds.update `  
  
Cloud Tool Results  |  Jetzt GA  |  ` cloudtoolresults.executions.create `  
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
  
Compute Engine  |  Jetzt GA  |  ` compute.instances.addMaintenancePolicies `  
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
  
Google Kubernetes Engine  |  Hinzugefügt  |  `
container.initializerConfigurations.create `  
` container.initializerConfigurations.delete `  
` container.initializerConfigurations.get `  
` container.initializerConfigurations.list `  
` container.initializerConfigurations.update `  
` container.pods.initialize `  
  
Google Kubernetes Engine  |  Jetzt GA  |  ` container.deployments.getScale `  
` container.deployments.updateScale `  
  
Dataprep by Trifacta  |  In benutzerdefinierten Rollen unterstützt  |  `
dataprep.projects.use `  
  
Cloud Identity and Access Management  |  In benutzerdefinierten Rollen
unterstützt  |  ` iam.roles.create `  
` iam.roles.delete `  
` iam.roles.get `  
` iam.roles.list `  
` iam.roles.undelete `  
` iam.roles.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 10.11.2017

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Google Kubernetes Engine  |  Hinzugefügt:  |  `
container.clusters.getIamPolicy `  
` container.clusters.setIamPolicy `  
  
AI Platform  |  Hinzugefügt:  |  ` ml.locations.get `  
` ml.locations.list `  
  
Cloud Monitoring  |  Hinzugefügt:  |  ` monitoring.metricDescriptors.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 27.10.2017

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Compute Engine  |  Hinzugefügt:  |  ` compute.instances.updateShieldedVmConfig
`  
  
Identity-Aware Proxy  |  Hinzugefügt:  |  ` iap.web.getIamPolicy `  
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
  
Dienstverwaltung  |  In benutzerdefinierten Rollen unterstützt  |  `
servicemanagement.services.create `  
` servicemanagement.services.delete `  
` servicemanagement.services.get `  
` servicemanagement.services.getIamPolicy `  
` servicemanagement.services.list `  
` servicemanagement.services.setIamPolicy `  
` servicemanagement.services.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 06.10.2017

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Dataproc  |  Jetzt GA  |  ` dataproc.workflowTemplates.create `  
` dataproc.workflowTemplates.delete `  
` dataproc.workflowTemplates.get `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.instantiate `  
` dataproc.workflowTemplates.list `  
` dataproc.workflowTemplates.setIamPolicy `  
` dataproc.workflowTemplates.update `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 22.09.2017

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
App Engine  |  Hinzugefügt:  |  ` appengine.memcache.addKey `  
` appengine.memcache.flush `  
` appengine.memcache.get `  
` appengine.memcache.getKey `  
` appengine.memcache.list `  
` appengine.memcache.update `  
  
Cloud SQL  |  Hinzugefügt:  |  ` cloudsql.instances.demoteMaster `  
  
Cloud SQL  |  Jetzt GA  |  ` cloudsql.instances.demoteMaster `  
  
  
##  Cloud IAM-Änderungen mit Wirkung ab 08.09.2017

Dienst  |  Änderung  |  Beschreibung  
---|---|---  
Cloud Functions  |  Hinzugefügt:  |  ` cloudfunctions.functions.call `  
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
  
Compute Engine  |  Hinzugefügt:  |  ` compute.instances.setDeletionProtection
`  
` compute.targetHttpsProxies.setUrlMap `  
  
Google Kubernetes Engine  |  Hinzugefügt  |  ` container.statefulSets.getScale
`  
` container.statefulSets.updateScale `  
  
Google Kubernetes Engine  |  Jetzt GA  |  ` container.statefulSets.getScale `  
` container.statefulSets.updateScale `  
  
Cloud Functions  |  Hinzugefügt:  |  ` dlp.kms.encrypt `  
` dlp.riskAnalysisOperations.cancel `  
` dlp.riskAnalysisOperations.create `  
` dlp.riskAnalysisOperations.get `  
` dlp.riskAnalysisOperations.list `  

