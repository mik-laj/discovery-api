#  Notas da versão

Nesta página, você encontrará atualizações de produção para o Cloud TPU.
Verifique-a periodicamente para ver avisos sobre recursos novos ou
atualizados, correção de bugs, problemas conhecidos e funcionalidades
obsoletas.

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  7 de maio de 2019

**FEATURE:**

O Cloud TPU v2 está disponível na versão Beta.

Como os recursos de TPU podem ser escalonados de um único Cloud TPU para um
pod do Cloud TPU, você não precisa escolher entre Cloud TPU único e um pod do
Cloud TPU. É possível solicitar partes dos pods do Cloud TPU em _frações_ ou
conjuntos de núcleos, para comprar apenas o poder de processamento necessário.

[ Vantagens do pod do Cloud TPU (beta) em relação a um único dispositivo Cloud
TPU v2: ](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=pt_br)

  * aumento da velocidade de treinamento para rápida iteração de P&D 
  * aumento da produtividade humana por meio de computador de machine learning (ML) escalonável automaticamente 
  * capacidade de treinar modelos muito maiores 

**FEATURE:**

O pod do Cloud TPU v3 está disponível na versão Beta.

Como os recursos de TPU podem ser escalonados de um único Cloud TPU para um
pod do Cloud TPU, você não precisa escolher entre Cloud TPU único e um pod do
Cloud TPU. É possível solicitar partes dos pods do Cloud TPU em _frações_ ou
conjuntos de núcleos, para comprar apenas o poder de processamento necessário.

[ Vantagens do pod do Cloud TPU (beta) em relação a um único dispositivo do
Cloud TPU v3: ](https://cloud.google.com/tpu/docs/deciding-pod-versus-
tpu?hl=pt_br)

  * aumento da velocidade de treinamento para rápida iteração de P&D 
  * aumento da produtividade humana por meio de computação de machine learning (ML) escalonável automaticamente 
  * capacidade de treinar modelos muito maiores 

Vantagens do pod do Cloud TPU v3 _(beta)_ em relação ao pod do Cloud TPU v2
_(beta)_ :

* Processamento mais rápido e memória maior: 

  * Pod v2: 11.5 petaflops e 4 TB de memória no chip (HBM) 
  * Pod v3: 100 petaflops e 32 TB HBM, com refrigeração líquida 

* Capacidade de treinar modelos ainda maiores 

##  11 de março de 2019

**CHANGED:**

O Cloud TPU agora é compatível com o [ TensorFlow versão 1.13
](https://www.tensorflow.org/versions/r1.13/api_docs/?hl=pt_br) . A
compatibilidade com as versões 1.8 e 1.9 do Tensorflow foi removida.

Consulte a [ política de controle de versão do Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=pt_br) para saber
quais versões atuais do TensorFlow são compatíveis.

##  31 de janeiro de 2019

**FEATURE:**

O Cloud TPU v3 agora é de disponibilidade geral (GA, na sigla em inglês). O
Cloud TPU v3 tem o dobro da memória da v2. Isso proporciona melhor desempenho
e compatibilidade com mais classes de modelos, por exemplo, ResNets mais
profundos e imagens maiores com o RetinaNet. Os modelos atuais executados no
Cloud TPU v2 continuarão funcionando. Consulte o [ guia de versões do Cloud
TPU ](https://cloud.google.com/tpu/docs/deciding-tpu-version?hl=pt_br) para
mais informações.

##  8 de novembro de 2018

**CHANGED:**

O Cloud TPU agora é compatível com o [ TensorFlow versão 1.12
](https://www.tensorflow.org/versions/r1.12/api_docs/?hl=pt_br) . Essa versão
inclui melhorias para Keras em Cloud TPUs, otimizações de desempenho em toda a
pilha de software e aprimoramentos em APIs, mensagens de erro e
confiabilidade.

Consulte a [ política de controle de versão do Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=pt_br) para saber
quais versões atuais do TensorFlow são compatíveis.

##  7 de novembro de 2018

**FEATURE:**

O Cloud TPU v2 está disponível na versão Alfa.

Como os recursos de TPU podem ser escalonados de um único Cloud TPU para um
pod do Cloud TPU, você não precisa escolher entre Cloud TPU único e um pod do
Cloud TPU. É possível solicitar partes dos pods do Cloud TPU em _frações_ ou
conjuntos de núcleos, para comprar apenas o poder de processamento necessário.

[ Vantagens do pod do Cloud TPU (alfa)
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=pt_br)

  * aumento da velocidade de treinamento para rápida iteração de P&D 
  * aumento da produtividade humana por meio de computação de machine learning (ML) escalonável automaticamente 
  * capacidade de treinar modelos muito maiores do que um único acelerador de ML 

##  10 de outubro de 2018

**FEATURE:**

O Cloud TPU v3 está disponível na versão Beta. Agora é possível escolher entre
v2 e v3 na configuração.

  * O Cloud TPU v3 tem o dobro da memória do Cloud TPU v2. Isso melhora o desempenho e permite que ele seja compatível com mais classes de modelos, como ResNets mais profundos e imagens maiores com o RetinaNet. 
  * Os modelos atuais executados no Cloud TPU v2 continuarão funcionando. 
  * Consulte o [ guia de versões do Cloud TPU para mais informações. ](https://cloud.google.com/tpu/docs/deciding-tpu-version?hl=pt_br)

##  10 de outubro de 2018

**CHANGED:**

As TPUs preemptivas agora são de disponibilidade geral. Uma TPU preemptiva é
um nó do Cloud TPU que pode ser criado e executado a um preço muito menor do
que o dos nós normais. No entanto, o Cloud TPU pode encerrar (por preempção)
esses nodes caso seja necessário ter acesso aos recursos para outros fins.

  * Veja como [ usar uma TPU preemptiva ](https://cloud.google.com/tpu/docs/preemptible?hl=pt_br) . 
  * Consulte os [ preços ](https://cloud.google.com/tpu/docs/pricing?hl=pt_br) dos nós preemptivos e normais do Cloud TPU. 

##  27 de setembro de 2018

**CHANGED:**

O Cloud TPU agora é compatível com o [ TensorFlow versão 1.11
](https://www.tensorflow.org/versions/r1.11/api_docs/?hl=pt_br) . O TensorFlow
1.11 tem compatibilidade experimental com todas as opções a seguir do Cloud
TPU: Keras, Colab, execução rápida, LARS, RNNs e [ Mesh TensorFlow
](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/mesh_tensorflow/README.md)
. Essa versão também inclui uma integração de alto desempenho do [ Cloud
Bigtable ](https://cloud.google.com/bigtable/?hl=pt_br) , otimizações do
compilador XLA, melhorias de desempenho em toda a pilha de software e
aprimoramentos em APIs, mensagens de erro e confiabilidade.

Consulte a [ política de controle de versão do Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=pt_br) para saber
quais versões atuais do TensorFlow são compatíveis.

##  7 de setembro de 2018

**CHANGED:**

A compatibilidade com o TensorFlow versão 1.7 terminou em 7 de setembro de
2018. Veja as versões atualmente compatíveis na página de [ política de
controle de versão do Cloud TPU ](https://cloud.google.com/tpu/docs/supported-
versions?hl=pt_br) .

##  24 de julho de 2018

**CHANGED:**

Temos o prazer de anunciar o preço promocional do Cloud TPU, com descontos
significativos. A tabela a seguir mostra o preço anterior e o novo, disponível
a partir de hoje:

###  EUA

|  Preço anterior por TPU/hora  |  Preço novo por TPU/hora  
---|---|---  
Cloud TPU  |  USD 6,50  |  USD 4,50  
TPU preemptiva  |  USD 1,95  |  USD 1,35  
  
###  Europa

|  Preço anterior por TPU/hora  |  Preço novo por TPU/hora  
---|---|---  
Cloud TPU  |  USD 7,15  |  USD 4,95  
TPU preemptiva  |  USD 2,15  |  USD 1,485  
  
###  Ásia-Pacífico

|  Preço anterior por TPU/hora  |  Preço novo por TPU/hora  
---|---|---  
Cloud TPU  |  USD 7,54  |  USD 5,22  
TPU preemptiva  |  USD 2,26  |  USD 1,566  
  
Veja mais detalhes no [ guia de preços
](https://cloud.google.com/tpu/docs/pricing?hl=pt_br) .

##  12 de julho de 2018

**FEATURE:**

O Cloud TPU já está disponível no Google Kubernetes Engine como um recurso
Beta. Execute sua carga de trabalho de machine learning em um cluster do GCP
para que o GKE gerencie e dimensione os recursos do Cloud TPU por você.

  * Siga o [ tutorial ](https://cloud.google.com/tpu/docs/tutorials/kubernetes-engine-resnet?hl=pt_br) para treinar o modelo Tensorflow ResNet-50 no Cloud TPU e no GKE. 
  * Consulte o [ guia de configuração do GKE ](https://cloud.google.com/tpu/docs/kubernetes-engine-setup?hl=pt_br) para saber instruções rápidas sobre como executar o Cloud TPU com o GKE. 

##  2 de julho de 2018

**CHANGED:**

O Cloud TPU agora é compatível com o [ TensorFlow versão 1.9
](https://www.tensorflow.org/versions/r1.9/api_docs/?hl=pt_br) . O TensorFlow
1.9 aumenta o desempenho do Cloud TPU, além de trazer melhorias nas APIs, nas
mensagens de erro e na confiabilidade.

##  27 de junho de 2018

**FEATURE:**

O Cloud TPU é de disponibilidade geral (GA, na sigla em inglês). As TPUs do
Google são revolucionárias e foram desenvolvidas para acelerar as cargas de
trabalho de aprendizado de máquina com o TensorFlow. Cada Cloud TPU fornece
até 180 teraflops de desempenho, o que corresponde à capacidade de computação
necessária para treinar e executar modelos de aprendizado de máquina modernos.

  * Siga o [ guia de início rápido ](https://cloud.google.com/tpu/docs/quickstart?hl=pt_br) para configurar seu Cloud TPU. 
  * Escolha um [ tutorial ](https://cloud.google.com/tpu/docs/tutorials?hl=pt_br) para executar um modelo específico em seu Cloud TPU. 

##  18 de junho de 2018

**FEATURE:**

As TPUs preemptíveis agora estão disponíveis na versão _Beta_ . Uma TPU
preemptiva é um nó do Cloud TPU que pode ser criado e executado a um preço
muito menor do que o dos nós normais. No entanto, o Cloud TPU pode encerrar
(por preempção) esses nodes caso seja necessário ter acesso aos recursos para
outros fins.

  * Veja como [ usar uma TPU preemptiva ](https://cloud.google.com/tpu/docs/preemptible?hl=pt_br) . 
  * Consulte os [ preços ](https://cloud.google.com/tpu/docs/pricing?hl=pt_br) dos nós preemptivos e normais do Cloud TPU. 

**CHANGED:**

O Cloud TPU agora está disponível nas regiões da Europa (EU) e Ásia-Pacífico
(APAC), além dos Estados Unidos (EUA). Veja os [ detalhes de preços
](https://cloud.google.com/tpu/docs/pricing?hl=pt_br) por região. As zonas a
seguir estão disponíveis:

  * **EUA**
    * ` us-central1-b `
    * ` us-central1-c `
    * ` us-central1-f ` ( [ (apenas o programa TFRC ](https://www.tensorflow.org/tfrc/?hl=pt_br) ) 
  * **EU**
    * ` europe-west4-a `
  * **APAC (Ásia-Pacífico)**
    * ` asia-east1-c `

##  12 de junho de 2018

**CHANGED:**

A compatibilidade com o TensorFlow versão 1.6 terminou dia 12 de junho de
2018. Veja as versões atualmente compatíveis na página de [ política de
controle de versão do Cloud TPU ](https://cloud.google.com/tpu/docs/supported-
versions?hl=pt_br) .

##  20 de abril de 2018

**CHANGED:**

O Cloud TPU agora é compatível com o [ TensorFlow versão 1.8
](https://www.tensorflow.org/versions/r1.8/api_docs/?hl=pt_br) . O TensorFlow
1.8 aumenta o desempenho do Cloud TPU, além de trazer melhorias nas APIs, nas
mensagens de erro e na confiabilidade.

A compatibilidade com o TensorFlow versão 1.7 termina dia 20 de junho de 2018.
Veja os detalhes na [ política de controle de versão do Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=pt_br) .

##  2 de abril de 2018

**CHANGED:**

O Cloud TPU agora é compatível com o [ TensorFlow versão 1.7
](https://www.tensorflow.org/versions/r1.7/api_docs/?hl=pt_br) . A
compatibilidade com o TensorFlow versão 1.6 termina dia 2 de junho de 2018.
Veja os detalhes na [ política de controle de versão do Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=pt_br) .

##  12 de fevereiro de 2018

**FEATURE:**

O Cloud TPU está disponível na versão Beta. As TPUs revolucionárias do Google
foram desenvolvidas para acelerar as cargas de trabalho de aprendizado de
máquina com o TensorFlow. Cada Cloud TPU fornece até 180 teraflops de
desempenho, o que corresponde à capacidade de computação necessária para
treinar e executar modelos de aprendizado de máquina modernos.

  * Veja como [ solicitar cotas de TPU ](https://cloud.google.com/tpu/docs/quota?hl=pt_br) . 
  * Siga o [ guia de início rápido ](https://cloud.google.com/tpu/docs/quickstart?hl=pt_br) para configurar seu Cloud TPU. 
  * Escolha um [ tutorial ](https://cloud.google.com/tpu/docs/tutorials?hl=pt_br) para executar um modelo específico em seu Cloud TPU. 

