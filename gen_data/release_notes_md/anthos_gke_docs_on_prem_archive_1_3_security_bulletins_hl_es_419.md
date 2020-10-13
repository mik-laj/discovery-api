You are viewing documentation for a previous version of Anthos GKE on-prem. [
View the latest documentation ](https://cloud.google.com/anthos/gke/docs/on-
prem?hl=es-419) .

#  Boletines de seguridad

Todos los boletines de seguridad para Anthos GKE On-Prem (GKE On-Prem) se
describen en este tema.

Las vulnerabilidades se suelen mantener en secreto y no se las puede divulgar
hasta que las partes afectadas hayan tenido la oportunidad de tratar el tema.
En estos casos, las [ notas de la versión
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.3/release-
notes?hl=es-419) de GKE On-Prem harán referencia a las “actualizaciones de
seguridad” hasta que se apruebe la divulgación. En ese momento, las notas se
actualizarán para reflejar la vulnerabilidad tratada en el parche.

**Nota:** Si ejecutas cargas de trabajo de multiusuarios en GKE On-Prem,
presta especial atención a estos boletines. Es más probable que estas
vulnerabilidades afecten a cargas de trabajo de multiusuarios. Para obtener
una descripción técnica de los límites de seguridad en GKE On-Prem y del
efecto que tienen en las cargas de trabajo, consulta [ Aislamiento en
distintas capas de la pila de Kubernetes
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Para recibir los boletines de seguridad más recientes, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  GCP-2020-007

**Fecha de publicación:** 1 de junio de 2020  
Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Recientemente, se descubrió la vulnerabilidad de falsificación de solicitudes
del servidor (SSRF) [ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555) en Kubernetes, que permitió a ciertos
usuarios autorizados filtrar hasta 500 bytes de información sensible desde la
red host del plano de control. En el plano de control de Google Kubernetes
Engine (GKE), se usan controladores de Kubernetes a los que afecta esta
vulnerabilidad. Te recomendamos actualizar el plano de control a la versión
más reciente del parche, como se detalla a continuación. No es necesario
actualizar los nodos.  

####  ¿Qué debo hacer?

En las siguientes versiones o en otras más recientes de Anthos GKE On-Prem
(GKE On-Prem), se incluye la solución para esta vulnerabilidad:

  * Anthos 1.3.0 

Si usas una versión anterior, [ actualiza el clúster existente
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.3/how-
to/upgrading?hl=es-419) a una versión en la que se incluya la solución.

####  ¿Qué vulnerabilidad trata este parche?

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
contenedor con privilegios redireccione el tráfico de nodo a otro contenedor.
El ataque no permite leer ni modificar el tráfico mutuo de TLS/SSH, como aquel
entre el kubelet y el servidor de la API, o el tráfico desde aplicaciones
mediante mTLS. Esta vulnerabilidad afecta a todos los nodos de Google
Kubernetes Engine (GKE). Te recomendamos actualizar a la versión más reciente
del parche, como se detalla a continuación.

####  ¿Qué debo hacer?

Si deseas mitigar esta vulnerabilidad para Anthos GKE On-Prem (GKE On-Prem), [
actualiza tus clústeres ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/how-to/upgrading?hl=es-419) a la siguiente versión o a otra
más reciente:

  * Anthos 1.3.2 

Por lo general, muy pocos contenedores requieren ` CAP_NET_RAW ` . Esta y
otras capacidades potentes se deben bloquear de forma predeterminada mediante
el [ controlador de políticas de Anthos ](https://cloud.google.com/anthos-
config-management/docs/concepts/policy-controller?hl=es-419) o la
actualización de las especificaciones del pod:

  * Descarta la capacidad ` CAP_NET_RAW ` de los contenedores: 
    * Puedes hacer esto si usas el controlador de políticas de Anthos o Gatekeeper con esta [ plantilla de restricciones ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) y la aplicas, como se muestra en el siguiente ejemplo: 
        
                
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
        

    * También puedes hacerlo mediante la actualización de las especificaciones del pod: 
        
                
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
  
  
##  GCP-2020-004

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco, se descubrió una vulnerabilidad en Kubernetes, descrita en [
CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) , que permite que cualquier usuario con
autorización para realizar solicitudes POST ejecute un ataque de denegación
del servicio de forma remota en un servidor de la API de Kubernetes. El Comité
de seguridad de productos (PSC) de Kubernetes publicó información adicional
sobre esta vulnerabilidad, que puedes encontrar [ aquí
](https://groups.google.com/g/kubernetes-security-
announce/c/wuwEwZigXBc?hl=es-419) .

Puedes mitigar esta vulnerabilidad si limitas qué clientes tienen acceso a la
red de los servidores de la API de Kubernetes.

####  ¿Qué debo hacer?

Te recomendamos actualizar los clústeres a versiones del parche en las que se
incluya la solución para esta vulnerabilidad en cuanto estén disponibles.

Estas son las versiones de parche que incluyen la corrección:

  * Anthos 1.3.0, que ejecuta la versión 1.15.7-gke.32 de Kubernetes 

####  ¿Qué vulnerabilidades trata este parche?

El parche corrige la siguiente vulnerabilidad de denegación del servicio
(DoS):

[ CVE‑2019‑11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)

|

Media

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  16 de octubre de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco, se descubrió una vulnerabilidad en Kubernetes, la cual se describe
en [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) , que permite que cualquier usuario
autorizado realice solicitudes POST para ejecutar un ataque a distancia de
denegación del servicio en un servidor de la API de Kubernetes. El comité de
seguridad de los productos (PSC) de Kubernetes difundió información adicional
sobre esta vulnerabilidad, que puedes encontrar [ aquí
](https://groups.google.com/forum/?hl=es-419#!topic/kubernetes-security-
announce/jk8polzSUxs) .

Puedes mitigar esta vulnerabilidad si limitas qué clientes tienen acceso a la
red de los servidores de la API de Kubernetes.

######  ¿Qué debo hacer?

Te recomendamos [ actualizar el clúster
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.3/how-
to/upgrading-clusters?hl=es-419) a una versión del parche en la que se incluya
la solución en cuanto esté disponible.

Las versiones del parche en las que se incluirá la solución se enumeran a
continuación:

  * Anthos 1.1.1, que ejecuta la versión 1.13.7-gke.30 de Kubernetes 

######  ¿Qué vulnerabilidad trata este parche?

Mediante el parche, se mitiga la siguiente vulnerabilidad: [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) .

|

Alta

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
##  23 de agosto de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco, descubrimos y mitigamos una vulnerabilidad en la que el proxy de
RBAC que se usa para asegurar los extremos de supervisión no autorizaba a los
usuarios de forma adecuada. Como resultado, usuarios no autorizados pueden
obtener métricas de ciertos componentes desde el interior de la red interna
del clúster. Los siguientes componentes se vieron afectados:

  * ` etcd `
  * ` etcd-events `
  * ` kube-apiserver `
  * ` kube-controller-manager `
  * ` kube-scheduler `
  * ` node-exporter `
  * ` kube-state-metrics `
  * ` prometheus `
  * ` alertmanager `

######  ¿Qué debo hacer?

Te recomendamos [ actualizar ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/how-to/upgrading-clusters?hl=es-419) los clústeres a la
versión [ 1.0.2-gke.3 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/downloads?hl=es-419#gkectl_latest) , en la que se incluye el
parche para esta vulnerabilidad, lo antes posible.

|

Media

|

[ Versiones de Anthos GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/downloads?hl=es-419#gkectl_latest)  
  
##  22 de agosto de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
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

Te recomendamos [ actualizar ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/how-to/upgrading-clusters?hl=es-419) los clústeres a la
versión [ 1.0.2-gke.3 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/downloads?hl=es-419#gkectl_latest) , en la que se incluye el
parche para esta vulnerabilidad, lo antes posible.

######  ¿Qué vulnerabilidad trata este parche?

El parche mitiga la siguiente vulnerabilidad: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Media

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

