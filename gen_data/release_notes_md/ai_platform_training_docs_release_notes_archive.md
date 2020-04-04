#  Archived release notes

On April 10, 2019, Cloud Machine Learning Engine became [ AI Platform Training
](/ai-platform/training) and [ AI Platform Prediction ](/ai-
platform/prediction) . This page documents historical updates to Cloud ML
Engine.

See the current release notes:

  * [ AI Platform Training release notes ](/ai-platform/training/docs/release-notes)
  * [ AI Platform Prediction release notes ](/ai-platform/prediction/docs/release-notes)

##  April 1, 2019

**FEATURE:**

Cloud ML Engine now offers reduced pricing for training, online prediction and
batch prediction.

Learn more about [ Cloud ML Engine pricing ](/ai-
platform/training/docs/pricing) .

##  March 28, 2019

**FEATURE:**

Cloud ML Engine now offers training with built-in algorithms. You can submit
your data for automatic preprocessing, and train a model on the TensorFlow [
linear learner ](https://www.tensorflow.org/tutorials/representation/linear) ,
TensorFlow [ wide and deep ](https://ai.googleblog.com/2016/06/wide-deep-
learning-better-together-with.html) , and [ XGBoost
](https://xgboost.readthedocs.io/en/latest/tutorials/model.html) algorithms
without writing any code.

Learn more about [ training with built-in algorithms ](/ai-
platform/training/docs/algorithms) .

##  March 25, 2019

**CHANGED:**

Cloud ML Engine runtime version 1.13 now supports TensorFlow 1.13.1. View the
[ runtime version list ](/ai-platform/training/docs/runtime-version-list) for
the full list of packages included in runtime version 1.13.

##  March 8, 2019

**FEATURE:**

Support for training with TPUs in Cloud ML Engine runtime version 1.9 ended on
March 8, 2019. See the currently supported versions in the [ runtime version
list ](/ai-platform/training/docs/tensorflow/runtime-version-list#tpu-support)
.

##  March 6, 2019

**FEATURE:**

Cloud ML Engine runtime version 1.13 is now available for training and
prediction. This version supports TensorFlow 1.13 and includes other packages
as listed in the [ runtime version list ](/ai-platform/training/docs/runtime-
version-list) .

Training with TPUs is not supported in runtime version 1.13 at this time.

##  March 1, 2019

**FEATURE:**

[ AI Platform Notebooks ](/ai-platform/training/docs/notebooks/overview) is
now available in beta. AI Platform Notebooks enables you to create and manage
virtual machine (VM) instances that are pre-packaged with [ JupyterLab
](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)
and a suite of deep learning software.

Visit the [ AI Platform Notebooks overview ](/ai-
platform/training/docs/notebooks/overview) and the [ guide to creating a new
notebook instance ](/ai-platform/training/docs/notebooks/create-new) to learn
more.

##  February 13, 2019

**FEATURE:**

Cloud TPU is now generally available for training TensorFlow models. Tensor
Processing Units (TPUs) are Google's custom-developed accelerators for
machine-learning workloads.

See how to [ use TPUs to train your models ](/ml-engine/docs/tensorflow/using-
tpus) on Cloud ML Engine, and read more about [ their pricing ](/ai-
platform/training/docs/pricing) .

##  February 7, 2019

**FEATURE:**

Training with custom containers is now available in Beta. This feature allows
you to run your training application on Cloud ML Engine using a custom Docker
image. You can build your custom container with the ML frameworks of your
choice. Get started with [ training a PyTorch model by using custom containers
](/ai-platform/training/docs/custom-containers-training) .

**FEATURE:**

You can now configure training jobs with certain Compute Engine machine types.
This provides additional flexibility for allocating computing resources to
your training jobs. This feature is available in Beta.

When you configure your job with Compute Engine machine types, you may attach
a custom set of GPUs.

Read more about [ Compute Engine machine types ](/ai-
platform/training/docs/machine-types#compute-engine-machine-types) , [ GPU
attachments ](/ml-engine/docs/tensorflow/using-gpus#compute-engine-machine-
types-with-gpu) , and [ their pricing ](/ai-platform/training/docs/pricing) .

**FEATURE:**

P4 GPUs are now in Beta for training. For more information, see the guides to
[ using GPUs ](/ml-engine/docs/tensorflow/using-gpus) , [ their regional
availability ](/ml-engine/docs/tensorflow/regions#training_with_accelerators)
, and [ their pricing ](/ai-platform/training/docs/pricing) .

##  February 1, 2019

**CHANGED:**

Quad core CPUs are now available in Beta for online prediction. The names of
the machine types are changed, and pricing is updated.

  * Set ` machineType ` on [ ` projects.models.versions.create ` ](/ai-platform/training/docs/reference/rest/v1/projects.models.versions) to specify the machine type to use for serving. Use ` mls1-c4-m2 ` for quad core CPUs. The default is the single core CPU, ` mls1-c1-m2 ` . 
  * The following machine names used in Alpha are **deprecated** : ` mls1-highmem-1 ` and ` mls1-highcpu-4 ` . 
  * For more information, see the guide to [ online prediction ](/ai-platform/training/docs/online-predict#machine-types) . 
  * See the updated [ pricing ](/ai-platform/training/docs/pricing) for serving machine types. 

##  January 25, 2019

**FEATURE:**

Online prediction is now available in the us-east4 region. See the guide to [
region availability ](/ai-platform/training/docs/regions) .

##  January 10, 2019

**FEATURE:**

V100 GPUs are now generally available for training. For more information, see
the guides to [ using GPUs ](/ml-engine/docs/tensorflow/using-gpus) and [
pricing ](/ai-platform/training/docs/pricing) .

##  December 19, 2018

**FEATURE:**

The Cloud ML Engine runtime versions 1.11 and 1.12 are now available for
training and prediction. These versions support TensorFlow 1.11 and 1.12
respectively, and other packages as listed in the [ runtime version list
](/ai-platform/training/docs/runtime-version-list) .

TPU training support has been added for Cloud ML Engine runtime versions 1.11
and 1.12. Version 1.10 is not supported. See the currently supported versions
in the [ runtime version list ](/ml-engine/docs/tensorflow/runtime-version-
list#tpu-support) .

**CHANGED:**

Each Cloud ML Engine runtime version now includes [ joblib
](https://joblib.readthedocs.io/en/latest/) . The earliest runtime version
that includes joblib is version 1.4.

##  October 26, 2018

**CHANGED:**

TPU training support for Cloud ML runtime version 1.8 ended on Oct 26, 2018\.
See the currently supported versions in the [ runtime version list ](/ml-
engine/docs/tensorflow/runtime-version-list#tpu-support) .

##  October 11, 2018

**ISSUE:**

The Cloud ML Engine runtime version 1.11 is rolled back due to [ errors caused
by a CuDNN version mismatch ](https://stackoverflow.com/q/52733440) during GPU
training. The current workaround is to use runtime version 1.10. For more
details, see the [ runtime version list ](/ai-platform/training/docs/runtime-
version-list) .

##  October 5, 2018

**FEATURE:**

The Cloud ML Engine runtime version 1.11 is now available for training and
prediction. This version supports TensorFlow 1.11 and other packages as listed
in the [ runtime version list ](/ai-platform/training/docs/runtime-version-
list) .

##  August 31, 2018

**FEATURE:**

The Cloud ML Engine runtime version 1.10 is now available for training and
prediction. This version supports TensorFlow 1.10 and other packages as listed
in the [ runtime version list ](/ai-platform/training/docs/runtime-version-
list) .

##  August 27, 2018

**FEATURE:**

V100 GPUs are now in Beta for training. Using V100 GPUs now incurs charges.
For more information, see the guides to [ using GPUs ](/ml-
engine/docs/tensorflow/using-gpus) and [ pricing ](/ai-
platform/training/docs/pricing) .

**FEATURE:**

P100 GPUs are now generally available for training. For more information, see
the guides to [ using GPUs ](/ml-engine/docs/tensorflow/using-gpus) and [
pricing ](/ai-platform/training/docs/pricing) .

**FEATURE:**

Two new regions: us-west1, europe-west4 are now available for training. See [
regions ](/ai-platform/training/docs/regions) page for info.

##  August 24, 2018

**CHANGED:**

TPU training support for Cloud ML runtime version 1.7 ended on Aug 24, 2018\.
See the currently supported versions in the [ runtime version list ](/ml-
engine/docs/tensorflow/runtime-version-list#tpu-support) .

##  August 9th, 2018

**CHANGED:**

We're delighted to announce significant price reductions for online prediction
with AI Platform Training.

The following table shows the previous pricing and the new pricing:

Region  |  Previous price per node per hour  |  New price per node per hour  
---|---|---  
US  |  $0.30 USD  |  $0.056 USD  
Europe  |  $0.348 USD  |  $0.061 USD  
Asia Pacific  |  $0.348 USD  |  $0.071 USD  
  
See the [ pricing guide ](/ai-platform/training/docs/pricing) for details.

##  August 8th, 2018

**CHANGED:**

We're delighted to announce promotional pricing for Cloud TPU with AI Platform
Training, resulting in significant price reductions.

The following table shows the previous pricing and the new pricing:

Region: US  |  Previous price per TPU per hour  |  New price per TPU per hour  
---|---|---  
Scale tier: ` BASIC_TPU ` _(Beta)_ |  $9.7674 USD  |  $6.8474 USD  
Custom machine type: ` cloud_tpu ` _(Beta)_ |  $9.4900 USD  |  $6.5700 USD  
  
Note that the table shows pricing in the US region only. There is no change in
Cloud TPU availability on Cloud ML Engine. See the [ pricing guide ](/ai-
platform/training/docs/pricing) for details.

##  August 6, 2018

**FEATURE:**

The Cloud ML Engine runtime version 1.9 is now available for training and
prediction. This version supports TensorFlow 1.9 and other packages as listed
in the [ runtime version list ](/ml-engine/docs/tensorflow/runtime-version-
list) .

##  July 23, 2018

**FEATURE:**

Cloud ML Engine now supports **scikit-learn** and **XGBoost** for training.
This feature is generally available. See the guide to [ training with scikit-
learn and XGBoost on Cloud ML Engine ](/ml-engine/docs/scikit/getting-started-
training) .

**FEATURE:**

Online prediction support for **scikit-learn** and **XGBoost** is now
generally available.

  * Set ` framework ` on [ ` projects.models.versions.create ` ](/ai-platform/training/docs/reference/rest/v1/projects.models.versions) to specify your machine learning framework when creating a model version. Valid values are ` TENSORFLOW ` , ` SCIKIT_LEARN ` , and ` XGBOOST ` . The default is ` TENSORFLOW ` . If you specify ` SCIKIT_LEARN ` or ` XGBOOST ` , you must also set ` runtimeVersion ` to 1.4 or greater on the model version. 
  * See the guide to [ local training and online predictions with scikit-learn and XGBoost ](/ml-engine/docs/scikit/quickstart) . 

##  July 12, 2018

**FEATURE:**

You can add labels to your AI Platform Training resources— [ jobs ](/ai-
platform/training/docs/reference/rest/v1/projects.jobs) , [ models ](/ai-
platform/training/docs/reference/rest/v1/projects.models) , and [ model
versions ](/ai-
platform/training/docs/reference/rest/v1/projects.models.versions) —then use
those labels to organize the resources into categories. Labels are also
available on [ operations ](/ai-
platform/training/docs/reference/rest/v1/projects.operations) —in this case
the labels are derived from the resource to which the operation applies. Read
more about [ adding and using labels ](/ml-engine/docs/tensorflow/resource-
labels) .

##  June 26, 2018

**CHANGED:**

The following additional regions are now fully available:

  * us-east1 
  * asia-northeast1 

See more details about [ region availability ](/ai-
platform/training/docs/regions) .

##  June 13, 2018

**CHANGED:**

TPU training support for Cloud ML runtime version 1.6 ended on June 13, 2018\.
See the currently supported versions in the [ Runtime Version List ](/ml-
engine/docs/tensorflow/runtime-version-list#tpu-support) .

##  May 29, 2018

**CHANGED:**

You can now use Cloud TPU ( _Beta_ ) with TensorFlow 1.8 and Cloud ML Engine
runtime version 1.8.

_Background information:_ Cloud TPU became available in Cloud ML Engine on May
14th in runtime versions 1.6 and 1.7. Last week saw the release of runtime
version 1.8, but at that time Cloud TPU was not yet available with TensorFlow
1.8. Now it is. See how to [ use TPUs to train your models ](/ml-
engine/docs/tensorflow/using-tpus) on Cloud ML Engine.

##  May 16, 2018

**FEATURE:**

The Cloud ML Engine runtime version 1.8 is now available for training and
prediction. This version supports TensorFlow 1.8 and other packages as listed
in the [ runtime version list ](/ml-engine/docs/tensorflow/runtime-version-
list) .

##  May 15, 2018

**FEATURE:**

You can now update the minimum number of nodes for [ autoscaling ](/ai-
platform/training/docs/reference/rest/v1/projects.models.versions#autoscaling)
on an existing model version, as well as specifying the attribute when
creating a new version.

##  May 14, 2018

**FEATURE:**

Cloud ML Engine now offers Cloud TPU _(Beta)_ for training TensorFlow models.
Tensor Processing Units (TPUs) are Google's custom-developed ASICs, used to
accelerate machine-learning workloads. See how to [ use TPUs to train your
models ](/ml-engine/docs/tensorflow/using-tpus) on Cloud ML Engine.

##  April 26, 2018

**FEATURE:**

The Cloud ML Engine runtime version 1.7 is now available for training and
prediction. This version supports TensorFlow 1.7 and other packages as listed
in the [ runtime version list ](/ml-engine/docs/tensorflow/runtime-version-
list) .

##  April 16, 2018

**FEATURE:**

**Hyperparameter algorithms:** When tuning the hyperparameters in your
training job, you can now specify a search algorithm in the [
HyperparameterSpec ](/ai-
platform/training/docs/reference/rest/v1/projects.jobs#hyperparameterspec) .
Available values are:

  * ` GRID_SEARCH ` : A simple grid search within the feasible space. This option is particularly useful if you want to specify a number of trials that is more than the number of points in the feasible space. In such cases, if you do not specify a grid search, the Cloud ML Engine default algorithm may generate duplicate suggestions. To use grid search, all parameters must be of type ` INTEGER ` , ` CATEGORICAL ` , or ` DISCRETE ` . 
  * ` RANDOM_SEARCH ` : A simple random search within the feasible space. 

If you do not specify an algorithm, your job uses the default Cloud ML Engine
algorithm, which drives the parameter search to arrive at the optimal solution
with a more effective search over the parameter space. For more about
hyperparameter tuning, see the [ hyperparameter tuning overview ](/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview) .

##  April 5, 2018

**FEATURE:**

Cloud ML Engine now supports **scikit-learn** and **XGBoost** for online
prediction. This feature is in _Beta_ .

  * Set ` framework ` on [ ` projects.models.versions.create ` ](/ai-platform/training/docs/reference/rest/v1/projects.models.versions) to specify your machine learning framework when creating a model version. Valid values are ` TENSORFLOW ` , ` SCIKIT_LEARN ` , and ` XGBOOST ` . The default is ` TENSORFLOW ` . If you specify ` SCIKIT_LEARN ` or ` XGBOOST ` , you must also set ` runtimeVersion ` to 1.4 or greater on the model version. 
  * See the guide to [ scikit-learn and XGBoost on Cloud ML Engine ](/ml-engine/docs/scikit/quickstart) . 

**FEATURE:**

Python 3.5 is available for online prediction.

  * Set ` pythonVersion ` on [ ` projects.models.versions.create ` ](/ai-platform/training/docs/reference/rest/v1/projects.models.versions) to specify your version of Python when creating a model version. The default is Python 2.7. 
  * For details of all available packages in Cloud ML Engine, see the [ runtime version list ](/ml-engine/docs/scikit/runtime-version-list) . 

##  March 20, 2018

**FEATURE:**

The Cloud ML Engine runtime version 1.6 is now available for training and
prediction. This version supports TensorFlow 1.6 and other packages as listed
in the [ runtime version list ](/ml-engine/docs/tensorflow/runtime-version-
list) .

##  March 13, 2018

**FEATURE:**

The Cloud ML Engine runtime version for TensorFlow 1.5 is now available for
training and prediction. For more information, see the [ Runtime Version List
](/ml-engine/docs/tensorflow/runtime-version-list) .

##  February 8, 2018

**FEATURE:**

Added new features for hyperparameter tuning: automated early stopping of
trials, resuming a previous hyperparameter tuning job, and additional
efficiency optimizations when you run similar jobs. For more information, See
the [ hyperparameter tuning overview ](/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview) .

##  December 14, 2017

**FEATURE:**

The Cloud ML Engine runtime version for TensorFlow 1.4 is now available for
training and prediction. For more information, see the [ Runtime Version List
](/ml-engine/docs/tensorflow/runtime-version-list) .

**FEATURE:**

Python 3 is now available for training as part of the Cloud ML Engine runtime
version for TensorFlow 1.4. For more information, see the [ Runtime Version
List ](/ml-engine/docs/tensorflow/runtime-version-list) .

**FEATURE:**

Online prediction is now generally available for single core serving. See the
guide to [ online prediction ](/ml-engine/docs/tensorflow/online-predict) and
the [ blog post ](https://cloud.google.com/blog/big-data/2017/12/bringing-
cloud-ml-engine-to-more-developers-with-online-prediction-features-and-
reduced-prices) .

**FEATURE:**

Pricing has been reduced and simplified for both training and prediction. See
the [ pricing details ](/ai-platform/training/docs/pricing) , the [ blog post
](https://cloud.google.com/blog/big-data/2017/12/bringing-cloud-ml-engine-to-
more-developers-with-online-prediction-features-and-reduced-prices) , and the
comparison of old and current prices in the [ pricing FAQ ](/ml-
engine/docs/tensorflow/pricing-faq) .

**FEATURE:**

P100 GPUs are now in Beta. Using P100 GPUs now incurs charges. For more
information, see [ Using GPUs ](/ml-engine/docs/tensorflow/using-gpus) and [
Pricing ](/ai-platform/training/docs/pricing) .

##  October 26, 2017

**FEATURE:**

Audit logging for Cloud ML Engine is now in Beta. For more information, see [
Viewing Audit Logs ](/ml-engine/docs/tensorflow/audit-logs) .

##  September 25, 2017

**FEATURE:**

Predefined IAM roles for Cloud ML Engine are available for general use. For
more information, see [ Access Control ](/ml-engine/docs/tensorflow/access-
control) .

##  June 27, 2017

**FEATURE:**

The Cloud ML Engine runtime version for TensorFlow 1.2 is now available for
training and prediction. For more information, see the [ Runtime Version List
](/ml-engine/docs/tensorflow/runtime-version-list) .

**DEPRECATED:**

The older runtime versions with TensorFlow 0.11 and 0.12 are no longer
supported on Cloud ML Engine. For more information, see the [ Runtime Version
List ](/ml-engine/docs/tensorflow/runtime-version-list) and the [ support
timelines for older runtime versions ](/ml-engine/docs/tensorflow/runtime-
version-list#runtime-version-support) .

##  May 9, 2017

**FEATURE:**

Announced general availability of GPU-enabled machines. For more information,
see [ Using GPUs for Training Models in the Cloud ](/ml-
engine/docs/tensorflow/using-gpus) .

##  April 27, 2017

**FEATURE:**

GPUs are now available in the us-central1 region. For the full list of regions
that support GPUs, see [ Using GPUs for Training Models in the Cloud ](/ml-
engine/docs/tensorflow/using-gpus#requesting_gpu-enabled_machines) .

##  v1 (March 8th, 2017)

**FEATURE:**

Announced general availability of AI Platform Training. Version 1 of Cloud ML
Engine is available for general use for training models, deploying models, and
generating batch predictions. The [ hyperparameter tuning ](/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview) feature is also
available for general use, but online prediction and [ GPU-enabled machines
](/ml-engine/docs/tensorflow/using-gpus) remain in beta.

**FEATURE:**

Online prediction is now in the Beta [ launch stage ](/terms/launch-stages) .
Its use is now subject to the Cloud ML Engine [ pricing policy ](/ai-
platform/training/docs/pricing) , and follows the same pricing formula as
batch prediction. While it remains in Beta, online prediction is not intended
for use in critical applications.

**CHANGED:**

The environments that Cloud ML Engine uses to train models and get predictions
have been defined as Cloud ML Engine [ runtime versions ](/ml-
engine/docs/tensorflow/versioning) . You can specify a supported runtime
version to use when training, defining a model resource, or requesting batch
predictions. The primary difference in runtime versions at this time is the
version of TensorFlow supported by each, but more differences may arise over
time. You can find the details in the [ runtime version list ](/ml-
engine/docs/tensorflow/runtime-version-list) .

**CHANGED:**

You can now run batch prediction jobs against TensorFlow SavedModels that are
stored in Google Cloud Storage, not hosted as a model version in Cloud ML
Engine. Instead of supplying a model or version ID when you create your job,
you can use the URI of your SavedModel.

**DEPRECATED:**

The Google Cloud Machine Learning SDK, formerly released as Alpha, is
deprecated, and will no longer be supported effective May 7, 2017. Most of the
functionality exposed by the SDK has moved to the new TensorFlow package, [
tf.Transform ](https://github.com/tensorflow/transform) . You can use whatever
technology or tool you like to preprocess your input data. However, we
recommend ` tf.Transform ` as well as services that are available on Google
Cloud Platform, including Google Cloud Dataflow, Google Cloud Dataproc, and
Google BigQuery.

##  v1beta1 (September 29th, 2016)

**FEATURE:**

Online prediction is an Alpha feature. Though AI Platform Training overall is
in its Beta phase, online prediction is still undergoing significant changes
to improve performance. You will not be [ charged ](/ai-
platform/training/docs/pricing) for online prediction while it remains in
Alpha.

**FEATURE:**

Preprocessing and the rest of the Cloud ML Engine SDK are Alpha features. The
SDK is undergoing active development to better integrate Cloud ML Engine with
Apache Beam.

