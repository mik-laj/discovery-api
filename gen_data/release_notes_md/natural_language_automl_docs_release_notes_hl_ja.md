#  リリースノート

このページには AutoML Natural Language
の更新内容が記載されています。このページを定期的にチェックして、新機能や更新された機能、バグ修正、既知の問題、非推奨になった機能に関するお知らせを確認してください。

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/automl-language-release-notes.xml
` を直接追加します。

##  April 03, 2020

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview?hl=ja) is now in [ beta stage
](https://cloud.google.com/products/?hl=ja#product-launch-stages) .

##  March 20, 2020

**CHANGED:**

AutoML Natural Language now supports TIFF files as training data and input for
predictions.

**CHANGED:**

AutoML Natural Language now supports classification and sentiment analysis in
[ 20 languages ](https://cloud.google.com/natural-
language/automl/docs/languages?hl=ja#classification) .

##  January 30, 2020

**FEATURE:**

AutoML Natural Language now supports entity analysis in [ over 100 languages
](https://cloud.google.com/natural-
language/automl/docs/languages?hl=ja#entity_analysis) .

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
](https://cloud.google.com/natural-language/automl/docs/?hl=ja) for details
about all features.

##  October 30, 2019

**FEATURE:**

AutoML Natural Language offers you control over where your datasets and models
are stored and where machine learning takes place. In particular, you can
configure AutoML Natural Language to at rest and perform machine learning
processing in the European Union only. See [ Locations
](https://cloud.google.com/natural-language/automl/docs/locations?hl=ja) for
more information.

##  October 21, 2019

**FEATURE:**

AutoML Natural Language Text Classification now supports [ batch prediction
](https://cloud.google.com/natural-language/automl/docs/predict?hl=ja) .

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
analysis/docs/datasets?hl=ja#label-items) for more information.

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
begin?hl=ja) .

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

