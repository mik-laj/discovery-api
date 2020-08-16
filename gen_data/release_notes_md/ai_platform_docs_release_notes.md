#  Release notes

This page documents production updates to all AI Platform products. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

For more detailed information, read [ the documentation for each product
](/ai-platform/docs) .

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/aiplatform-release-notes.xml `

##  August 14, 2020

**AI Platform Training**

**FEATURE:**

The [ TabNet ](https://arxiv.org/abs/1908.07442) built-in algorithm is now
available in Beta. You can train models on tabular data for classification and
regression problems, and also get feature attributions to help explain the
model's behavior.

Try the [ TabNet built-in algorithm introductory tutorial
](https://cloud.google.com/ai-platform/training/docs/algorithms/tab-net-start)
.

##  August 10, 2020

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M54 release**

  * Added support for the europe-west3 region 
  * Updated the Explainable AI sdk and added explainers 
  * Fixed llvm-openmp support 
  * Added support for instance auto upgrade 
  * Made Deep Learning VM images and Deep Learning Containers more consistent for TPU 
  * Updated NCCL to 2.7.6 in CU110 images 
  * Added the scikit-learn package and container 
  * Added JRE to R images 
  * Limited custom container memory utilization 

##  August 06, 2020

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M53 release**

TensorFlow Enterprise 2.3 images, including images that support CUDA 11.0, are
now available.

##  August 04, 2020

**AI Platform Training**

**FEATURE:**

Read a new guide to [ distributed PyTorch training
](https://cloud.google.com/ai-platform/training/docs/distributed-pytorch) .
You can use this guide with [ pre-built PyTorch containers
](https://cloud.google.com/ai-platform/training/docs/getting-started-
pytorch#pytorch_containers) , which are in beta.

##  July 20, 2020

**AI Platform Training**

**FEATURE:**

[ Customer-managed encryption keys (CMEK) for AI Platform Training
](https://cloud.google.com/ai-platform/training/docs/cmek) is now generally
available.

**FEATURE:**

The [ VPC Service Controls integration with AI Platform Training
](https://cloud.google.com/ai-platform/training/docs/vpc-service-controls) is
now generally available.

**FEATURE:**

You can now train a PyTorch model on AI Platform Training by [ using a pre-
built PyTorch container ](https://cloud.google.com/ai-
platform/training/docs/getting-started-pytorch) . Pre-built PyTorch containers
are available in beta.

##  July 14, 2020

**AI Platform Prediction**

**FEATURE:**

[ VPC Service Controls ](https://cloud.google.com/vpc-service-
controls/docs/overview) now supports AI Platform Prediction. Learn [ how to
use a service perimeter to protect online prediction
](https://cloud.google.com/ai-platform/prediction/docs/vpc-service-controls) .
This functionality is in beta.

##  July 13, 2020

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M51 release**

Allow removing ` sudo ` access from Deep Learning Containers.

Debian-10-based images are released. You can create [ Shielded VM instances
](https://cloud.google.com/security/shielded-cloud/shielded-vm) from these
images.

**AI Platform Training**

**FEATURE:**

You can now configure a training job to run using a [ custom service account
](https://cloud.google.com/ai-platform/training/docs/custom-service-account) .
Using a custom service account can help you customize which Google Cloud
resources your training code can access.

This feature is available in beta.

##  June 23, 2020

**AI Platform Deep Learning VM Image**

**FIXED:**

**M50 release**

Miscellaneous bug fixes.

##  June 22, 2020

**AI Platform Training**

**CHANGED:**

You can now [ use Cloud TPUs for training jobs ](https://cloud.google.com/ai-
platform/training/docs/using-tpus) in the ` europe-west4 ` region. TPU v2
accelerators are generally available, and TPU v3 accelerators are available in
beta.

Learn how to [ configure your training job to use TPUs
](https://cloud.google.com/ai-platform/training/docs/using-
tpus#configuring_a_custom_tpu_machine) , and read about [ TPU pricing on AI
Platform Training ](https://cloud.google.com/ai-platform/training/pricing) .

##  June 15, 2020

**AI Platform Training**

**FEATURE:**

AI Platform Training now supports [ private services access
](https://cloud.google.com/vpc/docs/private-access-options#service-networking)
in beta. You can use VPC Network Peering to create a private connection so
that training jobs can connect to your network on private IP.

Learn how to set up [ VPC Network Peering with AI Platform Training
](https://cloud.google.com/ai-platform/training/docs/vpc-peering) .

##  June 11, 2020

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M49 release**

TensorFlow Enterprise images updated to 1.15.3 and 2.1.1.

The [ tensorflow-enterprise-addons ](https://pypi.org/project/tensorflow-
enterprise-addons/) package is now available in all deep learning
environments.

XGBoost, MXNet, R, PyTorch, CNTK, and Caffe images have been updated with
library upgrades and bug fixes.

##  June 08, 2020

**AI Platform Prediction**

**FIXED:**

The [ **Total latency** chart ](https://cloud.google.com/ai-
platform/prediction/docs/monitor-prediction) on the **Version details** page
of the Google Cloud Console was reporting incorrect information. This chart
has now been fixed.

In some cases, this adjustment might cause latencies to appear higher than
they were previously. However, the latency of models has not changed.

This affects both Compute Engine (N1) machine types and legacy (MLS1) machine
types.

##  May 21, 2020

**AI Platform Training**

**FEATURE:**

You can now use TPUs with TensorFlow 2.1 when you create a training job with
runtime version 2.1. You can also [ use TPUs with TensorFlow 2.1 when you
train in a custom container ](https://cloud.google.com/ai-
platform/training/docs/using-tpus#custom-containers) .

Read the [ guide to using TPUs with AI Platform Training
](https://cloud.google.com/ai-platform/training/docs/using-tpus) , which has
been updated to show how to use TPUs with TensorFlow 2 APIs.

##  May 18, 2020

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M48 release**

TensorFlow 2.2 images have been added. The new TensorFlow 2.2 image families
are ` tf2-2-2-cpu ` and ` tf2-2-2-cu101 ` . See the [ available image families
](https://cloud.google.com/ai-platform/deep-learning-vm/docs/images) .

##  May 13, 2020

**AI Platform Prediction**

**FEATURE:**

AI Platform Prediction now supports the following regions for batch
prediction, in addition to those that were already supported:

  * ` northamerica-northeast1 ` (Montréal) 
  * ` southamerica-east1 ` (São Paulo) 
  * ` australia-southeast1 ` (Sydney) 

See the [ full list of available regions ](https://cloud.google.com/ai-
platform/prediction/docs/regions) .

` northamerica-northeast1 ` and ` southamerica-east1 ` have the same pricing
as other Americas regions, and ` australia-southeast1 ` has the same pricing
as other Asia Pacific regions. Learn about [ pricing for each region
](https://cloud.google.com/ai-platform/prediction/pricing) .

**AI Platform Training**

**FEATURE:**

AI Platform Training now supports the following regions, in addition to those
that were already supported:

  * ` northamerica-northeast1 ` (Montréal) 
  * ` southamerica-east1 ` (São Paulo) 
  * ` australia-southeast1 ` (Sydney) 

GPUs are available for training in each of the new regions:

  * NVIDIA Tesla P4 GPUs are available in ` northamerica-northeast1 ` . 
  * NVIDIA Tesla T4 GPUs are available in ` southamerica-east1 ` . 
  * NVIDIA Tesla P4 GPUs and NVIDIA Tesla P100 GPUs are available in ` australia-southeast1 ` . 

See the [ full list of available regions ](https://cloud.google.com/ai-
platform/training/docs/regions) and the [ guide to training with GPUs
](https://cloud.google.com/ai-platform/training/docs/using-gpus) .

` northamerica-northeast1 ` and ` southamerica-east1 ` have the same pricing
as other Americas regions, and ` australia-southeast1 ` has the same pricing
as other Asia Pacific regions. Learn about [ pricing for each region
](https://cloud.google.com/ai-platform/training/pricing) .

##  May 12, 2020

**AI Platform Deep Learning VM Image**

**FIXED:**

**M47 release**

Fixed an OS login issue under single user mode for a user external to an
organization.

Fixed a git extensions plugin issue in TensorFlow 2 images.

##  April 29, 2020

**AI Platform Prediction**

**FEATURE:**

AI Platform Prediction now supports several [ regional endpoints
](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints) for
online prediction. Regional endpoints provide additional protection against
outages in other regions by isolating your model and version resources from
other regions. The following regional endpoints are available in beta:

  * ` us-central1-ml.googleapis.com `
  * ` europe-west4-ml.googleapis.com `
  * ` asia-east1-ml.googleapis.com `

You can use these endpoints instead of the global endpoint, `
ml.googleapis.com ` , when you use AI Platform Prediction for online
prediction. [ Learn how to use regional endpoints for online prediction, and
read about their benefits and limitations. ](https://cloud.google.com/ai-
platform/prediction/docs/regional-endpoints)

**FEATURE:**

You can now deploy scikit-learn and XGBoost models for online prediction using
[ Compute Engine (N1) machine types ](https://cloud.google.com/ai-
platform/prediction/docs/machine-types-online-prediction) . Previously, you
could only deploy TensorFlow models when you used these machine types. Learn
more about [ ML framework support for Compute Engine (N1) machine types
](https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-
prediction#ml_framework_support) .

You cannot use GPUs with scikit-learn or XGBoost models, and you can only use
scikit-learn and XGBoost models with Compute Engine (N1) machine types when
you deploy your models and versions to a [ regional endpoint
](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints) .

Compute Engine (N1) machine types for online prediction remain available in
the beta launch stage.

**FEATURE:**

The ` europe-west4 ` (Netherlands) and ` asia-east1 ` (Taiwan) regions are now
available for online prediction. These regions are only available for online
prediction on their respective [ regional endpoints
](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints) ,
and you can only use [ Compute Engine (N1) machine types
](https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-
prediction) for online prediction in these regions.

When you deploy model versions in the ` europe-west4 ` region, you can
optionally use NVIDIA Tesla P4, NVIDIA Tesla T4, or NVIDIA Tesla V100 GPUs to
accelerate prediction.

When you deploy model versions in the ` asia-east1 ` region, you can
optionally use NVIDIA Tesla K80 or NVIDIA Tesla P100 GPUs to accelerate
prediction.

Learn more about [ using GPUs for online prediction
](https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-
prediction#gpus) , and see [ which GPUs are available in which regions
](https://cloud.google.com/ai-platform/prediction/docs/regions) .

Learn about the [ pricing for the newly available regions and GPU resources
](https://cloud.google.com/ai-platform/prediction/pricing) .

**CHANGED:**

We recommend against using Compute Engine (N1) machine types on the AI
Platform Prediction global endpoint. Instead, only use Compute Engine (N1)
machine types when you deploy models and versions to a [ regional endpoint
](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints) .

Model versions that use Compute Engine (N1) machine types and were previously
deployed to the ` us-central1 ` region on the global endpoint will continue to
function.

##  April 24, 2020

**AI Platform Prediction**

**FEATURE:**

Visualization settings for AI Explanations are now available. You can
customize how feature attributions are displayed for image data.

Learn more about [ visualizing explanations ](https://cloud.google.com/ai-
platform/prediction/docs/ai-explanations/visualizing-explanations) .

##  April 13, 2020

**AI Platform Prediction**

**CHANGED:**

The pricing of Compute Engine (N1) machine types for online prediction in the
us-central1 region has changed. vCPU resources now cost $0.031613 per vCPU
hour and RAM now costs $0.004242 per GB hour.

[ Read more details about pricing. ](https://cloud.google.com/ai-
platform/prediction/pricing)

##  April 09, 2020

**AI Platform Prediction**

**FIXED:**

If you deploy a model version for online prediction that uses [ runtime
version 2.1 ](https://cloud.google.com/ai-platform/prediction/docs/runtime-
version-list) with a [ GPU ](https://cloud.google.com/ai-
platform/prediction/docs/machine-types-online-prediction#gpus) , AI Platform
Prediction now correctly uses TensorFlow 2.1.0 to serve predictions.
Previously, AI Platform Prediction used TensorFlow 2.0.0 to serve predictions
in this situation.

**AI Platform Training**

**FEATURE:**

You can now specify virtual machine instances with the evaluator task type as
part of your training cluster for distributed training jobs. Read more about [
evaluators in TensorFlow distributed training ](https://cloud.google.com/ai-
platform/training/docs/distributed-training-details) , see [ how to configure
machine types for evaluators ](https://cloud.google.com/ai-
platform/training/docs/machine-types) , and learn about [ using evaluators
with custom containers ](https://cloud.google.com/ai-
platform/training/docs/distributed-training-containers) .

**CHANGED:**

The maximum running time for training jobs now defaults to seven days. If a
training job is still running after this duration, AI Platform Training
cancels the job.

[ Learn how to adjust the maximum running time for a job.
](https://cloud.google.com/ai-platform/training/docs/training-
jobs#configuring_the_job)

##  April 08, 2020

**AI Platform Optimizer**

**FEATURE:**

AI Platform Optimizer is now available in [ beta
](https://cloud.google.com/products#product-launch-stages) .

AI Platform Optimizer is a black-box optimization service that helps you tune
hyperparameters in complex machine learning models.

Visit the [ AI Platform Optimizer overview ](https://cloud.google.com/ai-
platform/optimizer/docs/overview) to learn more about how it works. To get
started, try using AI Platform Optimizer to [ optimize a machine learning
model ](https://cloud.google.com/ai-platform/optimizer/docs/optimizing-ml-
model) or to [ optimize two functions at once ](https://cloud.google.com/ai-
platform/optimizer/docs/optimizing-multiple-objectives) .

##  April 06, 2020

**AI Platform Training**

**FIXED:**

[ Runtime version 2.1 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) now includes scikit-learn 0.22.1
instead of scikit-learn 0.22.

##  April 03, 2020

**AI Platform Training**

**FEATURE:**

You can now use customer-managed encryption keys (CMEK) to protect data in
your AI Platform Training jobs. This feature is available in beta.

To learn about the benefits and limitations of using CMEK, and to walk through
configuring CMEK for a training job, read the [ guide to using CMEK with AI
Platform Training ](https://cloud.google.com/ai-platform/training/docs/cmek) .

##  March 31, 2020

**AI Platform Notebooks**

**FEATURE:**

AI Platform Notebooks is now [ Generally Available
](https://cloud.google.com/products#product-launch-stages) . Some integrations
with and specific features of AI Platform Notebooks are still in beta, such as
[ Virtual Private Cloud Service Controls ](https://cloud.google.com/ai-
platform/notebooks/docs/service-perimeter) , [ Identity and Access Management
(IAM) ](https://cloud.google.com/ai-platform/notebooks/docs/iam) roles, and [
AI Platform Notebooks API ](https://cloud.google.com/ai-
platform/notebooks/docs/reference/rest) .

##  March 27, 2020

**AI Platform Prediction**

**FEATURE:**

[ AI Explanations ](https://cloud.google.com/ai-platform/prediction/docs/ai-
explanations/overview) now supports [ XRAI ](https://arxiv.org/abs/1906.02825)
, a new feature attribution method for image data.

The [ image tutorial
](https://colab.sandbox.google.com/github/GoogleCloudPlatform/ml-on-
gcp/blob/master/tutorials/explanations/ai-explanations-image.ipynb) has been
updated to include XRAI. In the tutorial, you can deploy an image
classification model using both integrated gradients and XRAI, and compare the
results.

**FEATURE:**

[ AI Explanations ](https://cloud.google.com/ai-platform/prediction/docs/ai-
explanations/overview) provides an [ approximation error
](https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/using-
feature-attributions#using-approx-error) with your explanations results.

Learn more about the [ approximation error ](https://cloud.google.com/ai-
platform/prediction/docs/ai-explanations/using-feature-attributions#using-
approx-error) and how to improve your explanations results.

**FEATURE:**

AI Platform Prediction now supports the following regions for [ batch
prediction ](https://cloud.google.com/ai-platform/prediction/docs/batch-
predict) , in addition to those that were already supported:

  * ` us-west3 ` (Salt Lake City) 
  * ` europe-west2 ` (London) 
  * ` europe-west3 ` (Frankfurt) 
  * ` europe-west6 ` (Zurich) 
  * ` asia-south1 ` (Mumbai) 
  * ` asia-east2 ` (Hong Kong) 
  * ` asia-northeast1 ` (Tokyo) 
  * ` asia-northeast2 ` (Osaka) 
  * ` asia-northeast3 ` (Seoul) 

Note that ` asia-northeast1 ` was already available for online prediction.

See the [ full list of available regions ](https://cloud.google.com/ai-
platform/prediction/docs/regions) and read about [ pricing for each region
](https://cloud.google.com/ai-platform/prediction/pricing) .

**AI Platform Training**

**FEATURE:**

AI Platform Training now supports the following regions, in addition to those
that were already supported:

  * ` us-west3 ` (Salt Lake City) 
  * ` europe-west2 ` (London) 
  * ` europe-west3 ` (Frankfurt) 
  * ` europe-west6 ` (Zurich) 
  * ` asia-south1 ` (Mumbai) 
  * ` asia-east2 ` (Hong Kong) 
  * ` asia-northeast1 ` (Tokyo) 
  * ` asia-northeast2 ` (Osaka) 
  * ` asia-northeast3 ` (Seoul) 

Out of these regions, the following support [ training with NVIDIA Tesla T4
GPUs ](https://cloud.google.com/ai-platform/training/docs/using-gpus) :

  * ` europe-west2 `
  * ` asia-south1 `
  * ` aisa-northeast1 `
  * ` asia-northeast3 `

See the [ full list of available regions ](https://cloud.google.com/ai-
platform/training/docs/regions) and read about [ pricing for each region
](https://cloud.google.com/ai-platform/training/pricing) .

##  March 17, 2020

**AI Platform Training**

**DEPRECATED:**

[ Runtime versions 1.2 through 1.9 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) are no longer available for
training. We recommend that you use runtime version 1.14 or later for your
training jobs.

Read more about the [ AI Platform Training policy for supporting older runtime
versions ](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list#runtime-version-support) . This policy is being retroactively implemented
in several stages for runtime versions 1.13 and earlier.

##  March 09, 2020

**AI Platform Prediction**

**FEATURE:**

[ Runtime version 2.1 ](https://cloud.google.com/ai-
platform/prediction/docs/runtime-version-list) for AI Platform Prediction is
now available.

Runtime version 2.1 is the first runtime version to support TensorFlow 2 for
online and batch prediction. Specifically, this runtime version includes
TensorFlow 2.1.0. Review the updated [ guide to exporting TensorFlow
SavedModels for use with AI Platform Prediction ](https://cloud.google.com/ai-
platform/prediction/docs/exporting-savedmodel-for-prediction) for details
about exporting compatible models by using TensorFlow 2 APIs, like Keras.

When you use runtime version 2.1 for online prediction, you can currently only
deploy TensorFlow model versions. You cannot deploy scikit-learn, XGBoost, or
custom prediction routine artifacts for online prediction with runtime version
2.1. For the time being, continue to use runtime version 1.15 to serve
predictions from these types of models.

Runtime version 2.1 is also the first runtime version _not_ to support Python
2.7. The Python Software Foundation ended support for Python 2.7 on January 1,
2020. No AI Platform runtime versions released after January 1, 2020 support
Python 2.7.

**ISSUE:**

If you deploy a model version for online prediction that uses [ runtime
version 2.1 ](https://cloud.google.com/ai-platform/prediction/docs/runtime-
version-list) with a [ GPU ](https://cloud.google.com/ai-
platform/prediction/docs/machine-types-online-prediction#gpus) , AI Platform
Prediction uses TensorFlow 2.0.0 (instead of TensorFlow 2.1.0) to serve
predictions. This is a known issue, and the release notes will be updated when
online prediction with GPUs supports TensorFlow 2.1.0.

**AI Platform Training**

**FEATURE:**

[ Runtime version 2.1 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) for AI Platform Training is now
available.

Runtime version 2.1 is the first runtime version to support TensorFlow 2.
Specifically, this runtime version includes TensorFlow 2.1.0. Read the new [
Training with TensorFlow 2 guide ](https://cloud.google.com/ai-
platform/training/docs/tensorflow-2) to learn about important differences to
consider when using AI Platform Training with TensorFlow 2, compared to
TensorFlow 1.

Runtime version 2.1 is also the first runtime version _not_ to support Python
2.7. The Python Software Foundation ended support for Python 2.7 on January 1,
2020. No AI Platform runtime versions released after January 1, 2020 support
Python 2.7.

Runtime version 2.1 also updates many other dependencies; see the [ runtime
version list ](https://cloud.google.com/ai-platform/training/docs/runtime-
version-list) for more details.

**ISSUE:**

[ Runtime version 2.1 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) includes scikit-learn 0.22 rather
than 0.22.1. This is a known issue, and the release notes will be updated when
runtime version 2.1 includes scikit-learn 0.22.1.

**FEATURE:**

When you train with runtime version 2.1 or later, AI Platform Training uses
the ` chief ` task name to represent the master VM in the [ ` TF_CONFIG `
environment variable ](https://cloud.google.com/ai-
platform/training/docs/distributed-training-details#chief-versus-master/) .
This environment variable is important for distributed training with
TensorFlow. For runtime version 1.15 and earlier, AI Platform Training uses
the ` master ` task name instead, but this task name is not supported in
TensorFlow 2.

However, by default, AI Platform Training continues to use the ` master ` task
name in [ custom container training jobs ](https://cloud.google.com/ai-
platform/training/docs/distributed-training-containers) . If you are
performing multi-worker distributed training with TensorFlow 2 in a custom
container, set the new [ ` trainingInput.useChiefInTfConfig `
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs#traininginput) field to
` true ` when you create a custom container training job in order to use the `
chief ` task name.

[ Learn more about this change. ](https://cloud.google.com/ai-
platform/training/docs/distributed-training-details#chief-versus-master)

##  March 06, 2020

**AI Platform Training**

**CHANGED:**

The [ built-in linear learner algorithm ](https://cloud.google.com/ai-
platform/training/docs/algorithms/linear-learner) and the [ built-in wide and
deep algorithm ](https://cloud.google.com/ai-
platform/training/docs/algorithms/wide-and-deep) now use TensorFlow 1.14 for
training. They previously used TensorFlow 1.12.

The [ single-replica version of the built-in XGBoost algorithm
](https://cloud.google.com/ai-platform/training/docs/algorithms/xgboost) now
uses XGBoost 0.81 for training. It previously used XGBoost 0.80.

##  March 05, 2020

**AI Platform Pipelines**

**FEATURE:**

[ AI Platform Pipelines ](https://cloud.google.com/ai-
platform/pipelines/docs/) is now available in beta. AI Platform Pipelines
makes it easier to get started with MLOps by saving you the difficulty of
setting up Kubeflow Pipelines with TensorFlow Extended (TFX). [ Kubeflow
Pipelines ](https://www.kubeflow.org/docs/pipelines/overview/pipelines-
overview/) is an open source platform for running, monitoring, auditing, and
managing machine learning (ML) pipelines on Kubernetes. [ TFX
](https://www.tensorflow.org/tfx) is an open source project for building ML
pipelines that orchestrate end-to-end ML workflows.

  * [ Get started with AI Platform Pipelines ](https://cloud.google.com/ai-platform/pipelines/docs/getting-started) . 
  * Learn more about [ AI Platform Pipelines and ML pipelines ](https://cloud.google.com/ai-platform/pipelines/docs/introduction) . 
  * [ Orchestrate your ML process as a pipeline ](https://cloud.google.com/ai-platform/pipelines/docs/create-pipeline) . 

##  February 11, 2020

**AI Platform Training**

**FEATURE:**

You can now set a maximum running time when you create a training job. If your
training job is still running after this duration, AI Platform Training
cancels the job. Set the maximum running time by specifying the [ `
scheduling.maxRunningTime ` ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs#scheduling) field.

##  February 10, 2020

**AI Platform Prediction**

**FIXED:**

The known issue with using custom prediction routines together with runtime
version 1.15 and Python 3.7 has been fixed. The issue was described in a [
January 23, 2020 release note ](https://cloud.google.com/ai-
platform/prediction/docs/release-notes#January_23_2020) .

You can now use [ custom prediction routines ](https://cloud.google.com/ai-
platform/prediction/docs/custom-prediction-routines) with runtime version 1.15
and Python 3.7.

##  February 05, 2020

**AI Platform Prediction**

**FIXED:**

The GPU compatibility issue that was described in the [ January 7, 2020
release note ](https://cloud.google.com/ai-platform/prediction/docs/release-
notes#January_07_2020) has been resolved. You can now use GPUs to accelerate [
prediction ](https://cloud.google.com/ai-platform/prediction/docs/machine-
types-online-prediction#gpus) on [ runtime version 1.15
](https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list) .

**AI Platform Training**

**FIXED:**

The GPU compatibility issue that was described in the [ January 7, 2020
release note ](https://cloud.google.com/ai-platform/training/docs/release-
notes#January_07_2020) has been resolved. You can now use GPUs to accelerate [
training ](https://cloud.google.com/ai-platform/training/docs/using-gpus) on [
runtime version 1.15 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) .

##  February 04, 2020

**AI Platform Notebooks**

**FEATURE:**

[ VPC Service Controls ](https://cloud.google.com/vpc-service-
controls/docs/overview) now supports AI Platform Notebooks. Learn [ how to use
a notebook instance within a service perimeter ](https://cloud.google.com/ai-
platform/notebooks/docs/service-perimeter) . This functionality is in [ beta
](https://cloud.google.com/products/#product-launch-stages) .

##  February 03, 2020

**AI Platform Notebooks**

**FEATURE:**

AI Platform Notebooks now supports Access Transparency. Access Transparency
provides you with logs of actions that Google staff have taken when accessing
your data. To learn more about Access Transparency, see the [ Overview of
Access Transparency ](https://cloud.google.com/logging/docs/audit/access-
transparency-overview#overview) .

##  January 29, 2020

**AI Platform Prediction**

**CHANGED:**

[ AI Platform Prediction documentation ](https://cloud.google.com/ai-
platform/prediction/docs/) has been reorganized. The new information
architecture only includes documents that are relevant to AI Platform
Prediction.

Previously, documentation for AI Platform Prediction and AI Platform Training
were grouped together. You can now view [ AI Platform Training documentation
](https://cloud.google.com/ai-platform/training/docs/) separately. Some
overviews and tutorials that are relevant to both products are available in
the [ overall AI Platform documentation ](https://cloud.google.com/ai-
platform/docs/) .

**AI Platform Training**

**CHANGED:**

[ AI Platform Training documentation ](https://cloud.google.com/ai-
platform/training/docs/) has been reorganized. The new information
architecture only includes documents that are relevant to AI Platform
Training.

Previously, documentation for AI Platform Training and AI Platform Prediction
were grouped together. You can now view [ AI Platform Prediction documentation
](https://cloud.google.com/ai-platform/prediction/docs/) separately. Some
overviews and tutorials that are relevant to both products are available in
the [ overall AI Platform documentation ](https://cloud.google.com/ai-
platform/docs/) .

##  January 28, 2020

**AI Platform Training**

**FEATURE:**

AI Platform Training [ runtime version 1.15 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) now supports [ training with TPUs
](https://cloud.google.com/ai-platform/training/docs/using-tpus) using
TensorFlow 1.15.

##  January 23, 2020

**AI Platform Prediction**

**ISSUE:**

Creating an AI Platform Prediction [ custom prediction routine
](https://cloud.google.com/ai-platform/prediction/docs/custom-prediction-
routines) that uses [ runtime version 1.15 ](https://cloud.google.com/ai-
platform/prediction/docs/runtime-version-list) and Python 3.7 might fail due
to a problem with a dependency.

As a workaround, use runtime version 1.15 with Python 2.7 or use a different
runtime version when you [ create your model version
](https://cloud.google.com/ai-platform/prediction/docs/deploying-
models#create_a_model_version) .

##  January 22, 2020

**AI Platform Prediction**

**CHANGED:**

[ AI Explanations ](https://cloud.google.com/ai-platform/prediction/docs/ai-
explanations/overview) no longer supports AI Platform Prediction runtime
version 1.13. AI Explanations now supports runtime versions 1.14 and 1.15.
Learn more about AI Platform Prediction [ runtime versions
](https://cloud.google.com/ai-platform/prediction/docs/runtime-version-
list#xai-support) supported by AI Explanations.

##  January 21, 2020

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M41 release**

[ TensorFlow Enterprise ](https://cloud.google.com/tensorflow-
enterprise/docs/) 2.1 images are now available.

MXNet upgraded to 1.5.1.

PyTorch upgraded to 1.4.0.

XGBoost upgraded to 0.90.

##  January 15, 2020

**AI Platform Prediction**

**CHANGED:**

The [ price of using NVIDIA Tesla T4 GPUs for online prediction
](https://cloud.google.com/ai-platform/prediction/pricing#prediction-prices)
has changed from $0.9500 per hour to $0.3500 per hour.

**CHANGED:**

[ GPUs for online prediction ](https://cloud.google.com/ai-
platform/prediction/docs/machine-types-online-prediction#gpus) are currently
only available when you deploy your model in the ` us-central1 ` region and
use a Compute Engine (N1) machine type.

##  January 14, 2020

**AI Platform Training**

**CHANGED:**

The [ price of using NVIDIA Tesla T4 GPUs for training
](https://cloud.google.com/ai-platform/training/pricing#training-prices) has
changed. The following table describes the pricing change for various
geographic areas:

Geographic area  |  Old price per hour  |  New price per hour  
---|---|---  
` Americas ` |  $0.9500  |  $0.3500  
` Europe ` |  $1.0300  |  $0.3800  
` Asia Pacific ` |  $1.0300  |  $0.3900  
  
Read more about [ using GPUs for training ](https://cloud.google.com/ai-
platform/training/docs/using-gpus) .

##  January 08, 2020

**AI Platform Deep Learning Containers**

**FEATURE:**

TensorFlow Enterprise environments are now available. [ Use TensorFlow
Enterprise with Deep Learning Containers
](https://cloud.google.com/tensorflow-enterprise/docs/use-with-deep-learning-
containers) .

##  January 07, 2020

**AI Platform Prediction**

**ISSUE:**

Model versions that use both [ runtime version 1.15
](https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list)
and GPUs fail due to a compatibility issue with the CuDNN library, which
TensorFlow depends on.

As a workaround, do one of the following:

  * If you want to [ use GPUs to accelerate prediction ](https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-prediction#gpus) , then use [ runtime version 1.14 or earlier ](https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list) . 
  * If you want to use [ runtime version 1.15 ](https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list) , then do not use GPUs for your model version. 

**AI Platform Training**

**ISSUE:**

Training jobs that use both [ runtime version 1.15
](https://cloud.google.com/ai-platform/training/docs/runtime-version-list) and
GPUs fail due to a compatibility issue with the CuDNN library, which
TensorFlow depends on.

As a workaround, do one of the following:

  * If you want to [ use GPUs to accelerate training ](https://cloud.google.com/ai-platform/training/docs/using-gpus) , then use [ runtime version 1.14 or earlier ](https://cloud.google.com/ai-platform/training/docs/runtime-version-list) . 
  * If you want to use [ runtime version 1.15 ](https://cloud.google.com/ai-platform/training/docs/runtime-version-list) , then do not use GPUs for your training job. 

##  December 20, 2019

**AI Platform Training**

**FEATURE:**

[ VPC Service Controls ](https://cloud.google.com/vpc-service-
controls/docs/overview) now supports AI Platform Training. Learn [ how to use
a service perimeter to protect your training jobs
](https://cloud.google.com/ai-platform/training/docs/vpc-service-controls) .
This functionality is in beta.

##  December 19, 2019

**AI Platform Prediction**

**FEATURE:**

AI Platform runtime version 1.15 is now available for prediction. This version
supports TensorFlow 1.15.0 and includes other packages as listed in the [
runtime version list ](https://cloud.google.com/ai-
platform/prediction/docs/runtime-version-list) .

Runtime version 1.15 is the first runtime version to support serving
predictions using Python 3.7, instead of Python 3.5. Runtime version 1.15 also
still supports Python 2.7. Learn about specifying the Python version [ for
prediction ](https://cloud.google.com/ai-platform/prediction/docs/deploying-
models#create_a_model_version) .

**AI Platform Training**

**FEATURE:**

AI Platform Training now offers two built-in algorithms to train a machine
learning model on image data without writing your own training code:

  * [ Built-in image classification algorithm ](https://cloud.google.com/ai-platform/training/docs/algorithms/image-classification)
  * [ Built-in image object detection algorithm ](https://cloud.google.com/ai-platform/training/docs/algorithms/object-detection)

Both image algorithms are available in beta.

**FEATURE:**

AI Platform runtime version 1.15 is now available for training. This version
supports TensorFlow 1.15.0 and includes other packages as listed in the [
runtime version list ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) .

Runtime version 1.15 is the first runtime version to support training using
Python 3.7, instead of Python 3.5. Runtime version 1.15 also still supports
Python 2.7. Learn about specifying the Python version [ for training
](https://cloud.google.com/ai-platform/training/docs/versioning#set-python-
version-training) .

Training with TPUs is not supported in runtime version 1.15 at this time.

##  December 10, 2019

**AI Platform Prediction**

**DEPRECATED:**

Starting January 1, 2020, the Python Software Foundation will no longer
support Python 2.7. Accordingly, any [ runtime versions
](https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list)
released after January 1, 2020 will not support Python 2.7.

**CHANGED:** **Note:** The following change has been delayed. There will be an
additional announcement to affected customers before it goes into effect.

Starting on January 13, 2020, AI Platform Training and AI Platform Prediction
will support each runtime version for one year after its release date. You can
find the release date of each runtime version in the [ runtime version list
](https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list) .

Support for each runtime version changes according to the following schedule:

  1. **Starting on the release date:** You can create training jobs, batch prediction jobs, and model versions that use the runtime version. 

  2. **Starting 12 months after the release date:** You can no longer create training jobs, batch prediction jobs, or model versions that use the runtime version. 

Existing model versions that have been deployed to AI Platform Prediction
continue to function.

  3. **24 months after the release date:** AI Platform Prediction automatically deletes all model versions that use the runtime version. 

This policy will be applied retroactively on January 13, 2020. For example,
since runtime version 1.0 was released over 24 months ago, AI Platform
Training and AI Platform Prediction no longer support it. There will be a
three-month grace period (until April 13, 2020) before AI Platform Prediction
automatically deletes model versions that use the oldest runtime versions.

The following table describes the first two important dates that mark the end
of support for runtime versions:

Date  |  Runtime versions affected  |  Change in functionality  
---|---|---  
January 13, 2020  |  1.0, 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11,
1.12  |  You can no longer create training jobs, batch prediction jobs, or
model versions using these runtime versions.  
April 13, 2020  |  1.0, 1.1, 1.2, 1.4, 1.5, 1.6  |  AI Platform Prediction
automatically deletes any model versions using these runtime versions.  
  
To learn about when availability ends for every runtime version, see the [
runtime version list ](https://cloud.google.com/ai-
platform/prediction/docs/runtime-version-list) .

**CHANGED:**

Starting on January 13, 2020, ` runtimeVersion ` and ` pythonVersion ` will
become required fields when you create [ ` Job `
](https://cloud.google.com/ai-
platform/prediction/docs/reference/rest/v1/projects.jobs) or [ ` Version `
](https://cloud.google.com/ai-
platform/prediction/docs/reference/rest/v1/projects.models.versions)
resources. Previously, ` runtimeVersion ` defaulted to ` 1.0 ` and `
pythonVersion ` defaulted to ` 2.7 ` .

**AI Platform Training**

**DEPRECATED:**

Starting January 1, 2020, the Python Software Foundation will no longer
support Python 2.7. Accordingly, any [ runtime versions
](https://cloud.google.com/ai-platform/training/docs/runtime-version-list)
released after January 1, 2020 will not support Python 2.7.

**CHANGED:** **Note:** The following change has been delayed. There will be an
additional announcement to affected customers before it goes into effect.

Starting on January 13, 2020, AI Platform Training and AI Platform Prediction
will support each runtime version for one year after its release date. You can
find the release date of each runtime version in the [ runtime version list
](https://cloud.google.com/ai-platform/training/docs/runtime-version-list) .

Support for each runtime version changes according to the following schedule:

  1. **Starting on the release date:** You can create training jobs, batch prediction jobs, and model versions that use the runtime version. 

  2. **Starting 12 months after the release date:** You can no longer create training jobs, batch prediction jobs, or model versions that use the runtime version. 

Existing model versions that have been deployed to AI Platform Prediction
continue to function.

  3. **24 months after the release date:** AI Platform Prediction automatically deletes all model versions that use the runtime version. 

This policy will be applied retroactively on January 13, 2020. For example,
since runtime version 1.0 was released over 24 months ago, AI Platform
Training and AI Platform Prediction no longer support it. There will be a
three-month grace period (until April 13, 2020) before AI Platform Prediction
automatically deletes model versions that use the oldest runtime versions.

The following table describes the first two important dates that mark the end
of support for runtime versions:

Date  |  Runtime versions affected  |  Change in functionality  
---|---|---  
January 13, 2020  |  1.0, 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11,
1.12  |  You can no longer create training jobs, batch prediction jobs, or
model versions using these runtime versions.  
April 13, 2020  |  1.0, 1.1, 1.2, 1.4, 1.5, 1.6  |  AI Platform Prediction
automatically deletes any model versions using these runtime versions.  
  
To learn about when availability ends for every runtime version, see the [
runtime version list ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) .

**CHANGED:** **Note:** The following change has been delayed. There will be an
additional announcement to affected customers before it goes into effect.

Starting on January 13, 2020, AI Platform Training will automatically delete
the history of each training job 120 days after it is completed. A training
job is considered completed when the job enters the [ ` SUCCEEDED ` , ` FAILED
` , or ` CANCELLED ` state ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs#state) .

This policy will be applied retroactively on January 13, 2020: all jobs that
were completed September 15, 2019 or earlier will be deleted.

**CHANGED:**

Starting on January 13, 2020, ` runtimeVersion ` and ` pythonVersion ` will
become required fields when you create [ ` Job `
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs) or [ ` Version `
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions) resources.
Previously, ` runtimeVersion ` defaulted to ` 1.0 ` and ` pythonVersion `
defaulted to ` 2.7 ` .

##  December 03, 2019

**AI Platform Prediction**

**ISSUE:**

You cannot [ enable request-response logging for AI Platform Prediction
](https://cloud.google.com/ai-platform/prediction/docs/online-
predict#requesting_logs_for_online_prediction_requests) when you create a
model version. Instead, you must first [ create a model version
](https://cloud.google.com/ai-platform/prediction/docs/deploying-
models#create_a_model_version) without request-response logging enabled, then
enable request-response logging by sending a [ `
projects.models.versions.patch ` ](https://cloud.google.com/ai-
platform/prediction/docs/reference/rest/v1/projects.models.versions/patch)
request to the REST API.

##  November 27, 2019

**AI Platform Training**

**CHANGED:**

AI Platform Training no longer supports TPUs in [ runtime version 1.12
](https://cloud.google.com/ai-platform/training/docs/runtime-version-list) .
You can still [ train using TPUs ](https://cloud.google.com/ai-
platform/training/docs/using-tpus) in runtime versions 1.13 and 1.14.

##  November 20, 2019

**AI Platform Prediction**

**FEATURE:**

AI Explanations now offers [ feature attributions
](https://cloud.google.com/ai-platform/prediction/docs/ai-
explanations/overview) through AI Platform Prediction. This feature is
available in Beta. To gain more insight on your model's predictions, you can
use feature attributions based on the sampled Shapley and integrated gradients
methods. Try the [ example notebooks ](https://cloud.google.com/ai-
platform/prediction/docs/ai-explanations/getting-started) to get started, and
refer to the [ AI Explainability Whitepaper
](https://storage.googleapis.com/cloud-ai-
whitepapers/AI%20Explainability%20Whitepaper.pdf) to learn more.

**AI Platform Training**

**FEATURE:**

AI Platform Training now offers a [ built-in distributed XGBoost algorithm
](https://cloud.google.com/ai-platform/training/docs/algorithms/distributed-
xgboost) to train a machine learning model without writing your own training
code. This algorithm is available in beta.

The built-in distributed XGBoost algorithm provides functionality similar to
the existing [ single-replica version of the built-in XGBoost algorithm
](https://cloud.google.com/ai-platform/training/docs/algorithms/xgboost) , but
it lets you speed up training on large datasets by using multiple virtual
machines in parallel. The algorithm also lets you use GPUs for training.

The built-in distributed XGBoost algorithm does not support [ automatic
preprocessing of data ](https://cloud.google.com/ai-
platform/training/docs/algorithms/preprocessing-data) .

##  November 01, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

You can now create a TensorFlow Enterprise Deep Learning VM Image. TensorFlow
Enterprise image families provide users with a Google Cloud Platform optimized
distribution of TensorFlow with [ long-term version support
](https://cloud.google.com/tensorflow-
enterprise/docs/overview#long_term_support_lts) . To learn more about
TensorFlow Enterprise, read the [ TensorFlow Enterprise overview
](https://cloud.google.com/tensorflow-enterprise/docs/overview) .

##  October 28, 2019

**AI Platform Training**

**CHANGED:**

We now recommend that you use [ Compute Engine machine types
](https://cloud.google.com/ai-platform/training/docs/machine-types#compute-
engine-machine-types) when you create new AI Platform Training jobs. These
machine types offer the greatest flexibility for customizing the virtual CPU
(vCPU), RAM, GPU, and TPU resources that your jobs use.

The older machine types available for training, which were previously referred
to as "AI Platform Training machine types," are now called " [ legacy machine
types ](https://cloud.google.com/ai-platform/training/docs/machine-
types#legacy-machine-types) " in the AI Platform Training documentation.

##  October 24, 2019

**AI Platform Prediction**

**FEATURE:**

Many [ Compute Engine (N1) machine types ](https://cloud.google.com/ai-
platform/prediction/docs/machine-types-online-prediction) are now available
for online prediction in beta, in addition to the existing legacy (MLS1)
machine types. When you create a model version with a Compute Engine machine
type, you can allocate virtual machines with more vCPU and memory resources
for your online prediction nodes, improving throughput of predictions or
reducing latency. Additionally, you can use GPUs with these new machine types
and deploy TensorFlow models up to 2 GB in size. The machine types are
currently only available in the ` us-central1 ` region.

Learn more about the [ features, limitations, and usage of Compute Engine (N1)
machine types ](https://cloud.google.com/ai-platform/prediction/docs/machine-
types-online-prediction) . Model versions that use Compute Engine (N1) machine
types, including with GPUs, are available at no charge until November 14,
2019. Read about the [ pricing for these machine types
](https://cloud.google.com/ai-platform/prediction/pricing) that goes into
effect on November 14, 2019.

**ISSUE:**

Model versions that use one of the new [ Compute Engine (N1) machine types
](https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-
prediction) and scale to use more than 40 prediction nodes may exhibit high
latency when handling online prediction requests. In this case, AI Platform
Prediction may also drop requests.

For the best performance until this issue is resolved, do not scale your model
version to use more than 40 nodes.

**CHANGED:**

The default max model size for model versions that use a legacy (MLS1) machine
type has increased from 250 MB to 500 MB.

##  October 11, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M36 release**

The TensorFlow 2.0 image is out of experimental.

**CHANGED:**

[ What-If Tool ( ` witwidget ` ) ](https://pair-code.github.io/what-if-tool/)
upgraded to 1.4.2 for TensorFlow 1.x images.

##  October 04, 2019

**AI Platform Prediction**

**FEATURE:**

The [ ` us-west2 ` (Los Angeles), ` us-east4 ` (N. Virginia), and ` europe-
north1 ` (Finland) regions ](https://cloud.google.com/ai-
platform/prediction/docs/regions) are now available for batch prediction. Note
that ` us-east4 ` was already available for online prediction.

Additionally, [ the ` us-west1 ` (Oregon) and ` europe-west4 ` (Netherlands)
regions ](https://cloud.google.com/ai-platform/prediction/docs/regions) ,
which were already available for training, are now available for batch
prediction.

Read about [ pricing for batch prediction in these regions
](https://cloud.google.com/ai-platform/prediction/pricing) .

**AI Platform Training**

**FEATURE:**

The [ ` us-west2 ` (Los Angeles), ` us-east4 ` (N. Virginia), and ` europe-
north1 ` (Finland) regions ](https://cloud.google.com/ai-
platform/training/docs/regions) are now available for training. You can use [
NVIDIA Tesla P4 GPUs ](https://cloud.google.com/ai-
platform/training/docs/using-gpus) for training in ` us-west2 ` and ` us-east4
` .

Read about [ pricing for training in these regions
](https://cloud.google.com/ai-platform/training/docs/pricing) , including
pricing for accelerators.

##  September 16, 2019

**AI Platform Prediction**

**FEATURE:**

The [ What-If Tool ](https://pair-code.github.io/what-if-tool/) can be used to
inspect models deployed on AI Platform Prediction, and to compare two models.
Learn [ how to use the What-If Tool with AI Platform Prediction
](https://cloud.google.com/ai-platform/prediction/docs/using-what-if-tool) .

##  September 09, 2019

**AI Platform Notebooks**

**FEATURE:**

AI Platform Notebooks now provides more ways for you to customize your network
settings, encrypt your notebook content, and grant access to your notebook
instance. These options are available when you [ create a notebook
](https://cloud.google.com/ai-platform/notebooks/docs/create-new#create-with-
options) .

**FEATURE:**

Now you can implement AI Platform Notebooks using custom containers. Use a [
Deep Learning Containers image ](https://cloud.google.com/ai-platform/deep-
learning-containers/docs/choosing-container#choose_a_container_image_type) or
[ create a derivative container ](https://cloud.google.com/ai-platform/deep-
learning-containers/docs/derivative-container) of your own, then [ create a
new notebook instance using your custom container
](https://cloud.google.com/ai-platform/notebooks/docs/custom-container) .

**AI Platform Training**

**FEATURE:**

[ Runtime version 1.14 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) now supports [ training with TPUs
](https://cloud.google.com/ai-platform/training/docs/using-tpus) using
TensorFlow 1.14.

##  September 06, 2019

**AI Platform Prediction**

**FEATURE:**

When you [ deploy a model version ](https://cloud.google.com/ai-
platform/prediction/docs/deploying-models) to AI Platform Prediction, you can
now configure AI Platform Prediction to log a sample of online prediction
requests received by the model together with the responses it sends to these
requests. AI Platform Prediction saves these request-response pairs to
BigQuery. This feature is in beta.

Learn how to [ how to enable request-response logging
](https://cloud.google.com/ai-platform/prediction/docs/online-
predict#requesting_logs_for_online_prediction_requests) and read about [ the
configuration options ](https://cloud.google.com/ai-
platform/prediction/docs/reference/rest/v1/projects.models.versions#requestloggingconfig)
for this type of logging.

##  August 28, 2019

**AI Platform Prediction**

**CHANGED:**

The [ documentation for AI Platform Notebooks ](https://cloud.google.com/ai-
platform/notebooks/docs/) has moved to a new location.

**AI Platform Training**

**FEATURE:**

[ Training with custom containers ](https://cloud.google.com/ai-
platform/training/docs/containers-overview) is now generally available.

**FEATURE:**

Using [ Compute Engine machine types for your training configuration
](https://cloud.google.com/ai-platform/training/docs/machine-types#compute-
engine-machine-types) is now generally available.

**FEATURE:**

NVIDIA Tesla P4 and NVIDIA Tesla T4 GPUs are now generally available for
training. Read about [ using GPUs for training ](https://cloud.google.com/ai-
platform/training/docs/using-gpus) and learn about [ GPU pricing
](https://cloud.google.com/ai-platform/training/pricing) .

**CHANGED:**

The [ documentation for AI Platform Notebooks ](https://cloud.google.com/ai-
platform/notebooks/docs/) has moved to a new location.

##  August 26, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M34 release**

JupyterLab upgraded to 1.0 on all images.

PyTorch upgraded to 1.2.

**AI Platform Training**

**FEATURE:**

AI Platform Training now supports using Cloud TPU devices with [ TPU v3
configurations ](https://cloud.google.com/tpu/docs/system-
architecture#versions) to accelerate your training jobs. TPU v3 accelerators
for AI Platform Training are available in beta.

Learn more about [ how to configure your training job to use TPU v3
accelerators ](https://cloud.google.com/ai-platform/training/docs/using-
tpus#tpu-and-compute-engine-machine-type) and read about [ TPU v3 pricing
](https://cloud.google.com/ai-platform/training/pricing) .

##  August 22, 2019

**AI Platform Prediction**

**FEATURE:**

[ Continuous evaluation ](https://cloud.google.com/ai-
platform/prediction/docs/continuous-evaluation/) for AI Platform Prediction is
now available in beta. When you create a continuous evaluation job, [ AI
Platform Data Labeling Service ](https://cloud.google.com/data-labeling/docs)
assigns human reviewers to provide ground truth labels for a portion of your
model version's online predictions; alternatively, you can provide your own
ground truth labels. Then Data Labeling Service compares these labels to your
model version's predictions to calculate daily evaluation metrics.

Learn more about [ continuous evaluation ](https://cloud.google.com/ai-
platform/prediction/docs/continuous-evaluation/) .

##  August 16, 2019

**AI Platform Prediction**

**CHANGED:**

AI Platform runtime versions 1.13 and 1.14 now include [ numpy 1.16.4
](https://github.com/numpy/numpy/releases/tag/v1.16.4) instead of numpy
1.16.0. View the [ runtime version list ](https://cloud.google.com/ai-
platform/prediction/docs/runtime-version-list) for the full list of packages
included in runtime versions 1.13 and 1.14.

**AI Platform Training**

**CHANGED:**

AI Platform runtime versions 1.13 and 1.14 now include [ numpy 1.16.4
](https://github.com/numpy/numpy/releases/tag/v1.16.4) instead of numpy
1.16.0. View the [ runtime version list ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) for the full list of packages
included in runtime versions 1.13 and 1.14.

##  August 01, 2019

**AI Platform Prediction**

**CHANGED:**

The AI Platform Prediction Training and Prediction documentation has been
reorganized. Previously, documentation for using AI Platform Prediction with
specific machine learning frameworks was separated into sections. You can now
navigate to all Training and Prediction documentation from the [ AI Platform
documentation home page ](https://cloud.google.com/ai-
platform/prediction/docs/) .

**AI Platform Training**

**CHANGED:**

The AI Platform Training Training and Prediction documentation has been
reorganized. Previously, documentation for using AI Platform Training with
specific machine learning frameworks was separated into sections. You can now
navigate to all Training and Prediction documentation from the [ AI Platform
documentation home page ](https://cloud.google.com/ai-platform/training/docs/)
.

##  July 19, 2019

**AI Platform Prediction**

**FEATURE:**

AI Platform runtime version 1.14 is now available for prediction. This version
supports TensorFlow 1.14.0 and includes other packages as listed in the [
runtime version list ](https://cloud.google.com/ai-
platform/prediction/docs/runtime-version-list) .

**CHANGED:**

AI Platform runtime version 1.12 now supports TensorFlow 1.12.3. View the [
runtime version list ](https://cloud.google.com/ai-
platform/prediction/docs/runtime-version-list) for the full list of packages
included in runtime version 1.12.

**AI Platform Training**

**FEATURE:**

AI Platform runtime version 1.14 is now available for training. This version
supports TensorFlow 1.14.0 and includes other packages as listed in the [
runtime version list ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) .

Training with TPUs is not supported in runtime version 1.14 at this time.

**CHANGED:**

AI Platform runtime version 1.12 now supports TensorFlow 1.12.3. View the [
runtime version list ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) for the full list of packages
included in runtime version 1.12.

##  July 17, 2019

**AI Platform Prediction**

**CHANGED:**

The prediction input format for the following [ built-in algorithms
](https://cloud.google.com/ai-platform/training/docs/algorithms) has changed:

  * [ Linear learner ](https://cloud.google.com/ai-platform/training/docs/algorithms/linear-start#get_online_predictions)
  * [ Wide and deep learner ](https://cloud.google.com/ai-platform/training/docs/algorithms/wide-deep-start#get_online_predictions)

Instead of a raw string, make sure to format each instance as a JSON with a
"csv_row" key and "key" key. This "key" is useful for doing batch predictions
using AI Platform Prediction. For online predictions, you can pass in a dummy
value to the "key" key in your input JSON request. For example:

` {"csv_row": "1, 2, 3, 4, 0, abc", "key" : "dummy-key"} `

See the [ Census Income tutorial ](https://cloud.google.com/ai-
platform/training/docs/algorithms/linear-start#get_online_predictions) for an
example.

**AI Platform Training**

**CHANGED:**

The prediction input format for the following [ built-in algorithms
](https://cloud.google.com/ai-platform/training/docs/algorithms) has changed:

  * [ Linear learner ](https://cloud.google.com/ai-platform/training/docs/algorithms/linear-start#get_online_predictions)
  * [ Wide and deep learner ](https://cloud.google.com/ai-platform/training/docs/algorithms/wide-deep-start#get_online_predictions)

Instead of a raw string, make sure to format each instance as a JSON with a
"csv_row" key and "key" key. This "key" is useful for doing batch predictions
using AI Platform Training. For online predictions, you can pass in a dummy
value to the "key" key in your input JSON request. For example:

` {"csv_row": "1, 2, 3, 4, 0, abc", "key" : "dummy-key"} `

See the [ Census Income tutorial ](https://cloud.google.com/ai-
platform/training/docs/algorithms/linear-start#get_online_predictions) for an
example.

##  July 12, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M30 release**

R upgraded to version 3.6.

TensorFlow: added support for using Python 3.7.

R Notebooks are no longer dependent on a Conda environment.

**FIXED:**

Fix for the bug when Nvidia driver is not installed if the user does not have
the Google Cloud Storage API enabled.

[ What-If Tool ( ` witwidget ` ) ](https://pair-code.github.io/what-if-tool/)
fixes for TensorFlow 1.14.

Miscellaneous bug fixes.

**AI Platform Notebooks**

**CHANGED:**

R upgraded to version 3.6.

R Notebooks are no longer dependent on a Conda environment.

##  July 01, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M28 release**

[ What-If Tool ( ` witwidget ` ) ](https://pair-code.github.io/what-if-tool/)
added to DLVM.

**FIXED:**

Fixed TensorFlow 1.14 issues.

Miscellaneous bug fixes.

##  June 24, 2019

**AI Platform Deep Learning Containers**

**FEATURE:**

AI Platform Deep Learning Containers is now available in beta. AI Platform
Deep Learning Containers lets you quickly prototype with a portable and
consistent environment for developing, testing, and deploying your AI
applications.

Visit the [ AI Platform Deep Learning Containers overview
](https://cloud.google.com/ai-platform/deep-learning-containers/docs/overview)
and the guide to [ getting started with a local deep learning container
](https://cloud.google.com/ai-platform/deep-learning-containers/docs/getting-
started-local) .

##  June 20, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M27.1 release updates**

TensorFlow upgraded to: 1.14.0.

TensorFlow 2.0 upgraded to: Beta 1.

**FIXED:**

Miscellaneous bug fixes.

##  June 19, 2019

**AI Platform Prediction**

**FEATURE:**

[ The ` asia-southeast1 ` (Singapore) region ](https://cloud.google.com/ai-
platform/prediction/docs/regions) is now available for batch prediction.

**AI Platform Training**

**FEATURE:**

[ The ` asia-southeast1 ` (Singapore) region ](https://cloud.google.com/ai-
platform/training/docs/regions) is now available for training. You can use [
P4 or T4 GPUs ](https://cloud.google.com/ai-
platform/training/docs/tensorflow/using-gpus) for training in the region. Read
about [ pricing for training in ` asia-southeast1 `
](https://cloud.google.com/ai-platform/training/pricing) , including pricing
for accelerators.

##  June 18, 2019

**AI Platform Training**

**FEATURE:**

[ Runtime version 1.13 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) now supports [ training with TPUs
](https://cloud.google.com/ai-platform/training/docs/using-tpus) using
TensorFlow 1.13.

**CHANGED:**

Support for training with TPUs in runtime version 1.11 [ ended on June 6, 2019
](https://cloud.google.com/tpu/docs/supported-versions) .

##  June 17, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M27 release**

New ML framework added: CNTK 2.7 from Microsoft.

New ML framework added: Caffe 1.0 BVLC from UC Berkeley.

Updated TensorFlow 2.0 Beta0.

**FIXED:**

Miscellaneous bug fixes.

##  June 12, 2019

**AI Platform Training**

**FEATURE:**

You can now view monitoring data for training jobs directly within the AI
Platform Training **Job Details** page in the Cloud Console. The following
charts are available:

  * CPU, GPU, and memory utilization, broken down by master, worker, and parameter servers. 
  * Network usage: the rate per second of bytes sent and received. 

Learn more about [ how to monitor resource utilization for your training jobs
](https://cloud.google.com/ai-platform/training/docs/monitor-
training#monitoring_resource_consumption) .

**FEATURE:**

There are new options for [ filtering jobs ](https://cloud.google.com/ai-
platform/training/docs/monitor-training#checking_job_status) within the AI
Platform Training **Jobs** page in the Cloud Console. You can filter jobs by
**Type** and by whether or not the job used HyperTune.

Learn more about [ how to filter your training jobs
](https://cloud.google.com/ai-platform/training/docs/monitor-
training#checking_job_status) .

**FEATURE:**

You can now [ view and sort hyperparameter tuning trials
](https://cloud.google.com/ai-platform/training/docs/monitor-
training#checking_job_status) within the AI Platform Training **Job Details**
page in the Cloud Console. If your training job uses hyperparameter tuning,
your **Job Details** page includes a **HyperTune trials** table, where you can
view metrics such as RMSE, learning rate, and training steps. You can also
access logs for each trial. This table makes it easier to compare individual
trials.

Learn more about [ how to view your hyperparameter tuning trials
](https://cloud.google.com/ai-platform/training/docs/monitor-
training#checking_job_status) .

##  June 05, 2019

**AI Platform Prediction**

**FEATURE:**

You can now [ specify a service account ](https://cloud.google.com/ai-
platform/prediction/docs/deploying-models#service-account) for your model
version to use when you deploy a custom prediction routine to AI Platform
Prediction. This feature is in beta.

##  June 03, 2019

**AI Platform Notebooks**

**FEATURE:**

You can now create AI Platform Notebooks instances with R and core R packages
installed. Learn [ how to install R dependencies
](https://cloud.google.com/ai-platform/notebooks/docs/dependencies) , and read
guides for [ using R with BigQuery in AI Platform Notebooks
](https://cloud.google.com/ai-platform/notebooks/docs/use-r-bigquery) and [
using R and Python in the same notebook ](https://cloud.google.com/ai-
platform/notebooks/docs/r-python-same-notebook) .

**AI Platform Training**

**FEATURE:**

You can now create AI Platform Notebooks instances with R and core R packages
installed. Learn [ how to install R dependencies
](https://cloud.google.com/ai-platform/training/docs/notebooks/dependencies) ,
and read guides for [ using R with BigQuery in AI Platform Notebooks
](https://cloud.google.com/ai-platform/training/docs/notebooks/use-r-bigquery)
and [ using R and Python in the same notebook ](https://cloud.google.com/ai-
platform/training/docs/notebooks/r-python-same-notebook) .

##  May 29, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M26 release**

RAPIDS updated to 0.7.

Faster driver installation time for common TensorFlow and PyTorch images.

You can now use Deep Learning VMs without a public IP address if you have
enabled Google Private Access.

**FIXED:**

Miscellaneous bug fixes.

##  May 03, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M25 release**

New image added: CUDA 10.1.

PyTorch upgraded to 1.1.0.

fastai upgraded to 1.0.52.

MXNet upgraded to 1.4.0 (and now based on CUDA 10.0 images).

Chainer upgraded to 5.4.0.

**AI Platform Prediction**

**CHANGED:**

AI Platform runtime version 1.12 now supports TensorFlow 1.12.2. View the [
runtime version list ](https://cloud.google.com/ai-
platform/prediction/docs/runtime-version-list) for the full list of packages
included in runtime version 1.12.

**AI Platform Training**

**FEATURE:**

T4 GPUs are now in beta for AI Platform Training. For more information, see
the guides to [ using GPUs ](https://cloud.google.com/ai-
platform/training/docs/tensorflow/using-gpus) , [ their regional availability
](https://cloud.google.com/ai-
platform/training/docs/tensorflow/regions#training_with_accelerators) , and [
their pricing ](https://cloud.google.com/ai-platform/training/pricing) .

**CHANGED:**

AI Platform runtime version 1.12 now supports TensorFlow 1.12.2. View the [
runtime version list ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) for the full list of packages
included in runtime version 1.12.

##  April 26, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M24 release**

We now support two authorization modes in the new release: single user mode
and service account mode3.

rpy2 is now pre-installed in the R image.

A plugin for editing metadata of cells is now pre-installed.

jupyterlab-celltags JupyterLab extension is now pre-installed.

**FIXED:**

Fixed bug with sudo (now you can use sudo from the JupyterLab terminal).

Downloading files from JupyterLab file browser is now working.

##  April 25, 2019

**AI Platform Prediction**

**FEATURE:**

AI Platform Prediction now supports [ custom prediction routines
](https://cloud.google.com/ai-platform/prediction/docs/custom-prediction-
routines) in beta. Custom prediction routines let you provide AI Platform
Prediction with custom code to use when it serves online predictions from your
deployed model. This can be useful for preprocessing prediction input,
postprocessing your model's predictions, and more.

Work through a tutorial on [ deploying a custom prediction routine with Keras
](https://cloud.google.com/ai-platform/prediction/docs/custom-prediction-
routine-keras) or one on [ deploying a custom prediction routine with scikit-
learn ](https://cloud.google.com/ai-platform/prediction/docs/custom-
prediction-routine-scikit-learn) .

**FEATURE:**

AI Platform Prediction now supports [ custom transformers for scikit-learn
pipelines ](https://cloud.google.com/ai-platform/prediction/docs/exporting-
for-prediction#custom-pipeline-code) in beta. This lets you provide AI
Platform Prediction with custom code to use during online prediction. Your
deployed scikit-learn pipeline uses this code when it serves predictions.

Work through a tutorial on [ training and deploying a custom scikit-learn
pipeline ](https://cloud.google.com/ai-platform/prediction/docs/custom-
pipeline) .

**FEATURE:**

AI Platform Prediction now supports [ logging of your prediction nodes' `
stderr ` and ` stdout ` streams ](https://cloud.google.com/ai-
platform/prediction/docs/online-
predict#requesting_logs_for_online_prediction_requests) to Stackdriver logging
during online prediction. Stream logging is in beta. You can enable this type
of logging in addition to—or in place of—the access logging that was already
available. It can be useful for understanding how your deployment handles
prediction requests.

##  April 10, 2019

**AI Platform Data Labeling Service**

**FEATURE:**

AI Platform Data Labeling Service Beta has been released.

##  March 15, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M22 release**

Tensorflow upgraded to version 1.13.

**FEATURE:**

[ Fairing ](https://github.com/kubeflow/fairing) now preinstalled.

**FEATURE:**

cookiecutter and seaborn now preinstalled.

**FIXED:**

More descriptive serial logs to help customers debug common issues.

**FIXED:**

Misc bug fixes.

**ISSUE:**

Due to incompatibilities between Tensorflow 1.13 (which requires Numpy 1.16.2
or greater) and the latest Intel optimized version of Numpy (which is 1.15) we
are not using the intel optimized versions of Numpy and Scipy for this
release.

##  March 01, 2019

**AI Platform Notebooks**

**FEATURE:**

[ AI Platform Notebooks ](https://cloud.google.com/ai-
platform/notebooks/docs/overview) is now available in beta. AI Platform
Notebooks enables you to create and manage virtual machine (VM) instances that
are pre-packaged with [ JupyterLab
](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)
and a suite of deep learning software.

Visit the [ AI Platform Notebooks overview ](https://cloud.google.com/ai-
platform/notebooks/docs/overview) and the [ guide to creating a new notebook
instance ](https://cloud.google.com/ai-platform/notebooks/docs/create-new) to
learn more.

##  February 21, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M20 release**

TensorFlow and Pytorch GPU images switch between CPU-only/GPU-enabled binaries
at startup depending on whether GPUs are attached.

**FIXED:**

SSH is not disabled during NVIDIA driver installation on GPU images.

**ISSUE:**

Due to incompatibilities between the latest kernel update (Debian 9.8) and
Docker, we have put a hold on the kernel updates for this release (that is, `
apt-mark hold linux-image-4.9.0-8-amd64 ` ). If you require the latest kernel,
you can run ` sudo apt-mark unhold linux-image-4.9.0-8-amd64 && sudo apt
upgrade ` , but we cannot guarantee that Docker or our direct JupyterLab link
from [ Marketplace
](https://console.cloud.google.com/marketplace/details/click-to-deploy-
images/deeplearning) will function correctly if you force the upgrade.

##  January 29, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M19 release**

New TensorFlow 2.0 (experimental) flavor is added.

New experimental ability to use Deep Learning VMs with special Web proxy,
instead of SSHing to the VM.

##  January 14, 2019

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M16 release**

New MXNet 1.3 (experimental) flavor is added.

##  December 19, 2018

**AI Platform Deep Learning VM Image**

**FEATURE:**

**General Availability**

Launched the new 1.0 version of AI Platform Deep Learning VM Image.

**FEATURE:**

**M15 release**

BigQuery magic plugin now preloaded all the time.

Jupyter SQL integration now pre-installed and SQL plugin now preloaded.

TensorFlow images now include bazel pre-installed.

Python Dataproc client now pre-installed on all our images.

**CHANGED:**

fastai updated to the latest version 1.0.38.

##  December 10, 2018

**AI Platform Deep Learning VM Image**

**FIXED:**

**M14 release**

Fixed bug that was resulting in a broken Git UI in some cases.

**FEATURE:**

Fast.Ai updated to 1.0.36.

##  December 05, 2018

**AI Platform Deep Learning VM Image**

**FIXED:**

**M13 release**

Integrates fix for speed regression in linear models when using TensorFlow
with Intel® MKL DNN.

**FEATURE:**

Adds Git-Jupyter integration.

##  November 20, 2018

**AI Platform Deep Learning VM Image**

**CHANGED:**

**M12 release**

Chainer is now upgraded to 5.0.0 (and CuPy to 5.0.0).

CuDNN updated to 7.4.

TensorRT5 updated to GA.

XGBoost updated to 0.81.

Images now have papermill pre-installed.

Ability to change Jupyter UI that is running on the port 8080, currently
supported: Lab and Notebook.

##  November 13, 2018

**AI Platform Deep Learning VM Image**

**FIXED:**

**M11.1 release**

Fixed an issue where users were locked out of ` apt ` after startup due to a
package needing configuration. If you are using an M11 image and are
experiencing issues with apt, please either recreate your VM or run ` sudo
dpkg --configure -a ` to clear the lock.

##  November 08, 2018

**AI Platform Deep Learning VM Image**

**CHANGED:**

**M11 release**

All GPU images install NVIDIA driver 410.72.

TensorFlow updated to v1.12.0.

PyTorch 0.4 image now uses conda for package management.

##  October 23, 2018

**AI Platform Deep Learning VM Image**

**CHANGED:**

**M10 release**

PyTorch 1.0 updated to the latest build as of October 23.

` fastai ` updated to 1.0.12.

` fastai ` course materials are now available at ` $HOME/tutorials/fastai/ ` .

Chainer UI updated to 0.6.0.

Chainer MN updated to 1.3.1.

**FIXED:**

Fixed a bug that was causing Intel packages to be overwritten.

##  October 10, 2018

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M9 release**

Intel Optimized Python packages are installed in all distributions:

  * NumPy 
  * SciPy 
  * ` scikit-learn `
  * TensorFlow (when applicable) 

PyTorch 1.0 (Experimental) images include support for `
[conda](https://conda.io/) ` and ` [fastai](http://fast.ai/) ` .

**CHANGED:**

Chainer updated from v4.4.0 to v4.5.0.

##  September 27, 2018

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M8 release**

New XGBoost images:

  * ` xgboost-<var>VERSION</var>-cu92-experimental `
  * ` xgboost-<var>VERSION</var>-cpu-experimental `

New CUDA 10.0 image (common-cu100) with the following NVIDIA stack in it:

  * CuDNN 7.3 
  * NCCL 2.3.4 
  * Driver 410.48 
  * TensorRT 5 

**CHANGED:**

TensorFlow updated from v1.10.1 to v1.11.0.

TensorFlow now compiled with CUDA 10.0 and CuDNN 7.3.

Common CUDA 9.2 image now has latest NCCL 2.3.4

Common CUDA 9.0 image now has:

  * latest NCCL 2.3.4 
  * latest CuDNN 7.3 
  * TensorRT 5.0.0 

Following packages are now pre-installed on the images:

  * ` htop `
  * ` protobuf-compiler `
  * ` tree `

After SSHing to the instance you now will see the exact revision of the image
in the header.

##  September 18, 2018

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M7.1 release**

Introducing new experimental images with PyTorch 1.0RC. New image families
are:

  * ` pytorch-1-0-cu92-experimental `
  * ` pytorch-1-0-cpu-experimental `

##  September 12, 2018

**AI Platform Deep Learning VM Image**

**CHANGED:**

**M7 release**

Chainer updated from v4.3.0 to v4.4.0.

Better integration with BigQuery.

Pillow has been replaced with the faster Pillow-SIMD package.

` minikube ` is now pre-installed.

New simplified image families introduced:

  * ` tf-latest-gpu `
  * ` pytorch-latest-gpu `
  * ` chainer-latest-gpu-experimental `

**FIXED:**

Jupyter now running on behalf of its own user (not root).

##  August 30, 2018

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M6 release**

Introducing experimental images: these images bring new frameworks for you to
try out, but they come with no guarantees of future support. Current
experimental images:

  * Chainer (4.3) 

**FEATURE:**

All images now have ` kubectl ` installed.

**CHANGED:**

TensorFlow updated from v1.10.0 to v1.10.1.

##  August 14, 2018

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M5 release**

All images now have Docker and/or NVIDIA Docker pre-installed.

TensorFlow and PyTorch images now include pre-baked tutorials.

GPU flavors of TensorFlow and PyTorch images now swap binaries to the CPU
optimized binaries during the first boot if the instance does not have a GPU.

##  July 31, 2018

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M4 release**

Includes Tensorfow Serving: model server binary at
/usr/local/bin/tensorflow_model_server and tensorflow-serving-api
preinstalled.

Integration with Colab: default JupyterLab instance can be connected as a
Colab backend.

Upgraded to support CUDA 9.2 (note this changes the pytorch family name).

**FIXED:**

Fixed an issue with CUDA linking in the build process, binaries up to 10%
faster now.

##  July 17, 2018

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M3 release**

New common image with CUDA 9.0 has been introduced.

**CHANGED:**

The following changes are included in this release:

  * All images now include [ OpenMPI ](https://www.open-mpi.org) . 
  * TensorFlow GPU images now include [ Horovod ](https://github.com/uber/horovod) . 
  * CUDA 9.2 stack now includes latest NCCL 2.2.13. 

**FIXED:**

Bug that was preventing Jupyter Notebook from working correctly has been
resolved.

##  July 11, 2018

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M2 release**

TensorFlow updated to version 1.9.0.

New public Google Group for users: [ google-dl-platform
](https://groups.google.com/forum/#!forum/google-dl-platform)

##  July 02, 2018

**AI Platform Deep Learning VM Image**

**FEATURE:**

**Beta launch**

AI Platform Deep Learning VM Image is available as a beta release.

