#  リリースノート

このページには、Migrate for Compute Engine
に関する更新内容が記載されています。このページを定期的にチェックして、新機能や更新された機能、バグ修正、既知の問題、非推奨になった機能に関するお知らせを確認してください。

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ` https://cloud.google.com/feeds/migrate-for-compute-engine-release-
notes.xml ` を直接追加します。

このリリースのビルドやその他のビルドの一覧については、 [ ビルド履歴
](https://cloud.google.com/migrate/compute-engine/docs/build-history?hl=ja)
をご覧ください。

##  要件と OS サポート

[ 要件 ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/concepts/requirements?hl=ja) と [ サポートされているオペレーティング システム
](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=ja) をご覧ください。

##  4.10 新機能

###  Cloud Console の統合

**FEATURE:**

V4.10 は [ GCP Console ](https://cloud.google.com/cloud-console/?hl=ja)
と統合されているため、移行マネージャーをシームレスにデプロイし、必要なサービス アカウントを作成できます。

###  プライベート アクセス環境へのデプロイ

**FEATURE:**

V4.10 では、API プライベート アクセスが有効な環境へのデプロイのサポートが導入されています。これらの環境では、システムはパブリック IP
を使用せずにデプロイされ、クラウド API にアクセスするためのプライベート アクセスに依存します。 [ 移行マネージャの構成
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/configure-
manager/configuring-migration-manager?hl=ja) をご覧ください。

###  vCenter プラグインのデプロイ（オプション）

**FEATURE:**

V4.10 では、vCenter プラグインをデプロイするかどうかにかかわらず、オンプレミスのソース vCenter
環境にデプロイするオプションが導入されています。vCenter プラグインを使用せずにデプロイすると、同じ vCenter 環境に複数の Migrate
システムを接続できます。 [ VMware vCenter 環境の登録
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/configure-
manager/configuring-vms-vm?hl=ja#register_the_vmware_vcenter_environment)
をご覧ください。

###  Windows 2008 から 2012 へのアップグレード時の 事前 / 事後 のカスタム スクリプトのサポート

**FEATURE:**

V4.10 では、Windows アップグレードの使用時に 事前または事後の カスタム スクリプトを実行するためのサポートが導入されています。VM
にカスタム スクリプトを追加できます。詳細については、 [ Windows Server VM のアップグレード
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/upgrading-
vms/upgrading-windows-vms?hl=ja) をご覧ください。

###  Azure Gen2 インスタンスの Compute Engine への移行のサポート

**FEATURE:**

V4.10 では、 [ Azure Gen2 ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=ja) インスタンスから UEFI をサポートする
Compute Engine インスタンスへの移行がサポートされるようになっています。

###  O/S の自動検出とライセンスの割り当て

**FEATURE:**

V4.10 では、移行された OS の自動識別が導入されているため、デフォルトで正しいライセンスがVM に割り当てられるようになっています。Windows
BYOL ライセンスまたは Linux プレミアム ライセンスを使用して VM
を移行するシナリオでは、ランブックに入力として提供する必要があります。ドキュメントの [ ライセンス セクション
](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/runbooks?hl=ja) をご覧ください。

##  4.10.1

###  解決済みの問題

**FIXED:**

特定のボリューム構造の Windows パーティション検出に関する問題を修正しました。

**FIXED:**

4 TB を超える Azure ディスクのサポートを追加しました。

##  4.10

###  解決済みの問題

**FIXED:**

移行後に Windows イメージがクラッシュする原因となる AWS ENA ドライバの問題を修正しました。

##  4.10

###  既知の問題

**ISSUE:**

**#160405343:** SUSE のアクティベーション フローでの [ 動作の変更
](https://www.suse.com/support/kb/doc/?id=000019633) により、SUSE Enterprise Linux
インスタンスの接続解除後にリポジトリの構成が失敗するようになりました。

**回避策:** 接続を解除する前（移行前または接続解除前）に次の回避策を使用します。

  1. [ https://www.suse.com/support/kb/doc/?id=000019633 ](https://www.suse.com/support/kb/doc/?id=000019633) の状況 4 に記載された手順に従って、Compute Engine に必要なパッケージを tar.gz ファイルとしてダウンロードします。 
  2. **SLES 12.x の場合** 、次のコマンドを実行します。 
    
        sha1sum late_instance_offline_update_gce_SLE12.tar.gz
    tar -xf late_instance_offline_update_gce_SLE12.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm

  3. **SLES 15.x の場合** 、次のコマンドを実行します。 
    
        sha1sum late_instance_offline_update_gce_SLE15.tar.gz
    tar -xf late_instance_offline_update_gce_SLE15.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm

**ISSUE:**

**#149004085:** オンプレミスからの Ubuntu 14 が、接続解除後にネットワーク形成を開始できないことがあります。

**回避策:** シリアル コンソールを使用して接続し、DHCP にネットワーク インターフェースを手動で追加します。

**ISSUE:**

**#145086776:** まれに、RHEL7 の古いバージョンがストリーミング中に停止したり、カーネル
パニックが発生したりする場合があります。この問題は RHEL7 の今後のバージョンで解決されています。

**回避策:** ` sudo yum update ` を実行してから、システムを更新します。

**ISSUE:**

**＃145644737:** cloud-init を使用する Linux ディストリビューションのインスタンスから Azure または AWS
に作成されたクローンでは、Linux prep パッケージのインストール後に起動できないことがあります。

**回避策:** 移行の準備段階で、パッケージをアンインストールした後でクローンと再インストールを実行します。

**ISSUE:**

**#143313211:** RHEL 6.8 VM を移行すると、クラウドの宛先で起動の問題が発生することがあります。

RHEL 6.x システムがカーネル バージョン 2.6.32-xxx を使用していて、LVM を使用している場合、移行中の Compute Engine
起動時にカーネル パニックが発生することがあります。

**回避策:** 移行をする前にカーネルを 2.6.32-754 以降にアップグレードする必要があります。

**ISSUE:**

**＃143262721:** データディスクが 4 TB を超えると、Azure からの VM の移行が失敗します。

現時点で、Migrate for Compute Engine は 4 TB を超えるデータディスクを使用する Azure VM
の移行をサポートしていません。

**回避策:** VM のデータディスクが 4 TB より小さいことを確認します。

**ISSUE:**

**＃131532690:** Windows Server 2016 のワークロードで、Symantec Endpoint
Protection（SEP）がインストールされている場合に、クラウド内実行と移行オペレーションが失敗することがあります。これは、SEP
が無効になっているように思われる場合にも発生することがあります。

**回避策:** ワークロードのネットワーク インターフェース バインディングを変更して、SEP オプションを削除します。

  1. [ Microsoft Network VSP Bind（nvspbind） ](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850) のダウンロード 
  2. Microsoft_Nvspbind_package.EXE を c:\temp にインストールします。 
  3. 管理者としてコマンド プロンプトを開き、次のコマンドを実行します。 
    
        nvspbind.exe /d * symc_teefer2

**ISSUE:**

**#131614405:** Velostrata Prep RPM が SUSE Linux Enterprise Server 11
にインストールされている場合、VM は既存の静的 IP 構成に加えて DHCP IP アドレスを取得します。この問題は、VM が DHCP
サービスで有効になっているサブネット内でオンプレミスで起動された場合に発生します。

注: サブネットに DHCP サービスがない場合、この問題は発生しません。元の静的 IP アドレスとの通信には影響がありません。

**ISSUE:**

**#131637800:** Velostrata プラグインを登録した後、Cloud Extension
ウィザードを実行すると、「Finish」と表示されている場合にエラー「XXXXXXXXXX」が発生することがあります。

**回避策:** Velostrata プラグインの登録を解除し、vSphere ウェブ クライアント
サービスを再起動してから、プラグインを再登録します。問題が解決しない場合は、サポートにお問い合わせください。

**ISSUE:**

**#131548730:** VM を Run-in-Cloud に移行し、サードパーティの VM レベルのバックアップ
ソリューションで一時スナップショットを保持している場合、Migrate for Compute Engine バックアップ
ソリューションが一時スナップショットを削除した後も、定期的なライトバック オペレーションが完了しないことも時にはあります。VM 上の commit
されていない書き込みカウンタのサイズが大きくなると、オンプレミスで整合性チェックポイントが作成されません。

**回避策:** VM の [オンプレミスで実行] というアクションを選択し、タスクが完了するまで待ちます。これにより、保留中のすべての書き込みが
commit されます。次に、[クラウド内で実行] というアクションをもう一度選択します。保留中の書き込みを大量に commit
する場合には時間がかかることがあります。commit されていない書き込みが失われるため、強制オプションを使用しないでください。

**ISSUE:**

**＃131605387:** vCenter を再起動すると、vCenter の Velostrata タスクが UI に表示されなくなります。これは
vCenter の制限です。

**回避策:** Velostrata PowerShell モジュールを使用して、現在実行中の Velostrata マネージド VM または Cloud
Extensions のタスクをモニタリングします。

**ISSUE:**

**#131638716:** メンテナンス モードの ESXi ホストでは、VM
をクラウドに移動すると、オペレーションは失敗し、ロールバックの段階でスタックしてしまいます。

**回避策:** Run-in-Cloud タスクを手動でキャンセルし、VM をクラスタ内の別の ESXi ホストに移行してから、Run-in-Cloud
オペレーションを再試行します。

**ISSUE:**

**#131638455:** Run-in-
Cloudオペレーションが失敗し、「仮想マシンのスナップショットを作成できませんでした。試行された操作は現在の状態（電源がオフの状態）では実行できません。」と表示される。

**回避策:** VMware VM スナップショット
ファイルは、存在しないスナップショットを指している可能性があります。問題を解決するには、サポートにお問い合わせください。

**ISSUE:**

**#131534862:** まれに、ワークロードをオンプレミスで実行した後、ワークロード VMDK
がロックされることがあります。この問題は、Velostrata 管理アプライアンスとワークロードが実行されている ESXi
ホストの間のネットワーク中断が原因である場合があります。

注: この問題は 1 ～ 2 時間後に自然に解決されます。

**ISSUE:**

**#131550214:** 接続解除中に「操作はキャンセルされました」というエラー メッセージが表示され、操作が失敗することがあります。

**回避策:** 接続解除オペレーションを再試行してください。

**ISSUE:**

**#131650367:** 接続解除オペレーションを取り消した後、接続解除を実行するとアクションが失敗する可能性があります。

**回避策:** オペレーションを再試行します。

**ISSUE:**

**＃131649978:** 特定のシステム障害が発生した場合、Velostrata コンポーネントは vCenter
から切断されます。この場合、イベントが送信されず、アラームが正しく設定されていないか、正しく処理されていない可能性があります。

**回避策:** vCenter のアラームを手動でクリアします。

**ISSUE:**

**#131532549:** 販売店ライセンスを使用する Windows マシンのワークロードの場合、クラウドから戻るときにライセンスがない。

**回避策:** ライセンスを再インストールします。

**ISSUE:**

**＃131555885:** クラウドの VM がキャッシュ モードで実行されている場合は、vCenter の「OVA
のエクスポート」オペレーションを使用できますが、OVA が破損してしまいます。

**回避策:** 接続解除後にのみ OVA を作成します。

**ISSUE:**

**＃131647857:** タグ付けされる前にクラウド コンポーネント
インスタンスが作成され、システムに障害が発生した場合、インスタンスはタグ付けされないことがまれにあります。これにより、CE
の完全なクリーンアップや修復ができなくなります。

**回避策:** インスタンスに手動でタグ付けし、「修復」を実行します。

**ISSUE:**

**#131537125:** LVM 構成の Ubuntu OS を実行しているワークロードでは、Cloud Extension
の高可用性は機能しません。

**回避策:** カーネルを 3.13.0-161 以降に更新します。

**ISSUE:**

**#131560126:** Suse12: 4.2 より前の SUSE カーネルのバグにより、サブボリュームを持つ BTRFS
マウントを含む構成はサポートされていません。

**回避策:** カーネルが 4.2 以上の SUSE バージョン（SP2）にアップグレードします。

**ISSUE:**

**#131533480:** [Cloud Extension の作成] ウィザードを使用する場合、不正な HTTP プロキシ
アドレスを使用しても警告メッセージは生成されません。

**回避策:** CE を削除してから、有効な HTTP プロキシ アドレスを使用して CE を作成します。

**ISSUE:**

**#131647654:** オンプレミス
オペレーションの実行は成功しましたが、ステータスが「失敗」となり、「スナップショットの統合」というエラーが表示される。

**回避策:** vCenter を使用してスナップショットを統合し、エラーを手動でクリアします。

**ISSUE:**

**#131558198:** PowerShell 3.0 で実行すると、Cloud から Cloud へのランブック「Cloud Runbook に
PowerShell クライアントが格納されます。

**回避策:** PowerShell 4.0 にアップグレードします。

**ISSUE:**

**#131533056:** RHEL 7.4 を AWS から Google Cloud に移行する場合、Google Cloud
エージェントは自動的にインストールされません。

**回避策:** 手動でAWS エージェントを削除し、Google Cloud エージェントをインストールします。

**ISSUE:**

**#131532713:** Windows 2003R2 のオフライン移行後、NIC
を手動で削除すると、自動検出して自動的に再インストールできなくなることがあります。

回避策: VM ストレージを別の VM に接続でき、NIC レジストリ エントリは同様の VM
を使用して参照として手動でインポートできます。不明点はサポートまでお問い合わせください。

**ISSUE:**

**#131532666:** カーネル バージョン 2.6.32 を使用して実行されている Linux
バージョンでは、一時ストレージのアクセス障害でカーネル パニックが発生することがあります。これらは iSCSI
でのストリーミング中に発生しやすい傾向にあります。

回避策: カーネルをアップグレードします。また、接続解除後には問題が発生する可能性が低くなります。

**ISSUE:**

**#131532846:** 特定のファイアウォールやウィルス対策ソフトウェアを使用すると、iSCSI トラフィックをブロックして クラウドに移動する際に
Windows VM に障害が発生することがあります。

回避策: 移行中は該当するサービスを無効にし、接続解除後に再インストールします。

**ISSUE:**

**#131532882:** Windows の更新中にクラウド内実行を開始すると、更新が突然終了し、クラウドでの起動に失敗する可能性があります。

回避策: 移行前に Windows Update を完了するか、Windows Update を停止します。

**ISSUE:**

**#135664281:** Azure から Google Cloud への移行を完了またはキャンセルする際、Velostrata Management
がインポータを起動できなかった場合、Velostrata で作成されたリソースが元のインスタンスのリソース グループに残ります。

**ISSUE:**

**#133137658:** シナリオ: Migration Manager と VSphere の間にネットワーク接続がない。

ユーザーへの影響: RunInCloud タスクは、VSphere での getReadSessions の呼び出しが失敗したために停止します。

**回避策** : ネットワーク接続を修正します。もしくは、タスクをキャンセルしてもう一度お試しください。

**ISSUE:**

**#135573857** シナリオ: 「force」フラグを使用して VM をオンプレミスに戻した場合、スナップショットの統合に失敗すると、VM が
Velostrata によって管理されたままになります。マネージド VM では、同じ VM 上の RunInCloud
が許可されないため、失敗する可能性があります。

**回避策:** 数分待ってから、もう一度お試しください。

**ISSUE:**

**#137082702:** まれに、接続解除のキャンセル オペレーションが成功しても、VM インスタンスが起動しないことがあります。

**回避策** : インスタンスを元に戻し、もう一度クラウドに移動します。

