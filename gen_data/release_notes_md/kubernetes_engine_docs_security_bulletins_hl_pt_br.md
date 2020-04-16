#  Boletins de segurança

Todos os boletins de segurança para o Google Kubernetes Engine (GKE) são
descritos neste tópico.

Geralmente, as vulnerabilidades são mantidas sob sigilo e não podem ser
divulgadas até que as partes afetadas tenham a oportunidade de solucioná-las.
Nesses casos, nas [ notas de lançamento ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=pt_br) do GKE, serão mencionadas "atualizações de
segurança" até que a divulgação seja liberada. No momento da liberação, as
observações serão atualizadas para indicar a vulnerabilidade solucionada pelo
patch.

**Observação:** esses boletins são especialmente importantes para as pessoas
que têm cargas de trabalho com vários locatários no GKE. Geralmente, elas
costumam ser mais impactadas por essas vulnerabilidades. Para uma descrição
técnica dos limites de segurança no GKE e como eles afetam as cargas de
trabalho, consulte [ Isolamento em camadas diferentes da pilha do Kubernetes
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) (em inglês).

Para receber os boletins de segurança mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) (em inglês) ou
inclua o URL do feed diretamente: ` https://cloud.google.com/feeds/kubernetes-
engine-security-bulletins.xml ` .

##  21 de janeiro de 2020. Última atualização em 24 de janeiro de 2020

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
**Atualização de 24/01/2020:** o processo de disponibilização de versões com
patch está sendo realizado e será concluído em 25 de janeiro de 2020.

* * *

A Microsoft divulgou uma vulnerabilidade na validação de assinaturas Elliptic
Curve da Windows CryptoAPI. Para mais informações, consulte o [ anúncio da
Microsoft ](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) .

**O que fazer?**

**Para a maioria dos clientes, nenhuma outra ação é necessária. Somente os nós
executados no Windows Server são afetados.**

Nesse caso, para reduzir a vulnerabilidade, é necessário atualizar os nós e as
cargas de trabalho em contêiner executadas neles para as versões com patch.

**Para atualizar os contêineres:**

É necessário recriá-los. Para isso, use as imagens de contêiner de base mais
recentes da Microsoft e selecione uma [ tag de servercore
](https://hub.docker.com/_/microsoft-windows-servercore) ou [ de nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) (páginas em inglês)
que tenha o valor "1/14/2020" ou superior em "LastUpdated Time".

**Para atualizar os nós:**

O processo de disponibilização de versões com patch está sendo realizado e
será concluído em 24 de janeiro de 2020.

Faça o upgrade dos nós para uma versão de patch do GKE ou use o Windows Update
para implantar manualmente o patch mais recente do Windows a qualquer momento.

As versões de patch que incluem a mitigação são estas:

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
de spoofing da API Windows Crypto ](https://portal.msrc.microsoft.com/en-
US/security-guidance/advisory/CVE-2020-0601) . Usada para fazer executáveis
maliciosos parecerem confiáveis ou permitir que o invasor realize ataques
"man-in-the-middle" e descriptografe informações confidenciais nas conexões
TLS com o software afetado.

|

Pontuação base do NVD: 8,1 (alta)

|

[ CVE-2020-0601 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  14 de novembro de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
O Kubernetes divulgou um problema de segurança nos arquivos secundários
kubernetes-csi [ ` external-provisioner ` ](https://github.com/kubernetes-
csi/external-provisioner) , [ ` external-snapshotter `
](https://github.com/kubernetes-csi/external-snapshotter) e [ ` external-
resizer ` ](https://github.com/kubernetes-csi/external-resizer) que impacta a
maioria das versões dos arquivos secundários agrupados nos [ drivers do
Container Storage Interface (CSI) ](https://kubernetes-
csi.github.io/docs/drivers.html) [páginas em inglês]. Para mais detalhes,
consulte o [ anúncio do Kubernetes
](https://github.com/kubernetes/kubernetes/issues/85233) (em inglês).

**O que fazer?**  
**Essa vulnerabilidade não afeta componentes gerenciados do GKE** . Você é
impactado se gerenciar os próprios drivers do CSI em [ clusters Alfa do GKE
](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-
clusters?hl=pt_br) executados na versão 1.12 ou mais recente. Nesse caso,
verifique as instruções de upgrade com seu distribuidor de drivers do CSI.

**Quais vulnerabilidades são corrigidas por esse patch?**  
[ CVE-2019-11255 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : é uma vulnerabilidade nos arquivos
secundários ` kubernetes-csi ` [ ` external-provisioner `
](https://github.com/kubernetes-csi/external-provisioner) , [ ` external-
snapshotter ` ](https://github.com/kubernetes-csi/external-snapshotter) e [ `
external-resizer ` ](https://github.com/kubernetes-csi/external-resizer)
(páginas em inglês) que possibilitam acesso ou mutação não autorizados dos
dados de volume. Isso impacta a maioria das versões de arquivos secundários
agrupados em [ drivers do CSI ](https://kubernetes-
csi.github.io/docs/drivers.html) (em inglês).

|

Média

|

[ CVE-2019-11255 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  12 de novembro de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
A Intel divulgou CVEs que possivelmente permitem interações entre a execução
especulativa e o estado microarquitetônico para expor dados. Para mais
detalhes, consulte o [ anúncio da Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) (em inglês).

**A infraestrutura de host que executa o Kubernetes Engine isola as cargas de
trabalho do cliente. Nenhuma outra ação é necessária, a menos que você esteja
executando código não confiável nos próprios clusters de multilocatário do GKE
_e_ utilizando nós N2, M2 ou C2. ** Para as instâncias do GKE em nós N1,
nenhuma outra ação é necessária.

Se você executa o Anthos GKE implantado no local, a exposição depende do
hardware. Consulte o [ anúncio da Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) (em inglês) para comparar sua infraestrutura.

####  O que fazer?

**Você só será impactado se estiver usando pools com nós N2, M2 ou C2 _e_
esses nós estiverem executando código não confiável nos próprios clusters de
multilocatário do GKE. **

**Reiniciar seus nós aplica o patch.** A forma mais fácil de reiniciar todos
os nós no pool é usar a [ operação de upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br#upgrade_nodes) para forçar uma reinicialização em todos os
pools de nós afetados.  

Observação: não é necessário trocar de versão durante um upgrade. É possível
iniciar um upgrade para a mesma versão do nó com a sinalização ` cluster-
version ` .

####  Quais vulnerabilidades são corrigidas por esse patch?

O patch reduz as vulnerabilidades a seguir:

[ CVE-2019-11135 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11135) : também é chamada de TSX Async Abort (TAA).
Ela fornece outra via para exfiltração de dados, usando as mesmas estruturas
da microarquitetura de dados exploradas pela [ Amostragem de dados de
microarquitetura (MDS, na sigla em inglês)
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins?hl=pt_br#may-14-2019) .

[ CVE-2018-12207 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12207) : vulnerabilidade de negação de serviço (DoS)
que afeta hosts de máquina virtual. Ela permite que um convidado mal-
intencionado cause uma falha em um host desprotegido. Também é chamada de
"Erro de verificação de máquina na alteração do tamanho da página". Ela não
afeta o GKE.

|

Média

|

[ CVE-2019-11135 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12207)  
  
##  22 de outubro de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Uma vulnerabilidade foi descoberta recentemente na linguagem de programação
Go, descrita na [ CVE-2019-16276 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) . Ela tem potencial para impactar
configurações do Kubernetes usando um proxy de autenticação. Para mais
detalhes, consulte o [ anúncio do Kubernetes
](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-security-
announce/PtsUCqFi4h4) (em inglês).

O Kubernetes Engine não permite a configuração de um proxy de autenticação.
Portanto, ele não é afetado por essa vulnerabilidade.

|

Nenhuma

|

[ CVE-2019-16276 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  16 de outubro de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
**Atualização de 24/10/2019:** agora, versões em patch estão disponíveis em
todas as zonas.

* * *

Uma vulnerabilidade foi descoberta recentemente no Kubernetes, descrita na [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) (em inglês). Ela permite que qualquer
usuário autorizado a fazer solicitações POST execute um ataque remoto de
negação de serviço em um servidor da API do Kubernetes. O Comitê de Segurança
de Produto (PSC, na sigla em inglês) do Kubernetes divulgou mais informações
sobre essa vulnerabilidade. Para consultá-las, acesse [ esta página
](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-security-
announce/jk8polzSUxs) (em inglês).

Os clusters do GKE que usam [ redes mestres autorizadas
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=pt_br) e [ clusters privados sem endpoint público
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=pt_br#private_master) reduzem essa vulnerabilidade.

######  O que fazer?

É recomendado fazer o upgrade do cluster para uma versão de patch com a
correção assim que ela estiver disponível. Esperamos que esteja disponível em
todas as zonas com o lançamento do GKE previsto para a semana de 14 de
outubro.

As versões do patch com a redução são:

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  Quais vulnerabilidades são corrigidas por esse patch?

O patch reduz as vulnerabilidades a seguir:

A CVE-2019-11253 é uma vulnerabilidade de negação de serviço (DoS).

|

Alta

|

[ CVE-2019-11253 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  16 de setembro de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Este boletim já foi atualizado desde a publicação original.

As vulnerabilidades de segurança recentemente descobertas [ CVE-2019-9512
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9512) e [
CVE-2019-9514 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514)
(páginas em inglês) na linguagem de programação Go são de negação de serviço
(DoS). No GKE, elas permitem que um usuário crie solicitações mal-
intencionadas que consomem uma quantidade excessiva de CPU no servidor da API
do Kubernetes. Isso pode reduzir a disponibilidade do plano de controle do
cluster. Para mais detalhes, consulte o [ anúncio da linguagem de programação
Go ](https://groups.google.com/forum/?hl=pt_br#!topic/golang-
announce/65QixT3tcmg) (em inglês).

######  O que fazer?

É recomendável fazer o upgrade do cluster para a versão de patch mais recente
com a mitigação dessa vulnerabilidade assim que ela estiver disponível. Ela
será disponibilizada em todas as zonas com o próximo lançamento do GKE de
acordo com a [ programação de lançamentos
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#september_16_2019) .

As versões do patch com a redução são:

  * **Atualização de 16 de outubro de 2019:** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz as vulnerabilidades a seguir:

A [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) e a [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) (páginas em
inglês) são vulnerabilidades de negação de serviço (DoS).

|

Alta

|

[ CVE-2019-9512 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  5 de setembro de 2019

As informações sobre a correção da vulnerabilidade documentada no boletim de
31 de maio de 2019  estão atualizadas.

##  22 de agosto de 2019

O boletim de  5 de agosto de 2019  foi atualizado. A correção da
vulnerabilidade documentada no boletim anterior [ está disponível
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#august_22_2019) .

##  8 de agosto de 2019

O boletim de  5 de agosto de 2019  foi atualizado. A correção da
vulnerabilidade documentada nesse boletim estará disponível no próximo
lançamento do GKE.

##  5 de agosto de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Este boletim já foi atualizado desde a publicação original.

Recentemente, o Kubernetes descobriu a [ vulnerabilidade CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) , que
possibilita que instâncias de [ recurso personalizado
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) (páginas em inglês) com escopo de cluster sejam usadas como se
fossem objetos atuais em todos os namespaces. Isso significa que contas de
usuário e de serviço com apenas permissões do RBAC no nível do namespace podem
interagir com recursos personalizados com escopo de cluster. A exploração
dessa vulnerabilidade exige que o invasor tenha privilégios para acessar o
recurso nos namespaces.

######  O que fazer?

É recomendável [ fazer o upgrade ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=pt_br) do cluster para a versão de
patch mais recente com a mitigação dessa vulnerabilidade assim que ela estiver
disponível. Ela estará disponível em todas as zonas com o próximo lançamento
do GKE. As versões de patch que incluem a mitigação são estas:

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ Canal rápido ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=pt_br) ) 

######  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz esta vulnerabilidade: [ CVE-2019-11247 (em inglês)
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Média

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  3 de julho de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Uma versão com patch da ` kubectl ` para solucionar a CVE-2019-11246 está
disponível com a [ ` gcloud ` 253.0.0
](https://cloud.google.com/sdk/docs/release-notes?hl=pt_br#kubernetes_engine)
. Consulte o  boletim de segurança de 25 de junho de 2019  para mais
informações.

**Observação:** o patch não está disponível na ` kubectl ` 1.11.10.

|

Alta

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  3 de julho de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
######  Atualização de 3 de julho de 2019

No momento da última atualização, os patches para as versões 1.11.9 e 1.11.10
ainda não estavam disponíveis. A 1.11.10-gke.5 foi lançada como um upgrade das
duas versões 1.11.

Com esse lançamento, foram aplicados patches aos mestres do GKE e à
infraestrutura do Google que executa o Kubernetes Engine. Ela agora está
protegida contra essa vulnerabilidade.

Os mestres 1.11 ficarão obsoletos e serão atualizados automaticamente para a
versão 1.12 na semana de 8 de julho de 2019. Siga uma das ações sugeridas a
seguir para incluir os nós em uma versão com patch:

  * Faça upgrade do nó para 1.11.10-gke.5 até 8 de julho de 2019. Após essa data, as versões 1.11 serão removidas da lista de upgrades disponíveis. 
  * Ative os [ upgrades automáticos ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=pt_br) dos nós 1.11 para que eles sejam atualizados quando o upgrade dos mestres para 1.12 for feito. 
  * [ Faça o upgrade manual ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=pt_br) dos mestres e dos nós para uma versão 1.12 corrigida. 

Segue o boletim original de 24 de junho de 2019:

* * *

######  Atualização de 24 de junho de 2019

Às 21h40 UTC de 22/06/2019, as versões com patch do Kubernetes a seguir foram
disponibilizadas. Os mestres com versão 1.11.0 a 1.13.6 do Kubernetes serão
atualizados automaticamente para uma versão com patch. Se você não usa uma
versão compatível com esse patch, faça o upgrade para uma versão de mestre
aceita listada abaixo antes de atualizar os nós.

**Devido à gravidade dessas vulnerabilidades, tendo ou não ativado o upgrade
automático de nós, é recomendável que você faça o[ upgrade manual
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=pt_br) dos nós e dos mestres para uma dessas versões
assim que possível. **

As versões com patch são estas:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

Segue o boletim original de 18 de junho de 2019:

* * *

A Netflix divulgou recentemente três vulnerabilidades do TCP nos kernels do
Linux (em inglês):

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Essas CVEs são coletivamente denominadas [ NFLX-2019-001 (em inglês)
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) .

Os kernels do Linux sem patch podem ser vulneráveis a ataques de negação de
serviço disparados remotamente. **Os nós do Google Kubernetes Engine que
enviam e recebem tráfego de rede não confiável são afetados. É recomendável
seguir as etapas de mitigação abaixo para proteger suas cargas de trabalho.**

######  Instâncias mestre do Kubernetes

  * Os mestres do Kubernetes que usam [ redes autorizadas ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=pt_br) para limitar o tráfego de redes confiáveis não são afetadas. 

  * Os mestres de clusters do GKE que são gerenciados pelo Google receberão patches automaticamente nos próximos dias. Nenhuma ação do cliente é necessária. 

######  Nós do Kubernetes

Nós que limitam o tráfego a redes confiáveis não são afetados. Um cluster
afetado poderá apresentar o seguinte:

  * Nós protegidos por firewall contra redes não confiáveis ou sem IPs públicos ( [ clusters privados ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=pt_br) ) 
  * Clusters sem serviços públicos do tipo LoadBalancer 

O Google está preparando uma mitigação permanente dessas vulnerabilidades que
será disponibilizada como uma nova versão do nó. Quando a correção permanente
estiver disponível, este boletim será atualizado, e todos os clientes do GKE
receberão um e-mail.

Até lá, é possível usar um DaemonSet criado para o Kubernetes, que implementa
mitigações ao modificar a configuração do host ` iptables ` .

#####  O que fazer?

Execute o comando a seguir para aplicar o DaemonSet do Kubernetes a todos os
nós no cluster. Ele adiciona uma regra ` iptables ` às regras de ` iptables `
atuais no nó para reduzir a vulnerabilidade. **Execute o comando uma vez por
cluster para cada projeto do Google Cloud.**

    
    
    
    kubectl apply -f \
        https://raw.githubusercontent.com/GoogleCloudPlatform\
        /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
              

Como o Ipv6 não é compatível com o GKE, nenhuma regra ip6tables é necessária.

Quando uma versão do nó com patch estiver disponível, e todos os nós
possivelmente afetados tiverem sido atualizados, será possível remover o
DaemonSet usando o comando a seguir. **Execute o comando uma vez por cluster
para cada projeto do Google Cloud.**

    
    
    
    kubectl delete -f \
        https://raw.githubusercontent.com/GoogleCloudPlatform\
        /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
              

|  Alta  
Média  
Média  
|  [ CVE-2019-11477 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
  
  
##  25 de junho de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
**Atualização de 03/07/2019:** esse patch está disponível na ` gcloud `
253.0.0 para as versões 1.12.9, 1.13.6, 1.14.2 e mais recentes da ` kubectl `
.

**Observação:** o patch não está disponível na versão 1.11.10.

* * *

Recentemente, o Kubernetes descobriu a [ vulnerabilidade CVE-2019-11246
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11246) (em inglês),
que possibilita que um invasor com acesso a uma operação e execução de código
da ` kubectl cp ` dentro de um contêiner modifique arquivos no host. Essa
exploração possibilita que um invasor substitua ou crie um arquivo no sistema
de arquivos do host. Para mais detalhes, consulte o [ anúncio do Kubernetes
](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-security-
announce/NLs2TGbfPdo) (em inglês).

**Todas as versões da` gcloud ` do Google Kubernetes Engine (GKE) são afetadas
por essa vulnerabilidade. É recomendável fazer o upgrade para a versão de
patch mais recente da ` gcloud ` quando ela estiver disponível. ** Uma versão
de patch futura incluirá uma mitigação dessa vulnerabilidade.

######  O que fazer?

Uma versão com patch do ` kubectl ` será disponibilizada em um futuro
lançamento do ` gcloud ` . Também é possível fazer [ upgrade do ` kubectl `
](https://kubernetes.io/docs/tasks/tools/install-kubectl/) por conta própria.

Acompanhe a disponibilidade desse patch nas [ notas de lançamento do ` gcloud
` ](https://cloud.google.com/sdk/docs/release-notes?hl=pt_br) .

######  Qual vulnerabilidade é corrigida por esse patch?

A vulnerabilidade [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) possibilita que um invasor com acesso a
uma operação e execução de código do ` kubectl cp ` dentro de um contêiner
modifique arquivos no host. Essa exploração tem potencial para possibilitar
que um invasor substitua ou crie um arquivo no sistema de arquivos do host

|

Alta

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  18 de junho de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Recentemente, o Docker descobriu a [ vulnerabilidade CVE-2018-15664
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-15664) (em inglês),
que possibilita que um invasor capaz de executar um código dentro de um
contêiner sequestre uma operação ` docker cp ` iniciada externamente. Ela
permite que um invasor altere o local onde um arquivo está sendo gravado para
outro arbitrário no sistema de arquivos do host.

**Todos os nós do Google Kubernetes Engine (GKE) que executam o Docker são
afetados por essa vulnerabilidade. É recomendável fazer o upgrade para a
versão de patch mais recente assim que estiver disponível. Uma versão de patch
futura incluirá uma mitigação dessa vulnerabilidade.**

**Todos os mestres do Google Kubernetes Engine (GKE) anteriores à versão
1.12.7 executam o Docker e são afetados por essa vulnerabilidade.** No GKE, os
usuários não têm acesso ao ` docker cp ` no mestre. Portanto, o risco dessa
vulnerabilidade se limita aos mestres do GKE.

#####  O que fazer?

Apenas os nós que executam o Docker são afetados, e isso somente quando for
emitido um comando ` docker cp ` (ou equivalente na API) que possa ser
sequestrado. Espera-se que isso seja muito incomum em um ambiente do
Kubernetes. Os nós que executam o [ COS com o containerd
](https://cloud.google.com/kubernetes-engine/docs/concepts/using-
containerd?hl=pt_br) não são afetados.

Para fazer o upgrade dos nós, primeiro é necessário [ fazer o upgrade do
mestre ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br#upgrading_the_cluster) para a versão com patch. Quando o
patch estiver disponível, será possível iniciar o upgrade da instância mestre
ou esperar que o Google faça o upgrade automaticamente. O patch estará
disponível no Docker 18.09.7, que será incluído em um futuro patch do GKE.
**Esse patch será disponibilizado apenas para as versões 1.13 e mais recentes
do GKE.**

Faremos upgrade automático dos mestres do cluster para a versão com patch no
ritmo normal de upgrades. Também é possível iniciar o upgrade de um mestre por
conta própria depois que a versão com patch estiver disponível.

Este boletim será atualizado com as versões com patch assim que estiverem
disponíveis. Acompanhe a disponibilidade desses patches nas [ notas de
lançamento ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br) .

#####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz a vulnerabilidade a seguir:

A [ vulnerabilidade CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) (em inglês) possibilita que um invasor
capaz de executar um código dentro de um contêiner sequestre uma operação `
docker cp ` iniciada externamente. Essa exploração permite que um invasor
altere o local onde um arquivo está sendo gravado para outro arbitrário no
sistema de arquivos do host.

|  Alta  |  
  
##  31 de maio de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Este boletim já foi atualizado desde a publicação original.

######  Atualização de 2 de agosto de 2019

No momento da publicação do boletim inicial, apenas as versões de 1.13.6-gke.0
a 1.13.6-gke.5 foram impactadas. Devido a uma regressão, todas as versões
1.13.6.x agora são afetadas. Se você tiver a versão 1.13.6, faça o upgrade
para a 1.13.7 o quanto antes.

O projeto Kubernetes divulgou a [ vulnerabilidade CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) (em inglês) na
kubelet v1.13.6 e v1.14.2. Ela pode fazer os contêineres funcionarem como UID
0 (normalmente mapeia para o usuário ` root ` ), mesmo que um usuário
diferente seja especificado na imagem do contêiner. **Se os contêineres
funcionam como um usuário não raiz, e você está executando um nó de versão
1.13.6-gke.0 a 1.13.6-gke.6, é recomendável configurar o` RunAsUser ` em todos
os pods no cluster com os contêineres que não podem funcionar como UID 0. **

Se um valor de ` USER ` não raiz for especificado (por exemplo, ao configurar
o valor de ` USER ` em um Dockerfile), ocorrerá um comportamento inesperado.
Quando um contêiner é executado pela primeira vez em um nó, ele respeita
corretamente o UID especificado. No entanto, devido a esse defeito, na segunda
execução e nas posteriores, o contêiner é executado como UID 0 mesmo com o UID
especificado. Em geral, isso é um privilégio escalonado não pretendido, e pode
levar a um comportamento inesperado do aplicativo.

#####  Como saber se tenho uma versão afetada?

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

Se os contêineres funcionam como um usuário não raiz, e um nó de versão
1.13.6-gke.0 a 1.13.6-gke.6 é executado, você é impactado exceto nos casos a
seguir:

  * Os pods que especificam um valor não raiz válido para o PodSecurityContext de ` runAsUser ` não são afetados e continuam funcionando como esperado. 
  * As PodSecurityPolicies que aplicam uma configuração de ` runAsUser ` também não são afetadas e continuam funcionando como esperado. 
  * Os pods que especificam ` mustRunAsNonRoot:true ` não são iniciados como UID 0. No entanto, ocorrerá erro na inicialização deles quando impactados por esse problema. 

#####  O que fazer?

Configure o [ contexto de segurança do RunAsUser
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) (em inglês) em todos os pods no
cluster que não pode ser executado como UID 0. É possível [ usar uma
PodSecurityPolicy ](https://kubernetes.io/docs/concepts/policy/pod-security-
policy/) (em inglês) para aplicar essa configuração.

|  Média  |  [ CVE-2019-11245 (em inglês) ](https://cve.mitre.org/cgi-
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

Elas são coletivamente denominadas Amostragem de dados de microarquitetura
(MDS, na sigla em inglês). Essas vulnerabilidades possibilitam a exposição de
dados por meio da interação da execução especulativa com o estado de
microarquitetura. Para mais detalhes, consulte o [ anúncio da Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) (em inglês).

**A infraestrutura do host que executa o Kubernetes Engine isola as cargas de
trabalho do cliente umas das outras. Você não é impactado a menos que esteja
executando um código não confiável nos clusters de multilocatário do GKE.**

**Para os clientes que executam um código não confiável nos serviços de
multilocatário no Kubernetes Engine, esta é uma vulnerabilidade de severidade
alta.** Para reduzi-la no Kubernetes Engine, desative o Hyper-Threading nos
seus nós. Apenas os nós do Google Kubernetes Engine (GKE) que usam vários CPUs
são afetados por essas vulnerabilidades. As VMs n1-standard-1 (padrão do GKE),
g1-small e f1-micro expõem apenas uma vCPU para o ambiente convidado. Por
isso, não é necessário desativar o Hyper-Threading.

Mais proteção para ativar a funcionalidade de liberação será incluída em uma [
versão de patch ](https://cloud.google.com/kubernetes-engine/release-
notes?hl=pt_br) futura. Será feito o upgrade automático dos mestres e dos nós
para a versão com patch nas próximas semanas na frequência normal de upgrade.
**Apenas o patch não é suficiente para reduzir a exposição a essa
vulnerabilidade. Veja as ações recomendadas abaixo.**

Se o GKE for executado no local, talvez você seja impactado dependendo do
hardware utilizado. Consulte o [ anúncio da Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) (em inglês).

####  O que fazer?

**Você não é impactado a menos que esteja executando um código não confiável
nos clusters de multilocatário do GKE.**

**No caso dos nós no Kubernetes Engine, crie novos pools de nós com o Hyper-
Threading desativado e reprograme as cargas de trabalho neles.**

As VMs n1-standard-1, g1-small e f1-micro expõem apenas uma vCPU para o
ambiente convidado. Por isso, não é necessário desativar o Hyper-Threading.

**Aviso:**

  * Desativar o Hyper-Threading pode ter um grande impacto nos clusters e no aplicativo. Verifique se isso é apropriado antes de fazer a implantação nos clusters de produção. 
  * É possível desativar o Hyper-Threading no nível do pool de nós do GKE com a implantação de um DaemonSet. No entanto, isso reinicializará todos os nós no pool ao mesmo tempo. Portanto, é recomendável criar um novo pool de nós no cluster, implantar o DaemonSet para desativar o Hyper-Threading naquele pool de nós e migrar as cargas de trabalho para o novo pool. 

Para criar um novo pool de nós com o Hyper-Threading desativado:

  1. Crie um novo pool de nós no cluster com o rótulo do nó ` cloud.google.com/gke-smt-disabled=true ` : 
    
        
        gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
            --node-labels=cloud.google.com/gke-smt-disabled=true

  2. Implante o DaemonSet para esse novo pool de nós. O DaemonSet será executado somente em nós com o rótulo ` cloud.google.com/gke-smt-disabled=true ` . Ele desativará o Hyper-Threading e reinicializará o nó. 
    
        
        kubectl create -f \
        https://raw.githubusercontent.com/GoogleCloudPlatform/\
        k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. Verifique se os pods do DaemonSet estão no estado de execução. 
    
        
        kubectl get pods --selector=name=disable-smt -n kube-system

Você receberá uma resposta semelhante a:

    
        
        NAME                READY     STATUS    RESTARTS   AGE
    
        disable-smt-2xnnc   1/1       Running   0          6m

  4. Verifique se “SMT foi desativada” aparece nos registros dos pods. 
    
        
        kubectl logs disable-smt-2xnnc disable-smt -n kube-system

É necessário manter o DaemonSet em execução nos pools de nós para que as
alterações sejam aplicadas automaticamente aos novos nós criados no pool. É
possível acionar as criações de nós por meio do reparo automático de nós, do
upgrade manual ou automático e do escalonamento automático.

Para reativar o Hyper-Threading, é necessário recriar o pool de nós sem
implantar o DaemonSet fornecido e migrar as cargas de trabalho para o novo
pool.

Também é recomendável fazer o upgrade manual dos nós assim que o patch estiver
disponível. Para fazer o upgrade, primeiro é necessário [ fazer o upgrade do
mestre ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br#upgrading_the_cluster) para a versão mais recente. O upgrade
dos mestres do GKE será feito automaticamente na frequência normal de upgrade.

Este boletim será atualizado com as versões com um patch assim que eles
estiverem disponíveis.

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz as vulnerabilidades a seguir:

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
, [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) , [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) e [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)
(páginas em inglês): essas vulnerabilidades exploram uma execução
especulativa. Elas são coletivamente denominadas Amostragem de dados de
microarquitetura. Essas vulnerabilidades possibilitam a exposição de dados por
meio da interação da execução especulativa com o estado de microarquitetura.
|  Média  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  5 de abril de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Recentemente, as vulnerabilidades de segurança [ CVE-2019-9900
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900) e [
CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)
foram [ descobertas no Envoy ](https://www.envoyproxy.io/) (páginas em
inglês).

O Envoy é [ incorporado ao Istio ](https://istio.io/) (em inglês), e essas
vulnerabilidades possibilitam que a política do Istio seja ignorada em alguns
casos.

Se você ativou o Istio no Google Kubernetes Engine (GKE), talvez seja
impactado por essas vulnerabilidades. **É recomendável fazer o upgrade dos
clusters afetados para a versão de patch mais recente o quanto antes, além dos
arquivos secundários do Istio (instruções abaixo).**

####  O que fazer?

**Devido à gravidade dessas vulnerabilidades, tendo ou não ativado o upgrade
automático de nós, é recomendável o seguinte:**

  1. **[ Fazer o upgrade manual ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=pt_br) do cluster assim que o patch estiver disponível. **
  2. **Fazer o upgrade dos arquivos secundários seguindo a[ documentação relacionada ](https://istio.io/docs/setup/kubernetes/upgrade/steps/#sidecar-upgrade) (em inglês). **

As versões em patch serão disponibilizadas para todos os projetos do GKE hoje,
antes das 7:00 PM PDT.

Esse patch será disponibilizado nas versões do GKE abaixo. Os novos clusters
usarão a versão com patch por padrão quando anunciada na página de boletins de
segurança do GKE. A previsão é para 15 de abril de 2019. Se um novo cluster
for criado antes disso, será necessário especificar a versão com patch que ele
precisará usar. Na semana seguinte, a atualização dos nós de clientes do GKE
que ativaram os [ upgrades de nó automáticos
](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-
upgrades?hl=pt_br) e não fazem upgrade manual será feita automaticamente para
as versões com patch.

Versões com patch:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz as vulnerabilidades a seguir:

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) e [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) (páginas em
inglês). Saiba mais sobre elas no [ blog da Istio
](https://istio.io/blog/2019/announcing-1.1.2) (em inglês).

|  Alta  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901. ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  1º de março de 2019

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
**Atualização de 22/03/2019:** esse patch está disponível no Kubernetes
1.11.8-gke.4, 1.13.4-gke.1 e versões mais recentes. O patch ainda não está
disponível na versão 1.12. Acompanhe a disponibilidade desses patches nas [
notas de lançamento ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#march_19_2019) .

Recentemente, o Kubernetes descobriu a vulnerabilidade de negação de serviço [
CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) (em inglês). Ela possibilita que um
usuário autorizado faça solicitações de patch para criar uma solicitação
"json-patch" mal-intencionada que consome quantidades excessivas de CPU e
memória no servidor da API do Kubernetes. Isso pode reduzir a disponibilidade
do plano de controle do cluster. Para mais detalhes, consulte o [ anúncio do
Kubernetes ](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-
announce/vmUUNkYfG9g) (em inglês). **Todos os mestres do Google Kubernetes
Engine (GKE) são afetados por essas vulnerabilidades. Uma versão de patch
futura incluirá uma mitigação dessa vulnerabilidade. O upgrade automático dos
mestres do cluster para a versão com patch será feito nas próximas semanas na
frequência normal de upgrade.**

####  O que fazer?

**Nenhuma ação é necessária. O upgrade dos mestres do GKE será feito
automaticamente na frequência normal de upgrade.** Se quiser fazer isso antes,
[ inicie o upgrade do mestre manualmente
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br#upgrading_the_cluster) .

Este boletim será atualizado com as versões contendo um patch. O patch estará
disponível apenas na versão 1.11 e posteriores, e não na 1.10.

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz a vulnerabilidade a seguir:

A [ vulnerabilidade CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) (em inglês) possibilita que um usuário
crie um patch do tipo "json-patch" que consome quantidades excessivas de CPU
no servidor da API do Kubernetes. Isso pode reduzir a disponibilidade do plano
de controle do cluster.

|  Média  |  [ CVE-2019-1002100 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  11 de fevereiro de 2019 (RunC)

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
A Open Containers Initiative (OCI) [ descobriu recentemente
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=pt_br#!topic/dev/Tc1ELm-8oDI)
a vulnerabilidade de segurança [ CVE-2019-5736 no RunC
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736) (páginas em
inglês). Ela possibilita que um contêiner insira caracteres de escape para
conseguir privilégios raiz no nó do host.

**Os nós do Ubuntu do Google Kubernetes Engine (GKE) são afetados por essas
vulnerabilidades. É recomendável que você[ faça o upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br) para a versão mais recente do patch assim que possível,
conforme detalhado abaixo. **

####  O que fazer?

Para fazer o upgrade dos seus nós, primeiro você precisa fazer o upgrade do
mestre para a versão mais recente. Esse patch está disponível para o
Kubernetes 1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4, 1.12.5-gke.5 e para as
versões mais recentes. Acompanhe a disponibilidade desses patches nas [ notas
de lançamento ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#february-11-2019) .

Apenas os nós do Ubuntu no GKE são afetados. Os nós que executam o COS não são
afetados.

A nova versão do RunC tem uso maior de memória e pode exigir a atualização da
memória alocada em contêineres se você tiver limites baixos (< 16 MB)
configurados.

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz os riscos da seguinte vulnerabilidade:

A [ vulnerabilidade CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) (em inglês) no RunC permite que um
contêiner mal-intencionado, com interação mínima do usuário no formato de uma
execução, substitua o binário RunC do host e, assim, consiga a execução de
código no nível raiz no nó do host. Contêineres não executados como raiz não
são afetados. Isso é classificado como uma vulnerabilidade de alta gravidade.

|  Alta  |  [ CVE-2019-5736 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  11 de fevereiro de 2019 (Go)

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
**Atualização de 25/02/2019:** o patch não está disponível na versão
1.11.7-gke.4, conforme comunicado anteriormente. Se você usa a versão 1.11.7,
é possível fazer o downgrade para a 1.11.6, o upgrade para a 1.12 ou aguardar
pelo patch da 1.11.7, disponível na semana de 04/03/2019.

Recentemente, foi descoberta na linguagem de programação Go a vulnerabilidade
de segurança [ CVE-2019-6486 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486) . Ela é uma negação de serviço (DoS) nas
implementações elípticas/de criptografia das curvas elípticas P-521 e P-384.
No Google Kubernetes Engine (GKE), isso libera um usuário a criar solicitações
mal-intencionadas que consomem uma quantidade excessiva de CPU no servidor da
API do Kubernetes. Isso pode reduzir a disponibilidade do plano de controle do
cluster. Para mais detalhes, consulte o [ anúncio da linguagem de programação
Go ](https://groups.google.com/forum/?hl=pt_br#!topic/golang-
announce/mVeX35iXuSw) (em inglês).

**Todos os mestres do Google Kubernetes Engine (GKE) são afetados por essas
vulnerabilidades. A[ versão de patch mais recente
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#february-11-2019) inclui uma mitigação dessa vulnerabilidade. O
upgrade automático dos mestres do cluster para a versão com patch será feito
nas próximas semanas, na frequência normal de upgrade. **

####  O que fazer?

**Nenhuma ação é necessária. O upgrade dos mestres do GKE será feito
automaticamente na frequência normal de upgrade.** Se quiser fazer isso antes,
[ inicie o upgrade do mestre manualmente
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br#upgrading_the_cluster) .

Esse patch está disponível no GKE 1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4,
1.12.5-gke.5 e nas versões mais recentes.

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz a vulnerabilidade a seguir:

A CVE-2019-6486 é uma vulnerabilidade nas implementações elípticas/de
criptografia das curvas elípticas P-521 e P-384. Ela permite que um usuário
crie entradas que consomem uma quantidade excessiva de CPU.

|  Alta  |  [ CVE-2019-6486 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  3 de dezembro de 2018

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Recentemente, foi descoberta no Kubernetes a vulnerabilidade de segurança [
CVE-2018-1002105 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) . Ela permite que usuários com níveis
de privilégio relativamente baixos ignorem a autorização de acesso às APIs da
kubelet. Com isso, eles podem executar operações arbitrárias de qualquer pod
em qualquer nó do cluster. Para mais detalhes, consulte o [ anúncio do
Kubernetes ](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-
announce/GVllWCg6L88) (em inglês). **Todos os mestres do Google Kubernetes
Engine (GKE) foram afetados por essas vulnerabilidades. O upgrade dos clusters
para as[ versões de patch mais recentes ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=pt_br#november-12-2018) já foi feito. Nenhuma
ação é necessária. **

####  O que fazer?

**Nenhuma ação é necessária. O upgrade das instâncias mestre do GKE já foi
feito.**

Esse patch está disponível no GKE 1.9.7-gke.11, 1.10.6-gke.11, 1.10.7-gke.11,
1.10.9-gke.5, 1.11.2-gke.18 e nas versões mais recentes.

####  Qual vulnerabilidade é corrigida por esse patch?

O patch reduz a vulnerabilidade a seguir:

A vulnerabilidade CVE-2018-1002105 possibilita que um usuário com privilégios
relativamente baixos ignore a autorização para as APIs da kubelet. Assim, um
usuário com autorização para fazer solicitações de upgrade pode escalonar e
realizar chamadas arbitrárias à API da kubelet. Essa é uma vulnerabilidade
crítica no Kubernetes. Com base em alguns detalhes da implementação do GKE que
impediram o caminho não autorizado de escalonamento, essa vulnerabilidade é
classificada como alta.

|  Alta  |  [ CVE-2018-1002105 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  13 de novembro de 2018

Descrição  
---  
  
**Atualização de 16/11/2018:** a revogação e a rotação de todos os tokens
possivelmente afetados foram concluídas. Você não precisa fazer mais nada.

O Google descobriu recentemente um problema no plug-in da interface de rede de
contêiner (CNI, na sigla em inglês) do Calico. Em determinadas configurações,
isso pode registrar informações confidenciais. O problema está sendo
monitorado pela Tigera Technical Advisory [ TTA-2018-001 (em inglês)
](https://www.projectcalico.org/security-bulletins/) .

  * Se executado com geração de registros no nível de depuração, o plug-in da CNI do Calico gravará a configuração do cliente da API do Kubernetes nos registros. 
  * A CNI também gravará o token da API Kubernetes no nível de informação dos registros se o campo "k8s_auth_token" estiver definido na configuração de rede da CNI. 
  * Além disso, no caso de execução do plug-in com geração de registros no nível de depuração, se o token da conta de serviço estiver definido de modo explícito no arquivo de configuração lido pelo Calico ou como uma variável de ambiente usada pelo Calico, os respectivos componentes (calico/node, felix, CNI) gravarão essa informação nos arquivos de registro. 

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
cluster e o Stackdriver Logging ativado registraram os tokens da conta de
serviço do Calico no Stackdriver. Clusters sem a ativação da política de rede
não foram afetados.

Foi implantada uma correção que migra o plug-in da CNI do Calico para
registrar apenas no nível de aviso e usar uma nova conta de serviço. O código
com patch será implantado em um lançamento posterior.

Ao longo da próxima semana, executaremos uma revogação gradual de todos os
possíveis tokens afetados. Este boletim será atualizado quando a revogação for
concluída. **Não é necessária nenhuma ação da sua parte.** Essa rotação foi
concluída em 16/11/2018.

Se você quiser rotacionar esses tokens imediatamente, execute o comando a
seguir. O novo secret da conta de serviço será recriado automaticamente em
alguns segundos:  
      
    
    
        kubectl get sa --namespace kube-system calico -o template --template '{{(index .secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system
                
  
---  
  
####  Detecção

O GKE registra todos os acessos ao servidor da API. Para determinar se um
token do Calico foi usado fora do intervalo de IP esperado do Google Cloud,
execute a consulta do Stackdriver a seguir. A consulta retornará apenas
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
  * [ CVE-2018-3646 para virtualização ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (em inglês) 

Essas CVEs são coletivamente denominadas "L1 Terminal Fault (L1TF)".

As vulnerabilidades desse tipo atacam a configuração de estruturas de dados no
nível do processador para explorar a execução especulativa. "L1" se refere ao
cache de dados de nível 1 (L1D, na sigla em inglês), um pequeno recurso dos
núcleos usado para acelerar o acesso à memória.

Leia a [ postagem do blog do Google Cloud
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=pt_br) (em inglês) para mais detalhes sobre
essas vulnerabilidades e a mitigação do Compute Engine.

####  Impacto do Google Kubernetes Engine

A infraestrutura que executa o Kubernetes Engine e isola os clusters e os nós
do cliente é protegida contra ameaças conhecidas.

Os pools de nós do Kubernetes Engine que usam a imagem do Container-Optimized
OS do Google e estão com o [ upgrade automático
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=pt_br) ativado receberão as versões com patch da imagem do
Container-Optimized OS conforme elas forem disponibilizadas a partir de
20/08/2018.

É necessário fazer o [ upgrade manual ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=pt_br) dos pools de nós do
Kubernetes Engine que não estiverem com o [ upgrade automático
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=pt_br) ativado à medida que forem disponibilizadas as versões com
patch da imagem do COS.

|  Alta  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  6 de agosto de 2018. Última atualização: 5 de setembro de 2018

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
####  Atualização de 05/09/2018

O boletim [ sobre a CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) (em inglês) foi divulgado recentemente. [
Assim como a CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) , ela é uma vulnerabilidade de rede no
nível do kernel que aumenta a eficiência de ataques de negação de serviço
(DoS) contra sistemas vulneráveis. A principal diferença é que a CVE-2018-5391
pode ser explorada por meio de conexões IP. Este boletim foi atualizado para
detalhar as duas vulnerabilidades.

####  Descrição

Na [ CVE-2018-5390 ("SegmentSmack") ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) [em inglês], você encontra a descrição de
uma vulnerabilidade de rede no nível do kernel que aumenta a eficácia de
ataques de negação de serviço (DoS) em sistemas vulneráveis por meio de
conexões TCP.

Na [ CVE-2018-5391 ("FragmentSmack") ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) [em inglês], você encontra a descrição de
uma vulnerabilidade de rede no nível do kernel que aumenta a eficácia de
ataques de negação de serviço (DoS) em sistemas vulneráveis por meio de
conexões IP.

####  Impacto do Google Kubernetes Engine

Desde 11/08/2018, todos os mestres do Kubernetes Engine estão protegidos
contra essas duas vulnerabilidades. Além disso, todos os clusters desse
serviço com a opção de upgrade automático ativada também estão protegidos. Os
pools de nós que não estão com o [ upgrade automático
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=pt_br) ativado e foram atualizados manualmente pela última vez
antes de 11/08/2018 podem ser afetados por essas duas vulnerabilidades.

####  Versões com patch

Devido à gravidade dessa vulnerabilidade, é recomendável que você faça o [
upgrade manual ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=pt_br#upgrading_nodes) dos nós assim que o patch
estiver disponível.

|  Alta  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  30 de maio de 2018

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
Recentemente, foi descoberta no Git uma vulnerabilidade que possibilita o
escalonamento de privilégios no Kubernetes se usuários sem privilégios tiverem
permissão para criar pods com volumes gitRepo. A CVE é identificada pela [ tag
CVE-2018-11235 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-11235) (em inglês).

####  Meu ambiente foi afetado por essa vulnerabilidade?

Você pode ter sido afetado se todas as afirmações a seguir forem aplicáveis no
seu caso:

  * Usuários que não são de confiança podem criar pods (ou acionar a criação deles). 
  * Os pods criados por usuários que não são de confiança têm restrições que impedem o acesso raiz do host. Por exemplo, [ por meio da PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=pt_br) . 
  * Os pods criados por usuários que não são de confiança podem usar o tipo de volume gitRepo. 

Todos os nós do Kubernetes Engine estão vulneráveis.

####  O que fazer?

Proíba o uso do tipo de volume "gitRepo". Para proibir volumes gitRepo com a
PodSecurityPolicy, omita ` gitRepo ` da lista de permissões de ` volumes ` na
PodSecurityPolicy.

Clone um repositório git em um volume EmptyDir a partir de um initContainer
para conseguir um comportamento equivalente ao do volume gitRepo.

    
    
    
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
Elas possibilitam o escalonamento de privilégios ou a negação de serviço por
meio da falha do kernel a partir de um processo sem privilégios. Essas CVEs
são identificadas pelas tags [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) , [ CVE-2018-8897
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897) e [
CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)
(páginas em inglês). Todos os nós do Kubernetes Engine são afetados por essas
vulnerabilidades. É recomendável [ fazer o upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=pt_br) para a versão de patch mais recente, conforme
detalhado a seguir.

####  O que fazer?

Para fazer o upgrade, primeiro é necessário fazer o upgrade do mestre para a
versão mais recente. Esse patch está disponível no Kubernetes Engine
1.8.12-gke.1, 1.9.7-gke.1 e 1.10.2-gke.1. Esses lançamentos incluem patches de
imagens do Ubuntu e do Container-Optimized OS.

Se você criar um novo cluster antes disso, especifique qual é a versão com
patch para que ela seja usada. Os clientes que ativaram os [ upgrades de nós
automáticos ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=pt_br) e não realizaram o upgrade manualmente terão os nós
atualizados para versões com patch nas próximas semanas.

####  Quais vulnerabilidades são corrigidas por esse patch?

O patch reduz as vulnerabilidades a seguir:

[ CVE-2018-1000199 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : essa vulnerabilidade afeta o kernel
do Linux. Ela permite que um usuário ou processo sem privilégios cause uma
falha no kernel do sistema, o que leva a um ataque de DoS ou escalonamento de
privilégios. Essa é uma vulnerabilidade de alta gravidade, com classificação
de 7,8 no Sistema de pontuação de vulnerabilidades comuns (CVSS, na sigla em
inglês).

[ CVE-2018-8897 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : essa vulnerabilidade afeta o kernel do
Linux. Ela permite que um usuário ou processo sem privilégios cause uma falha
no kernel do sistema, o que leva a um ataque de DoS. Essa é uma
vulnerabilidade de média gravidade, com classificação 6,5 no CVSS.

[ CVE-2018-1087 (em inglês) ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : essa vulnerabilidade afeta o hipervisor
KVM do kernel do Linux. Ela permite que um processo sem privilégios cause uma
falha no kernel convidado ou possivelmente consiga privilégios. Um patch que
corrige essa vulnerabilidade foi incluído na infraestrutura em que o
Kubernetes Engine é executado, então esse serviço não é afetado. Essa é uma
vulnerabilidade de alta gravidade, com classificação de 8 no CVSS.

|  Alta  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  12 de março de 2018

Descrição  |  Gravidade  |  Observações  
---|---|---  
  
O projeto Kubernetes [ divulgou recentemente
](https://groups.google.com/forum/?hl=pt_br#!topic/kubernetes-security-
announce/P7lBjbjDKd8) as novas vulnerabilidades de segurança [
CVE-2017-1002101 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002101) e [ CVE-2017-1002102
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102) (páginas em
inglês). Elas possibilitam que os contêineres acessem arquivos que não estão
dentro deles. Todos os nós do Kubernetes Engine são afetados por essas
vulnerabilidades. É recomendável que você faça o upgrade para a versão de
patch mais recente assim que possível.

####  O que fazer?

Devido à gravidade dessas vulnerabilidades, mesmo que você tenha ativado os
upgrades automáticos, é recomendável fazer o [ upgrade manual
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=pt_br) dos nós assim que o patch estiver disponível. Isso
acontecerá até 16 de março. No entanto, de acordo com a [ programação de
lançamentos ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=pt_br#march-12-2018) , talvez você tenha acesso a ele antes com base
na zona em que seu cluster está.

Para fazer o upgrade, primeiro é necessário fazer o upgrade do mestre para a
versão mais recente. Esse patch está disponível no Kubernetes 1.9.4-gke.1,
1.8.9-gke.1 e 1.7.14-gke.1. Os novos clusters usarão a versão em patch por
padrão até 30 de março. Se você criar um novo cluster antes disso, especifique
qual é a versão em patch para que ela seja usada.

Os clientes que ativaram os [ upgrades de nós automáticos
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=pt_br) e não realizaram o upgrade manualmente terão os nós
atualizados para versões com patch até 23 de abril. No entanto, devido à
natureza dessa vulnerabilidade, é recomendável [ fazer o upgrade manual
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=pt_br) dos nós assim que o patch estiver disponível.

####  Quais vulnerabilidades são corrigidas por esse patch?

O patch reduz as duas vulnerabilidades a seguir:

Com a vulnerabilidade CVE-2017-1002101, os contêineres que usam ativações do [
volume subpath ](https://kubernetes.io/docs/concepts/storage/volumes/#using-
subpath) (em inglês) podem acessar arquivos fora do volume. Com isso, se você
tiver bloqueado o acesso do contêiner aos volumes do caminho do host com a
PodSecurityPolicy, um intruso com capacidade de atualizar ou criar pods poderá
ativar qualquer caminho de host usando outro tipo de volume.

A vulnerabilidade CVE-2017-1002102 possibilita que contêineres que usam certos
tipos de volume, incluindo chaves secretas, mapas de configuração, volumes
projetados ou APIs decrescentes, excluam arquivos que estão fora do volume. Ou
seja, se um contêiner que usa um desses tipos de volume for comprometido, ou
você permitir que usuários que não são de confiança criem pods, um intruso
poderá usar esse contêiner para excluir arquivos arbitrários no host.

Para saber mais sobre a correção, leia a [ postagem do blog do Kubernetes
](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-vulnerability/)
(em inglês).

|  Alta  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

