#  Release Notes

This page documents production updates to Cloud TPU. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/tpu-release-notes.xml `

##  August 20, 2020

**FEATURE:**

#  PyTorch/XLA 1.6 Release (GA)

##  Highlights

Cloud TPUs now support the [ PyTorch 1.6 release
](https://github.com/pytorch/pytorch/releases/tag/v1.6.0) , via PyTorch/XLA
integration. With this release we mark our general availability (GA) with the
models such as ResNet, FairSeq Transformer and RoBERTa, and HuggingFace GLUE
task models that have been rigorously tested and optimized.

In addition, with our PyTorch/XLA 1.6 release, you no longer need to run the [
env-setup.py ](https://github.com/pytorch/xla/blob/master/contrib/scripts/env-
setup.py) script on Colab/Kaggle as those are now compatible with native `
torch ` wheels. You can still continue to use that script if you would like to
run with our latest unstable releases.

##  New Features

  * XLA RNG state checkpointing/loading (https://github.com/pytorch/xla/pull/2096) 
  * Device Memory XRT API (https://github.com/pytorch/xla/pull/2295) 
  * [Kaggle/Colab] Small host VM memory environment utility (https://github.com/pytorch/xla/pull/2025) 
  * [Advanced User] XLA Builder Support (https://github.com/pytorch/xla/pull/2125) 
  * New op supported on PyTorch/XLA 
    * Hardsigmoid (https://github.com/pytorch/xla/pull/1940) 
    * true_divide (https://github.com/pytorch/xla/pull/1782) 
    * max_unpool2d (https://github.com/pytorch/xla/pull/2188) 
    * max_unpool3d (https://github.com/pytorch/xla/pull/2188) 
    * Replication_pad1d (https://github.com/pytorch/xla/pull/2188) 
    * Replication_pad2d (https://github.com/pytorch/xla/pull/2188) 
  * Dynamic shape support on XLA:CPU and XLA:GPU (experimental) 

##  Bug Fixes

  * RNG Fix (proper dropout) 
  * Manual all-reduce in backward pass (https://github.com/pytorch/xla/pull/2325) 

##  August 19, 2020

**FEATURE:**

Cloud TPU now supports Shared VPC in Beta.

Shared VPC allows an organization to connect resources from multiple projects
to a common VPC network to communicate with each other securely and
efficiently using internal IPs from that network. This release enables
connecting to Cloud TPU Nodes from Shared VPC networks.

##  May 29, 2020

**CHANGED:**

Cloud TPU now supports TensorFlow version 1.15.3. See the [ TensorFlow 1.15.3
Release Notes ](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.3)
.

##  May 21, 2020

**CHANGED:**

Cloud TPU now supports TensorFlow 2.1.1 with Keras support. See the [
TensorFlow 2.1.1 Release Notes
](https://github.com/tensorflow/tensorflow/releases/tag/v2.1.1) for a complete
list of features included in this release.

##  May 12, 2020

**CHANGED:**

Cloud TPU currently supports TensorFlow version 1.15.2. See the [ Release
Notes ](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.2) .

TensorFlow 1.15 supported Python 2, but that support has been discontinued
with TensorFlow 1.15.2.

##  May 08, 2020

**CHANGED:**

Cloud TPU now supports TensorFlow 2.2. See the [ TensorFlow 2.2 Release Notes
](https://github.com/tensorflow/tensorflow/releases/tag/v2.2.0) for a complete
list of features included with this release. New models for Image segmentation
and Image classification have been added to the official cloud [ TPU supported
models list ](https://cloud.google.com/tpu/docs/tutorials/support-matrix) .

##  April 21, 2020

**FEATURE:**

Cloud TPUs and Cloud TPU Pods now support PyTorch 1.5 via the PyTorch/XLA
integration. This integration makes it possible for PyTorch users to do
everything they can do on GPUs on Cloud TPUs, while minimizing changes to the
user experience. You can try out PyTorch on an 8-core Cloud TPU device for
free via Google Colab, and you can use PyTorch on Cloud TPUs at a much larger
scale on Google Cloud (all the way up to full Cloud TPU Pods).

See the ⁠ [ PyTorch/XLA 1.5 Release Notes
](https://github.com/pytorch/xla/releases/tag/v1.5.0) for a complete list of
features included in this release.

##  January 09, 2020

**FEATURE:**

Cloud TPU now supports TensorFlow 2.1 with Keras support. See the [ TensorFlow
2.1 Release Notes
](https://github.com/tensorflow/tensorflow/releases/tag/v2.1.0) for a complete
list of features included in this release.

##  December 05, 2019

**FEATURE:**

Cloud TPU v2 and v3 Pods are now Generally Available for TensorFlow version
1.x. Supported models can be found [ here
](https://cloud.google.com/tpu/docs/tutorials/supported-models) .

Since TPU resources can scale from a single Cloud TPU to a Cloud TPU Pod, you
don't need to choose between a single Cloud TPU and a Cloud TPU Pod. You can
request portions of Cloud TPU Pods in slices or sets of cores, so that you
purchase only the processing power you need.

Cloud TPU v2 and v3 Pod advantages over a single v2 or v3 Cloud TPU device:

  * Increased training speeds for fast iteration in R&D *Increased human productivity by providing automatically scalable machine learning (ML) compute 
  * Ability to train much larger models 

Cloud TPU v3 Pod advantages over Cloud TPU v2 Pod:

  * Faster processing and larger memory: 
    * v2 Pod: 11.5 petaflops and 4 TB on-chip memory (HBM) 
    * v3 Pod: 100 petaflops and 32 TB HBM, with liquid cooling* Can train even larger models 

##  October 22, 2019

**CHANGED:**

Cloud TPU now supports TensorFlow version 1.15 ( [ Release Notes
](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.0) , [ API
Documentation ](https://www.tensorflow.org/versions/r1.15/api_docs/) ). See
the current supported TensorFlow versions in the [ Cloud TPU supported
versions document ](https://cloud.google.com/tpu/docs/supported-versions) .

Cloud TPU support for TensorFlow 1.15 includes the following changes:

  * The [ official Cloud TPU supported models list ](https://cloud.google.com/tpu/docs/tutorials/support-matrix) has been updated. 

##  July 29, 2019

**CHANGED:**

Cloud TPU now supports [ TensorFlow version 1.14
](https://www.tensorflow.org/versions/r1.14/api_docs/) . Support for
Tensorflow versions 1.11 is removed. See the current supported TensorFlow
versions in the [ Cloud TPU versioning policy
](https://cloud.google.com/tpu/docs/supported-versions) .

Cloud TPU support for TensorFlow 1.14 includes the following changes:

  * Improved Error Messages: Cloud TPU errors in TensorFlow 1.14 are aggregated across multiple TPU cores and across multiple workers. This change makes error messages more comprehensible for user code. 
  * Redesigned object detection codebase: The [ object detection codebase ](https://github.com/tensorflow/tpu/tree/master/models/official/detection) provides optimized training performance, clean and configurable parameter management, and advanced features such as spatial partition, [ NAS-FPN ](https://arxiv.org/abs/1904.07392) and [ AutoAugment ](https://arxiv.org/abs/1805.09501) . 

##  May 07, 2019

**FEATURE:**

Cloud TPU v2 Pod is available in Beta release.

Since TPU resources can scale from a single Cloud TPU to a Cloud TPU Pod, you
don't need to choose between a single Cloud TPU and a Cloud TPU Pod. You can
request portions of Cloud TPU Pods in _slices_ or sets of cores, so that you
purchase only the processing power you need.

[ Cloud TPU Pod (beta) advantages over a single Cloud TPU v2 device:
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu)

  * Increased training speeds for fast iteration in R&D 
  * Increased human productivity by providing automatically scalable machine learning (ML) compute 
  * Ability to train much larger models 

**FEATURE:**

Cloud TPU v3 Pod is available in Beta release.

Since TPU resources can scale from a single Cloud TPU to a Cloud TPU Pod, you
don't need to choose between a single Cloud TPU and a Cloud TPU Pod. You can
request portions of Cloud TPU Pods in _slices_ or sets of cores, so that you
purchase only the processing power you need.

[ Cloud TPU Pod (beta) advantages over a single v3 Cloud TPU device:
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu)

  * Increased training speeds for fast iteration in R&D 
  * Increased human productivity by providing automatically scalable machine learning (ML) compute 
  * Ability to train much larger models 

Cloud TPU v3 Pod _(beta)_ advantages over Cloud TPU v2 Pod _(beta)_ :

  * Faster processing and larger memory: 
    * v2 Pod: 11.5 petaflops and 4 TB on-chip memory (HBM) 
    * v3 Pod: 100 petaflops and 32 TB HBM, with liquid cooling* Can train even larger models 

##  March 11, 2019

**CHANGED:**

Cloud TPU now supports [ TensorFlow version 1.13
](https://www.tensorflow.org/versions/r1.13/api_docs/) . Support for
Tensorflow versions 1.8 and 1.9 have been removed.

See the current supported TensorFlow versions in the [ Cloud TPU versioning
policy ](https://cloud.google.com/tpu/docs/supported-versions) .

##  January 31, 2019

**FEATURE:**

Cloud TPU v3 is now GA (generally available). Cloud TPU v3 has double the
memory of v2. This gives improved performance and enables support for more
classes of models, for example deeper ResNets and larger images with
RetinaNet. Existing models that run on Cloud TPU v2 will continue to work.
Refer to the [ Cloud TPU versions guide
](https://cloud.google.com/tpu/docs/deciding-tpu-version) for more
information.

##  November 08, 2018

**CHANGED:**

Cloud TPU now supports [ TensorFlow version 1.12
](https://www.tensorflow.org/versions/r1.12/api_docs/) . This release includes
improvements for Keras on Cloud TPUs, performance optimizations throughout the
software stack, and improved APIs, error messages, and reliability.

See the current supported TensorFlow versions in the [ Cloud TPU versioning
policy ](https://cloud.google.com/tpu/docs/supported-versions) .

##  November 07, 2018

**FEATURE:**

Cloud TPU v2 Pod is available in Alpha release.

Since TPU resources can scale from a single Cloud TPU to a Cloud TPU Pod, you
don't need to choose between a single Cloud TPU and a Cloud TPU Pod. You can
request portions of Cloud TPU Pods in _slices_ or sets of cores, so that you
purchase only the processing power you need.

[ Cloud TPU Pod (alpha) advantages:
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu)

  * Increased training speeds for fast iteration in R&D 
  * Increased human productivity by providing automatically scalable machine learning (ML) compute 
  * Ability to train much larger models than on a single ML accelerator 

##  October 10, 2018

**FEATURE:**

Cloud TPU v3 is available in Beta release. You now have a choice between v2
and v3 in your configuration.

  * Cloud TPU v3 has double the memory of v2. This gives improved performance and enables support for more classes of models, for example deeper ResNets and larger images with RetinaNet. 
  * Existing models that run on Cloud TPU v2 will continue to work. 
  * Refer to the [ Cloud TPU versions guide for more information. ](https://cloud.google.com/tpu/docs/deciding-tpu-version)

**CHANGED:**

Preemptible TPUs are now GA (generally available). A preemptible TPU is a
Cloud TPU node that you can create and run at a much lower price than normal
nodes. However, Cloud TPU may terminate (preempt) these nodes if it requires
access to the resources for another purpose.

  * See how to [ use a preemptible TPU ](https://cloud.google.com/tpu/docs/preemptible) . 
  * Review the [ pricing ](https://cloud.google.com/tpu/docs/pricing) for preemptible and normal Cloud TPU nodes. 

##  September 27, 2018

**CHANGED:**

Cloud TPU now supports [ TensorFlow version 1.11
](https://www.tensorflow.org/versions/r1.11/api_docs/) . TensorFlow 1.11
introduces experimental support for all of the following on Cloud TPU: Keras,
Colab, eager execution, LARS, RNNs, and [ Mesh TensorFlow
](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/mesh_tensorflow/README.md)
. This release also introduces a high-performance [ Cloud Bigtable
](https://cloud.google.com/bigtable/) integration, new XLA compiler
optimizations, other performance optimizations throughout the software stack,
and it provides improved APIs, error messages, and reliability.

See the current supported TensorFlow versions in the [ Cloud TPU versioning
policy ](https://cloud.google.com/tpu/docs/supported-versions) .

##  September 07, 2018

**CHANGED:**

Support for TensorFlow version 1.7 ended on September 7, 2018. See the current
supported versions in the [ Cloud TPU versioning policy
](https://cloud.google.com/tpu/docs/supported-versions) .

##  July 24, 2018

**CHANGED:**

We're delighted to announce promotional pricing for Cloud TPU, resulting in
significant price reductions. The following table shows the previous pricing
and the new pricing available from today:

**US**

|  Previous price per TPU per hour  |  New price per TPU per hour  
---|---|---  
Cloud TPU  |  $6.50 USD  |  $4.50 USD  
Preemptible TPU  |  $1.95 USD  |  $1.35 USD  
  
**Europe**

|  Previous price per TPU per hour  |  New price per TPU per hour  
---|---|---  
Cloud TPU  |  $7.15 USD  |  $4.95 USD  
Preemptible TPU  |  $2.15 USD  |  $1.485 USD  
  
**Asia Pacific**

|  Previous price per TPU per hour  |  New price per TPU per hour  
---|---|---  
Cloud TPU  |  $7.54 USD  |  $5.22 USD  
Preemptible TPU  |  $2.26 USD  |  $1.566 USD  
  
See the [ pricing guide ](https://cloud.google.com/tpu/docs/pricing) for
details.

##  July 12, 2018

**FEATURE:**

Cloud TPU is now available in Google Kubernetes Engine as a Beta feature. Run
your machine learning workload in a Kubernetes cluster on GCP, and let GKE
manage and scale the Cloud TPU resources for you.

  * Follow the [ tutorial ](https://cloud.google.com/tpu/docs/tutorials/kubernetes-engine-resnet) to train the Tensorflow ResNet-50 model on Cloud TPU and GKE. 
  * Refer to the [ GKE setup guide ](https://cloud.google.com/tpu/docs/kubernetes-engine-setup) for quick instructions on running Cloud TPU with GKE. 

##  July 02, 2018

**CHANGED:**

Cloud TPU now supports [ TensorFlow version 1.9
](https://www.tensorflow.org/versions/r1.9/api_docs/) . TensorFlow 1.9 brings
increases in Cloud TPU performance as well as improved APIs, error messages,
and reliability.

##  June 27, 2018

**FEATURE:**

Cloud TPU is now GA (generally available). Google's revolutionary TPUs are
designed to accelerate machine learning workloads with TensorFlow. Each Cloud
TPU provides up to 180 teraflops of performance, providing the computational
power to train and run cutting-edge machine learning models.

  * Follow the [ quickstart guide ](https://cloud.google.com/tpu/docs/quickstart) to set up your Cloud TPU. 
  * Choose a [ tutorial ](https://cloud.google.com/tpu/docs/tutorials) to run a specific model on your Cloud TPU. 

##  June 18, 2018

**FEATURE:**

Preemptible TPUs are now available in _Beta_ . A preemptible TPU is a Cloud
TPU node that you can create and run at a much lower price than normal nodes.
However, Cloud TPU may terminate (preempt) these nodes if it requires access
to the resources for another purpose.

  * See how to [ use a preemptible TPU ](https://cloud.google.com/tpu/docs/preemptible) . 
  * Review the [ pricing ](https://cloud.google.com/tpu/docs/pricing) for preemptible and normal Cloud TPU nodes. 

**CHANGED:**

Cloud TPU is now available in the European (EU) and Asia Pacific (APAC)
regions as well as the United States (US). See the the [ pricing details
](https://cloud.google.com/tpu/docs/pricing) per region. The following zones
are available:

  * **US**
    * ` us-central1-b `
    * ` us-central1-c `
    * ` us-central1-f ` ( [ TFRC program ](https://www.tensorflow.org/tfrc/) only) 
  * **EU**
    * ` europe-west4-a `
  * **APAC**
    * ` asia-east1-c `

##  June 12, 2018

**CHANGED:**

Support for TensorFlow version 1.6 ended on June 12, 2018. See the current
supported versions in the [ Cloud TPU versioning policy
](https://cloud.google.com/tpu/docs/supported-versions) .

##  April 20, 2018

**CHANGED:**

Cloud TPU now supports [ TensorFlow version 1.8
](https://www.tensorflow.org/versions/r1.8/api_docs/) . TensorFlow 1.8 brings
increases in Cloud TPU performance as well as improved APIs, error messages,
and reliability.

Support for TensorFlow version 1.7 ends on June 20, 2018. See the details in
the [ Cloud TPU versioning policy
](https://cloud.google.com/tpu/docs/supported-versions) .

##  April 02, 2018

**CHANGED:**

Cloud TPU now supports [ TensorFlow version 1.7
](https://www.tensorflow.org/versions/r1.7/api_docs/) . Support for TensorFlow
version 1.6 ends on June 2, 2018. See the details in the [ Cloud TPU
versioning policy ](https://cloud.google.com/tpu/docs/supported-versions) .

##  February 12, 2018

**FEATURE:**

Cloud TPU is available in Beta release. Google's revolutionary TPUs are
designed to accelerate machine learning workloads with TensorFlow. Each Cloud
TPU provides up to 180 teraflops of performance, providing the computational
power to train and run cutting-edge machine learning models.

  * See how to [ request TPU quota ](https://cloud.google.com/tpu/docs/quota) . 
  * Follow the [ quickstart guide ](https://cloud.google.com/tpu/docs/quickstart) to set up your Cloud TPU. 
  * Choose a [ tutorial ](https://cloud.google.com/tpu/docs/tutorials) to run a specific model on your Cloud TPU. 

