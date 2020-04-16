#  Notas de la versión

En esta página, se documentan las actualizaciones de producción para Cloud
TPU. Puedes consultar esta página de manera periódica si quieres ver anuncios
sobre características nuevas o actualizadas, correcciones de errores,
problemas conocidos y funcionalidad obsoleta.

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feed
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  7 de mayo de 2019

**FEATURE:**

El pod de Cloud TPU v2 está disponible en versión Beta.

Dado que los recursos de TPU pueden escalar a partir de una sola Cloud TPU a
un pod de Cloud TPU, no necesitas elegir entre una sola Cloud TPU y un pod de
Cloud TPU. Puedes solicitar partes de pods de Cloud TPU en _porciones_ o
conjuntos de núcleos, para comprar solo la potencia de procesamiento que
necesitas.

[ Ventajas del pod de Cloud TPU (Beta) sobre un solo dispositivo Cloud TPU v2:
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=es_419)

  * Mayores velocidades de entrenamiento para la iteración rápida en la investigación y el desarrollo 
  * Mayor productividad humana gracias al procesamiento escalable automáticamente del aprendizaje automático (AA) 
  * La capacidad de entrenar modelos mucho más grandes 

**FEATURE:**

El pod de Cloud TPU v3 está disponible en versión Beta.

Dado que los recursos de TPU pueden escalar a partir de una sola Cloud TPU a
un pod de Cloud TPU, no necesitas elegir entre una sola Cloud TPU y un pod de
Cloud TPU. Puedes solicitar partes de pods de Cloud TPU en _porciones_ o
conjuntos de núcleos, para comprar solo la potencia de procesamiento que
necesitas.

[ Ventajas del pod de Cloud TPU (Beta) sobre un solo dispositivo Cloud TPU v3:
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=es_419)

  * Mayores velocidades de entrenamiento para la iteración rápida en la investigación y el desarrollo 
  * Mayor productividad humana gracias al procesamiento escalable automáticamente del aprendizaje automático (AA) 
  * La capacidad de entrenar modelos mucho más grandes 

Ventajas del pod de Cloud TPU v3 _(Beta)_ sobre un pod de Cloud TPU v2
_(Beta)_ :

* Procesamiento más rápido y memoria más grande: 

  * Pod v2: 11.5 petaflops y 4 TB de memoria en chip (HBM) 
  * Pod v3: 100 petaflops y 32 TB HBM, con refrigeración líquida 

* Puedes entrenar modelos incluso más grandes. 

##  11 de marzo de 2019

**CHANGED:**

Cloud TPU ahora es compatible con la [ versión 1.13 de TensorFlow
](https://www.tensorflow.org/versions/r1.13/api_docs/?hl=es_419) . Se quitó la
compatibilidad para las versiones 1.8 y 1.9 de Tensorflow.

Consulta las versiones de TensorFlow compatibles actuales en la [ política de
control de versiones de Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=es_419) .

##  31 de enero de 2019

**FEATURE:**

Cloud TPU v3 ahora tiene disponibilidad general. Cloud TPU v3 tiene el doble
de memoria que v2. Esto proporciona un rendimiento mejorado y permite la
compatibilidad con más clases de modelos, por ejemplo, imágenes más grandes
con RetinaNet y ResNets más profundos. Los modelos existentes que se ejecutan
en Cloud TPU v2 no dejarán de funcionar. Consulta la [ guía de versiones de
Cloud TPU ](https://cloud.google.com/tpu/docs/deciding-tpu-version?hl=es_419)
para obtener más información.

##  8 de noviembre de 2018

**CHANGED:**

Cloud TPU ahora es compatible con la [ versión 1.12 de TensorFlow
](https://www.tensorflow.org/versions/r1.12/api_docs/?hl=es_419) . Esta
versión incluye mejoras para Keras en Cloud TPU, optimizaciones de rendimiento
en toda la pila de software y API mejoradas, mensajes de error y
confiabilidad.

Consulta las versiones de TensorFlow compatibles actuales en la [ política de
control de versiones de Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=es_419) .

##  7 de noviembre de 2018

**FEATURE:**

El pod de Cloud TPU v2 está disponible en versión Alfa.

Dado que los recursos de TPU pueden escalar a partir de una sola Cloud TPU a
un pod de Cloud TPU, no necesitas elegir entre una sola Cloud TPU y un pod de
Cloud TPU. Puedes solicitar partes de pods de Cloud TPU en _porciones_ o
conjuntos de núcleos, para comprar solo la potencia de procesamiento que
necesitas.

[ Ventajas de un pod de Cloud TPU (Alfa)
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=es_419)

  * Mayores velocidades de entrenamiento para la iteración rápida en la investigación y el desarrollo 
  * Mayor productividad humana gracias al procesamiento escalable automáticamente del aprendizaje automático (AA) 
  * La capacidad de entrenar modelos mucho más grandes que en un solo acelerador del AA 

##  10 de octubre de 2018

**FEATURE:**

Cloud TPU v3 está disponible en versión Beta. Ahora tienes que elegir entre v2
y v3 en la configuración.

  * Cloud TPU v3 tiene el doble de memoria que v2. Esto proporciona un rendimiento mejorado y permite la compatibilidad con más clases de modelos, por ejemplo, imágenes más grandes con RetinaNet y ResNets más profundos. 
  * Los modelos existentes que se ejecutan en Cloud TPU v2 no dejarán de funcionar. 
  * Consulta la [ guía de versiones de Cloud TPU para obtener más información. ](https://cloud.google.com/tpu/docs/deciding-tpu-version?hl=es_419)

##  10 de octubre de 2018

**CHANGED:**

Las TPU interrumpibles ahora tienen disponibilidad general. Una TPU
interrumpible es un nodo de Cloud TPU que puedes crear y ejecutar a un precio
mucho más bajo que los nodos normales. Sin embargo, Cloud TPU puede cancelar
(interrumpir) estos nodos si requiere acceso a los recursos para otro
propósito.

  * Consulta cómo [ usar una TPU interrumpible ](https://cloud.google.com/tpu/docs/preemptible?hl=es_419) . 
  * Revisa los [ precios ](https://cloud.google.com/tpu/docs/pricing?hl=es_419) de los nodos interrumpibles y normales de Cloud TPU. 

##  27 de septiembre de 2018

**CHANGED:**

Cloud TPU ahora es compatible con la [ versión 1.11 de TensorFlow
](https://www.tensorflow.org/versions/r1.11/api_docs/?hl=es_419) . TensorFlow
1.11 presenta compatibilidad experimental para todo lo siguiente en Cloud TPU:
Keras, Colab, ejecución inmediata, LARS, RNN y [ Mesh TensorFlow
](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/mesh_tensorflow/README.md)
. Esta versión también presenta una integración de [ Cloud Bigtable
](https://cloud.google.com/bigtable/?hl=es_419) de alto rendimiento, nuevas
optimizaciones del compilador XLA, otras optimizaciones de rendimiento en toda
la pila de software y proporciona API mejoradas, mensajes de error y
confiabilidad.

Consulta las versiones de TensorFlow compatibles actuales en la [ política de
control de versiones de Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=es_419) .

##  7 de septiembre de 2018

**CHANGED:**

La compatibilidad con la versión 1.7 de TensorFlow finalizó el 7 de septiembre
de 2018. Consulta las versiones compatibles actuales en la [ política de
control de versiones de Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=es_419) .

##  24 de julio de 2018

**CHANGED:**

Estamos encantados de anunciar el precio promocional de Cloud TPU, lo que se
traduce en importantes reducciones de precios. En la siguiente tabla, se
muestran los precios anteriores y los precios nuevos disponibles a partir de
hoy:

###  EE.UU.

|  Precio anterior por TPU por hora  |  Precio nuevo por TPU por hora  
---|---|---  
Cloud TPU  |  $6.50 USD  |  $4.50 USD  
TPU interrumpible  |  $1.95 USD  |  $1.35 USD  
  
###  Europa

|  Precio anterior por TPU por hora  |  Precio nuevo por TPU por hora  
---|---|---  
Cloud TPU  |  $7.15 USD  |  $4.95 USD  
TPU interrumpible  |  $2.15 USD  |  $1,485 USD  
  
###  Asia-Pacífico

|  Precio anterior por TPU por hora  |  Precio nuevo por TPU por hora  
---|---|---  
Cloud TPU  |  $7.54 USD  |  $5.22 USD  
TPU interrumpible  |  $2.26 USD  |  $1,566 USD  
  
Consulta la [ guía de precios
](https://cloud.google.com/tpu/docs/pricing?hl=es_419) para obtener más
detalles.

##  12 de julio de 2018

**FEATURE:**

Cloud TPU ahora está disponible en Google Kubernetes Engine como una
característica Beta. Ejecuta la carga de trabajo de aprendizaje automático en
un clúster de Kubernetes en GCP y deja que GKE administre y escale los
recursos de Cloud TPU por ti.

  * Sigue los pasos del [ instructivo ](https://cloud.google.com/tpu/docs/tutorials/kubernetes-engine-resnet?hl=es_419) para entrenar el modelo Tensorflow ResNet-50 en Cloud TPU y GKE. 
  * Consulta la [ guía de configuración de GKE ](https://cloud.google.com/tpu/docs/kubernetes-engine-setup?hl=es_419) para obtener instrucciones rápidas sobre cómo ejecutar Cloud TPU con GKE. 

##  2 de julio de 2018

**CHANGED:**

Cloud TPU ahora es compatible con la [ versión 1.9 de TensorFlow
](https://www.tensorflow.org/versions/r1.9/api_docs/?hl=es_419) . TensorFlow
1.9 proporciona aumentos en el rendimiento de Cloud TPU, así como API
mejoradas, mensajes de error y confiabilidad.

##  27 de junio de 2018

**FEATURE:**

Cloud TPU ahora tiene disponibilidad general. Las revolucionarias TPU de
Google están diseñadas para acelerar las cargas de trabajo de aprendizaje
automático con TensorFlow. Cada Cloud TPU proporciona hasta 180 teraflops de
rendimiento, es decir, la capacidad de procesamiento necesaria para entrenar y
ejecutar modelos de aprendizaje automático de vanguardia.

  * Sigue la [ guía de inicio rápido ](https://cloud.google.com/tpu/docs/quickstart?hl=es_419) para configurar la Cloud TPU. 
  * Elige un [ instructivo ](https://cloud.google.com/tpu/docs/tutorials?hl=es_419) para ejecutar un modelo específico en tu Cloud TPU. 

##  18 de junio de 2018

**FEATURE:**

Las TPU interrumpibles ahora están disponibles en _versión Beta_ . Una TPU
interrumpible es un nodo de Cloud TPU que puedes crear y ejecutar a un precio
mucho más bajo que los nodos normales. Sin embargo, Cloud TPU puede cancelar
(interrumpir) estos nodos si requiere acceso a los recursos para otro
propósito.

  * Consulta cómo [ usar una TPU interrumpible ](https://cloud.google.com/tpu/docs/preemptible?hl=es_419) . 
  * Revisa los [ precios ](https://cloud.google.com/tpu/docs/pricing?hl=es_419) de los nodos interrumpibles y normales de Cloud TPU. 

**CHANGED:**

Cloud TPU ahora está disponible en las regiones de Europa (UE) y Asia-Pacífico
(APAC), así como en los Estados Unidos (EE.UU.). Consulta los [ detalles de
precios ](https://cloud.google.com/tpu/docs/pricing?hl=es_419) por región. Las
zonas siguientes están disponibles:

  * **EE.UU.**
    * ` us-central1-b `
    * ` us-central1-c `
    * ` us-central1-f ` (solo [ programa TFRC ](https://www.tensorflow.org/tfrc/?hl=es_419) ) 
  * **UE**
    * ` europe-west4-a `
  * **Asia-Pacífico**
    * ` asia-east1-c `

##  12 de junio de 2018

**CHANGED:**

La compatibilidad con la versión 1.6 de TensorFlow finalizó el 12 de junio de
2018. Consulta las versiones compatibles actuales en la [ política de control
de versiones de Cloud TPU ](https://cloud.google.com/tpu/docs/supported-
versions?hl=es_419) .

##  20 de abril de 2018

**CHANGED:**

Cloud TPU ahora es compatible con la [ versión 1.8 de TensorFlow
](https://www.tensorflow.org/versions/r1.8/api_docs/?hl=es_419) . TensorFlow
1.8 proporciona aumentos en el rendimiento de Cloud TPU, así como API
mejoradas, mensajes de error y confiabilidad.

La compatibilidad con la versión 1.7 de TensorFlow finaliza el 20 de junio de
2018. Consulta los detalles en la [ política de control de versiones de Cloud
TPU ](https://cloud.google.com/tpu/docs/supported-versions?hl=es_419) .

##  2 de abril de 2018

**CHANGED:**

Cloud TPU ahora es compatible con la [ versión 1.7 de TensorFlow
](https://www.tensorflow.org/versions/r1.7/api_docs/?hl=es_419) . La
compatibilidad con la versión 1.6 de TensorFlow finaliza el 2 de junio de
2018. Consulta los detalles en la [ política de control de versiones de Cloud
TPU ](https://cloud.google.com/tpu/docs/supported-versions?hl=es_419) .

##  12 de febrero de 2018

**FEATURE:**

Cloud TPU está disponible en versión Beta. Las revolucionarias TPU de Google
están diseñadas para acelerar las cargas de trabajo de aprendizaje automático
con TensorFlow. Cada Cloud TPU proporciona hasta 180 teraflops de rendimiento,
es decir, la capacidad de procesamiento necesaria para entrenar y ejecutar
modelos de aprendizaje automático de vanguardia.

  * Consulta cómo [ solicitar la cuota de TPU ](https://cloud.google.com/tpu/docs/quota?hl=es_419) . 
  * Sigue la [ guía de inicio rápido ](https://cloud.google.com/tpu/docs/quickstart?hl=es_419) para configurar la Cloud TPU. 
  * Elige un [ instructivo ](https://cloud.google.com/tpu/docs/tutorials?hl=es_419) para ejecutar un modelo específico en tu Cloud TPU. 

