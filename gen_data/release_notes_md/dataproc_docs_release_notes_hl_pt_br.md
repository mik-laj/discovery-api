Notas da versão

Estas notas da versão aplicam-se ao serviço Cloud Dataproc principal. Você
pode consultar esta página periodicamente para ver anúncios sobre recursos
novos ou atualizados, correções de bugs, problemas conhecidos e
funcionalidades com uso suspenso.

Consulte a [ Lista das versões do Cloud Dataproc
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions?hl=pt_br) para ver os componentes de software atuais e anteriores
compatíveis com as imagens de software usadas nas máquinas virtuais do Cloud
Dataproc.

O Cloud Dataproc lança uma nova versão a cada semana, com uma janela de
distribuição de quatro dias a partir de terça-feira.

[ Inscreva-se nas notas da versão do Cloud Dataproc. ![Inscrever-
se](https://cloud.google.com/images/feed-icon.png?hl=pt_br)
](https://cloud.google.com/feeds/cloud-dataproc-release-notes.xml?hl=pt_br)

**Lançamentos em etapas** : as versões do Cloud Dataproc ocorrem em etapas ao
longo de quatro dias. Publicamos essas notas da versão no primeiro dia do
lançamento.

##  Observações importantes sobre atualização cruzada

**ISSUE:**

  * No futuro, o Cloud Dataproc será migrado de diversos repositórios do GitHub para o material do Cloud Dataproc, como [ ações de inicialização ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/) e [ documentação ](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/dataproc) neste [ repositório consolidado ](https://github.com/GoogleCloudPlatform/cloud-dataproc) . Isso facilitará a localização de todos os materiais relacionados ao Cloud Dataproc no GitHub. Durante a migração e por um período depois dela, o conteúdo ficará disponível nos dois locais. 
  * A partir de 04/01/2019, o [ Cloud Dataproc 1.3 ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) será a versão padrão para novos clusters. 

##  4 de dezembro de 2018

**FEATURE:**

  * Anúncio da versão [ Beta ](https://cloud.google.com/terms/launch-stages?hl=pt_br#launch-stages) de [ jobs do SparkR no Cloud Dataproc ](https://cloud.google.com/dataproc/docs/reference/rest/v1beta2/projects.regions.jobs?hl=pt_br#SparkRJob) . Esse recurso permite enviar jobs do [ SparkR ](https://spark.apache.org/docs/latest/sparkr.html) em um cluster do Cloud Dataproc usando a ferramenta de linha de comando ` gcloud ` , o Console do Google Cloud Platform ou a API Cloud Dataproc. 
  * Anúncio da versão de [ Disponibilidade geral (GA, na sigla em inglês) ](https://cloud.google.com/terms/launch-stages?hl=pt_br#launch-stages) de [ SSDs locais do Cloud Dataproc em trabalhos preemptivos ](https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-local-ssds?hl=pt_br) . [ SSDs locais ](https://cloud.google.com/compute/docs/disks/local-ssd?hl=pt_br) já podem ser adicionados a nós de trabalho preemptivos (secundários) em um cluster. 

##  16 de novembro de 2018

**FEATURE:**

  * Anúncio da versão [ Beta ](https://cloud.google.com/terms/launch-stages?hl=pt_br#launch-stages) do [ Cloud Dataproc: componente de nível superior Presto ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/optional-components?hl=pt_br#presto) . Esse recurso permite que os usuários instalem o [ Presto ](https://prestodb.io) ao criar novos clusters do Cloud Dataproc. 

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.102-deb9, 1.1.93-deb9, 1.2.56-deb9, 1.3.16-deb9 ` . 
  * A criação de clusters do Dataproc agora emitirá um aviso se detectarmos uma vulnerabilidade de segurança em potencial por causa de regras de firewall configuradas incorretamente, permitindo acesso público a portas YARN. 
  * A pesquisa dos detalhes de um job mostrará quem enviou esse job no campo submittedBy. 
  * Somente imagem 1.3: 
    * Upgrade do Conector do Cloud Storage para a versão 1.9.10. Consulte as [ notas da versão do GitHub ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.9.10) . 

##  12 de novembro de 2018

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.101-deb9, 1.1.92-deb9, 1.2.55-deb9, 1.3.15-deb9 ` . 
  * As versões de imagem secundárias agora redirecionam para imagens baseadas no Debian 9. Por exemplo, 1.2 agora aponta para 1.2-deb9. Não haverá novas imagens baseadas no Debian 8. 
  * Os UUIDs de job agora são expostos para permitir que as execuções de job sejam identificadas de maneira exclusiva. 
  * O conector do Cloud Storage agora define ` fadvise ` como ` SEQUENTIAL ` para jobs do Hadoop DistCp. Esse modo é otimizado para leituras de streaming, que são mais eficientes para essas cargas de trabalho. 
  * Remoção do jar de inicialização ALPN de versões do Cloud Dataproc 1.0 e 1.1 por causa da incompatibilidade com o OpenJDK 8 mais recente distribuído com o Debian. Os usuários do gRPC precisam usar uma forma de ` netty-tcnative ` . Por exemplo, ` io.grpc:grpc-netty-shaded ` . Isso já se aplica a 1.2 e 1.3. 
  * Redução da prioridade do processo Linux de jobs do usuário. 
  * ` dfs.namenode.datanode.registration.retry-hostname-dns-lookup ` já está definido como ` true ` . 
  * Aumento do número máximo de tarefas DistCp programadas por nó. Isso melhora o desempenho de DistCp. 
  * Somente imagem 1.3: 
    * Portação de [ HDFS-13056 ](https://issues.apache.org/jira/browse/HDFS-13056) para Hadoop 2.9. 
    * Upgrade do Conector do Cloud Storage para a versão 1.9.9. Consulte as [ notas da versão do GitHub ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.9.9) . 
    * O Presto já é compatível como um componente de nível superior opcional. 

**FIXED:**

  * Correção de um bug em que o CMEK não foi passado para PD em trabalhos preemptivos. 
  * Correção de um bug em que alterações feitas em ` PATH ` em imagens personalizadas interrompiam a inicialização do Cloud Dataproc. Por exemplo, alterar o Python padrão para o Python 3 interrompia a inicialização. 
  * Correção de um bug em que solicitações POST e PUT para a API REST YARN eram bloqueadas por usuários anônimos no Cloud Dataproc 1.3. Isso foi corrigido com adição de ` org.apache.hadoop.http.lib.StaticUserWebFilter ` de volta para ` hadoop.http.filter.initializers ` em ` core-site.xml `
  * Correção de avisos do registro em log no Hive 2 no Cloud Dataproc 1.1, 1.2 e 1.3. 

##  2 de novembro de 2018

**ISSUE:**

Desde 2 de novembro de 2018, o Cloud Dataproc parou de lançar imagens baseadas
no Debian 8. As versões 1.X depois de 2 de novembro de 2018 usarão o Debian 9
como o SO base delas. Não serão lançadas atualizações adicionais, patches ou
correções de segurança para o Debian 8 depois 2 de novembro de 2018.

**ISSUE:**

Em 9 de novembro de 2018, o jar de inicialização ALPN será removido do caminho
de classe de imagens futuras do Cloud Datproc versão 1.0 e 1.1 por causa de
incompatibilidades com os patches de segurança mais recentes do pacote do
Debian OpenJDK 8. As versões 1.2 e 1.3 da imagem serão clientes Java gRPC e
precisarão usar [ netty-tcnative ](https://github.com/grpc/grpc-
java/blob/master/SECURITY.md#tls-with-openssl) na autenticação com APIs do
Google. Os clientes, como o Cloud Bigtable que agrupam netty-tcnative podem
depender de [ grpc-netty-shaded
](https://search.maven.org/artifact/io.grpc/grpc-netty-shaded/1.16.1/jar) para
evitar colisões com o Hadoop Classpath. Consulte [ Gerenciar dependências Java
e Scala do Apache Spark
](https://cloud.google.com/dataproc/docs/guides/manage-spark-
dependencies?hl=pt_br) para saber mais informações.

##  26 de outubro de 2018

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.100-deb8, 1.1.91-deb8, 1.2.54-deb8, 1.3.14-deb8, 1.0.100-deb9, 1.1.91-deb9, 1.2.54-deb9, 1.3.14-deb9 ` . 

**FIXED:**

  * Correção de um problema de [ Desativação otimizada e funcionários secundários ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/scaling-clusters?hl=pt_br#graceful_decommissioning_and_secondary_workers) . Durante o uso da desativação otimizada para remover trabalhos secundários (preemptivos) logo após o escalonamento do grupo de trabalhos secundários, um erro ocorreria com uma mensagem de erro semelhante à seguinte: "O grupo de trabalhos secundários não pode ser modificado fora do Cloud Dataproc. Se você tiver criado ou atualizado este cluster recentemente, espere alguns minutos antes da desativação otimizada para permitir que todas as instâncias secundárias participem do cluster ou saiam dele. Tamanho do grupo de trabalhos secundário esperado: x, tamanho real: y."   
**Informações relacionadas:**

    * O Cloud Dataproc chama ` listManagedInstances ` no grupo de instâncias gerenciadas que administra trabalhos secundários, filtra instâncias com ação atual EXCLUSÃO ou ABANDONO e escolhe as instâncias a serem excluídas do grupo resultante. O Cloud Dataproc prefere excluir VMs que estejam sendo criadas, em vez de executar VMs. 
    * Durante a descrição de um cluster, o grupo de trabalhos secundário continuará sendo exibido para que tenham instâncias EXCLUSÃO e ABANDONO. Por isso, o tamanho de destino do grupo talvez não corresponda ao tamanho da lista de nomes do host, mesmo após a conclusão da operação do escalonamento. As instâncias serão removidas da lista quando forem excluídas do grupo de instâncias gerenciadas. 
  * Correção de problemas que levavam a um "erro interno do servidor" durante a criação de clusters. 

##  22 de outubro de 2018

**FEATURE:**

  * O Cloud Dataproc já está disponível na [ região ](https://cloud.google.com/compute/docs/regions-zones/regions-zones?hl=pt_br#available) ` asia-east2 ` (Hong Kong). 

##  19 de outubro de 2018

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.99-deb8, 1.1.90-deb8, 1.2.53-deb8, 1.3.13-deb8, 1.0.99-deb9, 1.1.90-deb9, 1.2.53-deb9, 1.3.13-deb9 ` . 

**FIXED:**

  * Somente imagem 1.0: correção de um bug em que as métricas do Stackdriver não estavam sendo publicadas, o que também afetava a funcionalidade de escalonamento automático. 

##  12 de outubro de 2018

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.98-deb8, 1.1.89-deb8, 1.2.52-deb8, 1.3.12-deb8, 1.0.98-deb9, 1.1.89-deb9, 1.2.52-deb9, 1.3.12-deb9 ` . 
  * Somente imagem 1.3: upgrade do conector do Cloud Storage. Para saber mais informações, consulte [ observações de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.9.8) no repositório do GitHub: 
    * O conector do Cloud Storage foi atualizado para a versão 1.9.8. 
  * Somente imagem 1.0: upgrade do Hadoop para 2.7.4. 

##  9 de outubro de 2018

**FEATURE:**

  * Anúncio da versão [ General Availability (GA) ](https://cloud.google.com/terms/launch-stages?hl=pt_br#launch-stages) de [ Chaves de criptografia gerenciadas pelo cliente do Cloud Dataproc no Compute Engine ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/customer-managed-encryption?hl=pt_br) . Esse recurso permite criar, usar e revogar a [ Key Encryption Key (KEK) ](https://cloud.google.com/security/encryption-at-rest?hl=pt_br) em discos permanentes (PDs, na sigla em inglês) associados a VMs do Compute Engine no cluster. 

##  5 de outubro de 2018

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.97-deb8, 1.1.88-deb8, 1.2.51-deb8, 1.3.11-deb8, 1.0.97-deb9, 1.1.88-deb9, 1.2.51-deb9, 1.3.11-deb9 ` . 
  * Somente imagem 1.1: upgrade do Zeppelin para 0.7.3. 
  * Somente imagem 1.1: publicação das métricas YARN e HDFS para o Stackdriver, exceto PendingDeletionBlocks HDFS, de clusters usando a versão da imagem 1.1.82 e posteriores. 

**FIXED:**

  * Correção de um problema em que o tempo limite da primeira ação de inicialização era usado como o tempo limite em todas as outras ações de inicialização. 
  * Correção do problema incomum em que a criação do cluster falhou com o erro ` debconf: DbDriver "config": /var/cache/debconf/config.dat is locked by another process: Resource temporarily unavailable ` . 

##  28 de setembro de 2018

**FEATURE:**

  * Recurso (1.2+): ativação da nova [ propriedade de cluster ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/cluster-properties?hl=pt_br) ` dataproc:am.primary_only ` para evitar a execução do mestre do aplicativo em trabalhos preemptivos. Esse recurso só é ativado para clusters do Dataproc 1.2+. Para usar a propriedade do cluster, defina ` --properties dataproc:am.primary_only=true ` ao criar um cluster. 

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.97-deb8, 1.1.88-deb8, 1.2.51-deb8, 1.3.11-deb8, 1.0.97-deb9, 1.1.88-deb9, 1.2.51-deb9, 1.3.11-deb9 ` . 
  * Somente imagem 1.3: upgrade do conector do Cloud Storage. Para saber mais informações, consulte [ observações de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.9.7) no repositório do GitHub: 
    * O conector do Cloud Storage foi atualizado para a versão 1.9.7. 
  * Somente imagem 1.0-1.2: upgrades dos conectores do Cloud Storage e do BigQuery. Para saber mais informações, consulte [ observações de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.6.10) no repositório do GitHub: 
    * O conector do Cloud Storage foi atualizado para a versão 1.6.10. 
    * O conector do BigQuery foi atualizado para a versão 0.10.11. 

**FIXED:**

  * Correção do problema em que o servidor de histórico do Spark falhava na inicialização. 
  * Correção do problema em que o escalonamento automático para após 1.000 períodos de refrigeração. 

##  25 de setembro de 2018

**FEATURE:**

  * Anúncio da versão [ General Availability (GA) ](https://cloud.google.com/terms/launch-stages?hl=pt_br#launch-stages) de [ Modelos do fluxo de trabalho do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/workflows/overview?hl=pt_br) , inclusive [ Parametrização do modelo do fluxo de trabalho ](https://cloud.google.com/dataproc/docs/concepts/workflows/workflow-parameters?hl=pt_br) e a [ API Workflow Templates InstantiateInline ](https://cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.workflowTemplates/instantiateInline?hl=pt_br) . 
  * Anúncio da versão [ General Availability (GA) ](https://cloud.google.com/terms/launch-stages?hl=pt_br#launch-stages) do [ IAM granular do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/iam/granular-iam?hl=pt_br) . Esse recurso permite definir papéis do IAM e as permissões correspondentes deles por cluster. 
  * Anúncio da versão [ Beta ](https://cloud.google.com/terms/launch-stages?hl=pt_br#launch-stages) de [ Importação/exportação do cluster de YAML ](https://cloud.google.com/dataproc/docs/guides/create-cluster?hl=pt_br#creating_a_dataproc_name_short_cluster) do Cloud Dataproc. Este recurso permite usar a ferramenta de linha de comando gcloud para exportar a configuração de um cluster do Cloud Dataproc atual para um arquivo YAML e criar um novo cluster importando a configuração do arquivo YAML. 
  * Anúncio da versão [ Beta ](https://cloud.google.com/terms/launch-stages?hl=pt_br#launch-stages) de [ Componentes opcionais ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/optional-components?hl=pt_br) do Cloud Dataproc. Com esse recurso, é possível especificar outros componentes para a instalação durante a criação de novos clusters do Cloud Dataproc. 

##  21 de setembro de 2018

**FEATURE:**

  * Anúncio da ação de inicialização [ Beam on Flink on Dataproc ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/blob/master/beam/) ( [ Beta ](https://cloud.google.com/terms/launch-stages?hl=pt_br#launch-stages) ) no GitHub, que configura o serviço Apache Beam em um cluster do Cloud Dataproc. 

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.95-deb8, 1.1.86-deb8, 1.2.49-deb8, 1.3.9-deb8, 1.0.95-deb9, 1.1.86-deb9, 1.2.49-deb9, 1.3.9-deb9 ` . 
  * Alteração das ações de inicialização a serem executadas dentro de um shell de login. Dessa maneira, as alterações feitas no perfil do ambiente podem ser vistas por ações init subsequentes. 
  * Somente imagem 1.3: upgrade do conector do Cloud Storage. Para saber mais informações, consulte [ observações de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.9.6) no repositório do GitHub: 
    * O conector do Cloud Storage foi atualizado para a versão 1.9.6. 
  * Somente imagem 1.0-1.2: upgrades dos conectores do Cloud Storage e do BigQuery. Para saber mais informações, consulte [ observações de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.6.9) no repositório do GitHub: 
    * O conector do Cloud Storage foi atualizado para a versão 1.6.9. 
    * O conector do BigQuery foi atualizado para a versão 0.10.10. 

**FIXED:**

  * Correção do problema em que os clientes baseados em gRPC podem falhar durante a chamada Receber/listar em operações após o uso da API v1beta2 para realizar operações de cluster. 

##  14 de setembro de 2018

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.94-deb8, 1.1.85-deb8, 1.2.48-deb8, 1.3.8-deb8, 1.0.94-deb9, 1.1.85-deb9, 1.2.48-deb9, 1.3.8-deb9 ` . 
  * Adição de ` Flink 1.5.0 ` e ` HBase 1.3.2 ` a imagens ` 1.3-deb8 ` . 

**FIXED:**

  * Aprimoramento de granularidade e precisão das métricas do Hadoop. 
  * Correção do problema de falha do serviço Hue ao iniciar em imagens ` 1.3-deb9 ` . 

##  31 de agosto de 2018

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.93-deb8, 1.1.84-deb8, 1.2.47-deb8, 1.3.7-deb8, 1.0.93-deb9, 1.1.84-deb9, 1.2.47-deb9, 1.3.7-deb9 ` . 

**FIXED:**

  * Correção do problema que impedia trabalhos de ingressar no cluster durante o uso da [ ação init de conectores ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/tree/master/connectors) . 
  * Correção do problema que provocava a falha dos jobs do Hive quando enviados durante o primeiro minuto após a criação do cluster. 
  * Correção do mau funcionamento das ações de inicialização por causa do erro ` E: Could not get lock /var/lib/dpkg/lock ` . 

##  30 de agosto de 2018

**FEATURE:**

  * Anúncio da versão de [ disponibilidade geral (GA, na sigla em inglês) ](https://cloud.google.com/terms/launch-stages?hl=pt_br#launch-stages) das [ chaves de criptografia gerenciadas pelo cliente do Cloud Dataproc no Cloud Storage ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/customer-managed-encryption?hl=pt_br) . Esse recurso permite criar, usar e revogar a [ chave de criptografia de chaves (KEK, na sigla em inglês) ](https://cloud.google.com/security/encryption-at-rest?hl=pt_br) no intervalo do Cloud Storage usado pelo Cloud Dataproc para gravar metadados de cluster e a saída do driver do job. 

##  24 de agosto de 2018

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.92-deb8, 1.1.83-deb8, 1.2.46-deb8, 1.3.6-deb8, 1.0.92-deb9, 1.1.83-deb9, 1.2.46-deb9, 1.3.6-deb9 ` . 
  * Somente imagem 1.0-1.2: upgrades dos conectores do Cloud Storage e do BigQuery. Para saber mais informações, consulte [ observações de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.6.8) no repositório do GitHub: 
    * O conector do Cloud Storage foi atualizado para a versão 1.6.8. 
    * O conector do BigQuery foi atualizado para a versão 0.10.9. 
  * Somente imagem 1.3: upgrade do conector do Cloud Storage para a versão 1.9.5. Para saber mais informações, consulte [ observações de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.9.5) no repositório do GitHub. 
  * Imagem 1.3 apenas com o Debian 9: 
    * Atualize o Spark para 2.3.1. 
    * Adicione o HBase 1.3.2. 
    * Adicione o Flink 1.5.0. 

**FIXED:**

  * Correção do [ problema ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/pull/313) no Dataproc imagem versão 1.2, em que JARs ASM conflitantes podem causar uma falha no Zeppelin. 
  * Correção do problema no Dataproc imagem versão 1.3, em que a compressão do Snappy no formato de arquivo ORC no Spark foi interrompida. Essa foi uma regressão introduzida na imagem versão 1.3.3, enquanto resolvia o [ SPARK-24018 ](https://issues.apache.org/jira/browse/SPARK-24018) . Após essa correção, o Parquet e o ORC podem usar a compressão do Snappy. 

##  16 de agosto de 2018

**FEATURE:**

  * Há novas imagens baseadas no Debian 9 para as versões de imagens 1.0-1.3. Elas podem ser acessadas anexando '-deb9" às faixas de versão existentes (por exemplo, 1.2-deb9). 
  * Até 2 de novembro de 2018, as versões de imagens 1.X atuais usarão imagens do Debian 8 (por exemplo, 1.3 será resolvido para 1.3.Y-deb8). Em 2 de novembro de 2018, as versões de imagens 1.X mudarão para imagens do Debian 9. O Debian 8 não será usado em novas versões de imagens a partir de 2 de novembro de 2018. 

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.91-deb8, 1.0.91-deb9, 1.1.82-deb8, 1.1.82-deb9, 1.2.45-deb8, 1.2.45-deb9, 1.3.5-deb8, 1.3.5-deb9 ` . 
  * Correção de segurança: instale o Linux Kernel 4.9 em todas as versões de imagens para receber correções de segurança para [ CVE-2018-3590 ](https://security-tracker.debian.org/tracker/CVE-2018-3590) e [ CVE-2018-3591 ](https://security-tracker.debian.org/tracker/CVE-2018-3591) em todas as novas imagens do Debian 8. 

##  10 de agosto de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.90, 1.1.81, 1.2.45, 1.3.5 ` . 
  * Definição do número máximo de arquivos abertos como 65535 para todos os serviços Systemd. 

##  3 de agosto de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.89, 1.1.80, 1.2.44, 1.3.4 ` . 
  * Nos clusters de alta disponibilidade (HA, na sigla em inglês), ` hadoop.security.token.service.use_ip ` está agora definido como "false". 
  * Atualização do Hadoop para 2.8.4. (Dataproc 1.2) 

**FIXED:**

  * Correção do problema de falha em que jobs do Hive falhariam em clusters 1.3 HA 
  * Correção do valor padrão de ` mapreduce.jobhistory.recovery.store.fs.uri ` com a definição novamente como ` ${hadoop.tmp.dir}/mapred/history/recoverystore ` . Ele havia sido configurado por engano para ` hdfs:///mapred/history/recoverystore ` na versão de 6 de julho. 
  * Backports de [ ZOOKEEPER -1576 ](https://issues.apache.org/jira/browse/ZOOKEEPER-1576) no ZooKeeper 3.4.6 no Dataproc 1.2 e 1.3. Esse bug causava falha nas conexões do Zookeper caso algum dos servidores falhasse na resolução. 

##  31 de julho de 2018

**FEATURE:**

  * Anúncio de [ Escalonamento automático do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling?hl=pt_br) (Alfa público). Esse recurso redimensiona automaticamente os clusters para atender às demandas de cargas de trabalho. 

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.3.3 ` . 
  * Houve alterações apenas na imagem do 1.3: 

**CHANGED:**

    * Desativação da adição de nós à lista negra em jobs do Tez (conjunto ` tez.am.node-blacklisting.enabled=false ` ). Isso afeta todos os jobs do Hive, que são executados no Tez por padrão. 

**FIXED:**

    * Correção do problema de quebra de compactação nativa do Snappy nativa no spark-shell ( [ SPARK-24018 ](https://issues.apache.org/jira/browse/SPARK-24018) ) e no [ Zeppelin ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/issues/289) . 
    * Correção do problema que impedia que gsutil e gcloud funcionassem em VMs de cluster quando o componente opcional ANACONDA era selecionado. 

##  18 de julho de 2018

**FEATURE:**

  * Anunciamos o recurso [ parâmetros de fluxo de trabalho do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/workflows/workflow-parameters?hl=pt_br) (Beta). Com esse recurso, é possível reutilizar os modelos de fluxo de trabalho do Cloud Dataproc diversas vezes com parâmetros diferentes. Como parte do lançamento desse recurso, os usuários podem [ importar e exportar modelos de fluxo de trabalho diretamente de arquivos YAML ](https://cloud.google.com/dataproc/docs/concepts/workflows/overview?hl=pt_br#using_workflow_template_yaml_files) usando a ferramenta de linha de comando ` gcloud ` . 

##  13 de julho de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.88, 1.1.79, 1.2.43, 1.3.2 ` . 
  * Com o Cloud Dataproc, agora o local de recursos é adicionado aos registros de auditoria gerados na nuvem. 

##  10 de julho de 2018

**FEATURE:**

  * O Cloud Dataproc agora está disponível na [ região ](https://cloud.google.com/compute/docs/regions-zones/regions-zones?hl=pt_br#available) ` us-west2 ` (Los Angeles). 

##  6 de julho de 2018

**FEATURE:**

  * Anunciamos a versão alfa dos [ componentes opcionais ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/optional-components?hl=pt_br) do Cloud Dataproc. Com esse recurso, é possível especificar outros componentes para a instalação ao criar novos clusters do Dataproc. 

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.87, 1.1.78, 1.2.42, 1.3.1 ` . 
  * Houve alterações apenas na imagem do 1.3: 
    * A IU da Web Spark por driver foi reativada. 
    * A biblioteca do HCatalog é instalada por padrão. 
  * A recuperação do servidor do histórico de jobs do MapReduce agora está ativada por padrão. 

**FIXED:**

  * Uma condição de corrida na criação do cluster de alta disponibilidade com o utilitário resolveip foi resolvida. 

##  29 de junho de 2018

**FEATURE:**

  * Cloud Dataproc 1.3: uma nova versão da imagem do Cloud Dataproc já está disponível. 
    * A versão 1.3 da imagem passará a ser a versão de imagem padrão para novos clusters a partir de 30/07/2018. Consulte a [ lista de versões do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) para mais informações. 
A versão 1.3 da imagem inclui as seguintes alterações:

    * O Apache Spark foi atualizado para a versão 2.3.0. 
    * O Apache Hadoop foi atualizado para a versão 2.9.0. 
    * O Apache Hive foi atualizado para a versão 2.3.2. 
    * O Hive é executado no Apache Tez por padrão. 
    * O [ YARN Timeline Server ](http://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/TimelineServer.html) está ativado por padrão. 
  * Anunciamos a versão de disponibilidade geral (GA, na sigla em inglês) das [ imagens personalizadas ](https://cloud.google.com/dataproc/docs/guides/dataproc-images?hl=pt_br) do Cloud Dataproc, anteriormente Beta. Com esse recurso, os usuários criam e salvam imagens personalizadas com pacotes pré-instalados. As imagens personalizadas são usadas para criar clusters do Cloud Dataproc. 

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.86, 1.1.77, 1.2.41, 1.3.0 ` . 
  * Houve alterações apenas na imagem do 1.3: 
    * O conector do Cloud Storage foi atualizado para a versão 1.9.0. Consulte as [ notas de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.9.0) no repositório do GitHub. 
    * O servidor Kernel NFS não está mais instalado. 

##  27 de junho de 2018

**FEATURE:**

  * Anúncio da versão Beta das [ chaves de criptografia gerenciadas pelo cliente (CMEK, na sigla em inglês) do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/customer-managed-encryption?hl=pt_br) , um recurso que permite usar e revogar a [ chave de criptografia de chaves (KEK, na sigla em inglês) ](https://cloud.google.com/security/encryption-at-rest/default-encryption?hl=pt_br#key_management) para VMs do Compute Engine no cluster e para o intervalo do Cloud Storage usado com o Cloud Dataproc. 
  * Anúncio da disponibilização geral (GA) do Cloud Dataproc e das chaves de criptografia gerenciadas pelo cliente no BigQuery. Os usuários do Cloud Dataproc já podem usar [ chaves de criptografia gerenciadas pelo cliente (CMEK, na sigla em inglês) ](https://cloud.google.com/bigquery/docs/customer-managed-encryption?hl=pt_br) para acesso a conjuntos de dados e tabelas protegidos do BigQuery. Consulte [ Como gravar um job do MapReduce com o conector do BigQuery ](https://cloud.google.com/dataproc/docs/tutorials/bigquery-connector-mapreduce-example?hl=pt_br) para ver um exemplo. 
  * Anunciamos a versão de disponibilidade geral (GA) dos [ discos permanentes de inicialização da unidade de estado sólido (PD-SSD, na sigla em inglês) do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-pd-ssd?hl=pt_br) . Com eles, é possível criar clusters que usam os PD-SSDs nos discos de inicialização dos nós mestres e de trabalho. 

##  22 de junho de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.85, 1.1.76, 1.2.40 ` . 
  * Foram atualizados os conectores do Cloud Storage e do BigQuery em 1.0.85, 1.1.76 e 1.2.40. Para mais informações, revise as [ notas de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.6.7) no repositório do GitHub: 
    * O conector do Cloud Storage foi atualizado para a versão 1.6.7. 
    * O conector do BigQuery foi atualizado para a versão 0.10.8. 

##  15 de junho de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.84, 1.1.75, 1.2.39 ` . 
  * A saída da "Ação de inicialização" atualmente está disponível no registro ` google.dataproc.startup ` do Stackdriver. 
  * Não será mais possível criar novos clusters no Cloud Dataproc com base na maioria das imagens criadas antes de 14/02/2018. Os clientes não precisam alterar as versões secundárias, mas caso especifiquem uma versão subsecundária adequada a esse grupo, precisarão de uma versão mais recente. Por exemplo, não é possível usar a 1.1.39 para novos clusters, mas a 1.1 e a 1.1.73 são válidas. 

**FIXED:**

  * Foi corrigido o [ problema de ação de inicialização do ZooKeeper ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/issues/279) . 

##  11 de junho de 2018

**FEATURE:**

  * O Cloud Dataproc atualmente está disponível na [ região ](https://cloud.google.com/compute/docs/regions-zones/regions-zones?hl=pt_br#available) ` europe-north1 ` (Finlândia). 

##  8 de junho de 2018

**FEATURE:**

  * Google Cloud SDK 203.0.0, 29-05-2018 
    * Veja a seguir algumas alterações realizadas: 
      * Foi adicionado o ` gcloud beta dataproc workflow-templates instantiate-from-file ` para tornar possível a instanciação de modelos de fluxo de trabalho diretamente de um arquivo YAML. 
      * Foi adicionado o ` gcloud beta dataproc clusters create-from-file ` para tornar possível a criação de clusters diretamente de um arquivo YAML. 
    * Consulte [ a documentação de referência do Cloud SDK ](https://cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates?hl=pt_br) para mais informações. 

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.83, 1.1.74, 1.2.38 ` . 
  * Altere a string de conexão do jdbc transmitida para o beeline ao enviar jobs do Hive para clusters de alta disponibilidade por meio da API Jobs do Cloud Dataproc. Essa nova string faz uso da alta disponibilidade do HiveServer2. 

**FIXED:**

  * O WorkflowTemplates passará a relatar corretamente as falhas do Job. 

##  28 de maio de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.82, 1.1.73, 1.2.37 ` . 
  * O Hive Server 2 atualmente executa os três mestres no modo de alta disponibilidade. 
  * Houve alterações de imagens de visualização no Dataproc 1.3: 
    * Agora é necessário um tamanho mínimo de disco de inicialização de 15 GB. 
    * A porta RPC do Serviço NameNode foi alterada de 8040 para 8051. 
    * A variável de ambiente ` SPARK_HOME ` agora está configurada de forma global. 

**FIXED:**

  * O jar de inicialização ALPN foi removido da 1.2. Esta regressão foi introduzida na 1.2.35. 

##  21 de maio de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.81, 1.1.72, 1.2.36 ` . 
  * Foram realizados upgrades dos conectores do Cloud Storage e do BigQuery em 1.0.81, 1.1.72, 1.2.36. Para mais informações, revise as [ notas de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.6.6) no repositório do GitHub: 
    * O conector do Cloud Storage foi atualizado para a versão 1.6.6. 
    * O conector do BigQuery foi atualizado para a versão 0.10.7. 
  * Há uma nova versão da imagem de visualização do Cloud Dataproc 1.3: 
    * Remover o conector do BigQuery da imagem. Os usuários precisam incluir o conector do BigQuery com jars nos respectivos jobs. 
    * O Cloud Dataproc 1.3 não é compatível. 
    * Consulte a [ lista de versões do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#other_versions) para mais informações. 
  * O Hive Metastore está configurado para execução nos três mestres em modo de alta disponibilidade. 

**FIXED:**

  * Foi corrigido um problema em que a cota do acelerador era validada incorretamente. Por exemplo, poderia ocorrer uma falha na criação do cluster com um erro "Cota 'NVIDIA_K80_GPUS' insuficiente", mesmo que a cota fosse suficiente. 

##  14 de maio de 2018

**FEATURE:**

  * Há um novo controle de imagens do Cloud Dataproc 1.3 disponível na visualização. 
    * Veja a seguir algumas alterações realizadas: 
      * Spark 2.3, Hadoop 2.9, Hive 2.3, Pig 0.17, Tez 0.9. 
      * Hive no Tez por padrão. A ação de inicialização do Tez não é necessária. 
    * O Cloud Dataproc 1.3 não é oficialmente compatível. 
    * Consulte a [ lista de versões do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#other_versions) para mais informações. 

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.80, 1.1.71, 1.2.35 ` . 

##  4 de maio de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.79, 1.1.70, 1.2.34 ` . 

**FIXED:**

  * Foi corrigido o problema em que os workers preemptivos não eram excluídos dos arquivos de associação do node após saírem do cluster. 

##  27 de abril de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.78, 1.1.69, 1.2.33 ` . 

##  20 de abril de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.77, 1.1.68, 1.2.32 ` . 
  * Foi alterada a porta HTTP do Namenode de 50070 para 9870 em clusters de alta disponibilidade (HA, na sigla em inglês) na imagem de visualização. O WebHDFS, por exemplo, está acessível em ` http://clustername-m-0:9870/webhdfs/v1/ ` . Isso é consistente com os clusters padrão e de node único no Dataproc 1.2+. Os clusters do Dataproc 1.0 e 1.1 continuarão a usar a porta 50070 para todos os modos de cluster. 
  * Foram atualizados os conectores do Cloud Storage e do BigQuery. Para mais informações, revise as [ notas de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.6.5) no repositório do GitHub: 
    * O conector do Cloud Storage foi atualizado para a versão 1.6.5. 
    * O conector do BigQuery foi atualizado para a versão 0.10.6. 

**FIXED:**

  * Foi corrigido o problema em que o cluster entra no estado ` ERROR ` devido a um erro no redimensionamento de um grupo de instâncias gerenciadas. 
  * Backport do [ PIG-4967 ](https://issues.apache.org/jira/browse/PIG-4967?attachmentOrder=desc) e do [ MAPREDUCE-6762 ](https://issues.apache.org/jira/browse/MAPREDUCE-6762?attachmentOrder=desc) para a versão de imagem 1.2 do Cloud Datproc para corrigir uma ` NullPointerException ` de vez em quando em jobs do Pig. 
  * Foi corrigido um problema incomum em que o reinício de um agente do Cloud Dataproc durante uma janela pequena da operação de downscale de um cluster causava problemas de desativação dos nodes de dados. 

##  13 de abril de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.76, 1.1.67, 1.2.31 ` . 
  * [ Foram atualizadas as versões do software ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) na versão de imagem 1.2 do Cloud Dataproc para os seguintes produtos: 
    * Apache Spark 2.2.0 -> 2.2.1 
    * Apache Hadoop 2.8.2 -> 2.8.3 

**FIXED:**

  * Foi corrigido um problema raro em que o agente do Cloud Dataproc falhava ao inicializar a configuração do HDFS e enviava pouquíssimos relatórios ao DataNodes. 
  * Foi corrigida a forma como o Cloud Dataproc determina que a desativação do HDFS está concluída. 

##  6 de abril de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.75, 1.1.66, 1.2.30 ` . 

##  30 de março de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.74, 1.1.65, 1.2.29 ` . 

##  23 de março de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) das imagens do Cloud Dataproc: ` 1.0.73, 1.1.64, 1.2.28 ` . 
  * Upgrades dos conectores do Cloud Storage e do BigQuery: foram realizados os upgrades do [ conector do Cloud Storage ](https://cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage?hl=pt_br) para ` gcs-connector-1.6.4 ` e do [ conector do BigQuery ](https://cloud.google.com/dataproc/docs/concepts/connectors/bigquery?hl=pt_br) para ` bigquery-connector-0.10.5 ` . Para mais informações, revise o repositório do GitHub: [ registro de alterações de 19/03/2018, Google Cloud Storage 1.6.4, BigQuery 0.10.5 ](https://github.com/GoogleCloudPlatform/bigdata-interop/releases/tag/v1.6.4) . 

##  22 de março de 2018

**FEATURE:**

  * As [ permissões de IAM granular ](https://cloud.google.com/dataproc/docs/concepts/iam/granular-iam?hl=pt_br) atualmente estão disponíveis para jobs, operações e modelos de fluxo de trabalho do Cloud Dataproc na versão Beta. 

##  16 de março de 2018

**FEATURE:**

  * O **[ Google Stackdriver Monitoring, versão Beta ](https://cloud.google.com/dataproc/docs/concepts/accessing/stackdriver-monitoring?hl=pt_br) ** é ativado automaticamente em clusters do Cloud Dataproc. Além disso, coleta e relata HDFS, YARN e outras métricas de cluster e de jobs do Cloud Dataproc. 
  * Adição de [ Ação de inicialização dos conectores ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/tree/master/connectors) . Com ela, os usuários atualizam os conectores do [ Cloud Storage ](https://cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage?hl=pt_br) e do [ BigQuery ](https://cloud.google.com/dataproc/docs/concepts/connectors/bigquery?hl=pt_br) instalados nos clusters do Cloud Dataproc. 

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) de imagens do Cloud Dataproc: ` 1.0.73, 1.1.64, 1.2.28 ` . 
  * Foi atualizada a [ Ação de inicialização do Conda ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/tree/master/conda) para usar a versão mais recente do Miniconda, caso a versão do Spark seja pelo menos 2.2.0. 

**FIXED:**

  * Foi corrigido um problema em que os jobs do Hive às vezes eram direcionados para um node mestre sem um Hive Server 2 no [ Modo de alta disponibilidade ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/high-availability?hl=pt_br) . Foi resolvido [ um problema no GitHub ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/issues/205) . 

## 9 de março de 2018

**CHANGED:**

  * O [ Cloud Dataproc Auto Zone ](https://cloud.google.com/dataproc/docs/concepts/auto-zone?hl=pt_br) já está disponível. 
  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc: ` 1.0.71, 1.1.62, 1.2.26 ` . 

**FIXED:**

  * Correção de um problema em que o ZooKeeper não estava configurado para limpar periodicamente os diretórios de dados. 

##  5 de março de 2018

**FEATURE:**

  * **[ Imagens personalizadas do Cloud Dataproc, versão Beta ](https://cloud.google.com/dataproc/docs/guides/dataproc-images?hl=pt_br) ** . Os usuários agora podem criar e salvar imagens personalizadas com pacotes pré-instalados. As imagens personalizadas podem então ser usadas para criar clusters do Cloud Dataproc. 

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc: ` 1.0.70, 1.1.61, 1.2.25 ` . 
  * Um campo ` requestId ` opcional foi adicionado a CreateCluster, UpdateCluster, DeleteCluster e SubmitJob. O campo requestId pode ser usado para evitar o processamento de solicitações duplicadas. Pedidos subsequentes com um requestId igual ao de um pedido anterior são ignorados. 
  * Aumento dos tamanhos de heap do MapReduce e do Spark History Server durante a execução em nós mestres grandes. 

**FIXED:**

  * Correção de um problema em que as ações de inicialização podiam falhar ao serem executadas com o erro "errno 26 Text file is busy". 

##  23 de fevereiro de 2018

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc: ` 1.0.69, 1.1.60, 1.2.24 ` . 

##  16 de fevereiro de 2018

**CHANGED:**

  * Novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc: ` 1.0.68, 1.1.59, 1.2.23 ` . 
  * A atualização de rótulos de cluster agora também atualiza rótulos em discos persistentes (PDs, na sigla em inglês) anexados às VMs de trabalho mestre e primária. 

**FIXED:**

  * Correção de um problema em que a exclusão do cluster poderia ficar lenta caso houvesse várias solicitações de cluster exclusivas em andamento. 
  * Correção de um problema em que os jobs eram paralisados caso o registro falhasse. 
  * Correção de um problema em que uma operação de redução de cluster falhava quando o agente dataproc identificava incorretamente o datanode HDFS desativado como paralisado. 
  * Correção de um problema em que o agente dataproc relatava incorretamente duas métricas YARN. 

##  9 de fevereiro de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc - ` 1.0.67, 1.1.58, 1.2.22 ` . 
  * O Modo de alta disponibilidade está disponível agora em versão pública. A versão anterior era Beta. Os clusters do Cloud Dataproc podem ser criados com o _modo de alta disponibilidade_ ativado. Esse é um recurso opcional disponível ao criar um cluster. Nesse modo, os clusters do Cloud Dataproc têm três nós mestres em vez de um. Com a alta disponibilidade do HDFS e do YARN é possível realizar operações ininterruptas do YARN e do HDFS, mesmo em caso de falhas ou reinicializações de qualquer nó único. 

Esse recurso está disponível ao criar clusters usando a ferramenta de linha de
comando ` [ gcloud
](https://cloud.google.com/sdk/gcloud/reference/dataproc?hl=pt_br) ` , a [ API
REST do Cloud Dataproc
](https://cloud.google.com/dataproc/docs/reference/rest?hl=pt_br) e o [
Console do Google Cloud Platform
](https://console.developers.google.com?hl=pt_br) . Consulte [ Modo de alta
disponibilidade ](https://cloud.google.com/dataproc/docs/concepts/configuring-
clusters/high-availability?hl=pt_br) para ver mais informações.

  * Uma operação "Atualizar cluster" agora retorna uma operação ` DONE ` se a solicitação de atualização não tem nenhum trabalho a ser executado. 

**FIXED:**

  * Correção de um problema em que um fluxo de trabalho pode ficar preso devido à exclusão manual de um cluster. 

##  2 de fevereiro de 2018

**FEATURE:**

  * Inclusão de suporte para definir as [ propriedades do Dataproc ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/cluster-properties?hl=pt_br) hadoop-env, mapred-env, spark-env e fio-env por meio de novos prefixos. OBSERVAÇÃO: aplica-se apenas a novas versões de imagens subsecundárias. 
  * Inclusão de um botão para vincular um cluster aos registros do [ Stackdriver ](https://cloud.google.com/dataproc/docs/concepts/accessing/stackdriver-monitoring?hl=pt_br) na página de detalhes do cluster no console do Google Cloud Platform. 

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc - ` 1.0.66, 1.1.57, 1.2.21 ` . 
  * Upgrades de conectores do Cloud Storage e do BigQuery: foi realizado o upgrade do [ conector do Cloud Storage ](https://cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage?hl=pt_br) para ` gcs-connector-1.6.3 ` e do [ conector do Google BigQuery ](https://cloud.google.com/dataproc/docs/concepts/connectors/bigquery?hl=pt_br) para ` bigquery-connector-0.10.4 ` . Para saber mais informações, revise as [ observações de alteração do Cloud Storage ](https://github.com/GoogleCloudPlatform/bigdata-interop/blob/branch-1.6.x/gcs/CHANGES.txt) e do [ BigQuery ](https://github.com/GoogleCloudPlatform/bigdata-interop/blob/branch-1.6.x/bigquery/CHANGES.txt) no repositório do GitHub. 
  * Atualizações para [ BoringSSL ](https://github.com/google/boringssl/commits/0c1eafc6feb694076e152237ad406b325e373cc0) e [ Conscrypt ](https://github.com/google/conscrypt/commits/773faf663084cade0812f37899a1ddbf929c474a) . 
  * Os rótulos de usuários definidos em um cluster agora se propagam para os discos anexados. 

**FIXED:**

  * Correção de um problema do Hadoop em que um número insuficiente de Datanodes criava relatórios. 
  * Aceleramos ` commitJob ` no Cloud Storage para jobs com muitas tarefas de última etapa (redução). 

##  10 de janeiro de 2018

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc - ` 1.0.63, 1.1.54, 1.2.18 ` . 
  * A tentativa automática do commitJob, introduzida no [ MAPREDUCE-5485 ](https://issues.apache.org/jira/browse/MAPREDUCE-5485) agora é ativada por padrão. Configure o ` mapreduce.fileoutputcommitter.failures.attempt ` como ` 1 ` para voltar ao comportamento antigo. 

**FIXED:**

  * Patch aplicado a CVE-2017-5754 ("Meltdown") juntamente com outros patches de segurança referenciados na [ DSA-4082-1 ](https://security-tracker.debian.org/tracker/DSA-4082-1) . 
  * Os SSDs locais agora são devidamente reformatados na inicialização após uma migração de host inesperada. Anteriormente, essas migrações de host em nodes com SSDs locais poderiam fazer com que os workers se tornassem extintos. 
  * Confiabilidade aprimorada na inicialização do cluster de alta disponibilidade para casos em que uma ou mais inicializações de mestres é atrasada. 

**FEATURE:**

  * Agora é possível instanciar os fluxos de trabalho do Dataproc diretamente sem criar um WorkflowTemplate usando o novo [ método InstantiateInline ](https://cloud.google.com/dataproc/docs/reference/rest/v1beta2/projects.regions.workflowTemplates/instantiateInline?hl=pt_br) . 
  * Anunciamos a versão Beta dos [ discos de inicialização da unidade de estado sólido permanente do Cloud Dataproc (PD-SSD, na sigla em inglês) ](https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-pd-ssd?hl=pt_br) . Com eles, é possível criar clusters que usam as PD-SSDs nos discos de inicialização dos nós mestre e de trabalho. 
  * O Cloud Dataproc agora está disponível na [ região ](https://cloud.google.com/compute/docs/regions-zones/regions-zones?hl=pt_br#available) ` northamerica-northeast1 ` (Montréal, Canadá). 
  * O Cloud Dataproc agora está disponível na [ região ](https://cloud.google.com/compute/docs/regions-zones/regions-zones?hl=pt_br#available) ` europe-west4 ` (Holanda). 

##  20 de dezembro de 2017

**FEATURE:**

  * Agora é possível selecionar uma [ plataforma mínima de CPU ](https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu?hl=pt_br) ao criar um cluster do Cloud Dataproc. 

**CHANGED:**

  * O recurso de desativação otimizada do Google Cloud Dataproc está na versão pública. A versão anterior era a Beta. Com ele, é possível remover nodes do cluster sem interromper os jobs em andamento. Um tempo limite especificado pelo usuário determina a espera pela conclusão dos jobs em andamento antes de forçar a remoção dos nós. Esse recurso está disponível ao atualizar clusters usando a ferramenta de linha de comando ` [ gcloud ](https://cloud.google.com/sdk/gcloud/reference/dataproc?hl=pt_br) ` , a [ API REST do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/reference/rest?hl=pt_br) e o [ Console do Google Cloud Platform ](https://console.developers.google.com?hl=pt_br) . Consulte [ Desativação otimizada ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/scaling-clusters?hl=pt_br#graceful_decommissioning) para saber mais informações. 
  * O recurso de clusters de node único está na versão pública (antes, estava na Beta). Eles são clusters do Cloud Dataproc com apenas um node que atua como mestre e worker. Os clusters de nó único são úteis em diversas atividades, incluindo desenvolvimento, educação e ciência de dados leves. 

Esse recurso está disponível ao criar clusters usando a ferramenta de linha de
comando ` [ gcloud
](https://cloud.google.com/sdk/gcloud/reference/dataproc?hl=pt_br) ` , a [ API
REST do Cloud Dataproc
](https://cloud.google.com/dataproc/docs/reference/rest?hl=pt_br) e o [
Console do Google Cloud Platform
](https://console.developers.google.com?hl=pt_br) . Consulte o artigo [
Clusters de nó único
](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/single-
node-clusters?hl=pt_br) para saber mais.

##  8 de dezembro de 2017

**CHANGED:**

  * O recurso de jobs reinicializáveis está disponível agora em versão pública. A versão anterior era Beta. Os jobs do Cloud Dataproc têm uma configuração opcional para reinicializar jobs com falha. Ao definir um job para reinicializar, você especifica o número máximo de tentativas por hora. O máximo são 10 tentativas. Com os jobs reinicializáveis, você reduz os tipos de falhas. Eles são úteis principalmente em jobs de streaming e de longa duração. Esse recurso está disponível ao enviar jobs usando a ferramenta de linha de comando ` [ gcloud ](https://cloud.google.com/sdk/gcloud/reference/dataproc?hl=pt_br) ` , a [ API REST do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/reference/rest?hl=pt_br) e o [ Console do Google Cloud Platform ](https://console.developers.google.com?hl=pt_br) . Consulte o artigo [ Jobs reinicializáveis ](https://cloud.google.com/dataproc/docs/concepts/jobs/restartable-jobs?hl=pt_br) para saber mais informações. 

##  17 de novembro de 2017

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc - ` 1.0.58, 1.1.49, 1.2.13 ` . 
  * Adicionada uma nova otimização que aumenta o desempenho das operações de lista para jobs e operações ao usar tags. 

##  10 de novembro de 2017

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc - ` 1.0.57, 1.1.48, 1.2.12 ` . 
  * Upgrade do Apache Hadoop para ` 2.8.2 ` na imagem do Cloud Dataproc 1.2. 

##  1º de novembro de 2017

**CHANGED:**

  * Ao usar [ seletores de cluster de fluxo de trabalho ](https://cloud.google.com/dataproc/docs/concepts/workflows/overview?hl=pt_br#adding_a_cluster_selector_to_a_template) , se mais de um cluster corresponder aos rótulos especificados, o Cloud Dataproc selecionará o cluster com a memória YARN que tiver mais espaço livre. Essa alteração substitui o comportamento anterior de escolher um cluster aleatório com o rótulo correspondente. 
  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc - ` 1.0.56, 1.1.47, 1.2.11 ` . 
  * Os erros HTTP ` 404 ` e ` 409 ` agora mostrarão o nome completo do recurso para fornecer mensagens de erro mais úteis. 

**FIXED:**

  * Corrigido um bug que impedia modelos de fluxo de trabalho de lidar com ` /locations/ ` em nomes de recursos. 

##  31 de outubro de 2017

**FEATURE:**

Agora o Cloud Dataproc está disponível na [ região
](https://cloud.google.com/compute/docs/regions-zones/regions-
zones?hl=pt_br#available) ` asia-south1 ` (Mumbai, Índia).

##  24 de outubro de 2017

**CHANGED:**

  * Todas as operações do [ ` WorkflowTemplate ` ](https://cloud.google.com/dataproc/docs/concepts/workflows/overview?hl=pt_br) após 27 de outubro de 2017 serão registradas no [ Cloud Audit Logging ](https://cloud.google.com/logging/docs/audit?hl=pt_br) . 
  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc - ` 1.0.55, 1.1.46, 1.2.10 ` . 

##  17 de outubro de 2017

**CHANGED:**

  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc - ` 1.0.54, 1.1.45, 1.2.9 ` . 

**FIXED:**

  * Correção de um bug em que o keep-alive HTTP causava erros ` java.lang.NullPointerException: ssl == null ` durante o acesso ao Cloud Storage. 
  * A [ ação de inicialização do Apache Oozie ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/tree/master/oozie) foi corrigida para funcionar com o Cloud Dataproc 1.2. 

##  11 de outubro de 2017

**CHANGED:**

  * O ` fluentd ` dos clusters do Cloud Dataproc foi reconfigurado para concatenar mensagens de erro de várias linhas. Isso facilitará a localização das mensagens de erro. 
  * Os clusters criados com os [ fluxos de trabalho do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/workflows/overview?hl=pt_br) agora usam o [ posicionamento em zona automática ](https://cloud.google.com/dataproc/docs/concepts/auto-zone?hl=pt_br) . 
  * A partir desta versão, as versões subsecundárias para as imagens do Cloud Dataproc serão mencionadas nas notas da versão. 
  * Há novas [ versões subsecundárias ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) de imagens do Cloud Dataproc - ` 1.0.53, 1.1.44, 1.2.8 ` . 

**FIXED:**

  * Correção de um bug ao ler arquivos ORC no Hive 2.1 no Cloud Dataproc 1.1. Para corrigir esse problema, o [ HIVE-17448 ](https://issues.apache.org/jira/browse/HIVE-17448) recebeu um patch para o Hive 2.1. 
  * Correção de um problema em que o Spark memoryOverhead era configurado incorretamente para clusters com máquinas mestres com muita memória e trabalhos com pouca memória. O memoryOverhead agora está configurado corretamente para esse tipo de cluster. 
  * A lógica do agente do Cloud Dataproc foi melhorada para iniciar jobs na ordem em que foram enviados. 
  * A [ ação de inicialização do HUE ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/tree/master/hue) foi corrigida para funcionar com o Cloud Dataproc 1.2. 
  * Correção de um bug em que as falhas na ação de inicialização não eram devidamente relatadas. 

##  4 de outubro de 2017

**FEATURE:**

  * **Modelos de fluxo de trabalho Cloud Dataproc** (Beta): este novo recurso do Cloud Dataproc permite que os jobs sejam compostos em um gráfico para execução em um conjunto temporário ou existente. O modelo pode criar um cluster, executar jobs e excluir o cluster quando o fluxo de trabalho estiver concluído. O andamento do gráfico pode ser monitorado com a pesquisa de uma única operação. Consulte [ Modelos de fluxo de trabalho - Visão geral ](https://cloud.google.com/dataproc/docs/concepts/workflows/overview?hl=pt_br) para mais informações. 

##  27 de setembro de 2017

**FEATURE:**

  * **IAM Granular do Cloud Dataproc** Beta  : agora é possível configurar papéis IAM e permissões correspondentes por cluster. Isso oferece um mecanismo para ter diferentes configurações de IAM de clusters do Cloud Dataproc. Consulte a [ documentação IAM do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/iam?hl=pt_br#cloud_dataproc_granular_iam) para mais informações. 

**FIXED:**

  * Correção de um bug que impedia o Apache Pig e o Apache Tez de funcionarem juntos no [ Cloud Dataproc 1.2 ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) . Essa correção foi aplicada ao Cloud Dataproc 1.1 em uma versão anterior. 
  * Correção de um bug envolvendo a validação do esquema Hive. Essa correção trata especificamente do [ HIVE-17448 ](https://issues.apache.org/jira/browse/HIVE-17448) e do [ HIVE-12274 ](https://issues.apache.org/jira/browse/HIVE-12274) . 

##  19 de setembro de 2017

**CHANGED:**

  * **Novas versões de imagens subsecundárias** : as versões de imagens subsecundárias mais recentes para 1.0, 1.1 e 1.2 são agora mapeadas respectivamente para ` 1.0.51 ` , ` 1.1.42 ` e ` 1.2.6 ` . 

##  6 de setembro de 2017

**FEATURE:**

  * **Exclusão Programada do Cluster** Beta  : agora é possível criar clusters do Cloud Dataproc com uma política de exclusão programada. Os clusters podem ser programados para exclusão após uma duração especificada ou em um horário especificado, ou após um período de inatividade especificado. Consulte [ Exclusão programada de cluster ](https://cloud.google.com/dataproc/docs/concepts/scheduled-deletion?hl=pt_br) para mais informações. 

##  5 de setembro de 2017

**FEATURE:**

O Cloud Dataproc atualmente está disponível na [ região
](https://cloud.google.com/compute/docs/regions-zones/regions-
zones?hl=pt_br#available) ` southamerica-east1 ` (São Paulo, Brasil).

##  18 de agosto de 2017

**CHANGED:**

  * **Novas versões de imagens subsecundárias** : as versões de imagens subsecundárias mais recentes para 1.0, 1.1 e 1.2 são agora mapeadas respectivamente para ` 1.0.49 ` , ` 1.1.40 ` e ` 1.2.4 ` . 
  * Todos os clusters do Cloud Dataproc agora têm um rótulo ` goog-dataproc-cluster-name ` que se propaga aos recursos subjacentes do Google Compute Engine e pode ser usado para determinar os custos combinados do Cloud Dataproc em dados de faturamento exportados. 

**FIXED:**

  * Os drivers PySpark agora são lançados com um código do grupo de processo alterado para permitir que o agente do Cloud Dataproc limpe corretamente os jobs cancelados ou com comportamento inadequado. 
  * Correção de um bug em que a atualização de rótulos de clusters e o número de workers secundários em uma única atualização resultavam no travamento de uma operação de atualização e em um cluster que não podia ser excluído. 

##  8 de agosto de 2017

**CHANGED:**

A partir de hoje, o [ Cloud Dataproc 1.2
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions?hl=pt_br) será a versão padrão para novos clusters. Para usar versões
mais antigas do Cloud Dataproc, você precisará selecionar manualmente a versão
na criação do cluster.

##  4 de agosto de 2017

**FEATURE:**

**Desativação otimizada** : os clusters do Cloud Dataproc que executam o [
Cloud Dataproc 1.2 ou posterior
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions?hl=pt_br) atualmente são compatíveis com a [ desativação otimizada
YARN ](https://issues.apache.org/jira/browse/YARN-914) . A desativação
otimizada permite a remoção de nodes do cluster sem interromper os jobs em
andamento. Um tempo limite especificado pelo usuário determina a espera pela
conclusão dos jobs em andamento antes de remover os nodes de modo forçado. A [
documentação de escalonamento do Cloud Dataproc
](https://cloud.google.com/dataproc/docs/concepts/scaling-
clusters?hl=pt_br#graceful_decommissioning) contém detalhes sobre como ativar
a desativação otimizada.

**CHANGED:**

O Apache Hadoop do Cloud Dataproc 1.2 foi atualizado para a versão 2.8.1

##  1 de agosto de 2017

**FEATURE:**

O Cloud Dataproc atualmente está disponível na [ região
](https://cloud.google.com/compute/docs/regions-zones/regions-
zones?hl=pt_br#available) ` europe-west3 ` (Frankfurt, Alemanha).

##  21 de julho de 2017

**FEATURE:**

  * **Cloud Dataproc 1.2** : uma nova versão de imagem do Cloud Dataproc já está disponível: ` 1.2 ` . Daqui a duas semanas, ela será a versão de imagem padrão dos novos clusters. Consulte a [ lista de versões do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) para mais informações. Algumas mudanças importantes incluídas nesta nova versão de imagem: 
    * O [ Apache Spark ](http://spark.apache.org) foi atualizado para a versão 2.2.0. 
    * O [ Apache Hadoop ](http://hadoop.apache.org) foi atualizado para a versão 2.8.0. 
    * O provedor de segurança padrão (SSL) usado pelo conector do Cloud Storage foi alterado para um que é baseado em [ Conscrypt ](https://github.com/google/conscrypt) . Essa alteração utilizará a CPU de maneira mais eficiente nas operações com SSL. Em muitos casos, essa alteração resultará em melhor desempenho de leitura e gravação entre o Cloud Dataproc e o Cloud Storage. 
    * O tamanho do bloco relatado do Cloud Storage agora é de 128 MB. 
    * A configuração de memória do Hadoop e Spark foi ajustada para melhorar o desempenho e a estabilidade. 
    * Os daemons HDFS não usam mais portas temporárias de acordo com novas atribuições de porta descritas em [ HDFS-9427 ](https://issues.apache.org/jira/browse/HDFS-9427) . Isso elimina certas condições raras de corrida que, de vez em quando, podem causar falhas de inicialização do daemon. 
    * O ordenamento justo do YARN Capacity Scheduler de [ YARN-3319 ](https://issues.apache.org/jira/browse/YARN-3319) agora está ativado por padrão. 

**CHANGED:**

A partir da versão do Cloud Dataproc 1.2, os jars de inicialização ALPN não
serão mais fornecidos na imagem do Cloud Dataproc. Para evitar falha no job do
Spark, faça upgrade das versões de cliente do Cloud Bigtable e agrupe `
boringssl-static ` com os jobs do Cloud Dataproc. Nosso [ repositório de ações
de inicialização ](https://github.com/GoogleCloudPlatform/dataproc-
initialization-actions) contém esse tipo de ação para voltar ao comportamento
anterior (obsoleto) de incluir o jar de inicialização ` jetty-alpn ` . Essa
alteração só terá impacto se você usar o Cloud Bigtable ou outros clientes
Java gRPC do Cloud Dataproc.

##  11 de julho de 2017

**FEATURE:**

  * **Spark 2.2.0 em Visualização** : a [ imagem de visualização ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) do Cloud Dataproc foi atualizada para o Spark 2.2.0. 

##  28 de junho de 2017

**FEATURE:**

  * **Disponibilidade dos pontos de extremidade regionais** : os [ pontos de extremidade regionais ](https://cloud.google.com/dataproc/docs/concepts/regional-endpoints?hl=pt_br) do Cloud Dataproc já estão disponíveis. 
  * **Autozone Beta  ** : quando você cria um novo cluster é possível usar, como alternativa à escolha de uma zona, o [ recurso zona automática do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/auto-zone?hl=pt_br) . A seleção de zona é feita dentro da região escolhida para a colocação do cluster. 
  * **Conector do Conscrypt para Cloud Storage** : o provedor de segurança padrão (SSL, na sigla em inglês) usado pelo conector do Cloud Storage na [ imagem de visualização do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) foi alterado para outro baseado no [ Conscrypt ](https://github.com/google/conscrypt) . Essa alteração utilizará a CPU de maneira mais eficiente nas operações com SSL. Em muitos casos, essa alteração resultará em melhor desempenho de leitura e gravação entre o Cloud Dataproc e o Cloud Storage. 

##  26 de junho de 2017

**DEPRECATED:**

  * As Cloud Dataproc APIs ` v1alpha1 ` e ` v1beta1 ` agora estão obsoletas e não podem ser usadas. Em vez disso, use a [ API ` v1 ` ](https://cloud.google.com/dataproc/docs/reference/rest?hl=pt_br) atual. 

##  20 de junho de 2017

**FEATURE:**

O Cloud Dataproc agora está disponível na [ região
](https://cloud.google.com/compute/docs/regions-zones/regions-zones?hl=pt_br)
` australia-southeast1 ` (Sydney).

##  6 de junho de 2017

**FEATURE:**

O Cloud Dataproc está agora disponível na região ` europe-west2 ` (Londres).

##  28 de abril de 2017

**CHANGED:**

**Upgrade de conectores do Cloud Storage e do BigQuery** : foram realizados os
upgrades do conector do Cloud Storage para ` gcs-connector-1.6.1 ` e do
conector do BigQuery para ` bigquery-connector-0.10.2 ` . Para ver mais
informações, leia as observações de alteração do [ Cloud Storage
](https://github.com/GoogleCloudPlatform/bigdata-
interop/blob/master/gcs/CHANGES.txt) ou do [ BigQuery
](https://github.com/GoogleCloudPlatform/bigdata-
interop/blob/master/bigquery/CHANGES.txt) no repositório do GitHub.

**DEPRECATED:**

As Cloud Dataproc APIs ` v1alpha1 ` e ` v1beta1 ` agora estão obsoletas e não
podem ser usadas. Em vez disso, use a [ API ` v1 `
](https://cloud.google.com/dataproc/docs/reference/rest?hl=pt_br) atual.

##  21 de abril de 2017

**CHANGED:**

  * Na [ imagem de visualização ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) com base no Hadoop 2.8, o YARN Capacity Scheduler foi definido para usar a política de ordenamento justo em vez do FIFO. 
  * Os [ nomes dos papéis do IAM do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/iam?hl=pt_br) foram atualizados para serem consistentes com outros produtos do Google Cloud. 
  * Novas permissões de registro e monitoramento foram incluídas no [ papel ` Dataproc/Dataproc Worker ` do IAM ](https://cloud.google.com/dataproc/docs/concepts/iam?hl=pt_br#cloud_dataproc_roles) . 

##  12 de abril de 2017

**CHANGED:**

O Apache Hive no [ Cloud Dataproc 1.1
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions?hl=pt_br) foi atualizado para a versão 2.1.1.

##  7 de abril de 2017

**FEATURE:**

**Papel do IAM de trabalho do Cloud Dataproc** : foi adicionado um novo papel
do IAM do Cloud Dataproc chamado [ ` Dataproc/Dataproc Worker `
](https://cloud.google.com/dataproc/docs/concepts/iam?hl=pt_br#cloud_dataproc_roles)
. Ele se destina especificamente ao uso com [ contas de serviço
](https://cloud.google.com/dataproc/docs/concepts/service-accounts?hl=pt_br) .

**CHANGED:**

O [ provedor de segurança do Conscrypt
](https://cloud.google.com/dataproc/docs/release-
notes/service?hl=pt_br#march_30_2017) foi temporariamente alterado do padrão
para um provedor de segurança opcional. Essa alteração foi feita devido a
incompatibilidades com algumas cargas de trabalho. O provedor do Conscrypt
será reativado como padrão posteriormente com o lançamento do Cloud Dataproc
1.2. Enquanto isso, você pode reativar o provedor do Conscrypt ao criar um
cluster especificando esta [ propriedade do Cloud Dataproc
](https://cloud.google.com/dataproc/docs/concepts/cluster-properties?hl=pt_br)
:

    
    
    --properties dataproc:dataproc.conscrypt.provider.enable=true

##  30 de março de 2017

**FEATURE:**

**Conector do Conscrypt para Cloud Storage** : o provedor de segurança padrão
(SSL) usado pelo conector do Cloud Storage foi alterado para outro baseado no
[ Conscrypt ](https://github.com/google/conscrypt) . Essa alteração utilizará
a CPU de maneira mais eficiente nas operações com SSL. Em muitos casos, essa
alteração resultará em melhor desempenho de leitura e gravação entre o Cloud
Dataproc e o Cloud Storage.

**CHANGED:**

As atualizações para [ rótulos de usuário
](https://cloud.google.com/dataproc/docs/concepts/labels?hl=pt_br) aplicadas
aos clusters do Cloud Dataproc agora serão aplicadas aos modelos de grupo de
instâncias gerenciadas. Como as [ máquinas virtuais preemptivas
](https://cloud.google.com/dataproc/docs/concepts/preemptible-vms?hl=pt_br)
são incluídas em um grupo de instâncias gerenciadas, as atualizações nos
rótulos agora são aplicadas às VMs preemptivas.

##  17 de março de 2017

**DEPRECATED:**

Conforme mencionado nas [ notas da versão de 9 de fevereiro
](https://cloud.google.com/dataproc/docs/release-
notes/service?hl=pt_br#february_9_2017) , os registros de auditoria do Cloud
referentes ao Cloud Dataproc não são mais emitidos para o tipo de recurso `
dataproc_cluster ` . A partir desta versão, eles serão emitidos para `
cloud_dataproc_cluster ` .

**CHANGED:**

O comando ` [ gcloud
](https://cloud.google.com/sdk/gcloud/reference/dataproc?hl=pt_br) ` agora [
requer um traço duplo ](https://cloud.google.com/sdk/docs/release-
notes?hl=pt_br#14700_2017-03-15) ( ` -- ` ) entre os argumentos específicos do
gcloud e os argumentos para esses comandos. Por exemplo, se você já usou este
comando:

    
    
    gcloud dataproc jobs submit spark --cluster example-cluster \
    --class sample_class --jars jar_file 1000

O novo formato dele requer um traço duplo entre espaços:

    
    
    gcloud dataproc jobs submit spark --cluster example-cluster \
    --class sample_class --jars jar_file **-- 1000**

.

##  7 de março de 2017

**FEATURE:**

  * **Rótulos de usuário** : esses [ rótulos com recursos do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/labels?hl=pt_br) já estão disponíveis. Você pode adicionar e atualizar rótulos nos clusters e jobs do Cloud Dataproc. Os rótulos são úteis em situações como contabilidade de custos, distribuição de trabalho e testes. 
  * **Anexamos GPUs a clusters Beta  ** : os clusters do Cloud Dataproc atualmente são compatíveis com [ GPUs do Compute Engine ](https://cloud.google.com/compute/docs/gpus?hl=pt_br) . Os clusters podem ter [ de uma a oito GPUs anexadas aos nós mestre e de trabalho ](https://cloud.google.com/dataproc/docs/concepts/gpu-clusters?hl=pt_br) . É possível usá-las com aplicativos no cluster, como o Apache Spark. O anexo de GPUs pode beneficiar alguns tipos de jobs de processamento de dados. 

##  1º de março de 2017

**FEATURE:**

  * **Jobs reinicializáveis Beta  ** : os jobs do Cloud Dataproc têm agora uma [ configuração opcional para reiniciar jobs ](https://cloud.google.com/dataproc/docs/concepts/restartable-jobs?hl=pt_br) com falha. Ao definir a reinicialização de um job, é preciso especificar o número máximo de novas tentativas por hora. Com os jobs reinicializáveis, você reduz os tipos comuns de falhas. Eles são úteis principalmente em jobs de streaming e de longa duração. 
  * **Clusters de nó único Beta  ** : [ clusters de nó único ](https://cloud.google.com/dataproc/docs/concepts/single-node-clusters?hl=pt_br) são clusters do Cloud Dataproc com apenas um nó que funcionam como mestre e trabalho. Eles são úteis em diversas atividades, incluindo desenvolvimento, educação e ciência de dados leves. 

##  9 de fevereiro de 2017

**CHANGED:**

  * **Alterações na geração de registros do Cloud Dataproc Stackdriver**
    * Com novas imagens, os registros do cluster agora são exportados para o Stackdriver como o tipo de recurso ` cloud_dataproc_cluster ` (antigo ` dataproc_cluster ` ). 
    * Os registros de auditoria do Cloud são emitidos para ambos ` cloud_dataproc_cluster ` e ` dataproc_cluster ` (com uso suspenso) até a versão de 9 de março. 
    * Os registros do Stackdriver das novas imagens são indexados primeiro por nome do cluster e, depois, por UUID para ajudar a filtrá-los por nome ou instância do cluster. 
  * **Alterações no monitoramento do Cloud Dataproc Stackdriver**
    * As [ métricas com base em registros ](https://cloud.google.com/logging/docs/view/logs_based_metrics?hl=pt_br) do Cloud Dataproc agora são visíveis no Stackdriver. 
  * **Alterações nos rótulos de usuário do Cloud Dataproc**
    * Agora é possível atualizar os [ rótulos de usuários ](https://cloud.google.com/dataproc/docs/concepts/labels?hl=pt_br) em jobs do Dataproc com a ferramenta de linha de comando [ gcloud ](https://cloud.google.com/dataproc/docs/gcloud-installation?hl=pt_br) ou a [ API REST do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/reference/rest?hl=pt_br) . 

##  19 de janeiro de 2017

**FEATURE:**

  * **Visualização do Cloud Dataproc` 1.2 ` ** : a [ ` preview image ` ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) foi atualizada para refletir a versão planejada do Cloud Dataproc ` 1.2 ` . Essa imagem inclui o Apache Spark 2.1 e o Apache Hadoop 2.8-SNAPSHOT. Ela foi disponibilizada para podermos conceder acesso ao Hadoop 2.8 (assim que ele for oficialmente lançado) no Dataproc 1.2 e às versões release candidate. 

##  5 de janeiro de 2017

**FEATURE:**

  * **Upgrade de conectores do Cloud Storage e do BigQuery** : foram realizados os upgrades do conector do Cloud Storage para ` gcs-connector-1.6.0 ` e do conector do BigQuery para ` bigquery-connector-0.10.1 ` . Para ver mais informações, leia as observações de alteração do [ Cloud Storage ](https://github.com/GoogleCloudPlatform/bigdata-interop/blob/master/gcs/CHANGES.txt) ou do [ BigQuery ](https://github.com/GoogleCloudPlatform/bigdata-interop/blob/master/bigquery/CHANGES.txt) no repositório do GitHub. 

**CHANGED:**

  * O comando ` [ diagnose ](https://cloud.google.com/dataproc/docs/support/diagnose-command?hl=pt_br) ` foi atualizado para incluir a saída do jstack do agente e dos drivers gerados. 

##  16 de dezembro de 2016

**FEATURE:**

  * **Instalação do agente do Google Stackdriver** : agora, o agente de monitoramento do [ Stackdriver ](https://cloud.google.com/stackdriver?hl=pt_br) é instalado por padrão nos clusters do Cloud Dataproc. A [ documentação de monitoramento do Cloud Dataproc Stackdriver ](https://cloud.google.com/dataproc/docs/concepts/stackdriver-monitoring?hl=pt_br) tem informações sobre como usar o monitoramento do Stackdriver com o Cloud Dataproc. É possível ativar e exibir o agente de monitoramento e geração de registros ajustando as [ propriedades do cluster ](https://cloud.google.com/dataproc/docs/concepts/cluster-properties?hl=pt_br) ao criá-lo. 
  * **Cloud Dataproc 1.1.15 e 1.0.24** : as imagens 1.1 e 1.0 receberam atualizações, correções de bugs e melhorias não impactantes. 

##  7 de dezembro de 2016

**ISSUE:**

  * A partir desta versão, **a API Google Cloud Dataproc precisa ser ativada no projeto para o Cloud Dataproc funcionar corretamente.** Use o [ console do Google Cloud Platform ](https://console.cloud.google.com/apis/dashboard?hl=pt_br) para ativar a API Cloud Dataproc. Projetos existentes com a API Cloud Dataproc ativada não serão afetados. 

**FEATURE:**

  * **Cloud Dataproc 1.1.14 e 1.0.23** : as imagens 1.1 e 1.0 receberam atualizações, correções de bugs e melhorias não impactantes. 

**CHANGED:**

  * Maior número de situações em que os serviços do Cloud-Dataproc são automaticamente reiniciados por ` systemd ` nos clusters em caso de comportamento inesperado ou problemático. 

##  29 de novembro de 2016

**FEATURE:**

  * **Suporte à conta de serviço personalizada** : ao criar um cluster do Cloud Dataproc, você agora pode especificar uma conta de serviço gerenciada pelo usuário (não padrão). Essa conta de serviço será usada para executar as máquinas virtuais do Google Compute Engine no cluster. Isso possibilita permissões muito mais minuciosas para os serviços de cada cluster. Consulte a [ documentação de conta de serviço ](https://cloud.google.com/dataproc/docs/concepts/service-accounts?hl=pt_br) para mais informações. 
  * **Cloud Dataproc 1.1.13 e 1.0.22** : a imagem 1.1 do Cloud Dataproc foi atualizada para incluir suporte ao Apache Spark 2.0.2, Apache Zeppelin 0.6.2 e Apache Flink 1.1.3. As imagens 1.1 e 1.0 também foram atualizadas com correções de bugs e melhorias não impactantes. Consulte a [ Lista das versões do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/versioning?hl=pt_br) para mais informações sobre as versões de imagem do Cloud Dataproc. 

##  14 de novembro de 2016

**CHANGED:**

  * Problema corrigido do argumento ` --jars ` que estava ausente do comando ` gcloud dataproc jobs submit pyspark ` . 

##  8 de novembro de 2016

**FEATURE:**

  * **Upgrade do conector do Google BigQuery** : foi realizado o upgrade do conector do BigQuery para ` bigquery-connector-0.10.1-SNAPSHOT ` . Esta versão introduz o novo ` IndirectBigQueryOutputFormat ` , que usa formatos de saída do Hadoop para gravar diretamente em um intervalo temporário do Cloud Storage e emite um job de carga único do BigQuery por job do Hadoop/Spark no tempo de efetivação. Para mais informações, consulte as notas de alteração do [ BigQuery ](https://github.com/GoogleCloudPlatform/bigdata-interop/blob/53151b1ffaf22767ffb5e8db4f01624ba6a680c1/bigquery/src/main/java/com/google/cloud/hadoop/io/bigquery/CHANGES.txt) no repositório do GitHub. 

##  7 de novembro de 2016

**FEATURE:**

  * **Suporte para a região[ recém anunciada asia-northeast1 ](https://www.blog.google/topics/google-cloud/google-cloud-platform-tokyo-region-now-open-for-business/) ** : o Cloud Dataproc está agora disponível na região recém-anunciada asia-northeast1. 

##  2 de novembro de 2016

**FEATURE:**

  * **Rótulos de usuários [BETA]** : atualmente, é possível aplicar rótulos ` key=value ` especificados pelo usuário a clusters e jobs do Cloud Dataproc. Dessa forma, você pode agrupar recursos e operações relacionadas para filtragem e listagem posterior. Como exemplo, você pode usar rótulos com clusters para distribuir o uso do Cloud Dataproc por grupos ou pessoas. Para mais informações, consulte a [ documentação de rótulos de usuário ](https://cloud.google.com/dataproc/docs/concepts/labels?hl=pt_br) . 

**CHANGED:**

  * Problemas corrigidos durante a atualização de cluster que provocavam falha nele. Agora, as falhas de atualização retornam o cluster para o estado ` Running ` . 
  * Problema corrigido no envio de um grande número de jobs rapidamente ou durante um longo período de tempo que provocava falha no cluster. 
  * Aumento do número máximo de jobs simultâneos por cluster. 

##  18 de outubro de 2016

**FEATURE:**

  * **Atualização do Cloud Dataproc 1.1** : a [ imagem do Cloud Dataproc 1.1 ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) foi atualizada para incluir o [ Spark 2.0.1 ](https://spark.apache.org/releases/spark-release-2-0-1.html) e o [ Hadoop 2.7.3 ](https://hadoop.apache.org/docs/r2.7.3/) . 

**CHANGED:**

  * Problema corrigido em que o HiveServer2 tinha a integridade afetada por até 60 segundos após a implantação do cluster. Agora, os jobs do Hive conectam-se com êxito ao HiveServer2 necessário logo após a implantação do cluster. 

##  11 de outubro de 2016

**FEATURE:**

  * **Upgrade de conectores do Cloud Storage e do BigQuery** : foram realizados os upgrades do conector do Cloud Storage para ` gcs-connector-1.5.4 ` e do conector do BigQuery para ` bigquery-connector-0.8.0 ` . Para ver mais informações, leia as observações de alteração do [ Cloud Storage ](https://github.com/GoogleCloudPlatform/bigdata-interop/blob/0e9d09a06ef2b191a8daa6620722b89f8d9081f2/gcs/CHANGES.txt) ou do [ BigQuery ](https://github.com/GoogleCloudPlatform/bigdata-interop/blob/0e9d09a06ef2b191a8daa6620722b89f8d9081f2/bigquery/src/main/java/com/google/cloud/hadoop/io/bigquery/CHANGES.txt) no repositório do GitHub. 
  * **dataproc.localssd.mount.enable** : foi adicionada a nova propriedade ` dataproc.localssd.mount.enable ` , configurável no momento da implantação do cluster, para fazer com que o Cloud Dataproc ignore os SSDs locais. Se definida, o Cloud Dataproc usará os discos permanentes principais do HDFS e os diretórios temporários do Hadoop para que os SSDs locais possam ser usados separadamente para finalidades definidas pelo usuário. Essa propriedade pode ser definida usando o argumento ` --properties dataproc:dataproc.localssd.mount.enable=false ` ao criar um cluster do Cloud Dataproc. 

**CHANGED:**

  * Problema corrigido em que a validação de cota da CPU das máquinas virtuais preemptivas estava sendo feita com a cota da CPU não preemptiva, mesmo quando a cota da CPU preemptiva estava definida. 

##  7 de outubro de 2016

**FEATURE:**

  * Console do Google Cloud Platform 
    * Agora, é possível adicionar até oito [ SSDs locais ](https://cloud.google.com/compute/docs/disks/local-ssd?hl=pt_br) aos worker nodes. O limite anterior era quatro. 
    * Ao consultar os detalhes do cluster, a página "Jobs" agora mostra os botões Parar e Excluir para cada job na lista. Antes, os botões só estavam visíveis na linha em que se passava o cursor do mouse. 

**CHANGED:**

  * Listagem otimizada de recursos por estado e UUID do cluster. Isso pode reduzir várias operações da lista de segundos para milissegundos. 

##  29 de setembro de 2016

**FEATURE:**

  * **Modo de alta disponibilidade do Hadoop [BETA]** : é possível criar clusters do Cloud Dataproc com o _modo de alta disponibilidade_ ativado. Esse é um recurso opcional disponível ao criar um cluster. Nesse modo, os clusters do Cloud Dataproc têm três nós mestres, em vez de um. Assim, tanto a alta disponibilidade do HDFS quanto a do YARN possibilitam operações ininterruptas do YARN e do HDFS, mesmo em caso de falhas ou reinicializações de qualquer nó único. 

Atualmente, esse recurso está disponível ao criar clusters com a ferramenta de
linha de comando ` [ gcloud ](https://cloud.google.com/dataproc/docs/gcloud-
installation?hl=pt_br) ` ou a [ API REST do Cloud Dataproc
](https://cloud.google.com/dataproc/docs/reference/rest?hl=pt_br) . Uma versão
futura permitirá o suporte à criação de clusters com alta disponibilidade no [
Console do Google Cloud Platform
](https://console.developers.google.com?hl=pt_br) .

Consulte a [ documentação do modo de alta disponibilidade
](https://cloud.google.com/dataproc/docs/concepts/high-availability?hl=pt_br)
para saber mais informações.

**CHANGED:**

  * Lista de jobs otimizada com base no estado ou no UUID do cluster. Isso pode reduzir significativamente o tempo necessário para listar os jobs. 

##  22 de setembro de 2016

**FEATURE:**

  * **Upgrade de conectores do Cloud Storage e do BigQuery** : foram realizados os upgrades do conector do Cloud Storage para ` gcs-connector-1.5.3 ` e do conector do BigQuery para ` bigquery-connector-0.7.9 ` . Para mais informações, consulte as [ notas de alteração ](https://github.com/GoogleCloudPlatform/bigdata-interop) no repositório do GitHub. 

**CHANGED:**

  * Como o Cloud Dataproc usa o Java 8 desde o lançamento da versão Beta em setembro de 2015, existe agora uma forte dependência no Java 8 ou superior. 
  * O comando ` --preemptible-worker-boot-disk-size ` não exige mais que você especifique ` 0 ` trabalho preemptivo se não quiser adicionar máquinas preemptivas ao criar um cluster. 

##  16 de setembro de 2016

**FEATURE:**

  * **Tamanhos de disco de inicialização preemptivos** : o tamanho do disco para workers preemptivos agora é configurado pela ferramenta de linha de comando ` gcloud ` na criação do cluster, mesmo quando os preemptivos não são adicionados a um cluster usando o comando ` --preemptible-worker-boot-disk-size ` . 

**CHANGED:**

  * Ambiente convidado do Debian atualizado com as últimas alterações, conforme descrito na visão geral [ Ambiente convidado Linux para Google Compute Engine ](https://github.com/GoogleCloudPlatform/compute-image-packages#guest-overview) . 

##  1º de setembro de 2016

**FEATURE:**

  * **Compatibilidade com o Gerenciamento de identidade e acesso [BETA]** : o Cloud Dataproc atualmente tem compatibilidade **beta** com o [ Gerenciamento de identidade e acesso (IAM, na sigla em inglês) do Google Cloud ](https://cloud.google.com/iam?hl=pt_br) . As permissões de IAM do Cloud Dataproc possibilitam que os usuários executem determinadas ações em clusters, jobs e operações do Cloud Dataproc. Consulte [ Permissões do Cloud Dataproc e papéis de IAM ](https://cloud.google.com/dataproc/docs/concepts/iam?hl=pt_br) para mais informações. 
  * **Suporte a LZO** : agora, os clusters do Cloud Dataproc oferecem suporte nativo ao formato de compactação de dados LZO. 
  * **Alternância de geração de registros do Google Stackdriver** : agora, é possível desativar a geração de registros do Google Stackdriver nos clusters do Cloud Dataproc. Para isso, use o comando "--properties dataproc:dataproc.logging.stackdriver.enable=false" ao criar um cluster com a ferramenta de linha de comando "gcloud". 

**CHANGED:**

  * Agora, as definições de recursos dos clusters recém-implantados exibem uma versão de imagem submenor totalmente resolvida (ex. ` 1.0.11 ` em vez de ` 1.0 ` ). Isso facilita reverter temporariamente para uma versão submenor mais antiga. Consulte [ Controle de versões do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/versioning?hl=pt_br) para mais informações. 
  * A mensagem exibida depois do envio de uma operação de longa duração no Console do Google Cloud Platform, como criar ou excluir um cluster, indicará agora que a operação foi "enviada" em vez de ter "conseguido". 

##  25 de agosto de 2016

**CHANGED:** **Padrão do Cloud Dataproc 1.1** : o [ ` Cloud Dataproc 1.1 `
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions?hl=pt_br) passa a ser a versão de imagem padrão para novos clusters.

**FEATURE:**

  * **Upgrade de conectores do Cloud Storage e do BigQuery** : foram feitos os upgrades do conector do Cloud Storage para ` gcs-connector-1.5.2 ` e o do conector do BigQuery para ` bigquery-connector-0.7.8 ` , otimizando o desempenho. Consulte as notas da versão do [ gcs-connector ](https://github.com/GoogleCloudPlatform/bigdata-interop/blob/8de83da3f65f3e629b9e6120d7db7b644e871704/gcs/CHANGES.txt) e do [ bigquery-connector ](https://github.com/GoogleCloudPlatform/bigdata-interop/blob/8de83da3f65f3e629b9e6120d7db7b644e871704/bigquery/src/main/java/com/google/cloud/hadoop/io/bigquery/CHANGES.txt) para saber mais informações. 
  * **Apache Zeppelin 0.6.1** : foi realizado o upgrade do [ Apache Zeppelin ](http://zeppelin.apache.org) , criado para o Cloud Dataproc e instalável com [ esta ação de inicialização ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/tree/master/zeppelin) para a versão ` 0.6.1 ` . Essa nova versão do Zeppelin é compatível com o Google BigQuery. 

**FIXED:**

  * Problema corrigido em que a adição de muitos nodes (mais de 200) a um cluster provocava falha em alguns deles. 
  * Problema corrigido em que a saída das ações de inicialização que esgotavam o tempo limite não era copiada para o Cloud Storage. 

##  16 de agosto de 2016

**DEPRECATED:** As duas [ versões de imagens
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions?hl=pt_br) do Cloud Dataproc, lançadas durante o Cloud Dataproc beta `
0.1 ` e ` 0.2 ` , não receberão mais atualizações. Você pode continuar usando
as imagens Beta, mas nenhuma atualização nova, como correções de bugs e
atualizações de conectores, será aplicada a essas duas versões de imagem com
uso suspenso.

**CHANGED:** As versões de imagens lançadas após a disponibilização do Cloud
Dataproc, a partir de ` 1.0 ` , estarão sujeitas à [ política de controle de
versões do Cloud Dataproc
](https://cloud.google.com/dataproc/docs/concepts/versioning?hl=pt_br) .

##  8 de agosto de 2016

**FEATURE:** **Cloud Dataproc 1.1** : foi lançada uma nova [ versão de imagens
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions?hl=pt_br) , ` Cloud Dataproc 1.1 ` . Vários componentes foram
atualizados para essa versão de imagem, incluindo:

  * [ Apache Spark ](http://spark.apache.org) ` 2.0.0 `
  * [ Apache Hive ](http://hive.apache.org) ` 2.1.0 `
  * [ Apache Pig ](http://pig.apache.org) ` 0.16.0 `

Para criar um cluster com a imagem ` 1.1 ` , use a ferramenta de linha de
comando ` gcloud ` com o argumento ` --image-version ` , como ` gcloud
dataproc clusters create --image-version 1.1 ` .

**CHANGED:** **SDK do Cloud versão 121.0.0** : diversos argumentos ` gcloud
dataproc ` foram atualizados.

  * O argumento ` --preemptible-worker-boot-disk-size ` foi promovido para disponibilidade geral e pode ser usado para ajustar o tamanho do disco permanente (em GB) dos trabalhos preemptivos. 
  * Os argumentos ` --master-boot-disk-size-gb ` e ` --worker-boot-disk-size-gb ` foram removidos. Em vez deles, use ` --master-boot-disk-size ` e ` --worker-boot-disk-size ` . 

##  2 de agosto de 2016

**FEATURE:** **Upgrade de conectores do Cloud Storage e do BigQuery** : foram
realizados os upgrades do conector do Cloud Storage para ` gcs-connector-1.5.1
` e do conector do BigQuery para ` bigquery-connector-0.7.7 ` . Consulte as
notas da versão do [ gcs-connector
](https://github.com/GoogleCloudPlatform/bigdata-
interop/blob/8de83da3f65f3e629b9e6120d7db7b644e871704/gcs/CHANGES.txt) e do [
bigquery-connector ](https://github.com/GoogleCloudPlatform/bigdata-
interop/blob/8de83da3f65f3e629b9e6120d7db7b644e871704/bigquery/src/main/java/com/google/cloud/hadoop/io/bigquery/CHANGES.txt)
para saber mais informações.

**FEATURE:** **Imagem de visualização atualizada** : diversos componentes da [
imagem de visualização
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions?hl=pt_br#other_versions) foram atualizados:

  * [ Apache Spark ](http://spark.apache.org) ` 2.0.0 `
  * [ Apache Hive ](http://hive.apache.org) ` 2.1.0 `
  * [ Apache Pig ](http://pig.apache.org) ` 0.16.0 `

**FIXED:** Problema corrigido em que o cache de consistência do Cloud Storage
com base em NFS não era limpo nos clusters de longa execução com altas taxas
de criação de arquivo em período prolongado (mais de 1 milhão de arquivos por
hora durante um longo período).

##  19 de julho de 2016

####  Novos recursos

  * **Suporte para a nova região` us-west1 ` ** : o Cloud Dataproc está disponível desde o primeiro dia na [ recém-anunciada região west-1 ](https://cloudplatform.googleblog.com/2016/07/the-latest-for-Cloud-customers-machine-learning-and-west-coast-expansion.html) . Conforme mencionado no aviso, parte da latência de alguns usuários da Costa Oeste dos EUA pode ser reduzida. 
  * **Upgrade do Apache Spark para 1.6.2** : Apache Spark na [ versão da imagem do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) ` 1.0 ` foi atualizado de ` 1.6.1 ` para ` 1.6.2 ` . 
  * **Upgrades dos conectores do Cloud Storage e do BigQuery** : o conector do Cloud Storage foi atualizado para ` gcs-connector-1.5.0 ` e o conector do BigQuery foi atualizado para ` bigquery-connector-0.7.6 ` . Essas novas versões apresentam vários recursos inéditos e correções. 
    * **Fluxos de saída anexáveis** : o GHFS (Google Hadoop File System) agora tem uma opção para ativar o suporte a fluxos de saída anexáveis. Ative essa opção definindo a propriedade ` fs.gs.outputstream.type ` como ` SYNCABLE_COMPOSITE ` . 
    * **Repete automaticamente em caso de erros 429** : agora, os erros HTTP 429 (limite de taxa) das APIs do Google serão automaticamente repetidos com uma retirada. 
    * **Desempenho do Cloud Storage** : desempenho de leitura do conector do Cloud Storage aprimorado, principalmente para várias leituras breves ou muitas buscas. Consulte o [ registro detalhado de alterações ](https://github.com/GoogleCloudPlatform/bigdata-interop/blob/master/gcs/CHANGES.txt) para saber mais informações. 

####  Correções de bugs

  * **Console do Google Cloud Platform**
    * O Console do Google Cloud Platform agora usa o Cloud Dataproc ` v1 ` em vez da API ` v1beta1 ` . O clique no link ` equivalent REST ` mostra os caminhos da API ` v1 ` apropriados e os nomes dos recursos. 
  * Correção do problema em que alguns nós HDFS não ingressavam no cluster porque o nome de domínio deles não foi resolvido na primeira inicialização. 

##  1º de julho de 2016

####  Novos recursos

  * **Ferramenta de linha de comando` gcloud ` **
    * Adicionada a sinalização ` --preemptible-worker-boot-disk-size ` , que pode ser usada para ajustar o tamanho do disco de trabalhos preemptivos. Ela foi adicionada ao rastreamento ` gcloud beta ` . 
    * Agora, a sinalização ` --*-boot-disk-size-gb ` está com o uso suspenso em todos os rastreamentos e foi substituída pelos comandos ` --*-boot-disk-size ` . 

####  Correções de bugs

  * Corrigido um bug na versão de junho. Ele provocava falha nos clusters somente após aguardar durante cerca de 30 minutos. Isso ocorria com mais frequência quando havia falha nas ações de inicialização durante a criação do cluster. Agora, pode haver falha nos clusters em um minuto a partir da falha de uma ação de inicialização. 
  * Redução no tempo de inicialização dos jobs do SparkSQL com diretórios particionados/aninhados ao aplicar um patch ao Spark ( [ SPARK-9926 ](https://issues.apache.org/jira/browse/SPARK-9926) ). 
  * Otimização do tempo de inicialização para qualquer job com muitas entradas de arquivo ao aplicar um patch ao Hadoop ( [ HADOOP-12810 ](https://issues.apache.org/jira/browse/HADOOP-12810) ). 

##  10 de junho de 2016

####  Novos recursos

  * **Visualização do Spark 2.0** : a [ imagem de visualização ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#other_versions) já inclui a versão de visualização do [ Apache Spark ](http://spark.apache.org) . 

##  4 de maio de 2016

####  Novos recursos

  * **Ação de inicialização do Cloud SQL** : o Cloud Dataproc já tem uma ação de inicialização [ E/S do Cloud SQL e Hive Metastore ](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions/tree/master/cloud-sql-proxy) . Essa ação instala um [ proxy do Google Cloud SQL ](https://cloud.google.com/sql/docs/sql-proxy?hl=pt_br) em cada nó em um cluster do Cloud Dataproc. Ela também configura o cluster para armazenar os metadados do Apache Hive em uma determinada instância do Cloud SQL. 

##  29 de abril de 2016

####  Correções de bugs

  * Agora, o diretório de teste de um job do Cloud Dataproc é limpo automaticamente quando o job é concluído. 
  * Se não for possível excluir o cluster adequadamente, agora ele será alterado para o estado ` FAILED ` , em vez de permanecer no estado ` DELETING ` . 
  * Correção de um problema que impedia [ ` --properties command ` ](https://cloud.google.com/dataproc/docs/concepts/cluster-properties?hl=pt_br) do Cloud Dataproc de alterar as propriedades do MapReduce. 
  * Correção do bug em que uma exceção era gerada ao tentar definir a agregação de registros do YARN como saída para o Cloud Storage (em relação ao [ YARN-3269 ](https://issues.apache.org/jira/browse/YARN-3269) ). 

##  30 de março de 2016

####  Novos recursos

  * **Spark 1.6.1** : a versão da imagem do Cloud Dataproc ` 1.0 ` foi atualizada para incluir a versão de manutenção do [ Spark 1.6.1 ](https://spark.apache.org/news/spark-1-6-1-released.html) , em vez do Spark 1.6.0. 
  * **Upgrades OSS** : esta versão atualiza os [ conectores ](https://github.com/GoogleCloudPlatform/bigdata-interop) do Cloud Storage e do Google BigQuery para gcs-connector-1.4.5 e bigquery-connector-0.7.5, respectivamente. 

####  Correções de bugs

  * Agora, é possível especificar ` --num-preemptible-workers 0 ` por meio da ferramenta de linha de comando ` gcloud ` . Antes, isso provocava falha. 
  * Correção de um problema de validação, que gerava erros HTTP ` 500 ` quando a resposta tinha que ser ` 400 bad input ` ou ` 200 OK ` . 
  * Resolvido um problema de validação de cache e inferência reativada do diretório de reativação no conector do Cloud Storage ( ` fs.gs.implicit.dir.infer.enable ` ). 
  * Ajuste das configurações de migração do Google Compute Engine por causa de falhas inesperadas no host. As VMs normais serão automaticamente reiniciadas após a migração, e as máquinas preemptivas não. Antes, todas as VMs eram definidas para não serem reiniciadas automaticamente após a migração. 
  * Resolução de um problema em que o envio de job rápido resultaria em um erro ` Too many pending operations on a resource ` . 

##  8 de março de 2016

####  Novos recursos

  * **Suporte de sub-rede** : o Cloud Dataproc agora aceita [ sub-redes ](https://cloud.google.com/compute/docs/subnetworks?hl=pt_br) por meio da ferramenta de linha de comando ` gcloud ` . Use agora o comando ` --subnet SUBNET ` para especificar uma sub-rede ao criar um cluster do Cloud Dataproc. 

####  Correções de bugs

  * Adição de validação rigorosa dos URIs completos dos recursos de computação. Os seguintes padrões são permitidos: 
    * ` https://<authority>/compute/<version>/projects/... `
    * ` compute/<version>/projects/... `
    * ` projects/... `
  * Correção do problema em que a cota de disco não era verificada quando aumentava o tamanho do cluster. 

##  22 de fevereiro de 2016

**Agora, o Cloud Dataproc está com disponibilidade geral.** Para mais
informações, consulte nossa [ postagem do blog de anúncio ]()

####  Novos recursos

  * **Tipos de máquina do Compute Engine personalizados** : os clusters do Cloud Dataproc agora aceitam [ tipos de máquina do Compute Engine ](https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type?hl=pt_br) para nós mestre e de trabalho. Isso significa ser possível criar clusters com quantidades personalizadas de memória e CPUs virtuais. Para saber mais informações, leia a [ documentação do Dataproc sobre tipos de máquina personalizados ](https://cloud.google.com/dataproc/docs/concepts/custom-machine-types?hl=pt_br) . 
  * **Upgrades OSS** : liberamos o [ Cloud Dataproc versão 1.0 ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) . Essa versão inclui um upgrade para o Apache Spark ` 1.6.0 ` e o Apache Hadoop ` 2.7.2 ` . Ela também inclui novas versões dos [ conectores ](https://github.com/GoogleCloudPlatform/bigdata-interop) do Cloud Storage e do Google BigQuery. 
  * **API v1** : a API ` v1 ` do Cloud Dataproc agora está ativa. Ela inclui suporte à regionalidade com correções e ajustes secundários. Ela está disponível no [ APIs Explorer ](https://developers.google.com/apis-explorer/?hl=pt_br#p/dataproc/v1/) e tem também um [ artefato do Maven ](http://search.maven.org/#artifactdetails%7Ccom.google.apis%7Cgoogle-api-services-dataproc%7Cv1-rev3-1.21.0%7Cjar) no Maven Central. Para ver mais informações, consulte a [ documentação da API REST ](https://cloud.google.com/dataproc/docs/reference/rest?hl=pt_br) . 
  * **Suporte para --jars do PySpark** : adição de suporte para uso da opção ` --jars ` em jobs do PySpark. 
  * **Ativação automática da API** : a ativação da API Cloud Dataproc agora ativa automaticamente as APIs dependentes necessárias, como do Cloud Storage e do Google Compute Engine. 

####  Correções de bugs

  * Resolução de vários problemas que travavam de vez em quando o processo de redução de alguns clusters. 
  * Aprimoramento da validação de alguns tipos de URLs inválidos, que antes falhavam durante a implantação do cluster. 

##  3 de fevereiro de 2016

####  Novos recursos

  * Uma nova opção ` --image-version ` foi adicionada: ` preview `
    * Diferentemente de outras versões numéricas, como ` 0.1 ` e ` 0.2 ` , a versão ` preview ` incluirá os componentes mais recentes do Hadoop, Spark, Pig e Hive, previstos para possível lançamento na próxima versão de distribuição estável do Cloud Dataproc, e será alterada ao longo do tempo. 
    * A partir de 3 de fevereiro de 2016, a versão ` preview ` contém o Spark 1.6.0, com as mesmas versões do Hadoop, Pig e Hive que o Cloud Dataproc ` 0.2 ` . 
    * A opção ` preview ` está sendo implantada no **Console do Google Cloud Platform** . Dessa maneira, ela não pode estar visível na conta para outra semana. Para todos os usuários, a opção ` preview ` pode ser acessada implantando os clusters com a ferramenta de linha de comando ` gcloud ` . 

####  Correções de bugs

  * Maior confiabilidade do comando ` DeleteJob ` . 
  * Correção do bug que fazia com que os jobs permanecessem no estado ` RUNNING ` depois de serem concluídos com êxito. 

##  27 de janeiro de 2016

####  Novos recursos

  * Duas novas opções foram adicionadas à ferramenta de linha de comando ` gcloud ` do Cloud Dataproc para incluir tags e metadados às máquinas virtuais usadas nos clusters do Cloud Dataproc. Essas tags e os metadados serão aplicados às instâncias regulares e preemptivas. 
    * A opção ` --tags ` adicionará tags às instâncias do Google Compute Engine em um cluster. Por exemplo, ao usar o argumento ` --tags foo,bar,baz ` , três tags serão adicionadas às instâncias de máquina virtual no cluster. 
    * A opção ` --metadata ` adicionará metadados às instâncias do Google Compute Engine. Por exemplo, ao usar ` --metadata 'meta1=value1,key1=value2' ` , dois pares de chave-valor de metadados serão adicionados. 
  * Suporte a clusters heterogêneos, em que o nó mestre e os nós de trabalho têm quantidades de memória diferentes. Algumas configurações de memória se baseavam no nó mestre, o que causava alguns problemas, conforme descrito nesta [ pergunta sobre o Stack Overflow ](http://stackoverflow.com/questions/33599308/incorrect-memory-allocation-for-yarn-spark-after-automatic-setup-of-dataproc-clu "Pergunta sobre o Stack Overflow") . Agora, o Cloud Dataproc é mais compatível com clusters que têm nós mestre e de trabalho. 
  * **Console do Google Cloud Platform**
    * A guia **Saída** de um job agora inclui a opção ` Line wrapping ` para facilitar a visualização da saída do job com linhas muito longas. 

####  Correções de bugs

  * Correção de dois problemas que, às vezes, faziam com que as máquinas virtuais permanecessem ativas após o envio de uma solicitação de exclusão do cluster. 
  * A configuração ` maxExecutors ` do Spark agora está definida como ` 10000 ` para evitar falha do AppMaster em jobs com muitas tarefas. 
  * Processamento aprimorado para envio de jobs agressivos por meio de várias alterações no agente do Cloud Dataproc, inclusive: 
    * limitação do número de jobs simultâneos de maneira proporcional à memória do nó mestre; 
    * verificação da memória livre antes de programar novos jobs; 
    * taxa de limitação da quantidade de jobs que podem ser programados por ciclo. 
  * Melhoria no cálculo da capacidade do HDFS antes da ativação ou desativação dos nós para impedir atualizações excessivamente longas. 

##  21 de janeiro de 2016

####  Novos recursos

  * Agora, o comando dataproc no SDK do Google Cloud inclui a opção ` --properties ` para adicionar ou atualizar propriedades em alguns arquivos de configuração do cluster, como ` core-site.xml ` . As propriedades são mapeadas para esses arquivos especificando um prefixo, como ` core:io.serializations ` . Esse comando possibilita modificar várias propriedades e arquivos ao criar um cluster. Para saber mais informações, consulte a [ documentação do Cloud Dataproc do comando ` --properties ` ](https://cloud.google.com/dataproc/docs/concepts/cluster-properties?hl=pt_br "Documentação de propriedades do Cloud Dataproc") . 
  * **Console do Google Cloud Platform**
    * Uma opção foi adicionada ao formulário “Criar clusters” para ativar o escopo da plataforma de nuvem de um cluster. Isso permite ver e gerenciar os dados em todos os serviços do Google Cloud Platform dos clusters do Cloud Dataproc. Para encontrar essa opção, expanda a seção ` Preemptible workers, bucket, network, version, initialization, & access options ` na parte inferior do formulário. 

####  Correções de bugs

  * Os jobs do SparkR não falham mais imediatamente com o erro “permissão negada” ( [ Problema no JIRA do Spark ](https://issues.apache.org/jira/browse/SPARK-11304) ). 
  * A configuração de geração de registros de jobs do Spark com a opção ` --driver-logging-levels ` não interfere mais nas opções de driver do Java. 
  * **Console do Google Cloud Platform**
    * O erro mostrado para ações de inicialização formatadas incorretamente agora aparece de maneira adequada com as informações sobre o problema. 
    * Agora, as mensagens de erro muito extensas incluem uma barra de rolagem para que o botão Fechar permaneça na tela. Referente às correções de bugs de ## 7 de janeiro de 2016 ####. 
  * Correção do problema na versão do Dataproc ` 0.1 ` que fazia com que os arquivos ` _SUCCESS ` e ` _FAILURE ` de zero byte de cada job fossem continuamente regravados no Cloud Storage. 

##  16 de dezembro de 2016

####  Novos recursos

  * Agora, os clusters do Cloud Dataproc têm ` vim ` , ` git ` e ` bash-completion ` instalados por padrão. 
  * A API Cloud Dataproc tem um [ artefato do Maven ](http://mvnrepository.com/artifact/com.google.apis/google-api-services-dataproc/v1beta1-rev1-1.21.0) oficial, [ Javadocs ](http://google-api-client-libraries.appspot.com/documentation/dataproc/v1beta1/java/latest/?hl=pt_br) e um arquivo [ .zip para download ](https://developers.google.com/api-client-library/java/apis/dataproc/v1?hl=pt_br) . 
  * **Console do Google Cloud Platform**
    * Agora, é possível especificar propriedades ao enviar um job e vê-las na guia _Configuração_ correspondente. 
    * O botão ` Clone ` foi adicionado para permitir que você copie facilmente todas as informações sobre um job para o novo formulário de envio dele. 
    * Os ícones da lateral esquerda de clusters e jobs agora são personalizados, e não genéricos. 
    * Na parte inferior do formulário de criação de cluster, o campo ` Image version ` foi adicionado para que você selecione uma [ versão de imagem do Cloud Dataproc específica ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br "Versões do Cloud Dataproc") . 
    * A guia ` VM Instances ` foi adicionada à página de detalhes do cluster, usada para exibir uma lista de todas as VMs no cluster e utilizar o SSH com facilidade no nó mestre. 
    * Na parte inferior do formulário de criação de cluster, o campo ` Initialization Actions ` foi adicionado para que você especifique [ ações de inicialização ](https://cloud.google.com/dataproc/docs/concepts/init-actions?hl=pt_br) . 
    * Os caminhos para os intervalos do [ Cloud Storage ](https://cloud.google.com/storage?hl=pt_br "Cloud Storage") que são exibidos nas mensagens de erro agora são links clicáveis. 

####  Correções de bugs

  * As configurações ` distcp ` são forçadas a corresponder às configurações ` mapred-site.xml ` e a fornecer outras correções para o comando ` distcp ` . Consulte [ este JIRA relacionado ](https://issues.apache.org/jira/browse/MAPREDUCE-5653) . 
  * Garantia de que os trabalhos criados durante uma atualização não ingressem no cluster antes do término das ações de inicialização personalizadas. 
  * Garantia de que os trabalhos sempre se desconectem do cluster quando o agente do Cloud Dataproc é encerrado. 
  * Correção da condição de corrida no front-end da API que ocorria durante a validação de uma solicitação e a marcação do cluster como em atualização. 
  * Aprimoramento de verificações de validação para cota, imagem do Cloud Dataproc e ações de inicialização ao atualizar clusters. 
  * Tratamento aprimorado de jobs quando o agente do Cloud Dataproc é reiniciado. 
  * **Console do Google Cloud Platform**
    * Permissão de argumentos duplicados ao enviar um job. 
    * Substituição da mensagem genérica ` Failed to load ` por detalhes sobre a causa do erro quando ele não é relacionado ao Cloud Dataproc. 
    * Quando um único arquivo jar de um job é enviado, ele pode ser listado somente no campo ` Main class or jar ` no formulário **Enviar um job** . Não é mais preciso listá-lo no campo ` Jar files ` . 

##  18 de novembro de 2015

_As implantações estão programadas para ocorrer em quatro dias e ser
implantadas ou disponibilizadas para uso nos clusters do Cloud Dataproc no fim
do quarto dia, a partir da data de lançamento anunciada da versão._

####  Novos recursos

  * **Seleção de versões** : com o lançamento do [ Cloud Dataproc versão 0.2 ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) , agora é possível selecionar versões diferentes do Cloud Dataproc. Consulte [ Controle de versões do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/versioning?hl=pt_br) para ver mais informações sobre compatibilidade com versões anteriores, bem como a [ Lista das versões do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br) para conhecer os componentes de software compatíveis com cada versão. Selecione uma versão do Cloud Dataproc ao criar um cluster por meio da API Cloud Dataproc, do SDK do Cloud (usando o comando ` gcloud beta dataproc clusters create --image-version ` ), ou pelo [ Console do Google Cloud Platform ](https://console.cloud.google.com/?hl=pt_br) . Dentro de quatro dias do lançamento da nova versão em uma região, ela se tornará a versão padrão usada para criar novos clusters na região. 
  * **Upgrades OSS** : liberamos o [ Cloud Dataproc versão 0.2 ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) . O novo componente do Spark inclui várias correções de bugs. O novo componente do Hive possibilita usar o comando ` hive ` , apresenta melhorias no desempenho e tem um novo metastore. 
  * **Atualizações de conectores** : lançamos atualizações para os [ conectores do BigQuery e do Google Cloud Storage ](https://github.com/GoogleCloudPlatform/bigdata-interop) , 0.7.3 e 1.4.3, respectivamente. Esses conectores corrigem diversos bugs, e as novas versões agora estão incluídas no [ Cloud Dataproc versão 0.2 ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions?hl=pt_br#supported_cloud_dataproc_versions) . 
  * **Metastore do Hive** : incluímos o metastore permanente por cluster com base em MySQL, compartilhado entre o Hive e o SparkSQL. Ele também corrige o comando ` hive ` . 
  * **Mais bibliotecas nativas** : agora, o Cloud Dataproc inclui bibliotecas nativas do Snappy. Ele também inclui as bibliotecas nativas BLAS, LAPACK e ARPACK no MLlib do Spark. 
  * **Comando` --diagnose ` de clusters ** : o SDK do Cloud agora inclui um comando [ \--diagnose ](https://cloud.google.com/dataproc/docs/support/diagnose-command?hl=pt_br) para reunir informações de registro e de diagnóstico sobre o cluster. Veja mais detalhes sobre esse comando na [ documentação de suporte do Cloud Dataproc ](https://cloud.google.com/dataproc/docs/support/diagnose-command?hl=pt_br) . 

####  Correções de bugs

  * Correção da capacidade para excluir jobs com falha rápida antes da criação de alguns diretórios de cluster e de teste. 
  * Correção de alguns erros restantes com as configurações vmem ao usar o comando ` distcp ` . 
  * Correção de um bug raro em que problemas subjacentes do Google Compute Engine provocavam falha na exclusão das instâncias de VM depois que o cluster do Cloud Dataproc era excluído com êxito. 
  * Correção do comando ` Hive ` . 
  * Correção de relatório de erros ao atualizar o número de trabalhos (padrão e preemptivos) no cluster. 
  * Correção de alguns casos de erros ` Rate Limit Exceeded ` . 
  * O comprimento máximo do nome do cluster agora é o correto de 55 caracteres, em vez de 56. 
  * **Console do Google Cloud Platform**
    * Agora, a lista de clusters inclui a coluna ` Created ` , e a guia de configuração do cluster inclui o campo ` Created ` , que informa o tempo de criação dele. 
    * Na tela de criação do cluster, tamanhos de memória maiores que 999 GB agora são exibidos em TB. 
    * Os campos que estavam faltando na guia de configuração de job do PySpark e do Hive ( ` Additional Python Files ` e ` Jar Files ` ) foram adicionados. 
    * A opção para adicionar nós preemptivos ao criar um cluster agora está no “extensor” na parte inferior do formulário. 
    * Tipos de máquina com memória insuficiente (menos de 3,5 GB) não são mais exibidos na lista (antes, a seleção de um desses tipos de máquinas pequenos gerava um erro de back-end). 
    * O texto de marcador no campo Argumentos do formulário de envio de job foi corrigido. 

####  Principais melhorias nos serviços

  * Se definida, a configuração da zona padrão de um projeto agora é usada como o valor padrão para a zona no formulário de criação de cluster no Console do GCP. 

####  Otimizações

  * O desempenho do Hive foi substancialmente melhorado, em especial nas tabelas particionadas com grande número de partições. 
  * Agora, o listStatus multissegmentado foi ativado, o que pode acelerar o tempo de inicialização do job no FileInputFormats que lê grandes números de arquivos e diretórios no Cloud Storage. 

##  23 de outubro de 2015

####  Novos recursos

  * **Console do Google Cloud Platform**
    * Compatibilidade incluída para adição, edição e remoção de [ instâncias preemptivas ](https://cloud.google.com/dataproc/docs/concepts/preemptible-vms?hl=pt_br "instâncias preemptivas") nos clusters. 

##  15 de outubro de 2015

####  Correções de bugs**

  * Correção de um bug em que havia falha no DataNodes ao se registrar no NameNode durante a inicialização, resultando em capacidade do HDFS menor do que a esperada. 
  * Impedimento do envio de jobs no estado ` Error ` . 
  * Bug corrigido que impedia a exclusão correta dos clusters em algumas situações. 
  * Redução dos erros HTTP ` 500 ` ao implantar clusters do Cloud Dataproc. 
  * Correção de erros ` distcp ` de falta de memória com melhor configuração do cluster. 
  * Correção da situação em que havia falha na exclusão correta dos jobs e eles ficavam paralisados no estado ` Deleting ` . 

####  Principais melhorias nos serviços

  * Fornecimento de mais detalhes sobre erros HTTP ` 500 ` em vez de mostrar ` 4xx errors. `
  * Adição das informações sobre os recursos existentes para os erros ` Resource already exists ` . 
  * Agora, informações específicas são fornecidas no lugar da mensagem de erro genérica referente aos erros relacionados ao [ Cloud Storage ](https://cloud.google.com/storage?hl=pt_br "Cloud Storage") . 
  * As operações de listagem agora permitem paginação. 

####  Otimizações

  * Melhoria significativa na utilização do YARN para jobs MapReduce executados diretamente no [ Cloud Storage ](https://cloud.google.com/storage?hl=pt_br "Cloud Storage") . 
  * Ajustes em ` yarn.scheduler.capacity.maximum-am-resource-percent ` para possibilitar melhor utilização e compatibilidade com jobs simultâneos. 

