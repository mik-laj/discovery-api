You are viewing documentation for a previous version of Anthos GKE on-prem. [
View the latest documentation ](https://cloud.google.com/anthos/gke/docs/on-
prem?hl=pt-br) .

#  Boletins de segurança

Todos os boletins de segurança do Anthos GKE On-Prem (GKE On-Prem) são
descritos neste tópico.

Geralmente, as vulnerabilidades são mantidas sob sigilo e não podem ser
divulgadas até que as partes afetadas tenham a oportunidade de solucioná-las.
Nesses casos, as [ notas de lançamento
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.3/release-
notes?hl=pt-br) do GKE On-Prem se referirão a "atualizações de segurança" até
o levantamento do embargo. No momento da liberação, as notas serão atualizadas
para indicar a vulnerabilidade solucionada pelo patch.

**Observação:** esses boletins são especialmente importantes para quem tem
cargas de trabalho com vários locatários no GKE On-Prem. Geralmente, elas
costumam ser mais impactadas por essas vulnerabilidades. Para uma descrição
técnica dos limites de segurança no GKE On-Prem e como eles afetam as cargas
de trabalho, consulte [ Isolamento em níveis diferentes da pilha do Kubernetes
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) (em inglês).

Para receber os boletins de segurança mais recentes, adicione o URL desta
página ao seu [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  GCP-2020-007

**Publicado:** 01/06/2020  
Descrição  |  Gravidade  |  Observações  
---|---|---  
  
A vulnerabilidade de falsificação de solicitação do lado do servidor (SSRF, na
sigla em inglês) [ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555) foi descoberta recentemente no Kubernetes.
Ela permite que determinados usuários autorizados vazem até 500 bytes de
informações confidenciais da rede do host do plano de controle. O plano de
controle do Google Kubernetes Engine (GKE) usa os controladores do Kubernetes
e, portanto, foi afetado por essa vulnerabilidade. Recomendamos fazer upgrade
do plano de controle para a versão mais recente do patch, conforme detalhamos
a seguir. Não é necessário fazer upgrade do nó.  

####  O que fazer?

As versões do Anthos GKE On-Prem (GKE On-Prem) a seguir ou mais recentes
contêm a correção dessa vulnerabilidade:

  * Anthos 1.3.0 

Se você estiver usando uma versão anterior, [ faça upgrade do cluster atual
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.3/how-
to/upgrading?hl=pt-br) para uma versão que contenha a correção.

####  Qual vulnerabilidade é corrigida por esse patch?

Esses patches mitigam a vulnerabilidade CVE-2020-8555. Ela é classificada como
uma vulnerabilidade de gravidade média para o GKE, porque era difícil explorá-
la já que havia várias medidas de aumento de proteção do plano de controle.

Um invasor com permissões para criar um pod com determinados tipos de volume
integrado (GlusterFS, Quobyte, StorageFS e ScaleIO) ou permissões para criar
um StorageClass pode fazer com que ` kube-controller-manager ` crie
solicitações ` GET ` ou ` POST ` _sem_ um corpo de solicitação controlado pelo
invasor na rede do host do mestre. Esses tipos de volume raramente são usados
no GKE, então uma nova utilização deles pode ser um sinal útil para detectar
problemas.

Combinado com um meio de vazar os resultados de ` GET/POST ` para o invasor,
como por meio de registros, essa vulnerabilidade pode levar à divulgação de
informações confidenciais. Atualizamos os drivers de armazenamento em questão
para remover a possibilidade desses vazamentos acontecerem.

|

Média

|

[ CVE-2020-8555 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**Publicado:** 01/06/2020  
Descrição  |  Gravidade  |  Observações  
---|---|---  
  
O Kubernetes divulgou uma [ vulnerabilidade
](https://github.com/kubernetes/kubernetes/issues/91507) que permite que um
contêiner com privilégios redirecione o tráfego do nó para outro contêiner. O
tráfego TLS/SSH mútuo, como entre o kubelet e o servidor da API, e o tráfego
de aplicativos que usam mTLS não podem ser lidos ou modificados por esse
ataque. Todos os nós do Google Kubernetes Engine (GKE) foram afetados por essa
vulnerabilidade, e recomendamos que você faça o upgrade para a última versão
do patch, como detalhamos a seguir.

####  O que fazer?

Para mitigar essa vulnerabilidade no Anthos GKE On-Prem (GKE On-Prem), faça [
upgrade dos clusters ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/how-to/upgrading?hl=pt-br) para a versão a seguir ou mais
recente:

  * Anthos 1.3.2 

Em geral, pouquíssimos contêineres exigem ` CAP_NET_RAW ` . Esse e outros
recursos avançados precisam ser bloqueados, por padrão, usando o [ Anthos
Policy Controller ](https://cloud.google.com/anthos-config-
management/docs/concepts/policy-controller?hl=pt-br) ou atualizando as
especificações de pod:

  * Remova a capacidade ` CAP_NET_RAW ` dos contêineres: 
    * Usando e aplicando o Anthos Policy Controller/Gatekeeper com este [ modelo de restrição ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) (em inglês), por exemplo: 
        
                
        # Dropping CAP_NET_RAW with Gatekeeper
        # (requires the K8sPSPCapabilities template)
        apiversion: constraints.gatekeeper.sh/v1beta1
        kind:  K8sPSPCapabilities
        metadata:
          name: forbid-cap-net-raw
        spec:
          match:
            kinds:
              - apiGroups: [""]
              kinds: ["Pod"]
            namespaces:
              #List of namespaces to enforce this constraint on
              - default
            # If running gatekeeper >= v3.1.0-beta.5,
            # you can exclude namespaces rather than including them above.
            excludedNamespaces:
              - kube-system
          parameters:
            requiredDropCapabilities:
              - "NET_RAW"
        

    * Atualizando suas especificações de pod: 
        
                
        # Dropping CAP_NET_RAW from a Pod:
        apiVersion: v1
        kind: Pod
        metadata:
          name: no-cap-net-raw
        spec:
          containers:
            -name: may-container
             ...
            securityContext:
              capabilities:
                drop:
                  -NET_RAW
        

####  Qual vulnerabilidade é corrigida por esse patch?

O patch mitiga a seguinte vulnerabilidade:

A vulnerabilidade descrita na capacidade ` CAP_NET_RAW ` do [ problema 91507
do Kubernetes ](https://github.com/kubernetes/kubernetes/issues/91507) (que
está incluída no conjunto de capacidades de contêiner padrão) que envolve
configurar de forma mal-intencionada a pilha do IPv6 no nó e redirecionar o
tráfego do nó para o contêiner controlado pelo invasor. Isso permite que o
invasor intercepte/modifique o tráfego que se origina do nó ou se destina a
ele. O tráfego mútuo TLS/SSH, como entre o kubelet e o servidor da API, ou o
tráfego de aplicativos que usam mTLS não pode ser lido ou modificado por essa
invasão.

|

Média

|

[ Problema 91507 do Kubernetes
](https://github.com/kubernetes/kubernetes/issues/91507)  
  
  
##  GCP-2020-004

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Uma vulnerabilidade foi descoberta no Kubernetes recentemente, descrita na [
CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) (em inglês). Ela permite que qualquer
usuário autorizado a fazer solicitações POST execute um ataque remoto de
negação de serviço em um servidor da API Kubernetes. O Comitê de Segurança de
Produto (PSC, na sigla em inglês) do Kubernetes divulgou mais informações
sobre essa vulnerabilidade. Para saber mais, acesse-as [ aqui
](https://groups.google.com/g/kubernetes-security-
announce/c/wuwEwZigXBc?hl=pt-br) (em inglês).

É possível mitigar essa vulnerabilidade limitando os clientes que têm acesso à
rede dos servidores da API Kubernetes.

####  O que fazer?

Recomendamos fazer upgrade de seus clusters para corrigir versões que
contenham a correção dessa vulnerabilidade assim que estiverem disponíveis.

Veja abaixo as versões de patch que solucionam o problema:

  * Anthos 1.3.0, que executa o Kubernetes versão 1.15.7-gke.32 

####  Quais vulnerabilidades são corrigidas por esse patch?

A de negação de serviço (DoS) a seguir:

[ CVE-2019-11254 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) .

|

Média

|

[ CVE-2019-11254 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  16 de outubro de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Uma vulnerabilidade foi descoberta no Kubernetes recentemente, descrita em [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) (em inglês). Ela permite que qualquer
usuário autorizado a fazer solicitações POST execute um ataque remoto de
negação de serviço em um servidor da API Kubernetes. O Comitê de Segurança de
Produto (PSC, na sigla em inglês) do Kubernetes divulgou mais informações
sobre essa vulnerabilidade, que podem ser encontradas [ aqui
](https://groups.google.com/forum/?hl=pt-br#!topic/kubernetes-security-
announce/jk8polzSUxs) .

É possível mitigar essa vulnerabilidade limitando os clientes que têm acesso à
rede aos servidores da API Kubernetes.

######  O que fazer?

Recomendamos fazer [ upgrade do cluster
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.3/how-
to/upgrading-clusters?hl=pt-br) para uma versão de patch com a correção assim
que ela estiver disponível.

As versões de patch que contêm a correção estão listadas abaixo:

  * Anthos 1.1.1, que executa o Kubernetes versão 1.13.7-gke.30 

######  Qual vulnerabilidade é corrigida por esse patch?

O patch mitiga a seguinte vulnerabilidade: [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) .

|

Alta

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) (em inglês)  
  
##  23 de agosto de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Descobrimos e mitigamos uma vulnerabilidade em que o proxy RBAC, usado para
proteger os endpoints de monitoramento, não autorizou corretamente os
usuários. Consequentemente, as métricas de determinados componentes estão
disponíveis para usuários não autorizados na rede interna do cluster. Os
seguintes componentes foram afetados:

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

Recomendamos [ fazer upgrade ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/how-to/upgrading-clusters?hl=pt-br) dos clusters para a
versão [ 1.0.2-gke.3 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/downloads?hl=pt-br#gkectl_latest) , que inclui o patch dessa
vulnerabilidade, o mais rápido possível.

|

Média

|

[ Versões do Anthos GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/downloads?hl=pt-br#gkectl_latest)  
  
##  22 de agosto de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Recentemente, o Kubernetes descobriu uma vulnerabilidade, a [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) , que
possibilita que instâncias de [ recursos personalizados
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) com escopo no cluster sejam usadas como se fossem objetos de
namespaces existentes em todos os namespaces. Isso significa que contas de
usuários e de serviço com permissões apenas do RBAC de nível do namespace
podem interagir com recursos personalizados com escopo no cluster. A
exploração dessa vulnerabilidade exige que o invasor tenha privilégios para
acessar o recurso no namespace.

######  O que fazer?

Recomendamos [ fazer upgrade ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/how-to/upgrading-clusters?hl=pt-br) dos clusters para a
versão [ 1.0.2-gke.3 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/downloads?hl=pt-br#gkectl_latest) , que inclui o patch dessa
vulnerabilidade, o mais rápido possível.

######  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz a seguinte vulnerabilidade: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Média

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

