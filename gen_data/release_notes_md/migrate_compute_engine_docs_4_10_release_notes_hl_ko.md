#  출시 노트

이 페이지에서는 Migrate for Compute Engine의 프로덕션 업데이트를 문서화합니다. 이 페이지를 정기적으로 확인하여 새로운
기능이나 업데이트된 기능, 버그 수정, 알려진 문제, 지원 중단된 기능에 대한 공지를 볼 수 있습니다.

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서
Google Cloud의 모든 최신 제품 업데이트를 확인할 수 있습니다.

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL( ` https://cloud.google.com/feeds/migrate-for-compute-engine-
release-notes.xml ` )을 직접 추가하세요.

이 출시 버전 및 기타 버전의 빌드 목록은 [ 빌드 기록 ](https://cloud.google.com/migrate/compute-
engine/docs/build-history?hl=ko) 을 참조하세요.

##  요구사항 및 OS 지원

[ 요구사항 ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/concepts/requirements?hl=ko) 및 [ 지원되는 운영체제
](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=ko) 를 참조하세요.

##  4.10 새로운 기능

###  Cloud Console 통합

**FEATURE:**

V4.10은 [ GCP Console ](https://cloud.google.com/cloud-console/?hl=ko) 과 통합되어
마이그레이션 관리자를 원활하게 배포하고 필요한 서비스 계정을 생성할 수 있습니다.

###  비공개 액세스 환경에 배포

**FEATURE:**

V4.10은 API 비공개 액세스가 사용 설정된 환경에 배포를 지원합니다. 이러한 환경에서는 시스템이 공개 IP 없이 배포되며 비공개
액세스를 사용하여 Cloud API에 액세스합니다. [ 마이그레이션 관리자 구성
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/configure-
manager/configuring-migration-manager?hl=ko) 을 참조하세요.

###  vCenter 플러그인 선택 배포

**FEATURE:**

V4.10에서는 vCenter 플러그인 배포 여부와 관계없이 온프렘 소스 vCenter 환경에 배포하는 옵션이 있습니다. vCenter
플러그인 없이 배포하면 여러 개의 Migrate 시스템을 동일한 vCenter 환경에 연결할 수 있습니다. [ VMware vCenter
환경 등록 ](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-
to/configure-manager/configuring-vms-
vm?hl=ko#register_the_vmware_vcenter_environment) 을 참조하세요.

###  Windows 2008을 2012로 업그레이드할 때 사전/사후 커스텀 스크립트 지원

**FEATURE:**

V4.10은 Windows 업그레이드를 사용할 때 사전/사후 커스텀 스크립트 실행을 지원합니다. VM에 커스텀 스크립트를 추가할 수
있습니다. 자세한 내용은 [ Windows Server VM 업그레이드
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/upgrading-
vms/upgrading-windows-vms?hl=ko) 를 참조하세요.

###  Azure Gen2 인스턴스를 Compute Engine으로 마이그레이션 지원

**FEATURE:**

V4.10에는 [ Azure Gen2 ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=ko) 인스턴스에서 UEFI가 지원되는
Compute Engine 인스턴스로의 마이그레이션이 지원됩니다.

###  자동 O/S 검색 및 라이선스 할당

**FEATURE:**

V4.10은 기본적으로 마이그레이션된 VM에 올바른 라이선스를 할당하는 마이그레이션된 OS를 자동으로 식별합니다. Windows BYOL
라이선스 또는 Linux 프리미엄 라이선스를 사용하여 VM을 마이그레이션하려는 경우, 이를 런북에 입력으로 제공해야 합니다. 문서의 [
라이선스 섹션 ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/runbooks?hl=ko) 을 참조하세요.

##  4.10.1

###  해결된 문제

**FIXED:**

특정 볼륨 구조의 Windows 파티션 인식 문제가 해결되었습니다.

**FIXED:**

4TB를 초과하는 Azure 디스크 지원 기능이 추가되었습니다.

##  4.10

###  해결된 문제

**FIXED:**

마이그레이션 후에 Windows 이미지가 비정상 종료되는 AWS ena 드라이버 관련 문제가 수정되었습니다.

##  4.10

###  알려진 문제

**ISSUE:**

**#160405343:** SUSE의 활성화 과정에서 [ 동작 변경
](https://www.suse.com/support/kb/doc/?id=000019633) 으로 인해 이제 분리 후 SUSE
Enterprise Linux 인스턴스에서 저장소를 구성할 수 없습니다.

**해결 방법:** 마이그레이션하기 전에 또는 분리하기 전에 다음 해결 방법을 사용할 수 있습니다.

  1. [ https://www.suse.com/support/kb/doc/?id=000019633 ](https://www.suse.com/support/kb/doc/?id=000019633) 에서 Situation 4에 설명된 안내에 따라 Compute Engine에 필요한 패키지를 tar.gz 파일로 다운로드하세요. 
  2. **SLES 12.x의 경우** , 다음 명령어를 실행합니다. 
    
        sha1sum late_instance_offline_update_gce_SLE12.tar.gz
    tar -xf late_instance_offline_update_gce_SLE12.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm

  3. **SLES 15.x의 경우** , 다음 명령어를 실행합니다. 
    
        sha1sum late_instance_offline_update_gce_SLE15.tar.gz
    tar -xf late_instance_offline_update_gce_SLE15.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm

**ISSUE:**

**#149004085:** 온프레미스의 Ubuntu 14는 분리 후 네트워킹 시작에 실패할 수 있습니다.

**해결 방법:** 직렬 콘솔을 통해 연결하고 DHCP로 네트워크 인터페이스를 수동으로 추가합니다.

**ISSUE:**

**#145086776:** 드물지만 RHEL7의 이전 버전이 스트리밍 중에 중단되거나 커널 패닉이 발생할 수 있습니다. 이 문제는 이후
버전의 RHEL7에서 해결되었습니다.

**해결 방법:** 마이그레이션 전에 ` sudo yum update ` 를 실행하여 시스템을 업데이트합니다.

**ISSUE:**

**#145644737:** cloud-init를 사용하는 Linux 배포 인스턴스에서 Azure 또는 AWS에 생성된 클론은 Linux
준비 패키지를 설치한 후 부팅 문제가 발생할 수 있습니다.

**해결 방법:** 클론하기 전에 패키지를 제거하고 마이그레이션을 준비할 때 다시 설치합니다.

**ISSUE:**

**#143313211:** RHEL 6.8 VM을 마이그레이션하는 고객이 클라우드 대상에서 부팅 문제를 겪을 수 있습니다.

커널 버전 2.6.32-xxx를 사용하고 LVM을 사용하는 RHEL 6.x 시스템은 마이그레이션 중에 Compute Engine에서 부팅할
때 커널 패닉이 발생할 수 있습니다.

**해결 방법:** 마이그레이션 전에 커널을 2.6.32-754 이상으로 업그레이드해야 합니다.

**ISSUE:**

**#143262721:** 데이터 디스크가 4테라바이트를 초과하면 Azure의 VM 마이그레이션이 실패합니다.

현재 Migrate for Compute Engine은 4TB 초과의 데이터 디스크가 있는 Azure VM 마이그레이션을 지원하지 않습니다.

**해결 방법:** VM에 4TB 미만의 데이터 디스크가 있는지 확인합니다.

**ISSUE:**

**#131532690:** Symantec Endpoint Protection(SEP)이 설치된 경우 클라우드 실행(Run-in-
cloud) 및 마이그레이션 작업이 Windows Server 2016 워크로드에 실패할 수 있습니다. SEP가 사용 중지된 것으로 보이는
경우에도 이 문제가 발생할 수 있습니다.

**해결 방법:** 워크로드 네트워크 인터페이스 바인딩을 수정하여 SEP 옵션을 삭제합니다.

  1. [ Microsoft Network VSP Bind(nvspbind) ](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850) 를 다운로드합니다. 
  2. Microsoft_Nvspbind_package.EXE를 c:\temp에 설치합니다. 
  3. 관리자 권한으로 명령 프롬프트를 열고 다음을 실행합니다. 
    
        nvspbind.exe /d * symc_teefer2

**ISSUE:**

**#131614405:** Velostrata Prep RPM이 SUSE Linux Enterprise Server 11에 설치된 경우
VM은 기존의 고정 IP 구성 외에도 DHCP IP 주소를 가져옵니다. 이 문제는 VM이 DHCP 서비스가 사용 설정된 서브넷에서
온프레미스로 시작될 때 발생합니다.

참고: 서브넷에 DHCP 서비스가 없으면 문제가 발생하지 않습니다. 원래의 고정 IP 주소와의 통신 연결에 영향을 미치지 않습니다.

**ISSUE:**

**#131637800:** Velostrata 플러그인을 등록한 후 Cloud Extension 마법사를 실행하면 'Finish(마침)'
시 'XXXXXXXXXX' 오류가 발생할 수 있습니다.

**해결 방법:** Velostrata 플러그인을 등록 취소하고 vSphere Web Client 서비스를 다시 시작한 다음 플러그인을 다시
등록합니다. 문제가 지속되면 지원팀에 문의하세요.

**ISSUE:**

**#131548730:** 경우에 따라 타사 VM 수준 백업 솔루션이 임시 스냅샷을 보유하고 있는 동안 VM이 클라우드 실행(Run-in-
cloud)으로 이동하는 경우, 백업 솔루션이 임시 스냅샷을 삭제한 후에도 Migrate for Compute Engine의 주기적인 다시
쓰기 작업이 완료되지 않습니다. VM의 커밋되지 않은 쓰기 카운터는 크기가 증가하며 일관성 체크포인트가 온프레미스에서 생성되지 않습니다.

**해결 방법:** VM에 대해 Run on Premises(온프레미스로 실행)를 선택하고 작업이 완료될 때까지 기다리면 대기중인 모든
쓰기가 커밋됩니다. 그런 다음 Run on Premises(온프레미스로 실행)를 다시 선택합니다. 대기중인 쓰기가 많은 경우 커밋하는 데
시간이 걸릴 수 있습니다. Force(강제) 옵션을 사용하면 커밋되지 않은 쓰기가 손실될 수 있으므로 사용하지 마세요.

**ISSUE:**

**#131605387:** vCenter 재부팅으로 인해 vCenter의 Velostrata 작업이 UI에서 사라집니다. 이것은
vCenter 제한사항입니다.

**해결 방법:** Velostrata PowerShell 모듈을 사용하여 현재 실행 중인 Velostrata 관리형 VM 또는 Cloud
Extension 작업을 모니터링합니다.

**ISSUE:**

**#131638716:** 유지보수 모드의 ESXi 호스트가 있는 상태에서 VM이 클라우드로 이동하면 작업이 실패하고 롤백 단계에서
멈춥니다.

**해결 방법:** 클라우드 실행(Run-in-cloud) 작업을 수동으로 취소하고 VM을 클러스터의 다른 ESXi 호스트로 마이그레이션한
다음 클라우드 실행(Run-in-cloud) 작업을 다시 시도합니다.

**ISSUE:**

**# 131638455:** 클라우드 실행(Run-in-cloud) 작업이 'Failed to create virtual machine
snapshot. The attempted operation cannot be performed in the current state
(Powered off)(가상 머신을 생성하지 못했습니다. 시도된 작업은 현재 상태(전원 꺼짐)에서 수행될 수 없습니다.)' 오류가
발생하면서 실패합니다.

**해결 방법:** VMware VM 스냅샷 파일이 존재하지 않는 스냅샷을 가리킬 수 있습니다. 지원팀에 문의하여 문제 해결에 도움을
받으세요.

**ISSUE:**

**#131534862:** 드물지만 워크로드를 온프레미스로 실행한 후 워크로드 VMDK가 잠깁니다. 경우에 따라 이 문제는
Velostrata 관리 어플라이언스와 워크로드가 실행 중인 ESXi 호스트 간의 네트워크 장애로 인해 발생합니다.

참고: 1~2 시간 후에 문제가 자동으로 해결됩니다.

**ISSUE:**

**#131550214:** 분리 중에 'Operation was canceled(작업이 취소되었습니다)'라는 오류 메시지와 함께 작업이
실패할 수 있습니다.

**해결 방법:** 분리 작업을 다시 시도합니다.

**ISSUE:**

**#131650367:** 분리 작업 취소 후 분리를 수행할 때 작업이 실패할 수 있습니다.

**해결 방법:** 작업을 재시도합니다.

**ISSUE:**

**#131649978:** 특정 시스템 오류가 발생하는 경우 Velostrata 구성요소가 vCenter와 연결이 끊깁니다. 이 경우
이벤트가 전송되지 않아 경보가 제대로 설정되지 않거나 제대로 삭제되지 않을 수 있습니다.

**해결 방법:** vCenter에서 경보를 수동으로 삭제합니다.

**ISSUE:**

**#131532549:** 소매용 라이선스를 사용하는 Windows 시스템의 워크로드인 경우 클라우드에서 돌아올 때 라이선스가 없습니다.

**해결 방법:** 라이선스를 다시 설치합니다.

**ISSUE:**

**#131555885:** 클라우드의 VM이 캐시 모드로 실행 중인 경우 vCenter 'Export OVA(OVA 내보내기)' 작업이
사용 가능하지만 이 작업을 수행하면 OVA가 손상됩니다.

**해결 방법:** 분리 후에만 OVA를 생성합니다.

**ISSUE:**

**#131647857:** 드물지만 클라우드 구성요소 인스턴스가 생성되고 태그가 지정되기 전에 시스템에 장애가 발생하면 인스턴스가 태그되지
않은 상태로 유지됩니다. 이렇게 되면 CE를 완전히 삭제하거나 복구할 수 없습니다.

**해결 방법:** 인스턴스에 수동으로 태그를 지정한 후 'Repair(복구)'를 실행합니다.

**ISSUE:**

**#131537125:** LVM 구성으로 Ubuntu OS를 실행하는 워크로드에는 Cloud Extension 고가용성이 작동하지
않습니다.

**해결 방법:** 커널을 3.13.0-161 이상으로 업데이트합니다.

**ISSUE:**

**#131560126:** Suse12: 4.2 이전 SUSE 커널의 버그로 인해 BTRFS 마운트를 하위 볼륨으로 포함하는 구성은
지원되지 않습니다.

**해결 방법:** SUSE 버전을 커널 4.2(SP2) 이상으로 업그레이드 합니다.

**ISSUE:**

**#131533480:** Cloud Extension 생성 마법사를 사용할 때 잘못된 HTTP 프록시 주소를 사용해도 경고 메시지가
생성되지 않습니다.

**해결 방법:** CE를 삭제한 다음 유효한 HTTP 프록시 주소로 CE를 생성하세요.

**ISSUE:**

**#131647654:** 온프레미스 실행 작업이 성공했지만 상태가 'Failed to consolidate snapshots(스냅샷 통합
실패)'와 함께 실패로 표시됩니다.

**해결 방법:** vCenter를 통해 스냅샷을 통합하고 오류를 수동으로 지웁니다.

**ISSUE:**

**#131558198:** 클라우드 간 런북용 PowerShell 클라이언트가 PowerShell 3.0에서 실행할 때 오류를 보고합니다.

**해결 방법:** PowerShell 4.0으로 업그레이드합니다.

**ISSUE:**

**#131533056:** RHEL 7.4를 AWS에서 Google Cloud로 마이그레이션할 때 Google Cloud 에이전트가
자동으로 설치되지 않습니다.

**해결 방법:** 수동으로 AWS 에이전트를 삭제하고 Google Cloud 에이전트를 설치합니다.

**ISSUE:**

**#131532713:** Windows 2003R2의 오프라인 마이그레이션 후 NIC가 수동으로 삭제된 경우, 자동으로 감지되고 자동으로
재설치할 수 없습니다.

해결 방법: VM 스토리지를 다른 VM에 연결할 수 있으며 NIC 레지스트리 항목을 유사한 VM을 참조로 수동으로 가져올 수 있습니다.
지원팀에 문의하세요.

**ISSUE:**

**#131532666:** 커널 버전 2.6.32로 실행되는 Linux 버전에서 임시 스토리지 액세스 실패시 커널 패닉이 발생할 수
있습니다. 이는 iSCSI를 통해 스트리밍할 때 발생할 가능성이 더 높습니다.

해결 방법: 커널을 업그레이드합니다. 분리 후에는 문제가 발생할 가능성도 줄어듭니다.

**ISSUE:**

**#131532846:** 특정 방화벽 및 바이러스 백신이 있으면 iSCSI 트래픽을 차단하여 클라우드로 이동할 때 Windows VM이
실패할 수 있습니다.

해결 방법: 마이그레이션하는 동안 영향을 받는 서비스를 사용 중지하고 분리 후에 재설치합니다.

**ISSUE:**

**#131532882:** 경우에 따라 Windows 업데이트 중에 클라우드 실행(Run-in-cloud)을 시작하면 업데이트가 갑자기
종료되고 클라우드에서 부팅되지 않을 수 있습니다.

해결 방법: 마이그레이션하기 전에 시스템이 Windows 업데이트를 완료하거나 Windows 업데이트를 정지합니다.

**ISSUE:**

**#135664281:** Azure에서 Google Cloud로의 마이그레이션을 완료하거나 취소할 때 Velostrata 관리에서
Importer를 시작하지 못한 경우 Velostrata에서 만든 리소스가 원래 인스턴스의 리소스 그룹에 남아 있을 수 있습니다.

**ISSUE:**

**#133137658:** 시나리오: 마이그레이션 관리자와 VSphere의 네트워크 연결이 없습니다.

고객 영향: RunInCloud 작업은 VSphere에서 getReadSessions 호출 실패로 인해 처리되지 않습니다.

**해결 방법** : 네트워크 연결을 수정합니다. 안된다면 작업을 취소하고 다시 시도합니다.

**ISSUE:**

**#135573857** 시나리오: 'force' 플래그로 VM을 온프렘으로 다시 이동할 때 스냅샷을 통합하지 못하면 VM이
Velostrata에서 관리하는 상태로 유지됩니다. 동일한 VM의 RunInCloud는 관리형 VM에서 허용되지 않으므로 실패할 수
있습니다.

**해결 방법:** 몇 분 정도 기다린 후 다시 시도하세요.

**ISSUE:**

**#137082702:** 드물지만 분리 취소 작업이 성공하지만 VM 인스턴스 시작이 실패합니다.

**해결 방법** : 인스턴스를 다시 이동하고 클라우드로 다시 이동합니다.

