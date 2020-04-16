#  Registro de alterações de permissões do IAM

Nesta página, descrevemos as alterações nas permissões públicas do Cloud IAM
de todos os serviços Beta e que normalmente estão disponíveis no Google Cloud.
Este registro de alterações ajuda você a manter e solucionar problemas dos
seus [ papéis personalizados
](https://cloud.google.com/iam/docs/understanding-custom-roles?hl=pt_br) .

Quando uma permissão é descontinuada ou não é mais compatível com papéis
personalizados, o Cloud IAM a remova automaticamente dos seus papéis
personalizados. Por outro lado, quando uma permissão é adicionada, o Cloud IAM
_não_ adiciona automaticamente a permissão aos seus papéis personalizados.

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) (em inglês) ou
adicione o URL do feed diretamente: ` https://cloud.google.com/feeds/cloud-
iam-permissions-change-log.xml `

Registro de alterações de permissões do IAM

##  Próximas alterações do Cloud IAM para a semana de 2 de março de 2020

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/compute.networkAdmin ` (Administrador de rede do Compute Engine):

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/compute.networkViewer ` (Visualizador de rede do Compute Engine):

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/editor ` (Editor):

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
  
Cloud Identity and Access Management  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/iam.securityAdmin `
(Administrador de segurança):

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
Cloud Identity and Access Management  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/iam.securityReviewer ` (Avaliador de segurança):

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
Identity Platform  |  Papel adicionado  |

O papel ` roles/identityplatform.admin ` (Administrador do Identity Platform)
foi adicionado com as seguintes permissões:

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
  
Identity Platform  |  Papel adicionado  |

O papel ` roles/identityplatform.viewer ` (Visualizador do Identity Platform)
foi adicionado com as seguintes permissões:

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
  
API Network Management  |  Agora com disponibilidade geral  |

O papel ` roles/networkmanagement.admin ` (Administrador do Network
Management) agora é GA.  
  
API Network Management  |  Agora com disponibilidade geral  |

O papel ` roles/networkmanagement.viewer ` (Visualizador do Network
Management) agora é GA.  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/owner `
(Proprietário):

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
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/viewer `
(Visualizador):

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.get `  
` servicedirectory.locations.list `  
  
BigQuery  |  Adicionado  |  ` bigquery.bireservations.get `  
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
  
BigQuery  |  Aceito em papéis personalizados  |  ` bigquery.bireservations.get
`  
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
  
Identity Platform  |  Adicionado  |  `
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
  
API Network Management  |  Agora com disponibilidade geral  |  `
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
  
Memorystore para Redis  |  Adicionado  |  ` redis.instances.failover `  
` redis.instances.upgrade `  
  
Memorystore para Redis  |  Aceito em papéis personalizados  |  `
redis.instances.failover `  
` redis.instances.upgrade `  
  
Diretório de serviços  |  Adicionado  |  ` servicedirectory.endpoints.create `  
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
  
Diretório de serviços  |  Aceito em papéis personalizados  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 27 de fevereiro de 2020

Serviço  |  Alteração  |  Descrição  
---|---|---  
BigQuery  |  Agora com disponibilidade geral  |

O papel ` roles/bigquery.readSessionUser ` (usuário de sessão de leitura do
BigQuery) agora é GA.  
  
Data Catalog  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/datacatalog.entryGroupCreator ` (Criador de EntryGroup do DataCatalog):

` datacatalog.entryGroups.list `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/editor ` (Editor):

` dlp.jobs.create `  
` dlp.jobs.get `  
` dlp.jobs.list `  
  
Gerenciador de secrets  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/secretmanager.secretAccessor ` (Acessador de secrets do Gerenciador de
secrets):

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Security Command Center  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/securitycenter.adminEditor ` (Editor administrativo da Central de
segurança):

` securitycenter.organizationsettings.get `  
  
Security Command Center  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/securitycenter.adminViewer ` (Visualizador administrativo da Central de
segurança):

` securitycenter.organizationsettings.get `  
  
Cloud Spanner  |  Agora com disponibilidade geral  |

O papel ` roles/spanner.backupAdmin ` (Administrador de backup do Cloud
Spanner) agora é GA.  
  
Cloud Spanner  |  Agora com disponibilidade geral  |

O papel ` roles/spanner.backupWriter ` (Gravador de backup do Cloud Spanner)
agora é GA.  
  
Cloud Spanner  |  Agora com disponibilidade geral  |

O papel ` roles/spanner.restoreAdmin ` (Administrador de restauração do Cloud
Spanner) agora é GA.  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/viewer `
(Visualizador):

` dlp.jobs.get `  
` dlp.jobs.list `  
  
BigQuery  |  Adicionado  |  ` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  Aceito em papéis personalizados  |  `
bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  Agora com disponibilidade geral  |  `
bigquery.readsessions.create `  
` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
Data Catalog  |  Adicionado  |  ` datacatalog.entryGroups.list `  
  
Data Catalog  |  Aceito em papéis personalizados  |  `
datacatalog.entryGroups.list `  
  
API Cloud Healthcare  |  Aceito em papéis personalizados  |  `
healthcare.fhirStores.executeBundle `  
  
Cloud Identity and Access Management  |  Aceito em papéis personalizados  |  `
iam.serviceAccounts.getOpenIdToken `  
  
Cloud Spanner  |  Adicionado  |  ` spanner.backupOperations.cancel `  
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
  
Cloud Spanner  |  Compatibilidade com papéis personalizados  |  `
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
  
Cloud Spanner  |  Agora com disponibilidade geral  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 21 de fevereiro de 2020

Serviço  |  Alteração  |  Descrição  
---|---|---  
Access Context Manager  |  Adicionado  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Access Context Manager  |  Agora com disponibilidade geral  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Compute Engine  |  Adicionado  |  ` compute.regionHealthCheckServices.create `  
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
  
Compute Engine  |  Aceito em papéis personalizados  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 14 de fevereiro de 2020

Serviço  |  Alteração  |  Descrição  
---|---|---  
Suporte do Google Cloud  |  Agora com disponibilidade geral  |

O papel ` roles/cloudsupport.techSupportEditor ` (Editor de suporte técnico)
agora é GA.  
  
Suporte do Google Cloud  |  Agora com disponibilidade geral  |

O papel ` roles/cloudsupport.techSupportViewer ` (Visualizador de suporte
técnico) agora é GA.  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/editor ` (Editor):

` healthcare.fhirStores.executeBundle `  
  
API Cloud Healthcare  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/healthcare.fhirResourceEditor ` (Editor de recursos do Healthcare FHIR):

` healthcare.fhirStores.executeBundle `  
  
API Cloud Healthcare  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/healthcare.fhirResourceReader ` (Leitor de recursos do Healthcare FHIR):

` healthcare.fhirStores.executeBundle `  
  
Cloud Logging  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/logging.privateLogViewer ` (Visualizador de registros privados):

` logging.buckets.get `  
` logging.buckets.list `  
  
Cloud Logging  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/logging.viewer `
(Visualizador de registros):

` logging.buckets.get `  
` logging.buckets.list `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/owner `
(Proprietário):

` healthcare.fhirStores.executeBundle `  
  
Security Command Center  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/securitycenter.admin ` (Administrador da Central de segurança):

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
  
Security Command Center  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/securitycenter.adminEditor ` (Editor administrativo da Central de
segurança):

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
  
Security Command Center  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/securitycenter.adminViewer ` (Visualizador administrativo da Central de
segurança):

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
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/viewer `
(Visualizador):

` healthcare.fhirStores.executeBundle `  
  
Suporte do Google Cloud  |  Adicionado  |  ` cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Suporte do Google Cloud  |  Aceito em papéis personalizados  |  `
cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Suporte do Google Cloud  |  Agora com disponibilidade geral  |  `
cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
API Cloud Healthcare  |  Adicionado  |  ` healthcare.fhirStores.executeBundle
`  
  
Cloud Logging  |  Adicionado  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud Logging  |  Aceito em papéis personalizados  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud Logging  |  Agora com disponibilidade geral  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
  
##  Alterações do Cloud IAM a partir de 7 de fevereiro de 2020

Serviço  |  Alteração  |  Descrição  
---|---|---  
Gerenciador de secrets  |  Agora com disponibilidade geral  |

O papel ` roles/secretmanager.admin ` (Administrador do Gerenciador de
secrets) agora é GA.  
  
Gerenciador de secrets  |  Agora com disponibilidade geral  |

O papel ` roles/secretmanager.secretAccessor ` (Acessador de secrets do
Gerenciador de secrets) agora é GA.  
  
Gerenciador de secrets  |  Agora com disponibilidade geral  |

O papel ` roles/secretmanager.viewer ` (Visualizador do Gerenciador de
secrets) agora é GA.  
  
API Cloud Healthcare  |  Aceito em papéis personalizados  |  `
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
  
reCAPTCHA Enterprise  |  Adicionado  |  `
recaptchaenterprise.assessments.annotate `  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
reCAPTCHA Enterprise  |  Aceito em papéis personalizados  |  `
recaptchaenterprise.assessments.annotate `  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
Gerenciador de secrets  |  Aceito em papéis personalizados  |  `
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
  
Gerenciador de secrets  |  Agora com disponibilidade geral  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 31 de janeiro de 2020

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud Build  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudbuild.builds.builder ` (conta de serviço do Cloud Build):

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
  
Cloud Composer  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/composer.worker `
(Worker do Compositor):

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
  
Google Cloud Game Servers  |  Adicionado  |  `
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
  
Google Cloud Game Servers  |  Aceito em papéis personalizados  |  `
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
  
Pacote de operações do Google Cloud  |  Adicionado  |  `
opsconfigmonitoring.resourceMetadata.write `  
  
  
##  Alterações do Cloud IAM a partir de 24 de janeiro de 2020

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud Scheduler  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudscheduler.admin ` (administrador do Cloud Scheduler):

` serviceusage.services.list `  
  
Cloud Scheduler  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudscheduler.jobRunner ` (Executor de jobs do Cloud Schedule):

` serviceusage.services.list `  
  
Cloud Scheduler  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudscheduler.viewer ` (Visualizador do Cloud Scheduler):

` serviceusage.services.list `  
  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/compute.networkAdmin ` (Administrador de rede do Compute Engine):

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/compute.networkViewer ` (Visualizador de rede do Compute Engine):

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.notificationConfigEditor ` (Editor de
configurações de notificação da Central de segurança) agora é GA.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.notificationConfigViewer ` (Visualizador de
configurações de notificação da Central de segurança) agora é GA.  
  
Artifact Registry  |  Adicionado  |  ` artifactregistry.files.get `  
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
  
Artifact Registry  |  Aceito em papéis personalizados  |  `
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
  
Cloud Identity and Access Management  |  Adicionado  |  `
iam.serviceAccounts.getOpenIdToken `  
  
Security Command Center  |  Adicionado  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
Security Command Center  |  Aceito em papéis personalizados  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
Security Command Center  |  Agora com disponibilidade geral  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
  
##  Alterações do Cloud IAM a partir de 10 de janeiro de 2020

Serviço  |  Alteração  |  Descrição  
---|---|---  
Inventário de recursos do Cloud  |  Agora com disponibilidade geral  |

O papel ` roles/cloudasset.owner ` (Proprietário de recursos do Cloud) agora
tem disponibilidade geral.  
  
Migrate for Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudmigration.inframanager ` (Gerenciador do Velostrata):

` compute.globalOperations.get `  
  
Cloud Spanner  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/spanner.databaseReader ` (Leitor de banco de dados do Cloud Spanner):

` spanner.instances.get `  
  
Cloud Spanner  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/spanner.databaseUser ` (Usuário de banco de dados do Cloud Spanner):

` spanner.instances.get `  
  
Inventário de recursos do Cloud  |  Agora com disponibilidade geral  |  `
cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Compute Engine  |  Adicionado  |  ` compute.networks.listPeeringRoutes `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.networks.listPeeringRoutes `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.networks.listPeeringRoutes `  
  
API Network Management  |  Adicionado  |  `
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
  
API Network Management  |  Aceito em papéis personalizados  |  `
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
  
  
##  Alteração do Cloud IAM a partir de 20 de dezembro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Migrate for Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudmigration.inframanager ` (Gerenciador do Velostrata):

` compute.disks.createSnapshot `  
` compute.snapshots.create `  
` compute.snapshots.delete `  
` compute.snapshots.get `  
` compute.snapshots.setLabels `  
` compute.snapshots.useReadOnly `  
  
Cloud Scheduler  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudscheduler.admin ` (administrador do Cloud Scheduler):

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud Scheduler  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudscheduler.jobRunner ` (Executor de jobs do Cloud Schedule):

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud Scheduler  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudscheduler.viewer ` (Visualizador do Cloud Scheduler):

` appengine.applications.get `  
` serviceusage.services.get `  
  
Compute Engine  |  Agora com disponibilidade geral  |

O papel ` roles/compute.packetMirroringAdmin ` (Administrador de espelhamento
de pacotes do Compute Engine) agora tem disponibilidade geral.  
  
Compute Engine  |  Agora com disponibilidade geral  |

O papel ` roles/compute.packetMirroringUser ` (Usuário de espelhamento de
pacotes do Compute Engine) agora tem disponibilidade geral.  
  
Cloud DNS  |  Agora com disponibilidade geral  |

O papel ` roles/dns.peer ` (peer DNS) agora tem disponibilidade geral.  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram removidas do papel ` roles/editor ` (Editor):

` datacatalog.taxonomies.create `  
  
Recomendador  |  Agora com disponibilidade geral  |

O papel ` roles/recommender.computeAdmin ` (Administrador de recomendações do
Compute Engine) agora tem disponibilidade geral.  
  
Recomendador  |  Agora com disponibilidade geral  |

O papel ` roles/recommender.computeViewer ` (Visualizador de recomendações do
Compute Engine) agora tem disponibilidade geral.  
  
Recomendador  |  Agora com disponibilidade geral  |

O papel ` roles/recommender.iamAdmin ` (Administrador de recomendações do IAM)
agora tem disponibilidade geral.  
  
Recomendador  |  Agora com disponibilidade geral  |

O papel ` roles/recommender.iamViewer ` (Visualizador de recomendações do IAM)
agora tem disponibilidade geral.  
  
Remote Build Execution  |  Papel adicionado  |

O papel ` roles/remotebuildexecution.reservationAdmin ` (Administrador de
reservas do Remote Build Execution) foi adicionado com as seguintes
permissões:

` remotebuildexecution.actions.create `  
` remotebuildexecution.actions.delete `  
` remotebuildexecution.actions.get `  
  
Cloud Bigtable  |  Adicionado  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  Aceito em papéis personalizados  |  `
bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  Agora com disponibilidade geral  |  `
bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Compute Engine  |  Adicionado  |  ` compute.nodeGroups.update `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.nodeGroups.update `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Data Catalog  |  Adicionado  |  ` datacatalog.entries.list `  
` datacatalog.entries.updateTag `  
` datacatalog.entryGroups.update `  
  
Dataproc  |  Adicionado  |  ` dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
Dataproc  |  Agora com disponibilidade geral  |  `
dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
Cloud DNS  |  Agora com disponibilidade geral  |  `
dns.networks.targetWithPeeringZone `  
  
Cloud Logging  |  Adicionado  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud Logging  |  Aceito em papéis personalizados  |  `
logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud Logging  |  Agora com disponibilidade geral  |  `
logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Recomendador  |  Agora com disponibilidade geral  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 22 de novembro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Data Catalog  |  Papel atualizado  |

As seguintes permissões foram removidas do papel ` roles/datacatalog.admin `
(Administrador do catálogo de dados):

` datacatalog.categories.fineGrainedGet `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/editor ` (Editor):

` remotebuildexecution.actions.delete `  
  
API Identity Toolkit  |  Agora com disponibilidade geral  |

O papel ` roles/identitytoolkit.admin ` (Administrador do Identity Toolkit)
agora tem disponibilidade geral.  
  
API Identity Toolkit  |  Agora com disponibilidade geral  |

O papel ` roles/identitytoolkit.viewer ` (Visualizador do Toolkit de
identidade) agora tem disponibilidade geral.  
  
API Apigee  |  Adicionado  |  ` apigee.apiproductattributes.createOrUpdateAll
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
  
API Apigee  |  Aceito em papéis personalizados  |  `
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
  
BigQuery  |  Adicionado  |  ` bigquery.tables.setCategory `  
  
Compute Engine  |  Adicionado  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Remote Build Execution  |  Adicionado  |  `
remotebuildexecution.actions.delete `  
  
Remote Build Execution  |  Aceito em papéis personalizados  |  `
remotebuildexecution.actions.delete `  
  
  
##  Alterações do Cloud IAM a partir de 14 de novembro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Aprovação de acesso  |  Adicionado  |  ` accessapproval.settings.delete `  
  
AI Platform Notebooks  |  Adicionado  |  ` notebooks.environments.create `  
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
  
AI Platform Notebooks  |  Aceito em papéis personalizados  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 1º de novembro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
API Hangouts Chat  |  Agora com disponibilidade geral  |

O papel ` roles/chat.owner ` (Proprietário de chatbots) agora tem
disponibilidade geral.  
  
API Hangouts Chat  |  Agora com disponibilidade geral  |

O papel ` roles/chat.reader ` (Visualizador de chatbots) agora tem
disponibilidade geral.  
  
API Hangouts Chat  |  Agora com disponibilidade geral  |  ` chat.bots.get `  
` chat.bots.update `  
  
Inventário de recursos do Cloud  |  Adicionado  |  `
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
  
Data Catalog  |  Adicionado  |  ` datacatalog.categories.fineGrainedGet `  
` datacatalog.categories.getIamPolicy `  
` datacatalog.categories.setIamPolicy `  
` datacatalog.taxonomies.create `  
` datacatalog.taxonomies.delete `  
` datacatalog.taxonomies.get `  
` datacatalog.taxonomies.getIamPolicy `  
` datacatalog.taxonomies.list `  
` datacatalog.taxonomies.setIamPolicy `  
` datacatalog.taxonomies.update `  
  
Identity-Aware Proxy  |  Adicionado  |  ` iap.projects.getSettings `  
` iap.projects.updateSettings `  
  
NetApp Cloud Volumes Service  |  Adicionado  |  ` netappcloudvolumes.jobs.get
`  
` netappcloudvolumes.jobs.list `  
  
Redis Enterprise Cloud  |  Adicionado  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 25 de outubro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Identity-Aware Proxy  |  Agora com disponibilidade geral  |

O papel ` roles/iap.tunnelResourceAccessor ` (Usuário de túnel protegido por
IAP) agora tem disponibilidade geral.  
  
Serviço gerenciado para Microsoft Active Directory  |  Agora com
disponibilidade geral  |

O papel ` roles/managedidentities.admin ` (Administrador de identidades
gerenciadas pelo Google Cloud) agora tem disponibilidade geral.  
  
Serviço gerenciado para Microsoft Active Directory  |  Agora com
disponibilidade geral  |

O papel ` roles/managedidentities.domainAdmin ` (Administrador de domínio de
identidades gerenciadas pelo Google Cloud) agora tem disponibilidade geral.  
  
Serviço gerenciado para Microsoft Active Directory  |  Agora com
disponibilidade geral  |

O papel ` roles/managedidentities.viewer ` (Visualizador de identidades
gerenciadas pelo Google Cloud) agora tem disponibilidade geral.  
  
API Actions  |  Adicionado  |  ` actions.agentVersions.get `  
  
API Actions  |  Aceito em papéis personalizados  |  `
actions.agentVersions.get `  
  
API Actions  |  Agora com disponibilidade geral  |  `
actions.agentVersions.get `  
  
Dialogflow  |  Adicionado  |  ` dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
Dialogflow  |  Agora com disponibilidade geral  |  `
dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
Identity-Aware Proxy  |  Agora com disponibilidade geral  |  `
iap.tunnel.getIamPolicy `  
` iap.tunnel.setIamPolicy `  
` iap.tunnelInstances.accessViaIAP `  
` iap.tunnelInstances.getIamPolicy `  
` iap.tunnelInstances.setIamPolicy `  
` iap.tunnelZones.getIamPolicy `  
` iap.tunnelZones.setIamPolicy `  
  
Serviço gerenciado para Microsoft Active Directory  |  Agora com
disponibilidade geral  |  ` managedidentities.domains.attachTrust `  
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
  
  
##  Alterações do Cloud IAM a partir de 18 de outubro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Identity-Aware Proxy  |  Agora com disponibilidade geral  |

O papel ` roles/iap.settingsAdmin ` (Administrador das configurações de IAP)
agora tem disponibilidade geral.  
  
Identity-Aware Proxy  |  Adicionado  |  ` iap.web.getSettings `  
` iap.web.updateSettings `  
` iap.webServiceVersions.getSettings `  
` iap.webServiceVersions.updateSettings `  
` iap.webServices.getSettings `  
` iap.webServices.updateSettings `  
` iap.webTypes.getSettings `  
` iap.webTypes.updateSettings `  
  
  
##  Alterações do Cloud IAM a partir de 11 de outubro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Regras de segurança do Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebaserules.admin ` (Administrador de regras do Firebase)
agora tem disponibilidade geral.  
  
Regras de segurança do Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebaserules.viewer ` (Visualizador de regras do Firebase)
agora tem disponibilidade geral.  
  
BigQuery  |  Aceito em papéis personalizados  |  ` bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Google Kubernetes Engine  |  Adicionado  |  ` container.csiDrivers.create `  
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
  
Google Kubernetes Engine  |  Compatibilidade com papéis personalizados  |  `
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
  
Google Kubernetes Engine  |  Agora com disponibilidade geral  |  `
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
  
Regras de segurança do Firebase  |  Agora com disponibilidade geral  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 4 de outubro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
API Actions  |  Adicionado  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
API Actions  |  Aceito em papéis personalizados  |  `
actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
API Actions  |  Agora com disponibilidade geral  |  `
actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Cloud Identity and Access Management  |  Aceito em papéis personalizados  |  `
iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
  
  
##  Alterações do Cloud IAM a partir de 27 de setembro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
API Hangouts Chat  |  Adicionado  |  ` chat.bots.get `  
` chat.bots.update `  
  
API Hangouts Chat  |  Aceito em papéis personalizados  |  ` chat.bots.get `  
` chat.bots.update `  
  
Inventário de recursos do Cloud  |  Adicionado  |  `
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
  
Inventário de recursos do Cloud  |  Aceito em papéis personalizados  |  `
cloudasset.assets.exportAccessPolicy `  
` cloudasset.assets.exportOrgPolicy `  
` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Cloud Identity and Access Management  |  Aceito em papéis personalizados  |  `
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
  
API VM Migration  |  Adicionado  |  ` vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
API VM Migration  |  Aceito em papéis personalizados  |  `
vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
  
##  Alterações do Cloud IAM a partir de 20 de setembro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud Key Management Service  |  Agora com disponibilidade geral  |

O papel ` roles/cloudkms.importer ` (Importador do Cloud KMS ) agora tem
disponibilidade geral.  
  
Cloud Key Management Service  |  Agora com disponibilidade geral  |

O papel ` roles/cloudkms.publicKeyViewer ` (Visualizador de chaves públicas de
CryptoKey do Cloud KMS) agora tem disponibilidade geral.  
  
Cloud Key Management Service  |  Agora com disponibilidade geral  |

O papel ` roles/cloudkms.signer ` (Signatário de CryptoKey do Cloud KMS) agora
tem disponibilidade geral.  
  
Cloud Key Management Service  |  Agora com disponibilidade geral  |

O papel ` roles/cloudkms.signerVerifier ` (Signatário/verificador de CryptoKey
do Cloud KMS) agora tem disponibilidade geral.  
  
Cloud Key Management Service  |  Adicionado  |  ` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  Aceito em papéis personalizados  |  `
cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  Agora com disponibilidade geral  |  `
cloudkms.cryptoKeyVersions.useToSign `  
` cloudkms.cryptoKeyVersions.viewPublicKey `  
` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
  
##  Alterações do Cloud IAM a partir de 13 de setembro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Configuração remota do Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/cloudconfig.admin ` (Administrador da Configuração remota do
Firebase) agora tem disponibilidade geral.  
  
Configuração remota do Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/cloudconfig.viewer ` (Visualizador de configuração remota do
Firebase) agora tem disponibilidade geral.  
  
Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebase.admin ` (Administrador do Firebase) agora tem
disponibilidade geral.  
  
Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebase.analyticsAdmin ` (Administrador do Firebase
Analytics) agora tem disponibilidade geral.  
  
Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebase.analyticsViewer ` (Visualizador do Firebase
Analytics) agora tem disponibilidade geral.  
  
Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebase.developAdmin ` (Administrador do Firebase Develop)
agora tem disponibilidade geral.  
  
Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebase.developViewer ` (Visualizador do Firebase Develop)
agora tem disponibilidade geral.  
  
Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebase.growthAdmin ` (Administrador do Firebase Grow) agora
tem disponibilidade geral.  
  
Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebase.growthViewer ` (Visualizador do Firebase Grow) agora
tem disponibilidade geral.  
  
Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebase.qualityAdmin ` (Administrador de qualidade do
Firebase) agora tem disponibilidade geral.  
  
Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebase.qualityViewer ` (Visualizador de qualidade do
Firebase) agora tem disponibilidade geral.  
  
Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebase.viewer ` (Visualizador do Firebase) agora tem
disponibilidade geral.  
  
Firebase Authentication  |  Agora com disponibilidade geral  |

O papel ` roles/firebaseauth.admin ` (Administrador do Firebase
Authentication) agora tem disponibilidade geral.  
  
Firebase Authentication  |  Agora com disponibilidade geral  |

O papel ` roles/firebaseauth.viewer ` (Visualizador do Firebase
Authentication) agora tem disponibilidade geral.  
  
Firebase Crashlytics  |  Agora com disponibilidade geral  |

O papel ` roles/firebasecrashlytics.admin ` (Administrador do Firebase
Crashlytics) agora tem disponibilidade geral.  
  
Firebase Crashlytics  |  Agora com disponibilidade geral  |

O papel ` roles/firebasecrashlytics.viewer ` (Visualizador do Firebase
Crashlytics) agora tem disponibilidade geral.  
  
Firebase Realtime Database  |  Agora com disponibilidade geral  |

O papel ` roles/firebasedatabase.admin ` (Administrador Firebase Realtime
Database) agora tem disponibilidade geral.  
  
Firebase Realtime Database  |  Agora com disponibilidade geral  |

O papel ` roles/firebasedatabase.viewer ` (Visualizador do Firebase Realtime
Database) agora tem disponibilidade geral.  
  
Firebase Dynamic Links  |  Agora com disponibilidade geral  |

O papel ` roles/firebasedynamiclinks.admin ` (Administrador do Firebase
Dynamic Links) agora tem disponibilidade geral.  
  
Firebase Dynamic Links  |  Agora com disponibilidade geral  |

O papel ` roles/firebasedynamiclinks.viewer ` (Visualizador do Firebase
Dynamic Links) agora tem disponibilidade geral.  
  
Firebase Hosting  |  Agora com disponibilidade geral  |

O papel ` roles/firebasehosting.admin ` (Administrador do Firebase Hosting)
agora tem disponibilidade geral.  
  
Firebase Hosting  |  Agora com disponibilidade geral  |

O papel ` roles/firebasehosting.viewer ` (Visualizador do Firebase Hosting)
agora tem disponibilidade geral.  
  
Firebase Cloud Messaging  |  Agora com disponibilidade geral  |

O papel ` roles/firebasenotifications.admin ` (Administrador do Firebase Cloud
Messaging) agora tem disponibilidade geral.  
  
Firebase Cloud Messaging  |  Agora com disponibilidade geral  |

O papel ` roles/firebasenotifications.viewer ` (Visualizador do Firebase Cloud
Messaging) agora tem disponibilidade geral.  
  
Monitoramento de desempenho do Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebaseperformance.admin ` (Administrador do Firebase
Performance Reporting) agora tem disponibilidade geral.  
  
Monitoramento de desempenho do Firebase  |  Agora com disponibilidade geral  |

O papel ` roles/firebaseperformance.viewer ` (Visualizador do Firebase
Performance Reporting) agora tem disponibilidade geral.  
  
Firebase Previsões  |  Agora com disponibilidade geral  |

O papel ` roles/firebasepredictions.admin ` (Administrador do Firebase
Previsões) agora tem disponibilidade geral.  
  
Firebase Previsões  |  Agora com disponibilidade geral  |

O papel ` roles/firebasepredictions.viewer ` (Visualizador do Firebase
Previsões) agora tem disponibilidade geral.  
  
Configuração remota do Firebase  |  Agora com disponibilidade geral  |  `
cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Cloud DNS  |  Agora com disponibilidade geral  |  `
dns.networks.bindPrivateDNSPolicy `  
` dns.policies.create `  
` dns.policies.delete `  
` dns.policies.get `  
` dns.policies.getIamPolicy `  
` dns.policies.list `  
` dns.policies.setIamPolicy `  
` dns.policies.update `  
  
Firebase  |  Agora com disponibilidade geral  |  ` firebase.billingPlans.get `  
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
  
Firebase Authentication  |  Agora com disponibilidade geral  |  `
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
  
Firebase Crashlytics  |  Agora com disponibilidade geral  |  `
firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase Realtime Database  |  Agora com disponibilidade geral  |  `
firebasedatabase.instances.create `  
` firebasedatabase.instances.get `  
` firebasedatabase.instances.list `  
` firebasedatabase.instances.update `  
  
Firebase Dynamic Links  |  Agora com disponibilidade geral  |  `
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
  
Firebase Hosting  |  Agora com disponibilidade geral  |  `
firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase Cloud Messaging  |  Agora com disponibilidade geral  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Monitoramento de desempenho do Firebase  |  Agora com disponibilidade geral  |
` firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Previsões  |  Agora com disponibilidade geral  |  `
firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
NetApp Cloud Volumes Service  |  Adicionado  |  `
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
  
Event Threat Detection  |  Aceito em papéis personalizados  |  `
threatdetection.detectorSettings.clear `  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  Alterações do Cloud IAM a partir de 6 de setembro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/owner `
(Proprietário):

` dataprocessing.iamaccesshistory.exportData `  
  
Acesso VPC sem servidor  |  Agora com disponibilidade geral  |

O papel ` roles/vpaccess.user ` (Usuário de acesso VPC sem servidor) agora tem
disponibilidade geral.  
  
Acesso VPC sem servidor  |  Agora com disponibilidade geral  |

O papel ` roles/vpaccess.viewer ` (Visualizador de acesso VPC sem servidor)
agora tem disponibilidade geral.  
  
Acesso VPC sem servidor  |  Agora com disponibilidade geral  |

O papel ` roles/vpcaccess.admin ` (Administrador de acesso VPC sem servidor)
agora tem disponibilidade geral.  
  
Compute Engine  |  Adicionado  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Acesso VPC sem servidor  |  Agora com disponibilidade geral  |  `
vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  Alterações do Cloud IAM a partir de 30 de agosto de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Firebase Test Lab  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudtestservice.testAdmin ` (Administrador do Firebase Test Lab):

` firebase.clients.get `  
` firebase.projects.get `  
  
Firebase Test Lab  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudtestservice.testViewer ` (Firebase Test Lab Viewer):

` firebase.clients.get `  
` firebase.projects.get `  
  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/compute.orgSecurityPolicyAdmin ` (Administrador de políticas de
segurança da organização do Compute Engine):

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/compute.orgSecurityPolicyUser ` (Usuário de políticas de segurança da
organização do Compute Engine):

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/compute.orgSecurityResourceAdmin ` (Administrador de recursos da
organização do Compute Engine):

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
  
##  Alterações do Cloud IAM a partir de 23 de agosto de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Tradução  |  Agora com disponibilidade geral  |

O papel ` roles/cloudtranslate.admin ` (Administrador da API Cloud
Translation) agora tem disponibilidade geral.  
  
Tradução  |  Agora com disponibilidade geral  |

O papel ` roles/cloudtranslate.editor ` (Editor da API Cloud Translation)
agora tem disponibilidade geral.  
  
Tradução  |  Agora com disponibilidade geral  |

O papel ` roles/cloudtranslate.user ` (Usuário da API Cloud Translation) agora
tem disponibilidade geral.  
  
Tradução  |  Agora com disponibilidade geral  |

O papel ` roles/cloudtranslate.viewer ` (Visualizador da API Cloud
Translation) agora tem disponibilidade geral.  
  
API Cloud Healthcare  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/healthcare.dicomEditor ` (Editor de DICOM do Healthcare):

` healthcare.dicomStores.dicomWebDelete `  
  
Tradução  |  Agora com disponibilidade geral  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 16 de agosto de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Tradução  |  Aceito em papéis personalizados  |  `
cloudtranslate.locations.get `  
` cloudtranslate.locations.list `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.networks.updatePeering `  
  
Data Catalog  |  Adicionado  |  ` datacatalog.entries.create `  
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
  
Data Catalog  |  Aceito em papéis personalizados  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 9 de outubro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/compute.orgSecurityPolicyAdmin ` (Administrador de políticas de
segurança da organização do Compute Engine):

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/compute.orgSecurityPolicyUser ` (Usuário de políticas de segurança da
organização do Compute Engine):

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/compute.orgSecurityResourceAdmin ` (Administrador de recursos da
organização do Compute Engine):

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Cloud Storage  |  Agora com disponibilidade geral  |

O papel ` roles/storage.hmacKeyAdmin ` (Administrador de chaves HMAC do
armazenamento) agora tem disponibilidade geral.  
  
Cloud Storage  |  Adicionado  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
Cloud Storage  |  Aceito em papéis personalizados  |  `
storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
Cloud Storage  |  Agora com disponibilidade geral  |  `
storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
  
##  Alterações do Cloud IAM a partir de 28 de junho de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/viewer `
(Visualizador):

` pubsub.snapshots.seek `  
  
Firebase Crashlytics  |  Adicionado  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase Crashlytics  |  Aceito em papéis personalizados  |  `
firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Memorystore para Redis  |  Adicionado  |  ` redis.instances.export `  
` redis.instances.import `  
  
Memorystore para Redis  |  Aceito em papéis personalizados  |  `
redis.instances.export `  
` redis.instances.import `  
  
  
##  Alterações do Cloud IAM a partir de 21 de junho de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Migrate for Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudmigration.inframanager ` (Gerenciador do Velostrata):

` compute.instances.updateShieldedInstanceConfig `  
  
Tradução  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudtranslate.viewer ` (Visualizador da API Cloud Translation):

` cloudtranslate.operations.wait `  
  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/compute.networkUser
` (Usuário de rede do Compute Engine):

` compute.vpnGateways.use `  
  
Firebase  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/firebase.admin `
(Administrador do Firebase):

` cloudmessaging.messages.create `  
  
Firebase  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/firebase.growthAdmin ` (Administrador do Firebase Grow):

` cloudmessaging.messages.create `  
  
Resource Manager  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/resourcemanager.projectMover ` (Movimentador de projetos):

` resourcemanager.projects.move `  
  
Security Command Center  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/securitycenter.adminEditor ` (Editor administrativo da Central de
segurança):

` securitycenter.assets.group `  
` securitycenter.assets.list `  
` securitycenter.assets.listAssetPropertyNames `  
  
BigQuery  |  Adicionado  |  ` bigquery.connections.create `  
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
  
BigQuery  |  Aceito em papéis personalizados  |  ` bigquery.routines.create `  
` bigquery.routines.delete `  
` bigquery.routines.get `  
` bigquery.routines.list `  
` bigquery.routines.update `  
  
Tradução  |  Aceito em papéis personalizados  |  `
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
  
Cloud Composer  |  Adicionado  |  ` composer.imageversions.list `  
  
Cloud Composer  |  Aceito em papéis personalizados  |  `
composer.imageversions.list `  
  
Cloud Composer  |  Agora com disponibilidade geral  |  `
composer.imageversions.list `  
  
Compute Engine  |  Adicionado  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
  
##  Alterações do Cloud IAM a partir de 14 de junho de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud Identity and Access Management  |  Agora com disponibilidade geral  |

O papel ` roles/iam.workloadIdentityUser ` (Usuário da identidade de carga de
trabalho) agora tem disponibilidade geral.  
  
Cloud Functions  |  Adicionado  |  ` cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Cloud Functions  |  Aceito em papéis personalizados  |  `
cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  Alterações do Cloud IAM a partir de 31 de maio de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Data Catalog  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/datacatalog.admin `
(Administrador do catálogo de dados):

` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
` pubsub.topics.updateTag `  
  
Migrate for Compute Engine  |  Adicionado  |  `
cloudmigration.velostrataendpoints.connect `  
  
Cloud Identity and Access Management  |  Disponível em papéis personalizados
|  ` iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
  
##  Alterações do Cloud IAM a partir de 24 de maio de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/viewer `
(Visualizador):

` managedidentities.domains.validateTrust `  
  
Recommendations AI  |  Aceito em papéis personalizados  |  `
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
  
BigQuery  |  Adicionado  |  ` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
BigQuery  |  Aceito em papéis personalizados  |  ` bigquery.datasets.updateTag
`  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
Data Catalog  |  Adicionado  |  ` datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
Data Catalog  |  Aceito em papéis personalizados  |  `
datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
Filestore  |  Adicionado  |  ` file.snapshots.update `  
  
Filestore  |  Aceito em papéis personalizados  |  ` file.snapshots.update `  
  
Pub/Sub  |  Adicionado  |  ` pubsub.topics.updateTag `  
  
Pub/Sub  |  Aceito em papéis personalizados  |  ` pubsub.topics.updateTag `  
  
  
##  Alterações do IAM a partir de 17 de maio de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Dialogflow  |  Adicionado  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  Compatibilidade com papéis personalizados  |  `
dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  Agora com disponibilidade geral  |  ` dialogflow.agents.create
`  
` dialogflow.agents.delete `  
  
  
##  Alterações do Cloud IAM a partir de 10 de maio de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud Identity and Access Management  |  Agora com disponibilidade geral  |

O papel ` roles/iam.securityAdmin ` (Administrador de segurança) agora tem
disponibilidade geral.  
  
Cloud IoT  |  Adicionado  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  Aceito em papéis personalizados  |  `
cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  Agora com disponibilidade geral  |  `
cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.healthChecks.create `  
` compute.healthChecks.delete `  
` compute.healthChecks.get `  
` compute.healthChecks.list `  
` compute.healthChecks.update `  
` compute.healthChecks.use `  
` compute.healthChecks.useReadOnly `  
` compute.instanceGroups.use `  
  
API Cloud Healthcare  |  Adicionado  |  ` healthcare.fhirResources.purge `  
  
Serviço gerenciado para Microsoft Active Directory  |  Adicionado  |  `
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
  
Serviço gerenciado para Microsoft Active Directory  |  Aceito em papéis
personalizados  |  ` managedidentities.domains.attachTrust `  
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
  
  
##  Alterações do Cloud IAM a partir de 3 de maio de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.admin ` (Administrador da Central de segurança)
agora tem disponibilidade geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.adminEditor ` (Editor administrativo da Central
de segurança) agora tem disponibilidade geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.adminViewer ` (Visualizador administrativo da
Central de segurança) agora tem disponibilidade geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.assetsDiscoveryRunner ` (Executor de detecção
de recursos da Central de segurança) agora tem disponibilidade geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.assetSecurityMarksWriter ` (Editor de marcação
de recursos da Central de segurança) agora tem disponibilidade geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.assetsViewer ` (Visualizador de recursos da
Central de segurança) agora tem disponibilidade geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.findingSecurityMarksWriter ` (Editor de
descoberta de marcações na Central de segurança) agora tem disponibilidade
geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.findingsEditor ` (Editor de descobertas da
Central de segurança) agora tem disponibilidade geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.findingsStateSetter ` (Definidor de estado de
descobertas da Central de segurança) agora tem disponibilidade geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.findingsViewer ` (Visualizador de descobertas
da Central de segurança) agora tem disponibilidade geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.sourcesAdmin ` (Administrador de fontes da
Central de segurança) agora tem disponibilidade geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.sourcesEditor ` (Editor de fontes da Central de
segurança) agora tem disponibilidade geral.  
  
Security Command Center  |  Agora com disponibilidade geral  |

O papel ` roles/securitycenter.sourcesViewer ` (Visualizador de fontes da
Central de segurança) agora tem disponibilidade geral.  
  
Recommendations AI  |  Adicionado  |  ` automlrecommendations.apiKeys.create `  
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
  
BigQuery  |  Adicionado  |  ` bigquery.models.create `  
` bigquery.models.delete `  
` bigquery.models.getData `  
` bigquery.models.getMetadata `  
` bigquery.models.list `  
` bigquery.models.updateData `  
` bigquery.models.updateMetadata `  
  
Firebase Cloud Messaging  |  Adicionado  |  ` cloudmessaging.messages.create `  
  
Firebase Cloud Messaging  |  Aceito em papéis personalizados  |  `
cloudmessaging.messages.create `  
  
Firebase Cloud Messaging  |  Agora com disponibilidade geral  |  `
cloudmessaging.messages.create `  
  
Security Command Center  |  Agora com disponibilidade geral  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 19 de abril de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram removidas do papel ` roles/editor ` (Editor):

` firebasedynamiclinks.domains.delete `  
  
Security Command Center  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/securitycenter.admin ` (Administrador da Central de segurança):

` securitycenter.findings.setState `  
  
Security Command Center  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/securitycenter.adminEditor ` (Editor administrativo da Central de
segurança):

` securitycenter.findings.setState `  
  
Security Command Center  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/securitycenter.findingsEditor ` (Editor de descobertas da Central de
segurança):

` securitycenter.findings.setState `  
  
Aprovação de acesso  |  Adicionado  |  ` accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
Aprovação de acesso  |  Aceito em papéis personalizados  |  `
accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
Cloud Bigtable  |  Adicionado  |  ` bigtable.locations.list `  
  
Cloud Bigtable  |  Aceito em papéis personalizados  |  `
bigtable.locations.list `  
  
Cloud Bigtable  |  Agora com disponibilidade geral  |  `
bigtable.locations.list `  
  
Cloud Scheduler  |  Adicionado  |  ` cloudscheduler.locations.get `  
` cloudscheduler.locations.list `  
  
Compute Engine  |  Adicionado  |  `
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
  
Compute Engine  |  Aceito em papéis personalizados  |  `
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
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.networkEndpointGroups.attachNetworkEndpoints `  
` compute.networkEndpointGroups.create `  
` compute.networkEndpointGroups.delete `  
` compute.networkEndpointGroups.detachNetworkEndpoints `  
` compute.networkEndpointGroups.get `  
` compute.networkEndpointGroups.getIamPolicy `  
` compute.networkEndpointGroups.list `  
` compute.networkEndpointGroups.setIamPolicy `  
` compute.networkEndpointGroups.use `  
  
Remote Build Execution  |  Adicionado  |  `
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
  
Remote Build Execution  |  Aceito em papéis personalizados  |  `
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
  
Acesso VPC sem servidor  |  Adicionado  |  ` vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  Alterações do Cloud IAM a partir de 29 de março de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/compute.networkUser
` (Usuário de rede do Compute Engine):

` servicenetworking.services.get `  
  
Cloud Monitoring  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/monitoring.admin `
(Administrador do Stackdriver Monitoring):

` serviceusage.services.enable `  
  
Cloud Monitoring  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/monitoring.editor `
(Editor do Stackdriver Monitoring):

` serviceusage.services.enable `  
  
Pacote de operações do Google Cloud  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/stackdriver.accounts.editor ` (Editor de contas do Stackdriver):

` serviceusage.services.enable `  
  
Cloud SQL  |  Adicionado  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  Aceito em papéis personalizados  |  `
cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  Agora com disponibilidade geral  |  `
cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Tradução  |  Adicionado  |  ` cloudtranslate.generalModels.batchPredict `  
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
  
Cloud DNS  |  Adicionado  |  ` dns.networks.targetWithPeeringZone `  
  
Cloud DNS  |  Aceito em papéis personalizados  |  `
dns.networks.targetWithPeeringZone `  
  
Event Threat Detection  |  Adicionado  |  `
threatdetection.detectorSettings.clear `  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  Alterações do Cloud IAM a partir de 22 de março de fevereiro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Talent Solution  |  Agora com disponibilidade geral  |

O papel ` roles/cloudjobdiscovery.admin ` (Administrador) agora tem
disponibilidade geral.  
  
Talent Solution  |  Agora com disponibilidade geral  |

O papel ` roles/cloudjobdiscovery.jobsEditor ` (Editor de jobs) agora tem
disponibilidade geral.  
  
Talent Solution  |  Agora com disponibilidade geral  |

O papel ` roles/cloudjobdiscovery.jobsViewer ` (Visualizador de jobs) agora
tem disponibilidade geral.  
  
Talent Solution  |  Agora com disponibilidade geral  |

O papel ` roles/cloudjobdiscovery.profilesEditor ` (Editor de perfil) agora
tem disponibilidade geral.  
  
Talent Solution  |  Agora com disponibilidade geral  |

O papel ` roles/cloudjobdiscovery.profilesViewer ` (Visualizador de perfis)
agora tem disponibilidade geral.  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/editor ` (Editor):

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Filestore  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/file.editor `
(Editor do Cloud Filestore):

` file.instances.restore `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/owner `
(Proprietário):

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Talent Solution  |  Agora com disponibilidade geral  |  `
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
  
Compute Engine  |  Adicionado  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Filestore  |  Adicionado  |  ` file.instances.restore `  
  
Firebase Authentication  |  Adicionado  |  `
firebaseauth.configs.getHashConfig `  
  
Firebase Authentication  |  Aceito em papéis personalizados  |  `
firebaseauth.configs.getHashConfig `  
  
API Cloud Healthcare  |  Adicionado  |  ` healthcare.datasets.create `  
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
  
  
##  Alterações do Cloud IAM a partir de 15 de março de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Talent Solution  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudjobdiscovery.profilesEditor ` (Editor de perfis):

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Talent Solution  |  Papel atualizado  |

As permissões a seguir foram removidas do papel `
roles/cloudjobdiscovery.profilesEditor ` (Editor de perfis):

` cloudjobdiscovery.companies.create `  
` cloudjobdiscovery.companies.delete `  
` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.companies.update `  
  
Talent Solution  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/cloudjobdiscovery.profilesViewer ` (Visualizador de perfis):

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  Papel atualizado  |

As permissões a seguir foram removidas do papel `
roles/cloudjobdiscovery.profilesViewer ` (Visualizador de perfis):

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/editor ` (Editor):

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/owner `
(Proprietário):

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Storage Transfer Service  |  Agora com disponibilidade geral  |

O papel ` roles/storagetransfer.admin ` (Administrador de transferências de
armazenamento) agora tem disponibilidade geral.  
  
Storage Transfer Service  |  Agora com disponibilidade geral  |

O papel ` roles/storagetransfer.user ` (Usuário de transferências de
armazenamento) agora tem disponibilidade geral.  
  
Storage Transfer Service  |  Agora com disponibilidade geral  |

O papel ` roles/storagetransfer.viewer ` (Visualizador de transferências de
armazenamento) agora tem disponibilidade geral.  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/viewer `
(Visualizador):

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  Adicionado  |  ` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Cloud DNS  |  Agora com disponibilidade geral  |  `
dns.networks.bindPrivateDNSZone `  
  
Cloud Run  |  Adicionado  |  ` run.configurations.get `  
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
  
Cloud Run  |  Não aceito em papéis personalizados  |  ` run.routes.invoke `  
  
Cloud Run  |  Aceito em papéis personalizados  |  ` run.configurations.get `  
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
  
Storage Transfer Service  |  Adicionado  |  ` storagetransfer.jobs.create `  
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
  
Storage Transfer Service  |  Aceito em papéis personalizados  |  `
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
  
Storage Transfer Service  |  Agora com disponibilidade geral  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 7 de março de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
BigQuery  |  Papel adicionado  |

O papel ` roles/bigquery.connectionAdmin ` (Administrador de conexão do
BigQuery) foi adicionado com as seguintes permissões:

` bigquery.connections.create `  
` bigquery.connections.delete `  
` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.setIamPolicy `  
` bigquery.connections.update `  
` bigquery.connections.use `  
  
BigQuery  |  Papel adicionado  |

O papel ` roles/bigquery.connectionUser ` (Usuário de conexão do BigQuery) foi
adicionado com as seguintes permissões:

` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.use `  
  
Dialogflow  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/dialogflow.admin `
(Administrador da API Dialogflow):

` dialogflow.agents.update `  
  
Dialogflow  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/dialogflow.consoleAgentEditor ` (Editor de agente do console do
Dialogflow):

` dialogflow.agents.update `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/editor ` (Editor):

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/file.editor `
(Editor do Cloud Filestore):

` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/file.viewer `
(Visualizador do Cloud Filestore):

` file.snapshots.get `  
` file.snapshots.list `  
  
Cloud Identity and Access Management  |  Agora com disponibilidade geral  |

O papel ` roles/iam.serviceAccountCreator ` (Criar contas de serviço) agora
tem disponibilidade geral.  
  
Cloud Identity and Access Management  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/iam.securityReviewer ` (Avaliador de segurança):

` file.snapshots.list `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/owner `
(Proprietário):

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Service Usage  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/serviceusage.apiKeysAdmin ` (Administrador da API Keys):

` serviceusage.operations.get `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/viewer `
(Visualizador):

` file.snapshots.get `  
` file.snapshots.list `  
  
Serviço de rotulagem de dados do AI Platform  |  Adicionado  |  `
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
  
Serviço de rotulagem de dados do AI Platform  |  Aceito em papéis
personalizados  |  ` datalabeling.annotateddatasets.delete `  
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
  
Dialogflow  |  Adicionado  |  ` dialogflow.agents.update `  
  
Filestore  |  Adicionado  |  ` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
  
##  Alterações do Cloud IAM a partir de 1º de março de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/compute.instanceAdmin.v1 ` (Administrador da instância do Compute Engine
(v1)):

` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Dataproc  |  Papel adicionado  |

O papel ` roles/dataproc.admin ` (Administrador do Dataproc) foi adicionado
com as seguintes permissões:

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
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/editor ` (Editor):

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
Cloud Identity and Access Management  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/iam.serviceAccountDeleter ` (Excluir contas de serviço):

` iam.serviceAccounts.get `  
` iam.serviceAccounts.list `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/viewer `
(Visualizador):

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
AutoML  |  Adicionado  |  ` automl.columnSpecs.get `  
` automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.export `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
AutoML  |  Aceito em papéis personalizados  |  ` automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.deploy `  
` automl.models.export `  
` automl.models.undeploy `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
Compute Engine  |  Adicionado  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  Alterações do Cloud IAM a partir de 15 de fevereiro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Access Context Manager  |  Agora com disponibilidade geral  |

O papel ` roles/accesscontextmanager.policyAdmin ` (Administrador do Access
Context Manager) agora tem disponibilidade geral.  
  
Access Context Manager  |  Agora com disponibilidade geral  |

O papel ` roles/accesscontextmanager.policyEditor ` (Editor do Access Context
Manager) agora tem disponibilidade geral.  
  
Access Context Manager  |  Agora com disponibilidade geral  |

O papel ` roles/accesscontextmanager.policyReader ` (Leitor do Access Context
Manage) agora tem disponibilidade geral.  
  
Talent Solution  |  Papel adicionado  |

O papel ` roles/cloudjobdiscovery.profilesEditor ` (Editor de perfil) foi
adicionado com as seguintes permissões:

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
  
Talent Solution  |  Papel adicionado  |

O papel ` roles/cloudjobdiscovery.profilesViewer ` (Visualizador de perfil)
foi adicionado com as seguintes permissões:

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/editor ` (Editor):

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/owner `
(Proprietário):

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
Papel primário  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel ` roles/viewer `
(Visualizador):

` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
  
Pacote de operações do Google Cloud  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/stackdriver.accounts.editor ` Editor de conta do Stackdriver:

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Pacote de operações do Google Cloud  |  Papel atualizado  |

As seguintes permissões foram adicionadas ao papel `
roles/stackdriver.accounts.viewer ` (Visualizador de contas do Stackdriver):

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Access Context Manager  |  Compatibilidade com papéis personalizados  |  `
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
  
Access Context Manager  |  Agora com disponibilidade geral  |  `
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
  
Talent Solution  |  Adicionado  |  ` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
  
##  Alterações do Cloud IAM a partir de 8 de fevereiro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Security Command Center  |  Aceito em papéis personalizados  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 1º de fevereiro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Dialogflow  |  Agora com disponibilidade geral  |

O papel ` roles/dialogflow.admin ` (Administrador da API Dialogflow) agora tem
disponibilidade geral.  
  
Dialogflow  |  Agora com disponibilidade geral  |

O papel ` roles/dialogflow.client ` (Cliente da API Dialogflow) agora tem
disponibilidade geral.  
  
Dialogflow  |  Agora com disponibilidade geral  |

O papel ` roles/dialogflow.consoleAgentEditor ` (Editor de agente do console
do Dialogflow) agora tem disponibilidade geral.  
  
Dialogflow  |  Agora com disponibilidade geral  |

O papel ` roles/dialogflow.reader ` (Leitor da API Dialogflow) agora tem
disponibilidade geral.  
  
Inventário de recursos do Cloud  |  Adicionado  |  `
cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Inventário de recursos do Cloud  |  Compatibilidade com papéis personalizados
|  ` cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Inventário de recursos do Cloud  |  Agora com disponibilidade geral  |  `
cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Dialogflow  |  Compatibilidade com papéis personalizados  |  `
dialogflow.agents.search `  
` dialogflow.agents.train `  
  
Dialogflow  |  Agora com disponibilidade geral  |  ` dialogflow.agents.export
`  
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
  
  
##  Alterações do Cloud IAM a partir de 25 de janeiro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Adicionado  |  ` compute.instances.updateDisplayDevice `  
  
  
##  Alterações do Cloud IAM a partir de 11 de janeiro de 2019

Serviço  |  Alteração  |  Descrição  
---|---|---  
Identity-Aware Proxy  |  Agora com disponibilidade geral  |

O papel ` roles/iap.admin ` (Administrador de políticas de IAP) agora tem
disponibilidade geral.  
  
Identity-Aware Proxy  |  Aceito em papéis personalizados  |  `
iap.web.getIamPolicy `  
` iap.web.setIamPolicy `  
` iap.webServiceVersions.accessViaIAP `  
` iap.webServiceVersions.getIamPolicy `  
` iap.webServiceVersions.setIamPolicy `  
` iap.webServices.getIamPolicy `  
` iap.webServices.setIamPolicy `  
` iap.webTypes.getIamPolicy `  
` iap.webTypes.setIamPolicy `  
  
  
##  Alterações do Cloud IAM a partir de 21 de dezembro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud DNS  |  Adicionado  |  ` dns.networks.bindPrivateDNSZone `  
  
Cloud DNS  |  Aceito em papéis personalizados  |  `
dns.networks.bindPrivateDNSZone `  
  
  
##  Alterações do Cloud IAM a partir de 14 de dezembro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Firebase Authentication  |  Adicionado  |  ` firebaseauth.configs.create `  
  
Firebase Authentication  |  Aceito em papéis personalizados  |  `
firebaseauth.configs.create `  
  
  
##  Alterações do Cloud IAM a partir de 7 de dezembro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
BigQuery  |  Adicionado  |  ` bigquery.readsessions.create `  
  
BigQuery  |  Aceito em papéis personalizados  |  `
bigquery.readsessions.create `  
  
Google Kubernetes Engine  |  Compatibilidade com papéis personalizados  |  `
container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
Google Kubernetes Engine  |  Agora com disponibilidade geral  |  `
container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  Alterações do Cloud IAM a partir de 30 de novembro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Inventário de recursos do Cloud  |  Agora com disponibilidade geral  |

O papel ` roles/cloudasset.viewer ` (Visualizador de recursos do Cloud) agora
tem disponibilidade geral.  
  
Inventário de recursos do Cloud  |  Agora com disponibilidade geral  |  `
cloudasset.assets.exportAll `  
  
Compute Engine  |  Adicionado  |  ` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
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
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
` compute.subnetworks.getIamPolicy `  
` compute.subnetworks.setIamPolicy `  
  
  
##  Alterações do Cloud IAM a partir de 16 de novembro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
AutoML  |  Adicionado  |  ` automl.locations.getIamPolicy `  
` automl.locations.setIamPolicy `  
  
AutoML  |  Aceito em papéis personalizados  |  ` automl.locations.getIamPolicy
`  
` automl.locations.setIamPolicy `  
  
Talent Solution  |  Adicionado  |  ` cloudjobdiscovery.events.create `  
` cloudjobdiscovery.events.delete `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.events.update `  
  
Compute Engine  |  Adicionado  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Google Kubernetes Engine  |  Adicionado  |  ` container.backendConfigs.create
`  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  Alterações do Cloud IAM a partir de 9 de novembro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Google Analytics  |  Adicionado  |  `
firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
Google Analytics  |  Aceito em papéis personalizados  |  `
firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
  
##  Alterações do Cloud IAM a partir de 2 de novembro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  Aceito em papéis personalizados  |  ` file.instances.create `  
` file.instances.delete `  
` file.instances.get `  
` file.instances.list `  
` file.instances.update `  
` file.locations.get `  
` file.locations.list `  
` file.operations.get `  
` file.operations.list `  
  
Pacote de operações do Google Cloud  |  Adicionado  |  `
stackdriver.resourceMetadata.write `  
  
Pacote de operações do Google Cloud  |  Aceito em papéis personalizados  |  `
stackdriver.resourceMetadata.write `  
  
  
##  Alterações do Cloud IAM a partir de 26 de outubro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
BigQuery  |  Agora com disponibilidade geral  |

O papel ` roles/bigquery.metadataViewer ` (Visualizador de metadados do
BigQuery) agora tem disponibilidade geral.  
  
Cloud Identity and Access Management  |  Agora com disponibilidade geral  |

O papel ` roles/iam.serviceAccountDeleter ` (Excluir contas de serviço) agora
tem disponibilidade geral.  
  
Firebase Realtime Database  |  Adicionado  |  `
firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
Firebase Realtime Database  |  Aceito em papéis personalizados  |  `
firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
Integrações do Firebase com serviços externos  |  Adicionado  |  `
firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
Integrações do Firebase com serviços externos  |  Aceito em papéis
personalizados  |  ` firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
  
##  Alterações do Cloud IAM a partir de 19 de outubro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Suporte do Google Cloud  |  Agora com disponibilidade geral  |

O papel ` roles/cloudsupport.admin ` (Administrador da conta de suporte) agora
tem disponibilidade geral.  
  
Suporte do Google Cloud  |  Agora com disponibilidade geral  |

O papel ` roles/cloudsupport.viewer ` (Visualizador de conta de suporte) agora
tem disponibilidade geral.  
  
Configuração remota do Firebase  |  Adicionado  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Configuração remota do Firebase  |  Aceito em papéis personalizados  |  `
cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Suporte do Google Cloud  |  Aceito em papéis personalizados  |  `
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
  
Suporte do Google Cloud  |  Agora com disponibilidade geral  |  `
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
  
Compute Engine  |  Adicionado  |  ` compute.networks.updatePeering `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.networks.updatePeering `  
  
Firebase Crashlytics  |  Adicionado  |  ` firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase Crashlytics  |  Aceito em papéis personalizados  |  `
firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase Dynamic Links  |  Adicionado  |  `
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
  
Firebase Dynamic Links  |  Aceito em papéis personalizados  |  `
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
  
Mensagens no app Firebase  |  Adicionado  |  `
firebaseinappmessaging.campaigns.create `  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Mensagens no app Firebase  |  Aceito em papéis personalizados  |  `
firebaseinappmessaging.campaigns.create `  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Firebase Cloud Messaging  |  Adicionado  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Cloud Messaging  |  Aceito em papéis personalizados  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Monitoramento de desempenho do Firebase  |  Adicionado  |  `
firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Monitoramento de desempenho do Firebase  |  Aceito em papéis personalizados  |
` firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Previsões  |  Adicionado  |  ` firebasepredictions.predictions.create
`  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
Firebase Previsões  |  Aceito em papéis personalizados  |  `
firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
Security Command Center  |  Adicionado  |  ` securitycenter.assets.get `  
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
  
Gestão de consumidores de serviço  |  Adicionado  |  `
serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
Gestão de consumidores de serviço  |  Compatibilidade com papéis
personalizados  |  ` serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
  
##  Alterações do Cloud IAM a partir de 12 de outubro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.admin ` (Administrador de DLP) agora tem disponibilidade
geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.analyzeRiskTemplatesEditor ` (Editor de modelos de risco
de análise do DLP) agora tem disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.analyzeRiskTemplatesReader ` (Leitor de modelos de risco
de análise do DLP) agora tem disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.deidentifyTemplatesEditor ` (Editor de modelos de
desidentificação do DLP) agora tem disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.deidentifyTemplatesReader ` (Leitor de modelos de
desidentificação do DLP) agora tem disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.inspectTemplatesEditor ` (Editor de modelos de inspeção do
DLP) agora tem disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.inspectTemplatesReader ` (Leitor de modelos de inspeção do
DLP) agora tem disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.jobsEditor ` (Editor de jobs do DLP) agora tem
disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.jobsReader ` (Leitor de jobs do DLP) agora tem
disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.jobTriggersEditor ` (Editor de acionadores de job do DLP)
agora tem disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.jobTriggersReader ` (Leitor de acionadores de job do DLP)
agora tem disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.reader ` (Leitor de DLP) agora tem disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.storedInfoTypesEditor ` (Editor de InfoTypes armazenados
no DLP) agora tem disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.storedInfoTypesReader ` (Leitor de InfoTypes armazenados
no DLP) agora tem disponibilidade geral.  
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|

O papel ` roles/dlp.user ` (Usuário do DLP) agora tem disponibilidade geral.  
  
Google Kubernetes Engine  |  Aceito em papéis personalizados  |  `
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
  
Prevenção contra perda de dados do Cloud  |  Aceito em papéis personalizados
|  ` dlp.analyzeRiskTemplates.create `  
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
  
Prevenção contra perda de dados do Cloud  |  Agora com disponibilidade geral
|  ` dlp.analyzeRiskTemplates.create `  
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
  
Cloud DNS  |  Aceito em papéis personalizados  |  ` dns.dnsKeys.get `  
` dns.dnsKeys.list `  
` dns.managedZoneOperations.get `  
` dns.managedZoneOperations.list `  
` dns.managedZones.update `  
  
Firebase  |  Adicionado  |  ` firebase.billingPlans.get `  
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
  
Firebase  |  Aceito em papéis personalizados  |  ` firebase.billingPlans.get `  
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
  
Teste A/B do Firebase  |  Adicionado  |  ` firebaseabt.experimentresults.get `  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Teste A/B do Firebase  |  Aceito em papéis personalizados  |  `
firebaseabt.experimentresults.get `  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Firebase Authentication  |  Adicionado  |  ` firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Authentication  |  Aceito em papéis personalizados  |  `
firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Realtime Database  |  Adicionado  |  ` firebasedatabase.instances.get
`  
` firebasedatabase.instances.update `  
  
Firebase Realtime Database  |  Aceito em papéis personalizados  |  `
firebasedatabase.instances.get `  
` firebasedatabase.instances.update `  
  
Firebase Hosting  |  Adicionado  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase Hosting  |  Aceito em papéis personalizados  |  `
firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
ML Kit para Firebase  |  Adicionado  |  ` firebaseml.compressionjobs.create `  
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
  
ML Kit para Firebase  |  Aceito em papéis personalizados  |  `
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
  
Regras de segurança do Firebase  |  Adicionado  |  `
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
  
Regras de segurança do Firebase  |  Aceito em papéis personalizados  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 5 de outubro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Adicionado  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.instances.resume `  
` compute.instances.suspend `  
  
Google Kubernetes Engine  |  Compatibilidade com papéis personalizados  |  `
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
  
Google Kubernetes Engine  |  Agora com disponibilidade geral  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 21 de setembro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
AutoML  |  Adicionado  |  ` automl.datasets.getIamPolicy `  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
AutoML  |  Aceito em papéis personalizados  |  ` automl.datasets.getIamPolicy
`  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
Inventário de recursos do Cloud  |  Adicionado  |  `
cloudasset.assets.exportAll `  
  
Inventário de recursos do Cloud  |  Aceito em papéis personalizados  |  `
cloudasset.assets.exportAll `  
  
Compute Engine  |  Adicionado  |  ` compute.licenses.delete `  
  
Google Kubernetes Engine  |  Compatibilidade com papéis personalizados  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 7 de setembro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Memorystore para Redis  |  Aceito em papéis personalizados  |  `
redis.operations.cancel `  
` redis.operations.delete `  
  
  
##  Alterações do Cloud IAM a partir de 31 de agosto de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Google Kubernetes Engine  |  Adicionado  |  ` container.cronJobs.getStatus `  
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
  
Prevenção contra perda de dados do Cloud  |  Adicionado  |  `
dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Prevenção contra perda de dados do Cloud  |  Aceito em papéis personalizados
|  ` dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud Source Repositories  |  Adicionado  |  ` source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud Source Repositories  |  Compatibilidade com papéis personalizados  |  `
source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud Source Repositories  |  Agora com disponibilidade geral  |  `
source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
  
##  Alterações do Cloud IAM a partir de 8 de agosto de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Autorização binária  |  Adicionado  |  `
binaryauthorization.attestors.verifyImageAttested `  
  
Autorização binária  |  Aceito em papéis personalizados  |  `
binaryauthorization.attestors.verifyImageAttested `  
  
Compute Engine  |  Adicionado  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  Adicionado  |  ` file.instances.create `  
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
  
  
##  Alterações do Cloud IAM a partir de 8 de março de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
API Android Management  |  Compatibilidade com papéis personalizados  |  `
androidmanagement.enterprises.manage `  
  
API Android Management  |  Agora com disponibilidade geral  |  `
androidmanagement.enterprises.manage `  
  
Faturamento do Cloud  |  Aceito em papéis personalizados  |  `
billing.resourceCosts.get `  
  
Autorização binária  |  Adicionado  |  ` binaryauthorization.policy.get `  
` binaryauthorization.policy.getIamPolicy `  
` binaryauthorization.policy.setIamPolicy `  
` binaryauthorization.policy.update `  
  
Cloud Composer  |  Agora com disponibilidade geral  |  `
composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
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
  
Google Kubernetes Engine  |  Agora com disponibilidade geral  |  `
container.hostServiceAgent.use `  
  
Memorystore para Redis  |  Adicionado  |  ` redis.operations.cancel `  
  
Memorystore para Redis  |  Aceito em papéis personalizados  |  `
redis.instances.create `  
` redis.instances.delete `  
` redis.instances.get `  
` redis.instances.list `  
` redis.instances.update `  
` redis.locations.get `  
` redis.locations.list `  
` redis.operations.get `  
` redis.operations.list `  
  
Assine com o Google  |  Adicionado  |  `
subscribewithgoogledeveloper.tools.get `  
  
Assine com o Google  |  Aceito em papéis personalizados  |  `
subscribewithgoogledeveloper.tools.get `  
  
  
##  Alterações do Cloud IAM a partir de 20 de julho de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Access Context Manager  |  Adicionado  |  `
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
  
AutoML  |  Adicionado  |  ` automl.annotationSpecs.create `  
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
  
AutoML  |  Aceito em papéis personalizados  |  ` automl.annotationSpecs.create
`  
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
  
Autorização binária  |  Adicionado  |  ` binaryauthorization.attestors.create
`  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
Autorização binária  |  Aceito em papéis personalizados  |  `
binaryauthorization.attestors.create `  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
Cloud DNS  |  Aceito em papéis personalizados  |  ` dns.changes.create `  
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
  
  
##  Alterações do Cloud IAM a partir de 13 de julho de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
BigQuery  |  Adicionado  |  ` bigquery.datasets.getIamPolicy `  
` bigquery.datasets.setIamPolicy `  
  
Datastore  |  Adicionado  |  ` datastore.locations.get `  
` datastore.locations.list `  
  
  
##  Alterações do Cloud IAM a partir de 6 de julho de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud Composer  |  Compatibilidade com papéis personalizados  |  `
composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Endpoints  |  Adicionado  |  ` endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud Endpoints  |  Compatibilidade com papéis personalizados  |  `
endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud TPU  |  Adicionado  |  ` tpu.acceleratortypes.get `  
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
  
Cloud TPU  |  Compatibilidade com papéis personalizados  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 29 de junho de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud Identity and Access Management  |  Agora com disponibilidade geral  |  `
iam.serviceAccounts.implicitDelegation `  
  
  
##  Alterações do Cloud IAM a partir de 15 de junho de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Aceito em papéis personalizados  |  `
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
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.regionBackendServices.create `  
` compute.regionBackendServices.delete `  
` compute.regionBackendServices.get `  
` compute.regionBackendServices.list `  
` compute.regionBackendServices.setSecurityPolicy `  
` compute.regionBackendServices.update `  
` compute.regionBackendServices.use `  
  
  
##  Alterações do Cloud IAM a partir de 8 de junho de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Adicionado  |  ` compute.nodeGroups.addNodes `  
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
  
Compute Engine  |  Aceito em papéis personalizados  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 11 de maio de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
BigQuery  |  Aceito em papéis personalizados  |  ` bigquery.jobs.listAll `  
  
Cloud Bigtable  |  Aceito em papéis personalizados  |  `
bigtable.appProfiles.create `  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.clusters.create `  
` bigtable.clusters.delete `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Bigtable  |  Agora com disponibilidade geral  |  `
bigtable.appProfiles.create `  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Composer  |  Agora Beta  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Life Sciences  |  Aceito em papéis personalizados  |  `
genomics.operations.cancel `  
` genomics.operations.create `  
` genomics.operations.get `  
` genomics.operations.list `  
  
Cloud Monitoring  |  Aceito em papéis personalizados  |  `
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
  
Cloud Monitoring  |  Agora com disponibilidade geral  |  `
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
  
  
##  Alterações do Cloud IAM a partir de 4 de maio de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
BigQuery  |  Disponível em papéis personalizados  |  ` bigquery.jobs.listAll `  
  
Cloud Bigtable  |  Adicionado  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  Aceito em papéis personalizados  |  `
bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  Agora com disponibilidade geral  |  `
bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.oslogin.updateExternalUser `  
  
Gerenciamento de serviços  |  Aceito em papéis personalizados  |  `
servicemanagement.services.bind `  
  
  
##  Alterações do Cloud IAM a partir de 6 de abril de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Aceito em papéis personalizados  |  `
compute.instances.setShieldedVmIntegrityPolicy `  
` compute.instances.updateShieldedVmConfig `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.instances.setShieldedVmIntegrityPolicy `  
  
Google Kubernetes Engine  |  Aceito em papéis personalizados  |  `
container.hostServiceAgent.use `  
  
Dataproc  |  Aceito em papéis personalizados  |  ` dataproc.jobs.getIamPolicy
`  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
Dataproc  |  Agora com disponibilidade geral  |  ` dataproc.jobs.getIamPolicy
`  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
  
##  Alterações do Cloud IAM a partir de 30 de março de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud IoT  |  Agora com disponibilidade geral  |  ` cloudiot.devices.create `  
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
  
  
##  Alterações do Cloud IAM a partir de 23 de março de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud Life Sciences  |  Aceito em papéis personalizados  |  `
genomics.datasets.create `  
` genomics.datasets.delete `  
` genomics.datasets.get `  
` genomics.datasets.getIamPolicy `  
` genomics.datasets.list `  
` genomics.datasets.setIamPolicy `  
` genomics.datasets.update `  
  
Pub/Sub  |  Aceito em papéis personalizados  |  ` pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.list `  
  
  
##  Alterações do Cloud IAM a partir de 9 de março de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Talent Solution  |  Adicionado  |  ` cloudjobdiscovery.companies.create `  
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
  
Talent Solution  |  Aceito em papéis personalizados  |  `
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
  
Cloud Profiler  |  Adicionado  |  ` cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
Cloud Profiler  |  Aceito em papéis personalizados  |  `
cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
  
##  Alterações do Cloud IAM a partir de 2 de março de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Abrir o agente de serviços do Google Cloud  |  Adicionado  |  `
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
  
Abrir o agente de serviços do Google Cloud  |  Aceito em papéis personalizados
|  ` servicebroker.bindingoperations.get `  
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
  
  
##  Alterações do Cloud IAM a partir de 23 de fevereiro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Resource Manager  |  Aceito em papéis personalizados  |  `
resourcemanager.projects.list `  
` resourcemanager.projects.move `  
  
Gerenciamento de serviços  |  Adicionado  |  `
servicemanagement.services.quota `  
  
Gerenciamento de serviços  |  Aceito em papéis personalizados  |  `
servicemanagement.services.quota `  
  
Cloud Source Repositories  |  Compatibilidade com papéis personalizados  |  `
source.repos.create `  
  
  
##  Alterações do Cloud IAM a partir de 16 de fevereiro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
BigQuery  |  Aceito em papéis personalizados  |  ` bigquery.tables.update `  
` bigquery.tables.updateData `  
  
Cloud IoT  |  Aceito em papéis personalizados  |  ` cloudiot.devices.create `  
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
  
Cloud SQL  |  Aceito em papéis personalizados  |  `
cloudsql.instances.demoteMaster `  
  
Suporte do Google Cloud  |  Adicionado  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Compute Engine  |  Adicionado  |  ` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
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
  
Dataproc  |  Aceito em papéis personalizados  |  ` dataproc.agents.create `  
` dataproc.agents.delete `  
` dataproc.agents.get `  
` dataproc.agents.list `  
` dataproc.agents.update `  
` dataproc.tasks.lease `  
` dataproc.tasks.listInvalidatedLeases `  
` dataproc.tasks.reportStatus `  
` dataproc.workflowTemplates.instantiateInline `  
  
Cloud DNS  |  Adicionado  |  ` dns.changes.create `  
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
  
  
##  Alterações do Cloud IAM a partir de 2 de fevereiro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Disponível em papéis personalizados  |  `
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
  
Prevenção contra perda de dados do Cloud  |  Adicionado  |  `
dlp.jobTriggers.create `  
` dlp.jobTriggers.delete `  
` dlp.jobTriggers.get `  
` dlp.jobTriggers.list `  
` dlp.jobTriggers.update `  
  
  
##  Alterações do Cloud IAM a partir de 26 de janeiro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
BigQuery  |  Adicionado  |  ` bigquery.jobs.listAll `  
  
Google Kubernetes Engine  |  Adicionado  |  `
container.podSecurityPolicies.create `  
` container.podSecurityPolicies.delete `  
` container.podSecurityPolicies.get `  
` container.podSecurityPolicies.list `  
` container.podSecurityPolicies.update `  
` container.podSecurityPolicies.use `  
  
  
##  Alterações do Cloud IAM a partir de 19 de janeiro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Adicionado  |  ` compute.addresses.createInternal `  
` compute.addresses.deleteInternal `  
` compute.addresses.useInternal `  
  
  
##  Alterações do Cloud IAM a partir de 12 de janeiro de 2018

Serviço  |  Alteração  |  Descrição  
---|---|---  
App Engine  |  Não aceito em papéis personalizados  |  `
appengine.runtimes.actAsAdmin `  
  
Compute Engine  |  Adicionado  |  ` compute.backendServices.setSecurityPolicy
`  
` compute.securityPolicies.create `  
` compute.securityPolicies.delete `  
` compute.securityPolicies.get `  
` compute.securityPolicies.getIamPolicy `  
` compute.securityPolicies.list `  
` compute.securityPolicies.setIamPolicy `  
` compute.securityPolicies.update `  
` compute.securityPolicies.use `  
  
Compute Engine  |  Não aceito em papéis personalizados  |  `
compute.organizations.administerXpn `  
` compute.targetHttpProxies.create `  
` compute.targetHttpProxies.setUrlMap `  
` compute.targetHttpsProxies.create `  
` compute.targetHttpsProxies.setUrlMap `  
` compute.targetSslProxies.create `  
` compute.targetSslProxies.setBackendService `  
` compute.targetTcpProxies.create `  
` compute.targetTcpProxies.update `  
  
Compute Engine  |  Agora com disponibilidade geral  |  `
compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
  
  
##  Alterações do Cloud IAM a partir de 22 de dezembro de 2017

Serviço  |  Alteração  |  Descrição  
---|---|---  
App Engine  |  Aceito em papéis personalizados  |  `
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
  
App Engine  |  Não aceito em papéis personalizados  |  `
appengine.applications.list `  
` appengine.operations.cancel `  
` appengine.operations.delete `  
` appengine.services.create `  
  
Faturamento do Cloud  |  Aceito em papéis personalizados  |  `
billing.accounts.close `  
` billing.accounts.reopen `  
` billing.budgets.delete `  
` billing.budgets.update `  
  
Cloud Debugger  |  Aceito em papéis personalizados  |  `
clouddebugger.breakpoints.create `  
` clouddebugger.breakpoints.delete `  
` clouddebugger.breakpoints.get `  
` clouddebugger.breakpoints.list `  
` clouddebugger.breakpoints.listActive `  
` clouddebugger.breakpoints.update `  
` clouddebugger.debuggees.create `  
` clouddebugger.debuggees.list `  
  
Cloud Key Management Service  |  Aceito em papéis personalizados  |  `
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
  
Cloud SQL  |  Aceito em papéis personalizados  |  ` cloudsql.backupRuns.create
`  
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
  
Cloud SQL  |  Não aceito em papéis personalizados  |  `
cloudsql.databases.getIamPolicy `  
` cloudsql.databases.setIamPolicy `  
` cloudsql.instances.demoteMaster `  
` cloudsql.instances.getIamPolicy `  
` cloudsql.instances.migrate `  
` cloudsql.instances.setIamPolicy `  
` cloudsql.sslCerts.createEphemeral `  
  
Cloud Trace  |  Aceito em papéis personalizados  |  ` cloudtrace.insights.get
`  
` cloudtrace.insights.list `  
` cloudtrace.stats.get `  
` cloudtrace.tasks.create `  
` cloudtrace.tasks.delete `  
` cloudtrace.tasks.get `  
` cloudtrace.tasks.list `  
` cloudtrace.traces.get `  
` cloudtrace.traces.list `  
` cloudtrace.traces.patch `  
  
Compute Engine  |  Adicionado  |  ` compute.instances.setMachineResources `  
` compute.instances.setMinCpuPlatform `  
` compute.instances.setServiceAccount `  
` compute.instances.updateAccessConfig `  
` compute.instances.updateNetworkInterface `  
` compute.licenseCodes.get `  
` compute.licenseCodes.list `  
` compute.licenseCodes.update `  
` compute.licenseCodes.use `  
  
Compute Engine  |  Aceito em papéis personalizados  |  `
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
  
Compute Engine  |  Não aceito em papéis personalizados  |  `
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
  
Google Kubernetes Engine  |  Adicionado  |  ` container.services.updateStatus
`  
  
Google Kubernetes Engine  |  Aceito em papéis personalizados  |  `
container.clusters.create `  
` container.clusters.delete `  
` container.clusters.get `  
` container.clusters.getCredentials `  
` container.clusters.list `  
` container.clusters.update `  
` container.operations.get `  
` container.operations.list `  
  
Dataproc  |  Aceito em papéis personalizados  |  ` dataproc.clusters.create `  
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
  
Datastore  |  Não aceito em papéis personalizados  |  `
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
  
Cloud Deployment Manager  |  Compatibilidade com papéis personalizados  |  `
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
  
Dialogflow  |  Aceito em papéis personalizados  |  ` dialogflow.agents.export
`  
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
  
Error Reporting  |  Aceito em papéis personalizados  |  `
errorreporting.applications.list `  
` errorreporting.errorEvents.create `  
` errorreporting.errorEvents.delete `  
` errorreporting.errorEvents.list `  
` errorreporting.groupMetadata.get `  
` errorreporting.groupMetadata.update `  
` errorreporting.groups.list `  
  
Cloud Identity and Access Management  |  Não aceito em papéis personalizados
|  ` iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
Cloud Logging  |  Aceito em papéis personalizados  |  `
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
  
AI Platform  |  Aceito em papéis personalizados  |  ` ml.jobs.cancel `  
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
  
Cloud Monitoring  |  Aceito em papéis personalizados  |  `
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
  
Pub/Sub  |  Aceito em papéis personalizados  |  ` pubsub.topics.setIamPolicy `  
  
Gerenciamento de serviços  |  Aceito em papéis personalizados  |  `
servicemanagement.services.check `  
` servicemanagement.services.report `  
  
Gerenciamento de serviços  |  Não aceito em papéis personalizados  |  `
servicemanagement.consumerSettings.get `  
` servicemanagement.consumerSettings.getIamPolicy `  
` servicemanagement.consumerSettings.list `  
` servicemanagement.consumerSettings.setIamPolicy `  
` servicemanagement.consumerSettings.update `  
  
Cloud Source Repositories  |  Compatibilidade com papéis personalizados  |  `
source.repos.delete `  
` source.repos.get `  
` source.repos.getIamPolicy `  
` source.repos.list `  
` source.repos.setIamPolicy `  
  
Cloud Source Repositories  |  Não aceito em papéis personalizados  |  `
source.repos.update `  
  
Cloud Spanner  |  Compatibilidade com papéis personalizados  |  `
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
  
Cloud Spanner  |  Não aceito em papéis personalizados  |  `
spanner.databaseOperations.delete `  
` spanner.databases.update `  
  
Cloud Storage  |  Aceito em papéis personalizados  |  ` storage.buckets.create
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
  
  
##  Alterações do Cloud IAM a partir de 8 de dezembro de 2017

Serviço  |  Alteração  |  Descrição  
---|---|---  
BigQuery  |  Aceito em papéis personalizados  |  ` bigquery.datasets.create `  
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
  
BigQuery  |  Não aceito em papéis personalizados  |  ` bigquery.config.get `  
` bigquery.config.update `  
` bigquery.service.actAsSuperuser `  
` bigquery.tables.update `  
` bigquery.tables.updateData `  
` bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Cloud Bigtable  |  Aceito em papéis personalizados  |  ` bigtable.clusters.get
`  
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
  
Compute Engine  |  Adicionado  |  ` compute.disks.getIamPolicy `  
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
  
Dataflow  |  Aceito em papéis personalizados  |  ` dataflow.jobs.cancel `  
` dataflow.jobs.create `  
` dataflow.jobs.get `  
` dataflow.jobs.list `  
` dataflow.jobs.updateContents `  
` dataflow.messages.list `  
` dataflow.metrics.get `  
  
Dataproc  |  Adicionado  |  ` dataproc.workflowTemplates.instantiateInline `  
  
Prevenção contra perda de dados do Cloud  |  Adicionado  |  `
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
  
Pub/Sub  |  Adicionado  |  ` pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.get `  
` pubsub.snapshots.getIamPolicy `  
` pubsub.snapshots.list `  
` pubsub.snapshots.seek `  
` pubsub.snapshots.setIamPolicy `  
` pubsub.snapshots.update `  
  
Pub/Sub  |  Aceito em papéis personalizados  |  ` pubsub.subscriptions.consume
`  
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
  
  
##  Alterações do Cloud IAM a partir de 1º de dezembro de 2017

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud Build  |  Aceito em papéis personalizados  |  ` cloudbuild.builds.create
`  
` cloudbuild.builds.get `  
` cloudbuild.builds.list `  
` cloudbuild.builds.update `  
  
Cloud Tool Results  |  Agora com disponibilidade geral  |  `
cloudtoolresults.executions.create `  
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
  
Compute Engine  |  Agora com disponibilidade geral  |  `
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
  
Google Kubernetes Engine  |  Adicionado  |  `
container.initializerConfigurations.create `  
` container.initializerConfigurations.delete `  
` container.initializerConfigurations.get `  
` container.initializerConfigurations.list `  
` container.initializerConfigurations.update `  
` container.pods.initialize `  
  
Google Kubernetes Engine  |  Agora com disponibilidade geral  |  `
container.deployments.getScale `  
` container.deployments.updateScale `  
  
Dataprep da Trifacta  |  Aceito em papéis personalizados  |  `
dataprep.projects.use `  
  
Cloud Identity and Access Management  |  Compatibilidade com papéis
personalizados  |  ` iam.roles.create `  
` iam.roles.delete `  
` iam.roles.get `  
` iam.roles.list `  
` iam.roles.undelete `  
` iam.roles.update `  
  
  
##  Alterações do Cloud IAM a partir de 11 de novembro de 2017

Serviço  |  Alteração  |  Descrição  
---|---|---  
Google Kubernetes Engine  |  Adicionado  |  ` container.clusters.getIamPolicy
`  
` container.clusters.setIamPolicy `  
  
AI Platform  |  Adicionado  |  ` ml.locations.get `  
` ml.locations.list `  
  
Cloud Monitoring  |  Adicionado  |  ` monitoring.metricDescriptors.update `  
  
  
##  Alterações do Cloud IAM a partir de 27 de outubro de 2017

Serviço  |  Alteração  |  Descrição  
---|---|---  
Compute Engine  |  Adicionado  |  ` compute.instances.updateShieldedVmConfig `  
  
Identity-Aware Proxy  |  Adicionado  |  ` iap.web.getIamPolicy `  
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
  
Gerenciamento de serviços  |  Aceito em papéis personalizados  |  `
servicemanagement.services.create `  
` servicemanagement.services.delete `  
` servicemanagement.services.get `  
` servicemanagement.services.getIamPolicy `  
` servicemanagement.services.list `  
` servicemanagement.services.setIamPolicy `  
` servicemanagement.services.update `  
  
  
##  Alterações do Cloud IAM a partir de 6 de outubro de 2017

Serviço  |  Alteração  |  Descrição  
---|---|---  
Dataproc  |  Agora com disponibilidade geral  |  `
dataproc.workflowTemplates.create `  
` dataproc.workflowTemplates.delete `  
` dataproc.workflowTemplates.get `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.instantiate `  
` dataproc.workflowTemplates.list `  
` dataproc.workflowTemplates.setIamPolicy `  
` dataproc.workflowTemplates.update `  
  
  
##  Alterações do Cloud IAM a partir de 22 de setembro de 2017

Serviço  |  Alteração  |  Descrição  
---|---|---  
App Engine  |  Adicionado  |  ` appengine.memcache.addKey `  
` appengine.memcache.flush `  
` appengine.memcache.get `  
` appengine.memcache.getKey `  
` appengine.memcache.list `  
` appengine.memcache.update `  
  
Cloud SQL  |  Adicionado  |  ` cloudsql.instances.demoteMaster `  
  
Cloud SQL  |  Agora com disponibilidade geral  |  `
cloudsql.instances.demoteMaster `  
  
  
##  Alterações do Cloud IAM a partir de 8 de setembro de 2017

Serviço  |  Alteração  |  Descrição  
---|---|---  
Cloud Functions  |  Adicionado  |  ` cloudfunctions.functions.call `  
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
  
Compute Engine  |  Adicionado  |  ` compute.instances.setDeletionProtection `  
` compute.targetHttpsProxies.setUrlMap `  
  
Google Kubernetes Engine  |  Adicionado  |  ` container.statefulSets.getScale
`  
` container.statefulSets.updateScale `  
  
Google Kubernetes Engine  |  Agora com disponibilidade geral  |  `
container.statefulSets.getScale `  
` container.statefulSets.updateScale `  
  
Cloud Functions  |  Adicionado  |  ` dlp.kms.encrypt `  
` dlp.riskAnalysisOperations.cancel `  
` dlp.riskAnalysisOperations.create `  
` dlp.riskAnalysisOperations.get `  
` dlp.riskAnalysisOperations.list `  

