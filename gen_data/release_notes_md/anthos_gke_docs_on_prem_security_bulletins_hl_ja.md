#  セキュリティに関する情報

このトピックでは、Anthos GKE On-Prem（GKE On-Prem）のすべてのセキュリティ情報を説明します。

脆弱性に関する情報は多くの場合、影響を受けた当事者が対処するまで、情報制限により非公開となります。この場合、GKE on-prem の [ リリースノート
](https://cloud.google.com/anthos/gke/docs/on-prem/release-notes?hl=ja)
には、制限情報が解除されるまで「セキュリティ更新」が記載されます。リリースノートは情報制限が解除された時点で更新され、パッチによって対処された脆弱性の情報が反映されます。

**注:** GKE On-Prem でマルチテナント ワークロードを実行する場合、上記の情報には特に注意してください。これらの脆弱性はマルチテナント
ワークロードに影響を及ぼす可能性が高くなります。GKE on-prem のセキュリティ境界とそれらによるワークロードへの影響に関する技術的説明については、
[ Kubernetes スタックのさまざまなレイヤでの隔離
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) をご覧ください。

最新のセキュリティ情報を入手するには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加します。

##  GCP-2020-007

**公開日:** 2020 年 6 月 1 日  
説明  |  重大度  |  注  
---|---|---  
  
最近、Kubernetes でサーバー側のリクエスト フォージェリ（SSRF）の脆弱性 [ CVE-2020-8555
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)
が検出され、特定の承認済みユーザーがコントロール プレーン ホスト ネットワークから最大 500 バイトの機密情報を漏洩する可能性が生じました。Google
Kubernetes Engine（GKE）コントロール プレーンでは、Kubernetes
のコントローラを使用するため、この脆弱性の影響を受けます。以下で説明するように、コントロール プレーンを最新のパッチ
バージョンにアップグレードすることをおすすめします。ノードのアップグレードは不要です。  

####  必要な対策

次の Anthos GKE On-Prem（GKE On-Prem）以降のバージョンには、この脆弱性に対する修正が含まれています。

  * Anthos 1.3.0 

以前のバージョンを使用している場合は、修正を含むバージョンに [ 既存のクラスタをアップグレード
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=ja)
します。

####  このパッチで対処される脆弱性

これらのパッチは、脆弱性 CVE-2020-8555 を軽減します。さまざまなコントロール プレーンの強化対策により、悪用が困難であるため、GKE
の脆弱性の重大度評価は「中」と判断されています。

攻撃者が特定の組み込みボリューム
タイプ（GlusterFS、Quobyte、StorageFS、ScaleIO）でポッドを作成する権限や、StorageClass
を作成する権限を持つ場合、マスターのホスト ネットワークから攻撃者が制御するリクエスト本文を使用せずに ` kube-controller-manager
` に ` GET ` リクエストや ` POST ` リクエストを発行させる可能性があります。 __ これらのボリューム タイプは GKE
ではほとんど使用されないため、新たに使用された場合は、それが攻撃の検出シグナルとなります。

` GET/POST `
の結果を攻撃者に返す手段（ログを通じてなど）と組み合わせることで、機密情報の漏洩につながる可能性があります。このような漏洩の可能性を排除するために、対象となるストレージ
ドライバを更新しました。

|

中

|

[ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**公開日:** 2020 年 6 月 1 日  
説明  |  重大度  |  注  
---|---|---  
  
Kubernetes は、特権コンテナでノード トラフィックを別のコンテナにリダイレクトできるようになる [ 脆弱性
](https://github.com/kubernetes/kubernetes/issues/91507) を公表しました。kubelet と API
サーバーの間の相互 TLS/SSH トラフィックや、mTLS
を使用するアプリケーションからのトラフィックは、この攻撃によって読み取ることも変更することもできません。この脆弱性は、すべての Google
Kubernetes Engine（GKE）ノードに影響を及ぼします。下記に示すように、最新のパッチ バージョンにアップグレードすることをおすすめします。

####  必要な対策

Anthos GKE On-Prem（GKE On-Prem）のこの脆弱性を緩和するには、次のバージョン以降に [ クラスタをアップグレード
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=ja)
します。

  * Anthos 1.3.2 

通常、 ` CAP_NET_RAW ` を必要とするコンテナはほとんどありません。この機能やその他の強力な機能は、 [ Anthos Policy
Controller ](https://cloud.google.com/anthos-config-
management/docs/concepts/policy-controller?hl=ja) を使用するか、Pod
仕様を更新することで、デフォルトでブロックする必要があります。

  * ` CAP_NET_RAW ` 機能をコンテナから次の方法で削除します。 
    * Anthos Policy Controller / Gatekeeper をこちらの [ 制約テンプレート ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) で使用して、適用する方法。たとえば、次のようにします。 
        
                
        # Dropping CAP_NET_RAW with Gatekeeper
        # (requires the K8sPSPCapabilities template)
        apiversion: constraints.gatekeeper.sh/v1beta1
        kind:  K8sPSPCapabilities
        metadata:
          name: forbid-cap-net-raw
        spec:
          match:
            kinds:
              - apiGroups: [""]
              kinds: ["Pod"]
            namespaces:
              #List of namespaces to enforce this constraint on
              - default
            # If running gatekeeper >= v3.1.0-beta.5,
            # you can exclude namespaces rather than including them above.
            excludedNamespaces:
              - kube-system
          parameters:
            requiredDropCapabilities:
              - "NET_RAW"
        

    * Pod の仕様を次のように更新する方法。 
        
                
        # Dropping CAP_NET_RAW from a Pod:
        apiVersion: v1
        kind: Pod
        metadata:
          name: no-cap-net-raw
        spec:
          containers:
            -name: may-container
             ...
            securityContext:
              capabilities:
                drop:
                  -NET_RAW
        

####  このパッチで対処される脆弱性

このパッチで緩和される脆弱性は以下のとおりです。

[ Kubernetes の問題 91507
](https://github.com/kubernetes/kubernetes/issues/91507) に記載された脆弱性。この脆弱性では、 `
CAP_NET_RAW ` 機能（デフォルトのコンテナ機能セットに含まれています）がノード上で IPv6
スタックを不正に構成して、攻撃者によって制御されるコンテナにノード
トラフィックをリダイレクトします。これにより、攻撃者はノードからのトラフィックやノードを宛先とするトラフィックをインターセプトして変更することが可能になります。kubelet
と API サーバーの間の相互 TLS / SSH トラフィックや、mTLS
を使用するアプリケーションからのトラフィックは、この攻撃によって読み取ることも変更することもできません。

|

中

|

[ Kubernetes の問題 91507
](https://github.com/kubernetes/kubernetes/issues/91507)  
  
  
##  GCP-2020-004

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Kubernetes で [ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) に記載された脆弱性が発見されました。これは、POST
リクエストの発行を許可された任意のユーザーが Kubernetes API サーバーへのリモート
サービス拒否攻撃を実行できるというものです。Kubernetes 製品セキュリティ委員会（PSC）から発表されたこの脆弱性に関する追加情報は、 [ こちら
](https://groups.google.com/g/kubernetes-security-
announce/c/wuwEwZigXBc?hl=ja) からご覧いただけます。

Kubernetes API サーバーにネットワーク アクセスできるクライアントを制限することで、この脆弱性を軽減できます。

####  必要な対策

この脆弱性に対する修正を含むパッチ バージョンが公開されたら、直ちにクラスタをアップグレードすることをおすすめします。

修正を含むパッチ バージョンは次のとおりです。

  * Anthos 1.3.0 で、Kubernetes バージョン 1.15.7-gke.32 を実行します。 

####  このパッチで対処される脆弱性

このパッチは次のサービス拒否攻撃（DoS）の脆弱性を修正します。

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) .

|

中

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  2019 年 10 月 16 日

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Kubernetes で [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) に記載された脆弱性が見つかりました。これは、POST
リクエストの発行を許可された任意のユーザーが Kubernetes API サーバーへのリモート
サービス拒否攻撃を実行できるというものです。Kubernetes 製品セキュリティ委員会（PSC）から発表されたこの脆弱性に関する追加情報を [ こちら
](https://groups.google.com/forum/?hl=ja#!topic/kubernetes-security-
announce/jk8polzSUxs) からご覧いただけます。

Kubernetes API サーバーにネットワーク アクセスできるクライアントを制限することで、この脆弱性を軽減できます。

######  必要な対策

修正を含むパッチ バージョンが公開されたら、直ちに [ クラスタをそのバージョンにアップグレード
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading-
clusters?hl=ja) することをおすすめします。

この修正が含まれるパッチ バージョンは次のとおりです。

  * Anthos 1.1.1 で、Kubernetes バージョン 1.13.7-gke.30 を実行します。 

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
  
最近、エンドポイントのモニタリングの保護に使用される RBAC
プロキシがユーザーを正しく認証しないという脆弱性が発見され、緩和されました。そのため、特定のコンポーネントの指標が、内部クラスタ
ネットワーク内から未承認ユーザーから使用可能になっています。影響を受けたコンポーネントは以下のとおりです。

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
prem/downloads?hl=ja#gkectl_latest) に、できる限り早く [ アップグレード
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading-
clusters?hl=ja) することをおすすめします。これには、この脆弱性に対するパッチが含まれています。

|

中

|

[ Anthos GKE On-Prem のリリース ](https://cloud.google.com/anthos/gke/docs/on-
prem/downloads?hl=ja#gkectl_latest)  
  
##  2019 年 8 月 22 日

説明  |  重大度  |  注  
---|---|---  
  
先ごろ、Kubernetes で脆弱性 [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) が発見されました。これは、クラスタ スコープの [ カスタム リソース
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) インスタンスを、あたかもすべての Namespace
に存在する名前空間オブジェクトであるかのように動作させることができるというものです。つまり、名前空間レベルの RBAC 権限しか持たないユーザー
アカウントまたはサービス アカウントでも、クラスタ スコープのカスタム リソースとやり取りできてしまいます。攻撃者がこの脆弱性を悪用するためには、任意の
Namespace のリソースにアクセスする権限が必要です。

######  必要な対策

クラスタをバージョン [ 1.0.2-gke.3 ](https://cloud.google.com/anthos/gke/docs/on-
prem/downloads?hl=ja#gkectl_latest) に、できる限り早く [ アップグレード
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading-
clusters?hl=ja) することをおすすめします。これには、この脆弱性に対するパッチが含まれています。

######  このパッチで対処される脆弱性

このパッチにより、次の脆弱性が緩和されます。 [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) 。

|

中

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

