#  보안 게시판

이 주제에서는 Google Kubernetes Engine(GKE)의 모든 보안 게시판에 대해 설명합니다.

취약점은 영향을 받는 당사자가 대처 방안을 마련할 수 있을 때까지 엠바고에 따라 비밀로 유지되는 경우가 많습니다. 이 경우 GKE의 [ 출시
노트 ](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=ko) 에서
이러한 취약점은 엠바고가 해제될 때까지 '보안 업데이트'로 지칭됩니다. 엠바고가 해제되면 패치가 해결한 취약점을 반영하여 출시 노트가
업데이트됩니다.

**참고:** GKE에서 멀티 테넌트 워크로드를 실행할 경우 해당 게시판에 각별히 유의하시기 바랍니다. 취약점이 멀티 테넌트 워크로드에
영향을 미칠 가능성이 크기 때문입니다. GKE의 보안 경계에 대한 기술적 설명과 이에 따라 워크로드가 받는 영향에 대해서는 [
Kubernetes 스택 내 여러 레이어의 격리
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) 를 참조하세요.

최신 보안 게시판을 보려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL을 다음과 같이 직접 추가하세요. ` https://cloud.google.com/feeds/kubernetes-
engine-security-bulletins.xml `

##  GCP-2020-007

**게시:** 2020년 6월 1일  
설명  |  심각도  |  참고  
---|---|---  
  
승인된 특정 사용자가 제어 영역 호스트 네트워크의 민감한 정보를 500바이트까지 유출할 수 있는 서버 측 요청 위조(SSRF) 취약점( [
CVE-2020-8555 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)
)이 최근 Kubernetes에서 감지되었습니다. Google Kubernetes Engine(GKE) 제어 영역은 Kubernetes의
컨트롤러를 사용하기 때문에 이 취약점의 영향을 받습니다. 아래의 세부정보를 참고하여 제어 영역을 최신 패치 버전으로 [ 업그레이드
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=ko) 하는 것이 좋습니다. 노드 업그레이드는 필요하지 않습니다.  

####  어떻게 해야 하나요?

대부분 고객의 경우 추가 조치는 필요하지 않습니다. 대다수의 클러스터가 이미 패치 버전을 실행하고 있습니다. 이 취약점의 수정사항이 포함된
GKE 버전은 다음과 같습니다.

  * 1.14.7-gke.39 
  * 1.14.8-gke.32 
  * 1.14.9-gke.17 
  * 1.14.10-gke.12 
  * 1.15.7-gke.17 
  * 1.16.4-gke.21 
  * 1.17.0-gke.0 

[ 출시 채널 ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-
channels?hl=ko) 을 사용하는 클러스터는 이미 완화책이 적용된 제어 영역 버전으로 업그레이드되었습니다.

####  이 패치로 어떤 취약점이 해결되나요?

이러한 패치는 CVE-2020-8555 취약점을 완화합니다. 여러 제어 영역 강화 조치로 인해 악용이 어렵기 때문에 이 문제는 GKE에서
'보통' 등급의 취약점으로 분류됩니다.

특정 볼륨 유형(GlusterFS, Quobyte, StorageFS, ScaleIO)이 내장된 Pod를 생성할 수 있는 권한이나
StorageClass를 생성할 수 있는 권한을 보유한 공격자는 마스터의 호스트 네트워크에서 요청 본문을 제어하지 _않아도_ ` kube-
controller-manager ` 에서 ` GET ` 요청 또는 ` POST ` 요청을 보내도록 만들 수 있습니다. 이러한 볼륨은
GKE에서 거의 사용되지 않으므로 이러한 볼륨이 새로 사용되는 것을 감지 신호로 보면 유용합니다.

로그처럼 ` GET/POST ` 의 결과를 공격자에게 반환하는 수단과 결합되면 민감한 정보 공개로 이어질 수 있습니다. 문제가 되는 스토리지
드라이버를 업데이트하여 이러한 유출 가능성을 제거했습니다.

|

보통

|

[ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**게시:** 2020년 6월 1일  
설명  |  심각도  |  참고  
---|---|---  
  
Kubernetes에서는 권한이 있는 컨테이너가 노드 트래픽을 다른 컨테이너로 리디렉션하도록 허용하는 [ 취약점
](https://github.com/kubernetes/kubernetes/issues/91507) 을 공개했습니다. 이 공격을 받으면
상호 TLS/SSH 트래픽(예: Kubelet과 API 서버 사이 또는 mTLS를 사용하는 애플리케이션 발생 트래픽)을 읽거나 수정할 수
없습니다. 이 취약점은 모든 Google Kubernetes Engine(GKE) 노드에 영향을 미치므로 아래의 세부정보를 참고하여 최신
패치 버전으로 [ 업그레이드 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=ko) 하는 것이 좋습니다.

####  어떻게 해야 하나요?

이 취약점을 완화하려면 제어 영역을 [ 업그레이드 ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=ko) 한 후 노드를 아래에 나온 패치 버전 중 하나로
업그레이드하세요. 출시 채널의 클러스터는 이미 제어 영역과 노드에서 이러한 패치 버전을 실행하고 있습니다.

  * 1.14.10-gke.36 
  * 1.15.11-gke.15 
  * 1.16.8-gke.15 

일반적으로 ` CAP_NET_RAW ` 가 필요한 컨테이너는 거의 없습니다. [ PodSecurityPolicy
](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-
policies?hl=ko) 또는 [ Anthos Policy Controller
](https://cloud.google.com/anthos-config-management/docs/concepts/policy-
controller?hl=ko) 를 통해 이 기능과 기타 강력한 기능을 기본적으로 차단해야 합니다.

  * 컨테이너에서 ` CAP_NET_RAW ` 기능을 사용 중지합니다. 
    * 다음과 같이 [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=ko) 를 통해 적용하면 됩니다. 
        
                
        # Require dropping CAP_NET_RAW with a PSP
        apiversion: extensions/v1beta1
        kind: PodSecurityPolicy
        metadata:
          name: no-cap-net-raw
        spec:
          requiredDropCapabilities:
            -NET_RAW
             ...
             # Unrelated fields omitted
        

    * 또는 이 [ 제약조건 템플릿 ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) 과 함께 Anthos Policy Controller/Gatekeeper를 사용한 후 적용하는 방법도 있습니다. 예를 들면 다음과 같습니다. 
        
                
        # Dropping CAP_NET_RAW with Gatekeeper
        # (requires the K8sPSPCapabilities template)
        apiversion: constraints.gatekeeper.sh/v1beta1
        kind:  K8sPSPCapabilities
        metadata:
          name: forbid-cap-net-raw
        spec:
          match:
            kinds:
              - apiGroups: [""]
              kinds: ["Pod"]
            namespaces:
              #List of namespaces to enforce this constraint on
              - default
            # If running gatekeeper >= v3.1.0-beta.5,
            # you can exclude namespaces rather than including them above.
            excludedNamespaces:
              - kube-system
          parameters:
            requiredDropCapabilities:
              - "NET_RAW"
        

    * 또는 Pod 사양을 업데이트합니다. 
        
                
        # Dropping CAP_NET_RAW from a Pod:
        apiVersion: v1
        kind: Pod
        metadata:
          name: no-cap-net-raw
        spec:
          containers:
            -name: may-container
             ...
            securityContext:
              capabilities:
                drop:
                  -NET_RAW
        

####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

[ Kubernetes 문제 91507 ](https://github.com/kubernetes/kubernetes/issues/91507)
에는 노드에서 IPv6 스택을 악의적으로 구성하고 노드 트래픽을 공격자가 제어하는 컨테이너로 리디렉션할 수 있는 ` CAP_NET_RAW `
기능(기본 컨테이너 기능 모음에 포함되어 있음)의 취약점이 설명되어 있습니다. 공격자는 이 취약점을 이용해 노드에서 송/수신되는 트래픽을
가로채거나 수정할 수 있습니다. 이 공격을 받으면 상호 TLS/SSH 트래픽(예: Kubelet과 API 서버 사이 또는 mTLS를 사용하는
애플리케이션의 트래픽)을 읽거나 수정할 수 없습니다.

|

보통

|

[ Kubernetes 문제 91507 ](https://github.com/kubernetes/kubernetes/issues/91507)  
  
  
##  GCP-2020-005

**게시:** 2020년 5월 7일  
**업데이트:** 2020년 5월 7일  설명  |  심각도  |  참고  
---|---|---  
  
[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) 에 설명된 바와 같이 최근 Linux 커널에서 취약점이 발견되었으며, 이
취약점은 컨테이너 이스케이프가 호스트 노드의 루트 권한을 확보할 수 있다는 문제를 안고 있습니다.

GKE 1.16 또는 1.17을 실행하는 Google Kubernetes Engine (GKE) Ubuntu 노드가 이 취약점의 영향을
받으며, 아래의 세부정보에 따라 최대한 빨리 최신 패치 버전으로 업그레이드하는 것이 좋습니다.

Container-Optimized OS를 실행하는 노드는 영향을 받지 않습니다. GKE On-Prem을 실행하는 노드는 영향을 받지
않습니다.

####  어떻게 해야 하나요?

**대부분 고객의 경우 추가 조치는 필요하지 않습니다. GKE 버전 1.16 또는 1.17의 Ubuntu를 실행하는 노드만 영향을
받습니다.**

노드를 업그레이드하려면 먼저 마스터를 최신 버전으로 업그레이드해야 합니다. 이 패치는 Kubernetes 1.16.8-gke.12,
1.17.4-gke.10 및 그 이상의 출시 버전에서 제공됩니다. [ 출시 노트
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=ko) 에서 이
패치의 가용성을 추적할 수 있습니다.

####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) 는 악의적인 컨테이너가 실행 형태인 사용자 상호작용이 최소화된 상태로 커널
메모리를 읽고 쓸 수 있게 하여 호스트 노드에서 루트 수준의 코드 실행을 획득할 수 있는 Linux 커널 버전 5.5.0 이상의 취약점을
설명합니다. 이 문제는 '높음' 등급의 취약점으로 분류됩니다.

|

높음

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP-2020-003

**게시:** 2020년 3월 31일  
**업데이트:** 2020년 3월 31일  설명  |  심각도  |  참고  
---|---|---  
  
[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) 에 설명된 바와 같이 최근 Kubernetes에서 취약점이 발견되었으며,
이 취약점에는 POST 요청 권한이 있는 모든 사용자가 Kubernetes API 서버에서 원격으로 서비스 거부 공격을 실행할 수 있다는
문제가 있습니다. Kubernetes Product Security Committee(PSC)에서 공개한 이 취약점에 관한 추가 정보는 [
여기 ](https://groups.google.com/forum/?hl=ko#!topic/kubernetes-security-
announce/wuwEwZigXBc) 에서 확인할 수 있습니다.

[ 마스터 승인 네트워크 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/authorized-networks?hl=ko) 와 [ 공개 엔드포인트가 없는 비공개 클러스터
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=ko#private_master) 를 사용하는 GKE 클러스터는 이 취약점을 완화합니다.

####  어떻게 해야 하나요?

이 취약점의 수정사항이 포함된 패치 버전으로 클러스터를 업그레이드하는 것이 좋습니다.

수정사항이 포함된 패치 버전은 아래와 같습니다.

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  이 패치로 어떤 취약점이 해결되나요?

이 패치는 다음 서비스 거부(DoS) 취약점을 해결합니다.

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)

|

보통

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**게시:** 2020년 3월 23일  
**업데이트:** 2020년 3월 23일  설명  |  심각도  |  참고  
---|---|---  
  
Kubernetes는 각각 API 서버와 Kubelet에 영향을 미치는 [ 2개의 서비스 거부 취약점
](https://groups.google.com/forum/?hl=ko#!topic/kubernetes-security-
announce/2UOlsba2g0s) 을 공개했습니다. 자세한 내용은 Kubernetes 문제: [ 89377
](https://github.com/kubernetes/kubernetes/issues/89377) 및 [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) 을 참조하세요.

####  어떻게 해야 하나요?

신뢰할 수 없는 사용자가 클러스터의 내부 네트워크에서 요청을 전송할 수 있는 경우만 아니라면 모든 GKE 사용자가
CVE-2020-8551로부터 보호됩니다. [ 마스터 승인 네트워크 ](https://cloud.google.com/kubernetes-
engine/docs/how-to/authorized-networks?hl=ko) 를 사용해도 CVE-2020-8552가 완화됩니다.

####  이 패치는 언제 적용되나요?

CVE-2020-8551 패치는 노드 업그레이드가 필요합니다. 취약점 완화 방법이 포함된 패치 버전은 아래와 같습니다.

  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

참고: 1.14.x 이하 버전은 이 취약점의 영향을 받지 않으므로 패치가 필요하지 않습니다.

CVE-2020-8552 패치는 마스터 업그레이드가 필요합니다. 취약점 완화 방법이 포함된 패치 버전은 아래와 같습니다.

  * 1.14.10-gke.32 
  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

|

보통

|

[ CVE-2020-8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE-2020-8552 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  2020년 1월 21일, 최종 업데이트: 2020년 1월 24일

**게시:** 2020년 1월 21일  
**업데이트:** 2020년 1월 24일  설명  |  심각도  |  참고  
---|---|---  
  
**2020년 1월 24일 업데이트:** 이미 패치 버전을 출시하기 위한 과정이 진행 중이며 2020년 1월 25일까지 완료될 예정입니다.

* * *

Microsoft에서 Windows Crypto API 및 타원 곡선 서명 검사의 취약점을 공개했습니다. 자세한 내용은 [ Microsoft
공개 정보 ](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) 를 참조하세요.

**어떻게 해야 하나요?**

**대부분 고객의 경우 추가 조치는 필요하지 않습니다. Windows Server를 실행 중인 노드만 영향을 받습니다.**

Windows Server 노드를 사용하고 있는 고객의 경우 노드와 해당 노드에서 실행되는 컨테이너화된 워크로드를 모두 패치 버전으로
업데이트해야 이 취약점을 완화할 수 있습니다.

**컨테이너 업데이트 방법:**

Microsoft의 최신 기본 컨테이너 이미지를 사용하고 최종 업데이트 시간이 2020년 1월 14일 이후인 [ servercore
](https://hub.docker.com/_/microsoft-windows-servercore) 또는 [ nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) 태그를 선택하여 컨테이너를 다시
빌드하세요.

**노드 업데이트 방법:**

이미 패치 버전을 출시하기 위한 과정이 진행 중이며 2020년 1월 24일까지 완료될 예정입니다.

그때까지 기다렸다가 패치된 GKE 버전으로 노드 업그레이드를 수행하거나 Windows Update를 사용하여 언제든지 최신 Windows
패치를 수동으로 배포할 수도 있습니다.

취약점 완화 방법이 포함된 패치 버전은 아래와 같습니다.

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**이 패치로 어떤 취약점이 해결되나요?**

이 패치로 다음의 취약점이 완화됩니다.

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) \- 이 취약점은 [ Windows Crypto API 스푸핑 취약점
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) 이라고도 하며, 악성 실행 파일을 신뢰할 수 있는 파일인 것처럼 보이게 하거나
공격자가 중간자 공격을 수행하고 TLS 연결의 기밀 정보를 영향을 받는 소프트웨어에 복호화하는 데 악용될 수 있습니다.

|

NVD 기본 점수: 8.1(높음)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  2019년 11월 14일

**게시:** 2019년 11월 14일  
**업데이트:** 2019년 11월 14일  설명  |  심각도  |  참고  
---|---|---  
  
Kubernetes는 [ 컨테이너 스토리지 인터페이스(CSI) 드라이버 ](https://kubernetes-
csi.github.io/docs/drivers.html) 에 번들로 포함된 사이드카 버전 대부분에 영향을 미치는 kubernetes-csi
[ ` external-provisioner ` ](https://github.com/kubernetes-csi/external-
provisioner) , [ ` external-snapshotter ` ](https://github.com/kubernetes-
csi/external-snapshotter) , [ ` external-resizer `
](https://github.com/kubernetes-csi/external-resizer) 사이드카의 보안 문제를 공개했습니다. 자세한
내용은 [ Kubernetes 정보 공개
](https://github.com/kubernetes/kubernetes/issues/85233) 를 참조하세요.

**어떻게 해야 하나요?**  
**이 취약점은 관리형 GKE 구성요소에 영향을 주지 않습니다** . GKE 버전 1.12 이상을 실행하는 [ GKE 알파 클러스터
](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-
clusters?hl=ko) 에서 자체 CSI 드라이버를 관리하는 경우 영향을 받을 수 있습니다. 영향을 받는 경우, CSI 드라이버
공급업체를 통해 업그레이드 안내를 확인하세요.

**이 패치로 어떤 취약점이 해결되나요?**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : 이 CVE는 승인되지 않은 대용량 데이터 액세스 또는 변형을 허용할 수
있는 ` kubernetes-csi ` [ ` external-provisioner `
](https://github.com/kubernetes-csi/external-provisioner) , [ ` external-
snapshotter ` ](https://github.com/kubernetes-csi/external-snapshotter) , [ `
external-resizer ` ](https://github.com/kubernetes-csi/external-resizer) 사이드카의
취약점입니다. 이 취약점은 [ CSI 드라이버 ](https://kubernetes-
csi.github.io/docs/drivers.html) 에 번들로 포함된 사이드카 버전 대부분에 영향을 줍니다.

|

보통

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  2019년 11월 12일

**게시:** 2019년 11월 12일  
**업데이트:** 2019년 11월 12일  설명  |  심각도  |  참고  
---|---|---  
  
Intel은 예측 실행과 마이크로아키텍처 상태 사이의 상호작용으로 인해 데이터가 노출될 수 있다는 내용의 CVE를 공개했습니다. 자세한
내용은 [ Intel 정보 공개 ](https://blogs.intel.com/technology/2019/11/ipas-
november-2019-intel-platform-update-ipu/) 를 참조하세요.

**Kubernetes Engine을 실행하는 호스트 인프라는 고객의 워크로드를 격리합니다. 자체 멀티 테넌트 GKE 클러스터 내에서 신뢰할
수 없는 코드를 실행 중인 경우 _및_ N2, M2, C2 노드를 사용하는 경우가 아니라면 추가 조치는 필요하지 않습니다. ** N1 노드의
GKE 인스턴스에도 새로운 조치가 필요하지 않습니다.

Anthos GKE On-Prem을 실행 중인 경우 노출 여부는 하드웨어에 따라 다릅니다. [ Intel 정보 공개
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) 와 인프라를 비교해 보세요.

####  어떻게 해야 하나요?

**N2, M2, C2 노드가 포함된 노드 풀을 사용 중 _이고_ 이러한 노드가 자체 멀티 테넌트 GKE 클러스터 내에서 신뢰할 수 없는
코드를 실행하는 경우에만 영향을 받습니다. **

**노드를 다시 시작하면 패치가 적용됩니다.** 노드 풀에서 모든 노드를 다시 시작하는 가장 간편한 방법은 [ 업그레이드
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ko#upgrade_nodes) 작업을 사용하여 영향을 받는 모든 노드 풀을 강제로 다시 시작하는 것입니다.  

참고: 업그레이드 중에는 버전을 변경할 필요가 없습니다. ` cluster-version ` 플래그를 사용하여 동일한 노드 버전으로
업그레이드를 시작할 수 있습니다.

####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
: 이 CVE는 TAA(TSX Async Abort)로도 알려져 있습니다. TAA는 [ 마이크로아키텍처 데이터 샘플링(MDS)
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins?hl=ko#may-14-2019) 에서 악용한 것과 동일한 마이크로아키텍처 데이터 구조로 데이터를 무단 반출할 수 있는 또
다른 경로를 제공합니다.

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
이 서비스 거부(DoS) 취약점은 가상 머신 호스트에 영향을 미치며, 악의적인 게스트가 보호되지 않는 호스트를 비정상 종료할 수 있다는
문제를 안고 있습니다. 이 CVE는 '페이지 크기 변경 시 머신 확인 오류'로도 알려져 있습니다. 이 문제는 GKE에 영향을 주지 않습니다.

|

보통

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  2019년 10월 22일

**게시:** 2019년 10월 22일  
**업데이트:** 2019년 10월 22일  설명  |  심각도  |  참고  
---|---|---  
  
이 취약점은 최근 Go 프로그래밍 언어에서 발견되었으며, [ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) 에 설명되어 있습니다. 이 취약점은 Authenticating Proxy를
사용하는 Kubernetes 구성에 영향을 줄 수 있습니다. 자세한 내용은 [ Kubernetes 정보 공개
](https://groups.google.com/forum/?hl=ko#!topic/kubernetes-security-
announce/PtsUCqFi4h4) 를 참조하세요.

Kubernetes Engine은 Authenticating Proxy 구성을 허용하지 않으므로 이 취약점의 영향을 받지 않습니다.

|

없음

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  2019년 10월 16일

**게시:** 2019년 10월 16일  
**업데이트:** 2019년 10월 24일  설명  |  심각도  |  참고  
---|---|---  
  
**2019년 10월 24일 업데이트:** 이제 모든 영역에서 패치 버전을 사용할 수 있습니다.

* * *

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) 에 설명된 바와 같이 최근 Kubernetes에서 취약점이 발견되었으며,
이 취약점에는 POST 요청 권한이 있는 모든 사용자가 Kubernetes API 서버에서 원격으로 서비스 거부 공격을 실행할 수 있다는
문제가 있습니다. Kubernetes PSC(Product Security Committee)에서 공개한 이 취약점에 관한 추가 정보는 [
여기 ](https://groups.google.com/forum/?hl=ko#!topic/kubernetes-security-
announce/jk8polzSUxs) 에서 확인할 수 있습니다.

[ 마스터 승인 네트워크 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/authorized-networks?hl=ko) 와 [ 공개 엔드포인트가 없는 비공개 클러스터
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=ko#private_master) 를 사용하는 GKE 클러스터는 이 취약점을 완화합니다.

######  어떻게 해야 하나요?

수정사항이 포함된 패치 버전이 제공되는 즉시 클러스터를 업그레이드하는 것이 좋습니다. 패치 버전은 10월 14일이 포함된 주에 계획된 GKE
출시를 통해 모든 영역에 제공될 예정입니다.

취약점 완화 방법이 포함된 패치 버전은 아래와 같습니다.

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

CVE-2019-11253은 서비스 거부(DoS) 취약점입니다.

|

높음

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  2019년 9월 16일

**게시:** 2019년 9월 16일  
**업데이트:** 2019년 10월 16일  설명  |  심각도  |  참고  
---|---|---  
  
이 게시판은 처음 게시된 이후 업데이트되었습니다.

Go 프로그래밍 언어는 최근 보안 취약점 [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) 와 [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) 를 발견했으며, 두
CVE는 서비스 거부(DoS) 취약점입니다. GKE에서 사용자는 이 취약점을 악용해 Kubernetes API 서버의 CPU를 과도하게
소비하도록 악의적인 요청을 만들어서 클러스터 제어 영역의 가용성을 줄일 수 있습니다. 자세한 내용은 [ Go 프로그래밍 언어 정보 공개
](https://groups.google.com/forum/?hl=ko#!topic/golang-announce/65QixT3tcmg) 를
참조하세요.

######  어떻게 해야 하나요?

이 취약점의 완화 방법이 포함된 최신 패치 버전이 제공되는 즉시 클러스터를 업그레이드하는 것이 좋습니다. 패치 버전은 [ 출시 일정
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=ko#september_16_2019) 에 따라 다음 GKE 출시를 통해 모든 영역에 제공될 예정입니다.

취약점 완화 방법이 포함된 패치 버전은 아래와 같습니다.

  * **2019년 10월 16일 업데이트:** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) 및 [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) 는 서비스 거부(DoS)
취약점입니다.

|

높음

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  2019년 9월 5일

**게시:** 2019년 9월 5일  
**업데이트:** 2019년 9월 5일

2019년 5월 31일  게시판에 설명된 취약점 해결책 게시판이 업데이트되었습니다.

##  2019년 8월 22일

**게시:** 2019년 8월 22일  
**업데이트:** 2019년 8월 22일

2019년 8월 5일  게시판이 업데이트되었습니다. 이전 게시판에 설명된 취약점 해결책이 [ 제공
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=ko#august_22_2019) 됩니다.

##  2019년 8월 8일

**게시:** 2019년 8월 8일  
**업데이트:** 2019년 8월 8일

2019년 8월 5일  게시판이 업데이트되었습니다. 해당 게시판에 설명된 취약점 해결책은 다음 GKE 출시에서 제공될 예정입니다.

##  2019년 8월 5일

**게시:** 2019년 8월 5일  
**업데이트:** 2019년 8월 9일  설명  |  심각도  |  참고  
---|---|---  
  
이 게시판은 처음 게시된 이후 업데이트되었습니다.

Kubernetes에서 최근 발견한 [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) 취약점에는 클러스터 범위의 [ 커스텀 리소스
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) 인스턴스가 모든 네임스페이스에 존재하는 네임스페이스화된 객체인 것처럼 처리될 수 있다는 문제가 있습니다. 즉, 사용자
및 서비스 계정은 네임스페이스 수준의 RBAC 권한만 있어도 클러스터 범위의 커스텀 리소스와 상호작용할 수 있습니다. 공격자에게
네임스페이스의 리소스에 액세스할 권한이 있으면 이 취약점을 악용할 수 있습니다.

######  어떻게 해야 하나요?

이 취약점의 완화 방법이 포함된 최신 패치 버전이 제공되는 즉시 클러스터를 [ 업그레이드
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ko) 하는 것이 좋습니다. 패치 버전은 다음 GKE 출시를 통해 모든 영역에 제공될 예정입니다. 취약점 완화 방법이
포함된 패치 버전은 아래와 같습니다.

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10( [ 신속 채널 ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=ko) ) 

######  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다. [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

|

보통

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  2019년 7월 3일

**게시:** 2019년 7월 3일  
**업데이트:** 2019년 7월 3일  설명  |  심각도  |  참고  
---|---|---  
  
CVE-2019-11246을 해결하는 ` kubectl ` 의 패치 버전이 이제 [ ` gcloud ` 253.0.0
](https://cloud.google.com/sdk/docs/release-notes?hl=ko#kubernetes_engine) 을
통해 제공됩니다. 자세한 내용은  2019년 6월 25일 보안 게시판  을 참조하세요.

**참고:** ` kubectl ` 1.11.10에서는 패치를 사용할 수 없습니다.

|

높음

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  2019년 7월 3일

**게시:** 2019년 6월 25일  
**업데이트:** 2019년 7월 3일  설명  |  심각도  |  참고  
---|---|---  
  
######  2019년 7월 3일 업데이트

최종 업데이트 당시 1.11.9 및 1.11.10 버전의 패치가 제공되지 않았지만, 이제 1.11.10-gke.5가 두 1.11 버전의
업그레이드 대상으로 출시되었습니다.

현재 GKE 마스터와 Kubernetes Engine을 실행하는 Google 인프라에 패치가 적용되어 취약점으로부터 보호됩니다.

1.11 마스터는 곧 지원 중단되며 2019년 7월 8일이 포함된 주에 1.12로 자동 업그레이드될 예정입니다. 제안된 다음 조치 중 하나를
선택하여 노드를 패치 버전으로 업그레이드할 수 있습니다.

  * 2019년 7월 8일까지 1.11.10-gke.5로 노드를 업그레이드하세요. 이 날짜 이후에는 1.11 버전이 업그레이드 대상 목록에서 삭제됩니다. 
  * 1.11 노드에서 [ 자동 업그레이드 ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=ko) 를 사용 설정하여 마스터를 1.12로 업그레이드할 때 노드를 업그레이드하도록 허용하세요. 
  * 마스터와 노드 모두를 수정된 1.12 버전으로 [ 수동 업그레이드 ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=ko) 하세요. 

2019년 6월 24일에 처음 공개된 게시판 내용은 다음과 같습니다.

* * *

######  2019년 6월 24일 업데이트

2019년 6월 22일 21시 40분(UTC)을 기준으로 다음 Kubernetes 패치 버전을 사용할 수 있습니다. Kubernetes
버전이 1.11.0~1.13.6인 마스터는 패치 버전으로 자동 업데이트됩니다. 이 패치와 호환되는 버전을 실행하고 있지 않다면 노드
업그레이드 전에 아래 목록을 참고하여 호환되는 마스터 버전으로 업그레이드하세요.

**이 취약점의 심각도가 높으므로 노드 자동 업그레이드의 사용 설정 여부와 관계없이 노드와 마스터 모두를 다음 버전 중 하나로 최대한 빨리[
수동 업그레이드 ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=ko) 하는 것이 좋습니다. **

패치 버전:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

2019년 6월 18일에 처음 공개된 게시판 내용은 다음과 같습니다.

* * *

Netflix는 최근 Linux 커널의 TCP 취약점 3가지를 공개했습니다.

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

이러한 CVE를 통칭하여 [ NFLX-2019-001 ](https://github.com/Netflix/security-
bulletins/blob/master/advisories/third-party/2019-001.md) 이라고 합니다.

패치되지 않은 Linux 커널은 원격으로 트리거된 서비스 거부 공격에 취약할 수 있습니다. **신뢰할 수 없는 네트워크 트래픽을 보내거나
받는 Google Kubernetes Engine 노드가 영향을 받으며, 아래의 완화 단계에 따라 워크로드를 보호하는 것이 좋습니다.**

######  Kubernetes 마스터

  * [ 승인된 네트워크 ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=ko) 를 사용하여 신뢰할 수 있는 네트워크로 트래픽을 제한하는 Kubernetes 마스터는 영향을 받지 않습니다. 

  * Google에서 관리하는 GKE 클러스터 마스터는 향후 자동으로 패치가 적용되므로 고객이 별도의 조치를 취하지 않아도 됩니다. 

######  Kubernetes 노드

신뢰할 수 있는 네트워크로 트래픽을 제한하는 노드는 영향을 받지 않습니다. 이러한 클러스터에는 다음이 포함됩니다.

  * 신뢰할 수 없는 네트워크에서 방화벽으로 차단되었거나 공개 IP가 없는 노드( [ 비공개 클러스터 ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=ko) ) 
  * 공개 LoadBalancer 서비스가 없는 클러스터 

Google은 이러한 취약점을 영구적으로 완화할 방법을 준비 중이며 새 노드 버전으로 제공할 예정입니다. 영구적 해결책이 제공되면 이
게시판을 업데이트하고 모든 GKE 고객에게 이메일을 보내드릴 것입니다.

영구적 해결책이 제공되기 전에 사용할 수 있도록 호스트 ` iptables ` 구성을 수정하여 완화 방법을 구현하는 Kubernetes
DaemonSet가 제공됩니다.

#####  어떻게 해야 하나요?

다음 명령어를 실행하여 클러스터의 모든 노드에 Kubernetes DaemonSet를 적용합니다. 이렇게 하면 노드에 있는 기존 `
iptables ` 규칙에 ` iptables ` 규칙을 추가하여 취약점을 완화할 수 있습니다. **명령어는 Google Cloud
프로젝트당 하나의 클러스터에 한 번 실행합니다.**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

Ipv6은 GKE에서 지원되지 않으므로 ip6tables 규칙은 필요하지 않습니다.

패치된 노드 버전이 제공되어 영향을 받을 수 있는 모든 노드를 업그레이드하고 나면 다음 명령어로 DaemonSet를 삭제할 수 있습니다.
**명령어는 Google Cloud 프로젝트당 하나의 클러스터에 한 번 실행합니다.**

    
    
    
    kubectl delete -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

|  높음  
보통  
보통  
|  [ CVE-2019-11477 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
  
  
##  2019년 6월 25일

설명  |  심각도  |  참고  
---|---|---  
  
**2019년 7월 3일 업데이트:** 이 패치는 ` gcloud ` 253.0.0에서 제공되며 ` kubectl ` 버전 1.12.9,
1.13.6, 1.14.2 및 그 이상의 출시 버전을 대상으로 합니다.

**참고:** 1.11.10에서는 이 패치를 사용할 수 없습니다.

* * *

Kubernetes에서 최근 발견한 [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) 취약점에는 컨테이너 내 ` kubectl cp ` 작업과 코드 실행에
액세스 권한이 있는 공격자가 호스트의 파일을 수정할 수 있다는 문제가 있습니다. 공격자는 이 취약점을 악용하여 호스트 파일 시스템에서 파일을
바꾸거나 만들 수 있습니다. 자세한 내용은 [ Kubernetes 정보 공개
](https://groups.google.com/forum/?hl=ko#!topic/kubernetes-security-
announce/NLs2TGbfPdo) 를 참조하세요.

**모든 Google Kubernetes Engine(GKE)` gcloud ` 버전이 이 취약점의 영향을 받으며, ` gcloud ` 의
최신 패치 버전이 제공되면 업그레이드하는 것이 좋습니다. ** 예정된 패치 버전에 이 취약점의 완화 방법이 포함됩니다.

######  어떻게 해야 하나요?

예정된 ` gcloud ` 출시를 통해 ` kubectl ` 패치 버전이 제공됩니다. 직접 [ ` kubectl ` 을 바로 업그레이드
](https://kubernetes.io/docs/tasks/tools/install-kubectl/) 할 수도 있습니다.

[ ` gcloud ` 출시 노트 ](https://cloud.google.com/sdk/docs/release-notes?hl=ko) 에서
이 패치의 가용성을 추적할 수 있습니다.

######  이 패치로 어떤 취약점이 해결되나요?

컨테이너 내부 ` kubectl cp ` 작업 및 코드 실행에 대한 액세스 권한이 있는 공격자는 취약점 [ CVE-2019-11246
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11246) 을 악용하여 호스트의
파일을 수정할 수 있습니다. 공격자는 이 취약점을 악용하여 호스트 파일 시스템에서 파일을 바꾸거나 만들 수 있습니다.

|

높음

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  2019년 6월 18일

설명  |  심각도  |  참고  
---|---|---  
  
Docker에서 최근 발견한 [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) 취약점에는 컨테이너 내부에서 코드를 실행할 수 있는 공격자가 외부에서
시작된 ` docker cp ` 작업을 도용할 수 있다는 문제가 있습니다. 공격자는 이 취약점을 악용하여 파일이 작성된 위치를 호스트 파일
시스템 내 임의의 위치로 변경할 수 있습니다.

**Docker를 실행하는 모든 Google Kubernetes Engine(GKE) 노드가 이 취약점의 영향을 받으며, 최신 패치 버전이
제공되면 업그레이드하는 것이 좋습니다. 예정된 패치 버전에 이 취약점의 완화 방법이 포함됩니다.**

**1.12.7 이전 버전인 Google Kubernetes Engine(GKE) 마스터는 모두 Docker를 실행하므로 이 취약점의 영향을
받습니다.** GKE에서 사용자는 마스터의 ` docker cp ` 에 액세스할 수 없으므로 이 취약점의 위험은 GKE 마스터로 한정됩니다.

#####  어떻게 해야 하나요?

도용 가능한 ` docker cp ` (또는 API 상응) 명령어가 실행되는 경우에 한해 Docker를 실행하는 노드만 영향을 받습니다.
Kubernetes 환경에서 이러한 상황은 상당히 드물 것으로 예상됩니다. [ 컨테이너가 있는 COS
](https://cloud.google.com/kubernetes-engine/docs/concepts/using-
containerd?hl=ko) 를 실행하는 노드는 영향을 받지 않습니다.

노드를 업그레이드하려면 패치 버전으로 먼저 [ 마스터를 업그레이드 ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=ko#upgrading_the_cluster) 해야 합니다.
패치가 제공되면 마스터 업그레이드를 시작하거나 Google이 마스터를 자동으로 업그레이드하기를 기다릴 수 있습니다. 이 패치는 Docker
18.09.7에서 제공되며, 예정된 GKE 패치에 포함됩니다. **이 패치는 GKE 버전 1.13 이상에만 사용할 수 있습니다.**

정기적인 업그레이드 주기에 따라 클러스터 마스터가 패치 버전으로 자동 업그레이드됩니다. 패치 버전이 제공되면 직접 마스터 업그레이드를
시작해도 됩니다.

패치가 제공되면 패치가 포함된 버전으로 이 게시판이 업데이트됩니다. [ 출시 노트
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=ko) 에서 이
패치의 가용성을 추적할 수 있습니다.

#####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

컨테이너 내부에서 코드를 실행할 수 있는 공격자는 취약점 [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) 를 이용하여 외부에서 시작된 ` docker cp ` 작업을 도용할 수
있습니다. 공격자는 이 취약점을 악용하여 파일이 작성된 위치를 호스트 파일 시스템에 있는 임의 위치로 변경할 수 있습니다.

|  높음  |  
  
##  2019년 5월 31일

설명  |  심각도  |  참고  
---|---|---  
  
이 게시판은 처음 게시된 이후 업데이트되었습니다.

######  2019년 8월 2일 업데이트

게시판이 처음 게시될 당시에는 1.13.6-gke.0~1.13.6-gke.5만 영향을 받았습니다. 회귀로 인해 이제 1.13.6.x 버전이
모두 영향을 받습니다. 1.13.6을 실행 중이라면 최대한 빨리 1.13.7로 업그레이드하세요.

Kubernetes 프로젝트에서 공개한 kubelet v1.13.6 및 v1.14.2의 취약점 [ CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) 로 인해 컨테이너 이미지에 다른
사용자가 지정되었더라도 컨테이너가 UID 0(일반적으로 ` root ` 사용자에 매핑)으로 실행될 수 있습니다. **컨테이너가 루트가 아닌
사용자로 실행되고 노드 버전 1.13.6-gke.0~1.13.6-gke.6을 실행하고 있다면 컨테이너가 UID 0으로 실행되어서는 안 되는
클러스터의 모든 Pod에` RunAsUser ` 를 설정하는 것이 좋습니다. **

루트가 아닌 ` USER ` 값이 지정되면(예: Dockerfile에서 ` USER ` 값 설정) 예상치 못한 동작이 발생합니다. 컨테이너가
노드에서 처음 실행될 때는 지정된 UID를 올바르게 고려합니다. 그러나, 이 결함으로 인해 두 번째 실행 이후에는 지정된 UID와 관계없이
컨테이너가 UID 0으로 실행됩니다. 이는 바람직하지 않게 에스컬레이션된 권한인 경우가 많으며 예상치 못한 애플리케이션 동작으로 이어질 수
있습니다.

#####  영향을 받는 버전을 실행 중인지 어떻게 알 수 있나요?

다음 명령어를 실행하여 모든 노드와 kubelet 버전을 나열합니다.

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

출력에 아래와 같은 kubelet 버전이 나열되면 영향을 받는 노드입니다.

  * v1.13.6 
  * v1.14.2 

#####  특정 구성이 영향을 받는지 어떻게 알 수 있나요?

컨테이너가 루트가 아닌 사용자로 실행되고 노드 버전 1.13.6-gke.0~1.13.6-gke.6을 실행하고 있다면 다음 경우를 제외하고는
영향을 받습니다.

  * 루트가 아닌 유효한 ` runAsUser ` PodSecurityContext 값을 지정하는 pod는 영향을 받지 않으며 계속 정상적으로 작동합니다. 
  * ` runAsUser ` 설정을 적용하는 PodSecurityPolicies도 영향을 받지 않으며 계속 정상적으로 작동합니다. 
  * ` mustRunAsNonRoot:true ` 를 지정하는 pod는 UID 0으로 시작하지 않지만 이 문제의 영향을 받을 경우 시작할 수 없습니다. 

#####  어떻게 해야 하나요?

UID 0으로 실행하면 안 되는 클러스터의 모든 Pod에서 [ RunAsUser Security Context
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) 를 설정합니다. [ PodSecurityPolicy
](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) 를 사용하여 이
구성을 적용할 수 있습니다.

|  보통  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  2019년 5월 14일

설명  |  심각도  |  참고  
---|---|---  
  
**2019년 6월 11일 업데이트:** 패치는 2019년 5월 28일이 포함된 주에 출시된 1.11.10-gke.4,
1.12.8-gke.6, 1.13.6-gke.5 및 그 이상의 출시 버전에서 제공됩니다.

Intel은 다음과 같은 CVE를 공개했습니다.

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

이러한 CVE를 통칭하여 마이크로아키텍처 데이터 샘플링(MDS)이라고 합니다. 잠재적으로 데이터가 마이크로아키텍처 상태에서 예측 실행의
상호작용을 통해 이러한 취약점에 노출될 수 있습니다. 자세한 내용은 [ Intel 정보 공개
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) 를 참조하세요.

**Kubernetes Engine을 실행하는 호스트 인프라는 고객의 워크로드를 서로 격리합니다. 자체 멀티 테넌트 GKE 클러스터 내에서
신뢰할 수 없는 코드를 실행하는 경우가 아니면 영향을 받지 않습니다.**

**Kubernetes Engine 내 자체 멀티 테넌트 서비스에서 신뢰할 수 없는 코드를 실행하는 고객에게는 특히 심각한 취약점입니다.**
Kubernetes Engine에서 취약점을 완화하려면 노드에서 하이퍼 스레딩을 사용 중지하세요. 이 취약점은 여러 CPU를 사용하는
Google Kubernetes Engine(GKE) 노드에만 영향을 미칩니다. n1-standard-1(GKE 기본값), g1-small,
f1-micro VM은 1개의 vCPU만 게스트 환경에 노출하므로 하이퍼 스레딩을 사용 중지할 필요가 없습니다.

삭제 기능을 사용 설정하는 추가적인 보호 조치가 예정된 [ 패치 버전 ](https://cloud.google.com/kubernetes-
engine/release-notes?hl=ko) 에 포함됩니다. 몇 주 후 정기적인 업그레이드 주기에 따라 마스터와 노드가 자동
업그레이드를 통해 패치 버전으로 자동 업그레이드됩니다. **패치만으로는 이 취약점에 대한 노출을 완화하기에 충분하지 않습니다. 아래에서 권장
조치를 참조하세요.**

GKE On-Prem을 실행하고 있다면 사용 중인 하드웨어에 따라 영향을 받을 수 있습니다. [ Intel 정보 공개
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) 를 참조하세요.

####  어떻게 해야 하나요?

**자체 멀티 테넌트 GKE 클러스터에서 신뢰할 수 없는 코드를 실행하는 경우가 아니라면 영향을 받지 않습니다.**

**Kubernetes Engine에 있는 노드의 경우 하이퍼 스레딩이 사용 중지된 새 노드 풀을 만들고 새 노드로 워크로드의 일정을
변경합니다.**

n1-standard-1, g1-small, f1-micro VM은 1개의 vCPU만 게스트 환경에 노출하므로 하이퍼 스레딩을 사용 중지할
필요가 없습니다.

**경고:**

  * 하이퍼 스레딩을 사용 중지하면 클러스터와 애플리케이션의 성능에 심각한 영향을 미칠 수 있습니다. 프로덕션 클러스터에 배포하기 전에 이러한 상황이 허용되는지 확인하시기 바랍니다. 
  * 하이퍼 스레딩은 DaemonSet를 배포하여 GKE 노드 풀 수준에서 사용 중지할 수 있습니다. 그러나 이 DaemonSet를 배포하면 노드 풀의 모든 노드가 동시에 재부팅됩니다. 그러므로 클러스터에서 새 노드 풀을 만들고 DaemonSet를 배포하여 노드 풀에서 하이퍼 스레딩을 사용 중지한 다음, 워크로드를 새 노드 풀로 마이그레이션하는 것이 좋습니다. 

하이퍼 스레딩이 사용 중지된 새 노드 풀을 만들려면 다음 안내를 따르세요.

  1. ` cloud.google.com/gke-smt-disabled=true ` 노드 라벨을 사용하여 클러스터에 새 노드 풀을 만듭니다. 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. 이 새 노드 풀에 DaemonSet를 배포합니다. DaemonSet는 ` cloud.google.com/gke-smt-disabled=true ` 라벨이 있는 노드에서만 실행되며 하이퍼 스레딩을 사용 중지한 다음 노드를 재부팅합니다. 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. DaemonSet pod가 실행 중인 상태인지 확인합니다. 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

다음과 비슷한 응답을 받게 됩니다.

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. Pod의 로그에 'SMT가 사용 중지됨'이 표시되는지 확인합니다. 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

참고: 노드에 [ 안전한 부팅 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/shielded-gke-nodes?hl=ko#secure_boot) 기능이 사용 설정되어 있으면 부팅 옵션을 수정할 수 없습니다.
안전한 부팅이 사용 설정된 경우 DaemonSet를 생성하기 전에 [ 사용 중지
](https://cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-
nodes?hl=ko#disabling) 해야 합니다.

풀에서 만든 새 노드에 변경사항이 자동으로 적용될 수 있도록 노드 풀에서 DaemonSet를 실행 중인 상태로 유지해야 합니다. 노드 생성은
노드 자동 복구, 수동 또는 자동 업그레이드, 자동 확장으로 트리거될 수 있습니다.

하이퍼 스레딩을 다시 사용 설정하려면 제공된 DaemonSet를 배포하지 않은 채 새 노드 풀을 다시 만들고 워크로드를 이 새 노드 풀로
마이그레이션해야 합니다.

또한 패치가 제공되면 노드를 수동으로 업그레이드하는 것이 좋습니다. 업그레이드하려면 우선 [ 마스터를 최신 버전으로 업그레이드
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ko#upgrading_the_cluster) 해야 합니다. GKE 마스터는 정기적인 업그레이드 주기에 따라 자동으로
업그레이드됩니다.

패치가 제공되면 패치가 포함된 버전으로 이 게시판이 업데이트됩니다.

####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
, [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) , [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) , [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091) :
이 취약점은 예측 실행을 악용합니다. 이러한 CVE를 통칭하여 마이크로아키텍처 데이터 샘플링이라고 합니다. 잠재적으로 데이터가
마이크로아키텍처 상태에서 예측 실행의 상호작용을 통해 이러한 취약점에 노출될 수 있습니다.  |  보통  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  2019년 4월 5일

설명  |  심각도  |  참고  
---|---|---  
  
최근 보안 취약점 [ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) 과 [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) 이 [ Envoy
](https://www.envoyproxy.io/) 에서 발견되었습니다.

[ Istio ](https://istio.io/) 는 Envoy를 삽입하므로 이 취약점으로 인해 경우에 따라 Istio 정책이 우회될 수
있습니다.

Google Kubernetes Engine(GKE)에서 Istio를 사용 설정한 경우 이 취약점의 영향을 받을 수 있습니다. **영향을
받는 클러스터를 최신 패치 버전으로 최대한 빨리 업그레이드하고 Istio 사이드카도 업그레이드하는 것이 좋습니다(아래 안내 참조).**

####  어떻게 해야 하나요?

**이 취약점의 심각도가 높으므로 노드 자동 업그레이드 사용 설정 여부와 관계없이 다음 조치를 취하는 것이 좋습니다.**

  1. **패치가 제공되는 즉시 클러스터를[ 수동 업그레이드 ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=ko) 합니다. **
  2. **[ 사이드카 업그레이드 문서 ](https://istio.io/docs/setup/kubernetes/upgrade/steps/#sidecar-upgrade) 에 따라 사이드카를 업그레이드합니다. **

패치 버전은 금일 오후 7시(PDT 기준) 이전에 모든 GKE 프로젝트에 제공될 예정입니다.

이 패치는 아래 GKE 버전에 제공됩니다. GKE 보안 게시판 페이지에서 패치 버전이 발표되면(2019년 4월 15일로 예정) 새
클러스터에서 기본적으로 이 패치 버전을 사용합니다. 그 전에 새 클러스터를 만드는 경우에는 여기에 사용할 패치 버전을 지정해야 합니다. [
노드 자동 업그레이드 ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-
auto-upgrades?hl=ko) 를 사용 설정했으며 수동으로 업그레이드 하지 않는 GKE 고객의 노드는 그 다음 주에 패치 버전으로
자동 업그레이드됩니다.

패치 버전:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) 및 [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) 자세한 내용은 [
Istio 블로그 ](https://istio.io/blog/2019/announcing-1.1.2) 에서 확인할 수 있습니다.

|  높음  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  2019년 3월 1일

설명  |  심각도  |  참고  
---|---|---  
  
**2019년 3월 22일 업데이트:** 이 패치는 Kubernetes 1.11.8-gke.4, 1.13.4-gke.1 및 그 이상의 출시
버전에서 제공됩니다. 1.12에서는 이 패치를 아직 사용할 수 없습니다. [ 출시 노트
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=ko#march_19_2019) 에서 이 패치의 가용성을 추적할 수 있습니다.

Kubernetes에서 최근 발견한 신규 서비스 거부 취약점 [ CVE-2019-1002100
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1002100) 에는 패치 요청
권한이 있는 사용자가 Kubernetes API 서버의 CPU와 메모리를 과도하게 소비하는 악의적인 'json-patch' 요청을 만들어
클러스터 제어 영역의 가용성을 줄일 수 있다는 문제가 있습니다. 자세한 내용은 [ Kubernetes 정보 공개
](https://groups.google.com/forum/?hl=ko#!topic/kubernetes-
announce/vmUUNkYfG9g) 를 참조하세요. **이 취약점은 모든 Google Kubernetes Engine(GKE) 마스터에
영향을 미칩니다. 예정된 패치 버전에 이 취약점의 완화 방법이 포함됩니다. 몇 주 후 정기적인 업그레이드 주기에 따라 클러스터 마스터가 패치
버전으로 자동 업그레이드됩니다.**

####  어떻게 해야 하나요?

**별도의 조치를 취할 필요가 없습니다. GKE 마스터는 정기적인 업그레이드 주기에 따라 자동으로 업그레이드됩니다.** 마스터를 더 빨리
업그레이드하려면 [ 마스터 업그레이드를 수동으로 시작 ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=ko#upgrading_the_cluster) 해도 됩니다.

패치가 포함된 버전으로 이 게시판이 업데이트됩니다. 이 패치는 버전 1.10이 아닌 버전 1.11+에서만 사용할 수 있습니다.

####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

취약점 [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) 으로 인해 사용자는 Kubernetes API 서버의 CPU를 과도하게
소비하는 'json-patch' 패치 유형을 만들어 클러스터 제어 영역의 가용성을 줄일 수 있습니다.

|  보통  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  2019년 2월 11일(runc)

설명  |  심각도  |  참고  
---|---|---  
  
Open Containers Initiative(OCI)가 runc에서 신규 보안 취약점 [ CVE-2019-5736
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736) 을 [ 최근 발견
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=ko#!topic/dev/Tc1ELm-8oDI)
했으며, 이 취약점은 컨테이너 이스케이프가 호스트 노드의 루트 권한을 확보할 수 있다는 문제를 안고 있습니다.

**Google Kubernetes Engine(GKE) Ubuntu 노드는 이 취약점의 영향을 받으며, 아래 세부정보에 따라 최대한 빨리
최신 패치 버전으로[ 업그레이드 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=ko) 하는 것이 좋습니다. **

####  어떻게 해야 하나요?

노드를 업그레이드하려면 먼저 마스터를 최신 버전으로 업그레이드해야 합니다. 이 패치는 Kubernetes 1.10.12-gke.7,
1.11.6-gke.11, 1.11.7-gke.4, 1.12.5-gke.5 및 그 이상의 출시 버전에서 제공됩니다. [ 출시 노트
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=ko#february-11-2019) 에서 패치의 가용성을 추적할 수 있습니다.

GKE의 Ubuntu 노드만 영향을 받습니다. COS를 실행하는 노드는 영향을 받지 않습니다.

새로운 버전의 runc는 메모리 사용량이 증가했으며 메모리 제한이 낮게(16MB 미만) 설정된 경우 컨테이너에 할당된 메모리를 업데이트해야
할 수 있습니다.

####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

[ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) 은 악의적인 컨테이너가 실행 형태인 사용자 상호작용이 최소화된 상태로 호스트
runc 바이너리를 덮어써서 호스트 노드에서 루트 수준의 코드 실행을 획득할 수 있는 runc의 취약점을 설명합니다. 루트로 실행되지 않는
컨테이너는 영향을 받지 않습니다. 이 문제는 '높음' 등급의 취약점으로 분류됩니다.

|  높음  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  2019년 2월 11일(Go)

설명  |  심각도  |  참고  
---|---|---  
  
**2019년 2월 25일 업데이트:** 패치는 이미 안내된 내용과 같이 1.11.7-gke.4에서는 제공되지 않습니다. 1.11.7을
실행하고 있다면 1.11.6으로 다운그레이드 또는 1.12로 업그레이드하거나 2019년 3월 4일이 포함된 주에 1.11.7 패치가 제공될
때까지 기다릴 수 있습니다.

Go 프로그래밍 언어에서 최근 발견한 신규 보안 취약점 [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486) 은 P-521 및 P-384 타원 곡선의 암호화/타원 구현에 관한 서비스
거부(DoS) 취약점입니다. Google Kubernetes Engine(GKE)에서 사용자는 이 취약점을 악용해 Kubernetes API
서버의 CPU를 과도하게 소비하는 악의적인 요청을 만들어서 클러스터 제어 영역의 가용성을 줄일 수 있습니다. 자세한 내용은 [ Go
프로그래밍 언어 정보 공개 ](https://groups.google.com/forum/?hl=ko#!topic/golang-
announce/mVeX35iXuSw) 를 참조하세요.

**이 취약점은 모든 Google Kubernetes Engine(GKE) 마스터에 영향을 미칩니다.[ 최신 패치 버전
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=ko#february-11-2019) 에 이 취약점의 완화 방법이 포함됩니다. 몇 주 후 정기적인 업그레이드 주기에 따라
클러스터 마스터가 패치 버전으로 자동 업그레이드됩니다 **

####  어떻게 해야 하나요?

**별도의 조치를 취할 필요가 없습니다. GKE 마스터는 정기적인 업그레이드 주기에 따라 자동 업그레이드됩니다.** 마스터를 더 빨리
업그레이드하려면 [ 마스터 업그레이드를 수동으로 시작 ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=ko#upgrading_the_cluster) 해도 됩니다.

이 패치는 GKE 1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4, 1.12.5-gke.5 및 그 이상의 출시
버전에서 제공됩니다.

####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

CVE-2019-6486은 P-521 및 P-384 타원 곡선의 암호화/타원 구현에 관한 취약점입니다. 이 취약점을 통해 사용자는 CPU를
과도하게 소비하는 입력을 만들 수 있습니다.

|  높음  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  2018년 12월 3일

설명  |  심각도  |  참고  
---|---|---  
  
Kubernetes에서 최근 발견한 신규 보안 취약점 [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) 는 권한이 비교적 낮은 사용자가 kubelet의 API에 대한 승인을
우회하여 클러스터 내의 어떤 노드에서든 모든 Pod에 대해 임의의 작업을 실행할 수 있다는 문제를 안고 있습니다. 자세한 내용은 [
Kubernetes 정보 공개 ](https://groups.google.com/forum/?hl=ko#!topic/kubernetes-
announce/GVllWCg6L88) 를 참조하세요. **모든 Google Kubernetes Engine(GKE) 마스터가 이 취약점의
영향을 받았으며, Google은 이미[ 최신 패치 버전 ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=ko#november-12-2018) 으로 클러스터를 업그레이드했습니다. 별도의 조치를
취할 필요가 없습니다. **

####  어떻게 해야 하나요?

**별도의 조치를 취할 필요가 없습니다. GKE 마스터가 이미 업그레이드되었습니다.**

이 패치는 GKE 1.9.7-gke.11, 1.10.6-gke.11, 1.10.7-gke.11, 1.10.9-gke.5,
1.11.2-gke.18 및 그 이상의 출시 버전에서 제공됩니다.

####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

취약점 CVE-2018-1002105는 권한이 비교적 낮은 사용자가 kubelet의 API에 대한 승인을 우회할 수 있다는 문제를 안고
있습니다. 이에 따라 사용자에게는 kubelet API 임의 호출 수행과 에스컬레이션을 위한 요청(업그레이드 가능) 권한이 주어집니다. 이는
Kubernetes에서 심각한 취약점으로 분류됩니다. 미승인 에스컬레이션 경로가 차단된 GKE 구현을 좀 더 상세히 고려해 보면 이 문제는
'높음' 등급의 취약점으로 분류됩니다.

|  높음  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  2018년 11월 13일

설명  
---  
  
**2018년 11월 16일 업데이트:** 영향을 받았을 가능성이 있는 모든 토큰의 취소와 순환이 완료되었습니다. 추가 조치는 필요하지
않습니다.

Google은 최근 Calico Container Network Interface(CNI) 플러그인이 특정 구성에서 민감한 정보를 로깅할 수
있다는 문제를 발견했습니다. 이 문제는 Tigera Technical Advisory [ TTA-2018-001
](https://www.projectcalico.org/security-bulletins/) 에서 추적됩니다.

  * 디버그 수준 로깅으로 실행 시 Calico CNI 플러그인은 Kubernetes API 클라이언트 구성을 로그에 씁니다. 
  * 또한 CNI 네트워크 구성에서 'k8s_auth_token' 필드가 설정된 경우 Calico CNI는 정보 수준에서 Kubernetes API 토큰을 로그에 씁니다. 
  * 또한 디버그 수준 로깅으로 실행 시 서비스 계정 토큰이 Calico가 읽는 Calico 구성 파일에서든 Calico에서 사용하는 환경 변수로서든 명시적으로 설정된 경우, Calico 구성요소(calico/node, felix, CNI)는 이 정보를 로그 파일에 씁니다. 

이러한 토큰에는 다음과 같은 권한이 있습니다.  
      
    
    
    bgpconfigurations.crd.projectcalico.org     [create get list update watch]
    bgppeers.crd.projectcalico.org              [create get list update watch]
    clusterinformations.crd.projectcalico.org   [create get list update watch]
    felixconfigurations.crd.projectcalico.org   [create get list update watch]
    globalbgpconfigs.crd.projectcalico.org      [create get list update watch]
    globalfelixconfigs.crd.projectcalico.org    [create get list update watch]
    globalnetworkpolicies.crd.projectcalico.org [create get list update watch]
    globalnetworksets.crd.projectcalico.org     [create get list update watch]
    hostendpoints.crd.projectcalico.org         [create get list update watch]
    ippools.crd.projectcalico.org               [create get list update watch]
    networkpolicies.crd.projectcalico.org       [create get list update watch]
    nodes                                       [get list update watch]
    pods                                        [get list watch patch]
    namespaces                                  [get list watch]
    networkpolicies.extensions                  [get list watch]
    endpoints                                   [get]
    services                                    [get]
    pods/status                                 [update]
    networkpolicies.networking.k8s.io           [watch list]
            
  
---  
  
클러스터 네트워크 정책과 Stackdriver Logging이 사용 설정된 Google Kubernetes Engine 클러스터가
Calico 서비스 계정 토큰을 Stackdriver에 로깅했습니다. 네트워크 정책이 사용 설정되지 않은 클러스터는 영향을 받지 않습니다.

Google은 수정 배포를 통해 Calico CNI 플러그인을 마이그레이션하여 경고 수준에서만 로깅하고 새로운 서비스 계정을 사용할 수
있도록 했습니다. 패치된 calico 코드는 후속 출시 버전에서 배포됩니다.

영향을 받았을 가능성이 있는 모든 토큰은 다음 주 중에 단계적으로 취소될 예정입니다. 취소가 완료되면 이 게시판이 업데이트됩니다. **추가
조치는 필요하지 않습니다.** (이 순환은 2018년 11월 16일에 완료됨)

이러한 토큰은 다음의 명령어를 실행해 즉시 순환할 수 있으며, 서비스 계정의 신규 보안 비밀이 몇 초 이내에 자동으로 재생성됩니다.  
      
    
    kubectl get sa --namespace kube-system calico -o template --template '{{(index .secrets 0).name}}x' | xargs kubectl delete secret --namespace kube-system
            
  
---  
  
####  감지

GKE가 API 서버에 모든 액세스를 로깅합니다. Calico 토큰이 Google Cloud의 예상 IP 범위 밖에서 사용되었는지 확인하려면
다음의 Stackdriver 쿼리를 실행하세요. 이 쿼리는 GCP 네트워크 밖에서 수행된 호출에 대한 레코드만 반환합니다. 이는 사용자의
환경별로 맞춤설정할 필요가 있습니다.  
  
---  
      
    
    
    resource.type="k8s_cluster"
    protoPayload.authenticationInfo.principalEmail="system:serviceaccount:kube-system:calico"
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.34.208.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.192.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.200.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.59.80.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.208.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.216.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.220.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.222.0/24")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.224.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.216.148.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.222.176.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "173.255.112.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "192.158.28.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.192.112.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.232.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.236.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.236.48.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.251.128.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.204.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.208.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.167.160.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.178.192.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.2.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.240.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.128.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.154.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.196.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "208.68.108.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.184.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.188.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.202.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.192.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.196.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.198.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.200.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "2600:1900::/35")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.232.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.234.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.236.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.240.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.232.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.220.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.242.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.244.0.0/14")
            
  
---  
  
##  2018년 8월 14일

설명  |  심각도  |  참고  
---|---|---  
  
[ Intel은 다음과 같은 CVE를 공개
](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) 했습니다.

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) ( [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) 용) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (운영체제 및 [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) 용) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (가상화용) 

이러한 CVE를 통칭하여 'L1 터미널 오류(L1TF)'라고 합니다.

이러한 L1TF 취약점은 프로세서 수준 데이터 구조의 구성을 공격하는 식의 예측 실행 악용 문제를 안고 있습니다. 'L1'은 레벨 1 데이터
캐시(L1D), 즉 메모리 액세스 가속화에 사용되는 소형 온코어(on-core) 리소스를 의미합니다.

이러한 취약점과 Compute Engine의 완화 조치에 대한 자세한 내용은 [ Google Cloud 블로그 게시물
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=ko) 을 참조하세요.

####  Google Kubernetes Engine에 미치는 영향

Kubernetes Engine을 실행하고 고객 클러스터와 노드를 서로 격리하는 인프라는 알려진 공격으로부터 안전합니다.

Google의 Container-Optimized OS 이미지를 사용하고 [ 자동 업그레이드
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=ko) 를 사용 설정한 Kubernetes Engine 노드 풀은 2018년 8월 20일로 시작하는 주부터 COS
이미지의 패치 버전이 제공될 때마다 자동으로 업데이트됩니다.

[ 자동 업그레이드 ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=ko) 를 사용 설정하지 않은 Kubernetes Engine 노드 풀은 COS 이미지의 패치 버전이 제공될
때마다 [ 수동으로 업그레이드 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=ko) 해야 합니다.

|  높음  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  2018년 8월 6일, 최종 업데이트 날짜: 2018년 9월 5일

설명  |  심각도  |  참고  
---|---|---  
  
####  2018년 9월 5일 업데이트

최근 공개된 [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) 은 [ CVE-2018-5390
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390) 과 같은 커널 수준의
네트워킹 취약점이며, 취약 시스템에 대한 서비스 거부(DoS) 공격 효과가 증가한다는 문제를 안고 있습니다. 주요한 차이는
CVE-2018-5391은 IP 연결 시 악용될 수 있다는 점입니다. 이 두 취약점을 모두 고려할 수 있도록 게시판이 업데이트되었습니다.

####  설명

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ('SegmentSmack')은 TCP 연결 시 취약 시스템에 대한 서비스
거부(DoS) 공격 효과가 증가하는 커널 수준의 네트워킹 취약점입니다.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ('FragmentSmack')은 IP 연결 시 취약 시스템에 대한 서비스
거부(DoS) 공격 효과가 증가하는 커널 수준의 네트워킹 취약점입니다.

####  Google Kubernetes Engine에 미치는 영향

2018년 8월 11일부터는 모든 Kubernetes Engine 마스터와 자동 업그레이드가 구성된 모든 Kubernetes Engine
클러스터가 두 취약점으로부터 안전해집니다. [ 자동 업그레이드 ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=ko) 가 구성되지 않았고 마지막 수동 업그레이드 시점이
2018년 8월 11일 이전인 Kubernetes Engine 노드 풀은 두 취약점에 영향을 받을 수 있습니다.

####  패치 버전

이 취약점의 심각도가 높으므로 패치가 제공되는 즉시 노드를 [ 수동으로 업그레이드
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=ko#upgrading-nodes) 하는 것이 좋습니다.

|  높음  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  2018년 5월 30일

설명  |  심각도  |  참고  
---|---|---  
  
Git에서 최근 발견된 취약점은 권한 없는 사용자가 gitRepo 볼륨이 포함된 Pod를 생성할 수 있을 경우 Kubernetes 내의 권한
에스컬레이션이 가능할 수도 있다는 문제를 안고 있습니다. 이 CVE는 [ CVE-2018-11235
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235) 태그로 식별됩니다.

####  영향을 받는지 여부는 어떻게 확인하나요?

다음 항목이 모두 해당된다면 이 취약점의 영향을 받는 것입니다.

  * 신뢰할 수 없는 사용자가 Pod를 생성하거나 Pod 생성을 트리거할 수 있습니다. 
  * 신뢰할 수 없는 사용자가 생성한 pod에 호스트 루트 액세스를 방지하는 제한이 있습니다(예: [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=ko) 를 통해 설정한 경우). 
  * 신뢰할 수 없는 사용자가 생성한 pod가 gitRepo 볼륨 유형을 사용할 수 있습니다. 

모든 Kubernetes Engine 노드가 취약합니다.

####  어떻게 해야 하나요?

gitRepo 볼륨 유형의 사용을 금지하세요. PodSecurityPolicy를 통해 gitRepo 볼륨을 사용 금지하려면
PodSecurityPolicy의 ` volumes ` 허용 목록에서 ` gitRepo ` 를 제외하면 됩니다.

이에 상응하는 gitRepo 볼륨 동작은 initContainer에서 git 저장소를 EmptyDir 볼륨으로 클론하여 구현할 수 있습니다.

    
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: git-repo-example
    spec:
      initContainers:
        # This container clones the desired git repo to the EmptyDir volume.
        - name: git-clone
          image: alpine/git # Any image with git will do
          args:
            - clone
            - --single-branch
            - --
            - https://github.com/kubernetes/kubernetes # Your repo
            - /repo # Put it in the volume
          securityContext:
            runAsUser: 1 # Any non-root user will do. Match to the workload.
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
          volumeMounts:
            - name: git-repo
              mountPath: /repo
      containers:
        ...
      volumes:
        - name: git-repo
          emptyDir: {}

####  어떤 패치로 이 취약점을 해결할 수 있나요?

향후 예정된 Kubernetes Engine 출시 버전에 패치가 포함될 예정입니다. 추후에 게시판을 다시 방문하여 자세한 내용을 확인하세요.

|  보통  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  2018년 5월 21일

설명  |  심각도  |  참고  
---|---|---  
  
Linux 커널에서 최근 발견된 몇몇 취약점은 권한 없는 프로세스의 (커널 장애를 통한) 서비스 거부 또는 권한 에스컬레이션이 가능할 수도
있다는 문제를 안고 있습니다. 이러한 CVE는 [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) , [ CVE-2018-8897
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897) , [
CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)
태그로 식별됩니다. 이 취약점은 모든 Kubernetes Engine 노드에 영향을 미치므로 아래의 세부정보를 참고하여 최신 패치 버전으로
[ 업그레이드 ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=ko) 하는 것이 좋습니다.

####  어떻게 해야 하나요?

업그레이드하려면 우선 마스터를 최신 버전으로 업그레이드해야 합니다. 이 패치는 Kubernetes Engine 1.8.12-gke.1,
Kubernetes Engine 1.9.7-gke.1, Kubernetes Engine 1.10.2-gke.1에서 제공됩니다. 이러한 출시
버전에는 Container-Optimized OS와 Ubuntu 이미지의 패치가 포함됩니다.

그 전에 새 클러스터를 만드는 경우 여기에 사용할 패치 버전을 지정해야 합니다. [ 노드 자동 업그레이드
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=ko) 를 사용 설정하고 수동으로는 업그레이드하지 않는 고객은 노드가 향후 몇 주 내에 패치 버전으로 업그레이드됩니다.

####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다.

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : 이 취약점은 Linux 커널에 영향을 미치며, 이로 인해 권한이
없는 사용자나 프로세스가 시스템 커널에 장애를 일으켜 DoS 공격이나 권한 에스컬레이션이 발생할 수 있습니다. 이 문제는 CVSS 7.8점에
해당하는 '높음' 등급의 취약점으로 분류됩니다.

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : 이 취약점은 Linux 커널에 영향을 미치며, 이로 인해 권한이 없는
사용자나 프로세스가 시스템 커널에 장애를 일으켜 DoS 공격이 발생할 수 있습니다. 이 문제는 CVSS 6.5점에 해당하는 '보통' 등급의
취약점으로 분류됩니다.

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : 이 취약점은 Linux 커널의 KVM 하이퍼바이저에 영향을 미치며, 이로
인해 권한이 없는 프로세스가 게스트 커널에 장애를 일으킬 수 있거나 이 프로세스에 권한이 주어질 가능성도 있습니다. Kubernetes
Engine 실행 인프라에서는 이 취약점을 해결하는 패치가 적용되었으므로 Kubernetes Engine은 영향을 받지 않습니다. 이 문제는
CVSS 8.0점에 해당하는 '높음' 등급의 취약점으로 분류됩니다.

|  높음  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  2018년 3월 12일

설명  |  심각도  |  참고  
---|---|---  
  
Kubernetes 프로젝트에서 [ 최근 공개된
](https://groups.google.com/forum/?hl=ko#!topic/kubernetes-security-
announce/P7lBjbjDKd8) 신규 보안 취약점 [ CVE-2017-1002101
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) 과 [
CVE-2017-1002102 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002102) 는 컨테이너가 컨테이너 외부 파일에 액세스할 수 있다는 문제를 안고 있습니다.
이 취약점은 모든 Kubernetes Engine 노드에 영향을 미치므로 아래의 세부정보를 참고하여 최대한 빨리 최신 패치 버전으로
업그레이드하는 것이 좋습니다.

####  어떻게 해야 하나요?

이 취약점의 심각도가 높으므로 노드의 자동 업그레이드 사용 설정 여부와 관계없이 패치가 제공되는 즉시 노드를 [ 수동으로 업그레이드
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=ko) 하는 것이 좋습니다. 패치는 3월 16일까지 모든 고객에게 제공될 예정이지만 사용자의 클러스터가
위치한 영역을 기준으로 [ 출시 일정 ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=ko#march-12-2018) 에 따라 더 일찍 제공될 수도 있습니다.

업그레이드하려면 우선 마스터를 최신 버전으로 업그레이드해야 합니다. 이 패치는 Kubernetes 1.9.4-gke.1, Kubernetes
1.8.9-gke.1, Kubernetes 1.7.14-gke.1에서 제공됩니다. 3월 30일까지는 새 클러스터가 기본적으로 패치 버전을
사용하게 되며, 그 전에 새 클러스터를 만드는 경우에는 여기에 사용할 패치 버전을 지정해야 합니다.

[ 노드 자동 업그레이드 ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=ko) 를 사용 설정하고 수동으로는 업그레이드하지 않는 Kubernetes Engine 고객의 노드는 4월
23일까지 패치 버전으로 업그레이드됩니다. 그러나 취약점의 특성을 고려할 때 패치가 제공되는 즉시 노드를 [ 수동으로 업그레이드
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=ko) 하는 것이 좋습니다.

####  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음 2가지 취약점이 완화됩니다.

취약점 CVE-2017-1002101은 [ subpath
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) 볼륨 마운트를
사용하는 컨테이너가 볼륨 외부의 파일에 액세스할 수 있다는 문제를 안고 있습니다. 즉, PodSecurityPolicy로 컨테이너의
hostpath 볼륨 액세스를 차단하는 경우 pod를 업데이트하거나 생성할 수 있는 공격자가 다른 볼륨 유형으로 임의의 hostpath를
마운트할 수 있게 됩니다.

취약점 CVE-2017-1002102는 특정 볼륨 유형(보안 비밀, 구성 맵, 예상 볼륨 또는 하향식 API 볼륨 등)을 사용하는 컨테이너가
볼륨 외부의 파일을 삭제할 수 있다는 문제를 안고 있습니다. 즉, 이러한 볼륨 유형 중 하나를 사용하는 컨테이너가 손상되거나 신뢰할 수 없는
사용자의 pod 생성이 허용되는 경우 공격자가 이러한 컨테이너로 호스트상의 임의 파일을 삭제할 수 있게 됩니다.

해결책에 대한 자세한 내용은 [ Kubernetes 블로그 게시물
](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-vulnerability/)
을 참조하세요.

|  높음  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

