A new version of Anthos GKE on AWS was released on August 5. See the [ release
notes ](https://cloud.google.com/anthos/gke/docs/aws/release-notes?hl=ja) for
information on breaking changes.

#  セキュリティに関する情報

Anthos GKE on AWS（GKE on AWS）のセキュリティに関する情報について説明します。

##  GCP-2020-011

**公開:** 2020-07-24  
説明  |  重大度  |  注  
---|---|---  
  
先ごろ、ネットワークに関する脆弱性 [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) が Kubernetes
で発見されました。Service は、ローカル ループバック インターフェース（127.0.0.1）を使用して同じ Pod
内で実行されている他のアプリケーションと通信することがあります。この脆弱性により、クラスタのネットワークにアクセスできる攻撃者が、隣接する Pod
とノードのループバック インターフェースにトラフィックを送信できてしまいます。Pod の外部からループバック
インターフェースにアクセスできないことに依存している Service が侵害される可能性があります。

攻撃者が GKE on AWS クラスタでこの脆弱性を悪用するには、クラスタ内の EC2 インスタンスで [ 送信元と宛先のチェック
](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html)
を無効にする必要があります。そのためには、攻撃者が EC2 インスタンスに対する ` ModifyInstanceAttribute ` または `
ModifyNetworkInterfaceAttribute ` の AWS IAM 権限を持っている必要があります。このため、この脆弱性には GKE
on AWS の重大度「低」が割り当てられています。

####  必要な対策

この脆弱性を修正するには、クラスタをパッチ適用済みバージョンにアップグレードします。次に示す今後の GKE on AWS
バージョン以降では、この脆弱性に対する修正が含まれる予定です。

  * GKE on AWS 1.4.2 

####  このパッチで対処される脆弱性

このパッチは、脆弱性 [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) を修正します。

|

低

|

[ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315)  
  
##  GCP-2020-009

**公開:** 2020-07-15  説明  |  重大度  |  注  
---|---|---  
  
先ごろ、権限昇格に関する脆弱性 [ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559) が Kubernetes
で発見されました。この脆弱性により、ノードを不正使用した攻撃者が、クラスタ内の任意の Pod
でコマンドを実行できてしまいます。これにより、攻撃者はすでに不正使用したノードを使用して他のノードを不正使用し、情報の読み取りや、破壊的な操作をする可能性があります。

攻撃者がこの脆弱性を悪用するには、クラスタ内のノードがすでに不正使用されている必要があります。この脆弱性だけで、クラスタ内のノードが不正使用されることはありません。

####  必要な対策

GKE on AWS 一般提供（1.4.1、2020 年 7
月末から入手可能）以降には、この脆弱性に対するパッチが含まれています。以前のバージョンを使用している場合は、 [ anthos-gke コマンドライン
ツールの新しいバージョンをダウンロード ](https://cloud.google.com/anthos/gke/docs/aws/how-
to/prerequisites?hl=ja) して、管理クラスタとユーザー クラスタを再作成します。

####  このパッチで対処される脆弱性

これらのパッチは、脆弱性 CVE-2020-8559
を軽減します。攻撃者は既存の不正使用ノードに加えて、この攻撃を効果的に悪用するためにクラスタ、ノード、ワークロードについて最初に情報を取得する必要があるため、GKE
の脆弱性の重大度評価は「中」です。この脆弱性だけで、不正使用されたノードが攻撃者に提供されることはありません。

|

中

|

[ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559)  
  
##  GCP-2020-007

**公開:** 2020-06-01  
説明  |  重大度  |  注  
---|---|---  
  
最近、Kubernetes でサーバー側のリクエスト フォージェリ（SSRF）の脆弱性 [ CVE-2020-8555
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)
が検出され、特定の承認済みユーザーがコントロール プレーン ホスト ネットワークから最大 500 バイトの機密情報を漏洩する可能性が生じました。Google
Kubernetes Engine（GKE）コントロール プレーンでは、Kubernetes
のコントローラを使用するため、この脆弱性の影響を受けます。以下で説明するように、コントロール プレーンを最新のパッチ
バージョンにアップグレードすることをおすすめします。ノードのアップグレードは不要です。  

####  必要な対策

Anthos GKE on AWS（GKE on AWS）v0.2.0
以降には、この脆弱性に対するパッチがすでに含まれています。以前のバージョンを使用している場合は、 [ anthos-gke コマンドライン
ツールの新しいバージョンをダウンロード ](https://cloud.google.com/anthos/gke/docs/aws/how-
to/prerequisites?hl=ja) して、管理クラスタとユーザー クラスタを再作成します。

####  このパッチで対処される脆弱性

これらのパッチは、脆弱性 CVE-2020-8555 を軽減します。さまざまなコントロール プレーンの強化対策により、悪用が困難であるため、GKE
の脆弱性の重大度評価は「中」です。

攻撃者が特定の組み込み Volume タイプ（GlusterFS、Quobyte、StorageFS、ScaleIO）で Pod
を作成する権限や、StorageClass を作成する権限を持つ場合、マスターのホスト ネットワークから攻撃者が制御するリクエスト本文を使用せずに `
kube-controller-manager ` に ` GET ` リクエストや ` POST ` リクエストを発行させる可能性があります。 __
これらの Volume タイプは GKE ではほとんど使用されないため、新たに使用された場合は、それが攻撃の検出シグナルとなります。

` GET/POST `
の結果を攻撃者に返す手段（ログを通じてなど）と組み合わせることで、機密情報の漏洩につながる可能性があります。このような漏洩の可能性を排除するために、対象となるストレージ
ドライバを更新しました。

|

中

|

[ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**公開:** 2020-06-01  
説明  |  重大度  |  注  
---|---|---  
  
Kubernetes は、特権コンテナでノード トラフィックを別のコンテナにリダイレクトできるようになる [ 脆弱性
](https://github.com/kubernetes/kubernetes/issues/91507) を公表しました。kubelet と API
サーバーの間の相互 TLS / SSH トラフィックや、mTLS
を使用するアプリケーションからのトラフィックは、この攻撃によって読み取ることも変更することもできません。この脆弱性はすべての Google
Kubernetes Engine（GKE）ノードに影響を及ぼすため、下記のとおり最新のパッチ バージョンにアップグレードすることをおすすめします。

####  必要な対策

次のバージョン以降の [ anthos-gke コマンドライン ツールをダウンロード
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=ja)
し、管理クラスタとユーザー クラスタを再作成します。

  * aws-0.2.1-gke.7 

通常、 ` CAP_NET_RAW ` を必要とするコンテナはほとんどありません。この機能やその他の強力な機能は、 [ Anthos Policy
Controller ](https://cloud.google.com/anthos-config-
management/docs/concepts/policy-controller?hl=ja) を使用するか、Pod
仕様を更新して、デフォルトでブロックする必要があります。

` CAP_NET_RAW ` 機能をコンテナから削除します。

  * Anthos Policy Controller / Gatekeeper をこの [ 制約テンプレート ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) で使用して、適用します。次に例を示します。 
    
        
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
    

  * または、Pod 仕様を更新します。 
    
        
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
トラフィックをリダイレクトします。これにより、攻撃者はノードからのトラフィックまたはノードを宛先とするトラフィックの傍受や変更ができてしまいます。kubelet
と API サーバーの間の相互 TLS / SSH トラフィックや、mTLS
を使用するアプリケーションからのトラフィックは、この攻撃によって読み取ることも変更することもできません。

|

中

|

[ Kubernetes の問題 91507
](https://github.com/kubernetes/kubernetes/issues/91507)  

