#  版本说明

本页面记录了 AutoML Tables 的正式版更新。您可以定期查看此页面，了解有关新增功能、功能更新、问题修复、已知问题和弃用功能的公告。

如需获取 AutoML Tables 的已知问题列表，请参阅 [ 已知问题 ](https://cloud.google.com/automl-
tables/docs/known-issues?hl=zh-cn) 。

**Beta 版**

此产品目前处于预发布状态，可能会更改或仅提供有限支持。如需了解详情，请参阅 [ 产品发布阶段
](https://cloud.google.com/products?hl=zh-cn#product-launch-stages) 。

您可以在 [ Google Cloud 版本说明 ](https://cloud.google.com/release-notes?hl=zh-cn)
页面上查看 Google Cloud 所有产品的最新产品动态。

要接收最新产品动态，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接添加 Feed 网址： `
https://cloud.google.com/feeds/automl-tables-release-notes.xml `

##  June 01, 2020

**FEATURE:**

Support for [ feature importance with batch predictions
](https://cloud.google.com/automl-tables/docs/explain?hl=zh-
cn#getting_local_feature_importance_for_batch_predictions) .

##  April 03, 2020

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview?hl=zh-cn) is now in [ beta stage
](https://cloud.google.com/products/?hl=zh-cn#product-launch-stages) .

##  November 21, 2019

**FEATURE:**

As part of AI Explanations, AutoML Tables now provides the option to show how
each feature impacted an online prediction. This capability is called local
feature importance, and is calculated using the Sampled Shapley method. [
Learn more ](https://cloud.google.com/automl-tables/docs/features?hl=zh-
cn#local) .

##  November 18, 2019

**FEATURE:**

Support for the European Union region, including the ability to configure
AutoML Tables to store your data at rest and perform machine learning
processing only in the European Union. [ Learn more
](https://cloud.google.com/automl-tables/docs/locations?hl=zh-cn) .

**FEATURE:**

Support for exporting AutoML Tables models to Cloud Storage, and then use
Docker to make the model available for predictions. [ Learn more
](https://cloud.google.com/automl-tables/docs/model-export?hl=zh-cn) .

**FEATURE:**

Support for using Stackdriver Logging to see final model hyperparameters as
well as hyperparameters used during training trials. [ Learn more
](https://cloud.google.com/automl-tables/docs/logging?hl=zh-cn) .

##  November 15, 2019

**CHANGED:**

  * Support for up to 500 distinct values for Categorical target column. 
  * Support for **Precision at recall** and **Recall at precision** optimization objectives for classification models. [ Learn more ](https://cloud.google.com/automl-tables/docs/train?hl=zh-cn#opt-obj) . 

**CHANGED:**

The AutoML Tables Python client library now includes additional methods that
simplify using the AutoML API for common AutoML Tables tasks. [ Learn more
](https://cloud.google.com/automl-tables/docs/client-libraries?hl=zh-cn) .

##  July 23, 2019

**CHANGED:**

Datasets smaller than 100,000 rows (and larger than the minimum size of 1,000
rows) are now [ fully supported ](https://cloud.google.com/automl-
tables/docs/known-issues?hl=zh-cn#fixed) .

##  June 28, 2019

**CHANGED:**

Support for the "early stopping" feature. The model training process now stops
by default when the search process is no longer finding better performing
models. Early stopping can also [ be disabled
](https://cloud.google.com/automl-tables/docs/train?hl=zh-cn) .

##  June 12, 2019

**CHANGED:**

  * Support for up to 100 distinct values for Categorical target column. 
  * Support for BigQuery views. 

##  April 29, 2019

**CHANGED:**

Filename change for CSV output files for batch predictions; now ` tables_1.csv
` , ` tables_2.csv ` and so on. [ Learn more
](https://cloud.google.com/automl-tables/docs/predict-batch?hl=zh-cn#csv-
results) .

##  April 10, 2019

**FEATURE:**

AutoML Tables Beta Release

##  March 19, 2019

**ISSUE:**

You must deploy a model before you can request online predictions using that
model. Once you deploy a model, it remains deployed until you undeploy it. You
can deploy and undeploy models by using Google Cloud Platform Console or by
using the Cloud AutoML. [ Learn more ](https://cloud.google.com/automl-
tables/docs/models?hl=zh-cn#deploy) .

##  December 14, 2018

**FEATURE:**

AutoML Tables EAP release

**ISSUE:**

Only the ` us-central1 ` location is supported.

