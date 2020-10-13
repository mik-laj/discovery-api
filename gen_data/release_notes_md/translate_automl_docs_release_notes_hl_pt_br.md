#  Notas da versão

Nesta página, você encontra as atualizações de produção do AutoML Translation.
Recomendamos que os desenvolvedores do AutoML Translation verifiquem
periodicamente esta lista para conhecer as novidades. As principais mudanças
também serão anunciadas na lista de e-mails do grupo [ google-translate-api
](https://groups.google.com/forum/?hl=pt_br#!forum/google-translate-api) (em
inglês).

É possível ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas da versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt_br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/automl-translate-
release-notes.xml `

##  July 17, 2020

**FEATURE:**

For test data, added support for the ` .tmx ` file type when evaluating
existing models. For more information, see [ Evaluating models
](https://cloud.google.com/translate/automl/docs/evaluate?hl=pt_br#evaluate_and_compare_models_using_a_new_test_set)
.

##  April 03, 2020

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview?hl=pt_br) is now in [ beta stage
](https://cloud.google.com/products/?hl=pt_br#product-launch-stages) .

##  October 14, 2019

**FEATURE:**

AutoML Translation is now generally available. Translations are now faster and
quality should be improved or on par with previous versions; individual
results will vary depending on your datasets. In addition, quality
improvements can vary across language pairs.

**CHANGED:**

**Model lifetime** AutoML Models run on a managed platform that is regularly
upgraded. AutoML Models need to be re-trained at least every 18 months to
ensure consistent performance and stability in translations over time and to
get any benefits of the upgrades since original training. Models created
before AutoML GA (for example, models created during service Alpha /Beta) need
to be re-trained within 18 months of GA to move all assets to the newest
version of the platform.

**FEATURE:**

AutoML Translation has upgraded its Google NMT base models onto a new training
architecture so that it now runs end-to-end on upgraded [ TPUs
](https://cloud.google.com/tpu/docs/tpus?hl=pt_br) . Going forward, all
training using Google NMT as the base model trains and serves on TPUs.

**CHANGED:**

Customers already using AutoML might experience additional differences between
v1 and previous versions of the service:

  * Data validation now provides warnings on data import to indicate certain data is not usable for training jobs. 
  * Data import takes longer in order to support data validation. 
  * To achieve higher quality on the new architecture, training durations are longer. 

##  September 04, 2019

**FEATURE:**

AutoML Translation has enabled Google Cloud Platform (GCP) Console-based UI
for all its customers. This improves the Cloud AutoML Translation experience
by adding UI elements such as controls to sort/filter datasets, which provides
consistency with the rest of GCP and allows for faster release of new
features.

**CHANGED:**

The URL for the AutoML Translation UI has changed to
https://console.cloud.google.com/translation.

##  December 11, 2018

**CHANGED:**

The minimum number of sentence pairs required to train a custom model has
changed. If you don't explicitly specify training, validation, and test sets,
the minimum number of sentence pairs is 1000. If you do explicitly specify
training, validation, and test sets, the minimum number of pairs used for
validation and test is 100 each.

##  November 01, 2018

**CHANGED:**

The AutoML Translation service account requires additional permissions to
access project resources when using the AutoML Translation UI. You must add
the role ` serviceusage.serviceUsageAdmin ` . See step 8 in [ Before You Begin
](https://cloud.google.com/translate/automl/docs/before-you-begin?hl=pt_br) .

##  September 18, 2018

**CHANGED:**

AutoML Translation supports many new languages as source or target languages
paired with English, bringing the total number of supported language pairs to
100. See [ Language Support for Custom Models
](https://cloud.google.com/translate/automl/docs/languages?hl=pt_br) for the
complete list.

##  August 24, 2018

**CHANGED:**

The URL for the AutoML Translation UI has changed to
https://cloud.google.com/automl/ui/translation. The previous URL https://beta-
dot-custom-vision.appspot.com/translation/ will remain active.

##  August 02, 2018

**CHANGED:**

AutoML Translation supports Swahili ( ` sw ` ) as a target language from
English ( ` en ` ) as a source language.

Language Pair  |  Language Codes  
---|---  
Swahili <\- English  |  ` sw ` <\- ` en `  
  
##  July 24, 2018

**FEATURE:**

Models created during the EAP will continue to be valid for the Beta. You do
not need to recreate/retrain models. However, the format of resource IDs
(dataset IDs, model IDs, and operation IDs) is changing. If you are using
hardcoded resource IDs, you need to obtain new IDs for those resources (using
the get or list method) by August 31, 2018.

**Note:** Enabling the AutoML API for your project automatically also enables
the Cloud Vision API, Cloud Translation API, and Cloud Natural Language API.
Disabling any of these three APIs will also disable the AutoML API

##  May 24, 2018

**CHANGED:**

The refresh of the AutoML Translation EAP release introduces a new UI design
and a new API. The previous version of the AutoML Translation EAP UI is
deprecated, and the new AutoML API is not compatible with the previous API.

You must reimport the contents any previously created datasets. You can find
the original contents at ` gs://{project-id}-vcm/{dataset-
name}/uploads/{document-name}.txt ` .

If you used the previous version of the AutoML Translation UI to create custom
models based on other custom translation models (rather than the default
Google Neural Machine Translation model), you will also need to recreate or
retrain those models using the new UI.

##  March 30, 2018

**CHANGED:**

  * The AutoML Translation EAP web application now enables you to build a custom model based on another custom translation model that you built. 
  * A sample Java application is available that demonstrates how to send a request for translation and obtain the response back. 

##  February 27, 2018

**CHANGED:**

The following language translation pairs have been added:

Language Pair  |  Language Codes  
---|---  
Dutch -> English  |  ` nl ` -> ` en `  
Hebrew -> English  |  ` iw ` -> ` en `  
  
##  February 05, 2018

**CHANGED:**

The following language translation pairs have been added:

Language Pair  |  Language Codes  
---|---  
Arabic -> English  |  ` ar ` -> ` ens `  
Chinese (Simplified) -> English  |  ` zh-CN ` -> ` ens `  
French <-> English  |  ` fr ` <-> ` ens `  
German -> English  |  ` de ` -> ` ens `  
Italian <-> English  |  ` it ` <-> ` ens `  
Japanese <\- English  |  ` ja ` <\- ` ens `  
Korean <\- English  |  ` ko ` <\- ` ens `  
Portuguese (Portugal, Brazil) -> English  |  ` pt ` -> ` ens `  
Russian <-> English  |  ` ru ` <-> ` ens `  
Turkish <\- English  |  ` tr ` <\- ` en `  
  
##  January 17, 2018

**FEATURE:**

AutoML Translation EAP release.

