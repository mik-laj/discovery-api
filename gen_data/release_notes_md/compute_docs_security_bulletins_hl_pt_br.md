#  Boletins de segurança

De vez em quando, lançamos boletins de segurança relacionados ao Compute
Engine. Todos eles estão descritos aqui.

[ Inscrever-se nos boletins de segurança do Compute Engine. ![Inscrever-
se](https://cloud.google.com/images/feed-icon.png?hl=pt_br)
](https://cloud.google.com/feeds/compute-engine-security-
bulletins.xml?hl=pt_br)

##  Data da publicação: 18/06/2019

**Última atualização: 25/06/2019, 6:30 (horário do Pacífico)**

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

A Netflix divulgou recentemente três vulnerabilidades do TCP nos kernels do
Linux:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Essas CVEs são coletivamente denominadas [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) (em inglês).

####  Impacto no Compute Engine

A infraestrutura que hospeda o Compute Engine tem proteção contra essa
vulnerabilidade.

As VMs do Compute Engine que executam sistemas operacionais Linux sem patches
e enviam/recebem tráfego de rede não confiável são vulneráveis a esse ataque
de DoS. É recomendado atualizar essas instâncias de VM assim que os patches
forem disponibilizados para os respectivos sistemas operacionais.

Balanceadores de carga que encerram conexões TCP receberam um patch que
corrige essa vulnerabilidade. As instâncias do Compute Engine que recebem
somente tráfego não confiável por meio desses balanceadores não estão
vulneráveis. Isso inclui balanceadores de carga HTTP, SSL Proxy e TCP Proxy.

Balanceadores de carga internos e de rede não encerram conexões TCP. As
instâncias do Compute Engine sem patches que recebem tráfego não confiável por
meio desses balanceadores de carga estão vulneráveis.

####  Imagens que receberam patch e recursos do fornecedor

Enviaremos links com informações sobre os patches de cada fornecedor de
sistema operacional assim que elas estiverem disponíveis, incluindo o status
de cada CVE. As versões anteriores dessas imagens públicas não contêm esses
patches e não reduzem o risco de possíveis ataques:

  * Projeto ` debian-cloud ` : 
    * ` debian-9-stretch-v20190618 `
  * Projeto ` centos-cloud ` : 
    * ` centos-6-v20190619 `
    * ` centos-7-v20190619 `
  * Projeto ` cos-cloud ` : 
    * ` cos-dev-77-12293-0-0 `
    * ` cos-beta-76-12239-21-0 `
    * ` cos-stable-75-12105-77-0 `
    * ` cos-73-11647-217-0 `
    * ` cos-69-10895-277-0 `
  * Projeto ` coreos-cloud ` : 
    * ` coreos-alpha-2163-2-1-v20190617 `
    * ` coreos-beta-2135-3-1-v20190617 `
    * ` coreos-stable-2079-6-0-v20190617 `
  * Projeto ` rhel-cloud ` : 
    * ` rhel-6-v20190618 `
    * ` rhel-7-v20190618 `
    * ` rhel-8-v20190618 `
  * Projeto ` rhel-sap-cloud ` : 
    * ` rhel-7-4-sap-v20190618 `
    * ` rhel-7-6-sap-v20190618 `
  * Projeto ` suse-cloud ` : 
    * ` sles-12-sp4-v20190617 `
    * ` sles-15-v20190617 `
  * Projeto ` suse-sap-cloud ` : 
    * ` sles-12-sp1-sap-v20190617 `
    * ` sles-12-sp2-sap-v20190617 `
    * ` sles-12-sp3-sap-v20190617 `
    * ` sles-12-sp4-sap-v20190617 `
    * ` sles-15-sap-v20190617 `
  * Projeto ` ubuntu-cloud ` : 
    * ` ubuntu-1604-xenial-v20190617 `
    * ` ubuntu-1804-bionic-v20190617 `
    * ` ubuntu-1810-cosmic-v20190618 `
    * ` ubuntu-1904-disco-v20190619 `
    * ` ubuntu-minimal-1604-xenial-v20190618 `
    * ` ubuntu-minimal-1804-bionic-v20190617 `
    * ` ubuntu-minimal-1810-cosmic-v20190618 `
    * ` ubuntu-minimal-1904-disco-v20190618 `

|  Média  |

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

  
  
##  Data da publicação: 14/05/2019

**Última atualização: 20/05/2019, 17:00 (horário do Pacífico)**

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

A Intel divulgou as CVEs a seguir:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Essas CVEs são coletivamente denominadas "amostragem de dados de
microarquitetura (MDS, na sigla em inglês)". Com essas vulnerabilidades, os
dados ficam em risco de exposição por meio da interação da execução
especulativa com o estado de microarquitetura.

####  Impacto no Compute Engine

**A infraestrutura de host que executa o Compute Engine isola as cargas de
trabalho do cliente umas das outras. Nenhuma ação extra é necessária a menos
que você esteja executando código não confiável nas VMs.**

Os clientes que executam código não confiável nos serviços de vários
locatários em máquinas virtuais do Compute Engine precisam consultar as
informações de mitigação recomendadas do fornecedor do SO convidado. Elas
podem incluir o uso dos recursos de mitigação de microcódigo da Intel.
Implantamos o acesso de passagem de convidado na nova funcionalidade de
liberação. Veja a seguir um resumo das etapas de mitigação disponíveis para
imagens comuns de convidado.

####  Imagens que receberam patch e recursos do fornecedor

Enviaremos links com informações sobre os patches de cada fornecedor do
sistema operacional assim que elas estiverem disponíveis, incluindo o status
de cada CVE. Use essas imagens para recriar instâncias de VM. As versões
anteriores dessas imagens públicas não contêm esses patches e não reduzem o
risco de possíveis ataques:

  * Projeto ` centos-cloud ` : [ CESA-2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) , [ CESA-2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html) (em inglês) 
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * Projeto ` coreos-cloud ` : [ mitigações de MDS para CoreOS Container Linux ](https://coreos.com/os/docs/latest/disabling-smt.html) (em inglês) 
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * Projeto ` cos-cloud `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * Projeto ` debian-cloud ` : [ DSA-4444 ](https://www.debian.org/security/2019/dsa-4444) (em inglês) 
    * ` debian-9-stretch-v20190514 `
  * Projeto ` rhel-cloud ` : [ artigo de informações de MDS do Red Hat ](https://access.redhat.com/security/vulnerabilities/mds) (em inglês) 
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * Projeto ` rhel-sap-cloud ` : [ artigo de informações de MDS do Red Hat ](https://access.redhat.com/security/vulnerabilities/mds) (em inglês) 
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * Projeto ` suse-cloud ` : [ base de conhecimento de MDS do SUSE ](https://www.suse.com/support/kb/doc/?id=7023736) (em inglês) 
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * Projeto ` suse-sap-cloud `
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * Projeto ` ubuntu-os-cloud ` : [ Wiki de MDS do Ubuntu ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS) (em inglês) 
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * Projetos ` windows-cloud ` e ` windows-sql-cloud ` : [ Microsoft ADV190013 ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013) (em inglês) 
    * Todas as imagens públicas do Windows Server e do SQL Server com o número de versão ` v20190514 ` . 
  * Projeto ` gce-uefi-images `
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * Todas as imagens públicas do Windows Server com o número de versão ` v20190514 ` . 

####  Container-Optimized OS

Se você usa o Container Optimized OS (COS) como SO convidado e está executando
cargas de trabalho não confiáveis de vários locatários na máquina virtual, é
recomendado o seguinte:

  1. Configure o ` nosmt ` na linha de comando do kernel para desativar o Hyper-Threading.   

Nas VMs atuais do COS, modifique o ` grub.cfg ` como mostrado a seguir para
definir a opção ` nosmt ` e reinicializar o sistema:

    
        
    # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

Por questões de conveniência, é possível executar o script abaixo para ter os
mesmos resultados que os comandos acima. Recomendamos que você o inclua nos
modelos de instância, scripts de inicialização e cloud-config para garantir
que as novas VMs usem esse novo parâmetro. Veja abaixo um exemplo de cloud-
config que executa o script.

**Aviso:** esse comando ativa a reinicialização imediata da instância quando
executado pela primeira vez. As próximas execuções do comando em uma instância
com o Hyper-Threading já desativado não terão efeito.

    
        
    # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

Para incluir esse comando como parte do cloud-config:

    
        
    #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

Para confirmar se o Hyper-Threading está desativado na instância, verifique a
saída dos arquivos ` /sys/devices/system/cpu/smt/active ` e `
/sys/devices/system/cpu/smt/control ` . Se o valor de ` active ` for ` 0 ` e o
de ` control ` for ` off ` , o Hyper-Threading estará desativado:

    
        
    cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**Observação:** se a inicialização segura UEFI estiver ativada na instância,
será necessário recriá-la com esse recurso desativado. Depois, você precisará
executar o comando acima com a inicialização segura UEFI desativada e ativar
esse recurso na nova instância.

  2. Use a nova versão da imagem do COS.   

Além de desativar o Hyper-Threading como descrito acima, você também precisa [
recriar as instâncias
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=pt_br#publicimage) com as imagens atualizadas listadas acima ou
com versões mais recentes disponíveis das imagens do Container-Optimized SO.
Só assim você terá proteção total contra a vulnerabilidade.

|  Média  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  Data da publicação: 14/08/2018

**Última atualização: 20/08/2018, 17:00 (horário do Pacífico)**

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

A [ Intel divulgou ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) as CVEs a seguir:

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) para [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) (links em inglês) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) para sistemas operacionais e [ SMT ](https://en.wikipedia.org/wiki/Hyper-Threading) (links em inglês) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) para virtualização (em inglês) 

Essas CVEs são coletivamente denominadas "L1 Terminal Fault (L1TF)".

As vulnerabilidades desse tipo atacam a configuração de estruturas de dados no
nível do processador para explorar a execução especulativa. "L1" se refere ao
cache de dados de nível 1 (L1D), um pequeno recurso dos núcleos usado para
acelerar o acesso à memória.

Leia a [ postagem do blog do Google Cloud
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=pt_br) para mais detalhes sobre essas
vulnerabilidades e as respectivas mitigações no Compute Engine.

####  Impacto no Compute Engine

A infraestrutura de host que executa o Compute Engine e isola as cargas de
trabalho do cliente umas das outras é protegida contra ataques conhecidos.

Recomendamos que os clientes do Compute Engine atualizem as imagens para
evitar a possibilidade de exploração indireta nos ambientes convidados deles.
Isso é importante principalmente para os clientes que executam os próprios
serviços de vários locatários nas máquinas virtuais do Compute Engine.

Os clientes do Google Compute Engine podem atualizar os sistemas operacionais
convidados nas instâncias deles usando uma das seguintes opções:

  * Use imagens públicas que receberam patch para [ recriar instâncias de VM ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=pt_br#publicimage) . 
  * Em instâncias atuais, instalar os patches cedidos pelo fornecedor do sistema operacional e reinicie as instâncias que receberam patch. 

####  Imagens que receberam patch e recursos do fornecedor

Enviaremos links com informações sobre os patches de cada fornecedor do
sistema operacional assim que estiverem disponíveis, incluindo o status de
ambas as CVEs. Use essas imagens para recriar instâncias de VM. As versões
anteriores dessas imagens públicas não têm esses patches e não diminuem os
riscos de possíveis ataques.

  * Projeto ` centos-cloud ` : 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Projeto ` coreos-cloud ` : 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Projeto ` cos-cloud ` : 
    * ` cos-stable-66-10452-110-0 `
    * ` cos-stable-67-10575-66-0 `
    * ` cos-beta-68-10718-81-0 `
    * ` cos-dev-69-10895-23-0 `
  * Projeto ` debian-cloud ` : 
    * ` debian-9-stretch-v20180820 `
  * Projeto ` rhel-cloud ` : 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Projeto ` rhel-sap-cloud ` : 
    * ` rhel-7-sap-apps-v20180814 `
    * ` rhel-7-sap-hana-v20180814 `
  * Projeto ` suse-cloud ` : 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
    * ` sles-11-sp4-v20180816 `
  * Projeto ` suse-sap-cloud ` : 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Projeto ` ubuntu-os-cloud ` : 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `
  * Projetos ` windows-cloud ` ` gce-uefi-images ` e ` windows-sql-cloud ` : 
    * Todas as [ imagens públicas ](https://cloud.google.com/compute/docs/images?hl=pt_br#os-compute-support) do Windows Server e do SQL Server com o número de versão ` -v201800814 ` e posterior têm patches. 

|  Alta  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  Data da publicação: 06/08/2018

**Última atualização: 05/09/2018, 17:00 (horário do Pacífico)**

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Atualização: 05/09/2018

A [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) (em inglês) foi publicada em 14/08/2018
pela US-CERT. Assim como a [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) (em inglês), trata-se de uma
vulnerabilidade de rede no nível do kernel que aumenta a eficácia de ataques
de negação de serviço (DoS, na sigla em inglês) em sistemas vulneráveis. A
principal diferença é que a CVE-2018-5391 pode ser explorada em conexões IP.
Atualizamos este boletim para cobrir as duas vulnerabilidades.

####  Descrição

Na [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack"), há a descrição de uma
vulnerabilidade de rede no nível do kernel que aumenta a eficácia de ataques
de negação de serviço (DoS) em sistemas vulneráveis com conexões TCP.

Na [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack"), há a descrição de uma
vulnerabilidade de rede no nível do kernel que aumenta a eficácia de ataques
de negação de serviço (DoS) em sistemas vulneráveis sobre conexões IP.

####  Impacto no Compute Engine

A infraestrutura de host que executa VMs do Compute Engine não está em risco.
A infraestrutura de rede que processa o tráfego com origem e destino nas VMs
do Compute Engine está protegida contra essa vulnerabilidade. As VMs do
Compute Engine que apenas enviam/recebem tráfego de rede não confiável por
meio de [ balanceadores de carga HTTP(S) ](https://cloud.google.com/load-
balancing/docs/https/?hl=pt_br) , [ SSL ](https://cloud.google.com/load-
balancing/docs/ssl/?hl=pt_br) ou [ TCP ](https://cloud.google.com/load-
balancing/docs/tcp/?hl=pt_br) estão protegidas contra essa vulnerabilidade.

As VMs do Compute Engine que executam sistemas operacionais sem patches que
enviam/recebem tráfego que não é confiável diretamente ou por meio de [
balanceadores de carga de rede ](https://cloud.google.com/load-
balancing/docs/network/?hl=pt_br) estão vulneráveis a esse ataque de DoS.

Recomendamos atualizar suas instâncias de VM assim que os patches forem
disponibilizados para os respectivos sistemas operacionais.

Os clientes do Compute Engine podem atualizar os sistemas operacionais
convidados nas instâncias usando uma das seguintes opções:

  * Use imagens públicas que receberam patch para [ recriar instâncias de VM ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=pt_br#publicimage) . Veja a seguir a lista de imagens públicas que receberam patch. 
  * Em instâncias, instale os patches cedidos pelo fornecedor do sistema operacional e reinicie as instâncias que receberam patch. 

####  Imagens que receberam patch e recursos do fornecedor

Enviaremos links com informações de patches de cada fornecedor de sistema
operacional, assim que estiverem disponíveis.

  * Projeto ` centos-cloud ` (apenas CVE-2018-5390): 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Projeto ` coreos-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Projeto ` cos-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` cos-stable-65-10323-98-0 `
    * ` cos-stable-66-10452-109-0 `
    * ` cos-stable-67-10575-65-0 `
    * ` cos-beta-68-10718-76-0 `
    * ` cos-dev-69-10895-16-0 `
  * Projeto ` debian-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` debian-9-stretch-v20180814 `
  * Projeto ` rhel-cloud ` (apenas CVE-2018-5390): 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Projeto ` suse-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
  * Projeto ` suse-sap-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Projeto ` ubuntu-os-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `

|  Alta  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  Data da publicação: 03/01/2018

**Última atualização: 21/05/2018, 15:00 (horário do Pacífico)**

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Atualização: 21/05/2018

A [ CVE-2018-3640 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-3640) e a [ CVE-2018-3639
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639) , variantes 3a
e 4, respectivamente, foram [ divulgadas pela Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00115.html) (links em inglês). Assim como no caso das primeiras três
variantes do Spectre e do Meltdown, a infraestrutura em que as instâncias de
VM do Compute Engine são executadas está protegida, e as instâncias de VM de
clientes estão isoladas e protegidas umas das outras. Além disso, a equipe do
Compute Engine planeja implantar patches de microcódigo da Intel na nossa
infraestrutura. Isso permitirá que os clientes que executam cargas de trabalho
não confiáveis ou multilocatárias em uma única instância de VM habilitem
mitigações na própria VM quando essas mitigações forem disponibilizadas pelos
fornecedores de sistemas operacionais. A equipe do Compute Engine implantará
os patches de microcódigo após a certificação da Intel, depois de testá-los e
qualificá-los para nosso ambiente de produção. Apresentaremos cronogramas e
atualizações mais detalhados nesta página quando eles estiverem disponíveis.

####  Descrição

Essas CVEs são variantes de uma nova classe de ataque. Elas exploram a
tecnologia de execução especulativa disponível em muitos processadores. Essa
classe de ataque pode permitir acesso somente leitura não autorizado aos dados
da memória em diversas circunstâncias.

O Google Compute Engine usou a tecnologia VM Live Migration para executar
atualizações no sistema host e no hipervisor sem impacto ao usuário, sem
janelas de manutenção forçadas e sem a necessidade de uma reinicialização
geral. No entanto, é preciso corrigir todos os sistemas operacionais
convidados e versões para fins de proteção contra essa nova classe de ataque,
independentemente do lugar de execução desses sistemas.

Leia a [ postagem do blog Project Zero
](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-
with-side.html) para saber detalhes técnicos completos sobre esse método de
ataque. Leia a [ postagem do blog de segurança do Google
](https://security.googleblog.com/2018/01/todays-cpu-vulnerability-what-you-
need.html) (em inglês) para saber detalhes completos sobre as mitigações do
Google, incluindo todas as informações específicas de produto.

####  Impacto no Compute Engine

A infraestrutura que executa o Compute Engine e isola as instâncias de VM do
cliente umas das outras é protegida contra ataques conhecidos. Nossas ações de
redução de danos impedem o acesso não autorizado a nossos sistemas host de
aplicativos que estão sendo executados em instâncias de VM. Essas ações também
impedem o acesso não autorizado entre instâncias de VM que funcionam no mesmo
sistema host.

Para evitar o acesso não autorizado nas instâncias da máquina virtual, é
necessário atualizar os sistemas operacionais convidados nessas instâncias
usando uma das seguintes opções:

  * Use imagens públicas que receberam patch para [ recriar suas instâncias de VM ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=pt_br#publicimage) . Veja a seguir a lista de imagens públicas que receberam patch. 
  * Em suas instâncias, instale os patches cedidos pelo fornecedor do sistema operacional para sua distribuição e reinicie as instâncias que receberam patch. Veja a seguir links para informações sobre os patches de cada fornecedor do sistema operacional. 

####  Imagens que receberam patch e recursos do fornecedor

**Observação:** as imagens que receberam patch podem não incluir correções
para todas as CVEs listadas neste aviso do boletim de segurança. Além disso,
imagens diferentes podem incluir diferentes métodos para prevenir esses tipos
de ataques. Entre em contato com o fornecedor do sistema operacional para
confirmar quais CVEs eles abordam nos respectivos patches e quais métodos de
prevenção eles usam.

  * Projeto ` cos-cloud ` : inclui patches que impedem os ataques da variante 2 ( [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ) e da variante 3 ( [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ). O Google usou a [ Retpoline ](https://support.google.com/faqs/answer/7625886?hl=pt_br) nessas imagens para diminuir os ataques da Variante 2. 
    * ` cos-stable-63-10032-71-0 ` ou família de imagens ` cos-stable `
  * Projeto ` centos-cloud ` : [ informações de patch do CentOS ](https://lwn.net/Alerts/CentOS/) (em inglês) 
    * ` centos-7-v20180104 ` ou família de imagens ` centos-7 `
    * ` centos-6-v20180104 ` ou família de imagens ` centos-6 `
  * Projeto ` coreos-cloud ` : [ informações de patch do CoreOS ](https://coreos.com/blog/container-linux-meltdown-patch) (em inglês) 
    * ` coreos-stable-1576-5-0-v20180105 ` ou família de imagens ` coreos-stable `
    * ` coreos-beta-1632-1-0-v20180105 ` ou família de imagens ` coreos-beta `
    * ` coreos-alpha-1649-0-0-v20180105 ` ou família de imagens ` coreos-alpha `
  * Projeto ` debian-cloud ` : [ informações de patch do Debian ](https://www.debian.org/security/#DSAS) (em inglês) 
    * ` debian-9-stretch-v20180105 ` ou família de imagens ` debian-9 `
    * ` debian-8-jessie-v20180109 ` ou família de imagens ` debian-8 `
  * Projeto ` rhel-cloud ` : [ informações de patch do RHEL ](https://access.redhat.com/security/vulnerabilities/speculativeexecution) (em inglês) 
    * ` rhel-7-v20180104 ` ou família de imagens ` rhel-7 `
    * ` rhel-6-v20180104 ` ou família de imagens ` rhel-6 `
  * Projeto ` suse-cloud ` : [ informações de patch do SUSE ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/) (em inglês) 
    * ` sles-12-sp3-v20180104 ` ou família de imagens ` sles-12 `
    * ` sles-11-sp4-v20180104 ` ou família de imagens ` sles-11 `
  * Projeto ` suse-sap-cloud ` : [ informações de patch do SUSE ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/) (em inglês) 
    * ` sles-12-sp3-sap-v20180104 ` ou família de imagens ` sles-12-sp3-sap `
    * ` sles-12-sp2-sap-v20180104 ` ou família de imagens ` sles-12-sp2-sap `
  * Projeto ` ubuntu-os-cloud ` : [ informações de patch do Ubuntu ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/) (em inglês) 
    * ` ubuntu-1710-artful-v20180109 ` ou família de imagens ` ubuntu-1710 `
    * ` ubuntu-1604-xenial-v20180109 ` ou família de imagens ` ubuntu-1604-lts `
    * ` ubuntu-1404-trusty-v20180110 ` ou família de imagens ` ubuntu-1404-lts `
  * Projetos ` windows-cloud ` e ` windows-sql-cloud ` : 
    * Todas as [ imagens públicas ](https://cloud.google.com/compute/docs/images?hl=pt_br#os-compute-support) do Windows Server e do SQL Server com número de versão ` -v20180109 ` e posterior têm patches. No entanto, você precisa seguir as ações recomendadas fornecidas pela Microsoft no boletim de suporte de [ orientação do Windows Server ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) para habilitar e verificar essas ações de redução em suas instâncias e instâncias criadas recentemente. 

Use essas imagens para [ recriar suas instâncias de VMs
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=pt_br#publicimage) . As versões anteriores dessas imagens públicas
não têm esses patches e não reduzem os danos de possíveis ataques.

####  Patches de fornecedores de hardware

A NVIDIA fornece drivers de patch para reduzir possíveis ataques contra
sistemas com o software do driver da NVIDIA® instalado. Para saber quais
versões de driver são corrigidas, leia o boletim de segurança [ Atualizações
de segurança no driver de exibição da GPU da NVIDIA
](http://nvidia.custhelp.com/app/answers/detail/a_id/4611) (em inglês) da
NVIDIA.

####  Histórico de revisão:

  * 21/05/2018 T 14h PST: informações adicionadas sobre duas novas variantes divulgadas em 21 de maio de 2018. 
  * 10/01/2018 T 15h PST: informações adicionadas sobre imagens públicas do Windows Server e do SQL Server corrigidas. 
  * 10/01/2018 T 10h15 PST: várias imagens Ubuntu adicionadas à lista de imagens públicas corrigidas. 
  * 10/01/2018 T 09h50 PST: fornecedores de hardware adicionaram orientações para correções. 
  * 03/01/2018 a 29/01/2018: várias revisões realizadas na lista de imagens públicas corrigidas. 

|  Alta  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  Data da publicação: 02/10/2017

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

O [ Dnsmasq ](http://www.thekelleys.org.uk/dnsmasq/doc.html) fornece
funcionalidades para veicular DNS, DHCP, anúncios de roteadores e
inicialização de rede. Normalmente, esse software é instalado em sistemas tão
variados quanto distribuições Linux para desktop (como Ubuntu), roteadores
domésticos e dispositivos IoT. O Dnsmasq é amplamente utilizado, tanto na
Internet aberta quanto internamente em redes privadas.

O Google descobriu sete problemas diferentes ao longo de nossas avaliações de
segurança interna regulares. Depois de determinarmos a gravidade desses
problemas, trabalhamos para investigar o impacto e a capacidade de exploração
deles e, em seguida, produzimos provas internas de conceito para cada um
deles. Também trabalhamos com o mantenedor do Dnsmasq, Simon Kelly, para
produzir os patches adequados e mitigar o problema.

Durante nossa revisão, a equipe encontrou três possíveis execuções de código
remoto, um vazamento de informações e três vulnerabilidades de negação de
serviço que afetam a versão mais recente no servidor git do projeto em 5 de
setembro de 2017.

Esses patches são encaminhados e inseridos no [ repositório Git do projeto
](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) (em inglês).

####  Impacto no Compute Engine

Por padrão, o Dnsmasq só é instalado em imagens que usam [ NetworkManager
](https://wikipedia.org/wiki/NetworkManager) (em inglês) e fica inativo por
padrão. As imagens públicas do Compute Engine a seguir têm o Dnsmasq
instalado:

  * Ubuntu 16.04, 16.10, 17.04 
  * CentOS 7 
  * RHEL 7 

No entanto, outras imagens podem ter o Dnsmasq instalado como uma dependência
de outros pacotes. Recomendamos que você atualize suas instâncias Debian,
Ubuntu, CentOS, RHEL, SLES e OpenSuse para que elas usem a imagem mais recente
do sistema operacional. O CoreOS e o Container-Optimized SO não são afetados.
As imagens do Windows também não são afetadas.

Para instâncias com o Debian e Ubuntu, execute uma atualização com os
seguintes comandos em sua instância:

    
    
    
    sudo apt-get -y update
    
    
    
    sudo apt-get -y dist-upgrade

Para instâncias do Red Hat Enterprise Linux e CentOS, execute:

    
    
    
    sudo yum -y upgrade

Para imagens SLES e OpenSUSE, execute:

    
    
    
    sudo zypper up

Como alternativa à execução dos comandos de atualização manual, [ recrie
instâncias de VM usando as famílias de imagens
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=pt_br#publicimage) do respectivo sistema operacional.

|  Alta  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  Data da publicação: 26/10/2016

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

A CVE-2016-5195 é uma disputa encontrada quando o subsistema de memória do
kernel Linux manipulava a quebra da cópia na escrita (COW, na sigla em inglês)
do mapeamento de memória particular somente de leitura.

Um usuário local sem privilégios pode usar essa falha para ter acesso de
gravação a mapeamentos de memória somente de leitura e, assim, aumentar os
privilégios dele no sistema.

Para mais informações, consulte [ Perguntas frequentes sobre Dirty COW
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)
(em inglês).

####  Impacto no Compute Engine

Todas as distribuições e versões do Linux no Compute Engine são afetadas. A
maioria das instâncias faz o download e a instalação de um kernel mais recente
automaticamente. No entanto, é necessário reinicializar para corrigir o
sistema em execução.

Instâncias novas ou recriadas com base nas seguintes imagens do Compute Engine
têm kernels com patches já instalados.

  * ` centos-6-v20161026 `
  * ` centos-7-v20161025 `
  * ` coreos-alpha-1192-2-0-v20161021 `
  * ` coreos-beta-1185-2-0-v20161021 `
  * ` coreos-stable-1122-3-0-v20161021 `
  * ` debian-8-jessie-v20161020 `
  * ` rhel-6-v20161026 `
  * ` rhel-7-v20161024 `
  * ` sles-11-sp4-v20161021 `
  * ` sles-12-sp1-v20161021 `
  * ` ubuntu-1204-precise-v20161020 `
  * ` ubuntu-1404-trusty-v20161020 `
  * ` ubuntu-1604-xenial-v20161020 `
  * ` ubuntu-1610-yakkety-v20161020 `

|  Alta  |  [ CVE-2016-5195
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)  
  
##  Data da publicação: 16/02/2016

**Última atualização: 22/02/2016**

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

A CVE-2015-7547 é uma vulnerabilidade na qual o resolvedor do cliente DNS
glibc deixa o software vulnerável a um estouro de buffer baseado em pilha,
quando se usa a função da biblioteca ` getaddrinfo() ` . Um invasor se
beneficia do software usando a função para explorar essa vulnerabilidade, com
nomes de domínio e servidores DNS controlados pelo invasor, ou por meio de um
ataque indireto.

Para mais detalhes, consulte o [ blog de segurança on-line do Google
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) ou o banco de dados [ Common Vulnerabilities and
Exposures (CVE) ](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-7547)
(links em inglês).

####  Impacto no Compute Engine

**Atualização em 22/02/2016:**

Agora é possível recriar suas instâncias usando as seguintes imagens do
CoreOS, SLES e OpenSUSE:

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**Atualização em 17/02/2016:**

Agora é possível fazer uma atualização nas instâncias do Ubuntu 12.04 LTS,
Ubuntu 14.04 LTS e Ubuntu 15.10 executando os seguintes comandos:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Como alternativa para executar comandos de atualização manual, recrie as
instâncias com estas imagens novas:

  * ` backports-debian-7-wheezy-v20160216 `
  * ` centos-6-v20160216 `
  * ` centos-7-v20160216 `
  * ` debian-7-wheezy-v20160216 `
  * ` debian-8-jessie-v20160216 `
  * ` rhel-6-v20160216 `
  * ` rhel-7-v20160216 `
  * ` ubuntu-1204-precise-v20160217a `
  * ` ubuntu-1404-trusty-v20160217a `
  * ` ubuntu-1510-wily-v20160217 `

Desconhecemos métodos que possam explorar essa vulnerabilidade por meio dos
resolvedores DNS do Compute Engine com a configuração glibc padrão. Ainda é
necessário fazer patches nas instâncias das suas máquinas virtuais o mais
rápido possível porque, assim como acontece com qualquer nova vulnerabilidade,
novos métodos de exploração são descobertos ao longo do tempo. Se você ativou
o edns0 (desativado por padrão), é necessário desabilitá-lo até que os patches
sejam aplicados às suas instâncias.

**Boletim original:**

É possível que sua distribuição Linux esteja vulnerável. Clientes do Compute
Engine precisam atualizar as imagens do sistema operacional das instâncias
deles para eliminar essa vulnerabilidade, caso estejam executando um SO Linux.

Para instâncias que executam o Debian, atualize com os seguintes comandos:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Recomendamos também a instalação de [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) para suas instâncias do Debian.

Para instâncias do Red Hat Enterprise Linux:

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

Atualizaremos esse boletim assim que outros responsáveis pela manutenção de
sistemas operacionais publicarem patches para essa vulnerabilidade, e o
Compute Engine liberar imagens atualizadas desses sistemas.

|  Alta  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  Data da publicação: 19/03/2015

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

A CVE-2015-1427 é uma vulnerabilidade em que o mecanismo de script Groovy no [
Elasticsearch ](https://www.elastic.co/products/elasticsearch) anterior à
versão 1.3.8 e outras versões 1.4.x anteriores à 1.4.3 permite que invasores
remotos ignorem o mecanismo de proteção sandbox e executem os comandos shell
que quiserem.

Para mais detalhes, consulte o [ National Vulnerability Database (NVD)
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) ou o banco
de dados [ Common Vulnerabilities and Exposures (CVE)
](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-1427) (links em
inglês).

####  Impacto no Compute Engine

Se você está executando o Elasticsearch nas suas instâncias do Compute Engine,
faça upgrade do Elasticsearch para a versão 1.4.3 ou posterior. Se o upgrade
já foi feito, você está protegido contra essa vulnerabilidade.

Se você não fez o upgrade do Elasticsearch 1.4.3 ou superior, é possível [
fazer um upgrade contínuo
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) .

Se você implantou o Elasticsearch usando o recurso [ click-to-deploy
](https://cloud.google.com/solutions/elasticsearch/click-to-deploy?hl=pt_br)
no [ Console do Google Cloud Platform
](https://console.cloud.google.com/?hl=pt_br) , é possível [ excluir a
implantação
](https://console.cloud.google.com/projectselector/deployments?hl=pt_br) para
remover instâncias que executem o Elasticsearch.

A equipe do Google Cloud Platform está trabalhando em uma correção para
implantar uma versão atualizada do Elasticsearch. No entanto, a correção ainda
não está disponível para o recurso click-to-deploy no [ Console do GCP
](https://console.cloud.google.com/?hl=pt_br) .

|  Alta  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  Data da publicação: 29/01/2015

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

A [ CVE-2015-0235 (Ghost)
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) é uma
vulnerabilidade na biblioteca glibc.

Não é necessária nenhuma ação de clientes do App Engine, Cloud Storage,
BigQuery e Cloud SQL. Os servidores do Google foram atualizados e estão
protegidos contra essa vulnerabilidade.

Talvez os clientes do Compute Engine precisem atualizar as imagens do SO.

####  Impacto no Compute Engine

É possível que sua distribuição Linux esteja vulnerável. Clientes do Compute
Engine precisam atualizar as imagens do sistema operacional das instâncias
deles para eliminar essa vulnerabilidade, caso estejam executando o Debian 7,
Debian 7 backports, Ubuntu 12.04 LTS, Red Hat Enterprise Linux, CentOS ou o
SUSE Linux Enterprise Server 11 SP3.

Essa vulnerabilidade não afeta o Ubuntu 14.04 LTS, o Ubuntu 14.10 nem o SUSE
Linux Enterprise Server 12.

Recomendamos que você faça o upgrade das suas distribuições Linux. Para
instâncias que executam o Debian 7, Debian 7 backports ou Ubuntu 12.04 LTS,
atualize com os seguintes comandos:

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Para instâncias do Red Hat Enterprise Linux ou CentOS:

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

Para instâncias do SUSE Linux Enterprise Server 11 SP3:

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

Como alternativa para executar os comandos de atualização manual acima, os
usuários recriam as instâncias deles com estas imagens novas:

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  Impacto na VM gerenciada do Google

Usuários de VM gerenciada que utilizam ` gcloud preview app deploy ` precisam
atualizar os contêineres base do docker com ` gcloud preview app setup-
managed-vms ` e implantar novamente cada um dos apps em execução usando `
gcloud preview app deploy ` . Usuários que implantam com o ` appcfg ` não
precisam fazer nada. O upgrade é feito automaticamente.

|  Alta  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  Data da publicação: 15/10/2014

**Última atualização: 17/10/2014**

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

A CVE-2014-3566 (também conhecida como POODLE) é uma vulnerabilidade na
concepção do SSL, versão 3.0. Essa vulnerabilidade permite que o plaintext de
conexões seguras seja calculado por um invasor de rede. Para mais detalhes,
confira nossa [ postagem do blog
](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) sobre a vulnerabilidade.

Não é necessária nenhuma ação de clientes do App Engine, Cloud Storage,
BigQuery e Cloud SQL. Os servidores do Google foram atualizados e estão
protegidos contra essa vulnerabilidade. Os clientes do Compute Engine precisam
atualizar as imagens do SO.

####  Impacto no Compute Engine

**Atualizado em 17/10/2014:**

Se você está usando o SSLv3, é possível que esteja vulnerável. Clientes do
Compute Engine precisam atualizar as imagens do SO das instâncias deles para
eliminar essa vulnerabilidade.

Recomendamos que você faça o upgrade das suas distribuições Linux. Para
instâncias que executam o Debian, atualize com os seguintes comandos:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

Para instâncias do CentOS:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

Como alternativa para executar os comandos de atualização manual acima, os
usuários recriam as instâncias deles com estas imagens novas:

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

Vamos atualizar o boletim para imagens RHEL e SLES assim que tivermos as
imagens. Enquanto isso, os usuários do RHEL podem consultar a [ Red Hat
](https://access.redhat.com/articles/1232123) para mais informações.

**Boletim original:**

Os clientes do Compute Engine precisam atualizar as imagens do SO das
instâncias deles para eliminar essa vulnerabilidade. Esse boletim de segurança
será atualizado com instruções assim que novas imagens do SO estiverem
disponíveis.

|  Média  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  Data da publicação: 24/09/2014

**Última atualização: 29/09/2014**

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

Há um bug no bash (CVE-2014-6271) que permite a execução remota do código
baseado em análise de qualquer variável de ambiente controlada pelo invasor. O
vetor mais provável de exploração ocorre por meio de solicitações HTTP mal-
intencionadas feitas para scripts CGI (Common Gateway Interface) expostos em
um servidor da Web. Para mais informações, consulte a [ descrição do bug
](http://seclists.org/oss-sec/2014/q3/650) .

Os bugs do bash foram minimizados para produtos do Google Cloud Platform,
exceto para imagens do SO convidado do Compute Engine com data anterior a
26/09/2014. Consulte abaixo as etapas para mitigar os bugs das suas imagens do
Compute Engine.

####  Impacto no Compute Engine

Esse bug afeta quase todos os sites que usam scripts CGI. Além disso, ele
provavelmente afeta sites que dependem de PHP, Perl, Python, SSI, Java, C++ e
servlets semelhantes que sempre invocam comandos shell por meio de chamadas
como ` popen ` , ` system ` , ` shell_exec ` ou APIs semelhantes. Ele também
afeta sistemas que tentam conceder acesso de login controlado a usuários
restritos por meio de mecanismos como limitação de comando SSH ou shell
restrito do bash.

**Atualização em 29/09/2014:**

Como alternativa à execução dos comandos de atualização manual abaixo, os
usuários agora podem recriar instâncias com imagens que mitiguem outras
vulnerabilidades relacionadas ao bug de segurança do bash, incluindo [
CVE-2014-7169 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169)
, [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) , [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
, [ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) e [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)
(links em inglês). Use estas imagens novas para recriar suas instâncias:

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**Atualização em 25/09/2014:**

Os usuários agora podem recriar as instâncias deles em vez de executar uma
atualização manual. Para recriar suas instâncias, use estas imagens novas que
contêm correções para este bug de segurança:

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

Para imagens RHEL e SUSE, faça as atualizações manualmente executando os
seguintes comandos em suas instâncias:

    
    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**Boletim original:**

Recomendamos que você faça o upgrade das suas distribuições Linux. Para
instâncias com o Debian, execute os seguintes comandos:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

Para instâncias do CentOS:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade

Para mais informações, analise o anúncio da respectiva distribuição Linux:

  * Patches originais: [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) , consulte a última entrada em *-patches para a versão apropriada 
  * Debian: [ [SECURITY] [DSA 3032-1] atualização de segurança do bash ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
  * RHEL: 
    * [ RHSA-2014:1293-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00048.html)
    * [ RHSA-2014:1294-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00049.html)
  * CentOS 5: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020582.html)
  * CentOS 6: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020585.html)
  * CentOS 7: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020583.html)

|  Alta  |  [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6271 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271)
, [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) , [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
[ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) , [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  Data da publicação: 25/07/2014

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

O [ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/)
é vulnerável à injeção de comando do SO que permite modificação e divulgação
não autorizadas de dados. Um invasor envia eventos elaborados para qualquer
uma das fontes de dados do Logstash, possibilitando a execução de comandos com
permissões do processo do Logstash.

####  Impacto no Compute Engine

Essa vulnerabilidade afeta todas as instâncias do Compute Engine que executam
versões do Elasticsearch Logstash anteriores à 1.4.2 com saídas Zabbix ou
nagios_nsca ativadas. Para evitar o ataque, siga estas etapas:

  * Faça o upgrade para Logstash 1.4.2. 
  * Aplique o patch nas versões 1.3.x. 
  * Desative as saídas ` zabbix ` e ` nagios_nsca ` . 

Leia mais sobre no [ blog Logstash
](http://www.elasticsearch.org/blog/logstash-1-4-2/) .

O Elasticsearch também recomenda o [ uso de um firewall
](http://www.elasticsearch.org/blog/scripting-security/) para impedir o acesso
remoto de IPs não confiáveis.

|  Alta  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  Data da publicação: 18/06/2014

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

Durante execução no Google Cloud Platform, vamos reservar um momento para
responder a eventuais dúvidas dos clientes sobre segurança de contêineres do
Docker. Isso inclui clientes que utilizam as extensões do App Engine que
suportam contêineres do Docker, máquinas virtuais otimizadas de contêiner ou
programador de Kubernetes de código aberto.

O excelente trabalho feito pelo Docker em resposta aos problemas está no blog.
Clique [ aqui ](http://blog.docker.com/2014/06/docker-container-breakout-
proof-of-concept-exploit/) e confira. Observe que, como diz a resposta, o
problema revelado só se aplica ao Docker 0.11, uma versão antiga de pré-
produção.

Com a preocupação mundial sobre segurança de contêiner, queremos observar que,
no Google Cloud Platform, as soluções baseadas em contêiner de aplicativo do
Linux (especificamente contêineres do Docker) são executadas em máquinas
virtuais completas (Compute Engine). Mesmo com nosso apoio aos esforços da
comunidade do Docker para fortalecer a pilha de contêineres de aplicativos do
Linux, reconhecemos que a tecnologia é nova e a área de superfície é grande.
Acreditamos que, por enquanto, hipervisores completos (máquinas virtuais)
oferecem uma área de superfície mais compacta e justificável. As máquinas
virtuais foram projetadas desde o início para isolar cargas de trabalho mal-
intencionadas e minimizar a probabilidade e o impacto de um bug de código.

Nossos clientes podem ter certeza de que existe um limite de hipervisor
completo entre eles e qualquer código potencialmente mal-intencionado de
terceiros. Quando considerarmos a pilha de contêineres de aplicativos do Linux
robusta o suficiente para suportar cargas de trabalho com hospedagem múltipla,
informaremos à comunidade. Por enquanto, o contêiner de aplicativos do Linux
não substitui a máquina virtual. É uma maneira de ter um desempenho ainda
melhor.

|  Baixa  |  [ Postagem do blog do Docker (em inglês)
](http://blog.docker.com/2014/06/docker-container-breakout-proof-of-concept-
exploit/)  
  
##  Data da publicação: 05/06/2014

**Última atualização: 09/06/2014**

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

No OpenSSL, as mensagens ` ChangeCipherSpec ` não são vinculadas corretamente
à maquina no estado handshake. Isso permite que elas sejam inseridas
antecipadamente no handshake. Um invasor que usa um handshake bem desenvolvido
força o uso de material de chave fraca em clientes e servidores do OpenSSL
SSL/TLS. É possível que isso seja explorado por um ataque indireto (MITM, na
sigla em inglês), em que o invasor descriptografa e modifica o tráfego do
cliente e do servidor invadido.

Esse problema é identificado como [ CVE-2014-0224
](https://www.openssl.org/news/secadv/20140605.txt) . A equipe do OpenSSL
corrigiu o problema e alertou a comunidade do OpenSSL para atualizá-lo.

####  Impacto no Compute Engine

Essa vulnerabilidade afeta todas as instâncias do Compute Engine que usam
OpenSSL, inclusive Debian, CentOS, Red Hat Enterprise Linux e SUSE Linux
Enterprise Server. Atualize suas instâncias recriando-as com novas imagens ou
atualizando manualmente os pacotes.

**Atualização em 09/06/2014:** para atualizar as instâncias que executam o
SUSE Linux Enterprise Server com novas imagens, recrie-as usando as seguintes
versões de imagem ou superiores:

  * ` sles-11-sp3-v20140609 `

**Postagem original:**

Para atualizar instâncias do Debian e do CentOS usando novas imagens, recrie
suas instâncias usando uma das seguintes versões de imagem ou superiores:

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

Para atualizar manualmente o OpenSSL em suas instâncias, execute os seguintes
comandos para atualizar os pacotes apropriados. Para instâncias com o CentOS e
o RHEL, atualize o OpenSSL executando estes comandos:

    
    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

Para instâncias que executam o Debian, atualize o OpenSSL com os seguintes
comandos:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

Para instâncias com o SUSE Linux Enterprise Server, garanta a atualização do
OpenSSL executando estes comandos:

    
    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  Média  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  Data da publicação: 08/04/2014

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

As implementações (1) TLS e (2) DTLS no OpenSSL 1.0.1 anteriores a 1.0.1g não
manipulam devidamente os pacotes de extensão do Heartbeat. Isso permite que
invasores remotos acessem informações confidenciais da memória do processo por
meio de pacotes elaborados que acionam um excesso de leitura no buffer, como
demonstrado pela leitura de chaves privadas relacionadas a ` d1_both.c ` e `
t1_lib.c ` , o que é conhecido como bug Heartbleed.

####  Impacto no Compute Engine

Essa vulnerabilidade afeta todas as instâncias de Debian, RHEL e CentOS do
Compute Engine que não têm a versão mais atualizada do OpenSSL. Atualize suas
instâncias recriando-as com imagens novas ou atualizando manualmente os
pacotes.

Para atualizar suas instâncias usando novas imagens, recrie-as usando qualquer
uma das seguintes versões de imagem ou superiores:

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

Para atualizar manualmente o OpenSSL em suas instâncias, execute os seguintes
comandos para atualizar os pacotes apropriados. Para instâncias com o CentOS e
o RHEL, garanta a atualização do OpenSSL executando estes comandos:

    
    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

Para instâncias que executam o Debian, atualize o OpenSSL com os seguintes
comandos:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

Instâncias que executam o SUSE Linux não são afetadas.

**Atualização em 14 de abril de 2014:** segundo o critério de novas pesquisas
sobre extração de chaves usando o bug Heartbleed, o Compute Engine recomenda
que seus clientes criem novas chaves para qualquer serviço SSL afetado.

|  Média  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  Data da publicação: 07/06/2013

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

**Observação:** essa vulnerabilidade só é aplicável a kernels obsoletos e
removidos desde a versão v1 da API.

A vulnerabilidade de string de formato na função ` b43_request_firmware ` em `
drivers/net/wireless/b43/main.c ` , no driver sem fio Broadcom B43, no kernel
do Linux por meio do 3.9.4, permite que usuários locais recebam privilégios ao
aproveitar o acesso root e ao incluir especificadores de string de formato em
um parâmetro ` fwpostfix ` do modprobe, levando à construção indevida de uma
mensagem de erro.

####  Impacto no Compute Engine

Essa vulnerabilidade afeta todos os kernels do Google Compute Engine
anteriores ao ` gcg-3.3.8-201305291443 ` . Em resposta, o Compute Engine
suspendeu o uso de todos os kernels anteriores e recomenda que os usuários
atualizem suas instâncias e imagens para usarem o kernel ` gce-v20130603 ` do
Compute Engine. O ` gce-v20130603 ` contém o kernel ` gcg-3.3.8-201305291443 `
, que tem o patch para essa vulnerabilidade.

Para saber qual versão do kernel a instância está usando, faça o seguinte:

  1. Conecte-se à sua instância com SSH. 
  2. Execute ` uname -r ` . 

|  Média  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  Data da publicação: 07/06/2013

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

**Observação:** essa vulnerabilidade só é aplicável a kernels obsoletos e
removidos desde a versão v1 da API.

A vulnerabilidade de string de formato na função register_disk em `
block/genhd.c ` , no kernel do Linux até o 3.9.4, permite que os usuários
locais recebam privilégios usando o acesso root e gravando especificadores de
string de formato em ` /sys/module/md_mod/parameters/new_array ` para criar um
nome de dispositivo ` /dev/md ` elaborado.

####  Impacto no Compute Engine

Essa vulnerabilidade afeta todos os kernels do Compute Engine anteriores ao `
gcg-3.3.8-201305291443 ` . Em resposta, o Compute Engine suspendeu o uso de
todos os kernels anteriores e recomenda que os usuários atualizem suas
instâncias e imagens para usarem o kernel ` gce-v20130603 ` do Compute Engine.
O ` gce-v20130603 ` contém o kernel ` gcg-3.3.8-201305291443 ` , que tem o
patch para essa vulnerabilidade.

Para saber qual versão do kernel a instância está usando, faça o seguinte:

  1. Conecte-se à sua instância com SSH. 
  2. Execute ` uname -r ` . 

|  Média  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  Data da publicação: 14/05/2013

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

**Observação:** essa vulnerabilidade só é aplicável a kernels obsoletos e
removidos desde a versão v1 da API.

A função perf_swevent_init em ` kernel/events/core.c ` , no kernel do Linux
anterior ao 3.8.9, usa um tipo de dados ` integer ` incorreto, que permite aos
usuários locais receber privilégios por meio de uma chamada de sistema `
perf_event_open ` elaborada.

####  Impacto no Compute Engine

Essa vulnerabilidade afeta todos os kernels do Google Compute Engine
anteriores ao ` gcg-3.3.8-201305211623 ` . Em resposta, o Compute Engine
suspendeu o uso de todos os kernels anteriores e recomenda que os usuários
atualizem suas instâncias e imagens para usarem o kernel ` gce-v20130521 ` do
Compute Engine. O ` gce-v20130521 ` contém o kernel ` gcg-3.3.8-201305211623 `
, que tem o patch para essa vulnerabilidade.

Para saber qual versão do kernel a instância está usando, faça o seguinte:

  1. Conecte-se à sua instância com SSH. 
  2. Execute ` uname -r ` . 

|  Alta  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  Data da publicação: 18/02/2013

Descrição  |  Gravidade  |  Notas  
---|---|---  
  
####  Descrição

**Observação:** essa vulnerabilidade só é aplicável a kernels obsoletos e
removidos desde a versão v1 da API.

A disputa na funcionalidade ptrace no kernel do Linux anterior ao 3.7.5
permite aos usuários locais receber privilégios por meio de uma chamada de
sistema ` PTRACE_SETREGS ptrace ` em um aplicativo elaborado.

####  Impacto no Compute Engine

Essa vulnerabilidade afeta os kernels ` 2.6.x-gcg- _ <date> _ ` do Compute
Engine. Em resposta, o Compute Engine suspendeu o uso dos kernels 2.6.x e
recomenda que os usuários atualizem suas instâncias e imagens para usarem o
kernel ` gce-v20130225 ` do Compute Engine. O ` gce-v20130225 ` contém o
kernel ` 3.3.8-gcg-201302081521 ` , que tem o patch para essa vulnerabilidade.

Para saber qual versão do kernel a instância está usando, faça o seguinte:

  1. Conecte-se à sua instância com SSH. 
  2. Execute ` uname -r ` . 

|  Média  |  [ CVE-2013-0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

