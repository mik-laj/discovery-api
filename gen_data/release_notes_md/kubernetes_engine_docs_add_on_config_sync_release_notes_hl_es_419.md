#  Notas de la versión

En esta página, se documentan las actualizaciones de producción del
Sincronizador de configuración. Consulta esta página para conocer los anuncios
sobre funciones nuevas o actualizadas, las correcciones de errores, los
problemas conocidos y las funciones obsoletas.

Puedes ver las últimas actualizaciones de productos de todo Google Cloud en la
página [ Notas de la versión de Google Cloud
](https://cloud.google.com/release-notes?hl=es_419) .

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , o agrega
directamente la URL del feed: ` https://cloud.google.com/feeds/kubernetes-
engine-add-on-config-sync-release-notes.xml `

##  1.2.0

Por lo general, la versión 1.2.0 de Config Sync está disponible para usarse en
producción. Esta es la primera versión del producto.

###  Problemas conocidos

**ISSUE:**

Si agregas un [ APIService ](https://kubernetes.io/docs/concepts/extend-
kubernetes/api-extension) al repositorio, se dejará Config Sync en mal estado
y con el mensaje de error “[KNV2002](/kubernetes-engine/docs/add-on/config-
sync/reference/errors#knv2002): no se pudieron obtener los recursos del
servidor: no se puede recuperar la lista completa de las API del servidor”.
Este problema afectará a los clústeres nuevos y existentes que se sincronizan
desde este repositorio. Para solucionar el problema, sigue estos pasos:

* Encuentra el nombre de los pods ` git-importer ` y ` syncer ` con ` kubectl get pods -n config-management-system ` . 
* Copia esos nombres y reinicia los pods con ` kubectl delete -n config-management-system pods git-importer-xxxx-xxxx syncer-xxxx-xxxx ` . 
* Estos pasos son obligatorios una vez para cada clúster. 
Una vez que los pods de un clúster se reinician, la sincronización vuelve a la
normalidad.

**ISSUE:**

` nomos view ` puede no analizar los CRD (definiciones de recursos
personalizados) que existen en la clonación local del repositorio, pero que
aún no se sincronizaron con un clúster.

Para solucionar este problema, usa [ ` nomos hydrate `
](https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/how-
to/nomos-command?hl=es_419#hydrate) en lugar de ` nomos view ` .

