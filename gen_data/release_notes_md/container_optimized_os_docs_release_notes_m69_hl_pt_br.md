#  Notas da versão: marco 69

##  Status atual

Família de imagens  |  cos-69-lts  
---|---  
Obsoleto após  |  11 de dezembro de 2019  
Kernel  |  [ 4.14.91+
](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/edb81c460eee7a4a35e2a95ebf6450df0963398e)  
Kubernetes  |  v1.11.1  
Docker  |  v17.03.2  
  
##  Registro de alterações (vs. marco 68)

###  cos-69-10895-172-0

_Data: 28 de fevereiro de 2019_

  * Ativação do kernel.softlockup_all_cpu_backtrace. Isso foi desativado anteriormente para atenuar um problema de impasse do kernel, que agora está resolvido. 
  * Configuração do docker.service ao definir o RestartSecs = 10 para sempre reiniciar o Docker após 10 segundos. 

###  cos-69-10895-138-0

_Data: 24 de janeiro de 2019_

  * Correção aplicada retroativamente a um problema de impasse na falha do kernel. 
  * Versão estável do Linux Kernel 'v4.14.91' mesclada. 

###  cos-69-10895-123-0

_Data: 10 de janeiro de 2019_

  * Configuração do CONFIG_BLK_WBT_MQ=y para melhorar o desempenho do isolamento em discos permanentes. Isso corrige um erro em que as gravações em um disco permanente SSD podem afetar o desempenho no disco de inicialização permanente padrão. 
  * Seleção criteriosa de confirmações Ext4 que gerencia inconsistências causadas por interrupções da operação NFS CREATE em determinadas condições 
  * Versão estável do Linux Kernel "v4.14.89" mesclada. 

###  cos-69-10895-102-0

_Data: 20 de dezembro de 2018_

  * Atualização automática desativada em imagens protegidas. Imagens no cos-cloud não são afetadas por essa mudança. 
  * Ativação do recurso ext4 "metadata_csum" na partição com estado. O que também melhora o desempenho da operação de redimensionamento do disco de inicialização. 
  * Aplicação da Política IMA apenas quando o cloud-audit-setup.service for explicitamente executado. 

###  cos-69-10895-93-0

_Data: 16 de novembro de 2018_

  * Atualização do Kernel para v4.14.79. 
  * Correção do erro em que o cloud-init não grava arquivos com gzip. 

###  cos-69-10895-91-0

_Data: 29 de outubro de 2018_

  * Correção de um problema em que uma interação entre o IMA e o NFS poderia causar um impasse. 
  * Correção de um problema do "stackdriver-logging.service" observado em contêineres no Compute Engine. 
  * O PCID agora é ativado por padrão quando compatível com a plataforma da CPU. 

###  cos-69-10895-85-0

_Data: 11 de outubro de 2018_

  * softlockup_all_cpu_backtrace redefinido para "0" para evitar o impasse do kernel em máquinas de alta CPU em certas circunstâncias. 

###  cos-69-10895-71-0

_Data: 1º de outubro de 2018_

  * Remoção dos cabeçalhos de espaço do usuário do artefato de cabeçalho do kernel. 

###  cos-69-10895-62-0

_Data: 18 de setembro de 2018_

  * Promoção para canal Stable. 
  * Backport de uma correção para garantir que o scsi contribua para a aleatoriedade ao executar o dispositivo rotacional  . Isso resolve um problema em que o docker demora para iniciar devido à baixa entropia em PDs padrão desde a mesclagem da v4.14.63. 
  * CONFIG_RANDOM_TRUST_CPU ativado para resolver a privação de entropia em discos de inicialização PD-SSD. 
  * OpenSSL atualizado para 1.0.2p. 
  * Versão estável do Linux v4.14.65 mesclada. 
  * Backport da correção para um bug do cloud-init em que write_files não pode lidar com conteúdo não-asci  . 
  * Correção de backport para um aviso de kernel "WARNING: fs/overlayfs/readdir.c:393 ovl_iterate+0x25c/0x260 WARN_ON(!cache->refcount)" 
  * Correção para o kernel do Linux CVE-2018-12232 
  * Correções de backport para o problema "L1 Terminal Fault" (L1TF) (CVE-2018-3615, CVE-2018-3620 e CVE-2018-3646). 
  * Correções para CVE-2018-5391. 
  * Corrigido um problema de softlockup que ocorria em VMs VCPU únicas ao usar sistemas de arquivos FUSE. 
  * Kubernetes atualizado para v1.11.1. 
  * Correções para CVE-2018-5390 
  * kernel.pid_max padrão aumentado para 2^22. 
  * Versão estável do Linux v4.14.54 mesclada no kernel. 
  * Removido o suporte a CD-ROM SCSI. Isso resolve o CVE-2018-11506. 
  * Kubelet integrado atualizado para v1.11.0. 
  * docker-credential-gcr atualizado para 1.5.0 
  * BUG_REPORT_URL atualizado em /etc/os-release. 
  * Configurações de depuração NFS ativadas no kernel. 
  * Módulo de kernel tcp_bbr ativado para controle de congestionamento TCP. 
  * Git atualizado para a versão 2.16.4 para corrigir o CVE 2018-11235. 
  * Configuração do Docker "--disable-legacy-registry" definida como verdadeira por padrão. 
  * Kubernetes atualizado para 1.10.4. 
  * Sshd_config atualizado para descartar criptografias baseadas em cbc. 
  * Certificados de CA raiz atualizados para corresponder ao Mozilla NSS 3.36.1. 
  * OpenSSL atualizado para 1.0.2o. 

