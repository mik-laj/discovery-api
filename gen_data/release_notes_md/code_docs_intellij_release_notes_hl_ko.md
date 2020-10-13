#  출시 노트

이 페이지에는 Cloud Code의 프로덕션 업데이트가 정리되어 있습니다. 새로운 기능이나 업데이트된 기능, 버그 수정, 알려진 문제, 지원
중단된 기능에 대한 공지를 볼 수 있습니다.

최신 업데이트는 [ GitHub 출시 노트 페이지 ](https://github.com/GoogleCloudPlatform/cloud-
code-intellij/blob/master/CHANGELOG.md) 에서도 확인할 수 있습니다.

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서 모든
Google Cloud의 최신 제품 업데이트를 확인할 수 있습니다.

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL( ` https://cloud.google.com/feeds/cloud-code-for-intellij-
release-notes.xml ` )을 직접 추가하세요.

##  18.5.1

이제 PyCharm(Community 및 Professional)에서 Cloud Code를 사용할 수 있습니다. PyCharm에서 Cloud
Storage 버킷을 탐색하고 Cloud Source Repositories와 상호작용할 수 있습니다. 더 많은 IDE가 제공될 예정입니다.

###  추가됨

  * IDEA 외에 다른 JetBrains IDE에서도 언어에 구애되지 않는 기능(Cloud Storage, Cloud Source Repositories)을 사용할 수 있도록 리팩터링된 플러그인이 추가되었습니다. [ 1896 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1896)

###  변경됨

  * 첫 번째 수동 취소 후 각 IDE 로드에 관리형 Cloud SDK가 더 이상 설치되지 않습니다. [ 2113 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2113)

###  수정됨

  * 2018.2 EAP의 예외가 수정되었습니다. [ 2124 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2124)

##  18.4.1

###  추가됨

  * Google Cloud 도구 플러그인이 사용자 대신 다운로드, 설치, 업데이트 같은 Cloud SDK 관리를 할 수 있습니다. 더 이상 SDK를 수동으로 다운로드할 필요가 없습니다. [ 673 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/673)
  * 기본 제공되는 Google Cloud 자바 BOM 지원과의 종속 항목 버전 충돌을 완화합니다. Google 클라이언트 라이브러리를 추가할 때 BOM의 자동 추가와 종속 항목 버전 충돌을 관리하는 데 도움이 되는 pom.xml 검사가 포함됩니다. [ 1921 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1921)
  * Google Cloud API에 로컬로 액세스하는 데 필요한 환경 변수가 App Engine 로컬 실행 구성에 자동으로 추가됩니다. [ 1917 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1917)

##  18.3.2

  * IntelliJ IDEA 2017.2 이하 버전에서 플러그인 초기화 오류를 발생시키는 버그가 수정되었습니다. [ 1972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1972)

##  18.3.1

###  추가됨

  * IDE 클라이언트 라이브러리 워크플로에서 서비스 계정을 만들고 서비스 계정 키를 다운로드하는 기능이 추가되었습니다. [ 1808 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1808)

###  수정됨

  * ` web.xml ` 이 누락되어 ` appengine-web.xml ` 이 생성되지 않는 오류가 수정되었습니다. [ 1903 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1903)

##  18.2.1

###  추가됨

  * IDE에서 Google Cloud 자바 클라이언트 라이브러리 검색 및 추가 기능이 추가되었습니다. [ 1806 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1806)
  * IDE에서 Google Cloud API를 사용 설정하는 기능이 추가되었습니다. [ 1807 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1807)

###  변경됨

  * 클라우드 프로젝트 선택기가 크게 향상된 사용자 환경으로 업데이트되었습니다. [ 1719 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1719)
  * 클라우드 프로젝트 선택기에서 마지막 선택을 기억해 기본값으로 설정하도록 업데이트되었습니다. [ 1812 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1812)

###  수정됨

  * 누락된 App Engine 표준 로컬 실행 아티팩트가 수정되었습니다. [ 1625 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1625)

##  18.1.1

###  수정됨

  * 잘못된 오류 보고 메커니즘이 수정되었습니다. [ 1842 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1842)

##  17.12.2

###  수정됨

  * 분석 중단을 일으키는 잘못된 분석 속성 설정이 수정되었습니다. [ 1773 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1773)

##  17.12.1

Google 계정 플러그인이 이제 Cloud 도구 플러그인에 병합되어 별도로 설치하지 않습니다. 이전에 계정 도구 플러그인을 설치한 경우 새
대화상자의 메시지에 따라 해당 플러그인을 제거하고 IDE를 다시 시작하여 문제가 발생하지 않게 하세요.

###  수정됨

  * 클라우드 프로젝트 선택기에서 여러 프로젝트를 입력하고 검색할 때의 메모리 부족 오류가 수정되었습니다. [ 1742 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1742)

###  변경됨

  * Google 계정 플러그인이 이제 Google Cloud 도구 플러그인에 병합되었습니다. 더 이상 별도의 Google 계정 플러그인 설치가 필요하지 않습니다. [ 1735 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1735)

##  17.11.1

###  추가됨

  * Cloud Storage가 IntelliJ에 통합되었습니다. 이제 IDE를 벗어나지 않고 버킷을 탐색하고 콘텐츠를 볼 수 있습니다. [ 1696 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1696)
  * 클라우드 프로젝트 선택기의 검색 및 필터링 기능. [ 1660 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1660)
  * 새로운 'App Engine 프레임워크 지원 추가' 도구 메뉴 바로가기로 프로젝트에 App Engine 지원을 추가하는 새로운 방법을 제공합니다. [ 1685 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1685)

###  수정됨

  * 클라우드 프로젝트가 선택되지 않았을 때 표시되는 App Engine 지역 표시기 상태 메시지가 수정되었습니다. [ 1607 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1607)

##  17.9.2

이제 App Engine 표준 환경의 자바 8이 [ 일반 공개
](https://cloudplatform.googleblog.com/2017/09/Java-8-on-App-Engine-Standard-
environment-is-now-generally-available.html) 되었습니다.

###  변경됨

  * 새로운 App Engine 표준 프로젝트 마법사가 기본적으로 자바 8 애플리케이션을 생성하도록 업데이트되었습니다. [ 1641 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1641)

##  17.9.1

###  추가됨

  * App Engine 가변형 배포를 위해 스테이징된 아티팩트의 이름을 변경할 수 있는 기능이 추가되었습니다. [ 1610 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1610)

###  변경됨

  * App Engine 가변형 배포 구성이 이제 아티팩트의 이름을 ` target.jar ` 또는 ` target.war ` 로 변경하지 않고 그대로 배포하도록 기본 설정됩니다. [ 1151 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1151)
  * 생성된 Dockerfile 템플릿에서 사용자가 자리표시자 아티팩트 이름을 업데이트해야 한다는 점을 분명히 하도록 업데이트되었습니다. [ 1648 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1648)
  * App Engine 표준 배포 구성이 이제 DoS, dispatch, cron, queues, datastore 색인을 업데이트하도록 기본 설정되어 있습니다. [ 1613 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1613)
  * App Engine용 Endpoints Frameworks에 대한 지원을 추가하는 네이티브 프로젝트에서 이제 Endpoints V2를 사용합니다. [ 1612 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1612)

###  수정됨

  * Maven 아티팩트를 배포할 때의 ` Deployment source not found ` 오류가 수정되었습니다. [ 1220 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1220)
  * HiDPI 디스플레이에서 사용자 아이콘의 크기가 수정되었습니다. [ 1633 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1633)
  * IDEA 2017.3 EAP에서 플러그인이 다운그레이드된 문제가 수정되었습니다. [ 1631 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1631)

##  17.8.2

###  수정됨

  * Google 계정으로 로그인할 때의 '오류: invalid_scope' 문제가 수정되었습니다. [ 1598 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1598)

##  17.8.1

###  추가됨

  * Google Cloud 도구 바로가기 메뉴에 의견 보내기 및 문제 보고 링크가 추가되었습니다. [ 1560 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1560)

###  변경됨

  * 사용자는 이제 부분적으로 완료되었거나 오류 상태인 배포 실행 구성을 저장할 수 있습니다. [ 1407 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1407)

###  수정됨

  * 플러그인을 .ignore 플러그인과 함께 실행하여 등록된 Docker 언어 충돌을 유발하는 문제가 수정되었습니다. [ 1535 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1535)
  * NPE 파싱 Cloud Debugger 중단점 타임스탬프가 수정되었습니다. [ 1537 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1537)
  * 로컬 개발 서버 실행에 적합한 App Engine 아티팩트 유형으로서 EAR가 제거되었습니다. [ 1190 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1190)
  * 배포가 이제 여러 IDE 창에 표시됩니다. [ 1432 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1432)
  * 읽기 전용 컬렉션을 수정하려고 시도하여 발생한 충돌이 수정되었습니다. [ 1571 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1571)

##  17.6.2

###  수정됨

  * 로컬 개발 서버 구성이 있지만 표준 속성이 없는 경우에 발생하는 NPE가 수정되었습니다. [ 1525 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1525)

##  17.6.1

###  추가됨

  * ` app.yaml ` 및 Dockerfile 구성이 포함된 App Engine 가변형 속성이 추가되었습니다. [ 1514 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1514)
  * App Engine 가변형 프레임워크 지원 감지가 추가되었습니다. [ 1277 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1277)

###  변경됨

  * 가변형 배포를 위해 사용자가 Dockerfile만 지정하는 대신 Docker 디렉토리를 지정할 수 있도록 허용됩니다. [ 1304 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1304)
  * 표준 및 가변형 배포 대화상자의 사용자 환경을 새로고칩니다. [ 1477 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1477)

###  수정됨

  * HiDPI 디스플레이의 Google 아바타 크기가 수정되었습니다. [ 1391 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1391)

##  17.2.5_2017

###  추가됨

  * 이제 App Engine 표준 로컬 실행 구성의 환경 변수가 개발 서버로 전달됩니다. [ #1364 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1364)
  * appengine-web.xml에 구성된 환경 변수가 이제 적용되어 개발 서버로 전달됩니다. [ #377 ](https://github.com/GoogleCloudPlatform/appengine-plugins-core/issues/377)

##  17.2.4_2017

###  추가됨

  * 서비스 배포 중에 모든 App Engine 구성 파일을 배포하는 체크박스가 추가되었습니다. [ #1346 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1346)

##  17.2.3_2017

###  변경됨

  * 서버의 현재 버전에서 Datastore 삭제 플래그를 지원하지 않기 때문에 App Engine 표준 로컬 개발 서버 구성에서 이 플래그가 제거되었습니다. ( [ #1345 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1345) ) 

##  17.2.2_2017

###  수정됨

  * App Engine 표준 앱을 스테이징하는 중의 잘못된 자바 런타임 환경(JRE)이 수정되었습니다. ( [ #1316 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1316) ) 
    
        > Unable to stage app: Cannot get the System Java Compiler. Please use a JDK, not a JRE.
    

##  17.2.1

Cloud Code 사용자를 위한 새해 소식입니다. 올해의 첫 번째 출시는 주로 유지관리 중심입니다. Cloud Source
Repositories와 플러그인을 사용하는 데 인증 문제가 있으면 [ 가능한 솔루션
](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1174) 을
확인하세요.

가시적인 변경사항의 목록은 다음과 같습니다.

###  추가됨

  * 단일 GCP 프로젝트를 위한 여러 Cloud Source Repositories에 대한 지원이 추가되었습니다. ( [ #1024 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1024) ) 
  * App Engine 초기화 및 영역 선택을 할 수 있습니다. ( [ #1232 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1232) ) 

###  수정됨

  * Windows에서 dev_appserver를 중지하면 항상 ` com.intellij.execution.ExecutionException ` 과 함께 실패하는 문제가 수정되었습니다. ( [ #1215 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1215) ) 
  * 새로운 App Engine 표준 프로젝트 마법사는 서블릿 2.5를 사용하여 web.xml을 생성합니다. ( [ #1194 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1194) ) 
  * App Engine 표준 로컬 서버의 Datastore 삭제 체크박스가 작동하지 않는 문제를 수정했습니다. ( [ #1188 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1188) ) 
  * 프로젝트 선택기에서 삭제 예정인 프로젝트가 표시되지 않습니다. ( [ #1119 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1119) ) 

전체 내용을 보려면 [ 17.2 출시 중요 단계 ](https://github.com/GoogleCloudPlatform/google-
cloud-intellij/milestone/19?closed=1) 를 방문하세요.

##  16.11.6

###  추가됨

  * 다양한 작업 바로가기를 사용하는 확장된 Google Cloud 도구 메뉴 항목이 추가되었습니다. ( [ #1061 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1061) ) 
  * 최소 지원 Cloud SDK 버전을 확인합니다. ( [ #1051 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1051) ) 
  * App Engine 표준 앱의 모든 관련 실행 구성이 자동으로 생성됩니다. ( [ #1063 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1063) ) 
  * App Engine 프레임워크는 이제 새로운 프로젝트 마법사에서 웹 프레임워크의 하위 요소입니다. ( [ #1065 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1065) ) 

###  수정됨

  * 애플리케이션 배포 패널의 고유한 배포 소스가 이제 별도의 개별 항목으로 표시됩니다. ( [ #821 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/821) ) 
  * Windows에서 유효하지 않은 Cloud SDK 경로의 유효성을 검사합니다. ( [ #1091 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1091) ) 

##  16.10.5

중요: 이 플러그인은 최신 자바 8 SDK를 사용하여 로컬 개발 서버를 올바르게 실행하기 위해 Cloud SDK 버전 133.0.0을
사용해야 합니다. 최신 Cloud SDK 버전인지 확인하려면 셸에서 ` gcloud components update ` 를 실행하세요.

###  수정됨

  * 서버가 실행되는 중에 변경이 이루어질 경우 로컬 개발 서버 디버그 모드의 문제가 수정되었습니다. ( [ #972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/972) ) 
  * 개발 서버에 잘못된 Cloud SDK 경로가 있을 때 표시되는 메시지가 개선되었습니다. ( [ #1043 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1043) ) 
  * 실행 구성 이름에 'Google…'이라는 프리픽스가 포함되도록 업데이트되었습니다. ( [ #1021 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1021) ) 

##  16.10.1

  * 버전 관리 체계를 YY.MM.i로 변경합니다. 업데이트의 중단을 최소화하기 위해 월 단위 출시 주기를 계획하고 있습니다. 또한 'Beta' 라벨을 삭제했습니다. 
  * 주의: 로컬 App Engine 개발 서버가 최신 JDK 8 출시와 호환되지 않습니다. ( [ #920 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/920) ). 이 문제는 곧 예정된 다음 App Engine SDK 출시와 함께 수정될 예정입니다. 

###  추가됨

  * 속성 및 프로젝트 마법사의 App Engine 표준 라이브러리 가져오기 도구가 추가되었습니다. ( [ #866 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/866) ) 
  * 자바 8 언어 수준을 사용하는 표준 App Engine 앱에 언어 수준 7을 사용하도록 알림이 전송됩니다. ( [ #966 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/966) ) 

###  변경됨

  * 실행 구성 라벨 및 아이콘이 업데이트되었습니다. Cloud Debugger는 이제 Cloud Debugger입니다. ( [ #936 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/936) ) 

###  수정됨

  * 로컬 개발 서버 디버그 모드가 수정되었습니다. ( [ #928 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/928) ) 
  * Windows 10에서 손상된 Flex 배포가 수정되었습니다. ( [ #937 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/937) ) 
  * Cloud Debugger 객체 검사기가 다시 작동합니다. ( [ #929 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/929) ) 
  * NPE를 유발하는 Cloud Debugger 스냅샷 타임스탬프가 수정되었습니다. ( [ #919 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/919) ) 

##  1.0-beta - 2016-09-14

###  추가됨

  * App Engine 표준 환경 지원이 추가되었습니다. ( [ #767 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/767) ) 
  * 이제 배포 구성에서 추가 필드를 사용할 수 있습니다. ( [ #868 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/868) ) 

##  0.9.7.5-beta - 2016-08-29

###  추가됨

  * 인증된 사용자에게 배포가 유효한지 확인하고 그렇지 않으면 새 사용자를 추가하라는 메시지가 표시됩니다. ( [ 837 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/837) ) 

##  0.9.6-beta - 2016-06-23

###  추가됨

  * App Engine 가변형 _compat_ 환경 배포 지원이 추가되었습니다. ( [ #720 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/720) ) 
  * App Engine 표준 환경 배포 지원이 추가되었습니다. ( [ #665 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/665) ) 
  * Cloud 도구 및 계정 플러그인 호환성을 확인합니다. ( [ #651 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/650) ) 

###  변경됨

  * 버전 입력이 배포 구성 대화상자 내의 최상위 구성으로 이동했습니다. ( [ #639 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/639) ) 

##  0.9.4-beta - 2016-04-20

###  추가됨

  * App Engine 가변형 환경에 배포 도구 메뉴 항목이 추가되었습니다. ( [ #635 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/635) ) 
  * App Engine 가변형 환경 배포를 위한 배포 소스로서 Maven 기반 프로젝트에 대한 지원이 추가되었습니다. ( [ #600 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/600) ) 

###  변경됨

  * App Engine 애플리케이션 서버에서 연결을 해제하여 App Engine 가변형 환경 배포를 취소할 수 있습니다. ( [ #581 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/581) ) 
  * App Engine 가변형 환경에서 생성된 Dockerfile과 ` app.yaml ` 이 이제 Maven 구조의 자바 프로젝트에서 권장 위치로 기본 설정됩니다. ( [ #575 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/575) ) 

###  수정됨

  * 사용자를 추가할 때 활성 사용자가 선택되지 않을 수 있는 로그인 버그가 수정되었습니다. ( [ #644 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/644) ) 
  * App Engine 배포를 취소하면 오류가 발생할 수 있던 문제를 수정하였습니다. ( [ #599 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/599) ) 

