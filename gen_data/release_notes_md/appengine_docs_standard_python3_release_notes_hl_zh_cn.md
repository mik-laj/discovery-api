#  Python 3 版本说明

Python [ 2.7
](https://cloud.google.com/appengine/docs/standard/python/release-
notes?hl=zh_cn "在 Python 2.7 运行时中查看此页面") /  3.7  |  Java [ 8
](https://cloud.google.com/appengine/docs/standard/java/release-notes?hl=zh_cn
"在 Java 8 运行时中查看此页面") / [ 11
](https://cloud.google.com/appengine/docs/standard/java11/

release-notes?hl=zh_cn "在 Java 11 运行时中查看此页面") |  PHP [ 5
](https://cloud.google.com/appengine/docs/standard/php/release-notes?hl=zh_cn
"在 PHP 5 运行时中查看此页面") / [ 7
](https://cloud.google.com/appengine/docs/standard/php7/

release-notes?hl=zh_cn "在 PHP 7 运行时中查看此页面") |  [ Ruby
](https://cloud.google.com/appengine/docs/standard/ruby/

release-notes?hl=zh_cn "在 Ruby 运行时中查看此页面") |  Go [ 1.9
](https://cloud.google.com/appengine/docs/standard/go/release-notes?hl=zh_cn
"在 Go 1.9 运行时中查看此页面") / [ 1.11
](https://cloud.google.com/appengine/docs/standard/go111/

release-notes?hl=zh_cn "在 Go 1.11 运行时中查看此页面") / [ 1.12
](https://cloud.google.com/appengine/docs/standard/go112/

release-notes?hl=zh_cn "在 Go 1.12 运行时中查看此页面") |  [ Node.js
](https://cloud.google.com/appengine/docs/standard/nodejs/

release-notes?hl=zh_cn "在 Node.js 运行时中查看此页面")

除下述版本说明之外，您还可以在 [ 问题跟踪器
](https://issuetracker.google.com/issues?q=componentid%3A187191%2B&hl=zh_cn)
上跟踪已知问题。

如需接收最新产品动态，请将此页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 。

##  2019 年 7 月 30 日

  * 通过 ` GoogleAppEngineLauncher.dmg ` 、 ` GoogleAppEngine.msi ` 和 ` google_appengine.zip ` 文件提供的 AppCfg 工具和旧版独立 App Engine SDK 现已弃用。Google 将于 2020 年 7 月 30 日关停并移除支持。 
  * App Engine SDK 的功能只能通过 [ Cloud SDK ](https://cloud.google.com/sdk/docs?hl=zh_cn) 提供。如需了解详情，请参阅 [ 迁移到 Cloud SDK ](https://cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration?hl=zh_cn) 。 

##  2019 年 4 月 18 日

  * App Engine 现已在 ` asia-northeast2 ` 区域（日本大阪）发布。 

##  2019 年 4 月 15 日

  * App Engine 现已在 ` europe-west6 ` 区域（瑞士苏黎世）发布。 

##  2019 年 4 月 9 日

  * [ Cloud Tasks ](https://cloud.google.com/tasks/docs?hl=zh_cn) 现已正式发布，可用于设置要在用户请求之外异步执行的任务。 

  * [ Serverless VPC Access ](https://cloud.google.com/appengine/docs/standard/python3/connecting-vpc?hl=zh_cn) 现已发布测试版。借助 Serverless VPC Access，您可以将应用连接到 VPC 网络中的内部资源，例如 Compute Engine 虚拟机实例、Cloud Memorystore 实例等。 

##  2019 年 4 月 4 日

  * Python 3 运行时已更新为 Python 3.7.3 版。 

##  2019 年 1 月 11 日

  * Python 3 运行时已更新为 Python 3.7.2 版。 

##  2018 年 12 月 14 日

  * 适用于 App Engine 标准环境的 [ Python 3.7 运行时 ](https://cloud.google.com/appengine/docs/standard/python3?hl=zh_cn) 现已正式发布。 

##  2018 年 12 月 12 日

  * Python SDK 已更新为 1.9.81 版。 
  * 所有应用都已改用 BSD 网络套接字，不需要更改应用。 
  * [ Sockets API ](https://cloud.google.com/appengine/docs/standard/python/sockets?hl=zh_cn) 现已正式发布。 

##  2018 年 11 月 16 日

  * nginx 现在是默认的网络服务器，不需要更改应用。 

##  2018 年 10 月 31 日

  * Python 3 运行时已更新为 Python 3.7.1 版。 
  * Python 3 运行时支持 ` requirements.txt ` 文件中的递归条目。 

##  2018 年 10 月 22 日

  * App Engine 现已在 ` asia-east2 ` 地区（香港）推出。 

##  2018 年 8 月 8 日

  * 适用于 App Engine 标准环境的 [ Python 3.7 运行时 ](https://cloud.google.com/appengine/docs/standard/python3?hl=zh_cn) 现已发布测试版。 
  * 现已提供 [ Python 2.7 运行时和 Python 3.7 运行时的差异 ](https://cloud.google.com/appengine/docs/standard/python3/python-differences?hl=zh_cn) 列表。 

##  2018 年 7 月 10 日

  * App Engine 现已在 ` us-west2 ` 区域（洛杉矶）发布。 

##  2018 年 7 月 2 日

修复了 [ 自动扩缩配置
](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=zh_cn#scaling_elements)
中的一个错误：使用 ` max_instances ` 设置时，此错误会造成 App Engine 主动关停实例。

##  2018 年 5 月 15 日

  * 完成了自动扩缩系统的逐步升级： 
    * 效率的提高通常会降低实例费用（对于许多用户，费用可降低多达 6%），并且“加载请求” __ （即发送给新实例的第一个请求）可降低多达 30%。 
    * 新增实例数上限设置，允许您限制要调度的实例总数。 
    * 新增实例数下限设置，允许您指定保持应用运行的实例数下限。 
    * 新增目标 CPU 利用率设置，可让您在延时和费用之间进行优化。 
    * 新增目标吞吐量利用率设置，可让您优化启动新实例时的并发请求数。 
    * 自动调节中不再有常驻实例。以前，如果您使用 ` min_idle_instances ` 设置，则最小空闲实例数在 Cloud Console 中被标记为“常驻” __ ，其余实例被标记为“动态” __ 。新的调度程序只是将所有实例都标记为“动态” __ ，可自动调节。不过，基本处理方式仍与之前类似。如果您使用 ` min_idle_instances ` 并启用预热请求，则即使在没有流量的时段内，您至少也会看到许多正在运行的动态实例。 
    * 如需了解详情，请参阅 [ 自动调节文档 ](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=zh_cn#scaling_elements) 。 

##  2017 年 12 月 14 日

  * 完善了关于使用 IAM 角色和服务帐号部署应用的访问权限控制文档： 

    * [ 预定义 App Engine 角色 ](https://cloud.google.com/appengine/docs/standard/python3/access-control?hl=zh_cn#predefined_app_engine_roles)
    * [ 使用 IAM 角色进行部署 ](https://cloud.google.com/appengine/docs/standard/python3/granting-project-access?hl=zh_cn#deploying_using_iam_roles)
    * [ 需要权限 ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=zh_cn#required_permissions)

##  2017 年 10 月 31 日

  * App Engine 现已在 ` asia-south1 ` 区域（印度孟买）发布。 

##  2017 年 10 月 11 日

  * 发布了 [ App Engine 防火墙 ](https://cloud.google.com/appengine/docs/standard/python3/creating-firewalls?hl=zh_cn) 正式版。 

##  2017 年 9 月 13 日

  * 您现可使用托管式证书将 SSL 添加到自定义网域。将自定义网域映射到应用后，App Engine 会自动预配 SSL 证书，并负责在证书到期之前续订证书，在您移除自定义网域后撤消证书。托管式证书现为测试版。如需了解详情，请参阅 [ 使用 SSL 保护自定义网域 ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=zh_cn) 。 

  * 如果您已有网域映射和 SSL 证书，则它将继续按预期发挥作用。您还可以 [ 升级到托管式 SSL 证书 ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=zh_cn#updating_to_managed_ssl_certificates) 。 

  * 用于 [ 映射自定义网域 ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=zh_cn) 的 ` gcloud ` 命令和 Admin API 方法现已正式发布。这包括 [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains?hl=zh_cn) 和 [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=zh_cn) 。但是，如果要使用托管式 SSL 证书，请使用在 [ 使用 SSL 保护自定义网域 ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=zh_cn) 中指定的测试版命令和方法。 

##  2017 年 9 月 5 日

  * App Engine 现已在 ` southamerica-east1 ` 区域（巴西圣保罗）发布。 

##  2017 年 8 月 1 日

  * App Engine 现已在 ` europe-west3 ` 区域（德国法兰克福）发布。 

##  2017 年 7 月 18 日

  * App Engine 现已在 ` australia-southeast1 ` 区域（澳大利亚悉尼）发布。 

##  2017 年 6 月 6 日

  * App Engine 现已在 ` europe-west2 ` 区域（伦敦）发布。 
  * 您现在可以使用 Admin API 和 ` gcloud ` 命令行工具中的测试版级别功能来 [ 创建和管理您的自定义网域和 SSL 证书 ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=zh_cn) 。 

##  2017 年 5 月 9 日

  * App Engine 现已在 ` us-east4 ` 区域（北弗吉尼亚州）发布。 

##  2016 年 10 月 27 日

  * Channel 和 XMPP 服务现 [ 已弃用 ](https://cloud.google.com/appengine/docs/deprecations?hl=zh_cn) 。这些服务将于 2017 年 10 月 31 日关停。 

##  2016 年 8 月 1 日

**Admin API 说明**

  * [ Admin API ](https://cloud.google.com/appengine/docs/admin-api?hl=zh_cn) 的第 1 版现已正式发布。 

##  2016 年 8 月 1 日 - 1.9.42 版

**Python 3.7 运行时说明**

  * 此版本不包含新的 Python 3.7 SDK。Python 3.7 用户应该继续使用 1.9.40 版 SDK。 

##  2016 年 7 月 18 日 - 1.9.40 版

  * 跳过了 1.9.39 版。 

  * LeaseTasksByTag 请求数将限制为每秒 25 个请求。 

  * “服务器错误”和“客户端错误”现在可以更准确地反映 App Engine 信息中心内的每个网址状态错误。 

  * 在 GCP Console 中新增了 [ App Engine 操作指南 ](https://console.cloud.google.com/start/appengine?hl=zh_cn) 。选择您的首选语言，然后直接在 Console 中启动互动式教程。 

  * 将 cron 任务数上限增加到 250。 

##  2016 年 7 月 1 日

**Cloud Datastore**

  * 新的 [ Cloud Datastore 价格 ](https://cloud.google.com/appengine/pricing?hl=zh_cn#costs-for-datastore-calls) 现已生效。 

##  2016 年 5 月 25 日 - 1.9.38 版

  * 对允许范围（80-90、440-450、1024-65535）之外的端口发出请求时，由网址提取返回的错误现在将始终返回 ` INVALID_URL ` 作为记录。 

**Cloud Datastore**

  * 提交跨组事务时，为新实体或更新的实体返回的版本号均相同。根据以前的行为，同一个组中作为跨组事务的一部分提交的实体具有相同的版本号，但是不同组中的实体可能具有不同的版本号。此更改确保所有新的实体和更新的实体在作为跨组事务的一部分提交时都具有相同的版本号，而无论其实体组如何。和以前一样，未更新的实体将没有新的版本号。 

##  2016 年 5 月 4 日 - 1.9.37 版

包含常规错误修复和改进。

##  2016 年 5 月 2 日

**App Engine 柔性环境**

  * [ Ruby 运行时 ](https://cloud.google.com/appengine/docs/flexible/ruby?hl=zh_cn) 现在可用于 App Engine 柔性环境。 

##  2016 年 4 月 18 日 - 1.9.36 版

为响应您的请求，App Engine Users API 与 App Engine 的其余组件一起支持 IAM
角色和群组扩展。这意味着，只要用户是项目所有者、编辑者、查看者或 App Engine
管理员，则无论用户角色是直接获授予还是以群组成员身份获授予，Users API 都会将这些用户视为“管理员”。* 此版本会在与 "OverQuota"
异常类型关联的错误消息中填充错误详情（如有）。

##  2016年 3 月 24 日 - 1.9.35 版

  * App Engine 托管虚拟机已重命名为 [ App Engine 柔性环境 ](https://cloud.google.com/appengine/docs/flexible?hl=zh_cn) 。 
  * 修复了跟踪时间戳以匹配日志时间戳。 

##  2016 年 3 月 4 日 - 1.9.34 版

  * 增加了付费应用网址提取的默认配额。如需了解详情，请参阅 [ “配额”页面 ](https://cloud.google.com/appengine/docs/quotas?hl=zh_cn#UrlFetch) 。 

##  2016 年 2 月 17 日 - 1.9.33 版

  * 网址路径“/form”现已获准使用，并且将会转发给应用。以前，系统禁止访问此路径。 

##  2016 年 2 月 3 日 - 1.9.32 版

  * 托管虚拟机的容器构造选择 

` gcloud preview app deploy ` （以及 ` mvn gcloud:deploy `
）命令用于将您的软件工件上传到我们的服务器并构建容器，以将您的应用部署到托管虚拟机环境。

远程构建容器映像的机制有两种。默认行为是在安装了 Docker 的暂时性 Compute Engine 虚拟机上构建容器。或者，您可以使用 [ Cloud
Build ](https://cloud.google.com/cloud-build/docs?hl=zh_cn) 服务。要使用 Cloud Build
服务，请按照下列步骤操作：

    1. 为您的项目 [ 激活 Cloud Build API ](https://support.google.com/cloud/answer/6158841?hl=zh_cn) 。 
    2. 使用命令 ` gcloud config set app/use_cloud_build True ` 。这将使所有对 ` gcloud preview app deploy ` 的调用都使用该服务。要恢复为默认行为，请使用命令 ` gcloud config set app/use_cloud_build False ` 。 

##  2016 年 1 月 14 日 - 1.9.31 版

App Engine 现在支持 Google 群组：将 Google 群组添加为项目成员，可授予群组成员访问 App Engine 的权限。例如，如果某个
Google 群组是项目的编辑者，则该群组的所有成员现在都对 App Engine 应用拥有编辑者访问权限。

##  2015 年 11 月 30 日 - 1.9.30 版

针对没有负载的任务队列任务发出的推送队列请求的标头现在将包含设置为“0”的 Content-Length 条目。以前，此类请求的标头不含 Content-
Length 条目。

##  2015 年 11 月 30 日 - 1.9.29 版

  * 对于不存在的队列、标记为要删除的队列以及队列表服务中断的情况，停止计算和存储队列深度。 
  * 对于使用 [ Endpoints API ](https://cloud.google.com/appengine/docs/standard/python/endpoints/create_api?hl=zh_cn#defining_the_api_endpointsapi) 的开发者，在 @Api 注释中添加了可发现的布尔值参数，以允许用户停用 API 发现功能。使用此功能将阻止某些客户端库（例如，JavaScript）和 API Explorer 运行，因为其依赖于发现功能。 

##  2015 年 10 月 29 日 - 1.9.28 版

2015 年 7 月 14 日弃用的 Prospective Search API 现在仅限现有用户使用。它将于 2015 年 12 月 1 日完全关停。*
提高了搜索查询中地理位置过滤的准确性。

##  2015 年 9 月 25 日 - 1.9.27 版

新启用结算功能的应用现在默认为每日预算无限制，而不再默认为每日最高预算为
$0。这可以防止因预算用完而导致意外的服务中断。要为应用的每日费用设置上限，请在启用结算功能后，在 [ App Engine 设置
](https://console.cloud.google.com/project/_/appengine/settings?hl=zh_cn)
中设置预算。如需了解详情，请参阅 [ 设置每日预算
](https://cloud.google.com/appengine/docs/developers-
console?hl=zh_cn#setting_a_daily_budget) 。

Datastore

  * 错误修正：现在允许重复的数字分面。 
  * 分面搜索现已正式发布。 

##  2015 年 8 月 27 日 - 1.9.26 版

  * 将 oauth2client 库升级到 [ 1.4.2 ](https://github.com/google/oauth2client/blob/master/CHANGELOG.md) 版。 
  * 为日志条目中有 thread_id 或 request_id 字段的 MVM 应用日志添加“显示上下文”菜单。这允许根据上述任一字段对应用日志进行排序。 
  * 能够为当前负载配置应用，并根据虚拟机和应用级指标设置弹性配置。 
  * 现在可以通过 https://developers.google.com/identity/protocols/application-default-credentials 页面使用 OAuth2 凭据访问 Remote API。 
  * 将 RequestPayloadTooLargeException 用于负载过大的 URLFetch 请求。 

##  2015 年 8 月 14 日 - 1.9.25 版

  * 添加了 PyAMF 0.7.2 版（测试版）。 
  * 管理控制台菜单开始重定向到 GCP Console。部分服务（例如管理日志）可以在管理控制台中继续使用。 
  * Datastore 现在允许属性表示空列表。 
  * 队列中“retry_limit”配置为零的失败任务将不再重试。 

