#  출시 노트

이 페이지에서는 Anthos GKE On-Prem의 프로덕션 업데이트에 대해 설명합니다. 이 페이지를 정기적으로 확인하여 새로운 기능이나
업데이트된 기능, 버그 수정, 알려진 문제, 지원 중단된 기능에 대한 공지를 볼 수 있습니다.

참조:

  * [ 다운로드 ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=ko)
  * [ 버전 관리 및 업그레이드 ](https://cloud.google.com/anthos/gke/docs/on-prem/versioning-and-upgrades?hl=ko)
  * [ 클러스터 업그레이드 ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=ko)
  * [ 관리 워크스테이션 업그레이드 ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=ko)

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서 모든
Google Cloud의 최신 제품 업데이트를 확인할 수 있습니다.

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL( ` https://cloud.google.com/feeds/gkeonprem-release-notes.xml `
)을 직접 추가하세요.

##  2019년 8월 22일

GKE On-Prem 버전 1.0.2-gke.3이 출시되었습니다. 이 패치 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  새로운 기능

**FEATURE:**

이제 Seesaw가 수동 부하 분산에 지원됩니다.

**FEATURE:**

이제 관리자 및 사용자 클러스터에 대해 다른 vSphere 네트워크를 지정할 수 있습니다.

**FEATURE:**

이제 ` gkectl ` 을 사용하여 사용자 클러스터를 삭제할 수 있습니다. [ 사용자 클러스터 삭제
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/administration/deleting-a-user-cluster?hl=ko) 를 참조하세요.

###  변경사항

**CHANGED:** 이제 ` gkectl diagnose snapshot ` 이 사용자 클러스터 제어 영역에서 로그를 가져옵니다.

**CHANGED:**

GKE On-Prem OIDC 사양이 여러 가지 새 필드( ` kubectlredirecturl ` , ` scopes ` , `
extraparams ` , ` usehttpproxy ` )로 업데이트되었습니다.

**CHANGED:**

Calico 버전 3.7.4로 업데이트되었습니다.

**CHANGED:**

Cloud Monitoring의 시스템 측정항목이 ` external.googleapis.com/prometheus/ ` 에서 `
kubernetes.io/anthos/ ` 로 프리픽스가 변경되었습니다. 측정항목 또는 알림을 추적하는 경우 다음 프리픽스로 대시보드를
업데이트하세요.

###  수정됨

**FIXED:**

[ CVE-2019-11247의 취약점이 해결되었습니다 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/security-bulletins?hl=ko#august-22-2019) .

**FIXED:**

[ RBAC 프록시의 취약점이 해결되었습니다 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/security-bulletins?hl=ko#august-23-2019) .

##  2019년 7월 30일

GKE On-Prem 버전 1.0.1-gke.5가 출시되었습니다. 이 패치 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  새로운 기능

**FEATURE:**

[ GKE On-Prem 간략한 도움말 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/reference/cheatsheet?hl=ko) 이 게시되었습니다.

###  변경사항

**CHANGED:**

고정 IP를 사용하는 경우 이제 ` gkectl check-config ` 도 노드 IP 가용성을 확인합니다.

**CHANGED:**

이제 ` gkectl prepare ` 에서 VM이 존재하는지, vSphere에서 템플릿으로 표시되는지 확인한 후 VM의 OVA 이미지
업로드를 시도합니다.

**CHANGED:**

해당 클러스터의 vCPU 클러스터 및 리소스 풀 지정 지원을 추가합니다.

**CHANGED:**

F5 BIG-IP 컨트롤러를 버전 1.9.0으로 업그레이드합니다.

**CHANGED:**

Istio 인그레스 컨트롤러를 버전 1.2.2로 업그레이드합니다.

###  수정

**FIXED:**

관리 워크스테이션의 Docker 레지스트리 관련 레지스트리 데이터 지속성 문제가 해결되었습니다.

**FIXED:**

사용자 클러스터의 이름이 이미 사용 중인지 확인하는 검사가 수정되었습니다.

##  2019년 6월 17일

이제 GKE On-Prem이 일반 안정화 버전으로 제공됩니다. 버전 1.0.10에는 다음과 같은 변경사항이 포함되어 있습니다.

###  베타 1.4에서 1.0.10으로 업그레이드

베타 클러스터를 첫 번째 일반 안정화 버전으로 업그레이드하기 전에 [ GKE On-Prem 베타에서 일반 안정화 버전으로 업그레이드
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/upgrading/from-beta?hl=ko) 에 설명된 단계를 수행하고 다음 사항을 검토하세요.

  * 베타 1.4 이전 버전을 사용하는 경우 먼저 베타 1.4 버전으로 업그레이드해야 합니다. 

  * 베타 클러스터가 기본 F5 BIG-IP가 아닌 자체 L4 부하 분산기를 실행하는 경우 최신 GKE On-Prem 버전을 실행하려면 클러스터를 삭제하고 다시 만들어야 합니다. 

  * 클러스터가 베타 1.3에서 베타 1.4로 업그레이드된 경우 업그레이드하기 전에 _각 사용자 클러스터에 대해_ 다음 명령어를 실행합니다. 
    
        kubectl delete crd networkpolicies.crd.projectcalico.org

  * 이제 vCenter 인증서 확인이 필요합니다. ( ` vsphereinsecure ` 는 더 이상 지원되지 않습니다.) 베타 1.4 클러스터를 1.0.10으로 업그레이드하는 경우 업그레이드 구성 파일에 vCenter 신뢰할 수 있는 루트 CA 공개 인증서를 제공해야 합니다. 

  * 실행 중인 클러스터를 _모두_ 업그레이드해야 합니다. 이 업그레이드를 완료하려면 클러스터를 혼합 버전 상태에서 실행할 수 없습니다. 

  * 먼저 관리 클러스터를 최신 버전으로 업그레이드한 다음 사용자 클러스터를 업그레이드해야 합니다. 

###  새로운 기능

**FEATURE:**

이제 [ 수동 부하 분산 모드 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/manual-lb?hl=ko) 를 사용 설정하여 L4 부하
분산기를 구성할 수 있습니다. 기본 부하 분산기인 F5 BIG-IP를 계속 사용할 수도 있습니다.

**FEATURE:**

GKE On-Prem의 구성 기반 설치 프로세스가 업데이트되었습니다. 이제 단일 [ 구성 파일
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/concepts/overview?hl=ko#config) 을 사용하여 선언적으로 설치합니다.

**FEATURE:**

` gkectl create-config ` 을 추가합니다. 그러면 GKE On-Prem을 설치하고 기존 클러스터를 업그레이드하고 기존
설치에 추가 사용자 클러스터를 만들 수 있는 구성 파일이 생성됩니다. 이렇게 하면 이전 버전의 설치 마법사와 ` create-
config.yaml ` 가 바뀝니다. [ GKE On-Prem 설치
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/install?hl=ko#generate_config) 에 대한 업데이트된 문서를 참조하세요.

**FEATURE:**

GKE On-Prem 구성 파일의 유효성을 검사하는 ` gkectl check-config ` 를 추가합니다. [ GKE On-Prem 설치
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/install?hl=ko#validate_config) 에 대한 업데이트된 문서를 참조하세요.

**FEATURE:**

선택사항인 ` --validate-attestations ` 플래그를 ` gkectl prepare ` 에 추가합니다. 이 플래그는 관리
워크스테이션에 포함된 컨테이너 이미지를 Google에서 만들고 서명했으며 이제 배포할 수 있음을 나타냅니다. [ GKE On-Prem 설치
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/install?hl=ko#prepare) 에 대한 업데이트된 문서를 참조하세요.

###  변경사항

**CHANGED:**

Kubernetes 버전을 1.12.7-gke.19로 업그레이드합니다. 이제 이 버전으로 [ 클러스터를 업그레이드
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/administration/upgrading-clusters?hl=ko) 할 수 있습니다. Kubernetes 버전
1.11.2-gke.19를 실행하는 클러스터는 더 이상 만들 수 없습니다.

사용자 클러스터를 업그레이드하기 전에 관리 클러스터를 업그레이드하는 것이 좋습니다.

**CHANGED:**

Istio 인그레스 컨트롤러를 버전 1.1.7로 업그레이드합니다.

**CHANGED:**

이제 vCenter 인증서 확인이 필요합니다. ( ` vsphereinsecure ` 은 더 이상 지원되지 않습니다.) GKE On-Prem
구성 파일의 ` cacertpath ` 필드에 인증서를 제공합니다.

클라이언트가 vCenter 서버를 호출할 때, vCenter는 인증서를 제시하여 클라이언트에 ID를 증명해야 합니다. 이 인증서는 인증
기관(CA)에서 서명해야 합니다. 인증서는 자체 서명할 수 없습니다.

베타 1.4 클러스터를 1.0.10으로 업그레이드하는 경우 업그레이드 구성 파일에 vCenter 신뢰할 수 있는 루트 CA 공개 인증서를
제공해야 합니다.

###  알려진 문제

**ISSUE:**

[ 클러스터를 업그레이드 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/upgrading-clusters?hl=ko) 하면 [ PodDisruptionBudget
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) (PDB)를 사용하는 워크로드에 장애 또는 다운타임이 발생할 수 있습니다.

**ISSUE:**

[ 수동 부하 분산 모드 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/manual-lb?hl=ko) 를 사용하는 베타 클러스터를
GKE On-Prem 1.0.10 버전으로 업그레이드하지 못할 수 있습니다. 이러한 클러스터에서 자체 부하 분산기를 업그레이드하고 계속
사용하려면 클러스터를 다시 만들어야 합니다.

##  2019년 5월 24일

GKE On-Prem 베타 버전 1.4.7이 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  새로운 기능

**FEATURE:**

이제 [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/diagnose?hl=ko#capture_admin) 명령어에서 ` --admin-ssh-key-path `
매개변수는 선택사항입니다.

###  변경사항

**CHANGED:**

2019년 5월 8일에 Cloud Console을 사용하여 GKE On-Prem 클러스터와 상호작용할 수 있는 서비스인 Connect가
변경되었습니다. 새 Connect 에이전트를 사용하려면 Cloud Console에 클러스터를 다시 등록하거나 GKE On-Prem
베타-1.4로 업그레이드해야 합니다.

GKE On-Prem 클러스터와 클러스터에서 실행 중인 워크로드는 중단 없이 계속 작동합니다. 그러나 클러스터를 다시 등록하거나 베타
1.4로 업그레이드해야 Cloud Console에 클러스터가 표시됩니다.

클러스터를 다시 등록하거나 업그레이드하기 전에 서비스 계정에 ` gkehub.connect ` 역할이 있는지 확인합니다. 또한 서비스 계정에
이전 clusterregistry.connect 역할이 있다면 해당 역할을 삭제하는 것이 좋습니다.

서비스 계정에 gkehub.connect 역할을 부여합니다.

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

서비스 계정에 이전 ` clusterregistry.connect ` 역할이 있으면 이전 역할을 삭제합니다.

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

클러스터를 재등록하거나 Anthos GKE On-Prem 베타 1.4로 업그레이드하세요.

[ 클러스터를 재등록 ](https://cloud.google.com/kubernetes-engine/connect/updating-
agent?hl=ko) 하려면 다음 안내를 따르세요.

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]

[ Anthos GKE On-Prem 베타 1.4로 업그레이드
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=ko) 하려면 다음 단계를 따르세요.

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  알려진 문제

**ISSUE:**

Connect 에이전트가 업그레이드 중에 새 버전으로 업데이트되지 않는 문제가 있습니다. 이 문제를 해결하려면 클러스터를 업그레이드한 후
다음 명령어를 실행하세요.

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  2019년 5월 13일

###  알려진 문제

**ISSUE:**

버전 베타-1.2에서 베타-1.3으로 업그레이드된 클러스터는 클러스터의 구성 파일을 손상시키고 향후 클러스터 업그레이드를 방지하는 알려진
문제의 영향을 받을 수 있습니다. 이 문제는 이후의 모든 클러스터 업그레이드에 영향을 미칩니다.

베타 1.2에서 베타 1.3으로 업그레이드된 클러스터를 삭제하고 다시 만들어야 이 문제를 해결할 수 있습니다.

클러스터를 삭제하고 다시 만들지 않고 문제를 해결하려면 각 클러스터의 보안 비밀을 다시 인코딩하고 적용해야 합니다. 다음 단계를 수행합니다.

  1. 관리자 클러스터에 저장된 ` create-config ` 보안 비밀의 콘텐츠를 가져옵니다. 이 작업은 kube-system 네임스페이스에 있는 ` create-config ` 보안 비밀, 그리고 각 사용자 클러스터의 네임스페이스에 있는 ` create-config ` 보안 비밀에 대해 실시해야 합니다. 
    
        kubectl get secret create-config -n kube-system -o jsonpath={.data.cfg} | base64 -d > kube-system_create_secret.yaml
    
        kubectl get secret create-config -n [USER_CLUSTER_NAME] -o jsonpath={.data.cfg} | base64 -d > [USER_CLUSTER_NAME]_create_secret.yaml

  2. 편집기에서 사용자 클러스터별로 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` 파일을 만듭니다. ` registerserviceaccountkey ` 및 ` connectserviceaccountkey ` 의 값이 ` REDACTED ` 가 아닌 경우 추가 작업이 필요하지 않습니다. 보안 비밀을 다시 인코딩하여 클러스터에 기록할 필요가 없습니다. 
  3. 다른 편집기에서 원본 ` create_config.yaml ` 파일을 엽니다. 
  4. ` [USER_CLUSTER_NAME]  _create_secret.yaml ` 에서 ` registerserviceaccountkey ` 및 ` connectserviceaccountkey ` 값을 원본 ` create_config.yaml ` 파일의 값으로 바꿉니다. 변경된 파일을 저장합니다. 
  5. 각 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` 및 ` kube-system_create_secret.yaml ` 파일에 대해 3~5단계를 반복합니다. 
  6. 각 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` 파일 및 ` kube-system_create_secret.yaml ` 파일을 Base64로 인코딩합니다. 
    
        cat [USER_CLUSTER_NAME]_create_secret.yaml | base64 > [USER_CLUSTER_NAME]_create_secret_create_secret.b64
    
        cat kube-system-cluster_create_secret.yaml | base64 >kube-system-cluster_create_secret.b64

  7. 클러스터의 각 보안 비밀에 있는 ` data[cfg] ` 필드를 해당 파일의 콘텐츠로 바꿉니다. 
    
        kubectl edit secret create-config -n [USER_CLUSTER_NAME]
    
      # kubectl edit opens the file in the shell's default text editor
      # Open `first-user-cluster_create_secret.b64` in another editor, and replace
      # the `cfg` value with the copied value
      # Make sure the copied string has no newlines in it!

  8. 각 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` 보안 비밀 및 ` kube-system_create_secret.yaml ` 보안 비밀에 대해 8단계를 반복합니다. 
  9. 업데이트가 완료되었는지 확인하려면 1단계를 반복합니다. 

##  2019년 5월 7일

GKE On-Prem 베타 버전 1.4.1이 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  새로운 기능

**FEATURE:**

이제 [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/diagnose?hl=ko#capture_admin) 명령어에서 ` --admin-ssh-key-path `
매개변수는 선택사항입니다.

###  변경사항

**CHANGED:**

2019년 5월 8일에 Cloud Console을 사용하여 GKE On-Prem 클러스터와 상호작용할 수 있는 서비스인 Connect가
변경되었습니다. 새 Connect 에이전트를 사용하려면 Cloud Console에 클러스터를 다시 등록하거나 GKE On-Prem
베타-1.4로 업그레이드해야 합니다.

GKE On-Prem 클러스터와 클러스터에서 실행 중인 워크로드는 중단 없이 계속 작동합니다. 그러나 클러스터를 다시 등록하거나 베타
1.4로 업그레이드해야 Cloud Console에 클러스터가 표시됩니다.

재등록 또는 업그레이드를 하기 전에 서비스 계정에 gkehub.connect 역할이 있는지 확인합니다. 또한 서비스 계정에 이전
clusterregistry.connect 역할이 있다면 해당 역할을 삭제하는 것이 좋습니다.

서비스 계정에 gkehub.connect 역할을 부여합니다.

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

서비스 계정에 이전 clusterregistry.connect 역할이 있으면 이전 역할을 삭제합니다.

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

클러스터를 재등록하거나 Anthos GKE On-Prem 베타 1.4로 업그레이드하세요.

[ 클러스터를 다시 등록 ](https://cloud.google.com/kubernetes-engine/connect/updating-
agent?hl=ko) 하려면 다음 안내를 따르세요.

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]

[ Anthos GKE On-Prem 베타 1.4로 업그레이드
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=ko) 하려면 다음 단계를 따르세요.

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  알려진 문제

**ISSUE:**

Connect 에이전트가 업그레이드 중에 새 버전으로 업데이트되지 않는 문제가 있습니다. 이 문제를 해결하려면 클러스터를 업그레이드한 후
다음 명령어를 실행하세요.

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  2019년 4월 25일

GKE On-Prem 베타 버전 1.3.1이 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  새로운 기능

**FEATURE:**

이제 ` gkectl diagnose snapshot ` 명령어에 [ ` --dry-run `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/administration/diagnose?hl=ko#performing_a_dry_run_for_a_snapshot) 플래그가
있습니다.

**FEATURE:**

이제 ` gkectl diagnose snapshot ` 명령어는 4개의 [ 시나리오
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/administration/diagnose?hl=ko#snapshot_scenarios) 를 지원합니다.

**FEATURE:**

` gkectl diagnose snapshot ` 명령어는 이제 네임스페이스를 지정하기 위한 정규식을 지원합니다.

###  변경사항

**CHANGED:**

이제 Istio 1.1이 기본 [ 인그레스 컨트롤러 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.3/how-to/administration/upgrading-a-
cluster?hl=ko#upgrading_the_ingress_controller) 입니다. 인그레스 컨트롤러는 관리자 및 사용자
클러스터의 ` gke-system ` 네임스페이스에서 실행됩니다. 이렇게 하면 인그레스의 TLS 관리가 더 쉬워집니다. 인그레스를 사용
설정하거나 업그레이드 후 인그레스를 다시 사용 설정하려면 [ 인그레스 사용 설정
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/installation/install?hl=ko#enabling_ingress) 의 안내를 따르세요.

**CHANGED:**

` gkectl ` 도구는 더 이상 Minikube 및 KVM을 부트스트랩에 사용하지 않습니다. 즉, 관리 워크스테이션 VM에서 중첩된
가상화를 사용 설정할 필요가 없습니다.

###  알려진 문제

**ISSUE:**

GKE On-Prem의 인그레스 컨트롤러는 자동 보안 비밀 검색이 포함된 Istio 1.1을 사용합니다. 하지만 보안 비밀을 삭제하면 보안
비밀 검색용 노드 에이전트에서 보안 비밀 업데이트를 받지 못할 수 있습니다. 따라서 보안 비밀을 삭제하지 마세요. 보안 비밀을 삭제해야 하고
인그레스 TLS가 실패하면 gke-system 네임스페이스에서 인그레스 Pod를 수동으로 다시 시작하세요.

##  2019년 4월 11일

GKE On-Prem 베타 버전 1.2.1이 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  새로운 기능

**FEATURE:**

이제 GKE On-Prem 클러스터가 [ Connect ](https://cloud.google.com/kubernetes-
engine/connect?hl=ko) 를 사용하여 Google에 자동으로 다시 연결됩니다.

**FEATURE:**

이제 사용자 클러스터당 최대 3개의 제어 영역을 실행할 수 있습니다.

###  변경사항

**CHANGED:**

이제 ` gkectl ` 가 클러스터를 만들어 Sphere 및 F5 BIG-IP 사용자 인증 정보를 검증합니다.

###  알려진 문제

**ISSUE:**

회귀 때문에 ` gkectl diagnose snapshot ` 명령어가 잘못된 SSH 키를 사용하므로 사용자 클러스터에서 정보를 수집하지
못하게 됩니다. 지원 기록 문제를 해결하려면 개별 사용자 클러스터 노드에 SSH로 연결하여 수동으로 데이터를 수집해야 할 수 있습니다.

##  2019년 4월 2일

GKE On-Prem 베타 버전 1.1.1이 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  새로운 기능

**FEATURE:**

이제 여러 명령줄 인터페이스 도구가 포함된 사전 구성된 가상 머신 이미지인 [ Open Virtual Appliance(OVA)
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/installation/getting-started?hl=ko#download_ova) 를 사용하여 GKE On-Prem을 설치합니다.
이렇게 변경하면 설치가 더욱 쉬워지고 가상화 레이어가 제거됩니다. 더 이상 Docker 컨테이너 내에서 ` gkectl ` 을 실행할 필요가
없습니다.

베타 1.1.1 이전에 GKE On-Prem 버전을 설치한 경우 문서화된 안내에 따라 새 관리 워크스테이션을 만들어야 합니다. 새 관리
워크스테이션을 설치한 후 SSH 키, 구성 파일, kubeconfigs 및 기타 필요한 파일을 이전 워크스테이션에서 새 워크스테이션으로
복사합니다.

**FEATURE:**

[ 클러스터 백업 및 복원 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.1/how-to/administration/backing-up?hl=ko) 에 대한 문서가
추가되었습니다.

**FEATURE:**

이제 OIDC 및 ADFS를 사용하여 클러스터에 대한 인증을 구성할 수 있습니다. 자세한 내용은 [ OIDC 및 ADFS로 인증
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/security/oidc-adfs?hl=ko) 과 [ 인증
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/concepts/authentication?hl=ko) 을 참조하세요.

###  변경사항

**CHANGED:**

이제 ` gkectl diagnose snapshot ` 를 실행하려면 관리자 클러스터의 비공개 키를 사용해야 합니다.

**CHANGED:**

설치 중에 다중 마스터 사용자 클러스터 배포를 위한 구성 옵션을 추가했습니다.

**CHANGED:**

[ Connect 문서 ](https://cloud.google.com/kubernetes-engine/connect?hl=ko) 가
마이그레이션되었습니다.

###  수정

**FIXED:**

노드가 예기치 않게 삭제될 때 클러스터 네트워킹이 중단되는 문제가 해결되었습니다.

###  알려진 문제

**ISSUE:**

GKE On-Prem의 구성 관리가 버전 0.11에서 0.13으로 업그레이드되었습니다. 시스템의 여러 구성요소 이름이 변경되었습니다. 이전
버전의 리소스를 정리하고 새 인스턴스를 설치하려면 몇 가지 단계를 수행해야 합니다.

활성 상태의 구성 관리 인스턴스가 있는 경우:

  1. 인스턴스를 제거합니다. 
    
        kubectl -n=nomos-system delete nomos --all

  2. 인스턴스의 네임스페이스에 리소스가 없는지 확인합니다. 
    
        kubectl -n nomos-system get all

  3. 네임스페이스를 삭제합니다. 
    
        kubectl delete ns nomos-system

  4. CRD를 삭제합니다. 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  5. 연산자에 대한 모든 kube-system 리소스를 삭제합니다. 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

활성 상태의 구성 관리 인스턴스가 없는 경우:

  1. 구성 관리 네임스페이스를 삭제합니다. 
    
        kubectl delete ns nomos-system

  2. CRD를 삭제합니다. 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  3. 연산자에 대한 모든 kube-system 리소스를 삭제합니다. 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

##  2019년 3월 12일

GKE On-Prem 베타 버전 1.0.3이 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  수정

**FIXED:**

Docker 인증서가 잘못된 위치에 저장되는 문제가 해결되었습니다.

##  2019년 3월 4일

GKE On-Prem 베타 버전 1.0.2가 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  새로운 기능

**FEATURE:**

이제 ` gkectl version ` 을 실행하여 실행 중인 ` gkectl ` 의 버전을 확인할 수 있습니다.

**FEATURE:**

이제 [ 사용자 클러스터를 향후 베타 버전으로 업그레이드 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.0/how-to/administration/upgrading-a-cluster?hl=ko) 할 수
있습니다.

**FEATURE:**

[ Anthos Config Management ](https://cloud.google.com/anthos-config-
management/docs?hl=ko) 버전 0.11.6이 출시되었습니다.

**FEATURE:**

이제 Stackdriver Logging이 각 노드에서 사용 설정됩니다. 기본적으로 로깅 에이전트는 GCP 프로젝트에 제어 영역 서비스,
클러스터 API, vSphere 컨트롤러, Calico, BIG-IP 컨트롤러, Envoy 프록시, Connect, Anthos Config
Management, Prometheus 및 Grafana 서비스, Istio 제어 영역, Docker에 대한 로그만 복제합니다.애플리케이션
컨테이너 로그는 기본적으로 제외되지만, 선택적으로 사용 설정할 수 있습니다.

**FEATURE:**

Stackdriver Prometheus 사이드카는 로깅 에이전트와 동일한 구성 요소의 측정항목을 캡처합니다.

**FEATURE:**

이제 [ Kubernetes 네트워크 정책 ](https://kubernetes.io/docs/concepts/services-
networking/network-policies/) 이 지원됩니다.

###  변경사항

**CHANGED:**

이제 클러스터 사양에서 IP 블록을 업데이트하여 해당 클러스터의 IP 범위를 확장할 수 있습니다.

**CHANGED:**

알파 기간 중에 설치한 클러스터가 베타 기간 후 Google에서 연결이 끊긴 경우 다시 연결해야 할 수 있습니다. [ 수동으로 사용자
클러스터 등록 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/registering-a-user-cluster?hl=ko)
을 참조하세요.

**CHANGED:**

[ 시작하기 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/getting-started?hl=ko) 가 서비스 계정
활성화 및 ` gkectl prepare ` 실행 단계로 업데이트되었습니다.

**CHANGED:**

` gkectl diagnose snapshot ` 는 이제 구성 데이터만 수집하고 로그는 제외합니다. 이 도구는 지원 사례를 열기 전에
환경의 세부정보를 캡처하는 데 사용됩니다.

**CHANGED:**

클러스터 생성 시 F5 BIG-IP의 SNAT 풀 이름 구성(선택사항)을 지원합니다. 이 값은 [ F5 BIG-IP 컨트롤러
](https://clouddocs.f5.com/products/connectors/k8s-bigip-ctlr/v1.8/) 에서 '--
dev-snat-pool-name' 값을 구성하는 데 사용할 수 있습니다.

**CHANGED:**

이제 관리자 클러스터에서 실행되는 부가기능에 VIP를 제공해야 합니다.

###  수정

**FIXED:**

의도하지 않은 노드 삭제를 방지하기 위해 클러스터 크기 조절 작업이 개선되었습니다.

##  2019년 2월 7일

GKE On-Prem 알파 버전 1.3이 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  새로운 기능

**FEATURE:**

이제 설치 중에 YAML 파일에 ` nodeip ` 블록을 제공하여 고정 IPAM을 구성할 수 있습니다.

###  변경사항

**CHANGED:**

이제 vSphere Datastore에서 100GB 디스크를 프로비저닝해야 합니다. GKE On-Prem은 디스크를 사용하여 etcd와 같은
중요한 데이터를 저장합니다. [ 시스템 요구사항 ](https://cloud.google.com/anthos/gke/docs/on-
prem/requirements?hl=ko) 을 참고하세요.

**CHANGED:**

이제 ` nodeip ` 블록에만 소문자 호스트 이름을 제공할 수 있습니다.

**CHANGED:**

GKE On-Prem은 이제 사용자 클러스터에 대해 고유한 이름을 적용합니다.

**CHANGED:**

Istio 엔드포인트를 사용하는 측정항목 엔드포인트 및 API는 이제 mTLS 및 역할 기반 액세스 제어를 사용하여 보호합니다.

**CHANGED:**

Grafana의 외부 통신이 사용 중지되었습니다.

**CHANGED:**

Prometheus 및 Alertmanager 상태 확인을 개선했습니다.

**CHANGED:**

이제 Prometheus는 보안 포트를 사용하여 측정항목을 스크랩합니다.

**CHANGED:**

Grafana 대시보드가 몇 가지 업데이트되었습니다.

###  알려진 문제

**ISSUE:**

vCenter 사용자 계정이 ` DOMAIN\USER ` 과 같은 형식을 사용하는 경우, 백슬래시를 이스케이프 처리해야 할 수도 있습니다(
` DOMAIN\\USER ` ). 설치하는 동안 사용자 계정을 입력하라는 메시지가 표시되면 이 작업을 수행해야 합니다.

##  2019년 1월 23일

GKE On-Prem 알파 버전 1.2.1이 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  새로운 기능

**FEATURE:**

이제 ` gkectl ` 를 사용하여 [ 관리자 클러스터를 삭제
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/administration/deleting-an-admin-cluster?hl=ko) 할 수 있습니다.

.

###  변경사항

**CHANGED:**

이제 ` gkectl diagnose snapshot ` 명령어를 사용하면 원격 명령어 결과 및 파일의 스냅샷을 캡처하면서 노드를 지정할 수
있습니다.

##  2019년 1월 14일

GKE On-Prem 알파 버전 1.1.2가 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  새로운 기능

**FEATURE:**

이제 ` gkectl prepare ` 명령어를 사용하여 GKE On-Prem의 컨테이너 이미지를 가져와서 푸시할 수 있습니다. 그러면 `
populate_registry.sh ` 스크립트가 지원 중단됩니다.

**FEATURE:**

이제 ` gkectl prepare ` 가 vSphere 클러스터와 리소스 풀에 대한 정보를 입력하라는 메시지를 표시합니다.

**FEATURE:**

이제 ` gkectl create ` 명령을 사용하여 기존 관리 제어 영역에 사용자 클러스터를 추가할 수 있습니다. 이를 위해 클러스터 생성
중에 메시지가 표시되면 기존 kubeconfig 파일을 전달합니다.

**FEATURE:**

이제 클러스터를 만들 때 관리자 및 사용자 클러스터에 대한 인그레스 TLS 보안 비밀을 전달할 수 있습니다. 다음과 같은 새 메시지가
표시됩니다.

` Do you want to use TLS for Admin Control Plane/User Cluster ingress? `

TLS 보안 비밀 및 인증서를 제공하면 ` gkectl ` 에서 인그레스 TLS를 설정할 수 있습니다. HTTP는 TLS 설치 시 자동으로
사용 중지되지 않습니다.

###  변경사항

**CHANGED:**

이제 GKE On-Prem은 Kubernetes 버전 **1.11.2-gke.19** 를 실행합니다.

**CHANGED:**

GKE On-Prem에 대한 기본 사용 공간이 변경되었습니다.

  * 이제 사용자 클러스터 노드의 최소 메모리 요구사항은 8192M입니다. 

**CHANGED:**

GKE On-Prem은 minikube 버전 **0.28.0** 에서 실행됩니다.

**CHANGED:**

GKE 정책 관리가 버전 **0.11.1** 로 업그레이드되었습니다.

**CHANGED:**

` gkectl ` 는 더 이상 프록시 구성을 기본으로 제공하라는 메시지를 표시하지 않습니다.

**CHANGED:**

사용자 클러스터 네임스페이스에는 ` cluster-api-etcd-metrics-config ` , ` kube-etcd-metrics-
config ` , ` kube-apiserver-config ` 의 3가지 새로운 ConfigMap 리소스가 있습니다. GKE On-
Prem은 이러한 파일을 사용하여 측정항목 프록시 컨테이너를 빠르게 부트스트랩합니다.

**CHANGED:**

kube-apiserver 이벤트는 이제 자체 etcd에 존재합니다. 사용자 클러스터의 네임스페이스에서 kube-etcd-events를 볼
수 있습니다.

**CHANGED:**

이제 클러스터 API 컨트롤러가 주요 변수 선택을 사용합니다.

**CHANGED:**

이제 vSphere 사용자 인증 정보를 사용자 인증 정보 파일에서 가져옵니다.

**CHANGED:**

` gkectl diagnose ` 명령어가 이제 관리자 및 사용자 클러스터 모두에서 작동합니다.

**CHANGED:**

` gkectl diagnose snapshot ` 는 이제 노드의 원격 파일 스냅샷, 노드의 원격 명령어 결과, Prometheus 쿼리를
만들 수 있습니다.

**CHANGED:**

` gkectl diagnose snapshot ` 는 이제 여러 개의 병렬 스레드에서 스냅샷을 만들 수 있습니다.

**CHANGED:**

이제 ` gkectl diagnose snapshot ` 를 사용하여 스냅샷 결과에서 제외할 단어를 지정할 수 있습니다.

###  수정

**FIXED:**

예기치 않은 네트워크 호출을 발생시킨 minikube 캐싱 문제가 해결되었습니다.

**FIXED:**

F5 BIG-IP 사용자 인증 정보를 가져오는 문제가 해결되었습니다. 이제 환경 변수를 사용하는 대신 사용자 인증 정보 파일에서 사용자 인증
정보를 읽습니다.

###  알려진 문제

**ISSUE:**

` gkectl prepare ` 를 실행할 때 다음과 같은 [ ` govmomi `
](https://github.com/vmware/govmomi) 경고가 표시될 수 있습니다.

` Warning: Line 102: Unable to parse 'enableMPTSupport' for attribute 'key' on
element 'Config' `

**ISSUE:**

사용자 클러스터의 크기를 조정하면 의도하지 않은 노드 삭제 또는 재생성이 발생할 수 있습니다.

**ISSUE:**

PersistentVolume이 마운트되지 않아 ` devicePath is empty ` 오류가 발생합니다. 이 문제를 해결하려면 연결된
PersistentVolumeClaim을 삭제하고 다시 만드세요.

**ISSUE:**

노드에 고정 IP 할당을 사용하는 경우 알파에서는 IPAM 주소 블록의 크기를 조정할 수 없습니다. 이 문제를 해결하려면 현재 필요한 것보다
많은 IP 주소를 할당하는 것이 좋습니다.

**ISSUE:**

속도가 느린 디스크에서는 VM 생성 시간이 초과되어 배포가 실패할 수 있습니다. 이 경우 모든 리소스를 삭제하고 다시 시도하세요.

##  2018년 12월 19일

GKE On-Prem 알파 1.0.4가 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  수정

**FIXED:**

[ CVE-2018-1002105 ](https://github.com/kubernetes/kubernetes/issues/71411) 로
인해 발생한 취약점이 패치되었습니다.

##  2018년 11월 30일

GKE On-Prem 알파 1.0이 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  변경사항

**CHANGED:**

GKE On-Prem 알파 1.0은 Kubernetes 1.11을 실행합니다.

**CHANGED:**

GKE On-Prem에 대한 기본 사용 공간이 변경되었습니다.

  * 관리 제어 영역은 CPU 4개, 메모리 16GB를 사용하는 3개의 노드를 실행합니다. 
  * 사용자 제어 영역은 CPU 4개, 메모리 16GB를 사용하는 1개의 노드를 실행합니다. 
  * 사용자 클러스터는 CPU 4개, 메모리 16GB를 사용하는 최소 3개의 노드를 실행합니다. 

**CHANGED:**

고가용성 Prometheus 설정 지원

**CHANGED:**

커스텀 Alert Manager 구성 지원

**CHANGED:**

Prometheus가 **2.3.2** 에서 **2.4.3** 으로 업그레이드되었습니다.

**CHANGED:**

Grafana가 **5.0.4** 에서 **5.3.4** 로 업그레이드되었습니다.

**CHANGED:**

kube-state-metrics가 **1.3.1** 에서 **1.4.0** 으로 업그레이드되었습니다.

**CHANGED:**

Alert Manager가 **1.14.0** 에서 **1.15.2** 로 업그레이드되었습니다.

**CHANGED:**

node_exporter가 **1.15.2** 에서 **1.16.0** 으로 업그레이드되었습니다.

###  수정

**FIXED:**

[ CVE-2018-1002103 ](https://github.com/kubernetes/minikube/issues/3208) 으로 인해
발생한 취약점이 패치되었습니다.

###  알려진 문제

**ISSUE:**

PersistentVolume이 마운트되지 않아 ` devicePath is empty ` 오류가 발생합니다. 이 문제를 해결하려면 연결된
PersistentVolumeClaim을 삭제하고 다시 만드세요.

**ISSUE:**

노드에 고정 IP 할당을 사용하는 경우 알파에서는 IPAM 주소 블록의 크기를 조정할 수 없습니다. 이 문제를 해결하려면 현재 필요한 것보다
많은 IP 주소를 할당하는 것이 좋습니다.

**ISSUE:**

GKE On-Prem 알파 1.0은 아직 모든 적합성 테스트를 통과하지 못했습니다.

**ISSUE:**

관리자 클러스터당 하나의 사용자 클러스터만 만들 수 있습니다. 추가 사용자 클러스터를 만들려면 다른 관리자 클러스터를 만듭니다.

##  2018년 10월 31일

GKE On-Prem EAP 2.1이 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  변경사항

**CHANGED:**

관리자 및 사용자 클러스터를 동시에 만들면 이제 관리자 클러스터의 F5 BIG-IP 사용자 인증 정보를 다시 사용하여 사용자 클러스터를 만들
수 있습니다. 또한 CLI에서 BIG-IP 사용자 인증 정보를 제공해야 합니다. 이 요구사항은 ` --dry-run ` 를 사용하여 건너뛸
수 없습니다.

**CHANGED:**

F5 BIG-IP 컨트롤러가 최신 OSS 버전 1.7.0을 사용하도록 업그레이드되었습니다.

**CHANGED:**

느린 vSphere 머신의 안정성을 개선하기 위해 이제 클러스터 머신 생성 시간 제한은 15분(이전에는 5분)입니다.

##  2018년 10월 17일

GKE On-Prem EAP 2.0이 출시되었습니다. 이 출시 버전에는 다음과 같은 변경사항이 포함되어 있습니다.

###  변경사항

**CHANGED:**

GKE Connect 지원

**CHANGED:**

Monitoring 지원

**CHANGED:**

비공개 레지스트리를 사용한 설치 지원

**CHANGED:**

F5 BIG-IP에서 L7 부하 분산기를 L4 VIP로 프런트엔드 지원

**CHANGED:**

클러스터 부트스트랩 시 노드의 고정 IP 할당 지원

###  알려진 문제

**ISSUE:**

관리자 클러스터당 하나의 사용자 클러스터만 만들 수 있습니다. 추가 사용자 클러스터를 만들려면 다른 관리자 클러스터를 만듭니다.

**ISSUE:**

EAP 2.0에서는 클러스터 업그레이드가 지원되지 않습니다.

**ISSUE:**

속도가 느린 디스크에서는 VM 생성 시간이 초과되어 배포가 실패할 수 있습니다. 이 경우 모든 리소스를 삭제하고 다시 시도하세요.

**ISSUE:**

클러스터 부트스트랩 프로세스의 일환으로 수명이 짧은 minikube 인스턴스가 실행됩니다. 사용된 minikube 버전에는 [
CVE-2018-1002103 ](https://github.com/kubernetes/minikube/issues/3208) 의 보안
취약점이 있습니다.

