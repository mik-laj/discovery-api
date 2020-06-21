#  출시 노트

이 페이지에서는 구성 동기화의 프로덕션 업데이트에 대해 설명합니다. 새로운 기능이나 업데이트된 기능, 버그 수정, 알려진 문제, 지원 중단된
기능에 대한 공지를 이 페이지에서 확인하세요.

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서 모든
Google Cloud의 최신 제품 업데이트를 확인할 수 있습니다.

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL( ` https://cloud.google.com/feeds/kubernetes-engine-add-on-
config-sync-release-notes.xml ` )을 직접 추가하세요.

##  1.2.0

Config Sync v1.2.0은 일반적으로 프로덕션 환경에서 사용할 수 있습니다. 이 제품의 첫 번째 버전입니다.

###  알려진 문제

**ISSUE:**

저장소에 [ APIService ](https://kubernetes.io/docs/concepts/extend-kubernetes/api-
extension) 를 추가하면 다음 오류 메시지와 함께 Config Sync가 좋지 않은 상태가 됩니다.
'[KNV2002](/kubernetes-engine/docs/add-on/config-
sync/reference/errors#knv2002): 서버 리소스를 가져올 수 없습니다: 서버 API의 전체 목록을 검색할 수
없습니다.' 이 문제는 이 저장소에서 동기화되는 새 클러스터와 기존 클러스터 모두에 영향을 줍니다. 문제를 해결하려면 다음 안내를 따르세요.

* ` kubectl get pods -n config-management-system ` 을 사용하여 ` git-importer ` 와 ` syncer ` pod 이름을 찾습니다. 
* 이름을 복사하고 ` kubectl delete -n config-management-system pods git-importer-xxxx-xxxx syncer-xxxx-xxxx ` 로 pod를 다시 시작합니다. 
* 이 단계는 클러스터마다 한 번씩 필요합니다. 
클러스터의 pod가 다시 시작되면 동기화가 정상으로 돌아갑니다.

**ISSUE:**

` nomos view ` 는 저장소의 로컬 클론에 존재하지만 아직 클러스터에 동기화되지 않은 CRD(커스텀 리소스 정의)를 파싱하지 못할
수 있습니다.

이 문제를 해결하려면 ` nomos view ` 대신 [ ` nomos hydrate `
](https://cloud.google.com/kubernetes-engine/docs/add-on/config-sync/how-
to/nomos-command?hl=ko#hydrate) 를 사용합니다.

