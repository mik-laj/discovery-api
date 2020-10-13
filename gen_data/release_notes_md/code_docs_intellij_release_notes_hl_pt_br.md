#  Notas da versão

Nesta página, você encontrará atualizações de produção para o Cloud Code.
Verifique-a para ver avisos sobre recursos novos ou atualizados, correção de
bugs, problemas conhecidos e funcionalidades obsoletas.

As atualizações mais recentes também podem ser encontradas na [ página de
notas da versão do GitHub ](https://github.com/GoogleCloudPlatform/cloud-code-
intellij/blob/master/CHANGELOG.md) .

É possível ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas da versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt-br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/cloud-code-for-intellij-
release-notes.xml `

##  18.5.1

O Cloud Code agora está disponível no PyCharm (Community e Professional).
Navegue pelos buckets do Cloud Storage e interaja com os Cloud Source
Repositories do PyCharm. Mais IDEs em breve.

###  Inclusão

  * Plug-in refatorado para que os recursos agnósticos de idioma (Cloud Storage, Cloud Source Repositories) estejam disponíveis em outros IDEs da JetBrains, além do IDEA. [ 1896 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1896)

###  Alteração

  * O SDK do Cloud gerenciado não será mais instalado em cada carregamento de IDE após o primeiro cancelamento manual. [ 2113 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2113)

###  Correção

  * Exceção corrigida em 2018.2 EAP. [ 2124 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2124)

##  18.4.1

###  Inclusão

  * Deixe que o plug-in do Google Cloud Tools gerencie o SDK do Cloud para você, incluindo download, instalação e atualizações. Não é mais necessário fazer o download do SDK manualmente. [ 673 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/673)
  * Reduza os conflitos de dependência da versão com o suporte integrado à BOM do Java para o Google Cloud. Inclui a adição automática da BOM com as bibliotecas de cliente do Google, além de inspeções de pom.xml para ajudar a gerenciar conflitos de dependência da versão. [ 1921 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1921)
  * Adicione automaticamente as variáveis de ambiente necessárias às configurações de execução local do App Engine para acessar localmente as APIs do Google Cloud. [ 1917 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1917)

##  18.3.2

  * Correção de um bug que causava erro de inicialização do plug-in no IntelliJ IDEA 2017.2 e versões anteriores. [ 1972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1972)

##  18.3.1

###  Inclusão

  * Inclusão da capacidade de criar contas de serviço e fazer o download de chaves de contas de serviço do fluxo de trabalho da biblioteca de clientes do IDE. [ 1808 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1808)

###  Correção

  * Correção de casos em que ` appengine-web.xml ` não era gerado devido à ausência de ` web.xml ` . [ 1903 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1903)

##  18.2.1

###  Inclusão

  * Inclusão da capacidade de descobrir e adicionar bibliotecas de clientes Java do Google Cloud a partir do IDE. [ 1806 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1806)
  * Inclusão da capacidade de ativar as APIs do Google Cloud a partir do IDE. [ 1807 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1807)

###  Alteração

  * Atualização do seletor de projeto da nuvem com uma experiência do usuário aprimorada. [ 1719 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1719)
  * Atualização do seletor de projeto da nuvem para que a última seleção seja lembrada e definida como padrão. [ 1812 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1812)

###  Correção

  * Correção dos artefatos de execução locais padrão do App Engine ausentes. [ 1625 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1625)

##  18.1.1

###  Correção

  * Correção do mecanismo de relatório de erros com falha. [ 1842 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1842)

##  17.12.2

###  Correção

  * Correção da configuração de propriedade de análise incorreta que causava o descarte da análise. [ 1773 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1773)

##  17.12.1

O plug-in da Conta do Google foi incorporado ao plug-in do Cloud Tools e já
não é uma instalação separada. Se você já tinha o plug-in Account Tools
instalado, siga o novo prompt para removê-lo e reinicie o IDE a fim de
garantir que não haja problemas.

###  Correção

  * Correção do erro de memória ao digitar e pesquisar vários projetos no seletor de projetos da nuvem. [ 1742 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1742)

###  Alteração

  * O plug-in da Conta do Google agora está integrado ao plug-in do Google Cloud Tools. Não é mais necessário instalar o plug-in da Conta do Google separadamente. [ 1735 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1735)

##  17.11.1

###  Inclusão

  * Integração do Google Cloud Storage no IntelliJ. Agora, é possível procurar seus buckets e ver o conteúdo deles sem sair do IDE. [ 1696 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1696)
  * Recursos de pesquisa e filtro no seletor do projeto da nuvem. [ 1660 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1660)
  * O novo atalho do menu "Ferramentas de suporte da biblioteca do App Engine" fornece outra maneira de adicionar o suporte do App Engine a um projeto. [ 1685 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1685)

###  Correção

  * Correção da mensagem de status do indicador da região do App Engine quando nenhum projeto da nuvem foi selecionado. [ 1607 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1607)

##  17.9.2

O Java 8 no ambiente padrão do App Engine agora está [ amplamente disponível
](https://cloudplatform.googleblog.com/2017/09/Java-8-on-App-Engine-Standard-
environment-is-now-generally-available.html) .

###  Alteração

  * Atualização do novo assistente de projeto padrão do App Engine para gerar aplicativos Java 8. [ 1641 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1641)

##  17.9.1

###  Inclusão

  * Inclusão da capacidade de alterar o nome do artefato testado para implementações flexíveis do App Engine. [ 1610 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1610)

###  Alteração

  * As configurações de implantação flexível do App Engine agora são padrão para implantar o artefato como está, sem renomear para ` target.jar ` ou ` target.war ` . [ 1151 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1151)
  * Atualização do nome do artefato do marcador nos modelos do Dockerfile gerados para que fique mais claro que ele precisa ser atualizado pelo usuário. [ 1648 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1648)
  * As configurações de implantação padrão do App Engine agora atualizam automaticamente para DoS, despachos, cron, filas e índices do armazenamento de dados. [ 1613 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1613)
  * Projetos nativos que adicionam suporte com Endpoints Frameworks para o App Engine agora usam o Endpoints V2. [ 1612 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1612)

###  Correção

  * Correção do erro ` Deployment source not found ` ao implantar artefatos do Maven. [ 1220 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1220)
  * Correção da escala do ícone do usuário nas telas HiDPI. [ 1633 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1633)
  * Correção de um problema em que foi feito downgrade do plug-in no IDEA 2017.3 EAP. [ 1631 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1631)

##  17.8.2

###  Correção

  * Correção do problema "Erro: invalid_scope" ao fazer login com sua Conta do Google. [ 1598 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1598)

##  17.8.1

###  Inclusão

  * Inclusão de um link de geração de relatórios de feedback e problemas ao menu de atalhos do Google Cloud Tools. [ 1560 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1560)

###  Alteração

  * Os usuários agora podem salvar configurações de execução de implantação que são parcialmente concluídas ou estão em um estado de erro. [ 1407 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1407)

###  Correção

  * Correção do conflito de idioma do Docker registrado que causa problemas na execução do plug-in ao lado do plug-in .ignore. [ 1535 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1535)
  * Correção da análise de NPE dos carimbos de data/hora do ponto de interrupção do Cloud Debugger. [ 1537 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1537)
  * Remoção de EAR como tipo de artefato aceitável do App Engine para execuções do servidor de desenvolvimento local. [ 1190 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1190)
  * As implantações agora são exibidas em várias janelas do IDE. [ 1432 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1432)
  * Correção da falha causada pela tentativa de modificar uma coleção somente leitura. [ 1571 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1571)

##  17.6.2

###  Correção

  * Correção de NPE que ocorre quando há uma configuração local do servidor de desenvolvimento, mas nenhum atributo padrão. [ 1525 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1525)

##  17.6.1

###  Inclusão

  * Atributo flexível do App Engine com ` app.yaml ` e configuração do Dockerfile. [ 1514 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1514)
  * Detecção de compatibilidade da biblioteca flexível do App Engine. [ 1277 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1277)

###  Alteração

  * O usuário pode especificar um diretório Docker em vez de apenas um Dockerfile para implantações flexíveis. [ 1304 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1304)
  * Atualização da experiência do usuário da caixa de diálogo de implantação (padrão e flexível). [ 1477 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1477)

###  Correção

  * Correção do tamanho do avatar do Google para telas HiDPI. [ 1391 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1391)

##  17.2.5_2017

###  Inclusão

  * As variáveis de ambiente na configuração de execução local padrão do App Engine agora são passadas para o servidor de desenvolvimento. [ #1364 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1364)
  * As variáveis de ambiente configuradas no appengine-web.xml agora são consideradas e passadas para o servidor de desenvolvimento. [ #377 ](https://github.com/GoogleCloudPlatform/appengine-plugins-core/issues/377)

##  17.2.4_2017

###  Inclusão

  * Inclusão de uma caixa de seleção para implantar todos os arquivos de configuração do App Engine durante a implantação do serviço. [ #1346 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1346)

##  17.2.3_2017

###  Alteração

  * Remoção da sinalização "Limpar datastore" da configuração do servidor de desenvolvimento local padrão do App Engine, uma vez que a versão atual do servidor não é compatível com ela. ( [ #1345 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1345) ) 

##  17.2.2_2017

###  Correção

  * Ambiente de execução do Java Runtime Environment (JRE) inválido ao criar um aplicativo padrão do App Engine ( [ #1316 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1316) ): 
    
        > Unable to stage app: Cannot get the System Java Compiler. Please use a JDK, not a JRE.
    

##  17.2.1

Feliz ano novo, usuários do Cloud Code! O primeiro lançamento deste ano é,
basicamente, uma versão de manutenção. Se você estiver tendo problemas de
autenticação usando os Cloud Source Repositories e nosso plug-in, confira [
esta possível solução ](https://github.com/GoogleCloudPlatform/google-cloud-
intellij/issues/1174) .

Esta é uma lista das alterações visíveis:

###  Inclusão

  * Suporte para vários Cloud Source Repositories para um único projeto do GCP. ( [ #1024 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1024) ) 
  * Inicialização e seleção de região do App Engine. ( [ #1232 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1232) ) 

###  Correção

  * Interromper o dev_appserver no Windows sempre falha com ` com.intellij.execution.ExecutionException ` . ( [ #1215 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1215) ) 
  * O novo assistente de projeto padrão do App Engine gera web.xml com servlet 2.5. ( [ #1194 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1194) ) 
  * A caixa de seleção "Limpar armazenamento de dados" do servidor local padrão do App Engine não funciona. ( [ #1188 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1188) ) 
  * O seletor de projeto não mostra projetos marcados para exclusão. ( [ #1119 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1119) ) 

Visite nosso [ lançamento 17.2
](https://github.com/GoogleCloudPlatform/google-cloud-
intellij/milestone/19?closed=1) para detalhes completos.

##  16.11.6

###  Inclusão

  * Expansão de item de menu do Google Cloud Tools com vários atalhos de ação. ( [ #1061 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1061) ). 
  * Verificação da versão do SDK do Cloud com suporte mínimo. ( [ #1051 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1051) ). 
  * Criação automática de todas as configurações de execução relevantes de aplicativos do App Engine Standard. ( [ #1063 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1063) ). 
  * A estrutura do App Engine agora é filha da estrutura da Web no novo assistente de projeto. ( [ #1065 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1065) ). 

###  Correção

  * As fontes de implantação únicas no painel de implantação do servidor de aplicativos agora aparecem como itens de linha separados. ( [ #821 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/821) ). 
  * Validação de caminhos inválidos do SDK do Cloud no Windows. ( [ #1091 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1091) ). 

##  16.10.5

IMPORTANTE: este plug-in requer o uso do SDK do Cloud v133.0.0 para a execução
correta do servidor de desenvolvimento local com o SDK do Java 8 mais recente.
Execute ` gcloud components update ` no shell para garantir que tem a versão
mais recente do SDK do Cloud.

###  Correção

  * Correção de problema com o modo de depuração do servidor de desenvolvimento local quando são feitas alterações enquanto o servidor está sendo executado. ( [ #972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/972) ) 
  * Melhoria do texto quando o servidor de desenvolvimento tem um caminho inválido do SDK do Cloud. ( [ #1043 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1043) ). 
  * Atualização dos nomes da configuração de execução para serem prefixados com 'Google...' ( [ #1021 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1021) ). 

##  16.10.1

  * Estamos alterando o esquema de controle de versão para YY.MM.i. Planejamos uma frequência de lançamento mensal para minimizar a interrupção das atualizações. Também descartamos o rótulo "Beta". 
  * ATENÇÃO: o servidor de desenvolvimento do App Engine local foi interrompido com as versões mais recentes do JDK 8. ( [ #920 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/920) ). Isso será corrigido na próxima versão do App Engine SDK em breve. 

###  Inclusão

  * Importador da Biblioteca do App Engine padrão no assistente de Atributo e Projeto. ( [ #866 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/866) ) 
  * Aplicativos padrão do App Engine que usam o nível de linguagem Java 8 serão notificados para usar o nível de linguagem 7 ( [ # 966 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/966) ) 

###  Alteração

  * Atualização de rótulos e ícones de configuração de execução. O Cloud Debugger agora é o Cloud Debugger ( [ #936 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/936) ) 

###  Correção

  * Correção do modo de depuração do servidor de desenvolvimento local. ( [ #928 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/928) ) 
  * Implementação flexível interrompida no Windows 10. ( [ #937 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/937) ) 
  * O inspetor de objetos do Cloud Debugger está funcionando novamente. ( [ #929 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/929) ) 
  * Carimbos de data/hora de snapshots do Cloud Debugger causando NPE ( [ #919 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/919) ) 

##  1.0-beta - 2016-09-14

###  Inclusão

  * Compatibilidade do ambiente padrão do App Engine ( [ #767 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/767) ) 
  * Campos adicionais agora disponíveis na configuração de implantação ( [ #868 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/868) ) 

##  0.9.7.5-beta - 2016-08-29

###  Inclusão

  * Verifique se a implantação é válida para o usuário credenciado, com prompt para adicionar um novo usuário, caso não seja. ( [ 837 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/837) ) 

##  0.9.6-beta - 2016-06-23

###  Inclusão

  * Implantação de suporte ao ambiente _compat_ flexível do App Engine. ( [ #720 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/720) ) 
  * Implantação de suporte ao ambiente padrão do App Engine. ( [ #665 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/665) ) 
  * Verificação da compatibilidade do plug-in Cloud Tools e Conta. ( [ #651 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/650) ) 

###  Alteração

  * Entrada de versão movida para ser uma configuração de nível superior na caixa de diálogo de configuração de implantação. ( [ #639 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/639) ) 

##  0.9.4-beta - 2016-04-20

###  Inclusão

  * Implantação de item do menu de ferramentas do ambiente flexível do App Engine. ( [ #635 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/635) ) 
  * Suporte para projetos com base em Maven como fontes de implantação do ambiente flexível do App Engine ( [ #600 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/600) ) 

###  Alteração

  * A implantação do ambiente flexível do App Engine pode ser cancelada desconectando nosso servidor de aplicativos do App Engine. ( [ #581 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/581) ) 
  * O Dockerfile gerado pelo ambiente flexível do App Engine e o ` app.yaml ` agora são padrão para o local recomendado em um projeto Java com estrutura do Maven. ( [ #575 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/575) ) 

###  Correção

  * Bug de login que pode resultar em nenhum usuário ativo sendo selecionado ao adicionar um usuário. ( [ #644 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/644) ) 
  * Desfazer uma implantação do App Engine pode causar um erro. ( [ #599 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/599) ) 

