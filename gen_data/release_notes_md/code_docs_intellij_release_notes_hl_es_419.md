#  Notas de la versión

En esta página, se presentan las actualizaciones de producción para Cloud
Code. Puedes consultar esta página si quieres ver anuncios sobre
características nuevas o actualizadas, correcciones de errores, problemas
conocidos y funciones obsoletas.

Las actualizaciones más recientes también se pueden encontrar en la [ página
de notas de la versión de GitHub
](https://github.com/GoogleCloudPlatform/cloud-code-
intellij/blob/master/CHANGELOG.md) .

Puedes ver las últimas actualizaciones de productos de todo Google Cloud en la
página [ Notas de la versión de Google Cloud
](https://cloud.google.com/release-notes?hl=es-419) .

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) o agrega
directamente la URL del feed: ` https://cloud.google.com/feeds/cloud-code-for-
intellij-release-notes.xml `

##  18.5.1

Ahora, Cloud Code está disponible en PyCharm (Community y Professional).
Explora tus depósitos de Cloud Storage y, también, interactúa con Cloud Source
Repositories desde PyCharm. Próximamente habrá más IDE.

###  Agregado

  * Complemento refactorizado para que las funciones independientes del lenguaje (Cloud Storage, Cloud Source Repositories) estén disponibles en otros IDE de JetBrains, además de IDEA. [ 1896 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1896)

###  Modificado

  * El SDK de Cloud administrado no se instalará en ninguna carga de IDE después de la primera cancelación manual. [ 2113 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2113)

###  Fijo

  * Se corrigió la excepción en el EAP 2018.2. [ 2124 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2124)

##  18.4.1

###  Agregado

  * Permite que el complemento de Google Cloud Tools administre el SDK de Cloud por ti, incluida la descarga, la instalación y las actualizaciones. Ya no es necesario descargar el SDK de forma manual. [ 673 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/673)
  * Mitiga los conflictos de versiones de dependencias con la asistencia para BOM de Java integrada en Google Cloud. Incluye la función de agregar forma automática la BOM cuando se agregan bibliotecas cliente de Google, además de inspeccionar pom.xml para ayudar a administrar conflictos de versiones de dependencias. [ 1921 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1921)
  * Agrega de forma automática las variables de entorno necesarias a los parámetros de configuración de ejecución local de App Engine a fin de acceder a las API de Google Cloud de forma local. [ 1917 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1917)

##  18.3.2

  * Se corrigió el error que provocaba el problema en la inicialización del complemento en las versiones 2017.2 y anteriores de IntelliJ IDEA. [ 1972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1972)

##  18.3.1

###  Agregado

  * Se agregó la capacidad de crear cuentas de servicio y descargar claves de cuenta de servicio del flujo de trabajo de la biblioteca cliente del IDE. [ 1808 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1808)

###  Fijo

  * Se corrigieron los casos en los que no se generaba ` appengine-web.xml ` debido a que faltaba ` web.xml ` . [ 1903 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1903)

##  18.2.1

###  Agregado

  * Se agregó la investigación y adición de la biblioteca cliente de Java para Google Cloud desde el IDE. [ 1806 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1806)
  * Se agregó la capacidad de habilitar las API de Google Cloud desde el IDE. [ 1807 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1807)

###  Modificado

  * Se actualizó el selector de proyectos en la nube con una experiencia del usuario mejorada. [ 1719 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1719)
  * Se actualizó el selector en la nube proyectos de para que la última selección se conserve y se establezca de forma predeterminada. [ 1812 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1812)

###  Fijo

  * Se corrigieron los artefactos de ejecución local estándar de App Engine faltantes. [ 1625 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1625)

##  18.1.1

###  Fijo

  * Se corrigió el mecanismo de informes de errores dañado. [ 1842 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1842)

##  17.12.2

###  Fijo

  * Se corrigió la configuración de la propiedad de estadísticas dañada. [ 1773 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1773)

##  17.12.1

El complemento de la Cuenta de Google se fusionó en el complemento de Cloud
Tools y ya no implica instalarlo por separado. Si ya tenías instalado el
complemento de Tools de la cuenta, sigue el nuevo cuadro de diálogo para
quitarlo y reinicia el IDE a fin de asegurarte de no surja ningún problema.

###  Fijo

  * Se corrigió el error de memoria insuficiente cuando se escribe y se buscan varios proyectos en el selector de proyectos en la nube. [ 1742 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1742)

###  Modificado

  * El complemento de la Cuenta de Google se integró en el complemento de Tools de Google Cloud. Ya no se requiere la instalación de un complemento de la Cuenta de Google. [ 1735 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1735)

##  17.11.1

###  Agregado

  * Integración de Cloud Storage en IntelliJ Ahora puedes explorar tus depósitos y ver su contenido sin salir del IDE. [ 1696 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1696)
  * Funciones de búsqueda y filtrado en el selector de proyectos en la nube. [ 1660 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1660)
  * Nuevo acceso directo al menú de herramientas “add App Engine framework support tools menu shortcut” (agregar compatibilidad con el framework de App Engine) a fin de proporcionar otra forma de agregar compatibilidad con App Engine a un proyecto. [ 1685 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1685)

###  Fijo

  * Se corrigió el mensaje de estado del indicador de región de App Engine cuando no se seleccionaba ningún proyecto en la nube. [ 1607 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1607)

##  17.9.2

Java 8 en el entorno estándar de App Engine ahora está [ disponible a nivel
general ](https://cloudplatform.googleblog.com/2017/09/Java-8-on-App-Engine-
Standard-environment-is-now-generally-available.html) .

###  Modificado

  * Se actualizó el asistente de proyecto estándar de App Engine para generar aplicaciones de Java 8 de forma predeterminada. [ 1641 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1641)

##  17.9.1

###  Agregado

  * Se agregó la capacidad de cambiar el nombre del artefacto por etapas para implementaciones flexibles de App Engine. [ 1610 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1610)

###  Modificado

  * Los parámetros de configuración de implementaciones flexibles de App Engine ahora implementan el artefacto tal como está de forma predeterminada, sin tener que cambiar el nombre a ` target.jar ` o ` target.war ` . [ 1151 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1151)
  * Se actualizó el nombre del artefacto de marcador de posición en las plantillas de Dockerfile que se generaron para aclarar que el usuario debe actualizarlo. [ 1648 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1648)
  * Ahora, los parámetros de configuración de la implementación estándar de App Engine actualizan de forma predeterminada los índices DoS, despacho, cron, colas y los índices del almacén de datos. [ 1613 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1613)
  * Los proyectos nativos que agregan compatibilidad con Endpoints Frameworks para App Engine ahora usan Endpoints V2. [ 1612 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1612)

###  Fijo

  * Se corrigió el error ` Deployment source not found ` cuando se implementan los artefactos de Maven. [ 1220 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1220)
  * Se corrigió el escalamiento del ícono de usuario en pantallas HiDPI. [ 1633 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1633)
  * Se solucionó un problema en el que el complemento cambiaba a una versión inferior en el IDEA 2017.3 EAP. [ 1631 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1631)

##  17.8.2

###  Fijo

  * Se solucionó el problema “Error: invalid_scope” cuando se accede a tu Cuenta de Google. [ 1598 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1598)

##  17.8.1

###  Agregado

  * Se agregó un vínculo de informes de problemas y comentarios al menú de acceso directo de Google Cloud Tools. [ 1560 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1560)

###  Modificado

  * Ahora los usuarios pueden guardar los parámetros de configuración de ejecución de implementación que se completaron de forma parcial o en un estado de error. [ 1407 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1407)

###  Fijo

  * Se solucionó el conflicto de lenguaje registrado de Docker que generaba problemas para ejecutar el complemento junto con el complemento .ignore. [ 1535 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1535)
  * Se corrigió el NPE que analizaba las marcas de tiempo de interrupción de Cloud Debugger. [ 1537 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1537)
  * Se quitó EAR como el tipo de artefacto de App Engine aceptable para las ejecuciones del servidor de desarrollo local. [ 1190 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1190)
  * Las implementaciones ahora se muestran en varias ventanas de IDE. [ 1432 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1432)
  * Se corrigió la falla que se generaba cuando se intentaba modificar una colección de solo lectura. [ 1571 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1571)

##  17.6.2

###  Fijo

  * Se corrigió el NPE que se generaba cuando había una configuración del servidor de desarrollo local, pero no una faceta estándar. [ 1525 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1525)

##  17.6.1

###  Agregado

  * Faceta flexible de App Engine con ` app.yaml ` y la configuración de Dockerfile [ 1514 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1514)
  * Detección de compatibilidad con el framework flexible de App Engine [ 1277 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1277)

###  Modificado

  * Permite que el usuario especifique un directorio de Docker, en lugar de solo un Dockerfile para implementaciones flexibles. [ 1304 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1304)
  * Actualiza la experiencia del usuario del diálogo de implementación (estándar y flexible). [ 1477 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1477)

###  Fijo

  * Se corrigió el tamaño del avatar de Google en pantallas HiPDI. [ 1391 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1391)

##  17.2.5_2017

###  Agregado

  * Las variables de entorno en la configuración de ejecución local estándar de App Engine ahora se pasan al servidor de desarrollo. [ #1364 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1364)
  * Las variables de entorno configuradas en appengine-web.xml ahora se respetan y se pasan al servidor de desarrollo. [ #377 ](https://github.com/GoogleCloudPlatform/appengine-plugins-core/issues/377)

##  17.2.4_2017

###  Agregado

  * Se agregó una casilla de verificación para implementar todos los archivos de configuración de App Engine durante la implementación del servicio. [ #1346 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1346)

##  17.2.3_2017

###  Modificado

  * Se quitó la marca “Clear Datastore” (Borrar Datastore) de la configuración del servidor de desarrollo local estándar de App Engine, ya que la versión actual del servidor no es compatible. ( [ #1345 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1345) ) 

##  17.2.2_2017

###  Fijo

  * Java Runtime Environment (JRE) no válido en la etapa de pruebas de una aplicación estándar de App Engine ( [ #1316 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1316) ): 
    
        > Unable to stage app: Cannot get the System Java Compiler. Please use a JDK, not a JRE.
    

##  17.2.1

¡Feliz año nuevo para los usuarios de Cloud Code! La primera versión de este
año es en esencia una versión de mantenimiento. Si tienes problemas de
autenticación cuando usas Cloud Source Repositories y nuestro complemento,
consulta [ esta posible solución
](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1174) .

A continuación, presentamos una lista de los cambios visibles:

###  Agregado

  * Compatibilidad con varios Cloud Source Repositories para un solo proyecto de GCP ( [ #1024 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1024) ) 
  * Inicialización de App Engine y selección de región ( [ #1232 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1232) ) 

###  Fijo

  * Detener dev_appserver en Windows siempre falla con ` com.intellij.execution.ExecutionException ` . ( [ #1215 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1215) ) 
  * El nuevo asistente de proyectos estándar de App Engine debería generar web.xml con el Servlet 2.5. ( [ #1194 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1194) ) 
  * La casilla de verificación “Clear datastore” (Borrar almacén de datos) para el servidor local estándar de App Engine no funciona. ( [ #1188 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1188) ) 
  * No mostrar proyectos programados para borrar en el selector de proyectos. ( [ #1119 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1119) ) 

Visita nuestro [ evento importante de actualización 17.2
](https://github.com/GoogleCloudPlatform/google-cloud-
intellij/milestone/19?closed=1) para obtener más información.

##  16.11.6

###  Agregado

  * Se expandió el elemento de menú de Google Cloud Tools con varios accesos directos. ( [ #1061 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1061) ). 
  * Verifica la compatibilidad mínima con la versión del SDK de Cloud. ( [ #1051 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1051) ). 
  * Crea de forma automática toda la configuración de ejecución relevante para las apps de App Engine Standard. ( [ #1063 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1063) ). 
  * El framework de App Engine ahora es un elemento secundario del framework web en el asistente de proyecto nuevo. ( [ #1065 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1065) ). 

###  Fijo

  * Las fuentes de implementación únicas en el panel de implementación del servidor de aplicaciones ahora aparecen como elementos de una sola línea individuales. ( [ #821 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/821) ). 
  * Validación de rutas de acceso del SDK de Cloud no válidas en Windows. ( [ #1091 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1091) ). 

##  16.10.5

IMPORTANTE: Este complemento requiere el uso del SDK de Cloud v.13.0.0 para la
ejecución correcta del servidor de desarrollo local con el SDK de Java 8 más
reciente. Ejecuta ` gcloud components update ` desde tu shell para asegurarte
de tener la versión más reciente del SDK de Cloud.

###  Fijo

  * Se solucionó el problema con el modo de depuración del servidor de desarrollo local cuando se realizan cambios mientras se ejecuta el servidor. ( [ #972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/972) ) 
  * Mejor redacción cuando el servidor de desarrollo tiene una ruta del SDK de Cloud no válida. ( [ #1043 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1043) ). 
  * Actualiza los nombres de configuración de ejecución para que tengan el prefijo “Google…” ( [ #1021 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1021) ). 

##  16.10.1

  * Ten en cuenta que cambiaremos el esquema de control de versiones a AA.MM.i. Planificamos una cadencia de actualización mensual para minimizar la interrupción de las actualizaciones. También ten en cuenta que hemos quitado la etiqueta “Beta”. 
  * ATENCIÓN: El servidor de desarrollo local de App Engine no funciona con las últimas versiones de JDK 8. ( [ #920 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/920) ). Esto debería solucionarse con la próxima versión del SDK de App Engine. 

###  Agregado

  * Importador de la biblioteca de App Engine Standard en el asistente de facetas y proyectos ( [ #866 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/866) ) 
  * Las aplicaciones de App Engine Standard que usen el nivel de lenguaje de Java 8 recibirán una notificación para usar el nivel 7 ( [ #966 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/966) ) 

###  Modificado

  * Se actualizaron los íconos y las etiquetas de configuración de ejecución (el Depurador de Cloud ahora es Depurador de Cloud)( [ #936 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/936) ). 

###  Fijo

  * Se corrigió el modo de depuración del servidor de desarrollo local ( [ #928 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/928) ) 
  * La implementación flexible no funciona en Windows 10 ( [ #937 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/937) ) 
  * El inspector de objetos del Depurador de Cloud ya funciona de nuevo ( [ #929 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/929) ) 
  * Marcas de tiempo de instantáneas del Depurador de Cloud que causan NPE ( [ #919 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/919) ) 

##  1.0-beta: 14/9/2016

###  Agregado

  * Compatibilidad con el entorno estándar de App Engine ( [ #767 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/767) ) 
  * Los campos adicionales ahora están disponibles en la configuración de implementación ( [ #868 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/868) ) 

##  0.9.7.5-beta: 29/8/2016

###  Agregado

  * Verifica que la implementación sea válida para el usuario acreditado o que se solicite agregar un usuario nuevo en caso contrario. ( [ 837 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/837) ) 

##  0.9.6-beta: 23/6/2016

###  Agregado

  * Implementa en el entorno de _compatibilidad_ flexible de App Engine. ( [ #720 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/720) ) 
  * Implementa en el entorno estándar de App Engine. ( [ #665 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/665) ) 
  * Verifica la compatibilidad de Cloud Tools y del complemento de cuenta. ( [ #651 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/650) ) 

###  Modificado

  * Se movió la entrada de la versión para que sea una configuración de nivel superior dentro del cuadro de diálogo de la configuración de la implementación. ( [ #639 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/639) ) 

##  0.9.4-beta: 20/4/2016

###  Agregado

  * Implementa en el elemento de menú de las herramientas del entorno flexible de App Engine. ( [ #635 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/635) ) 
  * Compatibilidad con proyectos basados en Maven como fuentes de implementación para implementaciones del entorno flexible de App Engine ( [ #600 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/600) ) 

###  Modificado

  * La implementación del entorno flexible de App Engine se puede cancelar si se desconecta de nuestro servidor de aplicaciones de App Engine. ( [ #581 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/581) ) 
  * El Dockerfile y el ` app.yaml ` generados por el entorno flexible de App Engine ahora se establecen de forma predeterminada como la ubicación recomendada en un proyecto de Java estructurado en Maven. ( [ #575 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/575) ) 

###  Fijo

  * Error de acceso que puede provocar que no se seleccione ningún usuario activo cuando se agrega uno ( [ #644 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/644) ) 
  * La anulación de una implementación de App Engine podría generar un error ( [ #599 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/599) ) 

