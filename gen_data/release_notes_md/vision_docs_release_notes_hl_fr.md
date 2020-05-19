#  Notes de version

Cette page répertorie les mises à jour en production de l'API Cloud Vision.
Nous recommandons aux développeurs qui utilisent l'API Cloud Vision de
consulter régulièrement cette liste pour prendre connaissance des nouvelles
annonces.

Pour recevoir les dernières mises à jour concernant ce produit, ajoutez l'URL
de cette page à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou ajoutez l'URL
du flux directement : ` https://cloud.google.com/feeds/vision-release-
notes.xml `

##  May 15, 2020

**CHANGED:**

**OCR model upgrades**

The ` text_detection ` and ` document_text_detection ` models have been
upgraded to newer versions. The API interface and client library will be the
same as previous version. The API follows the same [ Service Level Agreement
](https://cloud.google.com/vision/sla?hl=fr) .

The legacy models can still be accessed until June 30, 2020. Specify
"builtin/legacy_20190601" in the [ ` model `
](https://cloud.google.com/vision/docs/reference/rest/v1/Feature?hl=fr) field
of a ` Feature ` object to get the old model results. After June 30, 2020 the
old models will not longer be offered.

For more information, see the [ product documentation
](https://cloud.google.com/vision/docs/ocr?hl=fr) .

##  April 11, 2020

**FEATURE:**

**CMEK compliance**

Vision API is now compliant with customer-managed encryption keys (CMEK). To
learn more, vist the [ CMEK compliance page
](https://cloud.google.com/vision/docs/cmek?hl=fr) . Please note that [
Product Search ](https://cloud.google.com/vision/product-search/docs/?hl=fr)
is _not_ CMEK compliant at this time.

##  February 24, 2020

**CHANGED:**

**SafeSearch Detection update**

The SafeSearch model has been upgraded to a newer version. The API interface
and client library will be the same as previous version. The API follows the
same [ Service Level Agreement ](https://cloud.google.com/vision/sla?hl=fr) .

For more information, see the [ product documentation
](https://cloud.google.com/vision/docs/detecting-safe-search?hl=fr) .

##  February 19, 2020

**CHANGED:**

**Cloud Vision API will not return gendered labels such as 'man' and 'woman'
after February 19, 2020**

[ Detecting labels ](https://cloud.google.com/vision/docs/labels?hl=fr) in an
image containing humans will result in non-gendered label such as 'person'
being returned. Our prior approach was to return gendered terms, like 'man' or
'woman'.

Given that a person's gender cannot be inferred by appearance, we have decided
to remove these labels in order to align with the [ Artificial Intelligence
Principles at Google ](https://ai.google/principles/) , specifically Principle
#2: Avoid creating or reinforcing unfair bias.

##  December 13, 2019

**FEATURE:**

**Regional endpoints available for OCR**

The Vision API now offers [ multi-regional support
](https://cloud.google.com/vision/docs/ocr?hl=fr) ( ` us ` and ` eu ` ) for
the OCR feature.

Using a multi-region endpoint enables you to configure the Vision API to store
and perform machine learning (OCR) on your data in the United States or
European Union.

##  October 30, 2019

**FEATURE:**

**Beta feature**

The following beta features are available in API version **v1p4beta1** :

  * Celebrity recognition. For more information, see [ Celebrity recognition ](https://cloud.google.com/vision/docs/celebrity-recognition?hl=fr) . 

##  September 12, 2019

**FEATURE:**

**OCR regional support**

You can now specify a continent-level region for data processing of OCR
requests. For more infomation, see the OCR how-to pages:

  * [ Detect text in images ](https://cloud.google.com/vision/docs/ocr?hl=fr#regionalization)
  * [ Detect handwriting in images ](https://cloud.google.com/vision/docs/handwriting?hl=fr#regionalization)
  * [ Detect text in files (PDF/TIFF) ](https://cloud.google.com/vision/docs/pdf?hl=fr#regionalization)

##  August 29, 2019

**CHANGED:**

Improved detection models are now default for the following features:

  * [ Logo Detection ](https://cloud.google.com/vision/docs/detecting-logos?hl=fr)
  * [ Landmark Detection ](https://cloud.google.com/vision/docs/detecting-landmarks?hl=fr)
  * [ Crop hints ](https://cloud.google.com/vision/docs/detecting-crop-hints?hl=fr)
  * [ Object Localization ](https://cloud.google.com/vision/docs/object-localizer?hl=fr)

The legacy model can still be accessed for 90 days by specifying
"builtin/legacy" in the [ ` model `
](https://cloud.google.com/vision/docs/reference/rest/v1/Feature?hl=fr) field
of a ` Feature ` object.

##  August 16, 2019

**CHANGED:**

**Spring framework integration**

If you write your applications in Java with the [ Spring Framework
](https://spring.io/projects/spring-framework) , we now provide a guide to
help you [ add Spring Cloud Vision API to your application
](https://cloud.google.com/vision/docs/adding-spring?hl=fr) . Spring Cloud
Vision can make it easier and more efficient to work with Cloud Vision.

##  June 07, 2019

**FEATURE:**

**General Availability (GA) release** . Support for online small batch file
annotation has been released as GA. For more information, see [ Online small
batch file annotation ](https://cloud.google.com/vision/docs/document-small-
batch?hl=fr) .

**FEATURE:**

**General Availability (GA) release** . Support for offline batch image
annotation has been released as GA. For more information, see [ Offline batch
image annotation ](https://cloud.google.com/vision/docs/batch?hl=fr) .

**CHANGED:**

**Model updates**

Improved detection models are now available for the following features:

  * [ Logo detection ](https://cloud.google.com/vision/docs/detecting-logos?hl=fr)
  * [ Landmark detection ](https://cloud.google.com/vision/docs/detecting-landmarks?hl=fr)
  * [ Crop hints ](https://cloud.google.com/vision/docs/detecting-crop-hints?hl=fr)

Specify "builtin/latest" in the [ ` model `
](https://cloud.google.com/vision/docs/reference/rest/v1/Feature?hl=fr) field
of a ` Feature ` object to use the new models.

We'll support both the current model and the new model the next 90 days. After
90 days the current detection models will be deprecated and only the new
detection models will be used for all logo, landmark, and crop hint detection
requests.

**CHANGED:**

**Languages update**

More languages (with associated ` languageHint ` codes) have been added to the
list of languages [ supported
](https://cloud.google.com/vision/docs/languages?hl=fr#supported-langs) by `
TEXT_DETECTION ` and ` DOCUMENT_TEXT_DETECTION ` . [ Experimentally supported
](https://cloud.google.com/vision/docs/languages?hl=fr#experimental-langs)
languages and [ mapped languages
](https://cloud.google.com/vision/docs/languages?hl=fr#mapped-langs) lists
have also been added.

##  May 13, 2019

**CHANGED:**

**OCR Model Updates**

An [ improved OCR model ](https://cloud.google.com/vision/docs/release-
notes?hl=fr#september2018) is now the default for [ Text detection (OCR)
](https://cloud.google.com/vision/docs/detecting-text?hl=fr) .

The legacy model can still be accessed for 90 days by specifying
"builtin/legacy" in the [ ` model `
](https://cloud.google.com/vision/docs/reference/rest/v1/Feature?hl=fr) field
of a ` Feature ` object.

##  April 10, 2019

**FEATURE:**

**Beta features**

The following beta features are available in API version **v1p4beta1** :

  * **Online small batch file annotation** . Performs synchronous image detection and annotation for a batch of files (currently "application/pdf", "image/tiff" and "image/gif"). The API will extract at most 5 frames (gif) or pages (pdf or tiff) of your choosing from each file provided and perform detection and annotation for each image extracted. [ Learn more ](https://cloud.google.com/vision/docs/document-small-batch?hl=fr) . 
  * **Offline batch image annotation** . Allows users to call any Cloud Vision API feature type on a batch of images and perform asynchronous image detection and annotation on the list of images. [ Learn more ](https://cloud.google.com/vision/docs/batch?hl=fr) . 

##  December 12, 2018

**FEATURE:**

**Handwriting OCR feature General Availability (GA) release**

Support for handwriting OCR in document text detection has been released as
GA. For more information, see [ Detect handwriting in an image
](https://cloud.google.com/vision/docs/handwriting?hl=fr) .

##  September 28, 2018

**CHANGED:**

**Logo and OCR model updates**

Improved detection models are now available for the following features:

  * [ Logo Detection ](https://cloud.google.com/vision/docs/detecting-logos?hl=fr)
  * [ Text Detection (OCR) ](https://cloud.google.com/vision/docs/detecting-text?hl=fr)

Specify "builtin/latest" in the [ ` model `
](https://cloud.google.com/vision/docs/reference/rest/v1/Feature?hl=fr) field
of a ` Feature ` object to use the new models.

We'll support both the current model and the new model the next 90 days. After
90 days the current detection models will be deprecated and only the new
detection models will be used for all logo and text (OCR) detection requests.

**FEATURE:**

Support for object localization has been released as GA. For more information,
see [ Detect multiple objects ](https://cloud.google.com/vision/docs/object-
localizer?hl=fr) .

##  July 24, 2018

**FEATURE:**

Support for PDF and TIFF files in document text detection has been released as
GA. For more information, see [ PDF/TIFF Document Text Detection
](https://cloud.google.com/vision/docs/pdf?hl=fr) .

**FEATURE:**

The following beta features are available in API version **v1p3beta1** :

  * Object localizer. For more information, see [ Detect multiple objects ](https://cloud.google.com/vision/docs/object-localizer?hl=fr) . 

**CHANGED:**

The Vision API can now detect handwriting in an image. To detect handwriting
in an image, specify the ` DOCUMENT_TEXT_DETECTION ` feature and include a
language hint of "en-t-i0-handwrit". For more information, see [ Detect
handwriting in images
](https://cloud.google.com/vision/docs/ocr?hl=fr#detecting_handwriting) .

##  April 06, 2018

**FEATURE:**

**Beta features**

The following beta features are available in API version **v1p2beta1** :

  * Support for PDF and TIFF files in document text detection. 

**FEATURE:**

**New features**

The beta features from [ December 4, 2017
](https://cloud.google.com/vision/docs/release-notes?hl=fr#december2017) are
now available in the v1 API (GA). These include:

  * Document text detection: confidence scores for all levels of results, auto language detection, support for multiple languages, and faster and more accurate results. 
  * Web entities detection: accepts geotag input as detection hint, and returns best guess labels describing the contents of the image. 
  * Safe Search detection: includes additional ` racy ` category to enhance adult content moderation. 

##  December 04, 2017

**FEATURE:**

The following beta features are available in API version **v1p1beta1** :

  * Document text detection: confidence scores for all levels of results, auto language detection, support for multiple languages, and faster and more accurate results. [ Learn more ](https://cloud.google.com/vision/docs/beta-ocr?hl=fr) . 
  * Web entities detection: accepts geotag input as detection hint, and returns best guess labels describing the contents of the image. [ Learn more ](https://cloud.google.com/vision/docs/beta-web-entities?hl=fr) . 
  * Safe Search detection: includes additional ` racy ` category to enhance adult content moderation. [ Learn more ](https://cloud.google.com/vision/docs/beta-explicit-content?hl=fr) . 

##  November 06, 2017

**CHANGED:**

**Document text detection language update** :

  * Additional languages supported. 
  * Automatic language detection ( ` languageHint ` is no longer required in your requests). 
  * Multiple languages supported per image. 
  * Faster and more accurate text detection results. 

##  June 21, 2017

**CHANGED:**

**Text detection model update** : The [ text detection
](https://cloud.google.com/vision/docs/detecting-text?hl=fr) model has been
updated to improve quality. There is no change in response structure.

**CHANGED:**

**Label detection model update** : The [ label detection
](https://cloud.google.com/vision/docs/detecting-labels?hl=fr) model has been
updated to improve quality. Label detection, which names objects inside an
image, now recognizes more than 10,000 entities.

##  May 18, 2017

**FEATURE:**

**Cloud Vision API General Availability (GA) release**

**FEATURE:**

**Crop hints** : Find the optimal crop for your images. [ Code samples
](https://cloud.google.com/vision/docs/crop-hints?hl=fr) .

**FEATURE:**

**Web entities and similar pages** : Return image-related information,
including web entities, matching pages, and fully- and partially matching
image URLs. [ Code samples ](https://cloud.google.com/vision/docs/detecting-
web?hl=fr) and [ tutorial ](https://cloud.google.com/vision/docs/internet-
detection?hl=fr) .

**FEATURE:**

**Document text detection** : Return full text annotations for dense OCR text.
[ How-to ](https://cloud.google.com/vision/docs/ocr?hl=fr) , [ code samples
](https://cloud.google.com/vision/docs/detecting-fulltext?hl=fr) , and [
tutorial ](https://cloud.google.com/vision/docs/fulltext-annotations?hl=fr) .

**FEATURE:**

**HTTP/HTTPS image URIs** : Process images from publicly-accessible HTTP and
HTTPS URLs.

