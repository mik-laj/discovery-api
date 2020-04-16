#  リリースノート

このページには、Cloud TPU
の本番環境に関する更新情報が記載されています。このページを定期的にチェックして、新機能や更新された特徴、バグ修正、既知の問題、非推奨となった機能に関するお知らせを確認してください。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加します。

##  2019 年 5 月 7 日

**FEATURE:**

Cloud TPU v2 Pod のベータ版がリリースされました。

TPU リソースは単一の Cloud TPU から Cloud TPU Pod までのスケーリングが可能であるため、単一の Cloud TPU か
Cloud TPU Pod かを選択する必要はありません。必要な処理能力だけを購入できるよう、Cloud TPU Pod の一部をスライス単位 __
またはコアのセットでリクエストできます。

[ 単一の Cloud TPU v2 デバイスと比べて、Cloud TPU Pod（ベータ版）には次のメリットがあります。
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=ja)

  * トレーニング速度の向上により研究開発での反復型開発を迅速化 
  * 自動的にスケーラブルな機械学習（ML）コンピューティングを提供することにより人間の生産性が向上 
  * 非常に大型のモデルのトレーニングに対応 

**FEATURE:**

Cloud TPU v3 Pod のベータ版がリリースされました。

TPU リソースは単一の Cloud TPU から Cloud TPU Pod までのスケーリングが可能であるため、単一の Cloud TPU か
Cloud TPU Pod かを選択する必要はありません。必要な処理能力だけを購入できるよう、Cloud TPU Pod の一部をスライス単位 __
またはコアのセットでリクエストできます。

[ 単一の Cloud TPU v3 デバイスと比べて、Cloud TPU Pod（ベータ版）には次のメリットがあります。
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=ja)

  * トレーニング速度の向上により研究開発での反復型開発を迅速化 
  * 自動的にスケーラブルな機械学習（ML）コンピューティングを提供することにより人間の生産性が向上 
  * 非常に大型のモデルのトレーニングに対応 

Cloud TPU v2 Pod（ベータ版） __ と比べて、Cloud TPU v3 Pod（ベータ版） __ には次のメリットがあります。

* 処理の高速化とメモリ容量の増大化: 

  * v2 Pod: 11.5 PFLOPS、4 TB のオンチップ メモリ（HBM） 
  * v3 Pod: 100 PFLOPS、32 TB の HBM、液体冷却 

* 大型モデルのトレーニングが可能 

##  2019 年 3 月 11 日

**CHANGED:**

Cloud TPU で、 [ TensorFlow バージョン 1.13
](https://www.tensorflow.org/versions/r1.13/api_docs/?hl=ja)
がサポートされるようになりました。Tensorflow バージョン 1.8 および 1.9 のサポートは終了しました。

現在サポートされている TensorFlow バージョンについては、 [ Cloud TPU のバージョニング ポリシー
](https://cloud.google.com/tpu/docs/supported-versions?hl=ja) をご覧ください。

##  2019 年 1 月 31 日

**FEATURE:**

Cloud TPU v3 が GA（一般提供）になりました。Cloud TPU v3 のメモリ容量は v2 の 2
倍です。これにより、パフォーマンスが向上し、より多くのモデルクラスのサポートが可能になっています。たとえば、深層化された ResNets や
RetinaNet でのより大きなイメージなどにも対応できます。Cloud TPU v2 で稼働する既存のモデルは引き続き機能します。詳細については、 [
Cloud TPU バージョンのガイド ](https://cloud.google.com/tpu/docs/deciding-tpu-
version?hl=ja) をご覧ください。

##  2018 年 11 月 8 日

**CHANGED:**

Cloud TPU で、 [ TensorFlow バージョン 1.12
](https://www.tensorflow.org/versions/r1.12/api_docs/?hl=ja)
がサポートされるようになりました。このリリースでは、Cloud TPU 上の Keras に改善が加えれ、ソフトウェア
スタック全体にわたりパフォーマンスが向上しています。また、API、エラー メッセージ、信頼性も改善されています。

現在サポートされている TensorFlow バージョンについては、 [ Cloud TPU のバージョニング ポリシー
](https://cloud.google.com/tpu/docs/supported-versions?hl=ja) をご覧ください。

##  2018 年 11 月 7 日

**FEATURE:**

Cloud TPU v2 Pod のアルファ版がリリースされました。

TPU リソースは単一の Cloud TPU から Cloud TPU Pod までのスケーリングが可能であるため、単一の Cloud TPU か
Cloud TPU Pod かを選択する必要はありません。必要な処理能力だけを購入できるよう、Cloud TPU Pod の一部をスライス単位 __
またはコアのセットでリクエストできます。

[ Cloud TPU Pod（アルファ版）には次のメリットがあります。
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=ja)

  * トレーニング速度の向上により研究開発での反復型開発を迅速化 
  * 自動的にスケーラブルな機械学習（ML）コンピューティングを提供することにより人間の生産性が向上 
  * 単一の ML アクセラレータよりもはるかに大きなモデルのトレーニングに対応 

##  2018 年 10 月 10 日

**FEATURE:**

Cloud TPU v3 のベータ版がリリースされました。構成で v2 または v3 を選択できるようになりました。

  * Cloud TPU v3 のメモリ容量は v2 の 2 倍です。これにより、パフォーマンスが向上し、より多くのモデルクラスのサポートが可能になっています。たとえば、深層化された ResNets や RetinaNet でのより大きなイメージなどにも対応できます。 
  * Cloud TPU v2 で稼働する既存のモデルは引き続き機能します。 
  * 詳細については、 [ Cloud TPU バージョンのガイド ](https://cloud.google.com/tpu/docs/deciding-tpu-version?hl=ja) をご覧ください。 

##  2018 年 10 月 10 日

**CHANGED:**

プリエンプティブ TPU が GA（一般提供）になりました。プリエンプティブル TPU は、通常のノードよりはるかに低価格で作成および実行できる Cloud
TPU ノードです。ただし、別の目的のためにリソースにアクセスする必要がある場合、Cloud TPU
では、これらのノードを終了（プリエンプト）することがあります。

  * [ プリエンプティブ TPU の使用 ](https://cloud.google.com/tpu/docs/preemptible?hl=ja) 方法を確認します。 
  * プリエンプティブおよび通常の Cloud TPU ノードの [ 料金 ](https://cloud.google.com/tpu/docs/pricing?hl=ja) を確認します。 

##  2018 年 9 月 27 日

**CHANGED:**

Cloud TPU で、 [ TensorFlow バージョン 1.11
](https://www.tensorflow.org/versions/r1.11/api_docs/?hl=ja)
がサポートされるようになりました。TensorFlow 1.11 では、Cloud TPU 上での Keras、Colab、積極的実行、LARS、RNN、
[ Mesh TensorFlow
](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/mesh_tensorflow/README.md)
のすべてに対する実験的サポートを導入しています。このリリースではさらに、高パフォーマンス [ Cloud Bigtable
](https://cloud.google.com/bigtable/?hl=ja) の統合、新しい XLA コンパイラ最適化なども導入され、ソフトウェア
スタック全体にわたりパフォーマンスが向上しています。また、API、エラー メッセージ、信頼性も改善されています。

現在サポートされている TensorFlow バージョンについては、 [ Cloud TPU のバージョニング ポリシー
](https://cloud.google.com/tpu/docs/supported-versions?hl=ja) をご覧ください。

##  2018 年 9 月 7 日

**CHANGED:**

TensorFlow バージョン 1.7 のサポートは、2018 月 9 月 7 日に終了しました。現在サポートされているバージョンについては、 [
Cloud TPU のバージョニング ポリシー ](https://cloud.google.com/tpu/docs/supported-
versions?hl=ja) をご覧ください。

##  2018 年 7 月 24 日

**CHANGED:**

このたび、Cloud TPU を特別料金で提供し、料金を大幅に値下げすることになりました。次の表は、従来の料金と本日から有効な新しい料金を示紹介しています。

###  米国

|  1 時間あたりの TPU ごとの旧料金  |  1 時間あたりの TPU ごとの新料金  
---|---|---  
Cloud TPU  |  $6.50 USD  |  $4.50 USD  
プリエンプティブル TPU  |  $1.95 USD  |  $1.35 USD  
  
###  ヨーロッパ

|  1 時間あたりの TPU ごとの旧料金  |  1 時間あたりの TPU ごとの新料金  
---|---|---  
Cloud TPU  |  $7.15 USD  |  $4.95 USD  
プリエンプティブル TPU  |  $2.15 USD  |  $1.485 USD  
  
###  アジア太平洋

|  1 時間あたりの TPU ごとの旧料金  |  1 時間あたりの TPU ごとの新料金  
---|---|---  
Cloud TPU  |  $7.54 USD  |  $5.22 USD  
プリエンプティブル TPU  |  $2.26 USD  |  $1.566 USD  
  
詳細については、 [ 料金ガイド ](https://cloud.google.com/tpu/docs/pricing?hl=ja) をご覧ください。

##  2018 年 7 月 12 日

**FEATURE:**

Cloud TPU が、Google Kubernetes Engine でベータ版機能として使用できるようになりました。GCP 上の Kubernetes
クラスタ内で機械学習ワークロードを実行すると、GKE が Cloud TPU リソースの管理とスケーリングを自動的に行います。

  * [ チュートリアル ](https://cloud.google.com/tpu/docs/tutorials/kubernetes-engine-resnet?hl=ja) に従って、Cloud TPU と GKE 上で Tensorflow ResNet-50 モデルをトレーニングできます。 
  * GKE を使用して Cloud TPU を実行するクイック手順については、 [ GKE の設定に関するガイド ](https://cloud.google.com/tpu/docs/kubernetes-engine-setup?hl=ja) をご覧ください。 

##  2018 年 7 月 2 日

**CHANGED:**

Cloud TPU で、 [ TensorFlow バージョン 1.9
](https://www.tensorflow.org/versions/r1.9/api_docs/?hl=ja)
がサポートされるようになりました。TensorFlow 1.9 では、Cloud TPU のパフォーマンスが向上し、API、エラー
メッセージ、信頼性も改善されています。

##  2018 年 6 月 27 日

**FEATURE:**

Cloud TPU は、現在 GA（一般提供）です。Google の革新的な TPU は、機械学習のワークロードを TensorFlow
で高速化することを目的として設計されています。Cloud TPU 1 個あたりのパフォーマンスは最大 180 TFLOPS
であり、この計算能力で最先端の機械学習モデルのトレーニングと実行が可能になります。

  * [ クイックスタート ガイド ](https://cloud.google.com/tpu/docs/quickstart?hl=ja) に従って、Cloud TPU を設定します。 
  * Cloud TPU で特定のモデルを実行する [ チュートリアル ](https://cloud.google.com/tpu/docs/tutorials?hl=ja) を選択します。 

##  2018 年 6 月 18 日

**FEATURE:**

プリエンプティブ TPU のベータ版が利用可能になりました。 __ プリエンプティブル TPU は、通常のノードよりはるかに低価格で作成および実行できる
Cloud TPU ノードです。ただし、別の目的のためにリソースにアクセスする必要がある場合、Cloud TPU
では、これらのノードを終了（プリエンプト）することがあります。

  * [ プリエンプティブ TPU の使用 ](https://cloud.google.com/tpu/docs/preemptible?hl=ja) 方法を確認します。 
  * プリエンプティブおよび通常の Cloud TPU ノードの [ 料金 ](https://cloud.google.com/tpu/docs/pricing?hl=ja) を確認します。 

**CHANGED:**

Cloud TPU は、欧州（EU）、アジア太平洋（APAC）リージョン、米国（US）で利用可能になりました。リージョンごとの [ 料金の詳細
](https://cloud.google.com/tpu/docs/pricing?hl=ja) をご覧ください。次のゾーンを使用できます。

  * **US**
    * ` us-central1-b `
    * ` us-central1-c `
    * ` us-central1-f ` （ [ TFRC プログラム ](https://www.tensorflow.org/tfrc/?hl=ja) のみ） 
  * **EU**
    * ` europe-west4-a `
  * **APAC**
    * ` asia-east1-c `

##  2018 年 6 月 12 日

**CHANGED:**

TensorFlow バージョン 1.6 のサポートは、2018 年 6 月 12 日に終了しました。現在サポートされているバージョンについては、 [
Cloud TPU のバージョニング ポリシー ](https://cloud.google.com/tpu/docs/supported-
versions?hl=ja) をご覧ください。

##  2018 年 4 月 20 日

**CHANGED:**

Cloud TPU で、 [ TensorFlow バージョン 1.8
](https://www.tensorflow.org/versions/r1.8/api_docs/?hl=ja)
がサポートされるようになりました。TensorFlow 1.8 では、Cloud TPU のパフォーマンスが向上し、API、エラー
メッセージ、信頼性も改善されています。

TensorFlow バージョン 1.7 のサポートは、2018 年 6 月 20 日に終了します。詳細については、 [ Cloud TPU
のバージョニング ポリシー ](https://cloud.google.com/tpu/docs/supported-versions?hl=ja)
をご覧ください。

##  2018 年 4 月 2 日

**CHANGED:**

Cloud TPU で、 [ TensorFlow バージョン 1.7
](https://www.tensorflow.org/versions/r1.7/api_docs/?hl=ja)
がサポートされるようになりました。TensorFlow バージョン 1.6 のサポートは、2018 年 6 月 2 日に終了します。詳細については、 [
Cloud TPU のバージョニング ポリシー ](https://cloud.google.com/tpu/docs/supported-
versions?hl=ja) をご覧ください。

##  2018 年 2 月 12 日

**FEATURE:**

Cloud TPU のベータ版がリリースされました。Google の革新的な TPU は、機械学習のワークロードを TensorFlow
で高速化することを目的として設計されています。Cloud TPU 1 個あたりのパフォーマンスは最大 180 TFLOPS
であり、この計算能力で最先端の機械学習モデルのトレーニングと実行が可能になります。

  * [ TPU 割り当てをリクエスト ](https://cloud.google.com/tpu/docs/quota?hl=ja) する方法を確認します。 
  * [ クイックスタート ガイド ](https://cloud.google.com/tpu/docs/quickstart?hl=ja) に従って、Cloud TPU を設定します。 
  * Cloud TPU で特定のモデルを実行する [ チュートリアル ](https://cloud.google.com/tpu/docs/tutorials?hl=ja) を選択します。 

