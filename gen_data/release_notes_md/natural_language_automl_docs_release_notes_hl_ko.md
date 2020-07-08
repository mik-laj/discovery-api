#  출시 노트

이 페이지에서는 AutoML Natural Language의 프로덕션 업데이트를 설명합니다. 이 페이지를 정기적으로 확인하여 새로운 기능이나
업데이트된 기능, 버그 수정, 알려진 문제, 지원 중단된 기능에 대한 공지를 볼 수 있습니다.

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서 모든
Google Cloud의 최신 제품 업데이트를 확인할 수 있습니다.

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 다음의 피드 URL을 직접 추가하세요. ` https://cloud.google.com/feeds/automl-language-
release-notes.xml `

##  April 03, 2020

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview?hl=ko) is now in [ beta stage
](https://cloud.google.com/products/?hl=ko#product-launch-stages) .

##  March 20, 2020

**CHANGED:**

AutoML Natural Language now supports TIFF files as training data and input for
predictions.

**CHANGED:**

AutoML Natural Language now supports classification and sentiment analysis in
[ 20 languages ](https://cloud.google.com/natural-
language/automl/docs/languages?hl=ko#classification) .

##  January 30, 2020

**FEATURE:**

AutoML Natural Language now supports entity analysis in [ over 100 languages
](https://cloud.google.com/natural-
language/automl/docs/languages?hl=ko#entity_analysis) .

##  December 12, 2019

**FEATURE:**

**AutoML Natural Language General Availability (GA) release**

AutoML Natural Language enables you to train three types of custom machine
learning models:

  * **AutoML Text & Document Classification ** creates models to classify documents according to labels that you define. 
  * **AutoML Text & Document Entity Extraction ** creates models to identify a custom set of entities within documents. 
  * **AutoML Text & Document Sentiment Analysis ** creates models to analyze attitudes within text. 

The GA release consolidates these features, which were documented as separate
products during beta testing. See the [ AutoML Natural Language documentation
](https://cloud.google.com/natural-language/automl/docs/?hl=ko) for details
about all features.

##  October 30, 2019

**FEATURE:**

AutoML Natural Language offers you control over where your datasets and models
are stored and where machine learning takes place. In particular, you can
configure AutoML Natural Language to at rest and perform machine learning
processing in the European Union only. See [ Locations
](https://cloud.google.com/natural-language/automl/docs/locations?hl=ko) for
more information.

##  October 21, 2019

**FEATURE:**

AutoML Natural Language Text Classification now supports [ batch prediction
](https://cloud.google.com/natural-language/automl/docs/predict?hl=ko) .

**FEATURE:**

AutoML Natural Language Text Classification can now classify PDF files and
also supports PDF files as training items.

##  September 04, 2019

**FEATURE:**

AutoML Natural Language Entity Extraction offers support for document-based
entity extraction, which enables you to identify entities in a format that
recreates the basic layout of the training item. When you add annotations,
AutoML Natural Language Entity Extraction captures the annotation's position
on the page as a factor considered during training. See [ Managing datasets
](https://cloud.google.com/natural-language/automl/entity-
analysis/docs/datasets?hl=ko#label-items) for more information.

##  April 10, 2019

**FEATURE:**

AutoML Natural Language Entity Extraction Beta has been released.

**FEATURE:**

AutoML Natural Language Sentiment Analysis Beta has been released.

**ISSUE:**

Microsoft Edge and Microsoft Internet Explorer do not support all features of
AutoML Natural Language Entity Extraction. If you are having problems, try
Google Chrome, Safari, or Firefox.

**ISSUE:**

Microsoft Edge and Microsoft Internet Explorer do not support all features of
AutoML Natural Language Sentiment Analysis. If you are having problems, try
Google Chrome, Safari, or Firefox.

##  January 22, 2019

**CHANGED:**

Beginning January 22, 2019, inactive models are subject to automatic
undeployment. An inactive model is one that has not been used for prediction
in 60 days. An undeployed model is not available for use until you explicitly
redeploy it using a method that will be made available in advance of any
undeployments.

##  November 01, 2018

**CHANGED:**

The AutoML Natural Language Text Classification service account requires
additional permissions to access project resources when using the AutoML
Natural Language Text Classification UI. You must add the role `
serviceusage.serviceUsageAdmin ` . See step 8 in [ Before You Begin
](https://cloud.google.com/natural-language/automl/docs/before-you-
begin?hl=ko) .

##  August 24, 2018

**CHANGED:**

The URL for the AutoML Natural Language Text Classification UI has changed to
` https://console.cloud.google.com/natural-language ` . The previous URL `
https://beta-dot-custom-vision.appspot.com/text/ ` will remain active.

##  July 24, 2018

**FEATURE:**

**AutoML Natural Language Text Classification Beta Release**

Models created during the EAP will continue to be valid for the Beta. You do
not need to recreate/retrain models. However, the format of resource IDs
(dataset IDs, model IDs, and operation IDs) is changing. If you are using
hardcoded resource IDs, you need to obtain new IDs for those resources (using
the get or list method) by August 31, 2018.

**Note:** Enabling the AutoML API for your project automatically also enables
the Cloud Vision API, Cloud Translation API, and Cloud Natural Language API.
Disabling any of these three APIs will also disable the AutoML API.

##  June 07, 2018

**CHANGED:**

The earlier version of the AutoML Natural Language Text Classification UI has
been deprecated. Attempts to connect to the older UI are redirected to the new
UI.

##  May 21, 2018

**CHANGED:**

The refresh of the AutoML Natural Language Text Classification EAP release
introduces a new UI design and a new API.

##  April 02, 2018

**CHANGED:**

AutoML Natural Language Text Classification has changes to its modeling logic.
You may notice an increase in training latency as well as potential
improvements in training performance.

##  February 07, 2018

**FEATURE:**

AutoML Natural Language Text Classification EAP release

