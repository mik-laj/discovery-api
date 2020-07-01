#  リリースノート

このページには Anthos GKE On-Prem
に関する更新内容が記載されています。このページを定期的にチェックして、新機能や更新された機能、バグ修正、既知の問題、サポートが終了した（非推奨になった）機能に関するお知らせを確認してください。

関連情報:

  * [ ダウンロード ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=ja)
  * [ バージョニングとアップグレード ](https://cloud.google.com/anthos/gke/docs/on-prem/versioning-and-upgrades?hl=ja)
  * [ GKE On-Prem のアップグレード ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=ja)

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/gkeonprem-release-notes.xml `
を直接追加します。

##  2019 年 11 月 19 日

GKE on-prem バージョン 1.1.2-gke.0 が利用可能になりました。バージョン 1.1.2-gke.0 の OVA ` gkectl `
をダウンロードしてバンドルをアップグレードするには、 [ ダウンロード
](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=ja#latest)
をご覧ください。その後、 [ 管理ワークステーションのアップグレード
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=ja) と [
クラスタのアップグレード ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading?hl=ja) をご覧ください。

このパッチ バージョンには以下の変更内容が含まれています。

###  新機能

**FEATURE:**

[ クラスタの強化 ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/security/hardening-your-cluster?hl=ja) を公開しました。

**FEATURE:**

[ クラスタの管理 ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/managing-clusters?hl=ja) を公開しました。

###  修正済み

**FIXED:**

11 月 5 日  からの既知の問題を修正しました。

**FIXED:**

11 月 8 日  からの既知の問題を修正しました。

###  既知の問題

**ISSUE:**

vSphere で複数のデータセンターを実行している場合に ` gkectl diagnose cluster `
を実行すると次のエラーが返されることがありますが、無視しても問題ありません。

    
    
    Checking storage...FAIL
    path '*' resolves to multiple datacenters

**ISSUE:**

vSAN データストアを実行している場合に ` gkectl diagnose cluster `
を実行すると次のエラーが返されることがありますが、無視しても問題ありません。

    
    
    PersistentVolume [NAME]: virtual disk "[[DATASTORE_NAME]]
    [PVC]" IS NOT attached to machine "[MACHINE_NAME]" but IS listed in the Node.Status

##  2019 年 11 月 8 日

**ISSUE:**

GKE on-prem バージョン 1.1.1-gke.2 では、Docker
レジストリを使用するように構成されたクラスタを作成できないことが報告されています。GKE on-prem 構成ファイルの `
privateregistryconfig ` フィールドに入力して、Docker レジストリを構成します。クラスタの作成が ` Failed to
create root cluster: could not create external client: could not create
external control plane: docker run error: exit status 125 ` などのエラーで失敗します。

修正はバージョン 1.1.2 を対象としています。当面の間、Docker レジストリを使用するように構成されたクラスタを作成する場合は、 ` --skip-
validation-docker ` フラグを ` gkectl create cluster ` に渡します。

##  2019 年 11 月 5 日

**ISSUE:**

GKE on-prem の構成ファイルには、仮想マシンディスク（VMDK）ファイルへのパスを検索する ` vcenter.datadisk `
フィールドがあります。インストール中に、VMDK の名前を選択します。デフォルトでは、GKE on-prem によって VMDK が作成され、vSphere
データストアのルートに保存されます。

vSAN データストアを使用する場合は、VMDK を保存するフォルダをデータストアに作成する必要があります。フィールドへのフルパス（ ` datadisk:
anthos/gke/docs/on-prem/datadisk.vmdk ` など）を指定すると、GKE on-prem によって VMDK
がそのフォルダに保存されます。

フォルダを作成すると、vSphere によって Universally Unique Identifier（UUID）がフォルダに割り当てられます。GKE
on-prem 構成のフォルダパスを指定しますが、vSphere API はフォルダの UUID
を検索します。現在、この不一致によりクラスタの作成とアップグレードが失敗する可能性があります。

修正はバージョン 1.1.2 を対象としています。当面の間は、フォルダパスの代わりにフォルダの UUID を指定する必要があります。 [
クラスタのアップグレード ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/upgrading-
clusters?hl=ja#admin_datadisk_folder) とインストール
トピックに記載されている、現在利用可能な回避策の手順に従ってください。

##  2019 年 10 月 25 日

GKE on-prem バージョン 1.1.1-gke.2 が利用可能になりました。バージョン 1.1.1-gke.2 の OVA ` gkectl `
をダウンロードしてバンドルをアップグレードするには、 [ ダウンロード
](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=ja#latest)
をご覧ください。その後、 [ 管理ワークステーションのアップグレード
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=ja) と [
クラスタのアップグレード ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading?hl=ja) をご覧ください。

このパッチ バージョンには以下の変更内容が含まれています。

###  新機能

**FEATURE:**

**要対応:** このバージョンでは、管理ワークステーションの最小 ` gcloud ` バージョンが 256.0.0 にアップグレードされます。 [
管理ワークステーションをアップグレード ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/upgrading-admin-workstation?hl=ja)
してください。その後、 [ クラスタをアップグレード ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/upgrading-clusters?hl=ja) してください。

**FEATURE:**

オープンソースの [ CoreOS ツールボックス ](https://github.com/coreos/toolbox) がすべての GKE on-
prem クラスタ ノードに含まれるようになりました。このツールセットは、ノードの問題のトラブルシューティングに役立ちます。 [
ツールボックスを使用してノードの問題をデバッグする ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/toolbox?hl=ja) をご覧ください。

###  修正済み

**FIXED:**

OIDC で構成されたクラスタがアップグレードされない問題を修正しました。

**FIXED:**

[ セキュリティに関する情報 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/security-bulletins?hl=ja#october-16-2019) で説明されている [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) を修正しました。

**FIXED:**

Google Cloud への接続が失われたためにクラスタ指標が失われる問題を修正しました。GKE on-prem クラスタの Google Cloud
への接続が一定時間失われた場合、そのクラスタの指標が完全に復元されるようになりました。

**FIXED:**

管理クラスタの指標の取り込みが、ユーザー クラスタの指標の取り込みよりも遅くなる問題を修正しました。

###  既知の問題

**ISSUE:**

静的 IP を使用し、管理クラスタとは異なるネットワークを使用しているユーザー クラスタの場合: ユーザー
クラスタのネットワーク構成を上書きする際、ユーザー コントロール プレーンを起動できない場合があります。これは、ユーザー
クラスタのネットワークを使用しているが、管理クラスタから IP アドレスとゲートウェイが割り当てられているため発生します。

この問題を回避するには、適切なネットワークを使用するように各ユーザー コントロール プレーンの MachineDeployment
仕様を更新します。次に、各ユーザー コントロール プレーンの Machine を削除して、MachineDeployment で新しい Machine
を作成します。

  1.     # List MachineDeployments in the admin cluster
        kubectl get machinedeployments --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

  2.     # Update a user control plane MachineDeployment from your shell
        kubectl edit machinedeployment --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINEDEPLOYMENT_NAME]

  3.     # List Machines in the admin cluster
        kubectl get machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

  4.     # Delete user control plane Machines in the admin cluster
        kubectl delete machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINE_NAME]

##  2019 年 9 月 26 日

GKE on-prem バージョン 1.1.0-gke.6 が利用可能になりました。バージョン 1.1.0-gke.6 の ` gkectl `
をダウンロードしてバンドルをアップグレードするには、 [ ダウンロード
](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=ja#latest)
をご覧ください。次に、 [ クラスタのアップグレード ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/upgrading?hl=ja) をご覧ください。

このマイナー バージョンには以下の変更内容が含まれています。

###  新機能

**FEATURE:**

クラスタ ノードのデフォルトの Kubernetes バージョンが、バージョン 1.13.7-gke.20 になりました（以前は
1.12.7-gke.19）。

**FEATURE:**

**要対応:** バージョン 1.1.0-gke.6 以降、GKE On-Prem はユーザー クラスタのノード（vSphere VM）に対して
vShere [ Distributed Resource Scheduler（DRS）
](https://www.vmware.com/products/vsphere/drs-dpm.html)
のルールを作成し、データセンター内の少なくとも 3 つの物理ホストにそれらを分散させます。

**この機能は、バージョン 1.1.0-gke.6 を実行するすべての新規および既存のユーザー クラスタでデフォルトで有効になっています。**

この機能を使用するには、vSphere 環境が次の条件を満たしている必要があります。

  * VMware DRS が有効になっていること。VMware DRS には、vSphere Enterprise Plus ライセンス エディションが必要です。DRS を有効にする方法については、 [ クラスタ内の VMware DRS の有効化 ](https://kb.vmware.com/s/article/1034280) をご覧ください。 
  * GKE on-prem 構成ファイルの ` vcenter ` フィールドで指定されている vSphere ユーザー アカウントに ` Host.Inventory.EditCluster ` 権限が付与されていること。 
  * 利用可能な物理ホストが少なくとも 3 つあること。 

既存のユーザー クラスタでこの機能を有効にしない場合（たとえば、機能に対応するのに十分なホストがない場合）は、ユーザー
クラスターをアップグレードする前に、次の手順を実行します。 ___ _

  1. 既存の GKE On-Prem 構成ファイルを開きます。 
  2. ` usercluster ` 仕様で、 [ ` antiaffinitygroups ` のドキュメント ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-to/installation/install?hl=ja#antiaffinitygroups) の説明に従って ` antiaffinitygroups ` フィールドを追加します。 
    
        usercluster:
          ...
          antiaffinitygroups:
            enabled: false
    

  3. ファイルを保存します。 
  4. 構成ファイルを使用してアップグレードします。クラスタはアップグレードされますが、この機能は有効になりません。 

**FEATURE:**

これで、クラスタの [ デフォルトのストレージ クラス ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/default-storage-class?hl=ja)
を設定できるようになります。

**FEATURE:**

クラスタのストレージ クラスとして [ Container Storage Interface (CSI) 1.0
](https://github.com/container-storage-interface/spec) を使用できるようになりました。

**FEATURE:**

` gkectl delete cluster --force ` を使用して、 [ 破損している、あるいは異常なユーザー クラスタを削除
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/deleting-a-user-cluster?hl=ja#delete_unhealthy_cluster)
できるようになりました。

**FEATURE:**

` debug-toolbox ` コンテナ イメージを使用して [ ノードの問題を診断
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/support/debug-
toolbox?hl=ja) できるようになりました。

**FEATURE:**

` gkectl ` コマンドで実行される [ 検証をスキップ ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/install?hl=ja#skip_validate) できるようになりました。

**FEATURE:**

` gkectl diagnose snapshot ` が作成する tarball に、デフォルトでコマンドの出力のログが含まれるようになりました。

**FEATURE:**

` gkectl diagnose snapshot ` フラグ ` --seed-config ` を追加します。このフラグを渡すと、 `
snapshot ` によって生成された tarball にクラスタの GKE on-prem 構成ファイルが含まれます。

###  変更

**CHANGED:**

` gkeplatformversion ` フィールドが GKE on-prem 構成ファイルから削除されました。クラスタのバージョンを指定するには、 `
bundlepath ` フィールドにバージョンのバンドルを指定します。

**CHANGED:**

[ ` antiaffinitygroups ` ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/install?hl=ja#antiaffinitygroups)
を使用するには、vSphere 権限 ` Host.Inventory.EditCluster ` を追加する必要があります。

**CHANGED:**

` --snapshot-config ` （以前は ` --config ` ）を渡して ` gkectl diagnose snapshot `
の構成ファイルを指定するようになりました。 [ クラスタの問題の診断
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/diagnose?hl=ja#diagnose_snapshot) を参照してください。

**CHANGED:**

` --snapshot-config ` （以前は ` --config ` ）を渡して、 ` gkectl diagnose snapshot `
でクラスタの構成ファイルを取得するようになりました。 [ クラスタの問題の診断
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/diagnose?hl=ja#diagnose_snapshot) を参照してください。

**CHANGED:**

管理クラスタの kubeconfig ではなくユーザー クラスタの kubeconfig を指定した場合、 ` gkectl diagnose `
コマンドでエラーが返されるようになりました。

**CHANGED:**

Cloud Console で、登録済みユーザー クラスタのアップグレードが可能になると通知されるようになりました。

###  既知の問題

**ISSUE:**

OIDC を使用するバージョン 1.0.11、1.0.1-gke.5、1.0.2-gke.3 クラスタがバージョン 1.1
にアップグレードされないことが報告されています。修正はバージョン 1.1.1 を対象としています。バージョン
1.0.11、1.0.1-gke.5、1.0.2-gke.3 のクラスタを OIDC で構成した場合、クラスタをアップグレードできません。 [ GKE
on-prem のインストール ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/install?hl=ja) に従ってバージョン 1.1 クラスタを作成します。

##  2019 年 8 月 22 日

GKE on-prem バージョン 1.0.2-gke.3 が利用可能になりました。このパッチリリースには次の変更が含まれています。

###  新機能

**FEATURE:**

手動負荷分散で Seesaw がサポートされるようになりました。

**FEATURE:**

管理者クラスタとユーザー クラスタに別の vSphere ネットワークを指定できるようになりました。

**FEATURE:**

` gkectl ` を使用してユーザー クラスタを削除できるようになりました。 [ ユーザー クラスタの削除
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/deleting-a-user-cluster?hl=ja) をご覧ください。

###  変更

**CHANGED:** ` gkectl diagnose snapshot ` が、ユーザー クラスタ コントロール
プレーンからログが取得するようになりました。

**CHANGED:**

GKE on-prem OIDC 仕様が新しいフィールド（ ` kubectlredirecturl ` 、 ` scopes ` 、 `
extraparams ` 、 ` usehttpproxy ` ）で更新されました。

**CHANGED:**

Calico がバージョン 3.7.4 に更新されました。

**CHANGED:**

接頭辞が付いた Cloud Monitoring のシステム指標が ` external.googleapis.com/prometheus/ ` から `
kubernetes.io/anthos/ ` に変更されました。指標やアラートをトラッキングする場合は、ダッシュボードを次の接頭辞で更新します。

###  修正

**FIXED:**

[ CVE-2019-11247 に起因する脆弱性を修正しました
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/security-
bulletins?hl=ja#august-22-2019) 。

**FIXED:**

[ RBAC プロキシの脆弱性を修正しました ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/security-bulletins?hl=ja#august-23-2019) 。

##  2019 年 7 月 30 日

GKE on-prem バージョン 1.0.1-gke.5 が利用可能になりました。このパッチリリースには次の変更が含まれています。

###  新機能

**FEATURE:**

[ GKE on-prem クイック リファレンス ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/reference/cheatsheet?hl=ja) を公開しました。

###  変更

**CHANGED:**

静的 IP を使用している場合に、ノード IP の可用性が ` gkectl check-config ` によりチェックされるようになりました。

**CHANGED:**

` gkectl prepare ` が、VM の OVA イメージをアップロードする前に、VM が存在し、vSphere
でテンプレートとしてマークされているかどうかを確認するようになりました。

**CHANGED:**

vCenter クラスタとそのクラスタ内のリソースプールを指定するためのサポートを追加します。

**CHANGED:**

F5 BIG-IP コントローラをバージョン 1.9.0 にアップグレードします。

**CHANGED:**

Istio Ingress コントローラをバージョン 1.2.2 にアップグレードします。

###  修正済み

**FIXED:**

管理ワークステーションの Docker レジストリのレジストリ データの永続性の問題を修正しました。

**FIXED:**

ユーザー クラスタの名前が既に使用されているかどうかを確認する検証を修正しました。

##  2019 年 7 月 25 日

GKE on-prem バージョン 1.0.11 が利用可能になりました。

##  2019 年 6 月 17 日

GKE on-prem が一般提供されるようになりました。バージョン 1.0.10 には次の変更が含まれています。

###  ベータ版 -1.4 から 1.0.10 へのアップグレード

ベータ版クラスタを最初の一般提供バージョンにアップグレードする前に、 [ GKE on-prem ベータ版から一般提供にアップグレードする
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/upgrading/from-beta?hl=ja) の手順を行い、次の点を確認してください。

  * ベータ版 -1.4 より前のベータ版を実行している場合は、必ずベータ版 -1.4 にアップグレードしてください。 

  * ベータ版クラスタが（デフォルトの F5-BIG-IP ではなく）独自の L4 ロードバランサを実行している場合、最新の GKE on-prem バージョンを実行するには、クラスタを削除して再作成する必要があります。 

  * クラスタがベータ版 -1.3 からベータ版 -1.4 にアップグレードされた場合は、アップグレードの前に各ユーザー クラスタ __ に対して次のコマンドを実行します。 
    
        kubectl delete crd networkpolicies.crd.projectcalico.org

  * vCenter 証明書の検証が必要になりました。（ ` vsphereinsecure ` は現在サポートされていません。）ベータ版 1.4 クラスタを 1.0.10 にアップグレードする場合は、vCenter の信頼できるルート CA 公開証明書をアップグレード構成ファイルで指定する必要があります。 

  * 実行中のクラスタをすべて __ アップグレードする必要があります。クラスタがバージョンが混在した状態で実行されると、このアップグレードは上手くいきません。 

  * まず管理クラスタを最新バージョンにアップグレードしてから、ユーザー クラスタをアップグレードする必要があります。 

###  新機能

**FEATURE:**

[ 手動負荷分散モード ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/manual-lb?hl=ja) を有効にして、L4
ロードバランサを構成できるようになりました。デフォルトのロードバランサ F5 BIG-IP を使用することもできます。

**FEATURE:**

GKE on-prem の構成に基づくインストール プロセスが更新されました。単一の [ 構成ファイル
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/overview?hl=ja#config) を使用して宣言的にインストールするようになりました。

**FEATURE:**

` gkectl create-config ` を追加します。これは、GKE on-prem
のインストール、既存のクラスタのアップグレード、および既存のインストールでの追加のユーザー
クラスタの作成のための構成ファイルを生成します。これは、以前のバージョンのインストール ウィザードと ` create-config.yaml `
に置き換わるものです。 [ GKE on-prem のインストール
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=ja#generate_config) に関する最新のドキュメントをご覧ください。

**FEATURE:**

GKE on-prem 構成ファイルを検証する ` gkectl check-config ` を追加します。 [ GKE on-prem のインストール
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=ja#validate_config) に関する最新のドキュメントをご覧ください。

**FEATURE:**

オプションの ` --validate-attestations ` フラグを ` gkectl prepare `
に追加します。このフラグは、管理者ワークステーションに含まれるコンテナ イメージが Google
によって作成、署名され、デプロイの準備ができていることを確認します。 [ GKE on-prem のインストール
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=ja#prepare) に関する最新のドキュメントをご覧ください。

###  変更

**CHANGED:**

Kubernetes バージョンを 1.12.7-gke.19 にアップグレードします。 [ クラスタをこのバージョンにアップグレード
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters?hl=ja) できるようになりました。Kubernetes バージョン
1.11.2-gke.19 を実行するクラスタは作成できなくなりました。

管理クラスタをアップグレードしてから、ユーザー クラスタをアップグレードすることをおすすめします。

**CHANGED:**

Istio Ingress コントローラをバージョン 1.1.7 にアップグレードします。

**CHANGED:**

vCenter 証明書の検証が必要になりました。（ ` vsphereinsecure ` は現在サポートされていません。）GKE on-prem
構成ファイルの ` cacertpath ` フィールドで、証明書を指定します。

クライアントが vCenter Server を呼び出す場合、vCenter Server は証明書を提示してクライアントに自身の ID
を証明する必要があります。証明書には認証局（CA）が署名する必要があります。証明書は自己署名できません。

ベータ版 1.4 クラスタを 1.0.10 にアップグレードする場合は、vCenter の信頼できるルート CA
公開証明書をアップグレード構成ファイルで指定する必要があります。

###  既知の問題

**ISSUE:**

[ クラスタをアップグレードする ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/upgrading-clusters?hl=ja) と、 [ PodDisruptionBudgets
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) （PDB）を使用するワークロードで中断やダウンタイムが発生することがあります。

**ISSUE:**

[ 手動負荷分散モード ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/manual-lb?hl=ja) を使用するベータ版クラスタは、GKE on-
prem バージョン 1.0.10
にアップグレードできない場合があります。これらのクラスタでアップグレードして独自のロードバランサを引き続き使用するには、クラスタを再作成する必要があります。

##  2019 年 5 月 24 日

GKE on-prem ベータ版バージョン 1.4.7 が利用可能になりました。このリリースには次の変更が含まれています。

###  新機能

**FEATURE:**

[ ` gkectl diagnose snapshot ` ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.4/how-to/administration/diagnose?hl=ja#capture_admin)
コマンドで、 ` --admin-ssh-key-path ` パラメータを省略できるようになりました。

###  変更

**CHANGED:**

2019 年 5 月 8 日に、Cloud Console を使用して GKE On-Prem クラスタを操作できるサービス Connect
に変更を加えました。新しい Connect エージェントを使用するには、クラスタを Cloud Console に再登録するか、Anthos GKE On-
Prem ベータ版 -1.4 にアップグレードする必要があります。

GKE on-prem クラスタ、およびこれらのクラスタで実行されているワークロードは、中断なく動作し続けます。ただし、クラスタを再登録するか、ベータ版
-1.4 にアップグレードするまで Cloud Console には表示されません。

再登録またはアップグレードする前に、サービス アカウントに ` gkehub.connect ` のロールがあることを確認してください。また、サービス
アカウントに以前の clusterregistry.connect ロールがある場合は、そのロールを削除することをおすすめします。

サービス アカウントに gkehub.connect のロールを付与します。

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

サービス アカウントに以前の ` clusterregistry.connect ` ロールがある場合は、以前のロールを削除します。

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

クラスタを再登録するか、Anthos GKE on-prem ベータ版 -1.4 にアップグレードします。

[ クラスタを再登録するには ](https://cloud.google.com/kubernetes-engine/connect/updating-
agent?hl=ja) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]
          

[ Anthos GKE on-prem ベータ版 -1.4 にアップグレードするには
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=ja) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  既知の問題

**ISSUE:**

アップグレード中に Connect
エージェントが新しいバージョンに更新されない問題があります。この問題を回避するには、クラスタをアップグレードした後に次のコマンドを実行します。

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  2019 年 5 月 13 日

###  既知の問題

**ISSUE:**

ベータ版 -1.2 からベータ版 -1.3
にアップグレードされたクラスタは、クラスタの構成ファイルを損傷し、将来のクラスタのアップグレードを妨げる既知の問題の影響を受ける可能性があります。この問題は、今後のクラスタのアップグレードに影響します。

この問題は、ベータ版 -1.2 からベータ版 -1.3 にアップグレードしたクラスタを削除して再作成することで解決できます。

クラスタの削除および再作成をせずに問題を解決するには、各クラスタの Secret を再エンコードして適用する必要があります。次の手順を行います。

  1. 管理クラスタに保存されている ` create-config ` Secret の内容を取得します。これは、kube-system 名前空間の ` create-config ` Secret と、各ユーザー クラスタの名前空間の ` create-config ` Secret に対して行う必要があります。 
    
        kubectl get secret create-config -n kube-system -o jsonpath={.data.cfg} | base64 -d > kube-system_create_secret.yaml
    
        kubectl get secret create-config -n [USER_CLUSTER_NAME] -o jsonpath={.data.cfg} | base64 -d > [USER_CLUSTER_NAME]_create_secret.yaml

  2. ユーザー クラスタごとに、エディタで ` [USER_CLUSTER_NAME]  _create_secret.yaml ` ファイルを開きます。 ` registerserviceaccountkey ` と ` connectserviceaccountkey ` の値が ` REDACTED ` でない場合、追加の操作は必要ありません（Secret を再エンコードしてクラスタに書き込む必要はありません）。 
  3. 別のエディタで元の ` create_config.yaml ` ファイルを開きます。 
  4. ` [USER_CLUSTER_NAME]  _create_secret.yaml ` で、 ` registerserviceaccountkey ` 値と ` connectserviceaccountkey ` 値を元の ` create_config.yaml ` ファイルの値に置き換えます。変更したファイルを保存します。 
  5. 各 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` と ` kube-system_create_secret.yaml ` ファイルでステップ 3～5 を繰り返します。 
  6. 各 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` ファイルと ` kube-system_create_secret.yaml ` ファイルを Base64 エンコードします。 
    
        cat [USER_CLUSTER_NAME]_create_secret.yaml | base64 > [USER_CLUSTER_NAME]_create_secret_create_secret.b64
    
        cat kube-system-cluster_create_secret.yaml | base64 >kube-system-cluster_create_secret.b64

  7. クラスタ内の各 Secret の ` data[cfg] ` フィールドを、対応するファイルの内容に置き換えます。 
    
        kubectl edit secret create-config -n [USER_CLUSTER_NAME]
    
      # kubectl edit opens the file in the shell's default text editor
      # Open `first-user-cluster_create_secret.b64` in another editor, and replace
      # the `cfg` value with the copied value
      # Make sure the copied string has no newlines in it!

  8. 各 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` Secret と ` kube-system_create_secret.yaml ` Secret でステップ 8 を繰り返します。 
  9. 更新が正常に完了したことを確認するには、ステップ 1 を繰り返します。 

##  2019 年 5 月 7 日

GKE on-prem ベータ版バージョン 1.4.1 が利用可能になりました。このリリースには次の変更が含まれています。

###  新機能

**FEATURE:**

[ ` gkectl diagnose snapshot ` ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.4/how-to/administration/diagnose?hl=ja#capture_admin)
コマンドで、 ` --admin-ssh-key-path ` パラメータを省略できるようになりました。

###  変更

**CHANGED:**

2019 年 5 月 8 日に、Cloud Console を使用して GKE On-Prem クラスタを操作できるサービス Connect
に変更を加えました。新しい Connect エージェントを使用するには、クラスタを Cloud Console に再登録するか、Anthos GKE On-
Prem ベータ版 -1.4 にアップグレードする必要があります。

GKE on-prem クラスタ、およびこれらのクラスタで実行されているワークロードは、中断なく動作し続けます。ただし、クラスタを再登録するか、ベータ版
-1.4 にアップグレードするまで Cloud Console には表示されません。

再登録またはアップグレードする前に、サービス アカウントに gkehub.connect のロールがあることを確認してください。また、サービス
アカウントに以前の clusterregistry.connect ロールがある場合は、そのロールを削除することをおすすめします。

サービス アカウントに gkehub.connect のロールを付与します。

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

サービス アカウントに以前の clusterregistry.connect ロールがある場合は、以前のロールを削除します。

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

クラスタを再登録するか、Anthos GKE on-prem ベータ版 -1.4 にアップグレードします。

[ クラスタを再登録するには ](https://cloud.google.com/kubernetes-engine/connect/updating-
agent?hl=ja) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]
          

[ Anthos GKE on-prem ベータ版 -1.4 にアップグレードするには
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=ja) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  既知の問題

**ISSUE:**

アップグレード中に Connect
エージェントが新しいバージョンに更新されない問題があります。この問題を回避するには、クラスタをアップグレードした後に次のコマンドを実行します。

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  2019 年 4 月 25 日

GKE on-prem ベータ版バージョン 1.3.1 が利用可能になりました。このリリースには次の変更が含まれています。

###  新機能

**FEATURE:**

` gkectl diagnose snapshot ` コマンドに [ ` --dry-run `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/diagnose?hl=ja#performing_a_dry_run_for_a_snapshot)
フラグが追加されました。

**FEATURE:**

` gkectl diagnose snapshot ` コマンドで 4 つの [ シナリオ
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/diagnose?hl=ja#snapshot_scenarios) がサポートされるようになりました。

**FEATURE:**

` gkectl diagnose snapshot ` コマンドで、名前空間を指定する正規表現がサポートされるようになりました。

###  変更

**CHANGED:**

Istio 1.1 がデフォルトの [ Ingress コントローラ
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/upgrading-a-cluster?hl=ja#upgrading_the_ingress_controller)
になりました。Ingress コントローラは、管理クラスタとユーザー クラスタの両方の ` gke-system `
名前空間で実行されます。これにより、Ingress の TLS 管理が容易になります。Ingress を有効にするか、アップグレード後に Ingress
を再度有効にするには、 [ Ingress を有効にする ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.3/how-to/installation/install?hl=ja#enabling_ingress)
の手順に従います。

**CHANGED:**

` gkectl ` ツールは、ブートストラップに Minikube と KVM を使用しなくなりました。つまり、管理ワークステーション VM
でネストされた仮想化を有効にする必要はありません。

###  既知の問題

**ISSUE:**

GKE on-prem の Ingress コントローラは、Istio 1.1 と自動 Secret 検出を使用します。ただし、Secret 検出のノード
エージェントは、Secret の削除後に Secret の更新を取得できない場合があります。そのため、Secret は削除しないでください。Secret
を削除する必要があり、その後 Ingress TLS が失敗する場合は、gke-system 名前空間で Ingress Pod を手動で再起動します。

##  2019 年 4 月 11 日

GKE on-prem ベータ版バージョン 1.2.1 が利用可能になりました。このリリースには次の変更が含まれています。

###  新機能

**FEATURE:**

GKE On-prem クラスタが、 [ Connect ](https://cloud.google.com/kubernetes-
engine/connect?hl=ja) を使用して自動的に Google に接続するようになりました。

**FEATURE:**

ユーザー クラスタごとに最大 3 つのコントロール プレーンを実行できるようになりました。

###  変更

**CHANGED:**

` gkectl ` が、クラスタを作成する vSphere と F5 BIG-IP 認証情報を検証するようになりました。

###  既知の問題

**ISSUE:**

回帰により ` gkectl diagnose snapshot ` コマンドが誤った SSH キーを使用するため、このコマンドがユーザー
クラスタから情報を収集できなくなります。サポートケースの回避策として、個々のユーザー クラスタノードに SSH
接続し、手動でデータを収集する必要がある場合があります。

##  2019 年 4 月 2 日

GKE on-prem ベータ版バージョン 1.1.1 が利用可能になりました。このリリースには次の変更が含まれています。

###  新機能

**FEATURE:**

[ Open Virtual Appliance ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.1/how-to/installation/getting-
started?hl=ja#download_ova) （OVA、複数のコマンドライン インターフェース ツールを含む事前構成済みの仮想マシンイメージ）で
GKE on-prem をインストールするようになりました。この変更により、インストールが容易になり、仮想化のレイヤが取り除かれます。Docker
コンテナ内で ` gkectl ` を実行する必要はありません。

ベータ版 -1.1.1 より前の GKE on-prem
バージョンをインストールした場合は、文書化された手順に従い新しい管理ワークステーションを作成する必要があります。新しい管理ワークステーションをインストールしたら、SSH
認証鍵、構成ファイル、kubeconfigs などの必要なファイルを以前のワークステーションから新しいワークステーションにコピーします。

**FEATURE:**

[ クラスタのバックアップと復元 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.1/how-to/administration/backing-up?hl=ja)
に関するドキュメントを追加しました。

**FEATURE:**

OIDC と ADFS を使用して、クラスタの認証を構成できるようになりました。詳しくは、 [ OIDC と ADFS による認証
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.1/how-
to/security/oidc-adfs?hl=ja) と [ 認証
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/concepts/authentication?hl=ja) をご覧ください。

###  変更

**CHANGED:**

` gkectl diagnose snapshot ` を実行するために、管理クラスタの秘密鍵を使用しなければならなくなりました。

**CHANGED:**

インストール中に、マルチマスター ユーザー クラスタをデプロイするための構成オプションを追加しました。

**CHANGED:**

[ Connect のドキュメント ](https://cloud.google.com/kubernetes-engine/connect?hl=ja)
が移行されました。

###  修正済み

**FIXED:**

ノードが予期せず削除された場合にクラスタ ネットワークが中断される問題を修正しました。

###  既知の問題

**ISSUE:**

GKE on-prem の構成管理がバージョン 0.11 から 0.13 にアップグレードされました。一部のシステム
コンポーネントの名前が変更されました。以前のバージョンのリソースをクリーンアップして新しいインスタンスをインストールするには、いくつかの手順を実行する必要があります。

構成管理のアクティブなインスタンスがある場合:

  1. インスタンスをアンインストールします。 
    
        kubectl -n=nomos-system delete nomos --all

  2. インスタンスの名前空間にリソースがないことを確認します。 
    
        kubectl -n nomos-system get all

  3. 名前空間を削除します。 
    
        kubectl delete ns nomos-system

  4. CRD を削除します。 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  5. 演算子の kube-system リソースをすべて削除します。 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

構成管理のアクティブなインスタンスがない場合:

  1. 構成管理の名前空間を削除します。 
    
        kubectl delete ns nomos-system

  2. CRD を削除します。 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  3. 演算子の kube-system リソースをすべて削除します。 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

##  2019 年 3 月 12 日

GKE on-prem ベータ版バージョン 1.0.3 が利用可能になりました。このリリースには次の変更が含まれています。

###  修正済み

**FIXED:**

Docker 証明書が間違った場所に保存される問題を修正しました。

##  2019 年 3 月 4 日

GKE on-prem ベータ版バージョン 1.0.2 が利用可能になりました。このリリースには次の変更が含まれています。

###  新機能

**FEATURE:**

` gkectl version ` を実行して、実行中の ` gkectl ` のバージョンを確認できるようになりました。

**FEATURE:**

[ ユーザー クラスタを今後のベータ版にアップグレード ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.0/how-to/administration/upgrading-a-cluster?hl=ja)
できるようになりました。

**FEATURE:**

[ Anthos Config Management ](https://cloud.google.com/anthos-config-
management/docs?hl=ja) バージョン 0.11.6 が利用可能になりました。

**FEATURE:**

Stackdriver Logging が各ノードで有効になりました。デフォルトでは、ロギング エージェントは、コントロール プレーン サービス、クラスタ
API、vSphere コントローラ、Calico、BIG-IP コントローラ、Envoy プロキシ、Connect、Anthos Config
Management、Prometheus サービス、Grafana サービス、Istio コントロール プレーン、Docker のログのみを GCP
プロジェクトに複製します。アプリケーション コンテナ ログはデフォルトで除外されますが、必要に応じて有効にできます。

**FEATURE:**

Stackdriver Prometheus Sidecar は、ロギング エージェントと同じコンポーネントの指標を取得します。

**FEATURE:**

[ Kubernetes ネットワーク ポリシー ](https://kubernetes.io/docs/concepts/services-
networking/network-policies/) がサポートされるようになりました。

###  変更

**CHANGED:**

クラスタ仕様の IP ブロックを更新して、特定のクラスタの IP 範囲を拡張できるようになりました。

**CHANGED:**

アルファ版でインストールしたクラスタがベータ版後に Google から接続解除された場合は、再度接続する必要があることがあります。 [ 手動によるユーザー
クラスタの登録 ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/registering-a-user-cluster?hl=ja) をご覧ください。

**CHANGED:**

[ スタートガイド ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/getting-started?hl=ja) が更新され、サービス アカウントを有効にして ` gkectl prepare
` を実行する手順が追加されました。

**CHANGED:**

` gkectl diagnose snapshot `
が構成データのみを収集し、ログを除外するようになりました。このツールは、サポートケースを開く前に環境の詳細を取得するために使用されます。

**CHANGED:**

クラスタ作成時の F5 BIG-IP のオプションの SNAT プール名構成のサポート。これを使用して、 [ F5 BIG-IP コントローラ
](https://clouddocs.f5.com/products/connectors/k8s-bigip-ctlr/v1.8/) で「--vs-
snat-pool-name」の値を設定できます。

**CHANGED:**

管理クラスタで実行されるアドオンの VIP を指定しなければならなくなりました。

###  修正済み

**FIXED:**

クラスタのサイズ変更操作が改善され、意図しないノードの削除が防止されるようになりました。

##  2019 年 2 月 7 日

GKE on-prem アルファ版バージョン 1.3 が利用可能になりました。このリリースには次の変更が含まれています。

###  新機能

**FEATURE:**

インストール時に、YAML ファイルに ` nodeip ` ブロックを指定して静的 IPAM を構成できるようになりました。

###  変更

**CHANGED:**

vSphere データストアに 100 GB のディスクをプロビジョニングしなければならなくなりました。GKE on-prem
はこのディスクを使用して、重要なデータ（etcd など）を保存します。 [ システム要件
](https://cloud.google.com/anthos/gke/docs/on-prem/requirements?hl=ja)
でご確認ください。

**CHANGED:**

` nodeip ` ブロックに小文字のホスト名のみを指定できるようになりました。

**CHANGED:**

GKE on-prem でユーザー クラスタに一意の名前が適用されるようになりました。

**CHANGED:**

Istio エンドポイントを使用する指標エンドポイントと API は、mTLS とロールベースのアクセス制御を使用して保護されるようになりました。

**CHANGED:**

Grafana による外部通信が無効になりました。

**CHANGED:**

Prometheus と Alertmanager のヘルスチェックを改善しました。

**CHANGED:**

Prometheus がセキュリティ保護されたポートを使用して指標を取得するようになりました。

**CHANGED:**

Grafana ダッシュボードに関するアップデート。

###  既知の問題

**ISSUE:**

vCenter ユーザー アカウントで ` DOMAIN\USER ` のような形式を使用している場合に、バックスラッシュ（ ` DOMAIN\\USER
` ）をエスケープする必要がある場合があります。インストール中にユーザー アカウントを入力するよう求められた場合に、必ずこれを実行してください。

##  2019 年 1 月 23 日

GKE on-prem アルファ版バージョン 1.2.1 が利用可能になりました。このリリースには次の変更が含まれています。

###  新機能

**FEATURE:**

` gkectl ` を使用して [ 管理クラスタを削除 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/deleting-an-admin-cluster?hl=ja)
できるようになりました。

###  変更

**CHANGED:**

` gkectl diagnose snapshot ` コマンドで、リモート
コマンドの結果とファイルのスナップショットの取得中にノードを指定できるようになりました。

##  2019 年 1 月 14 日

GKE on-prem アルファ版バージョン 1.1.2 が利用可能になりました。このリリースには次の変更が含まれています。

###  新機能

**FEATURE:**

` gkectl prepare ` コマンドで、GKE on-prem のコンテナ イメージの pull および push
ができるようになりました。そのため、 ` populate_registry.sh ` スクリプトは非推奨になります。

**FEATURE:**

` gkectl prepare ` で、vSphere クラスタとリソースプールに関する情報を入力するように求められるようになりました。

**FEATURE:**

` gkectl create ` コマンドで、ユーザー クラスタを作成して既存の管理コントロール
プレーンに追加できるようになりました。これは、クラスタの作成時にプロンプトが表示されたときに、既存の kubeconfig
ファイルを渡すことにより達成できます。

**FEATURE:**

クラスタの作成時に、管理者クラスタとユーザー クラスタの Ingress TLS Secret
を渡すことができるようになりました。次のプロンプトが表示されます。

` Do you want to use TLS for Admin Control Plane/User Cluster ingress? `

TLS Secret と証明書を指定すると、 ` gkectl ` で Ingress TLS を設定できます。TLS のインストールでは、HTTP
は自動的に無効になりません。

###  変更

**CHANGED:**

GKE On-Prem で Kubernetes バージョン **1.11.2-gke.19** が実行されるようになりました。

**CHANGED:**

GKE On-Prem のデフォルトのフットプリントが変更されました。

  * ユーザー クラスタ ノードの最小メモリ要件が 8,192 MB になりました。 

**CHANGED:**

GKE On-Prem で minikube バージョン **0.28.0** が実行されるようになりました。

**CHANGED:**

GKE Policy Management がバージョン **0.11.1** にアップグレードされました。

**CHANGED:**

` gkectl ` で、デフォルトでプロキシ構成を指定するように求められなくなりました。

**CHANGED:**

ユーザー クラスタの名前空間には、 ` cluster-api-etcd-metrics-config ` 、 ` kube-etcd-metrics-
config ` 、 ` kube-apiserver-config ` の 3 つの新しい ConfigMap リソースがあります。GKE on-prem
はこれらのファイルを使用して、指標プロキシ コンテナをすばやくブートストラップします。

**CHANGED:**

kube-apiserver イベントがイベントの etcd に配置されるようになりました。kube-etcd イベントはユーザー
クラスタの名前空間に表示されます。

**CHANGED:**

クラスタ API コントローラでリーダー選択が使用されるようになりました。

**CHANGED:**

vSphere の認証情報が認証情報ファイルから取得されるようになりました。

**CHANGED:**

` gkectl diagnose ` コマンドが管理者クラスタとユーザー クラスタの両方で機能するようになりました。

**CHANGED:**

` gkectl diagnose snapshot ` で、ノード上のリモート ファイルのスナップショット、ノード上のリモート コマンドの結果、および
Prometheus クエリを取得できるようになりました。

**CHANGED:**

` gkectl diagnose snapshot ` が複数の並列スレッドでスナップショットを取得できるようになりました。

**CHANGED:**

` gkectl diagnose snapshot ` で、スナップショットの結果から除外する単語を指定できるようになりました。

###  修正済み

**FIXED:**

予期しないネットワーク呼び出しを引き起こした minikube キャッシュの問題を修正しました。

**FIXED:**

F5 BIG-IP 認証情報の取得に関する問題を修正しました。環境変数を使用せずに認証情報ファイルから認証情報を読み取るようになりました。

###  既知の問題

**ISSUE:**

` gkectl prepare ` を実行すると、次の [ ` govmomi `
](https://github.com/vmware/govmomi) 警告が表示されることがあります。

` Warning: Line 102: Unable to parse 'enableMPTSupport' for attribute 'key' on
element 'Config' `

**ISSUE:**

ユーザー クラスタのサイズを変更すると、意図しないノードの削除や再作成が発生する可能性があります。

**ISSUE:**

PersistentVolumes がマウントに失敗し、 ` devicePath is empty `
エラーが発生することがあります。この問題を回避するには、関連する PersistentVolumeClaim を削除してから再作成してください。

**ISSUE:**

IPAM アドレス ブロックのサイズ変更はアルファ版ではサポートされません（ノードに静的 IP 割り当てを使用する場合）。これを回避するには、現在より多くの
IP アドレスを割り当てることを検討してください。

**ISSUE:**

遅いディスクでは、VM の作成がタイムアウトし、デプロイが失敗する可能性があります。このような場合は、すべてのリソースを削除してからもう一度試してください。

##  2018 年 12 月 19 日

GKE on-prem アルファ版 1.0.4 が利用可能になりました。このリリースには次の変更が含まれています。

###  修正済み

**FIXED:**

[ CVE-2018-1002105 ](https://github.com/kubernetes/kubernetes/issues/71411)
に起因する脆弱性が修正されました。

##  2018 年 11 月 30 日

GKE on-prem アルファ版 1.0 が利用可能になりました。このリリースには次の変更が含まれています。

###  変更

**CHANGED:**

GKE On-Prem アルファ版 1.0 は Kubernetes 1.11 を実行します。

**CHANGED:**

GKE On-Prem のデフォルトのフットプリントが変更されました。

  * 管理コントロール プレーンは 3 つのノードを実行し、4 基の CPU と 16 GB のメモリを使用します。 
  * ユーザー コントロール プレーンは 1 つのノードを実行し、4 基の CPU と 16 GB のメモリを使用します。 
  * ユーザー クラスタは 3 つ以上のノードを実行し、4 基の CPU と 16 GB のメモリを使用します。 

**CHANGED:**

高可用性 Prometheus セットアップのサポート。

**CHANGED:**

カスタム アラート マネージャー構成のサポート。

**CHANGED:**

Prometheus が **2.3.2** から **2.4.3** にアップグレードされました。

**CHANGED:**

Grafana が **5.0.4** から **5.3.4** にアップグレードされました。

**CHANGED:**

kube-state-metrics が **1.3.1** から **1.4.0** にアップグレードされました。

**CHANGED:**

Alert Manager が **1.14.0** から **1.15.2** にアップグレードされました。

**CHANGED:**

node_exporter が **1.15.2** から **1.16.0** にアップグレードされました。

###  修正済み

**FIXED:**

[ CVE-2018-1002103 ](https://github.com/kubernetes/minikube/issues/3208)
に起因する脆弱性が修正されました。

###  既知の問題

**ISSUE:**

PersistentVolumes がマウントに失敗し、 ` devicePath is empty `
エラーが発生することがあります。この問題を回避するには、関連する PersistentVolumeClaim を削除してから再作成してください。

**ISSUE:**

IPAM アドレス ブロックのサイズ変更はアルファ版ではサポートされません（ノードに静的 IP 割り当てを使用する場合）。これを回避するには、現在より多くの
IP アドレスを割り当てることを検討してください。

**ISSUE:**

GKE on-prem アルファ版 1.0 は、まだすべての適合性テストに合格していません。

**ISSUE:**

管理クラスタごとに作成できるユーザー クラスタは 1 つだけです。追加のユーザー クラスタを作成するには、別の管理者クラスタを作成します。

##  2018 年 10 月 31 日

GKE on-prem EAP 2.1 が利用可能になりました。このリリースには次の変更が含まれています。

###  変更

**CHANGED:**

管理者クラスタとユーザー クラスタを同時に作成する場合に、管理者クラスタの F5 BIG-IP 認証情報を再利用してユーザー
クラスタを作成できるようになりました。また、CLI では BIG-IP 認証情報を指定する必要があります。この要件は、 ` --dry-run `
を使用してスキップすることはできません。

**CHANGED:**

F5 BIG-IP コントローラが、最新の OSS バージョン 1.7.0 を使用するようにアップグレードされました。

**CHANGED:**

遅い vSphere マシンの安定性を向上させるために、クラスタマシンの作成タイムアウト時間が 15 分（以前は 5 分）になりました。

##  2018 年 10 月 17 日

GKE on-prem EAP 2.0 が利用可能になりました。このリリースには次の変更が含まれています。

###  変更

**CHANGED:**

GKE Connect のサポート。

**CHANGED:**

Monitoring のサポート。

**CHANGED:**

限定公開レジストリを使用したインストールのサポート。

**CHANGED:**

F5 BIG-IP で L4 VIP として L7 ロードバランサのフロントエンドをサポート。

**CHANGED:**

クラスタ ブートストラップ時のノードの静的 IP 割り当てのサポート。

###  既知の問題

**ISSUE:**

管理クラスタごとに作成できるユーザー クラスタは 1 つだけです。追加のユーザー クラスタを作成するには、別の管理者クラスタを作成します。

**ISSUE:**

クラスタのアップグレードは EAP 2.0 ではサポートされていません。

**ISSUE:**

遅いディスクでは、VM の作成がタイムアウトし、デプロイが失敗する可能性があります。このような場合は、すべてのリソースを削除してからもう一度試してください。

**ISSUE:**

クラスタのブートストラップ プロセスの一環として、存続期間の短い Minikube インスタンスが実行されます。使用される Minikube
バージョンにはセキュリティの脆弱性 [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) があります。

