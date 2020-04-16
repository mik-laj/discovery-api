#  セキュリティに関する情報

Compute Engine に関連するセキュリティ情報は随時リリースされます。ここには、Compute Engine
に関するすべてのセキュリティ情報が記載されています。

[ Compute Engine のセキュリティ情報に登録する。 ![登録](https://cloud.google.com/images/feed-
icon.png?hl=ja) ](https://cloud.google.com/feeds/compute-engine-security-
bulletins.xml?hl=ja)

##  公開日: 2019 年 6 月 18 日

**最終更新日時: 2019 年 6 月 25 日 6:30（太平洋標準時間）**

説明  |  重大度  |  注  
---|---|---  
  
####  説明

先ごろ Netflix は、Linux カーネルにおける 3 件の TCP の脆弱性を公表しました。

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

これらの CVE は [ NFLX-2019-001 ](https://github.com/Netflix/security-
bulletins/blob/master/advisories/third-party/2019-001.md) と総称されます。

####  Compute Engine への影響

Compute Engine をホストするインフラストラクチャは、この脆弱性から保護されています。

Compute Engine VM が、パッチを適用していない Linux オペレーティング システムを実行しており、信頼されていないネットワーク
トラフィックを送受信する場合は、この DoS 攻撃に対する脆弱性が存在します。お使いのオペレーティング システム用のパッチが利用可能になったら、すぐに VM
インスタンスを更新してください。

TCP
接続を終端するロードバランサには、この脆弱性に対するパッチが適用されています。信頼されていないトラフィックでも、このようなロードバランサ経由でのみ受信する
Compute Engine インスタンスは脆弱ではありません。そのようなインスタンスとしては、HTTP ロードバランサ、SSL プロキシ
ロードバランサ、TCP プロキシ ロードバランサなどが挙げられます。

ネットワーク ロードバランサと内部ロードバランサでは、TCP 接続を終端しません。パッチを適用していない Compute Engine
インスタンスのうち、これらのロードバランサ経由で信頼されていないトラフィックを受信するインスタンスは脆弱です。

####  パッチ適用済みイメージとベンダーのリソース

各オペレーティング システム ベンダーからパッチが入手可能になると、ここにパッチ情報へのリンクが表示されます。これには各 CVE
に関するステータスが含まれます。これらの公開イメージの旧バージョンにはこうしたパッチが含まれないため、攻撃される可能性を軽減できません。

  * プロジェクト ` debian-cloud ` : 
    * ` debian-9-stretch-v20190618 `
  * プロジェクト ` centos-cloud ` : 
    * ` centos-6-v20190619 `
    * ` centos-7-v20190619 `
  * プロジェクト ` cos-cloud ` : 
    * ` cos-dev-77-12293-0-0 `
    * ` cos-beta-76-12239-21-0 `
    * ` cos-stable-75-12105-77-0 `
    * ` cos-73-11647-217-0 `
    * ` cos-69-10895-277-0 `
  * プロジェクト ` coreos-cloud ` : 
    * ` coreos-alpha-2163-2-1-v20190617 `
    * ` coreos-beta-2135-3-1-v20190617 `
    * ` coreos-stable-2079-6-0-v20190617 `
  * プロジェクト ` rhel-cloud ` : 
    * ` rhel-6-v20190618 `
    * ` rhel-7-v20190618 `
    * ` rhel-8-v20190618 `
  * プロジェクト ` rhel-sap-cloud ` : 
    * ` rhel-7-4-sap-v20190618 `
    * ` rhel-7-6-sap-v20190618 `
  * プロジェクト ` suse-cloud ` : 
    * ` sles-12-sp4-v20190617 `
    * ` sles-15-v20190617 `
  * プロジェクト ` suse-sap-cloud ` : 
    * ` sles-12-sp1-sap-v20190617 `
    * ` sles-12-sp2-sap-v20190617 `
    * ` sles-12-sp3-sap-v20190617 `
    * ` sles-12-sp4-sap-v20190617 `
    * ` sles-15-sap-v20190617 `
  * プロジェクト ` ubuntu-cloud ` : 
    * ` ubuntu-1604-xenial-v20190617 `
    * ` ubuntu-1804-bionic-v20190617 `
    * ` ubuntu-1810-cosmic-v20190618 `
    * ` ubuntu-1904-disco-v20190619 `
    * ` ubuntu-minimal-1604-xenial-v20190618 `
    * ` ubuntu-minimal-1804-bionic-v20190617 `
    * ` ubuntu-minimal-1810-cosmic-v20190618 `
    * ` ubuntu-minimal-1904-disco-v20190618 `

|  中  |

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

  
  
##  公開日: 2019 年 5 月 14 日

**最終更新日時: 2019 年 5 月 20 日 17:00（太平洋標準時間）**

説明  |  重大度  |  注  
---|---|---  
  
####  説明

次の CVE が Intel により開示されました。

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

これらの CVE は Microarchitectural Data
Sampling（MDS）と総称されます。これらの脆弱性により、マイクロアーキテクチャ状態での投機的実行の操作を通じてデータが公開されてしまう可能性があります。

####  Compute Engine への影響

**Compute Engine を実行するホスト インフラストラクチャは、お客様のワークロードを相互に分離します。信頼できないコードを VM
内で実行していない限り、以後の対応は特に必要ありません。**

Compute Engine 仮想マシン内の独自のマルチテナント サービスで信頼できないコードを実行しているお客様は、お使いのゲスト OS
ベンダーが提示する緩和策（Intel が提供するマイクロコード緩和機能の使用を含む）を参照してください。Google
では、新しいフラッシュ機能に対するゲストのパススルー アクセスをデプロイ済みです。次に示すのは、一般的なゲストイメージで実施できる緩和策の手順の概要です。

####  パッチ適用済みイメージとベンダーのリソース

各オペレーティング システム ベンダーからパッチが入手可能になると、ここにパッチ情報へのリンクが表示されます。これには各 CVE
に関するステータスが含まれます。これらのイメージを使用して、VM
インスタンスを作成してください。これらの公開イメージの旧バージョンにはこうしたパッチが含まれないため、攻撃される可能性を軽減できません。

  * プロジェクト ` centos-cloud ` : [ CESA-2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) 、 [ CESA-2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html)
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * プロジェクト ` coreos-cloud ` : [ CoreOS Container Linux に対応した MDS 緩和策 ](https://coreos.com/os/docs/latest/disabling-smt.html)
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * プロジェクト ` cos-cloud `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * プロジェクト ` debian-cloud ` : [ DSA-4444 ](https://www.debian.org/security/2019/dsa-4444)
    * ` debian-9-stretch-v20190514 `
  * プロジェクト ` rhel-cloud ` : [ Red Hat MDS ナレッジ記事 ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * プロジェクト ` rhel-sap-cloud ` : [ Red Hat MDS ナレッジ記事 ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * プロジェクト ` suse-cloud ` : [ SUSE MDS KB ](https://www.suse.com/support/kb/doc/?id=7023736)
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * プロジェクト ` suse-sap-cloud `
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * プロジェクト ` ubuntu-os-cloud ` : [ Ubuntu MDS Wiki ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS)
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * プロジェクト ` windows-cloud ` および ` windows-sql-cloud ` : [ Microsoft ADV190013 ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013)
    * バージョン番号 ` v20190514 ` を持つすべての Windows Server および SQL Server の公開イメージ。 
  * プロジェクト ` gce-uefi-images `
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * バージョン番号 ` v20190514 ` を持つすべての Windows Server 公開イメージ。 

####  Container-Optimized OS

ゲスト OS として Container Optimized OS（COS）を使用し、仮想マシン内で信頼できないマルチテナント
ワークロードを実行している場合は、次の手順を行うことをおすすめします。

  1. カーネル コマンドラインで ` nosmt ` を設定して、ハイパースレッディングを無効にします。   

既存の COS VM については、次のように ` grub.cfg ` を修正することで ` nosmt `
オプションを設定できます。設定したら、システムを再起動します。

    
        
    # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

便宜上、以下のスクリプトを実行して、上記のコマンドを実行した場合と同じ結果を得ることができます。このスクリプトは、cloud-config
の一部とするか、起動スクリプトまたはインスタンス テンプレートとして作成し、新しい VM
では必ず新しいパラメータが使用されるようにします。このスクリプトを実行する cloud-config の例は、以下に示すとおりです。

**警告:**
このコマンドの初回実行時は、インスタンスが直ちに再起動されます。その後、ハイパースレッディングが無効になっているインスタンスで実行しても、何も起こりません。

    
        
    # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

このスクリプトを cloud-config の一部として含めるには:

    
        
    #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

インスタンスでハイパースレッディングが無効になっているか確認するには、 ` /sys/devices/system/cpu/smt/active `
ファイルおよび ` /sys/devices/system/cpu/smt/control ` ファイルの出力を確認します。 ` active ` に対して
` 0 ` 、 ` control ` に対して ` off ` が返されている場合、ハイパースレッディングは無効になっています。

    
        
    cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**注:** インスタンスで UEFI セキュアブートを有効にしている場合は、UEFI セキュアブートを無効にした状態でインスタンスを再作成し、UEFI
セキュアブートを無効にした状態で上記のコマンドを実行してから、新しいインスタンスで UEFI セキュアブートを有効にする必要があります。

  2. 新しいバージョンの COS イメージを使用します。   

上記のようにハイパースレッディングを無効にすることに加え、上述の更新済みイメージか、さらに新しいバージョン（使用できる場合）の Container-
Optimized OS イメージを使用して [ インスタンスを再作成
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=ja#publicimage) し、脆弱性から完全に保護する必要があります。

|  中  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  公開日: 2018 年 8 月 14 日

**最終更新日時: 2018 年 8 月 20 日 17:00（太平洋標準時間）**

説明  |  重大度  |  注  
---|---|---  
  
####  説明

次の CVE が [ Intel により開示されました
](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) 。

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) （ [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) 関連） 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) （オペレーティング システムと [ SMT ](https://en.wikipedia.org/wiki/Hyper-Threading) 関連） 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) （仮想化関連） 

これらの CVE は「L1 Terminal Fault（L1TF）」と総称されます。

これらの L1TF 脆弱性は、投機的実行を悪用してプロセッサ レベルのデータ構造の構成を攻撃します。「L1」とは、レベル 1 データ
キャッシュ（L1D）と呼ばれるコア内の小さなリソースで、メモリアクセスを高速化するために使用されます。

これらの脆弱性と Compute Engine の緩和策の詳細については、 [ Google クラウドのブログ投稿
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=ja) をご覧ください。

####  Compute Engine への影響

Compute Engine を実行しお客様のワークロードを相互に分離するホスト インフラストラクチャは、既知の攻撃から保護されています。

Compute Engine
をご利用のお客様は、ゲスト環境内で間接的に悪用される可能性を防ぐために、イメージを更新することをおすすめします。これは、Compute Engine
仮想マシンで独自のマルチテナント サービスを実行している場合には特に重要です。

Google Compute Engine をお使いのお客様がご自分のインスタンスでゲスト オペレーティング
システムを更新する場合は、次のいずれかの方法をお使いください。

  * パッチ適用済みの公開イメージを使用して、 [ 既存の VM インスタンスを再作成する ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=ja#publicimage) 。 
  * オペレーティング システム ベンダーからパッチを入手して既存のインスタンスにインストールし、パッチ適用済みのインスタンスを再起動する。 

####  パッチ適用済みイメージとベンダーのリソース

各オペレーティング システム ベンダーからパッチが入手可能になると、ここにパッチ情報へのリンクが表示されます。これには各 CVE
に関するステータスが含まれます。これらのイメージを使用して、VM
インスタンスを作成してください。これらの公開イメージの旧バージョンにはこうしたパッチが含まれないため、攻撃される可能性を軽減できません。

  * プロジェクト ` centos-cloud ` : 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * プロジェクト ` coreos-cloud ` : 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * プロジェクト ` cos-cloud ` : 
    * ` cos-stable-66-10452-110-0 `
    * ` cos-stable-67-10575-66-0 `
    * ` cos-beta-68-10718-81-0 `
    * ` cos-dev-69-10895-23-0 `
  * プロジェクト ` debian-cloud ` : 
    * ` debian-9-stretch-v20180820 `
  * プロジェクト ` rhel-cloud ` : 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * プロジェクト ` rhel-sap-cloud ` : 
    * ` rhel-7-sap-apps-v20180814 `
    * ` rhel-7-sap-hana-v20180814 `
  * プロジェクト ` suse-cloud ` : 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
    * ` sles-11-sp4-v20180816 `
  * プロジェクト ` suse-sap-cloud ` : 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * プロジェクト ` ubuntu-os-cloud ` : 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `
  * プロジェクト ` windows-cloud ` ` gce-uefi-images ` および ` windows-sql-cloud ` : 
    * バージョン番号 ` -v201800814 ` 以降のすべての Windows Server と SQL Server の [ 公開イメージ ](https://cloud.google.com/compute/docs/images?hl=ja#os-compute-support) にパッチが含まれています。 

|  高  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  公開日: 2018 年 8 月 6 日

**最終更新日時: 2018 年 9 月 5 日 17:00（太平洋標準時間）**

説明  |  重大度  |  注  
---|---|---  
  
####  2018 年 9 月 5 日更新

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) は US-CERT によって 2018 年 8 月 14 日に開示されました。 [
CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
と同様に、これはカーネルレベルのネットワーク脆弱性で、脆弱性のあるシステムがサービス拒否（DoS）攻撃を受ける可能性が高まります。主な違いは、CVE-2018-5391
は IP 接続上で悪用されることです。両方の脆弱性が対象となるように、この情報を更新しました。

####  説明

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390)
（「SegmentSmack」）はカーネルレベルのネットワーク脆弱性で、脆弱性のあるシステムが TCP
接続でサービス拒否（DoS）攻撃を受ける可能性が高まります。

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391)
（「FragmentSmack」）はカーネルレベルのネットワーク脆弱性で、脆弱性のあるシステムが IP
接続でサービス拒否（DoS）攻撃を受ける可能性が高まります。

####  Compute Engine への影響

Compute Engine VM を実行するホスト インフラストラクチャには影響はありません。Compute Engine VM
との間のトラフィックを処理するネットワーク インフラストラクチャは、この脆弱性から保護されています。信頼されていないネットワーク
トラフィックでも、Compute Engine VM が [ HTTP(S) ](https://cloud.google.com/load-
balancing/docs/https/?hl=ja) 、 [ SSL ](https://cloud.google.com/load-
balancing/docs/ssl/?hl=ja) 、 [ TCP ロードバランサ ](https://cloud.google.com/load-
balancing/docs/tcp/?hl=ja) 経由でのみ送受信する場合は、この脆弱性から保護されています。

Compute Engine VM が、パッチを適用していないオペレーティング システムを実行しており、信頼されていないネットワーク
トラフィックを直接または [ ネットワーク ロードバランサ ](https://cloud.google.com/load-
balancing/docs/network/?hl=ja) 経由で送受信する場合は、この DoS 攻撃に対する脆弱性が存在します。

お使いのオペレーティング システム用のパッチが利用可能になったら、すぐに VM インスタンスを更新してください。

Compute Engine をお使いのお客様は、次のいずれかのオプションを使用して、インスタンスのゲスト オペレーティング システムを更新できます。

  * パッチ適用済みの公開イメージを使用して、 [ 既存の VM インスタンスを再作成する ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=ja#publicimage) 。パッチ適用済みの公開イメージは下のリストでご確認ください。 
  * オペレーティング システム ベンダーからパッチを入手して既存のインスタンスにインストールし、パッチ適用済みのインスタンスを再起動する。 

####  パッチ適用済みイメージとベンダーのリソース

各オペレーティング システム ベンダーからパッチが入手可能になると、ここにパッチ情報へのリンクが表示されます。

  * プロジェクト ` centos-cloud ` （CVE-2018-5390 のみ）: 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * プロジェクト ` coreos-cloud ` （CVE-2018-5390 と CVE-2018-5391）: 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * プロジェクト ` cos-cloud ` （CVE-2018-5390 と CVE-2018-5391）: 
    * ` cos-stable-65-10323-98-0 `
    * ` cos-stable-66-10452-109-0 `
    * ` cos-stable-67-10575-65-0 `
    * ` cos-beta-68-10718-76-0 `
    * ` cos-dev-69-10895-16-0 `
  * プロジェクト ` debian-cloud ` （CVE-2018-5390 と CVE-2018-5391）: 
    * ` debian-9-stretch-v20180814 `
  * プロジェクト ` rhel-cloud ` （CVE-2018-5390 のみ）: 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * プロジェクト ` suse-cloud ` （CVE-2018-5390 と CVE-2018-5391）: 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
  * プロジェクト ` suse-sap-cloud ` （CVE-2018-5390 と CVE-2018-5391）: 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * プロジェクト ` ubuntu-os-cloud ` （CVE-2018-5390 と CVE-2018-5391）: 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `

|  高  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  公開日: 2018 年 1 月 3 日

**最終更新日時: 2018 年 5 月 21 日 15:00（太平洋標準時間）**

説明  |  重大度  |  注  
---|---|---  
  
####  2018 年 5 月 21 日更新

[ CVE-2018-3640 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-3640) と [ CVE-2018-3639
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639) （それぞれバリアント 3a
と 4）は、 [ Intel によって開示 ](https://www.intel.com/content/www/us/en/security-
center/advisory/intel-sa-00115.html) されました。Spectre と Meltdown の最初の 3
つのバリアントと同様に、Compute Engine VM インスタンスを実行するインフラストラクチャは保護されており、お客様の VM
インスタンスは相互に分離されて保護されています。さらに、Compute Engine では、Intel のマイクロコード
パッチをインフラストラクチャにデプロイする予定であり、これにより、単一の VM インスタンス内で信頼できないワークロードまたはマルチテナント
ワークロードを実行するお客様は、オペレーティング システムのベンダーやプロバイダによって提供される VM 内追加対策を有効にできます。マイクロコード
パッチは、Intel によって認定され、Compute Engine で本番環境に対してテストおよび認定された後、Compute Engine
にデプロイされます。パッチが使用可能になった際には、このページでより詳細なタイムラインと更新情報が提供されます。

####  説明

これらの CVE
は、多くのプロセッサに搭載されている投機的実行テクノロジーを悪用する新しいクラスの攻撃のバリアントです。このクラスの攻撃を受けると、さまざまな状況下でメモリデータへの不正な読み取り専用アクセスが可能になるおそれがあります。

Compute Engine では、VM Live Migration
テクノロジーを使用してホストシステムとハイパーバイザを更新しました。これによるユーザーへの影響はなく、メンテナンスの時間枠を確保する必要も、大量の再起動も必要ありませんでした。ただし、この新しいクラスの攻撃からシステムを保護するには、その実行場所に関係なく、すべてのゲスト
オペレーティング システムとバージョンにパッチを適用する必要があります。

この攻撃の手法に関する詳しい技術情報については、 [ Project Zero のブログ記事
](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-
with-side.html) をご覧ください。Google が実施している対策の詳しい内容とすべてのサービス固有の情報は、 [ Google
のセキュリティ ブログの記事 ](https://security.googleblog.com/2018/01/todays-cpu-
vulnerability-what-you-need.html) にまとめられています。

####  Compute Engine への影響

Compute Engine を実行しお客様の VM インスタンスを相互に分離するインフラストラクチャは、既知の攻撃から保護されています。Google
は、VM インスタンス内で実行されているアプリケーションから Google
のホストシステムへの不正アクセスを防止する対策を講じました。この対策により、同じホストシステム上で実行されている VM
インスタンス間の不正アクセスも防止されます。

仮想マシン インスタンス内での不正アクセスを防止するには、次のいずれかの方法で VM インスタンスのゲスト オペレーティング
システムを更新する必要があります。

  * パッチ適用済みの公開イメージを使用して、 [ 既存の VM インスタンスを再作成する ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=ja#publicimage) 。パッチ適用済みの公開イメージは下のリストでご確認ください。 
  * 使用しているディストリビューションのパッチをオペレーティング システム ベンダーから入手して既存のインスタンスにインストールし、パッチ適用済みのインスタンスを再起動する。各オペレーティング システム ベンダーのパッチに関する情報は、下のリンクからご覧ください。 

####  パッチ適用済みイメージとベンダーのリソース

**注:** パッチ適用済みであっても、このセキュリティ情報に記載されているすべての CVE
の修正が含まれていない場合があります。また、この種の攻撃への防御策として、イメージごとに異なる手法が使用されている場合があります。パッチが対応している
CVE と使用されている防御策については、オペレーティング システムのベンダーに問い合わせて確認してください。

  * プロジェクト ` cos-cloud ` : バリアント 2（ [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ）とバリアント 3（ [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ）の攻撃を防止するパッチが含まれています。これらのイメージでは、バリアント 2 の攻撃対策として [ Retpoline ](https://support.google.com/faqs/answer/7625886?hl=ja) が使用されています。 
    * ` cos-stable-63-10032-71-0 ` またはイメージ ファミリー ` cos-stable `
  * プロジェクト ` centos-cloud ` : [ CentOS のパッチ情報 ](https://lwn.net/Alerts/CentOS/)
    * ` centos-7-v20180104 ` またはイメージ ファミリー ` centos-7 `
    * ` centos-6-v20180104 ` またはイメージ ファミリー ` centos-6 `
  * プロジェクト ` coreos-cloud ` : [ CoreOS のパッチ情報 ](https://coreos.com/blog/container-linux-meltdown-patch)
    * ` coreos-stable-1576-5-0-v20180105 ` またはイメージ ファミリー ` coreos-stable `
    * ` coreos-beta-1632-1-0-v20180105 ` またはイメージ ファミリー ` coreos-beta `
    * ` coreos-alpha-1649-0-0-v20180105 ` またはイメージ ファミリー ` coreos-alpha `
  * プロジェクト ` debian-cloud ` : [ Debian のパッチ情報 ](https://www.debian.org/security/#DSAS)
    * ` debian-9-stretch-v20180105 ` またはイメージ ファミリー ` debian-9 `
    * ` debian-8-jessie-v20180109 ` またはイメージ ファミリー ` debian-8 `
  * プロジェクト ` rhel-cloud ` : [ RHEL のパッチ情報 ](https://access.redhat.com/security/vulnerabilities/speculativeexecution)
    * ` rhel-7-v20180104 ` またはイメージ ファミリー ` rhel-7 `
    * ` rhel-6-v20180104 ` またはイメージ ファミリー ` rhel-6 `
  * プロジェクト ` suse-cloud ` : [ SUSE のパッチ情報 ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-v20180104 ` またはイメージ ファミリー ` sles-12 `
    * ` sles-11-sp4-v20180104 ` またはイメージ ファミリー ` sles-11 `
  * プロジェクト ` suse-sap-cloud ` : [ SUSE のパッチ情報 ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-sap-v20180104 ` またはイメージ ファミリー ` sles-12-sp3-sap `
    * ` sles-12-sp2-sap-v20180104 ` またはイメージ ファミリー ` sles-12-sp2-sap `
  * プロジェクト ` ubuntu-os-cloud ` : [ Ubuntu のパッチ情報 ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/)
    * ` ubuntu-1710-artful-v20180109 ` またはイメージ ファミリー ` ubuntu-1710 `
    * ` ubuntu-1604-xenial-v20180109 ` またはイメージ ファミリー ` ubuntu-1604-lts `
    * ` ubuntu-1404-trusty-v20180110 ` またはイメージ ファミリー ` ubuntu-1404-lts `
  * プロジェクト ` windows-cloud ` および ` windows-sql-cloud ` : 
    * バージョン番号 ` -v20180109 ` 以降のすべての Windows Server と SQL Server の [ 公開イメージ ](https://cloud.google.com/compute/docs/images?hl=ja#os-compute-support) にパッチが含まれています。ただし、Microsoft サポートページの [ Windows Server に関するガイダンス ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) に掲載されている「推奨される操作」を行い、既存のインスタンスと新たに作成したインスタンスの両方でこれらの対策を有効にして検証する必要があります。 

これらのイメージを使用して、 [ VM インスタンスを再作成してください。
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=ja#publicimage)
これらの公開イメージの旧バージョンにはこうしたパッチが含まれないため、攻撃される可能性を軽減できません。

####  ハードウェア ベンダーが提供するパッチ

NVIDIA は、NVIDIA® ドライバ
ソフトウェアがインストールされているシステムが攻撃される可能性を軽減するパッチを適用したドライバを提供しています。パッチ適用済みのドライバ
バージョンについては、NVIDIA が提供しているセキュリティ情報、 [ NVIDIA GPU ディスプレイ ドライバのセキュリティ更新
](http://nvidia.custhelp.com/app/answers/detail/a_id/4611) でご確認ください。

####  変更履歴:

  * 2018 年 5 月 21 日 T 14:00（太平洋標準時間）: 2018 年 5 月 21 日に開示された 2 つの新しいバリアントに関する情報を追加しました。 
  * 2018 年 1 月 10 日 T 15:00（太平洋標準時間）: Windows Server および SQL Server のパッチ適用済みの公開イメージに関する情報を追加しました。 
  * 2018 年 1 月 10 日 T 10:15（太平洋標準時間）: パッチ適用済みの公開イメージのリストに複数の Ubuntu イメージを追加しました。 
  * 2018 年 1 月 10 日 T 09:50（太平洋標準時間）: ハードウェア ベンダーが提供するパッチに関するガイダンスを追加しました。 
  * 2018 年 1 月 3 日〜2018 年 1 月 9 日: パッチ適用済みの公開イメージのリストに複数の変更を加えました。 

|  高  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  公開日: 2017 年 10 月 2 日

説明  |  重大度  |  注  
---|---|---  
  
####  説明

[ Dnsmasq ](http://www.thekelleys.org.uk/dnsmasq/doc.html) は DNS、DHCP、ルーター
アドバタイズメント、ネットワーク ブートの機能を提供します。通常、このソフトウェアはデスクトップ Linux ディストリビューション（Ubuntu
など）、家庭用ルーター、IoT 端末など、さまざまなシステムにインストールされます。Dnsmasq は、オープン インターネットとプライベート
ネットワークの両方で広く使われています。

Google は、定期的な社内セキュリティ評価の過程で 7
個の問題を発見しました。こうした問題の重大性を判断したうえで、その影響と悪用される可能性について調査し、それぞれについて Google
内部で概念実証を作成しました。また、Dnsmasq の管理者である Simon Kelly と協力して、適切なパッチを作成し、問題を緩和しました。

評価の際に、2017 年 9 月 5 日現在のプロジェクト git サーバーで、最新バージョンに影響を及ぼす 3 つの潜在的なリモートコード実行、1
つの情報漏洩、3 つのサービス拒否の脆弱性を発見しました。

これらのパッチはアップストリームされ、 [ プロジェクトの Git リポジトリ
](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) に commit されています。

####  Compute Engine への影響

デフォルトで、Dnsmasq は [ NetworkManager ](https://wikipedia.org/wiki/NetworkManager)
を使用するイメージのみにインストールされて非アクティブになっています。次の Compute Engine 公開イメージには、Dnsmasq
がインストールされています。

  * Ubuntu 16.04、16.10、17.04 
  * CentOS 7 
  * RHEL 7 

ただし、他のイメージでも、他のパッケージの依存関係として Dnsmasq
がインストールされていることがあります。Debian、Ubuntu、CentOS、RHEL、SLES、OpenSUSE
のインスタンスを、最新のオペレーティング システム イメージを使用するように更新することをおすすめします。CoreOS と Container-
Optimized OS は影響を受けません。Windows イメージにも影響はありません。

Debian と Ubuntu を実行するインスタンスの場合、インスタンスで次のコマンドを実行して、更新を行えます。

    
    
    
    sudo apt-get -y update
    
    
    
    sudo apt-get -y dist-upgrade

Red Hat Enterprise Linux と CentOS インスタンスの場合、次のコマンドを実行します。

    
    
    
    sudo yum -y upgrade

SLES と OpenSUSE イメージの場合、次のコマンドを実行します。

    
    
    
    sudo zypper up

手動の更新コマンドを実行する代わりに、それぞれのオペレーティング システムの [ イメージ ファミリーを使用して VM インスタンスを再作成
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=ja#publicimage) できます。

|  高  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  公開日: 2016 年 10 月 26 日

説明  |  重大度  |  注  
---|---|---  
  
####  説明

CVE-2016-5195 は、プライベートな読み取り専用メモリ マッピングにおける COW の破壊を Linux カーネルのメモリ
サブシステムが対処する過程で発生する競合状態です。

権限のないローカル ユーザーがこの不具合を悪用すると、本来は読み取り専用であるメモリ
マッピングへの書き込み権限を取得できるため、システム上で権限が昇格される可能性があります。

詳細は [ Dirty COW FAQ
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)
をご覧ください。

####  Compute Engine への影響

Compute Engine 上のすべての Linux
のディストリビューションとバージョンが影響を受けます。ほとんどのインスタンスは新しいカーネルを自動的にダウンロードしてインストールします。ただし、実行中のシステムにパッチを適用するには再起動する必要があります。

次の Compute Engine
イメージに基づく新しいインスタンスまたは再作成されたインスタンスには、パッチを適用したカーネルがすでにインストールされています。

  * ` centos-6-v20161026 `
  * ` centos-7-v20161025 `
  * ` coreos-alpha-1192-2-0-v20161021 `
  * ` coreos-beta-1185-2-0-v20161021 `
  * ` coreos-stable-1122-3-0-v20161021 `
  * ` debian-8-jessie-v20161020 `
  * ` rhel-6-v20161026 `
  * ` rhel-7-v20161024 `
  * ` sles-11-sp4-v20161021 `
  * ` sles-12-sp1-v20161021 `
  * ` ubuntu-1204-precise-v20161020 `
  * ` ubuntu-1404-trusty-v20161020 `
  * ` ubuntu-1604-xenial-v20161020 `
  * ` ubuntu-1610-yakkety-v20161020 `

|  高  |  [ CVE-2016-5195
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)  
  
##  公開日: 2016 年 2 月 16 日

**最終更新日: 2016 年 2 月 22 日**

説明  |  重大度  |  注  
---|---|---  
  
####  説明

CVE-2015-7547 は、 ` getaddrinfo() ` ライブラリ関数の使用時に glibc DNS
クライアント側のリゾルバによってスタックベースのバッファ
オーバーフローに対してソフトウェアが脆弱になるという脆弱性です。攻撃者は、この関数を使用してソフトウェアを利用し、攻撃者が制御するドメイン名、攻撃者が制御する
DNS サーバー、中間者攻撃によってこの脆弱性を悪用できます。

詳細については、 [ Google オンライン セキュリティ ブログ
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) または [ CVE（共通脆弱性識別子） ](http://www.cve.mitre.org/cgi-
bin/cvename.cgi?name=2015-7547) データベースをご覧ください。

####  Compute Engine への影響

**更新（2016 年 2 月 22 日）:**

次の CoreOS、SLES、OpenSUSE イメージを使用して、インスタンスを再作成できます。

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**更新（2016 年 2 月 17 日）:**

次のコマンドを実行して、Ubuntu 12.04 LTS、Ubuntu 14.04 LTS、Ubuntu 15.10
インスタンスに対する更新を実行できます。

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

手動更新コマンドを実行する代わりに、次の新しいイメージを使用してインスタンスを再作成することもできます。

  * ` backports-debian-7-wheezy-v20160216 `
  * ` centos-6-v20160216 `
  * ` centos-7-v20160216 `
  * ` debian-7-wheezy-v20160216 `
  * ` debian-8-jessie-v20160216 `
  * ` rhel-6-v20160216 `
  * ` rhel-7-v20160216 `
  * ` ubuntu-1204-precise-v20160217a `
  * ` ubuntu-1404-trusty-v20160217a `
  * ` ubuntu-1510-wily-v20160217 `

デフォルトの glibc 構成を使用した Compute Engine の DNS
リゾルバを介してこの脆弱性を悪用できる方法は確認されていません。ただし、他の新しい脆弱性のように、新たな悪用方法が今後発見される可能性もあるため、できる限り早く仮想マシン
インスタンスにパッチを適用する必要があります。edns0
を有効にしている場合は（デフォルトでは無効）、無効にしてからインスタンスにパッチを適用する必要があります。

**元の情報:**

お使いの Linux ディストリビューションは脆弱である可能性があります。Compute Engine ユーザーは、Linux OS
を実行している場合、インスタンスの OS イメージを更新して、この脆弱性を除去する必要があります。

Debian を実行するインスタンスの場合、インスタンスで次のコマンドを実行して更新できます。

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

また、Debian インスタンスに対して [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) をインストールすることもおすすめします。

Red Hat Enterprise Linux インスタンスの場合:

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

他のオペレーティング システム管理者によるこの脆弱性に対するパッチの公開、また Compute Engine での更新版 OS
イメージのリリースに伴い、この情報を引き続き更新します。

|  高  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  公開日: 2015 年 3 月 19 日

説明  |  重大度  |  注  
---|---|---  
  
####  説明

CVE-2015-1427 は、バージョン 1.3.8 よりも前のバージョンと 1.4.3 よりも前のすべての 1.4.x バージョンの [
Elasticsearch ](https://www.elastic.co/products/elasticsearch) の Groovy スクリプト
エンジンではリモートの攻撃者がサンドボックス保護メカニズムをバイパスして任意のシェルコマンドを実行できるという脆弱性です。

詳細については、 [ NVD（脆弱性データベース）
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) または [
CVE（共通脆弱性識別子） ](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-1427)
データベースをご覧ください。

####  Compute Engine への影響

Compute Engine インスタンスで Elasticsearch を実行している場合は、Elasticsearch のバージョンを 1.4.3
以上にアップグレードする必要があります。Elasticsearch ソフトウェアをすでにアップグレードしている場合は、この脆弱性から保護されています。

Elasticsearch 1.4.3 以上にアップグレードしていない場合は、 [ ローリング アップグレード
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) を実行できます。

[ Google Cloud Platform Console
](https://cloud.google.com/solutions/elasticsearch/click-to-deploy?hl=ja) で [
クリック デプロイ ](https://console.cloud.google.com/?hl=ja) を使用して Elasticsearch
をデプロイした場合、 [ デプロイを削除
](https://console.cloud.google.com/projectselector/deployments?hl=ja)
し、Elasticsearch を実行しているインスタンスを削除できます。

Google Cloud Platform チームは、Elasticsearch の更新バージョンをデプロイするために、修正に取り組んでいます。ただし、 [
GCP Console ](https://console.cloud.google.com/?hl=ja) のクリック
デプロイ機能用の修正プログラムはまだ提供されていません。

|  高  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  公開日: 2015 年 1 月 29 日

説明  |  重大度  |  注  
---|---|---  
  
####  説明

[ CVE-2015-0235（Ghost）
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) は glibc
ライブラリの脆弱性です。

App Engine、Cloud Storage、BigQuery、CloudSQL のユーザーは措置を講じる必要はありません。Google
のサーバーは更新されており、この脆弱性から保護されています。

Compute Engine のユーザーは OS イメージの更新が必要な場合があります。

####  Compute Engine への影響

お使いの Linux ディストリビューションは脆弱である可能性があります。Compute Engine ユーザーは、Debian 7、Debian 7
バックポート、Ubuntu 12.04 LTS、Red Hat Enterprise Linux、CentOS、SUSE Linux Enterprise
Server 11 SP3 を実行している場合、インスタンスの OS イメージを更新して、この脆弱性を除去する必要があります。

この脆弱性は、Ubuntu 14.04 LTS、Ubuntu 14.10、SUSE Linux Enterprise Server 12
には影響を及ぼしません。

Linux ディストリビューションをアップグレードすることをおすすめします。Debian 7、Debian 7 バックポート、Ubuntu 12.04
LTS を実行しているインスタンスの場合、インスタンスで次のコマンドを実行して更新できます。

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Red Hat Enterprise Linux または CentOS インスタンスの場合:

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

SUSE Linux Enterprise Server 11 SP3 インスタンスの場合:

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

上のコマンドを実行して更新を行う代わりに、次の新しいイメージを使用してインスタンスを再作成することもできます。

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  Google マネージド VM への影響

` gcloud preview app deploy ` を使用しているマネージド VM ユーザーは、 ` gcloud preview app
setup-managed-vms ` でベース Docker コンテナを更新し、 ` gcloud preview app deploy `
を使用して実行中の各アプリを再デプロイする必要があります。 ` appcfg `
でデプロイしているユーザーは何もする必要はなく、自動的にアップグレードされます。

|  高  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  公開日: 2014 年 10 月 15 日

**最終更新日: 2014 年 10 月 17 日**

説明  |  重大度  |  注  
---|---|---  
  
####  説明

CVE-2014-3566（別名 POODLE）は、SSL バージョン 3.0
の設計上の脆弱性です。この脆弱性により、ネットワーク攻撃者はセキュアな接続のプレーンテキストを計算できます。詳細については、この脆弱性に関する [
ブログ投稿 ](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) をご覧ください。

App Engine、Cloud Storage、BigQuery、CloudSQL のユーザーは措置を講じる必要はありません。Google
のサーバーは更新されており、この脆弱性から保護されています。Compute Engine のユーザーは OS イメージを更新する必要があります。

####  Compute Engine への影響

**更新（2014 年 10 月 17 日）:**

SSLv3 を使用している場合、脆弱である可能性があります。Compute Engine ユーザーは、インスタンスの OS
イメージを更新して、この脆弱性を除去する必要があります。

Linux ディストリビューションをアップグレードすることをおすすめします。Debian
を実行するインスタンスの場合、インスタンスで次のコマンドを実行して更新できます。

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

CentOS インスタンスの場合:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

上のコマンドを実行して更新を行う代わりに、次の新しいイメージを使用してインスタンスを再作成することもできます。

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

RHEL と SLES イメージについては、イメージを用意でき次第、情報を更新します。その間、RHEL ユーザーは、詳細については [ Red Hat
に直接 ](https://access.redhat.com/articles/1232123) お問い合わせください。

**元の情報:**

Compute Engine ユーザーは、インスタンスの OS イメージを更新して、この脆弱性を除去する必要があります。新しい OS
イメージを用意でき次第、手順を含むこのセキュリティ情報を更新します。

|  中  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  公開日: 2014 年 9 月 24 日

**最終更新日: 2014 年 9 月 29 日**

説明  |  重大度  |  注  
---|---|---  
  
####  説明

攻撃者が制御する環境変数の解析に基づくリモートコード実行が可能となる bash
のバグ（CVE-2014-6271）があります。悪用の手口として最も考えられるのは、ウェブサーバーで公開されている CGI
スクリプトに対して行われる悪意のある HTTP リクエストを介する方法です。詳細については、 [ バグに関する説明
](http://seclists.org/oss-sec/2014/q3/650) をご覧ください。

この bash のバグは、20140926 よりも前の日付の Compute Engine ゲスト OS イメージを除く、Google Cloud
Platform プロダクトに対しては緩和されています。お使いの Compute Engine
イメージのバグを緩和するための手順については、以下をご覧ください。

####  Compute Engine への影響

このバグは、CGI
スクリプトを使用する実質的にすべてのウェブサイトに影響を及ぼす可能性があります。また、PHP、Perl、Python、SSI、Java、C++
に依存するウェブサイトに加え、 ` popen ` 、 ` system ` 、 ` shell_exec ` 、同様の API
など、呼び出しを介してシェルコマンドを実行する同様のサーブレットに依存するウェブサイトに影響を及ぼすと考えられます。さらに、SSH コマンド制限や bash
制限付きシェルなどのメカニズムによって、制限されたユーザーに対して制御されたログイン アクセスを許可するシステムに影響を及ぼす可能性もあります。

**更新（2014 年 9 月 29 日）:**

下記の手動更新コマンドを実行する代わりに、bash のセキュリティ上のバグに関連する追加の脆弱性（ [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) 、 [
CVE-2014-6277 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277)
、 [ CVE-2014-6278
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278) 、 [
CVE-2014-7186 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186)
、 [ CVE-2014-7187
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)
）を緩和するイメージを使用して、インスタンスを再作成することもできます。次の新しいイメージを使用して、インスタンスを再作成してください。

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**更新（2014 年 9 月 25 日）:**

ユーザーは、手動更新を実行する代わりに、インスタンスを再作成することを選択できます。インスタンスを再作成するには、このセキュリティ
バグに対する修正を含む次の新しいイメージを使用します。

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

RHEL と SUSE イメージについては、インスタンスで次のコマンドを実行して、更新を手動で行うこともできます。

    
    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**元の情報:**

Linux ディストリビューションをアップグレードすることをおすすめします。Debian
を実行するインスタンスの場合、インスタンスで次のコマンドを実行して更新できます。

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

CentOS インスタンスの場合:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade

詳細については、各 Linux ディストリビューションに関する告知を確認してください。

  * 元のパッチ: [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) （適切なバージョンについては、*-patches の最後のエントリを参照してください） 
  * Debian: [ [SECURITY] [DSA 3032-1] bash セキュリティ更新プログラム ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
  * RHEL: 
    * [ RHSA-2014:1293-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00048.html)
    * [ RHSA-2014:1294-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00049.html)
  * CentOS 5: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020582.html)
  * CentOS 6: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020585.html)
  * CentOS 7: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020583.html)

|  高  |  [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) 、 [
CVE-2014-6271 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271)
、 [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) 、 [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
、 [ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) 、 [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  公開日: 2014 年 7 月 25 日

説明  |  重大度  |  注  
---|---|---  
  
####  説明

[ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/)
は、不正な変更やデータの開示を可能にする可能性がある OS コマンド インジェクションの脆弱性です。攻撃者は、細工したイベントを Logstash
のデータソースに送信して、Logstash プロセスの権限でコマンドを実行できます。

####  Compute Engine への影響

この脆弱性は、zabbix または nagios_nsca の出力が有効になった 1.4.2 よりも前の Elasticsearch Logstash
のバージョンを実行しているすべての Compute Engine インスタンスに影響を及ぼします。攻撃を防ぐために、次のいずれかを実行できます。

  * Logstash 1.4.2 にアップグレードする 
  * バージョン 1.3.x のパッチを適用する 
  * ` zabbix ` と ` nagios_nsca ` の出力を無効にする 

詳細については、 [ Logstash ブログ ](http://www.elasticsearch.org/blog/logstash-1-4-2/)
をご覧ください。

Elasticsearch では、 [ ファイアウォールを使用 ](http://www.elasticsearch.org/blog/scripting-
security/) して信頼できない IP によるリモート アクセスを防ぐことも推奨しています。

|  高  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  公開日: 2014 年 6 月 18 日

説明  |  重大度  |  注  
---|---|---  
  
####  説明

Google Cloud Platform 上での実行時における Docker
コンテナのセキュリティに関するユーザーのあらゆる懸念に対応できるよう、現在取り組み中です。これには、Docker
コンテナ、コンテナに最適化された仮想マシン、オープンソースの Kubernetes スケジューラをサポートする Google App Engine
の拡張機能を使用するユーザーが含まれます。

Docker はこの問題に適切に対応しており、それに関するブログ記事を [ ここ
](http://blog.docker.com/2014/06/docker-container-breakout-proof-of-concept-
exploit/) で確認できます。記事で説明されているように、明らかになった問題は本番環境版前の古いバージョンである Docker 0.11
にのみ該当することに注意してください。

コンテナのセキュリティについて世界中で検討されていますが、Google Cloud Platform 上では、Linux アプリケーション
コンテナベースのソリューション（特に Docker コンテナ）は完全な仮想マシン（Compute
Engine）で実行されることにご注意ください。Google では、Linux アプリケーション コンテナ スタックを強化する Docker
コミュニティの努力を支持していますが、このテクノロジーは新しく、境界面が大きいことを認識しています。現時点では、完全なハイパーバイザ（仮想マシン）はよりコンパクトで防御しやすい境界面を提供すると
Google は考えています。仮想マシンは、もともと、悪意のあるワークロードを分離し、コードバグの可能性と影響を最小限に抑えるように設計されています。

Google のお客様は、第三者、そして潜在的に悪意のあるコードとの間に完全なハイパーバイザ境界が存在することを確実に確保できます。Linux
アプリケーション コンテナ スタックが十分に堅牢でマルチテナント ワークロードをサポートできると考えられる段階になった場合には、Google
はコミュニティに報告します。現時点では、Linux アプリケーション コンテナは仮想マシンに代わるものではありません。あくまでも機能を拡張する方法です。

|  低  |  [ Docker ブログの投稿 ](http://blog.docker.com/2014/06/docker-container-
breakout-proof-of-concept-exploit/)  
  
##  公開日: 2014 年 6 月 5 日

**最終更新日: 2014 年 6 月 9 日**

説明  |  重大度  |  注  
---|---|---  
  
####  説明

OpenSSL には、 ` ChangeCipherSpec ` メッセージが handshake
ステートマシンに正しくバインドされないという問題があります。これにより、handshake への早期の注入が可能となります。攻撃者は、巧妙に細工した
handshake を使用して、OpenSSL SSL/TLS クライアントとサーバーで弱いキーイング
マテリアルの使用を強制できます。これは中間者（MITM）攻撃によって悪用される可能性があり、攻撃者は攻撃対象のクライアントとサーバーからのトラフィックを復号して変更できます。

この問題は [ CVE-2014-0224 ](https://www.openssl.org/news/secadv/20140605.txt)
として識別されています。OpenSSL チームは、この問題を修正済みであり、OpenSSL を更新するよう OpenSSL
コミュニティに注意を喚起しています。

####  Compute Engine への影響

この脆弱性は、Debian、CentOS、Red Hat Enterprise Linux、SUSE Linux Enterprise Server
など、OpenSSL を使用するすべての Compute Engine
インスタンスに影響を及ぼします。新しいイメージでインスタンスを再作成するか、インスタンスのパッケージを手動で更新することで、インスタンスを更新できます。

**更新（2014 年 6 月 9 日）** : 新しいイメージで SUSE Linux Enterprise Server
を実行しているインスタンスを更新するには、次のバージョン以上のイメージを使用して、インスタンスを再作成します。

  * ` sles-11-sp3-v20140609 `

**元の投稿:**

新しいイメージを使用して Debian インスタンスと CentOS
インスタンスを更新するには、次のバージョン以上のいずれかのイメージを使用してインスタンスを再作成します。

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

インスタンス上の OpenSSL を手動で更新するには、次のコマンドを実行して適切なパッケージを更新します。CentOS と RHEL
を実行するインスタンスの場合、インスタンスでこれらのコマンドを実行して、OpenSSL を更新できます。

    
    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

Debian を実行するインスタンスの場合、インスタンスで次のコマンドを実行して、OpenSSL を更新できます。

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

SUSE Linux Enterprise Server を実行するインスタンスの場合、インスタンスでこれらのコマンドを実行して、OpenSSL
を最新の状態できます。

    
    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  中  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  公開日: 2014 年 4 月 8 日

説明  |  重大度  |  注  
---|---|---  
  
####  説明

1.0.1g よりも前の OpenSSL 1.0.1 での（1）TLS と（2）DTLS の実装では、Heartbeat Extension
パケットが適切に処理されません。これは Heartbleed バグとも呼ばれる脆弱性で、 ` d1_both.c ` と ` t1_lib.c `
に関連する秘密鍵を読み取ることで実証されているように、バッファ
オーバーリードを誘発する細工したパケットを介してリモートの攻撃者がプロセスメモリから機密情報を入手できます。

####  Compute Engine への影響

この脆弱性は、OpenSSL の最新バージョンを使用していないすべての Compute Engine Debian、RHEL、CentOS
インスタンスに影響を及ぼします。新しいイメージでインスタンスを再作成するか、インスタンスのパッケージを手動で更新することで、インスタンスを更新できます。

新しいイメージを使用してインスタンスを更新するには、次のバージョン以上のいずれかのイメージを使用してインスタンスを再作成します。

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

インスタンス上の OpenSSL を手動で更新するには、次のコマンドを実行して適切なパッケージを更新します。CentOS と RHEL
を実行するインスタンスの場合、インスタンスでこれらのコマンドを実行して、OpenSSL を最新の状態にできます。

    
    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

Debian を実行するインスタンスの場合、インスタンスで次のコマンドを実行して、OpenSSL を更新できます。

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

SUSE Linux を実行しているインスタンスは影響を受けません。

**2014 年 4 月 14 日更新** : Heartbleed バグを利用した鍵の抽出に関する新たな調査に基づいて、Compute Engine
では、影響を受けるすべての SSL サービスについて新しい鍵を作成するよう Compute Engine ユーザーに推奨しています。

|  中  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  公開日: 2013 年 6 月 7 日

説明  |  重大度  |  注  
---|---|---  
  
####  説明

**注:** この脆弱性が該当するのは、API バージョン v1 以降では非推奨となり削除されているカーネルのみです。

3.9.4 までの Linux カーネルの Broadcom B43 ワイヤレス ドライバの `
drivers/net/wireless/b43/main.c ` の ` b43_request_firmware `
関数にある書式文字列の脆弱性により、ルートアクセス権を利用し、書式文字列指定子を ` fwpostfix ` modprobe パラメータに含めてエラー
メッセージの不適切な作成を発生させることで、ローカル ユーザーが権限を取得できます。

####  Compute Engine への影響

この脆弱性は、 ` gcg-3.3.8-201305291443 ` よりも前のすべての Compute Engine
カーネルに影響を及ぼします。対応として、Compute Engine ではすべての以前のカーネルを非推奨とし、インスタンスとイメージを更新して
Compute Engine カーネル ` gce-v20130603 ` を使用するようユーザーに推奨しています。カーネル ` gce-v20130603
` には、この脆弱性に対するパッチを備えるカーネル ` gcg-3.3.8-201305291443 ` が含まれています。

自分のインスタンスが使用しているカーネルのバージョンを確認するには:

  1. インスタンスに SSH 接続します。 
  2. ` uname -r ` を実行します。 

|  中  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  公開日: 2013 年 6 月 7 日

説明  |  重大度  |  注  
---|---|---  
  
####  説明

**注:** この脆弱性が該当するのは、API バージョン v1 以降では非推奨となり削除されているカーネルのみです。

3.9.4 までの Linux カーネルの ` block/genhd.c ` の register_disk
関数にある書式文字列の脆弱性により、ルートアクセス権を利用し、書式文字列指定子を `
/sys/module/md_mod/parameters/new_array ` に書き込んで細工された ` /dev/md `
デバイス名を作成することで、ローカル ユーザーが権限を取得できます。

####  Compute Engine への影響

この脆弱性は、 ` gcg-3.3.8-201305291443 ` よりも前のすべての Compute Engine
カーネルに影響を及ぼします。対応として、Compute Engine ではすべての以前のカーネルを非推奨とし、インスタンスとイメージを更新して
Compute Engine カーネル ` gce-v20130603 ` を使用するようユーザーに推奨しています。カーネル ` gce-v20130603
` には、この脆弱性に対するパッチを備えるカーネル ` gcg-3.3.8-201305291443 ` が含まれています。

自分のインスタンスが使用しているカーネルのバージョンを確認するには:

  1. インスタンスに SSH 接続します。 
  2. ` uname -r ` を実行します。 

|  中  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  公開日: 2013 年 5 月 14 日

説明  |  重大度  |  注  
---|---|---  
  
####  説明

**注:** この脆弱性が該当するのは、API バージョン v1 以降では非推奨となり削除されているカーネルのみです。

3.8.9 よりも前の Linux カーネルの ` kernel/events/core.c ` の perf_swevent_init 関数では、不適切な
` integer ` データ型を使用しており、細工した ` perf_event_open ` システム呼び出しを介してローカル
ユーザーが権限を取得できます。

####  Compute Engine への影響

この脆弱性は、 ` gcg-3.3.8-201305211623 ` よりも前のすべての Compute Engine
カーネルに影響を及ぼします。対応として、Compute Engine ではすべての以前のカーネルを非推奨とし、インスタンスとイメージを更新して
Compute Engine カーネル ` gce-v20130521 ` を使用するようユーザーに推奨しています。カーネル ` gce-v20130521
` には、この脆弱性に対するパッチを備えるカーネル ` gcg-3.3.8-201305211623 ` が含まれています。

自分のインスタンスが使用しているカーネルのバージョンを確認するには:

  1. インスタンスに SSH 接続します。 
  2. ` uname -r ` を実行します。 

|  高  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  公開日: 2013 年 2 月 18 日

説明  |  重大度  |  注  
---|---|---  
  
####  説明

**注:** この脆弱性が該当するのは、API バージョン v1 以降では非推奨となり削除されているカーネルのみです。

3.7.5 よりも前の Linux カーネルの ptrace 機能の競合状態により、細工したアプリケーションでの ` PTRACE_SETREGS
ptrace ` システム呼び出しを介してローカル ユーザーが権限を取得できます。

####  Compute Engine への影響

この脆弱性は、Compute Engine カーネル ` 2.6.x-gcg- _ <date> _ ` に影響を及ぼします。対応として、Compute
Engine では 2.6.x カーネルを非推奨とし、インスタンスとイメージを更新して Compute Engine カーネル `
gce-v20130225 ` を使用するようユーザーに推奨しています。カーネル ` gce-v20130225 `
には、この脆弱性に対するパッチを備えるカーネル ` 3.3.8-gcg-201302081521 ` が含まれています。

自分のインスタンスが使用しているカーネルのバージョンを確認するには:

  1. インスタンスに SSH 接続します。 
  2. ` uname -r ` を実行します。 

|  中  |  [ CVE-2013-0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

