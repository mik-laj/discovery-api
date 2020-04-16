#  Boletines de seguridad

Es posible que de vez en cuando publiquemos boletines de seguridad
relacionados con Compute Engine. En esta página se describen todos los
boletines de seguridad de Compute Engine.

[ Suscribirse a los boletines de seguridad de Compute Engine
![Suscribirse](https://cloud.google.com/images/feed-icon.png?hl=es)
](https://cloud.google.com/feeds/compute-engine-security-bulletins.xml?hl=es)

##  Fecha de publicación: 18/06/2019

**Última actualización: 25/06/2019 a las 6:30 PST (hora estándar del
Pacífico)**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

Netflix ha divulgado hace poco tres vulnerabilidades de TCP en los kernels de
Linux:

  * [ CVE‑2019‑11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE‑2019‑11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE‑2019‑11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

A estas CVE se las conoce conjuntamente como [ NFLX‑2019‑001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) .

####  Impacto en Compute Engine

La infraestructura que aloja Compute Engine está protegida frente a esta
vulnerabilidad.

Las máquinas virtuales de Compute Engine que ejecutan sistemas operativos
Linux sin parches y que envían o reciben tráfico de red no fiable son
vulnerables ante este tipo de ataques de denegación de servicio. Te
recomendamos que actualices estas instancias de máquina virtual en cuanto
estén disponibles los parches para sus sistemas operativos.

Se han aplicado parches contra esta vulnerabilidad en los balanceadores de
carga que cancelan las conexiones TCP. Las instancias de Compute Engine que
solo reciben tráfico que no es fiable mediante estos balanceadores de carga no
son vulnerables. Aquí se incluyen los balanceadores de carga HTTP, del proxy
SSL y del proxy TCP.

Los balanceadores de carga internos y de red no cancelan las conexiones TCP.
Las instancias de Compute Engine sin parches que reciben tráfico que no es
fiable mediante estos balanceadores de carga sí son vulnerables.

####  Imágenes con parche y recursos de proveedores

En esta página, incluiremos enlaces a documentos con información sobre los
parches de cada uno de los proveedores de sistemas operativos. Añadiremos esta
información cuando los parches estén disponibles, incluido el estado de todas
las CVE implicadas. Las versiones anteriores de estas imágenes públicas no
cuentan con estos parches y, por tanto, no sirven para reducir el riesgo de
sufrir ataques:

  * Proyecto ` debian-cloud ` : 
    * ` debian-9-stretch-v20190618 `
  * Proyecto ` centos-cloud ` : 
    * ` centos-6-v20190619 `
    * ` centos-7-v20190619 `
  * Proyecto ` cos-cloud ` : 
    * ` cos-dev-77-12293-0-0 `
    * ` cos-beta-76-12239-21-0 `
    * ` cos-stable-75-12105-77-0 `
    * ` cos-73-11647-217-0 `
    * ` cos-69-10895-277-0 `
  * Proyecto ` coreos-cloud ` : 
    * ` coreos-alpha-2163-2-1-v20190617 `
    * ` coreos-beta-2135-3-1-v20190617 `
    * ` coreos-stable-2079-6-0-v20190617 `
  * Proyecto ` rhel-cloud ` : 
    * ` rhel-6-v20190618 `
    * ` rhel-7-v20190618 `
    * ` rhel-8-v20190618 `
  * Proyecto ` rhel-sap-cloud ` : 
    * ` rhel-7-4-sap-v20190618 `
    * ` rhel-7-6-sap-v20190618 `
  * Proyecto ` suse-cloud ` : 
    * ` sles-12-sp4-v20190617 `
    * ` sles-15-v20190617 `
  * Proyecto ` suse-sap-cloud ` : 
    * ` sles-12-sp1-sap-v20190617 `
    * ` sles-12-sp2-sap-v20190617 `
    * ` sles-12-sp3-sap-v20190617 `
    * ` sles-12-sp4-sap-v20190617 `
    * ` sles-15-sap-v20190617 `
  * Proyecto ` ubuntu-cloud ` : 
    * ` ubuntu-1604-xenial-v20190617 `
    * ` ubuntu-1804-bionic-v20190617 `
    * ` ubuntu-1810-cosmic-v20190618 `
    * ` ubuntu-1904-disco-v20190619 `
    * ` ubuntu-minimal-1604-xenial-v20190618 `
    * ` ubuntu-minimal-1804-bionic-v20190617 `
    * ` ubuntu-minimal-1810-cosmic-v20190618 `
    * ` ubuntu-minimal-1904-disco-v20190618 `

|  Media  |

  * [ CVE‑2019‑11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE‑2019‑11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE‑2019‑11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

  
  
##  Fecha de publicación: 14/05/2019

**Última actualización: 20/05/2019 a las 17:00 PST (hora estándar del
Pacífico)**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

Intel ha divulgado las siguientes CVE:

  * [ CVE‑2018‑12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE‑2018‑12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE‑2018‑12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE‑2019‑11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

A estas CVE se las conoce conjuntamente como muestreo de datos de
microarquitectura (MDS). Estas vulnerabilidades podrían permitir que los datos
se expusieran por medio de la interacción de la ejecución especulativa y el
estado de microarquitectura.

####  Impacto en Compute Engine

**La infraestructura del host que ejecuta Compute Engine aísla las cargas de
trabajo del cliente entre sí. No es necesario que tomes ninguna medida, salvo
si ejecutas código no fiable en tus máquinas virtuales.**

Los clientes que ejecuten código no fiable en sus servicios de varios
propietarios dentro de máquinas virtuales de Compute Engine deben consultar la
mitigación recomendada por el proveedor de su SO invitado, que puede implicar
el uso de funciones de mitigación de microcódigo de Intel. Hemos desplegado el
acceso directo para invitados en la nueva funcionalidad de vaciado. A
continuación, incluimos un resumen de los pasos de mitigación para las
imágenes de invitado habituales.

####  Imágenes con parche y recursos de proveedores

En esta página, incluiremos enlaces a documentos con información sobre los
parches de cada uno de los proveedores de sistemas operativos. Añadiremos esta
información cuando los parches estén disponibles, incluido el estado de todas
las CVE implicadas. Usa estas imágenes para volver a crear las instancias de
máquina virtual. Las versiones anteriores de estas imágenes públicas no
cuentan con estos parches y, por tanto, no sirven para reducir el riesgo de
sufrir ataques:

  * Proyecto ` centos-cloud ` : [ CESA‑2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) , [ CESA‑2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html)
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * Proyecto ` coreos-cloud ` : [ mitigaciones de MDS para CoreOS Container Linux ](https://coreos.com/os/docs/latest/disabling-smt.html)
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * Proyecto ` cos-cloud `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * Proyecto ` debian-cloud ` : [ DSA‑4444 ](https://www.debian.org/security/2019/dsa-4444)
    * ` debian-9-stretch-v20190514 `
  * Proyecto ` rhel-cloud ` : [ artículo sobre el MDS de Red Hat ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * Proyecto ` rhel-sap-cloud ` : [ artículo sobre el MDS de Red Hat ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * Proyecto ` suse-cloud ` : [ artículo sobre el MDS de la base de conocimientos de SUSE ](https://www.suse.com/support/kb/doc/?id=7023736)
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * Proyecto ` suse-sap-cloud `
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * Proyecto ` ubuntu-os-cloud ` : [ entrada de la Wiki de Ubuntu sobre el MDS ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS)
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * Proyectos ` windows-cloud ` y ` windows-sql-cloud ` : [ Microsoft ADV190013 ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013)
    * Todas las imágenes públicas de Windows Server y SQL Server con el número de versión ` v20190514 ` . 
  * Proyecto ` gce-uefi-images `
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * Todas las imágenes públicas de Windows Server con el número de versión ` v20190514 ` . 

####  Container‑Optimized OS

Si Container‑Optimized OS (COS) es tu sistema operativo invitado y estás
ejecutando cargas de trabajo no fiables de varios propietarios en la máquina
virtual, te recomendamos que hagas lo siguiente:

  1. Inhabilita Hyper-Threading. Para ello, define ` nosmt ` en la línea de comandos del kernel.   

En las máquinas virtuales de COS, puedes modificar ` grub.cfg ` como te
indicamos abajo para definir la opción ` nosmt ` y, a continuación, reiniciar
el sistema:

    
        
    # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

Por comodidad, puedes ejecutar la siguiente secuencia de comandos para obtener
el mismo resultado que si ejecutaras los comandos anteriores. Te recomendamos
que integres esta secuencia en tus plantillas de cloud‑config, de secuencia de
comandos de inicio o de instancia para asegurarte de que las nuevas máquinas
virtuales usan este nuevo parámetro. Más abajo encontrarás un ejemplo de
cloud‑config que ejecuta esta secuencia.

**Advertencia:** Este comando reinicia inmediatamente la instancia cuando se
ejecuta por primera vez. El resto de veces que se ejecute en una instancia con
Hyper-Threading inhabilitado no tendrá ningún efecto.

    
        
    # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

Para incluir este fragmento en tu cloud‑config, añade lo siguiente:

    
        
    #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

Para confirmar si Hyper-Threading está inhabilitado en tu instancia, observa
el resultado de los archivos ` /sys/devices/system/cpu/smt/active ` y `
/sys/devices/system/cpu/smt/control ` . Si devuelven ` 0 ` en ` active ` y `
off ` en ` control ` , se habrá inhabilitado Hyper-Threading:

    
        
    cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**Nota:** Si tienes habilitado el arranque seguro UEFI en tu instancia,
deberás volver a crearla con este arranque inhabilitado, ejecutar el comando
de más arriba sin habilitar el arranque y, por último, habilitarlo en la nueva
instancia.

  2. Usa la nueva versión de la imagen de COS.   

Para protegerte totalmente frente a la vulnerabilidad, además de inhabilitar
Hyper-Threading como se describe anteriormente, debes [ volver a crear las
instancias ](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=es#publicimage) con las imágenes actualizadas que se enumeran más
arriba o con versiones nuevas de las imágenes de Container‑Optimized OS
(cuando estén disponibles).

|  Media  |

  * [ CVE‑2018‑12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE‑2018‑12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE‑2018‑12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE‑2018‑11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  Fecha de publicación: 14/08/2018

**Última actualización: 20/08/2018 a las 17:00 PST (hora estándar del
Pacífico)**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

[ Intel ha divulgado ](https://www.intel.com/content/www/us/en/architecture-
and-technology/l1tf.html) las siguientes CVE:

  * [ CVE‑2018‑3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (para [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE‑2018‑3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (para sistemas operativos y [ SMT ](https://en.wikipedia.org/wiki/Hyper-Threading) ) 
  * [ CVE‑2018‑3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (para virtualización) 

A estas CVE se las conoce conjuntamente como "L1 Terminal Fault (L1TF)".

Las vulnerabilidades de L1TF llevan a cabo la ejecución especulativa por medio
de ataques a la configuración de las estructuras de datos en el procesador.
"L1" hace referencia a la caché Level‑1 Data (L1D), un pequeño recurso del
núcleo que se utiliza para acelerar el acceso a la memoria.

Consulta esta [ entrada del blog de Google Cloud
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=es) para obtener más información sobre estas
vulnerabilidades y las medidas de mitigación de Compute Engine.

####  Impacto en Compute Engine

La infraestructura del host que ejecuta Compute Engine y aísla las cargas de
trabajo del cliente entre sí está protegida frente a ataques conocidos.

Aconsejamos a los clientes de Compute Engine que actualicen sus imágenes para
evitar que se pueda hacer un uso malintencionado de ellas de forma indirecta
en sus entornos de invitado. Esto es especialmente fundamental para los
clientes que ejecutan sus propios servicios de varios propietarios en máquinas
virtuales de Compute Engine.

Los clientes de Google Compute Engine disponen de las siguientes opciones para
actualizar los sistemas operativos invitados de sus instancias:

  * Usar imágenes públicas con parche para [ volver a crear las instancias de máquina virtual de las que dispongan ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=es#publicimage) . 
  * En las instancias que ya se han creado, instalar parches que proporcione el proveedor del sistema operativo y reiniciar las instancias con parche. 

####  Imágenes con parche y recursos de proveedores

En esta página, incluiremos enlaces a información sobre los parches de cada
uno de los proveedores de sistemas operativos. Añadiremos esta información
cuando los parches estén disponibles, incluido el estado correspondiente a los
CVE implicados. Usa estas imágenes para volver a crear las instancias de
máquina virtual. Las versiones anteriores de estas imágenes públicas no
cuentan con dichos parches y, por tanto, no sirven para reducir el riesgo de
sufrir ataques:

  * Proyecto ` centos-cloud ` : 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Proyecto ` coreos-cloud ` : 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Proyecto ` cos-cloud ` : 
    * ` cos-stable-66-10452-110-0 `
    * ` cos-stable-67-10575-66-0 `
    * ` cos-beta-68-10718-81-0 `
    * ` cos-dev-69-10895-23-0 `
  * Proyecto ` debian-cloud ` : 
    * ` debian-9-stretch-v20180820 `
  * Proyecto ` rhel-cloud ` : 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Proyecto ` rhel-sap-cloud ` : 
    * ` rhel-7-sap-apps-v20180814 `
    * ` rhel-7-sap-hana-v20180814 `
  * Proyecto ` suse-cloud ` : 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
    * ` sles-11-sp4-v20180816 `
  * Proyecto ` suse-sap-cloud ` : 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Proyecto ` ubuntu-os-cloud ` : 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `
  * Proyectos ` windows-cloud ` ` gce-uefi-images ` y ` windows-sql-cloud ` : 
    * Todas las [ imágenes públicas ](https://cloud.google.com/compute/docs/images?hl=es#os-compute-support) de Windows Server y SQL Server con el número de versión ` -v201800814 ` o uno posterior incluyen parches. 

|  Alta  |

  * [ CVE‑2018‑3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE‑2018‑3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE‑2018‑3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  Fecha de publicación: 06/08/2018

**Última actualización: 05/09/2018 a las 17:00 PST (hora estándar del
Pacífico)**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Actualización del 05/09/2018

El US‑CERT (el equipo de respuesta ante emergencias informáticas de Estados
Unidos) divulgó la [ CVE‑2018‑5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) el 14 de agosto del 2018. Al igual que la
[ CVE‑2018‑5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) , se trata de una vulnerabilidad de la red
a nivel del kernel que aumenta la efectividad de los ataques de denegación de
servicio contra sistemas vulnerables. La principal diferencia de la
CVE‑2018‑5391 es que puede aprovecharse a través de conexiones IP.
Actualizamos este boletín para que abarque ambas vulnerabilidades.

####  Descripción

La [ CVE‑2018‑5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") describe una
vulnerabilidad de la red a nivel del kernel que aumenta la efectividad de los
ataques de denegación de servicio (DoS) contra sistemas vulnerables a través
de conexiones TCP.

La [ CVE‑2018‑5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") describe una
vulnerabilidad de la red a nivel del kernel que aumenta la efectividad de los
ataques de denegación de servicio contra sistemas vulnerables a través de
conexiones IP.

####  Impacto en Compute Engine

Esta vulnerabilidad no afecta a la infraestructura del host que ejecuta las
máquinas virtuales de Compute Engine. La infraestructura de red que gestiona
el tráfico hacia y desde máquinas virtuales de Compute Engine se encuentra
protegida frente a esta vulnerabilidad. Las máquinas que solo envían o reciben
tráfico que no es fiable mediante [ HTTP y HTTPS
](https://cloud.google.com/load-balancing/docs/https/?hl=es) , [ SSL
](https://cloud.google.com/load-balancing/docs/ssl/?hl=es) o [ balanceadores
de carga TCP ](https://cloud.google.com/load-balancing/docs/tcp/?hl=es)
también están protegidas frente a esta vulnerabilidad.

Las máquinas virtuales de Compute Engine que ejecutan sistemas operativos sin
parches que envían y reciben tráfico no fiable (ya sea de forma directa o
mediante [ balanceadores de carga de red ](https://cloud.google.com/load-
balancing/docs/network/?hl=es) ) sí son vulnerables ante este tipo de ataques
de denegación de servicio.

Te recomendamos que actualices tus instancias de máquina virtual en cuanto
estén disponibles los parches para sus sistemas operativos.

Los clientes de Compute Engine disponen de las siguientes opciones para
actualizar los sistemas operativos invitados de sus instancias:

  * Usar imágenes públicas con parche para [ volver a crear las instancias de máquina virtual de las que dispongan ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=es#publicimage) . Puedes consultar la lista de imágenes públicas con parche un poco más abajo. 
  * En las instancias que ya se han creado, instalar parches que proporcione el proveedor del sistema operativo y reiniciar las instancias con parche. 

####  Imágenes con parche y recursos de proveedores

En esta página, incluiremos enlaces a información sobre los parches de cada
uno de los proveedores de sistemas operativos. Añadiremos esta información
cuando los parches estén disponibles.

  * Proyecto ` centos-cloud ` (solo CVE-2018-5390): 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Proyecto ` coreos-cloud ` (CVE-2018-5390 y CVE-2018-5391): 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Proyecto ` cos-cloud ` (CVE-2018-5390 y CVE-2018-5391): 
    * ` cos-stable-65-10323-98-0 `
    * ` cos-stable-66-10452-109-0 `
    * ` cos-stable-67-10575-65-0 `
    * ` cos-beta-68-10718-76-0 `
    * ` cos-dev-69-10895-16-0 `
  * Proyecto ` debian-cloud ` (CVE-2018-5390 y CVE-2018-5391): 
    * ` debian-9-stretch-v20180814 `
  * Proyecto ` rhel-cloud ` (solo CVE-2018-5390): 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Proyecto ` suse-cloud ` (CVE-2018-5390 y CVE-2018-5391): 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
  * Proyecto ` suse-sap-cloud ` (CVE-2018-5390 y CVE-2018-5391): 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Proyecto ` ubuntu-os-cloud ` (CVE-2018-5390 y CVE-2018-5391): 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `

|  Alta  |

  * [ CVE‑2018‑5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE‑2018‑5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  Fecha de publicación: 03/01/2018

**Última actualización: 21/05/2018 a las 15:00 PST (hora estándar del
Pacífico)**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Actualización del 21/05/2018

[ Intel divulgó ](https://www.intel.com/content/www/us/en/security-
center/advisory/intel-sa-00115.html) las vulnerabilidades [ CVE‑2018‑3640
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640) y [
CVE‑2018‑3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)
(variantes 3a y 4, respectivamente). Al igual que sucedía con las primeras
tres variantes de Spectre y Meltdown, la infraestructura que ejecuta las
instancias de máquina virtual de Compute Engine se encuentra protegida, y las
instancias de máquina virtual de los clientes están protegidas y aisladas
entre sí. Además, queremos que Compute Engine despliegue parches de
microcódigo de Intel en nuestra infraestructura. De esta forma, los clientes
que ejecuten con una sola instancia de máquina virtual cargas de trabajo que
no son fiables o que tienen varios propietarios podrán habilitar más medidas
de mitigación en su máquina virtual, siempre que los proveedores de sus
sistemas operativos les faciliten dichas medidas de mitigación. Desplegaremos
los parches de microcódigo en Computer Engine cuando Intel los certifique y
hayamos comprobado que cumplen los requisitos de nuestro entorno de
producción. Cuando estos parches estén disponibles, publicaremos más novedades
al respecto y detalles sobre las fechas en esta página.

####  Descripción

Estas CVE son variantes de una nueva clase de ataque que aprovecha la
tecnología de ejecución especulativa que utilizan muchos procesadores. Este
tipo de ataque permite el acceso sin autorización de solo lectura a los datos
en memoria cuando se dan determinadas circunstancias.

Compute Engine se sirvió de la tecnología de migración activa de las máquinas
virtuales para llevar a cabo actualizaciones en los sistemas host y los
hipervisores. Dichas actualizaciones no afectaron a la experiencia de los
usuarios ni provocaron ventanas de mantenimiento ni la necesidad de realizar
reinicios masivos. No obstante, deben aplicarse parches en todos los sistemas
operativos invitados y versiones para protegerlos frente a esta nueva clase de
ataque, independientemente del sistema en que se ejecuten.

Consulta esta [ entrada del blog de Project Zero
](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-
with-side.html) para obtener más información sobre los detalles técnicos de
este método de ataque. Consulta esta [ entrada del blog sobre seguridad de
Google ](https://security.googleblog.com/2018/01/todays-cpu-vulnerability-
what-you-need.html) para obtener más información sobre las medidas de
mitigación de Google, incluida la información específica de cada producto.

####  Impacto en Compute Engine

La infraestructura que ejecuta Compute Engine y aísla las instancias de
máquina virtual del cliente entre sí está protegida frente a ataques
conocidos. Nuestras medidas de mitigación evitan que las aplicaciones que se
ejecutan en instancias de máquina virtual puedan acceder sin autorización a
nuestros sistemas host. Además, estas medidas evitan el acceso sin
autorización entre las instancias de máquina virtual que se ejecutan en un
mismo sistema host

Para evitar que se produzcan accesos sin autorización en tus instancias de
máquina virtual, debes actualizar sus sistemas operativos invitados mediante
alguna de las siguientes opciones:

  * Usar imágenes públicas con parche para [ volver a crear las instancias de máquina virtual de las que dispongas ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=es#publicimage) . A continuación, puedes consultar la lista de imágenes públicas con parche. 
  * En las instancias que ya hayas creado, instala los parches que proporcione el proveedor del sistema operativo correspondientes a tu distribución y reinicia las instancias con parche. Más abajo puedes consultar la información sobre los parches de cada uno de los proveedores de sistemas operativos. 

####  Imágenes con parche y recursos de proveedores

**Nota:** Es posible que las imágenes con parche no incluyan soluciones para
todas las CVE que aparecen en este boletín de seguridad. Además, las distintas
imágenes podrían incluir métodos diferentes para evitar este tipo de ataques.
Ponte en contacto con el proveedor de tu sistema operativo para obtener más
información sobre las CVE a las que hacen frente sus parches y acerca de las
medidas de prevención que utilizan.

  * Proyecto ` cos-cloud ` : incluye parches que evitan ataques de las variantes 2 ( [ CVE‑2017‑5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ) y 3 ( [ CVE‑2017‑5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ). Google usó [ Retpoline ](https://support.google.com/faqs/answer/7625886?hl=es) para mitigar los ataques de la variante 2. 
    * ` cos-stable-63-10032-71-0 ` o la familia de imágenes ` cos-stable `
  * Proyecto ` centos-cloud ` : [ información sobre los parches de CentOS ](https://lwn.net/Alerts/CentOS/)
    * ` centos-7-v20180104 ` o la familia de imágenes ` centos-7 `
    * ` centos-6-v20180104 ` o la familia de imágenes ` centos-6 `
  * Proyecto ` coreos-cloud ` : [ información sobre los parques de CoreOS ](https://coreos.com/blog/container-linux-meltdown-patch)
    * ` coreos-stable-1576-5-0-v20180105 ` o la familia de imágenes ` coreos-stable `
    * ` coreos-beta-1632-1-0-v20180105 ` o la familia de imágenes ` coreos-beta `
    * ` coreos-alpha-1649-0-0-v20180105 ` o la familia de imágenes ` coreos-alpha `
  * Proyecto ` debian-cloud ` : [ información sobre los parches de Debian ](https://www.debian.org/security/#DSAS)
    * ` debian-9-stretch-v20180105 ` o la familia de imágenes ` debian-9 `
    * ` debian-8-jessie-v20180109 ` o la familia de imágenes ` debian-8 `
  * Proyecto ` rhel-cloud ` : [ información sobre los parches de RHEL ](https://access.redhat.com/security/vulnerabilities/speculativeexecution)
    * ` rhel-7-v20180104 ` o la familia de imágenes ` rhel-7 `
    * ` rhel-6-v20180104 ` o la familia de imágenes ` rhel-6 `
  * Proyecto ` suse-cloud ` : [ información sobre los parches de SUSE ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-v20180104 ` o la familia de imágenes ` sles-12 `
    * ` sles-11-sp4-v20180104 ` o la familia de imágenes ` sles-11 `
  * Proyecto ` suse-sap-cloud ` : [ información sobre los parches de SUSE ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-sap-v20180104 ` o la familia de imágenes ` sles-12-sp3-sap `
    * ` sles-12-sp2-sap-v20180104 ` o la familia de imágenes ` sles-12-sp2-sap `
  * Proyecto ` ubuntu-os-cloud ` : [ información sobre los parches de Ubuntu ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/)
    * ` ubuntu-1710-artful-v20180109 ` o la familia de imágenes ` ubuntu-1710 `
    * ` ubuntu-1604-xenial-v20180109 ` o la familia de imágenes ` ubuntu-1604-lts `
    * ` ubuntu-1404-trusty-v20180110 ` o la familia de imágenes ` ubuntu-1404-lts `
  * Proyectos ` windows-cloud ` y ` windows-sql-cloud ` : 
    * Todas las [ imágenes públicas ](https://cloud.google.com/compute/docs/images?hl=es#os-compute-support) de Windows Server y SQL Server con el número de versión ` -v20180109 ` o uno posterior incluyen parches. No obstante, a la hora de habilitar y verificar las medidas de mitigación en tus instancias (tanto las ya creadas como las creadas recientemente), debes seguir las acciones recomendadas que indica Microsoft en [ su boletín de asistencia de Windows Server ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) . 

Usa estas imágenes para [ volver a crear las instancias de máquina virtual
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=es#publicimage) . Las versiones anteriores de estas imágenes
públicas no cuentan con dichos parches y, por tanto, no sirven para reducir el
riesgo de sufrir ataques.

####  Parches de los proveedores de hardware

NVIDIA proporciona controladores con parche para mitigar posibles ataques
contra sistemas en los que se haya instalado software de controladores de
NVIDIA®. Si quieres obtener más información sobre qué versión de los
controladores incluye el parche, consulta el boletín de seguridad de NVIDIA: [
NVIDIA GPU Display Driver Security Updates
](http://nvidia.custhelp.com/app/answers/detail/a_id/4611)

####  Historial de revisiones:

  * 21/05/2018, 14:00 (PST): se añadió información sobre las 2 nuevas variantes que se divulgaron el 21 de mayo del 2018. 
  * 10/01/2018, 15:00 (PST): se añadió información sobre las imágenes públicas con parche de Windows Server y SQL Server. 
  * 10/01/2018, 10:15 (PST): se añadieron varias imágenes de Ubuntu a la lista de imágenes públicas con parche. 
  * 10/01/2018, 09:50 (PST): se añadió información instructiva sobre los parches de proveedores de hardware. 
  * 03/01/2018-09/01/2018: se añadieron varias revisiones a la lista de imágenes públicas con parche. 

|  Alta  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  Fecha de publicación: 02/10/2017

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

[ Dnsmasq ](http://www.thekelleys.org.uk/dnsmasq/doc.html) proporciona
funciones de servicio de DNS, DHCP, anuncios de router y arranques de red.
Normalmente, este software se instala en sistemas tan variados como las
distribuciones de escritorio de Linux (por ejemplo, Ubuntu), los routers
domésticos y los dispositivos del Internet de las cosas. El uso de Dnsmasq
está muy extendido en el Internet público e, internamente, en las redes
privadas.

En el transcurso de nuestras evaluaciones periódicas internas de seguridad,
detectamos siete errores diferentes. Tras determinar su gravedad, nos pusimos
manos a la obra para estudiar su impacto y las posibilidades de aprovecharse
de estos errores. A continuación, desarrollamos pruebas de concepto internas
para cada uno de ellos. También colaboramos con el encargado del mantenimiento
de Dnsmasq, Simon Kelly, para producir los parches adecuados y mitigar los
problemas.

Durante la revisión, el equipo encontró tres posibles ejecuciones remotas del
código, una filtración de información y tres vulnerabilidades de denegación de
servicio que afectaban a la versión más reciente en el servidor Git del
proyecto el 5 de septiembre del 2017.

Estos parches se suben y se confirman en el [ repositorio Git del proyecto
](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) .

####  Impacto en Compute Engine

De forma predeterminada, Dnsmasq solo se instala en imágenes que usen [
NetworkManager ](https://wikipedia.org/wiki/NetworkManager) (inactivo por
defecto). Las siguientes imágenes públicas de Compute Engine tienen Dnsmasq
instalado:

  * Ubuntu 16.04, 16.10 y 17.04 
  * CentOS 7 
  * RHEL 7 

Sin embargo, es posible que otras imágenes tengan Dnsmasq instalado como una
dependencia de otros paquetes. Te recomendamos que actualices tus instancias
de Debian, Ubuntu, CentOS, Red Hat Enterprise Linux (RHEL), SUSE Linux
Enterprise Server (SLES) y OpenSUSE para emplear la imagen más reciente de los
sistemas operativos. Esta vulnerabilidad no afecta a CoreOS, Container-
Optimized OS ni tampoco a las imágenes de Windows.

Para actualizar las instancias que ejecutan Debian y Ubuntu, ejecuta los
siguientes comandos en tu instancia:

    
    
    
    sudo apt-get -y update
    
    
    
    sudo apt-get -y dist-upgrade

En las instancias de RHEL y CentOS, ejecuta:

    
    
    
    sudo yum -y upgrade

En las imágenes de SLES y OpenSUSE, ejecuta:

    
    
    
    sudo zypper up

Como alternativa a ejecutar los comandos de la actualización manual, puedes [
volver a crear instancias de máquina virtual con las familias de imágenes
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=es#publicimage) del SO correspondiente.

|  Alta  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  Fecha de publicación: 26/10/2016

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

CVE-2016-5195 es una condición de carrera de la forma en que el subsistema de
memoria del kernel de Linux ha gestionado el incumplimiento de la situación de
copia en escritura de las asignaciones privadas de solo lectura en el acceso
de escritura.

Los usuarios locales sin privilegios podrían aprovechar este error para
obtener acceso de escritura a las asignaciones de memoria que de otra forma
serían de solo lectura y, por tanto, aumentarían sus privilegios en el
sistema.

Para obtener más información, consulta las [ preguntas frecuentes sobre Dirty
COW
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)
(en inglés).

####  Impacto en Compute Engine

Todas las distribuciones y versiones de Linux en Compute Engine se ven
afectadas. En la mayoría de las instancias se descargará e instalará
automáticamente un kernel más reciente. Sin embargo, tienes que reiniciar el
sistema en ejecución para aplicarle un parche.

Las instancias que se hayan creado por primera vez o que se hayan vuelto a
crear según las siguientes imágenes de Compute Engine ya tienen instalados los
kernels con los parches.

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
  
##  Fecha de publicación: 16/02/2016

**Última actualización: 22/02/2016**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

CVE-2015-7547 es una vulnerabilidad en la que la herramienta de resolución del
cliente de DNS de glibc vuelve al software vulnerable frente a un
desbordamiento del búfer basado en la pila cuando se utiliza la función de
biblioteca ` getaddrinfo() ` . Un atacante puede sacar provecho del software
que está usando la función para explotar esta vulnerabilidad con nombres de
dominio o servidores DNS controlados por el atacante, o bien mediante un
ataque de interceptación.

Para obtener más información, consulta el [ blog de seguridad online de Google
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) o la base de datos de [ vulnerabilidades y
exposiciones comunes (CVE) ](http://www.cve.mitre.org/cgi-
bin/cvename.cgi?name=2015-7547) .

####  Impacto en Compute Engine

**Actualización (22/02/2016):**

Ahora puedes volver a crear tus instancias con las siguientes imágenes de
CoreOS, SLES y OpenSUSE:

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**Actualización (17/02/2016):**

Ahora puedes actualizar las instancias de Ubuntu 12.04 LTS, Ubuntu 14.04 LTS y
Ubuntu 15.10, si ejecutas los siguientes comandos:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Como alternativa a ejecutar los comandos de actualización manual, ahora puedes
volver a crear tus instancias con las siguientes imágenes nuevas:

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

No conocemos ningún método que pueda explotar esta vulnerabilidad a través de
las herramientas de resolución de DNS de Compute Engine con la configuración
predeterminada de glibc. No obstante, deberías aplicar parches a las
instancias de tu máquina virtual lo antes posible porque, al igual que ocurre
con cualquier vulnerabilidad nueva, se pueden descubrir métodos de explotación
con el paso del tiempo. Si has habilitado los EDNS0 (inhabilitados de forma
predeterminada), debes inhabilitarlos hasta que se hayan aplicado los parches
a las instancias.

**Boletín original:**

Tu distribución de Linux podría ser vulnerable. Para eliminar esta
vulnerabilidad, los clientes de Compute Engine que ejecuten un SO Linux tienen
que actualizar las imágenes de SO de sus instancias.

Para actualizar las instancias que ejecutan Debian, ejecuta los siguientes
comandos en tu instancia:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

También te recomendamos instalar [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) para tus instancias de Debian.

En las instancias de RHEL, ejecuta:

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

Continuaremos actualizando este boletín a medida que otros encargados del
mantenimiento del sistema operativo publiquen parches para esta vulnerabilidad
y conforme Compute Engine publique imágenes de sistema operativo actualizadas.

|  Alta  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  Fecha de publicación: 19/03/2015

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

CVE-2015-1427 es una vulnerabilidad en la que el motor de secuencias de
comandos Groovy en [ Elasticsearch
](https://www.elastic.co/products/elasticsearch) previo a la versión 1.3.8 y a
cualquiera de las versiones 1.4.x anteriores a la 1.4.3 permite que los
atacantes remotos eludan el mecanismo de protección de la zona de pruebas y
ejecuten comandos shell arbitrarios.

Para obtener más información, consulta la [ base de datos de vulnerabilidades
nacional (NVD)
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) o la de [
vulnerabilidades y exposiciones comunes (CVE) ](http://www.cve.mitre.org/cgi-
bin/cvename.cgi?name=2015-1427) .

####  Impacto en Compute Engine

Si ejecutas Elasticsearch en tus instancias de Compute Engine, debes
actualizarlo a la versión 1.4.3 (o una posterior). Si ya lo has hecho, esta
vulnerabilidad no te afectará.

Si no has actualizado a Elasticsearch 1.4.3 (o a una versión posterior),
puedes [ realizar una actualización gradual
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) .

Si has desplegado Elasticsearch con la opción de [ clic para desplegar
](https://cloud.google.com/solutions/elasticsearch/click-to-deploy?hl=es) en
la [ consola de Google Cloud Platform
](https://console.cloud.google.com/?hl=es) , puedes [ eliminar el despliegue
](https://console.cloud.google.com/projectselector/deployments?hl=es) para
retirar las instancias que ejecutan Elasticsearch.

El equipo de Google Cloud Platform está trabajando en una corrección para
desplegar una versión actualizada de Elasticsearch. Sin embargo, esta
corrección aún no está disponible para la función de clic para desplegar en la
[ consola de GCP ](https://console.cloud.google.com/?hl=es) .

|  Alta  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  Fecha de publicación: 29/01/2015

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

[ CVE-2015-0235 (Ghost)
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) es una
vulnerabilidad de la biblioteca glibc.

Los clientes de App Engine, Cloud Storage, BigQuery y Cloud SQL no necesitan
realizar ninguna acción. Los servidores de Google se han actualizado y están
protegidos contra esta vulnerabilidad.

Es posible que los clientes de Compute Engine tengan que actualizar sus
imágenes de sistema operativo.

####  Impacto en Compute Engine

Tu distribución de Linux puede ser vulnerable. Los clientes de Compute Engine
tendrán que actualizar las imágenes del sistema operativo de sus instancias
para eliminar esta vulnerabilidad si ejecutan Debian 7, los backports de
Debian 7, Ubuntu 12.04 LTS, RHEL, CentOS o SLES 11 SP3.

Esta vulnerabilidad no afecta a Ubuntu 14.04 LTS, Ubuntu 14.10 ni SLES 12.

Te recomendamos que actualices tus distribuciones de Linux. Para actualizar
las instancias que ejecutan Debian 7, los backports de Debian 7 o Ubuntu 12.04
LTS, ejecuta los siguientes comandos en tu instancia:

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

En las instancias de RHEL o CentOS, ejecuta:

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

En las instancias de SLES 11 SP3, ejecuta:

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

Como alternativa a ejecutar los comandos de actualización manual de arriba,
ahora los usuarios pueden volver a crear sus instancias con las siguientes
imágenes nuevas:

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  Impacto en las máquinas virtuales gestionadas por Google

Los usuarios de máquinas virtuales gestionadas que utilizan ` gcloud preview
app deploy ` deben actualizar sus contenedores base de Docker con ` gcloud
preview app setup-managed-vms ` y volver a desplegar cada una de sus
aplicaciones en ejecución con ` gcloud preview app deploy ` . Los usuarios que
realizan despliegues con ` appcfg ` no tienen que hacer nada, ya que la
actualización se hará automáticamente.

|  Alta  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  Fecha de publicación: 15/10/2014

**Última actualización: 17/10/2014**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

CVE-2014-3566 (también conocido como POODLE) es una vulnerabilidad del diseño
de la versión 3.0 de SSL. Esta vulnerabilidad permite que un atacante de red
calcule el texto sin formato de las conexiones seguras. Para obtener más
información, consulta la [ entrada de nuestro blog
](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) sobre la vulnerabilidad (en inglés).

Los clientes de App Engine, Cloud Storage, BigQuery y Cloud SQL no necesitan
realizar ninguna acción. Los servidores de Google se han actualizado y están
protegidos contra esta vulnerabilidad. Los clientes de Compute Engine deben
actualizar sus imágenes de sistema operativo.

####  Impacto en Compute Engine

**Actualización (17/10/2014):**

Puedes ser vulnerable si usas SSLv3. Los clientes de Compute Engine tendrán
que actualizar las imágenes de sistema operativo de sus instancias para
eliminar esta vulnerabilidad.

Te recomendamos que actualices tus distribuciones de Linux. Para actualizar
las instancias que ejecutan Debian, ejecuta los siguientes comandos en tu
instancia:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

En las instancias de CentOS, ejecuta:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

Como alternativa a ejecutar los comandos de actualización manual de arriba,
ahora los usuarios pueden volver a crear sus instancias con las siguientes
imágenes nuevas:

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

Actualizaremos el boletín con las imágenes de RHEL y SLES cuando dispongamos
de ellas. Mientras tanto, los usuarios de RHEL pueden consultar este [
artículo de Red Hat ](https://access.redhat.com/articles/1232123) directamente
para obtener más información.

**Boletín original:**

Los clientes de Compute Engine tendrán que actualizar las imágenes del sistema
operativo de sus instancias para eliminar esta vulnerabilidad. Actualizaremos
este boletín de seguridad con más instrucciones cuando dispongamos de las
nuevas imágenes del sistema operativo.

|  Media  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  Fecha de publicación: 24/09/2014

**Última actualización: 29/09/2014**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

Hay un error en Bash (CVE-2014-6271) que permite la ejecución remota de código
basada en análisis de cualquier variable de entorno que un atacante controle.
El vector de explotación más probable es a través de peticiones HTTP
maliciosas que se realicen a secuencias de comandos de CGI expuestas en un
servidor web. Para obtener más información, consulta la [ descripción del
error ](http://seclists.org/oss-sec/2014/q3/650) (en inglés).

Los errores de Bash se han mitigado en los productos de GCP, excepto en las
imágenes del sistema operativo invitado de Compute Engine que tengan una fecha
anterior al 26/09/2014. Consulta los pasos detallados a continuación para
mitigar los errores de tus imágenes de Compute Engine.

####  Impacto en Compute Engine

Este error puede afectar a casi todos los sitios web que usen secuencias de
comandos de CGI. Además, es probable que afecte a los sitios web que dependan
de PHP, Perl, Python, SSI, Java, C++ y de servlets similares que en algún
momento invocarán comandos shell mediante llamadas como ` popen ` , ` system `
, ` shell_exec ` o API similares. También puede afectar a los sistemas que
intenten permitir el acceso de inicio de sesión controlado a usuarios
restringidos a través de mecanismos como la limitación del comando SSH o el
shell restringido de Bash.

**Actualización (29/09/2014):**

En lugar de ejecutar los comandos de actualización manual que aparecen a
continuación, ahora los usuarios también pueden volver a crear sus instancias
con imágenes que mitigan otras vulnerabilidades relacionadas con el error de
seguridad de Bash, entre las que se incluyen las siguientes: [ CVE‑2014‑7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE‑2014‑6277 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277)
, [ CVE‑2014‑6278
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278) , [
CVE‑2014‑7186 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186)
y [ CVE‑2014‑7187
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187) . Usa las
siguientes imágenes nuevas para volver a crear tus instancias:

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**Actualización (25/09/2014):**

Ahora los usuarios pueden volver a crear sus instancias en lugar de realizar
una actualización manual. Para hacerlo, usa las siguientes imágenes nuevas que
contienen correcciones del error de seguridad:

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

Para las imágenes de RHEL y SUSE, también puedes realizar actualizaciones
manualmente si ejecutas los siguientes comandos en tus instancias:

    
    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**Boletín original:**

Te recomendamos que actualices tus distribuciones de Linux. Para actualizar
las instancias que ejecutan Debian, ejecuta los siguientes comandos en tu
instancia:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

En las instancias de CentOS, ejecuta:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade

Para obtener más información, revisa el anuncio de la distribución de Linux
correspondiente:

  * Parches originales: [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) (consulta la última entrada en *-patches para saber cuál es la versión apropiada) 
  * Debian: [ [SECURITY] [DSA 3032-1] bash security update ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
  * RHEL: 
    * [ RHSA-2014:1293-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00048.html)
    * [ RHSA-2014:1294-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00049.html)
  * CentOS 5: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020582.html)
  * CentOS 6: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020585.html)
  * CentOS 7: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020583.html)

|  Alta  |  [ CVE‑2014‑7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE‑2014‑6271 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271)
, [ CVE‑2014‑6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) , [
CVE‑2014‑6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
[ CVE‑2014‑7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) y [
CVE‑2014‑7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  Fecha de publicación: 25/07/2014

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

[ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/) es
vulnerable a la inyección de comandos de sistema operativo, que permite la
modificación y la divulgación de datos sin autorización. Los atacantes pueden
enviar eventos elaborados a cualquiera de las fuentes de datos de Logstash, lo
que les permite ejecutar comandos con los permisos del proceso de Logstash.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todas las instancias de Compute Engine que
ejecutan versiones de Elasticsearch Logstash anteriores a la 1.4.2 con los
complementos de salida zabbix o nagios_nsca habilitados. Para evitar un
ataque, puedes realizar alguna de las siguientes acciones:

  * Actualizar a Logstash 1.4.2. 
  * Aplicar el parche para las versiones 1.3.x. 
  * Inhabilitar las salidas ` zabbix ` y ` nagios_nsca ` . 

Obtén más información en el [ blog de Logstash
](http://www.elasticsearch.org/blog/logstash-1-4-2/) (en inglés).

Elasticsearch también recomienda [ usar un cortafuegos
](http://www.elasticsearch.org/blog/scripting-security/) para evitar el acceso
remoto de direcciones IP que no sean de confianza.

|  Alta  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  Fecha de publicación: 18/06/2014

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

Nos gustaría dedicar un momento a responder a las posibles dudas de los
clientes sobre la seguridad de los contenedores Docker cuando se ejecutan en
GCP. Entre los clientes se incluyen los que usan nuestras extensiones de
Google App Engine compatibles con los contenedores Docker, las máquinas
virtuales optimizadas para contenedores o el programador de Kubernetes de
código abierto.

Docker ha respondido al problema de manera fantástica. Puedes ver la respuesta
en su [ blog ](http://blog.docker.com/2014/06/docker-container-breakout-proof-
of-concept-exploit/) (en inglés). Como se indica en esa publicación, el
problema descubierto solo se aplica a Docker 0.11, una versión anterior de
preproducción.

Mientras los usuarios piensan en la seguridad de los contenedores, nos
gustaría señalar que en Google Cloud Platform las soluciones basadas en
contenedores de aplicaciones Linux (en concreto, contenedores Docker) se
ejecutan en máquinas virtuales completas (Compute Engine). Aunque apoyamos los
esfuerzos que ha hecho la comunidad de Docker para proteger la pila de
contenedores de aplicaciones Linux, somos conscientes de que la tecnología es
nueva y que el área expuesta es grande. Creemos que, por ahora, los
hipervisores completos (máquinas virtuales) ofrecen un área expuesta más
compacta y defendible. Desde el principio, las máquinas virtuales se diseñaron
para aislar las cargas de trabajo maliciosas y reducir la probabilidad de que
se produzca un error de código y su impacto consiguiente.

Nuestros clientes pueden tener la tranquilidad de que hay un límite de
hipervisor completo entre ellos y cualquier código de terceros que pueda ser
malicioso. Si llegamos a un punto en el que consideramos que la pila de
contenedores de aplicaciones Linux es lo suficientemente robusta como para
admitir cargas de trabajo multicliente, se lo comunicaremos a la comunidad.
Por ahora, el contenedor de aplicaciones Linux no reemplaza a la máquina
virtual, si no que es una manera de sacarle más partido.

|  Baja  |  [ Entrada de blog de Docker
](http://blog.docker.com/2014/06/docker-container-breakout-proof-of-concept-
exploit/)  
  
##  Fecha de publicación: 05/06/2014

**Última actualización: 09/06/2014**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

OpenSSL tiene un error que provoca que los mensajes ` ChangeCipherSpec ` no se
enlacen correctamente con la máquina de estado de handshake. Por este motivo,
se insertan en el handshake de forma anticipada. Los atacantes que usen un
handshake bien elaborado pueden forzar el uso de material con claves débiles
en los clientes y los servidores SSL o TLS de OpenSSL. Un ataque de
interceptación puede explotar esta situación si los atacantes descifran y
modifican el tráfico del cliente y del servidor atacados.

Este problema se identifica como [ CVE-2014-0224
](https://www.openssl.org/news/secadv/20140605.txt) . El equipo de OpenSSL ha
corregido el error y ha avisado a su comunidad de que debe actualizar OpenSSL.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todas las instancias de Compute Engine que usan
OpenSSL, incluidas Debian, CentOS, RHEL y SLES. Para actualizar tus
instancias, puedes volver a crearlas con imágenes nuevas o actualizar
manualmente los paquetes en las instancias.

**Actualización (09/06/2014):** Para actualizar las instancias que ejecutan
SLES con imágenes nuevas, vuelve a crear tus instancias con las siguientes
versiones de imagen (o con versiones posteriores):

  * ` sles-11-sp3-v20140609 `

**Publicación original:**

Para actualizar las instancias de Debian y CentOS con imágenes nuevas, vuelve
a crear tus instancias con cualquiera de las siguientes versiones de imagen (o
con versiones posteriores):

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

Para actualizar OpenSSL en tus instancias de forma manual, ejecuta los
siguientes comandos para actualizar los paquetes apropiados. En el caso de las
instancias que ejecutan CentOS y RHEL, puedes actualizar OpenSSL si ejecutas
estos comandos en la instancia:

    
    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

Para actualizar OpenSSL en las instancias que ejecutan Debian, ejecuta los
siguientes comandos en tu instancia:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

En el caso de las instancias que ejecutan SLES, puedes comprobar si OpenSSL
está actualizado ejecutando estos comandos en la instancia:

    
    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  Media  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  Fecha de publicación: 08/04/2014

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

Las implementaciones de (1) TLS y (2) DTLS en OpenSSL 1.0.1 anteriores a la
versión 1.0.1g no gestionan correctamente los paquetes de Heartbeat Extension.
Esto permite que los atacantes remotos obtengan información sensible de la
memoria de procesos a través de paquetes elaborados que activan una
sobrelectura del búfer (como ha demostrado la lectura de las claves privadas)
relacionada con ` d1_both.c ` y ` t1_lib.c ` , lo que se conoce como error
Heartbleed.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todas las instancias de Debian, RHEL y CentOS de
Compute Engine que no tengan la versión más actualizada de OpenSSL. Para
actualizar tus instancias, vuelve a crearlas con nuevas imágenes o actualiza
manualmente los paquetes en las instancias.

Para actualizar tus instancias con imágenes nuevas, vuelve a crear las
instancias con cualquiera de las siguientes versiones de imagen (o con
versiones posteriores):

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

Para actualizar OpenSSL en tus instancias de forma manual, ejecuta los
siguientes comandos para actualizar los paquetes apropiados. Si quieres
comprobar que OpenSSL está actualizado en las instancias que ejecutan CentOS y
RHEL, ejecuta estos comandos en la instancia:

    
    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

Para actualizar OpenSSL en las instancias que ejecutan Debian, ejecuta los
siguientes comandos en tu instancia:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

Las instancias que ejecutan SUSE Linux no se ven afectadas.

**Actualización 14/04/2014:** Debido a recientes investigaciones sobre la
extracción de claves aprovechando el error Heartbleed, se recomienda a los
clientes de Compute Engine que creen claves nuevas para los servicios SSL
afectados.

|  Media  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  Fecha de publicación: 07/06/2013

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

**Nota:** Esta vulnerabilidad solo se aplica a los kernels, que ya no están
disponibles y se retiraron a partir de la versión 1 de la API.

La vulnerabilidad de cadenas de formato en la función ` b43_request_firmware `
de ` drivers/net/wireless/b43/main.c ` en el controlador inalámbrico Broadcom
B43 del kernel de Linux hasta la versión 3.9.4 permite que los usuarios
locales obtengan privilegios si aprovechan el acceso raíz e incluyen
especificadores de cadenas de formato en un parámetro modprobe ` fwpostfix ` ,
lo que da lugar a la construcción incorrecta de un mensaje de error.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todos los kernels de Compute Engine anteriores al
` gcg-3.3.8-201305291443 ` . Para solucionar este problema, Compute Engine ha
desactivado todos los kernels anteriores y recomienda que los usuarios
actualicen sus instancias e imágenes para usar el kernel de Compute Engine `
gce-v20130603 ` . El ` gce-v20130603 ` contiene el kernel `
gcg-3.3.8-201305291443 ` , que cuenta con el parche correspondiente a esta
vulnerabilidad.

Para saber qué versión de kernel usa tu instancia, sigue estos pasos:

  1. Aplica SSH en tu instancia. 
  2. Ejecuta ` uname -r ` . 

|  Media  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  Fecha de publicación: 07/06/2013

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

**Nota:** Esta vulnerabilidad solo se aplica a los kernels, que ya no están
disponibles y se retiraron desde la versión 1 de la API.

La vulnerabilidad de cadenas de formato en la función register_disk de `
block/genhd.c ` en el kernel de Linux hasta la versión 3.9.4 permite que los
usuarios locales obtengan privilegios si aprovechan el acceso raíz e
introducen especificadores de cadenas de formato en `
/sys/module/md_mod/parameters/new_array ` para crear un nombre de dispositivo
elaborado de ` /dev/md ` .

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todos los kernels de Compute Engine anteriores al
` gcg-3.3.8-201305291443 ` . Para solucionar este problema, Compute Engine ha
desactivado todos los kernels anteriores y recomienda que los usuarios
actualicen sus instancias e imágenes para usar el kernel de Compute Engine `
gce-v20130603 ` . El ` gce-v20130603 ` contiene el kernel `
gcg-3.3.8-201305291443 ` , que cuenta con el parche correspondiente a esta
vulnerabilidad.

Para saber qué versión de kernel usa tu instancia, sigue estos pasos:

  1. Aplica SSH en tu instancia. 
  2. Ejecuta ` uname -r ` . 

|  Media  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  Fecha de publicación: 14/05/2013

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

**Nota:** Esta vulnerabilidad solo se aplica a los kernels, que ya no están
disponibles y se retiraron a partir de la versión 1 de la API.

La función perf_swevent_init de ` kernel/events/core.c ` en el kernel de Linux
anterior a la versión 3.8.9 utiliza un tipo de datos ` integer ` incorrecto,
lo que permite que los usuarios locales obtengan privilegios mediante una
llamada de sistema ` perf_event_open ` elaborada.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todos los kernels de Compute Engine anteriores al
` gcg-3.3.8-201305211623 ` . Para solucionar este problema, Compute Engine ha
desactivado todos los kernels anteriores y recomienda que los usuarios
actualicen sus instancias e imágenes para usar el kernel de Compute Engine `
gce-v20130521 ` . El ` gce-v20130521 ` contiene el kernel `
gcg-3.3.8-201305211623 ` , que cuenta con el parche correspondiente a esta
vulnerabilidad.

Para saber qué versión de kernel usa tu instancia, sigue estos pasos:

  1. Aplica SSH en tu instancia. 
  2. Ejecuta ` uname -r ` . 

|  Alta  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  Fecha de publicación: 18/02/2013

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

**Nota:** Esta vulnerabilidad solo se aplica a los kernels, que ya no están
disponibles y se retiraron a partir de la versión 1 de la API.

La condición de carrera de la función ptrace en el kernel de Linux anterior a
la versión 3.7.5 permite que los usuarios locales obtengan privilegios
mediante una llamada de sistema ` PTRACE_SETREGS ptrace ` en una aplicación
elaborada.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a los kernels ` 2.6.x-gcg- _ <date> _ ` de Compute
Engine. Para solucionar este problema, Compute Engine ha desactivado los
kernels de las versiones 2.6.x y recomienda que los usuarios actualicen sus
instancias e imágenes para usar el kernel de Compute Engine ` gce-v20130225 `
. El ` gce-v20130225 ` contiene el kernel ` 3.3.8-gcg-201302081521 ` , que
cuenta con el parche correspondiente a esta vulnerabilidad.

Para saber qué versión de kernel usa tu instancia, sigue estos pasos:

  1. Aplica SSH en tu instancia. 
  2. Ejecuta ` uname -r ` . 

|  Media  |  [ CVE‑2013‑0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

