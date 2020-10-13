#  Release notes

This page documents production updates to Cloud Healthcare API. Check this
page for announcements about new or updated features, bug fixes, known issues,
and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/cloud-healthcare-release-
notes.xml `

##  June 08, 2020

v1

**FEATURE:**

It is now possible to de-identify data from within the Healthcare Browser in
the Cloud Console.

##  June 02, 2020

v1

**FEATURE:**

It is now possible to import DICOM data to and export DICOM data from BigQuery
using the Healthcare Browser in the Cloud Console. You can also import DICOM
data from Cloud Storage using the Healthcare Browser.

##  May 29, 2020

v1

**FEATURE:**

The Cloud Healthcare API offers single-region support in the ` asia-east2 `
(Hong Kong) region.

##  May 26, 2020

v1

**CHANGED:**

Search results for DICOM studies and series might take several seconds to
update after deleting an instance using [ ` instances.delete `
](https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances/delete)
.

##  April 23, 2020

v1

**FEATURE:**

Code samples are available for the Cloud Healthcare API v1 in Go, Java,
Node.js, and Python.

##  April 07, 2020

v1

**FEATURE:**

It is now possible to export resource changes to BigQuery each time a FHIR
resource is created, updated, patched, or deleted in a FHIR store, using the
new field for a store, [ ` streamConfigs `
](https://cloud.google.com/healthcare/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.stream_configs)
.

**FEATURE:**

You can now configure the HL7v2 store with multiple Pub/Sub topics and use
filters to send notifications to different Pub/Sub topics.

**FEATURE:**

**General availability release** Cloud Healthcare API is generally available
with release version v1.

For information on the differences between the v1beta1 release and the v1
release, see [ Transitioning to the v1 API
](https://cloud.google.com/healthcare/docs/how-tos/transition-guide) .

##  February 13, 2020

v1beta1

**CHANGED:**

The ` messages ` field returned by the [ `
projects.locations.datasets.hl7V2Stores.messages.list `
](https://cloud.google.com/healthcare/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores.messages/list)
method is deprecated. The method returns ` hl7_v2_messages ` , an array of [
messages
](https://cloud.google.com/healthcare/docs/reference/rest/v1beta1/projects.locations.datasets.hl7V2Stores.messages#Message)
. The new ` view ` input parameter specifies the fields to return. After the
deprecation period ends on March 2, 2020, the method will only return `
hl7_v2_messages ` .

##  February 10, 2020

v1beta1

**FEATURE:**

The Cloud Healthcare API supports all major release versions of the FHIR
standard. You can specify [ DSTU2 ](http://hl7.org/fhir/DSTU2) , [ STU3
](http://hl7.org/fhir/stu3) , or [ R4 ](http://hl7.org/fhir/r4) when you
create a FHIR store.

**FEATURE:**

Required permissions for the FHIR store have changed. You can now grant user
access as follows: * Access to APIs no longer includes ` read ` access to the
FHIR store configuration.  
* Access to the search API does not require ` get ` access. * Access to ` executeBundle ` does not give ` create ` , ` update ` , ` delete ` , or ` get ` permission. 

Logging has been added for ` executeBundle ` .

##  October 24, 2019

v1beta1

**FEATURE:**

DICOM and FHIR de-identification at the individual store level is now
available in beta. De-identification using filters is also now available in
beta. See the de-identification documentation for [ DICOM
](https://cloud.google.com/healthcare/docs/how-tos/dicom-
deidentify#dicom_store_level_de-identification) and [ FHIR
](https://cloud.google.com/healthcare/docs/how-tos/fhir-
deidentify#fhir_store_level_de-identification) data for more information.

##  September 24, 2019

v1beta1

**CHANGED:**

Public access to the Cloud Healthcare API v1alpha2 version has been
discontinued. Access to the v1alpha2 version is now restricted to Trusted
Testers. To become a Trusted Tester, complete [ this form
](https://services.google.com/fb/forms/cloudhealthcareapiearlyaccessprogram) .

##  September 16, 2019

v1beta1

**FEATURE:**

The Cloud Healthcare API offers single-region support in the ` asia-southeast1
` (Singapore) and ` us-west2 ` (Los Angeles) regions.

##  September 12, 2019

v1beta1

**FEATURE:**

Cloud Healthcare API ` gcloud ` tool commands are now available in ` gcloud
beta ` .

##  August 13, 2019

v1beta1

**FEATURE:**

DICOM de-identification supports an additional configuration option of not
automatically regenerating unique identifiers (UIDs), such as
StudyInstanceUID, SeriesInstanceUID, and SOPInstanceUID as part of the
operation. See the [ documentation
](https://cloud.google.com/healthcare/docs/reference/rest/v1beta1/projects.locations.datasets/deidentify#DicomConfig.FIELDS.skip_id_redaction)
for more information on when you might want to enable this option.

##  July 26, 2019

v1beta1

**FEATURE:**

The Cloud Healthcare API offers single-region support in the ` asia-northeast1
` (Tokyo) region.

##  July 15, 2019

v1beta1

**FEATURE:**

The Cloud Healthcare API offers single-region support in the ` europe-west4 `
(Netherlands) region.

##  July 10, 2019

v1beta1

**FEATURE:**

The Cloud Healthcare API offers multi-region support in the ` us ` (United
States) region.

##  June 19, 2019

v1beta1

**FEATURE:**

[ DICOM de-identification ](https://cloud.google.com/healthcare/docs/how-
tos/dicom-deidentify) has improved image output quality. There is now support
for lossless image output for lossless image input formats.

##  April 04, 2019

v1beta1

**FEATURE:**

The [ Google Cloud Console ](https://cloud.google.com/cloud-console/) provides
a user interface to the Cloud Healthcare API. The console allows you to:

  * [ Create and manage healthcare datasets ](https://cloud.google.com/healthcare/docs/how-tos/datasets)
  * Create and manage [ FHIR stores ](https://cloud.google.com/healthcare/docs/how-tos/fhir) , [ DICOM stores ](https://cloud.google.com/healthcare/docs/how-tos/dicom) , and [ HL7v2 stores ](https://cloud.google.com/healthcare/docs/how-tos/hl7v2)
  * [ Manage permissions ](https://cloud.google.com/healthcare/docs/how-tos/controlling-access)
  * View the status of long-running operations 

**FEATURE:**

An expanded set of configuration options are available for de-identification
operations on DICOM and FHIR data. These options provide greater control over
how resources (including pixel data) are processed. For details, see [ De-
identifying sensitive data ](https://cloud.google.com/healthcare/docs/how-
tos/deidentify) .

**FEATURE:**

DICOMweb has improved performance.

**FEATURE:**

DICOM has these conformance enhancements:

  * The API supports QIDO-RS result pagination, fuzzy patient-name matching, and transcoding additional DICOM transfer syntaxes, including lossless JPEG. 
  * To avoid managing multipart headers on the client side, the API supports single-part WADO-RS and STOW-RS requests. See the [ DICOM conformance statement ](https://cloud.google.com/healthcare/docs/dicom) for details. 

**FEATURE:**

User labels on DICOM, HL7v2, and FHIR stores make it possible to filter
resources and view billing charges based on label values.

**FEATURE:**

**Public beta release** The Cloud Healthcare API provides a managed solution
for storing and accessing healthcare data in Google Cloud Platform (GCP).

