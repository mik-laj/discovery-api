**참고:** 이 제품의 일부 요소는 베타 버전입니다. 하이브리드 설치 옵션은 GA입니다. 베타 프로그램에 참여하려면 Apigee 담당자에게
문의하세요.

#  1.2.0 - Apigee Hybrid 런타임 출시 노트

2020년 4월 3일, Apigee Hybrid 런타임 버전 1.2.0이 출시되었습니다.

자세한 내용은 다음 리소스를 참조하세요.

  * _[ 하이브리드 자세히 알아보기 ](https://cloud.google.com/apigee/docs/hybrid/v1.2/what-is-hybrid?hl=ko) _ 또는 _[ 설치 시작 ](https://cloud.google.com/apigee/docs/hybrid/v1.2/big-picture?hl=ko) _
  * _유료 계정 만들기:_ [ Apigee 영업팀 ](https://pages.apigee.com/contact-sales-reg.html?hl=ko) 에 문의하기 
  * _질문 또는 문제:_ [ Apigee 지원팀 ](https://cloud.google.com/apigee/support/?hl=ko) 에 문의하기 

####  도움말 및 알림

**프라이빗 클라우드 고객** : 이 클라우드 출시 버전이 프라이빗 클라우드 버전에 포함되어 있는지 확인하세요. 버전에 포함된 클라우드 출시
버전을 보려면 버전 출시 노트를 참조하세요. 또한 출시 버전 번호를 비교하여 이를 알아보는 방법은 [ 출시 버전 번호 지정 정보
](https://cloud.google.com/apigee/docs/release/apigee-edge-release-
process?hl=ko#aboutreleasenumbering) 를 참조하세요.

**질문 또는 문제:** [ 여기에서 도움을 받으세요
](https://cloud.google.com/apigee/support/?hl=ko) .

**출시 알림** : [ http://status.apigee.com ](http://status.apigee.com?hl=ko) 으로
이동하여 **업데이트 구독** 을 클릭합니다.

[ 출시 노트 홈페이지 ](https://cloud.google.com/apigee/docs/release/notes/apigee-
release-notes?hl=ko)

##  업그레이드

버전 1.1.1에서 1.2.0으로 업그레이드하려면 버전 1.1.1과 호환되지 않는 재정의 파일에서 변경 작업을 수행해야 합니다. 재정의
파일의 변경을 수행하는 것은 업그레이드를 수행하기 위한 기본 요건입니다. 새로운 구성은 API 호출이 잘못된 환경으로 라우팅되는 문제를
해결합니다. 자세한 내용은 [ Apigee Hybrid 업그레이드
](https://cloud.google.com/apigee/docs/hybrid/v1.2/upgrade?hl=ko) 를 참조하세요.

##  새로운 기능 및 업데이트

다음은 이번 출시의 새로운 기능과 업데이트입니다.

###  라우팅 규칙을 지정하기 위해 새로운 가상 호스트 구성 추가

새로운 ` virtualhosts ` 구성 기능은 기본 경로가 여러 환경으로 라우팅되는 순서가 불확실한 문제를 해결합니다. 자세한 내용은 [
가상 호스트 구성 ](https://cloud.google.com/apigee/docs/hybrid/v1.2/base-path-
routing?hl=ko) 을 참조하세요. (150336519)

###  OASValidation 정책 베타 출시

OASValidation(OpenAPI 사양 유효성 검사) 정책(베타)을 사용하면 OpenAPI 3.0 사양(JSON 또는 YAML)에 대한
수신 요청 또는 응답 메시지의 유효성을 검사할 수 있습니다. 자세한 내용은 [ OASValidation 정책(베타)
](https://cloud.google.com/apigee/docs/api-platform/reference/policies/oas-
validation-policy?hl=ko) 을 참조하세요. (144949685)

###  WebSocket 지원 베타 출시

Apigee Hybrid는 WebSocket 연결을 지원합니다. 이제 API 프록시 클라이언트가 HTTP에서 WebSockets로 프로토콜
업그레이드를 요청할 수 있습니다. 자세한 내용은 [ WebSocket 사용(베타)
](https://cloud.google.com/apigee/docs/hybrid/v1.2/websockets?hl=ko) 을 참조하세요.

###  Kubernetes 보안 비밀에서 정책 보안 비밀 값에 액세스

새로운 기능을 사용하면 프록시 흐름 변수의 Kubernetes 보안 비밀에 저장된 값에 액세스할 수 있습니다. 자세한 내용은 [
Kubernetes 보안 비밀에 데이터 저장
](https://cloud.google.com/apigee/docs/hybrid/v1.2/k8s-secrets?hl=ko) 을 참조하세요.
(133377603)

###  ADAC 및 ADAH를 대체하는 Apigee Operators(AO) 요소

Apigee Operators(AO)는 AD를 배포하고 유지하는 데 필요한 하위 수준 Kubernetes 및 Istio 리소스를 만들고
업데이트합니다. 예를 들어 컨트롤러는 메시지 프로세서의 출시를 수행합니다. 또한 ApigeeDeployment 구성을 Kubernetes
클러스터에서 유지하기 전에 검증합니다. AO는 Apigee 배포 Admissionhook(ADAH) 및 Apigee 배포 컨트롤러(ADC)를
대체합니다. [ 구성 속성 참조에 있는 AO
](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref?hl=ko#ao) 를
참조하세요. (151250559)

###  특정 클러스터 및 프로젝트 구성 속성 교체 및 지원 중단

2개의 새로운 구성 속성, ` k8sCluster ` 와 ` gcp ` 가 추가되었습니다. 이러한 속성은 지원 중단된 `
k8sClusterName ` , ` gcpRegion ` , ` gcpProjectID ` 속성을 대체합니다. 자세한 내용은 [ 구성 속성
참조 ](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref?hl=ko) 를
참조하세요. (146299599)

###  Kubernetes 기반 Cassandra의 영구 볼륨 확장

스토리지 요구사항을 충족하기 위해 더 많은 노드를 추가하지 않고도 apigee-cassandra에서 사용하는 영구 볼륨을 확장할 수 있는
프로세스가 추가되었습니다. [ Cassandra 영구 볼륨 확장
](https://cloud.google.com/apigee/docs/hybrid/v1.2/expand-persistent-
volumes?hl=ko) 을 참조하세요. (138167919)

###  인증서, 암호화 키, SA를 위한 추가 소스 지원

TLS 인증서, 암호화 키, 서비스 계정 키를 더 유연하게 지정할 수 있도록 해주는 새로운 구성 속성이 추가되었습니다. 새 속성은 다음과
같습니다.

  * ` kmsEncryptionPath `
  * ` kmsEncryptionSecret.key `
  * ` kmsEncryptionSecret.name `
  * ` cassandra.backup.serviceAccountSecretRef `
  * ` cassandra.restore.serviceAccountSecretRef `
  * ` envs[].cacheEncryptionPath `
  * ` envs[].cacheEncryptionSecret.key `
  * ` envs[].cacheEncryptionSecret.name `
  * ` envs[].kmsEncryptionPath `
  * ` envs[].kmsEncryptionSecret.key `
  * ` envs[].kmsEncryptionSecret.name `
  * ` envs[].serviceAccountSecretRefs.synchronizer `
  * ` envs[].serviceAccountSecretRefs.udca `
  * ` envs[].sslSecret `
  * ` logger.serviceAccountSecretRef `
  * ` mart.serviceAccountSecretRef `
  * ` mart.sslSecret `
  * ` metrics.serviceAccountSecretRef `
  * ` synchronizer.serviceAccountSecretRef `
  * ` udca.serviceAccountSecretRef `

자세한 내용은 [ 구성 속성 참조 ](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-
prop-ref?hl=ko) 를 참조하세요. (145303466)

###  분석하기 위해 데이터를 보내기 전에 데이터를 난독화

특정 분석 데이터를 관리 영역으로 전송되기 전에 난독화할 수 있는 기능이 추가되었습니다. 자세한 내용은 [ 분석을 위한 사용자 데이터 난독화
](https://cloud.google.com/apigee/docs/hybrid/v1.2/obfuscate-userdata-for-
analytics?hl=ko) 를 참조하세요. (142578910)

###  StatefulSets의 영구 볼륨 확장

스토리지 요구를 충족하기 위해 더 많은 컴퓨팅 성능을 추가하지 않고도 apigee-cassandra에서 사용하는 영구 볼륨을 확장할 수 있는
기능이 추가되었습니다. 자세한 내용은 [ StatefulSets의 영구 볼륨 확장
](https://cloud.google.com/apigee/docs/release/notes/hybrid/v1.2/expand-
persistent-volumes?hl=ko) 을 참조하세요. (138167919)

###  업그레이드된 GKE, Anthos, AKS의 지원되는 최소 버전

Apigee Hybrid는 이제 GKE 1.14.x, Anthos 1.2, AKS 1.14.x를 지원합니다. (149578101)

###  상위 연결을 위한 TLS 1.3 지원

2개의 새로운 구성 속성을 사용하여 인그레스의 최소( ` ingress.minTLSProtocolVersion ` ) 및 최대( `
maxTLSProtocolVersion ` ) TLS 버전을 설정할 수 있습니다. 가능한 값은 1.0, 1.1, 1.2, 1.3입니다.
자세한 내용은 [ 구성 속성 참조 ](https://cloud.google.com/apigee/docs/hybrid/v1.2/config-
prop-ref?hl=ko) 를 참조하세요. (117580780)

###  하이브리드 런타임을 위한 전달 프록시 구성 지원

이제 환경에 배포된 API 프록시에서 HTTP 전달 프록시가 지원됩니다. 자세한 내용은 [ 전달 프록시 구성
](https://cloud.google.com/apigee/docs/hybrid/v1.2/forward-proxy?hl=ko) 을
참조하세요. (148970527)

###  환경별로 여러 hostAliases 지원

새 구성 속성 ` envs[].hostAliases ` 가 추가되었습니다. 이 속성을 사용하면 환경에 여러 호스트 별칭을 추가할 수
있습니다. 지원 중단된 ` hostAlias ` 대신 이 요소를 사용하세요. 자세한 내용은 [ 환경에 여러 호스트 별칭 추가
](https://cloud.google.com/apigee/docs/hybrid/v1.2/environment-
create?hl=ko#adding-multiple-host-aliases-to-an-environment) 를 참조하세요.
(150738495)

###  속성 세트에 템플릿 허용

새 요소 <PropertySetRef>가 <AssignMessage> 정책의 <AssignVariable> 요소에 추가되었습니다.
<PropertySetRef>를 사용하면 속성 세트 이름/키 쌍을 동적으로 만들 수 있습니다. 이 기능은 Apigee Hybrid에 배포된
API 프록시에서만 사용할 수 있습니다. [ AssignVariable
](https://cloud.google.com/apigee/docs/api-platform/reference/policies/assign-
message-policy?hl=ko#assignvariable) 을 참조하세요. (148612340)

##  수정된 버그

이번 출시에서는 다음 버그가 수정되었습니다. 이 목록은 주로 지원 티켓이 수정되었는지 확인하는 사용자를 위한 것입니다. 모든 사용자에게
자세한 정보를 제공하기 위한 것은 아닙니다.

문제 ID  |  구성요소 이름  |  설명  
---|---|---  
147958049  |  런타임  |  간혹 동기화 도구가 제대로 시작되지 않도록 하던 런타임 시작 시퀀싱의 타이밍 문제가 해결되었습니다.  
149867244  |  K8S 플랫폼  |  멀티 리전 설정에서 apigee-cps-setup pod가 작동하지 않습니다.  
150187652 / 149117839  |  런타임  |  환경 이름에 하이픈을 사용할 수 없습니다.  
149220463  |  MP pod  |  이전에 배포된 프록시가 다시 배포되어야 했습니다.  
144321144  |  런타임  |  안전한 가상 호스트가 있는 프록시를 다시 로드할 수 없습니다.  
147685310  |  런타임  |  초기화 중 GCP 토큰 가져오기의 실패로 인한 동기화 도구 초기화의 실패가 발생하였습니다.  
151115900  |  런타임  |  HybridMART에 대해 주기적 내부 프로브가 발생하지 않아 거짓양성 결과가 나타났습니다.  
  
##  알려진 문제

다음 표에서는 이번 출시 버전의 알려진 문제를 설명합니다.

문제  |  설명  
---|---  
해당 없음  |

잘못된 HTTP 헤더 오류: Istio 인그레스는 모든 수신 대상 응답을 HTTP2 프로토콜로 전환합니다. 하이브리드 메시지 프로세서는
HTTP1만 지원하므로 API 프록시가 호출되면 다음 오류가 표시될 수 있습니다.

    
    
    
    http2 error: Invalid HTTP header field was received: frame type: 1, stream: 1,
       name: [:authority], value: [domain_name]

이 오류가 표시되면 다음 작업 중 하나를 수행하여 문제를 해결할 수 있습니다.

  * 응답에서 호스트 헤더를 생략하도록 대상 서비스를 수정합니다. 
  * 필요한 경우 API 프록시에서 AssignMessage 정책을 사용하여 호스트 헤더를 삭제합니다. 

  
144584813  |  디버그 세션을 만들었지만 세션에 아직 트랜잭션이 없으면 [ List Debug Sessions API
](https://cloud.google.com/hybrid/v1.2/reference/apis/rest/v1/organizations.environments.apis.revisions.debugsessions/list?hl=ko)
에는 이 목록에 있는 세션이 포함되지 않습니다. API는 세션에 하나 이상의 트랜잭션이 포함된 경우에만 응답에 세션을 포함합니다.  
143659917  |

PopulateCache 정책의 만료 설정은 1~30 사이의 명시적 값으로 설정되어야 합니다. 예:

    
    
    
    <ExpirySettings>
      <TimeoutInSec>30</TimeoutInSec>
    </ExpirySettings>  
  
133192879  |

요약: API 또는 UI를 사용하여 조직의 배포 상태를 가져올 때 지연 시간은 매우 깁니다. 이 지연 시간으로 인해 ` HTTP 204
(No Content) ` 또는 ` HTTP 400 (Bad Request) ` 응답이 발생할 수 있습니다.

해결 방법: 브라우저를 새로고침하거나 요청을 다시 보냅니다.

