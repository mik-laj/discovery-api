#  Release notes: Cloud Dataflow SDK for Python

**NOTE:** The [ Apache Beam downloads ](https://beam.apache.org/get-
started/downloads/#releases) page contains release notes for the Apache Beam
SDK releases.

**SDK Decommission Notice:** The following SDK versions will be decommissioned
by August 12, 2020 due to the [ discontinuation of support for JSON-RPC and
Global HTTP Batch Endpoints
](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-
rpc-and.html) .

  * Apache Beam SDK for Java, versions 2.0.0 to 2.4.0 (inclusive) 
  * Apache Beam SDK for Python, versions 2.0.0 to 2.4.0 (inclusive) 
  * Dataflow SDK for Java, versions 2.0.0 to 2.4.0 (inclusive) 
  * Dataflow SDK for Python, 2.0.0 to 2.4.0 (inclusive) 

When decommissioning happens, you will no longer be able to submit new
Dataflow jobs or update running Dataflow jobs that use the decommissioned
SDKs. In addition, existing streaming jobs that use these SDK versions may
fail.

**Dataflow SDK Deprecation Notice:** The Dataflow SDK 2.5.0 is the last
Dataflow SDK release that is separate from the Apache Beam SDK releases. The
Dataflow service supports official Apache Beam SDK releases as documented in
the [ SDK version support status page ](/dataflow/docs/support/sdk-version-
support-status) .

This page documents production updates to the Dataflow SDK for Python. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

The Dataflow SDK for Python now supports streaming execution (beta), as of
Dataflow SDK 2.5.0.

The [ SDK version support status page ](/dataflow/docs/support/sdk-version-
support-status) contains information about the support status of each release
of the Dataflow SDK.

To install and use the Dataflow SDK, see the [ Dataflow SDK installation guide
](/dataflow/docs/installing-dataflow-sdk) .

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

##  Cloud Dataflow SDK distribution contents

The Dataflow SDK distribution contains a subset of the Apache Beam ecosystem.
This subset includes the necessary components to define your pipeline and
execute it locally and on the Dataflow service, such as:

  * The core SDK 
  * DirectRunner and DataflowRunner 
  * I/O components for other Google Cloud services 

The Dataflow SDK distribution **does not** include other Beam components, such
as:

  * Runners for other distributed processing engines 
  * I/O components for non-Google Cloud services 

##  Release notes

This section provides each version's most relevant changes for Dataflow
customers.

###  March 24, 2019

**CHANGED:**

The following SDK versions will be decommissioned later in 2019 due to the [
discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints
](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-
rpc-and.html) . Note that this change overrides the release note from December
17, 2018, that states that decommissioning was expected to happen in March
2019.

  * Apache Beam SDK for Java, versions 2.0.0 to 2.4.0 (inclusive) 
  * Apache Beam SDK for Python, versions 2.0.0 to 2.4.0 (inclusive) 
  * Dataflow SDK for Java, versions 2.0.0 to 2.4.0 (inclusive) 
  * Dataflow SDK for Python, 2.0.0 to 2.4.0 (inclusive) 

See the [ SDK version support status page ](/dataflow/docs/support/sdk-
version-support-status) for detailed SDK support status.

###  December 17, 2018

**DEPRECATED:**

The following SDK versions will be decommissioned on March 25, 2019 due to the
[ discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints
](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-
rpc-and.html) . Shortly after this date, you will no longer be able to submit
new Dataflow jobs or update running Dataflow jobs that use the decommissioned
SDKs. In addition, existing streaming jobs that use these SDK versions might
fail.

  * Apache Beam SDK for Java, versions 2.0.0 to 2.4.0 (inclusive) 
  * Apache Beam SDK for Python, versions 2.0.0 to 2.4.0 (inclusive) 
  * Dataflow SDK for Java, versions 2.0.0 to 2.4.0 (inclusive) 
  * Dataflow SDK for Python, versions 2.0.0 to 2.4.0 (inclusive) 

