#  リリースノート

このページには、次の Service Infrastructure API の各バージョンのリリースノートが掲載されています。

  * Service Management API 
  * Service Control API 
  * Service Consumer Management API 

このページを定期的にチェックして、新機能や更新された機能、バグ修正、既知の問題、非推奨になった機能に関するお知らせを確認してください。

**注:** Service Usage API に関する Service Infrastructure のリリースノートについては [ リリースノート
](https://cloud.google.com/service-usage/docs/release-notes?hl=ja) をご覧ください。

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/serviceinfrastructure-release-
notes.xml ` を直接追加します。

##  April 01, 2019

**FEATURE:**

The Service Consumer Management API includes the following additions for
managing tenancy units:

**FEATURE:**

  * [ ` TenantProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig?hl=ja) defines a tenant project to be added to the specified tenancy unit as well as its initial configuration and properties. 

**FEATURE:**

  * [ ` services.tenancyUnits.applyProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig?hl=ja) applies a configuration to an existing tenant project. 

**FEATURE:**

  * [ ` services.tenancyUnits.attachProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject?hl=ja) attaches an existing project to a tenancy unit as a new tenant resource. 

**FEATURE:**

  * [ ` services.tenancyUnits.deleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject?hl=ja) deletes the specified project resource identified by a tenant resource tag. 

**FEATURE:**

  * [ ` services.tenancyUnits.undeleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject?hl=ja) attempts to undelete a previously deleted tenant project. 

##  March 01, 2019

**FEATURE:**

The Service Consumer Management API includes the following additions for
managing tenancy units:

**FEATURE:**

  * [ ` TenantProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig?hl=ja) defines a tenant project to be added to the specified tenancy unit, as well as its initial configuration and properties. 

**FEATURE:**

  * [ ` services.tenancyUnits.applyProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig?hl=ja) applies a configuration to an existing tenant project. 

**FEATURE:**

  * [ ` services.tenancyUnits.attachProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject?hl=ja) attaches an existing project to a tenancy unit as a new tenant resource. 

**FEATURE:**

  * [ ` services.tenancyUnits.deleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject?hl=ja) deletes the specified project resource identified by a tenant resource tag. 

**FEATURE:**

  * [ ` services.tenancyUnits.undeleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject?hl=ja) attempts to undelete a previously deleted tenant project. 

##  March 01, 2018

**FEATURE:**

Service Consumer Management API's Tenancy Units feature is now generally
available.

##  February 01, 2018

**FEATURE:**

Service Infrastructure supports [ billing ](https://cloud.google.com/service-
infrastructure/docs/reporting-billing-metrics?hl=ja) \- General Availability.

##  October 01, 2017

**FEATURE:**

Service Control API supports [ rate limiting
](https://cloud.google.com/service-infrastructure/docs/rate-limiting?hl=ja) \-
Public Beta.

##  September 01, 2017

**FEATURE:**

Service Control API supports [ billing ](https://cloud.google.com/service-
infrastructure/docs/reporting-billing-metrics?hl=ja) \- Public Beta.

Service Consumer Management API v1 - Public Beta.

##  May 01, 2017

**FEATURE:**

Added Service Control API [ service-level IAM access control
](https://cloud.google.com/service-infrastructure/docs/service-control/access-
control?hl=ja) .

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

