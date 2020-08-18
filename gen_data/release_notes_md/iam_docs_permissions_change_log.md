#  IAM permissions change log

This page describes changes to the public IAM permissions for all Generally
Available and Beta services on Google Cloud. This change log can help you
maintain and troubleshoot your [ custom roles ](/iam/docs/understanding-
custom-roles) .

When a permission is retired or is no longer supported in custom roles, IAM
automatically removes the permission from your custom roles. In contrast, when
a permission is added, IAM _does not_ automatically add the permission to your
custom roles.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/cloud-iam-permissions-change-
log.xml `

##  Upcoming Cloud IAM changes for the week of 2020-08-17

Service  |  Change  |  Description  
---|---|---  
Dialogflow  |  Role Updated  |

The following permissions have been added to the role ` roles/dialogflow.admin
` (Dialogflow API Admin):

` dialogflow.environments.lookupHistory `  
` dialogflow.versions.load `  
  
Dialogflow  |  Role Updated  |

The following permissions have been added to the role `
roles/dialogflow.consoleAgentEditor ` (Dialogflow Console Agent Editor):

` dialogflow.environments.lookupHistory `  
` dialogflow.versions.load `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/editor `
(Editor):

` dialogflow.environments.lookupHistory `  
` dialogflow.versions.load `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/owner ` (Owner):

` dialogflow.environments.lookupHistory `  
` dialogflow.versions.load `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/viewer `
(Viewer):

` dialogflow.environments.lookupHistory `  
  
Apigee API  |  Added  |  ` apigee.caches.delete `  
` apigee.caches.list `  
` apigee.canaryevaluations.create `  
` apigee.canaryevaluations.get `  
` apigee.datacollectors.create `  
` apigee.datacollectors.delete `  
` apigee.datacollectors.get `  
` apigee.datacollectors.list `  
` apigee.datacollectors.update `  
` apigee.datastores.create `  
` apigee.datastores.delete `  
` apigee.datastores.get `  
` apigee.datastores.list `  
` apigee.datastores.update `  
` apigee.envgroupattachments.create `  
` apigee.envgroupattachments.delete `  
` apigee.envgroupattachments.get `  
` apigee.envgroupattachments.list `  
` apigee.envgroups.create `  
` apigee.envgroups.delete `  
` apigee.envgroups.get `  
` apigee.envgroups.list `  
` apigee.envgroups.update `  
` apigee.exports.create `  
` apigee.exports.get `  
` apigee.exports.list `  
` apigee.hostqueries.create `  
` apigee.hostqueries.get `  
` apigee.hostqueries.list `  
` apigee.hoststats.get `  
` apigee.ingressconfigs.get `  
` apigee.instanceattachments.create `  
` apigee.instanceattachments.delete `  
` apigee.instanceattachments.get `  
` apigee.instanceattachments.list `  
` apigee.instances.create `  
` apigee.instances.delete `  
` apigee.instances.get `  
` apigee.instances.list `  
` apigee.instances.reportStatus `  
` apigee.operations.get `  
` apigee.operations.list `  
` apigee.projects.update `  
  
Apigee API  |  Supported In Custom Roles  |  ` apigee.datastores.create `  
` apigee.datastores.delete `  
` apigee.datastores.get `  
` apigee.datastores.list `  
` apigee.datastores.update `  
` apigee.exports.create `  
` apigee.exports.get `  
` apigee.exports.list `  
  
Apigee API  |  Now GA  |  ` apigee.caches.delete `  
` apigee.caches.list `  
` apigee.canaryevaluations.create `  
` apigee.canaryevaluations.get `  
` apigee.datacollectors.create `  
` apigee.datacollectors.delete `  
` apigee.datacollectors.get `  
` apigee.datacollectors.list `  
` apigee.datacollectors.update `  
` apigee.datastores.create `  
` apigee.datastores.delete `  
` apigee.datastores.get `  
` apigee.datastores.list `  
` apigee.datastores.update `  
` apigee.envgroupattachments.create `  
` apigee.envgroupattachments.delete `  
` apigee.envgroupattachments.get `  
` apigee.envgroupattachments.list `  
` apigee.envgroups.create `  
` apigee.envgroups.delete `  
` apigee.envgroups.get `  
` apigee.envgroups.list `  
` apigee.envgroups.update `  
` apigee.exports.create `  
` apigee.exports.get `  
` apigee.exports.list `  
` apigee.hostqueries.create `  
` apigee.hostqueries.get `  
` apigee.hostqueries.list `  
` apigee.hoststats.get `  
` apigee.ingressconfigs.get `  
` apigee.instanceattachments.create `  
` apigee.instanceattachments.delete `  
` apigee.instanceattachments.get `  
` apigee.instanceattachments.list `  
` apigee.instances.create `  
` apigee.instances.delete `  
` apigee.instances.get `  
` apigee.instances.list `  
` apigee.instances.reportStatus `  
` apigee.operations.get `  
` apigee.operations.list `  
` apigee.projects.update `  
  
Compute Engine  |  Now GA  |  ` compute.images.update `  
  
Dialogflow  |  Added  |  ` dialogflow.agents.list `  
` dialogflow.agents.validate `  
` dialogflow.environments.create `  
` dialogflow.environments.delete `  
` dialogflow.environments.get `  
` dialogflow.environments.getHistory `  
` dialogflow.environments.list `  
` dialogflow.environments.lookupHistory `  
` dialogflow.environments.update `  
` dialogflow.flows.create `  
` dialogflow.flows.delete `  
` dialogflow.flows.get `  
` dialogflow.flows.list `  
` dialogflow.flows.train `  
` dialogflow.flows.update `  
` dialogflow.flows.validate `  
` dialogflow.pages.create `  
` dialogflow.pages.delete `  
` dialogflow.pages.get `  
` dialogflow.pages.list `  
` dialogflow.pages.update `  
` dialogflow.transitionRouteGroups.create `  
` dialogflow.transitionRouteGroups.delete `  
` dialogflow.transitionRouteGroups.get `  
` dialogflow.transitionRouteGroups.list `  
` dialogflow.transitionRouteGroups.update `  
` dialogflow.versions.create `  
` dialogflow.versions.delete `  
` dialogflow.versions.get `  
` dialogflow.versions.list `  
` dialogflow.versions.load `  
` dialogflow.versions.update `  
` dialogflow.webhooks.create `  
` dialogflow.webhooks.delete `  
` dialogflow.webhooks.get `  
` dialogflow.webhooks.list `  
` dialogflow.webhooks.update `  
  
Dialogflow  |  Supported In Custom Roles  |  ` dialogflow.environments.create
`  
` dialogflow.environments.delete `  
` dialogflow.environments.get `  
` dialogflow.environments.getHistory `  
` dialogflow.environments.list `  
` dialogflow.environments.update `  
` dialogflow.versions.create `  
` dialogflow.versions.delete `  
` dialogflow.versions.get `  
` dialogflow.versions.list `  
` dialogflow.versions.update `  
  
Dialogflow  |  Now GA  |  ` dialogflow.agents.list `  
` dialogflow.agents.validate `  
` dialogflow.environments.create `  
` dialogflow.environments.delete `  
` dialogflow.environments.get `  
` dialogflow.environments.getHistory `  
` dialogflow.environments.list `  
` dialogflow.environments.update `  
` dialogflow.flows.create `  
` dialogflow.flows.delete `  
` dialogflow.flows.get `  
` dialogflow.flows.list `  
` dialogflow.flows.train `  
` dialogflow.flows.update `  
` dialogflow.flows.validate `  
` dialogflow.pages.create `  
` dialogflow.pages.delete `  
` dialogflow.pages.get `  
` dialogflow.pages.list `  
` dialogflow.pages.update `  
` dialogflow.transitionRouteGroups.create `  
` dialogflow.transitionRouteGroups.delete `  
` dialogflow.transitionRouteGroups.get `  
` dialogflow.transitionRouteGroups.list `  
` dialogflow.transitionRouteGroups.update `  
` dialogflow.versions.create `  
` dialogflow.versions.delete `  
` dialogflow.versions.get `  
` dialogflow.versions.list `  
` dialogflow.versions.update `  
` dialogflow.webhooks.create `  
` dialogflow.webhooks.delete `  
` dialogflow.webhooks.get `  
` dialogflow.webhooks.list `  
` dialogflow.webhooks.update `  
  
Cloud Healthcare API  |  Added  |  ` healthcare.annotationStores.create `  
` healthcare.annotationStores.delete `  
` healthcare.annotationStores.evaluate `  
` healthcare.annotationStores.export `  
` healthcare.annotationStores.get `  
` healthcare.annotationStores.getIamPolicy `  
` healthcare.annotationStores.import `  
` healthcare.annotationStores.list `  
` healthcare.annotationStores.setIamPolicy `  
` healthcare.annotationStores.update `  
` healthcare.annotations.create `  
` healthcare.annotations.delete `  
` healthcare.annotations.get `  
` healthcare.annotations.list `  
` healthcare.annotations.update `  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `
healthcare.annotationStores.create `  
` healthcare.annotationStores.delete `  
` healthcare.annotationStores.evaluate `  
` healthcare.annotationStores.export `  
` healthcare.annotationStores.get `  
` healthcare.annotationStores.getIamPolicy `  
` healthcare.annotationStores.import `  
` healthcare.annotationStores.list `  
` healthcare.annotationStores.setIamPolicy `  
` healthcare.annotationStores.update `  
` healthcare.annotations.create `  
` healthcare.annotations.delete `  
` healthcare.annotations.get `  
` healthcare.annotations.list `  
` healthcare.annotations.update `  
  
  
##  Cloud IAM changes as of 2020-08-14

Service  |  Change  |  Description  
---|---|---  
Private Catalog  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudprivatecatalog.consumer ` (Catalog Consumer):

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Private Catalog  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudprivatecatalogproducer.admin ` (Catalog Admin):

` cloudprivatecatalog.targets.get `  
` cloudprivatecatalogproducer.targets.associate `  
` cloudprivatecatalogproducer.targets.unassociate `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Private Catalog  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudprivatecatalogproducer.manager ` (Catalog Manager):

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Dialogflow  |  Added  |  ` dialogflow.fulfillments.get `  
` dialogflow.fulfillments.update `  
  
Dialogflow  |  Now GA  |  ` dialogflow.fulfillments.get `  
` dialogflow.fulfillments.update `  
  
  
##  Cloud IAM changes as of 2020-08-07

Service  |  Change  |  Description  
---|---|---  
Cloud Composer  |  Role Updated  |

The following permissions have been added to the role ` roles/composer.worker
` (Composer Worker):

` artifactregistry.packages.delete `  
` artifactregistry.repositories.create `  
` artifactregistry.repositories.delete `  
` artifactregistry.repositories.deleteArtifacts `  
` artifactregistry.repositories.getIamPolicy `  
` artifactregistry.repositories.setIamPolicy `  
` artifactregistry.repositories.update `  
` artifactregistry.tags.delete `  
` artifactregistry.versions.delete `  
  
GKE Hub  |  Role Updated  |

The following permissions have been added to the role ` roles/gkehub.viewer `
(GKE Hub Viewer):

` gkehub.features.getIamPolicy `  
` gkehub.gateway.get `  
` gkehub.gateway.getIamPolicy `  
  
Cloud Logging  |  Now GA  |

The role ` roles/logging.bucketWriter ` (Logs Bucket Writer) is now GA.  
  
Cloud Logging  |  Now GA  |

The role ` roles/logging.viewAccessor ` (Logs View Accessor) is now GA.  
  
Cloud Logging  |  Role Updated  |

The following permissions have been added to the role `
roles/logging.privateLogViewer ` (Private Logs Viewer):

` logging.views.access `  
  
Compute Engine  |  Now GA  |  ` compute.instances.getScreenshot `  
  
Identity and Access Management  |  Supported In Custom Roles  |  `
iam.serviceAccounts.disable `  
` iam.serviceAccounts.enable `  
` iam.serviceAccounts.undelete `  
  
Identity and Access Management  |  Now GA  |  ` iam.serviceAccounts.disable `  
` iam.serviceAccounts.enable `  
` iam.serviceAccounts.undelete `  
  
Cloud Logging  |  Added  |  ` logging.buckets.create `  
` logging.buckets.delete `  
` logging.buckets.undelete `  
` logging.buckets.write `  
` logging.views.access `  
  
Cloud Logging  |  Supported In Custom Roles  |  ` logging.buckets.create `  
` logging.buckets.delete `  
` logging.buckets.undelete `  
` logging.buckets.write `  
` logging.views.access `  
  
Cloud Logging  |  Now GA  |  ` logging.buckets.create `  
` logging.buckets.delete `  
` logging.buckets.undelete `  
` logging.buckets.write `  
` logging.views.access `  
  
OAuthConfig  |  Added  |  ` oauthconfig.clientpolicy.get `  
` oauthconfig.testusers.get `  
` oauthconfig.testusers.update `  
` oauthconfig.verification.get `  
` oauthconfig.verification.submit `  
` oauthconfig.verification.update `  
  
OAuthConfig  |  Supported In Custom Roles  |  ` oauthconfig.clientpolicy.get `  
` oauthconfig.testusers.get `  
` oauthconfig.testusers.update `  
` oauthconfig.verification.get `  
` oauthconfig.verification.submit `  
` oauthconfig.verification.update `  
  
OAuthPolicyMetadata  |  Added  |  `
oauthpolicymetadata.brandpolicy.createOrUpdate `  
` oauthpolicymetadata.brandpolicy.get `  
` oauthpolicymetadata.brandpolicy.submitVerification `  
` oauthpolicymetadata.clientpolicy.get `  
  
OAuthPolicyMetadata  |  Supported In Custom Roles  |  `
oauthpolicymetadata.brandpolicy.createOrUpdate `  
` oauthpolicymetadata.brandpolicy.get `  
` oauthpolicymetadata.brandpolicy.submitVerification `  
` oauthpolicymetadata.clientpolicy.get `  
  
OAuthTestApp  |  Added  |  ` oauthtestapp.userwhitelist.read `  
` oauthtestapp.userwhitelist.write `  
  
OAuthTestApp  |  Supported In Custom Roles  |  `
oauthtestapp.userwhitelist.read `  
` oauthtestapp.userwhitelist.write `  
  
Certificate Authority Service  |  Added  |  `
privateca.certificateAuthorities.create `  
` privateca.certificateAuthorities.delete `  
` privateca.certificateAuthorities.get `  
` privateca.certificateAuthorities.getIamPolicy `  
` privateca.certificateAuthorities.list `  
` privateca.certificateAuthorities.setIamPolicy `  
` privateca.certificateAuthorities.update `  
` privateca.certificateRevocationLists.create `  
` privateca.certificateRevocationLists.get `  
` privateca.certificateRevocationLists.getIamPolicy `  
` privateca.certificateRevocationLists.list `  
` privateca.certificateRevocationLists.setIamPolicy `  
` privateca.certificateRevocationLists.update `  
` privateca.certificates.create `  
` privateca.certificates.get `  
` privateca.certificates.getIamPolicy `  
` privateca.certificates.list `  
` privateca.certificates.setIamPolicy `  
` privateca.certificates.update `  
` privateca.locations.get `  
` privateca.locations.list `  
` privateca.operations.cancel `  
` privateca.operations.delete `  
` privateca.operations.get `  
` privateca.operations.list `  
` privateca.reusableConfigs.create `  
` privateca.reusableConfigs.delete `  
` privateca.reusableConfigs.get `  
` privateca.reusableConfigs.getIamPolicy `  
` privateca.reusableConfigs.list `  
` privateca.reusableConfigs.setIamPolicy `  
` privateca.reusableConfigs.update `  
  
Certificate Authority Service  |  Supported In Custom Roles  |  `
privateca.certificateAuthorities.create `  
` privateca.certificateAuthorities.delete `  
` privateca.certificateAuthorities.get `  
` privateca.certificateAuthorities.getIamPolicy `  
` privateca.certificateAuthorities.list `  
` privateca.certificateAuthorities.setIamPolicy `  
` privateca.certificateAuthorities.update `  
` privateca.certificateRevocationLists.create `  
` privateca.certificateRevocationLists.get `  
` privateca.certificateRevocationLists.getIamPolicy `  
` privateca.certificateRevocationLists.list `  
` privateca.certificateRevocationLists.setIamPolicy `  
` privateca.certificateRevocationLists.update `  
` privateca.certificates.create `  
` privateca.certificates.get `  
` privateca.certificates.getIamPolicy `  
` privateca.certificates.list `  
` privateca.certificates.setIamPolicy `  
` privateca.certificates.update `  
` privateca.locations.get `  
` privateca.locations.list `  
` privateca.operations.cancel `  
` privateca.operations.delete `  
` privateca.operations.get `  
` privateca.operations.list `  
` privateca.reusableConfigs.create `  
` privateca.reusableConfigs.delete `  
` privateca.reusableConfigs.get `  
` privateca.reusableConfigs.getIamPolicy `  
` privateca.reusableConfigs.list `  
` privateca.reusableConfigs.setIamPolicy `  
` privateca.reusableConfigs.update `  
  
Recommender  |  Added  |  ` recommender.commitmentUtilizationInsights.get `  
` recommender.commitmentUtilizationInsights.list `  
` recommender.commitmentUtilizationInsights.update `  
` recommender.usageCommitmentRecommendations.get `  
` recommender.usageCommitmentRecommendations.list `  
` recommender.usageCommitmentRecommendations.update `  
  
  
##  Cloud IAM changes as of 2020-07-31

Service  |  Change  |  Description  
---|---|---  
Apigee API  |  Now GA  |

The role ` roles/apigee.admin ` (Apigee Organization Admin) is now GA.  
  
Apigee API  |  Now GA  |

The role ` roles/apigee.analyticsAgent ` (Apigee Analytics Agent) is now GA.  
  
Apigee API  |  Now GA  |

The role ` roles/apigee.analyticsEditor ` (Apigee Analytics Editor) is now GA.  
  
Apigee API  |  Now GA  |

The role ` roles/apigee.analyticsViewer ` (Apigee Analytics Viewer) is now GA.  
  
Apigee API  |  Now GA  |

The role ` roles/apigee.apiCreator ` (Apigee API Creator) is now GA.  
  
Apigee API  |  Now GA  |

The role ` roles/apigee.deployer ` (Apigee Deployer) is now GA.  
  
Apigee API  |  Now GA  |

The role ` roles/apigee.developerAdmin ` (Apigee Developer Admin) is now GA.  
  
Apigee API  |  Now GA  |

The role ` roles/apigee.readOnlyAdmin ` (Apigee Read-only Admin) is now GA.  
  
Apigee API  |  Now GA  |

The role ` roles/apigee.runtimeAgent ` (Apigee Runtime Agent) is now GA.  
  
Apigee API  |  Now GA  |

The role ` roles/apigee.synchronizerManager ` (Apigee Synchronizer Manager) is
now GA.  
  
Apigee Connect  |  Now GA  |

The role ` roles/apigeeconnect.Admin ` (Apigee Connect Admin) is now GA.  
  
Apigee Connect  |  Now GA  |

The role ` roles/apigeeconnect.Agent ` (Apigee Connect Agent) is now GA.  
  
Google Cloud Game Servers  |  Now GA  |

The role ` roles/gameservices.admin ` (Game Services API Admin) is now GA.  
  
Google Cloud Game Servers  |  Now GA  |

The role ` roles/gameservices.viewer ` (Game Services API Viewer) is now GA.  
  
Identity and Access Management  |  Role Updated  |

The following permissions have been removed from the role `
roles/iam.securityAdmin ` (Security Admin):

` container.secrets.list `  
  
Identity and Access Management  |  Role Updated  |

The following permissions have been removed from the role `
roles/iam.securityReviewer ` (Security Reviewer):

` container.secrets.list `  
  
AI Platform Notebooks  |  Role Updated  |

The following permissions have been added to the role ` roles/notebooks.admin
` (Notebooks Admin):

` compute.acceleratorTypes.get `  
` compute.addresses.get `  
` compute.addresses.list `  
` compute.autoscalers.get `  
` compute.autoscalers.list `  
` compute.backendBuckets.get `  
` compute.backendBuckets.list `  
` compute.backendServices.get `  
` compute.backendServices.list `  
` compute.commitments.get `  
` compute.commitments.list `  
` compute.diskTypes.get `  
` compute.disks.get `  
` compute.disks.getIamPolicy `  
` compute.disks.list `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.firewalls.get `  
` compute.firewalls.list `  
` compute.forwardingRules.get `  
` compute.forwardingRules.list `  
` compute.globalAddresses.get `  
` compute.globalAddresses.list `  
` compute.globalForwardingRules.get `  
` compute.globalForwardingRules.list `  
` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalPublicDelegatedPrefixes.get `  
` compute.globalPublicDelegatedPrefixes.list `  
` compute.healthChecks.get `  
` compute.healthChecks.list `  
` compute.httpHealthChecks.get `  
` compute.httpHealthChecks.list `  
` compute.httpsHealthChecks.get `  
` compute.httpsHealthChecks.list `  
` compute.images.get `  
` compute.images.getFromFamily `  
` compute.images.getIamPolicy `  
` compute.images.list `  
` compute.instanceGroupManagers.get `  
` compute.instanceGroupManagers.list `  
` compute.instanceGroups.get `  
` compute.instanceGroups.list `  
` compute.instanceTemplates.get `  
` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.list `  
` compute.instances.get `  
` compute.instances.getEffectiveFirewalls `  
` compute.instances.getGuestAttributes `  
` compute.instances.getIamPolicy `  
` compute.instances.getScreenshot `  
` compute.instances.getSerialPortOutput `  
` compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.list `  
` compute.instances.listReferrers `  
` compute.interconnectAttachments.get `  
` compute.interconnectAttachments.list `  
` compute.interconnectLocations.get `  
` compute.interconnectLocations.list `  
` compute.interconnects.get `  
` compute.interconnects.list `  
` compute.licenseCodes.get `  
` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.list `  
` compute.licenses.get `  
` compute.licenses.getIamPolicy `  
` compute.licenses.list `  
` compute.machineTypes.get `  
` compute.maintenancePolicies.get `  
` compute.maintenancePolicies.getIamPolicy `  
` compute.maintenancePolicies.list `  
` compute.networkEndpointGroups.get `  
` compute.networkEndpointGroups.getIamPolicy `  
` compute.networkEndpointGroups.list `  
` compute.networks.get `  
` compute.networks.getEffectiveFirewalls `  
` compute.networks.list `  
` compute.networks.listPeeringRoutes `  
` compute.nodeGroups.get `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.list `  
` compute.nodeTemplates.get `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.list `  
` compute.nodeTypes.get `  
` compute.nodeTypes.list `  
` compute.organizations.listAssociations `  
` compute.projects.get `  
` compute.publicAdvertisedPrefixes.get `  
` compute.publicAdvertisedPrefixes.list `  
` compute.publicDelegatedPrefixes.get `  
` compute.publicDelegatedPrefixes.list `  
` compute.regionBackendServices.get `  
` compute.regionBackendServices.list `  
` compute.regionHealthCheckServices.get `  
` compute.regionHealthCheckServices.list `  
` compute.regionNotificationEndpoints.get `  
` compute.regionNotificationEndpoints.list `  
` compute.regionOperations.get `  
` compute.regionOperations.getIamPolicy `  
` compute.regionOperations.list `  
` compute.regions.get `  
` compute.regions.list `  
` compute.reservations.get `  
` compute.reservations.list `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.routers.get `  
` compute.routers.list `  
` compute.routes.get `  
` compute.routes.list `  
` compute.securityPolicies.get `  
` compute.securityPolicies.getIamPolicy `  
` compute.securityPolicies.list `  
` compute.snapshots.get `  
` compute.snapshots.getIamPolicy `  
` compute.snapshots.list `  
` compute.sslCertificates.get `  
` compute.sslCertificates.list `  
` compute.sslPolicies.get `  
` compute.sslPolicies.list `  
` compute.sslPolicies.listAvailableFeatures `  
` compute.subnetworks.get `  
` compute.subnetworks.getIamPolicy `  
` compute.targetHttpProxies.get `  
` compute.targetHttpProxies.list `  
` compute.targetHttpsProxies.get `  
` compute.targetHttpsProxies.list `  
` compute.targetInstances.get `  
` compute.targetInstances.list `  
` compute.targetPools.get `  
` compute.targetPools.list `  
` compute.targetSslProxies.get `  
` compute.targetSslProxies.list `  
` compute.targetTcpProxies.get `  
` compute.targetTcpProxies.list `  
` compute.targetVpnGateways.get `  
` compute.targetVpnGateways.list `  
` compute.urlMaps.get `  
` compute.urlMaps.list `  
` compute.urlMaps.validate `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnTunnels.get `  
` compute.vpnTunnels.list `  
` compute.zoneOperations.get `  
` compute.zoneOperations.getIamPolicy `  
` compute.zoneOperations.list `  
` compute.zones.get `  
` compute.zones.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
AI Platform Notebooks  |  Role Updated  |

The following permissions have been added to the role ` roles/notebooks.runner
` (Notebooks Runner):

` compute.acceleratorTypes.get `  
` compute.addresses.get `  
` compute.addresses.list `  
` compute.autoscalers.get `  
` compute.autoscalers.list `  
` compute.backendBuckets.get `  
` compute.backendBuckets.list `  
` compute.backendServices.get `  
` compute.backendServices.list `  
` compute.commitments.get `  
` compute.commitments.list `  
` compute.diskTypes.get `  
` compute.disks.get `  
` compute.disks.getIamPolicy `  
` compute.disks.list `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.firewalls.get `  
` compute.firewalls.list `  
` compute.forwardingRules.get `  
` compute.forwardingRules.list `  
` compute.globalAddresses.get `  
` compute.globalAddresses.list `  
` compute.globalForwardingRules.get `  
` compute.globalForwardingRules.list `  
` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalPublicDelegatedPrefixes.get `  
` compute.globalPublicDelegatedPrefixes.list `  
` compute.healthChecks.get `  
` compute.healthChecks.list `  
` compute.httpHealthChecks.get `  
` compute.httpHealthChecks.list `  
` compute.httpsHealthChecks.get `  
` compute.httpsHealthChecks.list `  
` compute.images.get `  
` compute.images.getFromFamily `  
` compute.images.getIamPolicy `  
` compute.images.list `  
` compute.instanceGroupManagers.get `  
` compute.instanceGroupManagers.list `  
` compute.instanceGroups.get `  
` compute.instanceGroups.list `  
` compute.instanceTemplates.get `  
` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.list `  
` compute.instances.get `  
` compute.instances.getEffectiveFirewalls `  
` compute.instances.getGuestAttributes `  
` compute.instances.getIamPolicy `  
` compute.instances.getScreenshot `  
` compute.instances.getSerialPortOutput `  
` compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.list `  
` compute.instances.listReferrers `  
` compute.interconnectAttachments.get `  
` compute.interconnectAttachments.list `  
` compute.interconnectLocations.get `  
` compute.interconnectLocations.list `  
` compute.interconnects.get `  
` compute.interconnects.list `  
` compute.licenseCodes.get `  
` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.list `  
` compute.licenses.get `  
` compute.licenses.getIamPolicy `  
` compute.licenses.list `  
` compute.machineTypes.get `  
` compute.maintenancePolicies.get `  
` compute.maintenancePolicies.getIamPolicy `  
` compute.maintenancePolicies.list `  
` compute.networkEndpointGroups.get `  
` compute.networkEndpointGroups.getIamPolicy `  
` compute.networkEndpointGroups.list `  
` compute.networks.get `  
` compute.networks.getEffectiveFirewalls `  
` compute.networks.list `  
` compute.networks.listPeeringRoutes `  
` compute.nodeGroups.get `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.list `  
` compute.nodeTemplates.get `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.list `  
` compute.nodeTypes.get `  
` compute.nodeTypes.list `  
` compute.organizations.listAssociations `  
` compute.projects.get `  
` compute.publicAdvertisedPrefixes.get `  
` compute.publicAdvertisedPrefixes.list `  
` compute.publicDelegatedPrefixes.get `  
` compute.publicDelegatedPrefixes.list `  
` compute.regionBackendServices.get `  
` compute.regionBackendServices.list `  
` compute.regionHealthCheckServices.get `  
` compute.regionHealthCheckServices.list `  
` compute.regionNotificationEndpoints.get `  
` compute.regionNotificationEndpoints.list `  
` compute.regionOperations.get `  
` compute.regionOperations.getIamPolicy `  
` compute.regionOperations.list `  
` compute.regions.get `  
` compute.regions.list `  
` compute.reservations.get `  
` compute.reservations.list `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.routers.get `  
` compute.routers.list `  
` compute.routes.get `  
` compute.routes.list `  
` compute.securityPolicies.get `  
` compute.securityPolicies.getIamPolicy `  
` compute.securityPolicies.list `  
` compute.snapshots.get `  
` compute.snapshots.getIamPolicy `  
` compute.snapshots.list `  
` compute.sslCertificates.get `  
` compute.sslCertificates.list `  
` compute.sslPolicies.get `  
` compute.sslPolicies.list `  
` compute.sslPolicies.listAvailableFeatures `  
` compute.subnetworks.get `  
` compute.subnetworks.getIamPolicy `  
` compute.targetHttpProxies.get `  
` compute.targetHttpProxies.list `  
` compute.targetHttpsProxies.get `  
` compute.targetHttpsProxies.list `  
` compute.targetInstances.get `  
` compute.targetInstances.list `  
` compute.targetPools.get `  
` compute.targetPools.list `  
` compute.targetSslProxies.get `  
` compute.targetSslProxies.list `  
` compute.targetTcpProxies.get `  
` compute.targetTcpProxies.list `  
` compute.targetVpnGateways.get `  
` compute.targetVpnGateways.list `  
` compute.urlMaps.get `  
` compute.urlMaps.list `  
` compute.urlMaps.validate `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnTunnels.get `  
` compute.vpnTunnels.list `  
` compute.zoneOperations.get `  
` compute.zoneOperations.getIamPolicy `  
` compute.zoneOperations.list `  
` compute.zones.get `  
` compute.zones.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
AI Platform Notebooks  |  Role Updated  |

The following permissions have been added to the role ` roles/notebooks.viewer
` (Notebooks Viewer):

` compute.acceleratorTypes.get `  
` compute.addresses.get `  
` compute.addresses.list `  
` compute.autoscalers.get `  
` compute.autoscalers.list `  
` compute.backendBuckets.get `  
` compute.backendBuckets.list `  
` compute.backendServices.get `  
` compute.backendServices.list `  
` compute.commitments.get `  
` compute.commitments.list `  
` compute.diskTypes.get `  
` compute.disks.get `  
` compute.disks.getIamPolicy `  
` compute.disks.list `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.firewalls.get `  
` compute.firewalls.list `  
` compute.forwardingRules.get `  
` compute.forwardingRules.list `  
` compute.globalAddresses.get `  
` compute.globalAddresses.list `  
` compute.globalForwardingRules.get `  
` compute.globalForwardingRules.list `  
` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalPublicDelegatedPrefixes.get `  
` compute.globalPublicDelegatedPrefixes.list `  
` compute.healthChecks.get `  
` compute.healthChecks.list `  
` compute.httpHealthChecks.get `  
` compute.httpHealthChecks.list `  
` compute.httpsHealthChecks.get `  
` compute.httpsHealthChecks.list `  
` compute.images.get `  
` compute.images.getFromFamily `  
` compute.images.getIamPolicy `  
` compute.images.list `  
` compute.instanceGroupManagers.get `  
` compute.instanceGroupManagers.list `  
` compute.instanceGroups.get `  
` compute.instanceGroups.list `  
` compute.instanceTemplates.get `  
` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.list `  
` compute.instances.get `  
` compute.instances.getEffectiveFirewalls `  
` compute.instances.getGuestAttributes `  
` compute.instances.getIamPolicy `  
` compute.instances.getScreenshot `  
` compute.instances.getSerialPortOutput `  
` compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.list `  
` compute.instances.listReferrers `  
` compute.interconnectAttachments.get `  
` compute.interconnectAttachments.list `  
` compute.interconnectLocations.get `  
` compute.interconnectLocations.list `  
` compute.interconnects.get `  
` compute.interconnects.list `  
` compute.licenseCodes.get `  
` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.list `  
` compute.licenses.get `  
` compute.licenses.getIamPolicy `  
` compute.licenses.list `  
` compute.machineTypes.get `  
` compute.maintenancePolicies.get `  
` compute.maintenancePolicies.getIamPolicy `  
` compute.maintenancePolicies.list `  
` compute.networkEndpointGroups.get `  
` compute.networkEndpointGroups.getIamPolicy `  
` compute.networkEndpointGroups.list `  
` compute.networks.get `  
` compute.networks.getEffectiveFirewalls `  
` compute.networks.list `  
` compute.networks.listPeeringRoutes `  
` compute.nodeGroups.get `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.list `  
` compute.nodeTemplates.get `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.list `  
` compute.nodeTypes.get `  
` compute.nodeTypes.list `  
` compute.organizations.listAssociations `  
` compute.projects.get `  
` compute.publicAdvertisedPrefixes.get `  
` compute.publicAdvertisedPrefixes.list `  
` compute.publicDelegatedPrefixes.get `  
` compute.publicDelegatedPrefixes.list `  
` compute.regionBackendServices.get `  
` compute.regionBackendServices.list `  
` compute.regionHealthCheckServices.get `  
` compute.regionHealthCheckServices.list `  
` compute.regionNotificationEndpoints.get `  
` compute.regionNotificationEndpoints.list `  
` compute.regionOperations.get `  
` compute.regionOperations.getIamPolicy `  
` compute.regionOperations.list `  
` compute.regions.get `  
` compute.regions.list `  
` compute.reservations.get `  
` compute.reservations.list `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.routers.get `  
` compute.routers.list `  
` compute.routes.get `  
` compute.routes.list `  
` compute.securityPolicies.get `  
` compute.securityPolicies.getIamPolicy `  
` compute.securityPolicies.list `  
` compute.snapshots.get `  
` compute.snapshots.getIamPolicy `  
` compute.snapshots.list `  
` compute.sslCertificates.get `  
` compute.sslCertificates.list `  
` compute.sslPolicies.get `  
` compute.sslPolicies.list `  
` compute.sslPolicies.listAvailableFeatures `  
` compute.subnetworks.get `  
` compute.subnetworks.getIamPolicy `  
` compute.targetHttpProxies.get `  
` compute.targetHttpProxies.list `  
` compute.targetHttpsProxies.get `  
` compute.targetHttpsProxies.list `  
` compute.targetInstances.get `  
` compute.targetInstances.list `  
` compute.targetPools.get `  
` compute.targetPools.list `  
` compute.targetSslProxies.get `  
` compute.targetSslProxies.list `  
` compute.targetTcpProxies.get `  
` compute.targetTcpProxies.list `  
` compute.targetVpnGateways.get `  
` compute.targetVpnGateways.list `  
` compute.urlMaps.get `  
` compute.urlMaps.list `  
` compute.urlMaps.validate `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnTunnels.get `  
` compute.vpnTunnels.list `  
` compute.zoneOperations.get `  
` compute.zoneOperations.getIamPolicy `  
` compute.zoneOperations.list `  
` compute.zones.get `  
` compute.zones.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Apigee API  |  Now GA  |  ` apigee.apiproductattributes.createOrUpdateAll `  
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
  
Apigee Connect  |  Now GA  |  ` apigeeconnect.connections.list `  
` apigeeconnect.endpoints.connect `  
  
Recommendations AI  |  Added  |  ` automlrecommendations.events.rejoin `  
` automlrecommendations.placements.create `  
` automlrecommendations.placements.delete `  
` automlrecommendations.recommendations.create `  
` automlrecommendations.recommendations.delete `  
` automlrecommendations.recommendations.pause `  
` automlrecommendations.recommendations.resume `  
` automlrecommendations.recommendations.update `  
  
Recommendations AI  |  Supported In Custom Roles  |  `
automlrecommendations.events.rejoin `  
` automlrecommendations.placements.create `  
` automlrecommendations.placements.delete `  
` automlrecommendations.placements.list `  
` automlrecommendations.recommendations.create `  
` automlrecommendations.recommendations.delete `  
` automlrecommendations.recommendations.pause `  
` automlrecommendations.recommendations.resume `  
` automlrecommendations.recommendations.update `  
  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.tables.setCategory `  
  
Google Cloud Game Servers  |  Now GA  |  `
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
  
Cloud Healthcare API  |  Added  |  ` healthcare.hl7V2Stores.import `  
` healthcare.locations.get `  
` healthcare.locations.list `  
  
Identity and Access Management  |  Added  |  ` iam.serviceAccounts.disable `  
` iam.serviceAccounts.enable `  
` iam.serviceAccounts.undelete `  
  
Identity and Access Management  |  Available In Custom Roles  |  `
iam.serviceAccounts.undelete `  
  
AI Platform Notebooks  |  Added  |  ` notebooks.instances.checkUpgradability `  
` notebooks.instances.reset `  
` notebooks.instances.setAccelerator `  
` notebooks.instances.setLabels `  
` notebooks.instances.setMachineType `  
` notebooks.instances.start `  
` notebooks.instances.stop `  
` notebooks.instances.upgrade `  
  
  
##  Cloud IAM changes as of 2020-07-24

Service  |  Change  |  Description  
---|---|---  
Identity and Access Management  |  Role Updated  |

The following permissions have been removed from the role `
roles/iam.securityAdmin ` (Security Admin):

` container.secrets.list `  
  
Identity and Access Management  |  Role Updated  |

The following permissions have been removed from the role `
roles/iam.securityReviewer ` (Security Reviewer):

` container.secrets.list `  
  
  
##  Cloud IAM changes as of 2020-07-17

Service  |  Change  |  Description  
---|---|---  
GKE Hub  |  Now GA  |

The role ` roles/gkehub.gatewayAdmin ` (Connect Gateway Admin) is now GA.  
  
Secret Manager  |  Now GA  |

The role ` roles/secretmanager.secretVersionAdder ` (Secret Manager Secret
Version Adder) is now GA.  
  
Secret Manager  |  Now GA  |

The role ` roles/secretmanager.secretVersionManager ` (Secret Manager Secret
Version Manager) is now GA.  
  
Cloud Bigtable  |  Added  |  ` bigtable.backups.create `  
` bigtable.backups.delete `  
` bigtable.backups.get `  
` bigtable.backups.getIamPolicy `  
` bigtable.backups.list `  
` bigtable.backups.restore `  
` bigtable.backups.setIamPolicy `  
` bigtable.backups.update `  
  
Cloud Bigtable  |  Supported In Custom Roles  |  ` bigtable.backups.create `  
` bigtable.backups.delete `  
` bigtable.backups.get `  
` bigtable.backups.getIamPolicy `  
` bigtable.backups.list `  
` bigtable.backups.restore `  
` bigtable.backups.setIamPolicy `  
` bigtable.backups.update `  
  
Cloud Bigtable  |  Now GA  |  ` bigtable.backups.create `  
` bigtable.backups.delete `  
` bigtable.backups.get `  
` bigtable.backups.getIamPolicy `  
` bigtable.backups.list `  
` bigtable.backups.restore `  
` bigtable.backups.setIamPolicy `  
` bigtable.backups.update `  
  
Cloud Commerce Consumer Procurement  |  Added  |  `
consumerprocurement.accounts.create `  
` consumerprocurement.accounts.delete `  
` consumerprocurement.accounts.get `  
` consumerprocurement.accounts.list `  
` consumerprocurement.entitlements.get `  
` consumerprocurement.entitlements.list `  
` consumerprocurement.freeTrials.create `  
` consumerprocurement.freeTrials.get `  
` consumerprocurement.freeTrials.list `  
` consumerprocurement.orders.cancel `  
` consumerprocurement.orders.get `  
` consumerprocurement.orders.list `  
` consumerprocurement.orders.modify `  
` consumerprocurement.orders.place `  
  
Cloud Commerce Consumer Procurement  |  Supported In Custom Roles  |  `
consumerprocurement.accounts.create `  
` consumerprocurement.accounts.delete `  
` consumerprocurement.accounts.get `  
` consumerprocurement.accounts.list `  
` consumerprocurement.entitlements.get `  
` consumerprocurement.entitlements.list `  
` consumerprocurement.freeTrials.create `  
` consumerprocurement.freeTrials.get `  
` consumerprocurement.freeTrials.list `  
` consumerprocurement.orders.cancel `  
` consumerprocurement.orders.get `  
` consumerprocurement.orders.list `  
` consumerprocurement.orders.modify `  
` consumerprocurement.orders.place `  
  
GKE Hub  |  Added  |  ` gkehub.gateway.delete `  
` gkehub.gateway.get `  
` gkehub.gateway.getIamPolicy `  
` gkehub.gateway.patch `  
` gkehub.gateway.post `  
` gkehub.gateway.put `  
` gkehub.gateway.setIamPolicy `  
  
GKE Hub  |  Now GA  |  ` gkehub.gateway.delete `  
` gkehub.gateway.get `  
` gkehub.gateway.getIamPolicy `  
` gkehub.gateway.patch `  
` gkehub.gateway.post `  
` gkehub.gateway.put `  
` gkehub.gateway.setIamPolicy `  
  
  
##  Cloud IAM changes as of 2020-07-10

Service  |  Change  |  Description  
---|---|---  
Cloud Monitoring  |  Now GA  |

The role ` roles/monitoring.servicesEditor ` (Monitoring Services Editor) is
now GA.  
  
Cloud Monitoring  |  Now GA  |

The role ` roles/monitoring.servicesViewer ` (Monitoring Services Viewer) is
now GA.  
  
NetApp Cloud Volumes Service  |  Added  |  ` cloudvolumesgcp-
api.netapp.com/activeDirectories.create `  
` cloudvolumesgcp-api.netapp.com/activeDirectories.delete `  
` cloudvolumesgcp-api.netapp.com/activeDirectories.get `  
` cloudvolumesgcp-api.netapp.com/activeDirectories.list `  
` cloudvolumesgcp-api.netapp.com/activeDirectories.update `  
` cloudvolumesgcp-api.netapp.com/ipRanges.list `  
` cloudvolumesgcp-api.netapp.com/jobs.get `  
` cloudvolumesgcp-api.netapp.com/jobs.list `  
` cloudvolumesgcp-api.netapp.com/regions.list `  
` cloudvolumesgcp-api.netapp.com/serviceLevels.list `  
` cloudvolumesgcp-api.netapp.com/snapshots.create `  
` cloudvolumesgcp-api.netapp.com/snapshots.delete `  
` cloudvolumesgcp-api.netapp.com/snapshots.get `  
` cloudvolumesgcp-api.netapp.com/snapshots.list `  
` cloudvolumesgcp-api.netapp.com/snapshots.update `  
` cloudvolumesgcp-api.netapp.com/volumes.create `  
` cloudvolumesgcp-api.netapp.com/volumes.delete `  
` cloudvolumesgcp-api.netapp.com/volumes.get `  
` cloudvolumesgcp-api.netapp.com/volumes.list `  
` cloudvolumesgcp-api.netapp.com/volumes.update `  
  
Cloud Monitoring  |  Added  |  ` monitoring.services.create `  
` monitoring.services.delete `  
` monitoring.services.get `  
` monitoring.services.list `  
` monitoring.services.update `  
` monitoring.slos.create `  
` monitoring.slos.delete `  
` monitoring.slos.get `  
` monitoring.slos.list `  
` monitoring.slos.update `  
  
Cloud Monitoring  |  Supported In Custom Roles  |  `
monitoring.services.create `  
` monitoring.services.delete `  
` monitoring.services.get `  
` monitoring.services.list `  
` monitoring.services.update `  
` monitoring.slos.create `  
` monitoring.slos.delete `  
` monitoring.slos.get `  
` monitoring.slos.list `  
` monitoring.slos.update `  
  
Cloud Monitoring  |  Now GA  |  ` monitoring.services.create `  
` monitoring.services.delete `  
` monitoring.services.get `  
` monitoring.services.list `  
` monitoring.services.update `  
` monitoring.slos.create `  
` monitoring.slos.delete `  
` monitoring.slos.get `  
` monitoring.slos.list `  
` monitoring.slos.update `  
  
Network Security  |  Added  |  ` networksecurity.authorizationPolicies.create
`  
` networksecurity.authorizationPolicies.delete `  
` networksecurity.authorizationPolicies.get `  
` networksecurity.authorizationPolicies.getIamPolicy `  
` networksecurity.authorizationPolicies.list `  
` networksecurity.authorizationPolicies.setIamPolicy `  
` networksecurity.authorizationPolicies.update `  
` networksecurity.authorizationPolicies.use `  
` networksecurity.clientTlsPolicies.create `  
` networksecurity.clientTlsPolicies.delete `  
` networksecurity.clientTlsPolicies.get `  
` networksecurity.clientTlsPolicies.getIamPolicy `  
` networksecurity.clientTlsPolicies.list `  
` networksecurity.clientTlsPolicies.setIamPolicy `  
` networksecurity.clientTlsPolicies.update `  
` networksecurity.clientTlsPolicies.use `  
` networksecurity.locations.get `  
` networksecurity.locations.list `  
` networksecurity.operations.cancel `  
` networksecurity.operations.delete `  
` networksecurity.operations.get `  
` networksecurity.operations.list `  
` networksecurity.serverTlsPolicies.create `  
` networksecurity.serverTlsPolicies.delete `  
` networksecurity.serverTlsPolicies.get `  
` networksecurity.serverTlsPolicies.getIamPolicy `  
` networksecurity.serverTlsPolicies.list `  
` networksecurity.serverTlsPolicies.setIamPolicy `  
` networksecurity.serverTlsPolicies.update `  
` networksecurity.serverTlsPolicies.use `  
  
Network Security  |  Supported In Custom Roles  |  `
networksecurity.authorizationPolicies.create `  
` networksecurity.authorizationPolicies.delete `  
` networksecurity.authorizationPolicies.get `  
` networksecurity.authorizationPolicies.getIamPolicy `  
` networksecurity.authorizationPolicies.list `  
` networksecurity.authorizationPolicies.setIamPolicy `  
` networksecurity.authorizationPolicies.update `  
` networksecurity.authorizationPolicies.use `  
` networksecurity.clientTlsPolicies.create `  
` networksecurity.clientTlsPolicies.delete `  
` networksecurity.clientTlsPolicies.get `  
` networksecurity.clientTlsPolicies.getIamPolicy `  
` networksecurity.clientTlsPolicies.list `  
` networksecurity.clientTlsPolicies.setIamPolicy `  
` networksecurity.clientTlsPolicies.update `  
` networksecurity.clientTlsPolicies.use `  
` networksecurity.locations.get `  
` networksecurity.locations.list `  
` networksecurity.operations.cancel `  
` networksecurity.operations.delete `  
` networksecurity.operations.get `  
` networksecurity.operations.list `  
` networksecurity.serverTlsPolicies.create `  
` networksecurity.serverTlsPolicies.delete `  
` networksecurity.serverTlsPolicies.get `  
` networksecurity.serverTlsPolicies.getIamPolicy `  
` networksecurity.serverTlsPolicies.list `  
` networksecurity.serverTlsPolicies.setIamPolicy `  
` networksecurity.serverTlsPolicies.update `  
` networksecurity.serverTlsPolicies.use `  
  
Network Services  |  Added  |  `
networkservices.endpointConfigSelectors.create `  
` networkservices.endpointConfigSelectors.delete `  
` networkservices.endpointConfigSelectors.get `  
` networkservices.endpointConfigSelectors.getIamPolicy `  
` networkservices.endpointConfigSelectors.list `  
` networkservices.endpointConfigSelectors.setIamPolicy `  
` networkservices.endpointConfigSelectors.update `  
` networkservices.endpointConfigSelectors.use `  
` networkservices.httpFilters.create `  
` networkservices.httpFilters.delete `  
` networkservices.httpFilters.get `  
` networkservices.httpFilters.getIamPolicy `  
` networkservices.httpFilters.list `  
` networkservices.httpFilters.setIamPolicy `  
` networkservices.httpFilters.update `  
` networkservices.httpFilters.use `  
` networkservices.locations.get `  
` networkservices.locations.list `  
` networkservices.operations.cancel `  
` networkservices.operations.delete `  
` networkservices.operations.get `  
` networkservices.operations.list `  
  
Network Services  |  Supported In Custom Roles  |  `
networkservices.endpointConfigSelectors.create `  
` networkservices.endpointConfigSelectors.delete `  
` networkservices.endpointConfigSelectors.get `  
` networkservices.endpointConfigSelectors.getIamPolicy `  
` networkservices.endpointConfigSelectors.list `  
` networkservices.endpointConfigSelectors.setIamPolicy `  
` networkservices.endpointConfigSelectors.update `  
` networkservices.endpointConfigSelectors.use `  
` networkservices.httpFilters.create `  
` networkservices.httpFilters.delete `  
` networkservices.httpFilters.get `  
` networkservices.httpFilters.getIamPolicy `  
` networkservices.httpFilters.list `  
` networkservices.httpFilters.setIamPolicy `  
` networkservices.httpFilters.update `  
` networkservices.httpFilters.use `  
` networkservices.locations.get `  
` networkservices.locations.list `  
` networkservices.operations.cancel `  
` networkservices.operations.delete `  
` networkservices.operations.get `  
` networkservices.operations.list `  
  
Pub/Sub  |  Added  |  ` pubsub.topics.detachSubscription `  
  
Pub/Sub  |  Now GA  |  ` pubsub.topics.detachSubscription `  
  
reCAPTCHA Enterprise  |  Added  |  ` recaptchaenterprise.metrics.get `  
  
reCAPTCHA Enterprise  |  Supported In Custom Roles  |  `
recaptchaenterprise.metrics.get `  
  
Recommender  |  Added  |  ` recommender.computeDiskIdleResourceInsights.get `  
` recommender.computeDiskIdleResourceInsights.list `  
` recommender.computeDiskIdleResourceInsights.update `  
  
Recommender  |  Supported In Custom Roles  |  `
recommender.computeDiskIdleResourceInsights.get `  
` recommender.computeDiskIdleResourceInsights.list `  
` recommender.computeDiskIdleResourceInsights.update `  
  
Recommender  |  Now GA  |  ` recommender.computeDiskIdleResourceInsights.get `  
` recommender.computeDiskIdleResourceInsights.list `  
` recommender.computeDiskIdleResourceInsights.update `  
  
  
##  Cloud IAM changes as of 2020-06-26

Service  |  Change  |  Description  
---|---|---  
Apigee API  |  Role Updated  |

The following permissions have been added to the role `
roles/apigee.analyticsViewer ` (Apigee Analytics Viewer):

` apigee.queries.get `  
` apigee.queries.list `  
` apigee.reports.get `  
` apigee.reports.list `  
  
Cloud Billing  |  Role Updated  |

The following permissions have been added to the role ` roles/billing.admin `
(Billing Account Administrator):

` dataprocessing.groupcontrols.list `  
  
Cloud Billing  |  Role Updated  |

The following permissions have been added to the role ` roles/billing.viewer `
(Billing Account Viewer):

` dataprocessing.groupcontrols.list `  
  
Cloud Composer  |  Role Updated  |

The following permissions have been added to the role ` roles/composer.worker
` (Composer Worker):

` monitoring.timeSeries.list `  
  
Dataproc  |  Role Updated  |

The following permissions have been added to the role ` roles/dataproc.viewer
` (Dataproc Viewer):

` compute.zones.list `  
  
Customer Usage Data Processing API  |  Role Updated  |

The following permissions have been added to the role `
roles/dataprocessing.admin ` (Data Processing Controls Resource Admin):

` billing.accounts.get `  
` billing.accounts.list `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/editor `
(Editor):

` containeranalysis.notes.getIamPolicy `  
` containeranalysis.occurrences.getIamPolicy `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/viewer `
(Viewer):

` containeranalysis.notes.getIamPolicy `  
` containeranalysis.occurrences.getIamPolicy `  
  
Serverless VPC Access  |  Now GA  |

The role ` roles/vpcaccess.user ` (Serverless VPC Access User) is now GA.  
  
Serverless VPC Access  |  Now GA  |

The role ` roles/vpcaccess.viewer ` (Serverless VPC Access Viewer) is now GA.  
  
Compute Engine  |  Added  |  ` compute.images.update `  
` compute.instances.getEffectiveFirewalls `  
` compute.networks.getEffectiveFirewalls `  
` compute.organizations.listAssociations `  
` compute.organizations.setSecurityPolicy `  
` compute.securityPolicies.addAssociation `  
` compute.securityPolicies.copyRules `  
` compute.securityPolicies.move `  
` compute.securityPolicies.removeAssociation `  
  
Compute Engine  |  Supported In Custom Roles  |  `
compute.instances.getEffectiveFirewalls `  
` compute.networks.getEffectiveFirewalls `  
` compute.organizations.listAssociations `  
` compute.organizations.setSecurityPolicy `  
` compute.securityPolicies.addAssociation `  
` compute.securityPolicies.copyRules `  
` compute.securityPolicies.move `  
` compute.securityPolicies.removeAssociation `  
  
Container Analysis  |  Added  |  ` containeranalysis.notes.attachOccurrence `  
` containeranalysis.notes.create `  
` containeranalysis.notes.delete `  
` containeranalysis.notes.get `  
` containeranalysis.notes.getIamPolicy `  
` containeranalysis.notes.list `  
` containeranalysis.notes.listOccurrences `  
` containeranalysis.notes.setIamPolicy `  
` containeranalysis.notes.update `  
` containeranalysis.occurrences.create `  
` containeranalysis.occurrences.delete `  
` containeranalysis.occurrences.get `  
` containeranalysis.occurrences.getIamPolicy `  
` containeranalysis.occurrences.list `  
` containeranalysis.occurrences.setIamPolicy `  
` containeranalysis.occurrences.update `  
  
Container Analysis  |  Supported In Custom Roles  |  `
containeranalysis.notes.attachOccurrence `  
` containeranalysis.notes.create `  
` containeranalysis.notes.delete `  
` containeranalysis.notes.get `  
` containeranalysis.notes.getIamPolicy `  
` containeranalysis.notes.list `  
` containeranalysis.notes.listOccurrences `  
` containeranalysis.notes.setIamPolicy `  
` containeranalysis.notes.update `  
` containeranalysis.occurrences.create `  
` containeranalysis.occurrences.delete `  
` containeranalysis.occurrences.get `  
` containeranalysis.occurrences.getIamPolicy `  
` containeranalysis.occurrences.list `  
` containeranalysis.occurrences.setIamPolicy `  
` containeranalysis.occurrences.update `  
  
Recommender  |  Added  |  ` recommender.iamServiceAccountInsights.get `  
` recommender.iamServiceAccountInsights.list `  
` recommender.iamServiceAccountInsights.update `  
  
Recommender  |  Supported In Custom Roles  |  `
recommender.iamServiceAccountInsights.get `  
` recommender.iamServiceAccountInsights.list `  
` recommender.iamServiceAccountInsights.update `  
  
Recommender  |  Now GA  |  ` recommender.iamServiceAccountInsights.get `  
` recommender.iamServiceAccountInsights.list `  
` recommender.iamServiceAccountInsights.update `  
  
Cloud Spanner  |  Added  |  ` spanner.databases.beginPartitionedDmlTransaction
`  
` spanner.databases.partitionQuery `  
` spanner.databases.partitionRead `  
  
Cloud Spanner  |  Supported In Custom Roles  |  `
spanner.databases.beginPartitionedDmlTransaction `  
` spanner.databases.partitionQuery `  
` spanner.databases.partitionRead `  
  
Cloud Spanner  |  Now GA  |  `
spanner.databases.beginPartitionedDmlTransaction `  
` spanner.databases.partitionQuery `  
` spanner.databases.partitionRead `  
  
  
##  Cloud IAM changes as of 2020-06-19

Service  |  Change  |  Description  
---|---|---  
Actions API  |  Role Updated  |

The following permissions have been added to the role ` roles/actions.Admin `
(Actions Admin):

` serviceusage.services.use `  
  
Actions API  |  Role Updated  |

The following permissions have been added to the role ` roles/actions.Viewer `
(Actions Viewer):

` serviceusage.services.use `  
  
Container Analysis  |  Now GA  |

The role ` roles/containeranalysis.admin ` (Container Analysis Admin) is now
GA.  
  
Container Analysis  |  Now GA  |

The role ` roles/containeranalysis.notes.attacher ` (Container Analysis Notes
Attacher) is now GA.  
  
Container Analysis  |  Now GA  |

The role ` roles/containeranalysis.notes.editor ` (Container Analysis Notes
Editor) is now GA.  
  
Container Analysis  |  Now GA  |

The role ` roles/containeranalysis.notes.viewer ` (Container Analysis Notes
Viewer) is now GA.  
  
Container Analysis  |  Now GA  |

The role ` roles/containeranalysis.occurrences.editor ` (Container Analysis
Occurrences Editor) is now GA.  
  
Container Analysis  |  Now GA  |

The role ` roles/containeranalysis.occurrences.viewer ` (Container Analysis
Occurrences Viewer) is now GA.  
  
Cloud OS Config  |  Now GA  |

The role ` roles/osconfig.assignmentAdmin ` (Assignment Admin) is now GA.  
  
Cloud OS Config  |  Now GA  |

The role ` roles/osconfig.assignmentEditor ` (Assignment Editor) is now GA.  
  
Cloud OS Config  |  Now GA  |

The role ` roles/osconfig.assignmentViewer ` (Assignment Viewer) is now GA.  
  
Cloud OS Config  |  Now GA  |

The role ` roles/osconfig.osConfigAdmin ` (OsConfig Admin) is now GA.  
  
Cloud OS Config  |  Now GA  |

The role ` roles/osconfig.osConfigEditor ` (OsConfig Editor) is now GA.  
  
Cloud OS Config  |  Now GA  |

The role ` roles/osconfig.osConfigViewer ` (OsConfig Viewer) is now GA.  
  
Cloud OS Config  |  Now GA  |

The role ` roles/osconfig.patchDeploymentAdmin ` (PatchDeployment Admin) is
now GA.  
  
Cloud OS Config  |  Now GA  |

The role ` roles/osconfig.patchDeploymentViewer ` (PatchDeployment Viewer) is
now GA.  
  
Cloud OS Config  |  Now GA  |

The role ` roles/osconfig.patchJobExecutor ` (Patch Job Executor) is now GA.  
  
Cloud OS Config  |  Now GA  |

The role ` roles/osconfig.patchJobViewer ` (Patch Job Viewer) is now GA.  
  
Primitive Role  |  Role Updated  |

The following permissions have been removed from the role ` roles/viewer `
(Viewer):

` apigee.appkeys.create `  
  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.connections.create `  
` bigquery.connections.delete `  
` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.setIamPolicy `  
` bigquery.connections.update `  
` bigquery.connections.use `  
  
Compute Engine  |  Added  |  ` compute.instances.update `  
  
Compute Engine  |  Supported In Custom Roles  |  ` compute.instances.update `  
  
Compute Engine  |  Now GA  |  ` compute.instances.update `  
  
Filestore  |  Added  |  ` file.backups.create `  
` file.backups.delete `  
` file.backups.get `  
` file.backups.list `  
` file.backups.update `  
  
GKE Hub  |  Added  |  ` gkehub.features.create `  
` gkehub.features.delete `  
` gkehub.features.get `  
` gkehub.features.getIamPolicy `  
` gkehub.features.list `  
` gkehub.features.setIamPolicy `  
` gkehub.features.update `  
  
GKE Hub  |  Now GA  |  ` gkehub.features.create `  
` gkehub.features.delete `  
` gkehub.features.get `  
` gkehub.features.getIamPolicy `  
` gkehub.features.list `  
` gkehub.features.setIamPolicy `  
` gkehub.features.update `  
  
Cloud OS Config  |  Now GA  |  ` osconfig.patchDeployments.create `  
` osconfig.patchDeployments.delete `  
` osconfig.patchDeployments.execute `  
` osconfig.patchDeployments.get `  
` osconfig.patchDeployments.list `  
` osconfig.patchDeployments.update `  
` osconfig.patchJobs.exec `  
` osconfig.patchJobs.get `  
` osconfig.patchJobs.list `  
  
Pub/Sub Lite  |  Added  |  ` pubsublite.subscriptions.create `  
` pubsublite.subscriptions.delete `  
` pubsublite.subscriptions.get `  
` pubsublite.subscriptions.getCursor `  
` pubsublite.subscriptions.list `  
` pubsublite.subscriptions.setCursor `  
` pubsublite.subscriptions.subscribe `  
` pubsublite.subscriptions.update `  
` pubsublite.topics.create `  
` pubsublite.topics.delete `  
` pubsublite.topics.get `  
` pubsublite.topics.getPartitions `  
` pubsublite.topics.list `  
` pubsublite.topics.listSubscriptions `  
` pubsublite.topics.publish `  
` pubsublite.topics.subscribe `  
` pubsublite.topics.update `  
  
Pub/Sub Lite  |  Supported In Custom Roles  |  `
pubsublite.subscriptions.create `  
` pubsublite.subscriptions.delete `  
` pubsublite.subscriptions.get `  
` pubsublite.subscriptions.getCursor `  
` pubsublite.subscriptions.list `  
` pubsublite.subscriptions.setCursor `  
` pubsublite.subscriptions.subscribe `  
` pubsublite.subscriptions.update `  
` pubsublite.topics.create `  
` pubsublite.topics.delete `  
` pubsublite.topics.get `  
` pubsublite.topics.getPartitions `  
` pubsublite.topics.list `  
` pubsublite.topics.listSubscriptions `  
` pubsublite.topics.publish `  
` pubsublite.topics.subscribe `  
` pubsublite.topics.update `  
  
Google Cloud VMware Engine  |  Now GA  |

The role ` roles/vmwareengine.vmwareengineAdmin ` (VMWare Engine Service
Admin) is now GA.  
  
Google Cloud VMware Engine  |  Now GA  |

The role ` roles/vmwareengine.vmwareengineViewer ` (VMWare Engine Service
Viewer) is now GA.  
  
Google Cloud VMware Engine  |  Added  |  `
vmwareengine.googleapis.com/services.use `  
` vmwareengine.googleapis.com/services.view `  
` vmwareengine.services.use `  
` vmwareengine.services.view `  
  
Google Cloud VMware Engine  |  Supported In Custom Roles  |  `
vmwareengine.googleapis.com/services.use `  
` vmwareengine.googleapis.com/services.view `  
` vmwareengine.services.use `  
` vmwareengine.services.view `  
  
Google Cloud VMware Engine  |  Now GA  |  `
vmwareengine.googleapis.com/services.use `  
` vmwareengine.googleapis.com/services.view `  
` vmwareengine.services.use `  
` vmwareengine.services.view `  
  
  
##  Cloud IAM changes as of 2020-06-12

Service  |  Change  |  Description  
---|---|---  
Customer Usage Data Processing API  |  Now GA  |

The role ` roles/dataprocessing.admin ` (Data Processing Controls Resource
Admin) is now GA.  
  
Customer Usage Data Processing API  |  Now GA  |

The role ` roles/dataprocessing.iamAccessHistoryExporter ` (Data Processing
IAM Access History Exporter) is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.inspectFindingsReader ` (DLP Inspect Findings Reader) is
now GA.  
  
GKE Hub  |  Now GA  |

The role ` roles/gkehub.admin ` (GKE Hub Admin) is now GA.  
  
GKE Hub  |  Now GA  |

The role ` roles/gkehub.connect ` (GKE Hub Connection Agent) is now GA.  
  
GKE Hub  |  Now GA  |

The role ` roles/gkehub.viewer ` (GKE Hub Viewer) is now GA.  
  
Cloud Life Sciences  |  Role Updated  |

The following permissions have been added to the role `
roles/lifesciences.viewer ` (Cloud Life Sciences Viewer):

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Cloud Monitoring  |  Now GA  |

The role ` roles/monitoring.dashboardEditor ` (Monitoring Dashboard
Configuration Editor) is now GA.  
  
Cloud Monitoring  |  Now GA  |

The role ` roles/monitoring.dashboardViewer ` (Monitoring Dashboard
Configuration Viewer) is now GA.  
  
Apigee Connect  |  Added  |  ` apigeeconnect.connections.list `  
` apigeeconnect.endpoints.connect `  
  
Apigee Connect  |  Supported In Custom Roles  |  `
apigeeconnect.connections.list `  
` apigeeconnect.endpoints.connect `  
  
Service Usage  |  Added  |  ` apikeys.keys.create `  
` apikeys.keys.delete `  
` apikeys.keys.get `  
` apikeys.keys.list `  
` apikeys.keys.lookup `  
` apikeys.keys.update `  
  
Recommendations AI  |  Supported In Custom Roles  |  `
automlrecommendations.events.create `  
  
BigQuery  |  Added  |  ` bigquery.tables.getIamPolicy `  
` bigquery.tables.setIamPolicy `  
  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.tables.getIamPolicy `  
` bigquery.tables.setIamPolicy `  
  
Cloud Asset Inventory  |  Added  |  `
cloudasset.assets.exportCloudkmsImportJobs `  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `
cloudasset.assets.exportCloudkmsImportJobs `  
  
Cloud Asset Inventory  |  Now GA  |  ` cloudasset.assets.searchAllIamPolicies
`  
` cloudasset.assets.searchAllResources `  
  
Compute Engine  |  Added  |  ` compute.globalPublicDelegatedPrefixes.create `  
` compute.globalPublicDelegatedPrefixes.delete `  
` compute.globalPublicDelegatedPrefixes.get `  
` compute.globalPublicDelegatedPrefixes.list `  
` compute.globalPublicDelegatedPrefixes.update `  
` compute.globalPublicDelegatedPrefixes.updatePolicy `  
` compute.globalPublicDelegatedPrefixes.use `  
` compute.publicAdvertisedPrefixes.create `  
` compute.publicAdvertisedPrefixes.delete `  
` compute.publicAdvertisedPrefixes.get `  
` compute.publicAdvertisedPrefixes.list `  
` compute.publicAdvertisedPrefixes.update `  
` compute.publicAdvertisedPrefixes.updatePolicy `  
` compute.publicAdvertisedPrefixes.use `  
` compute.publicDelegatedPrefixes.create `  
` compute.publicDelegatedPrefixes.delete `  
` compute.publicDelegatedPrefixes.get `  
` compute.publicDelegatedPrefixes.list `  
` compute.publicDelegatedPrefixes.update `  
` compute.publicDelegatedPrefixes.updatePolicy `  
` compute.publicDelegatedPrefixes.use `  
  
Compute Engine  |  Supported In Custom Roles  |  `
compute.globalPublicDelegatedPrefixes.create `  
` compute.globalPublicDelegatedPrefixes.delete `  
` compute.globalPublicDelegatedPrefixes.get `  
` compute.globalPublicDelegatedPrefixes.list `  
` compute.globalPublicDelegatedPrefixes.update `  
` compute.globalPublicDelegatedPrefixes.updatePolicy `  
` compute.globalPublicDelegatedPrefixes.use `  
` compute.publicAdvertisedPrefixes.create `  
` compute.publicAdvertisedPrefixes.delete `  
` compute.publicAdvertisedPrefixes.get `  
` compute.publicAdvertisedPrefixes.list `  
` compute.publicAdvertisedPrefixes.update `  
` compute.publicAdvertisedPrefixes.updatePolicy `  
` compute.publicAdvertisedPrefixes.use `  
` compute.publicDelegatedPrefixes.create `  
` compute.publicDelegatedPrefixes.delete `  
` compute.publicDelegatedPrefixes.get `  
` compute.publicDelegatedPrefixes.list `  
` compute.publicDelegatedPrefixes.update `  
` compute.publicDelegatedPrefixes.updatePolicy `  
` compute.publicDelegatedPrefixes.use `  
  
Cloud Data Fusion  |  Added  |  ` datafusion.instances.runtime `  
  
Customer Usage Data Processing API  |  Now GA  |  `
dataprocessing.featurecontrols.list `  
` dataprocessing.featurecontrols.update `  
` dataprocessing.groupcontrols.list `  
` dataprocessing.groupcontrols.update `  
  
Cloud Data Loss Prevention  |  Added  |  ` dlp.inspectFindings.list `  
` dlp.jobTriggers.hybridInspect `  
` dlp.jobs.hybridInspect `  
  
Cloud Data Loss Prevention  |  Now GA  |  ` dlp.inspectFindings.list `  
` dlp.jobTriggers.hybridInspect `  
` dlp.jobs.hybridInspect `  
  
GKE Hub  |  Now GA  |  ` gkehub.endpoints.connect `  
` gkehub.locations.get `  
` gkehub.locations.list `  
` gkehub.memberships.create `  
` gkehub.memberships.delete `  
` gkehub.memberships.generateConnectManifest `  
` gkehub.memberships.get `  
` gkehub.memberships.getIamPolicy `  
` gkehub.memberships.list `  
` gkehub.memberships.setIamPolicy `  
` gkehub.memberships.update `  
` gkehub.operations.cancel `  
` gkehub.operations.get `  
` gkehub.operations.list `  
  
Cloud Healthcare API  |  Added  |  `
healthcare.fhirResources.translateConceptMap `  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `
healthcare.fhirResources.translateConceptMap `  
  
Cloud Healthcare API  |  Now GA  |  `
healthcare.fhirResources.translateConceptMap `  
  
Recommender  |  Added  |  `
recommender.computeDiskIdleResourceRecommendations.get `  
` recommender.computeDiskIdleResourceRecommendations.list `  
` recommender.computeDiskIdleResourceRecommendations.update `  
  
Recommender  |  Supported In Custom Roles  |  `
recommender.computeDiskIdleResourceRecommendations.get `  
` recommender.computeDiskIdleResourceRecommendations.list `  
` recommender.computeDiskIdleResourceRecommendations.update `  
  
Recommender  |  Now GA  |  `
recommender.computeDiskIdleResourceRecommendations.get `  
` recommender.computeDiskIdleResourceRecommendations.list `  
` recommender.computeDiskIdleResourceRecommendations.update `  
  
  
##  Cloud IAM changes as of 2020-05-22

Service  |  Change  |  Description  
---|---|---  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/owner ` (Owner):

` apigee.appkeys.create `  
  
  
##  Cloud IAM changes as of 2020-03-27

Service  |  Change  |  Description  
---|---|---  
AI Platform Notebooks  |  Role Updated  |

The following permissions have been added to the role ` roles/notebooks.admin
` (Notebooks Admin):

` compute.acceleratorTypes.list `  
` compute.diskTypes.list `  
` compute.machineTypes.list `  
` compute.subnetworks.list `  
  
AI Platform Notebooks  |  Role Updated  |

The following permissions have been added to the role ` roles/notebooks.runner
` (Notebooks Runner):

` compute.acceleratorTypes.list `  
` compute.diskTypes.list `  
` compute.machineTypes.list `  
` compute.subnetworks.list `  
` notebooks.environments.get `  
` notebooks.environments.getIamPolicy `  
` notebooks.environments.list `  
` notebooks.instances.get `  
` notebooks.instances.getIamPolicy `  
` notebooks.instances.list `  
` notebooks.locations.get `  
` notebooks.locations.list `  
` notebooks.operations.get `  
` notebooks.operations.list `  
  
AI Platform Notebooks  |  Role Updated  |

The following permissions have been added to the role ` roles/notebooks.viewer
` (Notebooks Viewer):

` compute.acceleratorTypes.list `  
` compute.diskTypes.list `  
` compute.machineTypes.list `  
` compute.subnetworks.list `  
  
  
##  Cloud IAM changes as of 2020-03-20

Service  |  Change  |  Description  
---|---|---  
Data Catalog  |  Now GA  |

The role ` roles/datacatalog.admin ` (Data Catalog Admin) is now GA.  
  
Data Catalog  |  Now GA  |

The role ` roles/datacatalog.entryGroupCreator ` (DataCatalog EntryGroup
Creator) is now GA.  
  
Data Catalog  |  Now GA  |

The role ` roles/datacatalog.entryGroupOwner ` (DataCatalog entryGroup Owner)
is now GA.  
  
Data Catalog  |  Now GA  |

The role ` roles/datacatalog.entryOwner ` (DataCatalog entry Owner) is now GA.  
  
Data Catalog  |  Now GA  |

The role ` roles/datacatalog.entryViewer ` (DataCatalog Entry Viewer) is now
GA.  
  
Data Catalog  |  Now GA  |

The role ` roles/datacatalog.tagEditor ` (Data Catalog Tag Editor) is now GA.  
  
Data Catalog  |  Now GA  |

The role ` roles/datacatalog.tagTemplateCreator ` (Data Catalog TagTemplate
Creator) is now GA.  
  
Data Catalog  |  Now GA  |

The role ` roles/datacatalog.tagTemplateOwner ` (Data Catalog TagTemplate
Owner) is now GA.  
  
Data Catalog  |  Now GA  |

The role ` roles/datacatalog.tagTemplateUser ` (Data Catalog TagTemplate User)
is now GA.  
  
Data Catalog  |  Now GA  |

The role ` roles/datacatalog.tagTemplateViewer ` (Data Catalog TagTemplate
Viewer) is now GA.  
  
Data Catalog  |  Now GA  |

The role ` roles/datacatalog.viewer ` (Data Catalog Viewer) is now GA.  
  
Cloud Bigtable  |  Added  |  ` bigtable.keyvisualizer.get `  
` bigtable.keyvisualizer.list `  
  
Cloud Bigtable  |  Supported In Custom Roles  |  ` bigtable.keyvisualizer.get
`  
` bigtable.keyvisualizer.list `  
  
Cloud Bigtable  |  Now GA  |  ` bigtable.keyvisualizer.get `  
` bigtable.keyvisualizer.list `  
  
Cloud Asset Inventory  |  Added  |  ` cloudasset.assets.analyzeIamPolicy `  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `
cloudasset.assets.analyzeIamPolicy `  
  
Data Catalog  |  Supported In Custom Roles  |  ` datacatalog.entries.list `  
` datacatalog.entries.updateTag `  
` datacatalog.entryGroups.update `  
  
Data Catalog  |  Now GA  |  ` datacatalog.entries.create `  
` datacatalog.entries.delete `  
` datacatalog.entries.get `  
` datacatalog.entries.getIamPolicy `  
` datacatalog.entries.list `  
` datacatalog.entries.setIamPolicy `  
` datacatalog.entries.update `  
` datacatalog.entries.updateTag `  
` datacatalog.entryGroups.create `  
` datacatalog.entryGroups.delete `  
` datacatalog.entryGroups.get `  
` datacatalog.entryGroups.getIamPolicy `  
` datacatalog.entryGroups.list `  
` datacatalog.entryGroups.setIamPolicy `  
` datacatalog.entryGroups.update `  
` datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
Customer Usage Data Processing API  |  Added  |  `
dataprocessing.groupcontrols.list `  
` dataprocessing.groupcontrols.update `  
  
Customer Usage Data Processing API  |  Supported In Custom Roles  |  `
dataprocessing.featurecontrols.list `  
` dataprocessing.featurecontrols.update `  
` dataprocessing.groupcontrols.list `  
` dataprocessing.groupcontrols.update `  
  
Memorystore for Memcached  |  Added  |  ` memcache.instances.applyParameters `  
` memcache.instances.create `  
` memcache.instances.delete `  
` memcache.instances.get `  
` memcache.instances.list `  
` memcache.instances.update `  
` memcache.instances.updateParameters `  
` memcache.locations.get `  
` memcache.locations.list `  
` memcache.operations.cancel `  
` memcache.operations.delete `  
` memcache.operations.get `  
` memcache.operations.list `  
  
Memorystore for Memcached  |  Supported In Custom Roles  |  `
memcache.instances.applyParameters `  
` memcache.instances.create `  
` memcache.instances.delete `  
` memcache.instances.get `  
` memcache.instances.list `  
` memcache.instances.update `  
` memcache.instances.updateParameters `  
` memcache.locations.get `  
` memcache.locations.list `  
` memcache.operations.cancel `  
` memcache.operations.delete `  
` memcache.operations.get `  
` memcache.operations.list `  
  
Cloud OS Config  |  Added  |  ` osconfig.guestPolicies.create `  
` osconfig.guestPolicies.delete `  
` osconfig.guestPolicies.get `  
` osconfig.guestPolicies.list `  
` osconfig.guestPolicies.update `  
` osconfig.patchDeployments.create `  
` osconfig.patchDeployments.delete `  
` osconfig.patchDeployments.execute `  
` osconfig.patchDeployments.get `  
` osconfig.patchDeployments.list `  
` osconfig.patchDeployments.update `  
` osconfig.patchJobs.exec `  
` osconfig.patchJobs.get `  
` osconfig.patchJobs.list `  
  
Cloud OS Config  |  Supported In Custom Roles  |  `
osconfig.guestPolicies.create `  
` osconfig.guestPolicies.delete `  
` osconfig.guestPolicies.get `  
` osconfig.guestPolicies.list `  
` osconfig.guestPolicies.update `  
` osconfig.patchDeployments.create `  
` osconfig.patchDeployments.delete `  
` osconfig.patchDeployments.execute `  
` osconfig.patchDeployments.get `  
` osconfig.patchDeployments.list `  
` osconfig.patchDeployments.update `  
` osconfig.patchJobs.exec `  
` osconfig.patchJobs.get `  
` osconfig.patchJobs.list `  
  
  
##  Cloud IAM changes as of 2020-03-13

Service  |  Change  |  Description  
---|---|---  
Access Context Manager  |  Now GA  |

The role ` roles/accesscontextmanager.vpcScTroubleshooterViewer ` (VPC Service
Controls Troubleshooter Viewer) is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.annotationEditor ` (Healthcare Annotation Editor)
is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.annotationReader ` (Healthcare Annotation Reader)
is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.annotationStoreAdmin ` (Healthcare Annotation
Administrator) is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.annotationStoreViewer ` (Healthcare Annotation
Store Viewer) is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.datasetAdmin ` (Healthcare Dataset Administrator)
is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.datasetViewer ` (Healthcare Dataset Viewer) is now
GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.dicomEditor ` (Healthcare DICOM Editor) is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.dicomStoreAdmin ` (Healthcare DICOM Store
Administrator) is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.dicomStoreViewer ` (Healthcare DICOM Store Viewer)
is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.dicomViewer ` (Healthcare DICOM Viewer) is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.fhirResourceEditor ` (Healthcare FHIR Resource
Editor) is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.fhirResourceReader ` (Healthcare FHIR Resource
Reader) is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.fhirStoreAdmin ` (Healthcare FHIR Store
Administrator) is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.fhirStoreViewer ` (Healthcare FHIR Store Viewer)
is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.hl7V2Consumer ` (Healthcare HL7v2 Message
Consumer) is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.hl7V2Editor ` (Healthcare HL7v2 Message Editor) is
now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.hl7V2Ingest ` (Healthcare HL7v2 Message Ingest) is
now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.hl7V2StoreAdmin ` (Healthcare HL7v2 Store
Administrator) is now GA.  
  
Cloud Healthcare API  |  Now GA  |

The role ` roles/healthcare.hl7V2StoreViewer ` (Healthcare HL7v2 Store Viewer)
is now GA.  
  
Identity Platform  |  Role Updated  |

The following permissions have been added to the role `
roles/identityplatform.admin ` (Identity Platform Admin):

` firebaseauth.configs.create `  
` firebaseauth.configs.get `  
` firebaseauth.configs.getHashConfig `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Identity Platform  |  Role Updated  |

The following permissions have been added to the role `
roles/identityplatform.viewer ` (Identity Platform Viewer):

` firebaseauth.configs.get `  
` firebaseauth.users.get `  
  
AI Platform  |  Role Updated  |

The following permissions have been added to the role ` roles/ml.developer `
(ML Engine Developer):

` ml.studies.create `  
` ml.studies.delete `  
` ml.studies.get `  
` ml.studies.getIamPolicy `  
` ml.studies.list `  
` ml.studies.setIamPolicy `  
` ml.trials.create `  
` ml.trials.delete `  
` ml.trials.get `  
` ml.trials.list `  
` ml.trials.update `  
  
AI Platform  |  Role Updated  |

The following permissions have been added to the role ` roles/ml.viewer ` (ML
Engine Viewer):

` ml.studies.get `  
` ml.studies.getIamPolicy `  
` ml.studies.list `  
` ml.trials.get `  
` ml.trials.list `  
  
AI Platform Notebooks  |  Role Added  |

The role ` roles/notebooks.runner ` (Notebooks Runner) has been added with the
following permissions:

` notebooks.instances.create `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Recommender  |  Now GA  |

The role ` roles/recommender.firewallAdmin ` (Firewall Recommender Admin) is
now GA.  
  
Recommender  |  Now GA  |

The role ` roles/recommender.firewallViewer ` (Firewall Recommender Viewer) is
now GA.  
  
Cloud Asset Inventory  |  Added  |  ` cloudasset.assets.searchAllIamPolicies `  
` cloudasset.assets.searchAllResources `  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `
cloudasset.assets.searchAllIamPolicies `  
` cloudasset.assets.searchAllResources `  
  
Compute Engine  |  Added  |  ` compute.instances.getScreenshot `  
` compute.networks.access `  
  
Compute Engine  |  Supported In Custom Roles  |  `
compute.instances.getScreenshot `  
` compute.networks.access `  
  
Compute Engine  |  Now GA  |  ` compute.networks.access `  
  
Dataflow  |  Added  |  ` dataflow.jobs.snapshot `  
` dataflow.snapshots.delete `  
` dataflow.snapshots.get `  
` dataflow.snapshots.list `  
  
Dataflow  |  Supported In Custom Roles  |  ` dataflow.jobs.snapshot `  
` dataflow.snapshots.delete `  
` dataflow.snapshots.get `  
` dataflow.snapshots.list `  
  
Cloud Healthcare API  |  Added  |  ` healthcare.dicomStores.deidentify `  
` healthcare.fhirStores.deidentify `  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `
healthcare.dicomStores.deidentify `  
` healthcare.fhirStores.deidentify `  
` healthcare.operations.cancel `  
  
Cloud Healthcare API  |  Now GA  |  ` healthcare.datasets.create `  
` healthcare.datasets.deidentify `  
` healthcare.datasets.delete `  
` healthcare.datasets.get `  
` healthcare.datasets.getIamPolicy `  
` healthcare.datasets.list `  
` healthcare.datasets.setIamPolicy `  
` healthcare.datasets.update `  
` healthcare.dicomStores.create `  
` healthcare.dicomStores.deidentify `  
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
` healthcare.fhirStores.deidentify `  
` healthcare.fhirStores.delete `  
` healthcare.fhirStores.executeBundle `  
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
  
AI Platform  |  Added  |  ` ml.studies.create `  
` ml.studies.delete `  
` ml.studies.get `  
` ml.studies.getIamPolicy `  
` ml.studies.list `  
` ml.studies.setIamPolicy `  
` ml.trials.create `  
` ml.trials.delete `  
` ml.trials.get `  
` ml.trials.list `  
` ml.trials.update `  
  
AI Platform  |  Now GA  |  ` ml.studies.create `  
` ml.studies.delete `  
` ml.studies.get `  
` ml.studies.getIamPolicy `  
` ml.studies.list `  
` ml.studies.setIamPolicy `  
` ml.trials.create `  
` ml.trials.delete `  
` ml.trials.get `  
` ml.trials.list `  
` ml.trials.update `  
  
Recommender  |  Added  |  ` recommender.computeFirewallInsights.get `  
` recommender.computeFirewallInsights.list `  
` recommender.computeFirewallInsights.update `  
` recommender.computeInstanceIdleResourceRecommendations.get `  
` recommender.computeInstanceIdleResourceRecommendations.list `  
` recommender.computeInstanceIdleResourceRecommendations.update `  
` recommender.iamPolicyInsights.get `  
` recommender.iamPolicyInsights.list `  
` recommender.iamPolicyInsights.update `  
  
Recommender  |  Supported In Custom Roles  |  `
recommender.computeFirewallInsights.get `  
` recommender.computeFirewallInsights.list `  
` recommender.computeFirewallInsights.update `  
` recommender.computeInstanceIdleResourceRecommendations.get `  
` recommender.computeInstanceIdleResourceRecommendations.list `  
` recommender.computeInstanceIdleResourceRecommendations.update `  
` recommender.iamPolicyInsights.get `  
` recommender.iamPolicyInsights.list `  
` recommender.iamPolicyInsights.update `  
  
Recommender  |  Now GA  |  ` recommender.computeFirewallInsights.get `  
` recommender.computeFirewallInsights.list `  
` recommender.computeFirewallInsights.update `  
` recommender.computeInstanceIdleResourceRecommendations.get `  
` recommender.computeInstanceIdleResourceRecommendations.list `  
` recommender.computeInstanceIdleResourceRecommendations.update `  
` recommender.iamPolicyInsights.get `  
` recommender.iamPolicyInsights.list `  
` recommender.iamPolicyInsights.update `  
  
  
##  Cloud IAM changes as of 2020-03-06

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.networkAdmin ` (Compute Network Admin):

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.networkViewer ` (Compute Network Viewer):

` compute.acceleratorTypes.get `  
` compute.acceleratorTypes.list `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/editor `
(Editor):

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
  
Identity and Access Management  |  Role Updated  |

The following permissions have been added to the role `
roles/iam.securityAdmin ` (Security Admin):

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
Identity and Access Management  |  Role Updated  |

The following permissions have been added to the role `
roles/iam.securityReviewer ` (Security Reviewer):

` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.list `  
  
Identity Platform  |  Role Added  |

The role ` roles/identityplatform.admin ` (Identity Platform Admin) has been
added with the following permissions:

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
  
Identity Platform  |  Role Added  |

The role ` roles/identityplatform.viewer ` (Identity Platform Viewer) has been
added with the following permissions:

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
  
Network Management API  |  Now GA  |

The role ` roles/networkmanagement.admin ` (Network Management Admin) is now
GA.  
  
Network Management API  |  Now GA  |

The role ` roles/networkmanagement.viewer ` (Network Management Viewer) is now
GA.  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/owner ` (Owner):

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
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/viewer `
(Viewer):

` identityplatform.workloadPoolProviders.get `  
` identityplatform.workloadPoolProviders.list `  
` identityplatform.workloadPools.get `  
` identityplatform.workloadPools.list `  
` servicedirectory.locations.get `  
` servicedirectory.locations.list `  
  
BigQuery  |  Added  |  ` bigquery.bireservations.get `  
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
  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.bireservations.get `  
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
  
Identity Platform  |  Added  |  `
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
  
Network Management API  |  Now GA  |  `
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
  
Memorystore for Redis  |  Added  |  ` redis.instances.failover `  
` redis.instances.upgrade `  
  
Memorystore for Redis  |  Supported In Custom Roles  |  `
redis.instances.failover `  
` redis.instances.upgrade `  
  
Service Directory  |  Added  |  ` servicedirectory.endpoints.create `  
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
  
Service Directory  |  Supported In Custom Roles  |  `
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
  
  
##  Cloud IAM changes as of 2020-02-27

Service  |  Change  |  Description  
---|---|---  
BigQuery  |  Now GA  |

The role ` roles/bigquery.readSessionUser ` (BigQuery Read Session User) is
now GA.  
  
Data Catalog  |  Role Updated  |

The following permissions have been added to the role `
roles/datacatalog.entryGroupCreator ` (DataCatalog EntryGroup Creator):

` datacatalog.entryGroups.list `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/editor `
(Editor):

` dlp.jobs.create `  
` dlp.jobs.get `  
` dlp.jobs.list `  
  
Secret Manager  |  Role Updated  |

The following permissions have been added to the role `
roles/secretmanager.secretAccessor ` (Secret Manager Secret Accessor):

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Security Command Center  |  Role Updated  |

The following permissions have been added to the role `
roles/securitycenter.adminEditor ` (Security Center Admin Editor):

` securitycenter.organizationsettings.get `  
  
Security Command Center  |  Role Updated  |

The following permissions have been added to the role `
roles/securitycenter.adminViewer ` (Security Center Admin Viewer):

` securitycenter.organizationsettings.get `  
  
Cloud Spanner  |  Now GA  |

The role ` roles/spanner.backupAdmin ` (Cloud Spanner Backup Admin) is now GA.  
  
Cloud Spanner  |  Now GA  |

The role ` roles/spanner.backupWriter ` (Cloud Spanner Backup Writer) is now
GA.  
  
Cloud Spanner  |  Now GA  |

The role ` roles/spanner.restoreAdmin ` (Cloud Spanner Restore Admin) is now
GA.  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/viewer `
(Viewer):

` dlp.jobs.get `  
` dlp.jobs.list `  
  
BigQuery  |  Added  |  ` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
BigQuery  |  Now GA  |  ` bigquery.readsessions.create `  
` bigquery.readsessions.getData `  
` bigquery.readsessions.update `  
  
Data Catalog  |  Added  |  ` datacatalog.entryGroups.list `  
  
Data Catalog  |  Supported In Custom Roles  |  ` datacatalog.entryGroups.list
`  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `
healthcare.fhirStores.executeBundle `  
  
Identity and Access Management  |  Supported In Custom Roles  |  `
iam.serviceAccounts.getOpenIdToken `  
  
Cloud Spanner  |  Added  |  ` spanner.backupOperations.cancel `  
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
  
Cloud Spanner  |  Supported In Custom Roles  |  `
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
  
Cloud Spanner  |  Now GA  |  ` spanner.backupOperations.cancel `  
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
  
  
##  Cloud IAM changes as of 2020-02-21

Service  |  Change  |  Description  
---|---|---  
Access Context Manager  |  Added  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Access Context Manager  |  Now GA  |  `
accesscontextmanager.accessLevels.replaceAll `  
` accesscontextmanager.servicePerimeters.commit `  
` accesscontextmanager.servicePerimeters.replaceAll `  
  
Compute Engine  |  Added  |  ` compute.regionHealthCheckServices.create `  
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
  
Compute Engine  |  Supported In Custom Roles  |  `
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
  
  
##  Cloud IAM changes as of 2020-02-14

Service  |  Change  |  Description  
---|---|---  
Google Cloud Support  |  Now GA  |

The role ` roles/cloudsupport.techSupportEditor ` (Tech Support Editor) is now
GA.  
  
Google Cloud Support  |  Now GA  |

The role ` roles/cloudsupport.techSupportViewer ` (Tech Support Viewer) is now
GA.  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/editor `
(Editor):

` healthcare.fhirStores.executeBundle `  
  
Cloud Healthcare API  |  Role Updated  |

The following permissions have been added to the role `
roles/healthcare.fhirResourceEditor ` (Healthcare FHIR Resource Editor):

` healthcare.fhirStores.executeBundle `  
  
Cloud Healthcare API  |  Role Updated  |

The following permissions have been added to the role `
roles/healthcare.fhirResourceReader ` (Healthcare FHIR Resource Reader):

` healthcare.fhirStores.executeBundle `  
  
Cloud Logging  |  Role Updated  |

The following permissions have been added to the role `
roles/logging.privateLogViewer ` (Private Logs Viewer):

` logging.buckets.get `  
` logging.buckets.list `  
  
Cloud Logging  |  Role Updated  |

The following permissions have been added to the role ` roles/logging.viewer `
(Logs Viewer):

` logging.buckets.get `  
` logging.buckets.list `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/owner ` (Owner):

` healthcare.fhirStores.executeBundle `  
  
Security Command Center  |  Role Updated  |

The following permissions have been added to the role `
roles/securitycenter.admin ` (Security Center Admin):

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
  
Security Command Center  |  Role Updated  |

The following permissions have been added to the role `
roles/securitycenter.adminEditor ` (Security Center Admin Editor):

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
  
Security Command Center  |  Role Updated  |

The following permissions have been added to the role `
roles/securitycenter.adminViewer ` (Security Center Admin Viewer):

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
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/viewer `
(Viewer):

` healthcare.fhirStores.executeBundle `  
  
Google Cloud Support  |  Added  |  ` cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Google Cloud Support  |  Supported In Custom Roles  |  `
cloudsupport.properties.get `  
` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Google Cloud Support  |  Now GA  |  ` cloudsupport.techCases.create `  
` cloudsupport.techCases.escalate `  
` cloudsupport.techCases.get `  
` cloudsupport.techCases.list `  
` cloudsupport.techCases.update `  
  
Cloud Healthcare API  |  Added  |  ` healthcare.fhirStores.executeBundle `  
  
Cloud Logging  |  Added  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud Logging  |  Supported In Custom Roles  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
Cloud Logging  |  Now GA  |  ` logging.buckets.get `  
` logging.buckets.list `  
` logging.buckets.update `  
  
  
##  Cloud IAM changes as of 2020-02-07

Service  |  Change  |  Description  
---|---|---  
Secret Manager  |  Now GA  |

The role ` roles/secretmanager.admin ` (Secret Manager Admin) is now GA.  
  
Secret Manager  |  Now GA  |

The role ` roles/secretmanager.secretAccessor ` (Secret Manager Secret
Accessor) is now GA.  
  
Secret Manager  |  Now GA  |

The role ` roles/secretmanager.viewer ` (Secret Manager Viewer) is now GA.  
  
Cloud Healthcare API  |  Supported In Custom Roles  |  `
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
  
reCAPTCHA Enterprise  |  Added  |  ` recaptchaenterprise.assessments.annotate
`  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
reCAPTCHA Enterprise  |  Supported In Custom Roles  |  `
recaptchaenterprise.assessments.annotate `  
` recaptchaenterprise.assessments.create `  
` recaptchaenterprise.keys.create `  
` recaptchaenterprise.keys.delete `  
` recaptchaenterprise.keys.get `  
` recaptchaenterprise.keys.list `  
` recaptchaenterprise.keys.update `  
  
Secret Manager  |  Supported In Custom Roles  |  ` secretmanager.locations.get
`  
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
  
Secret Manager  |  Now GA  |  ` secretmanager.locations.get `  
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
  
  
##  Cloud IAM changes as of 2020-01-31

Service  |  Change  |  Description  
---|---|---  
Cloud Build  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudbuild.builds.builder ` (Cloud Build Service Account):

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
  
Cloud Composer  |  Role Updated  |

The following permissions have been added to the role ` roles/composer.worker
` (Composer Worker):

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
  
Google Cloud Game Servers  |  Added  |  `
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
  
Google Cloud Game Servers  |  Supported In Custom Roles  |  `
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
  
Google Cloud operations suite  |  Added  |  `
opsconfigmonitoring.resourceMetadata.write `  
  
  
##  Cloud IAM changes as of 2020-01-24

Service  |  Change  |  Description  
---|---|---  
Cloud Scheduler  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudscheduler.admin ` (Cloud Scheduler Admin):

` serviceusage.services.list `  
  
Cloud Scheduler  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudscheduler.jobRunner ` (Cloud Scheduler Job Runner):

` serviceusage.services.list `  
  
Cloud Scheduler  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudscheduler.viewer ` (Cloud Scheduler Viewer):

` serviceusage.services.list `  
  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.networkAdmin ` (Compute Network Admin):

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.networkViewer ` (Compute Network Viewer):

` compute.machineTypes.get `  
` compute.machineTypes.list `  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.notificationConfigEditor ` (Security Center
Notification Configurations Editor) is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.notificationConfigViewer ` (Security Center
Notification Configurations Viewer) is now GA.  
  
Artifact Registry  |  Added  |  ` artifactregistry.files.get `  
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
  
Artifact Registry  |  Supported In Custom Roles  |  `
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
  
Identity and Access Management  |  Added  |  `
iam.serviceAccounts.getOpenIdToken `  
  
Security Command Center  |  Added  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
Security Command Center  |  Supported In Custom Roles  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
Security Command Center  |  Now GA  |  `
securitycenter.notificationconfig.create `  
` securitycenter.notificationconfig.delete `  
` securitycenter.notificationconfig.get `  
` securitycenter.notificationconfig.list `  
` securitycenter.notificationconfig.update `  
  
  
##  Cloud IAM changes as of 2020-01-10

Service  |  Change  |  Description  
---|---|---  
Cloud Asset Inventory  |  Now GA  |

The role ` roles/cloudasset.owner ` (Cloud Asset Owner) is now GA.  
  
Migrate for Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudmigration.inframanager ` (Velostrata Manager):

` compute.globalOperations.get `  
  
Cloud Spanner  |  Role Updated  |

The following permissions have been added to the role `
roles/spanner.databaseReader ` (Cloud Spanner Database Reader):

` spanner.instances.get `  
  
Cloud Spanner  |  Role Updated  |

The following permissions have been added to the role `
roles/spanner.databaseUser ` (Cloud Spanner Database User):

` spanner.instances.get `  
  
Cloud Asset Inventory  |  Now GA  |  ` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Compute Engine  |  Added  |  ` compute.networks.listPeeringRoutes `  
  
Compute Engine  |  Supported In Custom Roles  |  `
compute.networks.listPeeringRoutes `  
  
Compute Engine  |  Now GA  |  ` compute.networks.listPeeringRoutes `  
  
Network Management API  |  Added  |  `
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
  
Network Management API  |  Supported In Custom Roles  |  `
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
  
  
##  Cloud IAM change as of 2019-12-20

Service  |  Change  |  Description  
---|---|---  
Migrate for Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudmigration.inframanager ` (Velostrata Manager):

` compute.disks.createSnapshot `  
` compute.snapshots.create `  
` compute.snapshots.delete `  
` compute.snapshots.get `  
` compute.snapshots.setLabels `  
` compute.snapshots.useReadOnly `  
  
Cloud Scheduler  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudscheduler.admin ` (Cloud Scheduler Admin):

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud Scheduler  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudscheduler.jobRunner ` (Cloud Scheduler Job Runner):

` appengine.applications.get `  
` serviceusage.services.get `  
  
Cloud Scheduler  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudscheduler.viewer ` (Cloud Scheduler Viewer):

` appengine.applications.get `  
` serviceusage.services.get `  
  
Compute Engine  |  Now GA  |

The role ` roles/compute.packetMirroringAdmin ` (Compute packet mirroring
admin) is now GA.  
  
Compute Engine  |  Now GA  |

The role ` roles/compute.packetMirroringUser ` (Compute packet mirroring user)
is now GA.  
  
Cloud DNS  |  Now GA  |

The role ` roles/dns.peer ` (DNS Peer) is now GA.  
  
Primitive Role  |  Role Updated  |

The following permissions have been removed from the role ` roles/editor `
(Editor):

` datacatalog.taxonomies.create `  
  
Recommender  |  Now GA  |

The role ` roles/recommender.computeAdmin ` (Compute Recommender Admin) is now
GA.  
  
Recommender  |  Now GA  |

The role ` roles/recommender.computeViewer ` (Compute Recommender Viewer) is
now GA.  
  
Recommender  |  Now GA  |

The role ` roles/recommender.iamAdmin ` (IAM Recommender Admin) is now GA.  
  
Recommender  |  Now GA  |

The role ` roles/recommender.iamViewer ` (IAM Recommender Viewer) is now GA.  
  
Remote Build Execution  |  Role Added  |

The role ` roles/remotebuildexecution.reservationAdmin ` (Remote Build
Execution Reservation Admin) has been added with the following permissions:

` remotebuildexecution.actions.create `  
` remotebuildexecution.actions.delete `  
` remotebuildexecution.actions.get `  
  
Cloud Bigtable  |  Added  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  Supported In Custom Roles  |  `
bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Cloud Bigtable  |  Now GA  |  ` bigtable.tables.getIamPolicy `  
` bigtable.tables.setIamPolicy `  
  
Compute Engine  |  Added  |  ` compute.nodeGroups.update `  
  
Compute Engine  |  Supported In Custom Roles  |  ` compute.nodeGroups.update `  
  
Compute Engine  |  Now GA  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Data Catalog  |  Added  |  ` datacatalog.entries.list `  
` datacatalog.entries.updateTag `  
` datacatalog.entryGroups.update `  
  
Dataproc  |  Added  |  ` dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
Dataproc  |  Now GA  |  ` dataproc.autoscalingPolicies.create `  
` dataproc.autoscalingPolicies.delete `  
` dataproc.autoscalingPolicies.get `  
` dataproc.autoscalingPolicies.getIamPolicy `  
` dataproc.autoscalingPolicies.list `  
` dataproc.autoscalingPolicies.setIamPolicy `  
` dataproc.autoscalingPolicies.update `  
` dataproc.autoscalingPolicies.use `  
  
Cloud DNS  |  Now GA  |  ` dns.networks.targetWithPeeringZone `  
  
Cloud Logging  |  Added  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud Logging  |  Supported In Custom Roles  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Cloud Logging  |  Now GA  |  ` logging.cmekSettings.get `  
` logging.cmekSettings.update `  
  
Recommender  |  Now GA  |  `
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
  
  
##  Cloud IAM changes as of 2019-11-22

Service  |  Change  |  Description  
---|---|---  
Data Catalog  |  Role Updated  |

The following permissions have been removed from the role `
roles/datacatalog.admin ` (Data Catalog Admin):

` datacatalog.categories.fineGrainedGet `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/editor `
(Editor):

` remotebuildexecution.actions.delete `  
  
Identity Toolkit API  |  Now GA  |

The role ` roles/identitytoolkit.admin ` (Identity Toolkit Admin) is now GA.  
  
Identity Toolkit API  |  Now GA  |

The role ` roles/identitytoolkit.viewer ` (Identity Toolkit Viewer) is now GA.  
  
Apigee API  |  Added  |  ` apigee.apiproductattributes.createOrUpdateAll `  
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
  
Apigee API  |  Supported In Custom Roles  |  `
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
  
BigQuery  |  Added  |  ` bigquery.tables.setCategory `  
  
Compute Engine  |  Added  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Compute Engine  |  Supported In Custom Roles  |  ` compute.networks.mirror `  
` compute.packetMirrorings.update `  
` compute.subnetworks.mirror `  
  
Remote Build Execution  |  Added  |  ` remotebuildexecution.actions.delete `  
  
Remote Build Execution  |  Supported In Custom Roles  |  `
remotebuildexecution.actions.delete `  
  
  
##  Cloud IAM changes as of 2019-11-14

Service  |  Change  |  Description  
---|---|---  
Access Approval  |  Added  |  ` accessapproval.settings.delete `  
  
AI Platform Notebooks  |  Added  |  ` notebooks.environments.create `  
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
  
AI Platform Notebooks  |  Supported In Custom Roles  |  `
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
  
  
##  Cloud IAM changes as of 2019-11-01

Service  |  Change  |  Description  
---|---|---  
Hangouts Chat API  |  Now GA  |

The role ` roles/chat.owner ` (Chat Bots Owner) is now GA.  
  
Hangouts Chat API  |  Now GA  |

The role ` roles/chat.reader ` (Chat Bots Viewer) is now GA.  
  
Hangouts Chat API  |  Now GA  |  ` chat.bots.get `  
` chat.bots.update `  
  
Cloud Asset Inventory  |  Added  |  `
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
  
Data Catalog  |  Added  |  ` datacatalog.categories.fineGrainedGet `  
` datacatalog.categories.getIamPolicy `  
` datacatalog.categories.setIamPolicy `  
` datacatalog.taxonomies.create `  
` datacatalog.taxonomies.delete `  
` datacatalog.taxonomies.get `  
` datacatalog.taxonomies.getIamPolicy `  
` datacatalog.taxonomies.list `  
` datacatalog.taxonomies.setIamPolicy `  
` datacatalog.taxonomies.update `  
  
Identity-Aware Proxy  |  Added  |  ` iap.projects.getSettings `  
` iap.projects.updateSettings `  
  
NetApp Cloud Volumes Service  |  Added  |  ` netappcloudvolumes.jobs.get `  
` netappcloudvolumes.jobs.list `  
  
Redis Enterprise Cloud  |  Added  |  ` redisenterprisecloud.databases.create `  
` redisenterprisecloud.databases.delete `  
` redisenterprisecloud.databases.get `  
` redisenterprisecloud.databases.list `  
` redisenterprisecloud.databases.update `  
` redisenterprisecloud.subscriptions.create `  
` redisenterprisecloud.subscriptions.delete `  
` redisenterprisecloud.subscriptions.get `  
` redisenterprisecloud.subscriptions.list `  
` redisenterprisecloud.subscriptions.update `  
  
  
##  Cloud IAM changes as of 2019-10-25

Service  |  Change  |  Description  
---|---|---  
Identity-Aware Proxy  |  Now GA  |

The role ` roles/iap.tunnelResourceAccessor ` (IAP-secured Tunnel User) is now
GA.  
  
Managed Service for Microsoft Active Directory  |  Now GA  |

The role ` roles/managedidentities.admin ` (Google Cloud Managed Identities
Admin) is now GA.  
  
Managed Service for Microsoft Active Directory  |  Now GA  |

The role ` roles/managedidentities.domainAdmin ` (Google Cloud Managed
Identities Domain Admin) is now GA.  
  
Managed Service for Microsoft Active Directory  |  Now GA  |

The role ` roles/managedidentities.viewer ` (Google Cloud Managed Identities
Viewer) is now GA.  
  
Actions API  |  Added  |  ` actions.agentVersions.get `  
  
Actions API  |  Supported In Custom Roles  |  ` actions.agentVersions.get `  
  
Actions API  |  Now GA  |  ` actions.agentVersions.get `  
  
Dialogflow  |  Added  |  ` dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
Dialogflow  |  Now GA  |  ` dialogflow.documents.create `  
` dialogflow.documents.delete `  
` dialogflow.documents.get `  
` dialogflow.documents.list `  
` dialogflow.knowledgeBases.create `  
` dialogflow.knowledgeBases.delete `  
` dialogflow.knowledgeBases.get `  
` dialogflow.knowledgeBases.list `  
  
Identity-Aware Proxy  |  Now GA  |  ` iap.tunnel.getIamPolicy `  
` iap.tunnel.setIamPolicy `  
` iap.tunnelInstances.accessViaIAP `  
` iap.tunnelInstances.getIamPolicy `  
` iap.tunnelInstances.setIamPolicy `  
` iap.tunnelZones.getIamPolicy `  
` iap.tunnelZones.setIamPolicy `  
  
Managed Service for Microsoft Active Directory  |  Now GA  |  `
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
  
  
##  Cloud IAM changes as of 2019-10-18

Service  |  Change  |  Description  
---|---|---  
Identity-Aware Proxy  |  Now GA  |

The role ` roles/iap.settingsAdmin ` (IAP Settings Admin) is now GA.  
  
Identity-Aware Proxy  |  Added  |  ` iap.web.getSettings `  
` iap.web.updateSettings `  
` iap.webServiceVersions.getSettings `  
` iap.webServiceVersions.updateSettings `  
` iap.webServices.getSettings `  
` iap.webServices.updateSettings `  
` iap.webTypes.getSettings `  
` iap.webTypes.updateSettings `  
  
  
##  Cloud IAM changes as of 2019-10-11

Service  |  Change  |  Description  
---|---|---  
Firebase Security Rules  |  Now GA  |

The role ` roles/firebaserules.admin ` (Firebase Rules Admin) is now GA.  
  
Firebase Security Rules  |  Now GA  |

The role ` roles/firebaserules.viewer ` (Firebase Rules Viewer) is now GA.  
  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Google Kubernetes Engine  |  Added  |  ` container.csiDrivers.create `  
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
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `
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
  
Google Kubernetes Engine  |  Now GA  |  ` container.csiDrivers.create `  
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
  
Firebase Security Rules  |  Now GA  |  ` firebaserules.releases.create `  
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
  
  
##  Cloud IAM changes as of 2019-10-04

Service  |  Change  |  Description  
---|---|---  
Actions API  |  Added  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Actions API  |  Supported In Custom Roles  |  `
actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Actions API  |  Now GA  |  ` actions.agent.claimContentProvider `  
` actions.agent.get `  
` actions.agent.update `  
` actions.agentVersions.create `  
` actions.agentVersions.delete `  
` actions.agentVersions.deploy `  
` actions.agentVersions.list `  
  
Identity and Access Management  |  Supported In Custom Roles  |  `
iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
  
  
##  Cloud IAM changes as of 2019-09-27

Service  |  Change  |  Description  
---|---|---  
Hangouts Chat API  |  Added  |  ` chat.bots.get `  
` chat.bots.update `  
  
Hangouts Chat API  |  Supported In Custom Roles  |  ` chat.bots.get `  
` chat.bots.update `  
  
Cloud Asset Inventory  |  Added  |  ` cloudasset.assets.exportAccessLevel `  
` cloudasset.assets.exportAccessPolicy `  
` cloudasset.assets.exportAllAccessPolicy `  
` cloudasset.assets.exportOrgPolicy `  
` cloudasset.assets.exportServicePerimeter `  
` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `
cloudasset.assets.exportAccessPolicy `  
` cloudasset.assets.exportOrgPolicy `  
` cloudasset.feeds.create `  
` cloudasset.feeds.delete `  
` cloudasset.feeds.get `  
` cloudasset.feeds.list `  
` cloudasset.feeds.update `  
  
Identity and Access Management  |  Supported In Custom Roles  |  `
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
  
VM Migration API  |  Added  |  ` vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
VM Migration API  |  Supported In Custom Roles  |  `
vmmigration.deployments.create `  
` vmmigration.deployments.get `  
` vmmigration.deployments.list `  
  
  
##  Cloud IAM changes as of 2019-09-20

Service  |  Change  |  Description  
---|---|---  
Cloud Key Management Service  |  Now GA  |

The role ` roles/cloudkms.importer ` (Cloud KMS Importer) is now GA.  
  
Cloud Key Management Service  |  Now GA  |

The role ` roles/cloudkms.publicKeyViewer ` (Cloud KMS CryptoKey Public Key
Viewer) is now GA.  
  
Cloud Key Management Service  |  Now GA  |

The role ` roles/cloudkms.signer ` (Cloud KMS CryptoKey Signer) is now GA.  
  
Cloud Key Management Service  |  Now GA  |

The role ` roles/cloudkms.signerVerifier ` (Cloud KMS CryptoKey
Signer/Verifier) is now GA.  
  
Cloud Key Management Service  |  Added  |  ` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  Supported In Custom Roles  |  `
cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
Cloud Key Management Service  |  Now GA  |  `
cloudkms.cryptoKeyVersions.useToSign `  
` cloudkms.cryptoKeyVersions.viewPublicKey `  
` cloudkms.importJobs.create `  
` cloudkms.importJobs.get `  
` cloudkms.importJobs.getIamPolicy `  
` cloudkms.importJobs.list `  
` cloudkms.importJobs.setIamPolicy `  
` cloudkms.importJobs.useToImport `  
  
  
##  Cloud IAM changes as of 2019-09-13

Service  |  Change  |  Description  
---|---|---  
Firebase Remote Config  |  Now GA  |

The role ` roles/cloudconfig.admin ` (Firebase Remote Config Admin) is now GA.  
  
Firebase Remote Config  |  Now GA  |

The role ` roles/cloudconfig.viewer ` (Firebase Remote Config Viewer) is now
GA.  
  
Firebase  |  Now GA  |

The role ` roles/firebase.admin ` (Firebase Admin) is now GA.  
  
Firebase  |  Now GA  |

The role ` roles/firebase.analyticsAdmin ` (Firebase Analytics Admin) is now
GA.  
  
Firebase  |  Now GA  |

The role ` roles/firebase.analyticsViewer ` (Firebase Analytics Viewer) is now
GA.  
  
Firebase  |  Now GA  |

The role ` roles/firebase.developAdmin ` (Firebase Develop Admin) is now GA.  
  
Firebase  |  Now GA  |

The role ` roles/firebase.developViewer ` (Firebase Develop Viewer) is now GA.  
  
Firebase  |  Now GA  |

The role ` roles/firebase.growthAdmin ` (Firebase Grow Admin) is now GA.  
  
Firebase  |  Now GA  |

The role ` roles/firebase.growthViewer ` (Firebase Grow Viewer) is now GA.  
  
Firebase  |  Now GA  |

The role ` roles/firebase.qualityAdmin ` (Firebase Quality Admin) is now GA.  
  
Firebase  |  Now GA  |

The role ` roles/firebase.qualityViewer ` (Firebase Quality Viewer) is now GA.  
  
Firebase  |  Now GA  |

The role ` roles/firebase.viewer ` (Firebase Viewer) is now GA.  
  
Firebase Authentication  |  Now GA  |

The role ` roles/firebaseauth.admin ` (Firebase Authentication Admin) is now
GA.  
  
Firebase Authentication  |  Now GA  |

The role ` roles/firebaseauth.viewer ` (Firebase Authentication Viewer) is now
GA.  
  
Firebase Crashlytics  |  Now GA  |

The role ` roles/firebasecrashlytics.admin ` (Firebase Crashlytics Admin) is
now GA.  
  
Firebase Crashlytics  |  Now GA  |

The role ` roles/firebasecrashlytics.viewer ` (Firebase Crashlytics Viewer) is
now GA.  
  
Firebase Realtime Database  |  Now GA  |

The role ` roles/firebasedatabase.admin ` (Firebase Realtime Database Admin)
is now GA.  
  
Firebase Realtime Database  |  Now GA  |

The role ` roles/firebasedatabase.viewer ` (Firebase Realtime Database Viewer)
is now GA.  
  
Firebase Dynamic Links  |  Now GA  |

The role ` roles/firebasedynamiclinks.admin ` (Firebase Dynamic Links Admin)
is now GA.  
  
Firebase Dynamic Links  |  Now GA  |

The role ` roles/firebasedynamiclinks.viewer ` (Firebase Dynamic Links Viewer)
is now GA.  
  
Firebase Hosting  |  Now GA  |

The role ` roles/firebasehosting.admin ` (Firebase Hosting Admin) is now GA.  
  
Firebase Hosting  |  Now GA  |

The role ` roles/firebasehosting.viewer ` (Firebase Hosting Viewer) is now GA.  
  
Firebase Cloud Messaging  |  Now GA  |

The role ` roles/firebasenotifications.admin ` (Firebase Cloud Messaging
Admin) is now GA.  
  
Firebase Cloud Messaging  |  Now GA  |

The role ` roles/firebasenotifications.viewer ` (Firebase Cloud Messaging
Viewer) is now GA.  
  
Firebase Performance Monitoring  |  Now GA  |

The role ` roles/firebaseperformance.admin ` (Firebase Performance Reporting
Admin) is now GA.  
  
Firebase Performance Monitoring  |  Now GA  |

The role ` roles/firebaseperformance.viewer ` (Firebase Performance Reporting
Viewer) is now GA.  
  
Firebase Predictions  |  Now GA  |

The role ` roles/firebasepredictions.admin ` (Firebase Predictions Admin) is
now GA.  
  
Firebase Predictions  |  Now GA  |

The role ` roles/firebasepredictions.viewer ` (Firebase Predictions Viewer) is
now GA.  
  
Firebase Remote Config  |  Now GA  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Cloud DNS  |  Now GA  |  ` dns.networks.bindPrivateDNSPolicy `  
` dns.policies.create `  
` dns.policies.delete `  
` dns.policies.get `  
` dns.policies.getIamPolicy `  
` dns.policies.list `  
` dns.policies.setIamPolicy `  
` dns.policies.update `  
  
Firebase  |  Now GA  |  ` firebase.billingPlans.get `  
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
  
Firebase Authentication  |  Now GA  |  ` firebaseauth.configs.create `  
` firebaseauth.configs.get `  
` firebaseauth.configs.getHashConfig `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Crashlytics  |  Now GA  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase Realtime Database  |  Now GA  |  ` firebasedatabase.instances.create
`  
` firebasedatabase.instances.get `  
` firebasedatabase.instances.list `  
` firebasedatabase.instances.update `  
  
Firebase Dynamic Links  |  Now GA  |  ` firebasedynamiclinks.destinations.list
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
  
Firebase Hosting  |  Now GA  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase Cloud Messaging  |  Now GA  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Performance Monitoring  |  Now GA  |  `
firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Predictions  |  Now GA  |  ` firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
NetApp Cloud Volumes Service  |  Added  |  `
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
  
Event Threat Detection  |  Supported In Custom Roles  |  `
threatdetection.detectorSettings.clear `  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  Cloud IAM changes as of 2019-09-06

Service  |  Change  |  Description  
---|---|---  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/owner ` (Owner):

` dataprocessing.iamaccesshistory.exportData `  
  
Serverless VPC Access  |  Now GA  |

The role ` roles/vpaccess.user ` (Serverless VPC Access User) is now GA.  
  
Serverless VPC Access  |  Now GA  |

The role ` roles/vpaccess.viewer ` (Serverless VPC Access Viewer) is now GA.  
  
Serverless VPC Access  |  Now GA  |

The role ` roles/vpcaccess.admin ` (Serverless VPC Access Admin) is now GA.  
  
Compute Engine  |  Added  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  Supported In Custom Roles  |  `
compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Compute Engine  |  Now GA  |  ` compute.externalVpnGateways.create `  
` compute.externalVpnGateways.delete `  
` compute.externalVpnGateways.get `  
` compute.externalVpnGateways.list `  
` compute.externalVpnGateways.setLabels `  
` compute.externalVpnGateways.use `  
  
Serverless VPC Access  |  Now GA  |  ` vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  Cloud IAM changes as of 2019-08-30

Service  |  Change  |  Description  
---|---|---  
Firebase Test Lab  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudtestservice.testAdmin ` (Firebase Test Lab Admin):

` firebase.clients.get `  
` firebase.projects.get `  
  
Firebase Test Lab  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudtestservice.testViewer ` (Firebase Test Lab Viewer):

` firebase.clients.get `  
` firebase.projects.get `  
  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.orgSecurityPolicyAdmin ` (Compute Organization Security Policy
Admin):

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.orgSecurityPolicyUser ` (Compute Organization Security Policy
User):

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.orgSecurityResourceAdmin ` (Compute Organization Resource
Admin):

` compute.globalOperations.get `  
` compute.globalOperations.getIamPolicy `  
` compute.globalOperations.list `  
` compute.globalOperations.setIamPolicy `  
  
  
##  Cloud IAM changes as of 2019-08-23

Service  |  Change  |  Description  
---|---|---  
Translation  |  Now GA  |

The role ` roles/cloudtranslate.admin ` (Cloud Translation API Admin) is now
GA.  
  
Translation  |  Now GA  |

The role ` roles/cloudtranslate.editor ` (Cloud Translation API Editor) is now
GA.  
  
Translation  |  Now GA  |

The role ` roles/cloudtranslate.user ` (Cloud Translation API User) is now GA.  
  
Translation  |  Now GA  |

The role ` roles/cloudtranslate.viewer ` (Cloud Translation API Viewer) is now
GA.  
  
Cloud Healthcare API  |  Role Updated  |

The following permissions have been added to the role `
roles/healthcare.dicomEditor ` (Healthcare DICOM Editor):

` healthcare.dicomStores.dicomWebDelete `  
  
Translation  |  Now GA  |  ` cloudtranslate.generalModels.batchPredict `  
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
  
  
##  Cloud IAM changes as of 2019-08-16

Service  |  Change  |  Description  
---|---|---  
Translation  |  Supported In Custom Roles  |  ` cloudtranslate.locations.get `  
` cloudtranslate.locations.list `  
  
Compute Engine  |  Now GA  |  ` compute.networks.updatePeering `  
  
Data Catalog  |  Added  |  ` datacatalog.entries.create `  
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
  
Data Catalog  |  Supported In Custom Roles  |  ` datacatalog.entries.create `  
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
  
  
##  Cloud IAM changes as of 2019-08-09

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.orgSecurityPolicyAdmin ` (Compute Organization Security Policy
Admin):

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.orgSecurityPolicyUser ` (Compute Organization Security Policy
User):

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.orgSecurityResourceAdmin ` (Compute organization resource
Admin):

` compute.projects.get `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
` serviceusage.quotas.get `  
` serviceusage.services.get `  
` serviceusage.services.list `  
  
Cloud Storage  |  Now GA  |

The role ` roles/storage.hmacKeyAdmin ` (Storage HMAC Key Admin) is now GA.  
  
Cloud Storage  |  Added  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
Cloud Storage  |  Supported In Custom Roles  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
Cloud Storage  |  Now GA  |  ` storage.hmacKeys.create `  
` storage.hmacKeys.delete `  
` storage.hmacKeys.get `  
` storage.hmacKeys.list `  
` storage.hmacKeys.update `  
  
  
##  Cloud IAM changes as of 2019-06-28

Service  |  Change  |  Description  
---|---|---  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/viewer `
(Viewer):

` pubsub.snapshots.seek `  
  
Firebase Crashlytics  |  Added  |  ` firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Firebase Crashlytics  |  Supported In Custom Roles  |  `
firebasecrashlytics.config.get `  
` firebasecrashlytics.config.update `  
` firebasecrashlytics.data.get `  
` firebasecrashlytics.issues.get `  
` firebasecrashlytics.issues.list `  
` firebasecrashlytics.issues.update `  
` firebasecrashlytics.sessions.get `  
  
Memorystore for Redis  |  Added  |  ` redis.instances.export `  
` redis.instances.import `  
  
Memorystore for Redis  |  Supported In Custom Roles  |  `
redis.instances.export `  
` redis.instances.import `  
  
  
##  Cloud IAM changes as of 2019-06-21

Service  |  Change  |  Description  
---|---|---  
Migrate for Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudmigration.inframanager ` (Velostrata Manager):

` compute.instances.updateShieldedInstanceConfig `  
  
Translation  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudtranslate.viewer ` (Cloud Translation API Viewer):

` cloudtranslate.operations.wait `  
  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.networkUser ` (Compute Network User):

` compute.vpnGateways.use `  
  
Firebase  |  Role Updated  |

The following permissions have been added to the role ` roles/firebase.admin `
(Firebase Admin):

` cloudmessaging.messages.create `  
  
Firebase  |  Role Updated  |

The following permissions have been added to the role `
roles/firebase.growthAdmin ` (Firebase Grow Admin):

` cloudmessaging.messages.create `  
  
Resource Manager  |  Role Updated  |

The following permissions have been added to the role `
roles/resourcemanager.projectMover ` (Project Mover):

` resourcemanager.projects.move `  
  
Security Command Center  |  Role Updated  |

The following permissions have been added to the role `
roles/securitycenter.adminEditor ` (Security Center Admin Editor):

` securitycenter.assets.group `  
` securitycenter.assets.list `  
` securitycenter.assets.listAssetPropertyNames `  
  
BigQuery  |  Added  |  ` bigquery.connections.create `  
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
  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.routines.create `  
` bigquery.routines.delete `  
` bigquery.routines.get `  
` bigquery.routines.list `  
` bigquery.routines.update `  
  
Translation  |  Supported In Custom Roles  |  `
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
  
Cloud Composer  |  Added  |  ` composer.imageversions.list `  
  
Cloud Composer  |  Supported In Custom Roles  |  ` composer.imageversions.list
`  
  
Cloud Composer  |  Now GA  |  ` composer.imageversions.list `  
  
Compute Engine  |  Added  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  Supported In Custom Roles  |  ` compute.vpnGateways.create
`  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
Compute Engine  |  Now GA  |  ` compute.vpnGateways.create `  
` compute.vpnGateways.delete `  
` compute.vpnGateways.get `  
` compute.vpnGateways.list `  
` compute.vpnGateways.setLabels `  
` compute.vpnGateways.use `  
  
  
##  Cloud IAM changes as of 2019-06-14

Service  |  Change  |  Description  
---|---|---  
Identity and Access Management  |  Now GA  |

The role ` roles/iam.workloadIdentityUser ` (Workload Identity User) is now
GA.  
  
Cloud Functions  |  Added  |  ` cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Cloud Functions  |  Supported In Custom Roles  |  `
cloudfunctions.functions.getIamPolicy `  
` cloudfunctions.functions.invoke `  
` cloudfunctions.functions.setIamPolicy `  
  
Compute Engine  |  Now GA  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  Cloud IAM changes as of 2019-05-31

Service  |  Change  |  Description  
---|---|---  
Data Catalog  |  Role Updated  |

The following permissions have been added to the role `
roles/datacatalog.admin ` (Data Catalog Admin):

` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
` pubsub.topics.updateTag `  
  
Migrate for Compute Engine  |  Added  |  `
cloudmigration.velostrataendpoints.connect `  
  
Identity and Access Management  |  Available In Custom Roles  |  `
iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.implicitDelegation `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
  
##  Cloud IAM changes as of 2019-05-24

Service  |  Change  |  Description  
---|---|---  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/viewer `
(Viewer):

` managedidentities.domains.validateTrust `  
  
Recommendations AI  |  Supported In Custom Roles  |  `
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
  
BigQuery  |  Added  |  ` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.datasets.updateTag `  
` bigquery.models.updateTag `  
` bigquery.tables.updateTag `  
  
Data Catalog  |  Added  |  ` datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
Data Catalog  |  Supported In Custom Roles  |  `
datacatalog.tagTemplates.create `  
` datacatalog.tagTemplates.delete `  
` datacatalog.tagTemplates.get `  
` datacatalog.tagTemplates.getIamPolicy `  
` datacatalog.tagTemplates.getTag `  
` datacatalog.tagTemplates.setIamPolicy `  
` datacatalog.tagTemplates.update `  
` datacatalog.tagTemplates.use `  
  
Filestore  |  Added  |  ` file.snapshots.update `  
  
Filestore  |  Supported In Custom Roles  |  ` file.snapshots.update `  
  
Pub/Sub  |  Added  |  ` pubsub.topics.updateTag `  
  
Pub/Sub  |  Supported In Custom Roles  |  ` pubsub.topics.updateTag `  
  
  
##  IAM changes as of 2019-05-17

Service  |  Change  |  Description  
---|---|---  
Dialogflow  |  Added  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  Supported In Custom Roles  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
Dialogflow  |  Now GA  |  ` dialogflow.agents.create `  
` dialogflow.agents.delete `  
  
  
##  Cloud IAM changes as of 2019-05-10

Service  |  Change  |  Description  
---|---|---  
Identity and Access Management  |  Now GA  |

The role ` roles/iam.securityAdmin ` (Security Admin) is now GA.  
  
Cloud IoT  |  Added  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  Supported In Custom Roles  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Cloud IoT  |  Now GA  |  ` cloudiot.devices.bindGateway `  
` cloudiot.devices.sendCommand `  
` cloudiot.devices.unbindGateway `  
  
Compute Engine  |  Supported In Custom Roles  |  ` compute.healthChecks.create
`  
` compute.healthChecks.delete `  
` compute.healthChecks.get `  
` compute.healthChecks.list `  
` compute.healthChecks.update `  
` compute.healthChecks.use `  
` compute.healthChecks.useReadOnly `  
` compute.instanceGroups.use `  
  
Cloud Healthcare API  |  Added  |  ` healthcare.fhirResources.purge `  
  
Managed Service for Microsoft Active Directory  |  Added  |  `
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
  
Managed Service for Microsoft Active Directory  |  Supported In Custom Roles
|  ` managedidentities.domains.attachTrust `  
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
  
  
##  Cloud IAM changes as of 2019-05-03

Service  |  Change  |  Description  
---|---|---  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.admin ` (Security Center Admin) is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.adminEditor ` (Security Center Admin Editor)
is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.adminViewer ` (Security Center Admin Viewer)
is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.assetsDiscoveryRunner ` (Security Center
Assets Discovery Runner) is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.assetSecurityMarksWriter ` (Security Center
Asset Security Marks Writer) is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.assetsViewer ` (Security Center Assets Viewer)
is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.findingSecurityMarksWriter ` (Security Center
Finding Security Marks Writer) is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.findingsEditor ` (Security Center Findings
Editor) is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.findingsStateSetter ` (Security Center
Findings State Setter) is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.findingsViewer ` (Security Center Findings
Viewer) is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.sourcesAdmin ` (Security Center Sources Admin)
is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.sourcesEditor ` (Security Center Sources
Editor) is now GA.  
  
Security Command Center  |  Now GA  |

The role ` roles/securitycenter.sourcesViewer ` (Security Center Sources
Viewer) is now GA.  
  
Recommendations AI  |  Added  |  ` automlrecommendations.apiKeys.create `  
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
  
BigQuery  |  Added  |  ` bigquery.models.create `  
` bigquery.models.delete `  
` bigquery.models.getData `  
` bigquery.models.getMetadata `  
` bigquery.models.list `  
` bigquery.models.updateData `  
` bigquery.models.updateMetadata `  
  
Firebase Cloud Messaging  |  Added  |  ` cloudmessaging.messages.create `  
  
Firebase Cloud Messaging  |  Supported In Custom Roles  |  `
cloudmessaging.messages.create `  
  
Firebase Cloud Messaging  |  Now GA  |  ` cloudmessaging.messages.create `  
  
Security Command Center  |  Now GA  |  ` securitycenter.assets.group `  
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
  
  
##  Cloud IAM changes as of 2019-04-19

Service  |  Change  |  Description  
---|---|---  
Primitive Role  |  Role Updated  |

The following permissions have been removed from the role ` roles/editor `
(Editor):

` firebasedynamiclinks.domains.delete `  
  
Security Command Center  |  Role Updated  |

The following permissions have been added to the role `
roles/securitycenter.admin ` (Security Center Admin):

` securitycenter.findings.setState `  
  
Security Command Center  |  Role Updated  |

The following permissions have been added to the role `
roles/securitycenter.adminEditor ` (Security Center Admin Editor):

` securitycenter.findings.setState `  
  
Security Command Center  |  Role Updated  |

The following permissions have been added to the role `
roles/securitycenter.findingsEditor ` (Security Center Findings Editor):

` securitycenter.findings.setState `  
  
Access Approval  |  Added  |  ` accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
Access Approval  |  Supported In Custom Roles  |  `
accessapproval.requests.approve `  
` accessapproval.requests.dismiss `  
` accessapproval.requests.get `  
` accessapproval.requests.list `  
` accessapproval.settings.get `  
` accessapproval.settings.update `  
  
Cloud Bigtable  |  Added  |  ` bigtable.locations.list `  
  
Cloud Bigtable  |  Supported In Custom Roles  |  ` bigtable.locations.list `  
  
Cloud Bigtable  |  Now GA  |  ` bigtable.locations.list `  
  
Cloud Scheduler  |  Added  |  ` cloudscheduler.locations.get `  
` cloudscheduler.locations.list `  
  
Compute Engine  |  Added  |  `
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
  
Compute Engine  |  Supported In Custom Roles  |  `
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
  
Compute Engine  |  Now GA  |  `
compute.networkEndpointGroups.attachNetworkEndpoints `  
` compute.networkEndpointGroups.create `  
` compute.networkEndpointGroups.delete `  
` compute.networkEndpointGroups.detachNetworkEndpoints `  
` compute.networkEndpointGroups.get `  
` compute.networkEndpointGroups.getIamPolicy `  
` compute.networkEndpointGroups.list `  
` compute.networkEndpointGroups.setIamPolicy `  
` compute.networkEndpointGroups.use `  
  
Remote Build Execution  |  Added  |  ` remotebuildexecution.actions.create `  
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
  
Remote Build Execution  |  Supported In Custom Roles  |  `
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
  
Serverless VPC Access  |  Added  |  ` vpcaccess.connectors.create `  
` vpcaccess.connectors.delete `  
` vpcaccess.connectors.get `  
` vpcaccess.connectors.list `  
` vpcaccess.connectors.use `  
` vpcaccess.locations.list `  
` vpcaccess.operations.get `  
` vpcaccess.operations.list `  
  
  
##  Cloud IAM changes as of 2019-03-29

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.networkUser ` (Compute Network User):

` servicenetworking.services.get `  
  
Cloud Monitoring  |  Role Updated  |

The following permissions have been added to the role ` roles/monitoring.admin
` (Monitoring Admin):

` serviceusage.services.enable `  
  
Cloud Monitoring  |  Role Updated  |

The following permissions have been added to the role `
roles/monitoring.editor ` (Monitoring Editor):

` serviceusage.services.enable `  
  
Google Cloud operations suite  |  Role Updated  |

The following permissions have been added to the role `
roles/stackdriver.accounts.editor ` (Stackdriver Accounts Editor):

` serviceusage.services.enable `  
  
Cloud SQL  |  Added  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  Supported In Custom Roles  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Cloud SQL  |  Now GA  |  ` cloudsql.instances.addServerCa `  
` cloudsql.instances.listServerCas `  
` cloudsql.instances.rotateServerCa `  
  
Translation  |  Added  |  ` cloudtranslate.generalModels.batchPredict `  
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
  
Cloud DNS  |  Added  |  ` dns.networks.targetWithPeeringZone `  
  
Cloud DNS  |  Supported In Custom Roles  |  `
dns.networks.targetWithPeeringZone `  
  
Event Threat Detection  |  Added  |  ` threatdetection.detectorSettings.clear
`  
` threatdetection.detectorSettings.get `  
` threatdetection.detectorSettings.update `  
` threatdetection.sinkSettings.get `  
` threatdetection.sinkSettings.update `  
` threatdetection.sourceSettings.get `  
` threatdetection.sourceSettings.update `  
  
  
##  Cloud IAM changes as of 2019-03-22

Service  |  Change  |  Description  
---|---|---  
Talent Solution  |  Now GA  |

The role ` roles/cloudjobdiscovery.admin ` (Admin) is now GA.  
  
Talent Solution  |  Now GA  |

The role ` roles/cloudjobdiscovery.jobsEditor ` (Job Editor) is now GA.  
  
Talent Solution  |  Now GA  |

The role ` roles/cloudjobdiscovery.jobsViewer ` (Job Viewer) is now GA.  
  
Talent Solution  |  Now GA  |

The role ` roles/cloudjobdiscovery.profilesEditor ` (Profile Editor) is now
GA.  
  
Talent Solution  |  Now GA  |

The role ` roles/cloudjobdiscovery.profilesViewer ` (Profile Viewer) is now
GA.  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/editor `
(Editor):

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Filestore  |  Role Updated  |

The following permissions have been added to the role ` roles/file.editor `
(Cloud Filestore Editor):

` file.instances.restore `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/owner ` (Owner):

` file.instances.restore `  
` healthcare.datasets.deidentify `  
  
Talent Solution  |  Now GA  |  ` cloudjobdiscovery.companies.create `  
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
  
Compute Engine  |  Added  |  ` compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  Supported In Custom Roles  |  `
compute.instances.getShieldedInstanceIdentity `  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Compute Engine  |  Now GA  |  ` compute.instances.getShieldedInstanceIdentity
`  
` compute.instances.getShieldedVmIdentity `  
` compute.instances.setShieldedInstanceIntegrityPolicy `  
` compute.instances.updateShieldedInstanceConfig `  
  
Filestore  |  Added  |  ` file.instances.restore `  
  
Firebase Authentication  |  Added  |  ` firebaseauth.configs.getHashConfig `  
  
Firebase Authentication  |  Supported In Custom Roles  |  `
firebaseauth.configs.getHashConfig `  
  
Cloud Healthcare API  |  Added  |  ` healthcare.datasets.create `  
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
  
  
##  Cloud IAM changes as of 2019-03-15

Service  |  Change  |  Description  
---|---|---  
Talent Solution  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudjobdiscovery.profilesEditor ` (Profile Editor):

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Talent Solution  |  Role Updated  |

The following permissions have been removed from the role `
roles/cloudjobdiscovery.profilesEditor ` (Profile Editor):

` cloudjobdiscovery.companies.create `  
` cloudjobdiscovery.companies.delete `  
` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.companies.update `  
  
Talent Solution  |  Role Updated  |

The following permissions have been added to the role `
roles/cloudjobdiscovery.profilesViewer ` (Profile Viewer):

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  Role Updated  |

The following permissions have been removed from the role `
roles/cloudjobdiscovery.profilesViewer ` (Profile Viewer):

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/editor `
(Editor):

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/owner ` (Owner):

` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Storage Transfer Service  |  Now GA  |

The role ` roles/storagetransfer.admin ` (Storage Transfer Admin) is now GA.  
  
Storage Transfer Service  |  Now GA  |

The role ` roles/storagetransfer.user ` (Storage Transfer User) is now GA.  
  
Storage Transfer Service  |  Now GA  |

The role ` roles/storagetransfer.viewer ` (Storage Transfer Viewer) is now GA.  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/viewer `
(Viewer):

` cloudjobdiscovery.tenants.get `  
  
Talent Solution  |  Added  |  ` cloudjobdiscovery.tenants.create `  
` cloudjobdiscovery.tenants.delete `  
` cloudjobdiscovery.tenants.get `  
` cloudjobdiscovery.tenants.update `  
  
Cloud DNS  |  Now GA  |  ` dns.networks.bindPrivateDNSZone `  
  
Cloud Run  |  Added  |  ` run.configurations.get `  
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
  
Cloud Run  |  Not Supported In Custom Roles  |  ` run.routes.invoke `  
  
Cloud Run  |  Supported In Custom Roles  |  ` run.configurations.get `  
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
  
Storage Transfer Service  |  Added  |  ` storagetransfer.jobs.create `  
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
  
Storage Transfer Service  |  Supported In Custom Roles  |  `
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
  
Storage Transfer Service  |  Now GA  |  ` storagetransfer.jobs.create `  
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
  
  
##  Cloud IAM changes as of 2019-03-07

Service  |  Change  |  Description  
---|---|---  
BigQuery  |  Role Added  |

The role ` roles/bigquery.connectionAdmin ` (BigQuery Connection Admin) has
been added with the following permissions:

` bigquery.connections.create `  
` bigquery.connections.delete `  
` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.setIamPolicy `  
` bigquery.connections.update `  
` bigquery.connections.use `  
  
BigQuery  |  Role Added  |

The role ` roles/bigquery.connectionUser ` (BigQuery Connection User) has been
added with the following permissions:

` bigquery.connections.get `  
` bigquery.connections.getIamPolicy `  
` bigquery.connections.list `  
` bigquery.connections.use `  
  
Dialogflow  |  Role Updated  |

The following permissions have been added to the role ` roles/dialogflow.admin
` (Dialogflow API Admin):

` dialogflow.agents.update `  
  
Dialogflow  |  Role Updated  |

The following permissions have been added to the role `
roles/dialogflow.consoleAgentEditor ` (Dialogflow Console Agent Editor):

` dialogflow.agents.update `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/editor `
(Editor):

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  Role Updated  |

The following permissions have been added to the role ` roles/file.editor `
(Cloud Filestore Editor):

` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Filestore  |  Role Updated  |

The following permissions have been added to the role ` roles/file.viewer `
(Cloud Filestore Viewer):

` file.snapshots.get `  
` file.snapshots.list `  
  
Identity and Access Management  |  Now GA  |

The role ` roles/iam.serviceAccountCreator ` (Create Service Accounts) is now
GA.  
  
Identity and Access Management  |  Role Updated  |

The following permissions have been added to the role `
roles/iam.securityReviewer ` (Security Reviewer):

` file.snapshots.list `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/owner ` (Owner):

` dialogflow.agents.update `  
` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
Service Usage  |  Role Updated  |

The following permissions have been added to the role `
roles/serviceusage.apiKeysAdmin ` (API Keys Admin):

` serviceusage.operations.get `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/viewer `
(Viewer):

` file.snapshots.get `  
` file.snapshots.list `  
  
AI Platform Data Labeling Service  |  Added  |  `
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
  
AI Platform Data Labeling Service  |  Supported In Custom Roles  |  `
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
  
Dialogflow  |  Added  |  ` dialogflow.agents.update `  
  
Filestore  |  Added  |  ` file.snapshots.create `  
` file.snapshots.delete `  
` file.snapshots.get `  
` file.snapshots.list `  
  
  
##  Cloud IAM changes as of 2019-03-01

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Role Updated  |

The following permissions have been added to the role `
roles/compute.instanceAdmin.v1 ` (Compute Instance Admin (v1)):

` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Dataproc  |  Role Added  |

The role ` roles/dataproc.admin ` (Dataproc Administrator) has been added with
the following permissions:

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
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/editor `
(Editor):

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
Identity and Access Management  |  Role Updated  |

The following permissions have been added to the role `
roles/iam.serviceAccountDeleter ` (Delete Service Accounts):

` iam.serviceAccounts.get `  
` iam.serviceAccounts.list `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/viewer `
(Viewer):

` dataproc.clusters.getIamPolicy `  
` dataproc.jobs.getIamPolicy `  
` dataproc.operations.getIamPolicy `  
  
AutoML  |  Added  |  ` automl.columnSpecs.get `  
` automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.export `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
AutoML  |  Supported In Custom Roles  |  ` automl.columnSpecs.list `  
` automl.columnSpecs.update `  
` automl.datasets.update `  
` automl.models.deploy `  
` automl.models.export `  
` automl.models.undeploy `  
` automl.tableSpecs.get `  
` automl.tableSpecs.list `  
` automl.tableSpecs.update `  
  
Compute Engine  |  Added  |  ` compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
Compute Engine  |  Supported In Custom Roles  |  `
compute.disks.addResourcePolicies `  
` compute.disks.removeResourcePolicies `  
` compute.resourcePolicies.create `  
` compute.resourcePolicies.delete `  
` compute.resourcePolicies.get `  
` compute.resourcePolicies.list `  
` compute.resourcePolicies.use `  
  
  
##  Cloud IAM changes as of 2019-02-15

Service  |  Change  |  Description  
---|---|---  
Access Context Manager  |  Now GA  |

The role ` roles/accesscontextmanager.policyAdmin ` (Access Context Manager
Admin) is now GA.  
  
Access Context Manager  |  Now GA  |

The role ` roles/accesscontextmanager.policyEditor ` (Access Context Manager
Editor) is now GA.  
  
Access Context Manager  |  Now GA  |

The role ` roles/accesscontextmanager.policyReader ` (Access Context Manager
Reader) is now GA.  
  
Talent Solution  |  Role Added  |

The role ` roles/cloudjobdiscovery.profilesEditor ` (Profile Editor) has been
added with the following permissions:

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
  
Talent Solution  |  Role Added  |

The role ` roles/cloudjobdiscovery.profilesViewer ` (Profile Viewer) has been
added with the following permissions:

` cloudjobdiscovery.companies.get `  
` cloudjobdiscovery.companies.list `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/editor `
(Editor):

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/owner ` (Owner):

` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
Primitive Role  |  Role Updated  |

The following permissions have been added to the role ` roles/viewer `
(Viewer):

` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
  
Google Cloud operations suite  |  Role Updated  |

The following permissions have been added to the role `
roles/stackdriver.accounts.editor ` (Stackdriver Account Editor):

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Google Cloud operations suite  |  Role Updated  |

The following permissions have been added to the role `
roles/stackdriver.accounts.viewer ` (Stackdriver Account Viewer):

` resourcemanager.projects.get `  
` resourcemanager.projects.list `  
  
Access Context Manager  |  Supported In Custom Roles  |  `
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
  
Access Context Manager  |  Now GA  |  `
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
  
Talent Solution  |  Added  |  ` cloudjobdiscovery.profiles.create `  
` cloudjobdiscovery.profiles.delete `  
` cloudjobdiscovery.profiles.get `  
` cloudjobdiscovery.profiles.search `  
` cloudjobdiscovery.profiles.update `  
  
  
##  Cloud IAM changes as of 2019-02-08

Service  |  Change  |  Description  
---|---|---  
Security Command Center  |  Supported In Custom Roles  |  `
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
  
  
##  Cloud IAM changes as of 2019-02-01

Service  |  Change  |  Description  
---|---|---  
Dialogflow  |  Now GA  |

The role ` roles/dialogflow.admin ` (Dialogflow API Admin) is now GA.  
  
Dialogflow  |  Now GA  |

The role ` roles/dialogflow.client ` (Dialogflow API Client) is now GA.  
  
Dialogflow  |  Now GA  |

The role ` roles/dialogflow.consoleAgentEditor ` (Dialogflow Console Agent
Editor) is now GA.  
  
Dialogflow  |  Now GA  |

The role ` roles/dialogflow.reader ` (Dialogflow API Reader) is now GA.  
  
Cloud Asset Inventory  |  Added  |  ` cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `
cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Cloud Asset Inventory  |  Now GA  |  ` cloudasset.assets.exportIamPolicy `  
` cloudasset.assets.exportResource `  
  
Dialogflow  |  Supported In Custom Roles  |  ` dialogflow.agents.search `  
` dialogflow.agents.train `  
  
Dialogflow  |  Now GA  |  ` dialogflow.agents.export `  
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
  
  
##  Cloud IAM changes as of 2019-01-25

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Added  |  ` compute.instances.updateDisplayDevice `  
  
  
##  Cloud IAM changes as of 2019-01-11

Service  |  Change  |  Description  
---|---|---  
Identity-Aware Proxy  |  Now GA  |

The role ` roles/iap.admin ` (IAP Policy Admin) is now GA.  
  
Identity-Aware Proxy  |  Supported In Custom Roles  |  ` iap.web.getIamPolicy
`  
` iap.web.setIamPolicy `  
` iap.webServiceVersions.accessViaIAP `  
` iap.webServiceVersions.getIamPolicy `  
` iap.webServiceVersions.setIamPolicy `  
` iap.webServices.getIamPolicy `  
` iap.webServices.setIamPolicy `  
` iap.webTypes.getIamPolicy `  
` iap.webTypes.setIamPolicy `  
  
  
##  Cloud IAM changes as of 2018-12-21

Service  |  Change  |  Description  
---|---|---  
Cloud DNS  |  Added  |  ` dns.networks.bindPrivateDNSZone `  
  
Cloud DNS  |  Supported In Custom Roles  |  ` dns.networks.bindPrivateDNSZone
`  
  
  
##  Cloud IAM changes as of 2018-12-14

Service  |  Change  |  Description  
---|---|---  
Firebase Authentication  |  Added  |  ` firebaseauth.configs.create `  
  
Firebase Authentication  |  Supported In Custom Roles  |  `
firebaseauth.configs.create `  
  
  
##  Cloud IAM changes as of 2018-12-07

Service  |  Change  |  Description  
---|---|---  
BigQuery  |  Added  |  ` bigquery.readsessions.create `  
  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.readsessions.create `  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `
container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
Google Kubernetes Engine  |  Now GA  |  ` container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  Cloud IAM changes as of 2018-11-30

Service  |  Change  |  Description  
---|---|---  
Cloud Asset Inventory  |  Now GA  |

The role ` roles/cloudasset.viewer ` (Cloud Asset Viewer) is now GA.  
  
Cloud Asset Inventory  |  Now GA  |  ` cloudasset.assets.exportAll `  
  
Compute Engine  |  Added  |  ` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
  
Compute Engine  |  Supported In Custom Roles  |  ` compute.disks.getIamPolicy
`  
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
  
Compute Engine  |  Now GA  |  ` compute.licenseCodes.getIamPolicy `  
` compute.licenseCodes.setIamPolicy `  
` compute.nodeGroups.getIamPolicy `  
` compute.nodeGroups.setIamPolicy `  
` compute.nodeTemplates.getIamPolicy `  
` compute.nodeTemplates.setIamPolicy `  
` compute.subnetworks.getIamPolicy `  
` compute.subnetworks.setIamPolicy `  
  
  
##  Cloud IAM changes as of 2018-11-16

Service  |  Change  |  Description  
---|---|---  
AutoML  |  Added  |  ` automl.locations.getIamPolicy `  
` automl.locations.setIamPolicy `  
  
AutoML  |  Supported In Custom Roles  |  ` automl.locations.getIamPolicy `  
` automl.locations.setIamPolicy `  
  
Talent Solution  |  Added  |  ` cloudjobdiscovery.events.create `  
` cloudjobdiscovery.events.delete `  
` cloudjobdiscovery.events.get `  
` cloudjobdiscovery.events.list `  
` cloudjobdiscovery.events.update `  
  
Compute Engine  |  Added  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  Supported In Custom Roles  |  `
compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Compute Engine  |  Now GA  |  ` compute.instanceTemplates.getIamPolicy `  
` compute.instanceTemplates.setIamPolicy `  
  
Google Kubernetes Engine  |  Added  |  ` container.backendConfigs.create `  
` container.backendConfigs.delete `  
` container.backendConfigs.get `  
` container.backendConfigs.list `  
` container.backendConfigs.update `  
` container.tokenReviews.create `  
  
  
##  Cloud IAM changes as of 2018-11-09

Service  |  Change  |  Description  
---|---|---  
Google Analytics  |  Added  |  `
firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
Google Analytics  |  Supported In Custom Roles  |  `
firebaseanalytics.resources.googleAnalyticsEdit `  
` firebaseanalytics.resources.googleAnalyticsReadAndAnalyze `  
  
  
##  Cloud IAM changes as of 2018-11-02

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Now GA  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  Supported In Custom Roles  |  ` file.instances.create `  
` file.instances.delete `  
` file.instances.get `  
` file.instances.list `  
` file.instances.update `  
` file.locations.get `  
` file.locations.list `  
` file.operations.get `  
` file.operations.list `  
  
Google Cloud operations suite  |  Added  |  `
stackdriver.resourceMetadata.write `  
  
Google Cloud operations suite  |  Supported In Custom Roles  |  `
stackdriver.resourceMetadata.write `  
  
  
##  Cloud IAM changes as of 2018-10-26

Service  |  Change  |  Description  
---|---|---  
BigQuery  |  Now GA  |

The role ` roles/bigquery.metadataViewer ` (BigQuery Metadata Viewer) is now
GA.  
  
Identity and Access Management  |  Now GA  |

The role ` roles/iam.serviceAccountDeleter ` (Delete Service Accounts) is now
GA.  
  
Firebase Realtime Database  |  Added  |  ` firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
Firebase Realtime Database  |  Supported In Custom Roles  |  `
firebasedatabase.instances.create `  
` firebasedatabase.instances.list `  
  
Firebase Integrations with External Services  |  Added  |  `
firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
Firebase Integrations with External Services  |  Supported In Custom Roles  |
` firebaseextensions.configs.create `  
` firebaseextensions.configs.delete `  
` firebaseextensions.configs.list `  
` firebaseextensions.configs.update `  
  
  
##  Cloud IAM changes as of 2018-10-19

Service  |  Change  |  Description  
---|---|---  
Google Cloud Support  |  Now GA  |

The role ` roles/cloudsupport.admin ` (Support Account Administrator) is now
GA.  
  
Google Cloud Support  |  Now GA  |

The role ` roles/cloudsupport.viewer ` (Support Account Viewer) is now GA.  
  
Firebase Remote Config  |  Added  |  ` cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Firebase Remote Config  |  Supported In Custom Roles  |  `
cloudconfig.configs.get `  
` cloudconfig.configs.update `  
  
Google Cloud Support  |  Supported In Custom Roles  |  `
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
  
Google Cloud Support  |  Now GA  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Compute Engine  |  Added  |  ` compute.networks.updatePeering `  
  
Compute Engine  |  Supported In Custom Roles  |  `
compute.networks.updatePeering `  
  
Firebase Crashlytics  |  Added  |  ` firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase Crashlytics  |  Supported In Custom Roles  |  `
firebasecrash.issues.update `  
` firebasecrash.reports.get `  
  
Firebase Dynamic Links  |  Added  |  ` firebasedynamiclinks.destinations.list
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
  
Firebase Dynamic Links  |  Supported In Custom Roles  |  `
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
  
Firebase In-App Messaging  |  Added  |  `
firebaseinappmessaging.campaigns.create `  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Firebase In-App Messaging  |  Supported In Custom Roles  |  `
firebaseinappmessaging.campaigns.create `  
` firebaseinappmessaging.campaigns.delete `  
` firebaseinappmessaging.campaigns.get `  
` firebaseinappmessaging.campaigns.list `  
` firebaseinappmessaging.campaigns.update `  
  
Firebase Cloud Messaging  |  Added  |  ` firebasenotifications.messages.create
`  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Cloud Messaging  |  Supported In Custom Roles  |  `
firebasenotifications.messages.create `  
` firebasenotifications.messages.delete `  
` firebasenotifications.messages.get `  
` firebasenotifications.messages.list `  
` firebasenotifications.messages.update `  
  
Firebase Performance Monitoring  |  Added  |  `
firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Performance Monitoring  |  Supported In Custom Roles  |  `
firebaseperformance.config.create `  
` firebaseperformance.config.delete `  
` firebaseperformance.config.update `  
` firebaseperformance.data.get `  
  
Firebase Predictions  |  Added  |  ` firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
Firebase Predictions  |  Supported In Custom Roles  |  `
firebasepredictions.predictions.create `  
` firebasepredictions.predictions.delete `  
` firebasepredictions.predictions.list `  
` firebasepredictions.predictions.update `  
  
Security Command Center  |  Added  |  ` securitycenter.assets.get `  
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
  
Service Consumer Management  |  Added  |  `
serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
Service Consumer Management  |  Supported In Custom Roles  |  `
serviceconsumermanagement.tenancyu.addResource `  
` serviceconsumermanagement.tenancyu.create `  
` serviceconsumermanagement.tenancyu.delete `  
` serviceconsumermanagement.tenancyu.list `  
` serviceconsumermanagement.tenancyu.removeResource `  
  
  
##  Cloud IAM changes as of 2018-10-12

Service  |  Change  |  Description  
---|---|---  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.admin ` (DLP Administrator) is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.analyzeRiskTemplatesEditor ` (DLP Analyze Risk Templates
Editor) is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.analyzeRiskTemplatesReader ` (DLP Analyze Risk Templates
Reader) is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.deidentifyTemplatesEditor ` (DLP De-identify Templates
Editor) is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.deidentifyTemplatesReader ` (DLP De-identify Templates
Reader) is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.inspectTemplatesEditor ` (DLP Inspect Templates Editor)
is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.inspectTemplatesReader ` (DLP Inspect Templates Reader)
is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.jobsEditor ` (DLP Jobs Editor) is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.jobsReader ` (DLP Jobs Reader) is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.jobTriggersEditor ` (DLP Job Triggers Editor) is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.jobTriggersReader ` (DLP Job Triggers Reader) is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.reader ` (DLP Reader) is now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.storedInfoTypesEditor ` (DLP Stored InfoTypes Editor) is
now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.storedInfoTypesReader ` (DLP Stored InfoTypes Reader) is
now GA.  
  
Cloud Data Loss Prevention  |  Now GA  |

The role ` roles/dlp.user ` (DLP User) is now GA.  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `
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
  
Cloud Data Loss Prevention  |  Supported In Custom Roles  |  `
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
  
Cloud Data Loss Prevention  |  Now GA  |  ` dlp.analyzeRiskTemplates.create `  
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
  
Cloud DNS  |  Supported In Custom Roles  |  ` dns.dnsKeys.get `  
` dns.dnsKeys.list `  
` dns.managedZoneOperations.get `  
` dns.managedZoneOperations.list `  
` dns.managedZones.update `  
  
Firebase  |  Added  |  ` firebase.billingPlans.get `  
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
  
Firebase  |  Supported In Custom Roles  |  ` firebase.billingPlans.get `  
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
  
Firebase A/B Testing  |  Added  |  ` firebaseabt.experimentresults.get `  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Firebase A/B Testing  |  Supported In Custom Roles  |  `
firebaseabt.experimentresults.get `  
` firebaseabt.experiments.create `  
` firebaseabt.experiments.delete `  
` firebaseabt.experiments.get `  
` firebaseabt.experiments.list `  
` firebaseabt.experiments.update `  
` firebaseabt.projectmetadata.get `  
  
Firebase Authentication  |  Added  |  ` firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Authentication  |  Supported In Custom Roles  |  `
firebaseauth.configs.get `  
` firebaseauth.configs.update `  
` firebaseauth.users.create `  
` firebaseauth.users.createSession `  
` firebaseauth.users.delete `  
` firebaseauth.users.get `  
` firebaseauth.users.sendEmail `  
` firebaseauth.users.update `  
  
Firebase Realtime Database  |  Added  |  ` firebasedatabase.instances.get `  
` firebasedatabase.instances.update `  
  
Firebase Realtime Database  |  Supported In Custom Roles  |  `
firebasedatabase.instances.get `  
` firebasedatabase.instances.update `  
  
Firebase Hosting  |  Added  |  ` firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
Firebase Hosting  |  Supported In Custom Roles  |  `
firebasehosting.sites.create `  
` firebasehosting.sites.delete `  
` firebasehosting.sites.get `  
` firebasehosting.sites.list `  
` firebasehosting.sites.update `  
  
ML Kit for Firebase  |  Added  |  ` firebaseml.compressionjobs.create `  
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
  
ML Kit for Firebase  |  Supported In Custom Roles  |  `
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
  
Firebase Security Rules  |  Added  |  ` firebaserules.releases.create `  
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
  
Firebase Security Rules  |  Supported In Custom Roles  |  `
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
  
  
##  Cloud IAM changes as of 2018-10-05

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Added  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  Supported In Custom Roles  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Compute Engine  |  Now GA  |  ` compute.instances.resume `  
` compute.instances.suspend `  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `
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
  
Google Kubernetes Engine  |  Now GA  |  ` container.cronJobs.getStatus `  
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
  
  
##  Cloud IAM changes as of 2018-09-21

Service  |  Change  |  Description  
---|---|---  
AutoML  |  Added  |  ` automl.datasets.getIamPolicy `  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
AutoML  |  Supported In Custom Roles  |  ` automl.datasets.getIamPolicy `  
` automl.datasets.setIamPolicy `  
` automl.models.getIamPolicy `  
` automl.models.setIamPolicy `  
  
Cloud Asset Inventory  |  Added  |  ` cloudasset.assets.exportAll `  
  
Cloud Asset Inventory  |  Supported In Custom Roles  |  `
cloudasset.assets.exportAll `  
  
Compute Engine  |  Added  |  ` compute.licenses.delete `  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `
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
  
  
##  Cloud IAM changes as of 2018-09-07

Service  |  Change  |  Description  
---|---|---  
Memorystore for Redis  |  Supported In Custom Roles  |  `
redis.operations.cancel `  
` redis.operations.delete `  
  
  
##  Cloud IAM changes as of 2018-08-31

Service  |  Change  |  Description  
---|---|---  
Google Kubernetes Engine  |  Added  |  ` container.cronJobs.getStatus `  
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
  
Cloud Data Loss Prevention  |  Added  |  ` dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud Data Loss Prevention  |  Supported In Custom Roles  |  `
dlp.storedInfoTypes.create `  
` dlp.storedInfoTypes.delete `  
` dlp.storedInfoTypes.get `  
` dlp.storedInfoTypes.list `  
` dlp.storedInfoTypes.update `  
  
Cloud Source Repositories  |  Added  |  ` source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud Source Repositories  |  Supported In Custom Roles  |  `
source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
Cloud Source Repositories  |  Now GA  |  ` source.repos.getProjectConfig `  
` source.repos.updateProjectConfig `  
` source.repos.updateRepoConfig `  
  
  
##  Cloud IAM changes as of 2018-08-10

Service  |  Change  |  Description  
---|---|---  
Binary Authorization  |  Added  |  `
binaryauthorization.attestors.verifyImageAttested `  
  
Binary Authorization  |  Supported In Custom Roles  |  `
binaryauthorization.attestors.verifyImageAttested `  
  
Compute Engine  |  Added  |  ` compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Compute Engine  |  Supported In Custom Roles  |  `
compute.globalAddresses.createInternal `  
` compute.globalAddresses.deleteInternal `  
  
Filestore  |  Added  |  ` file.instances.create `  
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
  
  
##  Cloud IAM changes as of 2018-08-03

Service  |  Change  |  Description  
---|---|---  
Android Management API  |  Supported In Custom Roles  |  `
androidmanagement.enterprises.manage `  
  
Android Management API  |  Now GA  |  ` androidmanagement.enterprises.manage `  
  
Cloud Billing  |  Supported In Custom Roles  |  ` billing.resourceCosts.get `  
  
Binary Authorization  |  Added  |  ` binaryauthorization.policy.get `  
` binaryauthorization.policy.getIamPolicy `  
` binaryauthorization.policy.setIamPolicy `  
` binaryauthorization.policy.update `  
  
Cloud Composer  |  Now GA  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Compute Engine  |  Now GA  |  ` compute.nodeGroups.addNodes `  
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
  
Google Kubernetes Engine  |  Now GA  |  ` container.hostServiceAgent.use `  
  
Memorystore for Redis  |  Added  |  ` redis.operations.cancel `  
  
Memorystore for Redis  |  Supported In Custom Roles  |  `
redis.instances.create `  
` redis.instances.delete `  
` redis.instances.get `  
` redis.instances.list `  
` redis.instances.update `  
` redis.locations.get `  
` redis.locations.list `  
` redis.operations.get `  
` redis.operations.list `  
  
Subscribe with Google  |  Added  |  ` subscribewithgoogledeveloper.tools.get `  
  
Subscribe with Google  |  Supported In Custom Roles  |  `
subscribewithgoogledeveloper.tools.get `  
  
  
##  Cloud IAM changes as of 2018-07-20

Service  |  Change  |  Description  
---|---|---  
Access Context Manager  |  Added  |  `
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
  
AutoML  |  Added  |  ` automl.annotationSpecs.create `  
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
  
AutoML  |  Supported In Custom Roles  |  ` automl.annotationSpecs.create `  
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
  
Binary Authorization  |  Added  |  ` binaryauthorization.attestors.create `  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
Binary Authorization  |  Supported In Custom Roles  |  `
binaryauthorization.attestors.create `  
` binaryauthorization.attestors.delete `  
` binaryauthorization.attestors.get `  
` binaryauthorization.attestors.getIamPolicy `  
` binaryauthorization.attestors.list `  
` binaryauthorization.attestors.setIamPolicy `  
` binaryauthorization.attestors.update `  
  
Cloud DNS  |  Supported In Custom Roles  |  ` dns.changes.create `  
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
  
  
##  Cloud IAM changes as of 2018-07-13

Service  |  Change  |  Description  
---|---|---  
BigQuery  |  Added  |  ` bigquery.datasets.getIamPolicy `  
` bigquery.datasets.setIamPolicy `  
  
Datastore  |  Added  |  ` datastore.locations.get `  
` datastore.locations.list `  
  
  
##  Cloud IAM changes as of 2018-07-06

Service  |  Change  |  Description  
---|---|---  
Cloud Composer  |  Supported In Custom Roles  |  `
composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Endpoints  |  Added  |  ` endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud Endpoints  |  Supported In Custom Roles  |  `
endpoints.portals.attachCustomDomain `  
` endpoints.portals.detachCustomDomain `  
` endpoints.portals.listCustomDomains `  
` endpoints.portals.update `  
  
Cloud TPU  |  Added  |  ` tpu.acceleratortypes.get `  
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
  
Cloud TPU  |  Supported In Custom Roles  |  ` tpu.acceleratortypes.get `  
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
  
  
##  Cloud IAM changes as of 2018-06-29

Service  |  Change  |  Description  
---|---|---  
Identity and Access Management  |  Now GA  |  `
iam.serviceAccounts.implicitDelegation `  
  
  
##  Cloud IAM changes as of 2018-06-15

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Supported In Custom Roles  |  `
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
  
Compute Engine  |  Now GA  |  ` compute.regionBackendServices.create `  
` compute.regionBackendServices.delete `  
` compute.regionBackendServices.get `  
` compute.regionBackendServices.list `  
` compute.regionBackendServices.setSecurityPolicy `  
` compute.regionBackendServices.update `  
` compute.regionBackendServices.use `  
  
  
##  Cloud IAM changes as of 2018-06-08

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Added  |  ` compute.nodeGroups.addNodes `  
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
  
Compute Engine  |  Supported In Custom Roles  |  ` compute.nodeGroups.addNodes
`  
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
  
  
##  Cloud IAM changes as of 2018-05-11

Service  |  Change  |  Description  
---|---|---  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.jobs.listAll `  
  
Cloud Bigtable  |  Supported In Custom Roles  |  ` bigtable.appProfiles.create
`  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.clusters.create `  
` bigtable.clusters.delete `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Bigtable  |  Now GA  |  ` bigtable.appProfiles.create `  
` bigtable.appProfiles.delete `  
` bigtable.appProfiles.get `  
` bigtable.appProfiles.list `  
` bigtable.appProfiles.update `  
` bigtable.tables.checkConsistency `  
` bigtable.tables.generateConsistencyToken `  
  
Cloud Composer  |  Now Beta  |  ` composer.environments.create `  
` composer.environments.delete `  
` composer.environments.get `  
` composer.environments.list `  
` composer.environments.update `  
` composer.operations.delete `  
` composer.operations.get `  
` composer.operations.list `  
  
Cloud Life Sciences  |  Supported In Custom Roles  |  `
genomics.operations.cancel `  
` genomics.operations.create `  
` genomics.operations.get `  
` genomics.operations.list `  
  
Cloud Monitoring  |  Supported In Custom Roles  |  `
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
  
Cloud Monitoring  |  Now GA  |  ` monitoring.dashboards.create `  
` monitoring.dashboards.delete `  
` monitoring.dashboards.get `  
` monitoring.dashboards.list `  
` monitoring.dashboards.update `  
` monitoring.publicWidgets.create `  
` monitoring.publicWidgets.delete `  
` monitoring.publicWidgets.get `  
` monitoring.publicWidgets.list `  
` monitoring.publicWidgets.update `  
  
  
##  Cloud IAM changes as of 2018-05-04

Service  |  Change  |  Description  
---|---|---  
BigQuery  |  Available In Custom Roles  |  ` bigquery.jobs.listAll `  
  
Cloud Bigtable  |  Added  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  Supported In Custom Roles  |  `
bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Cloud Bigtable  |  Now GA  |  ` bigtable.instances.getIamPolicy `  
` bigtable.instances.setIamPolicy `  
  
Compute Engine  |  Supported In Custom Roles  |  `
compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  Now GA  |  ` compute.oslogin.updateExternalUser `  
  
Service Management  |  Supported In Custom Roles  |  `
servicemanagement.services.bind `  
  
  
##  Cloud IAM changes as of 2018-04-06

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Supported In Custom Roles  |  `
compute.instances.setShieldedVmIntegrityPolicy `  
` compute.instances.updateShieldedVmConfig `  
  
Compute Engine  |  Now GA  |  ` compute.instances.setShieldedVmIntegrityPolicy
`  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `
container.hostServiceAgent.use `  
  
Dataproc  |  Supported In Custom Roles  |  ` dataproc.jobs.getIamPolicy `  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
Dataproc  |  Now GA  |  ` dataproc.jobs.getIamPolicy `  
` dataproc.jobs.setIamPolicy `  
` dataproc.operations.getIamPolicy `  
` dataproc.operations.setIamPolicy `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.setIamPolicy `  
  
  
##  Cloud IAM changes as of 2018-03-30

Service  |  Change  |  Description  
---|---|---  
Cloud IoT  |  Now GA  |  ` cloudiot.devices.create `  
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
  
  
##  Cloud IAM changes as of 2018-03-23

Service  |  Change  |  Description  
---|---|---  
Cloud Life Sciences  |  Supported In Custom Roles  |  `
genomics.datasets.create `  
` genomics.datasets.delete `  
` genomics.datasets.get `  
` genomics.datasets.getIamPolicy `  
` genomics.datasets.list `  
` genomics.datasets.setIamPolicy `  
` genomics.datasets.update `  
  
Pub/Sub  |  Supported In Custom Roles  |  ` pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.list `  
  
  
##  Cloud IAM changes as of 2018-03-09

Service  |  Change  |  Description  
---|---|---  
Talent Solution  |  Added  |  ` cloudjobdiscovery.companies.create `  
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
  
Talent Solution  |  Supported In Custom Roles  |  `
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
  
Cloud Profiler  |  Added  |  ` cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
Cloud Profiler  |  Supported In Custom Roles  |  `
cloudprofiler.profiles.create `  
` cloudprofiler.profiles.list `  
` cloudprofiler.profiles.update `  
  
  
##  Cloud IAM changes as of 2018-03-02

Service  |  Change  |  Description  
---|---|---  
Open Service Broker for Google Cloud  |  Added  |  `
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
  
Open Service Broker for Google Cloud  |  Supported In Custom Roles  |  `
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
  
  
##  Cloud IAM changes as of 2018-02-23

Service  |  Change  |  Description  
---|---|---  
Resource Manager  |  Supported In Custom Roles  |  `
resourcemanager.projects.list `  
` resourcemanager.projects.move `  
  
Service Management  |  Added  |  ` servicemanagement.services.quota `  
  
Service Management  |  Supported In Custom Roles  |  `
servicemanagement.services.quota `  
  
Cloud Source Repositories  |  Supported In Custom Roles  |  `
source.repos.create `  
  
  
##  Cloud IAM changes as of 2018-02-16

Service  |  Change  |  Description  
---|---|---  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.tables.update `  
` bigquery.tables.updateData `  
  
Cloud IoT  |  Supported In Custom Roles  |  ` cloudiot.devices.create `  
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
  
Cloud SQL  |  Supported In Custom Roles  |  ` cloudsql.instances.demoteMaster
`  
  
Google Cloud Support  |  Added  |  ` cloudsupport.accounts.create `  
` cloudsupport.accounts.delete `  
` cloudsupport.accounts.get `  
` cloudsupport.accounts.getIamPolicy `  
` cloudsupport.accounts.getUserRoles `  
` cloudsupport.accounts.list `  
` cloudsupport.accounts.setIamPolicy `  
` cloudsupport.accounts.update `  
` cloudsupport.accounts.updateUserRoles `  
` cloudsupport.operations.get `  
  
Compute Engine  |  Added  |  ` compute.oslogin.updateExternalUser `  
  
Compute Engine  |  Supported In Custom Roles  |  ` compute.addresses.create `  
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
  
Dataproc  |  Supported In Custom Roles  |  ` dataproc.agents.create `  
` dataproc.agents.delete `  
` dataproc.agents.get `  
` dataproc.agents.list `  
` dataproc.agents.update `  
` dataproc.tasks.lease `  
` dataproc.tasks.listInvalidatedLeases `  
` dataproc.tasks.reportStatus `  
` dataproc.workflowTemplates.instantiateInline `  
  
Cloud DNS  |  Added  |  ` dns.changes.create `  
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
  
  
##  Cloud IAM changes as of 2018-02-02

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Available In Custom Roles  |  `
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
  
Cloud Data Loss Prevention  |  Added  |  ` dlp.jobTriggers.create `  
` dlp.jobTriggers.delete `  
` dlp.jobTriggers.get `  
` dlp.jobTriggers.list `  
` dlp.jobTriggers.update `  
  
  
##  Cloud IAM changes as of 2018-01-26

Service  |  Change  |  Description  
---|---|---  
BigQuery  |  Added  |  ` bigquery.jobs.listAll `  
  
Google Kubernetes Engine  |  Added  |  ` container.podSecurityPolicies.create
`  
` container.podSecurityPolicies.delete `  
` container.podSecurityPolicies.get `  
` container.podSecurityPolicies.list `  
` container.podSecurityPolicies.update `  
` container.podSecurityPolicies.use `  
  
  
##  Cloud IAM changes as of 2018-01-19

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Added  |  ` compute.addresses.createInternal `  
` compute.addresses.deleteInternal `  
` compute.addresses.useInternal `  
  
  
##  Cloud IAM changes as of 2018-01-12

Service  |  Change  |  Description  
---|---|---  
App Engine  |  Not Supported In Custom Roles  |  `
appengine.runtimes.actAsAdmin `  
  
Compute Engine  |  Added  |  ` compute.backendServices.setSecurityPolicy `  
` compute.securityPolicies.create `  
` compute.securityPolicies.delete `  
` compute.securityPolicies.get `  
` compute.securityPolicies.getIamPolicy `  
` compute.securityPolicies.list `  
` compute.securityPolicies.setIamPolicy `  
` compute.securityPolicies.update `  
` compute.securityPolicies.use `  
  
Compute Engine  |  Not Supported In Custom Roles  |  `
compute.organizations.administerXpn `  
` compute.targetHttpProxies.create `  
` compute.targetHttpProxies.setUrlMap `  
` compute.targetHttpsProxies.create `  
` compute.targetHttpsProxies.setUrlMap `  
` compute.targetSslProxies.create `  
` compute.targetSslProxies.setBackendService `  
` compute.targetTcpProxies.create `  
` compute.targetTcpProxies.update `  
  
Compute Engine  |  Now GA  |  ` compute.instances.osAdminLogin `  
` compute.instances.osLogin `  
  
  
##  Cloud IAM changes as of 2017-12-22

Service  |  Change  |  Description  
---|---|---  
App Engine  |  Supported In Custom Roles  |  ` appengine.applications.create `  
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
  
App Engine  |  Not Supported In Custom Roles  |  ` appengine.applications.list
`  
` appengine.operations.cancel `  
` appengine.operations.delete `  
` appengine.services.create `  
  
Cloud Billing  |  Supported In Custom Roles  |  ` billing.accounts.close `  
` billing.accounts.reopen `  
` billing.budgets.delete `  
` billing.budgets.update `  
  
Cloud Debugger  |  Supported In Custom Roles  |  `
clouddebugger.breakpoints.create `  
` clouddebugger.breakpoints.delete `  
` clouddebugger.breakpoints.get `  
` clouddebugger.breakpoints.list `  
` clouddebugger.breakpoints.listActive `  
` clouddebugger.breakpoints.update `  
` clouddebugger.debuggees.create `  
` clouddebugger.debuggees.list `  
  
Cloud Key Management Service  |  Supported In Custom Roles  |  `
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
  
Cloud SQL  |  Supported In Custom Roles  |  ` cloudsql.backupRuns.create `  
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
  
Cloud SQL  |  Not Supported In Custom Roles  |  `
cloudsql.databases.getIamPolicy `  
` cloudsql.databases.setIamPolicy `  
` cloudsql.instances.demoteMaster `  
` cloudsql.instances.getIamPolicy `  
` cloudsql.instances.migrate `  
` cloudsql.instances.setIamPolicy `  
` cloudsql.sslCerts.createEphemeral `  
  
Cloud Trace  |  Supported In Custom Roles  |  ` cloudtrace.insights.get `  
` cloudtrace.insights.list `  
` cloudtrace.stats.get `  
` cloudtrace.tasks.create `  
` cloudtrace.tasks.delete `  
` cloudtrace.tasks.get `  
` cloudtrace.tasks.list `  
` cloudtrace.traces.get `  
` cloudtrace.traces.list `  
` cloudtrace.traces.patch `  
  
Compute Engine  |  Added  |  ` compute.instances.setMachineResources `  
` compute.instances.setMinCpuPlatform `  
` compute.instances.setServiceAccount `  
` compute.instances.updateAccessConfig `  
` compute.instances.updateNetworkInterface `  
` compute.licenseCodes.get `  
` compute.licenseCodes.list `  
` compute.licenseCodes.update `  
` compute.licenseCodes.use `  
  
Compute Engine  |  Supported In Custom Roles  |  `
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
  
Compute Engine  |  Not Supported In Custom Roles  |  `
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
  
Google Kubernetes Engine  |  Added  |  ` container.services.updateStatus `  
  
Google Kubernetes Engine  |  Supported In Custom Roles  |  `
container.clusters.create `  
` container.clusters.delete `  
` container.clusters.get `  
` container.clusters.getCredentials `  
` container.clusters.list `  
` container.clusters.update `  
` container.operations.get `  
` container.operations.list `  
  
Dataproc  |  Supported In Custom Roles  |  ` dataproc.clusters.create `  
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
  
Datastore  |  Not Supported In Custom Roles  |  ` datastore.databases.create `  
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
  
Cloud Deployment Manager  |  Supported In Custom Roles  |  `
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
  
Dialogflow  |  Supported In Custom Roles  |  ` dialogflow.agents.export `  
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
  
Error Reporting  |  Supported In Custom Roles  |  `
errorreporting.applications.list `  
` errorreporting.errorEvents.create `  
` errorreporting.errorEvents.delete `  
` errorreporting.errorEvents.list `  
` errorreporting.groupMetadata.get `  
` errorreporting.groupMetadata.update `  
` errorreporting.groups.list `  
  
Identity and Access Management  |  Not Supported In Custom Roles  |  `
iam.serviceAccounts.actAs `  
` iam.serviceAccounts.getAccessToken `  
` iam.serviceAccounts.signBlob `  
` iam.serviceAccounts.signJwt `  
  
Cloud Logging  |  Supported In Custom Roles  |  ` logging.exclusions.create `  
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
  
AI Platform  |  Supported In Custom Roles  |  ` ml.jobs.cancel `  
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
  
Cloud Monitoring  |  Supported In Custom Roles  |  ` monitoring.groups.create
`  
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
  
Pub/Sub  |  Supported In Custom Roles  |  ` pubsub.topics.setIamPolicy `  
  
Service Management  |  Supported In Custom Roles  |  `
servicemanagement.services.check `  
` servicemanagement.services.report `  
  
Service Management  |  Not Supported In Custom Roles  |  `
servicemanagement.consumerSettings.get `  
` servicemanagement.consumerSettings.getIamPolicy `  
` servicemanagement.consumerSettings.list `  
` servicemanagement.consumerSettings.setIamPolicy `  
` servicemanagement.consumerSettings.update `  
  
Cloud Source Repositories  |  Supported In Custom Roles  |  `
source.repos.delete `  
` source.repos.get `  
` source.repos.getIamPolicy `  
` source.repos.list `  
` source.repos.setIamPolicy `  
  
Cloud Source Repositories  |  Not Supported In Custom Roles  |  `
source.repos.update `  
  
Cloud Spanner  |  Supported In Custom Roles  |  `
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
  
Cloud Spanner  |  Not Supported In Custom Roles  |  `
spanner.databaseOperations.delete `  
` spanner.databases.update `  
  
Cloud Storage  |  Supported In Custom Roles  |  ` storage.buckets.create `  
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
  
  
##  Cloud IAM changes as of 2017-12-08

Service  |  Change  |  Description  
---|---|---  
BigQuery  |  Supported In Custom Roles  |  ` bigquery.datasets.create `  
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
  
BigQuery  |  Not Supported In Custom Roles  |  ` bigquery.config.get `  
` bigquery.config.update `  
` bigquery.service.actAsSuperuser `  
` bigquery.tables.update `  
` bigquery.tables.updateData `  
` bigquery.transfers.get `  
` bigquery.transfers.update `  
  
Cloud Bigtable  |  Supported In Custom Roles  |  ` bigtable.clusters.get `  
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
  
Compute Engine  |  Added  |  ` compute.disks.getIamPolicy `  
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
  
Dataflow  |  Supported In Custom Roles  |  ` dataflow.jobs.cancel `  
` dataflow.jobs.create `  
` dataflow.jobs.get `  
` dataflow.jobs.list `  
` dataflow.jobs.updateContents `  
` dataflow.messages.list `  
` dataflow.metrics.get `  
  
Dataproc  |  Added  |  ` dataproc.workflowTemplates.instantiateInline `  
  
Cloud Data Loss Prevention  |  Added  |  ` dlp.analyzeRiskTemplates.create `  
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
  
Pub/Sub  |  Added  |  ` pubsub.snapshots.create `  
` pubsub.snapshots.delete `  
` pubsub.snapshots.get `  
` pubsub.snapshots.getIamPolicy `  
` pubsub.snapshots.list `  
` pubsub.snapshots.seek `  
` pubsub.snapshots.setIamPolicy `  
` pubsub.snapshots.update `  
  
Pub/Sub  |  Supported In Custom Roles  |  ` pubsub.subscriptions.consume `  
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
  
  
##  Cloud IAM changes as of 2017-12-01

Service  |  Change  |  Description  
---|---|---  
Cloud Build  |  Supported In Custom Roles  |  ` cloudbuild.builds.create `  
` cloudbuild.builds.get `  
` cloudbuild.builds.list `  
` cloudbuild.builds.update `  
  
Cloud Tool Results  |  Now GA  |  ` cloudtoolresults.executions.create `  
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
  
Compute Engine  |  Now GA  |  ` compute.instances.addMaintenancePolicies `  
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
  
Google Kubernetes Engine  |  Added  |  `
container.initializerConfigurations.create `  
` container.initializerConfigurations.delete `  
` container.initializerConfigurations.get `  
` container.initializerConfigurations.list `  
` container.initializerConfigurations.update `  
` container.pods.initialize `  
  
Google Kubernetes Engine  |  Now GA  |  ` container.deployments.getScale `  
` container.deployments.updateScale `  
  
Dataprep by Trifacta  |  Supported In Custom Roles  |  ` dataprep.projects.use
`  
  
Identity and Access Management  |  Supported In Custom Roles  |  `
iam.roles.create `  
` iam.roles.delete `  
` iam.roles.get `  
` iam.roles.list `  
` iam.roles.undelete `  
` iam.roles.update `  
  
  
##  Cloud IAM changes as of 2017-11-10

Service  |  Change  |  Description  
---|---|---  
Google Kubernetes Engine  |  Added  |  ` container.clusters.getIamPolicy `  
` container.clusters.setIamPolicy `  
  
AI Platform  |  Added  |  ` ml.locations.get `  
` ml.locations.list `  
  
Cloud Monitoring  |  Added  |  ` monitoring.metricDescriptors.update `  
  
  
##  Cloud IAM changes as of 2017-10-27

Service  |  Change  |  Description  
---|---|---  
Compute Engine  |  Added  |  ` compute.instances.updateShieldedVmConfig `  
  
Identity-Aware Proxy  |  Added  |  ` iap.web.getIamPolicy `  
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
  
Service Management  |  Supported In Custom Roles  |  `
servicemanagement.services.create `  
` servicemanagement.services.delete `  
` servicemanagement.services.get `  
` servicemanagement.services.getIamPolicy `  
` servicemanagement.services.list `  
` servicemanagement.services.setIamPolicy `  
` servicemanagement.services.update `  
  
  
##  Cloud IAM changes as of 2017-10-06

Service  |  Change  |  Description  
---|---|---  
Dataproc  |  Now GA  |  ` dataproc.workflowTemplates.create `  
` dataproc.workflowTemplates.delete `  
` dataproc.workflowTemplates.get `  
` dataproc.workflowTemplates.getIamPolicy `  
` dataproc.workflowTemplates.instantiate `  
` dataproc.workflowTemplates.list `  
` dataproc.workflowTemplates.setIamPolicy `  
` dataproc.workflowTemplates.update `  
  
  
##  Cloud IAM changes as of 2017-09-22

Service  |  Change  |  Description  
---|---|---  
App Engine  |  Added  |  ` appengine.memcache.addKey `  
` appengine.memcache.flush `  
` appengine.memcache.get `  
` appengine.memcache.getKey `  
` appengine.memcache.list `  
` appengine.memcache.update `  
  
Cloud SQL  |  Added  |  ` cloudsql.instances.demoteMaster `  
  
Cloud SQL  |  Now GA  |  ` cloudsql.instances.demoteMaster `  
  
  
##  Cloud IAM changes as of 2017-09-08

Service  |  Change  |  Description  
---|---|---  
Cloud Functions  |  Added  |  ` cloudfunctions.functions.call `  
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
  
Compute Engine  |  Added  |  ` compute.instances.setDeletionProtection `  
` compute.targetHttpsProxies.setUrlMap `  
  
Google Kubernetes Engine  |  Added  |  ` container.statefulSets.getScale `  
` container.statefulSets.updateScale `  
  
Google Kubernetes Engine  |  Now GA  |  ` container.statefulSets.getScale `  
` container.statefulSets.updateScale `  
  
Cloud Functions  |  Added  |  ` dlp.kms.encrypt `  
` dlp.riskAnalysisOperations.cancel `  
` dlp.riskAnalysisOperations.create `  
` dlp.riskAnalysisOperations.get `  
` dlp.riskAnalysisOperations.list `  

