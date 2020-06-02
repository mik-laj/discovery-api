#  출시 노트

이 페이지에는 다음 Service Infrastructure API의 각 버전에 대한 출시 노트가 포함되어 있습니다.

  * Service Management API 
  * Service Control API 
  * Service Consumer Management API 

이 페이지를 정기적으로 확인하여 새로운 기능이나 업데이트된 기능, 버그 수정, 알려진 문제, 지원 중단된 기능에 대한 공지를 볼 수
있습니다.

**참고:** Service Usage API의 Service Infrastructure 출시 노트는 [ 출시 노트
](https://cloud.google.com/service-usage/docs/release-notes?hl=ko) 를 참조하세요.

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서 모든
Google Cloud의 최신 제품 업데이트를 확인할 수 있습니다.

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL을 다음과 같이 직접 추가하세요. `
https://cloud.google.com/feeds/serviceinfrastructure-release-notes.xml `

##  April 01, 2019

**FEATURE:**

The Service Consumer Management API includes the following additions for
managing tenancy units:

**FEATURE:**

  * [ ` TenantProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig?hl=ko) defines a tenant project to be added to the specified tenancy unit as well as its initial configuration and properties. 

**FEATURE:**

  * [ ` services.tenancyUnits.applyProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig?hl=ko) applies a configuration to an existing tenant project. 

**FEATURE:**

  * [ ` services.tenancyUnits.attachProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject?hl=ko) attaches an existing project to a tenancy unit as a new tenant resource. 

**FEATURE:**

  * [ ` services.tenancyUnits.deleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject?hl=ko) deletes the specified project resource identified by a tenant resource tag. 

**FEATURE:**

  * [ ` services.tenancyUnits.undeleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject?hl=ko) attempts to undelete a previously deleted tenant project. 

##  March 01, 2019

**FEATURE:**

The Service Consumer Management API includes the following additions for
managing tenancy units:

**FEATURE:**

  * [ ` TenantProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig?hl=ko) defines a tenant project to be added to the specified tenancy unit, as well as its initial configuration and properties. 

**FEATURE:**

  * [ ` services.tenancyUnits.applyProjectConfig ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig?hl=ko) applies a configuration to an existing tenant project. 

**FEATURE:**

  * [ ` services.tenancyUnits.attachProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject?hl=ko) attaches an existing project to a tenancy unit as a new tenant resource. 

**FEATURE:**

  * [ ` services.tenancyUnits.deleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject?hl=ko) deletes the specified project resource identified by a tenant resource tag. 

**FEATURE:**

  * [ ` services.tenancyUnits.undeleteProject ` ](https://cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject?hl=ko) attempts to undelete a previously deleted tenant project. 

##  March 01, 2018

**FEATURE:**

Service Consumer Management API's Tenancy Units feature is now generally
available.

##  February 01, 2018

**FEATURE:**

Service Infrastructure supports [ billing ](https://cloud.google.com/service-
infrastructure/docs/reporting-billing-metrics?hl=ko) \- General Availability.

##  October 01, 2017

**FEATURE:**

Service Control API supports [ rate limiting
](https://cloud.google.com/service-infrastructure/docs/rate-limiting?hl=ko) \-
Public Beta.

##  September 01, 2017

**FEATURE:**

Service Control API supports [ billing ](https://cloud.google.com/service-
infrastructure/docs/reporting-billing-metrics?hl=ko) \- Public Beta.

Service Consumer Management API v1 - Public Beta.

##  May 01, 2017

**FEATURE:**

Added Service Control API [ service-level IAM access control
](https://cloud.google.com/service-infrastructure/docs/service-control/access-
control?hl=ko) .

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

