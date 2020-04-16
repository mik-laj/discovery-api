#  Notas de la versión de Python 3

Python [ 2.7
](https://cloud.google.com/appengine/docs/standard/python/release-
notes?hl=es_419 "Ver esta página en el entorno de ejecución de Python 2.7") /
3.7  |  Java [ 8
](https://cloud.google.com/appengine/docs/standard/java/release-
notes?hl=es_419 "Ver esta página en el entorno de ejecución de Java 8") / [ 11
](https://cloud.google.com/appengine/docs/standard/java11/

release-notes?hl=es_419 "Ver esta página en el entorno de ejecución de
Java 11") |  PHP [ 5
](https://cloud.google.com/appengine/docs/standard/php/release-notes?hl=es_419
"Ver esta página en el entorno de ejecución de PHP 5") / [ 7
](https://cloud.google.com/appengine/docs/standard/php7/

release-notes?hl=es_419 "Ver esta página en el entorno de ejecución de PHP 7")
|  [ Ruby ](https://cloud.google.com/appengine/docs/standard/ruby/

release-notes?hl=es_419 "Ver esta página en el entorno de ejecución de Ruby")
|  Go [ 1.9 ](https://cloud.google.com/appengine/docs/standard/go/release-
notes?hl=es_419 "Ver esta página en el entorno de ejecución de Go 1.9") / [
1.11 ](https://cloud.google.com/appengine/docs/standard/go111/

release-notes?hl=es_419 "Ver esta página en el entorno de ejecución de
Go 1.11") / [ 1.12 ](https://cloud.google.com/appengine/docs/standard/go112/

release-notes?hl=es_419 "Ver esta página en el entorno de ejecución de
Go 1.12") |  [ Node.js
](https://cloud.google.com/appengine/docs/standard/nodejs/

release-notes?hl=es_419 "Ver esta página en el entorno de ejecución de
Node.js")

Además de las notas de versión siguientes, también puedes hacer un seguimiento
de los problemas conocidos desde la función de [ seguimiento de problemas
](https://issuetracker.google.com/issues?q=componentid%3A187191%2B&hl=es_419)
.

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feed
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  30 de julio de 2019

  * Las herramientas AppCfg y el SDK de App Engine independiente heredado, entregados a través de los archivos ` GoogleAppEngineLauncher.dmg ` , ` GoogleAppEngine.msi ` y ` google_appengine.zip ` , han quedado obsoletos. Google cerrará y retirará la asistencia el 30 de julio de 2020. 
  * Las funcionalidades del SDK de App Engine se entregan exclusivamente a través del [ SDK de Cloud ](https://cloud.google.com/sdk/docs?hl=es_419) . Para obtener más información, consulta [ Migra al SDK de Cloud ](https://cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration?hl=es_419) . 

##  18 de abril de 2019

  * App Engine ahora está disponible en la región ` asia-northeast2 ` (Osaka, Japón). 

##  15 de abril de 2019

  * App Engine ya está disponible en la región ` europe-west6 ` (Zúrich, Suiza). 

##  9 de abril de 2019

  * [ Cloud Tasks ](https://cloud.google.com/tasks/docs?hl=es_419) ahora tiene disponibilidad general y se puede usar para configurar tareas que deben realizarse de forma asíncrona, fuera de las solicitudes de los usuarios. 

  * [ El acceso a VPC sin servidores ](https://cloud.google.com/appengine/docs/standard/python3/connecting-vpc?hl=es_419) ahora está en versión Beta. El acceso a VPC sin servidores permite que tu aplicación se conecte a recursos internos en tu red de VPC, como instancias de VM de Compute Engine, instancias de Cloud Memorystore y más. 

##  4 de abril de 2019

  * Se actualizó el entorno de ejecución de Python 3 a la versión 3.7.3. 

##  11 de enero de 2019

  * Se actualizó el entorno de ejecución de Python 3 a la versión 3.7.2. 

##  14 de diciembre de 2018

  * El [ entorno de ejecución de Python 3.7 ](https://cloud.google.com/appengine/docs/standard/python3?hl=es_419) para el entorno estándar de App Engine tiene ahora disponibilidad general. 

##  12 de diciembre de 2018

  * Se actualizó el SDK de Python a la versión 1.9.81. 
  * Se cambiaron todas las aplicaciones a los sockets de red de BSD. No se requieren cambios en las aplicaciones. 
  * La [ API de Sockets ](https://cloud.google.com/appengine/docs/standard/python/sockets?hl=es_419) ahora tiene disponibilidad general. 

##  16 de noviembre de 2018

  * nginx ahora es el servidor web predeterminado. No se requieren cambios en las aplicaciones. 

##  31 de octubre de 2018

  * Se actualizó el entorno de ejecución de Python 3 a la versión 3.7.1 de Python. 
  * El entorno de ejecución de Python 3 es compatible con entradas recurrentes en el archivo ` requirements.txt ` . 

##  22 de octubre de 2018

  * App Engine ya está disponible en la región ` asia-east2 ` (Hong Kong). 

##  8 de agosto de 2018

  * El [ entorno de ejecución de Python 3.7 ](https://cloud.google.com/appengine/docs/standard/python3?hl=es_419) para el entorno estándar de App Engine ahora está en versión Beta. 
  * Está disponible una lista de las [ diferencias entre los entornos de ejecución de Python 2.7 y Python 3.7 ](https://cloud.google.com/appengine/docs/standard/python3/python-differences?hl=es_419) . 

##  10 de julio de 2018

  * App Engine ya está disponible en la región ` us-west2 ` (Los Ángeles). 

##  2 de julio de 2018

Se corrigió un error en [ la configuración del ajuste de escala automático
](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=es_419#scaling_elements)
en el que App Engine cerraba instancias de forma agresiva cuando se usaba la
configuración ` max_instances ` .

##  15 de mayo de 2018

  * Se completó el lanzamiento gradual de una actualización al sistema de ajuste de escala automático: 
    * Mayor eficiencia, que, por regla general, reduce el costo de las instancias (hasta un 6% para muchos usuarios) y las _solicitudes de carga_ (hasta un 30%), que son la primera solicitud a una instancia nueva. 
    * La nueva configuración de instancias máximas te permite limitar la cantidad total de instancias que se programarán. 
    * La nueva configuración de instancias mínimas te permite especificar un número mínimo de instancias que se seguirán ejecutando para tu aplicación. 
    * La nueva configuración del uso de CPU objetivo te permite optimizar la latencia y el costo. 
    * La nueva configuración de capacidad de procesamiento objetivo te permite optimizar el número de solicitudes simultáneas en las que se inician instancias nuevas. 
    * No hay más instancias residentes en el ajuste de escala automático. Anteriormente, si usabas la configuración ` min_idle_instances ` , las instancias inactivas mínimas se etiquetaban como _residentes_ en Cloud Console y el resto de las instancias se etiquetaban como _dinámicas_ . El nuevo programador simplemente etiqueta todas las instancias como _dinámicas_ con el ajuste de escala automático. Sin embargo, el comportamiento subyacente sigue siendo similar al comportamiento anterior. Si usas ` min_idle_instances ` y habilitas las solicitudes de preparación, verás al menos esa cantidad de instancias dinámicas ejecutándose incluso durante períodos sin tráfico. 
    * Para obtener más detalles, consulta la [ documentación del ajuste de escala automático ](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=es_419#scaling_elements) . 

##  14 de diciembre de 2017

  * Documentación de control de acceso mejorada sobre la implementación de aplicaciones con cuentas de servicio y funciones de IAM: 

    * [ Funciones predefinidas de App Engine ](https://cloud.google.com/appengine/docs/standard/python3/access-control?hl=es_419#predefined_app_engine_roles)
    * [ Implementa con las funciones de IAM ](https://cloud.google.com/appengine/docs/standard/python3/granting-project-access?hl=es_419#deploying_using_iam_roles)
    * [ Requiere permisos ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=es_419#required_permissions)

##  31 de octubre de 2017

  * App Engine ya está disponible en la región ` asia-south1 ` (Bombay, India). 

##  11 de octubre de 2017

  * Se anunció la disponibilidad general del [ firewall de App Engine ](https://cloud.google.com/appengine/docs/standard/python3/creating-firewalls?hl=es_419) . 

##  13 de septiembre de 2017

  * Ahora puedes usar certificados administrados para agregar SSL a tu dominio personalizado. Una vez que asignas tu dominio personalizado a tu aplicación, App Engine aprovisiona automáticamente un certificado SSL y gestiona la renovación del certificado antes de su vencimiento y lo revoca si quitas el dominio personalizado. Los certificados administrados están disponibles en versión Beta. Para obtener más información, consulta [ Protege dominios personalizados con SSL ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=es_419) . 

  * Si tienes un certificado SSL y una asignación de dominio existente, entonces continúa funcionando como se esperaba. También puedes [ actualizar a certificados SSL administrados ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=es_419#updating_to_managed_ssl_certificates) . 

  * Los comandos de ` gcloud ` y los métodos de la API de Administrador utilizados para [ asignar dominios personalizados ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=es_419) ahora tienen disponibilidad general. Esto incluye [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains?hl=es_419) y [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=es_419) . Sin embargo, si deseas usar certificados SSL administrados, usa los métodos y comandos Beta que se especifican en [ Protege dominios personalizados con SSL ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=es_419) . 

##  5 de septiembre de 2017

  * App Engine ya está disponible en la región ` southamerica-east1 ` (São Paulo, Brasil). 

##  1 de agosto de 2017

  * App Engine ya está disponible en la región ` europe-west3 ` (Fráncfort, Alemania). 

##  18 de julio de 2017

  * App Engine ya está disponible en la región ` australia-southeast1 ` (Sídney, Australia). 

##  6 de junio de 2017

  * App Engine ya está disponible en la región ` europe-west2 ` (Londres). 
  * Ahora puedes usar las funciones de nivel Beta en la API de Administrador y en la herramienta de línea de comandos de ` gcloud ` para [ crear y administrar tus dominios personalizados y tus certificados SSL ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=es_419) . 

##  9 de mayo de 2017

  * App Engine ya está disponible en la región ` us-east4 ` (Virginia del Norte). 

##  27 de octubre de 2016

  * Los servicios Channel y XMPP ahora están [ obsoletos ](https://cloud.google.com/appengine/docs/deprecations?hl=es_419) . Estos servicios se desactivarán el 31 de octubre de 2017. 

##  1 de agosto de 2016

**Notas de la API de Administrador**

  * La versión 1 de la [ API de Administrador ](https://cloud.google.com/appengine/docs/admin-api?hl=es_419) ahora tiene disponibilidad general. 

##  1 de agosto 2016 - Versión 1.9.42

**Notas del entorno de ejecución de Python 3.7**

  * Esta versión no incluye un SDK nuevo de Python 3.7. Los usuarios de Python 3.7 deberían continuar usando el SDK 1.9.40. 

##  18 de julio de 2016 - Versión 1.9.40

  * Se omitió la versión 1.9.39. 

  * Las solicitudes LeaseTasksByTag se limitarán a 25 solicitudes por segundo. 

  * Los errores de servidor y de cliente ahora reflejan con mayor precisión los errores de estado por URL en el panel de App Engine. 

  * [ Explicación guiada para App Engine ](https://console.cloud.google.com/start/appengine?hl=es_419) nueva en GCP Console. Elige el idioma que prefieras y ejecuta un instructivo interactivo directamente en la consola. 

  * Aumenta el límite máximo de tareas cron a 250. 

##  1 de julio de 2016

**Cloud Datastore**

  * El [ precio de Cloud Datastore ](https://cloud.google.com/appengine/pricing?hl=es_419#costs-for-datastore-calls) nuevo ahora está en vigor. 

##  25 de mayo de 2016 - Versión 1.9.38

  * El error que muestra la recuperación de URL para una solicitud a un puerto fuera de los rangos permitidos (80-90, 440-450, 1024-65535) ahora siempre mostrará ` INVALID_URL ` como se documenta. 

**Cloud Datastore**

  * Cuando se confirma una transacción entre grupos, los números de versión que se muestran para las entidades nuevas o actualizadas son todos iguales. Con el comportamiento anterior, las entidades dentro del mismo grupo confirmadas como parte de una transacción entre grupos tenían el mismo número de versión, pero las entidades en diferentes grupos podían haber tenido diferentes números de versión. Este cambio garantiza que todas las entidades nuevas y actualizadas tengan un número de versión idéntico, independientemente de su grupo de entidades, cuando se confirman como parte de una transacción entre grupos. Como antes, las entidades que no se actualizan no tendrán un número de versión nuevo. 

##  4 de mayo de 2016 - Versión 1.9.37

Incluye correcciones de errores generales y mejoras.

##  2 de mayo de 2016

**Entorno flexible de App Engine**

  * El [ entorno de ejecución de Ruby ](https://cloud.google.com/appengine/docs/flexible/ruby?hl=es_419) ahora está disponible para el entorno flexible de App Engine. 

##  18 de abril de 2016 - Versión 1.9.36

En respuesta a tus solicitudes, la API de usuarios de App Engine se une al
resto de App Engine para admitir expansión de grupo y funciones de IAM. Esto
significa que cualquier usuario que sea propietario, editor o visualizador del
proyecto o administrador de App Engine es considerado como un "administrador"
por la API de usuarios, con independencia de si se le otorgó la función al
usuario directamente o por ser miembro de un grupo. * Esta versión propaga los
detalles del error, cuando están disponibles, en mensajes de error asociados
con el tipo de excepción "OverQuota".

##  24 de marzo de 2016 - Versión 1.9.35

  * VM administradas de App Engine cambia su nombre a [ entorno flexible de App Engine ](https://cloud.google.com/appengine/docs/flexible?hl=es_419) . 
  * Corrige las marcas de tiempo de seguimiento para que coincidan con las marcas de tiempo del registro. 

##  4 de marzo de 2016 - Versión 1.9.34

  * Aumenta la cuota predeterminada para la recuperación de URL para aplicaciones facturadas. Consulta la [ página Cuotas ](https://cloud.google.com/appengine/docs/quotas?hl=es_419#UrlFetch) para obtener más detalles. 

##  17 de febrero de 2016 - Versión 1.9.33

  * La ruta de URL "/form" ahora está permitida y se reenviará a las aplicaciones. Anteriormente, esta ruta estaba bloqueada. 

##  3 de febrero de 2016 - Versión 1.9.32

  * Opciones de construcción de contenedores para VM administradas 

Los comandos ` gcloud preview app deploy ` (y ` mvn gcloud:deploy ` ) suben
tus artefactos a nuestros servidores y compilan un contenedor para implementar
tu aplicación en el entorno de VM administrada.

Existen dos mecanismos para compilar la imagen de contenedor de forma remota.
El comportamiento predeterminado es crear el contenedor en una máquina virtual
transitoria de Compute Engine que tiene instalado Docker. Como alternativa,
puedes usar el servicio de [ Cloud Build ](https://cloud.google.com/cloud-
build/docs?hl=es_419) . Para usar el servicio de Cloud Build, sigue estos
pasos:

    1. [ Activa la API Cloud Build ](https://support.google.com/cloud/answer/6158841?hl=es_419) para tu proyecto. 
    2. Usa el comando ` gcloud config set app/use_cloud_build True ` . Esto hará que todas las invocaciones de ` gcloud preview app deploy ` usen el servicio. (Para volver al comportamiento predeterminado, usa el comando ` gcloud config set app/use_cloud_build False ` ). 

##  14 de enero de 2016 - Versión 1.9.31

App Engine ahora admite Grupos de Google: cuando agregas un Grupo de Google
como miembro de un proyecto, los miembros del grupo obtienen acceso a App
Engine. Por ejemplo, si un Grupo de Google es editor en un proyecto, todos los
miembros del grupo ahora tienen acceso de editor a la aplicación de App
Engine.

##  30 de noviembre de 2015 - Versión 1.9.30

Los encabezados para solicitudes de lista de aplicaciones en cola realizados
para tareas de lista de tareas en cola sin carga útil ahora contendrán una
entrada de Content-Length establecida en "0". Anteriormente, los encabezados
para tales solicitudes no contenían entradas de Content-Length.

##  30 de noviembre de 2015 - Versión 1.9.29

  * Deja de calcular y almacenar la profundidad de la cola para colas inexistentes, colas marcadas para eliminación y en el caso de interrupciones de la tabla de colas. 
  * Para los desarrolladores que usan la [ API de Endpoints ](https://cloud.google.com/appengine/docs/standard/python/endpoints/create_api?hl=es_419#defining_the_api_endpointsapi) , se agregó un parámetro booleano detectable a la anotación @Api a fin de permitir que los usuarios inhabiliten la detección de la API. El uso de esta función evitará que algunas bibliotecas cliente (p. ej., JavaScript) y el Explorador de API funcionen, ya que dependen de la detección. 

##  29 de octubre de 2015 - Versión 1.9.28

La API de búsqueda potencial, que quedó obsoleta el 14 de julio de 2015, ahora
está restringida a los usuarios existentes. Se desactivará por completo el 1
de diciembre de 2015. * Mejoras en la precisión del filtro geográfico en la
búsqueda de consultas.

##  25 de septiembre de 2015 - Versión 1.9.27

Las aplicaciones recientemente habilitadas para facturación ahora tienen un
presupuesto diario ilimitado y no un presupuesto diario máximo de $0. Esto
evita interrupciones no deseadas debido a la falta de presupuesto. Para
establecer un límite en el costo diario de tu aplicación, después de habilitar
la facturación, establece un presupuesto en la [ configuración de App Engine
](https://console.cloud.google.com/project/_/appengine/settings?hl=es_419) .
Para obtener más información, consulta la página sobre [ cómo configurar un
presupuesto diario ](https://cloud.google.com/appengine/docs/developers-
console?hl=es_419#setting_a_daily_budget) .

Datastore

  * Corrección de errores: ahora se permiten facetas numéricas repetidas. 
  * La búsqueda por facetas ahora tiene disponibilidad general. 

##  27 de agosto de 2015 - Versión 1.9.26

  * Biblioteca oauth2client actualizada a la versión [ 1.4.2 ](https://github.com/google/oauth2client/blob/master/CHANGELOG.md)
  * Agrega el menú "mostrar en contexto" para los registros de aplicaciones MVM que tienen thread_id o request_id como campo en su entrada de registro. Esto permite ordenar los registros de la aplicación en función de cualquier campo. 
  * Capacidad para aprovisionar aplicaciones para la carga actual y configurar el aprovisionamiento elástico basado en métricas de nivel de aplicación y VM. 
  * Ahora se puede acceder a la API remota mediante el uso de las credenciales de OAuth2 con https://developers.google.com/identity/protocols/application-default-credentials 
  * Usa RequestPayloadTooLargeException para solicitudes URLFetch con cargas útiles que son demasiado grandes. 

##  14 de agosto de 2015 - Versión 1.9.25

  * Se agregó la versión 0.7.2 (Beta) de PyAMF. 
  * Los menús de la Consola del administrador comienzan a redireccionarse a GCP Console. Los servicios seleccionados, como los registros de administrador, seguirán estando disponibles en la Consola del administrador. 
  * Datastore ahora permite que las propiedades representen la lista vacía. 
  * Las tareas fallidas en las colas configuradas con un "retry_limit" de cero ya no se volverán a intentar. 

