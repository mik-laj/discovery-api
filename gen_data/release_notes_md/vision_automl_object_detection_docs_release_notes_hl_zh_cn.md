#  版本说明

本页面记录了 AutoML Vision Object Detection 的正式版更新。我们建议 AutoML Vision Object
Detection 开发者定期查看此列表，以便及时获知新公告。

您可以在 [ Google Cloud 版本说明 ](https://cloud.google.com/release-notes?hl=zh_cn)
页面上查看 Google Cloud Platform 所有产品的最新动态。

要接收最新产品动态，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接添加 Feed 网址： `
https://cloud.google.com/feeds/automl-vision-object-detection-release-
notes.xml `

##  June 04, 2020

**DEPRECATED:**

**v1beta1 endpoint end-of-life**

After June 4, 2020, the v1beta1 version of AutoML API will deny increasing
numbers of API requests from AutoML Vision users. Please refer to the [
November 20, 2019 ](https://cloud.google.com/vision/automl/object-
detection/docs/release-notes?hl=zh_cn#November_20_2019) release notes and
migrate to v1 version immediately.

If you have any questions regarding the above action items, join the [ cloud-
vision-discuss Google group ](https://groups.google.com/g/cloud-vision-
discuss?hl=zh_cn) . For further assistance, please open an issue in this [
private issue tracker
](https://issuetracker.google.com/issues/new?component=836902&template=1440861&hl=zh_cn)
.

##  April 03, 2020

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview?hl=zh_cn) is now in [ beta stage
](https://cloud.google.com/products/?hl=zh_cn#product-launch-stages) .

##  November 20, 2019

**CHANGED:**

**Object Detection General Availability (GA) release**

Some notes about the GA release:

  * Cloud AutoML Vision and AutoML Vision Edge are now in General Availability (GA). The [ Service Level Agreement ](https://cloud.google.com/vision/sla?hl=zh_cn) has been published. 
  * We've introduced a new version (v1) of the [ Cloud AutoML API ](https://cloud.google.com/vision/automl/docs/reference/rest/?hl=zh_cn) . The current version (v1beta1) is deprecated and is scheduled for deletion within six months. As a result, you will need to migrate your applications from the v1beta1 version to the v1 version. If you have integrated with the Create Dataset API, you will also need to change your code to reflect changes with v1 version integration. 
    * [ Creating datasets ](https://cloud.google.com/automl/docs/reference/rest/v1/projects.locations.datasets/create?hl=zh_cn) will now return an Operation, whose status must be requested to detect completion. 
    * Both [ dataset ](https://cloud.google.com/automl/docs/reference/rest/v1/projects.locations.datasets?hl=zh_cn) and [ model ](https://cloud.google.com/automl/docs/reference/rest/v1/projects.locations.models?hl=zh_cn) can be updated using patch, with a field mask that can include labels and displayName for both, and description only for dataset. 
    * Specifying an [ Image ](https://cloud.google.com/automl/docs/reference/rest/v1/projects.locations.models/predict?hl=zh_cn#image) is the only option for ExamplePayload of online prediction. The inputConfig option was not supported and has been deleted. 
  * The maximum supported lifespan for custom models created in Cloud AutoML Vision and AutoML Vision Edge has changed from two years to 18 months. 

For more information, see the [ product documentation
](http://cloud/vision/automl/object-detection/docs) .

##  October 14, 2019

**FEATURE:**

**Batch prediction Beta**

The following Beta feature is available in API version **v1beta1** :

In addition to online predictions in our Cloud and predictions at the Edge, we
now support batch predictions in our Cloud with your AutoML Vision models.

Making batch predictions is documented for both [ Image Classification
](https://cloud.google.com/vision/automl/docs/predict-batch?hl=zh_cn) and [
Object Detection ](https://cloud.google.com/vision/automl/object-
detection/docs/predict-batch?hl=zh_cn) .

**FEATURE:**

**TensorFlow.js Integration Beta**

This integration allows AutoML Vision Edge models to be exported as
TensorFlow.js package.

The edge model can be deployed in an increasing number of platforms with
TensorFlow.js support, including all major browsers and server-side in
Node.js. You may want to view the documented user journey for [ exporting to
web ](https://cloud.google.com/vision/automl/object-detection/docs/export-
edge?hl=zh_cn#export_for_web) , and [ TensorFlow.js tutorial
](https://cloud.google.com/vision/automl/object-detection/docs/tensorflow-js-
tutorial?hl=zh_cn) for Edge Object Detection models.

##  August 29, 2019

**FEATURE:**

**AutoML Vision Edge Beta Release**

Some notes about the Beta release:

  * You can access the updated AutoML Vision Object Detection Beta UI with with AutoML Vision Edge support at https://console.cloud.google.com/vision. 
  * You can now perform all of your AutoML Vision Edge tasks using the AutoML API. Create datasets, train models, make predictions, and export models. For details, see the [ how-to guides ](https://cloud.google.com/vision/automl/object-detection/docs/how-to?hl=zh_cn) . 
  * You can currently only supply base64-encoded image content to the ` predict ` method. For an example, see the [ Annotating prediction images ](https://cloud.google.com/vision/automl/object-detection/docs/predict?hl=zh_cn) page. 

For more information, see the [ product documentation
](https://cloud.google.com/vision/automl/object-detection/docs/?hl=zh_cn) .

**ISSUE:**

Microsoft Edge and Microsoft Internet Explorer do not support all features of
AutoML Vision Object Detection. If you are having problems, try Google Chrome,
Safari, or Firefox.

##  June 18, 2019

**CHANGED:**

**Model node number update**

Notes about the update:

  * You can now update the number of nodes a deploy model is on without first having to undeploy the model. 

For more information, see the [ managing models
](https://cloud.google.com/vision/automl/object-
detection/docs/models?hl=zh_cn#node-update) topic.

##  April 10, 2019

**FEATURE:**

**Cloud AutoML Vision Object Detection Beta Release**

Cloud AutoML Vision Object Detection Beta has been released. Some notes about
the Beta release:

  * You can access the Cloud AutoML Vision Beta UI with with AutoML Vision Object Detection support at [ https://console.cloud.google.com/vision ](https://console.cloud.google.com/vision?_ga=2.53927336.-1490361011.1561412245&hl=zh_cn) . 
  * You can now perform all of your AutoML Vision Object Detection tasks using the AutoML API. Create datasets, train models, make predictions, and more. For details, see the [ landing page ](https://cloud.google.com/vision/automl/object-detection/docs?hl=zh_cn) . 
  * You can currently only supply base64-encoded image content to the ` predict ` method. For an example, see [ Make a prediction ](https://cloud.google.com/vision/automl/object-detection/docs/predict?hl=zh_cn) . 
  * AutoML Vision Object Detection does not currently satisfy the requirements to be considered compliant with the Health Insurance Portability and Accountability Act (HIPAA). 

For more information, see the [ product documentation
](https://cloud.google.com/vision/automl/object-detection/docs?hl=zh_cn) .

**CHANGED:**

There are workflow differences between Cloud AutoML Vision image
classification and object detection. Consequently, changes have been made to
the [ Google Cloud Platform Console UI
](https://console.cloud.google.com/vision?_ga=2.146732340.-1490361011.1561412245&hl=zh_cn)
for object detection that are not reflected in the UI for image
classification.

**ISSUE:**

Microsoft Edge and Microsoft Internet Explorer do not support all features of
AutoML Vision Object Detection. If you are having problems, try Google Chrome,
Safari, or Firefox.

