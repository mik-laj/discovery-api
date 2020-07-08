#  Notas da versão

Nesta página, você encontra as atualizações de produção do AutoML Tables.
Acesse-a periodicamente para ver avisos de recursos novos ou atualizados,
correções de bugs, problemas conhecidos e recursos obsoletos.

Veja uma lista de problemas conhecidos do AutoML Tables em [ Problemas
conhecidos ](https://cloud.google.com/automl-tables/docs/known-issues?hl=pt-
br) .

**Beta**

Este produto está em estado de pré-lançamento, podendo ser alterado ou ter
suporte limitado. Para mais informações, consulte as [ etapas de lançamento do
produto ](https://cloud.google.com/products?hl=pt-br#product-launch-stages) .

Veja as atualizações mais recentes de todos os produtos do Google Cloud na
página [ Notas de versão do Google Cloud ](https://cloud.google.com/release-
notes?hl=pt-br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/automl-tables-release-
notes.xml `

##  June 01, 2020

**FEATURE:**

Support for [ feature importance with batch predictions
](https://cloud.google.com/automl-tables/docs/explain?hl=pt-
br#getting_local_feature_importance_for_batch_predictions) .

##  April 03, 2020

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview?hl=pt-br) is now in [ beta stage
](https://cloud.google.com/products/?hl=pt-br#product-launch-stages) .

##  November 21, 2019

**FEATURE:**

As part of AI Explanations, AutoML Tables now provides the option to show how
each feature impacted an online prediction. This capability is called local
feature importance, and is calculated using the Sampled Shapley method. [
Learn more ](https://cloud.google.com/automl-tables/docs/features?hl=pt-
br#local) .

##  November 18, 2019

**FEATURE:**

Support for the European Union region, including the ability to configure
AutoML Tables to store your data at rest and perform machine learning
processing only in the European Union. [ Learn more
](https://cloud.google.com/automl-tables/docs/locations?hl=pt-br) .

**FEATURE:**

Support for exporting AutoML Tables models to Cloud Storage, and then use
Docker to make the model available for predictions. [ Learn more
](https://cloud.google.com/automl-tables/docs/model-export?hl=pt-br) .

**FEATURE:**

Support for using Stackdriver Logging to see final model hyperparameters as
well as hyperparameters used during training trials. [ Learn more
](https://cloud.google.com/automl-tables/docs/logging?hl=pt-br) .

##  November 15, 2019

**CHANGED:**

  * Support for up to 500 distinct values for Categorical target column. 
  * Support for **Precision at recall** and **Recall at precision** optimization objectives for classification models. [ Learn more ](https://cloud.google.com/automl-tables/docs/train?hl=pt-br#opt-obj) . 

**CHANGED:**

The AutoML Tables Python client library now includes additional methods that
simplify using the AutoML API for common AutoML Tables tasks. [ Learn more
](https://cloud.google.com/automl-tables/docs/client-libraries?hl=pt-br) .

##  July 23, 2019

**CHANGED:**

Datasets smaller than 100,000 rows (and larger than the minimum size of 1,000
rows) are now [ fully supported ](https://cloud.google.com/automl-
tables/docs/known-issues?hl=pt-br#fixed) .

##  June 28, 2019

**CHANGED:**

Support for the "early stopping" feature. The model training process now stops
by default when the search process is no longer finding better performing
models. Early stopping can also [ be disabled
](https://cloud.google.com/automl-tables/docs/train?hl=pt-br) .

##  June 12, 2019

**CHANGED:**

  * Support for up to 100 distinct values for Categorical target column. 
  * Support for BigQuery views. 

##  April 29, 2019

**CHANGED:**

Filename change for CSV output files for batch predictions; now ` tables_1.csv
` , ` tables_2.csv ` and so on. [ Learn more
](https://cloud.google.com/automl-tables/docs/predict-batch?hl=pt-br#csv-
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
tables/docs/models?hl=pt-br#deploy) .

##  December 14, 2018

**FEATURE:**

AutoML Tables EAP release

**ISSUE:**

Only the ` us-central1 ` location is supported.

