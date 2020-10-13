#  版本说明

本页面记录了 Cloud Code 的正式版更新。您可以查看此页面，了解有关新增的功能、经过更新的功能、已弃用的功能、错误修复和已知问题的公告。

您也可以在 [ GitHub 版本说明页面 ](https://github.com/GoogleCloudPlatform/cloud-code-
intellij/blob/master/CHANGELOG.md) 上找到最近的更新。

您可以在 [ Google Cloud 版本说明 ](https://cloud.google.com/release-notes?hl=zh-cn)
页面上查看 Google Cloud 所有产品的最新产品动态。

如需接收最新产品动态，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接添加 Feed 网址： `
https://cloud.google.com/feeds/cloud-code-for-intellij-release-notes.xml `

##  18.5.1

PyCharm（Community 版和 Professional 版）中现在提供了 Cloud Code。您可以从 PyCharm 中浏览您的 Cloud
Storage 存储分区并与 Cloud Source Repositories 进行交互。更多 IDE 即将推出。

###  新增

  * 增加了重构插件，以便除了 IDEA 之外也在其他 JetBrains IDE 中提供与语言无关的功能（Cloud Storage、Cloud Source Repositories）。 [ 1896 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1896)

###  改动

  * 第一次手动取消安装托管式 Cloud SDK 后，每次加载 IDE 时，将不再安装该 SDK。 [ 2113 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2113)

###  修复

  * 修复了 2018.2 EAP 中的异常。 [ 2124 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2124)

##  18.4.1

###  新增

  * 让 Google Cloud Tools 插件为您管理 Cloud SDK - 包括下载、安装和更新。不再需要手动下载 SDK。 [ 673 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/673)
  * 通过内置的 Google Cloud Java BOM 支持，缓解依赖项版本冲突。增加了在添加 Google 客户端库时自动添加 BOM 的功能，并加入了 pom.xml 检查，以帮助管理依赖项版本冲突。 [ 1921 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1921)
  * 自动在 App Engine 本地运行配置中添加所需的环境变量，以便在本地访问 Google Cloud API。 [ 1917 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1917)

##  18.3.2

  * 修复了导致 2017.2 及更低版本的 IntelliJ IDEA 出现插件初始化错误的问题。 [ 1972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1972)

##  18.3.1

###  新增

  * 增加了通过 IDE 客户端库工作流创建服务帐号和下载服务帐号密钥的功能。 [ 1808 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1808)

###  修复

  * 修复了因缺少 ` web.xml ` 而未生成 ` appengine-web.xml ` 的问题。 [ 1903 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1903)

##  18.2.1

###  新增

  * 增加了从 IDE 发现和添加 Google Cloud Java 客户端库的功能。 [ 1806 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1806)
  * 增加了从 IDE 启用 Google Cloud API 的功能。 [ 1807 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1807)

###  改动

  * 更新了 Cloud 项目选择器，使用户体验得到显著改善。 [ 1719 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1719)
  * 更新了 Cloud 项目选择器，以使系统记住并默认采用上次的选择。 [ 1812 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1812)

###  修复

  * 修复了 App Engine 标准本地运行工件缺失的问题。 [ 1625 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1625)

##  18.1.1

###  修复

  * 修复了损坏的错误报告机制。 [ 1842 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1842)

##  17.12.2

###  修复

  * 修复了因分析属性设置损坏而导致分析丢失的问题。 [ 1773 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1773)

##  17.12.1

Google Account 插件现已合并到 Cloud Tools 插件中，不再需要单独安装。如果您以前安装了 Account Tools
插件，请按照新的对话框提示移除该插件并重启 IDE，以确保您不会遇到任何问题。

###  修复

  * 修复了在 Cloud 项目选择器中输入和搜索多个项目时出现的内存不足错误。 [ 1742 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1742)

###  改动

  * Google Account 插件现已集成到 Google Cloud Tools 插件中，不再需要单独安装。 [ 1735 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1735)

##  17.11.1

###  新增

  * 将 Cloud Storage 集成到了 IntelliJ 中。您现在无需离开 IDE 即可浏览您的存储分区并查看其内容。 [ 1696 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1696)
  * 在 Cloud 项目选择器中增加了搜索和过滤功能。 [ 1660 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1660)
  * 增加了新的“添加 App Engine 框架支持”工具菜单快捷方式，提供了另一种向项目添加 App Engine 支持的方法。 [ 1685 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1685)

###  修复

  * 修复了在未选择任何 Cloud 项目时出现的 App Engine 区域指示器状态消息。 [ 1607 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1607)

##  17.9.2

App Engine 标准环境中的 Java 8 现已 [ 正式发布
](https://cloudplatform.googleblog.com/2017/09/Java-8-on-App-Engine-Standard-
environment-is-now-generally-available.html) 。

###  改动

  * 更新了新的 App Engine 标准项目向导，使其默认生成 Java 8 应用。 [ 1641 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1641)

##  17.9.1

###  新增

  * 增加了为 App Engine 柔性部署更改暂存工件名称的功能。 [ 1610 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1610)

###  改动

  * 现在，App Engine 柔性部署配置默认按原样部署工件，无需重命名为 ` target.jar ` 或 ` target.war ` 。 [ 1151 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1151)
  * 更新了生成的 Dockerfile 模板中占位符工件的名称，明确指出该名称需要用户更新。 [ 1648 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1648)
  * App Engine 标准部署配置现在默认更新 dos、dispatch、cron、队列和数据存储区索引。 [ 1613 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1613)
  * 通过添加对适用于 App Engine 的 Endpoints Frameworks 的支持，原生项目现在使用 Endpoints V2。 [ 1612 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1612)

###  修复

  * 修复了部署 Maven 工件时发生的 ` Deployment source not found ` 错误。 [ 1220 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1220)
  * 修复了 HiDPI 显示屏上的用户图标比例。 [ 1633 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1633)
  * 修复了 IDEA 2017.3 EAP 版本中的插件降级问题。 [ 1631 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1631)

##  17.8.2

###  修复

  * 修复了在使用 Google 帐号登录时出现的“Error: invalid_scope”问题。 [ 1598 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1598)

##  17.8.1

###  新增

  * 在 Google Cloud Tools 快捷菜单中增加了反馈和问题报告链接。 [ 1560 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1560)

###  改动

  * 用户现在可以保存部分完成或处于错误状态的部署运行配置。 [ 1407 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1407)

###  修复

  * 修复了注册的 Docker 语言冲突，该冲突会导致插件与 .ignore 插件一起运行时出现问题。 [ 1535 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1535)
  * 修复了解析 Cloud Debugger 断点时间戳的 NPE。 [ 1537 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1537)
  * 从本地开发服务器运行的可接受 App Engine 工件类型中移除了 EAR。 [ 1190 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1190)
  * 现在，部署会在多个 IDE 窗口中显示。 [ 1432 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1432)
  * 修复了因尝试修改只读集合而导致的崩溃。 [ 1571 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1571)

##  17.6.2

###  修复

  * 修复了存在本地开发服务器配置但却没有标准构面时出现的 NPE。 [ 1525 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1525)

##  17.6.1

###  新增

  * 增加了使用 ` app.yaml ` 和 Dockerfile 配置的 App Engine 柔性构面。 [ 1514 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1514)
  * App Engine 柔性框架支持检测。 [ 1277 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1277)

###  改动

  * 允许用户为柔性部署指定 Docker 目录（而不仅仅是 Dockerfile）。 [ 1304 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1304)
  * 提供了新鲜的部署对话框（标准和柔性）用户体验。 [ 1477 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1477)

###  修复

  * 修复了 HiDPI 显示屏上的 Google 头像大小问题。 [ 1391 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1391)

##  17.2.5_2017

###  新增

  * App Engine 标准本地运行配置中的环境变量现在会传递到开发服务器。 [ #1364 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1364)
  * 在 appengine-web.xml 中配置的环境变量现在会被应用并传递到开发服务器。 [ #377 ](https://github.com/GoogleCloudPlatform/appengine-plugins-core/issues/377)

##  17.2.4_2017

###  新增

  * 增加了一个复选框，用于在服务部署期间部署所有 App Engine 配置文件。 [ #1346 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1346)

##  17.2.3_2017

###  改动

  * 从 App Engine 标准本地开发服务器配置中移除了“清除数据存储区”标志，因为当前的服务器版本不支持该标志。( [ #1345 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1345) ) 

##  17.2.2_2017

###  修复

  * 暂存 App Engine 标准应用时 Java 运行时环境 (JRE) 无效 ( [ #1316 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1316) )： 
    
        > Unable to stage app: Cannot get the System Java Compiler. Please use a JDK, not a JRE.
    

##  17.2.1

祝 Cloud Code 用户新年快乐！今年第一个版本的主题是维护。如果您在使用 Cloud Source Repositories
和我们的插件时遇到身份验证问题，请查看 [ 这个可能有帮助的解决方案
](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1174) 。

下方列出了明显的改动之处：

###  新增

  * 支持为单个 GCP 项目提供多个 Cloud Source Repositories 代码库。 ( [ #1024 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1024) ) 
  * App Engine 初始化和区域选择。 ( [ #1232 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1232) ) 

###  修复

  * 在 Windows 上停止 dev_appserver 始终会失败并引发 ` com.intellij.execution.ExecutionException ` 。 ( [ #1215 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1215) ) 
  * 新的 App Engine 标准项目向导应该会使用 servlet 2.5 生成 web.xml。( [ #1194 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1194) ) 
  * App Engine 标准本地服务器的“清除数据存储区”复选框不起作用。( [ #1188 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1188) ) 
  * 项目选择器中不显示已安排删除的项目。( [ #1119 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1119) ) 

如需了解完整详情，请访问我们的 [ 17.2 版本里程碑 ](https://github.com/GoogleCloudPlatform/google-
cloud-intellij/milestone/19?closed=1) 。

##  16.11.6

###  新增

  * 通过加入各种操作快捷方式扩展了 Google Cloud Tools 菜单项。( [ #1061 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1061) )。 
  * 检查支持的最低 Cloud SDK 版本。( [ #1051 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1051) )。 
  * 自动为 App Engine 标准应用创建所有相关的运行配置。( [ #1063 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1063) )。 
  * 在新项目向导中，App Engine 框架现在是 Web 框架的子项。( [ #1065 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1065) )。 

###  修复

  * 应用服务器部署面板中的唯一部署源现在显示为单独的专列项。( [ #821 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/821) )。 
  * 现在可在 Windows 上验证无效的 Cloud SDK 路径。 ( [ #1091 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1091) )。 

##  16.10.5

重要提示：此插件需要使用 Cloud SDK v 133.0.0 才能正确执行使用最新 Java 8 SDK 的本地开发服务器。请从您的 shell 运行
` gcloud components update ` ，以确保您拥有最新版本的 Cloud SDK。

###  修复

  * 修复了在服务器运行时进行更改所导致的本地开发服务器调试模式问题。( [ #972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/972) ) 
  * 当开发服务器的 Cloud SDK 路径无效时，向用户显示更明确的信息。( [ #1043 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1043) )。 
  * 将运行配置名称更新为带有“Google ..” ( [ #1021 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1021) )。 

##  16.10.1

  * 请注意，我们将更改版本控制方案，采用年-月-编号 (YY.MM.i) 的格式。我们计划每月发布一个版本，尽量减少更新中断。另请注意，我们已经删除了“Beta 版”标签。 
  * 注意：使用最新的 JDK 8 版本时，本地 App Engine 开发服务器会中断。 ( [ #920 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/920) )。 下一个版本的 App Engine SDK 即将推出，届时此问题应该会得到修复。 

###  新增

  * 在“构面和项目”(Facet and Project) 向导中添加了 App Engine 标准库导入工具。 ( [ #866 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/866) ) 
  * 使用 Java 8 语言的标准 App Engine 应用将收到使用 Java 7 语言的通知 ( [ #966 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/966) ) 

###  改动

  * 更新了运行配置标签和图标。（Cloud Debugger 现在更名为 Stackdriver Debug）( [ #936 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/936) ) 

###  修复

  * 修复了本地开发服务器调试模式。 ( [ #928 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/928) ) 
  * 修复了在 Windows 10 上柔性部署中断的问题。 ( [ #937 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/937) ) 
  * Cloud Debugger 对象检查器再次生效。 ( [ #929 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/929) ) 
  * 修复了导致 NPE 的 Cloud Debugger 快照时间戳 ( [ #919 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/919) ) 

##  1.0-beta - 2016-09-14

###  新增

  * 增加了对 App Engine 标准环境的支持 ( [ #767 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/767) ) 
  * 部署配置中现在提供更多字段 ( [ #868 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/868) ) 

##  0.9.7.5-beta - 2016-08-29

###  新增

  * 检查确保部署对拥有凭据的用户有效，并提示添加新用户（如果没有）。 ( [ 837 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/837) ) 

##  0.9.6-beta - 2016-06-23

###  新增

  * 支持部署到 App Engine 柔性兼容环境。 __ ( [ #720 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/720) ) 
  * 支持部署到 App Engine 标准环境。 ( [ #665 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/665) ) 
  * 检查 Cloud Tools 和 Account 插件兼容性。 ( [ #651 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/650) ) 

###  改动

  * 移动了版本输入位置，使其成为部署配置对话框中的顶层配置。 ( [ #639 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/639) ) 

##  0.9.4-beta - 2016-04-20

###  新增

  * 增加了部署到 App Engine 柔性环境工具菜单项的功能。 ( [ #635 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/635) ) 
  * 支持基于 Maven 的项目作为 App Engine 柔性环境部署的部署源 ( [ #600 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/600) ) 

###  改动

  * 您可以通过断开与 App Engine 应用服务器的连接，来取消 App Engine 柔性环境部署。( [ #581 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/581) ) 
  * App Engine 柔性环境生成的 Dockerfile 和 ` app.yaml ` 现在默认为 Maven 结构化 Java 项目中的推荐位置。( [ #575 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/575) ) 

###  修复

  * 修复了可能会导致在添加用户时未选择活跃用户的登录错误。( [ #644 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/644) ) 
  * 修复了取消 App Engine 部署可能会引发错误的问题。 ( [ #599 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/599) ) 

