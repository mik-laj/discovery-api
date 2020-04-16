#  Notas da versão: SDK do Dataflow 1.x para Java

**Aviso:** o SDK 1.x do Cloud Dataflow para Java não recebe mais suporte desde
16 de outubro de 2018. Consulte [ Migração do SDK 1.x do Cloud Dataflow para
Java ](https://cloud.google.com/dataflow/docs/guides/migrate-
java-1-to-2?hl=pt_br) para orientações sobre migração.

Nesta página, apresentamos as atualizações de produção para o SDK 1.x do
Dataflow para Java. Acesse-a periodicamente para ver anúncios sobre recursos
novos ou atualizados, correções de bugs, problemas conhecidos e
funcionalidades obsoletas. Consulte as [ Notas da versão do SDK 2.x do
Dataflow para Java ](https://cloud.google.com/dataflow/release-notes/release-
notes-java-2?hl=pt_br) para se informar sobre essa versão.

Veja na [ página de suporte
](https://cloud.google.com/dataflow/support?hl=pt_br#supportstatus) mais
informações sobre o status de suporte de cada versão do SDK do Dataflow.

Para instalar e usar o SDK do Dataflow, consulte o [ guia de instalação do SDK
do Dataflow ](https://cloud.google.com/dataflow/docs/installing-dataflow-
sdk?hl=pt_br) .

##  16 de outubro de 2018

**DEPRECATED:**

O SDK 1.x do Cloud Dataflow para Java estará indisponível a partir de 16 de
outubro de 2018. Em breve, o serviço do Cloud Dataflow rejeitará novos jobs do
Cloud Dataflow baseados no SDK do Cloud Dataflow 1.x para Java. Consulte [
Migração do SDK 1.x do Cloud Dataflow para Java
](https://cloud.google.com/dataflow/docs/guides/migrate-java-1-to-2?hl=pt_br)
para orientações sobre migração.

##  1.9.1 (28 de agosto de 2017)

**FIXED:**

Correção de um problema dos jobs do Dataflow na leitura de ` CompressedSource
` s com tipo de compactação definido como ` BZIP2 ` , que podem estar perdendo
dados durante o processamento. Para mais informações, consulte o [ Problema nº
596 ](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) no
repositório do GitHub.

##  1.9.0 (20 de dezembro de 2016)

**ISSUE:**

**Problema identificado:** jobs do Dataflow na leitura de ` CompressedSource `
s com tipo de compactação definido como ` BZIP2 ` podem estar perdendo dados
durante o processamento. Para mais informações, consulte o [ Problema nº 596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) no
repositório do GitHub.

**FEATURE:**

Inclusão de suporte para usar a [ Interface do Stackdriver Error Reporting
](https://cloud.google.com/dataflow/pipelines/dataflow-monitoring-
intf?hl=pt_br#error-reporting) .

**FEATURE:**

Inclusão da interface ` ValueProvider ` para uso em opções de pipeline. Ao
optar pelo tipo ` ValueProvider<T> ` em vez de ` T ` , o valor será fornecido
no ambiente de execução em vez de no tempo de construção do pipeline e ativará
os [ modelos do Cloud Dataflow
](https://cloud.google.com/dataflow/docs/templates/overview?hl=pt_br) . O
suporte para ` ValueProvider ` foi incluído em ` TextIO ` , ` PubSubIO ` e `
BigQueryIO ` e pode ser adicionado a PTransforms aleatórios também. Para mais
detalhes, consulte a [ documentação sobre modelos do Cloud Dataflow
](https://cloud.google.com/dataflow/docs/templates/overview?hl=pt_br) .

**FEATURE:**

Inclusão da capacidade de salvar automaticamente informações de perfil no
Google Cloud Storage usando a opção de pipeline ` --saveProfilesToGcs ` . Para
mais informações sobre pipelines de perfil executados pelo `
DataflowPipelineRunner ` , consulte o [ problema nº 72 do GitHub
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/72) .

**DEPRECATED:**

Suspensão do uso da opção de pipeline ` --enableProfilingAgent ` que salvava
perfis nos discos de cada worker. Para mais informações sobre pipelines de
perfil executados pelo ` DataflowPipelineRunner ` , consulte o [ problema nº
72 do GitHub
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/72) .

**CHANGED:**

Alteração de ` FileBasedSource ` para gerar uma exceção na leitura de um
padrão de arquivo que não tenha correspondências. Agora, em vez de não lerem
dados de maneira silenciosa, os pipelines falharão por tempo de execução. Essa
alteração afeta ` TextIO.Read ` ou ` AvroIO.Read ` quando ` withoutValidation
` está configurado.

**CHANGED:**

Validação de ` Coder ` aprimorada no ` DirectPipelineRunner ` para detectar
coders que não conseguem codificar e descodificar corretamente a entrada.

**CHANGED:**

Exibição aprimorada de dados em todas as transformações básicas, inclusive o
processamento apropriado de matrizes em ` PipelineOptions ` .

**CHANGED:**

Desempenho aprimorado de pipelines usando ` DataflowPipelineRunner ` no modo
de streaming.

**CHANGED:**

Escalabilidade aprimorada do ` InProcessRunner ` , possibilitando testes com
conjuntos de dados maiores.

**CHANGED:**

Limpeza aprimorada de arquivos temporários criados por ` TextIO ` , ` AvroIO `
e outras implementações de ` FileBasedSource ` .

##  1.8.1 (12 de dezembro de 2016)

**ISSUE:**

**Problema identificado:** jobs do Dataflow na leitura de ` CompressedSource `
s com tipo de compactação definido como ` BZIP2 ` podem estar perdendo dados
durante o processamento. Para mais informações, consulte o [ Problema nº 596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) no
repositório do GitHub.

**CHANGED:**

Desempenho aprimorado de entradas secundárias no ` DataflowPipelineRunner ` .

##  1.8.0 (3 de outubro de 2016)

**ISSUE:**

**Problema identificado:** jobs do Dataflow na leitura de ` CompressedSource `
s com tipo de compactação definido como ` BZIP2 ` podem estar perdendo dados
durante o processamento. Para mais informações, consulte o [ Problema nº 596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) no
repositório do GitHub.

**FEATURE:**

Inclusão de suporte em ` BigQueryIO.Read ` para consultas no novo dialeto [
SQL padrão ](https://cloud.google.com/bigquery/sql-reference/?hl=pt_br) do
BigQuery usando ` .withStandardSQL() ` .

**FEATURE:**

Inclusão de suporte em ` BigQueryIO ` para novos [ tipos
](https://cloud.google.com/bigquery/sql-reference/data-types?hl=pt_br) de `
BYTES ` , ` TIME ` , ` DATE ` e ` DATETIME ` .

**FEATURE:**

Inclusão de suporte em ` BigtableIO.Read ` para leitura de um intervalo de
chaves restrito usando ` .withKeyRange(ByteKeyRange) ` .

**CHANGED:**

Divisão inicial aprimorada de arquivos grandes descompactados em `
CompressedSource ` , o que melhora o desempenho durante a execução de
pipelines em lote que usam ` TextIO.Read ` no serviço do Cloud Dataflow.

**FIXED:**

Correção da [ regressão de desempenho
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/451) quando `
BigQueryIO.Write ` é usado no modo de streaming.

##  1.7.0 (9 de setembro de 2016)

**ISSUE:**

**Problema identificado:** jobs do Dataflow na leitura de ` CompressedSource `
s com tipo de compactação definido como ` BZIP2 ` podem estar perdendo dados
durante o processamento. Para mais informações, consulte o [ Problema nº 596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) no
repositório do GitHub.

**ISSUE:**

**Problema identificado:** encontramos uma regressão de desempenho em `
BigQueryIO.Write ` . Durante a execução no modo de streaming, os usuários
poderão notar um pequeno aumento nas falhas de inserção, mesmo que nenhum dado
seja perdido ou duplicado. Para mais informações, consulte o [ Problema nº 451
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/451) no
repositório do GitHub.

**FEATURE:**

Inclusão de suporte na API Cloud Datastore v1 no novo `
com.google.cloud.dataflow.sdk.io.datastore.DatastoreIO ` . Suspensão do uso da
antiga classe ` DatastoreIO ` que era compatível somente com a API Cloud
Datastore v1beta2, atualmente obsoleta.

**FEATURE:**

` DatastoreIO.Read ` aprimorado para ficar compatível com o rebalanceamento
dinâmico de trabalho. Inclusão de uma opção para controlar o número de
divisões de consulta usando ` withNumQuerySplits ` .

**FEATURE:**

` DatastoreIO.Write ` aprimorado para trabalhar com uma ` PCollection `
ilimitada, dando suporte à gravação no Cloud Datastore quando `
DataflowPipelineRunner ` for usado no modo de streaming.

**FEATURE:**

Inclusão da capacidade de excluir diretamente objetos ` Entity ` do Cloud
Datastore usando ` Datastore.v1().deleteEntity ` ou de excluir entidades por
chave usando ` Datastore.v1().deleteKey ` .

**FEATURE:**

Inclusão de suporte para leitura de um ` BoundedSource ` para o `
DataflowPipelineRunner ` no modo de streaming. Isso permite o uso de `
TextIO.Read ` , ` AvroIO.Read ` e outras fontes vinculadas nesses pipelines.

**FEATURE:**

Inclusão de suporte para gravação opcional de um cabeçalho e/ou rodapé em
arquivos de texto produzidos com ` TextIO.Write ` .

**FEATURE:**

Inclusão da capacidade de controlar o número de fragmentos de saída produzidos
com o uso de ` Sink ` .

**FEATURE:**

Inclusão de ` TestStream ` para possibilitar testes de acionadores com vários
painéis e dados atrasados com o ` InProcessPipelineRunner ` .

**FEATURE:**

Inclusão da capacidade de controlar a taxa em que ` UnboundedCountingInput `
produz elementos usando ` withRate(long, Duration) ` .

**FEATURE:**

Desempenho e estabilidade aprimorados para pipelines usando `
DataflowPipelineRunner ` no modo de streaming.

**CHANGED:**

Para ser aceito por ` TestStream ` , ` DataflowAssert ` foi reimplementado
para usar ` GroupByKey ` em vez de ` sideInputs ` ao verificar declarações.
Essa é uma alteração incompatível com atualizações no ` DataflowAssert ` para
pipelines executados no ` DataflowPipelineRunner ` no modo de streaming.

**FIXED:**

Correção de um problema em que um ` FileBasedSink ` não produzia arquivos ao
gravar uma ` PCollection ` vazia.

**FIXED:**

Correção de um problema em que ` BigQueryIO.Read ` não conseguia consultar
tabelas em uma região sem ser ` US ` quando ` DirectPipelineRunner ` ou `
InProcessPipelineRunner ` era usado.

**FIXED:**

Correção de um problema em que a combinação entre um ` allowedLateness `
grande e carimbos de data/hora próximos ao final da janela global provocava
uma ` IllegalStateException ` para pipelines executados em `
DirectPipelineRunner ` .

**FIXED:**

Correção de uma ` NullPointerException ` que podia ser gerada durante o envio
de pipelines ao usar um acionador ` AfterWatermark ` sem disparos atrasados.

##  1.6.1 (8 de agosto de 2016)

**ISSUE:**

**Problema identificado:** jobs do Dataflow na leitura de ` CompressedSource `
s com tipo de compactação definido como ` BZIP2 ` podem estar perdendo dados
durante o processamento. Para mais informações, consulte o [ Problema nº 596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) no
repositório do GitHub.

**FIXED:**

Correção de um problema dos jobs do Dataflow na leitura de ` TextIO ` com tipo
de compactação definido como ` GZIP ` ou ` BZIP2 ` . Para mais informações,
consulte o [ Problema nº 356
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/356) no
repositório do GitHub.

##  1.6.0 (10 de junho de 2016)

**ISSUE:**

**Problema identificado:** jobs do Dataflow na leitura de ` CompressedSource `
s com tipo de compactação definido como ` BZIP2 ` podem estar perdendo dados
durante o processamento. Para mais informações, consulte o [ Problema nº 596
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/596) no
repositório do GitHub.

**ISSUE:**

**Problema identificado:** jobs do Dataflow na leitura de ` TextIO ` com tipo
de compactação definido como ` GZIP ` ou ` BZIP2 ` podem estar perdendo dados
durante o processamento. É aconselhável que os usuários utilizem as soluções
alternativas discutidas no [ Problema nº 356
](https://github.com/GoogleCloudPlatform/DataflowJavaSDK/issues/356) do
repositório do GitHub.

**FEATURE:**

Inclusão da exibição de dados, permitindo a anotação de funções de usuário ( `
DoFn ` , ` CombineFn ` e ` WindowFn ` ), de ` Source ` s e de ` Sink ` s com
metadados estáticos a serem exibidos na Interface de monitoramento do
Dataflow. Esses dados foram implementados para os principais componentes e são
automaticamente aplicados a todas as ` PipelineOptions ` .

**FEATURE:**

Inclusão dos métodos ` getSplitPointsConsumed ` e ` getSplitPointsRemaining `
na API ` BoundedReader ` para melhorar a capacidade do Dataflow de fazer o
escalonamento automático de um job que faz leitura dessas fontes. Foram
fornecidas implementações padrão dessas funções, mas é aconselhável que os
implementadores de leitor as modifiquem para fornecer informações melhores,
quando disponíveis.

**FEATURE:**

Inclusão da capacidade de gravar vários ` CombineFn ` s em um único `
CombineFn ` usando ` CombineFns.compose ` ou ` CombineFns.composeKeyed ` .

**FEATURE:**

Inclusão de ` InProcessPipelineRunner ` , um aprimoramento do `
DirectPipelineRunner ` que implementa melhor o modelo do Dataflow. `
InProcessPipelineRunner ` é executado na máquina local de um usuário e é
compatível com execução multithread, ` PCollections ` ilimitadas e acionadores
para saídas especulativas e atrasadas.

**CHANGED:**

` BigQueryIO ` reimplementado para que as implementações de `
DirectPipelineRunner ` e ` InProcessPipelineRunner ` sejam executadas de modo
semelhante ao ` DataflowPipelineRunner ` . Agora, é preciso especificar o [
parâmetro de execução
](https://cloud.google.com/dataflow/pipelines/specifying-exec-params?hl=pt_br)
` --tempLocation ` ao usar ` DirectPipelineRunner ` ou `
InProcessPipelineRunner ` .

**FIXED:**

Desempenho aprimorado de entradas secundárias ao usar workers com vários
núcleos.

**FIXED:**

Eficiência aprimorada ao usar ` CombineFnWithContext ` .

**FIXED:**

Correção de vários problemas relacionados à estabilidade no modo de streaming.

##  1.5.1 (15 de abril de 2016)

  * Correção de um problema que ocultava ` BigtableIO.Read.withRowFilter ` . Agora, as linhas do Cloud Bigtable podem ser filtradas na transformação ` Read ` . 
  * Correção de suporte para arquivos GZip concatenados. 
  * Correção de um problema que impedia ` Write.to ` de ser usado com janelas de mesclagem. 
  * Correção de um problema que causava acionamentos excessivos com repetição de acionadores compostos. 
  * Correção de um problema em janelas de mesclagem e acionadores que terminavam antes do final da janela. 

##  1.5.0 (14 de março de 2016)

Nesta versão, começamos a preparar o SDK do Dataflow para Java para uma
possível migração para o [ Apache Beam (em desenvolvimento)
](https://www.google.com/url?sa=D&q=https%3A%2F%2Fcloudplatform.googleblog.com%2F2016%2F01%2FDataflow-
and-open-source-proposal-to-join-the-Apache-Incubator.html&hl=pt_br) .
Especificamente, refatoramos várias APIs internas e as removemos das classes
do SDK usadas somente dentro do worker. Agora elas serão fornecidas pelo
serviço do Google Cloud Dataflow durante a execução do job. Essa refatoração
não afetará nenhum código de usuário.

Além disso, a versão 1.5.0 inclui as seguintes alterações:

  * Ativação de um formato de entrada secundária indexada para pipelines em lote executados no serviço do Google Cloud Dataflow. As entradas secundárias indexadas aumentam significativamente o desempenho de ` View.asList ` , ` View.asMap ` , ` View.asMultimap ` e quaisquer ` PCollectionView ` s sem janelas globais. 
  * Atualização para a versão ` 3.0.0-beta-1 ` do serviço Buffers de protocolo. Se você usa buffers de protocolo personalizados, recompile-os com a versão correspondente do compilador ` protoc ` . Você pode continuar usando as versões 2 e 3 da sintaxe do Buffers de protocolo porque não é necessário alterar nenhum código de pipeline do usuário. 
  * Inclusão de ` ProtoCoder ` , que é um ` Coder ` de mensagens do Buffers de protocolo compatível com as versões 2 e 3 da sintaxe do Buffers de protocolo. Esse coder detecta quando as mensagens podem ser codificadas de maneira previsível. O uso de ` Proto2Coder ` está suspenso. Recomendamos que todos os usuários mudem para ` ProtoCoder ` . 
  * Inclusão de ` withoutResultFlattening ` a ` BigQueryIO.Read ` para desativar o nivelamento dos resultados de consulta na leitura do BigQuery. 
  * Inclusão de ` BigtableIO ` para permitir leitura e gravação no Google Cloud Bigtable. 
  * ` CompressedSource ` aprimorado para detectar o formato de compactação de acordo com a extensão do arquivo. Inclusão de suporte para leitura de arquivos ` .gz ` que são descompactados de maneira transparente pela lógica de transporte subjacente. 

_Apache Beam   é uma marca registrada da The Apache Software Foundation ou
afiliadas dela nos Estados Unidos e/ou em outros países. _

##  1.4.0 (22 de janeiro de 2016)

  * Inclusão de uma série de [ exemplos de pipelines de streaming e em lote ](https://cloud.google.com/dataflow/examples/gaming-example?hl=pt_br) em um domínio de jogos para dispositivos móveis que ilustra alguns tópicos avançados, como acionadores e gestão de janelas. 
  * Inclusão de suporte para funções ` Combine ` acessarem opções de pipeline e entradas secundárias por meio de um contexto. Consulte ` GlobalCombineFn ` e ` PerKeyCombineFn ` para conferir mais detalhes. 
  * Modificação de ` ParDo.withSideInputs() ` para que chamadas sucessivas sejam cumulativas. 
  * Modificação da detecção automática de coder para mensagens do Buffer de protocolo. Agora os coders são fornecidos automaticamente para essas classes. 
  * Inclusão de suporte para limitar o número de resultados retornados por ` DatastoreIO.Source ` . No entanto, quando esse limite é definido, a operação de leitura do Cloud Datastore é realizada por um único worker, em vez de ser executada em paralelo no pool de workers. 
  * Modificação da definição de ` PaneInfo.{EARLY, ON_TIME, LATE} ` para que painéis inteiramente compostos por dados atrasados sejam sempre ` LATE ` , e que painéis ` ON_TIME ` nunca realizem cálculos atrasados para gerar um painel ` LATE ` . 
  * Modificação de ` GroupByKey ` para remover dados atrasados quando eles chegarem para uma janela que tenha expirado. Uma janela expirada é aquela cujo final ultrapassou o atraso permitido. 
  * Não é preciso mais especificar ` withAllowedLateness() ` ao usar ` GlobalWindows ` porque nenhum dado é removido. 
  * Inclusão de suporte para receber o código do projeto padrão da respectiva configuração produzida por versões mais recentes do utilitário ` gcloud ` . Se não houver uma configuração de projeto padrão, o Dataflow voltará a usar a configuração de projeto anterior gerada por versões mais antigas do utilitário ` gcloud ` . 

##  1.3.0 (4 de dezembro de 2015)

  * ` IterableLikeCoder ` aprimorado para codificar valores menores com eficiência. Essa alteração é compatível com versões anteriores. No entanto, se houver um pipeline em execução que tenha sido construído com a versão 1.3.0 ou posterior do SDK, não será possível [ "atualizar" ](https://cloud.google.com/dataflow/pipelines/updating-a-pipeline?hl=pt_br) esse pipeline com um substituto construído com a versão 1.2.1 ou anterior do SDK. Já a atualização de um pipeline em execução usando um pipeline construído com uma nova versão do SDK será bem-sucedida. 
  * Inclusão de uma etapa de refragmentação (reprodução aleatória) imediatamente antes da etapa de gravação quando ` TextIO.Write ` ou ` AvroIO.Write ` resulta em um número fixo de arquivos. O custo dessa refragmentação geralmente é excedido pelo paralelismo adicional disponível no estágio anterior. 
  * Inclusão de suporte para carimbos de data/hora RFC 3339 em ` PubsubIO ` . Isso permite a leitura de tópicos do Cloud Pub/Sub publicados pelo Cloud Logging sem perder informações de carimbos de data/hora. 
  * Melhoria no gerenciamento de memória para impedir que pipelines no modo de execução em streaming fiquem estagnados ao serem executados com alta utilização de memória. Isso beneficia principalmente os pipelines com resultados extensos de ` GroupByKey ` . 
  * Inclusão da capacidade de personalizar carimbos de data/hora de janelas emitidas. Antes, a marca d'água era mantida no carimbo de data/hora mais antigo de qualquer entrada armazenada em buffer. Com essa alteração, é possível escolher uma hora posterior para permitir que a marca d'água avance mais. Por exemplo, use o final da janela para impedir que sessões de longa duração retenham a saída. Consulte ` Window.Bound.withOutputTime() ` . 
  * Inclusão de uma sintaxe simplificada para disparos antecipados e atrasados com um acionador ` AfterWatermark ` , como indicado a seguir: ` AfterWatermark.pastEndOfWindow().withEarlyFirings(...).withLateFirings(...) ` . 

##  1.2.1 (21 de outubro de 2015)

  * Correção de uma regressão em ` BigQueryIO ` que imprimia desnecessariamente várias mensagens quando executada com ` DirectPipelineRunner ` . 

##  1.2.0 (5 de outubro de 2015)

  * Inclusão de suporte a Java 8. Inclusão de novas transformações ` MapElements ` e ` FlatMapElements ` que aceitam lambdas em Java 8, para os casos em que a capacidade total de ` ParDo ` não é necessária. ` Filter ` e ` Partition ` também aceitam lambdas. A funcionalidade do Java 8 é demonstrada em um novo exemplo de ` MinimalWordCountJava8 ` . 
  * Ativação de anotações de ` @DefaultCoder ` para tipos genéricos. Antes, a anotação de ` @DefaultCoder ` em um tipo genérico era ignorada, resultando na redução da funcionalidade e em mensagens de erro confusas. Agora ela funciona conforme esperado. 
  * ` DatastoreIO ` agora é compatível com leituras (paralelas) nos namespaces. As entidades podem ser gravadas em namespaces definindo o namespace na chave ` Entity ` . 
  * Limitação da dependência ` slf4j-jdk14 ` ao escopo ` test ` . Quando um job do Dataflow estiver em execução, as dependências ` slf4j-api ` , ` slf4j-jdk14 ` , ` jcl-over-slf4j ` , ` log4j-over-slf4j ` e ` log4j-to-slf4j ` serão fornecidas pelo sistema. 

##  1.1.0 (15 de setembro de 2015)

  * Inclusão de um coder do tipo ` Set<T> ` ao registro de coders quando o tipo ` T ` tiver seu próprio coder registrado. 
  * Inclusão de ` NullableCoder ` , que pode ser usado em conjunto com outros coders para codificar uma ` PCollection ` cujos elementos podem conter valores ` null ` . 
  * Inclusão de ` Filter ` como um ` PTransform ` composto. Suspensão do uso de métodos estáticos na implementação ` Filter ` antiga que retorna transformações ` ParDo ` . 
  * Inclusão de ` SourceTestUtils ` , que é um conjunto de infraestruturas de testes e funções auxiliares para testar a correção de implementações ` Source ` . 

##  1.0.0 (10 de agosto de 2015)

  * A versão inicial de Disponibilidade geral (GA, na sigla em inglês) é aberta para todos os desenvolvedores e considerada estável e totalmente qualificada para ser usada na produção. Ela coincide com a Disponibilidade geral do serviço do Dataflow. 
  * Remoção dos valores padrão de ` numWorkers ` , ` maxNumWorkers ` e configurações semelhantes. Se não houver especificações, o serviço do Dataflow selecionará um valor apropriado. 
  * Inclusão de verificações em ` DirectPipelineRunner ` para garantir que ` DoFn ` s atendam ao requisito de que entradas e saídas não sejam modificadas. 
  * Inclusão de suporte em ` AvroCoder ` para campos ` @Nullable ` com codificação determinística. 
  * Inclusão de um requisito para que subclasses ` CustomCoder ` anônimas modifiquem o método ` getEncodingId ` . 
  * ` Source.Reader ` , ` BoundedSource.BoundedReader ` , ` UnboundedSource.UnboundedReader ` foram alterados para serem classes abstratas, em vez de interfaces. ` AbstractBoundedReader ` foi mesclado com ` BoundedSource.BoundedReader ` . 
  * ` ByteOffsetBasedSource ` e ` ByteOffsetBasedReader ` foram renomeados como ` OffsetBasedSource ` e ` OffsetBasedReader ` , introduzindo ` getBytesPerOffset ` como uma camada de conversão. 
  * ` OffsetBasedReader ` foi alterado. Agora, a subclasse precisa modificar ` startImpl ` e ` advanceImpl ` , em vez de ` start ` e ` advance ` . A variável protegida ` rangeTracker ` agora está oculta e é atualizada pela classe base automaticamente. Para indicar pontos de divisão, use o método ` isAtSplitPoint ` . 
  * Remoção de métodos para ajustar acionadores de marca d'água. 
  * Remoção de um parâmetro genérico desnecessário de ` TimeTrigger ` . 
  * Remoção da geração de painéis vazios, a menos que explicitamente solicitado. 

##  0.4.150727 (27 de julho de 2015)

  * Remoção da necessidade de definir explicitamente ` --project ` caso o Google Cloud SDK tenha a configuração de projeto padrão definida. 
  * Inclusão de suporte para criar fontes do BigQuery com base em uma consulta. 
  * Inclusão de suporte para fontes desvinculadas personalizadas em ` DirectPipelineRunner ` e ` DataflowPipelineRunner ` . Consulte ` UnboundedSource ` para saber os detalhes. 
  * Remoção do argumento ` ExecutionContext ` desnecessário em ` BoundedSource.createReader ` e outros métodos relacionados. 
  * Alteração de ` BoundedReader.splitAtFraction ` para exigir segurança de thread (ou seja, segurança para chamadas assíncronas com ` advance ` ou ` start ` ). Inclusão de ` RangeTracker ` para implementar leitores thread-safe. É altamente recomendável que os usuários usem a classe em vez de implementar uma solução ad-hoc. 
  * Modificação de transformações ` Combine ` elevando-as para ` GroupByKey ` (e acima) e possibilitando melhor desempenho. 
  * Modificação de acionadores. Agora, após uma ` GroupByKey ` , o sistema muda para um "Acionador de continuação", que tenta preservar a finalidade original de lidar com acionamentos especulativos e atrasados, em vez de retornar ao acionador padrão. 
  * Inclusão de ` WindowFn.getOutputTimestamp ` e alteração do comportamento de ` GroupByKey ` para que janelas de sobreposição incompletas não atrasem o progresso de janelas anteriores concluídas. 
  * Alteração do comportamento de acionamento para que painéis vazios sejam produzidos se forem o primeiro painel após a marca d'água ( ` ON_TIME ` ) ou o painel final. 
  * Remoção da classe builder intermediária ` Window.Trigger ` . 
  * Inclusão da validação de que o atraso permitido seja definido em ` Window ` ` PTransform ` quando um acionador for especificado. 
  * Reativação da verificação de uso de ` GroupByKey ` . A chave precisa ter especificamente um coder determinístico, e o uso de ` GroupByKey ` com ` PCollection ` não vinculado requer acionadores ou gestão de janelas. 
  * Alteração de nomes de ` PTransform ` para que não contenham mais o caractere ` '=' ` ou ` ';' ` . 

##  0.4.150710 (10 de julho de 2015)

  * Inclusão de suporte no ` BigQueryIO ` para tabelas por janela. 
  * Inclusão de suporte para uma implementação de fonte personalizada do Avro. Consulte ` AvroSource ` para saber mais detalhes. 
  * Remoção da restrição de tamanho de 250 GiB para upload de arquivo do Google Cloud Storage. 
  * Correção do bug na criação de tabela ` BigQueryIO.Write ` no modo de streaming. 
  * ` Source.createReader() ` e ` BoundedSource.createReader() ` foram alterados para serem abstratos. 
  * ` Source.splitIntoBundles() ` foi movido para ` BoundedSource.splitIntoBundles() ` . 
  * Inclusão de suporte para leitura de exibições limitadas de um stream do Pub/Sub em ` PubsubIO ` para ` DataflowPipeline ` s e ` DirectPipeline ` s sem streaming. 
  * Inclusão de suporte para receber um ` Coder ` usando uma ` Class ` para o ` CoderRegistry ` . 
  * Alteração de ` CoderRegistry.registerCoder(Class<T>, Coder<T>) ` para impor que o coder fornecido realmente codifique valores da classe fornecida. É proibido utilizá-lo com rawtypes de classes genéricas porque ele dificilmente funcionará corretamente. 
  * Migração para ` Create.withCoder() ` e ` CreateTimestamped.withCoder() ` , em vez de chamar ` setCoder() ` na ` PCollection ` de saída quando a ` Create ` ` PTransform ` estiver sendo aplicada. 
  * Inclusão de três exemplos sucessivos de ` WordCount ` mais detalhados. 
  * Remoção de ` PTransform.getDefaultName() ` , que era redundante com ` PTransform.getKindString() ` . 
  * Inclusão de suporte para verificação de nome exclusivo de ` PTransform ` durante a criação de jobs. 
  * Remoção de ` PTransform.withName() ` e ` PTransform.setName() ` . Agora, o nome de uma transformação é imutável após a construção. Transformações de biblioteca (como ` Combine ` ) podem fornecer métodos parecidos com builder para alterar o nome. Sempre é possível modificar os nomes no local em que a transformação é aplicada usando ` apply("name", transform) ` . 
  * Inclusão da capacidade de selecionar a rede para VMs de worker usando ` DataflowPipelineWorkerPoolOptions.setNetwork(String) ` . 

##  0.4.150602 (2 de junho de 2015)

  * Inclusão de uma dependência na versão 2015.02.05 ou posterior do componente ` [ gcloud ](https://cloud.google.com/sdk/gcloud/?hl=pt_br) core ` . Atualize para a versão mais recente de ` gcloud ` executando ` gcloud components update ` . Consulte o [ Application Default Credentials ](https://developers.google.com/accounts/docs/application-default-credentials?hl=pt_br) para ver mais detalhes sobre como especificar credenciais. 
  * Remoção de ` Flatten.create() ` , cujo uso estava suspenso. Use ` Flatten.pCollections() ` . 
  * Remoção de ` Coder.isDeterministic() ` , cujo uso estava suspenso. Implemente ` Coder.verifyDeterministic() ` . 
  * Substituição de ` DoFn.Context#createAggregator ` por ` DoFn#createAggregator ` . 
  * Inclusão de suporte para consultar o valor atual de um ` Aggregator ` . Veja ` PipelineResult ` para conferir mais informações. 
  * Inclusão de ` DoFnWithContext ` experimental para simplificar o acesso a informações adicionais de um ` DoFn ` . 
  * Remoção de ` RequiresKeyedState ` experimental. 
  * Inclusão de ` CannotProvideCoderException ` para indicar incapacidade de inferir um coder, em vez de retornar ` null ` nesses casos. 
  * Inclusão de ` CoderProperties ` para montar pacotes de teste para coders definidos pelo usuário. 
  * Substituição de um construtor de ` PDone ` por um ` PDone.in(Pipeline) ` estático de fábrica. 
  * Atualização da formatação de string dos valores ` TIMESTAMP ` retornados pela fonte do BigQuery ao usar ` DirectPipelineRunner ` ou quando os dados do BigQuery são utilizados como entrada secundária. Isso alinha a formatação ao uso de maiúsculas/minúsculas quando os dados do BigQuery são utilizados como entrada principal. 
  * Inclusão do requisito para que o valor retornado por ` Source.Reader.getCurrent() ` seja imutável e permaneça válido indefinidamente. 
  * Substituição de alguns usos de ` Source ` por ` BoundedSource ` . Por exemplo, agora a transformação ` Read.from() ` só pode ser aplicada a objetos ` BoundedSource ` . 
  * O gerenciamento experimental de dados atrasados (ou seja, os dados que chegam ao pipeline de streaming depois que a marca d'água foi transmitida) foi movido de ` PubSubIO ` para ` Window ` . Por padrão, os dados atrasados serão removidos na primeira ` GroupByKey ` após uma operação ` Read ` . Para permitir dados atrasados, use ` Window.Bound#withAllowedLateness ` . 
  * Inclusão de suporte experimental para acumular elementos em uma janela entre painéis. 

##  0.4.150414 (14 de abril de 2015)

  * Versão Beta inicial do SDK do Dataflow para Java. 
  * Melhor desempenho de execução em várias áreas do sistema. 
  * Inclusão de suporte para estimativa de progresso e rebalanceamento dinâmico de trabalho de fontes definidas pelo usuário. 
  * Inclusão de suporte para que fontes definidas pelo usuário forneçam o carimbo de data/hora dos valores lidos por meio de ` Reader.getCurrentTimestamp() ` . 
  * Inclusão de suporte para coletores definidos pelo usuário. 
  * Inclusão de suporte para tipos personalizados em ` PubsubIO ` . 
  * Inclusão de suporte para leitura e gravação de arquivos XML. Veja ` XmlSource ` e ` XmlSink ` . 
  * Renomeação de ` DatastoreIO.Write.to ` para ` DatastoreIO.writeTo ` . Além disso, as entidades gravadas no Cloud Datastore precisam ter chaves completas. 
  * Renomeação da transformação ` ReadSource ` para ` Read ` . 
  * Substituição de ` Source.createBasicReader ` por ` Source.createReader ` . 
  * Inclusão de suporte para acionadores, o que possibilita receber resultados antecipados ou parciais de uma janela e especificar quando processar dados atrasados. Veja ` Window.into.triggering ` . 
  * Redução da visibilidade de ` getInput() ` , ` getOutput() ` , ` getPipeline() ` e ` getCoderRegistry() ` da ` PTransform ` . Esses métodos serão excluídos em breve. 
  * Renomeação de ` DoFn.ProcessContext#windows ` para ` DoFn.ProcessContext#window ` . Para um ` DoFn ` chamar ` DoFn.ProcessContext#window ` , é preciso implementar ` RequiresWindowAccess ` . 
  * Inclusão de ` DoFn.ProcessContext#windowingInternals ` para ativar a gestão de janelas em executores terceirizados. 
  * Inclusão de suporte para entradas secundárias ao executar pipelines de streaming em ` [Blocking]DataflowPipelineRunner ` . 
  * Alteração de ` [Keyed]CombineFn.addInput() ` para retornar o novo valor do acumulador. Renomeação de ` Combine.perElement().withHotKeys() ` para ` Combine.perElement().withHotKeyFanout() ` . 
  * Renomeação de ` First.of ` para ` Sample.any ` e de ` RateLimiting ` para ` IntraBundleParallelization ` , para representar melhor a funcionalidade dela. 

##  0.3.150326 (26 de março de 2015)

  * Inclusão de suporte para acessar ` PipelineOptions ` no worker do Dataflow. 
  * Remoção de um dos parâmetros de tipo em ` PCollectionView ` , o que pode exigir alterações simples no código do usuário que usa ` PCollectionView ` . 
  * Alteração da API de entrada secundária para aplicação por janela. Agora, as chamadas a ` sideInput() ` retornam valores somente na janela específica que corresponde à janela do elemento de entrada principal, e não na ` PCollectionView ` inteira de entrada secundária. Consequentemente, ` sideInput() ` não pode mais ser chamada de ` startBundle ` e ` finishBundle ` de um ` DoFn ` . 
  * Inclusão de suporte para exibir uma ` PCollection ` como um ` Map ` quando usada como entrada secundária. Veja ` View.asMap() ` . 
  * Renomeação de API de origem personalizada para usar o termo "bundle" em lugar de "shard" em todos os nomes. Além disso, o termo "fork" foi substituído por "dynamic split". 
  * Agora, o ` Reader ` de origem personalizada exige a implementação do novo método ` start() ` . Para corrigir o código existente, basta adicionar esse método que apenas chama ` advance() ` e retorna respectivo valor dele. Além disso, o código que usa ` Reader ` será atualizado para utilizar ` start() ` e ` advance() ` , em vez de usar somente ` advance() ` . 

##  0.3.150227 (27 de fevereiro de 2015)

  * Versão Alpha inicial do SDK do Dataflow para Java com suporte para pipelines de streaming. 
  * Inclusão do verificador determinístico em ` AvroCoder ` para facilitar a interoperação com ` GroupByKey ` . 
  * Inclusão de suporte para acessar ` PipelineOptions ` no worker. 
  * Inclusão de suporte para fontes compactadas. 

##  0.3.150211 (11 de fevereiro de 2015)

  * Remoção da dependência na versão 2015.02.05 ou mais recente do componente ` gcloud core ` . 

##  0.3.150210 (11 de fevereiro de 2015)

_**Cuidado:** depende da versão 2015.02.05 ou posterior do componente ` gcloud
core ` . _

  * Inclusão do executor de pipeline de streaming que, por enquanto, requer uma lista de permissões adicional. 
  * Renomeação de várias APIs relacionadas à gestão de janelas de modo não compatível com versões anteriores. 
  * Inclusão de suporte para fontes personalizadas, que você pode usar para ler nos seus próprios formatos de entrada. 
  * Introdução do paralelismo de worker: uma tarefa por processador. 

##  0.3.150109 (10 de janeiro de 2015)

  * Correção de vários problemas específicos de plataforma para o Microsoft Windows. 
  * Correção de vários problemas específicos do Java 8. 
  * Inclusão de alguns novos exemplos. 

##  0.3.141216 (16 de dezembro de 2014)

  * Versão alfa inicial do SDK do Dataflow para Java. 

