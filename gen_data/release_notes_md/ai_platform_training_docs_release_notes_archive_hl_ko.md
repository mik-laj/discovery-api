#  보관처리된 출시 노트

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서 모든
Google Cloud의 최신 제품 업데이트를 확인할 수 있습니다.

2019년 4월 10일에 Cloud Machine Learning Engine이 [ AI Platform Training
](https://cloud.google.com/ai-platform/training?hl=ko) 및 [ AI Platform
Prediction ](https://cloud.google.com/ai-platform/prediction?hl=ko) 으로
변경되었습니다. 이 페이지에서는 Cloud ML Engine의 이전 업데이트를 설명합니다.

최신 출시 노트를 참조하세요.

  * [ AI Platform Training 출시 노트 ](https://cloud.google.com/ai-platform/training/docs/release-notes?hl=ko)
  * [ AI Platform Prediction 출시 노트 ](https://cloud.google.com/ai-platform/prediction/docs/release-notes?hl=ko)

##  2019년 4월 1일

**FEATURE:**

이제 Cloud ML Engine에서 할인된 가격으로 학습, 온라인 예측, 일괄 예측이 가능합니다.

[ Cloud ML Engine 가격 책정 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=ko) 에 대해 자세히 알아보세요.

##  2019년 3월 28일

**FEATURE:**

이제 Cloud ML Engine에서 기본 제공 알고리즘을 사용한 학습이 가능합니다. 자동 사전 처리를 위해 데이터를 제출하고 코드를
작성하지 않고도 TensorFlow [ 선형 학습자
](https://www.tensorflow.org/tutorials/representation/linear?hl=ko) ,
TensorFlow [ 와이드 앤 딥 ](https://ai.googleblog.com/2016/06/wide-deep-learning-
better-together-with.html) , [ XGBoost
](https://xgboost.readthedocs.io/en/latest/tutorials/model.html) 알고리즘으로 모델을
학습시킬 수 있습니다.

[ 기본 제공 알고리즘을 사용한 학습 ](https://cloud.google.com/ai-
platform/training/docs/algorithms?hl=ko) 에 대해 자세히 알아보세요.

##  2019년 3월 25일

**CHANGED:**

이제 Cloud ML Engine 런타임 버전 1.13에서 TensorFlow 1.13.1을 지원합니다. 런타임 버전 1.13에 포함된
패키지의 전체 목록은 [ 런타임 버전 목록 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=ko) 을 참조하세요.

##  2019년 3월 8일

**FEATURE:**

Cloud ML Engine 런타임 버전 1.9에서 TPU를 사용한 학습 지원이 2019년 3월 8일에 종료되었습니다. 현재 지원되는 버전은
[ 런타임 버전 목록 ](https://cloud.google.com/ai-
platform/training/docs/tensorflow/runtime-version-list?hl=ko#tpu-support) 을
참조하세요.

##  2019년 3월 6일

**FEATURE:**

이제 Cloud ML Engine 런타임 버전 1.13을 학습 및 예측에 사용할 수 있습니다. 이 버전은 TensorFlow 1.13을
지원하며 [ 런타임 버전 목록 ](https://cloud.google.com/ai-platform/training/docs/runtime-
version-list?hl=ko) 에 나열된 다른 패키지를 포함합니다.

현재 TPU를 사용한 학습은 런타임 버전 1.13에서 지원되지 않습니다.

##  2019년 3월 1일

**FEATURE:**

이제 [ AI Platform Notebooks ](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=ko) 가 베타 버전으로 제공됩니다. AI Platform
Notebooks를 사용하면 [ JupyterLab
](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) 및
딥 러닝 소프트웨어 모음과 함께 사전 패키징된 가상 머신(VM) 인스턴스를 만들고 관리할 수 있습니다.

[ AI Platform Notebooks 개요 ](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=ko) 및 [ 새 메모장 인스턴스 만들기 가이드
](https://cloud.google.com/ai-platform/training/docs/notebooks/create-
new?hl=ko) 에서 자세한 내용을 참조하세요.

##  2019년 2월 13일

**FEATURE:**

이제 Cloud TPU가 TensorFlow 모델 학습에 대한 일반 안정화 버전으로 제공됩니다. Tensor Processing
Unit(TPU)은 머신러닝 워크로드를 위해 Google에서 커스텀 개발한 가속기입니다.

Cloud ML Engine에서 [ TPU를 사용하여 모델을 학습 ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-tpus?hl=ko) 시키는 방법을 참조하고 [ 가격 책정
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ko) 에 대해 자세히
알아보세요.

##  2019년 2월 7일

**FEATURE:**

이제 커스텀 컨테이너를 사용한 학습 기능이 베타 버전으로 제공됩니다. 이 기능을 사용하면 커스텀 Docker 이미지로 Cloud ML
Engine에서 학습 애플리케이션을 실행할 수 있습니다. 선택한 ML 프레임워크를 사용하여 커스텀 컨테이너를 빌드할 수 있습니다. [ 커스텀
컨테이너를 사용하여 PyTorch 모델 학습 ](https://cloud.google.com/ai-
platform/training/docs/custom-containers-training?hl=ko) 을 시작해 보세요.

**FEATURE:**

이제 특정 Compute Engine 머신 유형으로 학습 작업을 구성할 수 있습니다. 이렇게 하면 학습 작업에 컴퓨팅 리소스를 보다 유연하게
할당할 수 있습니다. 이 기능은 베타 버전으로 제공됩니다.

Compute Engine 머신 유형으로 작업을 구성할 때 커스텀 GPU 세트를 연결할 수 있습니다.

[ Compute Engine 머신 유형 ](https://cloud.google.com/ai-
platform/training/docs/machine-types?hl=ko#compute-engine-machine-types) , [
GPU 연결 ](https://cloud.google.com/ml-engine/docs/tensorflow/using-
gpus?hl=ko#compute-engine-machine-types-with-gpu) , [ 가격 책정
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ko) 에 대해 자세히
알아보세요.

**FEATURE:**

이제 학습용 P4 GPU가 베타 버전으로 제공됩니다. 자세한 내용은 [ GPU 사용 ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=ko) , [ 리전별 제공 여부
](https://cloud.google.com/ml-
engine/docs/tensorflow/regions?hl=ko#training_with_accelerators) , [ 가격 책정
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ko) 가이드를
참조하세요.

##  2019년 2월 1일

**CHANGED:**

이제 온라인 예측용 쿼드 코어 CPU가 베타 버전으로 제공됩니다. 머신 유형 이름이 변경되었으며 가격이 업데이트되었습니다.

  * 서비스에 사용할 머신 유형을 지정하려면 [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=ko) 에서 ` machineType ` 을 설정합니다. 쿼드 코어 CPU에는 ` mls1-c4-m2 ` 를 사용합니다. 기본값은 단일 코어 CPU인 ` mls1-c1-m2 ` 입니다. 
  * 알파 버전에서 사용된 머신 이름은 **지원 중단** 되었습니다( ` mls1-highmem-1 ` 및 ` mls1-highcpu-4 ` ). 
  * 자세한 내용은 [ 온라인 예측 ](https://cloud.google.com/ai-platform/training/docs/online-predict?hl=ko#machine-types) 가이드를 참조하세요. 
  * 머신 유형 제공은 업데이트된 [ 가격 책정 ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ko) 을 참조하세요. 

##  2019년 1월 25일

**FEATURE:**

이제 us-east4 리전에서 온라인 예측을 사용할 수 있습니다. [ 리전별 제공 여부
](https://cloud.google.com/ai-platform/training/docs/regions?hl=ko) 가이드를
참조하세요.

##  2019년 1월 10일

**FEATURE:**

이제 학습용 V100 GPU가 일반 안정화 버전으로 제공됩니다. 자세한 내용은 [ GPU 사용
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ko) 및 [ 가격
책정 ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ko) 가이드를
참조하세요.

##  2018년 12월 19일

**FEATURE:**

이제 학습 및 예측에 Cloud ML Engine 런타임 버전 1.11 및 1.12를 사용할 수 있습니다. 이러한 버전은 각각
TensorFlow 1.11 및 1.12를 지원하고 [ 런타임 버전 목록 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=ko) 에 나와 있는 다른 패키지도 지원합니다.

Cloud ML Engine 런타임 버전 1.11 및 1.12에 TPU 학습 지원이 추가되었습니다. Version 1.10은 지원되지
않습니다. 현재 지원되는 버전은 [ 런타임 버전 목록 ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=ko#tpu-support) 을 참조하세요.

**CHANGED:**

이제 각 Cloud ML Engine 런타임 버전에 [ joblib
](https://joblib.readthedocs.io/en/latest/) 이 포함됩니다. joblib이 포함된 가장 오래된 런타임
버전은 1.4 버전입니다.

##  2018년 10월 26일

**CHANGED:**

2018년 10월 26일에 Cloud ML 런타임 버전 1.8에 대한 TPU 학습 지원이 종료되었습니다. 현재 지원되는 버전은 [ 런타임
버전 목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ko#tpu-support) 을 참조하세요.

##  2018년 10월 11일

**ISSUE:**

Cloud ML Engine 런타임 버전 1.11은 GPU 학습 중 [ CuDNN 버전 불일치로 발생한 오류
](https://stackoverflow.com/q/52733440) 로 인해 롤백됩니다. 현재 해결 방법은 런타임 버전 1.10을
사용하는 것입니다. 자세한 내용은 [ 런타임 버전 목록 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=ko) 을 참조하세요.

##  2018년 10월 5일

**FEATURE:**

이제 학습 및 예측에 Cloud ML Engine 런타임 버전 1.11을 사용할 수 있습니다. 이 버전은 TensorFlow 1.11 및 [
런타임 버전 목록 ](https://cloud.google.com/ai-platform/training/docs/runtime-
version-list?hl=ko) 에 나열된 다른 패키지를 지원합니다.

##  2018년 8월 31일

**FEATURE:**

이제 학습 및 예측에 Cloud ML Engine 런타임 버전 1.10을 사용할 수 있습니다. 이 버전은 텐서플로우 1.10 및 [ 런타임
버전 목록 ](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=ko) 에 나열된 다른 패키지를 지원합니다.

##  2018년 8월 27일

**FEATURE:**

이제 학습용 V100 GPU가 베타 버전으로 제공됩니다. V100 GPU 사용 시 요금이 부과됩니다. 자세한 내용은 [ GPU 사용
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ko) 및 [ 가격
책정 ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ko) 가이드를
참조하세요.

**FEATURE:**

이제 학습용 P100 GPU가 일반 안정화 버전으로 제공됩니다. 자세한 내용은 [ GPU 사용
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ko) 및 [ 가격
책정 ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ko) 가이드를
참조하세요.

**FEATURE:**

이제 새로운 두 리전(us-west1, europe-west4)에서 학습을 사용할 수 있습니다. 자세한 내용은 [ 지역
](https://cloud.google.com/ai-platform/training/docs/regions?hl=ko) 페이지를
참조하세요.

##  2018년 8월 24일

**CHANGED:**

2018년 8월 24일에 Cloud ML 런타임 버전 1.7에 대한 TPU 학습 지원이 종료되었습니다. 현재 지원되는 버전은 [ 런타임 버전
목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ko#tpu-support) 을 참조하세요.

##  2018년 8월 9일

**CHANGED:**

AI Platform Training을 사용한 온라인 예측 가격이 대폭 인하되었다는 소식을 전하게 되어 기쁩니다.

다음 표에서 이전 가격 및 새 가격을 확인할 수 있습니다.

리전  |  노드별 시간당 이전 가격  |  노드별 시간당 새 가격  
---|---|---  
미국  |  $0.30 USD  |  $0.056 USD  
유럽  |  $0.348 USD  |  $0.061 USD  
아시아 태평양  |  $0.348 USD  |  $0.071 USD  
  
자세한 내용은 [ 가격 책정 가이드 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=ko) 를 참조하세요.

##  2018년 8월 8일

**CHANGED:**

AI Platform Training을 사용한 Cloud TPU를 프로모션 가격으로 제공하므로 상당한 비용 절감 효과를 얻을 수 있게
되었습니다.

다음 표에서 이전 가격 및 새 가격을 확인할 수 있습니다.

리전: 미국  |  TPU별 시간당 이전 가격  |  TPU별 시간당 새 가격  
---|---|---  
확장 등급: ` BASIC_TPU ` _(베타)_ |  $9.7674 USD  |  $6.8474 USD  
커스텀 머신 유형: ` cloud_tpu ` _(베타)_ |  $9.4900 USD  |  $6.5700 USD  
  
이 표에서는 미국 리전 가격만 확인할 수 있습니다. Cloud ML Engine에서의 Cloud TPU 가용성에는 변화가 없습니다. 자세한
내용은 [ 가격 책정 가이드 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=ko) 를 참조하세요.

##  2018년 8월 6일

**FEATURE:**

이제 학습 및 예측에 Cloud ML Engine 런타임 버전 1.9을 사용할 수 있습니다. 이 버전은 텐서플로우 1.9 및 [ 런타임 버전
목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ko) 에 나열된 다른 패키지를 지원합니다.

##  2018년 7월 23일

**FEATURE:**

이제 Cloud ML Engine에서 학습용 **scikit-learn** 및 **XGBoost** 를 지원합니다. 이 기능은 일반 안정화
버전입니다. [ Cloud ML Engine에서 scikit-learn 및 XGBoost를 사용한 학습
](https://cloud.google.com/ml-engine/docs/scikit/getting-started-
training?hl=ko) 가이드를 참조하세요.

**FEATURE:**

**scikit-learn** 및 **XGBoost** 의 온라인 예측 지원이 이제 일반 안정화 버전으로 제공됩니다.

  * 모델 버전을 만들 때 머신러닝 프레임워크를 지정하려면 [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=ko) 에서 ` framework ` 를 설정합니다. 유효한 값은 ` TENSORFLOW ` , ` SCIKIT_LEARN ` , ` XGBOOST ` 입니다. 기본값은 ` TENSORFLOW ` 입니다. ` SCIKIT_LEARN ` 또는 ` XGBOOST ` 를 지정할 경우 ` runtimeVersion ` 도 모델 버전 1.4 이상으로 설정해야 합니다. 
  * [ scikit-learn 및 XGBoost를 사용한 로컬 학습 및 온라인 예측 ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=ko) 가이드를 참조하세요. 

##  2018년 7월 12일

**FEATURE:**

AI Platform Training 리소스( [ 작업 ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=ko) , [ 모델
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models?hl=ko) , [ 모델 버전
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=ko) )에
라벨을 추가한 다음 해당 라벨을 사용하여 리소스를 카테고리별로 정리할 수 있습니다. [ 작업
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.operations?hl=ko) 에도 라벨을 사용할
수 있으며, 이 경우 작업이 적용되는 리소스에 따라 라벨 이름이 지정됩니다. [ 라벨 추가 및 사용
](https://cloud.google.com/ml-engine/docs/tensorflow/resource-labels?hl=ko) 에
대해 자세히 알아보세요.

##  2018년 6월 26일

**CHANGED:**

이제 다음 추가 리전이 완전히 지원됩니다.

  * us-east1 
  * asia-northeast1 

자세한 내용은 [ 리전 가용성 ](https://cloud.google.com/ai-
platform/training/docs/regions?hl=ko) 을 참조하세요.

##  2018년 6월 13일

**CHANGED:**

2018년 6월 13일에 Cloud ML 런타임 버전 1.6에 대한 TPU 학습 지원이 종료되었습니다. 현재 지원되는 버전은 [ 런타임 버전
목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ko#tpu-support) 을 참조하세요.

##  2018년 5월 29일

**CHANGED:**

이제 TensorFlow 1.8 버전과 Cloud ML Engine 런타임 버전 1.8에서 Cloud TPU( _베타_ )를 사용할 수
있습니다.

_배경 정보:_ Cloud TPU는 5월 14일부터 Cloud ML Engine 런타임 버전 1.6 및 1.7에서 사용할 수 있게
되었습니다. 지난 주에 런타임 버전 1.8이 출시되었지만 TensorFlow 1.8 버전에서는 Cloud TPU를 사용할 수 없었습니다.
이제 Cloud ML Engine에서 [ TPU를 사용하여 모델을 학습 ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-tpus?hl=ko) 시키는 방법을 참조하세요.

##  2018년 5월 16일

**FEATURE:**

이제 학습 및 예측에 Cloud ML Engine 런타임 버전 1.8을 사용할 수 있습니다. 이 버전은 텐서플로우 1.8 및 [ 런타임 버전
목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ko) 에 나열된 다른 패키지를 지원합니다.

##  2018년 5월 15일

**FEATURE:**

이제 기존 모델 버전에서 [ 자동 확장 ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=ko#autoscaling)
에 필요한 최소 노드 수를 업데이트할 수 있으며 새 버전을 만들 때 속성을 지정할 수 있습니다.

##  2018년 5월 14일

**FEATURE:**

이제 Cloud ML Engine에서 TensorFlow 모델 학습용으로 Cloud TPU _(베타)_ 를 제공합니다. Tensor
Processing Unit(TPU)은 Google에서 커스텀식으로 개발한 ASIC로, 머신러닝 워크로드를 빠르게 처리하는 데 사용됩니다.
Cloud ML Engine에서 [ TPU를 사용하여 모델을 학습 ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-tpus?hl=ko) 시키는 방법을 참조하세요.

##  2018년 4월 26일

**FEATURE:**

이제 학습 및 예측에 Cloud ML Engine 런타임 버전 1.7을 사용할 수 있습니다. 이 버전은 텐서플로우 1.7 및 [ 런타임 버전
목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ko) 에 나열된 다른 패키지를 지원합니다.

##  2018년 4월 16일

**FEATURE:**

**초매개변수 알고리즘:** 이제 학습 작업에서 초매개변수를 조정할 때 [ HyperparameterSpec
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=ko#hyperparameterspec)
에서 검색 알고리즘을 지정할 수 있습니다. 사용 가능한 값은 다음과 같습니다.

  * ` GRID_SEARCH ` : 가능한 공간 내에서 단순 그리드 검색을 수행합니다. 이 옵션은 가능한 공간의 포인트 수보다 많은 시험 횟수를 지정하려는 경우에 특히 유용합니다. 이러한 경우 그리드 검색을 지정하지 않으면 Cloud ML Engine 기본 알고리즘에서 중복 제안을 생성할 수 있습니다. 그리드 검색을 사용하려면 모든 매개변수는 ` INTEGER ` , ` CATEGORICAL ` 또는 ` DISCRETE ` 유형이어야 합니다. 
  * ` RANDOM_SEARCH ` : 가능한 공간 내에서 단순 무작위 검색을 수행합니다. 

알고리즘을 지정하지 않으면 작업은 기본 Cloud ML Engine 알고리즘을 사용합니다. 이 알고리즘은 매개변수 검색이 매개변수 공간에서
효과적인 검색을 통해 최적의 솔루션이 되도록 유도합니다. 초매개변수 조정에 대한 자세한 내용은 [ 초매개변수 조정 개요
](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-tuning-
overview?hl=ko) 를 참조하세요.

##  2018년 4월 5일

**FEATURE:**

이제 Cloud ML Engine은 온라인 예측용 **scikit-learn** 및 **XGBoost** 를 지원합니다. 이 기능은 _베타_
버전입니다.

  * 모델 버전을 만들 때 머신러닝 프레임워크를 지정하려면 [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=ko) 에서 ` framework ` 를 설정합니다. 유효한 값은 ` TENSORFLOW ` , ` SCIKIT_LEARN ` , ` XGBOOST ` 입니다. 기본값은 ` TENSORFLOW ` 입니다. ` SCIKIT_LEARN ` 또는 ` XGBOOST ` 를 지정할 경우 ` runtimeVersion ` 도 모델 버전 1.4 이상으로 설정해야 합니다. 
  * [ Cloud ML Engine의 scikit-learn 및 XGBoost ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=ko) 가이드를 참조하세요. 

**FEATURE:**

온라인 예측에 Python 3.5를 사용할 수 있습니다.

  * 모델 버전을 만들 때 Python 버전을 지정하려면 [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=ko) 에서 ` pythonVersion ` 을 설정합니다. 기본값은 Python 2.7입니다. 
  * Cloud ML Engine에서 사용 가능한 모든 패키지에 대한 자세한 내용은 [ 런타임 버전 목록 ](https://cloud.google.com/ml-engine/docs/scikit/runtime-version-list?hl=ko) 을 참조하세요. 

##  2018년 3월 20일

**FEATURE:**

이제 학습 및 예측에 Cloud ML Engine 런타임 버전 1.6을 사용할 수 있습니다. 이 버전은 텐서플로우 1.6 및 [ 런타임 버전
목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ko) 에 나열된 다른 패키지를 지원합니다.

##  2018년 3월 13일

**FEATURE:**

이제 학습 및 예측에 TensorFlow 1.5용 Cloud ML Engine 런타임 버전을 사용할 수 있습니다. 자세한 내용은 [ 런타임
버전 목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ko) 을 참조하세요.

##  2018년 2월 8일

**FEATURE:**

초매개변수 조정에 새로운 기능(자동으로 시험 조기 중단, 이전 초매개변수 조정 작업 재개, 유사한 작업 실행 시 추가 효율성 최적화)이
추가되었습니다. 자세한 내용은 [ 초매개변수 조정 개요 ](https://cloud.google.com/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview?hl=ko) 를 참조하세요.

##  2017년 12월 14일

**FEATURE:**

이제 학습 및 예측에 TensorFlow 1.4용 Cloud ML Engine 런타임 버전을 사용할 수 있습니다. 자세한 내용은 [ 런타임
버전 목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ko) 을 참조하세요.

**FEATURE:**

이제 학습에 TensorFlow 1.4에 대한 Cloud ML Engine 런타임 버전의 일부로 Python 3을 사용할 수 있습니다.
자세한 내용은 [ 런타임 버전 목록 ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=ko) 을 참조하세요.

**FEATURE:**

이제 단일 코어 제공에 대한 온라인 예측이 일반 안정화 버전으로 제공됩니다. [ 온라인 예측
](https://cloud.google.com/ml-engine/docs/tensorflow/online-predict?hl=ko) 및 [
블로그 게시물 ](https://cloud.google.com/blog/big-data/2017/12/bringing-cloud-ml-
engine-to-more-developers-with-online-prediction-features-and-reduced-
prices?hl=ko) 가이드를 참조하세요.

**FEATURE:**

학습 및 예측 모두 가격이 저렴해지고 간소화되었습니다. [ 가격 책정 세부정보 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=ko) , [ 블로그 게시물
](https://cloud.google.com/blog/big-data/2017/12/bringing-cloud-ml-engine-to-
more-developers-with-online-prediction-features-and-reduced-prices?hl=ko) 을
참조하고 [ 가격 FAQ ](https://cloud.google.com/ml-engine/docs/tensorflow/pricing-
faq?hl=ko) 에서 이전 가격과 현재 가격을 비교해 보세요.

**FEATURE:**

이제 P100 GPU가 베타 버전으로 제공됩니다. P100 GPU 사용 시 요금이 부과됩니다. 자세한 내용은 [ GPU 사용
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ko) 및 [ 가격
책정 ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ko) 을
참조하세요.

##  2017년 10월 26일

**FEATURE:**

이제 Cloud ML Engine용 감사 로깅이 베타 버전으로 제공됩니다. 자세한 내용은 [ 감사 로그 보기
](https://cloud.google.com/ml-engine/docs/tensorflow/audit-logs?hl=ko) 를
참조하세요.

##  2017년 9월 25일

**FEATURE:**

Cloud ML Engine의 사전 정의된 IAM 역할이 일반 안정화 버전으로 제공됩니다. 자세한 내용은 [ 액세스 제어
](https://cloud.google.com/ml-engine/docs/tensorflow/access-control?hl=ko) 를
참조하세요.

##  2017년 6월 27일

**FEATURE:**

이제 학습 및 예측에 TensorFlow 1.2용 Cloud ML Engine 런타임 버전을 사용할 수 있습니다. 자세한 내용은 [ 런타임
버전 목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=ko) 을 참조하세요.

**DEPRECATED:**

TensorFlow 0.11 및 0.12가 포함된 이전 런타임 버전은 더 이상 Cloud ML Engine에서 지원되지 않습니다. 자세한
내용은 [ 런타임 버전 목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-
version-list?hl=ko) 과 [ 이전 런타임 버전 타임라인 지원 ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=ko#runtime-version-support) 을
참조하세요.

##  2017년 5월 9일

**FEATURE:**

GPU 지원 머신의 일반 안정화 버전이 발표되었습니다. 자세한 내용은 [ 클라우드에서 학습 모델용 GPU 사용
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=ko) 을
참조하세요.

##  2017년 4월 27일

**FEATURE:**

이제 GPU를 us-central1 리전에서 사용할 수 있습니다. GPU를 지원하는 전체 지역 목록은 [ 클라우드에서 학습 모델용 GPU
사용 ](https://cloud.google.com/ml-engine/docs/tensorflow/using-
gpus?hl=ko#requesting_gpu-enabled_machines) 을 참조하세요.

##  v1(2017년 3월 8일)

**FEATURE:**

AI Platform Training의 일반 안정화 버전이 공개되었습니다. 모델 학습, 모델 배포, 일괄 예측 생성용 Cloud ML
Engine 버전 1이 일반 안정화 버전으로 제공됩니다. [ 초매개변수 조정 ](https://cloud.google.com/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview?hl=ko) 기능도 일반 안정화 버전으로
제공되지만 온라인 예측 및 [ GPU 지원 머신 ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=ko) 은 베타 버전으로 제공됩니다.

**FEATURE:**

현재 온라인 예측이 베타 [ 출시 단계 ](https://cloud.google.com/terms/launch-stages?hl=ko) 에
있습니다. 현재 온라인 예측 사용은 Cloud ML Engine [ 가격 정책 ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=ko) 의 적용을 받으며 일괄 예측과 동일한 가격 책정 공식을 따릅니다. 온라인
예측은 베타 버전으로 제공되며 중요 애플리케이션에서 사용될 수 없습니다.

**CHANGED:**

Cloud ML Engine에서 모델을 학습시키고 예측하는 데 사용하는 환경은 Cloud ML Engine [ 런타임 버전
](https://cloud.google.com/ml-engine/docs/tensorflow/versioning?hl=ko) 으로 정의되어
있습니다. 모델 리소스를 학습시키거나 정의할 때 또는 일괄 예측을 요청할 때 사용할 지원되는 런타임 버전을 지정할 수 있습니다. 현재 런타임
버전 간 주요 차이점은 각 버전에서 지원되는 텐서플로우 버전이지만 시간이 지나면 더 많은 차이가 발생할 수 있습니다. 자세한 내용은 [
런타임 버전 목록 ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-
version-list?hl=ko) 을 참조하세요.

**CHANGED:**

이제 Cloud ML Engine에서 모델 버전으로 호스팅하지 않고 Google Cloud Storage에 저장된 텐서플로우 저장된 모델에
대해 일괄 예측 작업을 실행할 수 있습니다. 작업을 만들 때 모델 또는 버전 ID를 제공하는 대신 저장된 모델의 URI를 사용할 수
있습니다.

**DEPRECATED:**

Google Cloud Machine Learning SDK(이전에 알파 버전으로 출시)는 지원 중단되었으며 2017년 5월 7일부터 더
이상 지원되지 않습니다. SDK에서 노출된 대부분의 기능은 새로운 TensorFlow 패키지인 [ tf.Transform
](https://github.com/tensorflow/transform) 으로 이동했습니다. 입력 데이터를 사전 처리할 때 원하는 모든
기술 또는 도구를 사용할 수 있습니다. 하지만 Google Cloud Dataflow, Google Cloud Dataproc, Google
BigQuery 등 Google Cloud Platform에서 사용할 수 있는 서비스뿐만 아니라 ` tf.Transform ` 도
권장합니다.

##  v1beta1(2016년 9월 29일)

**FEATURE:**

온라인 예측은 알파 버전 기능입니다. AI Platform Training은 전반적으로 베타 단계에 있지만 온라인 예측의 경우는 여전히 성능
향상을 위한 중요한 변화의 과정에 있습니다. 온라인 예측이 알파 버전으로 제공되는 동안에는 [ 요금
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=ko) 이 청구되지
않습니다.

**FEATURE:**

사전 처리 및 나머지 Cloud ML Engine SDK는 알파 버전 기능입니다. SDK의 경우 Cloud ML Engine과 Apache
Beam을 더욱 완벽하게 통합하기 위한 개발이 진행 중입니다.

