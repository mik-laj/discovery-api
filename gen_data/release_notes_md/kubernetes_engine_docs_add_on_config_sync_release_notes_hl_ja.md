#  リリースノート

このページには、Config Sync
に関する更新内容が記載されています。このページをチェックして、新機能や更新された機能、バグ修正、既知の問題、非推奨となった機能に関するお知らせを確認してください。

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/kubernetes-engine-add-on-config-
sync-release-notes.xml ` を直接追加します。

##  1.2.0

Config Sync v1.2.0 は一般提供され、本番環境で使用できます。これは、プロダクトの最初のバージョンです。

###  既知の問題

**ISSUE:**

リポジトリに [ APIService ](https://kubernetes.io/docs/concepts/extend-
kubernetes/api-extension) を追加すると、Config Sync
の状態に問題が発生し、「[KNV2002](/kubernetes-engine/docs/add-on/config-
sync/reference/errors#knv2002): failed to get server resources: unable to
retrieve the complete list of server APIs.」というエラー
メッセージが表示されます。この問題は、このリポジトリから同期する新規クラスタと既存クラスタの両方に影響します。問題を解決するには:

* ` kubectl get pods -n config-management-system ` を使用して、 ` git-importer ` ポッドと ` syncer ` ポッドの名前を検索します。 
* これらの名前をコピーして、 ` kubectl delete -n config-management-system pods git-importer-xxxx-xxxx syncer-xxxx-xxxx ` でポッドを再起動します。 
* この手順は、クラスタごとに 1 回行う必要があります。 
クラスタのポッドを再起動すると、同期が正常な状態に戻ります。

**ISSUE:**

CRD（カスタム リソース定義）がリポジトリのローカル クローンに存在しても、クラスタと同期されていないと、 ` nomos view ` が CRD
の解析に失敗する場合があります。

この問題を回避するには、 ` nomos view ` ではなく [ ` nomos hydrate `
](https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/how-
to/nomos-command?hl=ja#hydrate) を使用します。

