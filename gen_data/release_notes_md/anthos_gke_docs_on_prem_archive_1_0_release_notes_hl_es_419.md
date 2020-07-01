#  Notas de la versión

En esta página, se documentan las actualizaciones de producción de Anthos GKE
On-Prem. Puedes revisar esta página de forma periódica para ver anuncios sobre
características nuevas o actualizadas, correcciones de errores, problemas
comunes y funciones obsoletas.

También puedes consultar estos vínculos:

  * [ Descargas ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=es-419)
  * [ Control de versiones y actualizaciones ](https://cloud.google.com/anthos/gke/docs/on-prem/versioning-and-upgrades?hl=es-419)
  * [ Actualiza clústeres ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=es-419)
  * [ Actualizar la estación de trabajo de administrador ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=es-419)

Puedes ver las últimas actualizaciones de productos de todo Google Cloud en la
página [ Notas de la versión de Google Cloud
](https://cloud.google.com/release-notes?hl=es-419) .

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) o agrega
directamente la URL del feed: ` https://cloud.google.com/feeds/gkeonprem-
release-notes.xml `

##  22 de agosto de 2019

La versión 1.0.2-gke.3 de GKE On-Prem ahora está disponible. Esta versión de
parche incluye los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

Se admite Seesaw para el balanceo de cargas manual.

**FEATURE:**

Ahora puedes especificar una red de vSphere diferente para los clústeres de
administrador y usuario.

**FEATURE:**

Ahora puedes borrar clústeres de usuario con ` gkectl ` . Consulta [ Borra un
clúster de usuario ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/how-to/administration/deleting-a-user-cluster?hl=es-419) .

###  Cambios

**CHANGED:** ` gkectl diagnose snapshot ` ahora obtiene registros de los
planos de control del clúster de usuario.

**CHANGED:**

La especificación OIDC de GKE On-Prem se actualizó con varios campos nuevos: `
kubectlredirecturl ` , ` scopes ` , ` extraparams ` y ` usehttpproxy ` .

**CHANGED:**

Calico se actualizó a la versión 3.7.4.

**CHANGED:**

Las métricas del sistema de Cloud Monitoring cambiaron de `
external.googleapis.com/prometheus/ ` a ` kubernetes.io/anthos/ ` . Si
realizas el seguimiento de métricas o alertas, actualiza los paneles con el
siguiente prefijo.

###  Fijo

**FIXED:**

[ Se corrigió una vulnerabilidad de CVE-2019-11247
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/security-
bulletins?hl=es-419#august-22-2019) .

**FIXED:**

[ Se corrigió una vulnerabilidad en el proxy RBAC
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/security-
bulletins?hl=es-419#august-23-2019) .

##  30 de julio de 2019

Ya está disponible la versión 1.0.1-gke.5 de GKE On-Prem. Esta versión de
parche incluye los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

[ Hoja de referencia de GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/reference/cheatsheet?hl=es-419) publicada.

###  Cambios

**CHANGED:**

` gkectl check-config ` ahora también verifica la disponibilidad de la IP del
nodo si usas direcciones IP estáticas.

**CHANGED:**

` gkectl prepare ` ahora verifica si existe una VM y se marca como una
plantilla en vSphere antes de intentar subir la imagen OVA de la VM.

**CHANGED:**

Agrega compatibilidad para especificar un clúster de vCenter y un grupo de
recursos en ese clúster.

**CHANGED:**

Actualiza el controlador F5 BIG-IP a la versión 1.9.0.

**CHANGED:**

Actualiza el controlador de entrada de Istio a la versión 1.2.2.

###  Ajustes

**FIXED:**

Corrige problemas de persistencia de datos de registro con el registro de
Docker de la estación de trabajo de administrador.

**FIXED:**

Corrige la validación que verifica si el nombre de un clúster de usuario ya
está en uso.

##  17 de junio de 2019

GKE On-Prem ahora está disponible para el público general. La versión 1.0.10
incluye los cambios siguientes:

###  Actualización de beta-1.4 a 1.0.10

Antes de actualizar tus clústeres Beta a la primera versión con disponibilidad
general, realiza los pasos que se describen en [ Actualización de la versión
Beta de GKE On-Prem a disponibilidad general
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/upgrading/from-beta?hl=es-419) y revisa los siguientes puntos:

  * Si tienes una versión Beta anterior a la 1.4, asegúrate de actualizar a la versión Beta-1.4. 

  * Si los clústeres Beta ejecutan sus propios balanceadores de cargas L4 (no el predeterminado, F5 BIG-IP), debes borrar y volver a crear los clústeres para ejecutar la última versión de GKE On-Prem. 

  * Si tus clústeres se actualizaron a Beta-1.4 de Beta-1.3, ejecuta el siguiente comando _para cada clúster de usuarios_ antes de realizar la actualización: 
    
        kubectl delete crd networkpolicies.crd.projectcalico.org

  * Ahora se requiere la verificación del certificado de vCenter (Ya no se admite ` vsphereinsecure ` ). Si actualizas tus clústeres Beta 1.4 a 1.0.10, debes proporcionar un certificado público de CA de confianza de vCenter en el archivo de configuración de la actualización. 

  * Debes actualizar _todos_ tus clústeres en ejecución. Para que esta actualización sea exitosa, los clústeres no se pueden ejecutar en un estado de versión mixta. 

  * Primero debes actualizar los clústeres de administrador a la versión más reciente y, luego, actualizar los clústeres de usuario. 

###  Nuevas funciones

**FEATURE:**

Ahora puedes habilitar el [ modo de balanceo de cargas manual
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/manual-lb?hl=es-419) para configurar un balanceador de cargas
L4. Aún puedes usar el balanceador de cargas predeterminado, F5 BIG-IP.

**FEATURE:**

Se actualizó el proceso de instalación basado en la configuración de GKE On-
Prem. Ahora instala de manera declarativa con un [ archivo de configuración
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/concepts/overview?hl=es-419#config) .

**FEATURE:**

Agrega ` gkectl create-config ` , que genera un archivo de configuración para
instalar GKE On-Prem, actualizar clústeres existentes y crear clústeres de
usuario adicionales en una instalación existente. Esto reemplaza el asistente
de instalación y ` create-config.yaml ` de las versiones anteriores. Consulta
la documentación actualizada para [ instalar GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/install?hl=es-419#generate_config) .

**FEATURE:**

Agrega ` gkectl check-config ` , que valida el archivo de configuración de GKE
On-Prem. Consulta la documentación actualizada para [ instalar GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/install?hl=es-419#validate_config) .

**FEATURE:**

Agrega una marca ` --validate-attestations ` opcional a ` gkectl prepare ` .
Esta marca verifica que las imágenes de contenedor incluidas en tu estación de
trabajo de administración estén compiladas y firmadas por Google, y estén
listas para la implementación. Consulta la documentación actualizada para [
instalar GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/install?hl=es-419#prepare) .

###  Cambios

**CHANGED:**

Actualiza la versión de Kubernetes a 1.12.7-gke.19. Ahora puedes [ actualizar
tus clústeres ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/administration/upgrading-clusters?hl=es-419) a
esta versión. Ya no puedes crear clústeres que ejecuten la versión de
Kubernetes 1.11.2-gke.19.

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
certificado no debe estar autofirmado.

Si actualizas los clústeres Beta 1.4 a 1.0.10, debes proporcionar un
certificado público de CA de confianza de vCenter en el archivo de
configuración de actualización.

###  Problemas conocidos

**ISSUE:**

[ Actualizar clústeres ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/upgrading-clusters?hl=es-419) puede causar
interrupciones o tiempo de inactividad para las cargas de trabajo que usan [
PodDisruptionBudgets
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) (PDB).

**ISSUE:**

Es posible que no puedas actualizar los clústeres Beta que usan el [ modo de
balanceo de cargas manual ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/manual-lb?hl=es-419) a GKE On-Prem
versión 1.0.10. Para actualizar y seguir usando tu propio balanceador de
cargas con estos clústeres, debes volver a crearlos.

##  24 de mayo de 2019

La versión Beta 1.4.7 de GKE On-Prem ahora está disponible. En esta versión,
se incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

En el comando [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
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
servicio tiene la función clusterregistry.connect anterior, es una buena idea
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
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=es-419) , ejecuta lo siguiente:

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Problemas conocidos

**ISSUE:**

Hay un problema que impide que el agente de Connect se actualice a la nueva
versión durante una actualización. Para solucionar este problema, ejecuta el
siguiente comando después de actualizar un clúster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  13 de mayo de 2019

###  Problemas conocidos

**ISSUE:**

Los clústeres actualizados de la versión Beta-1.2 a Beta-1.3 pueden verse
afectados por un problema conocido que daña el archivo de configuración del
clúster y evita las actualizaciones futuras del clúster. Este problema afecta
a todas las actualizaciones futuras de clústeres.

Para resolver este problema, borra y vuelve a crear los clústeres actualizados
de la versión Beta-1.2 a la versión Beta-1.3.

Para resolver el problema sin borrar ni volver a crear el clúster, debes
volver a codificar y aplicar los secretos de cada clúster. Completa los pasos
siguientes:

  1. Obtén el contenido de los secretos ` create-config ` almacenados en el clúster del administrador. Esto debe hacerse para el secreto ` create-config ` en el espacio de nombres del sistema de Kubernetes y para los secretos ` create-config ` en el espacio de nombres de cada clúster de usuario: 
    
        kubectl get secret create-config -n kube-system -o jsonpath={.data.cfg} | base64 -d > kube-system_create_secret.yaml
    
        kubectl get secret create-config -n [USER_CLUSTER_NAME] -o jsonpath={.data.cfg} | base64 -d > [USER_CLUSTER_NAME]_create_secret.yaml

  2. Para cada clúster de usuario, abre el archivo ` [USER_CLUSTER_NAME]  _create_secret.yaml ` en un editor. Si los valores de ` registerserviceaccountkey ` y ` connectserviceaccountkey ` no son ` REDACTED ` , no se requiere ninguna otra acción: no es necesario volver a codificar los secretos ni escribirlos en el clúster para ver sus detalles. 
  3. Abre el archivo ` create_config.yaml ` original en otro editor. 
  4. En ` [USER_CLUSTER_NAME]  _create_secret.yaml ` , reemplaza los valores ` registerserviceaccountkey ` y ` connectserviceaccountkey ` por los valores del archivo ` create_config.yaml ` original. Guarda el archivo modificado. 
  5. Repite los pasos del 3 al 5 para cada ` [USER_CLUSTER_NAME]  _create_secret.yaml ` y para el archivo ` kube-system_create_secret.yaml ` . 
  6. Codifica en base64 cada archivo ` [USER_CLUSTER_NAME]  _create_secret.yaml ` y el archivo ` kube-system_create_secret.yaml ` : 
    
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
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
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

Antes de volver a registrar o actualizar, asegúrate de que tu cuenta de
servicio tenga la función gkehub.connect. Además, si tu cuenta de servicio
tiene la función anterior clusterregistry.connect, es una buena idea quitar
esa función.

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
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=es-419) , ejecuta lo siguiente:

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Problemas conocidos

**ISSUE:**

Hay un problema que impide que el agente de Connect se actualice a la nueva
versión durante una actualización. Para solucionar este problema, ejecuta el
siguiente comando después de actualizar un clúster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  25 de abril de 2019

La versión Beta 1.3.1 de GKE On-Prem ahora está disponible. En esta versión,
se incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

El comando ` gkectl diagnose snapshot ` ahora tiene una marca [ ` --dry-run `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/administration/diagnose?hl=es-419#performing_a_dry_run_for_a_snapshot) .

**FEATURE:**

El comando ` gkectl diagnose snapshot ` ahora admite cuatro [ casos
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/administration/diagnose?hl=es-419#snapshot_scenarios) .

**FEATURE:**

El comando ` gkectl diagnose snapshot ` ahora admite expresiones regulares
para especificar espacios de nombres.

###  Cambios

**CHANGED:**

Istio 1.1 ahora es el [ controlador de entrada
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/administration/upgrading-a-
cluster?hl=es-419#upgrading_the_ingress_controller) predeterminado. El
controlador de entrada se ejecuta en el espacio de nombres ` gke-system ` para
los clústeres de administrador y de usuario. Esto permite una administración
de TLS más fácil para Ingress. Para habilitar la entrada o volver a habilitar
la entrada después de una actualización, sigue las instrucciones en [ Habilita
la entrada ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.3/how-
to/installation/install?hl=es-419#enabling_ingress) .

**CHANGED:**

La herramienta ` gkectl ` ya no usa Minikube ni KVM para el arranque. Esto
significa que no tienes que habilitar la virtualización anidada en la VM de tu
estación de trabajo de administrador.

###  Problemas conocidos

**ISSUE:**

El controlador de entrada de GKE On-Prem usa Istio 1.1 con la detección
automática de secretos. Sin embargo, es posible que el agente de nodo para la
detección de secretos no obtenga actualizaciones de secretos después de la
eliminación de estos. Por lo tanto, evita borrar los secretos. Si debes borrar
un secreto y TLS de Ingress falla, reinicia manualmente el pod de Ingress en
el espacio de nombres del sistema de GKE.

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

Una regresión hace que los comandos ` gkectl diagnose snapshot ` usen la clave
SSH incorrecta, lo que evita que estos recopilen información de clústeres de
usuario. Como solución alternativa para los casos de ayuda, es posible que
debas establecer una conexión SSH a nodos de clústeres de usuarios
individuales y recopilar datos de forma manual.

##  2 de abril de 2019

La versión Beta 1.1.1 de GKE On-Prem está disponible. En esta versión, se
incluyen los siguientes cambios:

###  Nuevas funciones

**FEATURE:**

Ahora instala GKE On-Prem con un [ dispositivo virtual abierto (OVA)
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/installation/getting-started?hl=es-419#download_ova) , una imagen de
máquina virtual preconfigurada que incluye varias herramientas de interfaz de
línea de comandos. Este cambio facilita las instalaciones y quita una capa de
virtualización. Ya no necesitas ejecutar ` gkectl ` dentro de un contenedor de
Docker.

Si instalaste las versiones de GKE On-Prem antes de la versión Beta 1.1.1,
debes crear una estación de trabajo de administrador nueva según las
instrucciones documentadas. Después de instalar la nueva estación de trabajo
de administrador, copia las claves SSH, los archivos de configuración,
kubeconfigs y cualquier otro archivo que necesites de tu estación de trabajo
anterior a la nueva.

**FEATURE:**

Se agregó documentación para [ crear copias de seguridad de clústeres y
restablecerlos ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.1/how-to/administration/backing-up?hl=es-419) .

**FEATURE:**

Ahora puedes configurar la autenticación para los clústeres que usan OIDC y
ADFS. Para obtener más información, consulta [ Autenticación con OIDC y ADFS
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/security/oidc-adfs?hl=es-419) y [ Autenticación
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/concepts/authentication?hl=es-419) .

###  Cambios

**CHANGED:**

Ahora debes usar la clave privada del clúster de administrador para ejecutar `
gkectl diagnose snapshot ` .

**CHANGED:**

Se agregó una opción de configuración durante la instalación para implementar
clústeres de usuario con instancias principales múltiples.

**CHANGED:**

Se migró la [ documentación de Connect ](https://cloud.google.com/kubernetes-
engine/connect?hl=es-419) .

###  Ajustes

**FIXED:**

Se solucionó un problema en el que la red del clúster se podía interrumpir
cuando se quitaba un nodo de forma inesperada.

###  Problemas conocidos

**ISSUE:**

La administración de configuración de GKE On-Prem se actualizó de la versión
0.11 a la 0.13. Se cambió el nombre de varios componentes del sistema. Debes
realizar algunos pasos para limpiar los recursos de las versiones anteriores e
instalar una instancia nueva.

Si tienes una instancia activa de Administración de configuración, sigue estos
pasos:

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

Si no tienes una instancia activa de Administración de configuración, sigue
estos pasos:

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
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.0/how-
to/administration/upgrading-a-cluster?hl=es-419) a versiones Beta futuras.

**FEATURE:**

La versión 0.11.6 de [ Anthos Config Management
](https://cloud.google.com/anthos-config-management/docs?hl=es-419) ahora está
disponible.

**FEATURE:**

Stackdriver Logging ahora está habilitado en cada nodo. De forma
predeterminada, el agente de registro replica los registros en tu proyecto de
GCP solo para los servicios del plano de control, la API del clúster, el
controlador de vSphere, Calico, el controlador BIG-IP, el proxy de Envoy,
Connect, Anthos Config Management, los servicios de Grafana y Prometheus, el
plano de control de Istio y Docker.Los registros del contenedor de la
aplicación se excluyen de forma predeterminada, pero también puede optar por
habilitarlos.

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

Si los clústeres que instalaste durante la versión Alfa se desconectaron de
Google después de la versión Beta, es posible que debas volver a conectarlos.
Consulta [ Registra un clúster de usuario de forma manual
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/registering-a-user-cluster?hl=es-419) .

**CHANGED:**

En esta [ guía de introducción ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/getting-started?hl=es-419) , se
actualizaron los pasos para activar tu cuenta de servicio y ejecutar ` gkectl
prepare ` .

**CHANGED:**

` gkectl diagnose snapshot ` ahora solo recopila datos de configuración y
excluye registros.Esta herramienta se usa para capturar los detalles de tu
entorno antes de abrir un caso de ayuda.

**CHANGED:**

Compatibilidad con la configuración opcional del nombre del grupo de SNAT para
F5 BIG-IP en el momento de la creación del clúster. Se puede usar para
configurar el valor "--vs-snat-pool-name" en el [ controlador F5 BIG-IP
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

Prometheus ahora usa un puerto seguro para extraer métricas.

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
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/administration/deleting-an-admin-cluster?hl=es-419)

.

###  Cambios

**CHANGED:**

Los comandos ` gkectl diagnose snapshot ` ahora te permiten especificar nodos
mientras se capturan instantáneas de los resultados y los archivos de comandos
remotos.

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
de vSphere y tu grupo de recursos.

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

Proporcionar el secreto y los certificados TLS permite que ` gkectl `
configure la TLS de Ingress. HTTP no se inhabilita automáticamente con la
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

Hay tres recursos de ConfigMap nuevos en el espacio de nombres del clúster de
usuario: ` cluster-api-etcd-metrics-config ` , ` kube-etcd-metrics-config ` y
` kube-apiserver-config ` . GKE On-Prem usa estos archivos para iniciar
rápidamente el contenedor del proxy de métricas.

**CHANGED:**

Los eventos de kube-apiserver ahora están disponibles en su propio etcd.
Puedes ver kube-etcd-events en el espacio de nombres de tu clúster de usuario.

**CHANGED:**

Los controladores de la API del clúster ahora usan la elección de líder.

**CHANGED:**

Las credenciales de vSphere ahora se extraen de los archivos de credenciales.

**CHANGED:**

Los comandos ` gkectl diagnose ` ahora funcionan con clústeres de
administrador y de usuario.

**CHANGED:**

` gkectl diagnose snapshot ` ahora puede tomar instantáneas de archivos
remotos en el nodo, resultados de comandos remotos en los nodos y consultas de
Prometheus.

**CHANGED:**

` gkectl diagnose snapshot ` ahora puede tomar instantáneas en varios
subprocesos paralelos.

**CHANGED:**

` gkectl diagnose snapshot ` ahora te permite especificar palabras para
excluirlas de los resultados de la instantánea.

###  Ajustes

**FIXED:**

Se solucionaron problemas con el almacenamiento en caché de Minikube que
generaba llamadas inesperadas a redes.

**FIXED:**

Se solucionó un problema con la extracción de credenciales de F5 BIG-IP. Las
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

En Alfa no se admite el cambio del tamaño de los bloques de direcciones IPAM
si se usa la asignación de IP estáticas para nodos. Para solucionar este
problema, considera asignar más direcciones IP de las que necesitas
actualmente.

**ISSUE:**

En discos lentos, la creación de VM puede agotar el tiempo de espera y hacer
que las implementaciones fallen. Si esto ocurre, borra todos los recursos y
vuelve a intentarlo.

##  19 de diciembre de 2018

La versión Alfa 1.0.4 de GKE On-Prem ahora está disponible. En esta versión,
se incluyen los siguientes cambios:

###  Ajustes

**FIXED:**

Se aplicó un parche a la vulnerabilidad causada por [ CVE-2018-1002105
](https://github.com/kubernetes/kubernetes/issues/71411) .

##  30 de noviembre de 2018

La versión Alfa 1.0 de GKE On-Prem ahora está disponible. En esta versión, se
incluyen los siguientes cambios:

###  Cambios

**CHANGED:**

La versión Alfa 1.0 de GKE On-Prem ejecuta Kubernetes 1.11.

**CHANGED:**

La huella predeterminada para GKE On-Prem cambió:

  * El plano de control de administrador ejecuta tres nodos, que usan 4 CPU y 16 GB de memoria. 
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

En Alfa no se admite el cambio del tamaño de los bloques de direcciones IPAM
si se usa la asignación de IP estáticas para nodos. Para solucionar este
problema, considera asignar más direcciones IP de las que necesitas
actualmente.

**ISSUE:**

La versión Alfa 1.0 de GKE On-Prem aún no pasa todas las pruebas de
conformidad.

**ISSUE:**

Solo se puede crear un clúster de usuario por cada clúster de administrador.
Para crear clústeres de usuario adicionales, crea otro clúster de
administrador.

##  31 de octubre de 2018

El EAP 2.1 de GKE On-Prem ahora está disponible. En esta versión, se incluyen
los siguientes cambios:

###  Cambios

**CHANGED:**

Cuando creas clústeres de administrador y de usuario al mismo tiempo, puedes
volver a usar las credenciales F5 BIG-IP del clúster de administrador para
crear el clúster de usuario. Además, la CLI ahora requiere que se proporcionen
credenciales de BIG-IP; este requisito no se puede omitir mediante ` --dry-run
` .

**CHANGED:**

Se actualizó el controlador F5 BIG-IP para usar la última versión de OSS,
1.7.0.

**CHANGED:**

Para mejorar la estabilidad de las máquinas lentas de vSphere, el tiempo de
espera de la creación de la máquina del clúster es de 15 minutos (antes eran
cinco minutos).

##  17 de octubre de 2018

El EAP 2.0 de GKE On-Prem ahora está disponible. En esta versión, se incluyen
los siguientes cambios:

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
administración.

**ISSUE:**

Las actualizaciones de clústeres no son compatibles con EAP 2.0.

**ISSUE:**

En discos lentos, la creación de VM puede agotar el tiempo de espera y hacer
que las implementaciones fallen. Si esto ocurre, borra todos los recursos y
vuelve a intentarlo.

**ISSUE:**

Como parte del proceso de arranque del clúster, se ejecuta una instancia de
Minikube de corta duración. La versión de Minikube que se usa tiene una
vulnerabilidad de seguridad de [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) .

