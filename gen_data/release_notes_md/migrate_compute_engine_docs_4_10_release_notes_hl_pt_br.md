#  Notas da versão

Veja nesta página as atualizações de produção do Migrate for Compute Engine.
Acesse-a periodicamente para ver avisos de recursos novos ou atualizados,
correções de bugs, problemas conhecidos e recursos obsoletos.

É possível ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas da versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt-br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/migrate-for-compute-
engine-release-notes.xml `

Para ver uma lista de versões para esta versão e outras, consulte o [
Histórico de versões ](https://cloud.google.com/migrate/compute-
engine/docs/build-history?hl=pt-br) .

##  Requisitos e suporte do sistema operacional

Consulte [ Requisitos ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/concepts/requirements?hl=pt-br) e [ Sistemas operacionais
compatíveis ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=pt-br) .

##  Novos recursos da versão 4.10

###  Integração com o Console do Cloud

**FEATURE:**

A V4.10 integra-se ao [ Console do GCP ](https://cloud.google.com/cloud-
console/?hl=pt-br) para permitir a implantação perfeita do gerenciador de
migrações com a criação de contas de serviço necessárias.

###  Implantação em ambiente de acesso privado

**FEATURE:**

A V4.10 introduz a compatibilidade para a implantação em ambientes com acesso
privado à API ativado. Nesses ambientes, o sistema será implantado sem IP
público e dependerá do acesso privado para acessar as APIs do Cloud. Consulte
[ Como configurar o gerenciador de migração
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/configure-
manager/configuring-migration-manager?hl=pt-br) .

###  Implantação opcional do plug-in do vCenter

**FEATURE:**

A V4.10 introduz a opção de implantar em um ambiente local de origem no
vCenter com ou sem implantar o plug-in do vCenter. A implantação sem o plug-in
do vCenter permite conectar vários sistemas do Migrate ao mesmo ambiente do
vCenter. Consulte [ Como registrar o ambiente VMware vCenter
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/configure-
manager/configuring-vms-vm?hl=pt-br#register_the_vmware_vcenter_environment) .

###  Suporte a script personalizado pré/pós upgrade do Windows 2008 para 2012

**FEATURE:**

A V4.10 introduz a compatibilidade com a execução de scripts personalizados
antes/depois ao usar o upgrade do Windows. É possível adicionar scripts
personalizados à VM. Consulte [ Como fazer upgrade de VMs do Windows Server
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/upgrading-
vms/upgrading-windows-vms?hl=pt-br) para saber mais.

###  Suporte à migração de instâncias do Azure Gen2 para o Compute Engine

**FEATURE:**

A V4.10 introduz a compatibilidade com a migração da instância do [ Azure Gen2
](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=pt-br) para a instância do
Compute Engine compatível com UEFI.

###  Descoberta automática de O/S e atribuição de licença

**FEATURE:**

A V4.10 introduz a identificação automática do SO migrado que, por padrão,
atribuirá a licença correta à VM migrada. Nos cenários em que você quer migrar
VMs usando a licença BYOL do Windows ou a licença premium do Linux, será
necessário fornecê-las como entradas no Runbook. Consulte a [ seção de
licenciamento ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/runbooks?hl=pt-br) na documentação.

##  4.10.1

###  Problemas resolvidos

**FIXED:**

Resolvido um problema com a detecção de partição do Windows para determinadas
estruturas de volume.

**FIXED:**

Inclusão de compatibilidade com discos do Azure acima de 4 TB.

##  4.10

###  Problemas resolvidos

**FIXED:**

Correção de um problema com os drivers ena da AWS que provocavam falha nas
imagens do Windows após a migração.

##  4.10

###  Problemas conhecidos

**ISSUE:**

**Nº 1605343:** devido a uma [ alteração de comportamnto
](https://www.suse.com/support/kb/doc/?id=000019633) no fluxo de ativação do
SUSE, a configuração de repositórios nas instâncias do SUSE Enterprise Linux
falham após a desanexação.

**Solução alternativa:** a solução alternativa a seguir pode ser usada antes
da desanexação (antes da migração ou antes da desanexação).

  1. Siga as instruções descritas em "Situation 4" no link [ https://www.suse.com/support/kb/doc/?id=000019633 ](https://www.suse.com/support/kb/doc/?id=000019633) para fazer o download dos pacotes necessários para o Compute Engine como um arquivo tar.gz. 
  2. **Para SLES 12.x** , execute os seguintes comandos: 
    
        sha1sum late_instance_offline_update_gce_SLE12.tar.gz
    tar -xf late_instance_offline_update_gce_SLE12.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm

  3. **Para SLES 15x** , execute os seguintes comandos: 
    
        sha1sum late_instance_offline_update_gce_SLE15.tar.gz
    tar -xf late_instance_offline_update_gce_SLE15.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm

**ISSUE:**

**#149004085:** o Ubuntu 14 do local pode não conseguir iniciar a publicação
da rede separada.

**Solução alternativa:** conecte-se pelo console serial e adicione manualmente
a interface de rede com o DHCP.

**ISSUE:**

**#145086776:** em casos raros, versões mais antigas do RHEL7 podem travar
durante o streaming ou atingir um pânico do Kernel. Esses problemas foram
resolvidos em versões posteriores do RHEL7.

**Solução alternativa:** execute ` sudo yum update ` antes de migrar para
atualizar o sistema.

**ISSUE:**

**#145644737:** os clones criados no Azure ou na AWS a partir de instâncias de
distribuições Linux que usam o cloud-init podem ter problemas na inicialização
após a instalação do pacote de preparação do Linux.

**Solução:** desinstale o pacote antes de clonar e reinstale-o, ao se preparar
para a migração.

**ISSUE:**

**#143313211:** o cliente que está migrando a VM do RHEL 6.8 pode ter
problemas de inicialização no destino da nuvem.

Os sistemas RHEL 6.x que usam versões do kernel 2.6.32-xxx e LVM podem atingir
um pânico de kernel ao inicializar no Compute Engine durante a migração.

**Solução alternativa:** o kernel precisa ser atualizado para 2.6.32-754 ou
superior antes da migração.

**ISSUE:**

**#143262721:** a migração da VM do Azure falha quando o disco de dados é
maior que 4 terabytes.

No momento, o Migrate for Compute Engine não é compatível com a migração de
VMs do Azure com discos de dados maiores que 4 TB.

**Solução alternativa:** verifique se a VM tem um disco de dados menor que 4
TB.

**ISSUE:**

**Nº 131532690:** as operações de execução na nuvem e de migração podem falhar
para a carga de trabalho do Windows Server 2016 quando o Symantec Endpoint
Management (SEP) está instalado. Isso também pode acontecer quando o SEP
parece estar desativado.

**Solução alternativa:** modifique as vinculações da interface de rede da
carga de trabalho para remover a opção SEP.

  1. Faça o download do [ Microsoft Network VSP Bind (nvspbind) ](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850)
  2. Instale o Microsoft_Nvspbind_package.EXE em c:\temp. 
  3. Abra um prompt de comando como administrador e execute o seguinte: 
    
        nvspbind.exe /d * symc_teefer2

**ISSUE:**

**#131614405:** quando o RPM de preparação do Velostrata é instalado no SUSE
Linux Enterprise Server 11, a VM recebe um endereço IP do DHCP, além de uma
configuração de IP estático existente. Esse problema ocorre quando a VM é
iniciada no local em uma sub-rede ativada com serviços de DHCP.

Observação: o problema não ocorre quando a sub-rede não tem serviços de DHCP.
Não há impacto na conectividade para as comunicações com o endereço IP
estático original.

**ISSUE:**

**#131637800:** depois de registrar o plug-in do Velostrata, a execução do
assistente do Cloud Extension pode gerar um erro "XXXXXXXXXX" ao "Concluir".

**Solução alternativa:** cancele o registro do plug-in do Velostrata e
reinicie o serviço de cliente da Web do vSphere. Em seguida, registre o plug-
in novamente. Entre em contato com o suporte se o problema persistir.

**ISSUE:**

**#131548730:** em alguns casos, quando uma VM é movida para a execução em
nuvem, enquanto uma solução de backup no nível da VM de terceiros contém um
snapshot temporário, as operações com write-back periódico do Migrate for
Compute Engine não serão concluídas, mesmo depois que a solução de backup
excluir o snapshot temporário. O contador de gravações não confirmadas na VM
mostrará um tamanho crescente e nenhum ponto de controle de consistência será
criado no local.

**Solução alternativa:** selecione a ação "Executar no local" da VM e aguarde
a conclusão da tarefa, o que confirmará todas as gravações pendentes. Em
seguida, selecione a ação "executar na nuvem novamente". Observe que confirmar
muitas gravações pendentes pode levar algum tempo. Não use a opção "Forçar"
porque isso resultará na perda de gravações não confirmadas.

**ISSUE:**

**#131605387:** :a reinicialização do vCenter faz com que as tarefas do
Velostrata no vCenter desapareçam da IU. Essa é uma limitação do vCenter.

**Solução alternativa:** use o módulo Velostrata PowerShell para monitorar as
VMs gerenciadas do Velostrata ou as tarefas do Cloud Extensions em execução no
momento.

**ISSUE:**

**#131638716:** com um host do ESXi no modo de manutenção, se uma VM for
movida para a nuvem, a operação falhará e ficará travada na fase de rollback.

**Solução alternativa:** cancele manualmente a tarefa de execução em nuvem,
migre a VM para outro host do ESXi no cluster e repita a operação de execução
em nuvem.

**ISSUE:**

**#131638455:** uma operação execução em nuvem falha com o erro "Falha ao
criar um snapshot da máquina virtual. A operação que você tentou realizar não
pode ser executada no estado atual (desativada)."

**Solução alternativa:** o arquivo de snapshot da VM VMware pode estar
apontando para um snapshot não existente. Entre em contato com o suporte para
receber ajuda na correção do problema.

**ISSUE:**

**#131534862:** em casos raros, depois de executar uma carga de trabalho
localmente, as VMDKs de carga de trabalho são bloqueadas. Em alguns casos,
isso ocorre devido a interrupções de rede entre o appliance de gerenciamento
do Velostrata e o host ESXi em que a carga de trabalho está sendo executada.

Observação: o problema será resolvido após uma ou duas horas.

**ISSUE:**

**#131550214:** durante a separação, a operação pode falhar com a seguinte
mensagem de erro: "A operação foi cancelada".

**Solução alternativa:** repita a operação "Separar".

**ISSUE:**

**#131650367:** ao realizar uma desanexação após uma operação de desanexação,
a ação pode falhar.

**Solução alternativa:** repita a operação.

**ISSUE:**

**#131649978:** no caso de determinadas falhas do sistema, os componentes do
Velostrata se desconectam do vCenter. Nesse caso, um evento pode não ser
enviado, o que resulta em um alarme que não foi definido ou limpo
corretamente.

**Solução alternativa:** limpe o alarme manualmente no vCenter.

**ISSUE:**

**#131532549:** para cargas de trabalho com uma máquina Windows que usa uma
licença de varejo, quando você retorna da nuvem, a licença não está presente.

**Solução alternativa:** reinstale a licença.

**ISSUE:**

**#131555885:** a operação "Export OVA" do vCenter está disponível quando a VM
na nuvem está em execução no modo de cache. No entanto, essa operação resulta
em um OVA corrompido.

**Solução alternativa:** crie o OVA somente após a separação.

**ISSUE:**

**#131647857:** em casos raros, quando uma instância de componente de nuvem é
criada e o sistema falha antes de ser marcado, a instância permanece sem tags.
Isso não permitirá limpeza ou reparo completo da CE.

**Solução alternativa:** marque a instância manualmente e execute o "Reparo".

**ISSUE:**

**#131537125:** a alta disponibilidade da Cloud Extension não funciona para
cargas de trabalho que executam o SO do Ubuntu com a configuração LVM.

**Solução alternativa:** atualize o kernel para a versão 3.13.0-161 ou
superior.

**ISSUE:**

**#131560126:** Suse12: devido a um bug no kernel SUSE anterior à 4.2, as
configurações que incluem ativações BTRFS com subvolumes não são compatíveis.

**Solução alternativa:** faça upgrade para a versão do SUSE com o Kernel >=4.2
(SP2).

**ISSUE:**

**#131533480:** ao usar o assistente "Criar extensão de nuvem", usar um
endereço de proxy HTTP ilegal não gerará uma mensagem de aviso.

**Solução alternativa:** exclua o CE e crie-o com um endereço de proxy HTTP
válido.

**ISSUE:**

**#131647654:** a operação no local foi bem-sucedida, mas o status está
marcado como falha com o erro "Falha ao consolidar snapshots"

**Solução alternativa:** consolide snapshots por meio do vCenter e limpe o
erro manualmente.

**ISSUE:**

**#131558198:** o cliente do PowerShell Runbook de nuvem para nuvem gera erros
quando executado no PowerShell 3.0

**Solução alternativa:** faça upgrade para o PowerShell 4.0

**ISSUE:**

**#131533056:** ao migrar o RHEL 7.0 da AWS para o Google Cloud, o agente do
Google Cloud não será instalado automaticamente.

**Solução alternativa:** remova manualmente o agente da AWS e instale-o.

**ISSUE:**

**#131532713:** após a migração off-line do Windows 2003R2, se uma NIC for
excluída manualmente, talvez seja impossível detectá-la e reinstalá-la
automaticamente.

Solução alternativa: o armazenamento da VM pode ser anexado a uma VM
diferente, e a entrada do Registro NIC pode ser importada manualmente usando
uma VM semelhante como referência. Entre em contato com o suporte para receber
ajuda.

**ISSUE:**

**#131532666:** as versões do Linux em execução com o versão 2.6.32 do kernel
podem sofrer um pane do kernel em caso de falhas de acesso ao armazenamento
temporário. Elas são mais prováveis durante o streaming no iSCSI.

Solução alternativa: atualize seu kernel. O problema também reduzirá a
probabilidade após a separação.

**ISSUE:**

**#131532846:** determinados firewalls e antivírus podem fazer com que as VMs
do Windows falhem quando forem movidas para a nuvem, bloqueando o tráfego
iSCSI.

Solução alternativa: desative o serviço afetado ao migrar e reinstalá-lo após
a separação.

**ISSUE:**

**#131532882:** em determinados casos, iniciar a execução em nuvem durante uma
atualização do Windows pode causar o encerramento abrupto da atualização e
causar uma falha na inicialização na nuvem.

Solução alternativa: permita que o sistema conclua a atualização do Windows
e/ou suspenda as atualizações do Windows antes de migrar.

**ISSUE:**

**#135664281:** ao concluir ou cancelar a migração do Azure para o Google
Cloud, se o Velostrata Management não iniciar o importador, os recursos
criados pelo Velostrata poderão ser deixados no grupo de recursos da instância
original.

**ISSUE:**

**#133137658:** cenário: nenhuma conexão de rede entre o Gerenciador de
migração e o VSphere

Impacto para o cliente: a tarefa RunInCloud permanecerá paralisada devido a
uma falha na chamada para getReadSessions no VSphere.

**Solução alternativa** : corrija a conexão de rede. Caso contrário, cancele a
tarefa e tente novamente.

**ISSUE:**

**#135573857** : cenário: ao mover uma VM de volta para o local com a
sinalização "forçar", a falha ao consolidar o snapshot fará com que a VM
permaneça gerenciada pelo Velostrata. Uma RunInCloud na mesma VM pode falhar
porque não é permitido em VMs gerenciadas.

**Solução alternativa:** aguarde alguns minutos e tente novamente.

**ISSUE:**

**#137082702:** em casos raros, a operação "Cancelar separação" é bem-
sucedida, mas a instância de VM falha ao iniciar.

**Solução alternativa** : mova a instância de volta e mova-a novamente para a
nuvem.

