A new version of Anthos GKE on AWS was released on August 5. See the [ release
notes ](https://cloud.google.com/anthos/gke/docs/aws/release-notes?hl=es-419)
for information on breaking changes.

#  Boletines de seguridad

Obtén información sobre los boletines de seguridad de Anthos GKE on AWS (GKE
on AWS).

##  GCP-2020-011

**Publicado:** 24/07/2020  
Descripción  |  Gravedad  |  Notas  
---|---|---  
  
En la actualidad, se descubrió una vulnerabilidad en las herramientas de
redes, [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) , en Kubernetes. A
veces, los servicios se comunican con otras aplicaciones que se ejecutan
dentro del mismo Pod mediante la interfaz de bucle invertido local
(127.0.0.1). Esta vulnerabilidad permite que un atacante con acceso a la red
del clúster envíe tráfico a la interfaz de bucle invertido de Pods y nodos
adyacentes. Podrían aprovecharse los servicios que dependen de que no se pueda
acceder a la interfaz de bucle invertido fuera del Pod.

Para aprovechar esta vulnerabilidad en los clústeres de GKE on AWS, el
atacante debe inhabilitar las [ verificaciones de destino de origen
](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html) en
las instancias de EC2 en el clúster. El atacante debería tener permisos de IAM
de AWS para ` ModifyInstanceAttribute ` o ` ModifyNetworkInterfaceAttribute `
en las instancias de EC2. Por esta razón, a esta vulnerabilidad se le asignó
un nivel bajo de gravedad para GKE on AWS.

####  ¿Qué debo hacer?

Para corregir esta vulnerabilidad, actualiza el clúster a una versión de
parche. Se espera que las próximas versiones de GKE on AWS o las versiones
posteriores incluyan la corrección para esta vulnerabilidad:

  * GKE on AWS 1.4.2 

####  ¿Qué vulnerabilidad trata este parche?

Este parche corrige la siguiente vulnerabilidad: [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) .

|

Baja

|

[ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315)  
  
##  GCP-2020-009

**Publicado:** 15/0/2020  Descripción  |  Gravedad  |  Notas  
---|---|---  
  
En la actualidad, se descubrió una vulnerabilidad de elevación de privilegios,
[ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559) , en Kubernetes. Esta vulnerabilidad
permite que un atacante que ya haya comprometido un nodo pueda ejecutar un
comando en cualquier Pod del clúster. Por lo tanto, existe la posibilidad de
que el atacante use el nodo ya comprometido para comprometer otros nodos y
leer información o causar acciones destructivas.

Ten en cuenta que, para que un atacante pueda aprovechar esta vulnerabilidad,
un nodo del clúster ya debe estar comprometido. Esta vulnerabilidad, por sí
sola, no comprometerá ningún nodo del clúster.

####  ¿Qué debo hacer?

La versión de GKE on AWS de disponibilidad general (1.4.1, disponible a fines
de julio de 2020), o versiones posteriores, incluye el parche para esta
vulnerabilidad. Si usas una versión anterior, [ descarga una versión nueva de
la herramienta de línea de comandos de anthos-gke
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=es-419)
y vuelve a crear los clústeres de administrador y de usuario.

####  ¿Qué vulnerabilidad trata este parche?

Estos parches mitigan la vulnerabilidad CVE-2020-8559. Esta se considera una
vulnerabilidad de nivel medio para GKE, ya que requiere que el atacante tenga
información de primera mano sobre el clúster, los nodos y las cargas de
trabajo para aprovechar este ataque de manera efectiva, además de un nodo
existente ya comprometido. Esta vulnerabilidad no le proporcionará un nodo
comprometido a un atacante.

|

Media

|

[ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559)  
  
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
más reciente del parche, como se muestra a continuación. No es necesario
actualizar los nodos.  

####  ¿Qué debo hacer?

Anthos GKE on AWS (GKE on AWS) v0.2.0 o posterior ya incluye el parche para
esta vulnerabilidad. Si usas una versión anterior, [ descarga una versión
nueva de la herramienta de línea de comandos de anthos-gke
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=es-419)
y vuelve a crear los clústeres de administrador y de usuario.

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
contenedor con privilegios redireccione el tráfico de nodo a otro contenedor.
El atacante no puede leer ni modificar el tráfico mutuo de TLS/SSH, como aquel
entre el kubelet y el servidor de la API, o el tráfico desde aplicaciones
mediante mTLS. Esta vulnerabilidad afecta a todos los nodos de Google
Kubernetes Engine (GKE). Te recomendamos actualizar a la versión más reciente
del parche, como se muestra a continuación.

####  ¿Qué debo hacer?

[ Descarga la herramienta de línea de comandos de anthos-gke
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=es-419)
con la siguiente versión o una más reciente y vuelve a crear los clústeres de
administrador y de usuario:

  * aws-0.2.1-gke.7 

Por lo general, muy pocos contenedores requieren ` CAP_NET_RAW ` . Esta y
otras capacidades potentes se deben bloquear de forma predeterminada mediante
el [ controlador de políticas de Anthos ](https://cloud.google.com/anthos-
config-management/docs/concepts/policy-controller?hl=es-419) o la
actualización de las especificaciones del Pod:

Descarta la capacidad ` CAP_NET_RAW ` de los contenedores:

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
    

  * O actualiza las especificaciones del Pod: 
    
        
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

