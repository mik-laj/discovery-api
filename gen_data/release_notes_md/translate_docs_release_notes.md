#  Release notes

This page documents production updates to Cloud Translation. We recommend that
Cloud Translation developers periodically check this list for any new
announcements. Major changes are also announced via the [ google-translate-api
](https://groups.google.com/forum/#!forum/google-translate-api) mailing list.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/translate-release-notes.xml `

##  March 23, 2020

**CHANGED:**

The Cloud Translation Advanced API is migrating to a [ new quota system
](https://cloud.google.com/translate/quotas) that eliminates the distinction
between default and maximum limits.

This change will roll out gradually, starting on **March 30, 2020 and
continuing through April 30, 2020** . Since quotas define the usage limits for
a project or a user, the change could impact your billing.

##  November 05, 2019

**FEATURE:**

Cloud Translation v3, rebranded as _Translation API - Advanced_ , is now
generally available. In addition to the features of Cloud Translation API
v3beta1, Translation API - Advanced supports: * [ User labels
](https://cloud.google.com/translate/docs/labels) * [ Audit logging
](https://cloud.google.com/translate/docs/audit-logging) * [ Separate quotas
](https://cloud.google.com/translate/quotas#advanced) for batch translation
and for translation using AutoML models * [ Client libraries
](https://cloud.google.com/translate/docs/reference/libraries/v3/overview-v3)
for additional languages PHP, GO, C#, and Ruby

**Note:** Existing users should pay careful attention to client library
versions before updating. Translation API - Basic and Translation API -
Advanced client libraries are not backward or forward compatible.

Translation API - Advanced also fixes bugs from the v3beta1 version, notably
for the [ glossary
](https://cloud.google.com/translate/docs/advanced/glossary) feature.

**CHANGED:**

Translation API - Advanced has a revised pricing structure. Each account
receives $10 worth of free usage per month, applied to usage of any of these
SKUs:

  * Neural Translation Model Predictions (D90A-CFB2-7CCD) 
  * Neural Translation Model Predictions In Translation V3 (E205-31DB-F1F4) 
  * Phrase-Based Translation Model Predictions (53BA-5E1D-4314) 

This credit replaces the free tier for Text Translation requests using NMT for
0-500k characters on Translation API v3beta1.

##  April 10, 2019

**FEATURE:**

Cloud Translation API [ v3beta1
](https://cloud.google.com/translate/docs/intro-to-v3) is now available. This
release includes support for [ AutoML
](https://cloud.google.com/translate/docs/translating-text-v3#automl-mode)
models when translating text. In addition, the release includes the following
new features:

  * [ custom glossaries ](https://cloud.google.com/translate/docs/glossary) for customer-specific terminology, 
  * [ batch translation ](https://cloud.google.com/translate/docs/batch-translation) for asynchronous translation of .txt, .tsv, and .html files saved in Google Cloud Storage. 

v3 API offers monthly [ free tier
](https://cloud.google.com/translate/pricing) , and guarded by new [ Quotas
and Limit ](https://cloud.google.com/translate/quotas) . Learn more on how to
use new features and [ client library
](https://cloud.google.com/translate/docs/reference/client-libraries) in v3.

##  September 10, 2018

**CHANGED:**

The maximum values for **Characters per 100 seconds** quotas have increased.
The new maximum for both **Characters per 100 seconds per project** and
**Characters per 100 seconds per project per user** is **10,000,000
characters** . The default quotas remain unchanged.

The recently updated default **Characters per day** quota has been adjusted
again; it is now **1 billion characters** .

See [ Quotas & Limits ](https://cloud.google.com/translate/quotas) .

##  August 22, 2018

**CHANGED:**

The change to the default **Characters per day** quota has taken effect. It is
now **unlimited** . See [ Quotas & Limits
](https://cloud.google.com/translate/quotas) .

##  August 01, 2018

**CHANGED:**

On August 15, the default **Characters per day** quota will be updated to
**unlimited** . For more information, see [ Quotas & Limits
](https://cloud.google.com/translate/quotas) .

##  November 01, 2017

**CHANGED:**

The maximum **Characters per day** quota has been updated to **unlimited** .
For more information, see [ Quotas & Limits
](https://cloud.google.com/translate/quotas) .

##  October 25, 2017

**CHANGED:**

The Neural Machine Translation (NMT) models for the following languages have
been updated for improved translation quality:

  * English (en) <-> French (fr) 
  * English (en) -> German (de) 
  * English (en) -> Spanish (es) 

For a list of all NMT supported languages, see [ Language Support for the
Neural Machine Translation Model
](https://cloud.google.com/translate/docs/languages#languages-nmt) .

##  September 26, 2017

**CHANGED:**

Quotas for usage of the Translation API have been updated. The quota for
characters requested per 100 seconds, per project has been updated to a
maximum of 1,000,000. While the quotas are updated, you may see a brief period
where the maximum is not limited to the per project maximum. The quota for
characters requested per 100 seconds, per user remains at 100,000 characters
per user, per project. For more information, see [ Quotas & Limits
](https://cloud.google.com/translate/quotas) .

##  September 15, 2017

**CHANGED:**

The Translation API has added support for 70 new languages in the Neural
Machine Translation (NMT) model. For a list of all NMT supported languages,
see [ Language Support for the Neural Machine Translation Model
](https://cloud.google.com/translate/docs/languages#languages-nmt) .

##  June 19, 2017

**CHANGED:**

The Translation API no longer supports conditional HTTPS requests. ` If-Match
` , ` If-None-Match ` , or ` ETag ` headers in requests to the Translation API
are ignored. The Translation API returns a status code of 200 for successful
requests, but does not return a status code of 304 for conditional HTTPS
requests. Conditional HTTPS requests are billed as a normal request to the
Translation API.

**CHANGED:**

The ` https://www.googleapis.com/language/translate/v2 ` endpoint now supports
the Neural Machine Translation (NMT) model. However, we recommend that you use
the ` https://translation.googleapis.com/language/translate/v2 ` endpoint for
requests to the Translation API.

##  April 06, 2017

**CHANGED:**

The Cloud Translation API is no longer taking requests for access to the
Premium Edition (Beta). Instead, the premium features of the Cloud Translation
API have been made generally available in the Standard Edition.

**FEATURE:**

You now have access to the robust translation features available using the [
Neural Machine Translation (NMT) model
](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html) .
There is no difference in pricing between the standard, Phrase-Based Machine
Translation (PBMT) model, and the NMT model.

By default, when you make a translation request to the Cloud Translation API,
your text is translated using the NMT model. If the NMT model is not supported
for the requested language translation pair, or if you explicitly request it,
the PBMT model is used.

In order for your request to be translated using the NMT model, you must send
your request to the current Translation API endpoint: `
https://translation.googleapis.com/language/translate/v2 ` . The `
https://www.googleapis.com/language/translate/v2 ` endpoint does not support
the NMT model.

NMT models are computationally intensive and may take more time to translate
your query as compared to the same query translated using the PBMT model. If
your application is latency sensitive, we recommend that you try both models
to determine which best fits your needs for response time.

**FEATURE:**

The [ ` model `
](https://cloud.google.com/translate/docs/reference/translate.html#body.QUERY_PARAMETERS.model)
query parameter has been added to the ` translate ` method. You can use the
model parameter to explicitly specify the translation model for your request.
Specify ` base ` to use the PBMT model, and ` nmt ` to use the NMT model.

If you do not specify a ` model ` parameter for your request, then ` nmt ` is
used.

If you specify the ` nmt ` model, and the requested language translation pair
is not supported for the NMT model, then the request is translated using the `
base ` model.

##  November 15, 2016

**FEATURE:**

Changed API endpoint from ` www.googleapis.com ` to `
translation.googleapis.com ` .

**DEPRECATED:**

API endpoint of ` www.googleapis.com ` will continue to work, but migrate code
to ` translation.googleapis.com ` to take advantage of the latest features.

Send feedback

