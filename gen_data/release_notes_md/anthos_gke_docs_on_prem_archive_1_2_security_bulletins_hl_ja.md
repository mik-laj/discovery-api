以前のバージョンの GKE On-Prem のドキュメントを表示しています。 [ 最新のドキュメントをご覧ください
](https://cloud.google.com/anthos/gke/docs/on-prem?hl=ja) 。

#  セキュリティに関する情報

このトピックでは、すべてのAnthos GKE On-Prem のセキュリティに関する情報について説明します。

脆弱性に関する情報は多くの場合、影響を受けた当事者が対処するまで、情報制限により非公開となります。このような場合、GKE on-prem の [
リリースノート ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/release-notes?hl=ja)
には、情報制限が解除されるまで「セキュリティ更新」が記載されます。リリースノートは情報制限が解除された時点で更新され、パッチによって対処された脆弱性の情報が反映されます。

**注:** GKE On-Prem でマルチテナント ワークロードを実行する場合、上記の情報には特に注意してください。これらの脆弱性はマルチテナント
ワークロードに影響を及ぼす可能性が高くなります。GKE On-Prem のセキュリティ境界とそれによるワークロードへの影響に関する技術的説明については、 [
Kubernetes スタックのさまざまなレイヤーでの隔離
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) をご覧ください。

最新のセキュリティ情報を入手するには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加します。

##  2019 年 10 月 16 日

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Kubernetes で [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) に記載された脆弱性が見つかりました。これは、POST
リクエストの発行を許可された任意のユーザーが Kubernetes API サーバーへのリモート
サービス拒否攻撃を実行できるというものです。Kubernetes 製品セキュリティ委員会（PSC）から発表されたこの脆弱性に関する追加情報を [ こちら
](https://groups.google.com/forum/?hl=ja#!topic/kubernetes-security-
announce/jk8polzSUxs) からご覧いただけます。

この問題を軽減するには、Kubernetes API サーバーにネットワーク アクセスできるクライアントを制限してください。

######  必要な対策

修正を含むパッチ バージョンが公開されたら、直ちに [ クラスタをそのバージョンにアップグレード
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/how-
to/upgrading-clusters?hl=ja) することをおすすめします。

この修正が含まれるパッチ バージョンは次のとおりです。

  * Anthos 1.1.1 で Kubernetes バージョン 1.13.7-gke.30 が実行されるようになりました。 

######  このパッチで対処される脆弱性

このパッチにより、次の脆弱性が緩和されます。 [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)

|

高

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
##  2019 年 8 月 23 日

説明  |  重大度  |  注  
---|---|---  
  
Google では最近、モニタリング エンドポイントの保護に使用される RBAC プロキシがユーザーを正しく承認しない脆弱性を発見し、それを緩和しました。
その結果として権限を与えられていないユーザーが、内部クラスタ
ネットワークから特定のコンポーネントの指標を取得できます。次のコンポーネントが影響を受けています。

  * ` etcd `
  * ` etcd-events `
  * ` kube-apiserver `
  * ` kube-controller-manager `
  * ` kube-scheduler `
  * ` node-exporter `
  * ` kube-state-metrics `
  * ` prometheus `
  * ` alertmanager `

######  必要な対策

クラスタをバージョン [ 1.0.2-gke.3 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=ja#gkectl_latest) に [ アップグレード
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/how-
to/upgrading-clusters?hl=ja) することをおすすめします。新バージョンにはこの脆弱性に対するパッチが含まれています。

|

中

|

[ Anthos GKE On-Prem のリリース ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=ja#gkectl_latest)  
  
##  2019 年 8 月 22 日

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Kubernetes で脆弱性 [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) が発見されました。これは、クラスタ スコープの [ カスタム リソース
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/)
インスタンスを、あたかもすべての名前空間に存在する名前空間オブジェクトであるかのように動作させることができるというものです。つまり、名前空間レベルの
RBAC 権限しか持たないユーザー アカウントまたはサービス アカウントでも、クラスタ スコープのカスタム
リソースとやり取りできてしまいます。攻撃者がこの脆弱性を悪用するためには、任意の名前空間のリソースにアクセスする権限が必要です。

######  必要な対策

クラスタをバージョン [ 1.0.2-gke.3 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=ja#gkectl_latest) に [ アップグレード
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/how-
to/upgrading-clusters?hl=ja) することをおすすめします。新バージョンにはこの脆弱性に対するパッチが含まれています。

######  このパッチで対処される脆弱性

このパッチにより、次の脆弱性が緩和されます。 [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) 。

|

中

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

