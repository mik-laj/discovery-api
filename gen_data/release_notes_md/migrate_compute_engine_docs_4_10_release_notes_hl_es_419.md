#  Notas de la versión

En esta página, se documentan las actualizaciones de producción de Migrate for
Compute Engine. Puedes revisar esta página de forma periódica para ver
anuncios sobre características nuevas o actualizadas, correcciones de errores,
problemas comunes y funciones obsoletas.

Puedes ver las últimas actualizaciones de productos de todo Google Cloud en la
página [ Notas de la versión de Google Cloud
](https://cloud.google.com/release-notes?hl=es-419) .

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) o agrega
directamente la URL del feed: ` https://cloud.google.com/feeds/migrate-for-
compute-engine-release-notes.xml `

Para obtener una lista de compilaciones de esta versión y otras, consulta el [
Historial de compilación ](https://cloud.google.com/migrate/compute-
engine/docs/build-history?hl=es-419) .

##  Requisitos y compatibilidad del SO

Consulta [ Requisitos ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/concepts/requirements?hl=es-419) y [ Sistemas operativos
compatibles ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=es-419) .

##  Nuevas funciones de la versión 4.10

###  Integración en Cloud Console

**FEATURE:**

V4.10 se integra en [ GCP Console ](https://cloud.google.com/cloud-
console/?hl=es-419) para permitir la implementación sin problemas del
administrador de migración junto con la creación de cuentas de servicio
obligatorias.

###  Implementación en entorno de acceso privado

**FEATURE:**

V4.10 presenta compatibilidad con la implementación en entornos con acceso
privado a la API habilitado. En estos entornos, el sistema se implementará sin
una IP pública y dependerá del acceso privado para acceder a las API en la
nube. Consulta [ Cómo configurar el administrador de migración
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/configure-
manager/configuring-migration-manager?hl=es-419) .

###  Implementación opcional del complemento de vCenter

**FEATURE:**

V4.10 presenta la opción de implementación en un entorno de origen de vCenter
local con o sin implementar el complemento de vCenter. La implementación sin
el complemento de vCenter te permite conectar varios sistemas de Migrate al
mismo entorno de vCenter. Consulta [ Registra el entorno de VMware vCenter
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/configure-
manager/configuring-vms-vm?hl=es-419#register_the_vmware_vcenter_environment)
.

###  Compatibilidad con secuencias de comandos personalizadas previas y
posteriores cuando se actualiza Windows 2008 a 2012

**FEATURE:**

V4.10 introduce compatibilidad con la ejecución de secuencias de comandos
personalizadas previas o posteriores cuando se usa la actualización de
Windows. Puedes agregar secuencias de comandos personalizadas a la VM.
Consulta [ Cómo actualizar las VM de Windows Server
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/upgrading-
vms/upgrading-windows-vms?hl=es-419) para obtener más información.

###  Admite la migración de instancias de Azure Gen2 a Compute Engine

**FEATURE:**

V4.10 introduce compatibilidad con la migración de la instancia de [ Azure
Gen2 ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=es-419) a la instancia de
Compute Engine con compatibilidad con UEFI.

###  Descubrimiento de O/S automática y asignación de licencias

**FEATURE:**

V4.10 presenta una identificación automática del SO migrado, que, de forma
predeterminada, asignará la licencia correcta a la VM migrada. En situaciones
en las que deseas migrar VM con una licencia BYOL de Windows o una licencia
premium de Linux, deberás proporcionarlas como entradas en el runbook.
Consulta la [ sección de licencias ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/runbooks?hl=es-419) en la documentación.

##  Problemas resueltos

**FIXED:**

Se solucionó un problema con los controladores de ena de AWS que provocaba que
las imágenes de Windows fallaran después de la migración.

##  Problemas conocidos

**ISSUE:**

**#149004085:** Ubuntu 14 desde la ubicación local podría no iniciar la
conexión a la red luego de la desconexión.

**Solución:** Conéctate a través de la consola en serie y agrega manualmente
la interfaz de red con DHCP.

**ISSUE:**

**#145086776:** En casos excepcionales, es posible que las versiones
anteriores de RHEL7 se bloqueen durante la transmisión o alcancen un error de
kernel. Este problema se resolvió en versiones posteriores de RHEL7.

**Solución:** Ejecuta ` sudo yum update ` antes de migrar para actualizar el
sistema.

**ISSUE:**

**#145644737:** Las clonaciones creadas en Azure o AWS desde instancias de
distribuciones de Linux que pueden usar cloud-init pueden experimentar
problemas de arranque después de instalar el paquete de preparación de Linux.

**Solución:** Desinstala el paquete antes de la clonación y reinstálalo cuando
te preparas para la migración.

**ISSUE:**

**#143313211:** El cliente que migra a la VM RHEL 6.8 puede experimentar
problemas de inicio en el destino de la nube.

Los sistemas RHEL 6.x que usan versiones de kernel 2.6.32-xxx y LVM pueden
alcanzar un kernel panic cuando se inician en Compute Engine durante la
migración.

**Solución:** El kernel debe actualizarse a 2.6.32-754 o una versión posterior
antes de la migración.

**ISSUE:**

**#143262721:** La migración de VM desde Azure falla cuando el disco de datos
es mayor a 4 terabytes.

En este momento, Migrate for Compute Engine no admite la migración de VM de
Azure con discos de datos de más de 4 TB.

**Solución:** Asegúrate de que la VM tenga un disco de datos inferior a 4 TB.

**ISSUE:**

**#131532690:** Las operaciones de ejecución en la nube y de migración pueden
fallar para la carga de trabajo de Windows Server 2016 cuando se instala
Symantec Endpoint Protection (SEP). Esto también puede ocurrir cuando SEP
parece estar inhabilitado.

**Solución alternativa:** Modifica las vinculaciones de la interfaz de red de
la carga de trabajo para quitar la opción SEP.

  1. Descarga [ Microsoft Network VSP Bind (nvspbind) ](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850) . 
  2. Instala Microsoft_Nvspbind_package.EXE en c:\temp. 
  3. Abre un símbolo del sistema como administrador y ejecuta lo siguiente: 
    
        nvspbind.exe /d * symc_teefer2

**ISSUE:**

**#131614405:** Cuando se instala el RPM de Velostrata Prep en SUSE Linux
Enterprise Server 11, la VM obtiene una dirección IP de DHCP además de una
configuración de IP estática existente. Este problema se produce cuando la VM
se inicia de manera local en una subred que está habilitada con servicios de
DHCP.

Nota: El problema no se produce cuando la subred no tiene servicios de DHCP.
No hay impacto de conectividad para las comunicaciones con la dirección IP
estática original.

**ISSUE:**

**#131637800:** Después de registrar el complemento de Velostrata, la
ejecución del asistente de extensión de Cloud puede generar un error
"XXXXXXXXXX" cuando está “Finalizado”.

**Solución:** Cancela el registro del complemento de Velostrata y reinicia el
servicio de cliente web de vSphere, y vuelve a registrar el complemento.
Comunícate con el equipo de asistencia si el problema persiste.

**ISSUE:**

**#131548730:** En algunos casos, cuando una VM se mueve a la ejecución en la
nube mientras una solución de copia de seguridad a nivel de VM de terceros
tiene una instantánea temporal, las operaciones de reescritura periódicas de
Migrate for Compute Engine no se completarán incluso después de que la
solución de copia de seguridad borra la instantánea temporal. El contador de
escrituras no confirmadas en la VM mostrará un tamaño creciente, y no se
creará ningún punto de control de coherencia local.

**Solución:** Selecciona la acción de Ejecutar a nivel local para la VM y
espera a que se complete la tarea, lo que confirmará todas las escrituras
pendientes. Luego, vuelve a seleccionar la acción de ejecución en la nube. Ten
en cuenta que la confirmación de muchas escrituras pendientes puede llevar un
tiempo. No uses la opción Forzar, ya que esto provocará la pérdida de
escrituras no confirmadas.

**ISSUE:**

**#131605387:** El reinicio de vCenter hace que las tareas de Velostrata
desaparezcan de la IU. Esta es una limitación de vCenter.

**Solución:** Usa el módulo de PowerShell de Velostrata para supervisar las VM
administradas de Velostrata o las tareas de las extensiones de Cloud que se
estén ejecutando actualmente.

**ISSUE:**

**#131638716:** Con un host de ESXi en modo de mantenimiento, si una VM se
mueve a la nube, la operación fallará y se detendrá en la fase de reversión.

**Solución:** Cancela manualmente la tarea de ejecución en la nube, migra la
VM a otro host de ESXi en el clúster y vuelve a intentar ejecutar la operación
de ejecución en la nube.

**ISSUE:**

**#131638455** : Una operación de ejecución en la nube falla con el error: “No
se pudo crear una instantánea de máquina virtual. La operación que se intentó
no se puede realizar en el estado actual (apagado)”.

**Solución:** El archivo de instantánea de VM de VMware puede apuntar a una
instantánea no existente. Comunícate con el equipo de asistencia para corregir
el problema.

**ISSUE:**

**#131534862:** En casos excepcionales, después de ejecutar una carga de
trabajo local: las cargas de trabajo de VMDK están bloqueadas. En algunos
casos, esto se debe a interrupciones de la red entre el dispositivo de
administración de Velostrata y el host de ESXi en el que se ejecuta la carga
de trabajo.

Nota: El problema se resolverá después de 1 o 2 horas.

**ISSUE:**

**#131550214:** Durante la desconexión, la operación podría fallar con el
siguiente mensaje de error: “La operación se canceló”.

**Solución:** Vuelve a intentar la operación de desconexión.

**ISSUE:**

**#131650367:** Cuando se realiza una desconexión después de una operación de
desconexión, es posible que la acción falle.

**Solución:** Vuelve a intentar la operación.

**ISSUE:**

**#131649978:** En caso de fallas del sistema, los componentes de Velostrata
se desconectan de vCenter. En este caso, es posible que no se envíe un evento,
por lo que la alarma no se configurará correctamente o no se borrará
correctamente.

**Solución:** Borra la alarma manualmente en vCenter.

**ISSUE:**

**#131532549:** Para las cargas de trabajo con una máquina de Windows que usan
una licencia minorista, cuando regresan desde la nube, la licencia no está
presente.

**Solución:** Reinstala la licencia.

**ISSUE:**

**#131555885:** La operación "Exportar OVA" de vCenter está disponible cuando
la VM en la nube se ejecuta en modo de caché; sin embargo, esta operación da
como resultado un OVA dañado.

**Solución alternativa:** Solo crea un OVA después de la desconexión.

**ISSUE:**

**#131647857:** En casos excepcionales, cuando se crea una instancia de
componente de nube y el sistema falla antes de que se etiquete, la instancia
permanecerá sin etiquetar. Esto no permitirá la limpieza completa ni la
reparación del CE.

**Solución:** Etiqueta la instancia de forma manual y, luego, ejecuta
"Reparar".

**ISSUE:**

**#131537125:** La alta disponibilidad de la extensión de Cloud no funciona
para cargas de trabajo que ejecutan el sistema operativo Ubuntu con
configuración de LVM.

**Solución:** Actualiza el kernel a la versión 3.13.0-161 o posterior.

**ISSUE:**

**#131560126:** Suse12: debido a un error en el kernel de SUSE anterior a 4.2,
no se admiten las configuraciones que incluyen activaciones de BTRFS con
subvolúmenes.

**Solución:** Actualiza a la versión de SUSE con kernel >=4.2 (SP2).

**ISSUE:**

**#131533480:** Cuando se usa el asistente de creación de extensiones de
Cloud, el uso de una dirección de proxy HTTP ilegal no generará un mensaje de
advertencia.

**Solución:** Borra el CE y, luego, crea el CE con una dirección proxy HTTP
válida.

**ISSUE:**

**#131647654:** La operación local se ejecutó correctamente, pero el estado se
marcó fallida con el error "No se pudieron consolidar las instantáneas".

**Solución:** Consolida las instantáneas a través de vCenter y borra el error
de forma manual.

**ISSUE:**

**#131558198:** El cliente de PowerShell para Runbook de nube a nube informa
los errores cuando se ejecuta en PowerShell 3.0.

**Solución:** Actualiza a PowerShell 4.0.

**ISSUE:**

**#131533056:** Cuando migres RHEL 7.4 de AWS a Google Cloud, el agente de
Google Cloud no se instalará automáticamente.

**Solución:** Quita manualmente el agente de AWS y, luego, instala el agente
de Google Cloud

**ISSUE:**

**#131532713:** Después de la migración sin conexión de Windows 2003R2, si se
borra una NIC de forma manual, puede ser imposible detectarla y reinstalarla
automáticamente.

Solución: El almacenamiento de la VM puede conectarse a una VM diferente y la
entrada del registro de NIC se puede importar manualmente con una VM similar
como referencia. Comunícate con el equipo de asistencia para recibir ayuda.

**ISSUE:**

**#131532666:** Las versiones de Linux que se ejecutan con la versión de
kernel 2.6.32 pueden experimentar un kernel panic en las fallas de acceso al
almacenamiento efímero; es más probable que suceda cuando se transmiten a
través de iSCSI.

Solución: Actualiza tu kernel. La probabilidad de que se genere este problema
se reducirá luego de la desconexión.

**ISSUE:**

**#131532846:** Algunos firewalls y antivirus pueden hacer que las VM de
Windows fallen cuando se mueven a la nube mediante el bloqueo del tráfico
iSCSI.

Solución: Inhabilita el servicio afectado durante la migración y la
reinstalación después de la desconexión.

**ISSUE:**

**#131532882:** En ciertos casos, iniciar la ejecución en la nube durante una
actualización de Windows puede hacer que la actualización finalice de forma
abrupta y provoque un error de inicio en la nube.

Solución: Permite que el sistema finalice la actualización de Windows o
suspende las actualizaciones de Windows antes de la migración.

**ISSUE:**

**#135664281:** Cuando se completa o cancela la migración de Azure a Google
Cloud, si la administración de Velostrata no pudo iniciar el importador, los
recursos creados por Velostrata pueden quedar en el grupo de recursos de la
instancia original.

**ISSUE:**

**#133137658:** Situación: Sin conexión de red entre el administrador de
migración y VSphere

Impacto en el cliente: La tarea RunInCloud permanecerá detenida debido a una
falla en la llamada a getReadSessions en VSphere.

**Solución** : Corrige la conexión de red. Si no es así, cancela la tarea y
vuelve a intentarlo.

**ISSUE:**

**#135573857** Situación: Cuando se mueve una VM de vuelta a la local con la
marca "forzar", la falla para consolidar la instantánea hará que la VM
permanezca como administrada por Velostrata. RunInCloud en la misma VM puede
fallar, ya que no está permitida en las VM administradas.

**Solución:** Espera un par de minutos y vuelve a intentarlo.

**ISSUE:**

**#137082702:** En casos excepcionales, la operación Cancelar desconexión se
realiza correctamente, pero la instancia de VM no se iniciará.

**Solución** : Mueve la instancia y vuelve a moverla a la nube.

