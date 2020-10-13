#  リリースノート

このページには、AutoML Tables
に関する更新内容が記載されています。このページを定期的にチェックして、新機能や更新された機能、バグ修正、既知の問題、非推奨になった機能に関するお知らせを確認してください。

AutoML Tables の既知の問題の一覧については、 [ 既知の問題 ](https://cloud.google.com/automl-
tables/docs/known-issues?hl=ja) をご覧ください。

**ベータ版**

このプロダクトはプレリリース版の状態で、変更やサポート制限が行われる可能性があります。 詳細については、 [ プロダクトのリリース ステージ
](https://cloud.google.com/products?hl=ja#product-launch-stages) をご覧ください。

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/automl-tables-release-notes.xml `
を直接追加します。

##  June 01, 2020

**FEATURE:**

Support for [ feature importance with batch predictions
](https://cloud.google.com/automl-
tables/docs/explain?hl=ja#getting_local_feature_importance_for_batch_predictions)
.

##  April 03, 2020

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview?hl=ja) is now in [ beta stage
](https://cloud.google.com/products/?hl=ja#product-launch-stages) .

##  November 21, 2019

**FEATURE:**

As part of AI Explanations, AutoML Tables now provides the option to show how
each feature impacted an online prediction. This capability is called local
feature importance, and is calculated using the Sampled Shapley method. [
Learn more ](https://cloud.google.com/automl-tables/docs/features?hl=ja#local)
.

##  November 18, 2019

**FEATURE:**

Support for the European Union region, including the ability to configure
AutoML Tables to store your data at rest and perform machine learning
processing only in the European Union. [ Learn more
](https://cloud.google.com/automl-tables/docs/locations?hl=ja) .

**FEATURE:**

Support for exporting AutoML Tables models to Cloud Storage, and then use
Docker to make the model available for predictions. [ Learn more
](https://cloud.google.com/automl-tables/docs/model-export?hl=ja) .

**FEATURE:**

Support for using Stackdriver Logging to see final model hyperparameters as
well as hyperparameters used during training trials. [ Learn more
](https://cloud.google.com/automl-tables/docs/logging?hl=ja) .

##  November 15, 2019

**CHANGED:**

  * Support for up to 500 distinct values for Categorical target column. 
  * Support for **Precision at recall** and **Recall at precision** optimization objectives for classification models. [ Learn more ](https://cloud.google.com/automl-tables/docs/train?hl=ja#opt-obj) . 

**CHANGED:**

The AutoML Tables Python client library now includes additional methods that
simplify using the AutoML API for common AutoML Tables tasks. [ Learn more
](https://cloud.google.com/automl-tables/docs/client-libraries?hl=ja) .

##  July 23, 2019

**CHANGED:**

Datasets smaller than 100,000 rows (and larger than the minimum size of 1,000
rows) are now [ fully supported ](https://cloud.google.com/automl-
tables/docs/known-issues?hl=ja#fixed) .

##  June 28, 2019

**CHANGED:**

Support for the "early stopping" feature. The model training process now stops
by default when the search process is no longer finding better performing
models. Early stopping can also [ be disabled
](https://cloud.google.com/automl-tables/docs/train?hl=ja) .

##  June 12, 2019

**CHANGED:**

  * Support for up to 100 distinct values for Categorical target column. 
  * Support for BigQuery views. 

##  April 29, 2019

**CHANGED:**

Filename change for CSV output files for batch predictions; now ` tables_1.csv
` , ` tables_2.csv ` and so on. [ Learn more
](https://cloud.google.com/automl-tables/docs/predict-batch?hl=ja#csv-results)
.

##  April 10, 2019

**FEATURE:**

AutoML Tables Beta Release

##  March 19, 2019

**ISSUE:**

You must deploy a model before you can request online predictions using that
model. Once you deploy a model, it remains deployed until you undeploy it. You
can deploy and undeploy models by using Google Cloud Platform Console or by
using the Cloud AutoML. [ Learn more ](https://cloud.google.com/automl-
tables/docs/models?hl=ja#deploy) .

##  December 14, 2018

**FEATURE:**

AutoML Tables EAP release

**ISSUE:**

Only the ` us-central1 ` location is supported.

