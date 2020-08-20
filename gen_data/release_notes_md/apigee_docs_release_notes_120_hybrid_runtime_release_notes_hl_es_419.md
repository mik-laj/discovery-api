**NOTE:** Some aspects of this product are in Beta. The hybrid installation
options are GA. To join the Beta program, reach out to your Apigee
representative.

#  1.2.0 - Notas de la versión del entorno de ejecución híbrido de Apigee

El 3 de abril de 2020, lanzamos la versión 1.2.0 del entorno de ejecución
híbrido de Apigee.

Para obtener más información, consulta los siguientes recursos:

  * _[ Más información sobre los híbridos ](https://cloud.google.com/apigee/docs/hybrid/v1.2/what-is-hybrid?hl=es-419) _ o _[ Comenzar la instalación ](https://cloud.google.com/apigee/docs/hybrid/v1.2/big-picture?hl=es-419) _
  * _Crea una cuenta paga:_ Comunícate con las [ ventas de Apigee ](https://pages.apigee.com/contact-sales-reg.html?hl=es-419)
  * _¿Preguntas o problemas?_ Comunícate con el [ equipo de asistencia de Apigee ](https://cloud.google.com/apigee/support/?hl=es-419)

####  Ayuda y notificaciones

**¿Preguntas o problemas?** [ Haz clic aquí para obtener ayuda.
](https://cloud.google.com/apigee/support/?hl=es-419)

**Notificaciones de la versión** : Ve a [ http://status.apigee.com
](http://status.apigee.com?hl=es-419) y haz clic en **Suscribirse a
actualizaciones** .

[ Página principal de las notas de la versión
](https://cloud.google.com/apigee/docs/release/notes/apigee-release-
notes?hl=es-419)

##  Actualiza

Para actualizar de la versión 1.1.1 a 1.2.0, debes realizar cambios en tu
archivo de anulación que sean incompatibles con la versión 1.1.1. Realizar
estos cambios en el archivo de anulaciones es un requisito previo para
realizar la actualización. La configuración nueva corrige un problema en el
que, en algunos casos, las llamadas a la API se enrutan al entorno incorrecto.
Para obtener más detalles, consulta [ Actualiza Apigee Hybrid
](https://cloud.google.com/apigee/docs/hybrid/v1.2/upgrade?hl=es-419) .

##  Nuevas funciones y actualizaciones

A continuación, se incluyen las nuevas funciones y actualizaciones de esta
versión.

###  Se agregó una nueva configuración de host virtual para especificar reglas
de enrutamiento

La nueva función de configuración ` virtualhosts ` aborda un problema en el
que el orden en que las rutas base se enrutaron a varios entornos no era
seguro. Para obtener más información, consulta [ Cómo configurar hosts
virtuales ](https://cloud.google.com/apigee/docs/hybrid/v1.2/base-path-
routing?hl=es-419) . (150336519)

###  Versión Beta de la política OASValidation

La política OASValidation (OpenAPI Specification Validation) (Beta) te permite
validar una solicitud entrante o un mensaje de respuesta en una especificación
OpenAPI 3.0 (JSON o YAML). Para obtener más información, consulta la [
Política de OASValidación (Beta) ](https://cloud.google.com/apigee/docs/api-
platform/reference/policies/oas-validation-policy?hl=es-419) . (144949685)

###  Versión Beta de la compatibilidad con WebSocket

Apigee Hybrid admite conexiones de WebSocket. Los clientes de proxy de API
ahora pueden solicitar una actualización del protocolo de HTTP a WebSockets.
Para obtener más información, consulta [ Usa WebSockets (Beta)
](https://cloud.google.com/apigee/docs/hybrid/v1.2/websockets?hl=es-419) .

###  Accede a los valores secretos de las políticas desde los secretos de
Kubernetes

Una nueva función te permite acceder a los valores almacenados en un secreto
de Kubernetes en variables de flujo del proxy. Para obtener más detalles,
consulta [ Almacena datos en un secreto de Kubernetes
](https://cloud.google.com/apigee/docs/hybrid/v1.2/k8s-secrets?hl=es-419) .
(133377603)

###  El elemento de operadores de Apigee (AO) reemplaza a ADAC y AADA

Los operadores de Apigee (AO) crean y actualizan los recursos de Istio y
Kubernetes de bajo nivel necesarios para implementar y mantener AD. Por
ejemplo, el controlador lleva a cabo la actualización de los procesadores de
mensajes. Además, valida la configuración de ApigeeDeployment antes de
conservarla en el clúster de Kubernetes. AO reemplaza a la admisión de
implementación de Apigee (AMI) y el controlador de implementación de Apigee
(ADC). Consulta [ elao en la referencia de la propiedad de configuración
](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-
ref?hl=es-419#ao) . (151250559)

###  Reemplazar y dar de baja ciertas propiedades de configuración de
clústeres y proyectos

Se agregaron dos propiedades de configuración nuevas: ` k8sCluster ` y ` gcp `
. Estas propiedades reemplazan las siguientes propiedades obsoletas: `
k8sClusterName ` , ` gcpRegion ` y ` gcpProjectID ` . Para obtener detalles,
consulta [ Referencia de propiedad de configuración
](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref?hl=es-419)
. (146299599)

###  Expansión de volumen persistente para Cassandra en Kubernetes

Se agregó un proceso para expandir el volumen persistente utilizado por
Apigee-cassandra para satisfacer las necesidades de almacenamiento, sin
necesidad de agregar más nodos solo para aumentar el almacenamiento. Consulta
la página sobre [ cómo expandir los volúmenes persistentes de Cassandra
](https://cloud.google.com/apigee/docs/hybrid/v1.2/expand-persistent-
volumes?hl=es-419) . (138167919)

###  Compatibilidad con fuentes adicionales para certificados, claves de
encriptación y SA

Se agregaron nuevas propiedades de configuración que proporcionan mayor
flexibilidad en la forma de especificar certificados TLS, claves de
encriptación y claves de cuentas de servicio. A continuación, se enumeran las
propiedades nuevas:

  * ` kmsEncryptionPath `
  * ` kmsEncryptionSecret.key `
  * ` kmsEncryptionSecret.name `
  * ` cassandra.backup.serviceAccountSecretRef `
  * ` cassandra.restore.serviceAccountSecretRef `
  * ` envs[].cacheEncryptionPath `
  * ` envs[].cacheEncryptionSecret.key `
  * ` envs[].cacheEncryptionSecret.name `
  * ` envs[].kmsEncryptionPath `
  * ` envs[].kmsEncryptionSecret.key `
  * ` envs[].kmsEncryptionSecret.name `
  * ` envs[].serviceAccountSecretRefs.synchronizer `
  * ` envs[].serviceAccountSecretRefs.udca `
  * ` envs[].sslSecret `
  * ` logger.serviceAccountSecretRef `
  * ` mart.serviceAccountSecretRef `
  * ` mart.sslSecret `
  * ` metrics.serviceAccountSecretRef `
  * ` synchronizer.serviceAccountSecretRef `
  * ` udca.serviceAccountSecretRef `

Para obtener más información, consulta la [ referencia de propiedades de
configuración ](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-
ref?hl=es-419) . (145303466)

###  Permita que los clientes ofusquen los datos antes de enviarlos a
Analytics

Se agregó una función que te permite ofuscar ciertos datos de estadísticas
antes de enviarlos al plano de administración. Para obtener más información,
consulta [ Ofusca datos de usuarios para estadísticas
](https://cloud.google.com/apigee/docs/hybrid/v1.2/obfuscate-userdata-for-
analytics?hl=es-419) . (142578910)

###  Expande volúmenes persistentes para conjuntos con estado

Se agregó una función que te permite expandir el volumen persistente utilizado
por apigee-cassandra para satisfacer las necesidades de almacenamiento, sin
agregar más potencia de procesamiento. A fin de obtener más información,
consulta [ Expande volúmenes persistentes para conjuntos con estado
](https://cloud.google.com/apigee/docs/release/notes/hybrid/v1.2/expand-
persistent-volumes?hl=es-419) . (138167919)

###  Se actualizan las versiones mínimas admitidas de GKE, Anthos y AKS

Apigee Hybrid ahora es compatible con GKE 1.14.x, Anthos 1.2 y AKS 1.14.x.
(149578101)

###  Compatibilidad con TLS 1.3 para conexiones de norte

Dos propiedades de configuración nuevas te permiten configurar la versión
mínima y máxima de TLS para las entradas: ` ingress.minTLSProtocolVersion ` y
` maxTLSProtocolVersion ` . Los valores posibles son 1.0, 1.1, 1.2 y 1.3. Para
obtener más información, consulta la [ referencia de propiedades de
configuración ](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-
ref?hl=es-419) . (117580780)

###  Compatibilidad con la configuración de proxy de reenvío para el entorno
de ejecución híbrido

El proxy HTTP de reenvío ahora es compatible con los proxies de API
implementados en un entorno. Para obtener más información, consulta [ Cómo
configurar el proxy de reenvío
](https://cloud.google.com/apigee/docs/hybrid/v1.2/forward-proxy?hl=es-419) .
(148970527)

###  Compatibilidad con varios hostAliases por entorno

Se agregó una nueva propiedad de configuración, ` envs[].hostAliases ` . Esta
propiedad te permite agregar varios alias de host a un entorno. Usa este
elemento en lugar de ` hostAlias ` , que dejó de estar disponible. Para
obtener más información, consulta [ Agrega varios alias de host a un entorno
](https://cloud.google.com/apigee/docs/hybrid/v1.2/environment-
create?hl=es-419#adding-multiple-host-aliases-to-an-environment) . (150738495)

###  Permite plantillas para conjuntos de propiedades

Se agregó un elemento nuevo {PropertySetRef} al elemento {AssignVariable} de
la política {AssignMessage}. <PropertySetRef> te permite crear un par de
nombre/clave de conjunto de propiedades de forma dinámica. Esta característica
solo está disponible para los proxies de API implementados en Apigee Hybris.
Consulta [ AssignVariable ](https://cloud.google.com/apigee/docs/api-
platform/reference/policies/assign-message-policy?hl=es-419#assignvariable) .
(148612340)

##  Fallas corregidas

En esta versión, se corrigieron los siguientes errores. Esta lista está
dirigida principalmente a que los usuarios verifiquen si se corrigieron sus
tickets de asistencia. No está diseñado para proporcionar información
detallada de todos los usuarios.

ID del problema  |  Nombre del componente  |  Descripción  
---|---|---  
147958049  |  Tiempo de ejecución  |  Se solucionó un problema de
sincronización en la secuencia de inicio del tiempo de ejecución que impedía
que el sincronizador se inicie de manera correcta.  
149867244  |  Plataforma K8S  |  El pod de apigee-cps-setup falla en la
configuración multirregional  
150187652 / 149117839  |  Tiempo de ejecución  |  No se pudo usar guiones en
los nombres de los entornos.  
149220463  |  Pod de MP  |  Los proxies implementados anteriormente debían
volver a implementarse.  
144321144  |  Tiempo de ejecución  |  No se pudieron volver a cargar los
proxies con hosts virtuales seguros.  
147685310  |  Tiempo de ejecución  |  Falló la inicialización del
sincronizador debido a una falla en la recuperación del token de GCP durante
la inicialización.  
151115900  |  Tiempo de ejecución  |  El sondeo interno periódico no ocurrió
para HyMMART, lo que da como resultado resultados falsos positivos.  
  
##  Problemas conocidos

En la siguiente tabla, se describen los problemas conocidos de esta versión:

Problema  |  Descripción  
---|---  
161658025  |

Estado de implementación inexacto para los flujos compartidos

En los flujos compartidos, el estado de implementación no se informa
correctamente a la IU, lo que genera un ícono de implementación girada de
forma indefinida. Si implementaste un flujo de uso compartido y ves el ícono
de implementación rotativo, debes suponer que la implementación falló.

Para obtener el estado de implementación correcto, usa la API [
v1.organizations.environments.sharedflows.revisions.deployments
](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest?hl=es-419#rest-
resource:-v1.organizations.environments.sharedflows.revisions.deployments) .
Por ejemplo:

    
    
    
    curl -s -H "$AUTH" \
    "https://apigee.googleapis.com/v1/o/$ORG/e/$ENV/sharedflows/$FLOW/revisions/$REV/deployments"  
  
N/A  |

Error de encabezado HTTP no válido: el Ingress de Istio cambia todas las
respuestas entrantes entrantes al protocolo HTTP2. Debido a que el procesador
de mensajes híbrido solo admite HTTP1, es posible que veas el siguiente error
cuando se llame a un proxy de API:

    
    
    
    http2 error: Invalid HTTP header field was received: frame type: 1, stream: 1,
       name: [:authority], value: [domain_name]

Si ves este error, puedes realizar alguna de las siguientes acciones para
corregir el problema:

  * Modifica el servicio de destino para omitir el encabezado de host en la respuesta. 
  * Si es necesario, quita el encabezado Host con la política AssignarMessage en el proxy de API. 

  
144584813  |  Si creas una sesión de depuración, pero la sesión aún no tiene
transacciones, entonces la [ API de lista de sesiones de depuración
](https://cloud.google.com/hybrid/v1.2/reference/apis/rest/v1/organizations.environments.apis.revisions.debugsessions/list?hl=es-419)
no incluye la sesión de esta lista. La API solo incluye sesiones en la
respuesta si la sesión contiene al menos una transacción.  
143659917  |

El parámetro de configuración de caducidad de la política PropagaseCache debe
configurarse como un valor explícito entre 1 y 30. Por ejemplo:

    
    
    
    <ExpirySettings>
      <TimeoutInSec>30</TimeoutInSec>
    </ExpirySettings>  
  
133192879  |

Resumen: Hay una latencia muy alta cuando se usa la API o la IU para obtener
el estado de implementación de la organización. Esta latencia puede generar
una respuesta ` HTTP 204 (No Content) ` o ` HTTP 400 (Bad Request) ` .

Solución alternativa: Actualiza el navegador (o vuelve a enviar la solicitud).

