#  Java リリースノート

Python [ 2.7
](https://cloud.google.com/appengine/docs/standard/python/release-notes?hl=ja
"Python 2.7 ランタイムに関するこのページを見る") / [ 3.7
](https://cloud.google.com/appengine/docs/standard/python3/

    release-notes?hl=ja "Python 3.7 ランタイムに関するこのページを見る") |  Java  8  / [ 11 ](https://cloud.google.com/appengine/docs/standard/java11/
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
java-runtimes-release-notes.xml ` を直接追加します。

##  2020 年 2 月 11 日

App Engine は、アプリへのリクエストの送信に使用する URL を変更します。URL に [ リージョン ID を含める
](https://cloud.google.com/appengine/docs/standard/java/how-requests-are-
routed?hl=ja#region-id) ことが可能となり、Google
でお客様のリクエストをより効率良く確実に転送できるようになります。たとえば、アプリは ` https://  PROJECT_ID  .
REGION_ID  .r.appspot.com ` でリクエストを受け取ることができます。この新しい URL
は、既存のアプリでは省略可能でしたが、新しいアプリではまもなく必須になります。

移行がスムーズに行われるように、リージョン ID を使用するよう App Engine を徐々に更新しています。Google Cloud
プロジェクトがまだ更新されていない場合、アプリにリージョン ID が表示されません。ID は既存のアプリでは省略可能なため、リージョン ID
が既存のアプリで使用可能になったときに、URL を更新したり、他の変更を行ったりする必要はありません。

##  2020 年 2 月 6 日

  * プロジェクトに新たな使用量上限を適用することはできません。既存の使用量上限は引き続き有効です。アプリの費用を制限する方法の詳細については、 [ 費用の制限 ](https://cloud.google.com/appengine/docs/managing-costs?hl=ja) をご覧ください。 

##  2019 年 1 月 21 日

  * Java SDK がバージョン 1.9.78 に更新されました。 

##  2019 年 12 月 11 日

  * [ サーバーレス VPC アクセス ](https://cloud.google.com/appengine/docs/standard/java/connecting-vpc?hl=ja) の一般提供を開始しました。 

##  2019 年 11 月 7 日

  * Java SDK がバージョン 1.9.77 に更新されました。 
  * Jarkata Jasper JSP コンパイラがバージョン 9.0.24 にアップグレードされます。 

##  2019 年 10 月 17 日

  * App Engine スタンダード環境の [ Java 11 ランタイム ](https://cloud.google.com/appengine/docs/standard/java11/runtime?hl=ja) が 一般提供を開始しました。 

##  2019 年 7 月 30 日

  * ` GoogleAppEngineLauncher.dmg ` 、 ` GoogleAppEngine.msi ` 、 ` google_appengine.zip ` ファイルを通じて提供される AppCfg ツールおよび従来のスタンドアロンの App Engine SDK は、非推奨になります。2020 年 7 月 30 日をもって、Google はサポートを終了します。 
  * App Engine SDK の機能は、 [ Cloud SDK ](https://cloud.google.com/sdk/docs?hl=ja) を通じてのみ提供されます。詳細については、 [ Cloud SDK への移行 ](https://cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration?hl=ja) をご覧ください。 

##  2019 年 6 月 24 日

  * Java SDK がバージョン 1.9.76 に更新されました。 

##  2019 年 6 月 5 日

  * App Engine スタンダード環境の [ Java 11 ランタイム ](https://cloud.google.com/appengine/docs/standard/java11/runtime?hl=ja) がベータ版になりました。 

##  2019 年 6 月 3 日

  * Java SDK がバージョン 1.9.75 に更新されました。 
  * Google App Engine API JAR は、Java 8 ターゲットとしてコンパイルされました。 
  * Memcache からの大規模なバッチ GET のパフォーマンスの問題を修正しました。 

##  2019 年 4 月 30 日

  * Java SDK がバージョン 1.9.74 に更新されました。 

##  2019 年 4 月 18 日

  * App Engine が ` asia-northeast2 ` リージョン（大阪、日本）で利用できるようになりました。 

##  2019 年 4 月 15 日

  * App Engine が ` europe-west6 ` リージョン（スイス、チューリッヒ）でご利用いただけるようになりました。 

##  2019 年 4 月 9 日

  * [ サーバーレス VPC アクセス ](https://cloud.google.com/appengine/docs/standard/java/connecting-vpc?hl=ja) のベータ版が利用可能になりました。サーバーレス VPC アクセスを使用すると、VPC ネットワーク内の Compute Engine VM インスタンス、Memorystore インスタンスなどの内部リソースにアプリを接続できます。 

##  2019 年 3 月 26 日

  * Java SDK がバージョン 1.9.73 に更新されました。 

##  2019 年 2 月 13 日

  * Java SDK がバージョン 1.9.72 に更新されました。 
  * Java 7 アプリはビルドできなくなりました。1 月 25 日に Java 7 アプリのデプロイがブロックされました。 

##  2019 年 1 月 25 日

  * Java 7 ランタイムでのアプリのデプロイがブロックされるようになりました。アプリが現在 Java 7 ランタイムを使用している場合は、自動的に [ Java 8 ランタイム ](https://cloud.google.com/appengine/docs/standard/java/runtime?hl=ja) に移行されます。 

##  2018 年 12 月 19 日

  * Java SDK がバージョン 1.9.71 に更新されました。 
  * ` com.google.appengine.api.search.Index ` 内の [ ` DeleteSchema ` メソッド ](https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/search?hl=ja#deleteSchema--) がサポートされるようになりました。インデックスを完全に削除するには、インデックスのドキュメントとスキーマを削除する必要があります。 

##  2018 年 12 月 6 日

  * Java SDK がバージョン 1.9.70 に更新されました。 
  * Jetty をバージョン 9.4.14.v20181114 に更新しました。 

##  2018 年 11 月 28 日

  * Java SDK がバージョン 1.9.69 に更新されました。 
  * ASM ライブラリがアップグレードされ、Java 11 バイトコードの処理が改善されます。 
  * JSP コンパイル クラスパスで ECJ（Eclipse コンパイラ）をバンドルしないようにします。 

##  2018 年 10 月 25 日

  * Java SDK がバージョン 1.9.68 に更新されました。 
  * 細かいバグを修正しました。 

##  2018 年 10 月 22 日

  * App Engine が ` asia-east2 ` リージョン（香港）でご利用いただけるようになりました。 

##  2018 年 10 月 18 日

  * Java SDK がバージョン 1.9.67 に更新されました。 
  * ` AppEngineSession.setAttribute ` で null 値がサポートされるようになり、以前は null ポインタ例外がスローされていた [ バグが修正 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2283) されます。 

##  2018 年 10 月 3 日

  * Java SDK がバージョン 1.9.66 に更新されました。 
  * Jetty をバージョン 9.4.12.v20180830 に更新しました。 

##  2018 年 9 月 19 日

**Java ランタイムに関する注意事項**

  * Java SDK がバージョン 1.9.65 に更新されました。 
  * 例外が発生すると、 ` enhance_jdos ` が失敗します。 
  * ` DatastoreType ` によって、常に高レプリケーションが返されます。 
  * ステージング オプションのデフォルトのヘルプで文法が修正されました。 
  * LocalMailService javadoc を修正しました。 
  * ` min-instances ` を ` appengine-web.xml ` で 0 に設定できます。 
  * Java 11 を使用して Java 8 ランタイムでアプリを開発およびデプロイするためのサポートが改善されました。 

##  2018 年 8 月 24 日

**Cloud Endpoints Frameworks v1 のシャットダウンが近づいています**

App Engine スタンダード環境用 Cloud Endpoints Frameworks v1 は、2017 年 8 月 2
日に非推奨になりました。このサービスは 2018 年 9 月 3 日に [ シャットダウンされる予定
](https://cloud.google.com/appengine/docs/deprecations/endpoints-v1?hl=ja)
であり、ドキュメントは削除されます。停止を回避するには、v1 アプリケーションを移行する必要があります。Endpoints Frameworks v2
へのアプリケーションの移行については、次のガイドを参照してください。

  * [ Java 移行ガイド ](https://cloud.google.com/endpoints/docs/frameworks/java/migrating?hl=ja)
  * [ Android プロジェクトの移行 ](https://cloud.google.com/endpoints/docs/frameworks/java/migrating-android?hl=ja)

##  2018 年 7 月 10 日

  * App Engine が ` us-west2 ` リージョン（ロサンゼルス）で利用できるようになりました。 

##  2018 年 7 月 2 日

` max-instances ` 設定が使用されたときに App Engine が積極的にインスタンスをシャットダウンしていた [ 自動スケーリング構成
](https://cloud.google.com/appengine/docs/standard/java/config/appref?hl=ja#scaling_elements)
におけるバグを修正しました。

##  2018 年 5 月 31 日

**Java ランタイムに関する注意事項**

  * Java SDK がバージョン 1.9.64 に更新されました。 
  * [ Java ランタイムで ` <min-instances>0</min-instances> ` がサポートされていない ](https://issuetracker.google.com/80273043?hl=ja) 問題が修正されます。 
  * \--application フラグが ` dev_appserver.py ` に追加されます。 
  * 改行を含むファイル名でのデプロイが防止されます。 
  * ` appengine-web.xml ` ファイルに設定されている環境変数がステージング プロセスに渡されず、アプリで使用できない問題が修正されます。 

##  2018 年 5 月 15 日

  * 自動スケーリング システムへのアップグレードの段階的ロールアウトが完了しました。 
    * 効率性が向上することで、全般的にインスタンス費用が削減され（多くのユーザーで最大 6% の削減）、新しいインスタンスへの最初のリクエストである __ 読み込みリクエストが最大 30% 削減されます。 
    * 新しい最大インスタンス数の設定により、スケジュールするインスタンス総数の上限を設定できるようになりました。 
    * 新しい最小インスタンス数の設定により、各アプリで実行し続けるインスタンスの最小数を指定できるようになりました。 
    * 新しいターゲット CPU 使用率設定により、レイテンシとコストのバランスを最適化できるようになりました。 
    * 新しいターゲット スループット使用率の設定により、新しいインスタンスの起動時の同時リクエスト数を最適化できるようになりました。 
    * 自動スケーリングの常駐インスタンスが廃止されました。以前は、 ` min_idle_instances ` 設定を使用すると、Cloud Console で最小アイドル状態のインスタンスが [常駐] __ としてラベル付けされ、残りのインスタンスは [ダイナミック] __ としてラベル付けされていました。新しいスケジューラでは、自動スケーリングによりすべてのインスタンスは [ダイナミック] としてラベル付けされます。 __ ただし、基本的な動作は以前の動作と同様です。 ` min_idle_instances ` を使用してウォームアップ リクエストを有効にすると、トラフィックが発生していない期間でも、少なくともその数の動的インスタンスが実行されていることがわかります。 
    * 詳細については、 [ 自動スケーリングのドキュメント ](https://cloud.google.com/appengine/docs/standard/java/config/appref?hl=ja#scaling_elements) をご覧ください。 

##  2018 年 2 月 27 日

**Java ランタイムに関する注意事項**

  * Java SDK がバージョン 1.9.63 に更新されました。 

##  2018 年 2 月 7 日

**Java ランタイムに関する注意事項**

  * Java SDK がバージョン 1.9.62 に更新されました。 
  * デプロイ時に Java 8 Servlet 3.1 のクイックスタート処理が失敗していた [ Cloud SDK の問題 ](https://issuetracker.google.com/issues/72808542?hl=ja) を修正しました。 

##  2018 年 1 月 22 日

**Java ランタイムに関する注意事項**

  * Java SDK バージョン 1.9.61 のパッチが公開されました。以前にこのバージョンをインストールしていた場合は、SDK を [ ダウンロード ](https://cloud.google.com/appengine/docs/standard/java/download?hl=ja) して再インストールしてください。 

##  2018 年 1 月 18 日

**Java ランタイムに関する注意事項**

  * Java SDK がバージョン 1.9.61 に更新されました。 

##  2017 年 12 月 20 日

**Java ランタイムに関する注意事項**

  * Java SDK がバージョン 1.9.60 に更新されました。 
  * Java 7 アプリケーションのデプロイ時またはローカル実行時に非推奨警告を追加しました。 
  * appcfg のフラグ use_google_application_default_credentials を使用したときに Google Compute Engine VM で正しく動作しなかったバグを修正しました。 
  * ` appcfg ` コマンドに ` enable_new_staging_defaults ` という新しいフラグを追加しました。これは、Java アプリケーションのデプロイフラグでより適切なデフォルト値を指定できるようにして、将来の Cloud SDK 統合に備えるためのフラグです。 
  * ランタイムが Java 8 の場合に、ローカル開発サーバーでデフォルトの文字エンコードを ` UTF-8 ` に変更しました。また、 ` appengine.file.encoding ` システム プロパティを使用して、文字エンコードを明示的に設定できるようになります。これらの変更によって、本番環境で起こることを模倣できます。 
  * [ Windows 上で実行されている開発サーバーのフィルタが一部のサーブレット URL を解析できない ](https://issuetracker.google.com/63595917?hl=ja) という問題を修正しました。 

##  2017 年 12 月 14 日

  * IAM の役割とサービス アカウントを使用したアプリのデプロイに関するアクセス制御のドキュメントで、次の項目を改善しました。 

    * [ App Engine の事前定義された役割 ](https://cloud.google.com/appengine/docs/standard/java/access-control?hl=ja#predefined_app_engine_roles)
    * [ IAM の役割を使用したデプロイ ](https://cloud.google.com/appengine/docs/standard/java/granting-project-access?hl=ja#deploying_using_iam_roles)
    * [ 権限の要求 ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=ja#required_permissions)

**Java ランタイムに関する注意事項**

  * Java SDK がバージョン 1.9.59 に更新されました。 
  * ローカル開発サーバーを更新して、 ` url-stream-handler ` 構成パラメータがデフォルトで ` native ` に設定されるようになりました。この変更は、本番環境での Java 8 ランタイムの動作を反映しています。 ` url-stream-handler ` の詳細については、 [ ` appengine-web.xml ` ](https://cloud.google.com/appengine/docs/standard/java/config/appref?hl=ja#url-stream-handler) のリファレンスをご覧ください。 
  * ローカル開発サーバーで Java 8 ランタイムと Endpoints Framework Gradle Plugin を使用している場合に発生する [ ` NoClassDefFoundError ` ](https://github.com/GoogleCloudPlatform/endpoints-framework-gradle-plugin/issues/53) エラーを修正しました。 
  * コロン文字が含まれているサーブレット URL での問題を解決するように、 [ ローカル開発サーバーのバグ ](https://issuetracker.google.com/63595917?hl=ja) を修正しました。 

##  2017 年 10 月 31 日

  * App Engine が、 ` asia-south1 ` リージョン（インドのムンバイ）で使用できるようになりました。 

##  2017 年 10 月 11 日

  * [ App Engine ファイアウォール ](https://cloud.google.com/appengine/docs/standard/java/creating-firewalls?hl=ja) の一般提供を発表しました。 

**Java ランタイムに関する注意事項**

  * Java SDK がバージョン 1.9.58 に更新されました。 
  * App Engine フレキシブル環境でのアノテーションの [ Jetty クイックスタート モジュール ](https://webtide.com/jetty-9-quick-start/) を修正しました。 
  * 特定の文字によって URL 解析で問題が発生していた、 [ ローカル開発サーバーのバグ ](https://issuetracker.google.com/63595917?hl=ja) を修正しました。 
  * JDK 9 を使用している場合は、Jetty 9 JSP コンパイラで 1.8 ターゲットを使用します。 

##  2017 年 9 月 25 日

**Java ランタイムに関する注意事項**

  * [ Java 8 ランタイムが一般提供されるようになりました ](https://cloudplatform.googleblog.com/2017/09/Java-8-on-App-Engine-Standard-environment-is-now-generally-available.html) 。 
  * Java SDK がバージョン 1.9.57 に更新されました。 
  * ローカル開発サーバーで、パスでの ` -Xbootclasspath/p ` と ` google_sql.jar ` がサポートされなくなります。 
  * Java 8 ランタイムで、 ` module-info.class ` が含まれている JDK9 JAR がサポートされなくなりました。 
  * Cloud Endpoints v1 が Java 8 ランタイムでサポートされなくなりました。 
  * Java 8 ランタイムで Cloud Endpoints v2 を使用している場合、ローカル開発サーバーでの ` NoClassDefFoundError ` 例外が修正されました。 

##  2017 年 9 月 18 日

**Java ランタイムに関する注意事項**

  * ` com.google.cloud.tools:appengine-gradle-plugin ` のリリース 1.3.3 
  * ローカル開発サーバーはログを ` dev_appserver.out ` に出力するようになりました。（ [ #156 ](https://github.com/GoogleCloudPlatform/app-gradle-plugin/pull/156) ） 
  * クリーンでない再ビルドで ` datastore-indexes-auto.xml ` が削除されなくなりました。（ [ #165 ](https://github.com/GoogleCloudPlatform/app-gradle-plugin/issues/165) ） 
  * explodeWar タスクで copy ではなく sync を使用するように切り替えました。（ [ #162 ](https://github.com/GoogleCloudPlatform/app-gradle-plugin/pull/162) ） 

##  2017 年 9 月 13 日

  * マネージド証明書を使用して、カスタム ドメインに SSL を追加できるようになりました。アプリケーションにカスタム ドメインをマッピングすると、App Engine によって SSL 証明書が自動的にプロビジョニングされ、証明書の期限が切れる前に更新処理が行われます。また、カスタム ドメインを削除すると、証明書が取り消されます。マネージド証明書はベータ版です。詳細については、 [ SSL によるカスタム ドメインの保護 ](https://cloud.google.com/appengine/docs/standard/java/securing-custom-domains-with-ssl?hl=ja) をご覧ください。 

  * 既存のドメイン マッピングと SSL 証明書がある場合、変わることなく想定どおりに機能します。 [ マネージド SSL 証明書にアップグレード ](https://cloud.google.com/appengine/docs/standard/java/securing-custom-domains-with-ssl?hl=ja#updating_to_managed_ssl_certificates) することもできます。 

  * [ カスタム ドメインのマッピング ](https://cloud.google.com/appengine/docs/standard/java/mapping-custom-domains?hl=ja) に使用する ` gcloud ` コマンドと Admin API メソッドが一般提供されるようになりました。対象のレポートには、 [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains?hl=ja) および [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=ja) が含まれます。ただし、マネージド SSL 証明書を使用する場合は、 [ SSL によるカスタム ドメインの保護 ](https://cloud.google.com/appengine/docs/standard/java/securing-custom-domains-with-ssl?hl=ja) で指定されているベータ版のコマンドとメソッドを使用してください。 

##  2017 年 9 月 11 日

**Java ランタイムに関する注意事項**

  * Java SDK がバージョン 1.9.56 に更新されました。 

  * App Engine スタンダード環境 API と互換性を持つフレキシブル ランタイム（ ` compat ` ランタイム）の場合、この SDK バージョンには ` appengine-web.xml ` ファイル構成への更新が含まれており、 ` subnetwork_name ` 、 ` session_affinity ` 、および更新された実行状況および準備状況のヘルスチェックに関するサポートが追加されています。 

  * Google App Engine SDK での環境変数 ` GAE_RUNTIME ` （ ` java 7 ` または ` java 8 ` ）および GAE_ENV（ ` standard ` ）に対するサポートが追加されました。 

##  2017 年 9 月 5 日

  * App Engine が ` southamerica-east1 ` リージョン（ブラジルのサンパウロ）で使用できるようになりました。 

  * Java SDK がバージョン 1.9.55 に更新されました。 

  * アプリが Java 8 / Jetty 9 を使用していても、SDK に対してセキュリティ マネージャーが使用されていたバグを修正しました。 

  * Java 8 で [ appstats ](https://cloud.google.com/appengine/docs/standard/java/tools/appstats?hl=ja) フィルタを使用すると、エラー メッセージが出力されます。 

  * [ 問題 63123716: Google Java HTTP クライアントを使用した URL 取得が開発サーバーで機能しない ](https://issuetracker.google.com/issues/63123716?hl=ja) を修正しました。 

##  2017 年 8 月 1 日

  * App Engine が ` europe-west3 ` リージョン（ドイツのフランクフルト）で使用できるようになりました。 

##  2017 年 7 月 18 日

  * App Engine が、 ` australia-southeast1 ` リージョン（オーストラリアのシドニー）で使用できるようになりました。 

##  2017 年 6 月 28 日

**新機能**

  * [ App Engine スタンダード環境用の Java 8 ランタイム ](https://cloud.google.com/appengine/docs/standard/java/runtime-java8?hl=ja) はベータ版です。 
  * ` <runtime>java8</runtime> ` が ` appengine-web.xml ` ファイルに追加されます。 
  * OpenJDK 8、Servlet 3.1、Jetty 9.3 に基づいています。 
  * App Engine 上の Java 7 および組み込み App Engine API との機能互換性があります。 
  * [ Java 用 Google Cloud クライアント ライブラリ ](https://googleapis.github.io/google-cloud-java/google-cloud-clients/) からアクセス可能な Google Cloud ベースの API をすべてサポートします。 
  * 公開 Java 8 API がすべて使用可能であり、 [ クラスのホワイトリスト ](https://cloud.google.com/appengine/docs/standard/java/jrewhitelist?hl=ja) が削除されました。 
  * [ Java セキュリティ マネージャー ](https://docs.oracle.com/javase/7/docs/api/java/lang/SecurityManager.html) が、Java 8 ランタイムで削除されました。 
  * 読み取り専用の [ GCP メタデータ サーバー ](https://cloud.google.com/compute/docs/storing-retrieving-metadata?hl=ja) プロジェクトとサービス アカウントの値をサポートしています。 
  * Java SDK 1.9.54 では Java 8 ランタイムがサポートされています。 

**Java 8 ランタイムの既知の制限事項**

  * ` /tmp ` ディレクトリは書き込み可能です。 ` /tmp ` 内のファイルは、インスタンスに割り当てられているメモリを消費します。 
  * Async Servlet 3.1 はサポートされていません。 
  * WebSocket はサポートされていません。 
  * Jetty 9 の構成は変更できません。 
  * App Engine API は、ウェブ リクエストを処理するスレッド、または [ ThreadManager ](https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/ThreadManager?hl=ja) を使用して作成されたスレッドからのみ呼び出すことができます。 
  * ` WEB-INF/appengine-web.xml ` を構成に使用する必要があります。現在、 ` app.yaml ` はサポートされていません。 
  * デプロイには、Maven、Gradle、または IDE のプラグインを使用する必要があります。 
  * たとえば、 ` ExecutorService pool = Executors.newCachedThreadPool(ThreadManager.currentRequestThreadFactory()) ` などを使用してスレッドプールを作成し、現在のリクエストが終了する前に ` pool.shutdown() ` を使用してそれを明示的にシャットダウンする必要があるとします。 
  * 以前は、単に ` org.joda.Instant ` が意図されていた場合に、 ` com.google.appengine.repackaged.org.joda.Instant ` のようなサードパーティのクラスを不注意で参照する可能性がありました。vendoring スキームが変更されたため、そのようなコードは動作しなくなりました。 
  * ネイティブ ネットワーク API（ ` HttpURLConnection ` など）を課金アプリケーションに対して有効化できます。ただし、無料のアプリケーションで使用すると例外（ ` java.net.SocketTimeoutException ` または ` java.io.IOException ` ）が返されます。無料のアプリケーションは ` *.googleapis.com ` と ` accounts.google.com ` にアクセスでき、URLFetch サービスを使用するように [ 構成する ](https://cloud.google.com/appengine/docs/standard/java/config/appref?hl=ja#url-stream-handler) こともできます。 
  * ` executor ` では ` google-cloud-java ` API をラップする必要があります。 [ Pub/Sub パブリッシャーが Executor 経由で送信されない場合にハングする ](https://github.com/googleapis/google-cloud-java/issues/2150) をご覧ください。 
  * Cloud Endpoints は v1 から v2 に [ 移行 ](https://cloud.google.com/endpoints/docs/frameworks/legacy/v1/java/migrating?hl=ja) する必要があります。 
  * Channels API および XMPP API はサポートされていません。 
  * ` appengine-labs-api.jar ` API はサポートされていないため、 [ Java 用 Appstats ](https://cloud.google.com/appengine/docs/standard/java/tools/appstats?hl=ja) はサポートされません。 
  * Java 7 ランタイムの場合と同様に、Java 8 ランタイムのデフォルトでは、URL 取得トランスポートではなく、ネイティブ Java HTTP(S) トランスポートが使用されます。詳細については、 [ url-stream-handler ](https://cloud.google.com/appengine/docs/standard/java/config/appref?hl=ja#url-stream-handler) をご覧ください。 

##  2017 年 6 月 15 日

  * Java SDK がバージョン 1.9.54 に更新されました。 

##  2017 年 6 月 6 日

  * App Engine が ` europe-west2 ` リージョン（ロンドン）で使用できるようになりました。 
  * Admin API と ` gcloud ` コマンドライン ツールのベータ版レベルの機能を使用して、 [ カスタム ドメインと SSL 証明書の作成と管理 ](https://cloud.google.com/appengine/docs/standard/java/mapping-custom-domains?hl=ja) ができるようになりました。 

##  2017 年 5 月 9 日

  * App Engine が ` us-east4 ` リージョン（北バージニア）で使用できるようになりました。 
  * Java SDK がバージョン 1.9.53 に更新されました。 
  * JSP タグライブラリの使用量が Java 8 SpringBoot アプリケーションで機能しなかった Java SDK の問題を修正しました。 

##  2017 年 5 月 8 日

  * ` com.google.cloud.tools:appengine-(gradle/maven)-plugin ` のリリース 1.3.1 
  * 開発サーバー上でローカルに実行すると、 ` appengine-web.xml ` 構成ファイルから環境変数が読み込まれ、インクルードされるようになりました。 
  * Maven / Gradle の構成ファイルを使用して追加の環境変数をインクルードするための ` environment ` パラメータを公開しました。 

##  2017 年 5 月 2 日

  * ` com.google.cloud.tools.appengine-(gradle/maven)-plugin ` のリリース 1.3.0 
  * デフォルトの開発サーバーは Dev App Server v1（Java モジュールのみ） 
  * 構成デプロイのための新しい Gradle タスク: ` appengineDeployCron ` 、 ` appengineDeployDispatch ` 、 ` appengineDeployDos ` 、 ` appengineDeployIndex ` 、 ` appengineDeployQueue `
  * 構成デプロイのための新しい Maven ゴール: ` appengine:deployCron ` 、 ` appengine:deployDispatch ` 、 ` appengine:deployDos ` 、 ` appengine:deployIndex ` 、 ` appengine:deployQueue `
  * Maven/Gradle によるフレキシブル アプリのステージングでは、 ` app.yaml ` のみがビルド / ターゲット ディレクトリにコピーされます。構成ファイルのデプロイには ` src/main/appengine ` を使用します。 
  * Gradle の exploded アプリのデフォルト ディレクトリが ` build/exploded-app ` から ` build/exploded-<module-name> ` に変更されました。 

##  2017 年 4 月 19 日

  * Java SDK がバージョン 1.9.52 に更新されました。 
  * Java 8 スタンダード環境のアルファ版ランタイムのサポートを改善しました。 
  * [ Java 8 ](https://docs.google.com/a/google.com/forms/d/1MDzykTWp77YzRgFs5R6ONOuKWYnKEhfy5VhSJYbDvmo/viewform?hl=ja) アルファ版スタンダード環境のランタイムで Jetty 9.3.18 にアップグレードしました。 
  * 最新の Jetty 機能を使用して Java 8 SpringBoot アプリケーションがより適切にサポートされるように、 ` quickstart-web.xml ` 処理が更新されます。 
  * 同じ名前で終わるディレクトリ名に置かれている複数のサービスのローカル実行を修正しました。 
  * SpringBoot アプリケーションの起動時に発生していた SDK エラーを修正しました。 

##  2017 年 3 月 29 日

  * Java SDK がバージョン 1.9.51 に更新されました。 

  * ` web.xml ` ファイルが含まれていない [ Java 8 アルファ版 ](https://docs.google.com/a/google.com/forms/d/1MDzykTWp77YzRgFs5R6ONOuKWYnKEhfy5VhSJYbDvmo/viewform?hl=ja) アプリケーションを [ ローカル開発サーバー ](https://cloud.google.com/appengine/docs/standard/java/tools/using-local-server?hl=ja) で実行できるようになりました。 

##  2017 年 3 月 21 日

  * ` com.google.cloud.tools:appengine-gradle-plugin ` が 1.1.1 に更新されました。 
  * マルチ モジュールの Gradle プロジェクトでフレキシブル環境のデプロイが失敗していた [ 問題 108 ](https://github.com/GoogleCloudPlatform/app-gradle-plugin/issues/108) を修正しました。 

##  2017 年 3 月 6 日

  * ` com.google.cloud.tools:appengine-maven-plugin ` が 1.2.1 に更新されました。 
  * カスタム デプロイ可能なパラメータが余分なディレクトリに誤って追加されていた [ 問題 144 ](https://github.com/GoogleCloudPlatform/app-maven-plugin/issues/144) を修正しました。 

##  2017 年 3 月 1 日

  * Java SDK がバージョン 1.9.50 に更新されました。 

  * ローカル開発サーバーで複数のサービスをテストするためのサポートが追加されました。 

  * Java 7 ランタイムを使用していて、サーブレット 3.1 スキーマを指定している ` web.xml ` をインクルードしているアプリに対して web.xml ファイルを生成しなくなりました。 

  * アプリケーションに JSP がない場合でも、Java クラスファイルを .zip ファイルにパッケージ化するようになりました。 

##  2017 年 2 月 17 日

App Engine 用の ` com.google.cloud.tools ` [ Maven
](https://cloud.google.com/appengine/docs/java/tools/maven-reference?hl=ja)
（1.2.0）プラグインと [ Gradle
](https://cloud.google.com/appengine/docs/java/tools/gradle-reference?hl=ja)
（1.1.0）プラグインが更新されました。

  * 起動時にローカル データストアをクリアするための ` clearDatastore ` フラグを追加しました。 
  * ソース コンテキスト タスク / 目標を追加しました。 

##  2017 年 1 月 30 日

  * Java SDK がバージョン 1.9.49 に更新されました。 

##  2016 年 12 月 1 日

  * Java SDK がバージョン 1.9.48 に更新されました。 

##  2016 年 11 月 3 日

  * バージョン 1.9.45 はスキップされました。 

  * Java Runtime と SDK がバージョン 1.9.46 に更新されました。 

##  2016 年 10 月 27 日

  * Channel サービスと XMPP サービスが [ 非推奨 ](https://cloud.google.com/appengine/docs/deprecations?hl=ja) になりました。これらのサービスは 2017 年 10 月 31 日に廃止されます。 

##  2016 年 10 月 17 日

  * Java Runtime と SDK がバージョン 1.9.44 に更新されました。 

  * Blobstore の blob が Cloud Storage バケットに保存されるときに設定される新しい BlobInfo プロパティが追加されました。 

##  2016 年 8 月 1 日

**Admin API に関する注意事項**

  * [ Admin API ](https://cloud.google.com/appengine/docs/admin-api?hl=ja) のバージョン 1 の正式版がリリースされました。 

##  2016 年 8 月 1 日 - バージョン 1.9.42

  * バージョン 1.9.41 はスキップされました。 

  * バージョン 1.9.42 には全般的なバグの修正と改善が含まれています。 

##  2016 年 7 月 21 日

**Java 8 ランタイムに関する注意事項**

  * App Engine ダッシュボードで誤って報告された可能性のあるメモリ使用量（インスタンス「平均メモリ」と「メモリ使用量」のグラフの下の値）を修正しました。この問題は請求には影響しません。 

##  2016 年 7 月 18 日 - バージョン 1.9.40

  * バージョン 1.9.39 はスキップされました。 

  * LeaseTasksByTag のリクエストは 1 秒間に 25 個のリクエストに制限されます。 

  * App Engine ダッシュボードに表示されるサーバーエラーとクライアント エラーに、URL ごとのステータス エラーがより正確に反映されるようになりました。 

  * Cloud Console の [ App Engine チュートリアル ](https://console.cloud.google.com/start/appengine?hl=ja) が新しくなりました。使用する言語を選択して、コンソール内で直接インタラクティブなチュートリアルを起動できます。 

  * cron タスクの最大制限が 250 に増えました。 

**Java ランタイムに関する注意事項**

  * すべての Java アプリケーションが 64 ビット版の Java ランタイムを使用するように、自動的にアップグレードされます。このローリング アップグレードは 2016 年 7 月 20 日に開始されます。 

##  2016 年 7 月 1 日

**Cloud Datastore**

  * 新しい [ Cloud Datastore の料金 ](https://cloud.google.com/appengine/pricing?hl=ja#costs-for-datastore-calls) が有効になりました。 

##  2016 年 5 月 25 日 - バージョン 1.9.38

  * ドキュメントに記載されているように、許可範囲（80～90、440～450、1024～65535）外のポートへのリクエストに対して URL 取得によって返されるエラーで、常に ` INVALID_URL ` を返すようになりました。 

**Cloud Datastore**

  * クロスグループ トランザクションを commit する場合、新しいエンティティまたは更新されたエンティティに対して返されるバージョン番号がすべて同じになりました。以前の動作では、クロスグループ トランザクションの一部として commit された同じグループ内のエンティティには同じバージョン番号が返されましたが、別のグループ内のエンティティには別のバージョン番号が返されることがありました。今回の変更によって、クロスグループ トランザクションの一部として commit されたすべての新しいエンティティと更新されたエンティティは、エンティティ グループに関係なく同じバージョン番号を持つことになります。以前と同様、更新されないエンティティには、新しいバージョン番号は付与されません。 

##  2016 年 5 月 4 日 - バージョン 1.9.37

全般的なバグの修正と改善が含まれています。

##  2016 年 5 月 2 日

**App Engine フレキシブル環境**

  * App Engine フレキシブル環境で [ Ruby ランタイム ](https://cloud.google.com/appengine/docs/flexible/ruby?hl=ja) が使用できるようになりました。 

##  2016 年 4 月 18 日 - バージョン 1.9.36

ユーザーのリクエストにお応えして、IAM の役割とグループ展開のサポートにおいて、App Engine に App Engine Users API
が加わりました。これは、プロジェクトのオーナー、編集者、または閲覧者、あるいは App Engine
の管理者であるユーザーが役割を直接またはグループのメンバーによって与えられているかどうかに関係なく、Users API
によって「管理者」とみなされることを意味します。このリリースでは、「OverQuota」例外タイプに関連するエラー
メッセージに、可能であればエラーの詳細が含まれるようになりました。

**Java ランタイムに関する注意事項**

  * Google はメールサービスの割り当ての増加リクエストを受け入れなくなりました。代わりに、 [ Sendgrid ](https://cloud.google.com/appengine/docs/standard/java/mail/sendgrid?hl=ja) を使用してください。 

##  2016 年 3 月 24 日 - バージョン 1.9.35

  * App Engine マネージド VM の名前が [ App Engine フレキシブル環境 ](https://cloud.google.com/appengine/docs/flexible?hl=ja) に変更されました。 
  * トレースのタイムスタンプをログのタイムスタンプに合わせて修正しました。 

**Java ランタイムに関する注意事項**

  * このリリースには、新しい Java SDK が含まれていません。Java ユーザーは引き続き 1.9.34 SDK を使用する必要があります。 

##  2016 年 3 月 16 日

**Java ランタイムに関する注意事項**

  * Java SDK のバージョン 1.9.34 を使用できるようになりました。 

##  2016 年 3 月 4 日 - バージョン 1.9.34

  * 有料アプリケーションの URL 取得のデフォルトの割り当てが増えました。詳細については、 [ 割り当てページ ](https://cloud.google.com/appengine/docs/quotas?hl=ja#UrlFetch) をご覧ください。 

**Java ランタイムに関する注意事項**

  * このリリースには、新しい Java SDK が含まれていません。Java ユーザーは引き続き 1.9.32 SDK を使用する必要があります。 

##  2016 年 2 月 17 日 - バージョン 1.9.33

  * URL パス /form が使用可能になり、アプリケーションに転送できるようになりました。以前は、このパスはブロックされていました。 

**Java ランタイムに関する注意事項**

  * このリリースには、新しい Java SDK が含まれていません。Java ユーザーは引き続き 1.9.32 SDK を使用する必要があります。 

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

**Java ランタイムに関する注意事項**

  * Datastore に対する低レベル API ` Transaction.rollback() ` の例外処理が向上しました。トランザクションに関連付けられたオペレーションが失敗した場合に、例外の代わりに、 ` INFO ` ログメッセージが生成されます。 

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

2015 年 7 月 14 日に非推奨になった Prospective Search API が既存のユーザーだけに制限されるようになりました。これは
2015 年 12 月 1 日に完全に停止されます。* 検索クエリでの Geo フィルタリングの精度が向上しました。

**Java ランタイムに関する注意事項**

  * Java DevAppServer の Files API が無効になりました。 

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

**Java ランタイムに関する注意事項**

  * Java の URLFetch API はデフォルトの取得期限を指定するプロパティを取得します。 ` appengine.api.urlfetch.defaultDeadline ` は、appengine-web.xml で Java のデフォルトの URLFetch タイムアウトを指定するために使用できる秒単位の浮動小数点数です。 

##  2015 年 8 月 14 日 - バージョン 1.9.25

  * PyAMF バージョン 0.7.2（ベータ版）が追加されました。 
  * 管理コンソールのメニューが Cloud Console にリダイレクトされるようになりました。管理ログなどの一部のサービスは、引き続き管理コンソールで使用できます。 
  * データストアで、プロパティが空白のリストを表現できるようになりました。 
  * retry_limit がゼロに構成されたキュー内の失敗したタスクは再試行されません。 

