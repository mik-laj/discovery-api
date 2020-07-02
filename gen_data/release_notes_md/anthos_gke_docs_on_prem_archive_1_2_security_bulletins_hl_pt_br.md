Você está visualizando a documentação de uma versão anterior do GKE On-Prem. [
Veja a documentação mais recente
](https://cloud.google.com/anthos/gke/docs/on-prem/?hl=pt-br) .

#  Boletins de segurança

Todos os boletins de segurança do Anthos GKE On-Prem são descritos neste
tópico.

Geralmente, as vulnerabilidades são mantidas sob sigilo e não podem ser
divulgadas até que as partes afetadas tenham a oportunidade de solucioná-las.
Nesses casos, as [ Notas de lançamento
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/release-
notes?hl=pt-br) do GKE On-Prem mencionarão "atualizações de segurança" até que
a divulgação seja liberada. No momento da liberação, as notas serão
atualizadas para indicar a vulnerabilidade solucionada pelo patch.

**Observação:** se você executar cargas de trabalho de vários locatários no
GKE On-Prem, preste atenção nesses boletins. Geralmente, elas costumam ser
mais impactadas por essas vulnerabilidades. Para ver uma descrição técnica dos
limites de segurança no GKE On-Prem e como isso afeta as cargas de trabalho,
consulte [ Isolamento em camadas diferentes da pilha do Kubernetes
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Para receber os boletins de segurança mais recentes, adicione o URL desta
página ao seu [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  16 de outubro de 2019

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
Uma vulnerabilidade foi descoberta no Kubernetes recentemente, descrita na [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) . Ela possibilita que qualquer usuário
autorizado a fazer solicitações POST execute um ataque remoto de negação de
serviço em um servidor da API Kubernetes. O Comitê de Segurança de Produto
(PSC, na sigla em inglês) do Kubernetes divulgou informações adicionais sobre
essa vulnerabilidade, que podem ser encontradas [ aqui
](https://groups.google.com/forum/?hl=pt-br#!topic/kubernetes-security-
announce/jk8polzSUxs) .

É possível reduzir essa vulnerabilidade limitando os clientes que têm acesso à
rede dos servidores da API Kubernetes.

######  O que fazer?

Recomendamos fazer [ upgrade do cluster
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/how-
to/upgrading-clusters?hl=pt-br) para uma versão de patch com a correção assim
que ela estiver disponível.

As versões de patch com a correção estão listadas a seguir:

  * Anthos 1.1.1, que executa o Kubernetes versão 1.13.7-gke.30 

######  Qual vulnerabilidade é corrigida pelo patch?

O patch reduz a seguinte vulnerabilidade: [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) .

|

Alta

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
##  23 de agosto de 2019

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
Descobrimos e eliminamos uma vulnerabilidade em que o proxy RBAC usado para
proteger os endpoints de monitoramento não autorizou corretamente os usuários.
Como resultado, as métricas de determinados componentes estão disponíveis para
usuários não autorizados dentro da rede de cluster interna. Os seguintes
componentes foram afetados:

  * ` etcd `
  * ` etcd-events `
  * ` kube-apiserver `
  * ` kube-controller-manager `
  * ` kube-scheduler `
  * ` node-exporter `
  * ` kube-state-metrics `
  * ` prometheus `
  * ` alertmanager `

######  O que fazer?

Recomendamos que você [ faça upgrade
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/how-
to/upgrading-clusters?hl=pt-br) dos clusters para a versão [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=pt-br#gkectl_latest) , que inclui o patch dessa
vulnerabilidade, o mais rápido possível.

|

Média

|

[ Versões do Anthos GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=pt-br#gkectl_latest)  
  
##  22 de agosto de 2019

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
Recentemente, o Kubernetes descobriu uma vulnerabilidade, a [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) , que
possibilita que instâncias de [ recursos personalizados
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) com escopo no cluster sejam usadas como se fossem objetos de
namespaces existentes em todos os namespaces. Isso significa que contas de
usuários e de serviço com permissões apenas do RBAC de nível namespace podem
interagir com recursos personalizados com escopo no cluster. A exploração
dessa vulnerabilidade exige que o invasor tenha privilégios para acessar o
recurso no namespace.

######  O que fazer?

Recomendamos que você [ faça upgrade
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/how-
to/upgrading-clusters?hl=pt-br) dos clusters para a versão [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=pt-br#gkectl_latest) , que inclui o patch dessa
vulnerabilidade, o mais rápido possível.

######  Qual vulnerabilidade é corrigida pelo patch?

O patch reduz a seguinte vulnerabilidade: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Média

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

