#  Notas de la versión archivadas

Puedes ver las últimas actualizaciones de productos de todo Google Cloud en la
página [ Notas de la versión de Google Cloud
](https://cloud.google.com/release-notes?hl=es_419) .

El 10 de abril de 2019, Cloud Machine Learning Engine se convirtió en [ AI
Platform Training ](https://cloud.google.com/ai-platform/training?hl=es_419) y
[ AI Platform Prediction ](https://cloud.google.com/ai-
platform/prediction?hl=es_419) . En esta página, se documentan las
actualizaciones pasadas de Cloud ML Engine.

Para ver las notas de la versión actuales, consulta lo siguiente:

  * [ Notas de la versión de AI Platform Training ](https://cloud.google.com/ai-platform/training/docs/release-notes?hl=es_419)
  * [ Notas de la versión AI Platform Prediction ](https://cloud.google.com/ai-platform/prediction/docs/release-notes?hl=es_419)

##  1 de abril de 2019

**FEATURE:**

Cloud ML Engine ahora ofrece precios reducidos para el entrenamiento, la
predicción en línea y la predicción por lotes.

Obtén más información sobre los [ precios de Cloud ML Engine
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=es_419) .

##  28 de marzo de 2019

**FEATURE:**

Cloud ML Engine ahora ofrece un entrenamiento con algoritmos integrados.
Puedes enviar los datos para el procesamiento previo automático y entrenar un
modelo en el [ algoritmo de aprendizaje lineal
](https://www.tensorflow.org/tutorials/representation/linear?hl=es_419) de
TensorFlow, el [ algoritmo de amplitud y profundidad
](https://ai.googleblog.com/2016/06/wide-deep-learning-better-together-
with.html) de TensorFlow y los algoritmos [ XGBoost
](https://xgboost.readthedocs.io/en/latest/tutorials/model.html) sin escribir
ningún código.

Obtén más información sobre el [ entrenamiento con algoritmos integrados
](https://cloud.google.com/ai-platform/training/docs/algorithms?hl=es_419) .

##  25 de marzo de 2019

**CHANGED:**

La versión 1.13 del entorno de ejecución de Cloud ML Engine ahora es
compatible con TensorFlow 1.13.1. Consulta la [ lista de versiones del entorno
de ejecución ](https://cloud.google.com/ai-platform/training/docs/runtime-
version-list?hl=es_419) para obtener la lista completa de los paquetes
incluidos en la versión 1.13 del entorno de ejecución.

##  8 de marzo de 2019

**FEATURE:**

La compatibilidad del entrenamiento con TPU en la versión 1.9 del entorno de
ejecución de Cloud ML Engine finalizó el 8 de marzo de 2019. Consulta las
versiones admitidas en la actualidad en la [ lista de versiones del entorno de
ejecución ](https://cloud.google.com/ai-
platform/training/docs/tensorflow/runtime-version-list?hl=es_419#tpu-support)
.

##  6 de marzo de 2019

**FEATURE:**

La versión 1.13 del entorno de ejecución de Cloud ML Engine ya está disponible
para el entrenamiento y la predicción. Esta versión es compatible con
TensorFlow 1.13 y, además, incluye otros paquetes que se enumeran en la [
lista de versiones del entorno de ejecución ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=es_419) .

En la actualidad, el entrenamiento con TPU no es compatible con la versión
1.13 del entorno de ejecución.

##  1 de marzo de 2019

**FEATURE:**

[ AI Platform Notebooks ](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=es_419) ya está disponible en
versión Beta. AI Platform Notebooks te permite crear y administrar instancias
de máquinas virtuales (VM) que vienen empaquetadas de forma previa con [
JupyterLab
](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) y
un paquete de software de aprendizaje profundo.

Visita la [ descripción general de AI Platform Notebooks
](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=es_419) y la [ guía para crear
una instancia nueva de notebook ](https://cloud.google.com/ai-
platform/training/docs/notebooks/create-new?hl=es_419) a fin de obtener más
información.

##  13 de febrero de 2019

**FEATURE:**

Ahora Cloud TPU está disponible de manera general para el entrenamiento de
modelos de TensorFlow. Las unidades de procesamiento tensorial (TPU) son los
aceleradores de desarrollo personalizado de Google para las cargas de trabajo
de aprendizaje automático.

Consulta cómo [ usar las TPU para entrenar tus modelos
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=es_419) en
Cloud ML Engine y obtén más información sobre [ sus precios
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=es_419) .

##  7 de febrero de 2019

**FEATURE:**

El entrenamiento con contenedores personalizados ahora está disponible en
versión Beta. Esta función te permite ejecutar la aplicación de entrenamiento
en Cloud ML Engine mediante el uso de una imagen personalizada de Docker.
Puedes compilar el contenedor personalizado con los frameworks de AA que
elijas. Comienza a [ entrenar un modelo de PyTorch mediante contenedores
personalizados ](https://cloud.google.com/ai-platform/training/docs/custom-
containers-training?hl=es_419) .

**FEATURE:**

Ahora puedes configurar trabajos de entrenamiento con ciertos tipos de
máquinas de Compute Engine. Esto proporciona una flexibilidad adicional para
la asignación de recursos de procesamiento a los trabajos de entrenamiento.
Está función está disponible en versión Beta.

Cuando configuras el trabajo con los tipos de máquinas de Compute Engine,
puedes conectar un conjunto personalizado de GPU.

Obtén más información sobre los [ tipos de máquinas de Compute Engine
](https://cloud.google.com/ai-platform/training/docs/machine-
types?hl=es_419#compute-engine-machine-types) , las [ GPU conectadas
](https://cloud.google.com/ml-engine/docs/tensorflow/using-
gpus?hl=es_419#compute-engine-machine-types-with-gpu) y [ los precios
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=es_419) .

**FEATURE:**

Las GPU P4 ahora están en versión Beta para el entrenamiento. Para obtener más
información, consulta las guías sobre [ el uso de GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=es_419) , [
su disponibilidad regional ](https://cloud.google.com/ml-
engine/docs/tensorflow/regions?hl=es_419#training_with_accelerators) y [ los
precios ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=es_419) .

##  1 de febrero de 2019

**CHANGED:**

Las CPU de cuatro núcleos ahora están disponibles en versión Beta para la
predicción en línea. Se cambian los nombres de los tipos de máquinas y se
actualiza el precio.

  * Configura ` machineType ` como [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=es_419) a fin de especificar el tipo de máquina que se usará para la entrega. Usa ` mls1-c4-m2 ` para las CPU de cuatro núcleos. La opción de configuración predeterminada es la CPU de un núcleo, ` mls1-c1-m2 ` . 
  * Los siguientes nombres de máquinas usados en la versión Alfa están **obsoletos** : ` mls1-highmem-1 ` y ` mls1-highcpu-4 ` . 
  * Para obtener más información, consulta la guía sobre la [ predicción en línea ](https://cloud.google.com/ai-platform/training/docs/online-predict?hl=es_419#machine-types) . 
  * Consulta los [ precios ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=es_419) actualizados para la entrega de tipos de máquinas. 

##  25 de enero de 2019

**FEATURE:**

La predicción en línea ya está disponible en la región us-east4. Consulta la
guía sobre la [ disponibilidad de las regiones ](https://cloud.google.com/ai-
platform/training/docs/regions?hl=es_419) .

##  10 de enero de 2019

**FEATURE:**

Las GPU V100 ahora están disponibles de forma general para el entrenamiento.
Para obtener más información, consulta las guías sobre [ el uso de GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=es_419) y [
los precios ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=es_419) .

##  19 de diciembre de 2018

**FEATURE:**

Las versiones 1.11 y 1.12 del entorno de ejecución de Cloud ML Engine ahora
están disponibles para el entrenamiento y la predicción. Estas versiones son
compatibles con TensorFlow 1.11 y 1.12 respectivamente, y con otros paquetes
que se enumeran en la [ lista de versiones del entorno de ejecución
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=es_419) .

Se agregó la compatibilidad con el entrenamiento de TPU a las versiones 1.11 y
1.12 del entorno de ejecución de Cloud ML Engine. La versión 1.10 no es
compatible. Consulta las versiones admitidas en la actualidad en la [ lista de
versiones del entorno de ejecución ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=es_419#tpu-support) .

**CHANGED:**

Cada versión del entorno de ejecución de Cloud ML Engine ahora incluye [
joblib ](https://joblib.readthedocs.io/en/latest/) . La primera versión del
entorno de ejecución que incluye joblib es la versión 1.4.

##  26 de octubre de 2018

**CHANGED:**

La compatibilidad con el entrenamiento de TPU para la versión 1.8 del entorno
de ejecución de Cloud ML finalizó el 26 de octubre de 2018. Consulta las
versiones admitidas en la actualidad en la [ lista de versiones del entorno de
ejecución ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-
version-list?hl=es_419#tpu-support) .

##  11 de octubre de 2018

**ISSUE:**

La versión 1.11 del entorno de ejecución de Cloud ML Engine se revierte debido
a [ errores causados por una incompatibilidad de las versiones de CuDNN
](https://stackoverflow.com/q/52733440) durante el entrenamiento de GPU. La
solución alternativa actual es usar la versión 1.10 del entorno de ejecución.
Para obtener más detalles, consulta la [ lista de versiones del entorno de
ejecución ](https://cloud.google.com/ai-platform/training/docs/runtime-
version-list?hl=es_419) .

##  5 de octubre de 2018

**FEATURE:**

La versión 1.11 del entorno de ejecución de Cloud ML Engine ya está disponible
para el entrenamiento y la predicción. Esta versión es compatible con
TensorFlow 1.11 y con otros paquetes que se enumeran en la [ lista de
versiones del entorno de ejecución ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=es_419) .

##  31 de agosto de 2018

**FEATURE:**

La versión 1.10 del entorno de ejecución de Cloud ML Engine ya está disponible
para el entrenamiento y la predicción. Esta versión es compatible con
TensorFlow 1.10 y con otros paquetes que se enumeran en la [ lista de
versiones del entorno de ejecución ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=es_419) .

##  27 de agosto de 2018

**FEATURE:**

Las GPU V100 ya están en versión Beta para entrenamiento. El uso de las GPU
V100 ahora genera cargos. Para obtener más información, consulta las guías
sobre [ el uso de GPU ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=es_419) y [ los precios
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=es_419) .

**FEATURE:**

Las GPU P100 ahora están disponibles para el entrenamiento. Para obtener más
información, consulta las guías sobre [ el uso de GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=es_419) y [
los precios ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=es_419) .

**FEATURE:**

Ahora están disponibles dos nuevas regiones para el entrenamiento: us-west1 y
europe-west4. Consulta la página de las [ regiones
](https://cloud.google.com/ai-platform/training/docs/regions?hl=es_419) para
obtener más información.

##  24 de agosto de 2018

**CHANGED:**

La compatibilidad con el entrenamiento de TPU para la versión 1.7 del entorno
de ejecución de Cloud ML finalizó el 24 de agosto de 2018. Consulta las
versiones admitidas en la actualidad en la [ lista de versiones del entorno de
ejecución ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-
version-list?hl=es_419#tpu-support) .

##  9 de agosto de 2018

**CHANGED:**

Estamos encantados de anunciar reducciones de precio significativas para la
predicción en línea con AI Platform Training.

En la siguiente tabla, se muestran los precios anteriores y los nuevos:

Región  |  Precio anterior por nodo, por hora  |  Precio nuevo por nodo, por
hora  
---|---|---  
EE.UU.  |  $0.30  |  $0.056  
Europa  |  $0.348  |  $0.061  
Asia-Pacífico  |  $0.348  |  $0.071  
  
Consulta la [ guía de precios ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=es_419) para obtener más detalles.

##  8 de agosto de 2018

**CHANGED:**

Estamos encantados de anunciar precios de promoción para Cloud TPU con AI
Platform Training, lo que supone una reducción significativa de los precios.

En la siguiente tabla, se muestran los precios anteriores y los nuevos:

Región: EE.UU.  |  Precio anterior por TPU por hora  |  Precio nuevo por TPU
por hora  
---|---|---  
Nivel de escala: ` BASIC_TPU ` _(versión Beta)_ |  $9.7674  |  $6.8474  
Tipo personalizado de máquina: ` cloud_tpu ` _(versión Beta)_ |  $9.4900  |
$6.5700  
  
Ten en cuenta que en la tabla solo se muestran los precios de la región de
EE.UU. La disponibilidad de Cloud TPU en Cloud ML Engine no presenta cambios.
Consulta la [ guía de precios ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=es_419) para obtener más detalles.

##  6 de agosto de 2018

**FEATURE:**

La versión 1.9 del entorno de ejecución de Cloud ML Engine ya está disponible
para el entrenamiento y la predicción. Esta versión es compatible con
TensorFlow 1.9 y con otros paquetes que se enumeran en la [ lista de versiones
del entorno de ejecución ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=es_419) .

##  23 de julio de 2018

**FEATURE:**

Cloud ML Engine ahora es compatible con **scikit-learn** y **XGBoost** para el
entrenamiento. Esta función está disponible de forma general. Consulta la guía
sobre el [ entrenamiento con scikit-learn y XGBoost en Cloud ML Engine
](https://cloud.google.com/ml-engine/docs/scikit/getting-started-
training?hl=es_419) .

**FEATURE:**

La compatibilidad con la predicción en línea para **scikit-learn** y
**XGBoost** ahora está disponible de forma general.

  * Cuando crees una versión del modelo, configura ` framework ` como [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=es_419) para especificar el framework de aprendizaje automático. Los valores válidos son ` TENSORFLOW ` , ` SCIKIT_LEARN ` y ` XGBOOST ` . El valor predeterminado es ` TENSORFLOW ` . Si especificas ` SCIKIT_LEARN ` o ` XGBOOST ` , también debes configurar ` runtimeVersion ` como 1.4 o superior para la versión del modelo. 
  * Consulta la guía sobre [ el entrenamiento local y las predicciones en línea con scikit-learn y XGBoost ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=es_419) . 

##  12 de julio de 2018

**FEATURE:**

Puedes agregar etiquetas a los recursos de AI Platform Training: [ trabajos
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=es_419) , [ modelos
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models?hl=es_419) y [
versiones de modelos ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=es_419) ,
y usarlas para organizar los recursos en categorías. Las etiquetas también
están disponibles en las [ operaciones ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.operations?hl=es_419) . En
este caso, las etiquetas se derivan del recurso en el que se aplica la
operación. Obtén más información sobre [ el agregado y el uso de etiquetas
](https://cloud.google.com/ml-engine/docs/tensorflow/resource-
labels?hl=es_419) .

##  26 de junio de 2018

**CHANGED:**

Las siguientes regiones adicionales ya están disponibles por completo:

  * us-east1 
  * asia-northeast1 

Obtén más detalles sobre la [ disponibilidad de las regiones
](https://cloud.google.com/ai-platform/training/docs/regions?hl=es_419) .

##  13 de junio de 2018

**CHANGED:**

La compatibilidad con el entrenamiento de TPU para la versión 1.6 del entorno
de ejecución de Cloud ML finalizó el 13 de junio de 2018. Consulta las
versiones admitidas en la actualidad en la [ lista de versiones del entorno de
ejecución ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-
version-list?hl=es_419#tpu-support) .

##  29 de mayo de 2018

**CHANGED:**

Ahora puedes usar Cloud TPU ( _versión Beta_ ) con TensorFlow 1.8 y con la
versión 1.8 del entorno de ejecución de Cloud ML Engine.

_Información general:_ Cloud TPU está disponible en Cloud ML Engine desde el
14 de mayo en las versiones 1.6 y 1.7 del entorno de ejecución. La semana
pasada se lanzó la versión 1.8 del entorno de ejecución, pero en ese momento
Cloud TPU aún no estaba disponible para TensorFlow 1.8. Ahora lo está.
Consulta cómo [ usar las TPU para entrenar tus modelos
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=es_419) en
Cloud ML Engine.

##  16 de mayo de 2018

**FEATURE:**

La versión 1.8 del entorno de ejecución de Cloud ML Engine ya está disponible
para el entrenamiento y la predicción. Esta versión es compatible con
TensorFlow 1.8 y con otros paquetes que se enumeran en la [ lista de versiones
del entorno de ejecución ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=es_419) .

##  15 de mayo de 2018

**FEATURE:**

Ahora puedes actualizar la cantidad mínima de nodos para el [ ajuste de escala
automático ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=es_419#autoscaling)
en una versión del modelo existente. También puedes especificar el atributo
cuando creas una versión nueva.

##  14 de mayo de 2018

**FEATURE:**

Cloud ML Engine ahora ofrece Cloud TPU _(versión Beta)_ para el entrenamiento
de modelos de TensorFlow. Las unidades de procesamiento tensorial (TPU) son
los ASIC de Google desarrollados de manera personalizada que se usan para
acelerar las cargas de trabajo de aprendizaje automático. Consulta cómo [ usar
TPU para entrenar los modelos ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-tpus?hl=es_419) en Cloud ML Engine.

##  26 de abril de 2018

**FEATURE:**

La versión 1.7 del entorno de ejecución de Cloud ML Engine ya está disponible
para el entrenamiento y la predicción. Esta versión es compatible con
TensorFlow 1.7 y con otros paquetes que se enumeran en la [ lista de versiones
del entorno de ejecución ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=es_419) .

##  16 de abril de 2018

**FEATURE:**

**Algoritmos de los hiperparámetros:** Ahora, cuando ajustas los
hiperparámetros en el trabajo de entrenamiento, puedes especificar un
algoritmo de búsqueda en [ HyperparameterSpec ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=es_419#hyperparameterspec)
. Los valores disponibles son estos:

  * ` GRID_SEARCH ` : Es una búsqueda por cuadrícula simple dentro del espacio posible. Esta opción es particularmente útil si deseas especificar un número de pruebas que sea mayor que el número de puntos en el espacio posible. En tales casos, si no especificas una búsqueda por cuadrícula, el algoritmo predeterminado de Cloud ML Engine podría generar sugerencias duplicadas. Para usar la búsqueda por cuadrícula, todos los parámetros deben ser del tipo ` INTEGER ` , ` CATEGORICAL ` o ` DISCRETE ` . 
  * ` RANDOM_SEARCH ` : Es una búsqueda aleatoria simple dentro del espacio posible. 

Si no especificas un algoritmo, tu trabajo usa el algoritmo predeterminado de
Cloud ML Engine, que impulsa la búsqueda de parámetros para llegar a la
solución óptima con una búsqueda más efectiva en el espacio de los parámetros.
Para obtener más información sobre el ajuste de hiperparámetros, consulta la [
descripción general del ajuste de hiperparámetros
](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-tuning-
overview?hl=es_419) .

##  5 de abril de 2018

**FEATURE:**

Cloud ML Engine ahora es compatible con **scikit-learn** y **XGBoost** para la
predicción en línea. Esta función está en versión _Beta_ .

  * Cuando crees una versión del modelo, configura ` framework ` como [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=es_419) para especificar el framework de aprendizaje automático. Los valores válidos son ` TENSORFLOW ` , ` SCIKIT_LEARN ` y ` XGBOOST ` . El valor predeterminado es ` TENSORFLOW ` . Si especificas ` SCIKIT_LEARN ` o ` XGBOOST ` , también debes configurar ` runtimeVersion ` como 1.4 o superior para la versión del modelo. 
  * Consulta la guía sobre [ scikit-learn y XGBoost en Cloud ML Engine ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=es_419) . 

**FEATURE:**

Python 3.5 está disponible para la predicción en línea.

  * Cuando crees una versión del modelo, configura ` pythonVersion ` como [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=es_419) para especificar la versión de Python. La opción predeterminada es Python 2.7. 
  * Para obtener más información sobre todos los paquetes disponibles en Cloud ML Engine, consulta la [ lista de versiones del entorno de ejecución ](https://cloud.google.com/ml-engine/docs/scikit/runtime-version-list?hl=es_419) . 

##  20 de marzo de 2018

**FEATURE:**

La versión 1.6 del entorno de ejecución de Cloud ML Engine ya está disponible
para el entrenamiento y la predicción. Esta versión es compatible con
TensorFlow 1.6 y con otros paquetes que se enumeran en la [ lista de versiones
del entorno de ejecución ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=es_419) .

##  13 de marzo de 2018

**FEATURE:**

La versión del entorno de ejecución de Cloud ML Engine para TensorFlow 1.5 ya
está disponible a fin de realizar el entrenamiento y la predicción. Para
obtener más información, consulta la [ lista de versiones del entorno de
ejecución ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-
version-list?hl=es_419) .

##  8 de febrero de 2018

**FEATURE:**

Se agregaron características nuevas para el ajuste de hiperparámetros: la
interrupción anticipada y automatizada de las pruebas, la reanudación de un
trabajo previo de ajuste de hiperparámetros y las optimizaciones adicionales
de la eficiencia cuando ejecutas trabajos similares. Para obtener más
información, consulta la [ descripción general del ajuste de hiperparámetros
](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-tuning-
overview?hl=es_419) .

##  14 de diciembre de 2017

**FEATURE:**

La versión del entorno de ejecución de Cloud ML Engine para TensorFlow 1.4 ya
está disponible a fin de realizar el entrenamiento y la predicción. Para
obtener más información, consulta la [ lista de versiones del entorno de
ejecución ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-
version-list?hl=es_419) .

**FEATURE:**

Python 3 ahora está disponible a fin de realizar el entrenamiento como parte
de la versión del entorno de ejecución de Cloud ML Engine para TensorFlow 1.4.
Para obtener más información, consulta la [ lista de versiones del entorno de
ejecución ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-
version-list?hl=es_419) .

**FEATURE:**

La predicción en línea ahora está disponible de forma general para la entrega
de un solo núcleo. Consulta la guía sobre la [ predicción en línea
](https://cloud.google.com/ml-engine/docs/tensorflow/online-predict?hl=es_419)
y la [ entrada de blog ](https://cloud.google.com/blog/big-
data/2017/12/bringing-cloud-ml-engine-to-more-developers-with-online-
prediction-features-and-reduced-prices?hl=es_419) .

**FEATURE:**

Se redujeron y simplificaron los precios de entrenamiento y predicción.
Consulta los [ detalles de los precios ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=es_419) , la [ entrada de blog
](https://cloud.google.com/blog/big-data/2017/12/bringing-cloud-ml-engine-to-
more-developers-with-online-prediction-features-and-reduced-prices?hl=es_419)
y la comparación de precios antiguos y actuales en las [ Preguntas frecuentes
sobre los precios ](https://cloud.google.com/ml-
engine/docs/tensorflow/pricing-faq?hl=es_419) .

**FEATURE:**

Las GPU P100 ya están en versión Beta. El uso de las GPU P100 ahora genera
cargos. Para obtener más información, consulta [ Uso de GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=es_419) y [
Precios ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=es_419) .

##  26 de octubre de 2017

**FEATURE:**

El registro de auditoría para Cloud ML Engine ahora se encuentra en versión
Beta. Para obtener más información, consulta [ Visualiza los registros de
auditoría ](https://cloud.google.com/ml-engine/docs/tensorflow/audit-
logs?hl=es_419) .

##  25 de septiembre de 2017

**FEATURE:**

Las funciones de IAM predefinidas de Cloud ML Engine están disponibles para su
uso general. Para obtener más información, consulta [ Control de acceso
](https://cloud.google.com/ml-engine/docs/tensorflow/access-control?hl=es_419)
.

##  27 de junio de 2017

**FEATURE:**

La versión del entorno de ejecución de Cloud ML Engine para TensorFlow 1.2
ahora está disponible a fin de realizar el entrenamiento y la predicción. Para
obtener más información, consulta la [ lista de versiones del entorno de
ejecución ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-
version-list?hl=es_419) .

**DEPRECATED:**

Las versiones anteriores del entorno de ejecución con TensorFlow 0.11 y 0.12
ya no son compatibles con Cloud ML Engine. Si quieres obtener más información,
consulta la [ lista de versiones del entorno de ejecución
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=es_419) y los [ cronogramas de compatibilidad para versiones
anteriores del entorno de ejecución ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=es_419#runtime-version-support)
.

##  9 de mayo de 2017

**FEATURE:**

Se anunció la disponibilidad general de las máquinas habilitadas para GPU. Si
quieres obtener más información, consulta [ Usa GPU para modelos de
entrenamiento en la nube ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=es_419) .

##  27 de abril de 2017

**FEATURE:**

Las GPU ya están disponibles en la región us-central1. Si quieres obtener la
lista completa de regiones que admiten las GPU, consulta [ Usa GPU para
modelos de entrenamiento en la nube ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=es_419#requesting_gpu-enabled_machines) .

##  v1 (8 de marzo de 2017)

**FEATURE:**

Se anunció la disponibilidad general de la AI Platform Training. La versión 1
de Cloud ML Engine está disponible para uso general a fin de entrenar modelos,
implementarlos y generar predicciones por lotes. La función de [ ajuste de
hiperparámetros ](https://cloud.google.com/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview?hl=es_419) también está
disponible para su uso general, pero la predicción en línea y las [ máquinas
habilitadas para GPU ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=es_419) permanecen en versión Beta.

**FEATURE:**

La predicción en línea ahora se encuentra en la [ etapa de lanzamiento
](https://cloud.google.com/terms/launch-stages?hl=es_419) en versión Beta. Su
uso ahora está sujeto a la [ política de precios
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=es_419) de
Cloud ML Engine y sigue la misma fórmula de precios que la predicción por
lotes. Si bien permanece en versión Beta, la predicción en línea no está
diseñada para su uso en aplicaciones críticas.

**CHANGED:**

Los entornos que Cloud ML Engine usa para el entrenamiento de modelos y la
obtención de predicciones se definieron como [ versiones del entorno de
ejecución ](https://cloud.google.com/ml-
engine/docs/tensorflow/versioning?hl=es_419) de Cloud ML Engine. Puedes
especificar una versión compatible del entorno de ejecución para que se use
durante el entrenamiento, la definición de un recurso del modelo o la
solicitud de predicciones por lotes. En este momento, la diferencia principal
entre las versiones del entorno de ejecución es la versión de TensorFlow que
admite cada una de ellas, pero pueden surgir más diferencias con el tiempo.
Puedes encontrar los detalles en la [ lista de versiones del entorno de
ejecución ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-
version-list?hl=es_419) .

**CHANGED:**

Ahora puedes ejecutar trabajos de predicción por lotes en modelos guardados de
TensorFlow que se almacenan en Google Cloud Storage y que no están alojados
como una versión del modelo en Cloud ML Engine. En lugar de proporcionar un ID
de la versión o del modelo cuando creas el trabajo, puedes usar el URI del
modelo guardado.

**DEPRECATED:**

El SDK de aprendizaje automático de Google Cloud, lanzado con anterioridad en
versión Alfa, se volvió obsoleto y ya no será compatible a partir del 7 de
mayo de 2017. La mayor parte de la funcionalidad que expuso el SDK se trasladó
al paquete nuevo de TensorFlow, [ tf.Transform
](https://github.com/tensorflow/transform) . Puedes usar cualquier tecnología
o herramienta que desees para realizar un procesamiento previo de los datos de
entrada. Sin embargo, recomendamos ` tf.Transform ` y los servicios
disponibles en Google Cloud Platform, incluidos Google Cloud Dataflow, Google
Cloud Dataproc y Google BigQuery.

##  v1beta1 (29 de septiembre de 2016)

**FEATURE:**

La predicción en línea es una función en versión Alfa. Si bien AI Platform
Training se encuentra, en general, en su fase Beta, todavía se están haciendo
cambios significativos a la predicción en línea para mejorar el rendimiento.
No se te [ cobrará ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=es_419) por la predicción en línea mientras
permanezca en versión Alfa.

**FEATURE:**

El procesamiento previo y el resto del SDK de Cloud ML Engine son funciones
Alfa. El SDK se encuentra en desarrollo activo para mejorar la integración de
Cloud ML Engine con Apache Beam.

