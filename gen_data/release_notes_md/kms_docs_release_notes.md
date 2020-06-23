#  Release notes

This page documents production updates to Cloud Key Management Service. You
can periodically check this page for announcements about new or updated
features, bug fixes, known issues, and deprecated functionality.

**Current version: v1**

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/kms-release-notes.xml `

##  June 22, 2020

**FEATURE:**

Keys hosted by [ Thales
](https://thalesdocs.com/dpod/services/key_management_services/ekms/ekms_setup_guide/)
are now supported in Cloud EKM. To learn more, see [ Cloud EKM
](https://cloud.google.com/kms/docs/ekm) .

##  June 08, 2020

**FEATURE:**

Cloud KMS and Cloud EKM resources are available in the ` asia-southeast2 `
region. Cloud HSM resources are **not** available in this region.

For information about which [ Cloud Locations
](https://cloud.google.com/about/locations/) are supported by Cloud KMS, Cloud
HSM, and Cloud EKM, see the [ Cloud KMS regional locations
](https://cloud.google.com/kms/docs/locations#regional) .

##  May 28, 2020

**FEATURE:**

Several fields related to data integrity have been added to the Cloud KMS API,
along with guidelines for using them. To learn more about maintaining data
integrity when performing cryptographic operations, see [ Verifying end-to-end
data integrity ](https://cloud.google.com/kms/docs/data-integrity-guidelines)
.

##  April 20, 2020

**FEATURE:**

Cloud KMS and Cloud EKM resources are available in the ` us-west4 ` region.
Cloud HSM resources are **not** available in this region.

Cloud HSM resources are available in the ` global ` multi-regional location.

For information about which [ Cloud Locations
](https://cloud.google.com/about/locations/) are supported by Cloud KMS, Cloud
HSM, and Cloud EKM, see the [ Cloud KMS regional locations
](https://cloud.google.com/kms/docs/locations#regional) .

##  April 15, 2020

**FEATURE:**

[ Cloud External Key Manager (Cloud EKM)
](https://cloud.google.com/kms/docs/ekm) is generally available.

##  March 18, 2020

**FEATURE:**

[ Importing keys ](https://cloud.google.com/kms/docs/importing-a-key) into
Cloud KMS software keys is generally available (GA).

##  March 05, 2020

**FEATURE:**

Cloud EKM resources are now available in the ` asia-northeast3 ` and ` us-
west3 ` [ locations ](https://cloud.google.com/kms/docs/locations) .

##  February 25, 2020

**FEATURE:**

Cloud KMS resources can now be created in the ` us-west3 ` region.

Cloud HSM resources are now also available in the ` us-west3 ` region.

Cloud EKM resources are not available in the ` us-west3 ` region.

For information about which [ Cloud Locations
](https://cloud.google.com/about/locations/) are supported by Cloud KMS, Cloud
HSM, and Cloud EKM, refer to [ Cloud KMS locations
](https://cloud.google.com/kms/docs/locations#regional) .

##  February 20, 2020

**FEATURE:**

You can now import key material into Cloud KMS software keys. For more
information, see [ Key import ](https://cloud.google.com/kms/docs/key-import)
. Importing key material into Cloud HSM keys is already generally available.

##  January 24, 2020

**FEATURE:**

Cloud KMS resources can now be created in the ` asia-northeast3 ` region.

Cloud HSM resources are now also available in the ` asia-northeast3 ` region.

**Note:** Cloud EKM resources are _not available_ in the ` asia-northeast3 `
region.

Learn more about [ Cloud Locations
](https://cloud.google.com/about/locations/) . For the list of all regions
supported by Cloud KMS, Cloud HSM, and Cloud EKM, see the [ Cloud KMS regional
locations ](https://cloud.google.com/kms/docs/locations#regional) .

##  December 17, 2019

**FEATURE:**

[ Cloud External Key Manager (Cloud EKM) (Beta)
](https://cloud.google.com/kms/docs/ekm) allows you to encrypt data stored in
Google Cloud using keys stored in a supported partner external key management
system. You can encrypt or decrypt data in BigQuery, Compute Engine persistent
disks, or directly using the Cloud KMS API.

You can learn about [ changes to the API
](https://cloud.google.com/kms/docs/ekm#api_changes) since the Alpha release.

##  August 22, 2019

**BREAKING:**

The Cryptographic Requests quota has been increased from 600 QPM to 60,000
QPM. If you use quotas to determine how much you are billed, this change could
increase the amount you end up spending on your Cloud KMS.

If you require a smaller quota than 60,000 QPM, or you don't need a quota
increase, go to the [ Cloud Console Quotas page
](https://console.cloud.google.com/iam-
admin/quotas?service=cloudkms.googleapis.com) and set a new value for
Cryptographic requests per minute. HSM specific quotas will not be increased.

##  July 02, 2019

**FEATURE:**

The [ ` gcloud beta kms import-jobs `
](https://cloud.google.com/sdk/gcloud/reference/beta/kms/import-jobs/) command
group was released as part of [ ` gcloud 253.0.0 `
](https://cloud.google.com/sdk/docs/release-notes#25300_2019-07-02) .

##  July 01, 2019

**FEATURE:**

Introduction of import key functionality into the Cloud KMS beta release.

**Note:** You can import only into keys with [ protection level
](https://cloud.google.com/kms/docs/algorithms#protection_levels) **HSM** .

The following are additions to the API definition.

###  New resources

[ ` ImportJob `
](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs)
has been added as a resource.

The ` ImportJob ` resource contains the following methods:

  * [ ` ImportJobs.create ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/create)
  * [ ` ImportJobs.get ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/get)
  * [ ` ImportJobs.getIamPolicy ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/getIamPolicy)
  * [ ` ImportJobs.list ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/list)
  * [ ` ImportJobs.setIamPolicy ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/setIamPolicy)
  * [ ` ImportJobs.testIamPermissions ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/testIamPermissions)

The ` ImportJob ` resource contains the following enums:

  * [ ` ImportJobState ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#importjobstate)
  * [ ` ImportMethod ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#importmethod)

The ` ImportJob ` resource contains the following type:

  * [ ` WrappingPublicKey ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#wrappingpublickey)

###  New methods

  * [ ` CryptoKeyVersions.import ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/import)

###  New fields

  * [ ` CreateCryptoKeyRequest.skip_initial_version_creation ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create#body.QUERY_PARAMETERS.skip_initial_version_creation)
  * [ ` CryptoKeyVersions.import_failure_reason ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.import_failure_reason)
  * [ ` CryptoKeyVersions.import_job ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.import_job)
  * [ ` CryptoKeyVersions.import_time ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.import_time)

###  New enums

  * [ ` CryptoKeyVersionState.PENDING_IMPORT ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState.ENUM_VALUES.PENDING_IMPORT)
  * [ ` CryptoKeyVersionState.IMPORT_FAILED ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState.ENUM_VALUES.IMPORT_FAILED)

###  New permissions

  * ` cloudkms.cryptoKeyVersions.useToImport `
  * ` cloudkms.importJobs.create `
  * ` cloudkms.importJobs.get `
  * ` cloudkms.importJobs.getIamPolicy `
  * ` cloudkms.importJobs.list `
  * ` cloudkms.importJobs.setIamPolicy `

For more information about Cloud KMS permissions, see [ Permissions and roles
](https://cloud.google.com/kms/docs/reference/permissions-and-roles) .

##  June 28, 2019

**FEATURE:**

Cloud HSM resources are now available in the following regional locations:

  * ` asia-east2 `
  * ` europe-west6 `
  * ` us-west2 `

For the list of all supported regions, see [ Supported regions
](https://cloud.google.com/kms/docs/locations) .

##  June 27, 2019

**FEATURE:**

Introduction of the Cloud KMS beta release to support filtering and sorting
results from the following ` list ` operations.

  * [ keyRings.list ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/list)
  * [ cryptoKeys.list ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list)
  * [ cryptoKeyVersions.list ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/list)

For more information, see [ Sorting and filtering list results
](https://cloud.google.com/kms/docs/sorting-and-filtering) .

##  June 20, 2019

**FEATURE:**

Cloud HSM resources are now available in the following regional locations:

  * ` asia-northeast1 `
  * ` asia-northeast2 `

For the list of all supported regions, see [ Supported regions
](https://cloud.google.com/kms/docs/locations) .

##  June 11, 2019

**CHANGED:**

The ` gcloud kms ` command group was updated as part of [ gcloud 250.0.0
](https://cloud.google.com/sdk/docs/release-notes#25000_2019-06-11) .

  * Promoted the following commands to GA. 
    * ` gcloud kms asymmetric-decrypt ` . 
    * ` gcloud kms asymmetric-sign ` . 
    * ` gcloud kms keys versions get-public-key ` . 
  * Promoted the following flags in ` gcloud kms keys ` command group to GA. 
    * ` --attestation-file ` . 
    * ` --default-algorithm ` . 
    * ` --purpose ` . 
    * ` --protection-level ` . 

##  June 04, 2019

**FEATURE:**

Cloud HSM resources are now available in the following regional locations:

  * ` asia-south1 `
  * ` europe-north1 `
  * ` europe-west1 `
  * ` europe-west4 `

For the list of all supported regions, see [ Supported regions for Cloud HSM
](https://cloud.google.com/kms/docs/locations) .

##  May 13, 2019

**FEATURE:**

Cloud HSM resources are now available in the ` us ` multi-regional location.
For the list of all supported regions, see [ Supported regions for Cloud HSM
](https://cloud.google.com/kms/docs/locations) .

##  April 18, 2019

**FEATURE:**

Cloud KMS resources can now be created in the ` asia-northeast2 ` region.
Learn more about [ Cloud Locations
](https://cloud.google.com/about/locations/) .

##  April 02, 2019

**FEATURE:**

Cloud HSM resources are now available in the ` asia-southeast ` 1 regional
location. For the list of all supported regions, see [ Supported regions for
Cloud HSM ](https://cloud.google.com/kms/docs/locations) .

##  March 11, 2019

**FEATURE:**

Cloud KMS resources can now be created in the ` europe-west6 ` region. Learn
more about [ Cloud Locations ](https://cloud.google.com/about/locations/) .

##  February 26, 2019

**FEATURE:**

` CAVIUM_V2_COMPRESSED ` has been added as an enum value to [ `
AttestationFormat `
](https://cloud.google.com/kms/docs/reference/rest/v1/KeyOperationAttestation#AttestationFormat)
. To learn how to verify an attestation that is in the ` CAVIUM_V2_COMPRESSED
` format, see [ Verifying Attestations
](https://cloud.google.com/kms/docs/attest-key) .

##  December 14, 2018

**FEATURE:**

Announced general availability of [ asymmetric keys
](https://cloud.google.com/kms/docs/asymmetric-encryption) and [ Cloud HSM
](https://cloud.google.com/kms/docs/hsm) in Cloud KMS.

##  December 13, 2018

**FEATURE:**

Cloud HSM resources are now available in the ` europe-west3 ` regional
location. For the list of all supported regions, see [ Supported regions for
Cloud HSM ](https://cloud.google.com/kms/docs/locations) .

##  December 06, 2018

**FEATURE:**

Cloud HSM resources are now available in the ` europe-west2 ` regional
location. For the list of all supported regions, see [ Supported regions for
Cloud HSM ](https://cloud.google.com/kms/docs/locations) .

##  November 12, 2018

**FEATURE:**

Cloud KMS resources can now be created in the ` eur4 ` and ` nam4 ` dual-
regions. Learn more about [ Cloud Locations
](https://cloud.google.com/about/locations/) .

##  October 26, 2018

**FEATURE:**

Cloud KMS resources can now be created in the ` asia-east2 ` region. Learn
more about [ Cloud Locations ](https://cloud.google.com/about/locations/) .

##  October 11, 2018

**FEATURE:**

New algorithms have been added:

  * RSA_SIGN_PSS_4096_SHA512 
  * RSA_SIGN_PKCS1_4096_SHA512 
  * RSA_DECRYPT_OAEP_4096_SHA512 

For the list of all supported algorithms, see [ Key purposes and algorithms
](https://cloud.google.com/kms/docs/algorithms) .

##  September 27, 2018

**FEATURE:**

Cloud HSM resources are now available in the ` us-central1 ` regional
location. For the list of all supported regions, see [ Supported regions for
Cloud HSM ](https://cloud.google.com/kms/docs/locations) .

##  September 05, 2018

**FEATURE:**

Attestations that are downloaded via the Google Cloud Platform Console are no
longer base64-encoded. This matches the raw format of the attestations
downloaded via the ` gcloud ` command-line tool and the Cloud KMS API. The
instructions for [ Verifying Attestations
](https://cloud.google.com/kms/docs/attest-key) expect the attestation to be
in raw format, not base64-encoded.

##  August 20, 2018

**FEATURE:**

Introduction of asymmetric keys and Cloud HSM into the Cloud KMS beta release.

Additions to the API definition:

  * New method for creating digital signatures: 
    * [ CryptoKeys.asymmetricSign ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricSign)
  * New method for retrieving an asymmetric key's public key: 
    * [ CryptoKeyVersions.getPublicKey ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey)
  * New method for decrypting data encoded with an asymmetric public key generated by Cloud KMS: 
    * [ CryptoKeyVersions.asymmetricDecrypt ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricDecrypt)
  * New types: 
    * [ CryptoKeyVersionAlgorithm ](https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm)
    * [ CryptoKeyVersionTemplate ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyVersionTemplate)
    * [ CryptoKeyVersionView ](https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionView)
    * [ ProtectionLevel ](https://cloud.google.com/kms/docs/reference/rest/v1/ProtectionLevel)
  * New fields: 
    * [ CryptoKey.versionTemplate ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.version_template)
    * [ CryptoKeyVersion.algorithm ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.algorithm)
    * [ CryptoKeyVersion.attestation ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.attestation)
    * [ CryptoKeyVersion.generateTime ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.generate_time)
    * [ CryptoKeyVersion.protectionLevel ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.protection_level)
    * [ LocationMetadata.hsmAvailable ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations#LocationMetadata.FIELDS.hsm_available)
  * The [ CryptoKey.list ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list) method now contains a [ versionView ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list#body.QUERY_PARAMETERS.version_view) query parameter that lists the fields of the primary key version to include in the response. 
  * The [ CryptoKeyVersion.list ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/list) method now contains a [ view ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/list#body.QUERY_PARAMETERS.view) query parameter that lists the fields to include in the response. 
  * The [ LocationMetadata ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations#LocationMetadata) resource returned by the [ Locations.get ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations/get) and [ Locations.list ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations/list) methods now contain an ` hsm_available ` field. The ` hsm_available ` field is a ` bool ` that indicates whether the location supports Hardware Security Modules (HSMs). 

**FEATURE:**

Cloud HSM resources are now available in the ` us-east1 ` and ` us-west1 `
regional locations.

##  July 14, 2018

**FEATURE:**

Cloud KMS resources can now be created in the ` us-west2 ` region. Learn more
about [ Cloud Locations ](https://cloud.google.com/about/locations/) .

##  June 14, 2018

**FEATURE:**

Cloud KMS resources can now be created in the ` europe-north1 ` region. Learn
more about [ Cloud Locations ](https://cloud.google.com/about/locations/) .

##  April 12, 2018

**FEATURE:**

Cloud KMS resources can now be created in the following regions:

  * ` asia-south1 `
  * ` australia-southeast1 `
  * ` europe-west2 `
  * ` europe-west3 `
  * ` northamerica-northeast1 `
  * ` southamerica-east1 `
  * ` us-east4 `

Learn more about [ Cloud Locations
](https://cloud.google.com/about/locations/) .

##  April 11, 2018

**CHANGED:**

The URL of the Cloud KMS page in the Google Cloud Platform Console has been
changed from https://console.cloud.google.com/iam-admin/kms to
https://console.cloud.google.com/security/kms.

##  April 03, 2018

**FEATURE:**

The name of the [ Cloud KMS ](https://console.cloud.google.com/iam-
admin/kms?_ga=2.253907791.-615102279.1537806205) page in the Google Cloud
Platform Console has been changed from **Encryption keys** to **Cryptographic
keys** .

##  March 29, 2018

**FEATURE:**

Cloud KMS resources can now be created in the ` asia-northeast1 ` region.
Learn more about [ Cloud Locations
](https://cloud.google.com/about/locations/) .

##  February 08, 2018

**FEATURE:**

Cloud KMS resources can now be created in the ` asia ` , ` europe ` , and ` us
` multi-regional locations. Learn more about [ Cloud KMS locations
](https://cloud.google.com/kms/docs/locations/) .

##  January 31, 2018

**FEATURE:**

Announced general availability of [ IAM custom roles
](https://cloud.google.com/kms/docs/reference/permissions-and-
roles#custom_roles) for Cloud KMS.

##  January 22, 2018

**FEATURE:**

The ` gcloud kms locations list ` command now supports the ` europe-west4 `
region.

##  January 17, 2018

**FEATURE:**

The Google Cloud Platform console now supports the ` europe-west4 ` region.
You can create new key rings in this region using the console, the API and the
` gcloud ` command-line tool. The ` gcloud kms locations list ` command will
support this region approximately January 22, 2018. Learn more about [ Cloud
Locations ](https://cloud.google.com/about/locations/) .

##  January 10, 2018

**FEATURE:**

Cloud KMS resources can now be created in the ` europe-west4 ` region. You can
use this region to create new key rings using the API and the ` gcloud `
command-line tool. This region will not be viewable in the Google Cloud
Platform console or returned by ` gcloud kms locations list ` until
approximately January 17, 2018. Learn more about [ Cloud Locations
](https://cloud.google.com/about/locations/) .

##  October 11, 2017

**CHANGED:**

Promoted ` keys update ` from ` gcloud beta kms ` to ` gcloud kms ` as part of
[ gcloud 175.0.0 ](https://cloud.google.com/sdk/docs/release-
notes#17500_2017-10-11) .

##  October 04, 2017

**CHANGED:**

The [ Envelope Encryption ](https://cloud.google.com/kms/docs/envelope-
encryption) topic provides more information about key wrapping and envelope
encryption.

##  September 19, 2017

**CHANGED:**

Batch operations are no longer supported.

##  September 06, 2017

**FEATURE:**

Labels can now be applied to CryptoKeys:

  * The [ ` CryptoKey ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey) type now contains the [ ` labels ` ](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.labels) field. 
  * To learn more about this feature, see [ Labeling CryptoKeys ](https://cloud.google.com/kms/docs/labeling-keys) . 

**FEATURE:**

` gcloud ` changes:

  * The ` gcloud kms keys create ` command has a new parameter, ` --labels ` . Use this parameter to specify labels when you create a key. 
  * The output from the ` gcloud kms keys list ` command now contains a ` LABELS ` column. 
  * The [ ` gcloud beta kms keys update ` ](https://cloud.google.com/sdk/gcloud/reference/beta/kms/keys/update) command is new. This command supports updating an existing key. 

These changes are effective in [ ` gcloud ` version 170.0.0
](https://cloud.google.com/sdk/docs/release-notes#17000_2017-09-06) .

##  August 23, 2017

**FEATURE:**

Cloud KMS resources can now be created in the ` asia-southeast1 ` region.
Learn more about [ Cloud Locations
](https://cloud.google.com/about/locations/) .

##  August 18, 2017

**CHANGED:**

Cloud KMS is now available in a larger group of countries.

##  June 14, 2017

**CHANGED:**

Promoted ` encrypt ` and ` decrypt ` commands from ` gcloud beta kms ` to `
gcloud kms ` as part of [ gcloud 159.0.0
](https://cloud.google.com/sdk/docs/release-notes#15900_2017-06-14) .

##  June 07, 2017

**DEPRECATED:**

API version v1beta1 has been turned off. Please use v1 API endpoint.

**CHANGED:**

As part of [ gcloud 158.0.0 ](https://cloud.google.com/sdk/docs/release-
notes#15800_2017-06-07) , when using ` gcloud ` to update IAM policies, data
access logs can be enabled for key rings and keys, in addition to projects
which were already supported.

  * [ ` gcloud kms keyrings set-iam-policy ` ](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/set-iam-policy)
  * [ ` gcloud kms keys set-iam-policy ` ](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-iam-policy)

##  May 31, 2017

**FEATURE:**

Added ` encrypt ` and ` decrypt ` commands to ` gcloud beta kms ` as part of [
gcloud 157.0.0 ](https://cloud.google.com/sdk/docs/release-
notes#15700_2017-05-31) .

  * [ Added examples ](https://cloud.google.com/kms/docs/encrypt-decrypt) for using ` gcloud beta kms encrypt ` and ` gcloud beta kms decrypt ` . 

##  May 02, 2017

**FEATURE:**

Data Access audit logs can now be self-enabled for Cloud KMS. For more
information, see [ Cloud Audit Logging documentation
](https://cloud.google.com/logging/docs/audit/configure-data-access) .

  * [ Updated documentation ](https://cloud.google.com/kms/docs/logging) on logs types in Cloud KMS. 

##  April 17, 2017

**FEATURE:**

Cloud KMS resources can now be created in the ` us-west1 ` region. Learn more
about [ Cloud Locations ](https://cloud.google.com/about/locations/) .

##  March 22, 2017

**CHANGED:**

Promoted ` gcloud beta kms ` commands to ` gcloud kms ` as part of [ gcloud
148.0.0 ](https://cloud.google.com/sdk/docs/release-notes#14800_2017-03-22) .

##  March 15, 2017

**CHANGED:**

Renamed ` cryptokey ` to ` key ` as part of [ gcloud 147.0.0
](https://cloud.google.com/sdk/docs/release-notes#14700_2017-03-15) .

Renamed ` gcloud kms cryptokeys ` as ` gcloud kms keys ` . Renamed the `
--cryptokey ` flag as ` --key ` . Deprecated the ` cryptokey ` variants.

##  March 08, 2017

**FEATURE:**

Launch of Cloud KMS to **General Availability** .

  * Updated client libraries and code samples in C#, Go, Java, Node.js, PHP, Python, and Ruby. 
  * [ New Secret Management documentation ](https://cloud.google.com/kms/docs/secret-management) that explains how to protect secrets using Cloud KMS. 
  * Added a [ Service Level Agreement (SLA) ](https://cloud.google.com/kms/sla) . 

**CHANGED:**

API version from v1beta1 to v1.

  * The v1beta1 API is deprecated and will be turned down no sooner than June 7, 2017. 
  * To start using the v1 API, follow the process to [ install the client library ](https://cloud.google.com/kms/docs/reference/libraries#installing_the_client_library) for your preferred language. Other than the API version, your code shouldn't need any other changes. 

##  January 11, 2017

**FEATURE:**

Launch of Cloud KMS to **Beta** . Use Cloud KMS to create, use, rotate,
automatically rotate, and destroy symmetric AES256 encryption keys. Cloud KMS
is [ accessible via ](https://cloud.google.com/kms/docs/accessing-the-api)

  * REST API 
  * Google APIs Client Libraries in go, python, and java 
  * Cloud Console user interface 

