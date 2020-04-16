#  Notas da versão do Python 3

Python [ 2.7
](https://cloud.google.com/appengine/docs/standard/python/release-
notes?hl=pt_br "Ver esta página no ambiente de execução do Python 2.7") /  3.7
|  Java [ 8 ](https://cloud.google.com/appengine/docs/standard/java/release-
notes?hl=pt_br "Ver esta página no ambiente de execução do Java 8") / [ 11
](https://cloud.google.com/appengine/docs/standard/java11/

release-notes?hl=pt_br "Ver esta página no ambiente de execução do Java 11") |
PHP [ 5 ](https://cloud.google.com/appengine/docs/standard/php/release-
notes?hl=pt_br "Ver esta página no ambiente de execução do PHP 5") / [ 7
](https://cloud.google.com/appengine/docs/standard/php7/

release-notes?hl=pt_br "Ver esta página no ambiente de execução do PHP 7") |
[ Ruby ](https://cloud.google.com/appengine/docs/standard/ruby/

release-notes?hl=pt_br "Ver esta página no ambiente de execução do Ruby") |
Go [ 1.9 ](https://cloud.google.com/appengine/docs/standard/go/release-
notes?hl=pt_br "Ver esta página no ambiente de execução do Go 1.9") / [ 1.11
](https://cloud.google.com/appengine/docs/standard/go111/

release-notes?hl=pt_br "Visualizar esta página no ambiente de execução do Go
1.11") / [ 1.12 ](https://cloud.google.com/appengine/docs/standard/go112/

release-notes?hl=pt_br "Ver esta página no ambiente de execução do Go 1.12") |
[ Node.js ](https://cloud.google.com/appengine/docs/standard/nodejs/

release-notes?hl=pt_br "Ver esta página no ambiente de execução do Node.js")

Além das notas da versão abaixo, você também pode rastrear problemas
conhecidos no [ rastreador de problemas
](https://issuetracker.google.com/issues?q=componentid%3A187191%2B&hl=pt_br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  30 de julho de 2019

  * As ferramentas AppCfg e o SDK autônomo legado do App Engine, viabilizados pelos arquivos ` GoogleAppEngineLauncher.dmg ` , ` GoogleAppEngine.msi ` e ` google_appengine.zip ` , tornam-se obsoletos. O Google desativará e removerá o suporte em 30 de julho de 2020. 
  * Os recursos do SDK do App Engine passam a ser viabilizadas exclusivamente por meio do [ SDK do Cloud ](https://cloud.google.com/sdk/docs?hl=pt_br) . Para mais informações, consulte [ Como migrar para o SDK do Cloud ](https://cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration?hl=pt_br) . 

##  18 de abril de 2019

  * O App Engine passa a estar disponível na região ` asia-northeast2 ` (Osaka, Japão). 

##  15 de abril de 2019

  * O App Engine passa a estar disponível na região ` europe-west6 ` (Zurique, Suíça). 

##  9 de abril de 2019

  * O [ Cloud Tasks ](https://cloud.google.com/tasks/docs?hl=pt_br) agora é GA e pode ser usado para configurar tarefas a serem executadas de forma assíncrona, não relacionadas às solicitações de usuários. 

  * O [ acesso VPC sem servidor ](https://cloud.google.com/appengine/docs/standard/python3/connecting-vpc?hl=pt_br) está disponível em versão Beta. O Acesso VPC sem servidor permite que seu aplicativo se conecte a recursos internos em sua rede VPC, como instâncias de VM do Compute Engine, instâncias do Cloud Memorystore e outros. 

##  4 de abril de 2019

  * O ambiente de execução do Python 3 foi atualizado para a versão 3.7.3. 

##  11 de janeiro de 2019

  * O ambiente de execução do Python 3 foi atualizado para a versão 3.7.2. 

##  14 de dezembro de 2018

  * O [ ambiente de execução do Python 3.7 ](https://cloud.google.com/appengine/docs/standard/python3?hl=pt_br) para o ambiente padrão do App Engine agora é GA. 

##  12 de dezembro de 2018

  * Atualização do SDK do Python para a versão 1.9.81. 
  * Todos os aplicativos foram alternados para soquetes de rede BSD. Não é necessário fazer nenhuma alteração nos aplicativos. 
  * A [ API Sockets ](https://cloud.google.com/appengine/docs/standard/python/sockets?hl=pt_br) passa a ser GA. 

##  16 de novembro de 2018

  * O nginx passa a ser o servidor da web padrão. Não é necessário fazer nenhuma alteração nos aplicativos. 

##  31 de outubro de 2018

  * O ambiente de execução do Python 3 foi atualizado para a versão 3.7.1 do Python. 
  * O ambiente de execução do Python 3 torna-se compatível com entradas recursivas no arquivo ` requirements.txt ` . 

##  22 de outubro de 2018

  * O App Engine agora está disponível na região ` asia-east2 ` (Hong Kong). 

##  8 de agosto de 2018

  * O [ ambiente de execução do Python 3.7 ](https://cloud.google.com/appengine/docs/standard/python3?hl=pt_br) para o ambiente padrão do App Engine agora está em versão Beta. 
  * Publica-se uma lista de [ diferenças entre os ambientes de execução do Python 2.7 e do Python 3.7 ](https://cloud.google.com/appengine/docs/standard/python3/python-differences?hl=pt_br) . 

##  10 de julho de 2018

  * O App Engine está disponível na região ` us-west2 ` (Los Angeles). 

##  2 de julho de 2018

Correção de um bug na [ configuração de escalonamento automático
](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=pt_br#scaling_elements)
que fazia com que o App Engine encerrasse subitamente as instâncias quando a
configuração ` max_instances ` era usada.

##  15 de maio de 2018

  * Uma implantação gradual de um upgrade no sistema de dimensionamento automático foi concluída: 
    * Maior eficiência que geralmente resulta em custo mais baixo de instância (redução de até 6% para muitos usuários) e até 30% de redução nas _solicitações de carregamento_ , que são a primeira solicitação para uma nova instância. 
    * Nova configuração máxima de instâncias que permite limitar o número total de instâncias a serem programadas. 
    * Nova configuração mínima de instâncias que permite especificar um número mínimo de instâncias para continuar em execução no aplicativo. 
    * Nova configuração de utilização da CPU de destino que permite a otimização entre latência e custo. 
    * Nova configuração de utilização de capacidade de destino que permite otimizar o número de solicitações simultâneas em que novas instâncias são iniciadas. 
    * Não há mais instâncias residentes no dimensionamento automático. Antes, se você usasse a configuração ` min_idle_instances ` , as instâncias ociosas mínimas eram marcadas como _Residentes_ no Console do Cloud, enquanto as restantes eram marcadas como _Dinâmicas_ . O novo programador simplesmente marca todas as instâncias como _Dinâmicas_ com dimensionamento automático. No entanto, o comportamento subjacente permanece semelhante ao comportamento anterior. Se você usar ` min_idle_instances ` e ativar as solicitações de aquecimento, verá no mínimo esse número de instâncias dinâmicas em execução, mesmo durante períodos sem tráfego. 
    * Para mais detalhes, consulte a [ documentação sobre dimensionamento automático ](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=pt_br#scaling_elements) . 

##  14 de dezembro de 2017

  * Aprimoramento da documentação de controle de acesso na implantação de apps com papéis do IAM e contas de serviço: 

    * [ Papéis predefinidos do App Engine ](https://cloud.google.com/appengine/docs/standard/python3/access-control?hl=pt_br#predefined_app_engine_roles)
    * [ Como implantar usando papéis de IAM ](https://cloud.google.com/appengine/docs/standard/python3/granting-project-access?hl=pt_br#deploying_using_iam_roles)
    * [ Exigir permissões ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=pt_br#required_permissions)

##  31 de outubro de 2017

  * Disponibilização do App Engine na região ` asia-south1 ` (Mumbai, Índia). 

##  11 de outubro de 2017

  * Anúncio da disponibilidade geral do [ firewall do App Engine ](https://cloud.google.com/appengine/docs/standard/python3/creating-firewalls?hl=pt_br) . 

##  13 de setembro de 2017

  * Agora, você pode usar certificados gerenciados para adicionar SSL ao seu domínio personalizado. Depois de mapear o domínio personalizado para o aplicativo, o App Engine fornece automaticamente um certificado SSL, processando a renovação do certificado antes que ele expire ou sua revogação, caso o domínio personalizado seja removido. Os certificados gerenciados estão em versão Beta. Para mais informações, consulte [ Como proteger domínios personalizados com SSL ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=pt_br) . 

  * Se houver um mapeamento de domínio e um certificado SSL, ele continuará funcionando conforme esperado. Você também pode [ fazer upgrade para certificados SSL gerenciados ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=pt_br#updating_to_managed_ssl_certificates) . 

  * Os comandos da ` gcloud ` e os métodos da API Admin usados para [ mapear domínios personalizados ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=pt_br) passam a ter disponibilidade geral. Isso inclui [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains?hl=pt_br) e [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=pt_br) . No entanto, se você preferir usar certificados SSL gerenciados, utilize os comandos Beta e os métodos especificados em [ Como proteger domínios personalizados com SSL ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=pt_br) . 

##  5 de setembro de 2017

  * Disponibilização do App Engine na região ` southamerica-east1 ` (São Paulo, Brasil). 

##  1 de agosto de 2017

  * Disponibilização do App Engine na região ` europe-west3 ` (Frankfurt, Alemanha). 

##  18 de julho de 2017

  * Disponibilização do App Engine na região ` australia-southeast1 ` (Sydney, Austrália). 

##  6 de junho de 2017

  * Disponibilização do App Engine na região ` europe-west2 ` (Londres). 
  * Agora é possível usar os recursos da versão Beta na API Admin e na ferramenta de linha de comando ` gcloud ` para [ criar e gerenciar domínios personalizados e certificados SSL ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=pt_br) . 

##  9 de maio de 2017

  * Disponibilização do App Engine na região ` us-east4 ` (Virgínia do Norte). 

##  27 de outubro de 2016

  * [ Suspensão de uso ](https://cloud.google.com/appengine/docs/deprecations?hl=pt_br) dos serviços de Canal e XMPP. Os serviços serão desativados em 31 de outubro de 2017. 

##  1º de agosto de 2016

**Observações sobre a API Admin**

  * Disponibilização geral da versão 1 da [ API Admin ](https://cloud.google.com/appengine/docs/admin-api?hl=pt_br) . 

##  1º de agosto de 2016 - versão 1.9.42

**Observações do ambiente de execução do Python 3.7**

  * Esta versão não inclui um novo SDK do Python 3.7. Os usuários do Python 3.7 precisam continuar usando o SDK 1.9.40. 

##  18 de julho de 2016 - versão 1.9.40

  * Omissão da versão 1.9.39. 

  * Limitação das solicitações do LeaseTasksByTag em 25 por segundo. 

  * Os erros de servidor e de cliente passaram a refletir com mais precisão os erros de status por URL no painel do App Engine. 

  * Novo [ tutorial guiado do App Engine ](https://console.cloud.google.com/start/appengine?hl=pt_br) no Console do GCP. Escolha o idioma preferido e inicie um tutorial interativo diretamente no console. 

  * Aumenta o limite máximo de tarefas cron para 250. 

##  1º de julho de 2016

**Cloud Datastore**

  * Vigência dos novos [ preços do Cloud Datastore ](https://cloud.google.com/appengine/pricing?hl=pt_br#costs-for-datastore-calls) . 

##  25 de maio de 2016 - versão 1.9.38

  * O erro retornado pela busca de URL para uma solicitação de uma porta fora dos intervalos permitidos (80-90, 440-450, 1024-65535) passa a retornar sempre ` INVALID_URL ` , conforme documentado. 

**Cloud Datastore**

  * Ao confirmar uma transação entre grupos, os números de versão retornados para entidades novas ou atualizadas são todos iguais. No comportamento anterior, as entidades dentro do mesmo grupo confirmado como parte de uma transação entre grupos tinham o mesmo número de versão, mas entidades em grupos diferentes podiam ter números de versão diferentes. Essa alteração garante que todas as entidades novas e atualizadas tenham um número de versão idêntico quando são confirmadas como parte de uma transação entre grupos, independentemente do grupo de entidades. As entidades não atualizadas não terão um novo número de versão, conforme acontecia antes da alteração. 

##  4 de maio de 2016 - versão 1.9.37

Inclusão de correções de bugs e melhorias gerais.

##  2 de maio de 2016

**Ambiente flexível do App Engine**

  * Disponibilização do [ ambiente de execução do Ruby ](https://cloud.google.com/appengine/docs/flexible/ruby?hl=pt_br) para o ambiente flexível do App Engine. 

##  18 de abril de 2016 - versão 1.9.36

Em resposta a solicitações, a API App Engine Users se junta ao restante do App
Engine ao oferecer compatibilidade com papéis de IAM e expansão de grupo. Isso
significa que qualquer usuário que seja proprietário, editor ou leitor de um
projeto ou um administrador do App Engine é considerado "administrador" pela
API Users, independentemente do usuário ter recebido o papel diretamente ou
por assinatura em um grupo. * Essa versão preenche detalhes do erro, quando
disponíveis, em mensagens de erro associadas ao tipo de exceção "OverQuota".

##  24 de março de 2016 - versão 1.9.35

  * Renomeação de VMs gerenciadas do App Engine para [ ambiente flexível do App Engine ](https://cloud.google.com/appengine/docs/flexible?hl=pt_br) . 
  * Correção dos carimbos de data/hora de trace de acordo com carimbos de data/hora de registro. 

##  4 de março de 2016 - versão 1.9.34

  * Aumento da cota padrão de busca de URL para aplicativos faturados. Consulte a página [ Cotas ](https://cloud.google.com/appengine/docs/quotas?hl=pt_br#UrlFetch) para detalhes. 

##  17 de fevereiro de 2016 - versão 1.9.33

  * O caminho do URL "/form" passou a ser permitido e será encaminhado para aplicativos. Anteriormente, esse caminho estava bloqueado. 

##  3 de fevereiro de 2016 - Versão 1.9.32

  * Opções de estrutura de contêiner para VMs gerenciadas 

Os comandos ` gcloud preview app deploy ` (e ` mvn gcloud:deploy ` ) fazem
upload dos artefatos para nossos servidores e criam um contêiner para
implantar o app no ambiente de VM gerenciada.

Há dois mecanismos para criar a imagem de contêiner remotamente. O
comportamento padrão é criar o contêiner em uma máquina virtual temporária do
Compute Engine que tenha o Docker instalado. Se preferir, você poderá usar o
serviço [ Cloud Build ](https://cloud.google.com/cloud-build/docs?hl=pt_br) .
Para usar esse serviço, siga estes passos:

    1. [ Ative a API Cloud Build ](https://support.google.com/cloud/answer/6158841?hl=pt_br) em seu projeto. 
    2. Use o comando ` gcloud config set app/use_cloud_build True ` . Isso fará com que todas as invocações de ` gcloud preview app deploy ` usem o serviço. Para retornar ao comportamento padrão, use o comando ` gcloud config set app/use_cloud_build False ` . 

##  14 de janeiro de 2016 - versão 1.9.31

Compatibilidade do App Engine com Grupos do Google. Adicionar um Grupo do
Google como membro de um projeto concede aos membros do grupo acesso ao App
Engine. Por exemplo, se um Grupo do Google for editor em um projeto, todos os
membros do grupo passam a ter acesso de editor ao aplicativo do App Engine.

##  30 de novembro de 2015 - versão 1.9.30

Agora, os cabeçalhos de solicitações da fila push feitos para tarefas da fila
de tarefas sem payload passam a conter uma entrada Content-Length definida
como "0". Anteriormente, os cabeçalhos dessas solicitações não tinham entradas
Content-Length.

##  30 de novembro de 2015 - versão 1.9.29

  * Não é mais feito o cálculo e a armazenagem de profundidade de filas inexistentes, filas marcadas para exclusão e no caso de interrupções da tabela de filas. 
  * Para desenvolvedores que usem a [ API endpoints ](https://cloud.google.com/appengine/docs/standard/python/endpoints/create_api?hl=pt_br#defining_the_api_endpointsapi) , foi adicionado um parâmetro booleano detectável à anotação @Api para permitir que usuários desativem a descoberta de API. O uso desse recurso impedirá o funcionamento de algumas bibliotecas de cliente (por exemplo, JavaScript) e o API Explorer porque elas dependem da descoberta. 

##  29 de outubro de 2015 - versão 1.9.28

A API Prospective Search, que se tornou obsoleta em 14 de julho de 2015, ficou
restrita aos usuários existentes. Encerramento total: 1º de dezembro de 2015.
* Precisão aprimorada da filtragem geográfica em consultas de pesquisa.

##  25 de setembro de 2015 - Versão 1.9.27

Os aplicativos recém-ativados para faturamento passaram a adotar como padrão
um orçamento diário ilimitado, e não mais um orçamento diário máximo de US$ 0.
Isso evita interrupções indesejadas causadas por falta de orçamento. Para
definir um teto no custo diário do aplicativo, depois de ativar o faturamento,
defina um orçamento nas [ configurações do App Engine
](https://console.cloud.google.com/project/_/appengine/settings?hl=pt_br) .
Para mais informações, consulte [ Como configurar um orçamento diário
](https://cloud.google.com/appengine/docs/developers-
console?hl=pt_br#setting_a_daily_budget) .

Datastore

  * Correção de bug: os atributos numéricos repetidas passam a ser permitidos. 
  * A pesquisa com atributos passa a ser GA. 

##  27 de agosto de 2015 - versão 1.9.26

  * Upgrade da biblioteca oauth2client para a [ versão 1.4.2 ](https://github.com/google/oauth2client/blob/master/CHANGELOG.md)
  * Adição do menu "mostrar no contexto" a registros do aplicativo MVM que tenham thread_id ou request_id como um campo na entrada de registro. Isso permite classificar registros de app com base em um dos campos. 
  * Capacidade de provisionar aplicativos para carga atual e configurar provisionamento elástico com base em métricas de nível de VM e de aplicativo. 
  * Possibilidade de acessar a API remota usando credenciais OAuth2 com https://developers.google.com/identity/protocols/application-default-credentials 
  * Use RequestPayloadTooLargeException para solicitações URLFetch com payloads muito grandes. 

##  14 de agosto de 2015 - Versão 1.9.25

  * Adição de PyAMF versão 0.7.2 (beta). 
  * Os menus do Admin Console começam a redirecionar para o console do GCP. Serviços selecionados, como o Admin Logs, continuarão disponíveis no Admin Console. 
  * O Datastore passa a permitir que as propriedades representem a lista vazia. 
  * As tarefas com falha em filas configuradas com um "retry_limit" de zero deixarão de ser repetidas. 

