#  Python 2.7 リリースノート

1  python  Python 2

Python  2.7  / [ 3.7
](https://cloud.google.com/appengine/docs/standard/python3/

    release-notes?hl=ja "Python 3.7 ランタイムに関するこのページを見る") |  Java [ 8 ](https://cloud.google.com/appengine/docs/standard/java/release-notes?hl=ja "Java 8 ランタイムに関するこのページを見る") / [ 11 ](https://cloud.google.com/appengine/docs/standard/java11/
    release-notes?hl=ja "Java 11 ランタイムに関するこのページを見る") |  PHP [ 5 ](https://cloud.google.com/appengine/docs/standard/php/release-notes?hl=ja "PHP 5 ランタイムに関するこのページを見る") / [ 7 ](https://cloud.google.com/appengine/docs/standard/php7/
    release-notes?hl=ja "PHP 7 ランタイムに関するこのページを見る") |  [ Ruby ](https://cloud.google.com/appengine/docs/standard/ruby/
    release-notes?hl=ja "Ruby ランタイムに関するこのページを見る") |  Go [ 1.11 ](https://cloud.google.com/appengine/docs/standard/go111/
    release-notes?hl=ja "Go 1.11 ランタイムに関するこのページを見る") / [ 1.12+ ](https://cloud.google.com/appengine/docs/standard/go/
    release-notes?hl=ja "Go 1.12 および最新のランタイムに関するこのページを見る") |  [ Node.js ](https://cloud.google.com/appengine/docs/standard/nodejs/
    release-notes?hl=ja "Node.js ランタイムに関するこのページを見る")

以下のリリースノート以外にも、 [ 公開バグトラッカー
](https://issuetracker.google.com/issues?q=componentid%3A187191%2B&hl=ja)
で既知の問題を追跡できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/app-engine-standard-environment-
python-runtimes-release-notes.xml ` を直接追加します。

##  2020 年 2 月 11 日

App Engine は、アプリへのリクエストの送信に使用する URL を変更します。URL に [ リージョン ID を含める
](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-
routed?hl=ja#region-id) ことが可能となり、Google
でお客様のリクエストをより効率良く確実に転送できるようになります。たとえば、アプリは ` https://  PROJECT_ID  .
REGION_ID  .r.appspot.com ` でリクエストを受け取ることができます。この新しい URL
は、既存のアプリでは省略可能でしたが、新しいアプリではまもなく必須になります。

移行がスムーズに行われるように、リージョン ID を使用するよう App Engine を徐々に更新しています。Google Cloud
プロジェクトがまだ更新されていない場合、アプリにリージョン ID が表示されません。ID は既存のアプリでは省略可能なため、リージョン ID
が既存のアプリで使用可能になったときに、URL を更新したり、他の変更を行ったりする必要はありません。

##  2020 年 2 月 6 日

  * プロジェクトに新たな使用量上限を適用することはできません。既存の使用量上限は引き続き有効です。アプリの費用を制限する方法の詳細については、 [ 費用の制限 ](https://cloud.google.com/appengine/docs/managing-costs?hl=ja) をご覧ください。 

##  2019 年 1 月 2 日

  * Python SDK がバージョン 1.9.88 にアップデートされました。 

##  2019 年 12 月 11 日

  * [ サーバーレス VPC アクセス ](https://cloud.google.com/appengine/docs/standard/python/connecting-vpc?hl=ja) の一般提供を開始しました。 

##  2019 年 10 月 30 日

  * Python SDK がバージョン 1.9.87 にアップデートされました。 

##  2019 年 7 月 30 日

  * ` GoogleAppEngineLauncher.dmg ` 、 ` GoogleAppEngine.msi ` 、 ` google_appengine.zip ` ファイルを通じて提供される AppCfg ツールおよび従来のスタンドアロンの App Engine SDK は、非推奨になります。2020 年 7 月 30 日をもって、Google はサポートを終了します。 
  * App Engine SDK の機能は、 [ Cloud SDK ](https://cloud.google.com/sdk/docs?hl=ja) を通じてのみ提供されます。詳細については、 [ Cloud SDK への移行 ](https://cloud.google.com/appengine/docs/standard/python/sdk-gcloud-migration?hl=ja) をご覧ください。 

##  2019 年 6 月 3 日

  * Python SDK がバージョン 1.9.86 にアップデートされました。 

##  2019 年 4 月 18 日

  * App Engine が ` asia-northeast2 ` リージョン（大阪、日本）で利用できるようになりました。 

##  2019 年 4 月 15 日

  * App Engine が ` europe-west6 ` リージョン（スイス、チューリッヒ）でご利用いただけるようになりました。 

##  2019 年 4 月 9 日

  * [ サーバーレス VPC アクセス ](https://cloud.google.com/appengine/docs/standard/python/connecting-vpc?hl=ja) のベータ版が利用可能になりました。サーバーレス VPC アクセスを使用すると、VPC ネットワーク内の Compute Engine VM インスタンス、Memorystore インスタンスなどの内部リソースにアプリを接続できます。 

##  2019 年 3 月 28 日

  * Python SDK がバージョン 1.9.85 にアップデートされました。 

##  2019 年 3 月 5 日

  * Python SDK がバージョン 1.9.84 にアップデートされました。 

##  2019 年 2 月 13 日

  * Python SDK がバージョン 1.9.83 にアップデートされました。 

##  2019 年 1 月 17 日

  * Python SDK がバージョン 1.9.82 にアップデートされました。 

##  2019 年 1 月 11 日

  * Python 3 ランタイムがバージョン 3.7.2 にアップデートされました。 

##  2018 年 12 月 21 日

  * ` select ` 、 ` mmap ` 、 ` grp ` 、 ` fcntl ` 、 ` spwd ` モジュールが Python インタープリタに追加されました。 
  * ` fork ` 、 ` waitpid ` 、 ` chown ` 、 ` execv ` 、 ` fchmod ` 、 ` fchown ` 、 ` ftruncate ` 、 ` kill ` 、 ` lchown ` 、 ` lstat ` 、 ` readline ` 、 ` setuid ` 関数が ` os ` モジュールに追加されました。 

##  2018 年 12 月 14 日

  * App Engine スタンダード環境用の [ Python 3.7 ランタイム ](https://cloud.google.com/appengine/docs/standard/python3?hl=ja) の一般提供を開始しました。 

##  2018 年 12 月 12 日

  * Python SDK がバージョン 1.9.81 にアップデートされました。 
  * すべてのアプリが BSD ネットワーク ソケットに切り替えられました。アプリの変更は不要です。 
  * [ Sockets API ](https://cloud.google.com/appengine/docs/standard/python/sockets?hl=ja) の一般提供を開始しました。 

##  2018 年 11 月 16 日

  * nginx がデフォルトのウェブサーバーになりました。アプリの変更は不要です。 

##  2018 年 11 月 8 日

  * Python SDK がバージョン 1.9.80 にアップデートされました。 
  * 細かいバグを修正しました。 

##  2018 年 10 月 31 日

  * Python 3 ランタイムは Python バージョン 3.7.1 にアップデートされました。 
  * Python 3 ランタイムは、 ` requirements.txt ` ファイル内の繰り返しエントリをサポートします。 

##  2018 年 10 月 25 日

  * Python SDK がバージョン 1.9.78 にアップデートされました。 
  * 細かいバグを修正しました。 

##  2018 年 10 月 22 日

  * App Engine が ` asia-east2 ` リージョン（香港）でご利用いただけるようになりました。 

##  2018 年 10 月 15 日

  * Python 2.7 ランタイムのすべてのアプリが [ gVisor サンドボックス ](https://github.com/google/gvisor) で実行できるようになりました。 
  * Python 2.7 のすべてのアプリが 64 ビット Python インタープリタで動作するようになりました。 

##  2018 年 10 月 4 日

  * Python SDK がバージョン 1.9.77 にアップデートされました。 

##  2018 年 9 月 26 日

  * Python SDK がバージョン 1.9.76 にアップデートされました。 
  * dev_appserver のインポート失敗の回避策として、ローカルにインストールされた ` grpcio ` を使用できます。 

##  2018 年 9 月 5 日

  * Python SDK がバージョン 1.9.75 にアップデートされました。 
  * ` dev_appserver ` ローカル開発用サーバーを使う場合のデフォルトのローカル データストア エミュレーションとして、 [ Cloud Datastore エミュレータ ](https://cloud.google.com/appengine/docs/standard/python/tools/migrate-cloud-datastore-emulator?hl=ja) のロールアウトが開始されました。 

##  2018 年 8 月 24 日

**Cloud Endpoints Frameworks v1 のシャットダウンが近づいています**

App Engine スタンダード環境用 Cloud Endpoints Frameworks v1 は、2017 年 8 月 2
日に非推奨になりました。このサービスは 2018 年 9 月 3 日に [ シャットダウンされる予定
](https://cloud.google.com/appengine/docs/deprecations/endpoints-v1?hl=ja)
であり、ドキュメントは削除されます。停止を回避するには、v1 アプリケーションを移行する必要があります。アプリケーションを Endpoints
Frameworks v2 に移行する方法については、 [ Python 移行ガイド
](https://cloud.google.com/endpoints/docs/frameworks/python/migrating?hl=ja)
をご覧ください。

##  2018 年 8 月 14 日

  * Python SDK がバージョン 1.9.74 にアップデートされました。 
  * 細かいバグを修正しました。 

##  2018 年 8 月 8 日

  * App Engine スタンダード環境用の [ Python 3.7 ランタイム ](https://cloud.google.com/appengine/docs/standard/python3?hl=ja) のベータ版が利用可能になりました。 
  * [ Python 2.7 ランタイムと Python 3.7 ランタイムの相違点 ](https://cloud.google.com/appengine/docs/standard/python3/python-differences?hl=ja) のリストが公開されました。 

##  2018 年 7 月 12 日

  * Python SDK がバージョン 1.9.73 にアップデートされました。 
  * dev_appserver が実行中の Cloud Datastore エミュレータと通信する際に発生するクラッシュを修正しました。この以前には、dev_appserver を実行したシェルに環境変数「DATASTORE_PROJECT_ID」が存在するときにクラッシュしていました。 
  * [ ローカルの開発用サーバー ](https://cloud.google.com/appengine/docs/standard/go/tools/using-local-server?hl=ja) が起動する際に実行中のプロセスのプロセス ID が出力されるようになりました。このプロセス ID をアプリのデバッグの際に使用できます。 

##  2018 年 7 月 10 日

  * App Engine が ` us-west2 ` リージョン（ロサンゼルス）で利用できるようになりました。 

##  2018 年 7 月 2 日

` max_instances ` 設定が使用されたときに App Engine が積極的にインスタンスをシャットダウンしていた [ 自動スケーリング構成
](https://cloud.google.com/appengine/docs/standard/python/config/appref?hl=ja#scaling_elements)
における不具合を修正しました。

##  2018 年 6 月 28 日

  * Python SDK がバージョン 1.9.72 にアップデートされました。 
  * ローカルの開発用サーバー（ ` dev_appserver ` ）プロセスの ` DATASTORE_PROJECT_ID ` 環境変数が削除されました。 ` dev_appserver ` が Cloud Datastore エミュレータと並行して実行できるようになりました。 
  * 起動の際にローカルの開発用サーバーからアプリプロセスのプロセス ID が出力されるようになりました。 

##  2018 年 6 月 21 日

  * Python SDK がバージョン 1.9.71 にアップデートされました。 
  * 細かいバグを修正しました。 

##  2018 年 5 月 24 日

  * すべてのアプリの SSL ライブラリをバージョン 2.7 からバージョン 2.7.11 に移行しました。詳しくは、 [ Python SSL バージョン 2.7 の提供終了に関するドキュメント ](https://cloud.google.com/appengine/docs/deprecations/python-ssl-27?hl=ja) をご覧ください。 

##  2018 年 5 月 17 日

  * Python SDK がバージョン 1.9.70 にアップデートされました。 
  * 細かいバグを修正しました。 

##  2018 年 5 月 15 日

  * 自動スケーリング システムへのアップグレードの段階的ロールアウトが完了しました。 
    * 効率性が向上することで、全般的にインスタンス費用が削減され（多くのユーザーで最大 6% の削減）、新しいインスタンスへの最初のリクエストである __ 読み込みリクエストが最大 30% 削減されます。 
    * 新しい最大インスタンス数の設定により、スケジュールするインスタンス総数の上限を設定できるようになりました。 
    * 新しい最小インスタンス数の設定により、各アプリで実行し続けるインスタンスの最小数を指定できるようになりました。 
    * 新しいターゲット CPU 使用率設定により、レイテンシとコストのバランスを最適化できるようになりました。 
    * 新しいターゲット スループット使用率の設定により、新しいインスタンスの起動時の同時リクエスト数を最適化できるようになりました。 
    * 自動スケーリングの常駐インスタンスが廃止されました。以前は、 ` min_idle_instances ` 設定を使用すると、Cloud Console で最小アイドル状態のインスタンスが _[常駐]_ としてラベル付けされ、残りのインスタンスは _[ダイナミック]_ としてラベル付けされていました。新しいスケジューラでは、自動スケーリングによりすべてのインスタンスは _[ダイナミック]_ としてラベル付けされます。ただし、基本的な動作は以前の動作と同様です。 ` min_idle_instances ` を使用してウォームアップ リクエストを有効にすると、トラフィックが発生していない期間でも、少なくともその数の動的インスタンスが実行されていることがわかります。 
    * 詳細については、 [ 自動スケーリングのドキュメント ](https://cloud.google.com/appengine/docs/standard/python/config/appref?hl=ja#scaling_elements) をご覧ください。 

##  2018 年 4 月 11 日

**Python ランタイムに関する注意事項**

  * Python SDK がバージョン 1.9.69 に更新されました。 
  * 組み込みサードパーティ ライブラリに [ PyTz バージョン 2017.3 ](https://pypi.python.org/pypi/pytz/2017.3) を追加しました。 

##  2018 年 4 月 3 日

**Python ランタイムに関する注意事項**

  * Python SDK がバージョン 1.9.68 に更新されました。 
  * 細かいバグを修正しました。 

##  2018 年 2 月 14 日

**Python ランタイムに関する注意事項**

  * Python SDK がバージョン 1.9.67 に更新されました。 

##  2018 年 1 月 23 日

  * Python SDK が 1.9.66 に更新されました。 
  * ローカル開発サーバーで PHP アプリを起動するときに、 [ ` ipaddr ` ライブラリのインポートに関する問題 ](https://issuetracker.google.com/issues/71704025?hl=ja) を修正しました。 

##  2017 年 12 月 20 日

**Python ランタイムに関する注意事項**

  * Python SDK がバージョン 1.9.65 に更新されました。 
  * 組み込みサードパーティ ライブラリに [ SetupTools バージョン 36.6.0 ](https://pypi.python.org/pypi/setuptools/36.6.0) を追加しました。 

##  2017 年 12 月 14 日

  * IAM の役割とサービス アカウントを使用したアプリのデプロイに関するアクセス制御のドキュメントで、次の項目を改善しました。 

    * [ App Engine の事前定義された役割 ](https://cloud.google.com/appengine/docs/standard/python/access-control?hl=ja#predefined_app_engine_roles)
    * [ IAM の役割を使用したデプロイ ](https://cloud.google.com/appengine/docs/standard/python/granting-project-access?hl=ja#deploying_using_iam_roles)
    * [ 権限の要求 ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=ja#required_permissions)

##  2017 年 12 月 9 日

**既知の問題** : [ Werkzeug 0.13 のアップデートにより、App Engine でサポートされていないモジュールが追加
](https://issuetracker.google.com/issues/70426718?hl=ja) され、その結果、 `
ImportError: cannot import name SpooledTemporaryFile ` エラーが発生しました。以前のバージョンの
werkzeug にアプリをダウングレードして、エラーを修正できます。詳しくは、リンクされている既知の問題をご覧ください。

##  2017 年 12 月 5 日

**Python ランタイムに関する注意事項**

  * Python SDK がバージョン 1.9.64 に更新されました。 
  * すべての着信 HTTP リクエストについては、 ` dev_appserver.py ` では、すべての HTTP リクエストに HTTP ` Host ` ヘッダーを付け、その値を IPv4 または IPv6 ループバック アドレスの ` localhost ` 、または指定されている場合は ` --host ` 経由で渡される値とすることが必要となりました。HTTP / 1.0 のみ、 ` Host ` ヘッダーのないリクエストが引き続き許可されます。ホストチェックを無効にするには、 ` --enable_host_checking ` フラグを ` false ` に設定します。ただし、DNS 再バインド攻撃から保護されるよう、ホストチェックを有効にしておくことをおすすめします。 
  * ` dev_appserver.py ` 管理コンソールにセキュリティ ヘッダーに関連する動作を追加しました。 
    * ` Origin ` ヘッダーを含む受信リクエストは拒否されます。 
    * すべてのレスポンスに次のヘッダーを追加しました。 
      * ` X-Frame-Options=SAMEORIGIN `
      * ` X-XSS-Protection=1; mode=block `
      * ` Content-Security-Policy=default-src 'self'; frame-ancestors 'none' `

##  2017 年 11 月 15 日

**Python ランタイムに関する注意事項**

  * Python SDK がバージョン 1.9.63 に更新されました。 
  * [ Python SSL ライブラリ バージョン 2.7 の非推奨 ](https://cloud.google.com/appengine/docs/deprecations/python-ssl-27?hl=ja) を発表しました。SSL バージョン 2.7.11 を使用するようアプリケーションを移行する必要があります。 
  * [ Go SDK ](https://cloud.google.com/appengine/docs/standard/go/release-notes?hl=ja#november_15_2017) をサポートする Python SDK 内のアップデート。 

##  2017 年 10 月 31 日

  * App Engine が、 ` asia-south1 ` リージョン（インドのムンバイ）で使用できるようになりました。 

##  2017 年 10 月 25 日

**Python ランタイムに関する注意事項**

  * Python SDK がバージョン 1.9.62 に更新されました。 
  * 細かいバグを修正しました。 

##  2017 年 10 月 11 日

  * [ App Engine ファイアウォール ](https://cloud.google.com/appengine/docs/standard/python/creating-firewalls?hl=ja) の一般提供を発表しました。 

##  2017 年 9 月 21 日

**Python ランタイムに関する注意事項**

  * Python SDK がバージョン 1.9.61 に更新されました。 
  * ` pytz ` を 2017.2 に更新しました。 

##  2017 年 9 月 13 日

  * マネージド証明書を使用して、カスタム ドメインに SSL を追加できるようになりました。アプリケーションにカスタム ドメインをマッピングすると、App Engine によって SSL 証明書が自動的にプロビジョニングされ、証明書の期限が切れる前に更新処理が行われます。また、カスタム ドメインを削除すると、証明書が取り消されます。マネージド証明書はベータ版です。詳細については、 [ SSL によるカスタム ドメインの保護 ](https://cloud.google.com/appengine/docs/standard/python/securing-custom-domains-with-ssl?hl=ja) をご覧ください。 

  * 既存のドメイン マッピングと SSL 証明書がある場合、変わることなく想定どおりに機能します。 [ マネージド SSL 証明書にアップグレード ](https://cloud.google.com/appengine/docs/standard/python/securing-custom-domains-with-ssl?hl=ja#updating_to_managed_ssl_certificates) することもできます。 

  * [ カスタム ドメインのマッピング ](https://cloud.google.com/appengine/docs/standard/python/mapping-custom-domains?hl=ja) に使用する ` gcloud ` コマンドと Admin API メソッドが一般提供されるようになりました。対象のレポートには、 [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains?hl=ja) および [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=ja) が含まれます。ただし、マネージド SSL 証明書を使用する場合は、 [ SSL によるカスタム ドメインの保護 ](https://cloud.google.com/appengine/docs/standard/python/securing-custom-domains-with-ssl?hl=ja) で指定されているベータ版のコマンドとメソッドを使用してください。 

##  2017 年 9 月 5 日

  * App Engine が ` southamerica-east1 ` リージョン（ブラジルのサンパウロ）で使用できるようになりました。 

**Python ランタイムに関する注意事項**

  * Python SDK がバージョン 1.9.60 に更新されました。 

  * リリースには細かいバグ修正が含まれています。 

##  2017 年 8 月 30 日

  * Python SDK がバージョン 1.9.59 に更新されました。 

##  2017 年 8 月 28 日

  * Python SDK がバージョン 1.9.58 に更新されました。 

  * このリリースでは、gRPC のクライアント サポートが追加され、App Engine アプリケーションから gRPC サーバーに接続できます。 ` grpcio ` ライブラリのリクエストとインストールについて詳しくは、 [ サードパーティ ライブラリの使用 ](https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27?hl=ja) をご覧ください。 

  * このリリースには、 [ Google Cloud クライアント ライブラリ ](https://googleapis.github.io/google-cloud-python/) や gRPC サーバー リクエストのサポートは含まれていません。 

##  2017 年 8 月 1 日

  * App Engine が ` europe-west3 ` リージョン（ドイツのフランクフルト）で使用できるようになりました。 

##  2017 年 7 月 18 日

  * App Engine が、 ` australia-southeast1 ` リージョン（オーストラリアのシドニー）で使用できるようになりました。 

##  2017 年 7 月 12 日

  * Python SDK がバージョン 1.9.57 に更新されました。 

##  2017 年 6 月 27 日

  * Python SDK がバージョン 1.9.56 に更新されました。 
  * [ 組み込みサードパーティ ライブラリ ](https://cloud.google.com/appengine/docs/standard/python/tools/built-in-libraries-27?hl=ja) に Django v1.11 を追加しました。 

##  2017 年 6 月 21 日

  * Python SDK がバージョン 1.9.55 に更新されました。 
  * [ 組み込みサードパーティ ライブラリ ](https://cloud.google.com/appengine/docs/standard/python/tools/built-in-libraries-27?hl=ja) に次の新しいライブラリを追加しました。 

    * ujson v1.35 
    * lxml v3.7.3 
    * flask v0.12. 
  * 検索 API: [ ファセット検出値の制限 ](https://cloud.google.com/appengine/docs/standard/python/refdocs/google.appengine.api.search.search?hl=ja#google.appengine.api.search.search.FacetOptions) の上限値を 100 に増やしました。 

##  2017 年 6 月 15 日

  * MySQLdb の場合は、 ` utf8mb4 ` 文字セットを使用できるようになりました。 

  * SSL ` 2.7.11 ` の場合、証明書のルートパスを指定しないときにデフォルトが ` /etc/ca-certificates.crt ` に設定されます。 

  * Unix のパスワード データベースには [ PWD モジュール ](https://docs.python.org/2/library/pwd.html) を使用できます。 

##  2017 年 6 月 6 日

  * App Engine が ` europe-west2 ` リージョン（ロンドン）で使用できるようになりました。 
  * Admin API と ` gcloud ` コマンドライン ツールのベータ版レベルの機能を使用して、 [ カスタム ドメインと SSL 証明書の作成と管理 ](https://cloud.google.com/appengine/docs/standard/python/mapping-custom-domains?hl=ja) ができるようになりました。 

##  2017 年 5 月 22 日

  * Python SDK がバージョン 1.9.54 に更新されました。 
  * Python 2.7.12 に基づいて Python SDK を更新しました。 

##  2017 年 5 月 15 日

  * Python ランタイムを Python 2.7.12 に更新しました。 
  * ` 2.7.11 ` としてバージョン化された SSL モジュールの SSL 証明書の検証動作を、証明書を検証しないように修正しました。この動作は、 [ 環境変数 ](https://cloud.google.com/appengine/docs/standard/python/config/appref?hl=ja#environment_variables) ` PYTHONHTTPSVERIFY ` によって制御できます。証明書の検証が必要な場合は ` 1 ` に設定します。 
  * アプリケーションの互換性を保証するため、トークナイザの [ https://bugs.python.org/issue22221 ](https://bugs.python.org/issue22221) に対する修正を削除しました。これにより、PEP-263 が正しく処理されます。 

##  2017 年 5 月 9 日

  * App Engine が ` us-east4 ` リージョン（北バージニア）で使用できるようになりました。 

##  2017 年 4 月 27 日

  * Python SDK がバージョン 1.9.53 に更新されました。 

  * Go 1.8 ベータ版の準備として、Go ` api_version ` が特定の ` GOROOT ` ディレクトリにマッピングされました。 

##  2017 年 4 月 5 日

  * Python SDK がバージョン 1.9.52 に更新されました。 

  * リモート API シェルで Server Name Indication（SNI）が機能しないというバグを修正しました。 

##  2017 年 3 月 20 日

  * Python SDK がバージョン 1.9.51 に更新されました。 

  * リモート API シェルの Server Name Indication（SNI）をサポートします。 

##  2017 年 1 月 23 日

  * Python SDK がバージョン 1.9.50 に更新されました。 

  * ` remote_api_shell.py ` ツールが Cloud Shell 上で動作しなくなるバグを修正しました。 

##  2016 年 12 月 1 日

  * Python SDK がバージョン 1.9.49 に更新されました。 

  * pycrypto が 2.6.1 に更新されました。 

  * pytz が2016.4 に更新されました。 

##  2016 年 10 月 27 日

  * Channel サービスと XMPP サービスが [ 非推奨 ](https://cloud.google.com/appengine/docs/deprecations?hl=ja) になりました。これらのサービスは 2017 年 10 月 31 日に廃止されます。 

##  2016 年 8 月 1 日

**Admin API に関する注意事項**

  * [ Admin API ](https://cloud.google.com/appengine/docs/admin-api?hl=ja) のバージョン 1 の正式版がリリースされました。 

##  2016 年 8 月 1 日 - バージョン 1.9.42

**Python 2 ランタイムに関する注意事項**

  * このリリースには新しい Python 2 SDK が含まれていません。Python 2 をお使いの場合は、引き続き 1.9.40 SDK を使用してください。 

##  2016 年 7 月 26 日

**Python 2 ランタイムに関する注意事項**

すべてのアプリで SSL 2.7.11 がデフォルトになりました。 ` app.yaml ` 構成ファイルで ` ssl ` ライブラリに `
version: 2.7 ` または ` version: latest ` が指定されている場合、アプリは 2.7 バージョンを使用します。 [
組み込みライブラリの詳細
](https://cloud.google.com/appengine/docs/standard/python/tools/using-
libraries-python-27?hl=ja#requesting_a_library) をご覧ください。

##  2016 年 7 月 18 日 - バージョン 1.9.40

  * バージョン 1.9.39 はスキップされました。 

  * LeaseTasksByTag のリクエストは 1 秒間に 25 個のリクエストに制限されます。 

  * App Engine ダッシュボードに表示されるサーバーエラーとクライアント エラーに、URL ごとのステータス エラーがより正確に反映されるようになりました。 

  * Cloud Console の [ App Engine チュートリアル ](https://console.cloud.google.com/start/appengine?hl=ja) が新しくなりました。使用する言語を選択して、コンソール内で直接インタラクティブなチュートリアルを起動できます。 

  * cron タスクの最大制限が 250 に増えました。 

**Python ランタイムに関する注意事項**

  * Python エンドポイントで、すべての有効な Google ID トークン発行元が受け入れられます。 

##  2016 年 7 月 1 日

**Cloud Datastore**

  * 新しい [ Cloud Datastore の料金 ](https://cloud.google.com/appengine/pricing?hl=ja#costs-for-datastore-calls) が有効になりました。 

##  2016 年 5 月 25 日 - バージョン 1.9.38

  * ドキュメントに記載されているように、許可範囲（80～90、440～450、1024～65535）外のポートへのリクエストに対して URL 取得によって返されるエラーで、常に ` INVALID_URL ` を返すようになりました。 

**Cloud Datastore**

  * クロスグループ トランザクションを commit する場合、新しいエンティティまたは更新されたエンティティに対して返されるバージョン番号がすべて同じになりました。以前の動作では、クロスグループ トランザクションの一部として commit された同じグループ内のエンティティには同じバージョン番号が返されましたが、別のグループ内のエンティティには別のバージョン番号が返されることがありました。今回の変更によって、クロスグループ トランザクションの一部として commit されたすべての新しいエンティティと更新されたエンティティは、エンティティ グループに関係なく同じバージョン番号を持つことになります。以前と同様、更新されないエンティティには、新しいバージョン番号は付与されません。 

##  2016 年 5 月 4 日 - バージョン 1.9.37

全般的なバグの修正と改善が含まれています。

**Python ランタイムに関する注意事項**

  * Python 2.7.11 をベースにしたサードパーティ ライブラリ "ssl" の新しいバージョンが含まれています。 ` app.yaml ` ファイルの [ ` libraries ` ](https://cloud.google.com/appengine/docs/standard/python/config/appref?hl=ja#libraries) セクションでライブラリのバージョン「2.7.11」を選択できます。 

##  2016 年 5 月 2 日

**App Engine フレキシブル環境**

  * App Engine フレキシブル環境で [ Ruby ランタイム ](https://cloud.google.com/appengine/docs/flexible/ruby?hl=ja) が使用できるようになりました。 

##  2016 年 4 月 18 日 - バージョン 1.9.36

ユーザーのリクエストにお応えして、IAM の役割とグループ展開のサポートにおいて、App Engine に App Engine Users API
が加わりました。これは、プロジェクトのオーナー、編集者、または閲覧者、あるいは App Engine
の管理者であるユーザーが役割を直接またはグループのメンバーによって与えられているかどうかに関係なく、Users API
によって「管理者」とみなされることを意味します。このリリースでは、「OverQuota」例外タイプに関連するエラー
メッセージに、可能であればエラーの詳細が含まれるようになりました。

**Python ランタイムに関する注意事項**

  * Google はメールサービスの割り当ての増加リクエストを受け入れなくなりました。代わりに、 [ Sendgrid ](https://cloud.google.com/appengine/docs/standard/python/mail/sendgrid?hl=ja) を使用してください。 

##  2016 年 3 月 24 日 - バージョン 1.9.35

  * App Engine マネージド VM の名前が [ App Engine フレキシブル環境 ](https://cloud.google.com/appengine/docs/flexible?hl=ja) に変更されました。 
  * トレースのタイムスタンプをログのタイムスタンプに合わせて修正しました。 

##  2016 年 3 月 4 日 - バージョン 1.9.34

  * 有料アプリケーションの URL 取得のデフォルトの割り当てが増えました。詳細については、 [ 割り当てページ ](https://cloud.google.com/appengine/docs/quotas?hl=ja#UrlFetch) をご覧ください。 

##  2016 年 2 月 17 日 - バージョン 1.9.33

  * URL パス /form が使用可能になり、アプリケーションに転送できるようになりました。以前は、このパスはブロックされていました。 

##  2016 年 2 月 3 日 - バージョン 1.9.32

  * マネージド VM のコンテナ作成の選択肢 

` gcloud preview app deploy ` （および ` mvn gcloud:deploy `
）コマンドは、アーティファクトをサーバーにアップロードし、アプリをマネージド VM 環境にデプロイするためのコンテナを構築します。

コンテナ イメージをリモートで作成するための 2 つのメカニズムがあります。 デフォルトの動作では、Docker がインストールされている一時的な
Compute Engine 仮想マシンにコンテナを作成します。また、 [ Cloud Build
](https://cloud.google.com/cloud-build/docs?hl=ja) サービスを使用することもできます。Cloud
Build サービスを使用するには、次の手順を行います。

    1. プロジェクトの [ Cloud Build API を有効化 ](https://support.google.com/cloud/answer/6158841?hl=ja) します。 
    2. ` gcloud config set app/use_cloud_build True ` コマンドを使用します。これにより、 ` gcloud preview app deploy ` のすべての呼び出しでサービスが使用されるようになります。デフォルトの動作に戻すには、コマンド ` gcloud config set app/use_cloud_build False ` を使用します。 

##  2016 年 1 月 14 日 - バージョン 1.9.31

App Engine で Google グループがサポートされるようになりました。Google
グループをプロジェクトのメンバーとして追加すると、グループのメンバーが App Engine へのアクセスを許可されます。たとえば、Google
グループがプロジェクトの編集者である場合、グループのすべてのメンバーに App Engine
アプリケーションへの編集者アクセス権限が付与されるようになりました。

##  2015 年 11 月 30 日 - バージョン 1.9.30

ペイロードがないタスクキュー タスクに対する push キュー リクエストのヘッダーに、0 に設定された Content-Length
エントリが含まれるようになりました。以前はこのようなリクエストのヘッダーに Content-Length エントリが含まれていませんでした。

**Python ランタイムに関する注意事項**

  * App Engine で実行される Python アプリケーションに対して、Stackdriver Debugger は自動的に有効になります。 [ 試してみる ](https://cloud.google.com/debugger/docs/setting-up-python-on-app-engine?hl=ja)

##  2015 年 11 月 30 日 - バージョン 1.9.29

  * 存在していないクエリ、削除とマークされたキュー、クエリテーブルが停止した場合のキューの深さの計算と保存が停止されます。 
  * [ Endpoints API ](https://cloud.google.com/appengine/docs/standard/python/endpoints/create_api?hl=ja#defining_the_api_endpointsapi) を使用する開発者向けに、@Api アノテーションへの検出可能な boolean パラメータが追加され、ユーザーが API 検出を無効にできるようになりました。この機能を使用すると、検出に依存するクライアント ライブラリ（JavaScript など）や API Explorer の動作が妨げられます。 

##  2015 年 10 月 29 日 - バージョン 1.9.28

2015 年 7 月 14 日に非推奨になった Prospective Search API が既存のユーザーだけに制限されるようになりました。これは
2015 年 12 月 1 日に完全に停止されます。* 検索クエリでの Geo フィルタリングの精度が向上しました。

**Python ランタイムに関する注意事項**

  * 検索クエリの比較句の中で引用符付きの数字を使用できます。 [ https://issuetracker.google.com/issues/35899722 ](https://issuetracker.google.com/issues/35899722?hl=ja)

##  2015 年 9 月 25 日 - バージョン 1.9.27

新しく課金が有効にされたアプリケーションはデフォルトで 1 日の予算が無制限になり、それまでデフォルトだった $0 の 1
日の最大予算がなくなりました。これによって、予算不足による望まない停止が回避されます。アプリケーションの 1
日のコストの上限を設定するには、課金を有効にした後で、 [ App Engine の設定
](https://console.cloud.google.com/project/_/appengine/settings?hl=ja)
で予算を設定します。詳しくは、 [ 1 日の予算の設定
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
  * 管理コンソールのメニューが Cloud Console にリダイレクトされるようになりました。管理ログなどの一部のサービスは、引き続き管理コンソールで使用できます。 
  * データストアで、プロパティが空白のリストを表現できるようになりました。 
  * retry_limit がゼロに構成されたキュー内の失敗したタスクは再試行されません。 

