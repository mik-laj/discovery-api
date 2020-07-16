#  Boletines de seguridad

En esta página se describen todos los boletines de seguridad de Google
Kubernetes Engine (GKE).

Es habitual que las vulnerabilidades se mantengan en secreto y no puedan
divulgarse hasta que las partes afectadas hayan tenido oportunidad de
mitigarlas. En estos casos, las [ notas de la versión
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=es) de GKE
harán referencia a "actualizaciones de seguridad" hasta que se apruebe la
divulgación. Llegado ese momento, las notas se actualizan para hacer
referencia a la vulnerabilidad que se ha mitigado con el parche.

**Nota:** Si ejecutas cargas de trabajo de varios propietarios en GKE, presta
especial atención a estos boletines. Lo más probable es que estas
vulnerabilidades afecten a las cargas de trabajo de varios propietarios. En [
esta entrada de blog sobre el aislamiento en diferentes capas de la pila de
Kubernetes ](https://cloudplatform.googleblog.com/2018/05/Exploring-container-
security-Isolation-at-different-layers-of-the-Kubernetes-stack.html) ,
encontrarás una descripción técnica de los límites de seguridad de GKE e
información sobre cómo pueden afectar a tus cargas de trabajo.

Si quieres recibir los últimos boletines de seguridad, añade la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) o incluye la URL
del feed directamente: ` https://cloud.google.com/feeds/kubernetes-engine-
security-bulletins.xml `

##  GCP-2020-007

**Publicación:** 01/06/2020  
Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco se ha descubierto una vulnerabilidad de falsificación de solicitud
del servidor (SSRF) en Kubernetes, descrita en la [ CVE-2020-8555
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555) , que permite
a ciertos usuarios autorizados filtrar hasta 500 bytes de información sensible
desde la red de host del plano de control. El plano de control de Google
Kubernetes Engine (GKE) utiliza controladores de Kubernetes y, por lo tanto,
se ve afectado por esta vulnerabilidad. Te recomendamos que [ actualices
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=es) el plano de control a la versión más reciente del
parche como se indica a continuación. No hace falta actualizar el nodo.  

####  ¿Qué debo hacer?

En el caso de la mayor parte de los clientes, no es necesario realizar ninguna
otra acción. La gran mayoría de los clústeres ya utilizan una versión con
parche. Las versiones de GKE que se indican a continuación o las que sean más
recientes contienen la mitigación de esta vulnerabilidad:

  * 1.14.7-gke.39 
  * 1.14.8-gke.32 
  * 1.14.9-gke.17 
  * 1.14.10-gke.12 
  * 1.15.7-gke.17 
  * 1.16.4-gke.21 
  * 1.17.0-gke.0 

Los clústeres que usan [ canales de versiones
](https://cloud.google.com/kubernetes-engine/docs/concepts/release-
channels?hl=es) ya utilizan una versión del plano de control con la
mitigación.

####  ¿Qué vulnerabilidad trata este parche?

Estos parches mitigan la vulnerabilidad CVE-2020-8555. Se considera una
vulnerabilidad media de GKE, ya que fue difícil aprovecharse de ella gracias a
diversas medidas de endurecimiento del plano de control.

Un atacante con permiso para crear un recurso StorageClass o un pod con
ciertos tipos de volúmenes integrados (GlusterFS, Quobyte, StorageFS o
ScaleIO) puede provocar que ` kube-controller-manager ` haga solicitudes ` GET
` o ` POST ` __ sin necesidad de controlar el cuerpo de la solicitud desde la
red de host de la instancia maestra. Esos tipos de volúmenes no se suelen
utilizar en GKE, así que un nuevo uso de cualquiera de ellos puede servir para
detectar un posible ataque.

Si se combina la vulnerabilidad con una forma de filtrar los resultados de la
solicitud ` GET/POST ` al atacante (por ejemplo, mediante registros), es
posible divulgar información sensible. Hemos actualizado los controladores de
almacenamiento afectados para reducir las posibilidades de que se produzcan
filtraciones.

|

Media

|

[ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**Publicación:** 01/06/2020  
Descripción  |  Gravedad  |  Notas  
---|---|---  
  
En Kubernetes, se ha descubierto una [ vulnerabilidad
](https://github.com/kubernetes/kubernetes/issues/91507) que permite que un
contenedor con privilegios redirija el tráfico de nodos a otro contenedor. El
tráfico TLS/SSH mutuo, como el que transcurre entre el kubelet y el servidor
de la API o el procedente de aplicaciones mediante mTLS, no se puede leer ni
modificar mediante este ataque. Esta vulnerabilidad afecta a todos los nodos
de Google Kubernetes Engine (GKE), así que te recomendamos que [ actualices
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es) a la versión más reciente del parche como se indica a
continuación.

####  ¿Qué debo hacer?

Para mitigar esta vulnerabilidad, [ actualiza
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es) primero tu plano de control y luego los nodos a una de las
versiones con parche que se indican a continuación. Los clústeres que usan
canales de versiones ya utilizan una versión con parche tanto en el plano de
control como en los nodos:

  * 1.14.10-gke.36 
  * 1.15.11-gke.15 
  * 1.16.8-gke.15 

Muy pocos contenedores suelen requerir ` CAP_NET_RAW ` . Esta y otras potentes
características deberían estar bloqueadas de forma predeterminada mediante [
PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-
to/pod-security-policies?hl=es) o [ Anthos Policy Controller
](https://cloud.google.com/anthos-config-management/docs/concepts/policy-
controller?hl=es) :

  * Inhabilita la característica ` CAP_NET_RAW ` de los contenedores: 
    * Haciendo obligatoria su inhabilitación mediante [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=es) con el siguiente código: 
        
                
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
        

    * O aplicando esta [ plantilla de restricción ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) de Anthos Policy Controller/Gatekeeper. Puedes hacerlo de esta forma: 
        
                
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
        

    * O actualizando las especificaciones de tu pod: 
        
                
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
        

####  ¿Qué vulnerabilidad trata este parche?

El parche mitiga la siguiente vulnerabilidad:

La vulnerabilidad que se describe en el [ error 91507 de Kubernetes
](https://github.com/kubernetes/kubernetes/issues/91507) con la característica
` CAP_NET_RAW ` (que se incluye en el conjunto de características
predeterminadas del contenedor) para configurar de forma malintencionada la
pila IPv6 del nodo y redirigir el tráfico al contenedor controlado por el
atacante. De esa forma, el atacante puede interceptar o modificar el tráfico
que se origine en el nodo o que lo tenga como destino. El tráfico TLS/SSH
mutuo, como el que transcurre entre el kubelet y el servidor de la API o el
procedente de aplicaciones mediante mTLS, no se puede leer ni modificar
mediante este ataque.

|

Media

|

[ Error 91507 de Kubernetes
](https://github.com/kubernetes/kubernetes/issues/91507)  
  
  
##  GCP-2020-005

**Publicación:** 07/05/2020  
**Última actualización:** 07/05/2020  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco se ha descubierto una vulnerabilidad en el kernel de Linux, descrita
en la [ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) , que permite usar el escape de
contenedores para obtener privilegios de raíz en el nodo del host.

Esta vulnerabilidad afecta a los nodos de Ubuntu en Google Kubernetes Engine
(GKE) que ejecuten la versión 1.16 o 1.17 de GKE. Por ello, recomendamos
actualizar cuanto antes a la versión más reciente del parche como se indica a
continuación.

No se ven afectados los nodos que ejecutan Container-Optimized OS (COS) ni los
que se ejecutan en GKE On-Prem.

####  ¿Qué debo hacer?

**En el caso de la mayor parte de los clientes, no es necesario realizar
ninguna otra acción. Solo se ven afectados los nodos que ejecutan Ubuntu en
las versiones 1.16 o 1.17 de GKE.**

Para actualizar tus nodos, primero debes actualizar tu instancia maestra a la
versión más reciente. Este parche estará disponible para Kubernetes
1.16.8-gke.12, 1.17.4-gke.10 y versiones posteriores. Consulta la
disponibilidad de estos parches en las [ notas de la versión
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=es) .

####  ¿Qué vulnerabilidad trata este parche?

Este parche mitiga la siguiente vulnerabilidad:

La [ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) describe una vulnerabilidad en la versión
5.5.0 y posteriores del kernel de Linux que permite que un contenedor
malicioso (con una interacción mínima del usuario en forma de un ejecutable)
lea y escriba la memoria del kernel y, de ese modo, pueda ejecutar código a
nivel raíz en el nodo del host. Se considera una vulnerabilidad de alta
gravedad.

|

Alta

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP-2020-003

**Publicación:** 31/03/2020  
**Última actualización:** 31/03/2020  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco se ha descubierto una vulnerabilidad en Kubernetes, descrita en la [
CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) , que permite que cualquier usuario
autorizado envíe solicitudes POST para ejecutar un ataque remoto de denegación
de servicio en un servidor de API de Kubernetes. El Comité de Seguridad de
Producto (PSC) de Kubernetes ha publicado [ información adicional sobre esta
vulnerabilidad ](https://groups.google.com/forum/?hl=es#!topic/kubernetes-
security-announce/wuwEwZigXBc) .

Los clústeres de GKE que usan [ redes maestras autorizadas
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=es) y [ clústeres privados sin punto de conexión público
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=es#private_master) mitigan esta vulnerabilidad.

####  ¿Qué debo hacer?

Te recomendamos que actualices tu clúster a una versión del parche que
contenga la mitigación a esta vulnerabilidad.

A continuación, se indican las versiones de parches que contienen la
mitigación:

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  ¿Qué vulnerabilidades trata este parche?

El parche mitiga una vulnerabilidad de denegación de servicio (DoS):

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)

|

Media

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**Publicación:** 23/03/2020  
**Última actualización:** 23/03/2020  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Kubernetes ha divulgado [ dos vulnerabilidades de denegación de servicio
](https://groups.google.com/forum/?hl=es#!topic/kubernetes-security-
announce/2UOlsba2g0s) : una afecta al servidor de APIs y la otra a los
kubelets. Si quieres obtener más información al respecto, consulta los
siguientes problemas de Kubernetes: [ 89377
](https://github.com/kubernetes/kubernetes/issues/89377) y [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) .

####  ¿Qué debo hacer?

En GKE, todos los usuarios están protegidos ante la vulnerabilidad
CVE-2020-8551, a menos que los usuarios que no son de confianza puedan enviar
solicitudes en la red interna del clúster. Si se utilizan [ redes maestras
autorizadas ](https://cloud.google.com/kubernetes-engine/docs/how-
to/authorized-networks?hl=es) , también se mitiga la vulnerabilidad
CVE-2020-8552.

####  ¿Cuándo se les aplicarán parches a estas vulnerabilidades?

Los parches para la CVE-2020-8551 requieren una actualización de nodos. A
continuación, se indican las versiones de parches que contendrán la
mitigación:

  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

Nota: Las versiones 1.14.x y todas las anteriores no se ven afectadas por esta
vulnerabilidad, por lo que no requieren parches.

Los parches para la CVE-2020-8552 requieren una actualización maestra. A
continuación, se indican las versiones de parches que contendrán la
mitigación:

  * 1.14.10-gke.32 
  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

|

Media

|

[ CVE-2020-8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE-2020-8552 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  21 de enero del 2020 (última actualización: 24 de enero del 2020)

**Publicación:** 21/01/2020  
**Última actualización:** 24/01/2020  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 24 de enero del 2020:** el proceso para que las versiones
parcheadas estén disponibles está aún en marcha y se completará el 25 de enero
del 2020.

* * *

Microsoft ha revelado una vulnerabilidad en la API de Windows Crypto y su
validación de firmas curvas elípticas. Para obtener más información, consulta
el [ aviso de Microsoft ](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) .

**¿Qué debo hacer?**

**En el caso de la mayor parte de los clientes, no es necesario realizar
ninguna otra acción. Solo afecta a los nodos que ejecutan Windows Server.**

En el caso de los clientes que usan nodos de Windows Server, los nodos y las
cargas de trabajo en contenedores que se ejecuten en dichos nodos deben
actualizarse a versiones parcheadas para reducir esa vulnerabilidad.

**Para actualizar los contenedores, realiza el siguiente procedimiento:**

Vuelve a compilar los contenedores mediante las últimas imágenes del
contenedor base de Microsoft. Para ello, selecciona una etiqueta [ servercore
](https://hub.docker.com/_/microsoft-windows-servercore) o [ nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) con una fecha de
última actualización de 14 de enero del 2020 o posterior.

**Para actualizar los nodos, realiza el siguiente procedimiento:**

El proceso de disponibilidad de las versiones parcheadas está aún en marcha y
se completará el 24 de enero del 2020.

Tendrás que esperar hasta esa fecha y actualizar el nodo a una versión de GKE
parcheada o usar Windows Update para desplegar manualmente el parche de
Windows más reciente en cualquier momento.

A continuación se indican las versiones de parches que contendrán la
mitigación:

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**¿Qué vulnerabilidades mitiga este parche?**

Este parche mitiga las siguientes vulnerabilidades:

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) : esta vulnerabilidad también se conoce
como [ vulnerabilidad de spoofing de la API de Windows Crypto
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) y se puede activar para que los archivos
ejecutables maliciosos parezcan de confianza o para permitir al atacante
realizar ataques de intermediario y descifrar información confidencial sobre
las conexiones de TLS en el software afectado.

|

Puntuación base de NVD: 8,1 (alta)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  14 de noviembre del 2019

**Publicación:** 14/11/2019  
**Última actualización:** 14/11/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
En Kubernetes, se ha descubierto un problema de seguridad en los contenedores
adicionales [ ` external-provisioner ` ](https://github.com/kubernetes-
csi/external-provisioner) , [ ` external-snapshotter `
](https://github.com/kubernetes-csi/external-snapshotter) y [ ` external-
resizer ` ](https://github.com/kubernetes-csi/external-resizer) de kubernetes-
csi que afecta a la mayoría de las versiones de los contenedores adicionales
incluidos en los [ controladores de Container Storage Interface (CSI)
](https://kubernetes-csi.github.io/docs/drivers.html) . Para obtener más
información, consulta el [ aviso
](https://github.com/kubernetes/kubernetes/issues/85233) que ha publicado
Kubernetes al respecto.

**¿Qué debo hacer?**  
**Esta vulnerabilidad no afecta a ningún componente de GKE gestionado** . Es
posible que te afecte si gestionas tus propios controladores de CSI en [
clústeres alfa de GKE ](https://cloud.google.com/kubernetes-
engine/docs/concepts/alpha-clusters?hl=es) con la versión 1.12 de GKE o una
posterior. Si tienes este problema, ponte en contacto con tu proveedor de
controladores de CSI para que te indique cómo llevar a cabo la actualización.

**¿Qué vulnerabilidades mitiga este parche?**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : esta CVE es una vulnerabilidad de los
contenedores adicionales ` kubernetes-csi ` [ ` external-provisioner `
](https://github.com/kubernetes-csi/external-provisioner) , [ ` external-
snapshotter ` ](https://github.com/kubernetes-csi/external-snapshotter) y [ `
external-resizer ` ](https://github.com/kubernetes-csi/external-resizer) que
puede permitir el acceso o la modificación de datos sin autorización. Esto
afecta a la mayoría de las versiones de contenedores adicionales incluidos en
[ controladores de CSI ](https://kubernetes-csi.github.io/docs/drivers.html) .

|

Media

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  12 de noviembre del 2019

**Publicación:** 12/11/2019  
**Última actualización:** 12/11/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Intel ha descubierto varias CVE que pueden permitir interacciones entre la
ejecución especulativa y el estado de microarquitectura para exponer datos.
Para obtener más información, consulta el [ aviso
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) que ha publicado Intel al respecto.

**La infraestructura del host que ejecuta Kubernetes Engine aísla las cargas
de trabajo de los clientes. No es necesario que tomes ninguna medida, salvo si
ejecutas código no fiable en tus propios clústeres de varios propietarios de
GKE __ y usas nodos N2, M2 o C2. ** Si usas instancias de GKE en nodos N1,
tampoco deberás tomar ninguna medida adicional.

Si utilizas GKE On‑Prem de Anthos, la exposición dependerá del hardware.
Compara tu infraestructura con la que se detalla en el [ aviso de Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

####  ¿Qué debo hacer?

**Esta situación te afectará únicamente si usas grupos de nodos N2, M2 o C2 __
y estos ejecutan código no fiable dentro de tus propios clústeres de varios
propietarios de GKE. **

**Reinicia los nodos para que se aplique el parche.** La forma más sencilla de
reiniciar todos los nodos de tu grupo de nodos es usar la operación de [
actualización ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=es#upgrade_nodes) . De este modo, se fuerza el
reinicio de todos los grupos de nodos afectados.  

Nota: No tienes que cambiar de versión durante una actualización. Puedes
iniciar una actualización a la misma versión de nodo con la marca ` cluster-
version ` .

####  ¿Qué vulnerabilidades trata este parche?

Este parche mitiga las siguientes vulnerabilidades:

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
: esta CVE también se denomina TSX Async Abort (TAA). TAA proporciona otra vía
para la filtración externa de datos usando las mismas estructuras de datos de
microarquitectura que fueron vulnerables ante el [ muestreo de datos de
microarquitectura (MDS) ](https://cloud.google.com/kubernetes-
engine/docs/security-bulletins?hl=es#may-14-2019) .

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
: es una vulnerabilidad de denegación de servicio (DoS) que afecta a los hosts
de máquinas virtuales y hace que un invitado malicioso provoque un fallo en un
host que no está protegido. Esta CVE también se denomina "Machine Check Error
on Page Size Change" (Error de comprobación de máquina al cambiar el tamaño de
página) y no afecta a GKE.

|

Media

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  22 de octubre del 2019

**Publicación:** 22/10/2019  
**Última actualización:** 22/10/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco se ha descubierto una vulnerabilidad en el lenguaje de programación
Go, descrita en la [ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) . Puede afectar a las configuraciones de
Kubernetes que usan un proxy de autenticación. Para obtener más información,
consulta el [ aviso
](https://groups.google.com/forum/?hl=es#!topic/kubernetes-security-
announce/PtsUCqFi4h4) que ha publicado Kubernetes al respecto.

Kubernetes Engine no permite configurar un proxy de autenticación, por lo que
no se ve afectado por esta vulnerabilidad.

|

Ninguna

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  16 de octubre del 2019

**Publicación:** 16/10/2019  
**Última actualización:** 24/10/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 24/10/2019:** Las versiones con parche ya están
disponibles en todas las zonas.

* * *

Hace poco se ha descubierto una vulnerabilidad en Kubernetes, descrita en la [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) , que permite que cualquier usuario
autorizado envíe solicitudes POST para ejecutar un ataque remoto de denegación
de servicio en un servidor de API de Kubernetes. El Comité de Seguridad de
Producto (PSC) de Kubernetes ha publicado [ información adicional sobre esta
vulnerabilidad ](https://groups.google.com/forum/?hl=es#!topic/kubernetes-
security-announce/jk8polzSUxs) .

Los clústeres de GKE que usan [ redes maestras autorizadas
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=es) y [ clústeres privados sin punto de conexión público
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=es#private_master) mitigan esta vulnerabilidad.

######  ¿Qué debo hacer?

Te recomendamos que actualices tu clúster en cuanto haya disponible una
versión del parche que contenga la corrección. Está previsto que el parche
esté disponible en todas las zonas con el lanzamiento de la versión de GKE
programado para la semana del 14 de octubre.

A continuación se indican las versiones de parches que contendrán la
mitigación:

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  ¿Qué vulnerabilidades trata este parche?

Este parche mitiga las siguientes vulnerabilidades:

La CVE-2019-11253 es una vulnerabilidad de denegación de servicio (DoS).

|

Alta

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  16 de septiembre del 2019

**Publicación:** 16/09/2019  
**Última actualización:** 16/10/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Este boletín se ha actualizado desde su publicación original.

Hace poco se han descubierto nuevas vulnerabilidades de denegación de servicio
(DoS) con el lenguaje de programación Go: las [ CVE-2019-9512
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9512) y [
CVE-2019-9514 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514)
. En GKE, estas vulnerabilidades podrían permitir que un usuario cree
solicitudes maliciosas que usen excesivamente la CPU en el servidor de API de
Kubernetes, lo que puede reducir la disponibilidad del plano de control del
clúster. Para obtener más información, consulta el [ aviso
](https://groups.google.com/forum/?hl=es#!topic/golang-announce/65QixT3tcmg)
del lenguaje de programación Go que se ha publicado al respecto.

######  ¿Qué debo hacer?

Te recomendamos que actualices el clúster a la versión más reciente del parche
en cuanto esté disponible, ya que contiene la mitigación de esta
vulnerabilidad. De acuerdo con el [ calendario de actualizaciones
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es#september_16_2019) , está previsto que el parche esté disponible
en todas las zonas con la próxima versión de GKE.

A continuación se indican las versiones de parches que contendrán la
mitigación:

  * **Actualización del 16 de octubre del 2019:** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  ¿Qué vulnerabilidad trata este parche?

Este parche mitiga las siguientes vulnerabilidades:

Las [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) y [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) son
vulnerabilidades de denegación de servicio (DoS).

|

Alta

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  5 de septiembre del 2019

**Publicación:** 05/09/2019  
**Última actualización:** 05/09/2019

Se ha actualizado el boletín sobre la corrección de la vulnerabilidad que se
publicó el  31 de mayo del 2019  .

##  22 de agosto del 2019

**Publicación:** 22/08/2019  
**Última actualización:** 22/08/2019

Se ha actualizado el boletín del  5 de agosto del 2019  . Ya está disponible [
la corrección de la vulnerabilidad que se mencionaba en el boletín anterior
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es#august_22_2019) .

##  8 de agosto del 2019

**Publicación:** 08/08/2019  
**Última actualización:** 08/08/2019

Se ha actualizado el boletín del  5 de agosto del 2019  . Está previsto que la
corrección de la vulnerabilidad incluida en dicho boletín esté disponible en
la próxima versión de GKE.

##  5 de agosto del 2019

**Publicación:** 05/08/2019  
**Última actualización:** 09/08/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Este boletín se ha actualizado desde su publicación original.

Hace poco se ha descubierto una vulnerabilidad en Kubernetes, la [
CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) , que permite que las instancias de [
recursos personalizados ](https://kubernetes.io/docs/concepts/extend-
kubernetes/api-extension/custom-resources/) con permiso de clúster se utilicen
como si fueran objetos espaciados por nombre en todos los espacios de nombres.
Esto quiere decir que las cuentas de usuario y de servicio que cuenten
únicamente con permisos para controlar el acceso basado en roles a nivel de
espacio de nombres pueden interactuar con recursos personalizados que tengan
permiso de clúster. Para que el atacante pueda aprovechar esta vulnerabilidad,
es necesario que cuente con privilegios para acceder al recurso en cualquier
espacio de nombres.

######  ¿Qué debo hacer?

Te recomendamos que [ actualices ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=es) tu clúster a la versión más
reciente del parche en cuanto esté disponible, ya que contiene la mitigación a
esta vulnerabilidad. Está previsto que el parche esté disponible en todas las
zonas con la próxima versión de GKE. A continuación se indican las versiones
de parches que contendrán la mitigación:

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ canal rápido ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=es) ) 

######  ¿Qué vulnerabilidad trata este parche?

El parche mitiga la siguiente vulnerabilidad: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Media

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  3 de julio del 2019

**Publicación:** 03/07/2019  
**Última actualización:** 03/07/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Ya hay disponible una versión con parche de ` kubectl ` con [ ` gcloud `
253.0.0 ](https://cloud.google.com/sdk/docs/release-
notes?hl=es#kubernetes_engine) para tratar la CVE-2019-11246. Consulta el
boletín de seguridad del 25 de junio del 2019  para obtener más información.

**Nota:** El parche no está disponible en ` kubectl ` 1.11.10.

|

Alta

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  3 de julio del 2019

**Publicación:** 25/06/2019  
**Última actualización:** 03/07/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
######  Actualización del 3 de julio del 2019

Cuando publicamos la última actualización, todavía no estaban disponibles los
parches de las versiones 1.11.9 y 1.11.10. Ya hemos lanzado la versión
1.11.10-gke.5 como actualización de ambas versiones 1.11.

En este momento, se han aplicado parches a las instancias maestras de GKE y la
infraestructura de Google que ejecuta Kubernetes Engine está protegida frente
a esta vulnerabilidad.

En poco tiempo, las instancias maestras 1.11 dejarán de estar disponibles y se
han programado actualizaciones automáticas a la versión 1.12 en la semana del
8 de julio del 2019. Puedes elegir cualquiera de las siguientes opciones para
obtener nodos con una versión con parche:

  * Actualiza los nodos a la versión 1.11.10-gke.5 a partir del 8 de julio del 2019. Después de esa fecha, se empezarán a eliminar las versiones 1.11 de la lista disponible de objetivos de actualización. 
  * Habilita las [ actualizaciones automáticas ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=es) en los nodos de la versión 1.11 y permite que puedan actualizarse a la versión 1.12 cuando lo hagan las instancias maestras. 
  * [ Actualiza manualmente ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=es) las instancias maestras y los nodos a una versión 1.12 corregida. 

El boletín original del 24 de junio del 2019 es el siguiente:

* * *

######  Actualización del 24 de junio del 2019

El 22 de junio del 2019 a las 21:40 (UTC), lanzamos las siguientes versiones
con parches de Kubernetes. Las instancias maestras entre las versiones de
Kubernetes 1.11.0 y 1.13.6 se actualizarán automáticamente a una versión con
parche. Si no estás ejecutando una versión compatible con este parche,
actualiza a una versión de instancia maestra compatible (se enumeran más
adelante) antes de actualizar tus nodos.

**Debido a la gravedad de estas vulnerabilidades, y tengas o no habilitadas
las actualizaciones automáticas de nodos, te recomendamos que[ actualices
manualmente ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=es) tus nodos e instancias maestras a una
de estas versiones en cuanto estén disponibles. **

Las versiones con parche:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

El boletín original del 18 de junio del 2019 es el siguiente:

* * *

Netflix ha divulgado hace poco tres vulnerabilidades de TCP en los kernels de
Linux:

  * [ CVE‑2019‑11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE‑2019‑11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE‑2019‑11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

A estas CVE se las conoce conjuntamente como [ NFLX‑2019‑001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) .

Es posible que los kernels de Linux sin parches sean vulnerables a un ataque
de denegación de servicio activado de forma remota. **Los nodos de Google
Kubernetes Engine que envían o reciben tráfico de redes no fiables se ven
afectados, así que te recomendamos que sigas estos pasos de mitigación para
proteger tus cargas de trabajo.**

######  Instancias maestras de Kubernetes

  * Las instancias maestras que utilizan [ redes autorizadas ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=es) para limitar el tráfico a la redes fiables no se ven afectadas. 

  * En los próximos días, se aplicará automáticamente el parche a las instancias maestras de los clústeres de GKE que gestiona Google. No hace falta que el cliente realice ninguna acción. 

######  Nodos de Kubernetes

Los nodos que limitan el tráfico a las redes fiables no se ven afectados. Se
trataría de clústeres con las siguientes características:

  * Nodos con cortafuegos que protegen frente a redes no fiables o que no tienen direcciones IP públicas ( [ clústeres privados ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=es) ). 
  * Clústeres sin servicios de tipo LoadBalancer públicos. 

Google está preparando una mitigación permanente de estas vulnerabilidades que
estará disponible en una nueva versión de nodo. Actualizaremos este boletín y
enviaremos un correo electrónico a todos los clientes de GKE cuando esté
disponible la corrección permanente.

Hasta entonces, hemos creado un DaemonSet de Kubernetes que modifica la
configuración de ` iptables ` del host para implementar las mitigaciones.

#####  ¿Qué debo hacer?

Ejecuta el siguiente comando para aplicar el DaemonSet de Kubernetes a todos
los nodos de tu clúster. De esta forma, se añade una regla ` iptables ` a las
reglas ` iptables ` actuales del nodo para mitigar la vulnerabilidad.
**Ejecuta el comando una vez por clúster en cada proyecto de Google Cloud.**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

No es necesario añadir ninguna regla ip6tables porque Ipv6 no es compatible
con GKE.

Una vez que haya disponible una versión del nodo con parche y hayas
actualizado todos los nodos que puedan haberse visto afectados, usa el
siguiente comando para eliminar el DaemonSet. **Ejecuta el comando una vez por
clúster en cada proyecto de Google Cloud.**

    
    
    
    kubectl delete -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

|  Alta  
Media  
Media  
|  [ CVE-2019-11477 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
  
  
##  25 de junio del 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 03/07/2019:** este parche está disponible en ` gcloud `
253.0.0 para ` kubectl ` 1.12.9, 1.13.6, 1.14.2 y versiones posteriores.

**Nota:** El parche no está disponible en la versión 1.11.10.

* * *

Hace poco se ha descubierto una vulnerabilidad en Kubernetes, la [
CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) , que permite que un atacante con acceso
a una operación ` kubectl cp ` y a la ejecución de código dentro de un
contenedor modifique archivos en el host. Es posible que esta vulnerabilidad
permita que un atacante sustituya o cree un archivo en el sistema de archivos
del host. Para obtener más información, consulta el [ aviso
](https://groups.google.com/forum/?hl=es#!topic/kubernetes-security-
announce/NLs2TGbfPdo) que ha publicado Kubernetes al respecto.

**Esta vulnerabilidad afecta a todas las versiones` gcloud ` de Google
Kubernetes Engine (GKE), así que te recomendamos actualizar a la versión más
reciente del parche de ` gcloud ` cuando esté disponible. ** Próximamente
habrá una versión del parche que incluya una mitigación de esta
vulnerabilidad.

######  ¿Qué debo hacer?

Habrá una versión con parche de ` kubectl ` disponible en una próxima versión
de ` gcloud ` . También puedes [ actualizar ` kubectl ` directamente
](https://kubernetes.io/docs/tasks/tools/install-kubectl/) por tu cuenta.

Consulta la disponibilidad de este parche en las [ notas de la versión de `
gcloud ` ](https://cloud.google.com/sdk/docs/release-notes?hl=es) .

######  ¿Qué vulnerabilidad trata este parche?

La vulnerabilidad [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) permite que un atacante con acceso a una
operación ` kubectl cp ` pueda ejecutar código dentro de un contenedor para
modificar archivos en el host. Es posible que esta vulnerabilidad permita que
un atacante sustituya o cree un archivo en el sistema de archivos del host.

|

Alta

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  18 de junio del 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco se ha descubierto una vulnerabilidad en Docker, la [ CVE-2018-15664
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-15664) , que permite
que un atacante que puede ejecutar código en un contenedor intercepte una
operación ` docker cp ` iniciada de forma externa. Es posible que esta
vulnerabilidad permita que un atacante cambie el lugar en el que se escribe un
archivo a una ubicación arbitraria en el sistema de archivos del host.

**Esta vulnerabilidad afecta a todos los nodos que ejecutan Docker en Google
Kubernetes Engine (GKE), así que te recomendamos actualizar a la versión más
reciente del parche cuando esté disponible. Próximamente habrá una versión del
parche que incluya una mitigación de esta vulnerabilidad.**

**Esta vulnerabilidad afecta a todas las instancias maestras que ejecutan
Docker en Google Kubernetes Engine (GKE) y que son anteriores a la versión
1.12.7.** En GKE, los usuarios no tienen acceso a ` docker cp ` en la
instancia maestra, por lo que el riesgo de esta vulnerabilidad se ve limitado
en las instancias maestras de este entorno.

#####  ¿Qué debo hacer?

Solo se ven afectados los nodos que ejecutan Docker y únicamente cuando se
emite un comando ` docker cp ` (o uno equivalente con una API) que pueda ser
interceptado. Se prevé que sea una situación bastante inusual en un entorno de
Kubernetes. No se ven afectados los nodos que ejecutan [ Container-Optimized
OS (COS) con containerd ](https://cloud.google.com/kubernetes-
engine/docs/concepts/using-containerd?hl=es) .

Para actualizar tus nodos, primero debes [ actualizar tus instancias maestras
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es#upgrading_the_cluster) a la versión con parche. Cuando el parche
esté disponible, podrás iniciar la actualización de la instancia maestra o
esperar a que Google lo haga automáticamente. Dicho parche se incluirá en
Docker 18.09.7 como parte de un próximo parche de GKE. **Este parche solo
estará disponible en GKE 1.13 y versiones posteriores.**

Actualizaremos automáticamente las instancias maestras del clúster a la
versión con parche según la programación habitual. También puedes iniciar la
actualización de las instancias maestras por tu cuenta cuando la versión con
parche esté disponible.

Actualizaremos este boletín cuando dispongamos de las versiones que contienen
un parche. Consulta la disponibilidad de estos parches en las [ notas de la
versión ](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=es)
.

#####  ¿Qué vulnerabilidad trata este parche?

Este parche mitiga la siguiente vulnerabilidad:

La vulnerabilidad [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) permite que un atacante que pueda
ejecutar código en un contenedor intercepte una operación ` docker cp `
iniciada de forma externa. Es posible que esta vulnerabilidad permita que un
atacante cambie el lugar en el que se ha escrito un archivo a una ubicación
arbitraria en el sistema de archivos del host.

|  Alta  |  
  
##  31 de mayo del 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Este boletín se ha actualizado desde su publicación original.

######  Actualización del 2 de agosto del 2019

Cuando se lanzó el boletín inicial, solo se veían afectadas las versiones de
la 1.13.6-gke.0 a la 1.13.6-gke.5. Debido a una regresión, ahora se ven
afectadas todas las versiones 1.13.6.x. Si utilizas la versión 1.13.6,
actualízala a la 1.13.7 cuanto antes.

El proyecto Kubernetes ha descubierto la [ CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) en kubelet v.
1.13.6 y v. 1.14.2, que puede provocar que los contenedores se ejecuten como
UID 0 (normalmente se asigna al usuario ` root ` ), aunque se haya
especificado un usuario diferente en la imagen de contenedor. **Si tus
contenedores se ejecutan como un usuario no raíz y utilizas una versión de
nodo entre la 1.13.6-gke.0 y la 1.13.6-gke.6, te recomendamos que establezcas`
RunAsUser ` en todos los pods del clúster cuyos contenedores no deberían
ejecutarse como UID 0. **

Si se especifica un valor de ` USER ` que no sea raíz (por ejemplo, si se
establece el valor de ` USER ` en un Dockerfile), se puede producir un
comportamiento inesperado. Cuando un contenedor se ejecuta por primera vez en
un nodo, respeta correctamente el UID especificado. No obstante, debido a este
defecto, en la segunda ejecución (y en las posteriores) el contenedor se
ejecuta como UID 0 independientemente del UID especificado. Se trata
normalmente de un privilegio de mayor prioridad no deseado, y puede conllevar
un comportamiento inesperado de la aplicación.

#####  ¿Cómo puedo saber si estoy utilizando una versión afectada?

Ejecuta el siguiente comando para enumerar todos los nodos y su versión de
kubelet:

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

Si el resultado muestra las versiones de kubelet que se indican a
continuación, eso significa que tus nodos se ven afectados:

  * v. 1.13.6 
  * v. 1.14.2 

#####  ¿Cómo puedo saber si mi configuración específica se ve afectada?

Si tus contenedores se ejecutan como un usuario no raíz y utilizas una versión
de nodo entre la 1.13.6-gke.0 y la 1.13.6-gke.6, tu configuración se verá
afectada salvo en los siguientes casos:

  * Los pods que especifican un valor no raíz válido para el PodSecurityContext de ` runAsUser ` no se ven afectados y siguen funcionando como estaba previsto. 
  * Los PodSecurityPolicies que aplican una configuración de ` runAsUser ` tampoco se ven afectados y siguen funcionando normalmente. 
  * Los pods que especifican ` mustRunAsNonRoot:true ` no se iniciarán como UID 0, pero no se podrán iniciar cuando se vean afectados por este problema. 

#####  ¿Qué debo hacer?

Establece el [ contexto de seguridad RunAsUser
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) en todos los pods del clúster que
no deban ejecutarse como UID 0. Usa un recurso [ PodSecurityPolicy
](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) para
aplicar esta configuración.

|  Media  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  14 de mayo del 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 11/06/2019:** el parche está disponible en las versiones
1.11.10-gke.4, 1.12.8-gke.6 y 1.13.6-gke.5 lanzadas la semana del 28/05/2019,
así como en las versiones posteriores.

Intel ha divulgado las siguientes CVE:

  * [ CVE‑2018‑12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE‑2018‑12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE‑2018‑12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE‑2019‑11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

A estas CVE se las conoce conjuntamente como muestreo de datos de
microarquitectura (MDS). Estas vulnerabilidades podrían permitir que los datos
se expusieran por medio de la interacción de la ejecución especulativa y el
estado de microarquitectura. Para obtener más información, consulta el [ aviso
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) que ha publicado Intel al respecto.

**La infraestructura del host que ejecuta Kubernetes Engine aísla las cargas
de trabajo de los clientes entre sí. No te afectará a menos que ejecutes
código no fiable en tus propios clústeres de varios propietarios de GKE.**

**Para los clientes que ejecuten código no fiable en sus propios servicios de
varios propietarios de Kubernetes Engine, se trata de una vulnerabilidad
considerablemente grave.** Para mitigarla en Kubernetes Engine, inhabilita
Hyper-Threading en tus nodos. Estas vulnerabilidades afectan únicamente a los
nodos que usan varias CPU en Google Kubernetes Engine (GKE). Ten en cuenta que
las máquinas virtuales n1-standard-1 (la predeterminada de GKE), g1-small y
f1-micro exponen únicamente 1 vCPU al entorno de invitado, de modo que no es
necesario inhabilitar Hyper-Threading.

Se incluirán protecciones adicionales que habiliten la funcionalidad de
vaciado en una próxima [ versión del parche
](https://cloud.google.com/kubernetes-engine/release-notes?hl=es) . En las
próximas semanas, actualizaremos las instancias maestras y los nodos a las
versiones con parche actualizadas automáticamente según la programación
habitual. **El parche no es suficiente por sí solo para mitigar la exposición
a esta vulnerabilidad. Consulta las siguientes acciones recomendadas.**

Si utilizas GKE On-Prem, la vulnerabilidad podría afectarte en función del
hardware que emplees. Consulta el [ aviso
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) que ha publicado Intel al respecto.

####  ¿Qué debo hacer?

**No te afectará a menos que ejecutes código no fiable en tus propios
clústeres de varios propietarios de GKE.**

**En el caso de los nodos de Kubernetes Engine, crea grupos de nodos con la
opción Hyper-Threading inhabilitada y reprograma tus cargas de trabajo en
ellos.**

Ten en cuenta que las máquinas virtuales n1-standard-1, g1-small y f1-micro
exponen 1 vCPU al entorno de invitado, de modo que no es necesario inhabilitar
Hyper-Threading.

**Advertencia:**

  * Inhabilitar Hyper-Threading podría afectar considerablemente al rendimiento de tus clústeres y tu aplicación. Asegúrate de que eso te parece bien antes de aplicar la medida en tus clústeres de producción. 
  * Hyper-Threading se puede inhabilitar a nivel de grupo de nodos de GKE desplegando un DaemonSet. No obstante, al desplegar dicho DaemonSet, todos los nodos del grupo de nodos se reiniciarán a la vez. Por tanto, te recomendamos que crees un grupo de nodos en tu clúster, despliegues el DaemonSet para inhabilitar Hyper-Threading en dicho grupo de nodos y, entonces, migres ahí tus cargas de trabajo. 

Para crear un grupo de nodos con Hyper-Threading inhabilitado:

  1. Crea un grupo de nodos en tu clúster con la etiqueta de nodo ` cloud.google.com/gke-smt-disabled=true ` : 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. Despliega el DaemonSet en el nuevo grupo de nodos. El DaemonSet se ejecutará solamente en los nodos con la etiqueta ` cloud.google.com/gke-smt-disabled=true ` . Inhabilitará Hyper-Threading y, a continuación, reiniciará el nodo. 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. Asegúrate de que los pods de DaemonSet están ejecutándose. 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

Deberías obtener una respuesta similar a esta:

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. Comprueba que aparece "SMT has been disabled" (Se ha inhabilitado SMT) en los registros de los pods. 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

Nota: Las opciones de arranque no se pueden modificar si el nodo tiene
habilitada la función [ Arranque seguro ](https://cloud.google.com/kubernetes-
engine/docs/how-to/shielded-gke-nodes?hl=es#secure_boot) . Si esta función
está habilitada, será necesario [ inhabilitarla
](https://cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-
nodes?hl=es#disabling) antes de crear el DaemonSet.

Debes mantener el DaemonSet en ejecución en los grupos de nodos para que los
cambios se apliquen automáticamente a los nodos que crees. Las creaciones de
nodos se pueden activar durante la actualización manual o automática de la
versión, la reparación automática y el autoescalado.

Para habilitar Hyper-Threading de nuevo, tendrás que volver a crear el grupo
de nodos sin desplegar el DaemonSet proporcionado y migrar ahí tus cargas de
trabajo.

También te recomendamos que actualices manualmente tus nodos cuando el parche
esté disponible. Antes de ello, deberás [ actualizar tu instancia maestra
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es#upgrading_the_cluster) a la versión más reciente. Las instancias
maestras de GKE se actualizarán automáticamente según la programación
habitual.

Actualizaremos este boletín con las versiones que contienen un parche en
cuanto estén disponibles.

####  ¿Qué vulnerabilidad trata este parche?

Este parche mitiga las siguientes vulnerabilidades:

Las [ CVE-2018-12126 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12126) , [ CVE-2018-12127
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127) , [
CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) y
[ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)
son vulnerabilidades que aprovechan la ejecución especulativa. A estas CVE se
las conoce conjuntamente como muestreo de datos de microarquitectura. Estas
vulnerabilidades podrían permitir que se expongan datos por medio de la
interacción de la ejecución especulativa y el estado de microarquitectura.  |
Media  |

  * [ CVE‑2018‑12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE‑2018‑12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE‑2018‑12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE‑2018‑11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  5 de abril del 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco se han descubierto las vulnerabilidades de seguridad [ CVE-2019-9900
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900) y [
CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)
en [ Envoy ](https://www.envoyproxy.io/) .

[ Istio ](https://istio.io/) inserta Envoy, y estas vulnerabilidades permiten
que se omita la política de Istio en algunos casos.

Si has habilitado Istio en Google Kubernetes Engine (GKE), puede que te
afecten estas vulnerabilidades. **Te recomendamos que actualices cuanto antes
los clústeres afectados a la versión más reciente del parche, así como tus
contenedores adicionales de Istio (las instrucciones se indican más abajo).**

####  ¿Qué debo hacer?

**Debido a la gravedad de estas vulnerabilidades, tanto si tienes nodos con la
actualización automática habilitada como si no, te recomendamos que sigas los
siguientes pasos:**

  1. **[ Actualiza manualmente ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=es) tu clúster en cuanto esté disponible el parche. **
  2. **Actualiza tus contenedores adicionales tal y como se indica en esta[ documentación ](https://istio.io/docs/setup/kubernetes/upgrade/steps/#sidecar-upgrade) . **

Las versiones con parche estarán disponibles en todos los proyectos de GKE
antes de las 19:00 (PDT) de hoy.

Este parche estará disponible en las versiones de GKE que se indican más
abajo. Los nuevos clústeres usarán la versión con parche de forma
predeterminada cuando se anuncie en la página de boletines de seguridad de
GKE, lo que está previsto para el 15 de abril del 2019. Si has creado un
clúster antes de esa fecha, deberás indicar la versión con parche que debe
utilizar. Para los clientes de GKE que tienen las [ actualizaciones
automáticas de los nodos ](https://cloud.google.com/kubernetes-
engine/docs/how-to/node-auto-upgrades?hl=es) habilitadas y no realicen la
actualización manualmente, sus nodos se actualizarán automáticamente a las
versiones con parche durante la semana siguiente.

Versiones con parche:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  ¿Qué vulnerabilidad trata este parche?

Este parche mitiga las siguientes vulnerabilidades:

Las [ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) y [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) . Puedes
obtener más información en el [ blog de Istio
](https://istio.io/blog/2019/announcing-1.1.2) .

|  Alta  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901. ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  1 de marzo del 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 22/03/2019:** este parche está disponible para Kubernetes
1.11.8-gke.4, 1.13.4-gke.1 y versiones posteriores. El parche aún no está
disponible en la versión 1.12. Consulta la disponibilidad de estos parches en
las [ notas de la versión ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=es#march_19_2019) .

Hace poco se ha descubierto una nueva vulnerabilidad de denegación de servicio
en Kubernetes, la [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) , que permite que un usuario autorizado
para enviar solicitudes de parche cree solicitudes "json-patch" maliciosas que
consumen excesivamente la CPU y la memoria en el servidor de API de
Kubernetes, lo que puede reducir la disponibilidad del plano de control del
clúster. Para obtener más información, consulta el [ aviso
](https://groups.google.com/forum/?hl=es#!topic/kubernetes-
announce/vmUUNkYfG9g) que ha publicado Kubernetes al respecto. **Las
vulnerabilidades anteriores afectan a todas las instancias maestras de Google
Kubernetes Engine (GKE). Próximamente habrá una versión del parche que incluya
una mitigación de esta vulnerabilidad. En las próximas semanas, actualizaremos
automáticamente las instancias maestras del clúster a la versión con parche
según la programación habitual.**

####  ¿Qué debo hacer?

**No tienes que hacer nada. Las instancias maestras de GKE se actualizarán
automáticamente según la programación habitual.** Si quieres actualizar tu
instancia maestra con antelación, puedes [ iniciar manualmente una
actualización maestra ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=es#upgrading_the_cluster) .

Actualizaremos este boletín con las versiones que contengan un parche. Ten en
cuenta que el parche solo estará disponible en las versiones 1.11+, pero no en
las versiones 1.10.

####  ¿Qué vulnerabilidad trata este parche?

Este parche mitiga la siguiente vulnerabilidad:

La vulnerabilidad [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) permite que un usuario cree
especialmente un parche de tipo "json-patch" que consume excesivamente la CPU
en el servidor de API de Kubernetes, lo que puede reducir la disponibilidad
del plano de control del clúster.

|  Media  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  11 de febrero del 2019 (runc)

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
La Open Containers Initiative (OCI) [ ha descubierto hace poco
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=es#!topic/dev/Tc1ELm-8oDI)
una nueva vulnerabilidad de seguridad en runc, la [ CVE-2019-5736
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736) , que permite
usar el escape de contenedores para obtener privilegios de raíz en el nodo del
host.

**Estas vulnerabilidades afectan a tus nodos de Ubuntu en Google Kubernetes
Engine (GKE), así que te recomendamos[ actualizar
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es) cuanto antes a la versión más reciente del parche como se
indica a continuación. **

####  ¿Qué debo hacer?

Para actualizar tus nodos, primero debes actualizar tu instancia maestra a la
versión más reciente. Este parche está disponible para Kubernetes
1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4, 1.12.5-gke.5 y versiones
posteriores. Consulta la disponibilidad de estos parches en las [ notas de la
versión ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es#february-11-2019) .

Ten en cuenta que solamente se ven afectados los nodos de Ubuntu en GKE. Los
nodos que ejecutan COS no se ven afectados.

Ten en cuenta que en la nueva versión de runc ha aumentado el uso de memoria,
por lo que es posible que debas actualizar la memoria asignada a los
contenedores si has establecido los límites de memoria en un nivel bajo (menos
de 16 MB).

####  ¿Qué vulnerabilidad trata este parche?

Este parche mitiga la siguiente vulnerabilidad:

La [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) describe una vulnerabilidad en runc que
permite que un contenedor malicioso (con una interacción mínima del usuario en
forma de un ejecutable) sobrescriba el binario runc del host y, de este modo,
pueda ejecutar código a nivel raíz en el nodo del host. No se ven afectados
los contenedores que se ejecutan como raíz. Se considera una vulnerabilidad de
alta gravedad.

|  Alta  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  11 de febrero del 2019 (Go)

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 25/02/2019:** el parche no está disponible en 1.11.7-gke.4
como se había anunciado anteriormente. Si utilizas la versión 1.11.7, puedes
cambiar a la versión inferior 1.11.6, actualizar a la versión 1.12 o esperar
hasta que esté disponible el próximo parche de 1.11.7 la semana del
04/03/2019.

Hace poco se ha descubierto una nueva vulnerabilidad de seguridad en el
lenguaje de programación Go, la [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486) . Se trata de una vulnerabilidad de
denegación de servicio (DoS) en las implementaciones de criptografía de curva
elíptica de las curvas elípticas P-521 y P-384. En Google Kubernetes Engine
(GKE), esta podría permitir que un usuario cree solicitudes maliciosas que
consumen excesivamente la CPU en el servidor de API de Kubernetes, lo que
puede reducir la disponibilidad del plano de control del clúster. Para saber
más, consulta el [ aviso
](https://groups.google.com/forum/?hl=es#!topic/golang-announce/mVeX35iXuSw)
sobre el lenguaje de programación Go que se ha publicado al respecto.

**Las vulnerabilidades anteriores afectan a todas las instancias maestras de
Google Kubernetes Engine (GKE). Habrá una[ nueva versión del parche
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es#february-11-2019) que incluya una mitigación para esta
vulnerabilidad. En las próximas semanas, actualizaremos automáticamente las
instancias maestras del clúster a la versión con parche según la programación
habitual. **

####  ¿Qué debo hacer?

**No tienes que hacer nada. Las instancias maestras de GKE se actualizarán
automáticamente según la programación habitual.** Si quieres actualizar tu
instancia maestra con antelación, puedes [ iniciar manualmente una
actualización maestra ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=es#upgrading_the_cluster) .

Este parche está disponible en GKE 1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4,
1.12.5-gke.5 y versiones posteriores.

####  ¿Qué vulnerabilidad trata este parche?

Este parche mitiga la siguiente vulnerabilidad:

La CVE-2019-6486 es una vulnerabilidad en las implementaciones de criptografía
de curva elíptica de las curvas elípticas P-521 y P-384. Permite que un
usuario cree entradas que consumen excesivamente la CPU.

|  Alta  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  3 de diciembre del 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
En los últimos días, se ha encontrado una nueva vulnerabilidad en la seguridad
de Kubernetes, la [ CVE‑2018‑1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) , por la que usuarios con privilegios
de un nivel relativamente bajo pueden saltarse la autorización de las API de
kubelet. En consecuencia, pueden ejecutar operaciones arbitrarias para
cualquier pod y en cualquier nodo del clúster. Para obtener más información,
consulta el [ aviso
](https://groups.google.com/forum/?hl=es#!topic/kubernetes-
announce/GVllWCg6L88) que ha publicado Kubernetes al respecto. **Las
vulnerabilidades anteriores han afectado a todas las instancias maestras en
Google Kubernetes Engine (GKE) y ya hemos actualizado los clústeres a la[
versión más reciente del parche ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=es#november-12-2018) . No tienes que hacer nada.
**

####  ¿Qué debo hacer?

**No tienes que hacer nada. Ya hemos actualizado las instancias maestras de
GKE.**

El parche está disponible en GKE 1.9.7‑gke.11, 1.10.6‑gke.11, 1.10.7‑gke.11,
1.10.9‑gke.5 y 1.11.2‑gke.18, así como en las últimas versiones.

####  ¿Qué vulnerabilidad trata este parche?

Este parche mitiga la siguiente vulnerabilidad:

La vulnerabilidad CVE-2018-1002105 permite que un usuario con privilegios de
un nivel relativamente bajo pueda saltarse la autorización de las API de
kubelet. Como consecuencia, puede enviar solicitudes de actualización de mayor
prioridad y realizar llamadas arbitrarias a cualquier API de kubelet. Se
considera una vulnerabilidad crítica en Kubernetes. Sin embargo, se ha
considerado una vulnerabilidad alta porque algunos detalles de la
implementación de GKE impidieron escalar sin autenticar.

|  Alta  |  [ CVE‑2018‑1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  13 de noviembre del 2018

Descripción  
---  
  
**Actualización del 16/11/2018:** Se ha completado la revocación y rotación de
todos los tokens que podrían haberse visto afectados. No hace falta que hagas
nada más.

Recientemente, Google descubrió un problema en el complemento Container
Network Interface (CNI) de Calico que puede incluir información sensible en
los registros con algunas configuraciones. El seguimiento de este problema lo
está realizando Tigera Technical Advisory [ TTA‑2018‑001
](https://www.projectcalico.org/security-bulletins/) .

  * Al ejecutar el complemento CNI de Calico con el registro de nivel de depuración, este escribe la configuración del cliente de la API de Kubernetes en los registros. 
  * El complemento CNI de Calico también escribe el token de la API de Kubernetes en los registros de nivel de información si el campo "k8s_auth_token" se ha establecido en la configuración de red de CNI. 
  * Además, al ejecutarse con el registro de nivel de depuración, si se establece de forma explícita el token de la cuenta de servicio, ya sea en el archivo de configuración de Calico leído por Calico o como variables del entorno usadas por Calico, los componentes de Calico (calico/nodo, felix, CNI) escriben esta información en los archivos de registro. 

Estos tokens tienen los siguientes permisos:  
      
    
    
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
  
Los clústeres de Google Kubernetes Engine con una política de red de clúster y
Stackdriver Logging habilitado han registrado tokens de cuenta de servicio de
Calico en Stackdriver. Los clústeres que no tienen habilitada la política de
red no se han visto afectados.

Hemos implementado una solución que migra el complemento CNI de Calico para
que solo acceda en el nivel de advertencia y utilice una nueva cuenta de
servicio. El código de Calico con el parche se implementará en una versión
posterior.

Durante la próxima semana, llevaremos a cabo una revocación progresiva de
todos los tokens que puedan estar afectados. Este boletín se actualizará
cuando se haya completado la revocación. **No hace falta que hagas nada más.**
(Esta rotación se completó el 16/11/2018).

Si quieres rotar estos tokens de forma inmediata, puedes ejecutar el siguiente
comando; el nuevo secreto correspondiente a la cuenta de servicio debería
volver a crearse automáticamente en unos segundos:  
  
kubectl get sa --namespace kube-system calico -o template --template '{{(index
.secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system  
---  
  
####  Detección

GKE registra todos los accesos al servidor de la API. Para saber si se utilizó
un token de Calico fuera del intervalo de IPs esperado de Google Cloud, puedes
ejecutar la siguiente consulta de Stackdriver. Solo se mostrarán los registros
de llamadas realizadas desde fuera de la red de Google Cloud Platform (GCP) y
te recomendamos que la personalices según las necesidades de tu entorno
específico.  
  
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
  
##  14 de agosto del 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
[ Intel ha divulgado ](https://www.intel.com/content/www/us/en/architecture-
and-technology/l1tf.html) las siguientes CVE:

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (para [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE‑2018‑3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (para sistemas operativos y [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) ) 
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

####  Impacto en Google Kubernetes Engine

La infraestructura que ejecuta Kubernetes Engine y aísla los nodos y clústeres
del cliente entre sí está protegida frente a ataques conocidos.

Los grupos de nodos de Kubernetes Engine que utilizan una imagen de
Container‑Optimized OS de Google y tienen habilitada la [ actualización
automática ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=es) se actualizarán automáticamente a las versiones con
parche de nuestra imagen de COS tan pronto como estén disponibles a partir de
la semana del 20/08/2018.

Los grupos de nodos de Kubernetes Engine que no tengan habilitada la [
actualización automática ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=es) deberán [ actualizarse
manualmente ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=es) cuando las versiones con parche de
nuestra imagen de COS estén disponibles.

|  Alta  |

  * [ CVE‑2018‑3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE‑2018‑3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE‑2018‑3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  6 de agosto del 2018 (última actualización: 5 de septiembre del 2018)

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Actualización del 05/09/2018

La [ CVE‑2018‑5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) se divulgó recientemente. Al igual que la
[ CVE‑2018‑5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) , se trata de una vulnerabilidad de la red
a nivel del kernel que aumenta la efectividad de los ataques de denegación de
servicio (DoS) contra sistemas vulnerables. La principal diferencia de la
CVE‑2018‑5391 es que puede realizarse a través de conexiones IP. Actualizamos
este boletín para que abarque ambas vulnerabilidades.

####  Descripción

La [ CVE‑2018‑5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") describe una
vulnerabilidad de la red a nivel del kernel que aumenta la efectividad de los
ataques de denegación de servicio (DoS) contra sistemas vulnerables a través
de conexiones TCP.

La [ CVE‑2018‑5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") describe una
vulnerabilidad de la red a nivel del kernel que aumenta la efectividad de los
ataques de denegación de servicio (DoS) contra sistemas vulnerables a través
de conexiones IP.

####  Impacto en Google Kubernetes Engine

Desde el 11/08/2018, todas las instancias maestras de Kubernetes Engine están
protegidas contra ambas vulnerabilidades. Además, todos los clústeres de
Kubernetes Engine configurados para actualizarse automáticamente están
protegidos contra ambas vulnerabilidades. No obstante, estas afectan a los
grupos de nodos de Kubernetes Engine que no estén configurados para [
actualizarse automáticamente ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=es) y que se hayan actualizado
manualmente por última vez antes del 11/08/2018.

####  Versiones con parche

Debido a la gravedad de esta vulnerabilidad, te recomendamos que [ actualices
manualmente ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=es#upgrading-nodes) tus nodos en cuanto esté
disponible el parche.

|  Alta  |

  * [ CVE‑2018‑5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE‑2018‑5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  30 de mayo del 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco se descubrió una vulnerabilidad en Git que podría permitir la
elevación de privilegios en Kubernetes si los usuarios sin privilegios
obtienen permisos para crear pods con volúmenes gitRepo. La CVE se identifica
con la etiqueta [ CVE‑2018‑11235 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-11235) .

####  ¿Me afecta esta vulnerabilidad?

Esta vulnerabilidad te afecta si todas estas afirmaciones se aplican a tu
caso:

  * Los usuarios que no son de confianza pueden crear pods (o activar su creación). 
  * Los pods creados por usuarios que no son de confianza tienen restricciones que impiden el acceso raíz al host (por ejemplo, mediante [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=es) ). 
  * Los pods creados por usuarios que no son de confianza pueden usar el tipo de volumen gitRepo. 

Todos los nodos de Kubernetes Engine son vulnerables.

####  ¿Qué debo hacer?

Prohibir el uso del tipo de volumen gitRepo. Para prohibir los volúmenes
gitRepo con PodSecurityPolicy, quita ` gitRepo ` de la lista blanca ` volumes
` de tu PodSecurityPolicy.

Es posible tener un comportamiento equivalente al volumen gitRepo si se clona
un repositorio de Git en un volumen EmptyDir desde un initContainer:

    
    
    
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

####  ¿Qué parche trata esta vulnerabilidad?

Se incluirá un parche en una futura versión de Kubernetes Engine. Vuelve a
visitar los boletines de seguridad próximamente para obtener más información.

|  Media  |

  * [ CVE‑2018‑11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  21 de mayo del 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Recientemente, se descubrieron diferentes vulnerabilidades en el kernel de
Linux que podrían permitir la elevación de privilegios o la denegación de
servicio (mediante el fallo del kernel) desde un proceso sin privilegios.
Estas CVE se identifican con las etiquetas [ CVE‑2018‑1000199
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199) , [
CVE‑2018‑8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
y [ CVE‑2018‑1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) . Estas vulnerabilidades afectan a todos
los nodos de Kubernetes Engine, por lo que te recomendamos [ actualizar
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=es) a la versión más reciente del parche como se indica a
continuación.

####  ¿Qué debo hacer?

En primer lugar, debes actualizar tu instancia maestra a la versión más
reciente. El parche está disponible en Kubernetes Engine 1.8.12‑gke.1,
Kubernetes Engine 1.9.7‑gke.1 y Kubernetes Engine 1.10.2‑gke.1. Estas
versiones incluyen parches para imágenes de Container‑Optimized OS y Ubuntu.

Si creas un clúster antes, tendrás que especificar la versión con parche que
debe usar. A los clientes que tengan habilitadas las [ actualizaciones de nodo
automáticas ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=es) y no actualicen manualmente se les actualizarán los nodos
a las versiones con parche en las próximas semanas.

####  ¿Qué vulnerabilidades trata este parche?

Este parche mitiga las siguientes vulnerabilidades:

[ CVE‑2018‑1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : esta vulnerabilidad afecta al kernel
de Linux. Permite que un usuario o proceso sin privilegios cause un fallo en
el kernel del sistema, lo que provoca un ataque DoS o una apropiación de
privilegios. Se considera una vulnerabilidad alta, con una puntuación de 7,8
en el sistema CVSS.

[ CVE‑2018‑8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : esta vulnerabilidad afecta al kernel de
Linux. Permite que un usuario o proceso sin privilegios cause un fallo en el
kernel del sistema, lo que provoca un ataque DoS. Se considera una
vulnerabilidad media, con una puntuación de 6,5 en el sistema CVSS.

[ CVE‑2018‑1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : esta vulnerabilidad afecta al hipervisor
KVM del kernel de Linux. Permite que un proceso sin privilegios cause un fallo
en el kernel invitado o que pueda adquirir privilegios. La vulnerabilidad
tiene un parche en la infraestructura sobre la que se ejecuta Kubernetes
Engine, por lo que este no se ve afectado. Se considera una vulnerabilidad
alta, con una puntuación de 8,0 en el sistema CVSS.

|  Alta  |

  * [ CVE‑2018‑1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE‑2018‑8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE‑2018‑1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  12 de marzo del 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco [ se han descubierto las nuevas vulnerabilidades de seguridad
](https://groups.google.com/forum/?hl=es#!topic/kubernetes-security-
announce/P7lBjbjDKd8) en Kubernetes [ CVE‑2017‑1002101
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) y [
CVE‑2017‑1002102 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002102) , que permiten que los contenedores accedan
a archivos externos. Todos los nodos de Kubernetes Engine se ven afectados por
estas vulnerabilidades, así que te recomendamos actualizar cuanto antes a la
versión más reciente del parche como se indica a continuación.

####  ¿Qué debo hacer?

Debido a la gravedad de estas vulnerabilidades, tengas o no habilitadas las
actualizaciones automáticas de nodos, te recomendamos que [ actualices
manualmente ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=es) tus nodos en cuanto esté disponible el
parche. De acuerdo con el [ calendario de actualizaciones
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es#march-12-2018) , este parche estará disponible para todos los
clientes a partir del 16 de marzo, pero es posible que lo tengas antes a tu
disposición en función de la zona en la que se encuentre tu clúster.

En primer lugar, debes actualizar tu instancia maestra a la versión más
reciente. Este parche estará disponible en Kubernetes 1.9.4‑gke.1, Kubernetes
1.8.9‑gke.1 y Kubernetes 1.7.14‑gke.1. Los nuevos clústeres usarán la versión
con parche de forma predeterminada antes del 30 de marzo; si creas un clúster
nuevo antes, tendrás que especificar la versión con parche que debe usar.

A los clientes de Kubernetes Engine que tengan habilitadas las [
actualizaciones automáticas de nodos ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=es) y no actualicen manualmente se
les actualizarán los nodos a las versiones con parche antes del 23 de abril.
Sin embargo, debido a la gravedad de estas vulnerabilidades, te recomendamos
que [ actualices manualmente ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=es) tus nodos en cuanto
esté disponible el parche.

####  ¿Qué vulnerabilidades trata este parche?

Este parche mitiga las dos vulnerabilidades siguientes:

La vulnerabilidad CVE‑2017‑1002101 permite que los contenedores que usan
activaciones de volumen [ subPath
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) tengan
acceso a archivos externos al volumen. Por tanto, si estás bloqueando el
acceso de los contenedores a volúmenes hostPath con PodSecurityPolicy, un
atacante con la capacidad para actualizar o crear pods puede activar cualquier
hostPath con cualquier otro tipo de volumen.

La vulnerabilidad CVE‑2017‑1002102 permite que los contenedores que usan
determinados tipos de volúmenes (incluidos los secretos, mapas de
configuración, volúmenes proyectados o volúmenes de la API Downward) borren
archivos externos al volumen. Por tanto, si se vulnera un contenedor que
utiliza uno de estos tipos de volúmenes o si permites que usuarios que no son
de confianza creen pods, un atacante podría usar ese contenedor para borrar
archivos al azar en el host.

Para obtener más información sobre la solución, consulta la [ entrada del blog
de Kubernetes ](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-
vulnerability/) .

|  Alta  |

  * [ CVE‑2017‑1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE‑2017‑1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

