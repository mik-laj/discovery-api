#  Python 3 リリースノート

Python [ 2.7
](https://cloud.google.com/appengine/docs/standard/python/release-notes?hl=ja
"Python 2.7 ランタイムに関するこのページを見る") /  3.7  |  Java [ 8
](https://cloud.google.com/appengine/docs/standard/java/release-notes?hl=ja
"Java 8 ランタイムに関するこのページを見る") / [ 11
](https://cloud.google.com/appengine/docs/standard/java11/

release-notes?hl=ja "Java 11 ランタイムに関するこのページを見る") |  PHP [ 5
](https://cloud.google.com/appengine/docs/standard/php/release-notes?hl=ja
"PHP 5 ランタイムに関するこのページを見る") / [ 7
](https://cloud.google.com/appengine/docs/standard/php7/

release-notes?hl=ja "PHP 7 ランタイムに関するこのページを見る") |  [ Ruby
](https://cloud.google.com/appengine/docs/standard/ruby/

release-notes?hl=ja "Ruby ランタイムに関するこのページを見る") |  Go [ 1.9
](https://cloud.google.com/appengine/docs/standard/go/release-notes?hl=ja "Go
1.9 ランタイムに関するこのページを見る") / [ 1.11
](https://cloud.google.com/appengine/docs/standard/go111/

release-notes?hl=ja "このページを Go 1.11 ランタイムで表示する") / [ 1.12
](https://cloud.google.com/appengine/docs/standard/go112/

release-notes?hl=ja "Go 1.12 ランタイムに関するこのページを見る") |  [ Node.js
](https://cloud.google.com/appengine/docs/standard/nodejs/

release-notes?hl=ja "Node.js ランタイムに関するこのページを見る")

以下のリリースノート以外にも、 [ 公開バグトラッカー
](https://issuetracker.google.com/issues?q=componentid%3A187191%2B&hl=ja)
で既知の問題を追跡できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加してください。

##  2019 年 7 月 30 日

  * ` GoogleAppEngineLauncher.dmg ` 、 ` GoogleAppEngine.msi ` 、 ` google_appengine.zip ` ファイルを通じて提供される AppCfg ツールおよび従来のスタンドアロンの App Engine SDK は、非推奨になります。2020 年 7 月 30 日をもって、Google はサポートを終了します。 
  * App Engine SDK の機能は、 [ Cloud SDK ](https://cloud.google.com/sdk/docs?hl=ja) を通じてのみ提供されます。詳細については、 [ Cloud SDK への移行 ](https://cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration?hl=ja) をご覧ください。 

##  2019 年 4 月 18 日

  * App Engine が、 ` asia-northeast2 ` リージョン（日本の大阪）で使用できるようになりました。 

##  2019 年 4 月 15 日

  * App Engine が、 ` europe-west6 ` リージョン（スイスのチューリッヒ）で使用できるようになりました。 

##  2019 年 4 月 9 日

  * [ Cloud Tasks ](https://cloud.google.com/tasks/docs?hl=ja) の一般提供を開始しました。ユーザー リクエスト外で非同期に実行するタスクの設定に使用できます。 

  * [ サーバーレス VPC アクセス ](https://cloud.google.com/appengine/docs/standard/python3/connecting-vpc?hl=ja) のベータ版が利用可能になりました。サーバーレス VPC アクセスを使用すると、VPC ネットワークの内部リソース（Compute Engine VM インスタンスや Cloud Memorystore インスタンス）にアプリを接続できます。 

##  2019 年 4 月 4 日

  * Python 3 ランタイムがバージョン 3.7.3 にアップデートされました。 

##  2019 年 1 月 11 日

  * Python 3 ランタイムがバージョン 3.7.2 にアップデートされました。 

##  2018 年 12 月 14 日

  * App Engine スタンダード環境用の [ Python 3.7 ランタイム ](https://cloud.google.com/appengine/docs/standard/python3?hl=ja) の一般提供を開始しました。 

##  2018 年 12 月 12 日

  * Python SDK がバージョン 1.9.81 にアップデートされました。 
  * すべてのアプリが BSD ネットワーク ソケットに切り替えられました。アプリの変更は不要です。 
  * [ Sockets API ](https://cloud.google.com/appengine/docs/standard/python/sockets?hl=ja) の一般提供を開始しました。 

##  2018 年 11 月 16 日

  * nginx がデフォルトのウェブサーバーになりました。アプリの変更は不要です。 

##  2018 年 10 月 31 日

  * Python 3 ランタイムは Python バージョン 3.7.1 にアップデートされました。 
  * Python 3 ランタイムで、 ` requirements.txt ` ファイルの再帰的エントリがサポートされるようになりました。 

##  2018 年 10 月 22 日

  * App Engine が、 ` asia-east2 ` リージョン（香港）で使用できるようになりました。 

##  2018 年 8 月 8 日

  * App Engine スタンダード環境用の [ Python 3.7 ランタイム ](https://cloud.google.com/appengine/docs/standard/python3?hl=ja) のベータ版が利用可能になりました。 
  * [ Python 2.7 ランタイムと Python 3.7 ランタイムの相違点 ](https://cloud.google.com/appengine/docs/standard/python3/python-differences?hl=ja) のリストが公開されました。 

##  2018 年 7 月 10 日

  * App Engine が、 ` us-west2 ` リージョン（ロサンゼルス）で使用できるようになりました。 

##  2018 年 7 月 2 日

` max_instances ` 設定を使用したときに App Engine が積極的にインスタンスをシャットダウンしていた [ 自動スケーリング構成
](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=ja#scaling_elements)
の不具合を修正しました。

##  2018 年 5 月 15 日

  * 自動スケーリング システムへのアップグレードの段階的導入を完了: 
    * 効率性が向上することで、全般的にインスタンス費用が削減され（多くのユーザーで最大 6% の削減）、新しいインスタンスへの最初のリクエストである読み込みリクエスト __ が最大 30% 削減されます。 
    * 新しい最大インスタンス数の設定により、スケジュールするインスタンス総数の上限を設定できるようになりました。 
    * 新しい最小インスタンス数の設定により、各アプリで実行し続けるインスタンスの最小数を指定できるようになりました。 
    * 新しいターゲット CPU 使用率設定により、レイテンシとコストのバランスを最適化できるようになりました。 
    * 新しいターゲット スループット使用率の設定により、新しいインスタンスの起動時の同時リクエスト数を最適化できるようになりました。 
    * 自動スケーリングの常駐インスタンスが廃止されました。以前は、 ` min_idle_instances ` 設定を使用すると、Cloud Console で最小アイドル状態のインスタンスが [常駐] __ としてラベル付けされ、残りのインスタンスは [ダイナミック] __ としてラベル付けされていました。新しいスケジューラでは、自動スケーリングのすべてのインスタンスは [ダイナミック] __ としてラベル付けされます。ただし、基本的な動作は以前の動作と同様です。 ` min_idle_instances ` を使用してウォームアップ リクエストを有効にすると、トラフィックが発生しない期間であっても、少なくとも多くの動的インスタンスが実行中であることを確認できます。 
    * 詳細については、 [ 自動スケーリングのドキュメント ](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=ja#scaling_elements) をご覧ください。 

##  2017 年 12 月 14 日

  * IAM の役割とサービス アカウントを使用したアプリのデプロイに関するアクセス制御のドキュメントで、次の項目を改善しました。 

    * [ App Engine の事前定義された役割 ](https://cloud.google.com/appengine/docs/standard/python3/access-control?hl=ja#predefined_app_engine_roles)
    * [ IAM の役割を使用したデプロイ ](https://cloud.google.com/appengine/docs/standard/python3/granting-project-access?hl=ja#deploying_using_iam_roles)
    * [ 権限の要求 ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=ja#required_permissions)

##  2017 年 10 月 31 日

  * App Engine が、 ` asia-south1 ` リージョン（インドのムンバイ）で使用できるようになりました。 

##  2017 年 10 月 11 日

  * [ App Engine ファイアウォール ](https://cloud.google.com/appengine/docs/standard/python3/creating-firewalls?hl=ja) の一般提供を発表しました。 

##  2017 年 9 月 13 日

  * マネージド証明書を使用して、カスタム ドメインに SSL を追加できるようになりました。アプリケーションにカスタム ドメインをマッピングすると、App Engine によって SSL 証明書が自動的にプロビジョニングされ、証明書の期限が切れる前に更新処理が行われます。また、カスタム ドメインを削除すると、証明書が取り消されます。マネージド証明書はベータ版です。詳細については、 [ SSL によるカスタム ドメインの保護 ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=ja) をご覧ください。 

  * 既存のドメイン マッピングおよび SSL 証明書がある場合、その証明書は引き続き想定どおりに機能します。 [ マネージド SSL 証明書にアップグレードする ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=ja#updating_to_managed_ssl_certificates) こともできます。 

  * [ カスタム ドメインのマッピング ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=ja) に使用する ` gcloud ` コマンドと Admin API メソッドが一般提供されるようになりました。 [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains?hl=ja) と [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=ja) が含まれます。ただし、マネージド SSL 証明書を使用する場合は、 [ SSL によるカスタム ドメインの保護 ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=ja) で指定されているベータ版のコマンドとメソッドを使用してください。 

##  2017 年 9 月 5 日

  * App Engine が、 ` southamerica-east1 ` リージョン（ブラジルのサンパウロ）で使用できるようになりました。 

##  2017 年 8 月 1 日

  * App Engine が、 ` europe-west3 ` リージョン（ドイツのフランクフルト）で使用できるようになりました。 

##  2017 年 7 月 18 日

  * App Engine が、 ` australia-southeast1 ` リージョン（オーストラリアのシドニー）で使用できるようになりました。 

##  2017 年 6 月 6 日

  * App Engine が、 ` europe-west2 ` リージョン（ロンドン）で使用できるようになりました。 
  * Admin API と ` gcloud ` コマンドライン ツールのベータ版レベルの機能を使用して、 [ カスタム ドメインと SSL 証明書の作成と管理 ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=ja) ができるようになりました。 

##  2017 年 5 月 9 日

  * App Engine が、 ` us-east4 ` リージョン（北バージニア）で使用できるようになりました。 

##  2016 年 10 月

  * Channel サービスと XMPP サービスが [ 非推奨 ](https://cloud.google.com/appengine/docs/deprecations?hl=ja) になりました。これらのサービスは 2017 年 10 月 31 日に廃止されます。 

##  2016 年 8 月 1 日

**Admin API に関する注意事項**

  * [ Admin API ](https://cloud.google.com/appengine/docs/admin-api?hl=ja) のバージョン 1 の正式版がリリースされました。 

##  2016 年 8 月 1 日 - バージョン 1.9.42

**Python 3.7 ランタイムに関する注意事項**

  * このリリースには新しい Python 3.7 SDK が含まれていません。Python 3.7 をお使いの場合は、引き続き 1.9.40 SDK を使用してください。 

##  2016 年 7 月 18 日 - バージョン 1.9.40

  * バージョン 1.9.39 はスキップされました。 

  * LeaseTasksByTag のリクエストは 1 秒間に 25 個のリクエストに制限されます。 

  * App Engine ダッシュボードに表示されるサーバーエラーとクライアント エラーに、URL ごとのステータス エラーがより正確に反映されるようになりました。 

  * GCP Console の [ App Engine チュートリアル ](https://console.cloud.google.com/start/appengine?hl=ja) が新しくなりました。使用する言語を選択して、コンソール内で直接インタラクティブなチュートリアルを起動できます。 

  * cron タスクの最大制限が 250 に増えました。 

##  2016 年 7 月 1 日

**Cloud Datastore**

  * 新しい [ Cloud Datastore の料金 ](https://cloud.google.com/appengine/pricing?hl=ja#costs-for-datastore-calls) が適用されました。 

##  2016 年 5 月 25 日 - バージョン 1.9.38

  * ドキュメントに記載されているとおり、許可された範囲（80～90、440～450、1024～65535）外のポートへのリクエストに対して URL 取得によって返されるエラーで、常に ` INVALID_URL ` が返されるようになりました。 

**Cloud Datastore**

  * クロスグループ トランザクションを commit する場合、新しいエンティティまたは更新されたエンティティに対して返されるバージョン番号がすべて同じになりました。以前の動作では、クロスグループ トランザクションの一部として commit された同じグループ内のエンティティには同じバージョン番号が返されましたが、別のグループ内のエンティティには別のバージョン番号が返されることがありました。今回の変更によって、クロスグループ トランザクションの一部として commit されたすべての新しいエンティティと更新されたエンティティは、エンティティ グループに関係なく同じバージョン番号を持つことになります。以前と同様、更新のないエンティティには、新しいバージョン番号は付与されません。 

##  2016 年 5 月 4 日 - バージョン 1.9.37

全般的なバグの修正と改善が含まれています。

##  2016 年 5 月 2 日

**App Engine フレキシブル環境**

  * App Engine フレキシブル環境で [ Ruby ランタイム ](https://cloud.google.com/appengine/docs/flexible/ruby?hl=ja) が使用できるようになりました。 

##  2016 年 4 月 18 日 - バージョン 1.9.36

ユーザーのリクエストにお応えして、IAM の役割とグループ展開のサポートにおいて、App Engine に App Engine Users API
が加わりました。これは、プロジェクトのオーナー、編集者、または閲覧者、あるいは App Engine
の管理者であるユーザーが役割を直接またはグループのメンバーによって与えられているかどうかに関係なく、Users API
によって「管理者」と見なされることを意味します。このリリースでは、「OverQuota」例外タイプに関連するエラー
メッセージに、可能であればエラーの詳細が含まれるようになりました。

##  2016 年 3 月 24 日 - バージョン 1.9.35

  * App Engine マネージド VM の名称が [ App Engine フレキシブル環境 ](https://cloud.google.com/appengine/docs/flexible?hl=ja) に変更されました。 
  * トレースのタイムスタンプをログのタイムスタンプに合わせて修正しました。 

##  2016 年 3 月 4 日 - バージョン 1.9.34

  * 有料アプリケーションの URL 取得のデフォルトの割り当てが増えました。詳細については、 [ 割り当てページ ](https://cloud.google.com/appengine/docs/quotas?hl=ja#UrlFetch) をご覧ください。 

##  2016 年 2 月 17 日 - バージョン 1.9.33

  * URL パス /form が使用可能になり、アプリケーションに転送できるようになりました。以前は、このパスはブロックされていました。 

##  2016 年 2 月 3 日 - バージョン 1.9.32

  * 管理対象 VM のコンテナ作成の選択肢 

` gcloud preview app deploy ` （および ` mvn gcloud:deploy `
）コマンドでは、アーティファクトをサーバーにアップロードし、アプリケーションを管理対象 VM 環境にデプロイするためのコンテナを作成します。

コンテナ イメージをリモートで作成するための 2 つのメカニズムがあります。デフォルトの動作は、Docker がインストールされている一時的な
Compute Engine 仮想マシンにコンテナを作成することです。また、 [ Cloud Build
](https://cloud.google.com/cloud-build/docs?hl=ja) サービスを使用することもできます。Cloud
Build サービスを使用するには、次の手順を実行します。

    1. プロジェクトの [ Cloud Build API を有効化 ](https://support.google.com/cloud/answer/6158841?hl=ja) します。 
    2. コマンド ` gcloud config set app/use_cloud_build True ` を使用します。これにより、 ` gcloud preview app deploy ` のすべての呼び出しで、このサービスを使用するようになります（デフォルトの動作に戻すには、コマンド ` gcloud config set app/use_cloud_build False ` を使用します）。 

##  2016 年 1 月 14 日 - バージョン 1.9.31

App Engine で Google グループがサポートされるようになりました。Google
グループをプロジェクトのメンバーとして追加すると、グループのメンバーが App Engine へのアクセスを許可されます。たとえば、Google
グループがプロジェクトの編集者である場合、グループのすべてのメンバーに App Engine
アプリケーションへの編集者アクセス権限が付与されるようになりました。

##  2015 年 11 月 30 日 - バージョン 1.9.30

ペイロードがないタスクキュー タスクに対する push キュー リクエストのヘッダーに、0 に設定された Content-Length
エントリが含まれるようになりました。以前はこのようなリクエストのヘッダーに Content-Length エントリが含まれていませんでした。

##  2015 年 11 月 30 日 - バージョン 1.9.29

  * 存在していないクエリ、削除とマークされたキュー、クエリテーブルが停止した場合のキューの深さの計算と保存が停止されます。 
  * [ Endpoints API ](https://cloud.google.com/appengine/docs/standard/python/endpoints/create_api?hl=ja#defining_the_api_endpointsapi) を使用する開発者向けに、@Api アノテーションへの検出可能な boolean パラメータが追加され、ユーザーが API 検出を無効にできるようになりました。この機能を使用すると、検出に依存するクライアント ライブラリ（JavaScript など）や API Explorer の動作が妨げられます。 

##  2015 年 10 月 29 日 - バージョン 1.9.28

2015 年 7 月 14 日に非推奨になった Prospective Search API が既存のユーザーに対しても制限されるようになりました。これは
2015 年 12 月 1 日に完全に停止されます。* 検索クエリでの Geo フィルタリングの精度が向上しました。

##  2015 年 9 月 25 日 - バージョン 1.9.27

新しく課金が有効にされたアプリケーションはデフォルトで 1 日の予算が無制限になり、それまでデフォルトだった $0 の 1
日の最大予算がなくなりました。これによって、予算不足による望まない停止が回避されます。アプリケーションの 1
日のコストの上限を設定するには、課金を有効にした後で、 [ App Engine の設定
](https://console.cloud.google.com/project/_/appengine/settings?hl=ja)
で予算を設定します。詳細については、 [ 1 日の予算の設定
](https://cloud.google.com/appengine/docs/developers-
console?hl=ja#setting_a_daily_budget) をご覧ください。

データストア

  * バグの修正: 繰り返される数値ファセットを使用できるようになりました。 
  * ファセット検索の一般提供を開始しました。 

##  2015 年 8 月 27 日 - バージョン 1.9.26

  * oauth2client ライブラリがバージョン [ 1.4.2 ](https://github.com/google/oauth2client/blob/master/CHANGELOG.md) にアップグレードされました。 
  * thread_id または request_id がログエントリのフィールドとして含まれる MVM アプリケーションログに [前後のログを表示] メニューが追加されました。これによって、いずれかのフィールドに基づいてアプリケーションのログを並べ換えられるようになりました。 
  * 現在の負荷に対してアプリケーションをプロビジョニングし、VM とアプリケーション レベルの両方の指標に基づいた柔軟なプロビジョニングを構成できるようになりました。 
  * https://developers.google.com/identity/protocols/application-default-credentials を使用する OAuth2 認証情報を使用して、リモート API にアクセスできるようになりました。 
  * ペイロードが大きすぎる URLFetch リクエストに対して RequestPayloadTooLargeException を使用します。 

##  2015 年 8 月 14 日 - バージョン 1.9.25

  * PyAMF バージョン 0.7.2（ベータ版）が追加されました。 
  * 管理コンソールのメニューが GCP Console にリダイレクトされるようになりました。管理ログなどの一部のサービスは、引き続き管理コンソールで使用できます。 
  * データストアで、プロパティが空白のリストを表現できるようになりました。 
  * retry_limit がゼロに構成されたキュー内の失敗したタスクは再試行されません。 

