Consulta la documentación de una versión anterior de GKE On-Prem. [ Consulta
la documentación más reciente ](https://cloud.google.com/anthos/gke/docs/on-
prem?hl=es-419) .

#  Boletines de seguridad

Todos los boletines de seguridad de GKE On-Prem se describen en este tema.

Las vulnerabilidades se suelen mantener en secreto y no se las puede divulgar
hasta que las partes afectadas hayan tenido la oportunidad de tratar el tema.
En estos casos, las [ notas de la versión
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/release-
notes?hl=es-419) de GKE On-Prem harán referencia a las "actualizaciones de
seguridad" hasta que se apruebe la divulgación. En ese momento, las notas se
actualizarán para reflejar la vulnerabilidad tratada en el parche.

**Nota:** Si ejecutas cargas de trabajo de varias instancias en GKE On-Prem,
presta especial atención a estos boletines. Es más probable que estas
vulnerabilidades afecten a cargas de trabajo de instancias múltiples. Para
obtener una descripción técnica de los límites de seguridad en GKE On-Prem y
cómo estos afectan las cargas de trabajo, consulta [ Aislamiento en diferentes
capas de la pila de Kubernetes
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Para recibir los boletines de seguridad más recientes, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  16 de octubre de 2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco tiempo, se descubrió una vulnerabilidad en Kubernetes, descrita en [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) , que permite que cualquier usuario
autorizado haga solicitudes POST para ejecutar un ataque a distancia de
denegación del servicio en un servidor de la API de Kubernetes. El Product
Security Committee (PSC) de Kubernetes publicó información adicional sobre
esta vulnerabilidad, que puedes encontrar [ aquí
](https://groups.google.com/forum/?hl=es-419#!topic/kubernetes-security-
announce/jk8polzSUxs) .

Puedes mitigar esta vulnerabilidad si limitas qué clientes tienen acceso a la
red a tus servidores de API de Kubernetes.

######  ¿Qué debo hacer?

Te recomendamos [ actualizar tus clústeres
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters?hl=es-419) a una versión de parche que
contenga la corrección en cuanto esté disponible.

Las versiones del parche que contendrán la corrección se enumeran a
continuación:

  * Anthos 1.1.1, que ejecuta la versión 1.13.7-gke.30 de Kubernetes 

######  ¿Qué vulnerabilidad trata este parche?

El parche mitiga la siguiente vulnerabilidad: [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) .

|

Alta

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
##  #august-05-2019

Descripción  |  Gravedad  |  Notas  
---|---|---  
  
Hace poco, descubrimos y mitigamos una vulnerabilidad en la que el proxy de
RBAC que se usa para los extremos de supervisión de seguridad no autorizaba a
los usuarios de forma correcta. Como resultado, las métricas de ciertos
componentes están disponibles para los usuarios no autorizados desde la red
interna del clúster. Los siguientes componentes se vieron afectados:

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
prem/archive/1.1/how-to/administration/upgrading-clusters?hl=es-419) tus
clústeres a la versión [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/downloads?hl=es-419#gkectl_latest) , que incluye el parche
para esta vulnerabilidad, lo antes posible.

|

Medio

|

[ Versiones de GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/downloads?hl=es-419#gkectl_latest)  
  
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
prem/archive/1.1/how-to/administration/upgrading-clusters?hl=es-419) tus
clústeres a la versión [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/downloads?hl=es-419#gkectl_latest) , que incluye el parche
para esta vulnerabilidad, lo antes posible.

######  ¿Qué vulnerabilidad trata este parche?

El parche mitiga la siguiente vulnerabilidad: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Media

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

