#  Release Notes: Dataflow SDK 1.x for Java

**Warning:** Dataflow SDK 1.x for Java is unsupported as of October 16, 2018.
After August 12, 2020, Dataflow will not run jobs using Dataflow 1.x and
below. See [ Migrating from Dataflow SDK 1.x for Java
](/dataflow/docs/guides/migrate-java-1-to-2) for migration guidance.

This page documents production updates to the Dataflow SDK 1.x for Java. You
can periodically check this page for announcements about new or updated
features, bug fixes, known issues, and deprecated functionality. For
information about version 2.x of the Dataflow SDK for Java, see the [ Dataflow
SDK 2.x for Java release notes ](/dataflow/release-notes/release-notes-java-2)
.

The [ support page ](/dataflow/support#supportstatus) contains information
about the support status of each release of the Dataflow SDK.

To install and use the Dataflow SDK, see the [ Dataflow SDK installation guide
](/dataflow/docs/installing-dataflow-sdk) .

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

##  October 16, 2018

**DEPRECATED:**

Dataflow SDK 1.x for Java is unsupported as of October 16, 2018. In the near
future, the Dataflow service will reject new Dataflow jobs that are based on
Dataflow SDK 1.x for Java. See [ Migrating from Dataflow SDK 1.x for Java
](/dataflow/docs/guides/migrate-java-1-to-2) for migration guidance.

##  1.9.1 (August 28, 2017)

**FIXED:**

Fixed an issue with Dataflow jobs that read from ` CompressedSource ` s with
compression type set to ` BZIP2 ` are potentially losing data during
processing. For more information, see [ Issue #596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) on the
GitHub repository.

##  1.9.0 (December 20, 2016)

**ISSUE:**

**Identified issue:** Dataflow jobs that read from ` CompressedSource ` s with
compression type set to ` BZIP2 ` are potentially losing data during
processing. For more information, see [ Issue #596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) on the
GitHub repository.

**FEATURE:**

Added support for using the [ Stackdriver Error Reporting Interface
](/dataflow/pipelines/dataflow-monitoring-intf#error-reporting) .

**FEATURE:**

Added the ` ValueProvider ` interface for use in pipeline options. Making an
option of type ` ValueProvider<T> ` instead of ` T ` allows its value to be
supplied at runtime (rather than pipeline construction time) and enables [
Cloud Dataflow templates ](/dataflow/docs/templates/overview) . Support for `
ValueProvider ` has been added to ` TextIO ` , ` PubSubIO ` , and ` BigQueryIO
` and can be added to arbitrary PTransforms as well. See the [ documentation
on Cloud Dataflow templates ](/dataflow/docs/templates/overview) for more
details.

**FEATURE:**

Added the ability to automatically save profiling information to Google Cloud
Storage using the ` --saveProfilesToGcs ` pipeline option. For more
information on profiling pipelines executed by the ` DataflowPipelineRunner `
, see [ GitHub issue #72
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/72) .

**DEPRECATED:**

Deprecated the ` --enableProfilingAgent ` pipeline option that saved profiles
to the individual worker disks. For more information on profiling pipelines
executed by the ` DataflowPipelineRunner ` , see [ GitHub issue #72
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/72) .

**CHANGED:**

Changed ` FileBasedSource ` to throw an exception when reading from a file
pattern that has no matches. Pipelines will now fail at runtime rather than
silently reading no data in this case. This change affects ` TextIO.Read ` or
` AvroIO.Read ` when configured ` withoutValidation ` .

**CHANGED:**

Enhanced ` Coder ` validation in the ` DirectPipelineRunner ` to catch coders
that cannot properly encode and decode their input.

**CHANGED:**

Improved display data throughout core transforms, including properly handling
arrays in ` PipelineOptions ` .

**CHANGED:**

Improved performance for pipelines using the ` DataflowPipelineRunner ` in
streaming mode.

**CHANGED:**

Improved scalability of the ` InProcessRunner ` , enabling testing with larger
datasets.

**CHANGED:**

Improved the cleanup of temporary files created by ` TextIO ` , ` AvroIO ` ,
and other ` FileBasedSource ` implementations.

##  1.8.1 (December 12, 2016)

**ISSUE:**

**Identified issue:** Dataflow jobs that read from ` CompressedSource ` s with
compression type set to ` BZIP2 ` are potentially losing data during
processing. For more information, see [ Issue #596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) on the
GitHub repository.

**CHANGED:**

Improved the performance of bounded side inputs in the `
DataflowPipelineRunner ` .

##  1.8.0 (October 3, 2016)

**ISSUE:**

**Identified issue:** Dataflow jobs that read from ` CompressedSource ` s with
compression type set to ` BZIP2 ` are potentially losing data during
processing. For more information, see [ Issue #596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) on the
GitHub repository.

**FEATURE:**

Added support to ` BigQueryIO.Read ` for queries in the new BigQuery [
Standard SQL ](https://cloud.google.com/bigquery/sql-reference/) dialect using
` .withStandardSQL() ` .

**FEATURE:**

Added support in ` BigQueryIO ` for the new ` BYTES ` , ` TIME ` , ` DATE ` ,
and ` DATETIME ` [ types ](https://cloud.google.com/bigquery/sql-
reference/data-types) .

**FEATURE:**

Added support to ` BigtableIO.Read ` for reading from a restricted key range
using ` .withKeyRange(ByteKeyRange) ` .

**CHANGED:**

Improved initial splitting of large uncompressed files in ` CompressedSource `
, leading to better performance when executing batch pipelines that use `
TextIO.Read ` on the Cloud Dataflow service.

**FIXED:**

Fixed a [ performance regression
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/451) when
using ` BigQueryIO.Write ` in streaming mode.

##  1.7.0 (September 9, 2016)

**ISSUE:**

**Identified issue:** Dataflow jobs that read from ` CompressedSource ` s with
compression type set to ` BZIP2 ` are potentially losing data during
processing. For more information, see [ Issue #596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) on the
GitHub repository.

**ISSUE:**

**Identified issue:** We have identified a performance regression in `
BigQueryIO.Write ` . When run in streaming mode, users may see a small
increase in failed inserts, though no data will be lost or duplicated. For
more information, see [ Issue #451
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/451) in the
GitHub repository.

**FEATURE:**

Added support for Cloud Datastore API v1 in the new `
com.google.cloud.dataflow.sdk.io.datastore.DatastoreIO ` . Deprecated the old
` DatastoreIO ` class that supported only the deprecated Cloud Datastore API
v1beta2.

**FEATURE:**

Improved ` DatastoreIO.Read ` to support dynamic work rebalancing, and added
an option to control the number of query splits using ` withNumQuerySplits ` .

**FEATURE:**

Improved ` DatastoreIO.Write ` to work with an unbounded ` PCollection ` ,
supporting writing to Cloud Datastore when using the ` DataflowPipelineRunner
` in streaming mode.

**FEATURE:**

Added the ability to delete Cloud Datastore ` Entity ` objects directly using
` Datastore.v1().deleteEntity ` or to delete entities by key using `
Datastore.v1().deleteKey ` .

**FEATURE:**

Added support for reading from a ` BoundedSource ` to the `
DataflowPipelineRunner ` in streaming mode. This enables the use of `
TextIO.Read ` , ` AvroIO.Read ` and other bounded sources in these pipelines.

**FEATURE:**

Added support for optionally writing a header and/or footer to text files
produced with ` TextIO.Write ` .

**FEATURE:**

Added the ability to control the number of output shards produced when using a
` Sink ` .

**FEATURE:**

Added ` TestStream ` to enable testing of triggers with multiple panes and
late data with the ` InProcessPipelineRunner ` .

**FEATURE:**

Added the ability to control the rate at which ` UnboundedCountingInput `
produces elements using ` withRate(long, Duration) ` .

**FEATURE:**

Improved performance and stability for pipelines using the `
DataflowPipelineRunner ` in streaming mode.

**CHANGED:**

To support ` TestStream ` , reimplemented ` DataflowAssert ` to use `
GroupByKey ` instead of ` sideInputs ` to check assertions. This is an update-
incompatible change to ` DataflowAssert ` for pipelines run on the `
DataflowPipelineRunner ` in streaming mode.

**FIXED:**

Fixed an issue in which a ` FileBasedSink ` would produce no files when
writing an empty ` PCollection ` .

**FIXED:**

Fixed an issue in which ` BigQueryIO.Read ` could not query a table in a non-
` US ` region when using the ` DirectPipelineRunner ` or the `
InProcessPipelineRunner ` .

**FIXED:**

Fixed an issue in which the combination of timestamps near the end of the
global window and a large ` allowedLateness ` could cause an `
IllegalStateException ` for pipelines run in the ` DirectPipelineRunner ` .

**FIXED:**

Fixed a ` NullPointerException ` that could be thrown during pipeline
submission when using an ` AfterWatermark ` trigger with no late firings.

##  1.6.1 (August 8, 2016)

**ISSUE:**

**Identified issue:** Dataflow jobs that read from ` CompressedSource ` s with
compression type set to ` BZIP2 ` are potentially losing data during
processing. For more information, see [ Issue #596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) on the
GitHub repository.

**FIXED:**

Fixed an issue with Dataflow jobs reading from ` TextIO ` with compression
type set to ` GZIP ` or ` BZIP2 ` . For more information, see [ Issue #356
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/356) on the
GitHub repository.

##  1.6.0 (June 10, 2016)

**ISSUE:**

**Identified issue:** Dataflow jobs that read from ` CompressedSource ` s with
compression type set to ` BZIP2 ` are potentially losing data during
processing. For more information, see [ Issue #596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) on the
GitHub repository.

**ISSUE:**

**Identified issue:** Dataflow jobs reading from ` TextIO ` , with compression
type set to ` GZIP ` or ` BZIP2 ` , are potentially losing data during
processing. Users are advised to employ the workarounds discussed in [ Issue
#356 ](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/356) in
the GitHub repository.

**FEATURE:**

Added display data, which allows annotating user functions ( ` DoFn ` , `
CombineFn ` , and ` WindowFn ` ), ` Source ` s, and ` Sink ` s with static
metadata to be displayed in the Dataflow Monitoring Interface. Display data
has been implemented for core components and is automatically applied to all `
PipelineOptions ` .

**FEATURE:**

Added the methods ` getSplitPointsConsumed ` and ` getSplitPointsRemaining `
to the ` BoundedReader ` API to improve Dataflow's ability to automatically
scale a job reading from these sources. Default implementations of these
functions have been provided, but reader implementers should override them to
provide better information when available.

**FEATURE:**

Added the ability to compose multiple ` CombineFn ` s into a single `
CombineFn ` using ` CombineFns.compose ` or ` CombineFns.composeKeyed ` .

**FEATURE:**

Added ` InProcessPipelineRunner ` , an improvement over the `
DirectPipelineRunner ` that better implements the Dataflow model. `
InProcessPipelineRunner ` runs on a user's local machine and supports
multithreaded execution, unbounded ` PCollections ` , and triggers for
speculative and late outputs.

**CHANGED:**

Reimplemented ` BigQueryIO ` so that the ` DirectPipelineRunner ` and `
InProcessPipelineRunner ` implementations execute similarly to the `
DataflowPipelineRunner ` . You must now specify the ` --tempLocation ` [
execution parameter ](/dataflow/pipelines/specifying-exec-params) when using `
DirectPipelineRunner ` or ` InProcessPipelineRunner ` .

**FIXED:**

Improved performance of side inputs when using workers with many cores.

**FIXED:**

Improved efficiency when using ` CombineFnWithContext ` .

**FIXED:**

Fixed several issues related to stability in the streaming mode.

##  1.5.1 (April 15, 2016)

  * Fixed an issue that hid ` BigtableIO.Read.withRowFilter ` , which allows Cloud Bigtable rows to be filtered in the ` Read ` transform. 
  * Fixed support for concatenated GZip files. 
  * Fixed an issue that prevented ` Write.to ` to be used with merging windows. 
  * Fixed an issue that caused excessive triggering with repeated composite triggers. 
  * Fixed an issue with merging windows and triggers that finish before the end of the window. 

##  1.5.0 (March 14, 2016)

With this release, we have begun preparing the Dataflow SDK for Java for an
eventual move to [ Apache Beam (incubating)
](https://www.google.com/url?sa=D&q=https%3A%2F%2Fcloudplatform.googleblog.com%2F2016%2F01%2FDataflow-
and-open-source-proposal-to-join-the-Apache-Incubator.html) . Specifically, we
have refactored a number of internal APIs and removed from the SDK classes
used only within the worker, which will now be provided by the Google Cloud
Dataflow Service during job execution. This refactoring should not affect any
user code.

Additionally, the 1.5.0 release includes the following changes:

  * Enabled an indexed side input format for batch pipelines executed on the Google Cloud Dataflow service. Indexed side inputs significantly increase performance for ` View.asList ` , ` View.asMap ` , ` View.asMultimap ` , and any non-globally-windowed ` PCollectionView ` s. 
  * Upgraded to Protocol Buffers version ` 3.0.0-beta-1 ` . If you use custom Protocol Buffers, you should recompile them with the corresponding version of the ` protoc ` compiler. You can continue using both version 2 and 3 of the Protocol Buffers syntax, and no user pipeline code needs to change. 
  * Added ` ProtoCoder ` , which is a ` Coder ` for Protocol Buffers messages that supports both version 2 and 3 of the Protocol Buffers syntax. This coder can detect when messages can be encoded deterministically. ` Proto2Coder ` is now deprecated; we recommend that all users switch to ` ProtoCoder ` . 
  * Added ` withoutResultFlattening ` to ` BigQueryIO.Read ` to disable flattening query results when reading from BigQuery. 
  * Added ` BigtableIO ` , enabling support for reading from and writing to Google Cloud Bigtable. 
  * Improved ` CompressedSource ` to detect compression format according to the file extension. Added support for reading ` .gz ` files that are transparently decompressed by the underlying transport logic. 

_Apache Beam ™  is a trademark of The Apache Software Foundation or its
affiliates in the United States and/or other countries. _

##  1.4.0 (January 22, 2016)

  * Added a series of [ batch and streaming example pipelines ](/dataflow/examples/gaming-example) in a mobile gaming domain that illustrate some advanced topics, including windowing and triggers. 
  * Added support for ` Combine ` functions to access pipeline options and side inputs through a context. See ` GlobalCombineFn ` and ` PerKeyCombineFn ` for further details. 
  * Modified ` ParDo.withSideInputs() ` such that successive calls are cumulative. 
  * Modified automatic coder detection of Protocol Buffer messages; such classes now have their coders provided automatically. 
  * Added support for limiting the number of results returned by ` DatastoreIO.Source ` . However, when this limit is set, the operation that reads from Cloud Datastore is performed by a single worker rather than executing in parallel across the worker pool. 
  * Modified definition of ` PaneInfo.{EARLY, ON_TIME, LATE} ` so that panes with only late data are always ` LATE ` , and an ` ON_TIME ` pane can never cause a later computation to yield a ` LATE ` pane. 
  * Modified ` GroupByKey ` to drop late data when that late data arrives for a window that has expired. An expired window means the end of the window is passed by more than the allowed lateness. 
  * When using ` GlobalWindows ` , you are no longer required to specify ` withAllowedLateness() ` , since no data is ever dropped. 
  * Added support for obtaining the default project ID from the default project configuration produced by newer versions of the ` gcloud ` utility. If the default project configuration does not exist, Dataflow reverts to using the old project configuration generated by older versions of the ` gcloud ` utility. 

##  1.3.0 (December 4, 2015)

  * Improved ` IterableLikeCoder ` to efficiently encode small values. This change is backward compatible; however, if you have a running pipeline that was constructed with SDK version 1.3.0 or later, it may not be possible to [ "update" ](/dataflow/pipelines/updating-a-pipeline) that pipeline with a replacement that was constructed using SDK version 1.2.1 or older. Updating a running pipeline with a pipeline constructed using a new SDK version, however, should be successful. 
  * When ` TextIO.Write ` or ` AvroIO.Write ` outputs to a fixed number of files, added a reshard (shuffle) step immediately prior to the write step. The cost of this reshard is often exceeded by additional parallelism available to the preceding stage. 
  * Added support for RFC 3339 timestamps in ` PubsubIO ` . This allows reading from Cloud Pub/Sub topics published by Cloud Logging without losing timestamp information. 
  * Improved memory management to help prevent pipelines in the streaming execution mode from stalling when running with high memory utilization. This particularly benefits pipelines with large ` GroupByKey ` results. 
  * Added ability to customize timestamps of emitted windows. Previously, the watermark was held to the earliest timestamp of any buffered input. With this change, you can choose a later time to allow the watermark to progress further. For example, using the end of the window will prevent long-lived sessions from holding up the output. See ` Window.Bound.withOutputTime() ` . 
  * Added a simplified syntax for early and late firings with an ` AfterWatermark ` trigger, as follows: ` AfterWatermark.pastEndOfWindow().withEarlyFirings(...).withLateFirings(...) ` . 

##  1.2.1 (October 21, 2015)

  * Fixed a regression in ` BigQueryIO ` that unnecessarily printed a lot of messages when executed using ` DirectPipelineRunner ` . 

##  1.2.0 (October 5, 2015)

  * Added Java 8 support. Added new ` MapElements ` and ` FlatMapElements ` transforms that accept Java 8 lambdas, for those cases when the full power of ` ParDo ` is not required. ` Filter ` and ` Partition ` accept lambdas as well. Java 8 functionality is demonstrated in a new ` MinimalWordCountJava8 ` example. 
  * Enabled ` @DefaultCoder ` annotations for generic types. Previously, a ` @DefaultCoder ` annotation on a generic type was ignored, resulting in diminished functionality and confusing error messages. It now works as expected. 
  * ` DatastoreIO ` now supports (parallel) reads within namespaces. Entities can be written to namespaces by setting the namespace in the ` Entity ` key. 
  * Limited the ` slf4j-jdk14 ` dependency to the ` test ` scope. When a Dataflow job is executing, the ` slf4j-api ` , ` slf4j-jdk14 ` , ` jcl-over-slf4j ` , ` log4j-over-slf4j ` , and ` log4j-to-slf4j ` dependencies will be provided by the system. 

##  1.1.0 (September 15, 2015)

  * Added a coder for type ` Set<T> ` to the coder registry, when type ` T ` has its own registered coder. 
  * Added ` NullableCoder ` , which can be used in conjunction with other coders to encode a ` PCollection ` whose elements may possibly contain ` null ` values. 
  * Added ` Filter ` as a composite ` PTransform ` . Deprecated static methods in the old ` Filter ` implementation that return ` ParDo ` transforms. 
  * Added ` SourceTestUtils ` , which is a set of helper functions and test harnesses for testing correctness of ` Source ` implementations. 

##  1.0.0 (August 10, 2015)

  * The initial General Availability (GA) version, open to all developers, and considered stable and fully qualified for production use. It coincides with the General Availability of the Dataflow Service. 
  * Removed the default values for ` numWorkers ` , ` maxNumWorkers ` , and similar settings. If these are unspecified, the Dataflow Service will pick an appropriate value. 
  * Added checks to ` DirectPipelineRunner ` to help ensure that ` DoFn ` s obey the existing requirement that inputs and outputs must not be modified. 
  * Added support in ` AvroCoder ` for ` @Nullable ` fields with deterministic encoding. 
  * Added a requirement that anonymous ` CustomCoder ` subclasses override ` getEncodingId ` method. 
  * Changed ` Source.Reader ` , ` BoundedSource.BoundedReader ` , ` UnboundedSource.UnboundedReader ` to be abstract classes, instead of interfaces. ` AbstractBoundedReader ` has been merged into ` BoundedSource.BoundedReader ` . 
  * Renamed ` ByteOffsetBasedSource ` and ` ByteOffsetBasedReader ` to ` OffsetBasedSource ` and ` OffsetBasedReader ` , introducing ` getBytesPerOffset ` as a translation layer. 
  * Changed ` OffsetBasedReader ` , such that the subclass now has to override ` startImpl ` and ` advanceImpl ` , rather than ` start ` and ` advance ` . The protected variable ` rangeTracker ` is now hidden and updated by base class automatically. To indicate split points, use the method ` isAtSplitPoint ` . 
  * Removed methods for adjusting watermark triggers. 
  * Removed an unecessary generic parameter from ` TimeTrigger ` . 
  * Removed generation of empty panes unless explicitly requested. 

##  0.4.150727 (July 27, 2015)

  * Removed the requirement to explicitly set ` --project ` if Google Cloud SDK has the default project configuration set. 
  * Added support for creating BigQuery sources from a query. 
  * Added support for custom unbounded sources in the ` DirectPipelineRunner ` and ` DataflowPipelineRunner ` . See ` UnboundedSource ` for details. 
  * Removed unnecessary ` ExecutionContext ` argument in ` BoundedSource.createReader ` and related methods. 
  * Changed ` BoundedReader.splitAtFraction ` to require thread-safety (i.e. safe to call asynchronously with ` advance ` or ` start ` ). Added ` RangeTracker ` to help implement thread-safe readers. Users are heavily encouraged to use the class rather than implementing an ad-hoc solution. 
  * Modified ` Combine ` transforms by lifting them into (and above) the ` GroupByKey ` resulting in better performance. 
  * Modified triggers such that after a ` GroupByKey ` , the system will switch to a "Continuation Trigger", which attempts to preserve the original intention regarding handling of speculative and late triggerings instead of returning to the default trigger. 
  * Added ` WindowFn.getOutputTimestamp ` and changed ` GroupByKey ` behavior to allow incomplete overlapping windows to not hold up progress of earlier, completed windows. 
  * Changed triggering behavior so that empty panes are produced if they are the first pane after the watermark ( ` ON_TIME ` ) or the final pane. 
  * Removed the ` Window.Trigger ` intermediate builder class. 
  * Added validation that allowed lateness is specified on the ` Window ` ` PTransform ` when a trigger is specified. 
  * Re-enabled verification of ` GroupByKey ` usage. Specifically, the key must have a deterministic coder and using ` GroupByKey ` with an unbounded ` PCollection ` requires windowing or triggers. 
  * Changed ` PTransform ` names so that they may no longer contain the ` '=' ` or ` ';' ` characters. 

##  0.4.150710 (July 10, 2015)

  * Added support for per-window tables to ` BigQueryIO ` . 
  * Added support for a custom source implementation for Avro. See ` AvroSource ` for more details. 
  * Removed 250GiB Google Cloud Storage file size upload restriction. 
  * Fixed ` BigQueryIO.Write ` table creation bug in streaming mode. 
  * Changed ` Source.createReader() ` and ` BoundedSource.createReader() ` to be abstract. 
  * Moved ` Source.splitIntoBundles() ` to ` BoundedSource.splitIntoBundles() `
  * Added support for reading bounded views of a Pub/Sub stream in ` PubsubIO ` for non-streaming ` DataflowPipeline ` s and ` DirectPipeline ` s. 
  * Added support for getting a ` Coder ` using a ` Class ` to the ` CoderRegistry ` . 
  * Changed ` CoderRegistry.registerCoder(Class<T>, Coder<T>) ` to enforce that the provided coder actually encodes values of the given class, and its use with rawtypes of generic classes is forbidden as it will rarely work correctly. 
  * Migrate to ` Create.withCoder() ` and ` CreateTimestamped.withCoder() ` instead of calling ` setCoder() ` on the outcoming ` PCollection ` when the ` Create ` ` PTransform ` is being applied. 
  * Added three successively more detailed ` WordCount ` examples. 
  * Removed ` PTransform.getDefaultName() ` which was redundant with ` PTransform.getKindString() ` . 
  * Added support a unique name check for ` PTransform ` 's during job creation. 
  * Removed ` PTransform.withName() ` and ` PTransform.setName() ` The name of a transform is now immutable after construction. Library transforms (like ` Combine ` ) can provide builder-like methods to change the name. Names can always be overridden at the location where the transform is applied using ` apply("name", transform) ` . 
  * Added the ability to select the network for worker VMs using ` DataflowPipelineWorkerPoolOptions.setNetwork(String) `

##  0.4.150602 (June 2, 2015)

  * Added a dependency on the ` [ gcloud ](https://cloud.google.com/sdk/gcloud/) core ` component version 2015.02.05 or newer. Update to the latest version of ` gcloud ` by running ` gcloud components update ` . See [ Application Default Credentials ](https://developers.google.com/accounts/docs/application-default-credentials) for more details on how credentials can be specified. 
  * Removed previously deprecated ` Flatten.create() ` . Use ` Flatten.pCollections() ` instead. 
  * Removed previously deprecated ` Coder.isDeterministic() ` . Implement ` Coder.verifyDeterministic() ` instead. 
  * Replaced ` DoFn.Context#createAggregator ` with ` DoFn#createAggregator ` . 
  * Added support for querying the current value of an ` Aggregator ` . See ` PipelineResult ` for more information. 
  * Added experimental ` DoFnWithContext ` to simplify accessing additional information from a ` DoFn ` . 
  * Removed experimental ` RequiresKeyedState ` . 
  * Added ` CannotProvideCoderException ` to indicate inability to infer a coder, instead of returning ` null ` in such cases. 
  * Added ` CoderProperties ` for assembling test suites for user-defined coders. 
  * Replaced a constructor of ` PDone ` with a static factory ` PDone.in(Pipeline) ` . 
  * Updated string formatting of the ` TIMESTAMP ` values returned by the BigQuery source, when using ` DirectPipelineRunner ` or when BigQuery data is used as a side input, which aligns it with the case when BigQuery data is used as a main input. 
  * Added a requirement that the value returned by ` Source.Reader.getCurrent() ` must be immutable and remain valid indefinitely. 
  * Replaced some usage of ` Source ` with ` BoundedSource ` . For example, ` Read.from() ` transform can now only be applied to ` BoundedSource ` objects. 
  * Moved experimental late-data handling, i.e., the data that arrives to the streaming pipeline after the watermark has passed it, from ` PubSubIO ` to ` Window ` . Late data will default to being dropped at the first ` GroupByKey ` following a ` Read ` operation. To allow late data through use ` Window.Bound#withAllowedLateness ` . 
  * Added experimental support for accumulating elements within a window across panes. 

##  0.4.150414 (April 14, 2015)

  * Initial Beta release of the Dataflow SDK for Java. 
  * Improved execution performance in many areas of the system. 
  * Added support for progress estimation and dynamic work rebalancing for user-defined sources. 
  * Added support for user-defined sources to provide the timestamp of the values read via ` Reader.getCurrentTimestamp() ` . 
  * Added support for user-defined sinks. 
  * Added support for custom types in ` PubsubIO ` . 
  * Added support for reading and writing XML files. See ` XmlSource ` and ` XmlSink ` . 
  * Renamed ` DatastoreIO.Write.to ` to ` DatastoreIO.writeTo ` . In addition, entities written to Cloud Datastore must have complete keys. 
  * Renamed ` ReadSource ` transform into ` Read ` . 
  * Replaced ` Source.createBasicReader ` with ` Source.createReader ` . 
  * Added support for triggers, which allows getting early or partial results for a window, and specifying when to process late data. See ` Window.into.triggering ` . 
  * Reduced visibility of ` PTransform ` 's ` getInput() ` , ` getOutput() ` , ` getPipeline() ` , and ` getCoderRegistry() ` . These methods will soon be deleted. 
  * Renamed ` DoFn.ProcessContext#windows ` to ` DoFn.ProcessContext#window ` . In order for a ` DoFn ` to call ` DoFn.ProcessContext#window ` , it must implement ` RequiresWindowAccess ` . 
  * Added ` DoFn.ProcessContext#windowingInternals ` to enable windowing on third-party runners. 
  * Added support for side inputs when running streaming pipelines on the ` [Blocking]DataflowPipelineRunner ` . 
  * Changed ` [Keyed]CombineFn.addInput() ` to return the new accumulator value. Renamed ` Combine.perElement().withHotKeys() ` to ` Combine.perElement().withHotKeyFanout() ` . 
  * Renamed ` First.of ` to ` Sample.any ` and ` RateLimiting ` to ` IntraBundleParallelization ` to better represent its functionality. 

##  0.3.150326 (March 26, 2015)

  * Added support for accessing ` PipelineOptions ` in the Dataflow worker. 
  * Removed one of the type parameters in ` PCollectionView ` , which may require simple changes to user's code that uses ` PCollectionView ` . 
  * Changed side input API to apply per window. Calls to ` sideInput() ` now return values only in the specific window corresponding to the window of the main input element, and not the whole side input ` PCollectionView ` . Consequently, ` sideInput() ` can no longer be called from ` startBundle ` and ` finishBundle ` of a ` DoFn ` . 
  * Added support for viewing a ` PCollection ` as a ` Map ` when used as a side input. See ` View.asMap() ` . 
  * Renamed custom source API to use term "bundle" instead of "shard" in all names. Additionally, term "fork" is replaced with "dynamic split". 
  * Custom source ` Reader ` now requires implementing new method ` start() ` . Existing code can be fixed by simply adding this method that just calls ` advance() ` and returns its value. Additionally, code that uses the ` Reader ` should be updated to use both ` start() ` and ` advance() ` , instead of ` advance() ` only. 

##  0.3.150227 (February 27, 2015)

  * Initial Alpha version of the Dataflow SDK for Java with support for streaming pipelines. 
  * Added determinism checker in ` AvroCoder ` to make it easier to interoperate with ` GroupByKey ` . 
  * Added support for accessing ` PipelineOptions ` in the worker. 
  * Added support for compressed sources. 

##  0.3.150211 (February 11, 2015)

  * Removed the dependency on the ` gcloud core ` component version 2015.02.05 or newer. 

##  0.3.150210 (February 11, 2015)

_**Caution:** depends on the ` gcloud core ` component version 2015.02.05 or
newer. _

  * Included streaming pipeline runner, which, for now, requires additional whitelisting. 
  * Renamed several windowing-related APIs in a non-backward-compatible way. 
  * Added support for custom sources, which you can use to read from your own input formats. 
  * Introduced worker parallelism: one task per processor. 

##  0.3.150109 (January 10, 2015)

  * Fixed several platform-specific issues for Microsoft Windows. 
  * Fixed several Java 8-specific issues. 
  * Added a few new examples. 

##  0.3.141216 (December 16, 2014)

  * Initial Alpha version of the Dataflow SDK for Java. 

