#  Release notes: Cloud Dataflow SDK 2.x for Java

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

**NOTE:** Cloud Dataflow SDK 2.x releases have a number of significant changes
from the 1.x series of releases. See the changes in the [ 1.x to 2.x migration
guide ](/dataflow/docs/guides/migrate-java-1-to-2) .

In January 2016, Google announced the donation of the Dataflow SDKs to the [
Apache Software Foundation ](http://www.apache.org/) as part of the [ Apache
Beam ](https://beam.apache.org/) project. The Dataflow SDKs are now based on
Apache Beam.

The Dataflow SDK for Java 2.0.0 is the first stable 2.x release of the
Dataflow SDK for Java, based on a subset of the Apache Beam code base. For
information about version 1.x of the Dataflow SDK for Java, see the [ Dataflow
SDK 1.x for Java release notes ](/dataflow/release-notes/release-notes-java-1)
.

The [ SDK version support status page ](/dataflow/docs/support/sdk-version-
support-status) contains information about the support status of each release
of the Dataflow SDK.

To install and use the Dataflow SDK, see the [ Dataflow SDK installation guide
](/dataflow/docs/installing-dataflow-sdk) .

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

**Warning for users upgrading from Dataflow SDK for Java 1.x:**  
This is a new major version, and therefore comes with the following caveats.  
* **Breaking Changes:** The Dataflow SDK 2.x for Java has a number of breaking changes from the 1.x series of releases. Please see below for details.   
* **Update Incompatibility:** The Dataflow SDK 2.x for Java is update-incompatible with Dataflow 1.x. Streaming jobs using a Dataflow 1.x SDK cannot be updated to use a Dataflow 2.x SDK. Dataflow 2.x pipelines may only be updated across versions starting with SDK version 2.0.0. 

##  Cloud Dataflow SDK distribution contents

The Dataflow SDK distribution contains a subset of the Apache Beam ecosystem.
This subset includes the necessary components to define your pipeline and
execute it locally and on the Dataflow service, such as:

  * The core SDK 
  * DirectRunner and DataflowRunner 
  * I/O components for other Google Cloud Platform services 
  * Apache Kafka 

The Dataflow SDK distribution **does not** include other Beam components, such
as:

  * Runners for other distributed processing engines (such as Apache Spark or Apache Flink) 
  * I/O components for non-Cloud Platform services that are not explicitly listed above 

If your use case requires any components that are not included, you can use
the appropriate Apache Beam modules directly and still run your pipeline on
the Dataflow service.

##  Release notes

This section provides each version's most relevant changes for Dataflow
customers.

The [ Apache Beam downloads ](https://beam.apache.org/get-
started/downloads/#releases) page contains release notes for the Apache Beam
SDK releases.

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

