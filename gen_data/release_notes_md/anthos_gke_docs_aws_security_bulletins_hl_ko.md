A new version of Anthos GKE on AWS was released on August 5. See the [ release
notes ](https://cloud.google.com/anthos/gke/docs/aws/release-notes?hl=ko) for
information on breaking changes.

#  보안 게시판

Anthos GKE on AWS(GKE on AWS)의 보안 게시판에 대해 알아봅니다.

##  GCP-2020-011

**게시:** 2020년 7월 24일  
설명  |  심각도  |  참고  
---|---|---  
  
네트워킹 취약점인 [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) 이 최근 Kubernetes에서
발견되었습니다. 경우에 따라 서비스는 로컬 루프백 인터페이스(127.0.0.1)를 사용하여 동일한 pod에서 실행되는 다른 애플리케이션과
통신합니다. 이 취약점으로 인해 클러스터의 네트워크에 대한 액세스 권한이 있는 공격자가 인접 pod 및 노드의 루프백 인터페이스로 트래픽을
전송할 수 있습니다. pod 외부에서 액세스할 수 없는 루프백 인터페이스를 사용하는 서비스는 악용될 수 있습니다.

GKE on AWS에서 이 취약점을 악용하려면 공격자가 클러스터의 EC2 인스턴스에서 [ 소스 대상 검사
](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html) 를 사용
중지해야 합니다. 이 경우 공격자에게 EC2 인스턴스의 ` ModifyInstanceAttribute ` 또는 `
ModifyNetworkInterfaceAttribute ` 에 대한 AWS IAM 권한이 있어야 합니다. 따라서 이 취약점은 GKE on
AWS에서 심각도 낮음으로 지정되었습니다.

####  어떻게 해야 하나요?

이 취약점을 해결하려면 클러스터를 패치 버전으로 업그레이드하세요. 다음 GKE on AWS 이상 버전에는 이 취약점의 수정 사항이 포함될
예정입니다.

  * GKE on AWS 1.4.2 

####  이 패치로 어떤 취약점이 해결되나요?

이 패치는 [ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315)
취약점을 해결합니다.

|

낮음

|

[ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315)  
  
##  GCP-2020-009

**게시:** 2020년 7월 15일  설명  |  심각도  |  참고  
---|---|---  
  
권한 에스컬레이션 취약점인 [ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559) 가 최근 Kubernetes에서 발견되었습니다. 이 취약점으로 인해 노드를
이미 손상시킨 공격자가 클러스터의 모든 pod에서 명령어를 실행할 수 있습니다. 따라서 공격자는 이미 손상된 노드를 사용하여 다른 노드를
손상시킬 수 있으며 정보를 읽거나 파괴적인 작업을 유발할 수 있습니다.

공격자가 이 취약점을 악용하려는 경우 클러스터의 노드는 이미 손상되었을 것입니다. 이 취약점 자체는 클러스터에 있는 노드를 손상시키지
않습니다.

####  어떻게 해야 하나요?

GKE on AWS GA(1.4.1, 2020년 7월 말 제공) 이상 버전에는 이 취약점의 패치가 포함됩니다. 이전 버전을 사용하는 경우 [
anthos-gke 명령줄 도구의 새 버전을 다운로드
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=ko) 하고
관리 및 사용자 클러스터를 다시 만듭니다.

####  이 패치로 어떤 취약점이 해결되나요?

이러한 패치는 CVE-2020-8559 취약점을 완화합니다. 이 문제는 GKE에서 '보통' 등급의 취약점으로 분류됩니다. 공격자가 클러스터,
노드, 워크로드에 대한 정보를 직접 제공하여 기존의 손상된 노드 외에 이 공격을 효과적으로 이용해야 하기 때문입니다. 이 취약점 자체는
공격자에게 손상된 노드를 제공하지 않습니다.

|

보통

|

[ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559)  
  
##  GCP-2020-007

**게시:** 2020년 6월 1일  
설명  |  심각도  |  참고  
---|---|---  
  
특정 승인된 사용자가 제어 영역 호스트 네트워크에서 최대 500바이트까지 민감한 정보를 누출할 수 있도록 허용하는 서버 측 요청
위조(SSRF) 취약점, [ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555) 가 최근 Kubernetes에서 발견되었습니다. Google
Kubernetes Engine(GKE) 제어 영역은 Kubernetes의 컨트롤러를 사용하기 때문에 이 취약점의 영향을 받습니다. 아래의
세부정보를 참고하여 제어 영역을 최신 패치 버전으로 업그레이드하는 것이 좋습니다. 노드 업그레이드는 필요하지 않습니다.  

####  어떻게 해야 하나요?

Anthos GKE on AWS(GKE on AWS) v0.2.0 이상 버전에는 이 취약점의 패치가 포함되어 있습니다. 이전 버전을 사용하는
경우 [ anthos-gke 명령줄 도구의 새 버전을 다운로드
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=ko) 하고
관리 및 사용자 클러스터를 다시 만듭니다.

####  이 패치로 어떤 취약점이 해결되나요?

이러한 패치는 CVE-2020-8555 취약점을 완화합니다. 악용을 방지하기 위한 여러 제어 영역 강화 조치로 이 문제는 GKE에서 '보통'
등급의 취약점으로 분류됩니다.

특정 볼륨 유형(GlusterFS, Quobyte, StorageFS, ScaleIO)이 내장된 Pod 생성 또는 StorageClass
생성 권한을 보유한 공격자는 마스터의 호스트 네트워크에서 요청 본문을 제어하지 _않아도_ ` kube-controller-manager `
에서 ` GET ` 요청 또는 ` POST ` 요청을 보내도록 만들 수 있습니다. 이러한 볼륨은 GKE에서 거의 사용되지 않으므로 이러한
볼륨이 새로 사용된 것은 유용한 감지 신호일 수 있습니다.

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
  
Kubernetes에서 권한이 있는 컨테이너가 노드 트래픽을 다른 컨테이너로 리디렉션할 수 있도록 허용하는 [ 취약점
](https://github.com/kubernetes/kubernetes/issues/91507) 이 발견되었습니다. 이 공격을 받으면
상호 TLS/SSH 트래픽(예: Kubelet과 API 서버 사이 또는 mTLS를 사용하는 애플리케이션 발생 트래픽)을 읽거나 수정할 수
없습니다. 이 취약점은 모든 Google Kubernetes Engine(GKE) 노드에 영향을 미치므로 아래의 세부정보를 참고하여 최신
패치 버전으로 업그레이드하는 것이 좋습니다.

####  어떻게 해야 하나요?

다음 버전 이상의 [ anthos-gke 명령줄 도구를 다운로드
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=ko) 하고
관리 및 사용자 클러스터를 다시 만듭니다.

  * aws-0.2.1-gke.7 

일반적으로 ` CAP_NET_RAW ` 가 필요한 컨테이너는 거의 없습니다. [ Anthos Policy Controller
](https://cloud.google.com/anthos-config-management/docs/concepts/policy-
controller?hl=ko) 를 통해 또는 pod 사양을 업데이트하여 이 기능과 기타 강력한 기능을 기본적으로 차단해야 합니다.

컨테이너에서 ` CAP_NET_RAW ` 기능을 사용 중지합니다.

  * 이 [ 제약조건 템플릿 ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) 과 함께 Anthos Policy Controller/Gatekeeper를 사용한 후 적용하는 방법도 있습니다. 예를 들면 다음과 같습니다. 
    
        
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
    

  * 또는 pod 사양을 업데이트합니다. 
    
        
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
에는 노드에서 악성 IPv6 스택을 구성하고 노드 트래픽을 공격자가 제어하는 컨테이너로 리디렉션할 수 있는 ` CAP_NET_RAW `
기능(기본 컨테이너 기능 모음에 포함되어 있음)의 취약점이 설명되어 있습니다. 공격자는 이 취약점을 이용해 노드에서 송/수신되는 트래픽을
가로채거나 수정할 수 있습니다. 이 공격을 받으면 상호 TLS/SSH 트래픽(예: Kubelet과 API 서버 사이 또는 mTLS를 사용하는
애플리케이션의 트래픽)을 읽거나 수정할 수 없습니다.

|

보통

|

[ Kubernetes 문제 91507 ](https://github.com/kubernetes/kubernetes/issues/91507)  

