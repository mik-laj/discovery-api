#  Release Notes

This page documents production updates to AutoML Tables. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

For a list of known issues for AutoML Tables, see [ Known issues ](/automl-
tables/docs/known-issues) .

**Beta**

This product is covered by the [ Pre-GA Offerings Terms ](/terms/service-
terms#1) of the Google Cloud Platform Terms of Service. Pre-GA products may
have limited support, and changes to pre-GA products may not be compatible
with other pre-GA versions. For more information, see the [ launch stage
descriptions ](/products#product-launch-stages) .

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/automl-tables-release-notes.xml
`

##  April 03, 2020

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview) is now in [ beta stage
](https://cloud.google.com/products/#product-launch-stages) .

##  November 21, 2019

**FEATURE:**

As part of AI Explanations, AutoML Tables now provides the option to show how
each feature impacted an online prediction. This capability is called local
feature importance, and is calculated using the Sampled Shapley method. [
Learn more ](https://cloud.google.com/automl-tables/docs/features#local) .

##  November 18, 2019

**FEATURE:**

Support for the European Union region, including the ability to configure
AutoML Tables to store your data at rest and perform machine learning
processing only in the European Union. [ Learn more
](https://cloud.google.com/automl-tables/docs/locations) .

**FEATURE:**

Support for exporting AutoML Tables models to Cloud Storage, and then use
Docker to make the model available for predictions. [ Learn more
](https://cloud.google.com/automl-tables/docs/model-export) .

**FEATURE:**

Support for using Stackdriver Logging to see final model hyperparameters as
well as hyperparameters used during training trials. [ Learn more
](https://cloud.google.com/automl-tables/docs/logging) .

##  November 15, 2019

**CHANGED:**

  * Support for up to 500 distinct values for Categorical target column. 
  * Support for **Precision at recall** and **Recall at precision** optimization objectives for classification models. [ Learn more ](https://cloud.google.com/automl-tables/docs/train#opt-obj) . 

**CHANGED:**

The AutoML Tables Python client library now includes additional methods that
simplify using the AutoML API for common AutoML Tables tasks. [ Learn more
](https://cloud.google.com/automl-tables/docs/client-libraries) .

##  July 23, 2019

**CHANGED:**

Datasets smaller than 100,000 rows (and larger than the minimum size of 1,000
rows) are now [ fully supported ](https://cloud.google.com/automl-
tables/docs/known-issues#fixed) .

##  June 28, 2019

**CHANGED:**

Support for the "early stopping" feature. The model training process now stops
by default when the search process is no longer finding better performing
models. Early stopping can also [ be disabled
](https://cloud.google.com/automl-tables/docs/train) .

##  June 12, 2019

**CHANGED:**

  * Support for up to 100 distinct values for Categorical target column. 
  * Support for BigQuery views. 

##  April 29, 2019

**CHANGED:**

Filename change for CSV output files for batch predictions; now ` tables_1.csv
` , ` tables_2.csv ` and so on. [ Learn more
](https://cloud.google.com/automl-tables/docs/predict-batch#csv-results) .

##  April 10, 2019

**FEATURE:**

AutoML Tables Beta Release

##  March 19, 2019

**ISSUE:**

You must deploy a model before you can request online predictions using that
model. Once you deploy a model, it remains deployed until you undeploy it. You
can deploy and undeploy models by using Google Cloud Platform Console or by
using the Cloud AutoML. [ Learn more ](https://cloud.google.com/automl-
tables/docs/models#deploy) .

##  December 14, 2018

**FEATURE:**

AutoML Tables EAP release

**ISSUE:**

Only the ` us-central1 ` location is supported.

