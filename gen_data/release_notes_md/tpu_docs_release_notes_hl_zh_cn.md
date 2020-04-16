#  版本说明

此页面记录 Cloud TPU 的正式版更新。您可以定期查看此页面，了解有关新功能或更新功能、问题修复、已知问题和弃用功能的公告。

如需接收最新产品动态，请将此页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 。

##  2019 年 5 月 7 日

**FEATURE:**

Cloud TPU v2 Pod 现已发布测试版。

由于 TPU 资源可以从单个 Cloud TPU 扩容到 Cloud TPU Pod，因此您并不需要在单个 Cloud TPU 与 Cloud TPU
Pod 之间做出选择。您可以通过核心切片或核心集的形式请求部分 Cloud TPU Pod，这样就可以只购买所需的处理能力 __ 。

[ Cloud TPU Pod（测试版）优于单个 Cloud TPU v2 设备：
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=zh_cn)

  * 在研发中提升训练速度，实现快速迭代 
  * 提供可自动扩容的机器学习 (ML) 计算，进而提高用户工作效率 
  * 能够训练更大的模型 

**FEATURE:**

Cloud TPU v3 Pod 现已发布测试版。

由于 TPU 资源可以从单个 Cloud TPU 扩容到 Cloud TPU Pod，因此您并不需要在单个 Cloud TPU 与 Cloud TPU
Pod 之间做出选择。您可以通过核心切片或核心集的形式请求部分 Cloud TPU Pod，这样就可以只购买所需的处理能力 __ 。

[ Cloud TPU Pod（测试版）优于单个 v3 Cloud TPU 设备：
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=zh_cn)

  * 在研发中提升训练速度，实现快速迭代 
  * 提供可自动扩容的机器学习 (ML) 计算，进而提高用户工作效率 
  * 能够训练更大的模型 

Cloud TPU v3 Pod（测试版）优于 Cloud TPU v2 Pod（测试版） __ __ ：

* 处理速度更快，内存更大： 

  * v2 Pod：每秒 11.5 千万亿次浮点运算，4 TB 片上存储器 (HBM) 
  * v3 Pod：每秒 100 千万亿次浮点运算，32 TB HBM，液体冷却 

* 能够训练更大的模型 

##  2019 年 3 月 11 日

**CHANGED:**

Cloud TPU 现在支持 [ TensorFlow 1.13 版本
](https://www.tensorflow.org/versions/r1.13/api_docs/?hl=zh_cn) 。我们不再支持
Tensorflow 1.8 和 1.9 版本。

请参阅 [ Cloud TPU 版本控制政策 ](https://cloud.google.com/tpu/docs/supported-
versions?hl=zh_cn) 中当前支持的 TensorFlow 版本。

##  2019 年 1 月 31 日

**FEATURE:**

Cloud TPU v3 现已公开发布 (GA)。Cloud TPU v3 的内存是 v2 的两倍，不仅提升了性能，而且能够支持更多类型的模型，例如更深的
ResNet 和使用 RetinaNet 的较大图片。在 Cloud TPU v2 上运行的现有模型仍可继续使用。请参阅 [ Cloud TPU 版本指南
](https://cloud.google.com/tpu/docs/deciding-tpu-version?hl=zh_cn) ，了解更多详情。

##  2018 年 11 月 8 日

**CHANGED:**

Cloud TPU 现支持 [ TensorFlow 1.12 版本
](https://www.tensorflow.org/versions/r1.12/api_docs/?hl=zh_cn) 。此版本改进了 Cloud
TPU 上的 Keras，优化了整个软件堆栈的性能，并改善了 API、错误消息和可靠性。

请参阅 [ Cloud TPU 版本控制政策 ](https://cloud.google.com/tpu/docs/supported-
versions?hl=zh_cn) 中当前支持的 TensorFlow 版本。

##  2018 年 11 月 7 日

**FEATURE:**

Cloud TPU v2 Pod 现已发布 Alpha 版。

由于 TPU 资源可以从单个 Cloud TPU 扩容到 Cloud TPU Pod，因此您并不需要在单个 Cloud TPU 与 Cloud TPU
Pod 之间做出选择。您可以通过核心切片或核心集的形式请求部分 Cloud TPU Pod，这样就可以只购买所需的处理能力 __ 。

[ Cloud TPU Pod（Alpha 版）的优势： ](https://cloud.google.com/tpu/docs/deciding-pod-
versus-tpu?hl=zh_cn)

  * 在研发中提升训练速度，实现快速迭代 
  * 提供可自动扩容的机器学习 (ML) 计算，进而提高用户工作效率 
  * 与单个机器学习加速器相比，能够训练更大的模型 

##  2018 年 10 月 10 日

**FEATURE:**

Cloud TPU v3 现已发布测试版。您现在可以在配置中选择 v2 和 v3。

  * Cloud TPU v3 的内存是 v2 的两倍，不仅提升了性能，而且能够支持更多类型的模型，例如更深的 ResNet 和使用 RetinaNet 的较大图片。 
  * 在 Cloud TPU v2 上运行的现有模型仍可继续使用。 
  * 请参阅 [ Cloud TPU 版本指南，了解更多详情 ](https://cloud.google.com/tpu/docs/deciding-tpu-version?hl=zh_cn) 。 

##  2018 年 10 月 10 日

**CHANGED:**

抢占式 TPU 现已公开发布 (GA)。抢占式 TPU 是一个 Cloud TPU 节点，此类节点的创建和运行费用要远低于普通节点。但是，如果 Cloud
TPU 需要访问资源以用于其他目的，则可能会终止（抢占）这些节点。

  * 了解如何 [ 使用抢占式 TPU ](https://cloud.google.com/tpu/docs/preemptible?hl=zh_cn) 。 
  * 查看抢占式和普通的 Cloud TPU 节点的 [ 价格 ](https://cloud.google.com/tpu/docs/pricing?hl=zh_cn) 。 

##  2018 年 9 月 27 日

**CHANGED:**

Cloud TPU 现支持 [ TensorFlow 1.11 版本
](https://www.tensorflow.org/versions/r1.11/api_docs/?hl=zh_cn) 。TensorFlow
1.11 在 Cloud TPU 上引入了对以下各项的实验性支持：Keras、Colab、即刻执行、LARS、RNN 和 [ Mesh TensorFlow
](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/mesh_tensorflow/README.md)
。此版本还集成了高性能的 [ Cloud Bigtable ](https://cloud.google.com/bigtable/?hl=zh_cn)
，优化了新的 XLA 编译器和整个软件堆栈的其他性能，并改善了 API、错误消息和可靠性。

请参阅 [ Cloud TPU 版本控制政策 ](https://cloud.google.com/tpu/docs/supported-
versions?hl=zh_cn) 中当前支持的 TensorFlow 版本。

##  2018 年 9 月 7 日

**CHANGED:**

对 TensorFlow 1.7 版本的支持于 2018 年 9 月 7 日结束。请参阅 [ Cloud TPU 版本控制政策
](https://cloud.google.com/tpu/docs/supported-versions?hl=zh_cn) ，了解当前支持的版本。

##  2018 年 7 月 24 日

**CHANGED:**

我们很高兴地宣布推出 Cloud TPU 促销活动，大幅降低相关价格。请参阅下表以了解新旧价格：

###  美国

|  每小时每 TPU 的价格（旧）  |  每小时每 TPU 的价格（新）  
---|---|---  
Cloud TPU  |  $6.50 USD  |  $4.50 USD  
抢占式 TPU  |  $1.95 USD  |  $1.35 USD  
  
###  欧洲

|  每小时每 TPU 的价格（旧）  |  每小时每 TPU 的价格（新）  
---|---|---  
Cloud TPU  |  $7.15 USD  |  $4.95 USD  
抢占式 TPU  |  $2.15 USD  |  $1.485 USD  
  
###  亚太地区

|  每小时每 TPU 的价格（旧）  |  每小时每 TPU 的价格（新）  
---|---|---  
Cloud TPU  |  $7.54 USD  |  $5.22 USD  
抢占式 TPU  |  $2.26 USD  |  $1.566 USD  
  
如需了解详细信息，请参阅 [ 价格指南 ](https://cloud.google.com/tpu/docs/pricing?hl=zh_cn) 。

##  2018 年 7 月 12 日

**FEATURE:**

在 Google Kubernetes Engine 中，Cloud TPU 现作为测试版功能提供。在 GCP 上的 Kubernetes
集群中运行您的机器学习工作负载，让 GKE 为您管理和扩缩 Cloud TPU 资源。

  * 按照 [ 教程 ](https://cloud.google.com/tpu/docs/tutorials/kubernetes-engine-resnet?hl=zh_cn) 在 Cloud TPU 和 GKE 上训练 Tensorflow ResNet-50 模型。 
  * 要了解有关如何使用 GKE 运行 Cloud TPU 的快速说明，请参阅 [ GKE 设置指南 ](https://cloud.google.com/tpu/docs/kubernetes-engine-setup?hl=zh_cn) 。 

##  2018 年 7 月 2 日

**CHANGED:**

Cloud TPU 现在支持 [ TensorFlow 1.9 版本
](https://www.tensorflow.org/versions/r1.9/api_docs/?hl=zh_cn) 。TensorFlow 1.9
提升了 Cloud TPU 性能，同时改善了 API、错误消息和可靠性。

##  2018 年 6 月 27 日

**FEATURE:**

Cloud TPU 现已公开发布 (GA)。它是 Google 推出的颠覆性 TPU，旨在加速 TensorFlow 机器学习工作负载。每个 Cloud
TPU 每秒可处理高达 180 万亿次浮点运算，为您提供强大的计算能力来训练和运行最先进的机器学习模型。

  * 按照 [ 快速入门指南 ](https://cloud.google.com/tpu/docs/quickstart?hl=zh_cn) 设置 Cloud TPU。 
  * 选择一个 [ 教程 ](https://cloud.google.com/tpu/docs/tutorials?hl=zh_cn) 以便在 Cloud TPU 上运行特定模型。 

##  2018 年 6 月 18 日

**FEATURE:**

抢占式 TPU 现已发布测试版 __ 。抢占式 TPU 是一个 Cloud TPU 节点，此类节点的创建和运行费用要远低于普通节点。但是，如果 Cloud
TPU 需要访问资源以用于其他目的，则可能会终止（抢占）这些节点。

  * 了解如何 [ 使用抢占式 TPU ](https://cloud.google.com/tpu/docs/preemptible?hl=zh_cn) 。 
  * 查看抢占式和普通的 Cloud TPU 节点的 [ 价格 ](https://cloud.google.com/tpu/docs/pricing?hl=zh_cn) 。 

**CHANGED:**

Cloud TPU 现已在欧洲 (EU)、亚太地区 (APAC) 和美国 (US) 发布。查看各个地区的 [ 价格详情
](https://cloud.google.com/tpu/docs/pricing?hl=zh_cn) 。现已在以下地区发布：

  * **美国**
    * ` us-central1-b `
    * ` us-central1-c `
    * ` us-central1-f ` （仅限 [ TFRC 计划 ](https://www.tensorflow.org/tfrc/?hl=zh_cn) ） 
  * **欧盟**
    * ` europe-west4-a `
  * **亚太地区**
    * ` asia-east1-c `

##  2018 年 6 月 12 日

**CHANGED:**

对 TensorFlow 1.6 版本的支持于 2018 年 6 月 12 日结束。请参阅 [ Cloud TPU 版本控制政策
](https://cloud.google.com/tpu/docs/supported-versions?hl=zh_cn) ，了解当前支持的版本。

##  2018 年 4 月 20 日

**CHANGED:**

Cloud TPU 现在支持 [ TensorFlow 1.8 版本
](https://www.tensorflow.org/versions/r1.8/api_docs/?hl=zh_cn) 。TensorFlow 1.8
提升了 Cloud TPU 性能，改进了 API、错误消息和可靠性。

对 TensorFlow 1.7 版本的支持于 2018 年 6 月 20 日结束。请参阅 [ Cloud TPU 版本控制政策
](https://cloud.google.com/tpu/docs/supported-versions?hl=zh_cn) ，了解详细信息。

##  2018 年 4 月 2 日

**CHANGED:**

Cloud TPU 现在支持 [ TensorFlow 1.7 版本
](https://www.tensorflow.org/versions/r1.7/api_docs/?hl=zh_cn) 。对 TensorFlow
1.6 版本的支持于 2018 年 6 月 2 日结束。请参阅 [ Cloud TPU 版本控制政策
](https://cloud.google.com/tpu/docs/supported-versions?hl=zh_cn) ，了解详细信息。

##  2018 年 2 月 12 日

**FEATURE:**

Cloud TPU 现已发布测试版。它是 Google 推出的颠覆性 TPU，旨在加速 TensorFlow 机器学习工作负载。每个 Cloud TPU
每秒可处理高达 180 万亿次浮点运算，为您提供强大的计算能力来训练和运行最先进的机器学习模型。

  * 请参阅如何 [ 申请 TPU 配额 ](https://cloud.google.com/tpu/docs/quota?hl=zh_cn) 。 
  * 按照 [ 快速入门指南 ](https://cloud.google.com/tpu/docs/quickstart?hl=zh_cn) 设置 Cloud TPU。 
  * 选择一个 [ 教程 ](https://cloud.google.com/tpu/docs/tutorials?hl=zh_cn) 以便在 Cloud TPU 上运行特定模型。 

