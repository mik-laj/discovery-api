#  セキュリティに関する情報

このトピックでは、Google Kubernetes Engine（GKE）に関するすべてのセキュリティ情報について説明します。

脆弱性に関する情報は多くの場合、影響を受けた当事者が対処するまで、情報制限により非公開となります。このような場合、GKE の [ リリースノート
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=ja)
には、情報制限が解除されるまで「セキュリティ更新」が記載されます。リリースノートは情報制限が解除された時点で更新され、パッチによって対処された脆弱性の情報が反映されます。

**注:** GKE でマルチテナント ワークロードを実行する場合、上記の情報には特に注意してください。これらの脆弱性はマルチテナント
ワークロードに影響を及ぼす可能性が高くなります。GKE のセキュリティ境界とそれによるワークロードへの影響に関する技術的説明については、 [
Kubernetes スタックのさまざまなレイヤでの隔離
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) をご覧ください。

最新のセキュリティ情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、フィード URL `
https://cloud.google.com/feeds/kubernetes-engine-security-bulletins.xml `
を直接追加してください。

##  GCP-2020-005

**公開日:** 2020 年 5 月 7 日  
**最終更新日:** 2020 年 5 月 7 日  説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Linux カーネルに脆弱性 [ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)
が発見されました。この脆弱性により、コンテナがエスケープ処理を行ってホストノードのルート権限を奪ってしまうおそれがあります。

この脆弱性は Google Kubernetes Engine（GKE）1.16 または 1.17 を実行する GKE Ubuntu
ノードに影響するため、できるだけ早く最新のパッチ バージョンにアップグレードすることをおすすめします。詳細については、以下をご覧ください。

コンテナ最適化 OS を実行しているノードは影響を受けません。GKE On-Prem 上で実行しているノードは影響を受けません。

####  必要な対策

**ほとんどのお客様は、以後の対応は必要ありません。GKE バージョン 1.16 または 1.17 の Ubuntu
を実行しているノードのみが影響を受けます。**

ご使用のノードをアップグレードするには、まずマスターを最新バージョンにアップグレードする必要があります。このパッチは Kubernetes
1.16.8-gke.12、1.17.4-gke.10、およびそれ以降のリリースで提供されます。パッチが公開されたかどうかについては、 [ リリースノート
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=ja)
で定期的にご確認ください。

####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) は Linux カーネル バージョン 5.5.0
以降の脆弱性であり、悪意のあるコンテナが（exec 形式での最小限のユーザー
インタラクションで）カーネルメモリの読み取りと書き込みにより、ホストノードでルート権限のコードを実行できるというものです。この脆弱性の重大度評価は高です。

|

高

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP-2020-003

**公開日:** 2020 年 3 月 31 日  
**最終更新日:** 2020 年 3 月 31 日  説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Kubernetes で [ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) に記載された脆弱性が発見されました。これは、POST
リクエストの発行を許可された任意のユーザーが Kubernetes API サーバーへのリモート
サービス拒否攻撃を実行できるというものです。Kubernetes 製品セキュリティ委員会（PSC）から発表されたこの脆弱性に関する追加情報は、 [ こちら
](https://groups.google.com/forum/?hl=ja#!topic/kubernetes-security-
announce/wuwEwZigXBc) からご覧いただけます。

この脆弱性は、 [ マスター承認済みネットワーク ](https://cloud.google.com/kubernetes-
engine/docs/how-to/authorized-networks?hl=ja) と [ パブリック エンドポイントを持たない限定公開クラスタ
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=ja#private_master) を使用した GKE クラスタでは緩和されます。

####  必要な対策

この脆弱性の修正を含むパッチ バージョンにクラスタをアップグレードすることをおすすめします。

修正を含むパッチ バージョンは次のとおりです。

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  このパッチで対処される脆弱性

このパッチは次のサービス拒否攻撃（DoS）の脆弱性を修正します。

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) .

|

中

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**公開日:** 2020 年 3 月 23 日  
**最終更新日:** 2020 年 3 月 23 日  説明  |  重大度  |  注  
---|---|---  
  
Kubernetes は [ サービス拒否攻撃の脆弱性を 2 件
](https://groups.google.com/forum/?hl=ja#!topic/kubernetes-security-
announce/2UOlsba2g0s) 公表しました。そのうちの 1 件は API サーバーに影響するもので、もう 1 件は Kubelet
に影響するものです。詳細については Kubernetes の問題 [ 89377
](https://github.com/kubernetes/kubernetes/issues/89377) と [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) をご覧ください。

####  必要な対策

クラスタの内部ネットワーク内で信頼されていないユーザーによるリクエスト送信が許可されていない限り、すべての GKE ユーザーは CVE-2020-8551
から保護されます。 [ マスター承認済みネットワーク ](https://cloud.google.com/kubernetes-
engine/docs/how-to/authorized-networks?hl=ja) を使うことで、CVE-2020-8552
の影響をさらに緩和できます。

####  パッチのリリース予定

CVE-2020-8551 のパッチにはノードのアップグレードが必要です。この脆弱性の緩和策が組み込まれるパッチ バージョンは次のとおりです。

  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

注: 1.14.x より前のバージョンはこの脆弱性の影響を受けないため、パッチを適用する必要はありません。

CVE-2020-8552 用のパッチではマスターのアップグレードが必要です。この脆弱性の緩和策が組み込まれるパッチ バージョンは次のとおりです。

  * 1.14.10-gke.32 
  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

|

中

|

[ CVE-2020-8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE-2020-8552 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  2020 年 1 月 21 日、最終更新日 2020 年 1 月 24 日

**公開日:** 2020 年 1 月 21 日  
**最終更新日:** 2020 年 1 月 24 日  説明  |  重大度  |  注  
---|---|---  
  
**2020 年 1 月 24 日更新:** パッチ適用済みバージョンを現在作成中で、2020 年 1 月 25 日までに完成する予定です。

* * *

Microsoft が Windows Crypto API とその楕円曲線署名の検証に脆弱性があることを公表しました。詳細については、 [
Microsoft の開示情報 ](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) をご覧ください。

**必要な対策**

**ほとんどのお客様は、以後の対応は必要ありません。Windows Server を実行しているノードのみが影響を受けます。**

Windows Server
ノードを使用している場合は、この脆弱性を軽減するために、ノードとそれらのノード上で実行されるコンテナ化されたワークロードの両方をパッチ適用済みバージョンに更新する必要があります。

**コンテナを更新するには:**

Microsoft の最新のベースコンテナ イメージを使用してコンテナを再ビルドします。その際、LastUpdated Time が 2020/1/14
またはそれ以降である [ servercore ](https://hub.docker.com/_/microsoft-windows-
servercore) または [ nanoserver ](https://hub.docker.com/_/microsoft-windows-
nanoserver) タグを選択してください。

**ノードを更新するには:**

パッチ適用済みバージョンを現在作成中で、2020 年 1 月 24 日までに完成する予定です。

パッチが完成してからパッチ適用済みの GKE バージョンにノードをアップグレードするか、任意の時点で Windows Update を使用して最新の
Windows パッチを手動で適用してください。

この脆弱性の緩和策が組み込まれるパッチ バージョンは次のとおりです。

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**このパッチで対処される脆弱性**

このパッチで緩和される脆弱性は以下のとおりです。

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) \- この脆弱性は [ Windows Crypto API のなりすましの脆弱性
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601)
とも呼ばれます。これを悪用すると、悪意ある実行可能ファイルを信頼されたもののように見せかけることができます。また、攻撃者が中間者攻撃を行って標的ソフトウェアへの
TLS 接続上で秘密情報を復号することも可能です。

|

NVD ベーススコア: 8.1（高）

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  2019 年 11 月 14 日

**公開日:** 2019 年 11 月 14 日  
**最終更新日:** 2019 年 11 月 14 日  説明  |  重大度  |  注  
---|---|---  
  
kubernetes-csi の [ ` external-provisioner ` ](https://github.com/kubernetes-
csi/external-provisioner) 、 [ ` external-snapshotter `
](https://github.com/kubernetes-csi/external-snapshotter) 、 [ ` external-
resizer ` ](https://github.com/kubernetes-csi/external-resizer) の各サイドカーに、 [
Container Storage Interface（CSI）ドライバ ](https://kubernetes-
csi.github.io/docs/drivers.html)
にバンドルされたサイドカーのほとんどのバージョンに影響を与えるセキュリティ問題があることが公表されました。詳細については、 [ Kubernetes
の開示情報 ](https://github.com/kubernetes/kubernetes/issues/85233) をご覧ください。

**必要な対策**  
**この脆弱性は、マネージド GKE コンポーネントには影響しません** 。GKE バージョン 1.12 以降を実行している [ GKE アルファ クラスタ
](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-
clusters?hl=ja) でお客様自身が独自の CSI
ドライバを管理している場合は、この脆弱性の影響を受ける可能性があります。これに該当する場合は、ご利用の CSI
ドライバのベンダーから提供されたアップグレードの指示をご覧ください。

**このパッチで対処される脆弱性**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : この CVE は、 ` kubernetes-csi ` の [ `
external-provisioner ` ](https://github.com/kubernetes-csi/external-
provisioner) 、 [ ` external-snapshotter ` ](https://github.com/kubernetes-
csi/external-snapshotter) 、 [ ` external-resizer `
](https://github.com/kubernetes-csi/external-resizer) の各サイドカーでボリューム
データに不正にアクセスできる、またはボリューム データをミューテーションできるという脆弱性です。これは、 [ CSI ドライバ
](https://kubernetes-csi.github.io/docs/drivers.html)
にバンドルされたサイドカーのほとんどのバージョンに影響します。

|

中

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  2019 年 11 月 12 日

**公開日:** 2019 年 11 月 12 日  
**最終更新日:** 2019 年 11 月 12 日  説明  |  重大度  |  注  
---|---|---  
  
Intel により、マイクロアーキテクチャ状態での投機的実行の操作を通じてデータが公開される可能性がある CVE が公表されました。詳細については、 [
Intel の開示情報 ](https://blogs.intel.com/technology/2019/11/ipas-
november-2019-intel-platform-update-ipu/) をご覧ください。

**Kubernetes Engine を実行するホスト インフラストラクチャは、お客様のワークロードを分離します。お客様自身が独自のマルチテナント GKE
クラスタ内で信頼できないコードを実行していて、なおかつ __ N2、M2、C2 ノードのいずれかを使用している場合を除き、特に対応する必要はありません。
** N1 ノード上の GKE インスタンスについては、新たな対策は不要です。

Anthos GKE On-Prem を実行している場合、漏洩の可能性があるかどうかはハードウェアによります。ご利用のインフラストラクチャを [ Intel
の開示情報 ](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) と比較してください。

####  必要な対策

**影響を受けるのは、N2、M2、または C2 ノードを含むノードプールを使用していて、なおかつ __ 独自のマルチテナント GKE
クラスタ内のそれらのノードで信頼できないコードを実行している場合だけです。 **

**ノードを再起動すると、パッチが適用されます。** ノードプール内のすべてのノードを再起動する最も簡単な方法は、 [ upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ja#upgrade_nodes) オペレーションを使用して対象となるすべてのノードプールを強制的に再起動することです。  

注: アップグレード中にバージョンを変更する必要はありません。 ` cluster-version ` フラグを使用して、同じノード
バージョンへのアップグレードを開始できます。

####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
: この CVE は TSX 非同期アボート（TAA）とも呼ばれます。TAA により、 [ マイクロアーキテクチャ データ サンプリング（MDS）
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins?hl=ja#may-14-2019) で悪用されていたのと同じマイクロアーキテクチャ
データ構造を使用してデータを引き出すことも可能になります。

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
:
これは仮想マシンホストを対象としたサービス拒否攻撃（DoS）の脆弱性であり、悪意のあるゲストが保護されていないホストをクラッシュさせることができるというものです。この
CVE は「ページサイズ変更時のマシンチェック エラー」とも呼ばれます。これは GKE には影響しません。

|

中

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  2019 年 10 月 22 日

**公開日:** 2019 年 10 月 22 日  
**最終更新日:** 2019 年 10 月 22 日  説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Go プログラミング言語で [ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) に記載された脆弱性が発見されました。この脆弱性は、認証プロキシを使用した
Kubernetes 構成に影響する可能性があります。詳細については、 [ Kubernetes の開示情報
](https://groups.google.com/forum/?hl=ja#!topic/kubernetes-security-
announce/PtsUCqFi4h4) をご覧ください。

Kubernetes Engine では認証プロキシの構成は許可されていないため、この脆弱性の影響は受けません。

|

なし

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  2019 年 10 月 16 日

**公開日:** 2019 年 10 月 16 日  
**最終更新日:** 2019 年 10 月 24 日  説明  |  重大度  |  注  
---|---|---  
  
**2019 年 10 月 24 日更新:** パッチ適用済みバージョンがすべてのリージョンで入手できるようになりました。

* * *

先ごろ、Kubernetes で [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) に記載された脆弱性が発見されました。これは、POST
リクエストの発行を許可された任意のユーザーが Kubernetes API サーバーへのリモート
サービス拒否攻撃を実行できるというものです。Kubernetes 製品セキュリティ委員会（PSC）から発表されたこの脆弱性に関する追加情報は、 [ こちら
](https://groups.google.com/forum/?hl=ja#!topic/kubernetes-security-
announce/jk8polzSUxs) からご覧いただけます。

この脆弱性は、 [ マスター承認済みネットワーク ](https://cloud.google.com/kubernetes-
engine/docs/how-to/authorized-networks?hl=ja) と [ パブリック エンドポイントを持たない限定公開クラスタ
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=ja#private_master) を使用した GKE クラスタでは緩和されます。

######  必要な対策

修正を含むパッチ バージョンが公開されたら、直ちにクラスタをそのバージョンにアップグレードすることをおすすめします。このパッチ バージョンは、10 月 14
日の週にすべてのゾーンで GKE リリースとともに提供される予定です。

この脆弱性の緩和策が組み込まれるパッチ バージョンは次のとおりです。

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

CVE-2019-11253 はサービス拒否攻撃（DoS）の脆弱性です。

|

高

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  2019 年 9 月 16 日

**公開日:** 2019 年 9 月 16 日  
**最終更新日:** 2019 年 10 月 16 日  説明  |  重大度  |  注  
---|---|---  
  
このセキュリティ情報は当初の発表時から更新されました。

先ごろ、Go プログラミング言語で新たなセキュリティ上の脆弱性 [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) と [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514)
が発見されました。これらはサービス拒否攻撃（DoS）を受ける可能性があるというものです。GKE では、悪意のあるユーザーがこの脆弱性を利用して
Kubernetes API サーバーの CPU を大量に消費するリクエストを送りつけ、クラスタ コントロール
プレーンの可用性を低下させるおそれがあります。詳細については、 [ Go プログラミング言語の開示情報
](https://groups.google.com/forum/?hl=ja#!topic/golang-announce/65QixT3tcmg)
をご覧ください。

######  必要な対策

この脆弱性の緩和策が組み込まれた最新のパッチ バージョンが公開されたら、直ちにクラスタをそのバージョンにアップグレードすることをおすすめします。このパッチ
バージョンは、 [ このリリース スケジュール ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=ja#september_16_2019) に従って、すべてのゾーンで次回の GKE
リリースとともに提供される予定です。

この脆弱性の緩和策が組み込まれるパッチ バージョンは次のとおりです。

  * **2019 年 10 月 16 日更新:** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) と [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514)
はサービス拒否攻撃（DoS）の脆弱性です。

|

高

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  2019 年 9 月 5 日

**公開日:** 2019 年 9 月 5 日  
**最終更新日:** 2019 年 9 月 5 日

2019 年 5 月 31 日付け  のセキュリティ情報に記載された脆弱性の修正に関する情報が更新されました。

##  2019 年 8 月 22 日

**公開日:** 2019 年 8 月 22 日  
**最終更新日:** 2019 年 8 月 22 日

2019 年 8 月 5 日付け  のセキュリティ情報が更新されました。先日のセキュリティ情報に記載された脆弱性の修正が [ 公開
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=ja#august_22_2019) されました。

##  2019 年 8 月 8 日

**公開日:** 2019 年 8 月 8 日  
**最終更新日:** 2019 年 8 月 8 日

2019 年 8 月 5 日付け  のセキュリティ情報が更新されました。このセキュリティ情報に記載された脆弱性の修正は次回の GKE
リリースとともに提供される予定です。

##  2019 年 8 月 5 日

**公開日:** 2019 年 8 月 5 日  
**最終更新日:** 2019 年 8 月 9 日  説明  |  重大度  |  注  
---|---|---  
  
このセキュリティ情報は当初の発表時から更新されました。

先ごろ、Kubernetes で脆弱性 [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) が発見されました。これは、クラスタ スコープの [ カスタム リソース
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) インスタンスを、あたかもすべての Namespace
に存在する名前空間オブジェクトであるかのように動作させることができるというものです。つまり、名前空間レベルの RBAC 権限しか持たないユーザー
アカウントまたはサービス アカウントでも、クラスタ スコープのカスタム リソースとやり取りできてしまいます。攻撃者がこの脆弱性を悪用するためには、任意の
Namespace のリソースにアクセスする権限が必要です。

######  必要な対策

この脆弱性の緩和策が組み込まれた最新のパッチ バージョンが公開されたら、直ちにクラスタをそのバージョンに [ アップグレード
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ja) することをおすすめします。このパッチ バージョンは、すべてのゾーンで次回の GKE
リリースとともに公開される予定です。この脆弱性の緩和策が組み込まれるパッチ バージョンは次のとおりです。

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10（ [ Rapid チャンネル ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=ja) ） 

######  このパッチで対処される脆弱性

このパッチにより、次の脆弱性が緩和されます。 [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) 。

|

中

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  2019 年 7 月 3 日

**公開日:** 2019 年 7 月 3 日  
**最終更新日:** 2019 年 7 月 3 日  説明  |  重大度  |  注  
---|---|---  
  
CVE-2019-11246 に対処する ` kubectl ` のパッチ適用済みバージョンが [ ` gcloud ` 253.0.0
](https://cloud.google.com/sdk/docs/release-notes?hl=ja#kubernetes_engine)
で提供されました。詳細については、  2019 年 6 月 25 日付けのセキュリティ情報  をご覧ください。

**注:** このパッチは ` kubectl ` 1.11.10 では提供されていません。

|

高

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  2019 年 7 月 3 日

**公開日:** 2019 年 6 月 25 日  
**最終更新日:** 2019 年 7 月 3 日  説明  |  重大度  |  注  
---|---|---  
  
######  2019 年 7 月 3 日更新

前回の更新の時点では、バージョン 1.11.9 と 1.11.10 のパッチはまだ公開されていませんでした。両方の 1.11 バージョンのアップグレード
ターゲットとして、1.11.10-gke.5 がリリースされました。

現時点で、GKE マスターにはすでにパッチが適用されています。また、Kubernetes Engine を実行する Google
インフラストラクチャにもパッチが適用され、この脆弱性から保護されています。

1.11 マスターはまもなくサポートが終了し、2019 年 7 月 8 日の週に自動的に 1.12
にアップグレードされる予定です。パッチ適用済みバージョンにノードが導入されるようにするため、次の推奨される対応の中からいずれかをお選びください。

  * 2019 年 7 月 8 日までにノードを 1.11.10-gke.5 にアップグレードする。この日付以降、1.11 バージョンは使用可能なアップグレード ターゲットのリストから削除されます。 
  * 1.11 ノードで [ 自動アップグレード ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=ja) を有効にし、マスターが 1.12 にアップグレードされたときにノードもアップグレードされるようにする。 
  * マスターとノードの両方を修正済みの 1.12 バージョンに [ 手動でアップグレードする ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=ja) 。 

2019 年 6 月 24 日に公開された当初のセキュリティ情報は次のとおりです。

* * *

######  2019 年 6 月 24 日更新

2019 年 6 月 22 日 21:40 UTC の時点で、以下のパッチ適用済み Kubernetes バージョンが公開されました。1.11.0 から
1.13.6 までの Kubernetes
バージョンのマスターは、パッチ適用済みバージョンに自動的にアップデートされます。現在ご利用のバージョンがこのパッチと互換性がない場合は、ノードをアップグレードする前に、互換性のあるマスター
バージョン（下記のリストを参照）にアップグレードしてください。

**これらの脆弱性は重大度が高いため、ノードの自動アップグレードを有効にしているかどうかにかかわらず、できるだけ早くノードとマスターの両方をこれらのいずれかのバージョンに[
手動でアップグレード ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-
a-container-cluster?hl=ja) することをおすすめします。 **

パッチ適用済みバージョン:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

2019 年 6 月 18 日に公開された当初のセキュリティ情報は次のとおりです。

* * *

先ごろ Netflix は、Linux カーネルにおける 3 件の TCP の脆弱性を公表しました。

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

これらの CVE は [ NFLX-2019-001 ](https://github.com/Netflix/security-
bulletins/blob/master/advisories/third-party/2019-001.md) と総称されます。

パッチが適用されていない Linux カーネルは、リモートから開始されたサービス拒否攻撃を受ける可能性があります。 **信頼されていないネットワーク
トラフィックを送受信する Google Kubernetes Engine
ノードは、この脆弱性の影響を受けます。そのため、以下の緩和策に従ってワークロードを保護することをおすすめします。**

######  Kubernetes マスター

  * [ 承認済みネットワーク ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=ja) を使用してトラフィックを信頼されているネットワークのみに制限している Kubernetes マスターは、影響を受けません。 

  * Google によって管理されている GKE クラスタのマスターは、近日中に自動的にパッチが適用されます。お客様による対応は必要ありません。 

######  Kubernetes ノード

トラフィックを信頼されているネットワークのみに制限しているノードは影響を受けません。これには、次のものを含むクラスタが該当します。

  * ファイアウォールによって信頼されていないネットワークから保護されているノード、またはパブリック IP を持たないノード（ [ 限定公開クラスタ ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=ja) ） 
  * パブリックの LoadBalancer サービスを使用していないクラスタ 

Google ではこれらの脆弱性に対する恒久的な緩和策を準備しており、新しいノード
バージョンで提供される予定です。恒久的な修正が公開されたら、このセキュリティ情報を更新し、GKE をご利用のすべてのお客様にメールを送信いたします。

恒久的な修正が公開されるまでの一時的な措置として、ホストの ` iptables ` 構成を変更することで緩和策を実装する Kubernetes
DaemonSet を作成しました。

#####  必要な対策

次のコマンドを実行して、クラスタ内のすべてのノードに Kubernetes DaemonSet を適用します。これにより、この脆弱性を緩和する `
iptables ` ルールがノードの既存の ` iptables ` ルールに追加されます。 **このコマンドは、それぞれの Google Cloud
プロジェクトのクラスタごとに 1 回ずつ実行してください。**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

Ipv6 は GKE でサポートされていないため、ip6tables ルールは必要ありません。

パッチ適用済みのノード バージョンが公開され、影響を受ける可能性のあるすべてのノードのアップグレードが完了したら、次のコマンドを使用して DaemonSet
を削除できます。 **このコマンドは、それぞれの Google Cloud プロジェクトのクラスタごとに 1 回ずつ実行してください。**

    
    
    
    kubectl delete -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

|  高  
中  
中  
|  [ CVE-2019-11477 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
  
  
##  2019 年 6 月 25 日

説明  |  重大度  |  注  
---|---|---  
  
**2019 年 7 月 3 日更新:** このパッチは、 ` kubectl ` バージョン
1.12.9、1.13.6、1.14.2、およびそれ以降のリリース用の ` gcloud ` 253.0.0 に含まれています。

**注:** このパッチは 1.11.10 では提供されていません。

* * *

先ごろ、Kubernetes で脆弱性 [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) が発見されました。これは、 ` kubectl cp `
のオペレーションへのアクセスとコンテナ内のコード実行が可能な攻撃者がホスト上のファイルを変更できるというものです。攻撃者はこの脆弱性を悪用して、ホストのファイル
システムにファイルを作成したり、既存のファイルを置き換えたりすることができます。詳細については、 [ Kubernetes の開示情報
](https://groups.google.com/forum/?hl=ja#!topic/kubernetes-security-
announce/NLs2TGbfPdo) をご覧ください。

**この脆弱性は、Google Kubernetes Engine（GKE）のすべての` gcloud ` バージョンに影響します。 ` gcloud `
の最新のパッチ バージョンが公開されたら、そのバージョンにアップグレードすることをおすすめします。 ** 近日中に公開されるパッチ
バージョンには、この脆弱性の緩和策が組み込まれます。

######  必要な対策

今後の ` gcloud ` のリリースでは、 ` kubectl ` のパッチ適用済みバージョンが提供されます。ご自身で [ ` kubectl `
を直接アップグレード ](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
することもできます。

このパッチが公開されたかどうかについては、 [ ` gcloud ` のリリースノート
](https://cloud.google.com/sdk/docs/release-notes?hl=ja) で定期的にご確認ください。

######  このパッチで対処される脆弱性

脆弱性 [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) は、 ` kubectl cp `
オペレーションへのアクセスとコンテナ内のコード実行が可能な攻撃者がホスト上のファイルを変更できるというものです。攻撃者はこの脆弱性を悪用して、ホストのファイル
システムにファイルを作成したり、既存のファイルを置き換えたりすることができます。

|

高

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  2019 年 6 月 18 日

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Docker で脆弱性 [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) が発見されました。これは、コンテナ内のコード実行が可能な攻撃者が外部から開始された
` docker cp ` オペレーションをハイジャックできるというものです。攻撃者はこの脆弱性を悪用して、ファイルの書き込み先をホストのファイル
システム上の任意の場所に変更できます。

**この脆弱性は、Docker を実行するすべての Google Kubernetes Engine（GKE）ノードに影響します。最新のパッチ
バージョンが公開されたら、そのバージョンにアップグレードすることをおすすめします。近日中に公開されるパッチ
バージョンには、この脆弱性の緩和策が組み込まれます。**

**バージョン 1.12.7 より前の Google Kubernetes Engine（GKE）マスターはすべて Docker
を実行するため、この脆弱性の影響を受けます。** GKE のユーザーはマスター上の ` docker cp ` に対するアクセス権がないため、GKE
マスターに対するこの脆弱性のリスクは限られます。

#####  必要な対策

影響を受けるのは、Docker を実行しているノードでハイジャック可能な ` docker cp ` コマンド（またはこれに相当する
API）が発行されたときだけに限定されます。これは Kubernetes 環境ではかなりまれであると考えられます。 [ containerd を含む COS
](https://cloud.google.com/kubernetes-engine/docs/concepts/using-
containerd?hl=ja) を実行しているノードは影響を受けません。

ノードをアップグレードするには、まずマスターをパッチ適用済みバージョンに [ アップグレード
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ja#upgrading_the_cluster)
する必要があります。パッチが公開されたら、マスターのアップグレードを手動で開始するか、Google
によって自動的にマスターがアップグレードされるまで待ちます。パッチは Docker 18.09.7 で提供されます。これは近日中に公開される GKE
パッチに含まれます。 **このパッチは GKE バージョン 1.13 以降でのみ提供されます。**

クラスタ マスターは、定期的なアップグレード
サイクルの一環としてパッチ適用済みバージョンに自動的にアップグレードされます。また、パッチ適用済みバージョンが公開された後、お客様自身でマスターのアップグレードを開始することもできます。

パッチが公開されたら、このセキュリティ情報が更新されてパッチを含むバージョンが追記されます。パッチが公開されたかどうかについては、 [ リリースノート
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=ja)
で定期的にご確認ください。

#####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

脆弱性 [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) は、コンテナ内のコード実行が可能な攻撃者が外部から開始された ` docker
cp ` オペレーションをハイジャックできるというものです。攻撃者はこの脆弱性を悪用して、ファイルの書き込み先をホストのファイル
システム上の任意の場所に変更できます。

|  高  |  
  
##  2019 年 5 月 31 日

説明  |  重大度  |  注  
---|---|---  
  
このセキュリティ情報は当初の発表時から更新されました。

######  2019 年 8 月 2 日更新

最初にセキュリティ情報を公開した時点では、影響を受けるバージョンは 1.13.6-gke.0 から 1.13.6-gke.5
までに限られていました。現時点では、回帰の影響で、すべての 1.13.6.x バージョンが影響を受けます。現在ご利用のバージョンが 1.13.6
の場合は、できるだけ早く 1.13.7 にアップグレードしてください。

Kubernetes プロジェクトにより、kubelet v1.13.6 と v1.14.2 で [ CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) が公表されました。これはコンテナを
UID 0（通常は ` root ` ユーザーにマップされている）として実行できるという脆弱性であり、コンテナ
イメージで別のユーザーが指定されている場合でも UID 0 として実行できます。 **コンテナを root
以外のユーザーとして実行していて、実行しているノードのバージョンが 1.13.6-gke.0～1.13.6-gke.6 である場合は、UID 0
として実行してはならないコンテナを含むクラスタ上のすべてのポッドで` RunAsUser ` を設定することをおすすめします。 **

root 以外の ` USER ` 値が指定されている（たとえば、Dockerfile で ` USER `
の値を設定するなど）場合は、予期しない動作が起こります。あるノードであるコンテナが初めて実行されるときは、指定された UID
が正しく使用されます。しかし、この不具合により、2 回目以降の実行では、指定されている UID にかかわらず UID 0
としてコンテナが実行されます。これは通常、望ましくないエスカレーションされた権限であり、アプリケーションの予期しない動作につながる可能性があります。

#####  実行中のバージョンが対象のバージョンかどうかを確認する方法

次のコマンドを実行して、すべてのノードとその kubelet バージョンの一覧を表示します。

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

出力に以下の kubelet バージョンが示された場合、そのノードはこの脆弱性の影響を受けます。

  * v1.13.6 
  * v1.14.2 

#####  特定の構成が影響を受けるかどうかを確認する方法

コンテナを root 以外のユーザーとして実行していて、実行しているノードのバージョンが 1.13.6-gke.0～1.13.6-gke.6
である場合は、この脆弱性の影響を受けます。ただし、以下の場合は除きます。

  * ` runAsUser ` PodSecurityContext に有効な root 以外の値が指定されているポッドは影響を受けず、引き続き正常に動作します。 
  * ` runAsUser ` の設定を強制する PodSecurityPolicy も影響を受けず、引き続き正常に動作します。 
  * ` mustRunAsNonRoot:true ` が指定されたポッドは UID 0 として起動することはありませんが、この問題の影響を受けた場合は起動できません。 

#####  必要な対策

UID 0 として実行してはならないクラスタ上のすべてのポッドで、 [ RunAsUser セキュリティ コンテキスト
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) を設定します。この構成は [ PodSecurityPolicy
](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)
を使用して適用できます。

|  中  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  2019 年 5 月 14 日

説明  |  重大度  |  注  
---|---|---  
  
**2019 年 6 月 11 日更新:** 2019 年 5 月 28 日の週にリリースされた
1.11.10-gke.4、1.12.8-gke.6、1.13.6-gke.5 とそれ以降のリリースでパッチが提供されました。

次の CVE が Intel により公表されました。

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

これらの CVE はマイクロアーキテクチャ データ
サンプリング（MDS）と総称されます。これらの脆弱性により、マイクロアーキテクチャ状態での投機的実行の操作を通じてデータが公開される可能性があります。詳細については、
[ Intel の開示情報 ](https://www.intel.com/content/www/us/en/security-
center/advisory/intel-sa-00233.html) をご覧ください。

**Kubernetes Engine を実行するホスト インフラストラクチャは、お客様のワークロードを相互に分離します。独自のマルチテナント GKE
クラスタ内で信頼できないコードを実行していない限り、これらの脆弱性の影響は受けません。**

**Kubernetes Engine 内の独自のマルチテナント サービスで信頼できないコードを実行している場合、これは特に重大な脆弱性となります。**
Kubernetes Engine でこれを緩和するため、ノードでハイパー スレッディングを無効にしてください。これらの脆弱性の影響を受けるのは、複数の
CPU を使用している Google Kubernetes Engine（GKE）ノードのみです。n1-standard-1（GKE
のデフォルト）、g1-small、f1-micro の各 VM でゲスト環境に公開される vCPU は 1 つだけなので、ハイパー
スレッディングを無効にする必要はありません。

近日中に公開される [ パッチ バージョン ](https://cloud.google.com/kubernetes-engine/release-
notes?hl=ja) では、追加の保護対策としてフラッシュ機能を有効にできるようになります。マスターとノードは、定期的なアップグレード
サイクルの一環として数週間以内にパッチ適用済みバージョンに自動的にアップグレードされます。
**パッチだけでは、この脆弱性の影響を緩和するのに十分ではありません。推奨される対応については、下記をご覧ください。**

GKE On-Prem を実行している場合、これらの脆弱性の影響を受けるかどうかは使用しているハードウェアによります。 [ Intel の開示情報
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) をご覧ください。

####  必要な対策

**独自のマルチテナント GKE クラスタ内で信頼できないコードを実行していない限り、これらの脆弱性の影響は受けません。**

**Kubernetes Engine のノード用に、ハイパー
スレッディングを無効にした新しいノードプールを作成し、ワークロードのスケジュールを新しいノードに設定し直します。**

n1-standard-1、g1-small、f1-micro の各 VM でゲスト環境に公開される vCPU は 1 つだけなので、ハイパー
スレッディングを無効にする必要はありません。

**警告:**

  * ハイパー スレッディングを無効にすると、クラスタとアプリケーションのパフォーマンスが大幅に低下する可能性があります。本番環境クラスタにこれを実装する前に、ハイパー スレッディングを無効にしても問題ないか確認してください。 
  * ハイパー スレッディングは、DaemonSet をデプロイすることで GKE ノードプール レベルで無効にできます。ただし、この DaemonSet をデプロイすると、ノードプールに含まれるすべてのノードが同時に再起動されます。したがって、クラスタに新しいノードプールを作成し、ハイパー スレッディングを無効にする DaemonSet をそのノードプールにデプロイしてから、ワークロードを新しいノードプールに移行することをおすすめします。 

ハイパー スレッディングを無効にした新しいノードプールを作成するには:

  1. ノードラベル ` cloud.google.com/gke-smt-disabled=true ` を使用して、クラスタに新しいノードプールを作成します。 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. この新しいノードプールに DaemonSet をデプロイします。この DaemonSet は、 ` cloud.google.com/gke-smt-disabled=true ` ラベルが付いているノードでのみ実行されます。これにより、ハイパー スレッディングが無効化された後、ノードが再起動されます。 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. DaemonSet ポッドが実行状態にあることを確認します。 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

次のようなレスポンスが返されれば問題ありません。

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. ポッドのログに「SMT has been disabled」と記録されていることを確認します。 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

注: ノードで [セキュアブート]（/kubernetes-engine/docs/how-to/shielded-gke-
nodes#secure_boot）機能が有効になっている場合、ブート
オプションは変更できません。セキュアブートが有効の場合、[無効]（/kubernetes-engine/docs/how-to/shielded-gke-
nodes#disabling）に変更してから DaemonSet を作成する必要があります。

この DaemonSet
をノードプールで実行し続ける必要があります。これにより、プールで作成された新しいノードにも自動的に変更が適用されます。ノードの作成は、ノードの自動修復、手動アップグレード、自動アップグレード、自動スケーリングによってトリガーされます。

ハイパー スレッディングを再び有効にするには、用意された DaemonSet
をデプロイせずにノードプールを再作成し、ワークロードを新しいノードプールに移行する必要があります。

また、パッチが公開された後、ノードを手動でアップグレードすることをおすすめします。アップグレードするには、まずマスターを最新バージョンに [ アップグレード
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ja#upgrading_the_cluster) する必要があります。GKE マスターは、定期的なアップグレード
サイクルの一環として自動的にアップグレードされます。

パッチが公開されたら、このセキュリティ情報が更新されてパッチを含むバージョンが追記されます。

####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
、 [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) 、 [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) 、 [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091) :
これらの脆弱性は投機的実行を悪用します。これらの CVE はマイクロアーキテクチャ データ
サンプリングと総称されます。これらの脆弱性により、マイクロアーキテクチャ状態での投機的実行の操作を通じてデータが公開される可能性があります。  |  中
|

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  2019 年 4 月 5 日

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、セキュリティ上の脆弱性 [ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) と [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) が [ Envoy
](https://www.envoyproxy.io/) で発見されました。

[ Istio ](https://istio.io/) には Envoy が組み込まれており、これらの脆弱性の影響で場合によっては Istio
ポリシーがバイパスされる危険性があります。

Google Kubernetes Engine（GKE）で Istio を有効にしている場合、これらの脆弱性の影響を受ける可能性があります。
**できるだけ早く対象のクラスタを最新のパッチ バージョンにアップグレードすることと、Istio
サイドカーをアップグレードすることをおすすめします（手順は後述します）。**

####  必要な対策

**これらの脆弱性は重大度が高いため、ノードの自動アップグレードを有効にしているかどうかにかかわらず、以下のことを行うことをおすすめします。**

  1. **パッチが公開されたら直ちにクラスタを[ 手動でアップグレード ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=ja) する。 **
  2. **[ サイドカーのアップグレードに関するドキュメント ](https://istio.io/docs/setup/kubernetes/upgrade/steps/#sidecar-upgrade) に従って、サイドカーをアップグレードする。 **

パッチ適用済みバージョンは、本日午後 7:00 PDT までにすべての GKE プロジェクトに対して公開される予定です。

このパッチは以下の GKE バージョンで使用できます。GKE セキュリティ情報ページでパッチ適用済みバージョンが発表された後（2019 年 4 月 15
日を予定）、新しいクラスタではそのバージョンがデフォルトで使用されます。それより前に新しいクラスタを作成する場合は、パッチ適用済みバージョンを明示的に指定する必要があります。
[ ノードの自動アップグレード ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-
auto-upgrades?hl=ja)
を有効にしていて、手動でアップグレードしない場合は、次の週にノードがパッチ適用済みバージョンに自動的にアップグレードされます。

パッチ適用済みバージョン:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) と [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)
。これらの脆弱性の詳細については、 [ Istio のブログ ](https://istio.io/blog/2019/announcing-1.1.2)
をご覧ください。

|  高  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901. ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  2019 年 3 月 1 日

説明  |  重大度  |  注  
---|---|---  
  
**2019 年 3 月 22 日更新:** このパッチは、Kubernetes
1.11.8-gke.4、1.13.4-gke.1、およびそれ以降のリリースで提供されています。1.12
ではまだ提供されていません。パッチが公開されたかどうかについては、 [ リリースノート
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=ja#march_19_2019) で定期的にご確認ください。

先ごろ、Kubernetes で新しいサービス拒否攻撃の脆弱性 [ CVE-2019-1002100
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1002100)
が発見されました。これは、パッチ リクエストの発行を許可されたユーザーが、Kubernetes API サーバーの CPU
とメモリを大量に消費する悪意ある「json-patch」リクエストを作成できるというもので、クラスタ コントロール
プレーンの可用性を低下させるおそれがあります。詳細については、 [ Kubernetes の開示情報
](https://groups.google.com/forum/?hl=ja#!topic/kubernetes-
announce/vmUUNkYfG9g) をご覧ください。 **この脆弱性の影響を受けるのは、すべての Google Kubernetes
Engine（GKE）マスターです。近日中に公開されるパッチ バージョンには、この脆弱性の緩和策が組み込まれます。クラスタ
マスターは、定期的なアップグレード サイクルの一環として数週間以内にパッチ適用済みバージョンに自動的にアップグレードされます。**

####  必要な対策

**お客様による対応は必要ありません。GKE マスターは、定期的なアップグレード サイクルの一環として自動的にアップグレードされます。**
マスターをすぐにアップグレードすることをご希望の場合は、 [ 手動でマスター アップグレードを開始
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ja#upgrading_the_cluster) することもできます。

パッチが公開されたら、このセキュリティ情報が更新されてパッチを含むバージョンが追記されます。パッチが提供されるのはバージョン 1.11
以降に対してのみであることにご注意ください。1.10 用のパッチは提供されません。

####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

脆弱性 [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) は、ユーザーが Kubernetes API サーバーの CPU
とメモリを大量に消費する悪意ある「json-patch」型のパッチを作成できるというもので、クラスタ コントロール
プレーンの可用性を低下させるおそれがあります。

|  中  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  2019 年 2 月 11 日（runc）

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Open Containers Initiative（OCI）によって runc に新しいセキュリティ上の脆弱性 [ CVE-2019-5736
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=ja#!topic/dev/Tc1ELm-8oDI)
が [ 発見されました ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736)
。これは、コンテナがエスケープ処理によってホストノードのルート権限を奪ってしまうおそれがあります。

**この脆弱性の影響を受けるのは Google Kubernetes Engine（GKE）Ubuntu ノードです。Ubuntu
ノードをご利用のお客様は、できるだけ早く最新のパッチ バージョンに[ アップグレード
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ja) することをおすすめします。詳細については、以下をご覧ください。 **

####  必要な対策

ご使用のノードをアップグレードするには、まずマスターを最新バージョンにアップグレードする必要があります。このパッチは Kubernetes
1.10.12-gke.7、1.11.6-gke.11、1.11.7-gke.4、1.12.5-gke.5、およびそれ以降のリリースで入手できます。パッチの提供状況については、
[ リリースノート ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=ja#february-11-2019) をご覧ください。

影響を受けるのは GKE の Ubuntu ノードだけです。COS を実行しているノードは影響を受けません。

新しいバージョンの runc はメモリ使用量が以前より増加しているため、メモリ上限を低く（16 MB
未満に）設定している場合はコンテナに割り当てられるメモリを更新しなければならないことがあります。

####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

[ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) は runc の脆弱性であり、悪意のあるコンテナが（exec
形式での最小限のユーザー インタラクションで）ホストの runc
バイナリを上書きすることにより、ホストノードでルート権限のコードを実行できるというものです。root
として実行されていないコンテナは影響を受けません。この脆弱性の重大度評価は高です。

|  高  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  2019 年 2 月 11 日（Go）

説明  |  重大度  |  注  
---|---|---  
  
**2019 年 2 月 25 日更新:** すでにお知らせしたように、1.11.7-gke.4 用のパッチはまだ提供されていません。1.11.7
をご利用のお客様は、次のいずれかをお選びいただけます。1.11.6 にダウングレードする、1.12 にアップグレードする、2019 年 3 月 4
日の週に次の 1.11.7 パッチが提供されるまで待つ。

先ごろ、Go プログラミング言語に新しいセキュリティ上の脆弱性 [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486) が発見されました。これは P-521 と P-384
の楕円曲線の暗号および楕円に関する実装に問題があり、サービス拒否攻撃（DoS）を受ける可能性があるというものです。Google Kubernetes
Engine（GKE）では、悪意のあるユーザーがこの脆弱性を利用して Kubernetes API サーバーの CPU
を大量に消費するリクエストを送りつけ、クラスタ コントロール プレーンの可用性を低下させるおそれがあります。詳細については、 [ Go
プログラミング言語の開示情報 ](https://groups.google.com/forum/?hl=ja#!topic/golang-
announce/mVeX35iXuSw) をご覧ください。

**この脆弱性の影響を受けるのは、すべての Google Kubernetes Engine（GKE）マスターです。[ 最新バージョンのパッチ
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=ja#february-11-2019) には、この脆弱性の緩和策が含まれています。クラスタ マスターは、定期的なアップグレード
サイクルの一環として数週間以内にパッチ適用済みバージョンに自動的にアップグレードされます。 **

####  必要な対策

**お客様による対応は必要ありません。GKE マスターは、定期的なアップグレード サイクルの一環として自動的にアップグレードされます。**
マスターをすぐにアップグレードすることをご希望の場合は、 [ 手動でマスター アップグレードを開始
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ja#upgrading_the_cluster) することもできます。

このパッチは、GKE
1.10.12-gke.7、1.11.6-gke.11、1.11.7-gke.4、1.12.5-gke.5、およびそれ以降のリリースで提供されています。

####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

CVE-2019-6486 は、P-521 と P-384
の楕円曲線の暗号および楕円の実装における脆弱性です。悪意のあるユーザーがこの脆弱性を利用して、CPU を大量に消費するリクエストを送りつけることができます。

|  高  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  2018 年 12 月 3 日

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Kubernetes にセキュリティ上の脆弱性 [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) が発見されました。これは、比較的権限の低いユーザーが kubelet の
API に対する権限付与をバイパスして、クラスタ内のポッドやノードに対して任意のオペレーションを実行できるというものです。詳細については、 [
Kubernetes の開示情報 ](https://groups.google.com/forum/?hl=ja#!topic/kubernetes-
announce/GVllWCg6L88) をご覧ください。 **この脆弱性の影響を受けるのは、すべての Google Kubernetes
Engine（GKE）マスターです。Google では、すでにクラスタを[ 最新のパッチ バージョン
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=ja#november-12-2018) にアップグレード済みです。お客様による対応は必要ありません。 **

####  必要な対策

**お客様による対応は必要ありません。GKE マスターはすでにアップグレード済みです。**

このパッチは、GKE
1.9.7-gke.11、1.10.6-gke.11、1.10.7-gke.11、1.10.9-gke.5、1.11.2-gke.18、およびそれ以降のリリースで提供されています。

####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

脆弱性 CVE-2018-1002105 は、比較的権限の低いユーザーが kubelet の API
に対する権限付与をバイパスできるというものです。これにより、ユーザーはアップグレード可能なリクエストを作成してエスカレーションし、kubelet の API
を任意に呼び出すことができます。この脆弱性は、Kubernetes ではきわめて重大と評価されています。GKE の実装では未認証のエスカレーション
パスを防ぐことに注意が払われているため、この脆弱性は高と評価されています。

|  高  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  2018 年 11 月 13 日

説明  
---  
  
**2018 年 11 月 16 日更新:**
影響を受けた可能性のあるすべてのトークンの取り消しと入れ替えが完了しました。以後の対応は特に必要はありません。

Calico Container Network
Interface（CNI）プラグインで、特定の構成において機密情報を記録できるという問題が発見されました。この問題は Tigera Technical
Advisory [ TTA-2018-001 ](https://www.projectcalico.org/security-bulletins/)
で追跡されています。

  * Calico CNI プラグインをデバッグレベルのロギングで実行している場合、Kubernetes API クライアントの構成がログに書き込まれます。 
  * CNI ネットワーク構成で「k8s_auth_token」フィールドが設定されている場合、Calico CNI は Kubernetes API トークンも情報レベルでログに書き込みます。 
  * さらに、デバッグレベルのロギングで実行している場合、サービス アカウント トークンが、Calico で読み取られる Calico 構成ファイルで明示的に設定されているか、Calico で使用される環境変数として明示的に設定されていると、Calico コンポーネント（calico/node、felix、CNI）がその情報をログファイルに書き込みます。 

これらのトークンには、次の権限があります。  
      
    
    
    bgpconfigurations.crd.projectcalico.org     [create get list update watch]
    bgppeers.crd.projectcalico.org              [create get list update watch]
    clusterinformations.crd.projectcalico.org   [create get list update watch]
    felixconfigurations.crd.projectcalico.org   [create get list update watch]
    globalbgpconfigs.crd.projectcalico.org      [create get list update watch]
    globalfelixconfigs.crd.projectcalico.org    [create get list update watch]
    globalnetworkpolicies.crd.projectcalico.org [create get list update watch]
    globalnetworksets.crd.projectcalico.org     [create get list update watch]
    hostendpoints.crd.projectcalico.org         [create get list update watch]
    ippools.crd.projectcalico.org               [create get list update watch]
    networkpolicies.crd.projectcalico.org       [create get list update watch]
    nodes                                       [get list update watch]
    pods                                        [get list watch patch]
    namespaces                                  [get list watch]
    networkpolicies.extensions                  [get list watch]
    endpoints                                   [get]
    services                                    [get]
    pods/status                                 [update]
    networkpolicies.networking.k8s.io           [watch list]
            
  
---  
  
クラスタ ネットワーク ポリシーと Stackdriver Logging が有効になっている Google Kubernetes Engine
クラスタで、Calico サービス アカウント トークンが Stackdriver に記録されることが確認されました。ネットワーク
ポリシーが有効になっていないクラスタは影響を受けません。

Calico CNI プラグインのロギングが警告レベルでのみ行われるよう変更し、新しいサービス
アカウントを使用する修正プログラムを導入しました。パッチが適用された Calico コードは、今後のリリースでデプロイされる予定です。

影響を受ける可能性のあるトークンの取り消しを、来週中に段階的に実施していく予定です。取り消しが完了次第、こちらの情報も更新いたします。
**お客様側での対応は特に必要ありません** （このトークン入れ替え作業は 2018 年 11 月 16 日に完了しました）。

これらのトークンをすぐに入れ替えたい場合は、次のコマンドを実行してください。サービス アカウントの新しいシークレットが数秒以内に自動で再作成されます。  
      
    
    
    kubectl get sa --namespace kube-system calico -o template --template '{{(index .secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system
            
  
---  
  
####  検出

GKE は、API サーバーへのアクセスをすべて記録します。Google Cloud で想定されている IP 範囲外から Calico
トークンが使用されたかどうかを判断するには、次の Stackdriver クエリを実行します。このクエリは、GCP
のネットワーク外から行われた呼び出しの記録のみを返す点にご留意ください。また、必要に応じて、ご使用の環境に合わせてカスタマイズしてください。  
  
---  
      
    
    
    resource.type="k8s_cluster"
    protoPayload.authenticationInfo.principalEmail="system:serviceaccount:kube-system:calico"
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.34.208.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.192.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.200.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.59.80.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.208.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.216.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.220.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.222.0/24")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.224.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.216.148.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.222.176.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "173.255.112.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "192.158.28.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.192.112.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.232.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.236.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.236.48.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.251.128.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.204.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.208.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.167.160.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.178.192.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.2.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.240.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.128.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.154.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.196.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "208.68.108.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.184.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.188.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.202.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.192.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.196.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.198.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.200.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "2600:1900::/35")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.232.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.234.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.236.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.240.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.232.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.220.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.242.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.244.0.0/14")
            
  
---  
  
##  2018 年 8 月 14 日

説明  |  重大度  |  注  
---|---|---  
  
次の CVE が [ Intel により公表されました
](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) 。

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) （ [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) 関連） 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) （オペレーティング システムと [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) に関連） 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) （仮想化関連） 

これらの CVE は「L1 Terminal Fault（L1TF）」と総称されます。

これらの L1TF 脆弱性は、投機的実行を悪用してプロセッサ レベルのデータ構造の構成を攻撃します。「L1」とは、レベル 1 データ
キャッシュ（L1D）と呼ばれるコア内の小さなリソースで、メモリアクセスを高速化するために使用されます。

これらの脆弱性と Compute Engine の緩和策の詳細については、 [ Google Cloud ブログの記事
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=ja) をご覧ください。

####  Google Kubernetes Engine への影響

Kubernetes Engine の基盤である、お客様のクラスタとノードを相互に分離するインフラストラクチャは、既知の攻撃から保護されています。

Google の Container-Optimized OS（COS）イメージを使用していて、 [ 自動アップグレード
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=ja) を有効にしている場合は、COS イメージのパッチ適用済みバージョンが 2018 年 8 月 20
日の週に公開されると、Kubernetes Engine ノードプールがそのバージョンに自動的に更新されます。

[ 自動アップグレード ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=ja) を無効にしている場合は、COS イメージのパッチ適用済みバージョンが公開された後、Kubernetes
Engine ノードプールを [ 手動でアップグレード ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=ja) する必要があります。

|  高  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  2018 年 8 月 6 日、最終更新日: 2018 年 9 月 5 日

説明  |  重大度  |  注  
---|---|---  
  
####  2018 年 9 月 5 日更新

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) が先ごろ公表されました。これは、 [ CVE-2018-5390
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
と同様にカーネルレベルのネットワーク脆弱性で、脆弱性のあるシステムがサービス拒否（DoS）攻撃を受ける可能性が高まります。主な違いは、CVE-2018-5391
は IP 接続上で悪用されることです。両方の脆弱性に対応するために、この情報を更新しました。

####  説明

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390)
（「SegmentSmack」）はカーネルレベルのネットワーク脆弱性で、脆弱性のあるシステムが TCP
接続でサービス拒否（DoS）攻撃を受ける可能性が高まります。

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391)
（「FragmentSmack」）はカーネルレベルのネットワーク脆弱性で、脆弱性のあるシステムが IP
接続でサービス拒否（DoS）攻撃を受ける可能性が高まります。

####  Google Kubernetes Engine への影響

2018 年 8 月 11 日現在、すべての Kubernetes Engine
マスターが両方の脆弱性から保護されています。また、自動的にアップグレードするように構成されている Kubernetes Engine
クラスタはすべて、両方の脆弱性から保護されています。Kubernetes Engine ノードプールが [ 自動的にアップグレード
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ja) するように構成されておらず、最後に手動でアップグレードした日付が 2018 年 8 月 11
日より前の場合は、両方の脆弱性の影響を受けます。

####  パッチ適用済みバージョン

この脆弱性は重大度が高いため、パッチが公開されたら直ちにノードを [ 手動でアップグレード
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ja#upgrading-nodes) することをおすすめします。

|  高  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  2018 年 5 月 30 日

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Git に脆弱性が発見されました。この脆弱性により、権限のないユーザーによる gitRepo
ボリュームを使用したポッド作成が許可されている場合、Kubernetes で権限をエスカレーションできてしまうおそれがあります。この CVE のタグは [
CVE-2018-11235 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-11235) です。

####  この脆弱性の影響

この脆弱性は、以下のすべてに当てはまる場合に影響します。

  * 信頼できないユーザーがポッドを作成できる（またはポッド作成をトリガーできる）。 
  * 信頼できないユーザーによって作成されたポッドに、（ [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=ja) などを使用して）ホストの root アクセス権を防止する制限がある。 
  * 信頼できないユーザーによって作成されたポッドで、gitRepo ボリューム タイプの使用が許可されている。 

すべての Kubernetes Engine ノードに、この脆弱性の影響を受ける可能性があります。

####  必要な対策

gitRepo ボリューム タイプの使用を禁止します。PodSecurityPolicy によって gitRepo
ボリュームを禁止するには、PodSecurityPolicy の ` volumes ` ホワイトリストから ` gitRepo ` を除外します。

同等の gitRepo ボリュームの動作を実現するには、Git リポジトリを initContainer から EmptyDir ボリュームに複製します。

    
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: git-repo-example
    spec:
      initContainers:
        # This container clones the desired git repo to the EmptyDir volume.
        - name: git-clone
          image: alpine/git # Any image with git will do
          args:
            - clone
            - --single-branch
            - --
            - https://github.com/kubernetes/kubernetes # Your repo
            - /repo # Put it in the volume
          securityContext:
            runAsUser: 1 # Any non-root user will do. Match to the workload.
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
          volumeMounts:
            - name: git-repo
              mountPath: /repo
      containers:
        ...
      volumes:
        - name: git-repo
          emptyDir: {}

####  この脆弱性に対処するパッチ

パッチは今後の Kubernetes Engine リリースに含まれます。詳細については、随時こちらでご確認ください。

|  中  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  2018 年 5 月 21 日

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Linux
カーネルにいくつかの脆弱性が発見されました。こうした脆弱性により、権限のないプロセスからの権限エスカレーションや（カーネルのクラッシュによる）サービス拒否を実行できるおそれがあります。これらの
CVE のタグは、それぞれ [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) 、 [ CVE-2018-8897
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897) 、 [
CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)
です。これらの脆弱性はすべての Kubernetes Engine ノードに影響するため、最新のパッチ バージョンに [ アップグレード
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=ja) することをおすすめします。詳細については、以下をご覧ください。

####  必要な対策

アップグレードするには、まずマスターを最新バージョンにアップグレードする必要があります。このパッチは、Kubernetes Engine
1.8.12-gke.1、Kubernetes Engine 1.9.7-gke.1、Kubernetes Engine 1.10.2-gke.1
で提供されています。これらのリリースには、Container-Optimized OS と Ubuntu の両方のイメージのパッチが含まれています。

その前に新しいクラスタを作成する場合は、パッチ適用済みバージョンを明示的に指定する必要があります。 [ ノードの自動アップグレード
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=ja) を有効にしていて、手動でアップグレードしない場合は、数週間以内にノードがパッチ適用済みバージョンにアップグレードされます。

####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : この脆弱性は Linux
カーネルに影響を及ぼします。権限のないユーザーまたはプロセスがシステム カーネルをクラッシュできるようになり、DoS
攻撃や権限エスカレーションが発生します。脆弱性の重大度評価は高で、CVSS は 7.8 です。

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : この脆弱性は Linux
カーネルに影響を及ぼします。権限のないユーザーまたはプロセスがシステム カーネルをクラッシュできるようになり、DoS
攻撃が発生します。脆弱性の評価は中で、CVSS は 6.5 です。

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : この脆弱性は Linux カーネルの KVM
ハイパーバイザに影響を及ぼします。権限のないプロセスがゲストカーネルをクラッシュできるようになり、場合によっては権限を取得できます。Kubernetes
Engine が実行されているインフラストラクチャにはこの脆弱性のパッチが適用されているため、Kubernetes Engine
は影響を受けません。脆弱性の重大度評価は高で、CVSS スコアは 8.0 です。

|  高  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  2018 年 3 月 12 日

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Kubernetes プロジェクトにより、新しいセキュリティ脆弱性 [ CVE-2017-1002101
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) と [
CVE-2017-1002102 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002102) が [ 公表されました
](https://groups.google.com/forum/?hl=ja#!topic/kubernetes-security-
announce/P7lBjbjDKd8) 。これは、コンテナの外部にあるファイルにコンテナからアクセスできるというものです。これらの脆弱性はすべての
Kubernetes Engine ノードに影響するため、できるだけ早く最新のパッチ
バージョンにアップグレードすることをおすすめします。詳細については、以下をご覧ください。

####  必要な対策

これらの脆弱性は重大度が高いため、ノードの自動アップグレードを有効にしているかどうかにかかわらず、パッチが公開されたら直ちにノードを [
手動でアップグレード ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-
a-container-cluster?hl=ja) することをおすすめします。このパッチは 3 月 16
日までにすべてのお客様に提供されますが、クラスタが属するゾーンによっては、 [ リリース スケジュール
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=ja#march-12-2018) に応じてそれより早く入手できる場合があります。

アップグレードするには、まずマスターを最新バージョンにアップグレードする必要があります。このパッチは、Kubernetes
1.9.4-gke.1、Kubernetes 1.8.9-gke.1、Kubernetes 1.7.14-gke.1
で提供されています。新しいクラスタでは、3 月 30
日までにパッチ適用済みバージョンがデフォルトで使用されるようになります。それより前に新しいクラスタを作成する場合は、パッチ適用済みバージョンを明示的に指定する必要があります。

[ ノードの自動アップグレード ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=ja) を有効にしていて、手動でアップグレードしない場合は、4 月
23 日までにノードがパッチ適用済みバージョンにアップグレードされます。ただし、この脆弱性の性質上、パッチが公開されたら直ちにノードを [
手動でアップグレード ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-
a-container-cluster?hl=ja) することをおすすめします。

####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下の 2 つです。

脆弱性 CVE-2017-1002101 は、 [ subPath
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) ボリューム
マウントを使用しているコンテナがボリュームの外部にあるファイルにアクセスできるというものです。つまり、PodSecurityPolicy で
hostPath ボリュームへのコンテナ アクセスをブロックしている場合、ポッドを更新または作成できる攻撃者が他のボリューム タイプを使用して任意の
hostPath をマウントするおそれがあります。

脆弱性 CVE-2017-1002102 は、特定のボリューム タイプ（シークレット、構成マップ、投影ボリューム、下位 API
ボリュームなど）を使用するコンテナがボリュームの外部にあるファイルを削除できるというものです。つまり、これらのボリューム
タイプのいずれかを使用するコンテナが不正使用された場合、または信頼できないユーザーによるポッド作成が許可されている場合、攻撃者がそのコンテナを利用してホスト上の任意のファイルを削除するおそれがあります。

この修正の詳細については、 [ Kubernetes ブログの記事
](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-vulnerability/)
をご覧ください。

|  高  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

