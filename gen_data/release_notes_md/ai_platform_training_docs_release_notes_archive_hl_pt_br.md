#  Notas da versão arquivadas

É possível ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas da versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt_br) .

Em 10 de abril de 2019, o Cloud Machine Learning Engine passou a ser [ AI
Platform Training ](https://cloud.google.com/ai-platform/training?hl=pt_br) e
[ AI Platform Prediction ](https://cloud.google.com/ai-
platform/prediction?hl=pt_br) . Nesta página, você verá registros das
atualizações históricas do Cloud ML Engine.

Veja as notas da versão atuais:

  * [ Notas da versão do AI Platform Training ](https://cloud.google.com/ai-platform/training/docs/release-notes?hl=pt_br)
  * [ Notas da versão do AI Platform Prediction ](https://cloud.google.com/ai-platform/prediction/docs/release-notes?hl=pt_br)

##  1º de abril de 2019

**FEATURE:**

O Cloud ML Engine agora oferece preços reduzidos para treinamento, previsão
on-line e previsão em lote.

Saiba mais sobre os [ preços do Cloud ML Engine ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=pt_br) .

##  28 de março de 2019

**FEATURE:**

O Cloud ML Engine agora oferece treinamento com algoritmos integrados. É
possível enviar dados para pré-processamento automático e treinar um modelo
nos algoritmos [ aprendizagem linear
](https://www.tensorflow.org/tutorials/representation/linear?hl=pt_br) do
TensorFlow, [ amplitude e profundidade
](https://ai.googleblog.com/2016/06/wide-deep-learning-better-together-
with.html) do TensorFlow e [ XGBoost
](https://xgboost.readthedocs.io/en/latest/tutorials/model.html) (links em
inglês) sem escrever nenhum código.

Saiba mais sobre o [ treinamento com algoritmos integrados
](https://cloud.google.com/ai-platform/training/docs/algorithms?hl=pt_br) .

##  25 de março de 2019

**CHANGED:**

A versão 1.13 do ambiente de execução do Cloud ML Engine agora é compatível
com o TensorFlow 1.13.1. Consulte a [ Lista de versões do ambiente de execução
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=pt_br) para ver todos os pacotes incluídos na versão 1.13.

##  8 de março de 2019

**FEATURE:**

A compatibilidade com o treinamento com TPUs no ambiente de execução do Cloud
ML Engine versão 1.9 terminou em 8 de março de 2019. Veja as versões
atualmente compatíveis na [ Lista de versões do ambiente de execução
](https://cloud.google.com/ai-platform/training/docs/tensorflow/runtime-
version-list?hl=pt_br#tpu-support) .

##  6 de março de 2019

**FEATURE:**

O ambiente de execução do Cloud ML Engine versão 1.13 já está disponível para
treinamento e previsão. Essa versão é compatível com o TensorFlow 1.13 e
inclui outros pacotes, que constam da [ Lista de versões do ambiente de
execução ](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=pt_br) .

O treinamento com TPUs ainda não é compatível com a versão 1.13 do ambiente de
execução.

##  1º de março de 2019

**FEATURE:**

O [ AI Platform Notebooks ](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=pt_br) agora está disponível na
versão Beta. Com o AI Platform Notebooks, você cria e gerencia instâncias de
máquina virtual (VM, na sigla em inglês) pré-empacotadas [ com o JupyterLab
](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)
(em inglês) e um conjunto de software de aprendizado profundo.

Para saber mais, acesse a [ visão geral do AI Platform Notebooks
](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=pt_br) e o [ guia para criar uma
nova instância de notebook ](https://cloud.google.com/ai-
platform/training/docs/notebooks/create-new?hl=pt_br) .

##  13 de fevereiro de 2019

**FEATURE:**

O Cloud TPU já está disponível para o treinamento de modelos do TensorFlow. As
unidades de processamento de tensor (TPUs, na sigla em inglês) são
aceleradores personalizados do Google para cargas de trabalho de machine
learning.

Veja como [ usar TPUs para treinar modelos ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-tpus?hl=pt_br) no Cloud ML Engine e [ conheça os
preços ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=pt_br)
.

##  7 de fevereiro de 2019

**FEATURE:**

O treinamento com contêineres personalizados já está disponível na versão
Beta. Esse recurso permite que você execute seu aplicativo de treinamento no
Cloud ML Engine usando uma imagem do Docker personalizada. Crie seu contêiner
personalizado com os frameworks de ML de sua escolha. Comece a [ treinar um
modelo PyTorch usando contêineres personalizados
](https://cloud.google.com/ai-platform/training/docs/custom-containers-
training?hl=pt_br) .

**FEATURE:**

Já é possível configurar jobs de treinamento com determinados tipos de máquina
do Compute Engine. Isso proporciona flexibilidade adicional para alocar
recursos computacionais aos jobs de treinamento. Esse recurso está disponível
na versão Beta.

Ao configurar o job com tipos de máquina do Compute Engine, é possível anexar
um conjunto personalizado de GPUs.

Leia mais sobre os [ tipos de máquina do Compute Engine
](https://cloud.google.com/ai-platform/training/docs/machine-
types?hl=pt_br#compute-engine-machine-types) , os [ anexos de GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-
gpus?hl=pt_br#compute-engine-machine-types-with-gpu) e [ respectivos preços
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=pt_br) .

**FEATURE:**

As GPUs P4 estão em fase Beta para treinamento. Para mais informações,
consulte os guias sobre [ como usar GPUs ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=pt_br) , [ disponibilidade por região
](https://cloud.google.com/ml-
engine/docs/tensorflow/regions?hl=pt_br#training_with_accelerators) e [ preços
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=pt_br) .

##  1º de fevereiro de 2019

**CHANGED:**

As CPUs com processador quad-core estão disponíveis em fase Beta para predição
on-line. Os nomes dos tipos de máquina foram alterados e os preços foram
atualizados.

  * Defina ` machineType ` em [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=pt_br) para especificar o tipo de máquina a ser usado para veiculação. Use ` mls1-c4-m2 ` para CPUs quad-core. O padrão é a CPU de um núcleo, ` mls1-c1-m2 ` . 
  * O uso dos seguintes nomes de máquina usados na versão Alfa está **suspenso** : ` mls1-highmem-1 ` e ` mls1-highcpu-4 ` . 
  * Para mais informações, consulte o guia de [ previsão on-line ](https://cloud.google.com/ai-platform/training/docs/online-predict?hl=pt_br#machine-types) . 
  * Consulte os [ preços atualizados ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=pt_br) dos tipos de máquina para veiculação. 

##  25 de janeiro de 2019

**FEATURE:**

A previsão on-line já está disponível na região us-east4. Veja o guia sobre [
disponibilidade por região ](https://cloud.google.com/ai-
platform/training/docs/regions?hl=pt_br) .

##  10 de janeiro de 2019

**FEATURE:**

As GPUs V100 já estão disponíveis para treinamento. Para mais informações,
consulte os guias sobre [ como usar GPUs ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=pt_br) e [ preços
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=pt_br) .

##  19 de dezembro de 2018

**FEATURE:**

As versões de ambiente de execução 1.11 e 1.12 do Cloud ML Engine já estão
disponíveis para treinamento e previsão. Essas versões são compatíveis com o
TensorFlow 1.11 e 1.12 e outros pacotes, conforme consta da [ Lista de versões
do ambiente de execução ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=pt_br) .

Agora as versões 1.11 e 1.12 do ambiente de execução do Cloud ML Engine são
compatíveis com o treinamento de TPUs, mas não a versão 1.10. Veja as versões
atualmente compatíveis na [ Lista de versões do ambiente de execução
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=pt_br#tpu-support) .

**CHANGED:**

Cada versão do ambiente de execução do Cloud ML Engine [ agora inclui o joblib
](https://joblib.readthedocs.io/en/latest/) (em inglês). A versão de ambiente
de execução mais antiga que inclui o joblib é a versão 1.4.

##  26 de outubro de 2018

**CHANGED:**

A compatibilidade com o treinamento de TPU na versão 1.8 do ambiente de
execução do Cloud ML terminou em 26 de outubro de 2018. Veja as versões
atualmente compatíveis na [ Lista de versões do ambiente de execução
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=pt_br#tpu-support) .

##  11 de outubro de 2018

**ISSUE:**

A versão 1.11 do ambiente de execução do Cloud ML Engine foi revertida devido
a [ erros causados por uma incompatibilidade de versão do CuDNN
](https://stackoverflow.com/q/52733440) (em inglês) durante o treinamento de
GPU. A alternativa atual é usar a versão 1.10 do ambiente de execução. Para
mais detalhes, consulte a [ Lista de versões do ambiente de execução
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=pt_br) .

##  5 de outubro de 2018

**FEATURE:**

A versão 1.11 do ambiente de execução do Cloud ML Engine já está disponível
para treinamento e previsão. Essa versão é compatível com o TensorFlow 1.11 e
outros pacotes, conforme descrito na [ Lista de versões do ambiente de
execução ](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=pt_br) .

##  31 de agosto de 2018

**FEATURE:**

A versão 1.10 do ambiente de execução do Cloud ML Engine já está disponível
para treinamento e previsão. Essa versão é compatível com o TensorFlow 1.10 e
outros pacotes, conforme descrito na [ Lista de versões do ambiente de
execução ](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=pt_br) .

##  27 de agosto de 2018

**FEATURE:**

As GPUs V100 estão agora em fase Beta para treinamento. O uso delas passará a
gerar cobranças. Para mais informações, consulte os guias sobre [ como usar
GPUs ](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=pt_br)
e [ preços ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=pt_br) .

**FEATURE:**

Atualmente, as GPUs P100 estão disponíveis para treinamento. Para mais
informações, consulte os guias sobre [ como usar GPUs
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=pt_br) e [
preços ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=pt_br)
.

**FEATURE:**

Duas regiões novas, us-west1 e europe-west4, estão disponíveis para
treinamento. Veja mais informações na [ página de regiões
](https://cloud.google.com/ai-platform/training/docs/regions?hl=pt_br) .

##  24 de agosto de 2018

**CHANGED:**

A compatibilidade com treinamento de TPU na versão 1.7 do ambiente de execução
do Cloud ML terminou em 24 de agosto de 2018. Veja as versões atualmente
compatíveis na [ Lista de versões do ambiente de execução
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=pt_br#tpu-support) .

##  9 de agosto de 2018

**CHANGED:**

Temos a satisfação de anunciar reduções significativas de preços para previsão
on-line com o AI Platform Training.

Na tabela a seguir, veja os preços anteriores e os novos:

Região  |  Preço anterior por nó/hora  |  Preço novo por nó/hora  
---|---|---  
EUA  |  USD 0,30  |  USD 0,056  
Europa  |  USD 0,348  |  USD 0,061  
Ásia-Pacífico  |  USD 0,348  |  USD 0,071  
  
Veja mais detalhes no [ guia de preços ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=pt_br) .

##  8 de agosto de 2018

**CHANGED:**

Temos a satisfação de anunciar o preço promocional da Cloud TPU com o AI
Platform Training, com significativas reduções de preço.

Na tabela a seguir, veja os preços anteriores e os novos:

Região: EUA  |  Preço anterior por TPU/hora  |  Preço novo por TPU/hora  
---|---|---  
Nível de escalonamento: ` BASIC_TPU ` _(Beta)_ |  USD 9,7674  |  USD 6,8474  
Tipo de máquina personalizado: ` cloud_tpu ` _(Beta)_ |  USD 9,4900  |  USD
6,5700  
  
Na tabela, mostramos os preços apenas para os EUA. Não há alteração na
disponibilidade da Cloud TPU no Cloud ML Engine. Veja mais detalhes no [ guia
de preços ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=pt_br) .

##  6 de agosto de 2018

**FEATURE:**

A versão 1.9 do ambiente de execução do Cloud ML Engine já está disponível
para treinamento e previsão. Essa versão é compatível com o TensorFlow 1.9 e
outros pacotes, conforme descrito na [ Lista de versões do ambiente de
execução ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=pt_br) .

##  23 de julho de 2018

**FEATURE:**

O Cloud ML Engine agora é compatível com **scikit-learn** e **XGBoost** para
treinamento. Esse recurso está com disponibilidade geral. Consulte o guia de [
treinamento com scikit-learn e XGBoost no Cloud ML Engine
](https://cloud.google.com/ml-engine/docs/scikit/getting-started-
training?hl=pt_br) .

**FEATURE:**

A previsão on-line com **scikit-learn** e **XGBoost** já está disponível para
o público em geral.

  * Defina ` framework ` em [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=pt_br) para especificar o framework de machine learning ao criar uma versão de modelo. Os valores válidos são: ` TENSORFLOW ` , ` SCIKIT_LEARN ` e ` XGBOOST ` . ` TENSORFLOW ` é o padrão. Se você especificar ` SCIKIT_LEARN ` ou ` XGBOOST ` , também precisará definir ` runtimeVersion ` como 1.4 ou superior na versão de modelo. 
  * Consulte o guia de [ treinamento local e previsões on-line com scikit-learn e XGBoost ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=pt_br) . 

##  12 de julho de 2018

**FEATURE:**

É possível adicionar rótulos aos recursos do AI Platform Training: [ jobs
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=pt_br) , [ modelos
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models?hl=pt_br) e [ versões
de modelo ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=pt_br) .
Use esses rótulos para organizar os recursos em categorias. Os rótulos também
estão disponíveis [ nas operações ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.operations?hl=pt_br) . Nesse
caso, eles são derivados do recurso referente à operação. Leia mais sobre [
como adicionar e usar rótulos ](https://cloud.google.com/ml-
engine/docs/tensorflow/resource-labels?hl=pt_br) .

##  26 de junho de 2018

**CHANGED:**

As seguintes regiões agora estão totalmente disponíveis:

  * us-east1 
  * asia-northeast1 

Veja mais detalhes sobre a [ disponibilidade por região
](https://cloud.google.com/ai-platform/training/docs/regions?hl=pt_br) .

##  13 de junho de 2018

**CHANGED:**

A compatibilidade com treinamento de TPU no ambiente de execução do Cloud ML
versão 1.6 terminou em 13 de junho de 2018. Veja as versões atualmente
compatíveis na [ Lista de versões do ambiente de execução
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=pt_br#tpu-support) .

##  29 de maio de 2018

**CHANGED:**

Agora é possível usar a Cloud TPU ( _Beta_ ) com o TensorFlow 1.8 e a versão
1.8 do ambiente de execução do Cloud ML Engine.

_Informações contextuais:_ a Cloud TPU ficou disponível para as versões 1.6 e
1.7 do ambiente de execução do Cloud ML Engine em 14 de maio. Na semana
passada, lançamos a versão 1.8 do ambiente de execução, mas a Cloud TPU ainda
não estava disponível para o TensorFlow 1.8. Agora ela está. Veja como [ usar
TPUs para treinar modelos ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-tpus?hl=pt_br) no Cloud ML Engine.

##  16 de maio de 2018

**FEATURE:**

A versão 1.8 do ambiente de execução do Cloud ML Engine já está disponível
para treinamento e previsão. Essa versão é compatível com o TensorFlow 1.8 e
outros pacotes, conforme descrito na [ Lista de versões do ambiente de
execução ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=pt_br) .

##  15 de maio de 2018

**FEATURE:**

Agora é possível atualizar o número mínimo de nós para [ escalonamento
automático ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=pt_br#autoscaling)
em uma versão de modelo atual, além de especificar o atributo ao criar uma
nova versão.

##  14 de maio de 2018

**FEATURE:**

O Cloud ML Engine agora oferece a Cloud TPU _(Beta)_ para treinamento de
modelos do TensorFlow. As unidades de processamento de tensor (TPUs) são ASICs
personalizados do Google, que são usadas para acelerar as cargas de trabalho
de machine learning. Veja [ como usar TPUs para treinar modelos
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=pt_br) no
Cloud ML Engine.

##  26 de abril de 2018

**FEATURE:**

A versão 1.7 do ambiente de execução do Cloud ML Engine já está disponível
para treinamento e previsão. Essa versão é compatível com o TensorFlow 1.7 e
outros pacotes, conforme descrito na [ Lista de versões do ambiente de
execução ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=pt_br) .

##  16 de abril de 2018

**FEATURE:**

**Algoritmos de hiperparâmetros:** ao ajustar os hiperparâmetros no job de
treinamento, agora é possível especificar um algoritmo de pesquisa [ em
HyperparameterSpec ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=pt_br#hyperparameterspec)
. Veja a seguir os valores disponíveis:

  * ` GRID_SEARCH ` : uma pesquisa de grade simples dentro do espaço viável. Essa opção será útil principalmente se você quiser especificar um número de tentativas que seja maior que o número de pontos no espaço viável. Nesse caso, se você não especificar uma pesquisa de grade, o algoritmo padrão do Cloud ML Engine poderá gerar sugestões duplicadas. Para usar a pesquisa de grade, todos os parâmetros precisam ser do tipo ` INTEGER ` , ` CATEGORICAL ` ou ` DISCRETE ` . 
  * ` RANDOM_SEARCH ` : uma pesquisa aleatória simples dentro do espaço viável. 

Se você não especificar um algoritmo, o job usará o algoritmo padrão do Cloud
ML Engine, que controla a pesquisa no espaço de parâmetros de maneira mais
eficaz para chegar à solução ideal. Para mais informações, consulte a [ visão
geral do ajuste de hiperparâmetros ](https://cloud.google.com/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview?hl=pt_br) .

##  5 de abril de 2018

**FEATURE:**

O Cloud ML Engine agora é compatível com o **scikit-learn** e o **XGBoost**
para previsões on-line. Esse recurso está na versão _Beta_ .

  * Defina ` framework ` em [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=pt_br) para especificar o framework de machine learning ao criar uma versão de modelo. Os valores válidos são: ` TENSORFLOW ` , ` SCIKIT_LEARN ` e ` XGBOOST ` . ` TENSORFLOW ` é o padrão. Se você especificar ` SCIKIT_LEARN ` ou ` XGBOOST ` , também precisará definir ` runtimeVersion ` como 1.4 ou superior na versão de modelo. 
  * Consulte o guia para [ scikit-learn e XGBoost no Cloud ML Engine ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=pt_br) . 

**FEATURE:**

O Python 3.5 está disponível para previsão on-line.

  * Defina ` pythonVersion ` em [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=pt_br) para especificar a versão do Python ao criar uma versão de modelo. O padrão é o Python 2.7. 
  * Para saber detalhes de todos os pacotes disponíveis no Cloud ML Engine, consulte a [ Lista de versões do ambiente de execução ](https://cloud.google.com/ml-engine/docs/scikit/runtime-version-list?hl=pt_br) . 

##  20 de março de 2018

**FEATURE:**

A versão 1.6 do ambiente de execução do Cloud ML Engine já está disponível
para treinamento e previsão. Esta versão é compatível com o TensorFlow 1.6 e
outros pacotes, conforme listado na [ Lista de versões do ambiente de execução
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=pt_br) .

##  13 de março de 2018

**FEATURE:**

A versão do ambiente de execução do Cloud ML Engine para TensorFlow 1.5 já
está disponível para treinamento e previsão. Para mais informações, consulte a
[ Lista de versões do ambiente de execução ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=pt_br) .

##  8 de fevereiro de 2018

**FEATURE:**

Foram adicionados novos recursos para o ajuste de hiperparâmetros: parada
antecipada automática de testes, retomada de um job anterior de ajuste de
hiperparâmetro e outras otimizações de eficiência quando você executa jobs
semelhantes. Para mais informações, consulte a [ visão geral do ajuste de
hiperparâmetro ](https://cloud.google.com/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview?hl=pt_br) .

##  14 de dezembro de 2017

**FEATURE:**

A versão do ambiente de execução do Cloud ML Engine para TensorFlow 1.4 já
está disponível para treinamento e previsão. Para mais informações, consulte a
[ Lista de versões do ambiente de execução ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=pt_br) .

**FEATURE:**

O Python 3 já está disponível para treinamento como parte da versão do
ambiente de execução do Cloud ML Engine para TensorFlow 1.4. Para mais
informações, consulte a [ Lista de versões do ambiente de execução
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=pt_br) .

**FEATURE:**

Agora o recurso de previsão on-line está disponível de modo geral para um
único núcleo. Consulte o guia sobre [ previsão on-line
](https://cloud.google.com/ml-engine/docs/tensorflow/online-predict?hl=pt_br)
e a [ postagem do blog ](https://cloud.google.com/blog/big-
data/2017/12/bringing-cloud-ml-engine-to-more-developers-with-online-
prediction-features-and-reduced-prices?hl=pt_br) .

**FEATURE:**

O preço foi reduzido e simplificado para treinamento e previsão. Consulte os [
detalhes de preços ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=pt_br) , a [ postagem do blog
](https://cloud.google.com/blog/big-data/2017/12/bringing-cloud-ml-engine-to-
more-developers-with-online-prediction-features-and-reduced-prices?hl=pt_br) e
a comparação entre os preços anteriores e atuais nas [ Perguntas frequentes
sobre preços ](https://cloud.google.com/ml-engine/docs/tensorflow/pricing-
faq?hl=pt_br) .

**FEATURE:**

As GPUs P100 estão agora em fase Beta. O uso delas passará a gerar cobranças.
Para mais informações, consulte [ Como usar GPUs
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=pt_br) e [
Preços ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=pt_br)
.

##  26 de outubro de 2017

**FEATURE:**

A geração de registros de auditoria do Cloud ML Engine está agora na versão
Beta. Para mais informações, consulte [ Como ver registros de auditoria
](https://cloud.google.com/ml-engine/docs/tensorflow/audit-logs?hl=pt_br) .

##  25 de setembro de 2017

**FEATURE:**

Os papéis de IAM predefinidos para Cloud ML Engine estão disponíveis para uso
geral. Consulte [ Controle de acesso ](https://cloud.google.com/ml-
engine/docs/tensorflow/access-control?hl=pt_br) para mais informações.

##  27 de junho de 2017

**FEATURE:**

A versão do ambiente de execução do Cloud ML Engine para TensorFlow 1.2 já
está disponível para treinamento e previsão. Para mais informações, consulte a
[ Lista de versões do ambiente de execução ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=pt_br) .

**DEPRECATED:**

As versões anteriores do ambiente de execução no TensorFlow 0.11 e 0.12 não
são mais compatíveis com o Cloud ML Engine. Para mais informações, consulte a
[ Lista de versões do ambiente de execução ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=pt_br) e os [ cronogramas de
compatibilidade para versões anteriores do ambiente de execução
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=pt_br#runtime-version-support) .

##  9 de maio de 2017

**FEATURE:**

Anunciada a disponibilidade geral de máquinas habilitadas para GPU. Para mais
informações, consulte [ Como usar GPUs para modelos de treinamento na nuvem
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=pt_br) .

##  27 de abril de 2017

**FEATURE:**

As GPUs estão agora disponíveis na região us-central1. Para a lista completa
de regiões compatíveis com GPUs, consulte [ Como usar GPUs para modelos de
treinamento na nuvem ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=pt_br#requesting_gpu-enabled_machines) .

##  v1 (8 de março de 2017)

**FEATURE:**

Anunciada a disponibilidade geral do AI Platform Training. A versão 1 do Cloud
ML Engine está disponível para uso geral para treinar modelos, implantar
modelos e gerar previsões em lote. O recurso de [ ajuste de hiperparâmetro
](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-tuning-
overview?hl=pt_br) também está disponível para uso geral, mas a previsão on-
line e as [ máquinas habilitadas para GPU ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=pt_br) permanecem na versão Beta.

**FEATURE:**

A previsão on-line está agora na [ fase de lançamento
](https://cloud.google.com/terms/launch-stages?hl=pt_br) Beta. No momento, seu
uso está sujeito à [ política de preços ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=pt_br) do Cloud ML Engine e à mesma fórmula
de preços da previsão em lote. Enquanto permanecer em Beta, a previsão on-line
não se destina ao uso em aplicativos críticos.

**CHANGED:**

Os ambientes que o Cloud ML Engine usa para treinar modelos e conseguir
previsões foram definidos como [ versões do ambiente de execução
](https://cloud.google.com/ml-engine/docs/tensorflow/versioning?hl=pt_br) do
Cloud ML Engine. Especifique uma versão de ambiente de execução compatível
para usar ao treinar, definir um recurso de modelo ou solicitar previsões em
lote. Neste momento, as versões de ambiente de execução diferem principalmente
em relação à versão do TensorFlow compatível com cada uma delas, mas outras
diferenças poderão surgir ao longo do tempo. Você encontra os detalhes na [
Lista de versões do ambiente de execução ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=pt_br) .

**CHANGED:**

Agora é possível executar trabalhos de previsão em lote com base nos
SavedModels do TensorFlow que estiverem armazenados no Google Cloud Storage e
não hospedados como uma versão do modelo no Cloud ML Engine. Ao criar o job,
use o URI do SavedModel em vez de fornecer um ID de modelo ou versão.

**DEPRECATED:**

O uso do SDK do Google Cloud Machine Learning, anteriormente lançado como
Alfa, está suspenso e não é mais aceito desde 7 de maio de 2017. A maior parte
da funcionalidade disponibilizada pelo SDK foi transferida para o novo pacote
do TensorFlow, [ tf.Transform ](https://github.com/tensorflow/transform) (em
inglês). Use a tecnologia ou ferramenta que preferir para fazer o pré-
processamento dos dados de entrada. No entanto, recomendamos o ` tf.Transform
` e os serviços disponíveis no Google Cloud Platform, incluindo o Google Cloud
Dataflow, o Google Cloud Dataproc e o Google BigQuery.

##  v1beta1 (29 de setembro de 2016)

**FEATURE:**

A previsão on-line é um recurso Alfa. O AI Platform Training está na versão
Beta, mas a previsão on-line ainda está passando por mudanças significativas
para melhorar o desempenho. Você não será [ cobrado
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=pt_br) pela
previsão on-line enquanto ela for um recurso Alfa.

**FEATURE:**

O pré-processamento e o restante do Cloud ML Engine SDK são recursos Alfa. O
SDK está em desenvolvimento ativo para melhorar a integração entre o Cloud ML
Engine e o Apache Beam.

