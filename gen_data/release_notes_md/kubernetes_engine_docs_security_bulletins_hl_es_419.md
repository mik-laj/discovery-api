#  Boletines de seguridad

Todos los boletines de seguridad de Google Kubernetes Engine (GKE) se
describen en este tema.

Las vulnerabilidades se suelen mantener en secreto y no se las puede divulgar
hasta que las partes afectadas hayan tenido la oportunidad de tratar el tema.
En estos casos, las [ notas de la versión
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=es_419) de
GKE tratan sobre “actualizaciones de seguridad” hasta que se apruebe la
divulgación. En ese momento, las notas se actualizarán para reflejar la
vulnerabilidad tratada en el parche.

**Nota:** Si ejecutas cargas de trabajo de instancias múltiples en GKE, presta
especial atención a estos boletines. Es más probable que estas
vulnerabilidades afecten a cargas de trabajo de instancias múltiples. A fin de
obtener una descripción técnica de los límites de seguridad en GKE y para
conocer el efecto que tienen en las cargas de trabajo, consulta [ Isolation at
different layers of the Kubernetes stack (Aislamiento en diferentes capas de
la pila de Kubernetes)
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Para recibir los boletines de seguridad más recientes, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) o agrega
directamente la URL del feed: ` https://cloud.google.com/feeds/kubernetes-
engine-security-bulletins.xml ` .

##  GCP-2020-007

**Fecha de publicación:** 1 de junio de 2020  
Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Recientemente se descubrió en Kubernetes una vulnerabilidad de falsificación
de solicitudes del servidor (SSRF), [ descrita en CVE-2020-8555
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555) , que permitía
a ciertos usuarios autorizados filtrar hasta 500 bytes de información sensible
desde la red host del plano de control. En el plano de control de Google
Kubernetes Engine (GKE), se usan controladores de Kubernetes a los que afecta
esta vulnerabilidad. Te recomendamos [ actualizar
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=es_419) el plano de control a la versión más reciente del
parche, como se muestra a continuación. No es necesario actualizar el nodo.  

####  ¿Qué debo hacer?

La mayoría de los clientes no debe realizar ninguna acción adicional. En la
gran mayoría de los clústeres ya se está ejecutando la versión con el parche.
Las siguientes versiones de GKE o las posteriores a ellas incluyen la
corrección para esta vulnerabilidad:

  * 1.14.7-gke.39 
  * 1.14.8-gke.32 
  * 1.14.9-gke.17 
  * 1.14.10-gke.12 
  * 1.15.7-gke.17 
  * 1.16.4-gke.21 
  * 1.17.0-gke.0 

Los clústeres que usan [ canales de versiones
](https://cloud.google.com/kubernetes-engine/docs/concepts/release-
channels?hl=es_419) ya están en las versiones del plano de control que tiene
la mitigación.

####  ¿Qué vulnerabilidad corrige este parche?

Estos parches mitigan la vulnerabilidad CVE-2020-8555. Esta tiene una
calificación de vulnerabilidad media para GKE, ya que fue difícil aprovecharla
debido a las medidas de endurecimiento del plano de control.

Un atacante con permisos para crear un Pod con ciertos tipos de volúmenes
incluidos (GlusterFS, Quobyte, StorageFS, ScaleIO) o con permisos para crear
un StorageClass puede hacer que ` kube-controller-manager ` cree solicitudes `
GET ` o ` POST ` _sin_ un cuerpo de solicitud que controle el atacante desde
la red de host de la instancia principal. En GKE rara vez se usan estos tipos
de volúmenes, por lo que un uso nuevo de ellos puede ser un indicador de
detección útil.

Combinados con un medio para que el atacante reciba los resultados filtrados
del ` GET/POST ` (como los registros), puede provocar que se divulgue
información sensible. Actualizamos los controladores de almacenamiento en
cuestión para evitar la posibilidad de que ocurran tales fugas.

|

Media

|

[ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**Fecha de publicación:** 1 de junio de 2020  
Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Kubernetes divulgó una [ vulnerabilidad
](https://github.com/kubernetes/kubernetes/issues/91507) que permite que un
contenedor con privilegios redireccione el tráfico de nodos a otro contenedor.
El ataque no permite leer ni modificar el tráfico mutuo de TLS/SSH, como aquel
entre el kubelet y el servidor de la API, o el tráfico desde aplicaciones
mediante mTLS. Esta vulnerabilidad afecta a todos los nodos de Google
Kubernetes Engine (GKE). Te recomendamos [ actualizar
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es_419) a la versión más reciente del parche, como se muestra a
continuación.

####  ¿Qué debo hacer?

Para mitigar esta vulnerabilidad, [ actualiza
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es_419) tu plano de control y, luego, tus nodos a una de las
versiones con el parche que se mencionan a continuación. Los clústeres en los
canales de versiones ya ejecutan una versión con el parche en el plano de
control y los nodos:

  * 1.14.10-gke.36 
  * 1.15.11-gke.15 
  * 1.16.8-gke.15 

Por lo general, muy pocos contenedores requieren ` CAP_NET_RAW ` . Esta y
otras capacidades potentes se deben bloquear de forma predeterminada mediante
[ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-
to/pod-security-policies?hl=es_419) o el [ Controlador de políticas de Anthos
](https://cloud.google.com/anthos-config-management/docs/concepts/policy-
controller?hl=es_419) :

  * Descarta la capacidad ` CAP_NET_RAW ` de los contenedores: 
    * Aplícalo mediante [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=es_419) con la siguiente plantilla: 
        
                
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
        

    * O mediante el controlador o el guardián de políticas de Anthos con esta [ plantilla de restricciones ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) y aplicando, por ejemplo, lo siguiente: 
        
                
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
        

    * O actualiza las especificaciones del pod: 
        
                
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
        

####  ¿Qué vulnerabilidad corrige este parche?

El parche mitiga las siguientes vulnerabilidades:

La vulnerabilidad descrita en el [ problema 91507 de Kubernetes
](https://github.com/kubernetes/kubernetes/issues/91507) : la capacidad `
CAP_NET_RAW ` (que se incluye en el conjunto de capacidades del contenedor
predeterminado) por configurar de forma maliciosa la pila de IPv6 en el nodo y
redireccionar el tráfico del nodo al contenedor que controla el atacante. Esto
permitirá que el atacante intercepte o modifique el tráfico que se origina en
el nodo o que se destina a este. El ataque no permite leer ni modificar el
tráfico mutuo de TLS/SSH, como entre el kubelet y el servidor de la API, o el
tráfico de aplicaciones con mTLS.

|

Media

|

[ Problema 91507 de Kubernetes
](https://github.com/kubernetes/kubernetes/issues/91507)  
  
  
##  GCP‑2020‑005

**Fecha de publicación:** 7/05/2020  
**Última actualización:** 7/05/2020  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco, se descubrió una vulnerabilidad en el kernel de Linux, descrita en
[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) , que permite obtener privilegios de
administrador en el nodo host mediante un escape de contenedor.

Esta vulnerabilidad afecta a los nodos de Google Kubernetes Engine (GKE) de
Ubuntu que se ejecutan en GKE 1.16 o 1.17, por lo que te recomendamos
actualizar a la versión de parche más reciente lo antes posible, como se
muestra a continuación.

Los nodos que ejecutan Container-Optimized OS no se ven afectados. Los nodos
que se ejecutan en GKE On-Prem tampoco se ven afectados.

####  ¿Qué debo hacer?

**La mayoría de los clientes no debe realizar ninguna acción adicional. Solo
se ven afectados los nodos que ejecutan Ubuntu en la versión 1.16 o 1.17 de
GKE.**

Para poder actualizar los nodos, primero debes actualizar la instancia
principal a la versión más reciente. Este parche estará disponible en
Kubernetes 1.16.8-gke.12, 1.17.4-gke.10 y en versiones más recientes. Haz un
seguimiento de la disponibilidad de estos parches en las [ notas de la versión
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=es_419) .

####  ¿Qué vulnerabilidad corrige este parche?

Este parche mitiga la siguiente vulnerabilidad:

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) es una vulnerabilidad en la versión 5.5.0
y posteriores del kernel de Linux que permite que un contenedor malicioso (con
una interacción mínima del usuario mediante un ejecutable) lea y escriba en la
memoria del kernel para lograr la ejecución de código con permisos de
administrador en el nodo host. Esta vulnerabilidad de seguridad tiene una
calificación de gravedad alta.

|

Alta

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP‑2020‑003

**Fecha de publicación:** 31/03/2020  
**Última actualización:** 31/03/2020  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco, se descubrió una vulnerabilidad en Kubernetes, descrita en [
CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) , que permite que cualquier usuario con
autorización para realizar solicitudes POST ejecute un ataque de denegación
del servicio de forma remota en un servidor de la API de Kubernetes. El Comité
de seguridad de productos (PSC) de Kubernetes publicó información adicional
sobre esta vulnerabilidad, que puedes encontrar [ aquí
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-security-
announce/wuwEwZigXBc) .

Los clústeres de GKE que usan [ redes autorizadas para instancias principales
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=es_419) y [ clústeres privados sin extremo público
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=es_419#private_master) mitigan esta vulnerabilidad.

####  ¿Qué debo hacer?

Te recomendamos que actualices el clúster a una versión de parche que incluya
la corrección para esta vulnerabilidad.

Estas son las versiones de parche que incluyen la corrección:

  * 1.13.12‑gke.29 
  * 1.14.9‑gke.27 
  * 1.14.10‑gke.24 
  * 1.15.9‑gke.20 
  * 1.16.6‑gke.1 

####  ¿Qué vulnerabilidades corrige este parche?

El parche corrige la siguiente vulnerabilidad de denegación del servicio
(DoS):

[ CVE‑2019‑11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)

|

Media

|

[ CVE‑2019‑11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP‑2020‑002

**Fecha de publicación:** 23/03/2020  
**Fecha de actualización:** 23/03/2020  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Kubernetes divulgó [ dos vulnerabilidades de denegación del servicio
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-security-
announce/2UOlsba2g0s) : una que afecta al servidor de la API y otra que afecta
a Kubelets. Para conocer más detalles, consulta los problemas de Kubernetes [
89377 ](https://github.com/kubernetes/kubernetes/issues/89377) y [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) .

####  ¿Qué debo hacer?

Todos los usuarios de GKE están protegidos contra la vulnerabilidad
CVE‑2020‑8551, excepto en los casos en que se permita que usuarios no
confiables puedan enviar solicitudes en la red interna del clúster. El uso de
[ redes autorizadas para instancias principales
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=es_419) también brinda protección contra la vulnerabilidad
CVE‑2020‑8552.

####  ¿Cuándo se aplicarán parches para corregir estas vulnerabilidades?

Los parches para CVE‑2020‑8551 requieren actualizar los nodos. Estas son las
versiones de parche que incluirán la mitigación:

  * 1.15.10‑gke.* 
  * 1.16.7‑gke.* 

Nota: Las versiones 1.14.x y anteriores no se ven afectadas por esta
vulnerabilidad, por lo que no necesitan parches.

Los parches para CVE‑2020‑8552 requieren actualizar las instancias
principales. Estas son las versiones de parche que incluirán la mitigación:

  * 1.14.10‑gke.32 
  * 1.15.10‑gke.* 
  * 1.16.7‑gke.* 

|

Media

|

[ CVE‑2020‑8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE‑2020‑8552 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  21 de enero de 2020 (última actualización: 24 de enero de 2020)

**Fecha de publicación:** 21/01/2020  
**Última actualización:** 24/01/2020  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 24/01/2020:** El proceso para que las versiones con parche
estén disponibles ya se está llevando a cabo y se completará el 25 de enero de
2020.

* * *

Microsoft divulgó una vulnerabilidad en la API de Windows Crypto y la
validación de las firmas de curva elíptica. Si deseas obtener más información,
puedes consultar el [ aviso de Microsoft
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) al respecto.

**¿Qué debo hacer?**

**La mayoría de los clientes no debe realizar ninguna acción adicional. Solo
los nodos que se ejecutan en Windows Server se ven afectados.**

Para mitigar la vulnerabilidad, los clientes que usan nodos en Windows Server
deben actualizar los nodos y las cargas de trabajo en contenedores que se
ejecutan en esos nodos a las versiones con parche.

**Para actualizar los contenedores, sigue estos pasos:**

Vuelve a compilar tus contenedores con las imágenes base de contenedor de
Microsoft más actuales. Para ello, debes seleccionar una etiqueta [ servercore
](https://hub.docker.com/_/microsoft-windows-servercore) o [ nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) cuya última fecha de
actualización sea el 14/01/2020 o posterior.

**Actualización de nodos:**

El proceso para que las versiones de parche estén disponibles ya se está
llevando a cabo y se completará el 24 de enero de 2020.

Puedes esperar hasta esa fecha y actualizar el nodo a una versión de GKE con
parche o puedes usar Windows Update en cualquier momento para implementar el
último parche de Windows de forma manual.

Estas son las versiones con parche que contendrán la mitigación:

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**¿Qué vulnerabilidades corrige este parche?**

Este parche mitiga las siguientes vulnerabilidades:

[ CVE‑2020‑0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) : Esta vulnerabilidad también se conoce
como la [ Windows Crypto API Spoofing Vulnerability (Vulnerabilidad de
falsificación de identidad de la API de Windows Crypto)
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) y se puede usar para que los archivos
ejecutables maliciosos parezcan confiables o a fin de permitir que el atacante
realice ataques de intermediario y desencripte información confidencial sobre
las conexiones TLS del software afectado.

|

Puntuación base de la NVD: 8.1 (alta)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  14 de noviembre de 2019

**Fecha de publicación:** 14/11/2019  
**Última actualización:** 14/11/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Kubernetes divulgó un problema de seguridad de los archivos adicionales de
kubernetes-csi [ ` external-provisioner ` ](https://github.com/kubernetes-
csi/external-provisioner) , [ ` external-snapshotter `
](https://github.com/kubernetes-csi/external-snapshotter) y [ ` external-
resizer ` ](https://github.com/kubernetes-csi/external-resizer) , que afecta a
la mayoría de las versiones de los archivos adicionales en paquetes de [
controladores de Container Storage Interface (CSI) ](https://kubernetes-
csi.github.io/docs/drivers.html) . Para obtener más detalles, consulta la [
divulgación de Kubernetes
](https://github.com/kubernetes/kubernetes/issues/85233) .

**¿Qué debo hacer?**  
**Esta vulnerabilidad no afecta a ningún componente administrado de GKE** . Es
posible que te veas afectado si administras tus propios controladores de CSI
en los [ clústeres Alfa de GKE ](https://cloud.google.com/kubernetes-
engine/docs/concepts/alpha-clusters?hl=es_419) que ejecutan la versión de GKE
1.12 o posteriores. Si te ves afectado, consulta con tu proveedor de
controladores de CSI para obtener instrucciones de actualización.

**¿Qué vulnerabilidades corrige este parche?**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : Esta CVE es una vulnerabilidad de los
archivos adicionales [ ` external-provisioner `
](https://github.com/kubernetes-csi/external-provisioner) , [ ` external-
snapshotter ` ](https://github.com/kubernetes-csi/external-snapshotter) y [ `
external-resizer ` ](https://github.com/kubernetes-csi/external-resizer) de `
kubernetes-csi ` , que pueden permitir el acceso a datos de volumen o su
mutación no autorizados. Esta afecta a la mayoría de las versiones de los
archivos adicionales en paquetes de [ controladores de CSI
](https://kubernetes-csi.github.io/docs/drivers.html) .

|

Media

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  12 de noviembre de 2019

**Fecha de publicación:** 12/11/2019  
**Última actualización:** 12/11/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Intel divulgó las CVE que podrían permitir las interacciones entre la
ejecución especulativa y el estado de microarquitectura para exponer datos.
Para obtener más detalles, consulta la [ divulgación de Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

**La infraestructura de host que ejecuta Kubernetes Engine aísla las cargas de
trabajo del cliente. A menos que ejecutes código no confiable dentro de tus
propios clústeres de GKE de instancias múltiples _y_ uses nodos N2, M2 o C2,
no será necesario que realices ninguna acción. ** En el caso de las instancias
de GKE en los nodos N1, no se requiere ninguna otra acción.

Si ejecutas Anthos GKE On‑Prem, el nivel de exposición dependerá del hardware.
Compara tu infraestructura con la [ divulgación de Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

####  ¿Qué debo hacer?

**Solo te verás afectado si usas grupos de nodos con nodos N2, M2 o C2 _y_
estos ejecutan código no confiable dentro de tus propios clústeres de GKE de
instancias múltiples. **

**Reiniciar los nodos aplica el parche.** La manera más sencilla de reiniciar
todos los nodos de tu grupo de nodos es usar la operación de [ actualización
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es_419#upgrade_nodes) para forzar un reinicio en todos los grupos
de nodos afectados.  

Nota: No es necesario que cambies las versiones durante una actualización.
Puedes iniciar una actualización a la misma versión de nodo con la marca `
cluster-version ` .

####  ¿Qué vulnerabilidades corrige este parche?

Este parche mitiga las siguientes vulnerabilidades:

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
: Esta CVE también se conoce como TSX Async Abort (TAA). TAA proporciona otra
forma de robo de datos mediante las mismas estructuras de datos de
microarquitectura que aprovechó [ el muestreo de datos de microarquitectura
(MDS) ](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins?hl=es_419#may-14-2019) .

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
: Se trata de una vulnerabilidad de denegación del servicio (DoS) que afecta a
los hosts de máquinas virtuales, ya que permite que un invitado malicioso haga
fallar un host sin protección. Esta CVE también se conoce como “Error de
verificación de máquina en el cambio de tamaño de página”. No afecta a GKE.

|

Media

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  22 de octubre de 2019

**Fecha de publicación:** 22/10/2019  
**Última actualización:** 22/10/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco tiempo, se descubrió una vulnerabilidad en el lenguaje de
programación Go y se describió en [ CVE-2019-16276
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16276) . Esta
vulnerabilidad podría afectar a las configuraciones de Kubernetes que usan un
proxy de autenticación. Para obtener más detalles, consulta la [ divulgación
de Kubernetes ](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-
security-announce/PtsUCqFi4h4) .

Kubernetes Engine no permite la configuración de un proxy de autenticación,
por lo que esta vulnerabilidad no lo afecta.

|

Ninguna

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  16 de octubre de 2019

**Fecha de publicación:** 16/10/2019  
**Última actualización:** 24/10/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 24/10/2019:** Las versiones con parche ahora están
disponibles en todas las zonas.

* * *

Hace poco tiempo, se descubrió una vulnerabilidad en Kubernetes, descrita en [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) , que permite que cualquier usuario
autorizado haga solicitudes POST para ejecutar un ataque a distancia de
denegación del servicio en un servidor de la API de Kubernetes. El Product
Security Committee (PSC) de Kubernetes publicó información adicional sobre
esta vulnerabilidad, que puedes encontrar [ aquí
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-security-
announce/jk8polzSUxs) .

Los clústeres de GKE que usan [ redes autorizadas para instancias principales
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=es_419) y [ clústeres privados sin extremo público
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=es_419#private_master) mitigan esta vulnerabilidad.

######  ¿Qué debo hacer?

Te recomendamos actualizar tu clúster a una versión de parche que contenga la
corrección en cuanto esté disponible. Esperamos que esté disponibles en todas
las zonas con la actualización de GKE planificada para la semana del 14 de
octubre.

Las versiones de parche que contendrán la mitigación son las siguientes:

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  ¿Qué vulnerabilidades corrige este parche?

Este parche mitiga las siguientes vulnerabilidades:

CVE-2019-11253 es una vulnerabilidad de denegación del servicio (DoS).

|

Alta

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  16 de septiembre de 2019

**Fecha de publicación:** 16/09/2019  
**Última actualización:** 16/10/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Este boletín se actualizó desde su publicación original.

Hace poco tiempo, se descubrieron vulnerabilidades de seguridad nuevas en el
lenguaje de programación Go: [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) y [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) , que son
vulnerabilidades de denegación del servicio (DoS). En GKE, esta vulnerabilidad
podría permitir que un usuario cree solicitudes malintencionadas que consuman
cantidades excesivas de CPU en el servidor de la API de Kubernetes, lo que
podría reducir la disponibilidad del plano de control de los clústeres. Para
obtener más detalles, consulta la [ divulgación del lenguaje de programación
Go ](https://groups.google.com/forum/?hl=es_419#!topic/golang-
announce/65QixT3tcmg) .

######  ¿Qué debo hacer?

Te recomendamos actualizar tu clúster a la versión más reciente del parche,
que contenga la mitigación para esta vulnerabilidad en cuanto esté disponible.
Esperamos que esté disponibles en todas las zonas con la próxima actualización
de GKE, según el [ programa de actualización
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#september_16_2019) .

Las versiones de parche que contendrán la mitigación son las siguientes:

  * **Actualización del 16 de octubre de 2019:** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  ¿Qué vulnerabilidad corrige este parche?

Este parche mitiga las siguientes vulnerabilidades:

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) y [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) son
vulnerabilidades de denegación del servicio (DoS).

|

Alta

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  5 de septiembre de 2019

**Fecha de publicación:** 5/09/2019  
**Última actualización:** 5/09/2019

Se actualizó el boletín de la corrección de la vulnerabilidad que se documentó
en la edición del  31 de mayo de 2019  .

##  22 de agosto de 2019

**Fecha de publicación:** 22/08/2019  
**Última actualización:** 22/08/2019

Se actualizó el boletín del  5 de agosto de 2019  . La corrección de la
vulnerabilidad documentada en el boletín anterior está [ disponible
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#august_22_2019) .

##  8 de agosto de 2019

**Fecha de publicación:** 8/08/2019  
**Última actualización:** 8/08/2019

Se actualizó el boletín del  5 de agosto de 2019  . Esperamos que la
corrección de la vulnerabilidad que se documentó en ese boletín esté
disponible en la próxima actualización de GKE.

##  5 de agosto de 2019

**Fecha de publicación:** 5/08/2019  
**Última actualización:** 9/08/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Este boletín se actualizó desde su publicación original.

Hace poco tiempo, se descubrió una vulnerabilidad en Kubernetes, [
CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) , que permite que se actúe sobre
instancias de [ recursos personalizados
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) de alcance de clúster como si fueran objetos con espacio de
nombres existentes en todos los espacios de nombres. Esto significa que las
cuentas de usuario y de servicio solo deben contar con permisos de RBAC a
nivel de espacio de nombres para interactuar con recursos personalizados de
alcance de clúster. A fin de aprovechar esta vulnerabilidad, el atacante debe
tener privilegios para acceder al recurso en cualquier espacio de nombres.

######  ¿Qué debo hacer?

Te recomendamos que [ actualices ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=es_419) el clúster a la versión más
reciente del parche, que contiene la mitigación para esta vulnerabilidad, en
cuanto esté disponible. Esperamos que esté disponible en todas las zonas con
la próxima actualización de GKE. Las versiones de parche que contendrán la
mitigación se mencionan a continuación:

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ Canal rápido ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=es_419) ) 

######  ¿Qué vulnerabilidad corrige este parche?

El parche mitiga la siguiente vulnerabilidad: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Media

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  3 de julio de 2019

**Fecha de publicación:** 3/07/2019  
**Última actualización:** 3/07/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Ya está disponible una versión con parche de ` kubectl ` para abordar la
CVE-2019-11246, con [ ` gcloud ` 253.0.0
](https://cloud.google.com/sdk/docs/release-notes?hl=es_419#kubernetes_engine)
. Consulta el  boletín de seguridad del 25 de junio de 2019  para obtener más
información.

**Nota:** El parche no está disponible en ` kubectl ` 1.11.10.

|

Alta

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  3 de julio de 2019

**Fecha de publicación:** 25/06/2019  
**Última actualización:** 3/07/2019  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
######  Actualización del 3 de julio de 2019

Al momento de nuestra última actualización, los parches de las versiones
1.11.9 y 1.11.10 no estaban disponibles. Ahora lanzamos la versión
1.11.10-gke.5 como una asignación de actualización para ambas versiones 1.11.

Por el momento, las instancias principales de GKE cuentan con el parche, y la
infraestructura de Google que ejecuta Kubernetes Engine, además de contar con
el parche, está protegida de esta vulnerabilidad.

Las instancias principales de 1.11 pronto quedarán obsoletas y están
programadas para actualizarse de forma automática a la versión 1.12 durante la
semana del 8 de julio de 2019. Puedes elegir cualquiera de las siguientes
acciones sugeridas para actualizar los nodos a una versión con parche:

  * Realiza la actualización de nodos a la versión 1.11.10-gke.5 antes del 8 de julio de 2019. Después de esta fecha, se comenzará a quitar las versiones 1.11 de la lista disponible de asignaciones de actualización. 
  * Habilita las [ actualizaciones automáticas ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=es_419) en los nodos 1.11 y permíteles actualizarse cuando las instancias principales se actualicen a la versión 1.12. 
  * [ Actualiza de forma manual ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=es_419) las instancias principales y los nodos a una versión 1.12 fija. 

El boletín original del 24 de junio de 2019 es el siguiente:

* * *

######  Actualización del 24 de junio de 2019

Desde el 22/06/2019 a las 09:40 p.m. (UTC), están disponibles las versiones de
Kubernetes con parche que se indican más abajo. Las instancias principales
entre las versiones 1.11.0 y 1.13.6 de Kubernetes se actualizarán de forma
automática a una versión con parche. Si no ejecutas una versión compatible con
este parche, actualiza a una versión de instancia principal compatible (que se
mencionan a continuación) antes de actualizar tus nodos.

**Debido a la gravedad de estas vulnerabilidades, ya sea que tengas habilitada
o no la actualización automática de nodos, te recomendamos que[ actualices de
forma manual ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=es_419) los nodos y las instancias
principales a una de estas versiones cuanto antes. **

Las versiones con parche son las siguientes:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

El boletín original del 18 de junio de 2019 es el siguiente:

* * *

Hace poco tiempo, Netflix divulgó tres vulnerabilidades de TCP de los kernels
de Linux:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Estas CVE se conocen en conjunto como [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) .

Los kernels de Linux sin parche pueden ser vulnerables a un ataque activado a
distancia de denegación del servicio. **Los nodos de Google Kubernetes Engine
que envían o reciben tráfico de red no confiable se ven afectados, por lo que
te recomendamos seguir los pasos de mitigación que aparecen a continuación
para proteger tus cargas de trabajo.**

######  Instancias principales de Kubernetes

  * Las instancias principales de Kubernetes que usan [ redes autorizadas ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=es_419) para limitar el tráfico a redes confiables no se ven afectadas. 

  * Las instancias principales de los clústeres de GKE, que administra Google, obtendrán el parche de manera automática en los próximos días. No se requiere que el cliente realice ninguna acción. 

######  Nodos de Kubernetes

Los nodos que limitan el tráfico a redes confiables no se ven afectados. Esto
se refiere a un clúster con lo siguiente:

  * Los nodos con firewall para redes no confiables o sin IP públicas ( [ clústeres privados ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=es_419) ) 
  * Clústeres sin servicios públicos de LoadBalancer 

Google prepara una mitigación permanente para estas vulnerabilidades que
estará disponible como una versión nueva de nodo. Actualizaremos este boletín
y enviaremos un correo electrónico a todos los clientes de GKE cuando la
corrección permanente esté disponible.

Mientras esperamos por la corrección permanente, creamos un DaemonSet de
Kubernetes que implementa mitigaciones mediante la modificación de la
configuración de ` iptables ` del host.

#####  ¿Qué debo hacer?

Aplica el DaemonSet de Kubernetes a todos los nodos de tu clúster; para ello,
ejecuta el comando de más abajo. Esta acción agrega una regla de ` iptables `
a las reglas de ` iptables ` existentes en el nodo para mitigar la
vulnerabilidad. **Ejecuta el comando una vez por clúster por proyecto de
Google Cloud.**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

Debido a que IPv6 no es compatible con GKE, no se requiere ninguna regla de
ip6tables.

Una vez que una versión de nodo con parche esté disponible y hayas actualizado
todos los nodos potencialmente afectados, podrás quitar el DaemonSet con el
comando que se indica a continuación. **Ejecútalo una vez por clúster por
proyecto de Google Cloud.**

    
    
    
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
  
  
##  25 de junio de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 03/07/2019:** Este parche está disponible en ` gcloud `
253.0.0, para las versiones 1.12.9, 1.13.6, 1.14.2 y más recientes de `
kubectl ` .

**Nota:** El parche no está disponible en 1.11.10.

* * *

Hace poco tiempo, se descubrió una vulnerabilidad en Kubernetes, [
CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) , que permite que un atacante con acceso
a una operación de ` kubectl cp ` y ejecución de código dentro de un
contenedor modifique los archivos en el host. Esta vulnerabilidad podría
permitir que los atacantes reemplacen o creen archivos en el sistema de
archivos del host. Para obtener más detalles, consulta la [ divulgación de
Kubernetes ](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-
security-announce/NLs2TGbfPdo) .

**Todas las versiones de` gcloud ` de Google Kubernetes Engine (GKE) se ven
afectadas por esta vulnerabilidad, por lo que te recomendamos que actualices a
la versión más reciente del parche de ` gcloud ` cuando esté disponible. **
Una próxima versión de parche incluirá una mitigación para esta
vulnerabilidad.

######  ¿Qué debo hacer?

Habrá una versión de parche de ` kubectl ` disponible en una próxima
actualización de ` gcloud ` . También puedes [ actualizar ` kubectl `
directamente ](https://kubernetes.io/docs/tasks/tools/install-kubectl/) por tu
cuenta.

Haz un seguimiento de la disponibilidad de este parche en las [ notas de la
versión de ` gcloud ` ](https://cloud.google.com/sdk/docs/release-
notes?hl=es_419) .

######  ¿Qué vulnerabilidad corrige este parche?

La vulnerabilidad [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) permite que un atacante con acceso a una
operación de ` kubectl cp ` y a la ejecución de código dentro de un contenedor
modifique los archivos del host. Esta vulnerabilidad podría permitir que los
atacantes reemplacen o creen archivos en el sistema de archivos del host.

|

Alta

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  18 de junio de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco tiempo, se descubrió una vulnerabilidad en Docker, [ CVE-2018-15664
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-15664) , que permite
que un atacante que puede ejecutar código dentro de un contenedor usurpe una
operación de ` docker cp ` iniciada de forma externa. Esta vulnerabilidad
podría permitir que un atacante cambie la ubicación en la que se escribe un
archivo a una ubicación arbitraria en el sistema de archivos del host.

**Todos los nodos de Google Kubernetes Engine (GKE) que ejecutan Docker se ven
afectados por esta vulnerabilidad, por lo que te recomendamos que actualices a
la versión más reciente del parche cuando esté disponible. Una próxima versión
del parche incluirá una mitigación para esta vulnerabilidad.**

**Las instancias principales de Google Kubernetes Engine (GKE) más antiguas
que la versión 1.12.7 ejecutan Docker y se ven afectadas por esta
vulnerabilidad.** En GKE, los usuarios no tienen acceso a ` docker cp ` en la
instancia principal, por lo que el riesgo de esta vulnerabilidad es limitado
en las instancias principales de GKE.

#####  ¿Qué debo hacer?

Solo los nodos que ejecutan Docker se ven afectados y solo cuando se emite un
comando ` docker cp ` (o equivalente de API) que puede usurparse. Se espera
que esta situación sea bastante inusual en los entornos de Kubernetes. Los
nodos que ejecutan [ COS con containerd ](https://cloud.google.com/kubernetes-
engine/docs/concepts/using-containerd?hl=es_419) no se ven afectados.

Con el fin de actualizar tus nodos, primero debes [ actualizar tu instancia
principal ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-
a-cluster?hl=es_419#upgrading_the_cluster) a la versión con parche. Cuando el
parche esté disponible, podrás iniciar una actualización de instancia
principal o esperar que Google la actualice de manera automática. El parche
estará disponible en Docker 18.09.7, que se incluye en un próximo parche de
GKE. **Este parche solo estará disponible para la versión 1.13 de GKE y
posteriores.**

Actualizaremos las instancias principales del clúster a la versión con parche
de manera automática, a la frecuencia de actualización habitual. También
puedes iniciar una actualización de instancias principales por tu cuenta
después de que esté disponible la versión con parche.

Actualizaremos este boletín con las versiones que contienen un parche una vez
que estén disponibles. Haz un seguimiento de la disponibilidad de estos
parches en las [ notas de la versión ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=es_419) .

#####  ¿Qué vulnerabilidad corrige este parche?

Este parche mitiga la siguiente vulnerabilidad:

La vulnerabilidad [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) permite que un atacante que puede
ejecutar código dentro de un contenedor usurpe una operación ` docker cp `
iniciada de forma externa. Esta vulnerabilidad podría permitir que un atacante
cambie la ubicación en la que se escribe un archivo a una ubicación arbitraria
en el sistema de archivos del host.

|  Alta  |  
  
##  31 de mayo de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Este boletín se actualizó desde su publicación original.

######  Actualización del 2 de agosto de 2019

Al momento del boletín inicial, solo las versiones de 1.13.6-gke.0 a
1.13.6-gke.5 se vieron afectadas. Debido a una regresión, todas las versiones
1.13.6.x ahora se ven afectadas. Si ejecutas la versión 1.13.6, actualiza a
1.13.7 cuanto antes.

El proyecto de Kubernetes divulgó la vulnerabilidad [ CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) en los kubelet
v1.13.6 y v1.14.2, que puede hacer que los contenedores se ejecuten como UID 0
(en general, mapea al usuario ` root ` ), incluso si se especifica un usuario
diferente en la imagen del contenedor. **Si tus contenedores se ejecutan como
un usuario diferente del usuario raíz y ejecutas una versión de nodo de
1.13.6-gke.0 a 1.13.6-gke.6, te recomendamos que configures` RunAsUser ` en
todos los pods del clúster cuyos contenedores no deban ejecutarse como UID 0.
**

Si se especifica un valor de ` USER ` distinto del usuario raíz (por ejemplo,
mediante la configuración del valor de ` USER ` en un Dockerfile), se produce
un comportamiento inesperado. Cuando un contenedor se ejecuta por primera vez
en un nodo, este respetará el UID especificado de forma correcta. Sin embargo,
debido a este defecto, la segunda vez que se ejecuta (y las posteriores), el
contenedor se ejecuta como UID 0 sin considerar el UID que se especificó. Por
lo general, este es un privilegio elevado no deseado y puede conllevar un
comportamiento imprevisto de las aplicaciones.

#####  ¿Cómo puedo saber si ejecuto una versión afectada?

Ejecuta el siguiente comando para crear una lista de todos los nodos y sus
versiones de kubelet:

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

Si el resultado menciona las versiones de kubelet incluidas abajo, tus nodos
se ven afectados:

  * v1.13.6 
  * v1.14.2 

#####  ¿Cómo puedo saber si mi configuración específica se ve afectada?

Si tus contenedores se ejecutan como un usuario distinto del usuario raíz y
ejecutas las versiones de nodo de 1.13.6-gke.0 a 1.13.6-gke.6, te verás
afectado, excepto en los siguientes casos:

  * Los pods que especifican un valor que es válido y que no es raíz para el PodSecurityContext de ` runAsUser ` no se ven afectados y siguen funcionando según lo previsto. 
  * Las PodSecurityPolicies que aplican una configuración de ` runAsUser ` tampoco se ven afectadas y siguen funcionando según lo previsto. 
  * Los pods que especifican ` mustRunAsNonRoot:true ` no se iniciarán como UID 0, pero no podrán iniciarse cuando los afecte este problema. 

#####  ¿Qué debo hacer?

Configura el [ contexto de seguridad RunAsUser
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) en todos los pods del clúster que
no deberían ejecutarse como UID 0. Puedes aplicar esta configuración con una [
PodSecurityPolicy ](https://kubernetes.io/docs/concepts/policy/pod-security-
policy/) .

|  Media  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  14 de mayo de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 11/06/2019:** El parche está disponible en las versiones
1.11.10-gke.4, 1.12.8-gke.6 y 1.13.6-gke.5 actualizadas durante la semana del
28/05/2019 y en versiones más recientes.

Intel divulgó las siguientes CVE:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Estas CVE se conocen en conjunto como Muestreo de datos de microarquitectura
(MDS). Estas vulnerabilidades pueden hacer que los datos se expongan cuando la
ejecución especulativa interactúa con el estado de la microarquitectura. Para
obtener más detalles, consulta la [ divulgación de Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) .

**La infraestructura del host que ejecuta Kubernetes Engine aísla las cargas
de trabajo del cliente entre sí. A menos que ejecutes código no confiable
dentro de tus propios clústeres de GKE de instancias múltiples, no te verás
afectado.**

**En el caso de los clientes que ejecutan código no confiable en sus propios
servicios de instancias múltiples dentro de Kubernetes Engine, esta representa
una vulnerabilidad muy grave.** Para mitigarla en Kubernetes Engine, debes
inhabilitar los hipersubprocesos en tus nodos. Solo los nodos de Google
Kubernetes Engine (GKE) que usan varias CPU se ven afectados por estas
vulnerabilidades. Ten en cuenta que las VM n1-standard-1 (la predeterminada de
GKE), g1-small y f1-micro solo exponen 1 CPU virtual al entorno de invitado,
de modo que no es necesario inhabilitar los hipersubprocesos.

Se incluirán protecciones adicionales para habilitar la funcionalidad de
vaciado en la próxima [ versión de parche
](https://cloud.google.com/kubernetes-engine/release-notes?hl=es_419) .
Actualizaremos las instancias principales y los nodos con la actualización
automática a la versión con parche en las próximas semanas, a la frecuencia de
actualización habitual. **Tener solo el parche no es suficiente para mitigar
la exposición a esta vulnerabilidad. Consulta la información que aparece a
continuación para conocer las acciones recomendadas.**

Si ejecutas GKE On-Prem, es posible que te veas afectado dependiendo del
hardware que uses. Consulta la [ divulgación de Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) .

####  ¿Qué debo hacer?

**A menos que ejecutes código no confiable dentro de tus propios clústeres de
GKE de instancias múltiples, no te verás afectado.**

**En el caso de los nodos de Kubernetes Engine, crea grupos de nodos nuevos
con los hipersubprocesos inhabilitados y vuelve a programar las cargas de
trabajo en los nodos nuevos.**

Ten en cuenta que las VM n1-standard-1, g1-small y f1-micro solo exponen 1 CPU
virtual al entorno de invitado, de modo que no es necesario inhabilitar los
hipersubprocesos.

**Advertencia:**

  * La inhabilitación de los hipersubprocesos puede tener un impacto grave en el rendimiento de tus clústeres y la aplicación. Asegúrate de que esto es aceptable antes de implementar esta opción en tus clústeres de producción. 
  * Los hipersubprocesos se pueden inhabilitar a nivel del grupo de nodos de GKE con la implementación de un DaemonSet. Sin embargo, implementar este DaemonSet hará que todos tus nodos en el grupo de nodos se reinicien al mismo tiempo. Por lo tanto, se recomienda crear un grupo de nodos nuevo en el clúster, implementar el DaemonSet para inhabilitar los hipersubprocesos en ese grupo y, luego, migrar tus cargas de trabajo al grupo de nodos nuevo. 

Haz lo siguiente para crear un grupo de nodos nuevo con hipersubprocesos
inhabilitados:

  1. Crea un grupo de nodos nuevo en tu clúster con la etiqueta de nodo ` cloud.google.com/gke-smt-disabled=true ` , como se indica a continuación: 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. Implementa el DaemonSet en este grupo de nodos nuevo. El DaemonSet solo se ejecutará en nodos con la etiqueta ` cloud.google.com/gke-smt-disabled=true ` . Este inhabilitará los hipersubprocesos y, luego, reiniciará el nodo. 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. Asegúrate de que los pods del DaemonSet estén en estado de ejecución. 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

Deberías obtener una respuesta similar a la siguiente:

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. Verifica que aparezca el mensaje “Se inhabilitó SMT” en los registros de los pods. 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

Nota: Las opciones de inicio no se pueden modificar si el nodo tiene
habilitada la característica de [ Inicio seguro
](https://cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-
nodes?hl=es_419#secure_boot) . Si el Inicio seguro está habilitado, se debe [
inhabilitar ](https://cloud.google.com/kubernetes-engine/docs/how-to/shielded-
gke-nodes?hl=es_419#disabling) antes de crear el DaemonSet.

Debes mantener el DaemonSet en ejecución en los grupos de nodos, de manera que
se apliquen los cambios automáticamente a los nodos nuevos que se creen en el
grupo. La creación de nodos puede activarse mediante la reparación automática,
la actualización manual o automática o con el ajuste de escala automático.

Para volver a habilitar los hipersubprocesos, será necesario que vuelvas a
crear el grupo de nodos sin implementar el DaemonSet proporcionado y migres
tus cargas de trabajo al grupo de nodos nuevo.

También te recomendamos que actualices los nodos de forma manual una vez que
el parche esté disponible. Para poder actualizar, primero debes [ actualizar
tu instancia principal ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=es_419#upgrading_the_cluster) a la versión más
reciente. Las instancias principales de GKE se actualizarán de forma
automática a la frecuencia de actualización habitual.

Actualizaremos este boletín con las versiones que contengan el parche cuando
estén disponibles.

####  ¿Qué vulnerabilidad corrige este parche?

Este parche mitiga las siguientes vulnerabilidades:

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
, [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) , [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) , [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091) :
Estas vulnerabilidades aprovechan la ejecución especulativa. Estas CVE se
conocen en conjunto como Muestreo de datos de microarquitectura. Estas
vulnerabilidades pueden hacer que los datos se expongan cuando la ejecución
especulativa interactúa con el estado de la microarquitectura.  |  Media  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  5 de abril de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco tiempo, se descubrieron las vulnerabilidades de seguridad [
CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
y [ CVE-2019-9901 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9901) en [ Envoy ](https://www.envoyproxy.io/) .

[ Istio ](https://istio.io/) incorpora Envoy, y estas vulnerabilidades
permiten que la política de Istio se omita en algunos casos.

Si habilitaste Istio en Google Kubernetes Engine (GKE), puedes verte afectado
por estas vulnerabilidades. **Recomendamos que actualices los clústeres
afectados a la versión más reciente del parche cuanto antes, además de los
archivos adicionales de Istio (las instrucciones se encuentran más abajo).**

####  ¿Qué debo hacer?

**Debido a la gravedad de estas vulnerabilidades, ya sea que hayas habilitado
las actualizaciones automáticas de nodos o no, te recomendamos hacer lo
siguiente:**

  1. **[ Actualiza de forma manual ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=es_419) tu clúster apenas el parche esté disponible. **
  2. **Sigue las instrucciones de la[ documentación para actualizar archivos adicionales ](https://istio.io/docs/setup/kubernetes/upgrade/steps/#sidecar-upgrade) a fin de realizar este proceso. **

Las versiones con parche estarán disponibles para todos los proyectos de GKE
antes de las 7:00 p.m. PDT de hoy.

Este parche estará disponible en las versiones de GKE que se mencionan abajo.
Los clústeres nuevos usarán la versión con parche de forma predeterminada
cuando se anuncie en la página de boletines de seguridad de GKE, prevista para
el 15 de abril de 2019. Si creas un clúster nuevo antes de esa fecha, deberás
especificar la versión con parche que debe usar. En el caso de los clientes de
GKE que habilitaron las [ actualizaciones automáticas de nodos
](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-
upgrades?hl=es_419) y que no realizan actualizaciones manuales, sus nodos se
actualizarán de forma automática a versiones con parche durante la siguiente
semana.

Versiones con parches:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  ¿Qué vulnerabilidad corrige este parche?

Este parche mitiga las siguientes vulnerabilidades:

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) y [ CVE-2019-9901.
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) Puedes obtener
más información sobre estas en el [ blog de Istio.
](https://istio.io/blog/2019/announcing-1.1.2)

|  Alta  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  1 de marzo de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 22/03/2019:** Este parche está disponible en las versiones
de Kubernetes 1.11.8-gke.4, 1.13.4-gke.1 y en las más recientes. El parche aún
no está disponible en la versión 1.12. Haz un seguimiento de la disponibilidad
de estos parches en las [ notas de la versión
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#march_19_2019) .

Hace poco tiempo, se descubrió una vulnerabilidad nueva de denegación del
servicio en Kubernetes, [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) , que permite que los usuarios con
autorización para crear solicitudes de parche puedan desarrollar solicitudes
“json-patch” malintencionadas que consumen cantidades excesivas de CPU y
memoria en el servidor de la API de Kubernetes, lo que podría reducir la
disponibilidad del plano de control de los clústeres. Para obtener más
detalles, consulta la [ divulgación de Kubernetes
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-
announce/vmUUNkYfG9g) . **Esta vulnerabilidad afecta a todas las instancias
principales de Google Kubernetes Engine (GKE). Una próxima versión del parche
incluirá una mitigación para esta vulnerabilidad. Actualizaremos las
instancias principales de los clústeres a la versión que incluye el parche de
manera automática durante las próximas semanas según la frecuencia de
actualización habitual.**

####  ¿Qué debo hacer?

**No es necesario que realices ninguna acción. Las instancias principales de
GKE se actualizarán de forma automática según la frecuencia de actualización
habitual.** Si quieres actualizar la instancia principal antes, puedes [
iniciar de forma manual una actualización de esta instancia
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es_419#upgrading_the_cluster) .

Actualizaremos este boletín con las versiones que contienen un parche. Ten en
cuenta que el parche solo estará disponible en las versiones 1.11 y
superiores, no en la versión 1.10.

####  ¿Qué vulnerabilidad corrige este parche?

Este parche mitiga la siguiente vulnerabilidad:

La vulnerabilidad [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) permite que un usuario desarrolle
especialmente un parche de tipo “json-patch” que consume cantidades excesivas
de CPU en el servidor de la API de Kubernetes, lo que podría reducir la
disponibilidad del plano de control de los clústeres.

|  Media  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  11 de febrero de 2019 (runc)

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Open Containers Initiative (OCI) [ descubrió hace poco tiempo
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=es_419#!topic/dev/Tc1ELm-8oDI)
una vulnerabilidad de seguridad nueva ( [ CVE-2019-5736
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736) ) en runc, que
permite obtener privilegios de administrador en el nodo host mediante un
escape de contenedor.

**Esta vulnerabilidad afecta a los nodos de Google Kubernetes Engine (GKE) que
ejecutan Ubuntu, por lo que te recomendamos que[ actualices
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es_419) a la versión más reciente del parche cuanto antes. Para
ello, sigue las instrucciones que se detallan a continuación. **

####  ¿Qué debo hacer?

Para actualizar los nodos, primero debes actualizar el nodo principal a la
versión más reciente. Este parche está disponible en Kubernetes 1.10.12-gke.7,
1.11.6-gke.11, 1.11.7-gke.4, 1.12.5-gke.5 y actualizaciones más recientes.
Puedes hacer un seguimiento de la disponibilidad de estos parches en las [
notas de la versión ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#february-11-2019) .

Ten en cuenta que la vulnerabilidad solo afecta a los nodos de GKE que
ejecutan Ubuntu y no a los que ejecutan COS.

Ten en cuenta que la versión nueva de runc consume más memoria, por lo que es
posible que debas actualizar la cantidad de memoria asignada a los
contenedores si configuraste límites de memoria bajos (menores que 16 MB).

####  ¿Qué vulnerabilidad corrige este parche?

Este parche mitiga la siguiente vulnerabilidad:

[ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) es una vulnerabilidad en runc que permite
que un contenedor malintencionado reemplace el objeto binario runc del host
con una interacción del usuario mínima mediante un ejecutable para lograr la
ejecución de código con permisos de administrador en el nodo host. Los
contenedores que se ejecutan sin permisos de administrador no se ven
afectados. Esta vulnerabilidad de seguridad tiene una calificación de gravedad
alta.

|  Alta  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  11 de febrero de 2019 (Go)

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 25/02/2019:** El parche no está disponible en la versión
1.11.7-gke.4 como se informó anteriormente. Si ejecutas la versión 1.11.7,
puedes cambiar a la versión inferior (1.11.6) y actualizar a 1.12, o esperar
hasta que el parche de 1.11.7 esté disponible durante la semana del 4 de marzo
de 2019.

Hace poco tiempo, se descubrió la vulnerabilidad de seguridad [ CVE-2019-6486
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-6486) en el lenguaje
de programación Go, que corresponde a una vulnerabilidad de denegación del
servicio (DoS) en las implementaciones de criptografía de las curvas elípticas
P-521 y P-384. En Google Kubernetes Engine (GKE), esta vulnerabilidad podría
permitir que un usuario desarrolle solicitudes malintencionadas que consuman
cantidades excesivas de CPU en el servidor de la API de Kubernetes, lo que
podría reducir la disponibilidad del plano de control de los clústeres. Para
obtener más detalles, consulta la [ divulgación del lenguaje de programación
Go ](https://groups.google.com/forum/?hl=es_419#!topic/golang-
announce/mVeX35iXuSw) .

**Esta vulnerabilidad afecta a todas las instancias principales de Google
Kubernetes Engine (GKE). La[ versión más reciente del parche
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#february-11-2019) incluye una mitigación contra esta
vulnerabilidad. Actualizaremos las instancias principales de los clústeres a
la versión que incluye el parche de manera automática durante las próximas
semanas según la frecuencia de actualización habitual. **

####  ¿Qué debo hacer?

**No es necesario que realices ninguna acción. Las instancias principales de
GKE se actualizarán de forma automática según la frecuencia de actualización
habitual.** Si quieres actualizar la instancia principal antes, puedes [
iniciar de forma manual una actualización de esta instancia
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es_419#upgrading_the_cluster) .

Este parche está disponible en GKE 1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4,
1.12.5-gke.5 y actualizaciones más recientes.

####  ¿Qué vulnerabilidad corrige este parche?

Este parche mitiga la siguiente vulnerabilidad:

CVE-2019-6486 es una vulnerabilidad de las implementaciones de criptografía de
las curvas elípticas P-521 y P-384 que permite que un usuario desarrolle
entradas que consuman cantidades excesivas de CPU.

|  Alta  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  3 de diciembre de 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco tiempo, se descubrió una nueva vulnerabilidad de seguridad, [
CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) , en Kubernetes, que autorizaba a un
usuario con privilegios relativamente bajos a omitir la autorización de las
API de kubelet y le permitía ejecutar operaciones arbitrarias para cualquier
Pod de cualquier nodo en el clúster. Para obtener más detalles, consulta la [
divulgación de Kubernetes
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-
announce/GVllWCg6L88) . **Todas las instancias principales de Google
Kubernetes Engine (GKE) se vieron afectadas por estas vulnerabilidades, y ya
hemos actualizado los clústeres a las[ versiones más recientes del parche
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#november-12-2018) . No es necesario que realices ninguna
acción. **

####  ¿Qué debo hacer?

**No es necesario que realices ninguna acción. Ya se actualizaron las
instancias principales de GKE.**

Este parche está disponible en GKE 1.9.7-gke.11, 1.10.6-gke.11, 1.10.7-gke.11,
1.10.9-gke.5, 1.11.2-gke.18 y las versiones más recientes.

####  ¿Qué vulnerabilidad corrige este parche?

Este parche mitiga la siguiente vulnerabilidad:

La vulnerabilidad CVE-2018-1002105 permite que un usuario con privilegios
relativamente bajos omita la autorización de las API de kubelet. Esto le
permite al usuario realizar solicitudes de actualización para escalar y
realizar llamadas arbitrarias a la API de kubelet. Esto está calificado como
una vulnerabilidad crítica en Kubernetes. Debido a ciertos detalles en la
implementación de GKE que impidieron la ruta de escalamiento no autenticada,
se lo calificó como vulnerabilidad alta.

|  Alta  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  13 de noviembre de 2018

Descripción  
---  
  
**Actualización del 16/11/2018:** Se completó la revocación y rotación de
todos los tokens posiblemente afectados. No es necesario que realices ninguna
otra acción.

Hace poco tiempo, Google descubrió un problema en el complemento de la
Interfaz de la Red del Contenedor (CNI) Calico que puede, en ciertas
configuraciones, registrar información sensible. La Asesoría Técnica Tigera
está controlando este problema, con el código [ TTA-2018-001
](https://www.projectcalico.org/security-bulletins/) .

  * Cuando se ejecuta con el registro de nivel de depuración, el complemento de la CNI Calico escribe la configuración del cliente de la API de Kubernetes en los registros. 
  * La CNI Calico también escribirá el token de la API de Kubernetes en los registros en el nivel de información si el campo “k8s_auth_token” se ha establecido en la configuración de la red CNI. 
  * Además, cuando se ejecuta con el registro de nivel de depuración, si el token de la cuenta de servicio se establece de manera explícita, ya sea en el archivo de configuración de Calico que lee Calico o como variables de entorno que usa Calico, los componentes de Calico (calico/nodo, felix, CNI) escriben esta información en los archivos de registro. 

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
  
Los clústeres de Google Kubernetes Engine con una Política de red del clúster
y Stackdriver Logging habilitado registraron tokens de cuenta de servicio
Calico en Stackdriver. Los clústeres sin la Política de red habilitada no se
ven afectados.

Hemos implementado una solución que migra el complemento de la CNI Calico para
que solo acceda en el nivel de advertencia y utilice una nueva cuenta de
servicio. El código Calico con el parche se implementará en una versión
posterior.

Durante la próxima semana, realizaremos una revocación progresiva de todos los
tokens potencialmente afectados. Este boletín se actualizará cuando se haya
completado la revocación. **No se requiere ninguna otra acción de tu parte.**
(Esta rotación se completó el 16/11/2018).

Si deseas rotar estos tokens de inmediato, puedes ejecutar el siguiente
comando; el nuevo secreto correspondiente a la cuenta de servicio debería
volver a crearse de forma automática en unos segundos:  
  
kubectl get sa --namespace kube-system calico -o template --template '{{(index
.secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system  
---  
  
####  Detección

GKE registra todos los accesos en el servidor de la API. Para determinar si se
utilizó un token de Calico fuera del rango de IP esperado de Google Cloud,
puedes ejecutar la siguiente consulta de Stackdriver. Ten en consideración que
esto solo mostrará los registros de llamadas realizadas desde afuera de la red
de GCP. Recomendamos que lo personalices según las necesidades de tu entorno
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
  
##  14 de agosto de 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
[ Intel divulgó ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) las siguientes CVE:

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (para [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (para sistemas operativos y [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (para virtualización) 

A estas CVE se hace referencia de forma colectiva como "Falla de terminal L1
(L1TF)".

Estas vulnerabilidades L1TF explotan la ejecución especulativa, ya que atacan
la configuración de estructuras de datos en el procesador. "L1" hace
referencia a la caché de datos de nivel 1 (L1D), un recurso pequeño del núcleo
que se utiliza para acelerar el acceso a la memoria.

Consulta la [ entrada de blog de Google Cloud
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=es_419) para obtener más detalles sobre estas
vulnerabilidades y la mitigación de Compute Engine.

####  El impacto de Google Kubernetes Engine

La infraestructura que ejecuta Kubernetes Engine y aísla los clústeres y nodos
del cliente de sí mismos está protegida contra ataques conocidos.

Los grupos de nodos de Kubernetes Engine que utilizan una imagen de Container-
Optimized OS de Google y que tienen la [ actualización automática
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=es_419) habilitada se actualizarán de forma automática a las
versiones con parches de nuestra imagen COS ni bien estén disponibles a partir
de la semana del 20 de agosto de 2018.

Los grupos de nodos de Kubernetes Engine que no tengan la [ actualización
automática ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=es_419) habilitada deberán [ actualizarse de forma manual
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=es_419) cuando estén disponibles las versiones con parche
de nuestra imagen COS.

|  Alta  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  6 de agosto de 2018; última actualización: 5 de septiembre de 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Actualización del 05/09/2018

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) se divulgó hace poco tiempo. Al igual que
con [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) , se trata de una vulnerabilidad de la red
en el kernel que aumenta la efectividad de los ataques de denegación del
servicio (DoS) contra sistemas vulnerables. La diferencia principal es que se
puede utilizar CVE-2018-5391 en conexiones IP. Actualizamos este boletín para
que abarque ambas vulnerabilidades.

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

####  El impacto de Google Kubernetes Engine

A partir del 11/08/2018, todas las instancias principales de Kubernetes Engine
están protegidas contra ambas vulnerabilidades. Además, todos los clústeres de
Kubernetes Engine configurados para actualizarse de forma automática también
están protegidos contra ambas vulnerabilidades. Los grupos de nodos de
Kubernetes Engine que no estén configurados para [ actualizarse de forma
automática ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-
a-cluster?hl=es_419) , y se actualizaron de forma manual por última vez antes
del 11/08/2018, están afectados por ambas vulnerabilidades.

####  Versiones con parche

Debido a la gravedad de esta vulnerabilidad, te recomendamos [ actualizar de
forma manual ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=es_419#upgrading-nodes) tus nodos ni bien esté
disponible el parche.

|  Alta  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  30 de mayo de 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco tiempo, se descubrió una vulnerabilidad en Git que podría permitir
el aumento de privilegios en Kubernetes si usuarios sin privilegios tienen
permitido crear Pods con volúmenes gitRepo. La CVE se identifica con la
etiqueta [ CVE-2018-11235 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-11235) .

####  ¿Me veo afectado?

Esta vulnerabilidad te afecta si todas las siguientes afirmaciones son
verdaderas:

  * Los usuarios que no son de confianza pueden crear Pods (o activar su creación). 
  * Los pods creados por usuarios que no son de confianza tienen restricciones que impiden el acceso a la raíz del host (por ejemplo, mediante [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=es_419) ). 
  * Los pods creados por usuarios que no son de confianza pueden usar el tipo de volumen gitRepo. 

Todos los nodos de Kubernetes Engine son vulnerables.

####  ¿Qué debo hacer?

Prohibir el uso del tipo de volumen gitRepo. Para prohibir los volúmenes
gitRepo con PodSecurityPolicy, omite ` gitRepo ` de la lista blanca ` volumes
` en tu PodSecurityPolicy.

Se pueden lograr comportamientos equivalentes del volumen gitRepo si se clona
un repositorio de Git en un volumen EmptyDir de un initContainer:

    
    
    
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

Se incluirá un parche en una próxima versión de Kubernetes Engine. Vuelve a
visitar este sitio para obtener más detalles.

|  Media  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  21 de mayo de 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco tiempo, se descubrieron diferentes vulnerabilidades en el kernel de
Linux que podrían permitir la elevación de privilegios o la denegación del
servicio (mediante el fallo del kernel) desde un proceso sin privilegios.
Estas CVE se identifican con las etiquetas [ CVE-2018-1000199
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199) , [
CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
y [ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) . Todos los nodos de Kubernetes Engine se
ven afectados por estas vulnerabilidades. Te recomendamos [ actualizar
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=es_419) a la versión más reciente del parche, como se
muestra a continuación.

####  ¿Qué debo hacer?

Para poder llevar a cabo la actualización, primero debes actualizar tu
instancia principal a la versión más reciente. El parche está disponible en
Kubernetes Engine 1.8.12-gke.1, Kubernetes Engine 1.9.7-gke.1 y Kubernetes
Engine 1.10.2-gke.1. Estas versiones incluyen parches para imágenes de
Container-Optimized OS y Ubuntu.

Si creas un clúster nuevo antes, debes especificar la versión con parche que
debe usarse. A los clientes que tengan las [ actualizaciones automáticas de
nodo ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=es_419) habilitadas y no hagan la actualización de forma manual,
se les actualizarán los nodos a la versión con parche en las próximas semanas.

####  ¿Qué vulnerabilidades corrige este parche?

Este parche mitiga las siguientes vulnerabilidades:

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : Esta vulnerabilidad afecta el kernel
de Linux. Permite que un usuario o proceso sin privilegios genere una falla en
el kernel del sistema, lo que lleva a un ataque DoS o elevación de
privilegios. Tiene una calificación de vulnerabilidad alta, con un CVSS de
7.8.

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : Esta vulnerabilidad afecta el kernel de
Linux. Permite que un usuario o proceso sin privilegios genere una falla en el
kernel del sistema, lo que lleva a un ataque DoS. Tiene una calificación de
vulnerabilidad media, con un CVSS de 6.5.

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : Esta vulnerabilidad afecta el hipervisor
KVM del kernel de Linux. Permite que un proceso sin privilegios genere una
falla en el kernel invitado o que, potencialmente, adquiera privilegios. La
vulnerabilidad tiene un parche en la infraestructura sobre la que se ejecuta
Kubernetes Engine, por lo que Kubernetes Engine no se ve afectado. Tiene una
calificación de vulnerabilidad alta, con un CVSS de 8.0.

|  Alta  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  12 de marzo de 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
El proyecto Kubernetes [ divulgó hace poco tiempo
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-security-
announce/P7lBjbjDKd8) vulnerabilidades de seguridad nuevas, [ CVE-2017-1002101
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) y [
CVE-2017-1002102 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002102) , que permiten que los contenedores accedan
a archivos externos. Todos los nodos de Kubernetes Engine se ven afectados por
estas vulnerabilidades. Te recomendamos actualizar a la versión más reciente
del parche tan pronto como sea posible, como se muestra a continuación.

####  ¿Qué debo hacer?

Debido a la gravedad de estas vulnerabilidades, ya sea que hayas habilitado
las actualizaciones automáticas de nodos o no, recomendamos que [ actualices
de forma manual ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=es_419) tus nodos ni bien esté disponible
el parche. Este parche estará disponible para todos los clientes a partir del
16 de marzo, pero puede que esté disponible para ti antes, según la zona en la
que se encuentra tu clúster, en función del [ programa de actualizaciones
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#march-12-2018) .

Para poder llevar a cabo la actualización, primero debes actualizar tu
instancia principal a la versión más reciente. Este parche estará disponible
en Kubernetes 1.9.4-gke.1, Kubernetes 1.8.9-gke.1 y Kubernetes 1.7.14-gke.1.
Los clústeres nuevos usarán la versión con parche de forma predeterminada a
partir del 30 de marzo. Si creas un clúster nuevo antes, debes especificar la
versión con parche que debe usarse.

A los clientes de Kubernetes Engine que tengan las [ actualizaciones
automáticas de nodos ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=es_419) habilitadas y no hagan la
actualización de forma manual, se les actualizarán los nodos a la versión con
parche antes del 23 de abril. Sin embargo, debido a la gravedad de estas
vulnerabilidades, recomendamos que [ actualices de forma manual
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=es_419) tus nodos en cuanto esté disponible el parche.

####  ¿Qué vulnerabilidades corrige este parche?

Este parche mitiga las siguientes dos vulnerabilidades:

La vulnerabilidad CVE-2017-1002101 permite que los contenedores que utilizan
activaciones de volumen de [ subpath (subruta)
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) tengan
acceso a archivos externos al volumen. Eso significa que si estás bloqueando
acceso al contenedor a volúmenes de la ruta del host con PodSecurityPolicy, un
atacante con la capacidad para actualizar o crear pods puede activar cualquier
ruta del host mediante cualquier otro tipo de volumen.

La vulnerabilidad CVE-2017-1002102 permite que los contenedores que utilizan
ciertos tipos de volúmenes (incluidos los secretos, mapas de configuración,
volúmenes proyectados o volúmenes de la API descendentes) borren archivos
externos al volumen. Esto significa que si un contenedor que utiliza uno de
estos tipos de volúmenes se ve comprometido, o si permites que usuarios que no
son de confianza creen pods, un atacante podría usar ese contenedor para
borrar archivos arbitrarios en el host.

Para obtener más información sobre la solución, lee la [ entrada de blog de
Kubernetes ](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-
vulnerability/) .

|  Alta  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

