#  版本说明

此页面记录了 Access Context Manager 的正式版更新。您可以定期查看本页面，以了解有关新功能或更新功能、Bug
修复、已知问题和已弃用功能的公告。

您可以在 [ Google Cloud 版本说明 ](https://cloud.google.com/release-notes?hl=zh-cn)
页面上查看 Google Cloud 所有产品的最新产品动态。

要接收最新产品动态，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接添加 Feed 网址： `
https://cloud.google.com/feeds/access-context-manager-release-notes.xml `

##  June 11, 2020

**FEATURE:**

General availability of the Access Context Manager Bulk API.

Use the Access Context Manager Bulk API to replace all of your organization's
access levels in one operation. For more information, see [ Making bulk
changes to access levels ](https://cloud.google.com/access-context-
manager/docs/bulk-operations?hl=zh-cn) .

##  June 01, 2020

**FEATURE:**

General availability of custom access levels.

[ Custom access levels ](https://cloud.google.com/access-context-
manager/docs/custom-access-levels?hl=zh-cn) provide a way to use Common
Expression Language to craft custom conditions. [ Create custom access levels
](https://cloud.google.com/access-context-manager/docs/create-custom-access-
level?hl=zh-cn) using the ` gcloud ` command line tool, the Access Context
Manager API, and in the Google Cloud Console using the Advanced Mode for
configuring access levels.

##  April 03, 2020

**FEATURE:**

Beta release of the Access Context Manager Bulk API.

The Access Context Manager Bulk API can be used for operations such as
replacing all of your organization's access levels. For more information, see
[ Making bulk changes to access levels ](https://cloud.google.com/access-
context-manager/docs/bulk-operations?hl=zh-cn) .

##  February 25, 2020

**FEATURE:**

Access Context Manager support for mobile devices has entered Beta. You can
now [ create access levels that target iOS and Android devices
](https://cloud.google.com/access-context-manager/docs/use-mobile-
devices?hl=zh-cn) .

Currently, the **[ OS policy ](https://cloud.google.com/access-context-
manager/docs/access-level-attributes?hl=zh-cn#os-policy) ** and **[ Require
screen lock ](https://cloud.google.com/access-context-manager/docs/access-
level-attributes?hl=zh-cn#require-screen-lock) ** device attributes are
supported for use with iOS and Android devices.

To take advantage of the new feature, your organization must use G Suite [
basic mobile device management
](https://support.google.com/a/answer/7400753?hl=zh-cn) .

##  January 06, 2020

**DEPRECATED:**

The Access Context Manager v1beta API is being deprecated in July 2020.

##  October 07, 2019

**CHANGED:**

Access Context Manager's v1alpha API is re-enabled.

The v1alpha API no longer uses ` AccessZone ` . ` AccessZone ` has been
replaced with ` ServicePerimeter ` .

To use the v1alpha API, you must be whitelisted.

##  August 05, 2019

**CHANGED:**

Error handling in Access Context Manager API v1alpha:

  * Attempting to call any v1alpha API method will start returning errors as of 08/12/2019. 

**DEPRECATED:**

Access Context Manager API v1alpha is being deprecated in Q3 2019.

##  March 19, 2019

**FEATURE:**

The following access level attributes are now available:

  * Regions 
  * For Device policy: 
    * Require admin approval 
    * Require corp owned device 
    * Require verified Chrome OS 

##  March 08, 2019

**FEATURE:**

General availability of Access Context Manager.

##  June 01, 2018

**FEATURE:**

Access Context Manager Closed Beta launch.

