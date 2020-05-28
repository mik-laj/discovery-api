#  リリースノート

このページには、Cloud Code
の本番環境に関する更新情報が記載されています。このページをチェックして、新機能や更新された特徴、バグ修正、既知の問題、非推奨となった機能に関するお知らせを確認してください。

最新のアップデートは [ GitHub リリースノートのページ
](https://github.com/GoogleCloudPlatform/cloud-code-
intellij/blob/master/CHANGELOG.md) でもご覧いただけます。

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ` https://cloud.google.com/feeds/cloud-code-for-intellij-release-notes.xml
` を直接追加します。

##  2018 年 5 月 1 日

Cloud Code が PyCharm（コミュニティとプロフェッショナル）で利用できるようになりました。PyCharm から Cloud Storage
バケットの参照と Cloud Source Repositories の操作ができます。その他の IDE にも近日中に対応する予定です。

###  追加

  * プラグインがリファクタリングされて、言語に依存しない機能（Cloud Storage、Cloud Source Repositories）を IDEA 以外の JetBrains IDE でも利用できるようになりました。 [ 1896 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1896)

###  変更

  * 最初に手動でキャンセルすると、IDE を読み込むたびにマネージド Cloud SDK がインストールされることはなくなります。 [ 2113 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2113)

###  修正

  * 2018.2 EAP で例外を修正しました。 [ 2124 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2124)

##  2018 年 4 月 1 日

###  追加

  * Google Cloud Tools プラグインで Cloud SDK を自動的に管理できるようになりました（ダウンロード、インストール、アップデートなど）。SDK を手動でダウンロードする必要がなくなりました。 [ 673 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/673)
  * 組み込みの Google Cloud Java BOM サポートとの依存関係バージョンの競合が緩和されました。Google クライアント ライブラリの追加時に BOM を自動的に追加する機能に加えて、依存関係バージョンの競合を管理するための pom.xml 検査機能が導入されました。 [ 1921 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1921)
  * Google Cloud API にローカルでアクセスできるように、必要な環境変数が App Engine のローカルの実行構成に自動的に追加されるようになりました。 [ 1917 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1917)

##  2018 年 3 月 2 日

  * 2017.2 以前の IntelliJ IDEA バージョンでプラグインの初期化エラーが発生するバグを修正しました。 [ 1972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1972)

##  2018 年 3 月 1 日

###  追加

  * IDE クライアント ライブラリ ワークフローからサービス アカウントを作成してサービス アカウントキーをダウンロードする機能を追加しました。 [ 1808 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1808)

###  修正

  * ` web.xml ` がないために ` appengine-web.xml ` が生成されなかった問題を修正しました。 [ 1903 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1903)

##  2018 年 2 月 1 日

###  追加

  * IDE からの Google Cloud Java クライアント ライブラリの検出と追加機能を追加しました。 [ 1806 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1806)
  * IDE から Google Cloud API を有効にする機能を追加しました。 [ 1807 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1807)

###  変更

  * クラウド プロジェクト セレクタの機能が大幅に改善され、ユーザー エクスペリエンスが向上しました。 [ 1719 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1719)
  * クラウド プロジェクト セレクタで、最後の選択項目がデフォルトとして記憶されるようになりました。 [ 1812 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1812)

###  修正

  * App Engine スタンダード環境のローカル実行アーティファクトが見つからないという問題を修正しました。 [ 1625 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1625)

##  2018 年 1 月 1 日

###  修正

  * エラー報告メカニズムの破損を修正しました。 [ 1842 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1842)

##  2017 年 12 月 2 日

###  修正

  * 分析の欠落が生じる原因となっていた分析プロパティの設定の破損を修正しました。 [ 1773 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1773)

##  2017 年 12 月 1 日

Google アカウント プラグインが Cloud Tools プラグインに統合され、別のインストールではなくなりました。これまで Account
Tools プラグインをインストールしていた場合は、新しいダイアログ プロンプトに従って削除して、IDE
を再起動し、問題が発生しないことを確認してください。

###  修正

  * クラウド プロジェクト セレクタで複数のプロジェクトを入力して検索すると発生するメモリ不足エラーを修正しました。 [ 1742 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1742)

###  変更

  * Google アカウント プラグインが Google Cloud Tools プラグインに統合されました。Google アカウント プラグインを別にインストールする必要がなくなりました。 [ 1735 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1735)

##  2017 年 11 月 1 日

###  追加

  * Google Cloud Storage と IntelliJ の統合。IDE を終了せずにバケットを参照し、コンテンツを表示できるようになりました。 [ 1696 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1696)
  * クラウド プロジェクト セレクタの検索機能とフィルタリング機能。 [ 1660 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1660)
  * 新しい [add App Engine framework support] ツールメニューのショートカットにより、プロジェクトに App Engine サポートを追加する別の方法を提供します。 [ 1685 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1685)

###  修正

  * クラウド プロジェクトが選択されていないときの App Engine リージョン インジケーターのステータス メッセージを修正しました。 [ 1607 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1607)

##  2017 年 9 月 2 日

App Engine スタンダード環境で Java 8 が [ 一般的に利用可能
](https://cloudplatform.googleblog.com/2017/09/Java-8-on-App-Engine-Standard-
environment-is-now-generally-available.html) になりました。

###  変更

  * 新しい App Engine スタンダード プロジェクト ウィザードがデフォルトで Java 8 アプリケーションを生成するように更新されました。 [ 1641 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1641)

##  2017 年 9 月 1 日

###  追加

  * App Engine フレキシブル環境のデプロイでステージングされたアーティファクトの名前を変更する機能を追加しました。 [ 1610 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1610)

###  変更

  * App Engine フレキシブル デプロイ構成では、 ` target.jar ` または ` target.war ` に名前を変更せずに、アーティファクトがデフォルトでデプロイされるようになりました。 [ 1151 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1151)
  * 生成された Dockerfile テンプレートのプレースホルダ アーティファクトの名前を更新し、ユーザーが更新する必要があることを明確にしました。 [ 1648 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1648)
  * App Engine スタンダードのデプロイ構成は、デフォルトで、dos、dispatch、cron、queues、datastore のインデックスを更新するようになりました。 [ 1613 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1613)
  * App Engine 用 Endpoints Frameworks のサポートを追加するネイティブ プロジェクトで、Endpoints V2 が使用されるようになりました。 [ 1612 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1612)

###  修正

  * Maven アーティファクトをデプロイする際の ` Deployment source not found ` エラーを修正しました。 [ 1220 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1220)
  * HiDPI ディスプレイ上のユーザー アイコンのスケールを修正しました。 [ 1633 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1633)
  * IDEA 2017.3 EAP でプラグインがダウングレードされた問題を修正しました。 [ 1631 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1631)

##  2017 年 8 月 2 日

###  修正

  * Google アカウントでログインしたときの「エラー: invalid_scope」の問題を修正しました。 [ 1598 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1598)

##  2017 年 8 月 1 日

###  追加

  * Google Cloud Tools のショートカット メニューにフィードバックと問題報告のリンクを追加しました。 [ 1560 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1560)

###  変更

  * ユーザーは、部分的に完了した、またはエラー状態のデプロイ実行構成を保存できるようになりました。 [ 1407 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1407)

###  修正

  * .ignore プラグインとともにプラグインが実行される問題の原因となる登録済みの Docker 言語の競合が修正されました。 [ 1535 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1535)
  * Cloud Debugger のブレークポイントのタイムスタンプを解析する NPE を修正しました。 [ 1537 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1537)
  * ローカル開発用サーバーの実行に許容可能な App Engine アーティファクト タイプとしての EAR を削除しました。 [ 1190 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1190)
  * 複数の IDE ウィンドウにデプロイが表示されるようになりました。 [ 1432 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1432)
  * 読み取り専用コレクションを変更しようとするとクラッシュする問題を修正しました。 [ 1571 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1571)

##  2017 年 6 月 2 日

###  修正

  * ローカル開発用サーバーの構成があり、スタンダード ファセットがない場合に発生する NPE を修正しました。 [ 1525 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1525)

##  2017 年 6 月 1 日

###  追加

  * ` app.yaml ` と Dockerfile 構成を含む App Engine フレキシブル ファセット。 [ 1514 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1514)
  * App Engine フレキシブル フレームワーク サポートの検出。 [ 1277 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1277)

###  変更

  * ユーザーは、フレキシブル環境のデプロイで Docker ファイルだけでなく Docker ディレクトリを指定できるようになりました。 [ 1304 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1304)
  * デプロイ ダイアログのユーザー エクスペリエンスをスタンダードとフレキシブルの両方で更新しました。 [ 1477 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1477)

###  修正

  * HiDPI ディスプレイの Google アバターのサイズを修正しました。 [ 1391 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1391)

##  2017 年 2 月 5 日

###  追加

  * App Engine スタンダード ローカル実行構成の環境変数は、開発用サーバーに渡されるようになりました。 [ #1364 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1364)
  * appengine-web.xml で構成された環境変数が使用され、開発用サーバーに渡されるようになりました。 [ #377 ](https://github.com/GoogleCloudPlatform/appengine-plugins-core/issues/377)

##  2017 年 2 月 4 日

###  追加

  * サービスのデプロイ中にすべての App Engine 構成ファイルをデプロイするためのチェックボックスを追加しました。 [ #1346 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1346)

##  2017 年 2 月 3 日

###  変更

  * 現在のバージョンのサーバーではサポートされていないため、App Engine スタンダード ローカル開発用サーバー構成からデータストアのクリアフラグを削除しました。（ [ #1345 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1345) ） 

##  2017 年 2 月 2 日

###  修正

  * App Engine スタンダード アプリをステージングする際の無効な Java Runtime Environment（JRE）（ [ #1316 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1316) ）: 
    
        > Unable to stage app: Cannot get the System Java Compiler. Please use a JDK, not a JRE.
    

##  2017 年 2 月 1 日

Cloud Code のユーザーの皆様、謹んで新年のご挨拶を申し上げます。今年の最初のリリースは主にメンテナンス リリースです。Cloud Source
Repositories とプラグインの使用中に認証の問題が発生する場合は、 [ この可能な解決策
](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1174)
をご確認ください。

認識できる変更のリストは次のとおりです。

###  追加

  * 1 つの GCP プロジェクトに対する複数の Cloud Source Repositories のサポート。 （ [ #1024 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1024) ） 
  * App Engine の初期化とリージョン選択。 （ [ #1232 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1232) ） 

###  修正

  * Windows 上の dev_appserver の停止が毎回 ` com.intellij.execution.ExecutionException ` で失敗します。( [ #1215 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1215) ) 
  * 新しい App Engine スタンダード プロジェクト ウィザードは、サーブレット 2.5 を使用して web.xml を生成します。（ [ #1194 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1194) ） 
  * App Engine スタンダード ローカル サーバーのデータストアのクリア チェックボックスは機能しません。（ [ #1188 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1188) ） 
  * 削除予定のプロジェクトをプロジェクト セレクタで表示しません。（ [ #1119 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1119) ） 

詳細は、 [ 17.2 リリース マイルストーン ](https://github.com/GoogleCloudPlatform/google-
cloud-intellij/milestone/19?closed=1) をご覧ください。

##  2016 年 11 月 6 日

###  追加

  * さまざまなアクションのショートカットを含む Google Cloud Tools のメニュー項目を拡張しました。（ [ #1061 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1061) ） 
  * Cloud SDK の最小サポート バージョンのチェック。（ [ #1051 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1051) ） 
  * App Engine スタンダード アプリのすべての関連する実行構成を自動的に作成します。（ [ #1063 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1063) ） 
  * App Engine フレームワークは、新しいプロジェクト ウィザードのウェブ フレームワークの子になりました。（ [ #1065 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1065) ） 

###  修正

  * アプリケーション サーバーのデプロイパネル固有のデプロイソースは、個別の項目として表示されるようになりました。（ [ #821 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/821) ） 
  * Windows 上の無効な Cloud SDK パスの検証。 （ [ #1091 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1091) ） 

##  2016 年 10 月 5 日

重要: このプラグインでは、最新の Java 8 SDK を使用してローカル開発用サーバーを正しく実行するために Cloud SDK v133.0.0
を使用する必要があります。シェルから ` gcloud components update ` を実行して、最新の Cloud SDK
リリースがインストールされていることを確認してください。

###  修正

  * サーバーの実行中に変更が加えられた場合のローカル開発用サーバーのデバッグモードの問題を修正しました。（ [ #972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/972) ） 
  * 開発用サーバーの Cloud SDK パスが無効な場合の表現方法を改善しました。（ [ #1043 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1043) ） 
  * 先頭に「Google ..」が付加されるように実行構成名を更新しました。（ [ #1021 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1021) ） 

##  2016 年 10 月 1 日

  * バージョニング スキームが YY.MM.i に変更されます。Google では、アップデートの中断を最小限に抑えるため、月次でのリリースを予定しています。また、「ベータ」ラベルが削除されました。 
  * 注意: ローカルの App Engine 開発用サーバーは最新の JDK 8 リリースで動作しません。( [ #920 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/920) ). これは、近日提供予定の次の App Engine SDK リリースで修正されます。 

###  追加

  * ファセットとプロジェクト ウィザードの App Engine スタンダード ライブラリ インポーター。 ( [ #866 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/866) ) 
  * Java 8 言語レベルを使用する App Engine スタンダード アプリには、言語レベル 7 を使用するように通知されます。（ [ #966 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/966) ） 

###  変更

  * 実行構成ラベルとアイコンが更新されました。（Cloud Debugger は Cloud デバッガになりました）（ [ #936 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/936) ） 

###  修正

  * ローカル開発用サーバーのデバッグモードが修正されました。 ( [ #928 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/928) ) 
  * フレキシブル デプロイが Windows 10 で失敗します。 ( [ #937 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/937) ) 
  * Cloud Debugger オブジェクトのインスペクタが再び動作するようになりました。 ( [ #929 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/929) ) 
  * Cloud Debugger スナップショットのタイムスタンプにより NPE が発生します。（ [ #919 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/919) ） 

##  1.0- ベータ版 - 2016 年 9 月 14 日

###  追加

  * App Engine スタンダード環境のサポート（ [ #767 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/767) ） 
  * デプロイ構成で追加のフィールドが利用できるようになりました。（ [ #868 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/868) ） 

##  0.9.7.5-Bata - 2016 年 8 月 29 日

###  追加

  * 認定されたユーザーに対してデプロイが有効であることを確認し、そうでない場合は新しいユーザーを追加するように求めるプロンプトを表示します。 ( [ 837 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/837) ) 

##  0.9.6- ベータ版 - 2016 年 6 月 23 日

###  追加

  * App Engine フレキシブル __ 互換環境へのデプロイのサポート。 ( [ #720 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/720) ) 
  * App Engine スタンダード環境へのデプロイのサポート。 ( [ #665 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/665) ) 
  * クラウドツールとアカウント プラグインの互換性の確認。 ( [ #651 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/650) ) 

###  変更

  * バージョン入力をデプロイ構成ダイアログ内の最上位レベルの構成に移動しました。 ( [ #639 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/639) ) 

##  0.9.4- ベータ版 - 2016 年 4 月 20 日

###  追加

  * App Engine フレキシブル環境へのデプロイのツールメニュー項目。 （ [ #635 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/635) ） 
  * App Engine フレキシブル環境デプロイのデプロイソースとしての Maven ベース プロジェクトのサポート。（ [ #600 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/600) ） 

###  変更

  * App Engine フレキシブル環境デプロイを、App Engine アプリケーション サーバーへの接続を解除することでキャンセルできます。（ [ #581 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/581) ） 
  * App Engine フレキシブル環境で生成される Dockerfile と ` app.yaml ` が、Maven 構造化 Java プロジェクトの推奨ロケーションにデフォルト設定されるようになりました。 ( [ #575 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/575) ) 

###  修正

  * ユーザーを追加するときにアクティブなユーザーが選択されなくなる可能性のあるログインバグ。（ [ #644 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/644) ） 
  * App Engine デプロイをデプロイ解除するとエラーが発生する可能性があります。 （ [ #599 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/599) ） 

