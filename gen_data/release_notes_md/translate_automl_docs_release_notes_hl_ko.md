#  출시 노트

이 페이지에서는 AutoML Translation의 프로덕션 업데이트에 대해 설명합니다. AutoML Translation 개발자는 이
목록을 주기적으로 참고하여 새로운 소식을 확인하는 것이 좋습니다. 주요 변경사항은 [ google-translate-api
](https://groups.google.com/forum/?hl=ko#!forum/google-translate-api) 메일링 리스트를
통해서도 공지됩니다.

**베타**

이 기능은 출시 전 상태로 변경되거나 지원이 제한될 수 있습니다. 자세한 내용은 [ 제품 출시 단계
](https://cloud.google.com/products?hl=ko#product-launch-stages) 를 참조하세요.

최신 제품 업데이트를 제공받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하세요.

##  2018년 12월 11일

**CHANGED:**

커스텀 모델을 학습시키는 데 필요한 최소 문장 쌍 수가 변경되었습니다. 학습, 검증, 테스트 세트를 명시적으로 지정하지 않으면 최소 문장 쌍
수는 1,000개입니다. 학습, 검증, 테스트 세트를 명시적으로 지정하지 않으면 검증 및 테스트에 사용되는 최소 쌍 수는 각각
100개입니다.

##  2018년 11월 1일

**CHANGED:**

AutoML Translation 서비스 계정은 AutoML Translation UI를 사용할 때 프로젝트 리소스에 액세스하기 위한 추가
권한이 필요합니다. ` serviceusage.serviceUsageAdmin ` 역할을 추가해야 합니다. [ 시작하기 전에
](https://cloud.google.com/translate/automl/docs/before-you-begin?hl=ko) 의
8단계를 참조하세요.

##  2018년 9월 18일

**많은 새로운 언어 지원**

**CHANGED:**

AutoML Translation은 영어와 조합을 이루는 출발어 또는 도착어로 많은 새로운 언어를 지원하여 이제 총 지원되는 언어 조합 수가
100개에 이릅니다. 전체 목록은 [ 커스텀 모델에 대한 언어 지원
](https://cloud.google.com/translate/automl/docs/languages?hl=ko) 을 참조하세요.

##  2018년 8월 24일

**CHANGED:**

AutoML Translation UI의 URL이 [ https://cloud.google.com/automl/ui/translation
](https://cloud.google.com/automl/ui/translation?hl=ko) 으로 변경되었습니다. 이전 URL
https://beta-dot-custom-vision.appspot.com/translation/은 활성 상태로 유지됩니다.

##  2018년 8월 2일

**스와힐리어 지원**

**CHANGED:**

AutoML Translation은 스와힐리어(`sw`)를 영어(`en`) 출발어의 도착어로 지원합니다.

언어 조합  |  언어 코드  
---|---  
스와힐리어 <\- 영어  |  ` sw ` <\- ` en `  
  
##  2018년 7월 24일

**AutoML Translation 베타 출시**

**FEATURE:**

EAP 중에 생성된 모델은 베타 버전에서 계속 유효합니다. 모델을 다시 만들거나 재학습할 필요가 없습니다. 그러나 리소스 ID(데이터세트
ID, 모델 ID, 작업 ID)의 형식이 변경됩니다. 하드코딩된 리소스를 사용하려면 해당 리소스에 대한 새 ID를 2018년 8월 31일까지
발급받아야 합니다( ` get ` 또는 ` list ` 메소드 사용).

프로젝트에 AutoML API를 사용하도록 설정하면 Cloud Vision API, Cloud Translation API, Cloud
Natural Language API도 자동으로 사용하도록 설정됩니다. 이 세 API 중 하나를 사용 중지하면 AutoML API도 사용
중지됩니다.

##  2018년 5월 24일

**CHANGED:**

새로워진 UI 디자인과 새 API를 선보이는 AutoML Translation EAP의 새 버전이 출시되었습니다. AutoML
Translation EAP UI의 이전 버전은 지원이 중단되었으며, 새 AutoML API는 이전 API와 호환되지 않습니다.

이전에 생성된 데이터세트의 콘텐츠를 다시 가져와야 합니다. ` gs://  project-id  -vcm/  dataset-name
/uploads/  document-name  .txt ` 에서 원래 콘텐츠를 찾을 수 있습니다.

이전 버전의 AutoML Translation UI를 사용하여 기본 Google 인공신경망 기계 번역 모델 이외의 다른 커스텀 번역 모델을
기반으로 커스텀 모델을 생성한 경우 새로운 UI를 사용하여 모델을 다시 생성하거나 재학습해야 합니다.

AutoML Translation UI로 생성한 모델은 아직 AutoML API를 통해 사용할 수 없습니다.

##  2018년 3월 30일

**CHANGED:**

  * 이제 AutoML Translation EAP 웹 애플리케이션을 통해 직접 작성한 다른 커스텀 번역 모델을 기반으로 커스텀 모델을 구축할 수 있습니다. 
  * 번역 요청을 보내고 응답을 받는 방법을 보여주는 샘플 자바 애플리케이션이 제공됩니다. 

##  2018년 2월 27일

**CHANGED:**

다음과 같은 언어 번역 조합이 추가되었습니다.

언어 조합  |  언어 코드  
---|---  
네덜란드어 -> 영어  |  ` nl ` -> ` en `  
히브리어 -> 영어  |  ` iw ` -> ` en `  
  
##  2018년 2월 5일

**CHANGED:**

다음과 같은 언어 번역 조합이 추가되었습니다.

언어 조합  |  언어 코드  
---|---  
아랍어 -> 영어  |  ` ar ` -> ` en `  
중국어(간체) -> 영어  |  ` zh-CN ` -> ` en `  
프랑스어 <-> 영어  |  ` fr ` <-> ` en `  
독일어 -> 영어  |  ` de ` -> ` en `  
이탈리아어 <-> 영어  |  ` it ` <-> ` en `  
일본어 <\- 영어  |  ` ja ` <\- ` en `  
한국어 <\- 영어  |  ` ko ` <\- ` en `  
포르투갈어(포르투갈, 브라질) -> 영어  |  ` pt ` -> ` en `  
러시아어 <-> 영어  |  ` ru ` <-> ` en `  
터키어 <\- 영어  |  ` tr ` <\- ` en `  
  
##  2018년 1월 17일

**FEATURE:**

AutoML Translation EAP가 출시되었습니다.

