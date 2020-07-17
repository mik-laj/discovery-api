#  Boletins de segurança

Todos os boletins de segurança para o Google Kubernetes Engine (GKE) são
descritos neste tópico.

Geralmente, as vulnerabilidades são mantidas sob sigilo e não podem ser
divulgadas até que as partes afetadas tenham a oportunidade de solucioná-las.
Nesses casos, as [ notas de lançamento ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=pt_br) do GKE mencionarão "atualizações de
segurança" até que a divulgação seja liberada. No momento da liberação, as
notas serão atualizadas para indicar a vulnerabilidade solucionada pelo patch.

**Observação:** esses boletins são especialmente importantes para as pessoas
que têm cargas de trabalho com vários locatários no GKE. Geralmente, elas
costumam ser mais impactadas por essas vulnerabilidades. Para uma descrição
técnica dos limites de segurança no GKE e como eles afetam as cargas de
trabalho, consulte [ Isolamento em camadas diferentes da pilha do Kubernetes
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) (em inglês).

Para receber os boletins de segurança mais recentes, adicione o URL desta
página ao seu [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/kubernetes-engine-
security-bulletins.xml `

##  GCP-2020-007

**Publicado:** 01/06/2020  
Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Uma vulnerabilidade de falsificação da solicitação no lado do servidor (SSRF,
na sigla em inglês), [ a CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555) (em inglês), recentemente foi detectada no
Kubernetes. Essa vulnerabilidade permite que certos usuários autorizados vazem
até 500 bytes de informações confidenciais da rede do host no plano de
controle. O plano de controle do Google Kubernetes Engine (GKE) usa os
controladores do Kubernetes e, portanto, foi afetado por essa vulnerabilidade.
Recomendamos que você faça [ o upgrade ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=pt_br) do plano de
controle para a última versão do patch, como detalhamos a seguir. Um upgrade
dos nós não é exigido.  

####  O que fazer?

Para quase todos os clientes, nenhuma ação é necessária. A grande maioria dos
clusters já executa uma versão com o patch. As seguintes versões do GKE ou
superiores contêm a solução para essa vulnerabilidade:

  * 1.14.7-gke.39 
  * 1.14.8-gke.32 
  * 1.14.9-gke.17 
  * 1.14.10-gke.12 
  * 1.15.7-gke.17 
  * 1.16.4-gke.21 
  * 1.17.0-gke.0 

Os clusters que usam [ canais de lançamento
](https://cloud.google.com/kubernetes-engine/docs/concepts/release-
channels?hl=pt_br) já estão nas versões do plano de controle com a mitigação.

####  Qual vulnerabilidade é corrigida pelo patch?

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
  
O Kubernetes divulgou [ uma vulnerabilidade
](https://github.com/kubernetes/kubernetes/issues/91507) (em inglês) que
permite a um contêiner privilegiado redirecionar o tráfego do nó para outro
contêiner. O tráfego mútuo TLS/SSH, como entre o kubelet e o servidor da API,
ou o tráfego de aplicativos que usam mTLS não pode ser lidos ou modificado por
essa invasão. Todos os nós do Google Kubernetes Engine (GKE) foram afetados
por essa vulnerabilidade, e recomendamos que você faça [ o upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br) para a última versão do patch, como detalhamos a seguir.

####  O que fazer?

Para mitigar essa vulnerabilidade, faça [ o upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br) do seu plano de controle e dos seus nós para uma das versões
com patch listadas a seguir. Os clusters nos canais de lançamento já estão
executando uma versão com patch no plano de controle e nos nós:

  * 1.14.10-gke.36 
  * 1.15.11-gke.15 
  * 1.16.8-gke.15 

Em geral, pouquíssimos contêineres exigem ` CAP_NET_RAW ` . Essa e outras
capacidades poderosas deveriam estar bloqueadas por padrão [ pela
PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-
to/pod-security-policies?hl=pt_br) ou o [ Policy Controller do Anthos
](https://cloud.google.com/anthos-config-management/docs/concepts/policy-
controller?hl=pt_br) :

  * Remova a capacidade ` CAP_NET_RAW ` dos contêineres: 
    * Por meio da [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=pt_br) e usando: 
        
                
        # Require dropping CAP_NET_RAW with a PSP
        apiversion: extensions/v1beta1
        kind: PodSecurityPolicy
        metadata:
          name: no-cap-net-raw
        spec:
          requiredDropCapabilities:
            -NET_RAW
             ...
             # Unrelated fields omitted
        

    * Ou ao utilizar e aplicar o Policy Controller/Gatekeeper do Anthos com este [ modelo de restrição ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) (em inglês), por exemplo: 
        
                
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
        

####  Qual vulnerabilidade é corrigida pelo patch?

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
  
  
##  GCP-2020-005

**Publicação:** 07/05/2020  
**Atualizado em:** 07/05/2020  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Uma vulnerabilidade foi recentemente descoberta no kernel do Linux, descrita
em [ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) (em inglês), permitindo que o escape de
contêiner receba privilégios de raiz no nó do host.

Os nós do Ubuntu do Google Kubernetes Engine executando a versão 1.16 ou 1.17
do GKE foram afetados por essa vulnerabilidade. Recomendamos que você faça
upgrade para a versão de patch mais recente assim que possível, conforme
detalhado abaixo.

Os nós executando o SO otimizado para contêineres não foram afetados. Os nós
executando o GKE On-Prem não foram afetados.

####  O que fazer?

**Para a maioria dos clientes, nenhuma outra ação é necessária. Apenas os nós
executando o Ubuntu na versão 1.16 ou 1.17 do GKE foram afetados** .

Para fazer upgrade dos seus nós, primeiro você precisa fazer o upgrade do
mestre para a versão mais recente. Esse patch será disponibilizado nestas
versões do Kubernetes: 1.16.8-gke.12, 1.17.4-gke.10 e lançamentos posteriores.
Acompanhe a disponibilidade dos patches nas [ notas de lançamento
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=pt_br) .

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz os riscos da seguinte vulnerabilidade:

A [ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) (em inglês) descreve uma vulnerabilidade
na versão 5.5.0 e posteriores do kernel do Linux, que permite que um contêiner
mal-intencionado (com interação mínima do usuário na forma de um exec) leia e
grave na memória do kernel e consiga a execução do código no nível da raiz do
nó do host. Isso é classificado como uma vulnerabilidade de alto nível de
gravidade.

|

Alta

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) (em inglês)  
  
  
##  GCP-2020-003

**Publicação:** 31/03/2020  
**Atualizado em:** 31/03/2020  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Uma vulnerabilidade foi descoberta no Kubernetes recentemente, descrita em [
CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) (em inglês). Ela permite que qualquer
usuário autorizado a fazer solicitações POST execute um ataque remoto de
negação de serviço em um servidor da API Kubernetes. O Comitê de Segurança de
Produto (PSC, na sigla em inglês) do Kubernetes divulgou mais informações
sobre essa vulnerabilidade. Para saber mais, acesse-as [ aqui
](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-security-
announce/wuwEwZigXBc) (em inglês).

Os clusters do GKE que usam [ redes mestras autorizadas
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=pt_br) e [ clusters privados sem endpoint público
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=pt_br#private_master) reduzem essa vulnerabilidade.

####  O que fazer?

Recomendamos que você faça o upgrade do seu cluster para uma versão de patch
com a correção da vulnerabilidade.

Veja abaixo as versões de patch que solucionam o problema:

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  Quais vulnerabilidades são corrigidas por esse patch?

A de negação de serviço (DoS) a seguir:

[ CVE-2019-11254 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) .

|

Média

|

[ CVE-2019-11254 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**Publicação:** 23/03/2020  
**Atualizado em:** 23/03/2020  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
O Kubernetes divulgou [ duas vulnerabilidades de negação de serviço
](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-security-
announce/2UOlsba2g0s) (em inglês), uma com impacto no servidor de API e outra
no Kubelets. Para mais detalhes, veja os seguintes problemas do Kubernetes: [
89377 ](https://github.com/kubernetes/kubernetes/issues/89377) e [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) (ambos em inglês).

####  O que fazer?

Todos os usuários do GKE estão protegidos contra a CVE-2020-8551, a menos que
usuários que não sejam de confiança possam enviar solicitações dentro da rede
interna dos clusters. Além disso, o uso das [ redes mestras autorizadas
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=pt_br) reduz a CVE-2020-8552.

####  Quando essas vulnerabilidades serão corrigidas?

Os patches para a CVE-2020-8551 exigem um upgrade de nó. Abaixo, as versões de
patch que mitigam o problema:

  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

Observação: as versões 1.14.x e anteriores não foram afetadas por essa
vulnerabilidade, então os patches não são obrigatórios para elas.

Os patches para a CVE-2020-8552 exigem o upgrade de um mestre. Abaixo, as
versões de patch que mitigam o problema:

  * 1.14.10-gke.32 
  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

|

Média

|

[ CVE-2020-8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE-2020-8552 (ambas em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  21 de janeiro de 2020. Última atualização em 24 de janeiro de 2020

**Publicação:** 21/01/2020  
**Atualizado em:** 24/01/2020  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
**Atualização de 24/01/2020:** o processo de disponibilização de versões com
patch está sendo realizado e será concluído em 25 de janeiro de 2020.

* * *

A Microsoft divulgou uma vulnerabilidade na Windows CryptoAPI e em sua
validação de assinaturas de curva elíptica. Para mais informações, consulte o
[ anúncio da Microsoft ](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) .

**O que fazer?**

**Para a maioria dos clientes, nenhuma outra ação é necessária. Somente os nós
com Windows Server em execução são afetados.**

Nesse caso, para reduzir a vulnerabilidade, é necessário atualizar os nós e as
cargas de trabalho em contêineres executadas neles para as versões com patch.

**Para atualizar os contêineres:**

É necessário recriá-los. Para isso, use as imagens de contêiner de base mais
recentes da Microsoft selecionando uma tag de [ servercore
](https://hub.docker.com/_/microsoft-windows-servercore) ou [ nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) (páginas em inglês)
que tenha o valor "1/14/2020" ou posterior em "LastUpdated Time".

**Para atualizar os nós:**

O processo de disponibilização de versões com patch está sendo realizado e
será concluído em 24 de janeiro de 2020.

Faça o upgrade dos nós para uma versão de patch do GKE ou use o Windows Update
para implantar manualmente o patch mais recente do Windows a qualquer momento.

Abaixo, as versões de patch que incluem a mitigação:

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**Quais vulnerabilidades são corrigidas por esse patch?**

O patch reduz as vulnerabilidades a seguir:

[ CVE-2020-0601 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) : também conhecida como [ Vulnerabilidade
de spoofing da Windows CryptoAPI ](https://portal.msrc.microsoft.com/en-
US/security-guidance/advisory/CVE-2020-0601) . Usada para fazer executáveis
maliciosos parecerem confiáveis ou permitir que o invasor realize ataques
"man-in-the-middle" e descriptografe informações confidenciais nas conexões
TLS com o software afetado.

|

Pontuação base do NVD: 8,1 (alta)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  14 de novembro de 2019

**Publicação:** 14/11/2019  
**Atualizado em:** 14/11/2019  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
O Kubernetes divulgou um problema de segurança nos arquivos secundários [ `
external-provisioner ` ](https://github.com/kubernetes-csi/external-
provisioner) , [ ` external-snapshotter ` ](https://github.com/kubernetes-
csi/external-snapshotter) e [ ` external-resizer `
](https://github.com/kubernetes-csi/external-resizer) do kubernetes-csi que
impacta a maioria das versões dos arquivos secundários incluídos nos [ drivers
da Container Storage Interface (CSI) ](https://kubernetes-
csi.github.io/docs/drivers.html) [páginas em inglês]. Para ver mais detalhes,
consulte a [ divulgação do Kubernetes
](https://github.com/kubernetes/kubernetes/issues/85233) .

**O que fazer?**  
**Essa vulnerabilidade não afeta nenhum componente do GKE gerenciado** . Você
pode ser afetado se gerenciar seus próprios drivers CSI em [ clusters Alfa do
GKE ](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-
clusters?hl=pt_br) executando o GKE versão 1.12 ou mais recente. Se você for
afetado, verifique as instruções de upgrade com seu distribuidor de drivers
CSI.

**Quais vulnerabilidades são corrigidas por esse patch?**  
[ CVE-2019-11255 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : é uma vulnerabilidade nos arquivos
secundários ` kubernetes-csi ` [ ` external-provisioner `
](https://github.com/kubernetes-csi/external-provisioner) , [ ` external-
snapshotter ` ](https://github.com/kubernetes-csi/external-snapshotter) e [ `
external-resizer ` ](https://github.com/kubernetes-csi/external-resizer) que
possibilita acesso ou mutação não autorizados dos dados de volumes. Isso
impacta a maioria das versões de arquivos secundários incluídos em [ drivers
CSI ](https://kubernetes-csi.github.io/docs/drivers.html) .

|

Média

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  12 de novembro de 2019

**Publicação:** 12/11/2019  
**Atualizado em:** 12/11/2019  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
A Intel divulgou CVEs que potencialmente permitem interações entre a execução
especulativa e o estado microarquitetônico para expor dados. Para ver mais
detalhes, consulte o [ anúncio da Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) (em inglês).

**A infraestrutura de host na qual o Kubernetes Engine é executado isola as
cargas de trabalho do cliente. A não ser que você esteja executando código não
confiável nos seus próprios clusters GKE multilocatários _e_ utilizando nós
N2, M2 ou C2, nenhuma ação extra é necessária. ** Para instâncias do GKE em
nós N1, nenhuma outra ação é necessária.

Se você executa o Anthos GKE no local, a exposição depende do hardware.
Compare sua infraestrutura com o [ anúncio da Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

####  O que fazer?

**Você só será impactado se estiver usando pools de nós N2, M2 ou C2 _e_ esses
nós estiverem executando código não confiável nos próprios clusters
multilocatários do GKE. **

**Reiniciar seus nós aplica o patch.** A forma mais fácil de reiniciar todos
os nós em seu pool de nós é usar a operação de [ upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br#upgrade_nodes) para forçar uma reinicialização em todos os
pools de nós afetados.  

Observação: não é necessário trocar de versão durante um upgrade. É possível
iniciar um upgrade da mesma versão do nó com a sinalização ` cluster-version `
.

####  Quais vulnerabilidades são corrigidas por esse patch?

O patch reduz os riscos das seguintes vulnerabilidades:

[ CVE-2019-11135 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11135) : também é chamada de "TSX Async Abort"
(TAA). Fornece outra via para a exfiltração de dados, usando as mesmas
estruturas da microarquitetura de dados exploradas pela [ Amostragem de dados
de microarquitetura (MDS, na sigla em inglês)
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins?hl=pt_br#may-14-2019) .

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
: vulnerabilidade de negação de serviço (DoS) que afeta hosts de máquina
virtual, permitindo que um convidado mal-intencionado cause uma falha em um
host desprotegido. Também é chamada de "Erro de verificação de máquina na
alteração do tamanho da página". Ela não afeta o GKE.

|

Média

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
(ambas em inglês).  
  
##  22 de outubro de 2019

**Publicação:** 22/10/2019  
**Atualizado em:** 22/10/2019  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Uma vulnerabilidade foi descoberta recentemente na Linguagem de programação
Go, descrita na [ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) . Ela tem potencial para impactar
configurações do Kubernetes usando um proxy de autenticação. Para ver mais
detalhes, consulte o [ anúncio do Kubernetes
](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-security-
announce/PtsUCqFi4h4) .

O Kubernetes Engine não permite a configuração de um proxy de autenticação.
Portanto, não é afetado por essa vulnerabilidade.

|

Nenhuma

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  16 de outubro de 2019

**Publicação:** 16/10/2019  
**Atualizado em:** 24/10/2019  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
**Atualização de 24/10/2019:** agora, versões com patch estão disponíveis em
todas as zonas.

* * *

Uma vulnerabilidade foi descoberta no Kubernetes recentemente, descrita na [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) . Ela possibilita que qualquer usuário
autorizado a fazer solicitações POST execute um ataque remoto de negação de
serviço em um servidor da API Kubernetes. O Comitê de Segurança de Produto
(PSC, na sigla em inglês) do Kubernetes divulgou informações adicionais sobre
essa vulnerabilidade, que podem ser encontradas [ aqui
](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-security-
announce/jk8polzSUxs) .

Os clusters do GKE que usam [ redes mestras autorizadas
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=pt_br) e [ clusters privados sem endpoint público
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=pt_br#private_master) reduzem essa vulnerabilidade.

######  O que fazer?

Recomendamos fazer upgrade do cluster para uma versão de patch com a correção
assim que ela estiver disponível. Esperamos que esteja disponível em todas as
zonas com a versão para o GKE prevista para a semana de 14 de outubro.

As versões de patch com a mitigação são:

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  Quais vulnerabilidades são corrigidas por esse patch?

O patch reduz os riscos das seguintes vulnerabilidades:

A CVE-2019-11253 é uma vulnerabilidade de negação de serviço (DoS).

|

Alta

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  16 de setembro de 2019

**Publicação:** 16/09/2019  
**Atualizado em:** 16/10/2019  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Este boletim já foi atualizado desde a publicação original.

As vulnerabilidades de segurança [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) e [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) (páginas em
inglês) na linguagem de programação Go são vulnerabilidades de negação de
serviço (DoS) que foram recentemente descobertas. No GKE, elas possibilitariam
que um usuário criasse solicitações mal-intencionadas que consomem uma
quantidade excessiva de CPU no servidor da API Kubernetes, potencialmente
reduzindo a disponibilidade do plano de controle do cluster. Para mais
detalhes, consulte a [ divulgação da Linguagem de programação Go
](https://groups.google.com/forum/?hl=pt_br#!topic/golang-
announce/65QixT3tcmg) .

######  O que fazer?

Recomendamos fazer upgrade do cluster para a versão de patch mais recente com
a mitigação dessa vulnerabilidade assim que ela estiver disponível. Esperamos
que ela esteja disponível em todas as zonas com o próximo lançamento do GKE,
de acordo com a [ programação de lançamento
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#september_16_2019) .

As versões de patch com a mitigação são:

  * **Atualização de 16 de outubro de 2019:** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz os riscos das seguintes vulnerabilidades:

A [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) e a [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) (páginas em
inglês) são vulnerabilidades de negação de serviço (DoS).

|

Alta

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  5 de setembro de 2019

**Publicação:** 05/09/2019  
**Atualizado em:** 05/09/2019

O boletim sobre a correção da vulnerabilidade documentada no boletim de  31 de
maio de 2019  foi atualizado.

##  22 de agosto de 2019

**Publicação:** 22/08/2019  
**Atualizado em:** 22/08/2019

O boletim de  5 de agosto de 2019  foi atualizado. A correção da
vulnerabilidade documentada no boletim anterior está [ disponível
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#august_22_2019) .

##  8 de agosto de 2019

**Publicação:** 08/08/2019  
**Atualizado em:** 08/08/2019

O boletim de  5 de agosto de 2019  foi atualizado. Esperamos que a correção da
vulnerabilidade documentada naquele boletim esteja disponível na próxima
versão do GKE.

##  5 de agosto de 2019

**Publicação:** 05/08/2019  
**Atualizado em:** 09/08/2019  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Este boletim já foi atualizado desde a publicação original.

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

Recomendamos fazer [ upgrade ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=pt_br) do cluster para a versão de
patch mais recente com a mitigação dessa vulnerabilidade, assim que ela
estiver disponível. Esperamos que ela esteja disponível em todas as zonas com
a próxima versão do GKE. As versões de patch com a mitigação são:

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ Canal rápido ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=pt_br) ) 

######  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz a seguinte vulnerabilidade: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Média

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  3 de julho de 2019

**Publicação:** 03/07/2019  
**Atualizado em:** 03/07/2019  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Uma versão de patch de ` kubectl ` para tratar da CVE-2019-11246 está
disponível agora com a [ ` gcloud ` 253.0.0
](https://cloud.google.com/sdk/docs/release-notes?hl=pt_br#kubernetes_engine)
. Consulte o  boletim de segurança de 25 de junho de 2019  para mais
informações.

**Observação:** O patch não está disponível na ` kubectl ` 1.11.10.

|

Alta

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  3 de julho de 2019

**Publicação:** 25/06/2019  
**Atualizado em:** 03/07/2019  Descrição  |  Gravidade  |  Observações  
---|---|---  
  
######  Atualização de 3 de julho de 2019

Quando você fez sua última atualização, os patches para as versões 1.11.9 e
1.11.10 ainda não estavam disponíveis. A 1.11.10-gke.5 foi lançada agora como
um upgrade para as duas versões 1.11.

Neste momento, as instâncias mestras do GKE e a infraestrutura do Google na
qual o Kubernetes Engine é executado já tiveram patches aplicados a elas e a
infraestrutura está protegida contra essa vulnerabilidade.

As instâncias mestras da versão 1.11 ficarão obsoletas em breve e estão
programadas para fazer upgrade para a 1.12 na semana de 8 de julho de 2019. É
possível escolher qualquer uma das ações sugeridas a seguir para aplicar uma
versão com patch aos nós:

  * Faça o upgrade do nó para 1.11.10-gke.5 até 8 de julho de 2019. Após essa data, as versões 1.11 começarão a ser removidas da lista de upgrades disponíveis. 
  * Ative os [ upgrades automáticos ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=pt_br) dos nós 1.11 para a realização do upgrade quando os mestres forem atualizados para a versão 1.12. 
  * [ Faça o upgrade manual ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=pt_br) dos mestres e dos nós para uma versão 1.12 corrigida. 

Segue o boletim original de 24 de junho de 2019:

* * *

######  Atualização de 24 de junho de 2019

Às 21h40 UTC de 22/06/2019, disponibilizamos as seguintes versões com patch do
Kubernetes. Os mestres com versões 1.11.0 e 1.13.6 do Kubernetes serão
atualizados automaticamente para uma versão com patch. Se você não está usando
uma versão compatível com esse patch, faça upgrade para uma versão compatível
do mestre (listada abaixo) antes de fazer upgrade dos nós.

**Devido à gravidade dessas vulnerabilidades, tendo ou não ativado o upgrade
automático de nós, é recomendável que você faça[ upgrade manualmente
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=pt_br) dos nós e dos mestres para uma dessas versões
assim que possível. **

Versões com patch:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

Segue o boletim original de 18 de junho de 2019:

* * *

A Netflix divulgou recentemente três vulnerabilidades do TCP nos kernels do
Linux:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Essas CVEs são coletivamente denominadas [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) (em inglês).

Os kernels do Linux sem patch podem ser vulneráveis a ataques de negação de
serviço disparados remotamente. **Os nós do Google Kubernetes Engine que
enviam e recebem tráfego de redes não confiáveis são afetados. É recomendável
seguir as etapas de mitigação abaixo para proteger suas cargas de trabalho.**

######  Mestres do Kubernetes

  * Os mestres do Kubernetes que usam [ Redes autorizadas ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=pt_br) para limitar o tráfego de redes confiáveis não são afetados. 

  * Os mestres de clusters do GKE, que são gerenciados pelo Google, serão corrigidos automaticamente nos próximos dias. Nenhuma ação do cliente é necessária. 

######  Nós do Kubernetes

Nós que limitam o tráfego a redes confiáveis não são afetados. Um cluster
afetado poderá apresentar:

  * Nós protegidos por firewall contra redes não confiáveis ou sem IPs públicos ( [ Clusters privados ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=pt_br) ) 
  * Clusters sem serviços públicos do tipo LoadBalancer 

O Google está preparando uma mitigação permanente dessas vulnerabilidades que
será disponibilizada como uma nova versão de nó. Quando a correção permanente
estiver disponível, este boletim será atualizado e todos os clientes do GKE
receberão um e-mail.

Até lá, é possível usar um DaemonSet criado para o Kubernetes, que implementa
mitigações ao modificar a configuração ` iptables ` do host.

#####  O que fazer?

Aplique o DaemonSet do Kubernetes para todos os nós no cluster executando o
comando a seguir. Isso adiciona uma regra ` iptables ` às regras ` iptables `
existentes no nó para reduzir a vulnerabilidade. **Execute o comando uma vez
por cluster para cada projeto do Google Cloud.**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

Como o Ipv6 não é compatível com o GKE, nenhuma regra dele é necessária.

Quando uma versão com patch do nó estiver disponível e todos os nós
possivelmente afetados tiverem passado por upgrade, será possível remover o
DaemonSet usando o comando a seguir. **Execute o comando uma vez por cluster
para cada projeto do Google Cloud.**

    
    
    
    kubectl delete -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

|  Alta  
Média  
Média  
|  [ CVE-2019-11477 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
(páginas em inglês).  
  
##  25 de junho de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
**Atualização de 03/07/2019:** Este patch está disponível na ` gcloud `
253.0.0, para as versões 1.12.9, 1.13.6, 1.14.2 e mais recentes da ` kubectl `
.

**Observação:** O patch não está disponível na versão 1.11.10.

* * *

Recentemente, o Kubernetes descobriu uma vulnerabilidade, a [ CVE-2019-11246
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11246) (em inglês),
que possibilita que um invasor com acesso a uma operação ` kubectl cp ` e
execução de código dentro de um contêiner modifique arquivos no host. Essa
exploração tem potencial para possibilitar que um invasor substitua ou crie um
arquivo no sistema de arquivos do host. Para ver mais detalhes, consulte o [
anúncio do Kubernetes
](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-security-
announce/NLs2TGbfPdo) .

**Todas as versões da` gcloud ` no Google Kubernetes Engine (GKE) são afetadas
por essa vulnerabilidade. É recomendável fazer upgrade para a versão de patch
mais recente da ` gcloud ` quando ela estiver disponível. ** Uma futura versão
de patch incluirá uma mitigação dessa vulnerabilidade.

######  O que fazer?

Uma versão com patch da ` kubectl ` será disponibilizada em um futuro
lançamento da ` gcloud ` . Também é possível fazer [ upgrade da ` kubectl `
](https://kubernetes.io/docs/tasks/tools/install-kubectl/) por conta própria.

Acompanhe a disponibilidade desse patch nas [ notas de lançamento da ` gcloud
` ](https://cloud.google.com/sdk/docs/release-notes?hl=pt_br) .

######  Qual vulnerabilidade é corrigida por esse patch?

A vulnerabilidade [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) possibilita que um invasor com acesso a
uma operação ` kubectl cp ` e capaz de executar um código dentro de um
contêiner modifique arquivos no host. Essa exploração tem potencial para
possibilitar que um invasor substitua ou crie um arquivo no sistema de
arquivos do host.

|

Alta

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  18 de junho de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Recentemente, o Docker descobriu uma vulnerabilidade, a [ CVE-2018-15664
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-15664) (em inglês),
que possibilita que um invasor capaz de executar um código dentro de um
contêiner sequestre uma operação ` docker cp ` iniciada externamente. Essa
exploração tem potencial para possibilitar que um invasor altere o local onde
um arquivo está sendo gravado para um local arbitrário no sistema de arquivos
do host.

**Todos os nós do Google Kubernetes Engine (GKE) nos quais o Docker é
executado são afetados por essa vulnerabilidade. É recomendável fazer upgrade
para a versão de patch mais recente assim que estiver disponível. Uma futura
versão de patch incluirá uma mitigação dessa vulnerabilidade.**

**Todos os mestres do Google Kubernetes Engine (GKE) anteriores à versão
1.12.7 executam o Docker e são afetados por essa vulnerabilidade.** No GKE, os
usuários não têm acesso à operação ` docker cp ` no mestre. Portanto, o risco
dessa vulnerabilidade para mestres do GKE é limitado.

#####  O que fazer?

Apenas os nós com o Docker em execução são afetados, e somente quando for
emitido um comando ` docker cp ` (ou equivalente da API) que possa ser
invadido. Espera-se que isso seja bastante incomum em um ambiente do
Kubernetes. Nós com o [ Container-Optimized OS com containerd
](https://cloud.google.com/kubernetes-engine/docs/concepts/using-
containerd?hl=pt_br) em execução não são afetados.

Para fazer o upgrade dos nós, primeiro é necessário [ fazer upgrade do mestre
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br#upgrading_the_cluster) para a versão com patch. Quando o
patch estiver disponível, será possível iniciar o upgrade do mestre ou esperar
que o Google faça o upgrade automaticamente. O patch estará disponível no
Docker 18.09.7, que será incluído em um futuro patch do GKE. **Esse patch será
disponibilizado apenas para as versões 1.13 e mais recentes do GKE.**

Faremos upgrade automático dos mestres do cluster para a versão com patch no
ritmo normal de upgrades. Também é possível iniciar o upgrade de um mestre por
conta própria depois que a versão com patch estiver disponível.

Este boletim será atualizado com as versões com patch assim que estiverem
disponíveis. Acompanhe a disponibilidade desses patches nas [ notas de
lançamento ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br) .

#####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz os riscos da seguinte vulnerabilidade:

A vulnerabilidade [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) possibilita que um invasor capaz de
executar um código dentro de um contêiner invada uma operação ` docker cp `
iniciada externamente. Essa exploração permite que um invasor altere o local
onde um arquivo está sendo gravado para um local arbitrário no sistema de
arquivos do host.

|  Alta  |  
  
##  31 de maio de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Este boletim já foi atualizado desde a publicação original.

######  Atualização de 2 de agosto de 2019

No momento da publicação do boletim inicial, apenas as versões de 1.13.6-gke.0
a 1.13.6-gke.5 foram impactadas. Devido a uma regressão, todas as versões
1.13.6.x foram afetadas agora. Se você tiver a versão 1.13.6, faça o upgrade
para a 1.13.7 o mais rápido possível.

O projeto Kubernetes divulgou a [ vulnerabilidade CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) (em inglês) no
kubelet v1.13.6 e v1.14.2. Ela pode fazer os contêineres funcionarem como UID
0 (normalmente associado ao usuário ` root ` ), mesmo que um usuário diferente
seja especificado na imagem do contêiner. **Se os contêineres funcionam como
um usuário não raiz e você está executando uma versão de nó entre a
1.13.6-gke.0 e a 1.13.6-gke.6, é recomendável configurar` RunAsUser ` em todos
os pods no cluster cujos contêineres não deveriam funcionar como UID 0. **

Se um valor de ` USER ` não raiz for especificado (por exemplo, ao configurar
o valor de ` USER ` em um Dockerfile), ocorrerá algum comportamento
inesperado. Quando um contêiner é executado pela primeira vez em um nó, ele
respeita corretamente o UID especificado. Contudo, devido a esse defeito, na
segunda execução (e nas subsequentes) o contêiner é executado como UID 0
apesar do UID especificado. Em geral, isso é um privilégio escalonado
indesejado e pode levar a um comportamento inesperado do aplicativo.

#####  Como saber se tenho uma versão impactada?

Execute o seguinte comando para listar todos os nós e a versão do kubelet
deles:

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

Se o resultado mostrar versões do kubelet listadas abaixo, seus nós foram
impactados:

  * v1.13.6 
  * v1.14.2 

#####  Como saber se minha configuração específica foi afetada?

Se os contêineres funcionam como um usuário não raiz e você está executando
uma versão de nó entre a 1.13.6-gke.0 e a 1.13.6-gke.6, você foi impactado
exceto nos casos a seguir:

  * Pods que especificam um valor não raiz válido para o PodSecurityContext ` runAsUser ` não são afetados e continuam funcionando como esperado. 
  * PodSecurityPolicies que aplicam uma configuração ` runAsUser ` tampouco são afetadas e continuam funcionando como esperado. 
  * Pods que especificam ` mustRunAsNonRoot:true ` não iniciarão como UID 0, mas ocorrerá um erro ao iniciarem quando impactados por esse problema. 

#####  O que fazer?

Configure o [ Contexto de segurança RunAsUser
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) (em inglês) em todos os pods no
cluster que não devem ser executados como UID 0. É possível aplicar essa
configuração usando uma [ PodSecurityPolicy
](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) .

|  Média  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  14 de maio de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
**Atualização de 11/06/2019:** o patch está disponível nas versões
1.11.10-gke.4, 1.12.8-gke.6 e 1.13.6-gke.5 lançadas na semana de 28/05/2019 e
outras posteriores.

A Intel divulgou as CVEs a seguir:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Elas são coletivamente denominadas "amostragem de dados de microarquitetura"
(MDS). Essas vulnerabilidades possibilitam a exposição de dados por meio da
interação da execução especulativa com o estado de microarquitetura. Para ver
mais detalhes, consulte a [ divulgação da Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) .

**A infraestrutura do host na qual o Kubernetes Engine é executado isola as
cargas de trabalho do cliente umas das outras. A menos que você esteja
executando um código não confiável dentro de seus clusters multilocatários do
GKE, você não é impactado.**

**Para clientes que estão executando um código não confiável nos seus serviços
multilocatários dentro do Kubernetes Engine, isso é uma vulnerabilidade
particularmente severa.** Para reduzi-la no Kubernetes Engine, desative o
Hyper-Threading nos seus nós. Apenas os nós do Google Kubernetes Engine (GKE)
que usam várias CPUs são afetados por essas vulnerabilidades. Observe que as
VMs n1-standard-1 (padrão do GKE), g1-small e f1-micro expõem apenas uma vCPU
para o ambiente convidado. Por isso, não é necessário desativar o Hyper-
Threading.

Proteções adicionais para ativar a funcionalidade de despejo serão incluídas
em uma futura [ versão de patch ](https://cloud.google.com/kubernetes-
engine/release-notes?hl=pt_br) . Faremos upgrade automático dos mestres e dos
nós para a versão com patch nas próximas semanas, no ritmo normal de upgrades.
**Apenas o patch não é suficiente para mitigar a exposição a essa
vulnerabilidade. Veja as ações recomendadas abaixo.**

Se o GKE On-Prem for executado, você poderá ser afetado dependendo do hardware
utilizado. Consulte o [ anúncio da Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) .

####  O que fazer?

**Você não é impactado, a menos que esteja executando um código não confiável
dentro dos seus clusters multilocatários do GKE.**

**Para nós no Kubernetes Engine, crie novos nós com o Hyper-Threading
desativado e reprograme as cargas de trabalho em novos nós.**

Observe que as VMs n1-standard-1, g1-small e f1-micro expõem apenas uma vCPU
para o ambiente convidado. Por isso, não é necessário desativar o Hyper-
Threading.

**Alerta:**

  * Desativar o Hyper-Threading pode ter um impacto severo nos clusters e no aplicativo. Verifique se isso é permitido antes de implantar nos seus clusters de produção. 
  * É possível desativar o Hyper-threading no nível do pool de nós do GKE com a implantação de um DaemonSet. Contudo, implantar esse DaemonSet reinicializará todos os seus nós no pool de nós ao mesmo tempo. Portanto, é recomendável criar um novo pool de nós no cluster, implantar o DaemonSet para desativar o Hyper-Threading naquele pool de nós e, então, migrar as cargas de trabalho para o novo pool de nós. 

Para criar um novo pool de nós com o Hyper-Threading desativado:

  1. Crie um novo pool de nós no cluster com o rótulo do nó ` cloud.google.com/gke-smt-disabled=true ` : 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. Implante o DaemonSet para esse novo pool de nós. O DaemonSet será executado somente em nós com o rótulo ` cloud.google.com/gke-smt-disabled=true ` . Ele desativará o Hyper-Threading e, depois, reinicializará o nó. 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. Verifique se os pods do DaemonSet estão no estado de execução. 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

Você receberá uma resposta semelhante a:

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. Verifique se a mensagem “SMT foi desativada” aparece nos registros dos pods. 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

Observação: as opções de inicialização não poderão ser modificadas se o
recurso [ Inicialização segura ](https://cloud.google.com/kubernetes-
engine/docs/how-to/shielded-gke-nodes?hl=pt_br#secure_boot) estiver ativado.
Se esse for o caso, você precisará [ desativar essa funcionalidade
](https://cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-
nodes?hl=pt_br#disabling) antes da criação do DaemonSet.

É necessário manter o DaemonSet em execução nos pools de nós para que as
alterações sejam aplicadas automaticamente aos novos nós criados no pool. É
possível acionar as criações de nós por meio do reparo automático de nós, do
upgrade manual ou automático e do escalonamento automático.

Para reativar o Hyper-Threading, é necessário recriar o pool de nós sem
implantar o DaemonSet fornecido e migrar as cargas de trabalho para o novo
pool de nós.

Também é recomendável fazer o upgrade manual dos nós assim que o patch estiver
disponível. Para fazer o upgrade, primeiro é necessário [ fazer upgrade do
mestre ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br#upgrading_the_cluster) para a versão mais recente. O upgrade
dos mestres do GKE será feito automaticamente no ritmo normal de upgrades.

Este boletim será atualizado com as versões com um patch assim que eles
estiverem disponíveis.

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz os riscos das seguintes vulnerabilidades:

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
, [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) , [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) e [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)
(páginas em inglês): essas vulnerabilidades exploram uma execução
especulativa. Elas são coletivamente denominadas "amostragem de dados de
microarquitetura" (MDS). Essas vulnerabilidades possibilitam a exposição de
dados por meio da interação da execução especulativa com o estado de
microarquitetura.  |  Média  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  5 de abril de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Recentemente, as vulnerabilidades de segurança [ CVE-2019-9900
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900) e [
CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)
foram descobertas no [ Envoy ](https://www.envoyproxy.io/) (páginas em
inglês).

O Envoy é incorporado ao [ Istio ](https://istio.io/) , e essas
vulnerabilidades possibilitam que a política do Istio seja contornada em
alguns casos.

Se você ativou o Istio no Google Kubernetes Engine (GKE) você pode ser afetado
por essas vulnerabilidades. **É recomendável fazer upgrade dos clusters
afetados para a versão de patch mais recente o mais rápido possível, bem como
dos arquivos secundários do Istio (instruções abaixo).**

####  O que fazer?

**Devido à gravidade dessas vulnerabilidades, tendo ou não ativado o upgrade
automático de nós, é recomendável:**

  1. **[ Fazer upgrade manual ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=pt_br) do cluster assim que o patch estiver disponível. **
  2. **Fazer upgrade dos seus arquivos secundários seguindo a[ documentação de upgrade de arquivos secundários ](https://istio.io/docs/setup/kubernetes/upgrade/steps/#sidecar-upgrade) . **

As versões com patch serão disponibilizadas para todos os projetos do GKE
hoje, antes das 19h00 PDT.

Esse patch será disponibilizado nas versões do GKE abaixo. Os novos clusters
usarão a versão com patch por padrão quando anunciado na página de boletins de
segurança do GKE (previsto para 15 de abril de 2019). Se um novo cluster for
criado antes disso, será necessário especificar a versão com patch que ele
deverá usar. O upgrade dos nós de clientes do GKE que ativaram os [ upgrades
de nós automáticos ](https://cloud.google.com/kubernetes-engine/docs/how-
to/node-auto-upgrades?hl=pt_br) e não fazem upgrade manual será feito
automaticamente para versões com patch na próxima semana.

Versões com patch:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz os riscos das seguintes vulnerabilidades:

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) e [ CVE-2019-9901.
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) Saiba mais
sobre elas no [ blog da Istio. ](https://istio.io/blog/2019/announcing-1.1.2)

|  Alta  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901. ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  1º de março de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
**Atualização de 22/03/2019:** esse patch está disponível no Kubernetes
versões 1.11.8-gke.4, 1.13.4-gke.1 e posteriores. O patch ainda não está
disponível na versão 1.12. Acompanhe a disponibilidade desses patches nas [
notas de lançamento ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#march_19_2019) .

Recentemente, o Kubernetes descobriu uma vulnerabilidade de negação de serviço
[ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) (em inglês). Ela possibilita que um
usuário autorizado faça solicitações de patch para criar uma solicitação
"json-patch" mal-intencionada que consome quantidades excessivas de CPU e
memória no servidor da API Kubernetes, potencialmente reduzindo a
disponibilidade do plano de controle do cluster. Para ver mais detalhes,
consulte a [ divulgação do Kubernetes
](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-
announce/vmUUNkYfG9g) . **Todos os mestres do Google Kubernetes Engine (GKE)
são afetados por essas vulnerabilidades. Uma futura versão de patch incluirá
uma mitigação dessa vulnerabilidade. Faremos upgrade automático dos mestres do
cluster para a versão com patch nas próximas semanas, no ritmo normal de
upgrades.**

####  O que fazer?

**Nenhuma ação é necessária. O upgrade dos mestres do GKE será feito
automaticamente, no ritmo normal de upgrades.** Se quiser fazer isso antes, [
inicie o upgrade do mestre manualmente ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=pt_br#upgrading_the_cluster) .

Este boletim será atualizado com as versões com um patch assim que estiverem
disponíveis. Observe que o patch estará disponível apenas nas versões 1.11+,
não nas 1.10.

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz os riscos da seguinte vulnerabilidade:

A vulnerabilidade [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) possibilita que um usuário crie um
patch do tipo "json-patch" que consome quantidades excessivas de CPU no
servidor da API Kubernetes, potencialmente reduzindo a disponibilidade do
plano de controle do cluster.

|  Média  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  11 de fevereiro de 2019 (RunC)

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Recentemente, a Open Containers Initiative (iniciativa que cria padrões para
contêineres) [ descobriu
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=pt_br#!topic/dev/Tc1ELm-8oDI)
uma nova vulnerabilidade de segurança no RunC, a [ CVE-2019-5736
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736) , que
possibilita que um contêiner insira caracteres de escape para conseguir
privilégios raiz no nó do host.

**Seus nós de Ubuntu do Kubernetes Engine (GKE) são afetados por essas
vulnerabilidades. Recomendamos que você[ faça upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br) para a versão de patch mais recente assim que possível,
conforme detalhado abaixo. **

####  O que fazer?

Para fazer upgrade dos seus nós, primeiro você precisa fazer o upgrade do
mestre para a versão mais recente. Esse patch está disponível para Kubernetes
1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4, 1.12.5-gke.5 e para as versões
mais recentes. Acompanhe a disponibilidade desses patches nas [ notas de
lançamento ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#february-11-2019) .

Apenas os nós do Ubuntu no GKE são afetados. Nós que executam COS não são
afetados.

A nova versão do RunC tem uso maior de memória e pode exigir a atualização da
memória alocada para contêineres se você tiver limites baixos (< 16MB)
configurados.

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz os riscos da seguinte vulnerabilidade:

A [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) descreve uma vulnerabilidade no RunC que
permite que um contêiner mal-intencionado (com interação mínima do usuário na
forma de um exec) substitua o binário RunC do host e, assim, consiga execução
de código no nível raiz do nó do host. Contêineres não executados como raiz
não são afetados. Isso é classificado como uma vulnerabilidade de alto nível
de gravidade.

|  Alta  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  11 de fevereiro de 2019 (Go)

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
**Atualização de 25/02/2019:** o patch não está disponível na versão
1.11.7-gke.4, conforme comunicado anteriormente. Se você usa a versão 1.11.7,
é possível fazer downgrade para a 1.11.6, upgrade para a 1.12 ou aguardar pelo
patch da 1.11.7, disponível a partir da semana de 04/03/2019.

Foi descoberta recentemente uma nova vulnerabilidade de segurança na linguagem
de programação Go, a [ CVE-2019-6486 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486) , que é uma negação de serviço (DoS) nas
implementações de criptografia/elípticas das curvas elípticas P-521 e P-384.
No Google Kubernetes Engine (GKE), isso permitiria um usuário a criar
solicitações mal-intencionadas que consomem uma quantidade excessiva de CPU no
servidor da API Kubernetes, potencialmente reduzindo a disponibilidade do
plano de controle do cluster. Para mais detalhes, consulte a [ divulgação da
Linguagem de programação Go
](https://groups.google.com/forum/?hl=pt_br#!topic/golang-
announce/mVeX35iXuSw) .

**Todos os mestres do Google Kubernetes Engine (GKE) são afetados por essas
vulnerabilidades. A[ versão de patch mais recente
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#february-11-2019) inclui uma mitigação dessa vulnerabilidade.
Faremos upgrade automático dos clusters mestres para a versão com patch nas
próximas semanas, no ritmo normal de atualização. **

####  O que fazer?

**Nenhuma ação é necessária. O upgrade dos mestres do GKE será feito
automaticamente no ritmo normal de upgrades.** Se quiser fazer isso antes, [
inicie o upgrade do mestre manualmente ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=pt_br#upgrading_the_cluster) .

Esse patch está disponível nas versões 1.10.12-gke.7, 1.11.6-gke.11,
1.11.7-gke.4, 1.12.5-gke.5 e em versões posteriores.

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz os riscos da seguinte vulnerabilidade:

CVE-2019-6486 é uma vulnerabilidade nas implementações de
criptografia/elípticas das curvas elípticas P-521 e P-384. Isso permite que um
usuário crie entradas que consomem uma quantidade excessiva de CPU.

|  Alta  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  3 de dezembro de 2018

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Recentemente, foi descoberta no Kubernetes uma nova vulnerabilidade de
segurança, a [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) , que permite a usuários com níveis de
privilégio relativamente baixos ignorarem a autorização de acesso às APIs do
kubelet. Com isso, eles podem executar operações arbitrárias em qualquer pod e
em qualquer nó do cluster. Para ver mais detalhes, consulte a [ divulgação do
Kubernetes ](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-
announce/GVllWCg6L88) . **Todas as instâncias mestras do Google Kubernetes
Engine (GKE) foram afetadas por essas vulnerabilidades. O upgrade dos clusters
para[ as versões de patch mais recentes ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=pt_br#november-12-2018) já foi feito. Nenhuma
ação é necessária. **

####  O que fazer?

**Nenhuma ação é necessária. O upgrade das instâncias mestras do GKE já foi
feito.**

Esse patch está disponível no GKE 1.9.7-gke.11, 1.10.6-gke.11, 1.10.7-gke.11,
1.10.9-gke.5, 1.11.2-gke.18 e nas versões mais recentes.

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz os riscos da seguinte vulnerabilidade:

A vulnerabilidade CVE-2018-1002105 possibilita que um usuário com privilégios
relativamente baixos contorne a autorização para as APIs do kubelet. Com isso,
um usuário com autorização para fazer solicitações de upgrade pode encaminhar
e fazer chamadas arbitrárias à API do kubelet. Essa é uma vulnerabilidade
crítica no Kubernetes. Com base em alguns detalhes na implementação do GKE que
impediram o caminho de intensificação não autorizado, podemos classificar a
vulnerabilidade como alta.

|  Alta  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  13 de novembro de 2018

Descrição  
---  
  
**Atualização de 16/11/2018:** a revogação e a rotação de todos os tokens
potencialmente afetados foram concluídas. Você não precisa fazer mais nada.

O Google descobriu recentemente um problema no plug-in da interface de rede de
contêiner (CNI, na sigla em inglês) do Project Calico. Em determinadas
configurações, isso pode causar o registro de informações confidenciais. O
problema está sendo monitorado pela deliberação técnica da Tigera [
TTA-2018-001 ](https://www.projectcalico.org/security-bulletins/) (em inglês).

  * Se executado com geração de registros no nível de depuração, o plug-in da CNI do Calico gravará a configuração do cliente da API Kubernetes nos registros. 
  * A CNI do Calico também gravará o token da API Kubernetes no nível de informação dos registros se o campo “k8s_auth_token” estiver definido na configuração de rede da CNI. 
  * Além disso, no caso de execução do plug-in com geração de registros no nível de depuração, se o token da conta de serviço estiver definido de modo explícito no arquivo de configuração lido pelo Calico ou como uma variável de ambiente usada pelo Calico, os respectivos componentes (calico/node, felix, CNI) gravarão essas informações nos arquivos de registro. 

Esses tokens têm as seguintes permissões:  
      
    
    
    bgpconfigurations.crd.projectcalico.org     [create get list update watch]
    bgppeers.crd.projectcalico.org              [create get list update watch]
    clusterinformations.crd.projectcalico.org   [create get list update watch]
    felixconfigurations.crd.projectcalico.org   [create get list update watch]
    globalbgpconfigs.crd.projectcalico.org      [create get list update watch]
    globalfelixconfigs.crd.projectcalico.org    [create get list update watch]
    globalnetworkpolicies.crd.projectcalico.org [create get list update watch]
    globalnetworksets.crd.projectcalico.org     [create get list update watch]
    hostendpoints.crd.projectcalico.org         [create get list update watch]
    ippools.crd.projectcalico.org               [create get list update watch]
    networkpolicies.crd.projectcalico.org       [create get list update watch]
    nodes                                       [get list update watch]
    pods                                        [get list watch patch]
    namespaces                                  [get list watch]
    networkpolicies.extensions                  [get list watch]
    endpoints                                   [get]
    services                                    [get]
    pods/status                                 [update]
    networkpolicies.networking.k8s.io           [watch list]
            
  
---  
  
Os clusters do Google Kubernetes Engine que têm uma política de rede de
cluster e o Stackdriver Logging ativados registraram os tokens da conta de
serviço do Calico no Stackdriver. Clusters sem a ativação da política de rede
não foram afetados.

Implantamos uma correção que migra o plug-in da CNI do Calico para gravar
apenas no nível de aviso e usar uma nova conta de serviço. O código com patch
será implantado em uma versão posterior.

Ao longo da próxima semana, executaremos uma revogação gradual de todos os
potenciais tokens afetados. Este boletim será atualizado quando a revogação
for concluída. **Não é necessária nenhuma ação da sua parte.** Essa rotação
foi concluída em 16/11/2018.

Se você quiser alternar esses tokens imediatamente, execute o comando a
seguir. O novo secret da conta de serviço será recriado automaticamente em
alguns segundos:  
  
kubectl get sa --namespace kube-system calico -o template --template '{{(index
.secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system  
---  
  
####  Detecção

O GKE registra todos os acessos ao servidor da API. Para determinar se um
token do Calico foi usado fora do intervalo de IPs esperado, execute a
consulta do Stackdriver a seguir. Observação: a consulta retornará apenas
registros de chamadas feitas fora da rede do GCP. Faça as alterações
necessárias de acordo com seu ambiente específico.  
  
---  
      
    
    
    resource.type="k8s_cluster"
    protoPayload.authenticationInfo.principalEmail="system:serviceaccount:kube-system:calico"
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.34.208.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.192.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.200.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.59.80.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.208.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.216.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.220.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.222.0/24")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.224.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.216.148.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.222.176.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "173.255.112.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "192.158.28.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.192.112.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.232.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.236.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.236.48.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.251.128.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.204.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.208.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.167.160.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.178.192.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.2.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.240.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.128.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.154.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.196.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "208.68.108.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.184.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.188.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.202.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.192.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.196.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.198.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.200.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "2600:1900::/35")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.232.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.234.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.236.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.240.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.232.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.220.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.242.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.244.0.0/14")
            
  
---  
  
##  14 de agosto de 2018

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
A [ Intel divulgou ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) as CVEs a seguir:

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (para [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (para sistemas operacionais e [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (para virtualização) 

Essas CVEs são coletivamente denominadas "L1 Terminal Fault (L1TF)".

As vulnerabilidades desse tipo atacam a configuração de estruturas de dados no
nível do processador para explorar a execução especulativa. "L1" se refere ao
cache de dados de nível 1 (L1D), um pequeno recurso dos núcleos usado para
acelerar o acesso à memória.

Leia a [ postagem do blog do Google Cloud
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=pt_br) para ver mais detalhes sobre essas
vulnerabilidades e os recursos do Compute Engine que ajudam a reduzir o
impacto delas.

####  Impacto no Google Kubernetes Engine

A infraestrutura que suporta o Kubernetes Engine e isola os clusters e os nós
do cliente é protegida contra ameaças conhecidas.

Os pools de nós do Kubernetes Engine que usam a imagem do Container-Optimized
OS do Google e estão com o [ upgrade automático
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=pt_br) ativado receberão as versões com patch da imagem do
Container-Optimized OS conforme elas forem disponibilizadas, a partir de
20/08/2018.

É necessário fazer [ o upgrade manual ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=pt_br) dos pools de nós do
Kubernetes Engine que não estiverem com o [ upgrade automático
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=pt_br) ativado, à medida que forem disponibilizadas as versões com
patch da imagem do Container-Optimized OS.

|  Alta  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  6 de agosto de 2018. Última atualização: 5 de setembro de 2018

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
####  Atualização de 05/09/2018

O boletim sobre a [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) foi divulgado recentemente. Assim como a [
CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
, é uma vulnerabilidade de rede no nível do kernel que aumenta a eficiência de
ataques de negação de serviço (DoS) contra sistemas vulneráveis. A principal
diferença é que a CVE-2018-5391 pode ser explorada por meio de conexões IP.
Atualizamos este boletim para detalhar as duas vulnerabilidades.

####  Descrição

Na [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack"), há a descrição de uma
vulnerabilidade de rede no nível do kernel que aumenta a eficácia de ataques
de negação de serviço (DoS) em sistemas vulneráveis com conexões TCP.

Na [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) (“FragmentSmack”), você encontra a
descrição de uma vulnerabilidade de rede no nível do kernel que aumenta a
eficiência de ataques de negação de serviço (DoS) em sistemas vulneráveis por
meio de conexões IP.

####  Impacto no Google Kubernetes Engine

Desde 11/08/2018, todas as instâncias mestras do Kubernetes Engine estão
protegidas contra essas duas vulnerabilidades. Além disso, todos os clusters
desse serviço com a opção de upgrade automático ativada também estão
protegidos. Os pools de nós que não estão com o [ upgrade automático
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br) ativado e foram atualizados manualmente pela última vez
antes de 11 de agosto de 2018 podem ser afetados por essas duas
vulnerabilidades.

####  Versões com patch

Devido à gravidade dessa vulnerabilidade, recomendamos que você faça o [
upgrade manual ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=pt_br#upgrading-nodes) dos seus nós assim que o
patch estiver disponível.

|  Alta  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  30 de maio de 2018

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Recentemente foi descoberta no Git uma vulnerabilidade que possibilita a
intensificação de privilégios no Kubernetes caso usuários sem privilégios
tenham a permissão para criar pods com volumes gitRepo. A CVE é identificada
pela tag [ CVE-2018-11235 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-11235) .

####  Meu ambiente foi afetado por essa vulnerabilidade?

Seu ambiente pode ter sido afetado se todas as afirmações a seguir forem
aplicáveis:

  * Usuários que não são de confiança podem criar pods (ou acionar a criação deles). 
  * Os pods criados por usuários que não são de confiança têm restrições que impedem o acesso root do host (por exemplo, por meio da [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=pt_br) ). 
  * Os pods criados por usuários que não são de confiança podem usar o tipo de volume "gitRepo". 

Todos os nós do Kubernetes Engine estão vulneráveis.

####  O que fazer?

Proíba o uso do tipo de volume "gitRepo". Para proibir volumes gitRepo com a
PodSecurityPolicy, omita ` gitRepo ` da lista de permissões de ` volumes ` na
sua PodSecurityPolicy.

Clone um repositório git em um volume "EmptyDir" a partir de um
"initContainer" para conseguir um comportamento equivalente ao do volume
"gitRepo".

    
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: git-repo-example
    spec:
      initContainers:
        # This container clones the desired git repo to the EmptyDir volume.
        - name: git-clone
          image: alpine/git # Any image with git will do
          args:
            - clone
            - --single-branch
            - --
            - https://github.com/kubernetes/kubernetes # Your repo
            - /repo # Put it in the volume
          securityContext:
            runAsUser: 1 # Any non-root user will do. Match to the workload.
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
          volumeMounts:
            - name: git-repo
              mountPath: /repo
      containers:
        ...
      volumes:
        - name: git-repo
          emptyDir: {}

####  Qual patch corrige essa vulnerabilidade?

Um patch será incluído em uma das próximas versões do Kubernetes Engine. Volte
a esta página em breve para mais detalhes.

|  Média  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  21 de maio de 2018

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Diversas vulnerabilidades foram descobertas recentemente no kernel do Linux.
Elas podem permitir a intensificação de privilégios de negação de serviço (por
meio da falha do kernel) a partir de um processo sem privilégios. Essas CVEs
são identificadas pelas tags [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) , [ CVE-2018-8897
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897) e [
CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)
. Todos os nós do Kubernetes Engine são afetados por essas vulnerabilidades. É
recomendável [ fazer upgrade ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=pt_br) para a versão de
patch mais recente, conforme detalhado a seguir.

####  O que fazer?

Para fazer o upgrade, primeiro você precisa atualizar sua instância mestra
para a versão mais recente. Esse patch está disponível no Kubernetes Engine
versões 1.8.12-gke.1, 1.9.7-gke.1 e 1.10.2-gke.1. Essas versões incluem
patches para imagens do Ubuntu e do Container-Optimized OS.

Se você criar um novo cluster antes disso, especifique qual é a versão com o
patch para que ela seja usada. Os clientes que ativaram os [ upgrades de nós
automáticos ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=pt_br) e não realizaram a atualização manualmente terão os
nós atualizados para versões com patch nas próximas semanas.

####  Quais vulnerabilidades são corrigidas por esse patch?

O patch reduz os riscos das seguintes vulnerabilidades:

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : essa vulnerabilidade afeta o kernel
do Linux. Ela permite que um usuário ou processo sem privilégios cause uma
falha no kernel do sistema, o que levaria a um ataque de DoS ou um
escalonamento de privilégios. Essa é uma vulnerabilidade de alta gravidade,
com classificação de 7,8 no Sistema de Pontuação de Vulnerabilidades Comuns
(CVSS, na sigla em inglês).

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : essa vulnerabilidade afeta o kernel do
Linux. Ela permite que um usuário ou processo sem privilégios cause uma falha
no kernel do sistema, o que levaria a um ataque de DoS. Essa é uma
vulnerabilidade de gravidade moderada, com classificação de 6,5 no Sistema de
Pontuação de Vulnerabilidades Comuns (CVSS, na sigla em inglês).

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : essa vulnerabilidade afeta o hipervisor
KVM do kernel do Linux. Ela permite que um processo sem privilégios cause uma
falha no kernel convidado ou possivelmente consiga privilégios. Um patch que
corrige essa vulnerabilidade foi incluído na infraestrutura em que o
Kubernetes Engine é executado, portanto, esse serviço não é afetado. Essa é
uma vulnerabilidade de alta gravidade, com classificação de 8,0 no Sistema de
Pontuação de Vulnerabilidades Comuns (CVSS, na sigla em inglês).

|  Alta  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  12 de março de 2018

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
O projeto Kubernetes [ divulgou recentemente
](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-security-
announce/P7lBjbjDKd8) novas vulnerabilidades de segurança, a [
CVE-2017-1002101 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002101) e a [ CVE-2017-1002102
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102) . Elas
possibilitam que os contêineres acessem arquivos que não estão dentro deles.
Todos os nós do Kubernetes Engine são afetados por essas vulnerabilidades.
Recomendamos que você faça o upgrade para a versão com patch mais recente
assim que possível.

####  O que fazer?

Devido à gravidade dessas vulnerabilidades, mesmo que você tenha ativado os
upgrades automáticos, recomendamos que faça o [ upgrade manual
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=pt_br) dos seus nós assim que o patch estiver disponível.
Isso deve acontecer até 16 de março, mas, de acordo com a [ programação de
lançamento ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#march-12-2018) , talvez você tenha acesso a ele antes com base
na zona do seu cluster.

Para fazer o upgrade, primeiro você precisa atualizar sua instância mestra
para a versão mais recente. Esse patch está disponível no Kubernetes versões
1.9.4-gke.1, 1.8.9-gke.1 e 1.7.14-gke.1. Os novos clusters usarão a versão com
patch por padrão até 30 de março. Se você criar um novo cluster antes disso,
especifique qual é a versão com patch para que ela seja usada.

Os clientes que ativaram os [ upgrades de nós automáticos
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=pt_br) e não realizaram a atualização manualmente terão os nós
atualizados para versões com patch até 23 de abril. No entanto, devido à
natureza dessa vulnerabilidade, é recomendável [ fazer o upgrade manual
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=pt_br) dos seus nós assim que o patch estiver disponível.

####  Quais vulnerabilidades são corrigidas por esse patch?

O patch reduz os riscos das duas vulnerabilidades a seguir:

Com a vulnerabilidade CVE-2017-1002101, os contêineres que usam ativações do [
volume subpath ](https://kubernetes.io/docs/concepts/storage/volumes/#using-
subpath) podem acessar arquivos fora do volume. Com isso, se você tiver
bloqueado o acesso do contêiner aos volumes do caminho do host com a
PodSecurityPolicy, um intruso com capacidade de atualizar ou criar pods poderá
ativar qualquer caminho de host usando outro tipo de volume.

A vulnerabilidade CVE-2017-1002102 possibilita que contêineres que usam certos
tipos de volume, incluindo chaves secretas, mapas de configuração, volumes
projetados ou APIs decrescentes, excluam arquivos que estão fora do volume.
Isso significa que, se um contêiner que usa um desses tipos de volume for
comprometido ou você permitir que usuários que não são de confiança criem
pods, um intruso poderá usar esse contêiner para excluir arquivos aleatórios
no host.

Para saber mais sobre a correção, leia a [ postagem do blog do Kubernetes
](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-vulnerability/)
.

|  Alta  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

