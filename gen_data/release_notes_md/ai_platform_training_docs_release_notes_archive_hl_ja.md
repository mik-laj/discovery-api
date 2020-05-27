#  リリースノートのアーカイブ

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

2019 年 4 月 10 日、Cloud Machine Learning Engine が [ AI Platform Training
](https://cloud.google.com/ai-platform/training?hl=ja) と [ AI Platform
Prediction ](https://cloud.google.com/ai-platform/prediction?hl=ja)
になりました。このページには Cloud ML Engine の更新履歴が記載されています。

現在のリリースノートをご覧ください。

  * [ AI Platform Training リリースノート ](https://cloud.google.com/ai-platform/training/docs/release-notes?hl=ja)
  * [ AI Platform Prediction リリースノート ](https://cloud.google.com/ai-platform/prediction/docs/release-notes?hl=ja)

##  2019 年 4 月 1 日

**FEATURE:**

Cloud ML Engine のトレーニング、オンライン予測、バッチ予測の料金が引き下げられました。

詳細については、 [ Cloud ML Engine の料金 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=ja) をご覧ください。

##  2019 年 3 月 28 日

**FEATURE:**

Cloud ML Engine は、組み込みアルゴリズムを使用したトレーニングの提供を開始しました。データを送信して自動で前処理させて、モデルを
TensorFlow [ 線形学習者
](https://www.tensorflow.org/tutorials/representation/linear?hl=ja)
、TensorFlow [ ワイド＆ディープ ](https://ai.googleblog.com/2016/06/wide-deep-learning-
better-together-with.html) 、および [ XGBoost
](https://xgboost.readthedocs.io/en/latest/tutorials/model.html)
アルゴリズムでトレーニングできます。コードを記述する必要はありません。

詳しくは、 [ 組み込みアルゴリズムを使用したトレーニング ](https://cloud.google.com/ai-
platform/training/docs/algorithms?hl=ja) をご覧ください。

##  2019 年 3 月 25 日

**CHANGED:**

Cloud ML Engine ランタイム バージョン 1.13 に TensorFlow 1.13.1 のサポートが追加されました。ランタイム バージョン
1.13 に含まれる全パッケージのリストについては、 [ ランタイム バージョンのリスト ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=ja) をご覧ください。

##  2019 年 3 月 8 日

**FEATURE:**

Cloud ML Engine ランタイム バージョン 1.9 の TPU を使用したトレーニングのサポートは、2019 年 3 月 8
日に終了しました。現在サポートされているバージョンについては、 [ ランタイム バージョンのリスト
](https://cloud.google.com/ai-platform/training/docs/tensorflow/runtime-
version-list?hl=ja#tpu-support) をご覧ください。

##  2019 年 3 月 6 日

**FEATURE:**

Cloud ML Engine ランタイム バージョン 1.13 がトレーニングと予測に使用できるようになりました。このバージョンは、TensorFlow
1.13 をサポートし、 [ ランタイム バージョンのリスト ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=ja) に記載される他のパッケージを含んでいます。

TPU を使用したトレーニングは、現時点ではランタイム バージョン 1.13 でサポートされていません。

##  2019 年 3 月 1 日

**FEATURE:**

[ AI Platform Notebooks ](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=ja) のベータ版がリリースされました。AI Platform
Notebooks を使用すると、 [ JupyterLab
](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)
にあらかじめパッケージ化された仮想マシン（VM）インスタンスとディープ ラーニング ソフトウェア スイートを作成および管理できます。

詳しくは、 [ AI Platform Notebooks の概要 ](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=ja) と [ 新しいノートブック インスタンスを作成する
](https://cloud.google.com/ai-platform/training/docs/notebooks/create-
new?hl=ja) をご覧ください。

##  2019 年 2 月 13 日

**FEATURE:**

Cloud TPU が一般提供され、TensorFlow モデルのトレーニングで使用できるようになりました。Tensor Processing
Unit（TPU）は、機械学習ワークロードを高速化するために Google が独自に開発したアクセラレータです。

Cloud ML Engine 上で [ TPU を使用してモデルをトレーニングする方法 ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-tpus?hl=ja) を確認してください。TPU の料金については [ こちら
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ja) をご覧ください。

##  2019 年 2 月 7 日

**FEATURE:**

カスタム コンテナを使用したトレーニングがベータ版で利用可能になりました。この機能により、Cloud ML Engine 上でカスタム Docker
イメージを使用してトレーニング アプリケーションを実行できます。カスタム コンテナは、任意の ML フレームワークを使用して作成できます。 [ カスタム
コンテナを使用した PyTorch モデルのトレーニング ](https://cloud.google.com/ai-
platform/training/docs/custom-containers-training?hl=ja) をお試しください。

**FEATURE:**

特定の Compute Engine マシンタイプを指定してトレーニング ジョブを構成できるようになりました。これにより、トレーニング
ジョブにさらに柔軟にコンピューティング リソースを割り当てることができます。この機能はベータ版で利用できます。

Compute Engine マシンタイプを指定してジョブを構成するときに、任意のセットの GPU を接続することもできます。

詳細については、 [ Compute Engine のマシンタイプ ](https://cloud.google.com/ai-
platform/training/docs/machine-types?hl=ja#compute-engine-machine-types) 、 [
GPU 接続 ](https://cloud.google.com/ml-engine/docs/tensorflow/using-
gpus?hl=ja#compute-engine-machine-types-with-gpu) 、 [ 料金
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ja) をご覧ください。

**FEATURE:**

トレーニングに P4 GPU のベータ版を利用できるようなりました。詳細については、 [ GPU の使用
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ja) 、 [ GPU
を利用可能なリージョン ](https://cloud.google.com/ml-
engine/docs/tensorflow/regions?hl=ja#training_with_accelerators) 、 [ GPU の料金
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ja)
に関するガイドをご覧ください。

##  2019 年 2 月 1 日

**CHANGED:**

クアッドコア CPU のベータ版でオンライン予測が可能になりました。マシンタイプの名前が変更され、料金が更新されました。

  * [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=ja) に ` machineType ` を設定して、サービスに使用するマシンタイプを指定します。クアッドコア CPU には ` mls1-c4-m2 ` を使用します。デフォルトは、シングルコア CPU である ` mls1-c1-m2 ` です。 
  * アルファ版で使用されているマシン名 ` mls1-highmem-1 ` と ` mls1-highcpu-4 ` は **非推奨** になりました。 
  * 詳細については、 [ オンライン予測 ](https://cloud.google.com/ai-platform/training/docs/online-predict?hl=ja#machine-types) のガイドをご覧ください。 
  * マシンタイプについては、更新版の [ 料金 ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ja) をご覧ください。 

##  2019 年 1 月 25 日

**FEATURE:**

オンライン予測が、us-east4 リージョンで利用可能になりました。 [ 利用可能なリージョン
](https://cloud.google.com/ai-platform/training/docs/regions?hl=ja)
に関するガイドをご覧ください。

##  2019 年 1 月 10 日

**FEATURE:**

V100 GPU を使用するトレーニングが一般提供になりました。詳細については、 [ GPU の使用
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ja) と [ 料金
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ja)
に関するガイドをご覧ください。

##  2018 年 12 月 19 日

**FEATURE:**

Cloud ML Engine ランタイム バージョン 1.11 と 1.12 がトレーニングと予測に使用できるようになりました。これらのバージョンは
TensorFlow 1.11、1.12 をそれぞれサポートしています。また、 [ ランタイム バージョンのリスト
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=ja) にある他のパッケージもサポートしています。

TPU トレーニングが Cloud ML Engine ランタイム バージョン 1.11 と 1.12 でサポートされるようになりました。バージョン
1.10 はサポートされていません。現在サポートされているバージョンについては、 [ ランタイム バージョンのリスト
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ja#tpu-support) をご覧ください。

**CHANGED:**

Cloud ML Engine ランタイムのバージョンごとに [ joblib
](https://joblib.readthedocs.io/en/latest/) が同梱されるようになりました。joblib は、バージョン 1.4
以降のランタイムに同梱されます。

##  2018 年 10 月 26 日

**CHANGED:**

Cloud ML ランタイム バージョン 1.8 向けの TPU トレーニングのサポートは、2018 年 10 月 26
日に終了しました。現在サポートされているバージョンについては、 [ ランタイム バージョンのリスト
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ja#tpu-support) をご覧ください。

##  2018 年 10 月 11 日

**ISSUE:**

Cloud ML Engine ランタイム バージョン 1.11 は、GPU トレーニング中の [ CuDNN バージョンの不一致によるエラー
](https://stackoverflow.com/q/52733440) のためにロールバックされます。当面の回避策として、ランタイム バージョン
1.10 をご使用ください。詳細については、 [ ランタイム バージョン リスト ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=ja) をご覧ください。

##  2018 年 10 月 5 日

**FEATURE:**

Cloud ML Engine ランタイム バージョン 1.11 がトレーニングと予測に使用できるようになりました。このバージョンは、TensorFlow
1.11 と [ ランタイム バージョンのリスト ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=ja) にある他のパッケージをサポートしています。

##  2018 年 8 月 31 日

**FEATURE:**

Cloud ML Engine ランタイム バージョン 1.10 がトレーニングと予測に使用できるようになりました。このバージョンは、TensorFlow
1.10 と [ ランタイム バージョンのリスト ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=ja) にある他のパッケージをサポートしています。

##  2018 年 8 月 27 日

**FEATURE:**

トレーニングに V100 GPU のベータ版を使用できるようになりました。今後、V100 GPU を使用すると、料金が発生します。詳細については、 [
GPU の使用 ](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ja)
と [ 料金 ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ja)
に関するガイドをご覧ください。

**FEATURE:**

P100 GPU を使用するトレーニングが一般提供になりました。詳細については、 [ GPU の使用
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ja) と [ 料金
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ja)
に関するガイドをご覧ください。

**FEATURE:**

us-west1 と europe-west4 の 2 つの新しいリージョンでトレーニングを実施できることになりました。詳細については、 [ リージョン
](https://cloud.google.com/ai-platform/training/docs/regions?hl=ja)
のページをご覧ください。

##  2018 年 8 月 24 日

**CHANGED:**

Cloud ML ランタイム バージョン 1.7 の TPU トレーニングのサポートは、2018 年 8 月 24
日に終了しました。現在サポートされているバージョンについては、 [ ランタイム バージョンのリスト
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ja#tpu-support) をご覧ください。

##  2018 年 8 月 9 日

**CHANGED:**

AI Platform Training によるオンライン予測の料金を大幅に値下げしました。

次の表に、新旧の料金を示します。

リージョン  |  1 時間あたりのノードごとの旧料金  |  1 時間あたりのノードごとの新料金  
---|---|---  
米国  |  $0.30 米ドル  |  $0.056 米ドル  
ヨーロッパ  |  $0.348 米ドル  |  $0.061 米ドル  
アジア太平洋  |  $0.348 米ドル  |  $0.071 米ドル  
  
詳細については、 [ 料金ガイド ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=ja) をご覧ください。

##  2018 年 8 月 8 日

**CHANGED:**

AI Platform Training を使用した Cloud TPU のキャンペーンを実施し、料金を大幅に値下げしました。

次の表に、新旧の料金を示します。

リージョン: 米国  |  1 時間あたりの TPU ごとの旧料金  |  1 時間あたりの TPU ごとの新料金  
---|---|---  
スケール階層: ` BASIC_TPU ` （ベータ版） __ |  $9.7674 米ドル  |  $6.8474 米ドル  
カスタム マシンタイプ: ` cloud_tpu ` （ベータ版） __ |  $9.4900 米ドル  |  $6.5700 米ドル  
  
この表には、米国リージョンのみの料金が示されています。Cloud ML Engine での Cloud TPU
の提供状況に変更はありません。詳細については、 [ 料金ガイド ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=ja) をご覧ください。

##  2018 年 8 月 6 日

**FEATURE:**

Cloud ML Engine ランタイム バージョン 1.9 がトレーニングと予測に使用できるようになりました。このバージョンは、TensorFlow
1.9 と [ ランタイム バージョンのリスト ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=ja) にある他のパッケージをサポートしています。

##  2018 年 7 月 23 日

**FEATURE:**

Cloud ML Engine で、トレーニングに **scikit-learn** と **XGBoost**
を利用できるようになりました。この機能は一般提供です。 [ Cloud ML Engine での scikit-learn と XGBoost
によるトレーニング ](https://cloud.google.com/ml-engine/docs/scikit/getting-started-
training?hl=ja) のガイドをご覧ください。

**FEATURE:**

オンライン予測での **scikit-learn** と **XGBoost** のサポートが一般提供になりました。

  * モデル バージョンを作成する際に、 [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=ja) に ` framework ` を設定して機械学習フレームワークを指定します。有効な値は ` TENSORFLOW ` 、 ` SCIKIT_LEARN ` 、 ` XGBOOST ` です。デフォルトは ` TENSORFLOW ` です。 ` SCIKIT_LEARN ` または ` XGBOOST ` を指定する場合は、モデル バージョンで ` runtimeVersion ` を 1.4 以上に設定する必要があります。 
  * [ scikit-learn と XGBoost によるローカル トレーニングとオンライン予測 ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=ja) のガイドをご覧ください。 

##  2018 年 7 月 12 日

**FEATURE:**

AI Platform Training のリソース（ [ ジョブ ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=ja) 、 [ モデル
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models?hl=ja) 、 [ モデル バージョン
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=ja)
）にラベルを追加すると、これらのラベルを使用してリソースをカテゴリ別に整理できます。ラベルは [ オペレーション
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.operations?hl=ja)
でも使用できますが、この場合はオペレーションの適用先のリソースからラベルが導出されます。詳細については、 [ ラベルの追加と使用
](https://cloud.google.com/ml-engine/docs/tensorflow/resource-labels?hl=ja)
に関する記事をご覧ください。

##  2018 年 6 月 26 日

**CHANGED:**

次の追加のリージョンで全機能が利用できるようになりました。

  * us-east1 
  * asia-northeast1 

詳細については、 [ 利用可能なリージョン ](https://cloud.google.com/ai-
platform/training/docs/regions?hl=ja) をご覧ください。

##  2018 年 6 月 13 日

**CHANGED:**

Cloud ML ランタイム バージョン 1.6 での TPU トレーニングのサポートは、2018 年 6 月 13
日に終了しました。現在サポートされているバージョンについては、 [ ランタイム バージョンのリスト
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ja#tpu-support) をご覧ください。

##  2018 年 5 月 29 日

**CHANGED:**

TensorFlow 1.8 と Cloud ML Engine ランタイム バージョン 1.8 で Cloud TPU（ _ベータ版_
）を使用できるようになりました。

背景情報: __ 5 月 14 日より、Cloud TPU が Cloud ML Engine ランタイム バージョン 1.6 と 1.7
で使用できるようになりました。先週、ランタイム バージョン 1.8 がリリースされましたが、その時点では TensorFlow 1.8 で Cloud
TPU はまだ使用できませんでした。現在は使用できるようになりました。Cloud ML Engine で [ TPU を使用してモデルをトレーニングする
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=ja)
方法をご覧ください。

##  2018 年 5 月 16 日

**FEATURE:**

Cloud ML Engine ランタイム バージョン 1.8 がトレーニングと予測に使用できるようになりました。このバージョンは、TensorFlow
1.8 と [ ランタイム バージョンのリスト ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=ja) にある他のパッケージをサポートしています。

##  2018 年 5 月 15 日

**FEATURE:**

既存のモデル バージョンで [ 自動スケーリング ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=ja#autoscaling)
するノードの最小数を更新できるようになりました。また、新しいバージョンを作成するときに属性を指定できるようになりました。

##  2018 年 5 月 14 日

**FEATURE:**

Cloud ML Engine は、TensorFlow モデルのトレーニング用に Cloud TPU（ベータ版） __
を提供するようになりました。Tensor Processing Unit（TPU）は、Google 独自開発の ASIC
であり、機械学習ワークロードを高速化します。Cloud ML Engine で [ TPU を使用してモデルをトレーニングする
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=ja)
方法をご覧ください。

##  2018 年 4 月 26 日

**FEATURE:**

Cloud ML Engine ランタイム バージョン 1.7 がトレーニングと予測に使用できるようになりました。このバージョンは、TensorFlow
1.7 と [ ランタイム バージョンのリスト ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=ja) にある他のパッケージをサポートしています。

##  2018 年 4 月 16 日

**FEATURE:**

**ハイパーパラメータ アルゴリズム:** トレーニング ジョブでハイパーパラメータを調整するときに、 [ HyperparameterSpec
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=ja#hyperparameterspec)
で検索アルゴリズムを指定できるようになりました。使用可能な値は次のとおりです。

  * ` GRID_SEARCH ` : 実行可能領域内の単純なグリッド検索。このオプションは、実行可能領域内のポイント数を超える試行回数を指定する場合に特に便利です。そのような場合、グリッド検索を指定しないと、Cloud ML Engine のデフォルト アルゴリズムによって重複した候補が生成されることがあります。グリッド検索を使用するには、すべてのパラメータの型が ` INTEGER ` 、 ` CATEGORICAL ` 、または ` DISCRETE ` でなければなりません。 
  * ` RANDOM_SEARCH ` : 実行可能領域内の単純なランダム検索。 

アルゴリズムを指定しない場合、デフォルトの Cloud ML Engine
アルゴリズムが使用されます。このアルゴリズムは、パラメータ空間のより効果的な検索により、最適なソリューションを導き出します。ハイパーパラメータ調整の詳細については、
[ ハイパーパラメータ調整の概要 ](https://cloud.google.com/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview?hl=ja) をご覧ください。

##  2018 年 4 月 5 日

**FEATURE:**

Cloud ML Engine で、オンライン予測に **scikit-learn** と **XGBoost**
を利用できるようになりました。この機能はベータ版 __ です。

  * モデル バージョンを作成する際に、 [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=ja) に ` framework ` を設定して機械学習フレームワークを指定します。有効な値は ` TENSORFLOW ` 、 ` SCIKIT_LEARN ` 、 ` XGBOOST ` です。デフォルトは ` TENSORFLOW ` です。 ` SCIKIT_LEARN ` または ` XGBOOST ` を指定する場合は、モデル バージョンで ` runtimeVersion ` を 1.4 以上に設定する必要があります。 
  * [ Cloud ML Engine での scikit-learn と XGBoost ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=ja) のガイドをご覧ください。 

**FEATURE:**

オンライン予測に Python 3.5 を利用できます。

  * モデル バージョンを作成する際に [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=ja) に ` pythonVersion ` を設定して Python のバージョンを指定します。デフォルトは Python 2.7 です。 
  * Cloud ML Engine で利用可能なパッケージの詳細については、 [ ランタイム バージョンのリスト ](https://cloud.google.com/ml-engine/docs/scikit/runtime-version-list?hl=ja) をご覧ください。 

##  2018 年 3 月 20 日

**FEATURE:**

Cloud ML Engine ランタイム バージョン 1.6 がトレーニングと予測に使用できるようになりました。このバージョンは、TensorFlow
1.6 と [ ランタイム バージョンのリスト ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=ja) にある他のパッケージをサポートしています。

##  2018 年 3 月 13 日

**FEATURE:**

TensorFlow 1.5 の Cloud ML Engine ランタイム バージョンがトレーニングと予測に使用できるようになりました。詳細については、
[ ランタイム バージョン リスト ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=ja) をご覧ください。

##  2018 年 2 月 8 日

**FEATURE:**

ハイパーパラメータ調整に新機能が追加されました。トライアルの早期自動停止、以前のハイパーパラメータ調整ジョブの再開、類似したジョブの実行時の効率的な最適化などの機能が追加されています。ハイパーパラメータ調整については、
[ ハイパーパラメータ調整の概要 ](https://cloud.google.com/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview?hl=ja) をご覧ください。

##  2017 年 12 月 14 日

**FEATURE:**

TensorFlow 1.4 の Cloud ML Engine ランタイム バージョンがトレーニングと予測に使用できるようになりました。詳細については、
[ ランタイム バージョン リスト ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=ja) をご覧ください。

**FEATURE:**

TensorFlow 1.4 の Cloud ML Engine ランタイム バージョンの一部として、Python 3
がトレーニングに使用できるようになりました。詳細については、 [ ランタイム バージョン リスト
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ja) をご覧ください。

**FEATURE:**

オンライン予測が一般提供され、シングルコア サービスで使えるようになりました。 [ オンライン予測
](https://cloud.google.com/ml-engine/docs/tensorflow/online-predict?hl=ja)
に関するガイドと [ ブログ投稿 ](https://cloud.google.com/blog/big-data/2017/12/bringing-
cloud-ml-engine-to-more-developers-with-online-prediction-features-and-
reduced-prices?hl=ja) をご覧ください。

**FEATURE:**

トレーニングと予測の両方で価格設定が引き下げられ、シンプルになりました。 [ 料金の詳細 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=ja) と [ ブログ投稿
](https://cloud.google.com/blog/big-data/2017/12/bringing-cloud-ml-engine-to-
more-developers-with-online-prediction-features-and-reduced-prices?hl=ja)
をご覧ください。また、新旧の料金の比較については [ 料金に関するよくある質問 ](https://cloud.google.com/ml-
engine/docs/tensorflow/pricing-faq?hl=ja) をご覧ください。

**FEATURE:**

P100 GPU がベータ版で利用可能になりました。今後、P100 GPU を使用すると料金が発生します。詳細については、 [ GPU の使用
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ja) と [ 料金
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ja) をご覧ください。

##  2017 年 10 月 26 日

**FEATURE:**

Cloud ML Engine の監査ロギングがベータ版で利用可能になりました。詳細については、 [ 監査ログの表示
](https://cloud.google.com/ml-engine/docs/tensorflow/audit-logs?hl=ja)
をご覧ください。

##  2017 年 9 月 25 日

**FEATURE:**

Cloud ML Engine の事前定義された IAM ロールが一般提供になりました。詳細については、 [ アクセス制御
](https://cloud.google.com/ml-engine/docs/tensorflow/access-control?hl=ja)
をご覧ください。

##  2017 年 6 月 27 日

**FEATURE:**

TensorFlow 1.2 の Cloud ML Engine ランタイム バージョンがトレーニングと予測に使用できるようになりました。詳細については、
[ ランタイム バージョン リスト ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=ja) をご覧ください。

**DEPRECATED:**

TensorFlow 0.11 および 0.12 の古いランタイム バージョンが Cloud ML Engine
でサポートされなくなりました。詳細については、 [ ランタイム バージョン リスト ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=ja) と [ 古いランタイム バージョンのサポート
タイムライン ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ja#runtime-version-support) をご覧ください。

##  2017 年 5 月 9 日

**FEATURE:**

GPU が有効なマシンの一般提供が発表されました。詳細については、 [ クラウド中のトレーニング モデルに GPU を使用
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ja)
をご覧ください。

##  2017 年 4 月 27 日

**FEATURE:**

GPU は us-central1 リージョンで利用できるようになりました。GPU をサポートするリージョンの一覧については、 [
クラウド内でのモデルのトレーニングに GPU を使用する ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=ja#requesting_gpu-enabled_machines)
をご覧ください。

##  v1（2017 年 3 月 8 日）

**FEATURE:**

AI Platform Training の一般提供を発表しました。Cloud ML Engine のバージョン 1
は、モデルのトレーニング、モデルの導入、バッチ予測の生成に一般的に使用できます。 [ ハイパーパラメータ調整
](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-tuning-
overview?hl=ja) 機能も一般提供になりましたが、オンライン予測と [ GPU 対応マシン
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ja)
はベータ版のままです。

**FEATURE:**

オンラインでの予測は、ベータ版の [ リリース段階 ](https://cloud.google.com/terms/launch-
stages?hl=ja) に入っています。現在、Cloud ML Engine の [ 料金ポリシー
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ja)
の対象となっており、バッチ予測と同じ価格設定式に従います。まだベータ版のままで、オンライン予測は重要なアプリケーションでは使用できません。

**CHANGED:**

Cloud ML Engine をモデルのトレーニングや予測のために使用する環境では、Cloud ML Engine の [ ランタイム バージョン
](https://cloud.google.com/ml-engine/docs/tensorflow/versioning?hl=ja)
として定義されています。トレーニング、モデルリソースの定義、またはバッチ予測の要求時に使用する、サポートされているランタイム
バージョンを指定できます。現時点でのランタイム バージョンの主な違いは、それぞれがサポートしている TensorFlow
のバージョンですが、今後より多くの違いが生じる可能性があります。詳細については、 [ ランタイム バージョン リスト
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ja) をご覧ください。

**CHANGED:**

Google Cloud Storage でモデル バージョンとしてホストされていない Google Cloud Storage に保存されている
TensorFlow SavedModels に対してバッチ予測ジョブを実行できるようになりました。ジョブの作成時にモデルまたはバージョンの ID
を指定する代わりに、SavedModel の URI を使用できます。

**DEPRECATED:**

以前はアルファ版としてリリースされていた Google Cloud Machine Learning SDK は非推奨となり、2017 年 5 月 7
日以降はサポートされなくなります。SDK によって公開されている機能のほとんどは、新しい TensorFlow パッケージ [ tf.Transform
](https://github.com/tensorflow/transform)
に移行されました。どのような技術やツールを使用しても、入力データを前処理できます。ただし、 ` tf.Transform ` とともに、Google
Cloud Platform で使用可能なサービス（Google Cloud Dataflow、Google Cloud Dataproc、Google
BigQuery など）をおすすめしています。

##  v1 ベータ 1（2016 年 9 月 29 日）

**FEATURE:**

オンライン予測はアルファ版機能です。AI Platform Training
全体としてはベータ版のフェーズにありますが、オンライン予測は、性能改善のための重大な変更がいまだ進行中です。アルファ版である間は、オンライン予測には [
課金 ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ja) されません。

**FEATURE:**

前処理とその他の Cloud ML Engine SDK はアルファ版の機能です。Cloud ML Engine と Apache Beam
の統合を進めるため、SDK の開発が積極的に進められています。

