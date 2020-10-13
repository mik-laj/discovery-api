A new version of Anthos GKE on AWS was released on August 5. See the [ release
notes ](https://cloud.google.com/anthos/gke/docs/aws/release-notes?hl=pt-br)
for information on breaking changes.

#  Boletins de segurança

Saiba mais sobre os boletins de segurança do Anthos GKE na AWS (GKE na AWS).

##  GCP-2020-011

**Publicado:** 24/07/2020  
Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Uma vulnerabilidade de rede, [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) (em inglês), foi
descoberta recentemente no Kubernetes. Às vezes, os serviços se comunicam com
outros aplicativos em execução no mesmo pod usando a interface de loopback
local (127.0.0.1). Essa vulnerabilidade permite que um invasor com acesso à
rede do cluster envie tráfego para a interface de loopback de pods e nós
adjacentes. Os serviços que dependem da interface de loopback e não são
acessados fora do pod podem ser explorados.

A exploração dessa vulnerabilidade nos clusters do GKE na AWS exige que um
invasor desative as [ verificações de destino de origem
](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html) nas
instâncias do EC2 no cluster. Isso exige que o invasor tenha permissões do IAM
da AWS para ` ModifyInstanceAttribute ` ou ` ModifyNetworkInterfaceAttribute `
nas instâncias do EC2. Por esse motivo, essa vulnerabilidade recebeu uma
gravidade baixa para o GKE na AWS.

####  O que fazer?

Para corrigir essa vulnerabilidade, faça upgrade do cluster para uma versão
com patch. As próximas versões do GKE na AWS ou mais recentes precisam incluir
a correção para essa vulnerabilidade:

  * GKE na AWS 1.4.2 

####  Qual vulnerabilidade é corrigida por esse patch?

Esse patch corrige a seguinte vulnerabilidade: [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) (em inglês).

|

Baixa

|

[ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315) (em
inglês)  
  
##  GCP-2020-009

**Publicado:** 15/07/2020  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Uma vulnerabilidade de escalonamento de privilégios, [ CVE-2020-8559
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559) (em inglês),
foi descoberta recentemente no Kubernetes. Essa vulnerabilidade permite que um
invasor que já tenha comprometido um nó execute um comando em qualquer pod do
cluster. Dessa forma, o invasor pode usar o nó já comprometido para
comprometer outros nós e possivelmente ler informações ou causar ações
destrutivas.

Observe que, para que um invasor explore essa vulnerabilidade, é preciso que
um nó do cluster já tenha sido comprometido. Essa vulnerabilidade, por si só,
não comprometerá os nós do cluster.

####  O que fazer?

O GKE na AWS GA (1.4.1, disponível no final de julho de 2020) ou mais recente
inclui o patch para essa vulnerabilidade. Se você estiver usando uma versão
anterior, [ faça o download de uma nova versão da ferramenta de linha de
comando anthos-gke ](https://cloud.google.com/anthos/gke/docs/aws/how-
to/prerequisites?hl=pt-br) e recrie seus clusters de gerenciamento e usuário.

####  Qual vulnerabilidade é corrigida por esse patch?

Esses patches mitigam a vulnerabilidade CVE-2020-8559. Isso é classificado
como uma vulnerabilidade média do GKE, porque exige que o invasor tenha
informações em primeira mão sobre o cluster, os nós e as cargas de trabalho
para aproveitar esse ataque de forma eficaz, além de um nó comprometido. Essa
vulnerabilidade em si não fornece um nó comprometido a um invasor.

|

Média

|

[ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559) (em inglês)  
  
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
e, portanto, foi afetado por essa vulnerabilidade. Recomendamos que você faça
o upgrade do plano de controle para a última versão do patch, como detalhamos
a seguir. Não é necessário fazer upgrade do nó.  

####  O que fazer?

O Anthos GKE na AWS (GKE na AWS) v0.2.0 ou mais recente já inclui o patch para
essa vulnerabilidade. Se você estiver usando uma versão anterior, [ faça o
download de uma nova versão da ferramenta de linha de comando anthos-gke
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=pt-br)
e recrie seus clusters de gerenciamento e usuário.

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

[ Faça o download da ferramenta de linha de comando anthos-gke
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=pt-br)
com a seguinte versão ou mais recente e recrie seus clusters de gerenciamento
e usuário:

  * aws-0.2.1-gke.7 

Em geral, pouquíssimos contêineres exigem ` CAP_NET_RAW ` . Esse e outros
recursos avançados precisam ser bloqueados, por padrão, usando o [ Anthos
Policy Controller ](https://cloud.google.com/anthos-config-
management/docs/concepts/policy-controller?hl=pt-br) ou atualizando as
especificações de pod:

Remova a capacidade ` CAP_NET_RAW ` dos contêineres:

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
    

  * Ou ao atualizar as especificações do pod: 
    
        
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
](https://github.com/kubernetes/kubernetes/issues/91507) (em inglês)  

