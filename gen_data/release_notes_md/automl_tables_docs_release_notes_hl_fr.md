#  Notes de version

Cette page répertorie les mises à jour en production d'AutoML Tables.
Consultez-la régulièrement pour obtenir des informations sur les
fonctionnalités nouvelles ou mises à jour, les corrections de bugs, les
problèmes connus et les fonctionnalités obsolètes.

Pour obtenir la liste des problèmes connus d'AutoML Tables, consultez la page
[ Problèmes connus ](https://cloud.google.com/automl-tables/docs/known-
issues?hl=fr) .

**Beta**

Ce produit est disponible dans sa version préliminaire, et peut changer ou
bénéficier d'une assistance limitée. Pour en savoir plus, consultez les [
étapes de lancement des produits
](https://cloud.google.com/products?hl=fr#product-launch-stages) .

Vous pouvez consulter les dernières mises à jour de l'ensemble des produits
Google Cloud sur la page [ Notes de version de Google Cloud
](https://cloud.google.com/release-notes?hl=fr) .

Pour recevoir les dernières mises à jour concernant ce produit, ajoutez l'URL
de cette page à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou ajoutez l'URL
du flux directement : ` https://cloud.google.com/feeds/automl-tables-release-
notes.xml `

##  June 01, 2020

**FEATURE:**

Support for [ feature importance with batch predictions
](https://cloud.google.com/automl-
tables/docs/explain?hl=fr#getting_local_feature_importance_for_batch_predictions)
.

##  April 03, 2020

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview?hl=fr) is now in [ beta stage
](https://cloud.google.com/products/?hl=fr#product-launch-stages) .

##  November 21, 2019

**FEATURE:**

As part of AI Explanations, AutoML Tables now provides the option to show how
each feature impacted an online prediction. This capability is called local
feature importance, and is calculated using the Sampled Shapley method. [
Learn more ](https://cloud.google.com/automl-tables/docs/features?hl=fr#local)
.

##  November 18, 2019

**FEATURE:**

Support for the European Union region, including the ability to configure
AutoML Tables to store your data at rest and perform machine learning
processing only in the European Union. [ Learn more
](https://cloud.google.com/automl-tables/docs/locations?hl=fr) .

**FEATURE:**

Support for exporting AutoML Tables models to Cloud Storage, and then use
Docker to make the model available for predictions. [ Learn more
](https://cloud.google.com/automl-tables/docs/model-export?hl=fr) .

**FEATURE:**

Support for using Stackdriver Logging to see final model hyperparameters as
well as hyperparameters used during training trials. [ Learn more
](https://cloud.google.com/automl-tables/docs/logging?hl=fr) .

##  November 15, 2019

**CHANGED:**

  * Support for up to 500 distinct values for Categorical target column. 
  * Support for **Precision at recall** and **Recall at precision** optimization objectives for classification models. [ Learn more ](https://cloud.google.com/automl-tables/docs/train?hl=fr#opt-obj) . 

**CHANGED:**

The AutoML Tables Python client library now includes additional methods that
simplify using the AutoML API for common AutoML Tables tasks. [ Learn more
](https://cloud.google.com/automl-tables/docs/client-libraries?hl=fr) .

##  July 23, 2019

**CHANGED:**

Datasets smaller than 100,000 rows (and larger than the minimum size of 1,000
rows) are now [ fully supported ](https://cloud.google.com/automl-
tables/docs/known-issues?hl=fr#fixed) .

##  June 28, 2019

**CHANGED:**

Support for the "early stopping" feature. The model training process now stops
by default when the search process is no longer finding better performing
models. Early stopping can also [ be disabled
](https://cloud.google.com/automl-tables/docs/train?hl=fr) .

##  June 12, 2019

**CHANGED:**

  * Support for up to 100 distinct values for Categorical target column. 
  * Support for BigQuery views. 

##  April 29, 2019

**CHANGED:**

Filename change for CSV output files for batch predictions; now ` tables_1.csv
` , ` tables_2.csv ` and so on. [ Learn more
](https://cloud.google.com/automl-tables/docs/predict-batch?hl=fr#csv-results)
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
tables/docs/models?hl=fr#deploy) .

##  December 14, 2018

**FEATURE:**

AutoML Tables EAP release

**ISSUE:**

Only the ` us-central1 ` location is supported.

