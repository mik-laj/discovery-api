#  Release notes

This page documents production updates to Cloud Data Loss Prevention (DLP).
You can periodically check this page for announcements about new or updated
features, known issues, and deprecated functionality.

For a list of known issues for Cloud DLP, see [ Known issues
](/dlp/docs/known-issues) .

**Current version: v2**

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/dlp-release-notes.xml `

##  June 19, 2020

**FEATURE:**

Added support for location-based processing. Learn more:

  * [ Cloud DLP locations ](https://cloud.google.com/dlp/docs/locations)
  * [ Specifying processing locations ](https://cloud.google.com/dlp/docs/specifying-location)

##  June 15, 2020

**FEATURE:**

Added [ infoType detector ](https://cloud.google.com/dlp/docs/infotypes-
reference) :

  * VEHICLE_IDENTIFICATION_NUMBER 

##  May 21, 2020

**FEATURE:**

Added additional [ infoType detectors
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * IRELAND_DRIVING_LICENSE_NUMBER 
  * IRELAND_EIRCODE 

##  May 16, 2020

**FEATURE:**

Added [ infoType detectors ](https://cloud.google.com/dlp/docs/infotypes-
reference) :

AWS_CREDENTIALS

##  May 04, 2020

**CHANGED:**

We have made quality and performance enhancements to our name detectors.
PERSON_NAME should be used in most scenarios as it will return the most
comprehensive finding. MALE_NAME and FEMALE_NAME are now synonymous with
FIRST_NAME with [ ` Likelihood `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#likelihood)
now never being greater than ` POSSIBLE ` . These changes will be rolled out
over the coming days.

##  April 28, 2020

**FEATURE:**

Added additional [ infoType detector
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * JSON_WEB_TOKEN 

##  April 16, 2020

**FEATURE:**

Added support for ` PDF ` and ` WORD ` [ ` FileTypes `
](http://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#filetype)
and ` PDF ` and ` WORD_DOCUMENT ` [ ` BytesTypes `
](http://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#bytestype)
.

##  April 13, 2020

**FEATURE:**

Added additional [ infoType detectors
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * IRELAND_PPSN 
  * IRELAND_PASSPORT 

##  April 08, 2020

**FEATURE:**

Added additional infoType detectors:

  * ` AZURE_AUTH_TOKEN `
  * ` GCP_API_KEY `

##  March 16, 2020

**FEATURE:**

Added support for streaming data from external sources for inspection using
hybrid jobs and job triggers. Hybrid jobs and job triggers in Cloud DLP enable
you to stream data from virtually any source, whether on- or off-cloud,
inspect it using Cloud DLP, and then save the results of the inspection scan
as part of a job resource within Cloud DLP or to BigQuery.

##  March 01, 2020

**FEATURE:**

[ ` Regex ` ](https://cloud.google.com/dlp/docs/reference/rest/v2/Regex) , [ `
WordList `
](https://cloud.google.com/dlp/docs/reference/rest/v2/Dictionary#wordlist) ,
and small [ ` Dictionary `
](https://cloud.google.com/dlp/docs/reference/rest/v2/Dictionary) objects can
now be loaded from metadata stored in Cloud Spanner using [ `
CustomInfoType.Regex `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#regex) or
[ ` CustomInfoType.Dictionary `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#dictionary)
. Doing this can be useful when sharing regexes or dictionaries for custom
infoType inspection across multiple requests.

##  January 09, 2020

**FEATURE:**

Added additional infoType detectors:

  * ` GENERIC_ID `

##  December 10, 2019

**FEATURE:**

Added additional [ infoType detectors
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` AUSTRALIA_DRIVERS_LICENSE_NUMBER `
  * ` FRANCE_TAX_IDENTIFICATION_NUMBER `

##  November 08, 2019

**FEATURE:**

Added additional [ infoType detectors
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` AUTH_TOKEN `
  * ` BASIC_AUTH_HEADER `
  * ` ENCRYPTION_KEY `
  * ` HTTP_COOKIE `
  * ` PASSWORD `
  * ` WEAK_PASSWORD_HASH `
  * ` XSRF_TOKEN `

**FEATURE:**

The summary of a ` DlpJob ` findings can be published to Stackdriver using the
new action [ ` PublishToStackdriver `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#action)
. Metrics on bytes inspected and transformed are automatically published for
monitoring usage. For more information, see [ Monitoring with Stackdriver
](https://cloud.google.com/dlp/docs/monitoring) .

**CHANGED:**

The pricing model for content methods has changed from "units" to a simpler
model based just on bytes. For more information, see [ Pricing
](https://cloud.google.com/dlp/pricing) .

##  October 10, 2019

**FEATURE:**

Added additional [ infoType detectors
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` ADVERTISING_ID `
  * ` ORGANIZATION_NAME `
  * ` SPAIN_DNI_NUMBER `

##  September 13, 2019

**FEATURE:**

Added additional [ infoType detector
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` SCOTLAND_COMMUNITY_HEALTH_NUMBER `

##  August 26, 2019

**FEATURE:**

The [ Cloud DLP user interface (UI) ](https://cloud.google.com/dlp/docs/dlp-
ui) is now generally available (GA) in the [ Google Cloud Platform Console
](https://console.cloud.google.com/security/dlp;source=7) .

##  August 15, 2019

**FEATURE:**

Added additional [ infoType detector
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` MEDICAL_TERM `

##  August 05, 2019

**FEATURE:**

Added additional [ infoType detector
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` SPAIN_SOCIAL_SECURITY_NUMBER `

##  July 09, 2019

**FEATURE:**

Added additional [ infoType detectors
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` GERMANY_SCHUFA_ID `
  * ` CREDIT_CARD_TRACK_NUMBER `
  * ` ITALY_FISCAL_CODE `

##  June 28, 2019

**FEATURE:**

Added additional [ infoType detector
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` STREET_ADDRESS `

##  June 12, 2019

**CHANGED:**

New simplified SKU for scanning of data in storage. [ Updated Pricing
](https://cloud.google.com/dlp/pricing) .

**FEATURE:**

Support for structured scanning of Avro files, surfacing findings as rows and
columns rather than byte offsets. Existing jobs will begin scanning Avro files
as structured.

##  May 31, 2019

**FEATURE:**

Added support for [ ` CustomInfoTypes `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#custominfotype)
and [ ` DetectionRules `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#detectionrule)
to the [ Cloud DLP Beta UI
](https://console.cloud.google.com/security/dlp;source=7) in the Google Cloud
Platform Console.

##  April 18, 2019

**FEATURE:**

Added additional [ infoType detectors
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` GERMANY_DRIVERS_LICENSE_NUMBER `
  * ` GERMANY_IDENTITY_CARD_NUMBER `
  * ` HONG_KONG_ID_NUMBER `
  * ` INDIA_AADHAAR_INDIVIDUAL `
  * ` INDIA_GST_INDIVIDUAL `
  * ` THAILAND_NATIONAL_ID_NUMBER `

##  April 04, 2019

**FEATURE:**

Added additional [ infoType detectors
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` INDONESIA_NIK_NUMBER `
  * ` AUSTRALIA_PASSPORT `
  * ` BELGIUM_NATIONAL_ID_CARD_NUMBER `
  * ` GERMANY_TAXPAYER_IDENTIFICATION_NUMBER `
  * ` PASSPORT `
  * ` SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER `
  * ` SINGAPORE_PASSPORT `
  * ` TAIWAN_PASSPORT `
  * ` TURKEY_ID_NUMBER `

##  March 29, 2019

**FEATURE:**

Added new crypto-based tokenization method: [ ` CryptoDeterministicConfig `
](https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#cryptodeterministicconfig)
. For more information, see [ Transformations Reference
](https://cloud.google.com/dlp/docs/transformations-reference) .

##  March 08, 2019

**FEATURE:**

Added new [ Cloud DLP Beta UI
](https://console.cloud.google.com/security/dlp;source=7) in the Google Cloud
Platform Console.

##  February 11, 2019

**FIXED:**

Clarified the documentation as to what behavior users can expect for the [ `
ALL_BASIC ` ](https://cloud.google.com/dlp/docs/infotypes-reference) .

**CHANGED:**

Updated the default list of infotypes included in [ ` ALL_BASIC `
](https://cloud.google.com/dlp/docs/infotypes-reference) .

##  December 12, 2018

**FIXED:**

De-identification requests using [ ` CryptoReplaceFfxFpeConfig `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#cryptoreplaceffxfpeconfig)
now correctly validate the alphabet of the value being transformed to match
the transformations alphabet, now correctly rejecting values with whitespace,
when whitespace is not part of the alphabet. Invalid requests will return an
error in the ` TransformationSummary ` with the message
"CryptoReplaceFfxFpeConfig's 'alphabet' does not include all the characters in
the value being transformed; the set of distinct characters in any given value
being transformed by this transformation must be a subset of the set of
characters comprising the 'alphabet'."

##  October 25, 2018

**FEATURE:**

Added an additional [ infoType detector
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` NORWAY_NI_NUMBER `

##  October 02, 2018

**FEATURE:**

Added support to Cloud Storage [ ` FileSet `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig#fileset)
for using regular expression filters to specify which files to include or
exclude from the scan. This is useful for cases where the set of files to scan
cannot be concisely expressed with a path and wildcards, such as:

  * Scan all files, but skip some specific files or folders that you are confident have no sensitive data. 
  * Scan only files whose endings are in some known set of file extensions - for example, only .txt, .csv, and .json files. 
  * Scan only files whose endings aren't in some known set of extensions - for example, skip .pdf files. 

##  September 19, 2018

**FEATURE:**

Added support for [ augmenting existing infoType detectors
](https://cloud.google.com/dlp/docs/creating-custom-infotypes-rules) using
exclusion rules and hotword rules.

##  August 24, 2018

**FEATURE:**

Added an additional [ infoType detector
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` DENMARK_CPR_NUMBER `

##  August 17, 2018

**FEATURE:**

Added additional [ infoType detectors
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * ` CANADA_DRIVERS_LICENSE_NUMBER `
  * ` DATE `
  * ` DATE_OF_BIRTH `
  * ` FEMALE_NAME `
  * ` FINLAND_NATIONAL_ID_NUMBER `
  * ` GCP_CREDENTIALS `
  * ` GENDER `
  * ` JAPAN_BANK_ACCOUNT `
  * ` JAPAN_DRIVERS_LICENSE_NUMBER `
  * ` MALE_NAME `
  * ` NETHERLANDS_PASSPORT `
  * ` SPAIN_DRIVERS_LICENSE_NUMBER `
  * ` SWEDEN_NATIONAL_ID_NUMBER `
  * ` SWEDEN_PASSPORT `
  * ` TIME `
  * ` US_STATE `

##  August 10, 2018

**FEATURE:**

Added support for [ large custom dictionaries
](https://cloud.google.com/dlp/docs/creating-stored-infotypes) . Cloud DLP can
now scan for dictionaries containing up to tens of millions of entries.

**FEATURE:**

Added support to [ ` CloudStorageOptions `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig#cloudstorageoptions)
for limiting the number of bytes to scan per file by percentage.

**FEATURE:**

Added support to [ ` BigQueryOptions `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig#bigqueryoptions)
for limiting the number of rows to scan per file by percentage.

##  June 01, 2018

**FEATURE:**

Added support for [ delta-presence estimation
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#privacymetric)
, a risk metric used when membership in the dataset is itself a piece of
sensitive information.

##  May 18, 2018

**FEATURE:**

Added ` sample_method ` flag to [ ` BigQueryOptions `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#bigqueryoptions)
and [ ` CloudStorageOptions `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#cloudstorageoptions)
for limiting scans to a sample of content. This is useful to more efficiently
scan large datasets where the intent is to only determine whether sensitive
data may be located there and the exhaustive list of findings is not
necessary.

##  April 25, 2018

**FEATURE:**

Added ` row_limit ` flag to [ ` BigQueryOptions `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#bigqueryoptions)
to allow for sampling tables instead of scanning all rows.

**FEATURE:**

Dictionaries can now be loaded from files stored in Cloud Storage that consist
of newline-delimited lists of phrases using the ` cloud_storage_path `
parameter in [ ` CustomInfoType.Dictionary `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.CustomInfoType.Dictionary)
. Useful when sharing dictionaries for custom inspection across multiple
requests.

**FEATURE:**

For customers using Cloud Security Command Center, the summary of a ` DlpJob `
can be published to Cloud SCC using the new action [ ` PublishSummaryToCscc `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#action)
.

##  March 21, 2018

**FEATURE:**

**Cloud Data Loss Prevention (DLP) General Availability (GA) Release**

**FEATURE:**

Launched the new [ V2 ](https://cloud.google.com/dlp/docs/reference/rest/v2/)
version of the API.

**CHANGED:**

The [ ` jobs.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs/create)
method has been added to replace ` dataSource.analyze ` and `
dataSource.inspect ` .

**CHANGED:**

The [ ` ContentItem `
](https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem) object has
been simplified with a [ ` BytesType `
](https://cloud.google.com/dlp/docs/reference/rest/v2/ByteContentItem#BytesType)
enum to specify the type of data to inspect.

**CHANGED:**

The [ ` Finding `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#google.privacy.dlp.v2.Finding)
object has been expanded with a new [ ` ContentLocation `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#contentlocation)
to better report findings from various data types (including images, records,
and documents).

**CHANGED:**

` InfoTypeStatistics ` object has been renamed to [ ` InfoTypeStats `
](https://cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs#infotypestats)
.

**DEPRECATED:**

The v2beta1 and v2beta2 APIs are now deprecated.

##  February 16, 2018

**FEATURE:**

Newly added [ ` JobTriggers `
](https://cloud.google.com/dlp/docs/reference/rest/v2/projects.jobTriggers#resource-
jobtrigger) allow for scheduling regular scans of storage. Combined with the
new [ ` TimespanConfig `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig#TimespanConfig)
, scans can be limited to only re-scanning new or modified content in BigQuery
and Cloud Storage.

**FEATURE:**

Added support for [ regular expression
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InspectConfig#regex)
-based custom detectors.

**FEATURE:**

Added support for choosing a default [ likelihood
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#likelihood)
for [ ` CustomInfoType `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#custominfotype)
detectors and for adjusting likelihood using a new [ ` DetectionRule `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#detectionrule)
, which looks for related content within the vicinity of a finding.

**FEATURE:**

Job completion notifications for both risk analysis and inspection can now be
sent to [ Cloud Pub/Sub
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InspectJobConfig#Action)
.

##  December 14, 2017

**FEATURE:**

Launched the new v2beta2 version of the API, which includes a number of new
and improved features, including templates for persisting de-identification
and inspect configurations, a simplified job API for inspecting storage and
risk analysis, and more.

Tips for migrating:

  * [ ` Content ` ](https://cloud.google.com/dlp/docs/reference/rest/v2/projects.content) API methods now take a single ` ContentItem ` . 
  * [ ` InspectConfig ` ](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig) now has a default likelihood, so when left unset findings below ` POSSIBLE ` will be excluded automatically. 
  * Findings from inspect storage are now always stored in your own BigQuery instance, giving you more control of where your sensitive data is stored. 
  * ` content.redact ` , was deprecated in favor of using [ ` content.deidentify ` ](https://cloud.google.com/dlp/docs/reference/rest/v2/projects.content/deidentify) , for redacting text, and [ ` image.redact ` ](https://cloud.google.com/dlp/docs/reference/rest/v2/projects.image/redact) , for redacting images. 
  * [ ` InspectConfig ` ](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig) now requires at least one [ ` InfoType ` ](https://cloud.google.com/dlp/docs/reference/rest/v2/InfoType) or [ ` CustomInfoType ` ](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectConfig#custominfotype) . 
  * Long running operations were replaced by [ ` DlpJob ` ](https://cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs#resource-dlpjob) objects for risk analysis and storage inspection. ` inspect.operations.create ` was renamed to ` dataSource.inspect ` . 

##  November 22, 2017

**FEATURE:**

Added a new risk analysis metric, _k_ -map estimation, to [ `
dataSource.analyze `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/dataSource/analyze)
.

##  October 20, 2017

**FEATURE:**

Launched support for searching for words or phrases from a custom dictionary
provided by the user with the addition of ` CustomInfoType ` to [ `
InspectConfig `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/InspectConfig) .
This feature is enabled in [ ` content.inspect `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/inspect) ,
[ ` content.redact `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/redact) , [
` content.deidentify `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/deidentify)
, and [ ` inspect.operations.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.operations/create)
.

##  September 15, 2017

**FEATURE:**

Launched support to de-identify content with the addition of [ `
content.deidentify `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/deidentify)
.

**FEATURE:**

Launched support to conduct risk analysis on BigQuery with the addition of [ `
dataSource.analyze `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/dataSource/analyze)
.

##  August 17, 2017

**FEATURE:**

Added support to limit the number of findings per ` InfoType ` with the
addition of ` InfoTypeLimit ` in [ ` InspectConfig `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/InspectConfig) .

**FEATURE:**

Added support to limit the number of findings per file, Cloud Datastore
entity, or database row with the addition of ` OperationConfig ` to [ `
inspect.operations.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.operations/create)
.

##  August 10, 2017

**FEATURE:**

Added support for scanning and redacting structured data in both [ `
content.redact `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/redact) and
[ ` content.inspect `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/inspect) by
providing a ` Table ` in [ ` ContentItem `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/ContentItem) .

##  August 03, 2017

**FEATURE:**

BigQuery can now be scanned using [ ` inspect.operations.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.operations/create)
.

**FEATURE:**

Results can now be stored to BigQuery when scanning BigQuery, Cloud Datastore,
and Cloud Storage using [ ` inspect.operations.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.operations/create)
.

##  June 15, 2017

**FEATURE:**

Added support for auto-redacting all text from images. You can now also choose
custom colors when using [ ` content.redact `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/redact) to
fill the bounding boxes during image redaction.

##  May 11, 2017

**FEATURE:**

Launched support to filter [ findings
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/InspectResult#finding)
by infoType and likelihood when using [ ` inspect.results.list `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.results.findings/list)
.

##  May 01, 2017

**FEATURE:**

You can now store results from scanning Cloud Datastore or Cloud Storage using
[ ` inspect.operations.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.operations/create)
. Results are stored in Cloud Storage.

##  March 23, 2017

**FEATURE:**

Added support for auto-redacting findings in images. You can now use [ `
content.redact `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/redact) to
fill the [ bounding box
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/InspectResult#ImageLocation)
of a finding with a solid color.

##  March 09, 2017

**FEATURE:**

Launch of Cloud DLP API to **Beta** . Cloud DLP API enables developers and
data owners to better understand and manage sensitive data by providing a
fast, scalable classification for sensitive elements. Scan small text streams
and images or larger datasets in Cloud Storage and Cloud Datastore. The Cloud
DLP API is currently available as a REST API.

