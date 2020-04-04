#  Release notes

This page documents production updates to Natural Language. We recommend that
Natural Language developers periodically check this list for any new
announcements. Major changes will also be announced via the [ cloud-nl-discuss
](https://groups.google.com/forum/#!forum/cloud-nl-discuss) mailing list.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/language-release-notes.xml `

##  March 20, 2020

**CHANGED:**

The Natural Language API now supports [ additional languages
](https://cloud.google.com/natural-language/docs/languages#sentiment_analysis)
for sentiment analysis.

##  February 20, 2020

**FEATURE:**

The Natural Language API now offers two [ multiregion endpoints
](https://cloud.google.com/natural-language/docs/locations) ( ` us-
language.googleapis.com ` and ` eu-language.googleapis.com ` ). Using a
multiregion endpoint enables you to configure the Natural Language API to
store and perform machine learning on your data in the United States or
European Union.

##  May 03, 2019

**FEATURE:**

The Natural Language API now supports [ Spanish
](https://cloud.google.com/natural-language/docs/languages) for entity
sentiment analysis.

##  April 04, 2019

**FEATURE:**

The Natural Language API now supports [ Russian
](https://cloud.google.com/natural-language/docs/languages) for entity
analysis and syntactic analysis, and Japanese for entity sentiment analysis.

**FEATURE:**

The ` analyzeEntities ` method identifies and returns [ additional entity
types ](https://cloud.google.com/natural-
language/docs/reference/rest/v1/Entity#Type) : phone numbers, addresses,
dates, prices, and numbers.

##  November 16, 2017

**FEATURE:**

Cloud Natural Language API version 1.2 GA release.

**FEATURE:**

The Natural Language API has released the new ` classifyText ` method that
analyzes text content and returns a content category for the content. For more
information, see [ Content Classification ](https://cloud.google.com/natural-
language/docs/basics#content-classification) .

##  September 19, 2017

**FEATURE:**

The Natural Language API ` v1 ` now supports entity sentiment analysis with
the ` analyzeEntitySentiment ` method. Entity sentiment analysis is currently
only available for the English language. For more information, see [ Entity
Sentiment Analysis ](https://cloud.google.com/natural-
language/docs/basics#entity-sentiment-analysis) .

**FEATURE:**

The Natural Language API ` v1beta2 ` has added beta support for a new `
classifyText ` method that analyzes text content and returns a content
category for the content. For more information, see [ Content Classification
](https://cloud.google.com/natural-language/docs/basics#content-
classification) .

##  August 04, 2017

**FEATURE:**

The following languages are now fully supported for entity, sentiment, and
syntax analysis: * Chinese (Simplified and Traditional) * French * German *
Italian * Korean * Portuguese

**CHANGED:**

Sentiment analysis has been updated. You might see minor differences in score
and magnitude from the same request made to previous releases.

**CHANGED:**

Entity analysis has been updated. You might see minor differences in metadata
(Wikipedia URLs, knowledge graph MIDs) of entities identified in a block of
text from the same request made to the previous releases.

##  May 02, 2017

**FEATURE:**

Cloud Natural Language API ` v1beta2 ` release. Added beta support for entity,
sentiment, and syntax analysis for the following languages: * Chinese
(Simplified and Traditional) * French * German * Italian * Korean * Portuguese

**FEATURE:**

Added beta support for entity sentiment analysis ( ` analyzeEntitySentiment `
). Entity sentiment analysis is currently only available for the English
language. For more information, see [ Entity Sentiment Analysis
](https://cloud.google.com/natural-language/docs/basics#entity-sentiment-
analysis) .

**CHANGED:**

The ` v1beta2 ` release includes updated document sentiment analysis. You
might see differing results from the same request made to the Natural Language
API ` v1 ` and ` v1beta2 ` releases.

**CHANGED:**

The ` v1beta2 ` release includes updated entity analysis. You might see minor
differences in metadata (Wikipedia URLs, knowledge graph MIDs) from the same
request made to the Natural Language API ` v1 ` and ` v1beta2 ` releases.

**DEPRECATED:**

The Natural Language API ` v1beta1 ` release has been deprecated.

##  November 15, 2016

**FEATURE:**

Promoted the Cloud Natural Language API from Beta (v1beta1) to General
Availability (v1). Updates for v1 from the previous v1beta1 API endpoint
include the features listed below.

**FEATURE:**

The sentiment analysis feature has these enhancements: * Support for Japanese
( ` ja ` ) and Spanish ( ` es ` ) * Availability of [ sentence level sentiment
](https://cloud.google.com/natural-
language/docs/reference/rest/v1/documents/analyzeSentiment#response-body) *
Support for [ EncodingType ](https://cloud.google.com/natural-
language/docs/reference/rest/v1/EncodingType) within a Sentiment Analysis
request to calculate offsets for sentence-level sentiment *Addition of a `
score ` field within the [ ` Sentiment ` ](https://cloud.google.com/natural-
language/docs/reference/rest/v1/Sentiment) type to replace the previous `
polarity ` field

**FEATURE:**

The entity analysis feature has these enhancements: * Added Google Knowledge
Graph MID values, if available, to the [ ` metadata ` field for each ` Entity
` ](https://cloud.google.com/natural-language/docs/reference/rest/v1/Entity)
returned * Returns [ Entity Mention Types ](https://cloud.google.com/natural-
language/docs/reference/rest/v1/Entity#type_1) for both proper nouns and
common nouns (known as "nominals")

**FEATURE:**

Syntactic analysis has these enhancements: * Added a new [ ` analyzeSyntax `
](https://cloud.google.com/natural-
language/docs/reference/rest/v1/documents/analyzeSyntax) method * Added
morphology support to returned [ tokens ](https://cloud.google.com/natural-
language/docs/reference/rest/v1/Token)

**DEPRECATED:**

Removed the ` polarity ` field within the [ ` Sentiment `
](https://cloud.google.com/natural-language/docs/reference/rest/v1/Sentiment)
type in favor of the new ` score ` field.

