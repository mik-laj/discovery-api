#  Notas da versão

Nesta página, documentamos as atualizações de produção do Anthos GKE On-Prem.
Acesse-a periodicamente para ver avisos de recursos novos ou atualizados,
correções de bugs, problemas conhecidos e recursos obsoletos.

Veja também:

  * [ Downloads ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=pt-br)
  * [ Controle de versão e upgrades ](https://cloud.google.com/anthos/gke/docs/on-prem/versioning-and-upgrades?hl=pt-br)
  * [ Como fazer upgrade de clusters ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=pt-br)
  * [ Como fazer upgrade da estação de trabalho do administrador ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=pt-br)

É possível ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas da versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt-br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/gkeonprem-release-
notes.xml `

##  22 de agosto de 2019

A versão 1.0.2-gke.3 do GKE On-Prem já está disponível. Esta versão do patch
inclui as seguintes alterações:

###  Novos recursos

**FEATURE:**

Agora, o balanceamento de carga manual é compatível com a análise.

**FEATURE:**

Agora, é possível especificar uma rede vSphere diferente para clusters de
administrador e usuário.

**FEATURE:**

Agora é possível excluir clusters de usuários usando ` gkectl ` . Consulte [
Como excluir um cluster de usuários
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/administration/deleting-a-user-cluster?hl=pt-br) .

###  Alterações

**CHANGED:** ` gkectl diagnose snapshot ` agora recebe registros dos planos de
controle do cluster de usuários.

**CHANGED:**

A especificação OIDC do GKE On-Prem foi atualizada com vários novos campos: `
kubectlredirecturl ` , ` scopes ` , ` extraparams ` e ` usehttpproxy ` .

**CHANGED:**

Calico atualizado para a versão 3.7.4.

**CHANGED:**

As métricas do sistema do Cloud Monitoring prefixadas mudaram de `
external.googleapis.com/prometheus/ ` para ` kubernetes.io/anthos/ ` . Se você
estiver rastreando métricas ou alertas, atualize seus painéis com o próximo
prefixo.

###  Correção

**FIXED:**

[ Corrigida uma vulnerabilidade do CVE-2019-11247
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/security-
bulletins?hl=pt-br#august-22-2019) .

**FIXED:**

[ Corrigida uma vulnerabilidade no proxy RBAC
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/security-
bulletins?hl=pt-br#august-23-2019) .

##  30 de julho de 2019

A versão 1.0.1-gke.5 GKE On-Prem já está disponível. Esta versão do patch
inclui as seguintes alterações:

###  Novos recursos

**FEATURE:**

Publicação da [ folha de referências do GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/reference/cheatsheet?hl=pt-br) .

###  Alterações

**CHANGED:**

` gkectl check-config ` agora também verifica a disponibilidade do IP do nó se
você estiver usando IPs estáticos.

**CHANGED:**

` gkectl prepare ` agora verifica se há uma VM e está marcada como um modelo
no vSphere antes de tentar fazer upload da imagem OVA da VM.

**CHANGED:**

Inclusão de compatibilidade com a especificação de um cluster do vCenter e um
pool de recursos nesse cluster.

**CHANGED:**

Atualiza o controlador F5 BIG-IP para a versão 1.9.0.

**CHANGED:**

Atualiza o controlador de entrada do Istio para a versão 1.2.2.

###  Correções

**FIXED:**

Corrige problemas de persistência de dados de registro com o registro do
Docker da estação de trabalho de administrador.

**FIXED:**

Corrige a validação que verifica se o nome de um cluster de usuário já está em
uso.

##  17 de junho de 2019

O GKE On-Prem já está disponível para todos os usuários. A versão 1.0.10
inclui as seguintes alterações:

###  Como fazer upgrade da versão Beta-1.4 para 1.0.10

Antes de fazer upgrade dos clusters Beta para a primeira versão de
disponibilidade geral, execute as etapas descritas em [ Como fazer upgrade da
versão Beta do GKE On-Prem para a disponibilidade geral
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/upgrading/from-beta?hl=pt-br) , e analise os seguintes pontos:

  * Se você estiver executando uma versão Beta anterior à beta-1.4, faça upgrade para a versão beta-1.4 primeiro. 

  * Se os clusters Beta estiverem executando os próprios balanceadores de carga L4, e não o padrão, F5 BIG-IP, será necessário excluir e recriar os clusters para executar a versão mais recente do GKE On-Prem. 

  * Se os clusters tiverem upgrade para a versão Beta-1.4 do Beta-1.3, execute o seguinte comando _para cada cluster de usuários_ antes de fazer upgrade: 
    
        kubectl delete crd networkpolicies.crd.projectcalico.org

  * A verificação do certificado do vCenter agora é necessária. " ` vsphereinsecure ` " não é mais compatível. Se você estiver atualizando seus clusters beta 1.4 para 1.0.10, será necessário fornecer um certificado público raiz da CA confiável no arquivo de configuração do upgrade. 

  * Você precisa fazer upgrade de _todos_ os clusters em execução. Para que essa atualização seja bem-sucedida, seus clusters não podem ser executados em um estado de versão misto. 

  * Primeiro, você precisa fazer upgrade dos clusters de administrador para a versão mais recente e depois fazer upgrade dos clusters de usuário. 

###  Novos recursos

**FEATURE:**

Agora é possível ativar o [ Modo de balanceamento de carga manual
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/manual-lb?hl=pt-br) para configurar um balanceador de carga
L4. Você ainda pode optar por usar o balanceador de carga padrão F5 BIG-IP.

**FEATURE:**

O processo de instalação baseado em configuração do GKE On-Prem foi
atualizado. Agora, é possível instalar de maneira declarativa usando apenas um
[ arquivo de configuração ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/concepts/overview?hl=pt-br#config) .

**FEATURE:**

Adiciona ` gkectl create-config ` , que gera um arquivo de configuração para
instalar o GKE On-Prem, fazer upgrade de clusters atuais e criar clusters de
usuário adicionais em uma instalação existente. Isso substitui o assistente de
instalação e o ` create-config.yaml ` das versões anteriores. Consulte a
documentação atualizada para [ como instalar o GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/install?hl=pt-br#generate_config) .

**FEATURE:**

Adiciona ` gkectl check-config ` , que valida o arquivo de configuração do GKE
On-Prem. Consulte a documentação atualizada para [ como instalar o GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/install?hl=pt-br#validate_config) .

**FEATURE:**

Adiciona uma sinalização ` --validate-attestations ` opcional a ` gkectl
prepare ` . Essa sinalização verifica se as imagens de contêiner incluídas na
estação de trabalho do administrador foram criadas e assinadas pelo Google e
estão prontas para implantação. Consulte a documentação atualizada para [ como
instalar o GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/install?hl=pt-br#prepare) .

###  Alterações

**CHANGED:**

Faz o upgrade da versão do Kubernetes para 1.12.7-gke.19. Agora é possível [
fazer upgrade dos clusters ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/administration/upgrading-clusters?hl=pt-br)
para essa versão. Não é mais possível criar clusters que executam o Kubernetes
versão 1.11.2-gke.19.

Recomendamos fazer upgrade do cluster de administrador antes de fazer upgrade
dos clusters de usuário.

**CHANGED:**

Atualiza o controlador de entrada do Istio para a versão 1.1.7.

**CHANGED:**

A verificação do certificado do vCenter agora é necessária. ` vsphereinsecure
` não é mais compatível. Você fornece o certificado no campo ` cacertpath ` do
arquivo de configuração do GKE On-Prem.

Quando um cliente chama o servidor vCenter, o servidor vCenter precisa provar
a identidade ao cliente, apresentando um certificado. Esse certificado precisa
ser assinado por uma autoridade de certificação (CA, na sigla em inglês). O
certificado não pode ser autoassinado.

Se você estiver fazendo upgrade dos clusters Beta 1.4 para a versão 1.0.10,
precisará fornecer um certificado público raiz da CA confiável do vCenter no
arquivo de configuração do upgrade.

###  Problemas conhecidos

**ISSUE:**

O [ upgrade de clusters ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/upgrading-clusters?hl=pt-br) pode causar interrupções
ou inatividade para cargas de trabalho que usam [ PodDisruptionBudgets
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) (PDBs).

**ISSUE:**

Talvez não seja possível fazer upgrade dos clusters Beta que usam o [ Modo de
balanceamento de carga manual ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/manual-lb?hl=pt-br) para a versão
1.0.10 do GKE On-Prem. Para fazer upgrade e continuar usando o próprio
balanceador de carga com esses clusters, é preciso recriar os clusters.

##  24 de maio de 2019

A versão Beta 1.4.7 do GKE On-Prem está disponível. Esta versão inclui as
seguintes alterações:

###  Novos recursos

**FEATURE:**

No comando [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/diagnose?hl=pt-br#capture_admin) , o parâmetro ` --admin-
ssh-key-path ` agora é opcional.

###  Alterações

**CHANGED:**

Em 8 de maio de 2019, introduzimos uma alteração no Connect, o serviço que
permite interagir com os clusters do GKE On-Prem usando o Console do Cloud.
Para usar o novo agente do Connect, é necessário registrar novamente os
clusters com o Console do Cloud ou fazer upgrade para o Anthos GKE On-Prem
Beta-1.4.

Os clusters locais do GKE e as cargas de trabalho em execução continuarão
funcionando sem interrupções. No entanto, seus clusters não estarão visíveis
no Console do Cloud até que você os registre novamente ou faça upgrade para a
versão Beta-1.4.

Antes de registrar novamente ou fazer upgrade, verifique se a conta de serviço
tem o papel ` gkehub.connect ` . Além disso, se sua conta de serviço tiver o
papel de clusterregistry.connect antigo, remova-o.

Conceda à conta de serviço o papel gkehub.connect:

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

Se a conta de serviço tiver o papel ` clusterregistry.connect ` antigo,
remova-o:

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

Registre seu cluster novamente ou faça upgrade para o Anthos GKE On-Prem
Beta-1.4.

Para [ registrar novamente o cluster ](https://cloud.google.com/kubernetes-
engine/connect/updating-agent?hl=pt-br) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]

Para [ fazer upgrade para o Anthos GKE On-Prem beta-1.4
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=pt-br) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Problemas conhecidos

**ISSUE:**

Há um problema que impede que o agente do Connect seja atualizado para a nova
versão durante um upgrade. Para contornar esse problema, execute o seguinte
comando depois de fazer upgrade de um cluster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  13 de maio de 2019

###  Problemas conhecidos

**ISSUE:**

Os clusters atualizados da versão beta-1.2 para beta-1.3 podem ser afetados
por um problema conhecido que danifica o arquivo de configuração do cluster e
impede futuras atualizações do cluster. Esse problema afeta todos os upgrades
futuros do cluster.

Para resolver esse problema, exclua e recrie os clusters atualizados da versão
Beta-1.2 para Beta-1.3.

Para resolver o problema sem excluir e recriar o cluster, é necessário
recodificar e aplicar os secrets de cada cluster. Siga as etapas abaixo:

  1. Receba o conteúdo dos secrets ` create-config ` armazenados no cluster de administrador. Isso precisa ser feito para o secret ` create-config ` no namespace kube-system e para as secrets ` create-config ` no namespace de cada cluster de usuário: 
    
        kubectl get secret create-config -n kube-system -o jsonpath={.data.cfg} | base64 -d > kube-system_create_secret.yaml
    
        kubectl get secret create-config -n [USER_CLUSTER_NAME] -o jsonpath={.data.cfg} | base64 -d > [USER_CLUSTER_NAME]_create_secret.yaml

  2. Para cada cluster de usuário, abra o arquivo ` [USER_CLUSTER_NAME]  _create_secret.yaml ` em um editor. Se os valores de ` registerserviceaccountkey ` e ` connectserviceaccountkey ` não forem ` REDACTED ` , nenhuma ação adicional será necessária: os Secrets não precisam ser recodificados e gravados no cluster. 
  3. Abra o arquivo ` create_config.yaml ` original em outro editor. 
  4. Em ` [USER_CLUSTER_NAME]  _create_secret.yaml ` , substitua os valores ` registerserviceaccountkey ` e ` connectserviceaccountkey ` pelos valores do arquivo ` create_config.yaml ` original. Salve o arquivo alterado. 
  5. Repita as etapas 3 a 5 para cada ` [USER_CLUSTER_NAME]  _create_secret.yaml ` e para o arquivo ` kube-system_create_secret.yaml ` . 
  6. Codifique em Base64 cada arquivo ` [USER_CLUSTER_NAME]  _create_secret.yaml ` e o arquivo ` kube-system_create_secret.yaml ` : 
    
        cat [USER_CLUSTER_NAME]_create_secret.yaml | base64 > [USER_CLUSTER_NAME]_create_secret_create_secret.b64
    
        cat kube-system-cluster_create_secret.yaml | base64 >kube-system-cluster_create_secret.b64

  7. Substitua o campo ` data[cfg] ` em cada Secret no cluster pelo conteúdo do arquivo correspondente: 
    
        kubectl edit secret create-config -n [USER_CLUSTER_NAME]
    
      # kubectl edit opens the file in the shell's default text editor
      # Open `first-user-cluster_create_secret.b64` in another editor, and replace
      # the `cfg` value with the copied value
      # Make sure the copied string has no newlines in it!

  8. Repita a etapa 8 para cada Secret ` [USER_CLUSTER_NAME]  _create_secret.yaml ` e para o Secret ` kube-system_create_secret.yaml ` . 
  9. Para garantir que a atualização foi bem-sucedida, repita a etapa 1. 

##  7 de maio de 2019

A versão Beta 1.4.1 do GKE On-Prem está disponível. Esta versão inclui as
seguintes alterações:

###  Novos recursos

**FEATURE:**

No comando [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/diagnose?hl=pt-br#capture_admin) , o parâmetro ` --admin-
ssh-key-path ` agora é opcional.

###  Alterações

**CHANGED:**

Em 8 de maio de 2019, introduzimos uma alteração no Connect, o serviço que
permite interagir com os clusters do GKE On-Prem usando o Console do Cloud.
Para usar o novo agente do Connect, é necessário registrar novamente os
clusters com o Console do Cloud ou fazer upgrade para o Anthos GKE On-Prem
Beta-1.4.

Os clusters locais do GKE e as cargas de trabalho em execução continuarão
funcionando sem interrupções. No entanto, seus clusters não estarão visíveis
no Console do Cloud até que você os registre novamente ou faça upgrade para a
versão Beta-1.4.

Antes de registrar novamente ou fazer upgrade, verifique se a conta de serviço
tem o papel gkehub.connect. Além disso, se a conta de serviço tiver o papel
clusterregistry.connect antigo, remova-o.

Conceda à conta de serviço o papel gkehub.connect:

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

Se a conta de serviço tiver o papel clusterregistry.connect antigo, remova o
papel antigo:

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

Registre seu cluster novamente ou faça upgrade para o Anthos GKE On-Prem
Beta-1.4.

Para [ registrar novamente seu cluster ](https://cloud.google.com/kubernetes-
engine/connect/updating-agent?hl=pt-br) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]

Para [ fazer upgrade para o Anthos GKE On-Prem beta-1.4
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=pt-br) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Problemas conhecidos

**ISSUE:**

Há um problema que impede que o agente do Connect seja atualizado para a nova
versão durante um upgrade. Para contornar esse problema, execute o seguinte
comando depois de fazer upgrade de um cluster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  25 de abril de 2019

A versão 1.3.1 do GKE Beta local já está disponível. Esta versão inclui as
seguintes alterações:

###  Novos recursos

**FEATURE:**

O comando ` gkectl diagnose snapshot ` agora tem uma sinalização [ ` --dry-run
` ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/administration/diagnose?hl=pt-br#performing_a_dry_run_for_a_snapshot) .

**FEATURE:**

O comando ` gkectl diagnose snapshot ` agora é compatível com quatro [
cenários ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.3/how-to/administration/diagnose?hl=pt-
br#snapshot_scenarios) .

**FEATURE:**

O comando ` gkectl diagnose snapshot ` agora é compatível com expressões
regulares para especificar namespaces.

###  Alterações

**CHANGED:**

O Istio 1.1 agora é o [ controlador de entrada
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/administration/upgrading-a-cluster?hl=pt-
br#upgrading_the_ingress_controller) padrão. O controlador de entrada é
executado no namespace ` gke-system ` para clusters de administradores e
usuários. Isso facilita o gerenciamento do TLS para o Ingress. Para ativar a
entrada ou reativar a entrada após um upgrade, siga as instruções em [ Como
ativar a entrada ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.3/how-to/installation/install?hl=pt-
br#enabling_ingress) .

**CHANGED:**

A ferramenta ` gkectl ` não usa mais o Minikube e o KVM para bootstrap. Isso
significa que você não precisa ativar a virtualização aninhada na VM da
estação de trabalho do administrador.

###  Problemas conhecidos

**ISSUE:**

O controlador de entrada do GKE On-Prem usa o Istio 1.1 com descoberta
automática de Secrets. No entanto, o agente do nó para descoberta de Secrets
pode falhar ao receber atualizações de Secrets após a exclusão de um.
Portanto, evite excluir secrets. Se você precisar excluir um secret e o TLS do
Ingress falhar posteriormente, reinicie manualmente o pod do Ingress no
namespace gke-system.

##  11 de abril de 2019

A versão Beta 1.2.1 do GKE On-Prem está disponível. Esta versão inclui as
seguintes alterações:

###  Novos recursos

**FEATURE:**

Agora, os clusters do GKE On-Prem se conectam automaticamente ao Google usando
o [ Connect ](https://cloud.google.com/kubernetes-engine/connect?hl=pt-br) .

**FEATURE:**

Agora é possível executar até três planos de controle por cluster de usuário.

###  Alterações

**CHANGED:**

` gkectl ` agora valida credenciais do vSphere e F5 BIG-IP criando clusters.

###  Problemas conhecidos

**ISSUE:**

Uma regressão faz com que os comandos ` gkectl diagnose snapshot ` usem a
chave SSH errada, o que impede o comando de coletar informações dos clusters
de usuários. Como alternativa em casos de suporte, pode ser necessário
executar SSH em nós de cluster de usuários individuais e coletar dados
manualmente.

##  2 de abril de 2019

A versão Beta 1.1.1 do GKE On-Prem já está disponível. Esta versão inclui as
seguintes alterações:

###  Novos recursos

**FEATURE:**

Instale o GKE On-Prem com um [ Open Virtual Appliance (OVA)
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/installation/getting-started?hl=pt-br#download_ova) , uma imagem de máquina
virtual pré-configurada que inclui várias ferramentas de interface de linha de
comando. Essa alteração facilita as instalações e remove uma camada de
virtualização. Não é mais necessário executar ` gkectl ` dentro de um
contêiner do Docker.

Se você instalou o GKE On-prem versões anteriores à versão Beta-1.1.1, é
preciso criar uma nova estação de trabalho de administrador seguindo as
instruções documentadas. Depois de instalar a nova estação de trabalho de
administrador, copie todas as chaves SSH, arquivos de configuração,
kubeconfigs e outros arquivos necessários da estação de trabalho anterior para
a nova.

**FEATURE:**

Foi adicionada documentação para [ fazer backup e restaurar clusters
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/administration/backing-up?hl=pt-br) .

**FEATURE:**

Agora é possível configurar a autenticação para clusters usando o OIDC e ADFS.
Para saber mais, consulte [ Como autenticar com OIDC e ADFS
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/security/oidc-adfs?hl=pt-br) e [ Autenticação
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/concepts/authentication?hl=pt-br) .

###  Alterações

**CHANGED:**

Agora você precisa usar a chave privada de um cluster de administrador para
executar ` gkectl diagnose snapshot ` .

**CHANGED:**

Adição de uma opção de configuração durante a instalação para implantar
clusters de usuários de vários mestres.

**CHANGED:**

A [ documentação do Connect ](https://cloud.google.com/kubernetes-
engine/connect?hl=pt-br) foi migrada.

###  Correções

**FIXED:**

Correção de um problema em que a rede do cluster era interrompida quando um nó
era removido inesperadamente.

###  Problemas conhecidos

**ISSUE:**

O gerenciamento de configuração do GKE On-Prem foi atualizado da versão 0.11
para 0.13. Vários componentes do sistema foram renomeados. É necessário seguir
algumas etapas para limpar os recursos das versões anteriores e instalar uma
nova instância.

Se você tiver uma instância ativa do gerenciamento de configuração siga estas
etapas:

  1. Desinstale a instância: 
    
        kubectl -n=nomos-system delete nomos --all

  2. Verifique se o namespace da instância não tem recursos: 
    
        kubectl -n nomos-system get all

  3. Exclua o namespace: 
    
        kubectl delete ns nomos-system

  4. Exclua a CRD: 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  5. Exclua todos os recursos kube-system para o operador: 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

Se você não tiver uma instância ativa do gerenciamento de configuração siga
estas etapas:

  1. Exclua o namespace de gerenciamento de configuração: 
    
        kubectl delete ns nomos-system

  2. Exclua a CRD: 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  3. Exclua todos os recursos kube-system para o operador: 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

##  12 de março de 2019

A versão Beta 1.0.3 do GKE On-Prem está disponível. Esta versão inclui as
seguintes alterações:

###  Correções

**FIXED:**

Correção de um problema que fazia com que os certificados do Docker fossem
salvos no local errado.

##  4 de março de 2019

A versão Beta 1.0.2 do GKE On-Prem está disponível. Esta versão inclui as
seguintes alterações:

###  Novos recursos

**FEATURE:**

Agora é possível executar ` gkectl version ` para verificar qual versão do `
gkectl ` você está executando.

**FEATURE:**

Agora é possível [ fazer upgrade de clusters de usuários
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.0/how-
to/administration/upgrading-a-cluster?hl=pt-br) para versões Beta futuras.

**FEATURE:**

A versão 0.11.6 do [ Anthos Config Management
](https://cloud.google.com/anthos-config-management/docs?hl=pt-br) já está
disponível.

**FEATURE:**

O Stackdriver Logging agora está ativado em cada nó. Por padrão, o agente de
geração de registros replica os registros no seu projeto do GCP apenas para
serviços de plano de controle, API de cluster, controlador do vSphere, Calico,
controlador BIG-IP, proxy Envoy, Connect, Anthos Config Management, serviços
Prometheus e Grafana, plano de controle do Istio e Docker. Os registros de
contêiner do aplicativo são excluídos por padrão, mas podem ser ativados
opcionalmente.

**FEATURE:**

O sidecar do Stackdriver Prometheus captura métricas para os mesmos
componentes que o agente de geração de registros.

**FEATURE:**

As [ políticas de rede do Kubernetes
](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
agora são compatíveis.

###  Alterações

**CHANGED:**

Agora é possível atualizar os blocos de IP na especificação do cluster para
expandir o intervalo de IP de um determinado cluster.

**CHANGED:**

Se os clusters instalados durante a versão Alfa forem desconectados do Google
após a versão Beta, talvez seja necessário conectá-los novamente. Consulte [
Como registrar manualmente um cluster de usuário
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/registering-a-user-cluster?hl=pt-br) .

**CHANGED:**

Os [ Primeiros passos ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/getting-started?hl=pt-br) foram
atualizados com as etapas para ativar sua conta de serviço e executar ` gkectl
prepare ` .

**CHANGED:**

` gkectl diagnose snapshot ` agora coleta apenas dados de configuração e
exclui registros. Essa ferramenta é usada para capturar detalhes do ambiente
antes de abrir um caso de suporte.

**CHANGED:**

Suporte para configuração de nome do pool SNAT opcional para o F5 BIG-IP no
momento da criação do cluster. Pode ser usado para configurar o valor "--vs-
snat-pool-name" no [ controlador F5 BIG-IP
](https://clouddocs.f5.com/products/connectors/k8s-bigip-ctlr/v1.8/) .

**CHANGED:**

Agora você precisa fornecer um VIP para os complementos executados no cluster
de administrador.

###  Correções

**FIXED:**

As operações de redimensionamento de cluster foram aprimoradas para evitar a
exclusão acidental de nós.

##  7 de fevereiro de 2019

A versão Alfa 1.3 do GKE On-Prem já está disponível. Esta versão inclui as
seguintes alterações:

###  Novos recursos

**FEATURE:**

Durante a instalação, é possível fornecer arquivos YAML com blocos ` nodeip `
para configurar o IPAM estático.

###  Alterações

**CHANGED:**

Agora você precisa provisionar um disco de 100 GB no Datastore do vSphere. O
GKE On-Prem usa o disco para armazenar alguns dos dados vitais dele, como
etcd. Consulte os [ requisitos do sistema
](https://cloud.google.com/anthos/gke/docs/on-prem/requirements?hl=pt-br) .

**CHANGED:**

Agora, só é possível fornecer nomes de host em letras minúsculas a blocos `
nodeip ` .

**CHANGED:**

O GKE On-Prem agora aplica nomes exclusivos para clusters de usuários.

**CHANGED:**

Endpoints de métricas e APIs que usam endpoints do Istio agora são protegidos
com mTLS e controle de acesso baseado em papéis.

**CHANGED:**

A comunicação externa do Grafana está desativada.

**CHANGED:**

Melhorias na verificação de integridade do Prometheus e do Alertmanager.

**CHANGED:**

Agora, o Prometheus usa a porta segura para coletar métricas.

**CHANGED:**

Várias atualizações nos painéis do Grafana.

###  Problemas conhecidos

**ISSUE:**

Se a conta de usuário do vCenter usar um formato como ` DOMAIN\USER ` , talvez
seja necessário evitar a barra invertida ( ` DOMAIN\\USER ` ). Faça isso
quando solicitado a inserir a conta de usuário durante a instalação.

##  23 de janeiro de 2019

A versão Alfa 1.2.1 do GKE On-Prem já está disponível. Esta versão inclui as
seguintes alterações:

###  Novos recursos

**FEATURE:**

Agora é possível usar ` gkectl ` para [ excluir clusters de administrador
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/administration/deleting-an-admin-cluster?hl=pt-br)

.

###  Alterações

**CHANGED:**

Agora, os comandos ` gkectl diagnose snapshot ` permitem especificar nós ao
capturar snapshots de resultados de comando remoto e arquivos.

##  14 de janeiro de 2019

A versão Alfa 1.1.2 do GKE On-Prem está disponível. Esta versão inclui as
seguintes alterações:

###  Novos recursos

**FEATURE:**

Agora é possível usar o comando ` gkectl prepare ` para extrair e enviar
imagens de contêiner do GKE On-Prem, o que suspende o uso do script `
populate_registry.sh ` .

**FEATURE:**

Agora, ` gkectl prepare ` solicita que você insira informações sobre o cluster
vSphere e o pool de recursos.

**FEATURE:**

Agora é possível usar o comando ` gkectl create ` para criar e adicionar
clusters de usuários a planos de controle de administrador existentes passando
um arquivo kubeconfig existente quando solicitado durante a criação do
cluster.

**FEATURE:**

Agora é possível passar um secret TLS do Ingress para clusters administradores
e de usuários no momento da criação do cluster. Você verá o seguinte prompt:

` Do you want to use TLS for Admin Control Plane/User Cluster ingress? `

O fornecimento do segredo e dos certificados TLS permite que o ` gkectl `
configure o TLS de entrada. O HTTP não é desativado automaticamente com a
instalação do TLS.

###  Alterações

**CHANGED:**

O GKE On-Prem agora executa o Kubernetes versão **1.11.2-gke.19** .

**CHANGED:**

A abrangência padrão do GKE On-Prem mudou:

  * O requisito mínimo de memória para nós de cluster de usuário agora é de 8.192 MB. 

**CHANGED:**

O GKE On-Prem agora executa o minikube versão **0.28.0** .

**CHANGED:**

O Gerenciamento de políticas do GKE foi atualizado para a versão **0.11.1** .

**CHANGED:**

O ` gkectl ` não solicita mais que você forneça uma configuração de proxy por
padrão.

**CHANGED:**

Há três novos recursos do ConfigMap no namespace do cluster de usuários: `
cluster-api-etcd-metrics-config ` , ` kube-etcd-metrics-config ` e ` kube-
apiserver-config ` . O GKE On-Prem usa esses arquivos para inicializar
rapidamente o contêiner de proxy de métricas.

**CHANGED:**

Os eventos do kube-apiserver agora estão no próprio etcd. É possível ver kube-
etcd-event no namespace do cluster de usuário.

**CHANGED:**

Os controladores da API do cluster agora usam a eleição de líder.

**CHANGED:**

Agora, as credenciais do vSphere são extraídas de arquivos de credenciais.

**CHANGED:**

Os comandos ` gkectl diagnose ` agora funcionam com clusters de administrador
e de usuário.

**CHANGED:**

` gkectl diagnose snapshot ` agora pode tirar snapshots de arquivos remotos no
nó, resultados de comandos remotos nos nós e consultas do Prometheus.

**CHANGED:**

` gkectl diagnose snapshot ` agora pode tirar snapshots em várias linhas de
execução paralelas.

**CHANGED:**

` gkectl diagnose snapshot ` agora permite que você especifique palavras a
serem excluídas dos resultados do snapshot.

###  Correções

**FIXED:**

Correção de problemas com o cache do minikube que causavam chamadas de rede
inesperadas.

**FIXED:**

Corrigido um problema ao extrair credenciais F5 BIG-IP. Agora, as credenciais
são lidas em um arquivo de credenciais em vez de usar variáveis de ambiente.

###  Problemas conhecidos

**ISSUE:**

Talvez você encontre o seguinte aviso [ ` govmomi `
](https://github.com/vmware/govmomi) ao executar ` gkectl prepare ` :

` Warning: Line 102: Unable to parse 'enableMPTSupport' for attribute 'key' on
element 'Config' `

**ISSUE:**

O redimensionamento de clusters de usuários pode causar exclusão ou recriação
de nós inadvertidos.

**ISSUE:**

Os PersistentVolumes podem falhar ao ativar, produzindo o erro ` devicePath is
empty ` . Como solução alternativa, exclua e recrie o PersistentVolumeClaim
associado.

**ISSUE:**

Se estiver usando alocação de IP estático para nós, o redimensionamento de
blocos de endereços IPAM não é compatível com a versão Alfa. Como alternativa,
considere alocar mais endereços IP do que você precisa atualmente.

**ISSUE:**

Em discos lentos, a criação da VM pode atingir o tempo limite e causar falhas
nas implantações. Se isso ocorrer, exclua todos os recursos e tente novamente.

##  19 de dezembro de 2018

A versão Alfa 1.0.4 do GKE On-Prem está disponível. Esta versão inclui as
seguintes alterações:

###  Correções

**FIXED:**

A vulnerabilidade causada por [ CVE-2018-1002105
](https://github.com/kubernetes/kubernetes/issues/71411) foi corrigida.

##  30 de novembro de 2018

O GKE On-Prem Alfa 1.0 está disponível. As seguintes alterações estão
incluídas nesta versão:

###  Alterações

**CHANGED:**

O GKE On-Prem Alfa 1.0 executa o Kubernetes 1.11.

**CHANGED:**

A abrangência padrão do GKE On-Prem mudou:

  * O plano de controle do administrador executa três nós, que usam 4 CPUs e 16 GB de memória. 
  * O plano de controle do usuário executa um nó que usa 4 CPUs com 16 GB de memória. 
  * Os clusters do usuário executam no mínimo três nós, que usam 4 CPUs e 16 GB de memória. 

**CHANGED:**

Suporte para configuração do Prometheus de alta disponibilidade.

**CHANGED:**

Suporte para a configuração personalizada do Gerenciador de alertas.

**CHANGED:**

O Prometheus foi atualizado de **2.3.2** para **2.4.3** .

**CHANGED:**

O Grafana foi atualizado do **5.0.4** para o **5.3.4** .

**CHANGED:**

O kube-state-metrics foi atualizado de **1.3.1** para **1.4.0** .

**CHANGED:**

O Gerenciador de alertas foi atualizado de **1.14.0** para **1.15.2** .

**CHANGED:**

O node_export foi atualizado de **1.15.2** para **1.16.0** .

###  Correções

**FIXED:**

A vulnerabilidade causada por [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) foi corrigida.

###  Problemas conhecidos

**ISSUE:**

Os PersistentVolumes podem falhar ao ativar, produzindo o erro ` devicePath is
empty ` . Como solução alternativa, exclua e recrie o PersistentVolumeClaim
associado.

**ISSUE:**

Se estiver usando alocação de IP estático para nós, o redimensionamento de
blocos de endereços IPAM não é compatível com a versão Alfa. Como alternativa,
considere alocar mais endereços IP do que você precisa atualmente.

**ISSUE:**

O GKE On-Prem Alfa 1.0 ainda não passou em todos os testes de conformidade.

**ISSUE:**

Somente um cluster de usuário por cluster de administrador pode ser criado.
Para criar clusters de usuário adicionais, crie outro cluster de
administrador.

##  31 de outubro de 2018

A versão 2.1 do EAP do GKE On-Prem já está disponível. As seguintes alterações
estão incluídas nesta versão:

###  Alterações

**CHANGED:**

Ao criar clusters de administrador e de usuário ao mesmo tempo, agora é
possível reutilizar as credenciais F5 BIG-IP do cluster de administrador para
criar o cluster de usuário. Além disso, a CLI agora requer que as credenciais
BIG-IP sejam fornecidas. Esse requisito não pode ser ignorado usando ` --dry-
run ` .

**CHANGED:**

Upgrade do controlador F5 BIG-IP para usar a versão mais recente do OSS,
1.7.0.

**CHANGED:**

Para melhorar a estabilidade de máquinas lentas do vSphere, o tempo limite de
criação da máquina do cluster agora é de 15 minutos (anteriormente cinco
minutos).

##  17 de outubro 2018

O EAP 2.0 do GKE On-Prem já está disponível. As seguintes alterações estão
incluídas nesta versão:

###  Alterações

**CHANGED:**

Suporte para o GKE Connect.

**CHANGED:**

Suporte para o Monitoring.

**CHANGED:**

Suporte para instalação usando registros particulares.

**CHANGED:**

Suporte para front-end do balanceador de carga L7 como um VIP L4 no F5 BIG-IP.

**CHANGED:**

Suporte para alocação de IP estático para nós durante a inicialização do
cluster.

###  Problemas conhecidos

**ISSUE:**

Somente um cluster de usuário por cluster de administrador pode ser criado.
Para criar clusters de usuário adicionais, crie outro cluster de
administrador.

**ISSUE:**

Os upgrades de cluster não são compatíveis com o EAP 2.0.

**ISSUE:**

Em discos lentos, a criação da VM pode atingir o tempo limite e causar falhas
nas implantações. Se isso ocorrer, exclua todos os recursos e tente novamente.

**ISSUE:**

Como parte do processo de inicialização do cluster, uma instância de minikube
de curta duração é executada. A versão do minikube usada tem vulnerabilidade
de segurança [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) .

