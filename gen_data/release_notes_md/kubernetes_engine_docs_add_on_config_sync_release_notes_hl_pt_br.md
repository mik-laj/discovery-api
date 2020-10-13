#  Notas da versão

Nesta página, você encontra as atualizações de produção do Config Sync.
Acesse-a para se informar sobre avisos de recursos novos ou atualizados,
correções de bugs, problemas conhecidos e funcionalidades obsoletas.

É possível ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas da versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt_br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/kubernetes-engine-add-
on-config-sync-release-notes.xml `

##  1.2.0

Geralmente, o Config Sync v1.2.0 está disponível para uso na produção. Esta é
a primeira versão do produto.

###  Problemas conhecidos

**ISSUE:**

[ Adicionar um APIService ](https://kubernetes.io/docs/concepts/extend-
kubernetes/api-extension) (em inglês) ao repo gera um estado inválido para o
Config Syng. É exibida esta mensagem de erro: "[KNV2002](/kubernetes-
engine/docs/add-on/config-sync/reference/errors#knv2002): failed to get server
resources: unable to retrieve the complete list of server APIs." Esse problema
afeta a sincronização dos clusters novos e atuais desse repo. Para corrigir o
problema:

* use ` kubectl get pods -n config-management-system ` para encontrar o nome dos pods ` git-importer ` e ` syncer ` ; 
* copie esses nomes e reinicie os pods com ` kubectl delete -n config-management-system pods git-importer-xxxx-xxxx syncer-xxxx-xxxx ` ; 
* é necessário realizar essas etapas para cada cluster. 
Depois que os pods de um cluster forem reiniciados, a sincronização voltará ao
normal.

**ISSUE:**

` nomos view ` pode falhar ao analisar as definições personalizadas de
recursos (CRDs, na sigla em inglês) que estão no clone local do repo, mas que
ainda não foram sincronizadas com um cluster.

Para solucionar esse problema, use [ ` nomos hydrate `
](https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/how-
to/nomos-command?hl=pt_br#hydrate) em vez de ` nomos view ` .

