#  Notas de la versión

En esta página, se documentan las actualizaciones de producción de Anthos GKE
On-Prem. Puedes revisar esta página de forma periódica para ver anuncios sobre
características nuevas o actualizadas, correcciones de errores, problemas
conocidos y funciones obsoletas.

También consulta lo siguiente:

  * [ Descargas ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=es-419)
  * [ Control de versiones y actualizaciones ](https://cloud.google.com/anthos/gke/docs/on-prem/versioning-and-upgrades?hl=es-419)
  * [ Actualizar GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=es-419)

Puedes ver las últimas actualizaciones de productos de todo Google Cloud en la
página [ Notas de la versión de Google Cloud
](https://cloud.google.com/release-notes?hl=es-419) .

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) o agrega
directamente la URL del feed: ` https://cloud.google.com/feeds/gkeonprem-
release-notes.xml `

##  19 de noviembre de 2019

Ya está disponible la versión 1.1.2-gke.0 de GKE local. Para descargar la
versión OVA de 1.1.2-gke.0, ` gkectl ` , y el paquete de actualización,
consulta [ Descargas ](https://cloud.google.com/anthos/gke/docs/on-
prem/downloads?hl=es-419#latest) . Luego, consulta [ Actualiza una estación de
trabajo de administrador ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/upgrading?hl=es-419) y [ Actualiza clústeres
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=es-419)
.

Esta versión del parche incluye los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

Se publicó [ Endurecimiento de tu clúster
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/security/hardening-your-cluster?hl=es-419) .

**FEATURE:**

Se publicó [ Cómo administrar clústeres
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/managing-clusters?hl=es-419) .

###  Ajustes

**FIXED:**

Se solucionó el problema conocido desde el  5 de noviembre  .

**FIXED:**

Se solucionó el problema conocido desde el  8 de noviembre  .

###  Problemas conocidos

**ISSUE:**

Si ejecutas varios centros de datos en vSphere, la ejecución de ` gkectl
diagnose cluster ` puede mostrar el siguiente error, que puedes ignorar de
forma segura:

    
    
    Checking storage...FAIL
    path '*' resolves to multiple datacenters

**ISSUE:**

Si ejecutas un almacén de datos de vSAN, la ejecución de ` gkectl diagnose
cluster ` podría mostrar el siguiente error, que puedes ignorar de manera
segura:

    
    
    PersistentVolume [NAME]: virtual disk "[[DATASTORE_NAME]]
    [PVC]" IS NOT attached to machine "[MACHINE_NAME]" but IS listed in the Node.Status

##  8 de noviembre de 2019

**ISSUE:**

En la versión 1.1.1-gke.2 de GKE local, un problema conocido impide la
creación de clústeres configurados para usar un registro de Docker. Para
configurar un registro de Docker, propaga el campo ` privateregistryconfig `
del archivo de configuración local de GKE. La creación del clúster falla con
un error como ` Failed to create root cluster: could not create external
client: could not create external control plane: docker run error: exit status
125 `

Una corrección está dirigida a la versión 1.1.2. Mientras tanto, si deseas
crear un clúster configurado para usar un registro de Docker, pasa la marca `
--skip-validation-docker ` a ` gkectl create cluster ` .

##  5 de noviembre de 2019

**ISSUE:**

El archivo de configuración de GKE local tiene un campo, ` vcenter.datadisk `
, que busca una ruta a un archivo de disco de máquina virtual (VMDK). Durante
la instalación, eliges un nombre para la VMDK. De forma predeterminada, GKE
local crea un VMDK y lo guarda en la raíz de tu almacén de datos de vSphere.

Si usas un almacén de datos de SAN, debes crear una carpeta en el almacén de
datos en el que se guardará la VMDK. Proporciona la ruta completa al campo,
por ejemplo, ` datadisk: anthos/gke/docs/on-prem/datadisk.vmdk ` , y GKE local
guarda el VMDK en esa carpeta.

Cuando creas la carpeta, vSphere asigna a la carpeta un identificador único
universal (UUID). Aunque proporcionas la ruta de acceso a la carpeta de la
configuración de GKE local, la API de vSphere busca el UUID de la carpeta.
Actualmente, esta discrepancia puede causar la creación de clústeres y las
actualizaciones.

Una corrección está dirigida a la versión 1.1.2. Mientras tanto, debes
proporcionar el UUID de la carpeta en lugar de la ruta de la carpeta. Sigue
las instrucciones alternativas que se encuentran disponibles en la sección
sobre [ cómo actualizar clústeres
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters?hl=es-419#admin_datadisk_folder) y los
temas de instalación.

##  25 de octubre de 2019

La versión 1.1.1-gke.2 de GKE local ahora está disponible. Para descargar la
versión 1.1.1-gke.2 de OVA, ` gkectl ` y el paquete de actualización, consulta
[ Descargas ](https://cloud.google.com/anthos/gke/docs/on-
prem/downloads?hl=es-419#latest) . Luego, consulta [ Actualiza la estación de
trabajo de administrador ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/upgrading?hl=es-419) y [ Actualiza clústeres
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=es-419)
.

Esta versión del parche incluye los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

**Acción necesaria:** Esta versión actualiza la versión mínima de ` gcloud `
de la estación de trabajo de administrador a 256.0.0. Debes [ actualizar tu
estación de trabajo de administrador
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-admin-workstation?hl=es-419) . Luego, debes [
actualizar tus clústeres ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/upgrading-clusters?hl=es-419) .

**FEATURE:**

La [ caja de herramientas de CoreOS ](https://github.com/coreos/toolbox) de
código abierto ahora se incluye en todos los nodos del clúster local de GKE.
Este conjunto de herramientas es útil para solucionar problemas de nodos.
Consulta [ Cómo depurar problemas de nodos con la caja de herramientas
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/toolbox?hl=es-419) .

###  Ajustes

**FIXED:**

Se solucionó un problema que impedía la actualización de los clústeres
configurados con OIDC.

**FIXED:**

Se corrigió [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) que se describe en [ Boletines de
seguridad ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/security-bulletins?hl=es-419#october-16-2019) .

**FIXED:**

Se solucionó un problema que provocaba la pérdida de las métricas del clúster
debido a una pérdida de conexión a Google Cloud. Cuando se pierde la conexión
de un clúster local de GKE a Google Cloud por un período de tiempo, las
métricas de ese clúster se recuperan por completo.

**FIXED:**

Se solucionó un problema que causaba que la transferencia de las métricas del
clúster del administrador fuera más lenta que la transferencia de las métricas
del clúster de usuarios.

###  Problemas conocidos

**ISSUE:**

Para los clústeres de usuario que usan IP estáticas y una red diferente de su
clúster de administración: si reemplazas la configuración de red del clúster
de usuarios, es posible que el plano de control de usuario no pueda iniciarse.
Esto ocurre porque usa la red del clúster del usuario, pero asigna una
dirección IP y una puerta de enlace desde el clúster del administrador.

Como solución alternativa, puedes actualizar la especificación
MachineDeployment de cada plano de control de usuario para usar la red
correcta. Luego, borra cada máquina de plano de control de usuario, lo que
hace que MachineDeployment cree máquinas nuevas:

  1.     # List MachineDeployments in the admin cluster
        kubectl get machinedeployments --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

  2.     # Update a user control plane MachineDeployment from your shell
        kubectl edit machinedeployment --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINEDEPLOYMENT_NAME]

  3.     # List Machines in the admin cluster
        kubectl get machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

  4.     # Delete user control plane Machines in the admin cluster
        kubectl delete machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINE_NAME]

##  26 de septiembre de 2019

Ya está disponible la versión 1.1.0-gke.6 de GKE local. Para descargar la
versión ` gkectl ` de 1.1.0-gke.6 y el paquete de actualización, consulta [
Descargas ](https://cloud.google.com/anthos/gke/docs/on-
prem/downloads?hl=es-419#latest) . Luego, consulta [ Actualiza clústeres
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=es-419)
.

Esta versión secundaria incluye los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

La versión predeterminada de Kubernetes para los nodos del clúster ahora es la
versión 1.13.7-gke.20 (anteriormente, 1.12.7-gke.19).

**FEATURE:**

**Acción necesaria:** A partir de la versión 1.1.0-gke.6, GKE local crea
reglas de [ Programador de recursos distribuido (DRS)
](https://www.vmware.com/products/vsphere/drs-dpm.html) para los nodos de tu
clúster de usuario (VM de vSphere). ), lo que hace que se distribuyan en al
menos tres hosts físicos del centro de datos.

**Esta función está habilitada de forma predeterminada para todos los
clústeres de usuarios nuevos y existentes que ejecutan la versión
1.1.0-gke.6.**

La característica requiere que tu entorno de vSphere cumpla con las siguientes
condiciones:

  * VMware DRS debe estar habilitado. Para DRS de VMware, se requiere la edición de licencia de vSphere Enterprise Plus. Para aprender a habilitar DRS, consulta [ Habilita DRS de VMware en un clúster ](https://kb.vmware.com/s/article/1034280) . 
  * La cuenta de usuario de vSphere que se proporciona en el campo ` vcenter ` del archivo de configuración local de GKE debe tener el permiso ` Host.Inventory.EditCluster ` . 
  * Hay al menos tres hosts físicos disponibles. 

Si _no_ deseas habilitar esta función para tus clústeres de usuarios
existentes, por ejemplo, si no tienes suficientes hosts que cumplan la
función, realiza los siguientes pasos _antes_ de actualizar tus clústeres de
usuario:

  1. Abre tu archivo de configuración de GKE On-Prem existente. 
  2. En la especificación ` usercluster ` , agrega el campo ` antiaffinitygroups ` como se describe en la [ documentación de ` antiaffinitygroups ` ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-to/installation/install?hl=es-419#antiaffinitygroups) : 
    
        usercluster:
          ...
          antiaffinitygroups:
            enabled: false
    

  3. Guarde el archivo. 
  4. Usa el archivo de configuración para actualizar. Tus clústeres están actualizados, pero la función no está habilitada. 

**FEATURE:**

Ahora puedes establecer la [ clase de almacenamiento predeterminada
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/default-storage-class?hl=es-419) para tus clústeres.

**FEATURE:**

Ahora puedes usar [ Container Storage Interface (CSI) 1.0
](https://github.com/container-storage-interface/spec) como una clase de
almacenamiento para tus clústeres.

**FEATURE:**

Ahora puedes [ borrar los clústeres de usuarios dañados o en mal estado
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/deleting-a-user-cluster?hl=es-419#delete_unhealthy_cluster)
con ` gkectl delete cluster --force ` .

**FEATURE:**

Ahora puedes [ diagnosticar problemas de nodos
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/support/debug-
toolbox?hl=es-419) con la imagen de contenedor ` debug-toolbox ` .

**FEATURE:**

Ahora puedes [ omitir invalidaciones
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=es-419#skip_validate) ejecutando los comandos `
gkectl ` .

**FEATURE:**

El tarball que crea ` gkectl diagnose snapshot ` ahora incluye un registro del
resultado del comando de forma predeterminada.

**FEATURE:**

Agrega la marca ` gkectl diagnose snapshot ` ` --seed-config ` . Cuando pasas
la marca, incluye el archivo de configuración local de GKE de tus clústeres en
el archivo tarball proporcionado por ` snapshot ` .

###  Cambios

**CHANGED:**

Se quitó el campo ` gkeplatformversion ` del archivo de configuración local de
GKE. Para especificar la versión de un clúster, proporciona el paquete de la
versión en el campo ` bundlepath ` .

**CHANGED:**

Debes agregar el permiso de vSphere, ` Host.Inventory.EditCluster ` , antes de
poder usar [ ` antiaffinitygroups `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=es-419#antiaffinitygroups) .

**CHANGED:**

Ahora especifica un archivo de configuración en ` gkectl diagnose snapshot `
pasando el ` --snapshot-config ` (antes ` --config ` ). Consulta [ Cómo
diagnosticar problemas del clúster
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/diagnose?hl=es-419#diagnose_snapshot) .

**CHANGED:**

Ahora puedes capturar el archivo de configuración de tu clúster con ` gkectl
diagnose snapshot ` si pasas ` --snapshot-config ` (anteriormente ` --config `
). Consulta [ Cómo diagnosticar problemas con los clústeres
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/diagnose?hl=es-419#diagnose_snapshot) .

**CHANGED:**

Los comandos ` gkectl diagnose ` ahora muestran un error si proporcionas un
kubeconfig de un clúster de usuario, en lugar de kubeconfig de un clúster de
administración.

**CHANGED:**

Cloud Console ahora te notifica cuando una actualización está disponible para
un clúster de usuario registrado.

###  Problemas conocidos

**ISSUE:**

Un problema conocido impide que los clústeres de las versiones 1.0.11,
1.0.1-gke.5 y 1.0.2-gke.3 que usan OIDC se actualicen a la versión 1.1. Una
corrección está dirigida a la versión 1.1.1. Si configuraste un clúster de la
versión 1.0.11, 1.0.1-gke.5 o 1.0.2-gke.3 con OIDC, no podrás actualizarlo.
Para crear un clúster de la versión 1.1, sigue [ Instala GKE local
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/install?hl=es-419) .

##  22 de agosto de 2019

La versión 1.0.2-gke.3 de GKE local ahora está disponible. Esta versión de
parche incluye los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

Se admite Seesaw para el balanceo de cargas manual.

**FEATURE:**

Ahora puedes especificar una red de vSphere diferente para los clústeres de
administrador y usuario.

**FEATURE:**

Ahora puedes borrar clústeres de usuarios con ` gkectl ` . Consulta [ Borra un
clúster de usuario ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/deleting-a-user-cluster?hl=es-419) .

###  Cambios

**CHANGED:** Ahora ` gkectl diagnose snapshot ` obtiene los registros de los
planos de control de los clústeres de usuario.

**CHANGED:**

La especificación OIDC de GKE On-Prem se actualizó con varios campos nuevos: `
kubectlredirecturl ` , ` scopes ` , ` extraparams ` y ` usehttpproxy ` .

**CHANGED:**

Calico se actualizó a la versión 3.7.4.

**CHANGED:**

Las métricas del sistema de Cloud Monitoring cambiaron de `
external.googleapis.com/prometheus/ ` a ` kubernetes.io/anthos/ ` . Si realiza
el seguimiento de métricas o alertas, actualice sus paneles con el siguiente
prefijo.

###  Fijo

**FIXED:**

[ Se corrigió una vulnerabilidad de CVE-2019-11247
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/security-
bulletins?hl=es-419#august-22-2019) .

**FIXED:**

[ Se corrigió una vulnerabilidad en el proxy RBAC
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/security-
bulletins?hl=es-419#august-23-2019) .

##  30 de julio de 2019

Ya está disponible la versión 1.0.1-gke.5 de GKE local. Esta versión del
parche incluye los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

[ Hoja de referencia de GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/reference/cheatsheet?hl=es-419) publicada.

###  Cambios

**CHANGED:**

` gkectl check-config ` ahora también verifica la disponibilidad de IP de nodo
si usas IP estáticas.

**CHANGED:**

` gkectl prepare ` ahora verifica si existe una VM y se marca como una
plantilla en vSphere antes de intentar subir la imagen OVA de la VM.

**CHANGED:**

Agrega compatibilidad para especificar un clúster de vCenter y un grupo de
recursos en ese clúster.

**CHANGED:**

Actualiza el controlador FIG-IP B5 a la versión 1.9.0.

**CHANGED:**

Actualiza el controlador de entrada de Istio a la versión 1.2.2.

###  Ajustes

**FIXED:**

Corrige problemas de persistencia de datos de registro con el registro de
Docker de la estación de trabajo de administrador.

**FIXED:**

Corrige la validación que verifica si el nombre del clúster de un usuario ya
está en uso.

##  25 de julio de 2019

Ya está disponible la versión 1.0.11 de GKE local.

##  17 de junio de 2019

GKE On-Prem ahora está disponible de forma general. La versión 1.0.10 incluye
los siguientes cambios:

###  Actualiza de beta-1.4 a 1.0.10

Antes de actualizar tus clústeres Beta a la primera versión con disponibilidad
general, realiza los pasos que se describen en [ Actualización de la versión
Beta de GKE On-Prem a disponibilidad general
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/upgrading/from-beta?hl=es-419) y revisa los siguientes puntos:

  * Si tienes una versión Beta anterior a la 1.4, asegúrate de actualizar a la versión Beta-1.4. 

  * Si los clústeres Beta ejecutan sus propios balanceadores de cargas L4 (no el predeterminado, F5 BIG-IP), debes borrar y volver a crear los clústeres para ejecutar la última versión de GKE On-Prem. 

  * Si tus clústeres se actualizaron a Beta-1.4 de Beta-1.3, ejecuta el siguiente comando _para cada clúster de usuarios_ antes de realizar la actualización: 
    
        kubectl delete crd networkpolicies.crd.projectcalico.org

  * Ahora se requiere la verificación del certificado de vCenter (ya no se admite ` vsphereinsecure ` ). Si actualizas los clústeres Beta 1.4 a 1.0.10, debes proporcionar un certificado público de CA de confianza de vCenter en el archivo de configuración de actualización. 

  * Debes actualizar _todos_ tus clústeres en ejecución. Para que esta actualización tenga éxito, tus clústeres no pueden ejecutarse en un estado de versión mixto. 

  * Primero debes actualizar los clústeres de administrador a la versión más reciente y, luego, actualizar los clústeres de usuario. 

###  Nuevas funciones

**FEATURE:**

Ahora puedes habilitar el [ modo de balanceo de cargas manual
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/manual-lb?hl=es-419) para configurar un balanceador de cargas
L4. Aún puedes usar el balanceador de cargas predeterminado, F5 BIG-IP.

**FEATURE:**

Se actualizó el proceso de instalación basado en la configuración de GKE On-
Prem. Ahora instala de manera declarativa con un [ archivo de configuración
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/overview?hl=es-419#config) .

**FEATURE:**

Agrega ` gkectl create-config ` , que genera un archivo de configuración para
instalar GKE local, actualizar clústeres existentes y crear clústeres de
usuario adicionales en una instalación existente. Esto reemplaza el asistente
de instalación y ` create-config.yaml ` de las versiones anteriores. Consulta
la documentación actualizada para [ instalar GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=es-419#generate_config) .

**FEATURE:**

Agrega ` gkectl check-config ` , que valida el archivo de configuración de GKE
On-Prem. Consulta la documentación actualizada para [ instalar GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=es-419#validate_config) .

**FEATURE:**

Agrega una marca ` --validate-attestations ` opcional a ` gkectl prepare ` .
Esta marca verifica que Google haya compilado y firmado las imágenes de
contenedor incluidas en tu estación de trabajo de administrador y que estén
listas para la implementación. Consulta la documentación actualizada para [
instalar GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/install?hl=es-419#prepare) .

###  Cambios

**CHANGED:**

Actualiza la versión de Kubernetes a la versión 1.12.7-gke.19. Ahora puedes [
actualizar tus clústeres ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/upgrading-clusters?hl=es-419) a esta
versión. Ya no puedes crear clústeres que ejecuten la versión 1.11.2-gke.19 de
Kubernetes.

Recomendamos actualizar el clúster de administrador antes de actualizar los
clústeres de usuarios.

**CHANGED:**

Actualiza el controlador de entrada de Istio a la versión 1.1.7.

**CHANGED:**

Ahora se requiere la verificación del certificado de vCenter (ya no se admite
` vsphereinsecure ` ). Proporciona el certificado en el campo ` cacertpath `
del archivo de configuración de GKE On-Prem.

Cuando un cliente llama al servidor de vCenter, este debe demostrar su
identidad al cliente mediante la presentación de un certificado. Ese
certificado debe estar firmado por una autoridad certificada (CA). El
certificado no debe ser autofirmado.

Si actualizas los clústeres Beta 1.4 a 1.0.10, debes proporcionar un
certificado público de CA de confianza de vCenter en el archivo de
configuración de actualización.

###  Problemas conocidos

**ISSUE:**

[ Actualizar clústeres ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/upgrading-clusters?hl=es-419) puede causar interrupciones o
tiempo de inactividad para las cargas de trabajo que usan [
PodDisruptionBudgets
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) (PDB).

**ISSUE:**

Es posible que no puedas actualizar los clústeres Beta que usan el [ modo de
balanceo de cargas manual ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/manual-lb?hl=es-419) a la versión 1.0.10
de GKE local. Para actualizar y seguir usando tu propio balanceador de cargas
con estos clústeres, debes volver a crearlos.

##  24 de mayo de 2019

La versión Beta 1.4.7 de GKE On-Prem ahora está disponible. En esta versión,
se incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

En el comando [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/diagnose?hl=es-419#capture_admin) , el parámetro ` --admin-
ssh-key-path ` ahora es opcional.

###  Cambios

**CHANGED:**

El 8 de mayo de 2019, presentamos un cambio en Connect, el servicio que te
permite interactuar con tus clústeres de GKE On-Prem mediante Cloud Console.
Para usar el nuevo agente de Connect, debes volver a registrar tus clústeres
con Cloud Console o actualizar a Anthos GKE On-Prem Beta-1.4.

Los clústeres de GKE On-Prem y las cargas de trabajo que se ejecutan en ellos
seguirán funcionando sin interrupciones. Sin embargo, los clústeres no serán
visibles en Cloud Console hasta que los vuelvas a registrar o actualices a la
versión Beta-1.4.

Antes de volver a registrarte o actualizar, asegúrate de que tu cuenta de
servicio tenga la función ` gkehub.connect ` . Además, si tu cuenta de
servicio tiene la función anterior clusterregistry.connect, es una buena idea
quitar esa función.

Otorga a tu cuenta de servicio la función gkehub.connect:

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

Si tu cuenta de servicio tiene la función ` clusterregistry.connect `
anterior, quita esa función:

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

Vuelve a registrar tu clúster o actualiza a Anthos GKE On-Prem Beta-1.4.

Para [ volver a registrar tu clúster ](https://cloud.google.com/kubernetes-
engine/connect/updating-agent?hl=es-419) , ejecuta lo siguiente:

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]
          

Para [ actualizar a Anthos GKE On-Prem Beta-1.4
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=es-419) , ejecuta lo siguiente:

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Problemas conocidos

**ISSUE:**

Existe un problema que impide que el agente de conexión se actualice a la
nueva versión durante una actualización. Para solucionar este problema,
ejecuta el siguiente comando después de actualizar un clúster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  13 de mayo de 2019

###  Problemas conocidos

**ISSUE:**

Los clústeres actualizados de la versión Beta-1.2 a Beta-1.3 pueden verse
afectados por un problema conocido que daña el archivo de configuración del
clúster y evita las actualizaciones futuras del clúster. Este problema afecta
a todas las actualizaciones futuras del clúster.

Para resolver este problema, borra y vuelve a crear los clústeres actualizados
de la versión Beta-1.2 a la versión Beta-1.3.

Para resolver el problema sin borrar y volver a crear el clúster, debes volver
a codificar y aplicar los secretos de cada clúster. Sigue los siguientes
pasos:

  1. Obtén el contenido de los secretos ` create-config ` almacenados en el clúster del administrador. Esto debe hacerse para el secreto ` create-config ` en el espacio de nombres de kube-system y para los secretos ` create-config ` en el espacio de nombres de cada clúster de usuarios: 
    
        kubectl get secret create-config -n kube-system -o jsonpath={.data.cfg} | base64 -d > kube-system_create_secret.yaml
    
        kubectl get secret create-config -n [USER_CLUSTER_NAME] -o jsonpath={.data.cfg} | base64 -d > [USER_CLUSTER_NAME]_create_secret.yaml

  2. Para cada clúster de usuario, abre el archivo ` [USER_CLUSTER_NAME]  _create_secret.yaml ` en un editor. Si los valores de ` registerserviceaccountkey ` y ` connectserviceaccountkey ` no son ` REDACTED ` , no se requiere ninguna otra acción: no es necesario volver a codificar y escribir los secretos en el clúster. 
  3. Abre el archivo ` create_config.yaml ` original en otro editor. 
  4. En ` [USER_CLUSTER_NAME]  _create_secret.yaml ` , reemplaza los valores ` registerserviceaccountkey ` y ` connectserviceaccountkey ` por los valores del archivo ` create_config.yaml ` original. Guarde el archivo modificado. 
  5. Repite los pasos del 3 al 5 para cada ` [USER_CLUSTER_NAME]  _create_secret.yaml ` y para el archivo ` kube-system_create_secret.yaml ` . 
  6. Codifica en Base64 cada archivo ` [USER_CLUSTER_NAME]  _create_secret.yaml ` y el archivo ` kube-system_create_secret.yaml ` : 
    
        cat [USER_CLUSTER_NAME]_create_secret.yaml | base64 > [USER_CLUSTER_NAME]_create_secret_create_secret.b64
    
        cat kube-system-cluster_create_secret.yaml | base64 >kube-system-cluster_create_secret.b64

  7. Reemplaza el campo ` data[cfg] ` en cada secreto del clúster con el contenido del archivo correspondiente: 
    
        kubectl edit secret create-config -n [USER_CLUSTER_NAME]
    
      # kubectl edit opens the file in the shell's default text editor
      # Open `first-user-cluster_create_secret.b64` in another editor, and replace
      # the `cfg` value with the copied value
      # Make sure the copied string has no newlines in it!

  8. Repite el paso 8 para cada secreto ` [USER_CLUSTER_NAME]  _create_secret.yaml ` y el secreto ` kube-system_create_secret.yaml ` . 
  9. Para asegurarte de que la actualización se haya realizado correctamente, repite el paso 1. 

##  7 de mayo de 2019

La versión Beta 1.4.1 de GKE On-Prem ahora está disponible. En esta versión,
se incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

En el comando [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/diagnose?hl=es-419#capture_admin) , el parámetro ` --admin-
ssh-key-path ` ahora es opcional.

###  Cambios

**CHANGED:**

El 8 de mayo de 2019, presentamos un cambio en Connect, el servicio que te
permite interactuar con tus clústeres de GKE On-Prem mediante Cloud Console.
Para usar el nuevo agente de Connect, debes volver a registrar tus clústeres
con Cloud Console o actualizar a Anthos GKE On-Prem Beta-1.4.

Los clústeres de GKE On-Prem y las cargas de trabajo que se ejecutan en ellos
seguirán funcionando sin interrupciones. Sin embargo, los clústeres no serán
visibles en Cloud Console hasta que los vuelvas a registrar o actualices a la
versión Beta-1.4.

Antes de volver a registrarte o actualizar la cuenta, asegúrate de que tu
cuenta de servicio tenga la función de gkehub.connect. Además, si tu cuenta de
servicio tiene la función clusterregistry.connect anterior, es una buena idea
quitar esa función.

Otorga a tu cuenta de servicio la función gkehub.connect:

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

Si tu cuenta de servicio tiene la función anterior clusterregistry.connect,
quita esa función:

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

Vuelve a registrar tu clúster o actualiza a Anthos GKE On-Prem Beta-1.4.

Para [ volver a registrar tu clúster ](https://cloud.google.com/kubernetes-
engine/connect/updating-agent?hl=es-419) , ejecuta lo siguiente:

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]
          

Para [ actualizar a Anthos GKE On-Prem Beta-1.4
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=es-419) , ejecuta lo siguiente:

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Problemas conocidos

**ISSUE:**

Existe un problema que impide que el agente de conexión se actualice a la
nueva versión durante una actualización. Para solucionar este problema,
ejecuta el siguiente comando después de actualizar un clúster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  25 de abril de 2019

La versión Beta 1.3.1 de GKE On-Prem ahora está disponible. En esta versión,
se incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

El comando ` gkectl diagnose snapshot ` ahora tiene una marca [ ` --dry-run `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/diagnose?hl=es-419#performing_a_dry_run_for_a_snapshot) .

**FEATURE:**

El comando ` gkectl diagnose snapshot ` ahora admite cuatro [ casos
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/diagnose?hl=es-419#snapshot_scenarios) .

**FEATURE:**

El comando ` gkectl diagnose snapshot ` ahora admite expresiones regulares
para especificar espacios de nombres.

###  Cambios

**CHANGED:**

Istio 1.1 ahora es el [ controlador de entrada
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/upgrading-a-
cluster?hl=es-419#upgrading_the_ingress_controller) predeterminado. El
controlador de entrada se ejecuta en el espacio de nombres ` gke-system ` para
los clústeres del administrador y del usuario. Esto permite una administración
de TLS más fácil para Ingress. Para habilitar la entrada o volver a habilitar
la entrada después de una actualización, sigue las instrucciones en [ Habilita
la entrada ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.3/how-
to/installation/install?hl=es-419#enabling_ingress) .

**CHANGED:**

La herramienta ` gkectl ` ya no usa Minikube y KVM para el arranque. Esto
significa que no tienes que habilitar la virtualización anidada en la VM de tu
estación de trabajo de administrador.

###  Problemas conocidos

**ISSUE:**

El controlador de Ingress de GKE local usa Istio 1.1 con descubrimiento de
secreto automático. Sin embargo, es posible que el agente de nodo para el
descubrimiento secreto no pueda obtener actualizaciones secretas después de su
eliminación. Así que evita borrar los secretos. Si después debes borrar un
secreto y el TLS de Ingress falla, reinicia manualmente el pod de Ingress en
el espacio de nombres de gke-system.

##  11 de abril de 2019

Ya está disponible la versión Beta 1.2.1 de GKE On-Prem. En esta versión, se
incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

Los clústeres de GKE On-Prem ahora se conectan automáticamente a Google
mediante [ Connect ](https://cloud.google.com/kubernetes-
engine/connect?hl=es-419) .

**FEATURE:**

Ahora puedes ejecutar hasta tres planos de control por clúster de usuario.

###  Cambios

**CHANGED:**

` gkectl ` ahora valida las credenciales F5 BIG-IP de vSphere para crear
clústeres.

###  Problemas conocidos

**ISSUE:**

Una regresión hace que los comandos ` gkectl diagnose snapshot ` usen la Llave
SSH incorrecta, lo que evita que el comando recopile información de los
clústeres de usuario. Como solución alternativa a los casos de ayuda, es
posible que debas establecer una conexión SSH a nodos de clúster de usuarios
individuales y recopilar datos de forma manual.

##  2 de abril de 2019

La versión Beta 1.1.1 de GKE On-Prem está disponible. En esta versión, se
incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

Ahora instala GKE local con un [ dispositivo virtual abierto (OVA)
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.1/how-
to/installation/getting-started?hl=es-419#download_ova) , una imagen de
máquina virtual preconfigurada que incluye varias herramientas de interfaz de
línea de comandos. Este cambio facilita las instalaciones y quita una capa de
virtualización. Ya no es necesario ejecutar ` gkectl ` dentro de un contenedor
de Docker.

Si instalaste las versiones de GKE On-Prem antes de la versión Beta 1.1.1,
debes crear una estación de trabajo de administrador nueva según las
instrucciones documentadas. Después de instalar la nueva estación de trabajo
de administrador, copia las claves SSH, los archivos de configuración,
kubeconfigs y cualquier otro archivo que necesites de tu estación de trabajo
anterior a la nueva.

**FEATURE:**

Se agregó documentación para [ crear copias de seguridad de clústeres y
restablecerlos ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.1/how-to/administration/backing-up?hl=es-419) .

**FEATURE:**

Ahora puedes configurar la autenticación para clústeres con OIDC y ADFS. Para
obtener más información, consulta [ Cómo autenticar con OIDC y ADFS
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.1/how-
to/security/oidc-adfs?hl=es-419) y [ Autenticación
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/concepts/authentication?hl=es-419) .

###  Cambios

**CHANGED:**

Ahora debes usar la clave privada del clúster de administrador para ejecutar `
gkectl diagnose snapshot ` .

**CHANGED:**

Se agregó una opción de configuración durante la instalación para implementar
clústeres de usuario con instancias principales múltiples.

**CHANGED:**

[ La documentación de conexión ](https://cloud.google.com/kubernetes-
engine/connect?hl=es-419) se migró.

###  Ajustes

**FIXED:**

Se solucionó un problema en el que la red del clúster se podía interrumpir
cuando se quitaba un nodo de forma inesperada.

###  Problemas conocidos

**ISSUE:**

La Administración de configuración de GKE local se actualizó de la versión
0.11 a 0.13. Se cambió el nombre de varios componentes del sistema. Debes
realizar algunos pasos para limpiar los recursos de las versiones anteriores
y, luego, instalar una instancia nueva.

Si tienes una instancia activa de Administración de configuración:

  1. Desinstala la instancia: 
    
        kubectl -n=nomos-system delete nomos --all

  2. Asegúrate de que el espacio de nombres de la instancia no tenga recursos: 
    
        kubectl -n nomos-system get all

  3. Borra el espacio de nombres: 
    
        kubectl delete ns nomos-system

  4. Borra el CRD: 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  5. Borra todos los recursos del sistema de Kubernetes para el operador: 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

Si no tienes una instancia activa de Administración de configuración:

  1. Borra el espacio de nombres de la Administración de configuración: 
    
        kubectl delete ns nomos-system

  2. Borra el CRD: 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  3. Borra todos los recursos del sistema de Kubernetes para el operador: 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

##  12 de marzo de 2019

Ya está disponible la versión Beta 1.0.3 de GKE On-Prem. En esta versión, se
incluyen los siguientes cambios:

###  Ajustes

**FIXED:**

Se corrigió un problema que provocaba que los certificados Docker se guardaran
en la ubicación incorrecta.

##  4 de marzo de 2019

La versión Beta 1.0.2 de GKE On-Prem ahora está disponible. En esta versión,
se incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

Ahora puedes ejecutar ` gkectl version ` para verificar qué versión de `
gkectl ` estás ejecutando.

**FEATURE:**

Ahora puedes [ actualizar los clústeres de usuario
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.0/how-
to/administration/upgrading-a-cluster?hl=es-419) a versiones Beta futuras.

**FEATURE:**

La versión 0.11.6 de la [ administración de configuraciones de Anthos
](https://cloud.google.com/anthos-config-management/docs?hl=es-419) ahora está
disponible.

**FEATURE:**

Stackdriver Logging ahora está habilitado en cada nodo. De forma
predeterminada, el agente de registro replica los registros en tu proyecto de
GCP solo para servicios de plano de control, API de clúster, Calico,
controlador BIG-IP, proxy de Envoy, Connect, Anthos Config Management,
Prometheus y Grafana control, y Docker.Los registros del contenedor de la
aplicación se excluyen de forma predeterminada, pero se pueden habilitar de
forma opcional.

**FEATURE:**

El proxy de sidecar de Stackdriver para Prometheus captura métricas para los
mismos componentes que el agente de registro.

**FEATURE:**

Las [ políticas de red de Kubernetes
](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
ahora son compatibles.

###  Cambios

**CHANGED:**

Ahora puedes actualizar los bloques de IP en la especificación del clúster
para expandir el rango de IP de un clúster determinado.

**CHANGED:**

Si los clústeres que instalaste durante la etapa Alfa se desconectaron de
Google después de la versión Beta, es posible que debas volver a conectarlos.
Consulta [ Registra un clúster de usuario de forma manual
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/registering-a-user-cluster?hl=es-419) .

**CHANGED:**

En esta [ guía de introducción ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/getting-started?hl=es-419) , se
actualizaron los pasos para activar tu cuenta de servicio y ejecutar ` gkectl
prepare ` .

**CHANGED:**

` gkectl diagnose snapshot ` ahora solo recopila datos de configuración y
excluye registros.Esta herramienta se usa para capturar detalles de tu entorno
antes de abrir un caso de ayuda.

**CHANGED:**

Compatibilidad con la configuración de nombre de grupo de SNAT opcional para
F5 BIG-IP en el momento de la creación del clúster Esto se puede usar para
configurar el valor "--vs-snat-pool-name" en el [ controlador BIG-IP F5
](https://clouddocs.f5.com/products/connectors/k8s-bigip-ctlr/v1.8/) .

**CHANGED:**

Ahora debes proporcionar una VIP para los complementos que se ejecutan en el
clúster de administrador.

###  Ajustes

**FIXED:**

Se mejoraron las operaciones de cambio de tamaño de clústeres para evitar la
eliminación accidental de nodos.

##  7 de febrero de 2019

Ya está disponible la versión Alfa 1.3 de GKE On-Prem. En esta versión, se
incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

Durante la instalación, puedes proporcionar archivos YAML con bloques ` nodeip
` para configurar una IPAM estática.

###  Cambios

**CHANGED:**

Ahora debes aprovisionar un disco de 100 GB en el almacén de datos de vSphere.
GKE On-Prem usa el disco para almacenar algunos de sus datos esenciales, como
etcd. Consulta [ Requisitos del sistema
](https://cloud.google.com/anthos/gke/docs/on-prem/requirements?hl=es-419) .

**CHANGED:**

Ahora solo puedes proporcionar nombres de host en minúscula a bloques ` nodeip
` .

**CHANGED:**

GKE On-Prem ahora aplica nombres únicos para clústeres de usuario.

**CHANGED:**

Los extremos de las métricas y las API que usan extremos de Istio ahora están
protegidos mediante mTLS y el control de acceso basado en funciones.

**CHANGED:**

La comunicación externa de Grafana está inhabilitada.

**CHANGED:**

Se aplicaron mejoras en la verificación de estado de Prometheus y
Alertmanager.

**CHANGED:**

Prometheus ahora usa un puerto seguro para las métricas de recopilación.

**CHANGED:**

Se realizaron varias actualizaciones de los paneles de Grafana.

###  Problemas conocidos

**ISSUE:**

Si tu cuenta de usuario de vCenter usa un formato como ` DOMAIN\USER ` , es
posible que debas escapar la barra inversa ( ` DOMAIN\\USER ` ). Asegúrate de
hacer esto cuando se te solicite ingresar la cuenta de usuario durante la
instalación.

##  23 de enero de 2019

Ya está disponible la versión Alfa 1.2.1 de GKE On-Prem. En esta versión, se
incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

Ahora puedes usar ` gkectl ` para [ borrar clústeres de administrador
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/deleting-an-admin-cluster?hl=es-419)

###  Cambios

**CHANGED:**

Los comandos ` gkectl diagnose snapshot ` ahora te permiten especificar nodos
mientras capturas instantáneas de los resultados y archivos del comando
remoto.

##  14 de enero de 2019

La versión Alfa 1.1.2 de GKE On-Prem ahora está disponible. En esta versión,
se incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

Ahora puedes usar el comando ` gkectl prepare ` para extraer y enviar imágenes
de contenedor de GKE On-Prem, lo que hace que ya no se use la secuencia de
comandos ` populate_registry.sh ` .

**FEATURE:**

` gkectl prepare ` ahora te solicita que ingreses información sobre tu clúster
de vSphere y grupo de recursos.

**FEATURE:**

Ahora puedes usar el comando ` gkectl create ` para crear y agregar clústeres
de usuario a los planos de control de administrador existentes si pasas un
archivo kubeconfig existente cuando se te solicite durante la creación del
clúster.

**FEATURE:**

Ahora puedes pasar un secreto de TLS de Ingress para clústeres de usuario y de
administrador en el momento de la creación del clúster. Verás el siguiente
mensaje nuevo:

` Do you want to use TLS for Admin Control Plane/User Cluster ingress? `

Proporcionar el secreto y los certificados de TLS permite que ` gkectl `
configure el TLS de Ingress. HTTP no se inhabilita automáticamente con la
instalación de TLS.

###  Cambios

**CHANGED:**

GKE On-Prem ahora ejecuta la versión de Kubernetes **1.11.2-gke.19** .

**CHANGED:**

La huella predeterminada para GKE On-Prem cambió:

  * El requisito mínimo de memoria para los nodos del clúster de usuario ahora es de 8192 M. 

**CHANGED:**

GKE On-Prem ahora ejecuta la versión de minikube **0.28.0** .

**CHANGED:**

La administración de políticas de GKE se actualizó a la versión **0.11.1** .

**CHANGED:**

` gkectl ` ya no te solicita que proporciones una configuración de proxy de
forma predeterminada.

**CHANGED:**

Hay tres recursos nuevos de ConfigMap en el espacio de nombres de clúster del
usuario: ` cluster-api-etcd-metrics-config ` , ` kube-etcd-metrics-config ` y
` kube-apiserver-config ` . GKE local usa estos archivos para iniciar
rápidamente el contenedor del proxy de métricas.

**CHANGED:**

Los eventos de kube-apiserver ahora están en su propio etcd. Puedes ver kube-
etcd-events en el espacio de nombres de tu clúster de usuarios.

**CHANGED:**

Los controladores de la API del clúster ahora usan la elección de líder.

**CHANGED:**

Las credenciales de vSphere ahora se extraen de los archivos de credenciales.

**CHANGED:**

Los comandos ` gkectl diagnose ` ahora funcionan con los clústeres de
administrador y de usuario.

**CHANGED:**

` gkectl diagnose snapshot ` ahora puede tomar instantáneas de archivos
remotos en el nodo, resultados de comandos remotos en los nodos y consultas de
Prometheus.

**CHANGED:**

Ahora ` gkectl diagnose snapshot ` puede tomar instantáneas en varios
subprocesos paralelos.

**CHANGED:**

` gkectl diagnose snapshot ` ahora te permite especificar palabras para
excluirlas de los resultados de la instantánea.

###  Ajustes

**FIXED:**

Se solucionaron problemas con el almacenamiento en caché de Minikube que
generaba llamadas inesperadas a redes.

**FIXED:**

Se solucionó un problema con la extracción de credenciales F5 BIG-IP. Las
credenciales ahora se leen desde un archivo de credenciales en lugar de usar
variables de entorno.

###  Problemas conocidos

**ISSUE:**

Es posible que encuentres la siguiente advertencia de [ ` govmomi `
](https://github.com/vmware/govmomi) cuando ejecutes ` gkectl prepare ` :

` Warning: Line 102: Unable to parse 'enableMPTSupport' for attribute 'key' on
element 'Config' `

**ISSUE:**

Cambiar el tamaño de los clústeres de usuarios puede hacer que los nodos se
borren o se vuelvan a crear por accidente.

**ISSUE:**

Los PersistentVolumes no pueden activarse, y se produce el error ` devicePath
is empty ` . Como solución alternativa, borra y vuelve a crear la
PersistentVolumeClaim asociada.

**ISSUE:**

El cambio de tamaño de los bloques de direcciones IPAM si se usa la asignación
de IP estática para nodos no es compatible con la versión Alfa. Para
solucionar este problema, considera asignar más direcciones IP de las que
necesitas actualmente.

**ISSUE:**

En discos lentos, la creación de VM puede agotar el tiempo de espera y hacer
que las implementaciones falle. Si esto ocurre, borra todos los recursos y
vuelve a intentarlo.

##  19 de diciembre de 2018

La versión Alfa 1.0.4 de GKE On-Prem ahora está disponible. En esta versión,
se incluyen los siguientes cambios:

###  Ajustes

**FIXED:**

La vulnerabilidad causada por [ CVE-2018-1002105
](https://github.com/kubernetes/kubernetes/issues/71411) tiene un parche.

##  30 de noviembre de 2018

La versión Alfa 1.0 de GKE On-Prem ahora está disponible. En esta versión, se
incluyen los siguientes cambios:

###  Cambios

**CHANGED:**

La versión Alfa 1.0 de GKE On-Prem ejecuta Kubernetes 1.11.

**CHANGED:**

La huella predeterminada para GKE On-Prem cambió:

  * El plano de control del administrador ejecuta tres nodos, que usan 4 CPU y 16 GB de memoria. 
  * El plano de control de usuario ejecuta un nodo que usa 4 CPU de 16 GB de memoria. 
  * Los clústeres de usuario ejecutan un mínimo de tres nodos, que usan 4 CPU y 16 GB de memoria. 

**CHANGED:**

Compatibilidad con la configuración de Prometheus de alta disponibilidad.

**CHANGED:**

Compatibilidad con la configuración personalizada del Administrador de
alertas.

**CHANGED:**

Prometheus se actualizó de la versión **2.3.2** a **2.4.3** .

**CHANGED:**

Grafana se actualizó de la versión **5.0.4** a **5.3.4** .

**CHANGED:**

kube-state-metrics se actualizó de la versión **1.3.1** a **1.4.0** .

**CHANGED:**

El Administrador de alertas se actualizó de la versión **1.14.0** a **1.15.2**
.

**CHANGED:**

node_exporter se actualizó de la versión **1.15.2** a **1.16.0** .

###  Ajustes

**FIXED:**

Se aplicó un parche a la vulnerabilidad causada por [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) .

###  Problemas conocidos

**ISSUE:**

Los PersistentVolumes no pueden activarse, y se produce el error ` devicePath
is empty ` . Como solución alternativa, borra y vuelve a crear la
PersistentVolumeClaim asociada.

**ISSUE:**

Cambiar el tamaño de los bloques de direcciones IPAM si se usa la asignación
de IP estática para nodos no es compatible en versión Alfa. Para solucionar
este problema, considera asignar más direcciones IP de las que necesitas
actualmente.

**ISSUE:**

La versión Alfa 1.0 de GKE On-Prem aún no pasa todas las pruebas de
conformidad.

**ISSUE:**

Solo se puede crear un clúster de usuario por cada clúster de administrador.
Para crear clústeres de usuario adicionales, crea otro clúster de
administrador.

##  31 de octubre de 2018

El EAP 2.1 de GKE local ahora está disponible. En esta versión, se incluyen
los siguientes cambios:

###  Cambios

**CHANGED:**

Cuando creas clústeres de administrador y de usuario al mismo tiempo, puedes
volver a usar las credenciales F5 BIG-IP del clúster de administrador para
crear el clúster de usuario. Además, la CLI ahora requiere que se proporcionen
credenciales de BIG-IP; este requisito no se puede omitir mediante ` --dry-run
` .

**CHANGED:**

Controlador F5 BIG-IP para usar la versión más reciente de OSS, 1.7.0.

**CHANGED:**

Para mejorar la estabilidad de las máquinas lentas de vSphere, el tiempo de
espera de la creación de la máquina del clúster es de 15 minutos (antes eran
cinco minutos).

##  17 de octubre de 2018

El EAP 2.0 de GKE local ahora está disponible. Los siguientes cambios se
incluyen en esta versión:

###  Cambios

**CHANGED:**

Compatibilidad con GKE Connect.

**CHANGED:**

Compatibilidad con Monitoring.

**CHANGED:**

Compatibilidad con la instalación mediante registros privados.

**CHANGED:**

Compatibilidad con el balanceador de cargas L7 como una VIP L4 en F5 BIG-IP.

**CHANGED:**

Compatibilidad con la asignación de IP estáticas para nodos durante el
arranque del clúster.

###  Problemas conocidos

**ISSUE:**

Solo se puede crear un clúster de usuario por cada clúster de administrador.
Para crear clústeres de usuario adicionales, crea otro clúster de
administrador.

**ISSUE:**

Las actualizaciones de clústeres no son compatibles con EAP 2.0.

**ISSUE:**

En discos lentos, la creación de la VM puede agotar el tiempo de espera y
hacer que las implementaciones fallen. Si esto ocurre, borra todos los
recursos y vuelve a intentarlo.

**ISSUE:**

Como parte del proceso de arranque del clúster, se ejecuta una instancia de
minikube de corta duración. La versión de minikube utilizada tiene una
vulnerabilidad de seguridad [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) .

