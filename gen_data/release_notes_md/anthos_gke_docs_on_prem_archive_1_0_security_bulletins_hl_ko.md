이전 버전의 GKE On-Prem 문서를 보고 있습니다. [ 최신 문서 보기
](https://cloud.google.com/anthos/gke/docs/on-prem?hl=ko)

#  보안 게시판

이 주제에서는 GKE On-Prem의 모든 보안 게시판에 대해 설명합니다.

취약점은 영향을 받는 당사자가 대처 방안을 마련할 수 있을 때까지 엠바고에 따라 비밀로 유지되는 경우가 많습니다. 이 경우 GKE On-
Prem의 [ 출시 노트 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/release-notes?hl=ko) 에서 이러한 취약점은 엠바고가 해제될 때까지 '보안 업데이트'로
지칭됩니다. 엠바고가 해제되면 패치가 해결한 취약점을 반영하여 출시 노트가 업데이트됩니다.

**참고:** GKE On-Prem에서 멀티 테넌트 워크로드를 실행할 경우 해당 게시판에 각별히 유의하시기 바랍니다. 취약점이 멀티 테넌트
워크로드에 영향을 미칠 가능성이 크기 때문입니다. GKE On-Prem의 보안 경계에 대한 기술적 설명과 이에 따라 워크로드가 받는 영향에
대해서는 [ 다양한 Kubernetes 스택 레이어에서의 격리
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) 를 참조하세요.

사용자에게 제공된 최신 보안 게시판을 보려면 이 페이지의 URL을 사용자의 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 추가합니다.

##  2019년 8월 23일

설명  |  심각도  |  참고  
---|---|---  
  
최근 Monitoring 엔드포인트 보안을 위해 사용되는 RBAC 프록시가 사용자를 올바르게 승인하지 않는 취약점이 발견되어 완화 조치가
수행되었습니다. 따라서 내부 클러스터 네트워크 내에서 승인되지 않은 사용자에게 특정 구성요소의 측정항목이 제공됩니다. 영향을 받는 구성요소는
다음과 같습니다.

  * ` etcd `
  * ` etcd-events `
  * ` kube-apiserver `
  * ` kube-controller-manager `
  * ` kube-scheduler `
  * ` node-exporter `
  * ` kube-state-metrics `
  * ` prometheus `
  * ` alertmanager `

######  어떻게 해야 하나요?

가능한 빨리 이 취약점에 대한 패치가 포함된 [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/downloads?hl=ko#gkectl_latest) 버전으로 [ 업그레이드
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/administration/upgrading-clusters?hl=ko) 하는 것이 좋습니다.

|

중간

|

[ GKE On-Prem 출시 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/downloads?hl=ko#gkectl_latest)  
  
##  2019년 8월 22일

설명  |  심각도  |  참고  
---|---|---  
  
Kubernetes에서 최근 발견한 [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) 취약점에는 클러스터 범위의 [ 커스텀 리소스
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) 인스턴스가 모든 네임스페이스에 존재하는 네임스페이스화된 객체인 것처럼 처리될 수 있다는 문제가 있습니다. 즉, 사용자
및 서비스 계정은 네임스페이스 수준의 RBAC 권한만 있어도 클러스터 범위의 커스텀 리소스와 상호작용할 수 있습니다. 공격자에게
네임스페이스의 리소스에 액세스할 권한이 있으면 이 취약점을 악용할 수 있습니다.

######  어떻게 해야 하나요?

가능한 빨리 이 취약점에 대한 패치가 포함된 [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/downloads?hl=ko#gkectl_latest) 버전으로 [ 업그레이드
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/administration/upgrading-clusters?hl=ko) 하는 것이 좋습니다.

######  이 패치로 어떤 취약점이 해결되나요?

이 패치로 다음의 취약점이 완화됩니다. [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

|

보통

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

