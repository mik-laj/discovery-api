#  출시 노트

이 페이지에서는 AutoML Vision 객체 감지의 프로덕션 업데이트를 설명합니다. AutoML Vision 객체 감지 개발자는 이 목록을
주기적으로 참고하여 새로운 공지사항을 확인하는 것이 좋습니다.

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서 모든
Google Cloud의 최신 제품 업데이트를 확인할 수 있습니다.

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL을 다음과 같이 직접 추가하세요. ` https://cloud.google.com/feeds/automl-vision-
object-detection-release-notes.xml `

##  June 04, 2020

**DEPRECATED:**

**v1beta1 endpoint end-of-life**

After June 4, 2020, the v1beta1 version of AutoML API will deny increasing
numbers of API requests from AutoML Vision users. Please refer to the [
November 20, 2019 ](https://cloud.google.com/vision/automl/object-
detection/docs/release-notes?hl=ko#November_20_2019) release notes and migrate
to v1 version immediately.

If you have any questions regarding the above action items, join the [ cloud-
vision-discuss Google group ](https://groups.google.com/g/cloud-vision-
discuss?hl=ko) . For further assistance, please open an issue in this [
private issue tracker
](https://issuetracker.google.com/issues/new?component=836902&template=1440861&hl=ko)
.

##  April 03, 2020

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview?hl=ko) is now in [ beta stage
](https://cloud.google.com/products/?hl=ko#product-launch-stages) .

##  November 20, 2019

**CHANGED:**

**Object Detection General Availability (GA) release**

Some notes about the GA release:

  * Cloud AutoML Vision and AutoML Vision Edge are now in General Availability (GA). The [ Service Level Agreement ](https://cloud.google.com/vision/sla?hl=ko) has been published. 
  * We've introduced a new version (v1) of the [ Cloud AutoML API ](https://cloud.google.com/vision/automl/docs/reference/rest/?hl=ko) . The current version (v1beta1) is deprecated and is scheduled for deletion within six months. As a result, you will need to migrate your applications from the v1beta1 version to the v1 version. If you have integrated with the Create Dataset API, you will also need to change your code to reflect changes with v1 version integration. 
    * [ Creating datasets ](https://cloud.google.com/automl/docs/reference/rest/v1/projects.locations.datasets/create?hl=ko) will now return an Operation, whose status must be requested to detect completion. 
    * Both [ dataset ](https://cloud.google.com/automl/docs/reference/rest/v1/projects.locations.datasets?hl=ko) and [ model ](https://cloud.google.com/automl/docs/reference/rest/v1/projects.locations.models?hl=ko) can be updated using patch, with a field mask that can include labels and displayName for both, and description only for dataset. 
    * Specifying an [ Image ](https://cloud.google.com/automl/docs/reference/rest/v1/projects.locations.models/predict?hl=ko#image) is the only option for ExamplePayload of online prediction. The inputConfig option was not supported and has been deleted. 
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
](https://cloud.google.com/vision/automl/docs/predict-batch?hl=ko) and [
Object Detection ](https://cloud.google.com/vision/automl/object-
detection/docs/predict-batch?hl=ko) .

**FEATURE:**

**TensorFlow.js Integration Beta**

This integration allows AutoML Vision Edge models to be exported as
TensorFlow.js package.

The edge model can be deployed in an increasing number of platforms with
TensorFlow.js support, including all major browsers and server-side in
Node.js. You may want to view the documented user journey for [ exporting to
web ](https://cloud.google.com/vision/automl/object-detection/docs/export-
edge?hl=ko#export_for_web) , and [ TensorFlow.js tutorial
](https://cloud.google.com/vision/automl/object-detection/docs/tensorflow-js-
tutorial?hl=ko) for Edge Object Detection models.

##  August 29, 2019

**FEATURE:**

**AutoML Vision Edge Beta Release**

Some notes about the Beta release:

  * You can access the updated AutoML Vision Object Detection Beta UI with with AutoML Vision Edge support at https://console.cloud.google.com/vision. 
  * You can now perform all of your AutoML Vision Edge tasks using the AutoML API. Create datasets, train models, make predictions, and export models. For details, see the [ how-to guides ](https://cloud.google.com/vision/automl/object-detection/docs/how-to?hl=ko) . 
  * You can currently only supply base64-encoded image content to the ` predict ` method. For an example, see the [ Annotating prediction images ](https://cloud.google.com/vision/automl/object-detection/docs/predict?hl=ko) page. 

For more information, see the [ product documentation
](https://cloud.google.com/vision/automl/object-detection/docs/?hl=ko) .

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
detection/docs/models?hl=ko#node-update) topic.

##  April 10, 2019

**FEATURE:**

**Cloud AutoML Vision Object Detection Beta Release**

Cloud AutoML Vision Object Detection Beta has been released. Some notes about
the Beta release:

  * You can access the Cloud AutoML Vision Beta UI with with AutoML Vision Object Detection support at [ https://console.cloud.google.com/vision ](https://console.cloud.google.com/vision?_ga=2.53927336.-1490361011.1561412245&hl=ko) . 
  * You can now perform all of your AutoML Vision Object Detection tasks using the AutoML API. Create datasets, train models, make predictions, and more. For details, see the [ landing page ](https://cloud.google.com/vision/automl/object-detection/docs?hl=ko) . 
  * You can currently only supply base64-encoded image content to the ` predict ` method. For an example, see [ Make a prediction ](https://cloud.google.com/vision/automl/object-detection/docs/predict?hl=ko) . 
  * AutoML Vision Object Detection does not currently satisfy the requirements to be considered compliant with the Health Insurance Portability and Accountability Act (HIPAA). 

For more information, see the [ product documentation
](https://cloud.google.com/vision/automl/object-detection/docs?hl=ko) .

**CHANGED:**

There are workflow differences between Cloud AutoML Vision image
classification and object detection. Consequently, changes have been made to
the [ Google Cloud Platform Console UI
](https://console.cloud.google.com/vision?_ga=2.146732340.-1490361011.1561412245&hl=ko)
for object detection that are not reflected in the UI for image
classification.

**ISSUE:**

Microsoft Edge and Microsoft Internet Explorer do not support all features of
AutoML Vision Object Detection. If you are having problems, try Google Chrome,
Safari, or Firefox.

