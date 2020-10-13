#  版本说明

本页面包含以下 Service Infrastructure API 的各个版本的版本说明：

  * Service Management API 
  * Service Control API 
  * Service Consumer Management API 

您可以定期查看此页面，以了解有关全新或经过更新的功能、问题修复、已知问题和已弃用功能的公告。

**注意** ：  如需了解 Service Usage API 的服务基础架构版本说明，请参阅 [ 版本说明
](https://cloud.google.com/service-usage/docs/release-notes?hl=zh-cn) 。

您可以在 [ Google Cloud 版本说明 ](https://cloud.google.com/release-notes?hl=zh-cn)
页面上查看 Google Cloud 所有产品的最新产品动态。

要接收最新产品动态，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接添加 Feed 网址： `
https://cloud.google.com/feeds/serviceinfrastructure-release-notes.xml `

##  April 01, 2019

**FEATURE:**

The Service Consumer Management API includes the following additions for
managing tenancy units:

**FEATURE:**

  * [ ` TenantProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig?hl=zh-cn) defines a tenant project to be added to the specified tenancy unit as well as its initial configuration and properties. 

**FEATURE:**

  * [ ` services.tenancyUnits.applyProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig?hl=zh-cn) applies a configuration to an existing tenant project. 

**FEATURE:**

  * [ ` services.tenancyUnits.attachProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject?hl=zh-cn) attaches an existing project to a tenancy unit as a new tenant resource. 

**FEATURE:**

  * [ ` services.tenancyUnits.deleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject?hl=zh-cn) deletes the specified project resource identified by a tenant resource tag. 

**FEATURE:**

  * [ ` services.tenancyUnits.undeleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject?hl=zh-cn) attempts to undelete a previously deleted tenant project. 

##  March 01, 2019

**FEATURE:**

The Service Consumer Management API includes the following additions for
managing tenancy units:

**FEATURE:**

  * [ ` TenantProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig?hl=zh-cn) defines a tenant project to be added to the specified tenancy unit, as well as its initial configuration and properties. 

**FEATURE:**

  * [ ` services.tenancyUnits.applyProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig?hl=zh-cn) applies a configuration to an existing tenant project. 

**FEATURE:**

  * [ ` services.tenancyUnits.attachProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject?hl=zh-cn) attaches an existing project to a tenancy unit as a new tenant resource. 

**FEATURE:**

  * [ ` services.tenancyUnits.deleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject?hl=zh-cn) deletes the specified project resource identified by a tenant resource tag. 

**FEATURE:**

  * [ ` services.tenancyUnits.undeleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject?hl=zh-cn) attempts to undelete a previously deleted tenant project. 

##  March 01, 2018

**FEATURE:**

Service Consumer Management API's Tenancy Units feature is now generally
available.

##  February 01, 2018

**FEATURE:**

Service Infrastructure supports [ billing ](https://cloud.google.com/service-
infrastructure/docs/reporting-billing-metrics?hl=zh-cn) \- General
Availability.

##  October 01, 2017

**FEATURE:**

Service Control API supports [ rate limiting
](https://cloud.google.com/service-infrastructure/docs/rate-limiting?hl=zh-cn)
\- Public Beta.

##  September 01, 2017

**FEATURE:**

Service Control API supports [ billing ](https://cloud.google.com/service-
infrastructure/docs/reporting-billing-metrics?hl=zh-cn) \- Public Beta.

Service Consumer Management API v1 - Public Beta.

##  May 01, 2017

**FEATURE:**

Added Service Control API [ service-level IAM access control
](https://cloud.google.com/service-infrastructure/docs/service-control/access-
control?hl=zh-cn) .

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

