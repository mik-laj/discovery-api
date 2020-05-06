#  Boletines de seguridad

Todos los boletines de seguridad de Google Kubernetes Engine (GKE) se
describen en este tema.

En general, las vulnerabilidades se mantienen ocultas y no se las puede
divulgar hasta que las partes afectadas hayan tenido la oportunidad de tratar
el tema. En estos casos, las [ Notas de la versión
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=es_419) de
GKE se refieren a “actualizaciones de seguridad” hasta que se apruebe la
divulgación. En ese momento, las notas se actualizarán para reflejar la
vulnerabilidad tratada en el parche.

**Nota:** Si ejecutas cargas de trabajo de multiusuario en GKE, presta
especial atención a estos boletines. Es más probable que estas
vulnerabilidades afecten a cargas de trabajo de multiusuario. A fin de obtener
una descripción técnica de los límites de seguridad en GKE y para conocer el
efecto que tienen en las cargas de trabajo, consulta [ Aislamiento en
diferentes capas de la pila de Kubernetes
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Para recibir los boletines de seguridad más recientes, agrega la URL de esta
página a un [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) o incluye
directamente la URL del feed: ` https://cloud.google.com/feeds/kubernetes-
engine-security-bulletins.xml ` .

##  GCP‑2020‑003

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco, se descubrió una vulnerabilidad en Kubernetes, descrita en [
CVE‑2019‑11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) , que permite que cualquier usuario con
autorización para realizar solicitudes POST ejecute un ataque de denegación
del servicio de forma remota en un servidor de la API de Kubernetes. El Comité
de Seguridad del Producto (PSC) de Kubernetes publicó información adicional
sobre esta vulnerabilidad, que puedes encontrar [ aquí
](https://groups.google.com/g/kubernetes-security-
announce/c/wuwEwZigXBc?hl=es_419) .

Los clústeres de GKE que usan [ redes autorizadas para instancias principales
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=es_419) y los [ clústeres privados sin extremo público
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=es_419#private_master) están protegidos ante esta vulnerabilidad.

####  ¿Qué debo hacer?

Te recomendamos que actualices el clúster a una versión de parche que incluya
la corrección para esta vulnerabilidad.

Estas son las versiones de parche que incluyen la corrección:

  * 1.13.12‑gke.29 
  * 1.14.9‑gke.27 
  * 1.14.10‑gke.24 
  * 1.15.9‑gke.20 
  * 1.16.6‑gke.1 

####  ¿Qué vulnerabilidades trata este parche?

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

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Kubernetes divulgó [ dos vulnerabilidades de denegación del servicio
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-security-
announce/2UOlsba2g0s) : una que afecta al servidor de la API y otra que afecta
a Kubelets. Para obtener más detalles, consulta los problemas de Kubernetes [
89377 ](https://github.com/kubernetes/kubernetes/issues/89377) y [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) .

####  ¿Qué debo hacer?

Todos los usuarios de GKE están protegidos contra la vulnerabilidad
CVE‑2020‑8551, excepto en los casos en que se permita que usuarios no
confiables puedan enviar solicitudes en la red interna del clúster. Usar [
redes autorizadas para instancias principales
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

Descripción  |  Gravedad  |  Notas  
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

Los clientes que usan nodos en Windows Server deben actualizar los nodos y las
cargas de trabajo en contenedores que se ejecutan en esos nodos a las
versiones con parche para mitigar la vulnerabilidad.

**Para actualizar los contenedores, sigue estos pasos:**

Vuelve a compilar tus contenedores con las imágenes base de contenedor de
Microsoft más actuales. Para ello, debes seleccionar una etiqueta [ servercore
](https://hub.docker.com/_/microsoft-windows-servercore) o [ nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) cuya fecha de última
actualización sea el 14/01/2020 o posterior.

**Actualización de nodos:**

El proceso para que las versiones de parche estén disponibles ya se está
llevando a cabo y se completará el 24 de enero de 2020.

Puedes esperar hasta esa fecha y actualizar el nodo a una versión de GKE con
parche o puedes usar Windows Update en cualquier momento para implementar el
último parche de Windows de forma manual.

Las versiones con parche que contendrán la mitigación se mencionan a
continuación:

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**¿Qué vulnerabilidades trata este parche?**

Con este parche, se mitigan las siguientes vulnerabilidades:

[ CVE‑2020‑0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) Esta vulnerabilidad también se conoce como
la [ Vulnerabilidad de falsificación de identidad de la API de Windows Crypto
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) y se puede aprovechar para que los archivos
ejecutables maliciosos parezcan confiables o a fin de permitir que el atacante
realice ataques de intermediario y desencripte información confidencial sobre
las conexiones TLS del software afectado.

|

Puntuación base de la NVD: 8.1 (alta)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  14 de noviembre de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Kubernetes divulgó un problema de seguridad de los archivos adicionales [ `
external-provisioner ` ](https://github.com/kubernetes-csi/external-
provisioner) , [ ` external-snapshotter ` ](https://github.com/kubernetes-
csi/external-snapshotter) y [ ` external-resizer `
](https://github.com/kubernetes-csi/external-resizer) de kubernetes-csi, que
afecta a la mayoría de las versiones de los archivos adicionales en paquetes
de [ controladores de Container Storage Interface (CSI) ](https://kubernetes-
csi.github.io/docs/drivers.html) . Para obtener más información, consulta el [
aviso de Kubernetes ](https://github.com/kubernetes/kubernetes/issues/85233)
al respecto.

**¿Qué debo hacer?**  
**Esta vulnerabilidad no afecta a ningún componente administrado de GKE** . Es
posible que te veas afectado si administras tus propios controladores de CSI
en los [ clústeres Alfa de GKE ](https://cloud.google.com/kubernetes-
engine/docs/concepts/alpha-clusters?hl=es_419) que ejecutan la versión de GKE
1.12 o versiones posteriores. Si te ves afectado, consulta con tu proveedor de
controladores de CSI a fin de obtener instrucciones para la actualización.

**¿Qué vulnerabilidades trata este parche?**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : Esta CVE es una vulnerabilidad de los
archivos adicionales [ ` external-provisioner `
](https://github.com/kubernetes-csi/external-provisioner) , [ ` external-
snapshotter ` ](https://github.com/kubernetes-csi/external-snapshotter) y [ `
external-resizer ` ](https://github.com/kubernetes-csi/external-resizer) de `
kubernetes-csi ` , que puede permitir el acceso no autorizado a datos de
volumen y su mutación. Esta afecta a la mayoría de las versiones de los
archivos adicionales en paquetes de [ controladores de CSI
](https://kubernetes-csi.github.io/docs/drivers.html) .

|

Media

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  12 de noviembre de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Intel divulgó las CVE que pueden permitir las interacciones entre la ejecución
especulativa y el estado de microarquitectura para exponer datos. Si deseas
obtener más información, consulta el [ aviso de Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) al respecto.

**La infraestructura de host que ejecuta Kubernetes Engine aísla las cargas de
trabajo del cliente. A menos que ejecutes código no confiable dentro de tus
propios clústeres de GKE de multiusuario _y_ uses nodos N2, M2 o C2, no es
necesario que realices ninguna acción. ** En el caso de las instancias de GKE
en los nodos N1, no se requiere ninguna otra acción.

Si ejecutas Anthos GKE On‑Prem, el nivel de exposición dependerá del hardware.
Compara tu infraestructura con la [ divulgación de Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

####  ¿Qué debo hacer?

**Solo te verás afectado si usas grupos de nodos con nodos N2, M2 o C2 _y_
estos ejecutan código no confiable dentro de tus propios clústeres de GKE de
multiusuario. **

**El parche se aplica mediante el reinicio de los nodos.** La manera más
sencilla de reiniciar todos los nodos de tu grupo de nodos es usar la
operación de [ actualización ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=es_419#upgrade_nodes) para forzar un
reinicio de todos los nodos del grupo afectado.  

Nota: No es necesario que cambies las versiones durante una actualización.
Puedes iniciar una actualización a la misma versión de nodo con la marca `
cluster-version ` .

####  ¿Qué vulnerabilidades trata este parche?

Con este parche, se mitigan las siguientes vulnerabilidades:

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
: Esta CVE también se conoce como Anulación asíncrona de TSX o (TAA). TAA
habilita otra alternativa para el robo de datos mediante las mismas
estructuras de datos de microarquitectura que fueron vulnerables ante el [
Muestreo de datos de microarquitectura (MDS)
](https://cloud.google.com/kubernetes-engine/docs/security-
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

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Recientemente, se descubrió una vulnerabilidad en el lenguaje de programación
Go, y se la describe en [ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) . Esta vulnerabilidad puede afectar a la
configuración de Kubernetes que usa un proxy de autenticación. Para obtener
más información, consulta la [ divulgación de Kubernetes
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-security-
announce/PtsUCqFi4h4) al respecto.

Kubernetes Engine no permite la configuración de un proxy de autenticación,
por lo que esta vulnerabilidad no lo afecta.

|

Ninguna

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  16 de octubre de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 24-10-2019:** Las versiones con parche ahora están
disponibles en todas las zonas.

* * *

Hace poco, se descubrió una vulnerabilidad en Kubernetes, descrita en [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) , que permite que cualquier usuario con
autorización para realizar solicitudes POST ejecute un ataque de denegación
del servicio de forma remota en un servidor de la API de Kubernetes. El Comité
de seguridad de productos (PSC) de Kubernetes publicó información adicional
sobre esta vulnerabilidad, que puedes encontrar [ aquí
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-security-
announce/jk8polzSUxs) .

Los clústeres de GKE que usan [ redes autorizadas principales
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=es_419) y los [ clústeres privados sin extremo público
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=es_419#private_master) mitigan esta vulnerabilidad.

######  ¿Qué debo hacer?

Te recomendamos actualizar tu clúster a una versión de parche que contenga la
opción de corrección en cuanto esté disponible. Se estima que estará
disponible en todas las zonas con la actualización de GKE planificada en la
semana del 14 de octubre.

Las versiones de parche que contendrán la mitigación son las siguientes:

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  ¿Qué vulnerabilidades trata este parche?

Con este parche, se mitigan las siguientes vulnerabilidades:

CVE-2019-11253 es una vulnerabilidad de denegación del servicio (DoS).

|

Alta

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  16 de septiembre de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Este boletín se actualizó desde su publicación original.

Hace poco, se descubrieron vulnerabilidades de seguridad nuevas en el lenguaje
de programación Go: [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) y [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) , que son
vulnerabilidades de denegación del servicio (DoS). En GKE, esta vulnerabilidad
puede permitir que un usuario cree solicitudes maliciosas que consuman
cantidades excesivas de CPU en el servidor de la API de Kubernetes, lo que
podría reducir la disponibilidad del plano de control de los clústeres. Para
obtener más información, consulta la [ divulgación del lenguaje de
programación Go ](https://groups.google.com/forum/?hl=es_419#!topic/golang-
announce/65QixT3tcmg) al respecto.

######  ¿Qué debo hacer?

Recomendamos que actualices el clúster a la versión de parche más reciente,
que contendrá la mitigación para esta vulnerabilidad, en cuanto esté
disponible. Se estima estará disponible en todas las zonas con la próxima
actualización de GKE, según el [ programa de lanzamiento
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#september_16_2019) .

Las versiones de parche que contendrán la mitigación son las siguientes:

  * **Actualización del 16 de octubre de 2019:** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  ¿Qué vulnerabilidad trata este parche?

Con este parche, se mitigan las siguientes vulnerabilidades:

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

Se actualizó el boletín de la corrección de la vulnerabilidad que se documentó
en el boletín del  31 de mayo de 2019  .

##  22 de agosto de 2019

Se actualizó el boletín del  5 de agosto de 2019  . La corrección de la
vulnerabilidad documentada en el boletín anterior está [ disponible
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#august_22_2019) .

##  8 de agosto de 2019

Se actualizó el boletín del  5 de agosto de 2019  . Se estima que la
corrección de la vulnerabilidad que se documentó en ese boletín estará
disponible en la próxima actualización de GKE.

##  5 de agosto de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Este boletín se actualizó desde su publicación original.

Hace poco, se descubrió una vulnerabilidad en Kubernetes, [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) , que permite
que se actúe sobre las instancias de [ recursos personalizados
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) de alcance de clúster como si fueran objetos con espacio de
nombres existentes en todos los espacios de nombres. Esto significa que las
cuentas de usuario y de servicio que solo cuentan con permisos de RBAC a nivel
de espacio de nombres pueden interactuar con recursos personalizados de
alcance de clúster. A fin de aprovechar esta vulnerabilidad, el atacante debe
tener privilegios para acceder al recurso en cualquier espacio de nombres.

######  ¿Qué debo hacer?

Recomendamos que [ actualices ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=es_419) el clúster a la versión de
parche más reciente, que contendrá la mitigación para esta vulnerabilidad, en
cuanto esté disponible. Se estima que estará disponible en todas las zonas con
la próxima actualización de GKE. Las versiones de parche que contendrán la
mitigación se mencionan a continuación:

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ Canal rápido ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=es_419) ) 

######  ¿Qué vulnerabilidad trata este parche?

Con el parche, se mitiga la siguiente vulnerabilidad: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Media

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  3 de julio de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Ya está disponible una versión de parche de ` kubectl ` para abordar la
vulnerabilidad CVE-2019-11246 con [ ` gcloud ` 253.0.0
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

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
######  Actualización del 3 de julio de 2019

En el momento de nuestra última actualización, los parches de las versiones
1.11.9 y 1.11.10 no estaban disponibles. Ahora lanzamos la versión
1.11.10-gke.5 como una actualización para ambas versiones 1.11.

Por el momento, las instancias principales de GKE cuentan con el parche, al
igual que la infraestructura de Google que ejecuta Kubernetes Engine. Esta
última, además, está protegida contra esta vulnerabilidad.

Las instancias principales de 1.11 pronto quedarán obsoletas y están
programadas para actualizarse de forma automática a la versión 1.12 durante la
semana del 8 de julio de 2019. Puedes elegir cualquiera de las siguientes
acciones sugeridas para actualizar los nodos a una versión de parche:

  * Realiza la actualización de nodos a la versión 1.11.10-gke.5 antes del 8 de julio de 2019. Después de esta fecha, se comenzarán a quitar las versiones 1.11 de la lista de asignaciones de actualización disponibles. 
  * Habilita las [ actualizaciones automáticas ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=es_419) en los nodos 1.11 y permite que se actualicen cuando las instancias principales se actualicen a la versión 1.12. 
  * [ Actualiza de forma manual ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=es_419) las instancias principales y los nodos a una versión 1.12 corregida. 

El boletín original del 24 de junio de 2019 es el siguiente:

* * *

######  Actualización del 24 de junio de 2019

Las versiones de parche de Kubernetes que se indican más abajo están
disponibles desde el 22/06/2019 a las 09:40 p.m. (UTC). Las instancias
principales entre las versiones 1.11.0 y 1.13.6 de Kubernetes se actualizarán
de forma automática a una versión de parche. Si no ejecutas una versión
compatible con este parche, actualiza a una versión de instancia principal
compatible (que se mencionan a continuación) antes de actualizar tus nodos.

**Debido a la gravedad de estas vulnerabilidades, ya sea que tengas habilitada
o no la actualización automática de nodos, te recomendamos[ actualizar de
forma manual ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=es_419) los nodos y las instancias
principales a una de estas versiones cuanto antes. **

Las versiones de parche son las siguientes:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

El boletín original del 18 de junio de 2019 es el siguiente:

* * *

Hace poco, Netflix divulgó tres vulnerabilidades de TCP de los kernels de
Linux:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Estas CVE se conocen en conjunto como [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) .

Los kernels de Linux sin parche pueden ser vulnerables a un ataque de
denegación del servicio activado de forma remota. Los **nodos de Google
Kubernetes Engine que envían o reciben tráfico de red no confiable se ven
afectados, por lo que te recomendamos seguir los pasos de mitigación que se
detallan a continuación para proteger tus cargas de trabajo.**

######  Instancias principales de Kubernetes

  * Las instancias principales de Kubernetes que usan [ Redes autorizadas ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=es_419) para limitar el tráfico a redes confiables no se ven afectadas. 

  * Las instancias principales de los clústeres de GKE, que son administradas por Google, obtendrán el parche de forma automática en los próximos días. Los clientes no deben realizar ninguna acción. 

######  Nodos de Kubernetes

Los nodos que limitan el tráfico a redes confiables no se ven afectados. Esto
se refiere a un clúster con las siguientes características:

  * Nodos con firewall de redes no confiables o sin IP públicas ( [ clústeres privados ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=es_419) ) 
  * Clústeres sin servicios públicos de LoadBalancer 

Google prepara una mitigación permanente para estas vulnerabilidades que
estará disponible como una versión nueva de nodo. Actualizaremos este boletín
y enviaremos un correo electrónico a todos los clientes de GKE cuando la
corrección permanente esté disponible.

Hasta entonces, creamos un DaemonSet de Kubernetes que implementa mitigaciones
mediante la modificación de la configuración de ` iptables ` del host.

#####  ¿Qué debo hacer?

Aplica el DaemonSet de Kubernetes a todos los nodos de tu clúster mediante la
ejecución del comando que se muestra a continuación. Esta acción agrega una
regla ` iptables ` a las reglas ` iptables ` existentes en el nodo a fin de
mitigar la vulnerabilidad. **Ejecuta el comando una vez por clúster y por
proyecto de Google Cloud.**

    
    
    
    kubectl apply -f \
        https://raw.githubusercontent.com/GoogleCloudPlatform\
        /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
              

Debido a que IPv6 no es compatible con GKE, no se requiere ninguna regla
ip6tables.

Una vez que una versión de parche de nodo esté disponible y hayas actualizado
todos los nodos posiblemente afectados, podrás quitar el DaemonSet con el
comando que se indica a continuación. **Ejecuta el comando una vez por clúster
y por proyecto de Google Cloud.**

    
    
    
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
253.0.0, para las versiones de ` kubectl ` 1.12.9, 1.13.6, 1.14.2 y versiones
más recientes.

**Nota:** El parche no está disponible en 1.11.10.

* * *

Hace poco, se descubrió una vulnerabilidad en Kubernetes, [ CVE-2019-11246
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11246) , que permite
que un atacante con acceso a una operación ` kubectl cp ` y a la ejecución de
código dentro de un contenedor modifique los archivos en el host. Si se
aprovecha esta vulnerabilidad, los atacantes pueden reemplazar o crear
archivos en el sistema de archivos del host. Para obtener más detalles,
consulta la [ divulgación de Kubernetes
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-security-
announce/NLs2TGbfPdo) al respecto.

**Todas las versiones de` gcloud ` de Google Kubernetes Engine (GKE) se ven
afectadas por esta vulnerabilidad, por lo que te recomendamos que actualices a
la versión de parche más reciente de ` gcloud ` cuando esté disponible. ** En
una versión de parche próxima, se incluirá una mitigación para esta
vulnerabilidad.

######  ¿Qué debo hacer?

Habrá una versión de parche de ` kubectl ` disponible en una actualización de
` gcloud ` próxima. También puedes [ actualizar ` kubectl ` directamente
](https://kubernetes.io/docs/tasks/tools/install-kubectl/) por tu cuenta.

Haz un seguimiento de la disponibilidad de este parche en las [ notas de la
versión de ` gcloud ` ](https://cloud.google.com/sdk/docs/release-
notes?hl=es_419) .

######  ¿Qué vulnerabilidad trata este parche?

La vulnerabilidad [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) permite que un atacante con acceso a una
operación de ` kubectl cp ` y a la ejecución de código dentro de un contenedor
modifique los archivos del host. Potencialmente, esta vulnerabilidad permite
que los atacantes reemplacen o creen archivos en el sistema de archivos del
host.

|

Alta

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  18 de junio de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco, se descubrió una vulnerabilidad en Docker, [ CVE-2018-15664
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-15664) , que permite
que un atacante con habilitación para ejecutar código dentro de un contenedor
usurpe una operación ` docker cp ` iniciada de forma externa. Con esta
vulnerabilidad, un atacante puede cambiar la ubicación en la que se escribe un
archivo por una ubicación arbitraria en el sistema de archivos del host.

**Todos los nodos de Google Kubernetes Engine (GKE) que ejecutan Docker se ven
afectados por esta vulnerabilidad, por lo que te recomendamos actualizar a la
versión de parche más reciente cuando esté disponible. En una versión de
parche próxima, se incluirá una mitigación para esta vulnerabilidad.**

**Las instancias principales de Google Kubernetes Engine (GKE) anteriores a la
versión 1.12.7 ejecutan Docker y se ven afectadas por esta vulnerabilidad.**
En GKE, los usuarios no tienen acceso a ` docker cp ` en la instancia
principal, por lo que el riesgo de esta vulnerabilidad es limitado en las
instancias principales de GKE.

#####  ¿Qué debo hacer?

Solo los nodos que ejecutan Docker se ven afectados, y solo cuando se emite un
comando ` docker cp ` (o equivalente de la API) que puede usurparse. Lo
previsto es que esta situación sea bastante inusual en los entornos de
Kubernetes. Los nodos que ejecutan [ COS con containerd
](https://cloud.google.com/kubernetes-engine/docs/concepts/using-
containerd?hl=es_419) no se ven afectados.

Si deseas actualizar los nodos, primero debes [ actualizar la instancia
principal ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-
a-cluster?hl=es_419#upgrading_the_cluster) a la versión de parche. Cuando el
parche esté disponible, podrás iniciar una actualización de instancia
principal o esperar que Google la actualice de forma automática. El parche
estará disponible en Docker 18.09.7, que se incluye en un próximo parche de
GKE. **Este parche solo estará disponible para la versión 1.13 de GKE y las
versiones posteriores.**

Las instancias principales del clúster se actualizarán a la versión de parche
de forma automática, con la frecuencia de actualización habitual. También
puedes iniciar una actualización de instancias principales por tu cuenta una
vez que esté disponible la versión de parche.

Se actualizará este boletín a fin de incluir las versiones que contienen un
parche una vez que estén disponibles. Haz un seguimiento de la disponibilidad
de estos parches en las [ notas de la versión
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=es_419) .

#####  ¿Qué vulnerabilidad trata este parche?

Con este parche, se mitiga la siguiente vulnerabilidad:

La vulnerabilidad [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) permite que un atacante con habilitación
para ejecutar código dentro de un contenedor usurpe una operación ` docker cp
` iniciada de forma externa. Con esta vulnerabilidad, un atacante puede
cambiar la ubicación en la que se escribe un archivo por una ubicación
arbitraria en el sistema de archivos del host.

|  Alta  |  
  
##  31 de mayo de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Este boletín se actualizó desde su publicación original.

######  Actualización del 2 de agosto de 2019

En el momento en que se emitió el primer boletín, solo las versiones incluidas
entre la 1.13.6-gke.0 y la 1.13.6-gke.5 se vieron afectadas. Debido a una
regresión, ahora todas las versiones 1.13.6.x se ven afectadas. Si ejecutas la
versión 1.13.6, actualiza a la versión 1.13.7 cuanto antes.

El proyecto de Kubernetes divulgó la vulnerabilidad [ CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) en las versiones
de kubelet v1.13.6 y v1.14.2, que puede causar que los contenedores se
ejecuten como UID 0 (en general, mapea al usuario ` root ` ), incluso si se
especifica un usuario diferente en la imagen de contenedor. **Si tus
contenedores se ejecutan como un usuario no raíz y ejecutas una versión de
nodo entre la versión 1.13.6-gke.0 y la 1.13.6-gke.6, te recomendamos
configurar` RunAsUser ` en todos los pods del clúster cuyos contenedores no
deban ejecutarse como UID 0. **

Si se especifica un valor de ` USER ` no raíz (por ejemplo, mediante la
configuración del valor de ` USER ` en un Dockerfile), se producirá un
comportamiento inesperado. Cuando un contenedor se ejecuta por primera vez en
un nodo, respetará de forma correcta el UID especificado. Sin embargo, debido
a este defecto, durante la segunda ejecución (y las posteriores), el
contenedor se ejecuta como UID 0 sin importar el UID que se especificó. Por lo
general, este es un privilegio elevado no deseado y puede conllevar un
comportamiento imprevisto de la aplicación.

#####  ¿Cómo me doy cuenta si ejecuto una versión afectada?

Ejecuta el siguiente comando para crear una lista de todos los nodos y sus
versiones de kubelet:

    
    
    
        kubectl get nodes -o=jsonpath='{range .items[*]}'\
        '{.status.nodeInfo.machineID}'\
        '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

Si el resultado menciona las versiones de kubelet incluidas abajo, tus nodos
se ven afectados:

  * v1.13.6 
  * v1.14.2 

#####  ¿Cómo me doy cuenta si mi configuración específica está afectada?

Si tus contenedores se ejecutan como un usuario no raíz, y ejecutas las
versiones de nodo incluidas entre la versión 1.13.6-gke.0 y la 1.13.6-gke.6,
te verás afectado, excepto en los siguientes casos:

  * Los pods que especifican un valor no raíz válido para ` runAsUser ` PodSecurityContext no se ven afectados y siguen funcionando según lo previsto. 
  * Las PodSecurityPolicies que se aplican en una configuración ` runAsUser ` tampoco se ven afectadas y siguen funcionando según lo previsto. 
  * Los pods que especifican ` mustRunAsNonRoot:true ` no se iniciarán como UID 0, pero no se iniciarán cuando se vean afectados por este problema. 

#####  ¿Qué debo hacer?

Configura el [ contexto de seguridad RunAsUser
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) en todos los pods del clúster que
no deben ejecutarse como UID 0. Puedes aplicar esta configuración mediante una
[ PodSecurityPolicy ](https://kubernetes.io/docs/concepts/policy/pod-security-
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
(MDS). Como consecuencia de estas vulnerabilidades, es posible que los datos
se expongan ante una interacción entre la ejecución especulativa y el estado
de la microarquitectura. Para obtener más detalles, consulta la [ divulgación
de Intel ](https://www.intel.com/content/www/us/en/security-
center/advisory/intel-sa-00233.html) al respecto.

**La infraestructura del host que ejecuta Kubernetes Engine aísla las cargas
de trabajo del cliente entre sí. A menos que ejecutes código no confiable
dentro de tus propios clústeres de GKE de multiusuario, no te verás
afectado.**

**En el caso de los clientes que ejecutan código no confiable en sus propios
servicios de multiusuario dentro de Kubernetes Engine, esta vulnerabilidad es
bastante grave.** Para mitigarla en Kubernetes Engine, debes inhabilitar los
hipersubprocesos en tus nodos. Estas vulnerabilidades solo afectan a los nodos
de Google Kubernetes Engine (GKE) que usan varias CPU. Ten en cuenta que las
VM n1-standard-1 (la predeterminada de GKE), g1-small y f1-micro solo exponen
1 CPU virtual en el entorno de invitado, de modo que no es necesario
inhabilitar los hipersubprocesos.

Se incluirán protecciones adicionales para habilitar la funcionalidad de
vaciado en la próxima [ versión de parche
](https://cloud.google.com/kubernetes-engine/release-notes?hl=es_419) . En las
próximas semanas, se actualizarán las instancias principales y los nodos a la
versión de parche mediante la actualización automática con la frecuencia de
actualización habitual. **Tener solo el parche no es suficiente para mitigar
la exposición a esta vulnerabilidad. Consulta la información que aparece a
continuación para conocer las acciones recomendadas.**

Si ejecutas GKE a nivel local, es posible que esta vulnerabilidad te afecte,
según el hardware que uses. Consulta la [ divulgación de Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) al respecto.

####  ¿Qué debo hacer?

**A menos que ejecutes código no confiable dentro de tus propios clústeres de
GKE de multiusuario, la vulnerabilidad no te afectará.**

**En el caso de los nodos de Kubernetes Engine, crea grupos de nodos nuevos
con los hipersubprocesos inhabilitados y vuelve a programar las cargas de
trabajo en los nodos nuevos.**

Ten en cuenta que las VM n1-standard-1, g1-small y f1-micro solo exponen 1 CPU
virtual en el entorno de invitado, de modo que no es necesario inhabilitar los
hipersubprocesos.

**Advertencia:**

  * La inhabilitación de los hipersubprocesos puede afectar en profundidad el rendimiento de los clústeres y la aplicación. Asegúrate de que esto es aceptable antes de implementar esta opción en los clústeres de producción. 
  * Los hipersubprocesos se pueden inhabilitar a nivel de grupo de nodos de GKE con la implementación de un DaemonSet. Sin embargo, implementar este DaemonSet hará que todos los nodos del grupo de nodos se reinicien al mismo tiempo. Por lo tanto, se recomienda crear un grupo de nodos nuevo en el clúster, implementar el DaemonSet para inhabilitar los hipersubprocesos en ese grupo y, luego, migrar las cargas de trabajo al grupo de nodos nuevo. 

Haz lo siguiente para crear un grupo de nodos nuevo con los hipersubprocesos
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

Debes mantener el DaemonSet en ejecución en los grupos de nodos, de manera que
se apliquen los cambios de forma automática a los nodos nuevos que se creen en
el grupo. La creación de nodos puede activarse mediante la reparación
automática, la actualización manual o automática o el ajuste de escala
automático.

Para volver a habilitar los hipersubprocesos, será necesario que vuelvas a
crear el grupo de nodos sin implementar el DaemonSet proporcionado y migres
tus cargas de trabajo al grupo de nodos nuevo.

También te recomendamos actualizar los nodos de forma manual una vez que el
parche esté disponible. Para poder actualizar los nodos, primero debes [
actualizar la instancia principal ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=es_419#upgrading_the_cluster) a la
versión más reciente. Las instancias principales de GKE se actualizarán de
forma automática según con la frecuencia de actualización habitual.

Se actualizará este boletín a fin de incluir las versiones que contienen un
parche cuando estén disponibles.

####  ¿Qué vulnerabilidad trata este parche?

Con este parche, se mitigan las siguientes vulnerabilidades:

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
, [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) , [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) , [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091) :
Estas vulnerabilidades aprovechan la ejecución especulativa. A estas CVE se
las conoce en conjunto como Muestreo de datos de microarquitectura. Como
consecuencia de estas vulnerabilidades, es posible que los datos se expongan
ante la interacción entre la ejecución especulativa y el estado de la
microarquitectura.  |  Media  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  5 de abril de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco, se descubrieron las vulnerabilidades de seguridad [ CVE-2019-9900
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900) y [
CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)
en [ Envoy ](https://www.envoyproxy.io/) .

[ Istio ](https://istio.io/) incorpora Envoy, y estas vulnerabilidades
permiten que la política de Istio se omita en algunos casos.

Si habilitaste Istio en Google Kubernetes Engine (GKE), es posible que estas
vulnerabilidades te afecten. **Recomendamos que actualices los clústeres
afectados a la versión de parche más reciente cuanto antes, además de
actualizar los archivos adicionales de Istio (las instrucciones se encuentran
más abajo).**

####  ¿Qué debo hacer?

**Debido a la gravedad de estas vulnerabilidades, te recomendamos hacer lo
siguiente, sin importar si habilitaste o no las actualizaciones automáticas de
los nodos:**

  1. **[ Actualiza de forma manual ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=es_419) tu clúster apenas esté disponible el parche. **
  2. **Sigue las instrucciones de la[ documentación sobre la actualización de archivos adicionales ](https://istio.io/docs/setup/kubernetes/upgrade/steps/#sidecar-upgrade) a fin de realizar este proceso. **

Las versiones de parche estarán disponibles para todos los proyectos de GKE
antes de las 7:00 p.m. PDT de hoy.

Este parche estará disponible en las versiones de GKE que se mencionan abajo.
Los clústeres nuevos usarán la versión de parche de forma predeterminada
cuando se anuncie en la página de boletines de seguridad de GKE el 15 de abril
de 2019, según se estima. Si creas un clúster nuevo antes de esa fecha,
deberás especificar la versión de parche que debe usar. En el caso de los
clientes de GKE que habilitaron las [ actualizaciones automáticas de los nodos
](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-
upgrades?hl=es_419) y que no realizan actualizaciones manuales, sus nodos se
actualizarán de forma automática a versiones de parche durante la siguiente
semana.

Versiones de parche:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  ¿Qué vulnerabilidad trata este parche?

Con este parche, se mitigan las siguientes vulnerabilidades:

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) y [ CVE-2019-9901.
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) Puedes obtener
más información sobre ellas en el [ blog de Istio.
](https://istio.io/blog/2019/announcing-1.1.2)

|  Alta  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  1 de marzo de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
**Actualización del 22/03/2019:** Este parche está disponible en las versiones
de Kubernetes 1.11.8-gke.4, 1.13.4-gke.1 y en versiones más recientes. El
parche aún no está disponible en la versión 1.12. Haz un seguimiento de la
disponibilidad de estos parches en las [ notas de la versión
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#march_19_2019) .

Hace poco, se descubrió una vulnerabilidad nueva de denegación del servicio en
Kubernetes, [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) , que permite que los usuarios con
autorización para crear solicitudes de parche desarrollen solicitudes “json-
patch” maliciosas que consumen cantidades excesivas de CPU y memoria en el
servidor de la API de Kubernetes, lo que puede reducir la disponibilidad del
plano de control de los clústeres. Para obtener más información, consulta la [
divulgación de Kubernetes
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-
announce/vmUUNkYfG9g) al respecto. **Estas vulnerabilidades afectan a todas
las instancias principales de Google Kubernetes Engine (GKE). En una versión
de parche próxima, se incluirá una mitigación para esta vulnerabilidad. En las
próximas semanas, se actualizarán las instancias principales del clúster a la
versión de parche de forma automática, con la frecuencia de actualización
habitual.**

####  ¿Qué debo hacer?

**No es necesario que realices ninguna acción. Las instancias principales de
GKE se actualizarán de forma automática con la frecuencia de actualización
habitual.** Si quieres actualizar la instancia principal antes, puedes [
iniciar una actualización de instancia principal de forma manual
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es_419#upgrading_the_cluster) .

Se actualizará este boletín a fin de incluir las versiones que contienen un
parche. Ten en cuenta que el parche solo estará disponible en las versiones
1.11 y posteriores, no en la versión 1.10.

####  ¿Qué vulnerabilidad trata este parche?

Con este parche, se mitiga la siguiente vulnerabilidad:

La vulnerabilidad [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) permite que un usuario desarrolle, en
especial, un parche de tipo “json-patch” que consuma cantidades excesivas de
CPU en el servidor de la API de Kubernetes, lo que puede reducir la
disponibilidad del plano de control de los clústeres.

|  Media  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  11 de febrero de 2019 (runc)

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Open Containers Initiative (OCI) [ descubrió hace poco
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=es_419#!topic/dev/Tc1ELm-8oDI)
una vulnerabilidad de seguridad nueva, ( [ CVE-2019-5736
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736) ) en runc, que
permite usar el escape de contenedores con el fin de obtener privilegios de
usuario raíz en el nodo host.

**Esta vulnerabilidad afecta a los nodos de Ubuntu en Google Kubernetes Engine
(GKE), por lo que te recomendamos[ actualizar
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es_419) a la versión de parche más reciente cuanto antes. Para
ello, sigue las instrucciones que se detallan a continuación. **

####  ¿Qué debo hacer?

Para poder actualizar los nodos, primero debes actualizar la instancia
principal a la versión más reciente. Este parche está disponible en Kubernetes
.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4, 1.12.5-gke.5 y en versiones más
recientes. Haz un seguimiento de la disponibilidad de estos parches en las [
notas de la versión ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#february-11-2019) .

Ten en cuenta que la vulnerabilidad solo afecta a los nodos de Ubuntu en GKE.
Los nodos que ejecutan COS no se ven afectados.

Ten en cuenta que la versión nueva de runc tiene un uso de memoria mayor, por
lo que es posible que debas actualizar la cantidad de memoria asignada a los
contenedores si configuraste límites de memoria bajos (inferiores a 16 MB).

####  ¿Qué vulnerabilidad trata este parche?

Este parche mitiga la siguiente vulnerabilidad:

[ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) es una vulnerabilidad en runc que permite
que un contenedor malicioso (con una interacción mínima del usuario, mediante
un ejecutable) reemplace el objeto binario runc del host para lograr la
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
puedes cambiar a la versión inferior 1.11.6, actualizar a la versión 1.12 o
esperar hasta que el parche 1.11.7 esté disponible en la semana del
04/03/2019.

Hace poco, se descubrió la vulnerabilidad de seguridad [ CVE-2019-6486
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-6486) en el lenguaje
de programación Go, que corresponde a una vulnerabilidad de denegación del
servicio (DoS) en las implementaciones de criptografía de las curvas elípticas
P-521 y P-384. En Google Kubernetes Engine (GKE), esta vulnerabilidad puede
permitir que un usuario desarrolle solicitudes maliciosas que consuman
cantidades excesivas de CPU en el servidor de la API de Kubernetes, lo que
puede reducir la disponibilidad del plano de control de los clústeres. Para
obtener más detalles, consulta la [ divulgación del lenguaje de programación
Go ](https://groups.google.com/forum/?hl=es_419#!topic/golang-
announce/mVeX35iXuSw) .

**Estas vulnerabilidades afectan a todas las instancias principales de Google
Kubernetes Engine (GKE). En la[ versión de parche más reciente
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#february-11-2019) , se incluye una mitigación para esta
vulnerabilidad. En las siguientes semanas, se actualizarán las instancias
principales de los clústeres a la versión de parche de manera automática, con
la frecuencia de actualización habitual. **

####  ¿Qué debo hacer?

**No es necesario que realices ninguna acción. Las instancias principale de
GKE se actualizarán de forma automática, con la frecuencia de actualización
habitual.** Si quieres actualizar la instancia principal antes, puedes [
iniciar una actualización de instancia principal de forma manual
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=es_419#upgrading_the_cluster) .

Este parche está disponible en GKE 1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4,
1.12.5-gke.5 y en actualizaciones más recientes.

####  ¿Qué vulnerabilidad trata este parche?

Con este parche, se mitiga la siguiente vulnerabilidad:

CVE-2019-6486 es una vulnerabilidad de las implementaciones de criptografía de
las curvas elípticas P-521 y P-384. Permite que un usuario desarrolle entradas
que consuman cantidades excesivas de CPU.

|  Alta  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  3 de diciembre de 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco, se descubrió una nueva vulnerabilidad de seguridad en Kubernetes,
la [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) , que habilita a un usuario con
privilegios bajos a omitir la autorización de las API de kubelet y, así,
ejecutar operaciones arbitrarias para cualquier pod de cualquier nodo en el
clúster. Para obtener más información, consulta la [ divulgación de Kubernetes
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-
announce/GVllWCg6L88) al respecto. **Estas vulnerabilidades afectaron a todas
las instancias principales de Google Kubernetes Engine (GKE), y ya se
actualizaron los clústeres a las[ versiones de parche más recientes
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#november-12-2018) . No es necesario que realices ninguna
acción. **

####  ¿Qué debo hacer?

**No es necesario que realices ninguna acción. Ya se actualizaron las
instancias principales de GKE.**

Este parche está disponible en GKE 1.9.7-gke.11, 1.10.6-gke.11, 1.10.7-gke.11,
1.10.9-gke.5, 1.11.2-gke.18 y en las versiones más recientes.

####  ¿Qué vulnerabilidad trata este parche?

Con este parche, se mitiga la siguiente vulnerabilidad:

La vulnerabilidad CVE-2018-1002105 permite que un usuario con privilegios
bajos omita la autorización de las API de kubelet. Esto habilita al usuario a
realizar solicitudes de actualización para escalar y realizar llamadas
arbitrarias a la API de kubelet. Esta vulnerabilidad se considera crítica en
Kubernetes. Debido a ciertos detalles en la implementación de GKE que
impidieron la ruta de escalamiento sin autenticación, la gravedad de esta
vulnerabilidad se clasificó como alta.

|  Alta  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  13 de noviembre de 2018

Descripción  
---  
  
**Actualización del 16/11/2018:** Se completó la revocación y rotación de
todos los tokens con sospecha de estar afectados. No es necesario que realices
ninguna otra acción.

Hace poco, Google descubrió un problema en el complemento de Container Network
Interface (CNI) de Calico que puede registrar información sensible cuando se
lo configura de cierta manera. A este problema lo está controlando la Asesoría
Técnica Tigera [ TTA-2018-001 ](https://www.projectcalico.org/security-
bulletins/) .

  * Cuando se ejecuta con el registro de nivel de depuración, el complemento de CNI de Calico escribirá la configuración del cliente de la API de Kubernetes en los registros. 
  * La CNI de Calico también escribirá el token de la API de Kubernetes en los registros en el nivel de información si el campo “k8s_auth_token” se estableció en la configuración de red de la CNI. 
  * Además, cuando se ejecuta con el registro de nivel de depuración, si el token de la cuenta de servicio se establece de forma explícita, ya sea en el archivo de configuración de Calico leído por Calico o como variables de entorno usadas por Calico, los componentes de Calico (calico/nodo, felix, CNI) escribirán esta información en los archivos de registro. 

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
Stackdriver Logging habilitados registraron tokens de cuenta de servicio de
Calico en Stackdriver. Los clústeres con no tienen la política de red
habilitada no se ven afectados.

Se implementó una corrección mediante la que se migra el complemento CNI de
Calico para que solo acceda en el nivel de advertencia y que use una nueva
cuenta de servicio. El código de Calico con el parche se implementará en una
versión posterior.

Durante la próxima semana, se realizará una revocación progresiva de todos los
tokens que pueden estar afectados. Este boletín se actualizará cuando se haya
completado la revocación. **No se requiere ninguna otra acción de tu parte.**
(Esta rotación se completó el 16/11/2018).

Si deseas rotar estos tokens de inmediato, puedes ejecutar el siguiente
comando; el nuevo secreto correspondiente a la cuenta de servicio se debe
volver a crear de forma automática en los segundos subsiguientes:  
      
    
    
        kubectl get sa --namespace kube-system calico -o template --template '{{(index .secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system
                
  
---  
  
####  Detección

GKE registra todos los accesos en el servidor de la API. Para determinar si se
usó un token de Calico fuera del rango de IP esperado de Google Cloud, puedes
ejecutar la siguiente consulta de Stackdriver. Ten en cuenta que solo se
mostrarán los registros de llamadas realizadas desde afuera de la red de GCP.
Te recomendamos que realices la personalización necesaria según tu entorno
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

Estas CVE se conocen en conjunto como “Falla de la terminal L1 (L1TF)”.

Estas vulnerabilidades L1TF aprovechan la ejecución especulativa por medio de
ataques a la configuración de las estructuras de datos en el procesador. “L1”
hace referencia a la caché Level‑1 Data (L1D), un recurso pequeño del núcleo
que se usa para acelerar el acceso a la memoria.

Consulta la [ entrada de blog de Google Cloud
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=es_419) para obtener más detalles sobre estas
vulnerabilidades y la mitigación de Compute Engine.

####  El impacto de Google Kubernetes Engine

La infraestructura que ejecuta Kubernetes Engine y aísla los clústeres y nodos
del cliente entre sí está protegida contra ataques conocidos.

Los grupos de nodos de Kubernetes Engine que usan una imagen de Container-
Optimized SO de Google y que tienen la [ actualización automática
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=es_419) habilitada se actualizarán de forma automática a las
versiones de parche de nuestra imagen de COS ni bien estén disponibles a
partir de la semana del 20/08/2018.

Los grupos de nodos de Kubernetes Engine que no tengan la [ actualización
automática ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=es_419) habilitada deberán [ actualizarse de forma manual
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=es_419) cuando estén disponibles las versiones de parche
de la imagen de COS.

|  Alta  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  6 de agosto de 2018; última actualización: 5 de septiembre de 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
####  Actualización del 05-09-2018

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) se divulgó hace poco. Al igual que con la
vulnerabilidad [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) , se trata de una vulnerabilidad de la red
en el kernel que aumenta la efectividad de los ataques de denegación del
servicio (DoS) contra sistemas vulnerables. La diferencia principal es que la
CVE-2018-5391 se puede usar en conexiones IP. Este boletín se actualizó a fin
de incluir ambas vulnerabilidades.

####  Descripción

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) (“SegmentSmack”) describe una
vulnerabilidad de la red en el kernel que aumenta la efectividad de los
ataques de denegación del servicio (DoS) contra sistemas vulnerables por medio
de conexiones TCP.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) (“FragmentSmack”) describe una
vulnerabilidad de la red en el kernel que aumenta la efectividad de los
ataques de denegación del servicio (DoS) contra sistemas vulnerables por medio
de conexiones IP.

####  El impacto de Google Kubernetes Engine

Desde el 11/08/2018, todas las instancias principales de Kubernetes Engine
están protegidas contra ambas vulnerabilidades. Además, todos los clústeres de
Kubernetes Engine configurados para actualizarse de forma automática también
están protegidos contra ambas vulnerabilidades. Estas dos vulnerabilidades
afectan a los grupos de nodos de Kubernetes Engine que no están configurados
para [ actualizarse de forma automática ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=es_419) y que se actualizaron de
forma manual por última vez antes del 11/08/2018.

####  Versiones de parche

Debido a la gravedad de esta vulnerabilidad, te recomendamos que [ actualices
manualmente ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=es_419#upgrading-nodes) los nodos en cuanto esté
disponible el parche.

|  Alta  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  30 de mayo de 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco, se descubrió una vulnerabilidad en Git que puede permitir la
elevación de privilegios en Kubernetes si usuarios sin privilegios tienen
permitido crear pods con volúmenes gitRepo. La CVE se identifica con la
etiqueta [ CVE-2018-11235 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-11235) .

####  ¿Me afecta esta vulnerabilidad?

Esta vulnerabilidad te afecta si las siguientes afirmaciones son verdad:

  * Los usuarios que no son de confianza pueden crear pods (o activar su creación). 
  * Los pods creados por usuarios que no son de confianza tienen restricciones que impiden el acceso raíz al host (por ejemplo, mediante [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=es_419) ). 
  * Los pods creados por usuarios que no son de confianza pueden usar el tipo de volumen gitRepo. 

Todos los nodos de Kubernetes Engine son vulnerables.

####  ¿Qué debo hacer?

Prohíbe el uso del tipo de volumen gitRepo. Para prohibir los volúmenes
gitRepo con PodSecurityPolicy, omite ` gitRepo ` de la lista blanca ` volumes
` en tu PodSecurityPolicy.

Se pueden lograr comportamientos equivalentes del volumen gitRepo si se clona
un repositorio de Git en un volumen EmptyDir de un initContainer, como se
indica a continuación:

    
    
    
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
  
Recientemente, se descubrieron diferentes vulnerabilidades en el kernel de
Linux que pueden permitir la elevación de privilegios o la denegación del
servicio (mediante el fallo del kernel) a partir de un proceso sin
privilegios. Estas CVE se identifican con las etiquetas [ CVE-2018-1000199
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199) , [
CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
y [ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) . Estas vulnerabilidades afectan a todos
los nodos de Kubernetes Engine, por lo que te recomendamos [ actualizar
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=es_419) a la versión de parche más reciente, como se
muestra a continuación.

####  ¿Qué debo hacer?

Para poder actualizar los nodos, primero debes actualizar la instancia
principal a la versión más reciente. El parche está disponible en Kubernetes
Engine 1.8.12-gke.1, Kubernetes Engine 1.9.7-gke.1 y Kubernetes Engine
1.10.2-gke.1. Estas versiones incluyen parches para imágenes de Container-
Optimized OS y Ubuntu.

Si creas un clúster nuevo antes, debes especificar la versión de parche que
debe usarse. A los clientes que tengan las [ actualizaciones automáticas de
nodo ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=es_419) habilitadas y no hagan la actualización de forma manual,
se les actualizarán los nodos a la versión de parche en las próximas semanas.

####  ¿Qué vulnerabilidades trata este parche?

Con este parche, se mitigan las siguientes vulnerabilidades:

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : Esta vulnerabilidad afecta el kernel
de Linux. Permite que un usuario o proceso sin privilegios cause una falla en
el kernel del sistema, lo que lleva a un ataque DoS o la elevación de
privilegios. Tiene una calificación de vulnerabilidad alta, con un puntaje de
7.8 según el CVSS.

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : Esta vulnerabilidad afecta el kernel de
Linux. Permite que un usuario o proceso sin privilegios cause una falla en el
kernel del sistema, lo que lleva a un ataque DoS. Tiene una calificación de
vulnerabilidad media, con puntaje de 6.5 según el CVSS.

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : Esta vulnerabilidad afecta el hipervisor
KVM del kernel de Linux. Permite que un proceso sin privilegios cause una
falla en el kernel invitado o que pueda adquirir privilegios. La
vulnerabilidad tiene un parche en la infraestructura sobre la que se ejecuta
Kubernetes Engine, por lo que Kubernetes Engine no se ve afectado. Tiene una
calificación de vulnerabilidad alta, con un puntaje de 8.0 según el CVSS.

|  Alta  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  12 de marzo de 2018

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
El proyecto Kubernetes [ divulgó recientemente
](https://groups.google.com/forum/?hl=es_419#!topic/kubernetes-security-
announce/P7lBjbjDKd8) vulnerabilidades de seguridad nuevas ( [
CVE-2017-1002101 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002101) y [ CVE-2017-1002102
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102) ) que permiten
que los contenedores accedan a archivos externos. Estas vulnerabilidades
afectan a todos los nodos de Kubernetes Engine, por lo que te recomendamos
actualizar a la versión de parche más reciente tan pronto como sea posible,
como se muestra a continuación.

####  ¿Qué debo hacer?

Debido a la gravedad de estas vulnerabilidades, ya sea que hayas habilitado
las actualizaciones automáticas de nodos o no, te recomendamos [ actualizar de
forma manual ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=es_419) tus nodos ni bien esté disponible
el parche. En el [ programa de lanzamientos
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=es_419#march-12-2018) , se indica que este parche estará disponible
para todos los clientes a partir del 16 de marzo, pero es posible que esté
disponible para ti antes, según la zona en la que se encuentra tu clúster.

Para poder actualizar los nodos, primero debes actualizar la instancia
principal a la versión más reciente. Este parche estará disponible en
Kubernetes 1.9.4-gke.1, Kubernetes 1.8.9-gke.1 y Kubernetes 1.7.14-gke.1. Los
clústeres nuevos usarán la versión de parche de forma predeterminada a partir
del 30 de marzo. Si creas un clúster nuevo antes de esa fecha, deberás
especificar la versión de parche que debe usarse.

A los clientes de Kubernetes Engine que tengan las [ actualizaciones
automáticas de nodos ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=es_419) habilitadas y no hagan la
actualización de forma manual, se les actualizarán los nodos a la versión de
parche antes del 23 de abril. Sin embargo, debido a la gravedad de estas
vulnerabilidades, recomendamos [ actualizar los nodos de forma manual
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=es_419) en cuanto esté disponible el parche.

####  ¿Qué vulnerabilidades trata este parche?

Con este parche, se mitigan las siguientes vulnerabilidades:

La vulnerabilidad CVE-2017-1002101 permite que los contenedores que usan
activaciones de volumen [ subPath
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) tengan
acceso a archivos externos al volumen. Eso significa que si estás bloqueando
el acceso de los contenedores a volúmenes de la ruta del host con
PodSecurityPolicy, un atacante con la capacidad para actualizar o crear pods
puede activar cualquier ruta del host mediante cualquier otro tipo de volumen.

La vulnerabilidad CVE-2017-1002102 permite que los contenedores que usan
ciertos tipos de volúmenes (incluidos los secretos, mapas de configuración,
volúmenes proyectados o volúmenes de la API descendentes) borren archivos
externos al volumen. Esto significa que si un contenedor que usa uno de estos
tipos de volúmenes se ve afectado, o si permites que usuarios que no son de
confianza creen pods, un atacante puede usar ese contenedor para borrar
archivos arbitrarios en el host.

Para obtener más información sobre la corrección, lee la [ entrada de blog de
Kubernetes ](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-
vulnerability/) .

|  Alta  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

