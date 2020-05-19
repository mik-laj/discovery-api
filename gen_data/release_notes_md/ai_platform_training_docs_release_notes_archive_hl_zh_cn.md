#  已归档的版本说明

您可以在 [ Google Cloud 版本说明 ](https://cloud.google.com/release-notes?hl=zh_cn)
页面上查看 Google Cloud 所有产品的最新产品动态。

2019 年 4 月 10 日，Cloud Machine Learning Engine 划分为 [ AI Platform Training
](https://cloud.google.com/ai-platform/training?hl=zh_cn) 和 [ AI Platform
Prediction ](https://cloud.google.com/ai-platform/prediction?hl=zh_cn) 。此页面记录了
Cloud ML Engine 的历史更新内容。

请参阅当前的版本说明：

  * [ AI Platform Training 版本说明 ](https://cloud.google.com/ai-platform/training/docs/release-notes?hl=zh_cn)
  * [ AI Platform Prediction 版本说明 ](https://cloud.google.com/ai-platform/prediction/docs/release-notes?hl=zh_cn)

##  2019 年 4 月 1 日

**FEATURE:**

Cloud ML Engine 现在针对训练、在线预测和批量预测提供折扣价格。

详细了解 [ Cloud ML Engine 价格 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=zh_cn) 。

##  2019 年 3 月 28 日

**FEATURE:**

Cloud ML Engine 现在提供了具有内置算法的训练。您可以提交数据以进行自动预处理，并在 TensorFlow [ 线性学习器
](https://www.tensorflow.org/tutorials/representation/linear?hl=zh_cn)
、TensorFlow [ 广度和深度 ](https://ai.googleblog.com/2016/06/wide-deep-learning-
better-together-with.html) 算法以及 [ XGBoost
](https://xgboost.readthedocs.io/en/latest/tutorials/model.html)
算法上训练模型，而无需编写任何代码。

详细了解 [ 使用内置算法进行训练 ](https://cloud.google.com/ai-
platform/training/docs/algorithms?hl=zh_cn) 。

##  2019 年 3 月 25 日

**CHANGED:**

Cloud ML Engine 运行时版本 1.13 现在支持 TensorFlow 1.13.1。 如需查看运行时版本 1.13
中包含的完整软件包列表，请参阅 [ 运行时版本列表 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=zh_cn) 。

##  2019 年 3 月 8 日

**FEATURE:**

我们已于 2019 年 3 月 8 日停止支持在 Cloud ML Engine 运行时版本 1.9 中使用 TPU
进行训练。如需了解目前支持的版本，请参阅 [ 运行时版本列表 ](https://cloud.google.com/ai-
platform/training/docs/tensorflow/runtime-version-list?hl=zh_cn#tpu-support) 。

##  2019 年 3 月 6 日

**FEATURE:**

Cloud ML Engine 运行时版本 1.13 现已推出，可用于训练和预测。此版本支持 TensorFlow 1.13，且包含 [ 运行时版本列表
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=zh_cn) 中列出的其他软件包。

目前，运行时版本 1.13 不支持使用 TPU 进行训练。

##  2019 年 3 月 1 日

**FEATURE:**

[ AI Platform Notebooks ](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=zh_cn) 现已发布 Beta 版。AI Platform
Notebooks 使您能够创建和管理预封装有 [ JupyterLab
](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)
的虚拟机 (VM) 实例和一套深度学习软件。

如需了解详情，请访问 [ AI Platform Notebooks 概览 ](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=zh_cn) 和 [ 创建新的笔记本实例的相关指南
](https://cloud.google.com/ai-platform/training/docs/notebooks/create-
new?hl=zh_cn) 。

##  2019 年 2 月 13 日

**FEATURE:**

Cloud TPU 现已推出，可用于训练 TensorFlow 模型。 张量处理单元 (TPU) 是 Google
定制开发的加速器，用于加速机器学习工作负载。

了解如何在 Cloud ML Engine 上 [ 使用 TPU 训练您的模型 ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-tpus?hl=zh_cn) ，并详细了解其 [ 价格
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=zh_cn) 。

##  2019 年 2 月 7 日

**FEATURE:**

使用自定义容器进行训练的功能现已发布 Beta 版。此功能允许您使用自定义 Docker 映像在 Cloud ML Engine
上运行训练应用。您可以使用自己偏好的机器学习框架构建自定义容器。如需开始使用，请参阅 [ 使用自定义容器训练 PyTorch 模型
](https://cloud.google.com/ai-platform/training/docs/custom-containers-
training?hl=zh_cn) 。

**FEATURE:**

您现在可以使用某些 Compute Engine 机器类型来配置训练作业。为训练作业分配计算资源时，这可提供更高的灵活性。此功能现已发布 Beta 版。

使用 Compute Engine 机器类型来配置作业时，可以挂接一组您指定的 GPU。

详细了解 [ Compute Engine 机器类型 ](https://cloud.google.com/ai-
platform/training/docs/machine-types?hl=zh_cn#compute-engine-machine-types) 、
[ GPU 挂接 ](https://cloud.google.com/ml-engine/docs/tensorflow/using-
gpus?hl=zh_cn#compute-engine-machine-types-with-gpu) 及其 [ 价格
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=zh_cn) 。

**FEATURE:**

P4 GPU 现已推出 Beta 版，可用于训练。如需了解详情，请参阅 [ 使用 GPU ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=zh_cn) 指南、 [ 其区域可用性
](https://cloud.google.com/ml-
engine/docs/tensorflow/regions?hl=zh_cn#training_with_accelerators) 指南以及 [ 其价格
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=zh_cn) 指南。

##  2019 年 2 月 1 日

**CHANGED:**

使用四核 CPU 进行在线预测的功能已推出 Beta 版。机器类型的名称已更改，并且价格也已更新。

  * 为 [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=zh_cn) 设置 ` machineType ` ，以指定用于提供服务的机器类型。对于四核 CPU，请使用 ` mls1-c4-m2 ` 。默认为单核 CPU ` mls1-c1-m2 ` 。 
  * Alpha 版中使用的以下机器名称 **已弃用** ： ` mls1-highmem-1 ` 和 ` mls1-highcpu-4 ` 。 
  * 如需了解详情，请参阅 [ 在线预测 ](https://cloud.google.com/ai-platform/training/docs/online-predict?hl=zh_cn#machine-types) 指南。 
  * 如需了解支持的机器类型，请参阅更新后的 [ 价格 ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=zh_cn) 。 

##  2019 年 1 月 25 日

**FEATURE:**

在线预测功能现已在 us-east4 区域发布。请参阅 [ 区域可用性 ](https://cloud.google.com/ai-
platform/training/docs/regions?hl=zh_cn) 指南。

##  2019 年 1 月 10 日

**FEATURE:**

V100 GPU 现已正式推出，可用于训练。如需了解详情，请参阅 [ 使用 GPU ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=zh_cn) 指南和 [ 价格
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=zh_cn) 指南。

##  2018 年 12 月 19 日

**FEATURE:**

Cloud ML Engine 运行时版本 1.11 和 1.12 现已推出，可用于训练和预测。这两个版本分别支持 TensorFlow 1.11 和
1.12，以及 [ 运行时版本列表 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=zh_cn) 中列出的其他软件包。

Cloud ML Engine 运行时版本 1.11 和 1.12 中新增了对 TPU 训练的支持。不支持 1.10 版。如需了解目前支持的版本，请参阅 [
运行时版本列表 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn#tpu-support) 。

**CHANGED:**

每个 Cloud ML Engine 运行时版本现在都包含 [ joblib
](https://joblib.readthedocs.io/en/latest/) 。包含 joblib 的最低运行时版本是 1.4 版。

##  2018 年 10 月 26 日

**CHANGED:**

我们已于 2018 年 10 月 26 日停止支持在 Cloud ML 运行时版本 1.8 中使用 TPU 进行训练。如需了解目前支持的版本，请参阅 [
运行时版本列表 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn#tpu-support) 。

##  2018 年 10 月 11 日

**ISSUE:**

由于 GPU 训练期间 [ CuDNN 版本不匹配导致的错误 ](https://stackoverflow.com/q/52733440) ，Cloud
ML Engine 运行时版本 1.11 已回滚。当前的折衷解决方法是使用运行时版本 1.10。如需了解详情，请参阅 [ 运行时版本列表
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=zh_cn) 。

##  2018 年 10 月 5 日

**FEATURE:**

Cloud ML Engine 运行时版本 1.11 现已推出，可用于训练和预测。此版本支持 TensorFlow 1.11 和 [ 运行时版本列表
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=zh_cn) 中列出的其他软件包。

##  2018 年 8 月 31 日

**FEATURE:**

Cloud ML Engine 运行时版本 1.10 现已推出，可用于训练和预测。此版本支持 TensorFlow 1.10 和 [ 运行时版本列表
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=zh_cn) 中列出的其他软件包。

##  2018 年 8 月 27 日

**FEATURE:**

V100 GPU 现已推出 Beta 版，可用于训练。使用 V100 GPU 现在会产生费用。 如需了解详情，请参阅 [ 使用 GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=zh_cn) 指南和
[ 价格 ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=zh_cn)
指南。

**FEATURE:**

P100 GPU 现已正式推出，可用于训练。如需了解详情，请参阅 [ 使用 GPU ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=zh_cn) 指南和 [ 价格
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=zh_cn) 指南。

**FEATURE:**

us-west1 和 europe-west4 这两个新区域现已推出，可用于训练。如需了解详情，请参阅 [ 区域
](https://cloud.google.com/ai-platform/training/docs/regions?hl=zh_cn) 页面。

##  2018 年 8 月 24 日

**CHANGED:**

我们已于 2018 年 8 月 24 日停止支持在 Cloud ML 运行时版本 1.7 中使用 TPU 进行训练。如需了解目前支持的版本，请参阅 [
运行时版本列表 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn#tpu-support) 。

##  2018 年 8 月 9 日

**CHANGED:**

我们很高兴地宣布，AI Platform Training 在线预测的价格已大幅降低。

请参阅下表以了解新旧价格：

区域  |  每小时每节点的价格（旧）  |  每小时每节点的价格（新）  
---|---|---  
美国  |  $0.30 USD  |  $0.056 USD  
欧洲  |  $0.348 USD  |  $0.061 USD  
亚太地区  |  $0.348 USD  |  $0.071 USD  
  
如需了解详情，请参阅 [ 价格指南 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=zh_cn) 。

##  2018 年 8 月 8 日

**CHANGED:**

我们很高兴地宣布推出 Cloud TPU 和 AI Platform Training 促销活动，大幅降低相关价格。

请参阅下表以了解新旧价格：

区域：美国  |  每小时每 TPU 的价格（旧）  |  每小时每 TPU 的价格（新）  
---|---|---  
容量层级： ` BASIC_TPU ` （Beta 版） __ |  $9.7674 USD  |  $6.8474 USD  
自定义机器类型： ` cloud_tpu ` （Beta 版） __ |  $9.4900 USD  |  $6.5700 USD  
  
请注意，该表仅显示了美国区域的价格。Cloud ML Engine 中 Cloud TPU 的可用性没有变化。如需了解详细信息，请参阅 [ 价格指南
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=zh_cn) 。

##  2018 年 8 月 6 日

**FEATURE:**

Cloud ML Engine 运行时版本 1.9 现已推出，可用于训练和预测。此版本支持 TensorFlow 1.9 和 [ 运行时版本列表
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn) 中列出的其他软件包。

##  2018 年 7 月 23 日

**FEATURE:**

Cloud ML Engine 现在支持使用 **scikit-learn** 和 **XGBoost** 进行训练。此功能已正式发布。请参阅 [ 在
Cloud ML Engine 上使用 scikit-learn 和 XGBoost 进行训练 ](https://cloud.google.com/ml-
engine/docs/scikit/getting-started-training?hl=zh_cn) 指南。

**FEATURE:**

现已正式发布对 **scikit-learn** 和 **XGBoost** 的在线预测支持。

  * 为 [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=zh_cn) 设置 ` framework ` ，以在创建模型版本时指定机器学习框架。有效值为 ` TENSORFLOW ` 、 ` SCIKIT_LEARN ` 和 ` XGBOOST ` 。默认值为 ` TENSORFLOW ` 。如果指定了 ` SCIKIT_LEARN ` 或 ` XGBOOST ` ，则还必须在模型版本中将 ` runtimeVersion ` 设置为 1.4 或更高版本。 
  * 请参阅 [ 使用 scikit-learn 和 XGBoost 进行本地训练和在线预测 ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=zh_cn) 指南。 

##  2018 年 7 月 12 日

**FEATURE:**

您可以为 AI Platform Training 资源（包括 [ 作业 ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=zh_cn) 、 [ 模型
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models?hl=zh_cn) 和 [ 模型版本
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=zh_cn)
）添加标签，然后使用这些标签对资源进行分类。此外，您也可以为 [ 操作 ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.operations?hl=zh_cn)
添加标签。在这种情况下，应根据操作所使用的资源来定义标签。请详细了解如何 [ 添加和使用标签 ](https://cloud.google.com/ml-
engine/docs/tensorflow/resource-labels?hl=zh_cn) 。

##  2018 年 6 月 26 日

**CHANGED:**

以下区域现已全面上线 Cloud ML Engine：

  * us-east1 
  * asia-northeast1 

请详细了解 [ 区域可用性 ](https://cloud.google.com/ai-
platform/training/docs/regions?hl=zh_cn) 。

##  2018 年 6 月 13 日

**CHANGED:**

我们已于 2018 年 6 月 13 日停止支持在 Cloud ML 运行时版本 1.6 中使用 TPU 进行训练。如需了解目前支持的版本，请参阅 [
运行时版本列表 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn#tpu-support) 。

##  2018 年 5 月 29 日

**CHANGED:**

您现在可以搭配使用 Cloud TPU（ __ Beta 版）、TensorFlow 1.8 和 Cloud ML Engine 运行时版本 1.8。

背景信息： __ 早在 5 月 14 日，Cloud ML Engine 运行时版本 1.6 和 1.7 就已提供 Cloud
TPU。虽然上周发布了运行时版本 1.8，但当时 Cloud TPU 还不能与 TensorFlow 1.8
一起使用。现在，我们正式支持这一组合。了解如何在 Cloud ML Engine 上 [ 使用 TPU 训练您的模型
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=zh_cn) 。

##  2018 年 5 月 16 日

**FEATURE:**

Cloud ML Engine 运行时版本 1.8 现已推出，可用于训练和预测。此版本支持 TensorFlow 1.8 和 [ 运行时版本列表
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn) 中列出的其他软件包。

##  2018 年 5 月 15 日

**FEATURE:**

您现在可以为现有模型版本更新 [ 自动扩缩 ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=zh_cn#autoscaling)
的最小节点数，以及在创建新版本时指定该属性。

##  2018 年 5 月 14 日

**FEATURE:**

Cloud ML Engine 现在提供用于训练 TensorFlow 模型的 Cloud TPU __ （Beta 版）。张量处理单元 (TPU) 是
Google 定制开发的 ASIC，用于加速机器学习工作负载。了解如何在 Cloud ML Engine 上 [ 使用 TPU 训练您的模型
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=zh_cn) 。

##  2018 年 4 月 26 日

**FEATURE:**

Cloud ML Engine 运行时版本 1.7 现已推出，可用于训练和预测。此版本支持 TensorFlow 1.7 和 [ 运行时版本列表
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn) 中列出的其他软件包。

##  2018 年 4 月 16 日

**FEATURE:**

**超参数算法** ：在训练作业中调节超参数时，您现在可以在 [ HyperparameterSpec
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=zh_cn#hyperparameterspec)
中指定搜索算法。可用的值包括：

  * ` GRID_SEARCH ` ：在可行空间内进行简单的网格搜索。如果您要指定的试验次数超过可行空间中的点数，则此选项特别有用。在这种情况下，如果您未指定网格搜索，则 Cloud ML Engine 默认算法可能会生成重复的建议。如需使用网格搜索，所有参数都必须是 ` INTEGER ` 、 ` CATEGORICAL ` 或 ` DISCRETE ` 类型。 
  * ` RANDOM_SEARCH ` ：在可行空间内执行的简单随机搜索。 

如果您未指定算法，则您的作业将使用默认的 Cloud ML Engine
算法，该算法可驱动参数搜索，从而通过在参数空间上进行更有效的搜索来获得最佳解决方案。如需了解超参数调节的更多信息，请参阅 [ 超参数调节概述
](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-tuning-
overview?hl=zh_cn) 。

##  2018 年 4 月 5 日

**FEATURE:**

Cloud ML Engine 现在支持使用 **scikit-learn** 和 **XGBoost** 进行在线预测。此功能目前处于 Beta 版阶段。
__

  * 为 [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=zh_cn) 设置 ` framework ` ，以在创建模型版本时指定机器学习框架。有效值为 ` TENSORFLOW ` 、 ` SCIKIT_LEARN ` 和 ` XGBOOST ` 。默认值为 ` TENSORFLOW ` 。如果指定了 ` SCIKIT_LEARN ` 或 ` XGBOOST ` ，则还必须在模型版本中将 ` runtimeVersion ` 设置为 1.4 或更高版本。 
  * 请参阅 [ 在 Cloud ML Engine 上使用 scikit-learn 和 XGBoost ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=zh_cn) 指南。 

**FEATURE:**

Python 3.5 现已推出，可用于在线预测。

  * 为 [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=zh_cn) 设置 ` pythonVersion ` ，以在创建模型版本时指定 Python 版本。默认值为 Python 2.7。 
  * 如需详细了解 Cloud ML Engine 中的所有可用软件包，请参阅 [ 运行时版本列表 ](https://cloud.google.com/ml-engine/docs/scikit/runtime-version-list?hl=zh_cn) 。 

##  2018 年 3 月 20 日

**FEATURE:**

Cloud ML Engine 运行时版本 1.6 现已推出，可用于训练和预测。此版本支持 TensorFlow 1.6 和 [ 运行时版本列表
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn) 中列出的其他软件包。

##  2018 年 3 月 13 日

**FEATURE:**

适用于 TensorFlow 1.5 的 Cloud ML Engine 运行时版本现已推出，可用于训练和预测。如需了解详情，请参阅 [ 运行时版本列表
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn) 。

##  2018 年 2 月 8 日

**FEATURE:**

新增多个超参数调节功能：自动提前停止测试、恢复先前的超参数调节作业，以及提高运行类似作业时的效率。如需了解详情，请参阅 [ 超参数调节概览
](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-tuning-
overview?hl=zh_cn) 。

##  2017 年 12 月 14 日

**FEATURE:**

适用于 TensorFlow 1.4 的 Cloud ML Engine 运行时版本现已推出，可用于训练和预测。如需了解详情，请参阅 [ 运行时版本列表
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn) 。

**FEATURE:**

适用于 TensorFlow 1.4 的 Cloud ML Engine 运行时版本中包含 Python 3，后者现在可用于训练。如需了解详情，请参阅 [
运行时版本列表 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn) 。

**FEATURE:**

单核 CPU 机器现在可使用在线预测功能。请参阅 [ 在线预测 ](https://cloud.google.com/ml-
engine/docs/tensorflow/online-predict?hl=zh_cn) 指南和 [ 博文
](https://cloud.google.com/blog/big-data/2017/12/bringing-cloud-ml-engine-to-
more-developers-with-online-prediction-features-and-reduced-prices?hl=zh_cn) 。

**FEATURE:**

我们简化了训练和预测作业的运行，并降低了相关费用。 请参阅 [ 价格详情 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=zh_cn) 、 [ 博文
](https://cloud.google.com/blog/big-data/2017/12/bringing-cloud-ml-engine-to-
more-developers-with-online-prediction-features-and-reduced-prices?hl=zh_cn)
以及 [ 价格常见问题解答 ](https://cloud.google.com/ml-engine/docs/tensorflow/pricing-
faq?hl=zh_cn) 中的新旧价格对比。

**FEATURE:**

P100 GPU 现已推出 Beta 版。使用 P100 GPU 现在会产生费用。 如需了解详情，请参阅 [ 使用 GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=zh_cn) 和 [
价格 ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=zh_cn) 。

##  2017 年 10 月 26 日

**FEATURE:**

适用于 Cloud ML Engine 的审核日志现在处于 Beta 版阶段。 如需了解详情，请参阅 [ 查看审核日志
](https://cloud.google.com/ml-engine/docs/tensorflow/audit-logs?hl=zh_cn) 。

##  2017 年 9 月 25 日

**FEATURE:**

适用于 Cloud ML Engine 的预定义 IAM 角色现已正式发布。如需了解详情，请参阅 [ 访问权限控制
](https://cloud.google.com/ml-engine/docs/tensorflow/access-control?hl=zh_cn)
。

##  2017 年 6 月 27 日

**FEATURE:**

适用于 TensorFlow 1.2 的 Cloud ML Engine 运行时版本现已推出，可用于训练和预测。如需了解详情，请参阅 [ 运行时版本列表
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn) 。

**DEPRECATED:**

Cloud ML Engine 不再支持适用于 TensorFlow 0.11 和 0.12 的旧运行时版本。如需了解详情，请参阅 [ 运行时版本列表
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn) 和 [ 旧运行时版本的支持时间表 ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=zh_cn#runtime-version-support)
。

##  2017 年 5 月 9 日

**FEATURE:**

我们很高兴地宣布正式发布支持 GPU 的机器。 如需了解详情，请参阅 [ 在云端使用 GPU 训练模型
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=zh_cn) 。

##  2017 年 4 月 27 日

**FEATURE:**

GPU 现已在 us-central1 区域发布。如需查看支持 GPU 的区域的完整列表，请参阅 [ 在云端使用 GPU 训练模型
](https://cloud.google.com/ml-engine/docs/tensorflow/using-
gpus?hl=zh_cn#requesting_gpu-enabled_machines) 。

##  v1（2017 年 3 月 8 日）

**FEATURE:**

AI Platform Training 正式版发布。用户可使用 Cloud ML Engine 版本 1 训练模型、部署模型和生成批量预测结果。 [
超参数调节 ](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-
tuning-overview?hl=zh_cn) 功能也已正式发布，但在线预测功能和 [ 支持 GPU 的机器
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=zh_cn) 仍处于
Beta 版阶段。

**FEATURE:**

在线预测功能现在处于 Beta 版 [ 发布阶段 ](https://cloud.google.com/terms/launch-
stages?hl=zh_cn) 。该功能现在受 Cloud ML Engine [ 价格政策 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=zh_cn) 的约束，并采用与批量预测功能相同的价格公式。虽然已处于 Beta
版阶段，但在线预测功能不适合在关键应用中使用。

**CHANGED:**

Cloud ML Engine [ 运行时版本 ](https://cloud.google.com/ml-
engine/docs/tensorflow/versioning?hl=zh_cn)
定义了其训练模型和获取预测结果的环境。您可以指定在训练和定义模型资源或请求批量预测结果时使用的受支持的运行时版本。此时运行时版本的主要区别在于每个版本支持的
TensorFlow 版本不同，但随着时间的推移可能会出现更多差异。如需了解详情，请参阅 [ 运行时版本列表
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=zh_cn) 。

**CHANGED:**

您现在可以针对存储在 Google Cloud Storage（而不是作为模型版本托管在 Cloud ML Engine）中的 TensorFlow
SavedModel 运行批量预测作业。您可以使用 SavedModel 的 URI，而不是在创建作业时提供模型或版本 ID。

**DEPRECATED:**

以前发布的 Alpha 版 Google Cloud Machine Learning SDK 已弃用，从 2017 年 5 月 7
日起将不再受支持。SDK 提供的大多数功能都已迁移至新的 TensorFlow 软件包 [ tf.Transform
](https://github.com/tensorflow/transform)
。您可以使用您喜欢的任何技术或工具来预处理输入数据。但是，我们建议您使用 ` tf.Transform ` 以及 Google Cloud Platform
提供的服务，包括 Google Cloud Dataflow、Google Cloud Dataproc、Google BigQuery。

##  v1beta1（2016 年 9 月 29 日）

**FEATURE:**

在线预测是一个 Alpha 版功能。虽然 AI Platform Training 整体处于 Beta 版阶段，但在线预测仍在进行重大更改以改善性能。使用
Alpha 版在线预测功能不会产生 [ 费用 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=zh_cn) 。

**FEATURE:**

预处理功能和 Cloud ML Engine SDK 的其余功能都是 Alpha 版功能。我们还在积极开发该 SDK，以便更紧密地将 Cloud ML
Engine 与 Apache Beam 集成。

