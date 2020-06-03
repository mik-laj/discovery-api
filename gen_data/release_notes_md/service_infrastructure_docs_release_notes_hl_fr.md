#  Notes de version

Cette page contient des notes de version pour chaque version des API de
Service Infrastructure suivantes :

  * API Service Management 
  * API Service Control 
  * API Service Consumer Management 

Consultez-la régulièrement pour obtenir des informations sur les
fonctionnalités nouvelles ou mises à jour, les corrections de bugs, les
problèmes connus et les fonctionnalités obsolètes.

**Remarque** : Pour obtenir les notes de version de Service Infrastructure
concernant l'API Service Usage, consultez la page [ Notes de version
](https://cloud.google.com/service-usage/docs/release-notes?hl=fr) .

Vous pouvez consulter les dernières mises à jour de produits pour l'ensemble
de Google Cloud sur la page [ Notes de version de Google Cloud
](https://cloud.google.com/release-notes?hl=fr) .

Pour recevoir les dernières mises à jour concernant ce produit, ajoutez l'URL
de cette page à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou ajoutez l'URL
du flux directement : ` https://cloud.google.com/feeds/serviceinfrastructure-
release-notes.xml `

##  April 01, 2019

**FEATURE:**

The Service Consumer Management API includes the following additions for
managing tenancy units:

**FEATURE:**

  * [ ` TenantProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig?hl=fr) defines a tenant project to be added to the specified tenancy unit as well as its initial configuration and properties. 

**FEATURE:**

  * [ ` services.tenancyUnits.applyProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig?hl=fr) applies a configuration to an existing tenant project. 

**FEATURE:**

  * [ ` services.tenancyUnits.attachProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject?hl=fr) attaches an existing project to a tenancy unit as a new tenant resource. 

**FEATURE:**

  * [ ` services.tenancyUnits.deleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject?hl=fr) deletes the specified project resource identified by a tenant resource tag. 

**FEATURE:**

  * [ ` services.tenancyUnits.undeleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject?hl=fr) attempts to undelete a previously deleted tenant project. 

##  March 01, 2019

**FEATURE:**

The Service Consumer Management API includes the following additions for
managing tenancy units:

**FEATURE:**

  * [ ` TenantProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig?hl=fr) defines a tenant project to be added to the specified tenancy unit, as well as its initial configuration and properties. 

**FEATURE:**

  * [ ` services.tenancyUnits.applyProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig?hl=fr) applies a configuration to an existing tenant project. 

**FEATURE:**

  * [ ` services.tenancyUnits.attachProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject?hl=fr) attaches an existing project to a tenancy unit as a new tenant resource. 

**FEATURE:**

  * [ ` services.tenancyUnits.deleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject?hl=fr) deletes the specified project resource identified by a tenant resource tag. 

**FEATURE:**

  * [ ` services.tenancyUnits.undeleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject?hl=fr) attempts to undelete a previously deleted tenant project. 

##  March 01, 2018

**FEATURE:**

Service Consumer Management API's Tenancy Units feature is now generally
available.

##  February 01, 2018

**FEATURE:**

Service Infrastructure supports [ billing ](https://cloud.google.com/service-
infrastructure/docs/reporting-billing-metrics?hl=fr) \- General Availability.

##  October 01, 2017

**FEATURE:**

Service Control API supports [ rate limiting
](https://cloud.google.com/service-infrastructure/docs/rate-limiting?hl=fr) \-
Public Beta.

##  September 01, 2017

**FEATURE:**

Service Control API supports [ billing ](https://cloud.google.com/service-
infrastructure/docs/reporting-billing-metrics?hl=fr) \- Public Beta.

Service Consumer Management API v1 - Public Beta.

##  May 01, 2017

**FEATURE:**

Added Service Control API [ service-level IAM access control
](https://cloud.google.com/service-infrastructure/docs/service-control/access-
control?hl=fr) .

##  December 01, 2016

**FEATURE:**

Service Control API v1 - General Availability.

**FEATURE:**

Service Control API pricing structure is made available.

**FEATURE:**

Service Control API request size limits are enforced.

##  August 01, 2016

**CHANGED:**

Service Control API v1 - Public Beta.

**CHANGED:**

Service Management API v1 - Public Beta.

