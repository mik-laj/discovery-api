#  Boletines de seguridad

Periódicamente, es posible que publiquemos boletines de seguridad relacionados
con Compute Engine. Todos los boletines de seguridad de Compute Engine se
describen aquí.

[ Suscríbete a los boletines de seguridad de Compute Engine.
![Suscribirse](https://cloud.google.com/images/feed-icon.png?hl=es_419)
](https://cloud.google.com/feeds/compute-engine-security-
bulletins.xml?hl=es_419)

##  Fecha de publicación: 18-06-2019

**Última actualización: 25-06-2019 H 6:30 a.m. PST**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

Netflix divulgó recientemente tres vulnerabilidades de TCP de los kernel de
Linux:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Estas CVE se conocen en conjunto como [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) .

####  Impacto en Compute Engine

La infraestructura que aloja Google Compute Engine está protegida contra esta
vulnerabilidad.

Las VM de Compute Engine que ejecutan sistemas operativos de Linux sin parches
y que envían o reciben tráfico de red no confiable, son vulnerables a este
ataque DoS. Evalúa actualizar estas instancias de VM apenas estén disponibles
los parches para sus sistemas operativos.

Los balanceadores de cargas que finalizan las conexiones TCP cuentan con
parches frente a esta vulnerabilidad. Las instancias de Compute Engine que
reciben tráfico no confiable únicamente a través de estos balanceadores de
cargas no son vulnerables. Esto incluye balanceadores de cargas de HTTP y de
proxies SSL y TCP.

Los balanceadores de cargas de red y los internos no finalizan las conexiones
TCP. Las instancias de Compute Engine sin parches que reciben tráfico no
confiable a través de estos balanceadores de cargas son vulnerables.

####  Imágenes con parches y recursos de proveedores

Proporcionamos vínculos a la información sobre los parches de cada proveedor
de sistemas operativos a medida que estén disponibles, incluido el estado de
cada CVE. Las versiones anteriores de estas imágenes públicas no contienen
estos parches y no disminuyen la posibilidad de ataques:

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

|  Medio  |

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

  
  
##  Fecha de publicación: 14-05-2019

**Última actualización: 20-05-2019 H 17:00 PST**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

Intel divulgó las siguientes CVE:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Estas CVE se conocen en conjunto como Muestreo de datos de microarquitectura
(MDS). Estas vulnerabilidades pueden hacer que los datos se expongan cuando la
ejecución especulativa interactúa con el estado de la microarquitectura.

####  Impacto en Compute Engine

**La infraestructura del host que ejecuta Compute Engine aísla las cargas de
trabajo del cliente entre sí. Con esto, no se requieren más acciones, a menos
que ejecutes códigos no confiables en tus VM.**

Los clientes que ejecuten códigos no confiables en sus servicios de varias
instancias dentro de las máquinas virtuales de Compute Engine deben consultar
la mitigación recomendada por el proveedor de su SO invitado, que puede
consistir en el uso de las características de mitigación de microcódigo de
Intel. Hemos implementado acceso de tránsito para invitados en la
funcionalidad nueva de vaciado. A continuación, se muestra un resumen sobre
los pasos de mitigación disponibles para imágenes comunes de invitado.

####  Imágenes con parches y recursos de proveedores

Proporcionamos vínculos a la información sobre los parches de cada proveedor
de sistemas operativos a medida que estén disponibles, incluido el estado de
cada CVE. Usa estas imágenes para recrear instancias de VM. Las versiones
anteriores de estas imágenes públicas no contienen estos parches y no
disminuyen la posibilidad de ataques:

  * Proyecto ` centos-cloud ` : [ CESA-2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) , [ CESA-2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html)
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * Proyecto ` coreos-cloud ` : [ Mitigaciones contra MDS para CoreOS Container Linux ](https://coreos.com/os/docs/latest/disabling-smt.html)
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * Proyecto ` cos-cloud ` : 
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * Proyecto ` debian-cloud ` : [ DSA-4444 ](https://www.debian.org/security/2019/dsa-4444)
    * ` debian-9-stretch-v20190514 `
  * Proyecto ` rhel-cloud ` : [ Artículo de la base de conocimientos de Red Hat sobre MDS ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * Proyecto ` rhel-sap-cloud ` : [ Artículo de la base de conocimientos de Red Hat sobre MDS ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * Proyecto ` suse-cloud ` : [ Artículo de la base de conocimientos de SUSE sobre MDS ](https://www.suse.com/support/kb/doc/?id=7023736)
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * Proyecto ` suse-sap-cloud ` : 
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * Proyecto ` ubuntu-os-cloud ` : [ Artículo de la wiki de Ubuntu sobre MDS ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS)
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * Proyectos ` windows-cloud ` y ` windows-sql-cloud ` : [ Artículo ADV190013 de Microsoft ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013)
    * Todas las imágenes públicas de Windows Server y SQL Server con el número de versión ` v20190514 `
  * Proyecto ` gce-uefi-images ` : 
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * Todas las imágenes públicas de Windows Server con el número de versión ` v20190514 `

####  Container-Optimized OS

Te recomendamos hacer lo siguiente si tu SO invitado es Container Optimized OS
(COS) y ejecutas cargas de trabajo de varias instancias no confiables en tu
máquina virtual:

  1. Ingresa ` nosmt ` en la línea de comandos del kernel para inhabilitar el Hyper-Threading.   

Para ingresar la opción de ` nosmt ` en las VM con COS y luego reiniciar el
sistema, modifica el ` grub.cfg ` de la siguiente manera:

    
        
    # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

Para mayor comodidad, puedes ejecutar la secuencia de comandos que se muestra
abajo y obtendrás el mismo resultado que proporciona la ejecución de los
comandos de arriba. Te recomendamos incorporar esta secuencia de comandos a tu
cloud-config, a tus secuencias de comandos de inicio o a tus plantillas de
instancia para asegurarte de que las VM recién creadas usen este parámetro
nuevo. A continuación, proporcionamos un ejemplo de un cloud-config que
ejecuta esta secuencia de comandos.

**Advertencia** : Cuando se ejecuta por primera vez, esta secuencia de
comandos reinicia inmediatamente la instancia. Las ejecuciones posteriores de
este comando en una instancia donde se ha inhabilitado el Hyper-Threading no
tendrán efecto alguno.

    
        
    # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

Ingresa lo siguiente para incluirla en tu cloud-config:

    
        
    #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

Mira el output de los archivos en ` /sys/devices/system/cpu/smt/active ` y `
/sys/devices/system/cpu/smt/control ` para verificar si el Hyper-Threading
está inhabilitado en tu instancia. Si muestra ` 0 ` en ` active ` y ` off ` en
` control ` , significa que el Hyper-Threading está inhabilitado:

    
        
    cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**Nota** : Si tu instancia tiene inicio seguro de UEFI, tendrás que recrearla
sin esa característica, ejecutar el comando mostrado arriba y luego volver a
habilitar el inicio seguro de UEFI en tu instancia nueva.

  2. Usa una versión nueva de la imagen de COS.   

Además de inhabilitar el Hyper-Threading con los pasos ya descritos, deberías
[ recrear tus instancias
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=es_419#publicimage) con las imágenes actualizadas de la lista de
arriba o versiones más nuevas (si están disponibles) de las imágenes del
Container-Optimized OS para obtener protección total contra la vulnerabilidad.

|  Medio  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  Fecha de publicación: 14-08-2018

**Última actualización: 20-08-2018 H 17:00 PST**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

[ Intel divulgó ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) las siguientes CVE:

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (para [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (para sistemas operativos y [ SMT ](https://en.wikipedia.org/wiki/Hyper-Threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (para virtualización) 

Estas CVE se conocen en conjunto como "Falla de terminal L1 (L1TF)".

Estas vulnerabilidades L1TF explotan la ejecución especulativa, ya que atacan
la configuración de estructuras de datos en el procesador. "L1" hace
referencia a la caché de datos de nivel 1 (L1D), un recurso pequeño del núcleo
que se utiliza para acelerar el acceso a la memoria.

Consulta la [ entrada de blog de Google Cloud
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=es_419) para obtener más detalles sobre estas
vulnerabilidades y las mitigaciones de Compute Engine.

####  Impacto en Compute Engine

La infraestructura del host que ejecuta Compute Engine y aísla las cargas de
trabajo del cliente entre sí está protegida frente a los ataques conocidos.

Se recomienda a los clientes de Compute Engine que actualicen su imagen para
impedir la posible explotación indirecta dentro de los entornos invitados.
Esto es importante especialmente para los clientes que ejecutan sus propios
servicios de varias instancias en las máquinas virtuales de Compute Engine.

Los clientes de Google Compute Engine pueden actualizar los sistemas
operativos invitados en sus instancias con una de las siguientes opciones:

  * Usa las imágenes públicas con parches para [ recrear las instancias de VM existentes ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=es_419#publicimage) . 
  * En las instancias existentes, instala los parches que suministra el proveedor del sistema operativo y reinicia las instancias con parches. 

####  Imágenes con parches y recursos de proveedores

Proporcionamos vínculos a la información sobre los parches de cada proveedor
de sistemas operativos a medida que estén disponibles, incluido el estado de
ambas CVE. Usa estas imágenes para recrear las instancias de VM. Las versiones
anteriores de estas imágenes públicas no contienen estos parches y no
disminuyen la posibilidad de ataques:

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
    * Todas las [ imágenes públicas ](https://cloud.google.com/compute/docs/images?hl=es_419#os-compute-support) de Windows Server y SQL Server con el número de versión ` -v201800814 ` y posteriores incluyen parches 

|  Alta  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  Fecha de publicación: 06-08-2018

**Última actualización: 05-09-2018 H 17:00 PST**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Actualización del 05-09-2018

US-CERT divulgó la vulnerabilidad [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) el 14 de agosto de 2018. Al igual que [
CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
, se trata de una vulnerabilidad de las herramientas de red del kernel que
aumenta la eficacia de los ataques de denegación del servicio (DoS) realizados
contra sistemas vulnerables. La diferencia principal es que la CVE-2018-5391
se puede utilizar en conexiones IP. Actualizamos este boletín para que abarque
ambas vulnerabilidades.

####  Descripción

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") describe una
vulnerabilidad de la red en el kernel que aumenta la efectividad de los
ataques de denegación del servicio (DoS) contra sistemas vulnerables a través
de conexiones de TCP.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") describe una
vulnerabilidad de la red en el kernel que aumenta la efectividad de los
ataques de denegación del servicio (DoS) contra sistemas vulnerables a través
de conexiones IP.

####  Impacto en Compute Engine

La infraestructura del host que ejecuta las VM de Compute Engine no está en
riesgo. La infraestructura de red que controla el tráfico desde y hacia las VM
de Compute Engine está protegida frente a esta vulnerabilidad. Las VM de
Compute Engine que solo envían o reciben tráfico de red no confiable a través
de [ balanceadores de cargas HTTP(S) ](https://cloud.google.com/load-
balancing/docs/https/?hl=es_419) , [ SSL ](https://cloud.google.com/load-
balancing/docs/ssl/?hl=es_419) o [ TCP ](https://cloud.google.com/load-
balancing/docs/tcp/?hl=es_419) están protegidas frente a esta vulnerabilidad.

Las VM de Compute Engine que ejecutan sistemas operativos sin parches que
envían o reciben tráfico de red no confiable directamente o a través de [
balanceadores de carga de red ](https://cloud.google.com/load-
balancing/docs/network/?hl=es_419) son vulnerables a este ataque DoS.

Evalúa actualizar tus instancias de VM apenas estén disponibles los parches
para sus sistemas operativos.

Los clientes de Compute Engine pueden actualizar los sistemas operativos
invitados en sus instancias con una de las siguientes opciones:

  * Usa las imágenes públicas con parches para [ recrear las instancias de VM existentes ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=es_419#publicimage) . Consulta la lista de imágenes públicas con parches que se muestra a continuación. 
  * En las instancias existentes, instala los parches que suministra el proveedor del sistema operativo y reinicia las instancias con parches. 

####  Imágenes con parches y recursos de proveedores

Proporcionamos vínculos a la información sobre los parches de cada proveedor
de sistemas operativos a medida que estén disponibles.

  * Proyecto ` centos-cloud ` (CVE-2018-5390 únicamente): 
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
  * Proyecto ` rhel-cloud ` (CVE-2018-5390 únicamente): 
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

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  Fecha de publicación: 03-01-2018

**Última actualización: 21-05-2018 H 15:00 PST**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Actualización del 21-05-2018

[ Intel divulgó ](https://www.intel.com/content/www/us/en/security-
center/advisory/intel-sa-00115.html) las vulnerabilidades [ CVE-2018-3640
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640) y [
CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)
, variantes 3a y 4, respectivamente. Al igual que con las primeras tres
variantes de Spectre y Meltdown, la infraestructura que ejecuta las instancias
de VM de Compute Engine está protegida y las instancias de VM de los clientes
están aisladas y protegidas entre sí. Además, Compute Engine planea
implementar los parches de microcódigo de Intel en su infraestructura, lo que
permitirá que los clientes que ejecutan cargas de trabajo no confiables o de
varias instancias en una única instancia de VM puedan habilitar mitigaciones
adicionales dentro de las VM cuando los proveedores de los sistemas operativos
proporcionen esas mitigaciones. Una vez que Intel certifique los parches de
microcódigo, Compute Engine los implementará después de probarlos y
calificarlos para el entorno de producción. Brindaremos cronogramas detallados
y actualizaciones en esta página a medida que estén disponibles.

####  Descripción

Estas CVE son variantes de una clase nueva de ataque que explota la tecnología
de ejecución especulativa disponible en varios procesadores. Esta clase de
ataque puede otorgar acceso de solo lectura no autorizado a los datos de la
memoria en diversas circunstancias.

Compute Engine usó la tecnología de migración en vivo de VM para llevar a cabo
actualizaciones del sistema de host y del hipervisor sin afectar a los
usuarios y sin períodos de mantenimiento forzoso ni reinicios masivos. Sin
embargo, todos los sistemas operativos invitados y las versiones deben contar
con parches que los protejan frente a esta nueva clase de ataque,
independientemente de dónde se ejecuten esos sistemas.

Consulta la [ entrada de blog sobre Project Zero
](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-
with-side.html) para obtener detalles técnicos completos sobre este método de
ataque. Consulta la [ entrada de blog sobre la seguridad de Google
](https://security.googleblog.com/2018/01/todays-cpu-vulnerability-what-you-
need.html) para obtener detalles completos sobre las mitigaciones de Google,
incluida información específica de los productos.

####  Impacto en Compute Engine

La infraestructura que ejecuta Compute Engine y aísla las instancias de VM de
los clientes entre sí está protegida frente a ataques conocidos. Nuestras
mitigaciones evitan el acceso no autorizado a los sistemas de host desde
aplicaciones que se ejecuten dentro de las instancias de VM. Estas
mitigaciones también evitan el acceso no autorizado entre las instancias de VM
que se ejecuten en el mismo sistema de host.

Para evitar el acceso no autorizado dentro de tus instancias de máquina
virtual, debes actualizar los sistemas operativos invitados en esas instancias
con una de las siguientes opciones:

  * Usa las imágenes públicas con parches para [ recrear tus instancias de VM existentes ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=es_419#publicimage) . Consulta la lista de imágenes públicas con parches que se muestra a continuación. 
  * En las instancias existentes, instala los parches que suministra el proveedor del sistema operativo para tu distribución y reinicia las instancias con parches. Consulta los vínculos a la información sobre los parches de cada proveedor de sistemas operativos a continuación. 

####  Imágenes con parches y recursos de proveedores

**Nota:** Las imágenes con parches pueden no incluir correcciones para todas
las CVE mencionadas en este aviso del boletín de seguridad. Además, las
diferentes imágenes pueden incluir métodos distintos para evitar estos tipos
de ataques. Comunícate con el proveedor de tu sistema operativo para confirmar
cuáles CVE se abordan en sus parches y qué métodos de prevención usan.

  * Proyecto ` cos-cloud ` : Incluye parches que previenen los ataques de las variantes 2 ( [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ) y 3 ( [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ). Google usó [ Retpoline ](https://support.google.com/faqs/answer/7625886?hl=es_419) en estas imágenes para mitigar los ataques de la variante 2. 
    * ` cos-stable-63-10032-71-0 ` o la familia de imágenes ` cos-stable `
  * Proyecto ` centos-cloud ` : [ Información de parches de CentOS ](https://lwn.net/Alerts/CentOS/)
    * ` centos-7-v20180104 ` o la familia de imágenes ` centos-7 `
    * ` centos-6-v20180104 ` o la familia de imágenes ` centos-6 `
  * Proyecto ` coreos-cloud ` : [ Información de parches de CoreOS ](https://coreos.com/blog/container-linux-meltdown-patch)
    * ` coreos-stable-1576-5-0-v20180105 ` o la familia de imágenes ` coreos-stable `
    * ` coreos-beta-1632-1-0-v20180105 ` o la familia de imágenes ` coreos-beta `
    * ` coreos-alpha-1649-0-0-v20180105 ` o la familia de imágenes ` coreos-alpha `
  * Proyecto ` debian-cloud ` : [ Información de parches de Debian ](https://www.debian.org/security/#DSAS)
    * ` debian-9-stretch-v20180105 ` o la familia de imágenes ` debian-9 `
    * ` debian-8-jessie-v20180109 ` o la familia de imágenes ` debian-8 `
  * Proyecto ` rhel-cloud ` : [ Información de parches de RHEL ](https://access.redhat.com/security/vulnerabilities/speculativeexecution)
    * ` rhel-7-v20180104 ` o la familia de imágenes ` rhel-7 `
    * ` rhel-6-v20180104 ` o la familia de imágenes ` rhel-6 `
  * Proyecto ` suse-cloud ` : [ Información de parches de SUSE ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-v20180104 ` o la familia de imágenes ` sles-12 `
    * ` sles-11-sp4-v20180104 ` o la familia de imágenes ` sles-11 `
  * Proyecto ` suse-sap-cloud ` : [ Información de parches de SUSE ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-sap-v20180104 ` o la familia de imágenes ` sles-12-sp3-sap `
    * ` sles-12-sp2-sap-v20180104 ` o la familia de imágenes ` sles-12-sp2-sap `
  * Proyecto ` ubuntu-os-cloud ` : [ Información de parches de Ubuntu ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/)
    * ` ubuntu-1710-artful-v20180109 ` o la familia de imágenes ` ubuntu-1710 `
    * ` ubuntu-1604-xenial-v20180109 ` o la familia de imágenes ` ubuntu-1604-lts `
    * ` ubuntu-1404-trusty-v20180110 ` o la familia de imágenes ` ubuntu-1404-lts `
  * Proyectos ` windows-cloud ` y ` windows-sql-cloud ` : 
    * Todas las [ imágenes públicas ](https://cloud.google.com/compute/docs/images?hl=es_419#os-compute-support) de Windows Server y SQL Server con el número de versión ` -v20180109 ` y posteriores incluyen parches. Sin embargo, debes realizar las acciones recomendadas que indica Windows en el boletín de asistencia de la [ Guía de Windows Server ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) para habilitar y verificar estas mitigaciones en ambas instancias existentes y en las instancias nuevas. 

Usa estas imágenes para [ recrear las instancias de VM
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=es_419#publicimage) . Las versiones anteriores de estas imágenes
públicas no contienen estos parches y no disminuyen la posibilidad de ataques.

####  Parches de proveedores de hardware

NVIDIA ofrece controladores con parches para disminuir la posibilidad de
ataques contra los sistemas que tienen instalado el software de controlador
NVIDIA®. Para conocer qué versiones de los controladores tienen parches,
consulta el boletín de seguridad [ Actualizaciones de seguridad de
controladores gráficos de GPU de NVIDIA
](http://nvidia.custhelp.com/app/answers/detail/a_id/4611) .

####  Historial de revisión:

  * 21-05-2018, 14:00 horas PST: Se agregó información sobre 2 variantes nuevas publicadas el 21 de mayo de 2018. 
  * 10-01-2018, 15:00 PST: Se agregó información sobre las imágenes públicas de Windows Server y SQL Server con parches. 
  * 10-01-2018, 10:15 PST: Se agregaron varias imágenes de Ubuntu a la lista de imágenes públicas con parches. 
  * 10-01-2018, 09:50 PST: Se agregaron lineamientos sobre los parches de los proveedores de hardware. 
  * Del 03-01-2018 al 09-01-2018: Se realizaron varias revisiones a la lista de imágenes públicas con parches. 

|  Alta  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  Fecha de publicación: 02-10-2017

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

[ Dnsmasq ](http://www.thekelleys.org.uk/dnsmasq/doc.html) proporciona
funciones para publicar anuncios de DNS, DHCP y de router, y para iniciar la
red. Por lo general, este software está instalado en sistemas tan variados
como computadoras de escritorio, distribuciones de Linux (como Ubuntu),
routers domésticos y dispositivos de IoT. Dnsmasq es muy usado tanto en
Internet abierto como en redes privadas.

Google descubrió siete problemas distintos en el transcurso de nuestras
evaluaciones internas y habituales de seguridad. Después de determinar la
gravedad de estos problemas, trabajamos para investigar su impacto y riesgo de
utilización, y generamos pruebas de concepto internas para cada uno. También
trabajamos con Simon Kelly, el encargado de mantenimiento de Dnsmasq, para
generar los parches apropiados y mitigar el problema.

Durante nuestra revisión, el equipo descubrió tres ejecuciones de código
remotas posibles, una filtración de información y tres vulnerabilidades de
denegación del servicio que afectaban la última versión en el servidor Git del
proyecto a partir del 5 de septiembre de 2017.

Estos parches se envían de manera ascendente y se confirman en el [
repositorio de Git del proyecto
](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) .

####  Impacto en Compute Engine

De manera predeterminada, Dnsmasq solo está instalado en imágenes que usan [
NetworkManager ](https://wikipedia.org/wiki/NetworkManager) y se encuentra
inactivo. Las siguientes imágenes públicas de Compute Engine tienen instalado
Dnsmasq:

  * Ubuntu 16.04, 16.10, 17.04 
  * CentOS 7 
  * RHEL 7 

Sin embargo, es posible que otras imágenes tengan instalado Dnsmasq como una
dependencia para otros paquetes. Te recomendamos actualizar las instancias de
Debian, Ubuntu, CentOS, RHEL, SLES y OpenSuse para usar la imagen de sistema
operativo más reciente. CoreOS y Container-Optimized OS no se ven afectados.
Las imágenes de Windows tampoco se ven afectadas.

Para las instancias con Debian y Ubuntu, puedes actualizarlas si ejecutas en
ellas los siguientes comandos:

    
    
    
    sudo apt-get -y update
    
    
    
    sudo apt-get -y dist-upgrade

En instancias de Red Hat Enterprise Linux y CentOS, ejecuta lo siguiente:

    
    
    
    sudo yum -y upgrade

En imágenes de SLES y OpenSUSE, ejecuta lo siguiente:

    
    
    
    sudo zypper up

En lugar de ejecutar los comandos de actualización manual, puedes [ recrear
instancias de VM con las familias de imágenes
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=es_419#publicimage) del sistema operativo correspondiente.

|  Alta  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  Fecha de publicación: 26-10-2016

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

CVE-2016-5195 es una condición de carrera debida a la manera en que el
subsistema de memoria del kernel de Linux controlaba las fallas de la función
COW sobre las asignaciones privadas de solo lectura durante el acceso de
escritura.

Un usuario local sin privilegios podría usar esta vulnerabilidad para obtener
acceso de escritura a asignaciones de memoria que de lo contrario serían de
solo lectura y, de esta manera, aumentar sus privilegios en el sistema.

Para obtener más información, consulta las [ Preguntas frecuentes sobre Dirty
COW
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails) .

####  Impacto en Compute Engine

Todas las distribuciones y versiones de Linux en Compute Engine se ven
afectadas. La mayoría de las instancias se descargarán automáticamente y se
instalarán en un kernel más reciente. Sin embargo, debes reiniciar la
instancia para aplicar el parche a un sistema en ejecución.

Las instancias nuevas o vueltas a crear basadas en las siguientes imágenes de
Compute Engine incluyen kernels con parches instalados.

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
  
##  Fecha de publicación: 16-02-2016

**Última actualización: 22-02-2016**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

CVE-2015-7547 es una vulnerabilidad en la que el agente de resolución del lado
del cliente DNS glibc hace que el software sea vulnerable a un desbordamiento
de búfer basado en la pila cuando se usa la función ` getaddrinfo() ` de la
biblioteca. Si el software usa esta función, un atacante puede aprovecharlo
para explotar la vulnerabilidad mediante ataques de intermediarios o nombres
de dominios y servidores DNS controlados por el atacante.

Para ver más detalles, consulta el [ blog de Google Online Security
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) o la base de datos de [ riesgos y vulnerabilidades
comunes (CVE) ](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-7547) .

####  Impacto en Compute Engine

**Actualización (22-02-2016):**

Ahora puedes recrear tus instancias con las siguientes imágenes de CoreOS,
SLES y OpenSUSE:

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**Actualización (17-02-2016):**

Ahora puedes aplicar una actualización en las instancias de Ubuntu 12.04 LTS,
Ubuntu 14.04 LTS y Ubuntu 15.10 si ejecutas los siguientes comandos:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

En lugar de ejecutar los comandos de actualización en forma manual, ahora
puedes recrear estas instancias con las siguientes imágenes nuevas:

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

No conocemos métodos que puedan explotar esta vulnerabilidad a través de los
agentes de resolución del DNS de Compute Engine con la configuración
predeterminada de glibc. De todas formas, deberías aplicar un parche a tus
instancias de máquinas virtuales lo antes posible, ya que, como ocurre con
todas las vulnerabilidades nuevas, es posible que se descubran nuevos métodos
de explotación con el tiempo. Si habilitaste edns0, que está inhabilitado de
manera predeterminada, deberías inhabilitarlo hasta que se aplique un parche a
las instancias.

**Boletín original:**

Es posible que tu distribución de Linux sea vulnerable. Los clientes de
Compute Engine deberán actualizar las imágenes de SO de sus instancias para
eliminar esta vulnerabilidad si ejecutan un SO de Linux.

Para aplicar una actualización en las instancias que ejecutan Debian, puedes
usar los siguientes comandos en tu instancia:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

También te recomendamos instalar [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) para tus instancias de Debian.

En instancias de Red Hat Enterprise Linux, ejecuta lo siguiente:

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

Seguiremos actualizando este boletín en la medida que otros encargados del
mantenimiento de sistemas operativos publiquen parches para esta
vulnerabilidad y Compute Engine publique imágenes de SO actualizadas.

|  Alta  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  Fecha de publicación: 19-03-2015

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

CVE-2015-1427 es una vulnerabilidad en la que el motor de secuencias de
comandos Groovy de [ Elasticsearch
](https://www.elastic.co/products/elasticsearch) antes de la versión 1.3.8 y
en cualquier versión 1.4.x antes de la 1.4.3, permite que los atacantes eludan
el mecanismo de protección de la zona de pruebas y ejecuten comandos
arbitrarios del shell.

Para ver más detalles, consulta la [ base de datos nacional de
vulnerabilidades (NVD)
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) o la base de
datos de [ riesgos y vulnerabilidades comunes (CVE)
](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-1427) .

####  Impacto en Compute Engine

Si ejecutas Elasticsearch en instancias de Compute Engine, deberías actualizar
tu versión de Elasticsearch a la 1.4.3 o una más reciente. Si ya actualizaste
el software de Elasticsearch, estás protegido contra esta vulnerabilidad.

Si aún no actualizas Elasticsearch a la versión 1.4.3 o una más reciente,
puedes [ ejecutar una actualización progresiva
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) .

Si implementaste Elasticsearch con la [ implementación en un clic
](https://cloud.google.com/solutions/elasticsearch/click-to-deploy?hl=es_419)
en [ Google Cloud Platform Console
](https://console.cloud.google.com/?hl=es_419) , puedes [ borrar la
implementación
](https://console.cloud.google.com/projectselector/deployments?hl=es_419) para
quitar las instancias que ejecutan Elasticsearch.

El equipo de Google Cloud Platform está trabajando en una solución para
implementar una versión actualizada de Elasticsearch. Sin embargo, la solución
aún no está disponible para la función de implementación en un clic en [ GCP
Console ](https://console.cloud.google.com/?hl=es_419) .

|  Alta  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  Fecha de publicación: 29-01-2015

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

[ CVE-2015-0235 (Ghost)
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) es una
vulnerabilidad de la biblioteca glibc.

No es necesario que los clientes de App Engine, Cloud Storage, BigQuery y
CloudSQL realicen ninguna acción. Los servidores de Google se actualizaron y
están protegidos contra esta vulnerabilidad.

Es posible que los clientes de Compute Engine deban actualizar sus imágenes de
SO.

####  Impacto en Compute Engine

Es posible que tu distribución de Linux sea vulnerable. Los clientes de
Compute Engine deberán actualizar las imágenes de SO de sus instancias para
eliminar esta vulnerabilidad si ejecutan Debian 7, backports de Debian 7,
Ubuntu 12.04 LTS, Red Hat Enterprise Linux, CentOS o SUSE Linux Enterprise
Server 11 SP3.

Esta vulnerabilidad no afecta a Ubuntu 14.04 LTS, Ubuntu 14.10 ni SUSE Linux
Enterprise Server 12.

Te recomendamos actualizar tus distribuciones de Linux. Para actualizar las
instancias que ejecutan Debian 7, backports de Debian 7 o Ubuntu 12.04 LTS,
ejecuta los siguientes comandos en tu instancia:

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

En instancias de Red Hat Enterprise Linux o CentOS, ejecuta lo siguiente:

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

En instancias de SUSE Linux Enterprise Server 11 SP3, ejecuta lo siguiente:

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

En lugar de ejecutar en forma manual los comandos de actualización indicados
previamente, ahora los usuarios pueden recrear sus instancias con las
siguientes imágenes nuevas:

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  Impacto sobre VM administradas por Google

Los usuarios de VM administradas que usan ` gcloud preview app deploy ` deben
actualizar sus contenedores de Docker base con ` gcloud preview app setup-
managed-vms ` y volver a implementar cada una de las apps en ejecución con `
gcloud preview app deploy ` . Los usuarios que implementan con ` appcfg ` no
deben realizar ninguna acción ya que se les actualizará automáticamente.

|  Alta  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  Fecha de publicación: 15-10-2014

**Última actualización: 17-10-2014**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

CVE-2014-3566 (conocida también como POODLE) es una vulnerabilidad en el
diseño de SSL versión 3.0. Esta vulnerabilidad permite que un atacante de la
red calcule el texto sin formato de las conexiones seguras. Para ver detalles,
consulta nuestra [ publicación en el blog
](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) sobre la vulnerabilidad.

No es necesario que los clientes de App Engine, Cloud Storage, BigQuery y
CloudSQL realicen ninguna acción. Los servidores de Google se actualizaron y
están protegidos contra esta vulnerabilidad. Los clientes de Compute Engine
deben actualizar sus imágenes de SO.

####  Impacto en Compute Engine

**Actualización (17-10-2014):**

Si usas SSLv3, es posible que seas vulnerable. Los clientes de Compute Engine
deberán actualizar las imágenes de SO de sus instancias para eliminar esta
vulnerabilidad.

Te recomendamos actualizar tus distribuciones de Linux. Para aplicar una
actualización en las instancias que ejecutan Debian, puedes usar los
siguientes comandos en tu instancia:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

En instancias de CentOS:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

En lugar de ejecutar en forma manual los comandos de actualización indicados
previamente, ahora los usuarios pueden recrear sus instancias con las
siguientes imágenes nuevas:

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

Actualizaremos el boletín para las imágenes de RHEL y SLES una vez que
tengamos las imágenes. Por el momento, los usuarios de RHEL pueden consultar [
directamente con Red Hat ](https://access.redhat.com/articles/1232123) para
obtener más información.

**Boletín original:**

Los clientes de Compute Engine deberán actualizar las imágenes de SO de sus
instancias para eliminar esta vulnerabilidad. Actualizaremos este boletín de
seguridad con instrucciones una vez que haya imágenes de SO nuevas
disponibles.

|  Medio  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  Fecha de publicación: 24-09-2014

**Última actualización: 29-09-2014**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

Existe un error en bash (CVE-2014-6271) que permite la ejecución remota de
código a partir del análisis de variables de entorno controladas por el
atacante. El vector de explotación más probable es a través de solicitudes
HTTP maliciosas compuestas por secuencias de comandos de CGI expuestas en un
servidor web. Para obtener más información, consulta la [ descripción del
error ](http://seclists.org/oss-sec/2014/q3/650) .

Los errores de bash se mitigaron para productos de Google Cloud Platform,
excepto para las imágenes de SO de invitado de Compute Engine con fecha previa
al 26-09-2014. Consulta los siguientes pasos para mitigar los errores en tus
imágenes de Compute Engine.

####  Impacto en Compute Engine

Es posible que este error afecte prácticamente a todos los sitios web que usan
secuencias de comandos de CGI. Además, es probable que afecte a sitios web que
dependen de PHP, Perl, Python, SSI, Java, C++ y servlets similares que alguna
vez invocarán comandos del shell a través de llamadas como ` popen ` , `
system ` , ` shell_exec ` o API similares. También podría afectar sistemas que
intentan permitir el acceso controlado a los usuarios restringidos mediante
mecanismos como la limitación de comandos de SSH o el shell con restricción de
bash.

**Actualización (29-09-2014):**

En lugar de ejecutar en forma manual los comandos de actualización indicados a
continuación, ahora los usuarios pueden recrear sus instancias con imágenes
que mitigan vulnerabilidades adicionales relacionadas con el error de
seguridad de Bash, incluidas [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6277 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277)
, [ CVE-2014-6278
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278) , [
CVE-2014-7186 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186)
y [ CVE-2014-7187
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187) . Usa las
siguientes imágenes nuevas para recrear tus instancias:

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**Actualización (25-09-2014):**

Ahora, los usuarios pueden recrear sus instancias en lugar de ejecutar una
actualización manual. Para recrear tus instancias, usa las siguientes imágenes
que contienen soluciones a este error de seguridad:

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

Para aplicar actualizaciones manuales a imágenes de RHEL y SUSE, puedes
ejecutar los siguientes comandos en tus instancias:

    
    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**Boletín original:**

Te recomendamos actualizar tus distribuciones de Linux. Para aplicar una
actualización en las instancias que ejecutan Debian, puedes usar los
siguientes comandos en tu instancia:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

En instancias de CentOS:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade

Para ver información detallada, revisa el anuncio para la distribución de
Linux correspondiente:

  * Parches originales: [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) (consulta la última entrada en *-patches para la versión que corresponda) 
  * Debian: [ [SECURITY] [DSA 3032-1] actualización de seguridad de bash ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
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
, [ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) , [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  Fecha de publicación: 25-07-2014

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

[ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/) es
vulnerable a la inyección de comandos de SO que pueden permitir la
modificación y divulgación de los datos sin autorización. Un atacante puede
enviar eventos fabricados a cualquiera de las fuentes de datos de Logstash, lo
que le permite ejecutar comandos con los permisos del proceso de Logstash.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todas las instancias de Compute Engine que
ejecutan versiones de Elasticsearch Logstash previas a la 1.4.2 con salidas
zabbix o nagios_nsca habilitadas. Para evitar ataques, puedes seguir uno de
estos pasos:

  * Actualiza a Logstash 1.4.2. 
  * Aplica el parche para las versiones 1.3.x. 
  * Inhabilita las salidas ` zabbix ` y ` nagios_nsca ` . 

Obtén más información en el [ blog de Logstash
](http://www.elasticsearch.org/blog/logstash-1-4-2/) .

Elasticsearch también recomienda [ usar un firewall
](http://www.elasticsearch.org/blog/scripting-security/) para evitar el acceso
remoto de las IP que no sean de confianza.

|  Alta  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  Fecha de publicación: 18-06-2014

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

Nos gustaría tomarnos un momento para responder a todos los posibles problemas
que tienen los clientes sobre la seguridad de los contenedores de Docker
cuando ejecutan Google Cloud Platform. Esto incluye a los clientes que usan
extensiones de Google App Engine que admiten contenedores de Docker, máquinas
virtuales optimizadas para contenedores o el programador Kubernetes de código
abierto.

Docker respondió al problema de manera excelente y puedes ver la respuesta en
su blog [ aquí ](http://blog.docker.com/2014/06/docker-container-breakout-
proof-of-concept-exploit/) . Ten en cuenta que, como señalan allí, el problema
revelado solo se aplica a Docker 0.11, una versión antigua previa a
producción.

Si bien los usuarios se preocupan por la seguridad de los contenedores, nos
gustaría señalar que en Google Cloud Platform las soluciones basadas en
contenedores de aplicaciones de Linux (específicamente, contenedores de
Docker) se ejecutan en máquinas virtuales completas (Compute Engine). Si bien
apoyamos los esfuerzos de la comunidad de Docker para fortalecer la pila de
contenedores de aplicaciones de Linux, reconocemos que la tecnología es nueva
y su área de superficie es amplia. Creemos que, por ahora, los hipervisores
completos (máquinas virtuales) proporcionan un área de superficie defendible
más compacta. Las máquinas virtuales se diseñaron desde el comienzo para
aislar las cargas de trabajo maliciosas y minimizar la probabilidad y el
impacto de un error de código.

Nuestros clientes pueden estar seguros de que existe una barrera de un
hipervisor completo entre ellos y cualquier código externo posiblemente
malicioso. Si alcanzamos un punto en el que consideramos que la pila de
contenedores de aplicación de Linux es lo suficientemente sólida como para
admitir cargas de trabajo multiusuario, lo informaremos a la comunidad. Por
ahora, el contenedor de aplicaciones de Linux no reemplaza la máquina virtual.
Es una manera de aprovecharlo mucho más.

|  Baja  |  [ Publicación en el blog de Docker
](http://blog.docker.com/2014/06/docker-container-breakout-proof-of-concept-
exploit/)  
  
##  Fecha de publicación: 05-06-2014

**Última actualización: 09-06-2014**

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

OpenSSL tiene un problema en el que los mensajes de ` ChangeCipherSpec ` no se
vinculan correctamente con la máquina de estados del protocolo de enlace. Esto
permite que se inyecten antes en el protocolo de enlace. Un atacante que use
un protocolo de enlace fabricado cuidadosamente puede forzar el uso de
material de claves vulnerable en clientes y servidores SSL/TLS de OpenSSL.
Esto se puede explotar mediante un ataque de intermediarios, en el que el
atacante puede desencriptar y modificar el tráfico desde el cliente y el
servidor atacados.

Este problema se identifica como [ CVE-2014-0224
](https://www.openssl.org/news/secadv/20140605.txt) . El equipo de OpenSSL
corrigió el problema y alertó a su comunidad para que actualicen OpenSSL.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todas las instancias de Compute Engine que usan
OpenSSL, incluido Debian, CentOS, Red Hat Enterprise Linux y SUSE Linux
Enterprise Server. Para actualizar tus instancias, puedes recrearlas con
imágenes nuevas o actualizar sus paquetes de forma manual.

**Actualización (09-06-2014):** Para actualizar tus instancias que ejecutan
SUSE Linux Enterprise Server con imágenes nuevas, recréalas con las siguientes
versiones de las imágenes o con otras más recientes:

  * ` sles-11-sp3-v20140609 `

**Publicación original:**

Para actualizar imágenes de Debian y CentOS con imágenes nuevas, recrea tus
instancias con cualquiera de las siguientes versiones de las imágenes o con
otras más recientes:

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

Si deseas actualizar OpenSSL de forma manual en tus instancias, ejecuta los
siguientes comandos para actualizar los paquetes que correspondan. Para
actualizar OpenSSL en instancias con CentOS y RHEL, ejecuta estos comandos:

    
    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

Para actualizar OpenSSL en instancias con Debian, ejecuta los siguientes
comandos:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

Para asegurarte de que OpenSSL está actualizado en instancias con SUSE Linux
Enterprise Server, ejecuta estos comandos:

    
    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  Medio  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  Fecha de publicación: 08-04-2014

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

Las implementaciones (1) TLS y (2) DTLS en OpenSSL 1.0.1, antes de la versión
1.0.1g, no administran adecuadamente los paquetes de Heartbeat Extension, lo
que permite que los atacantes remotos obtengan información confidencial de la
memoria de procesos mediante paquetes fabricados que activan una sobrelectura
del búfer, como se refleja en la lectura de claves privadas, en relación con `
d1_both.c ` y ` t1_lib.c ` , también conocido como el error Heartbleed.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todas las instancias de Compute Engine que
ejecutan Debian, RHEL y CentOS y que no tienen la versión más actualizada de
OpenSSL. Para actualizar tus instancias, puedes recrearlas con imágenes nuevas
o actualizar los paquetes de tus instancias de forma manual.

Para actualizar tus instancias con imágenes nuevas, recréalas con cualquiera
de las siguientes versiones de las imágenes o con otras más recientes:

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

Si deseas actualizar OpenSSL de forma manual en tus instancias, ejecuta los
siguientes comandos para actualizar los paquetes que correspondan. Para
asegurarte de que OpenSSL esté actualizado en instancias con CentOS y RHEL,
ejecuta estos comandos:

    
    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

Para actualizar OpenSSL en instancias con Debian, ejecuta los siguientes
comandos:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

Las instancias que ejecutan SUSE Linux no se ven afectadas.

**Actualización del 14 de abril de 2014:** A la luz de los nuevos estudios
sobre la extracción de claves con el error Heartbleed, Compute Engine
recomienda que los usuarios de Compute Engine creen claves nuevas para todos
los servicios de SSL afectados.

|  Medio  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  Fecha de publicación: 07-06-2013

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

**Nota:** Esta vulnerabilidad solo se aplica a los kernels que dejaron de
estar disponibles y se quitaron a partir de la versión v1 de la API.

La vulnerabilidad en el string de formato de la función ` b43_request_firmware
` en ` drivers/net/wireless/b43/main.c ` en el controlador inalámbrico
Broadcom B43 del kernel de Linux hasta la versión 3.9.4 permite que los
usuarios locales obtengan privilegios si aprovechan el acceso de raíz y
agregan especificadores al string de formato en un parámetro modprobe de `
fwpostfix ` , lo que genera la construcción inadecuada de un mensaje de error.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todos los kernels de Compute Engine previos al `
gcg-3.3.8-201305291443 ` . En respuesta, Compute Engine dio de baja todos los
kernels anteriores y recomienda que los usuarios actualicen sus instancias y
sus imágenes para usar el kernel ` gce-v20130603 ` de Compute Engine. El
kernel ` gce-v20130603 ` contiene el ` gcg-3.3.8-201305291443 ` , que tiene el
parche para esta vulnerabilidad.

Para saber qué versión de kernel usa tu instancia, ejecuta lo siguiente:

  1. Implementa SSH en tu instancia. 
  2. Ejecuta ` uname -r ` . 

|  Medio  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  Fecha de publicación: 07-06-2013

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

**Nota:** Esta vulnerabilidad solo se aplica a los kernels que dejaron de
estar disponibles y se quitaron a partir de la versión v1 de la API.

La vulnerabilidad en el string de formato de la función register_disk de `
block/genhd.c ` en el kernel de Linux hasta la versión 3.9.4 permite que los
usuarios locales obtengan privilegios si aprovechan el acceso de raíz y
escriben especificadores en el string de formato para `
/sys/module/md_mod/parameters/new_array ` , a fin de crear un nombre de
dispositivo de ` /dev/md ` fabricado.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todos los kernels de Compute Engine previos al `
gcg-3.3.8-201305291443 ` . En respuesta, Compute Engine dio de baja todos los
kernels anteriores y recomienda que los usuarios actualicen sus instancias y
sus imágenes para usar el kernel ` gce-v20130603 ` de Compute Engine. El
kernel ` gce-v20130603 ` contiene el ` gcg-3.3.8-201305291443 ` , que tiene el
parche para esta vulnerabilidad.

Para saber qué versión de kernel usa tu instancia, ejecuta lo siguiente:

  1. Implementa SSH en tu instancia. 
  2. Ejecuta ` uname -r ` . 

|  Medio  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  Fecha de publicación: 14-05-2013

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

**Nota:** Esta vulnerabilidad solo se aplica a los kernels que dejaron de
estar disponibles y se quitaron a partir de la versión v1 de la API.

La función perf_swevent_init de ` kernel/events/core.c ` en el kernel de Linux
antes de la versión 3.8.9 usa un tipo de datos ` integer ` incorrecto, lo que
permite que los usuarios locales obtengan privilegios mediante una llamada de
sistema ` perf_event_open ` fabricada.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a todos los kernels de Compute Engine previos al `
gcg-3.3.8-201305211623 ` . En respuesta, Compute Engine dio de baja todos los
kernels anteriores y recomienda que los usuarios actualicen sus instancias y
sus imágenes para usar el kernel ` gce-v20130521 ` de Compute Engine. El
kernel ` gce-v20130521 ` contiene el ` gcg-3.3.8-201305211623 ` , que tiene el
parche para esta vulnerabilidad.

Para saber qué versión de kernel usa tu instancia, ejecuta lo siguiente:

  1. Implementa SSH en tu instancia. 
  2. Ejecuta ` uname -r ` . 

|  Alta  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  Fecha de publicación: 18-02-2013

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Descripción

**Nota:** Esta vulnerabilidad solo se aplica a los kernels que dejaron de
estar disponibles y se quitaron a partir de la versión v1 de la API.

La condición de carrera en la función ptrace del kernel de Linux antes de la
versión 3.7.5 permite que los usuarios locales obtengan privilegios mediante
una llamada de sistema ` PTRACE_SETREGS ptrace ` en una aplicación fabricada.

####  Impacto en Compute Engine

Esta vulnerabilidad afecta a los kernels de Compute Engine previos al `
2.6.x-gcg- _ <date> _ ` . En respuesta, Compute Engine dio de baja los kernels
de las versiones 2.6.x y recomienda que los usuarios actualicen sus instancias
y sus imágenes para usar el kernel ` gce-v20130225 ` de Compute Engine. El
kernel ` gce-v20130225 ` contiene el ` 3.3.8-gcg-201302081521 ` , que tiene el
parche para esta vulnerabilidad.

Para saber qué versión de kernel usa tu instancia, ejecuta lo siguiente:

  1. Implementa SSH en tu instancia. 
  2. Ejecuta ` uname -r ` . 

|  Medio  |  [ CVE-2013-0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

