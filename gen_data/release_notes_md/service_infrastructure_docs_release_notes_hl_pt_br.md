#  Notas da versão

Esta página contém notas de versão para cada versão das seguintes APIs da
Service Infrastructure:

  * API Service Management 
  * API Service Control 
  * API Service Consumer Management 

Acesse-a periodicamente para ver anúncios de recursos novos ou atualizados,
correções de bugs, problemas conhecidos e funcionalidades obsoletas.

**Nota:** Para notas de versão da Service Infrastructure para a API Service
Usage, consulte [ Notas da versão ](https://cloud.google.com/service-
usage/docs/release-notes?hl=pt-br) .

É possível ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas da versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt-br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/serviceinfrastructure-
release-notes.xml `

##  April 01, 2019

**FEATURE:**

The Service Consumer Management API includes the following additions for
managing tenancy units:

**FEATURE:**

  * [ ` TenantProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig?hl=pt-br) defines a tenant project to be added to the specified tenancy unit as well as its initial configuration and properties. 

**FEATURE:**

  * [ ` services.tenancyUnits.applyProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig?hl=pt-br) applies a configuration to an existing tenant project. 

**FEATURE:**

  * [ ` services.tenancyUnits.attachProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject?hl=pt-br) attaches an existing project to a tenancy unit as a new tenant resource. 

**FEATURE:**

  * [ ` services.tenancyUnits.deleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject?hl=pt-br) deletes the specified project resource identified by a tenant resource tag. 

**FEATURE:**

  * [ ` services.tenancyUnits.undeleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject?hl=pt-br) attempts to undelete a previously deleted tenant project. 

##  March 01, 2019

**FEATURE:**

The Service Consumer Management API includes the following additions for
managing tenancy units:

**FEATURE:**

  * [ ` TenantProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig?hl=pt-br) defines a tenant project to be added to the specified tenancy unit, as well as its initial configuration and properties. 

**FEATURE:**

  * [ ` services.tenancyUnits.applyProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig?hl=pt-br) applies a configuration to an existing tenant project. 

**FEATURE:**

  * [ ` services.tenancyUnits.attachProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject?hl=pt-br) attaches an existing project to a tenancy unit as a new tenant resource. 

**FEATURE:**

  * [ ` services.tenancyUnits.deleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject?hl=pt-br) deletes the specified project resource identified by a tenant resource tag. 

**FEATURE:**

  * [ ` services.tenancyUnits.undeleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject?hl=pt-br) attempts to undelete a previously deleted tenant project. 

##  March 01, 2018

**FEATURE:**

Service Consumer Management API's Tenancy Units feature is now generally
available.

##  February 01, 2018

**FEATURE:**

Service Infrastructure supports [ billing ](https://cloud.google.com/service-
infrastructure/docs/reporting-billing-metrics?hl=pt-br) \- General
Availability.

##  October 01, 2017

**FEATURE:**

Service Control API supports [ rate limiting
](https://cloud.google.com/service-infrastructure/docs/rate-limiting?hl=pt-br)
\- Public Beta.

##  September 01, 2017

**FEATURE:**

Service Control API supports [ billing ](https://cloud.google.com/service-
infrastructure/docs/reporting-billing-metrics?hl=pt-br) \- Public Beta.

Service Consumer Management API v1 - Public Beta.

##  May 01, 2017

**FEATURE:**

Added Service Control API [ service-level IAM access control
](https://cloud.google.com/service-infrastructure/docs/service-control/access-
control?hl=pt-br) .

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

