#  Versionshinweise

Auf dieser Seite werden Produktionsupdates von Cloud TPU dokumentiert. Hier
finden Sie regelmäßig Hinweise zu neuen oder aktualisierten Features,
Fehlerkorrekturen, bekannten Problemen und verworfenen Funktionen.

Fügen Sie die URL dieser Seite Ihrem [ Feedreader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) hinzu, um die
neuesten Produktaktualisierungen zu erhalten.

##  7\. Mai 2019

**FEATURE:**

Cloud TPU v2 Pod ist als Betarelease verfügbar.

Die Skalierbarkeit von TPU-Ressourcen reicht von einer einzelnen Cloud TPU bis
zu einem Cloud TPU Pod. Deshalb müssen Sie sich nicht zwischen einer einzelnen
Cloud TPU und einem Cloud TPU Pod entscheiden. Sie können Teile von Cloud TPU
Pods in _Slices_ oder Sätzen von Kernen anfordern, sodass Sie ausschließlich
die benötigte Verarbeitungsleistung erwerben.

[ Vorteile von Cloud TPU Pod (Beta) gegenüber einem einzelnen Cloud TPU
v2-Gerät: ](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=de)

  * Erhöhte Trainingsgeschwindigkeit für schnelle Ausführung in F&E 
  * Gesteigerte menschliche Produktivität durch automatisch skalierbares maschinelles Lernen 
  * Möglichkeit zum Trainieren erheblich größerer Modelle 

**FEATURE:**

Cloud TPU v3 Pod ist als Betarelease verfügbar.

Die Skalierbarkeit von TPU-Ressourcen reicht von einer einzelnen Cloud TPU bis
zu einem Cloud TPU Pod. Deshalb müssen Sie sich nicht zwischen einer einzelnen
Cloud TPU und einem Cloud TPU Pod entscheiden. Sie können Teile von Cloud TPU
Pods in _Slices_ oder Sätzen von Kernen anfordern, sodass Sie ausschließlich
die benötigte Verarbeitungsleistung erwerben.

[ Vorteile von Cloud TPU Pod (Beta) gegenüber einem einzelnen Cloud TPU
v3-Gerät: ](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=de)

  * Erhöhte Trainingsgeschwindigkeit für schnelle Ausführung in F&E 
  * Gesteigerte menschliche Produktivität durch automatisch skalierbares maschinelles Lernen 
  * Möglichkeit zum Trainieren erheblich größerer Modelle 

Vorteile von Cloud TPU v3 Pod _(Beta)_ gegenüber Cloud TPU v2 Pod _(Beta)_ :

* Schnellere Verarbeitung und größerer Arbeitsspeicher: 

  * v2 Pod: 11,5 PetaFLOPS und 4 TB On-Chip-Arbeitsspeicher (HBM) 
  * v3 Pod: 100 PetaFLOPS und 32 TB HBM mit Flüssigkeitskühlung 

* Kann noch größere Modelle trainieren 

##  11\. März 2019

**CHANGED:**

Cloud TPU unterstützt jetzt die [ TensorFlow-Version 1.13
](https://www.tensorflow.org/versions/r1.13/api_docs/?hl=de) . Die TensorFlow-
Versionen 1.8 und 1.9 werden nicht mehr unterstützt.

Die aktuell unterstützten TensorFlow-Versionen finden Sie unter [ Unterstützte
Cloud TPU-Versionen ](https://cloud.google.com/tpu/docs/supported-
versions?hl=de) .

##  31\. Januar 2019

**FEATURE:**

Cloud TPU v3 ist jetzt allgemein verfügbar. Cloud TPU v3 bietet doppelt so
viel Arbeitsspeicher wie v2. Damit können Leistungssteigerungen erzielt und
mehr Modellklassen wie tiefere ResNets und größere Bilder mit RetinaNet
unterstützt werden. Vorhandene Modelle, die auf Cloud TPU v2 ausgeführt
werden, funktionieren weiterhin. Weitere Informationen finden Sie im [
Leitfaden zu Cloud TPU-Versionen ](https://cloud.google.com/tpu/docs/deciding-
tpu-version?hl=de) .

##  8\. November 2018

**CHANGED:**

Cloud TPU unterstützt jetzt die [ TensorFlow-Version 1.12
](https://www.tensorflow.org/versions/r1.12/api_docs/?hl=de) . Dieser Release
bietet Verbesserungen für Keras auf Cloud TPUs, Leistungsoptimierungen im
gesamten Softwarepaket sowie verbesserte APIs, Fehlermeldungen und
Zuverlässigkeit.

Die aktuell unterstützten TensorFlow-Versionen finden Sie unter [ Unterstützte
Cloud TPU-Versionen ](https://cloud.google.com/tpu/docs/supported-
versions?hl=de) .

##  7\. November 2018

**FEATURE:**

Cloud TPU v2 Pod ist als Alpharelease verfügbar.

Die Skalierbarkeit von TPU-Ressourcen reicht von einer einzelnen Cloud TPU bis
zu einem Cloud TPU Pod. Deshalb müssen Sie sich nicht zwischen einer einzelnen
Cloud TPU und einem Cloud TPU Pod entscheiden. Sie können Teile von Cloud TPU
Pods in _Slices_ oder Sätzen von Kernen anfordern, sodass Sie ausschließlich
die benötigte Verarbeitungsleistung erwerben.

[ Vorteile von Cloud TPU Pod (Alpha):
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=de)

  * Erhöhte Trainingsgeschwindigkeit für schnelle Ausführung in F&E 
  * Gesteigerte menschliche Produktivität durch automatisch skalierbares maschinelles Lernen 
  * Möglichkeit zum Trainieren erheblich größerer Modelle als auf einem einzelnen ML-Beschleuniger 

##  10\. Oktober 2018

**FEATURE:**

Cloud TPU v3 ist als Betarelease verfügbar. Sie können jetzt in Ihrer
Konfiguration zwischen v2 und v3 auswählen.

  * Cloud TPU v3 bietet doppelt so viel Arbeitsspeicher wie v2. Damit können Leistungssteigerungen erzielt und mehr Modellklassen wie tiefere ResNets und größere Bilder mit RetinaNet unterstützt werden. 
  * Vorhandene Modelle, die auf Cloud TPU v2 ausgeführt werden, funktionieren weiterhin. 
  * [ Weitere Informationen finden Sie in der Anleitung zu Cloud TPU-Versionen. ](https://cloud.google.com/tpu/docs/deciding-tpu-version?hl=de)

##  10\. Oktober 2018

**CHANGED:**

TPUs auf Abruf sind jetzt allgemein verfügbar. Eine TPU auf Abruf ist ein
Cloud TPU-Knoten, den Sie erstellen und zu einem viel niedrigeren Preis als
normale Knoten ausführen können. Cloud TPU kann diese Knoten jedoch
(präemptiv) beenden, wenn für andere Aufgaben Zugriff auf die Ressourcen
benötigt wird.

  * Möglichkeiten zur [ Verwendung einer präemptiven TPU ](https://cloud.google.com/tpu/docs/preemptible?hl=de) . 
  * Überprüfen Sie die [ Preise ](https://cloud.google.com/tpu/docs/pricing?hl=de) für Cloud TPU-Knoten auf Abruf und normale Cloud TPU-Knoten. 

##  27\. September 2018

**CHANGED:**

Cloud TPU unterstützt jetzt die [ TensorFlow-Version 1.11
](https://www.tensorflow.org/versions/r1.11/api_docs/?hl=de) . TensorFlow 1.11
bietet Unterstützung für die folgenden, in der experimentellen Phase
befindlichen Features auf Cloud TPU: Keras, Colab, Ausführung im Eager-Modus,
LARS, RNNs und [ Mesh TensorFlow
](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/mesh_tensorflow/README.md)
. Dieser Release ermöglicht außerdem die Einbindung von [ Cloud Bigtable
](https://cloud.google.com/bigtable/?hl=de) für hohe Leistung und bietet neue
XLA-Compileroptimierungen, weitere Leistungsoptimierungen im gesamten
Softwarepaket sowie verbesserte APIs, Fehlermeldungen und Zuverlässigkeit.

Die aktuell unterstützten TensorFlow-Versionen finden Sie unter [ Unterstützte
Cloud TPU-Versionen ](https://cloud.google.com/tpu/docs/supported-
versions?hl=de) .

##  7\. September 2018

**CHANGED:**

Die Unterstützung für die TensorFlow-Version 1.7 wurde am 7. September 2018
eingestellt. Siehe die aktuell unterstützten Versionen in der [ Richtlinie für
die Cloud TPU-Versionsverwaltung
](https://cloud.google.com/tpu/docs/supported-versions?hl=de) .

##  24\. Juli 2018

**CHANGED:**

Wir freuen uns, Aktionspreise für Cloud TPU ankündigen zu können, die zu
erheblichen Preissenkungen führen. In der folgenden Tabelle sind die
bisherigen und die neuen, ab heute gültigen Preise aufgeführt:

###  USA

|  Bisheriger Preis pro TPU pro Stunde  |  Neuer Preis pro TPU pro Stunde  
---|---|---  
Cloud TPU  |  6,50 $  |  4,50 $  
TPU auf Abruf  |  1,95 $  |  1,35 $  
  
###  Europa

|  Bisheriger Preis pro TPU pro Stunde  |  Neuer Preis pro TPU pro Stunde  
---|---|---  
Cloud TPU  |  7,15 $  |  4,95 $  
TPU auf Abruf  |  2,15 $  |  1,485 $  
  
###  Asiatisch-pazifischer Raum

|  Bisheriger Preis pro TPU pro Stunde  |  Neuer Preis pro TPU pro Stunde  
---|---|---  
Cloud TPU  |  7,54 $  |  5,22 $  
TPU auf Abruf  |  2,26 $  |  1,566 $  
  
[ Weitere Informationen zu den Preisen
](https://cloud.google.com/tpu/docs/pricing?hl=de)

##  12\. Juli 2018

**FEATURE:**

Cloud TPU ist jetzt in Google Kubernetes Engine als Betafeature verfügbar.
Wenn Sie Ihre ML-Arbeitslast in einem Kubernetes-Cluster auf der GCP
ausführen, übernimmt GKE das Verwalten und Skalieren der Cloud TPU-Ressourcen
für Sie.

  * Folgen Sie der [ Anleitung ](https://cloud.google.com/tpu/docs/tutorials/kubernetes-engine-resnet?hl=de) , um das TensorFlow ResNet-50-Modell auf Cloud TPU und GKE zu trainieren. 
  * Unter [ Cloud TPU in GKE einrichten ](https://cloud.google.com/tpu/docs/kubernetes-engine-setup?hl=de) erhalten Sie eine Kurzanleitung zum Ausführen von Cloud TPU mit GKE. 

##  2\. Juli 2018

**CHANGED:**

Cloud TPU unterstützt jetzt die [ TensorFlow-Version 1.9
](https://www.tensorflow.org/versions/r1.9/api_docs/?hl=de) . TensorFlow 1.9
bietet eine höhere Cloud TPU-Leistung sowie verbesserte APIs, Fehlermeldungen
und Zuverlässigkeit.

##  27\. Juni 2018

**FEATURE:**

Cloud TPU ist jetzt allgemein verfügbar. Googles revolutionäre TPUs wurden
entwickelt, um ML-Arbeitslasten mit TensorFlow zu beschleunigen. Jede Cloud
TPU bietet bis zu 180 TeraFLOPS Leistung und damit ausreichend Rechenleistung,
um selbst sehr anspruchsvolle Modelle für maschinelles Lernen zu trainieren
und auszuführen.

  * Führen Sie die Schritte der [ Schnellstartanleitung ](https://cloud.google.com/tpu/docs/quickstart?hl=de) aus, um Ihre Cloud TPU einzurichten. 
  * Wählen Sie eine [ Anleitung ](https://cloud.google.com/tpu/docs/tutorials?hl=de) aus, um ein bestimmtes Modell auf Ihrer Cloud TPU auszuführen. 

##  18\. Juni 2018

**FEATURE:**

Präemptive TPUs sind jetzt in der _Betaversion_ verfügbar. Eine TPU auf Abruf
ist ein Cloud TPU-Knoten, den Sie erstellen und zu einem viel niedrigeren
Preis als normale Knoten ausführen können. Cloud TPU kann diese Knoten jedoch
(präemptiv) beenden, wenn für andere Aufgaben Zugriff auf die Ressourcen
benötigt wird.

  * Möglichkeiten zur [ Verwendung einer präemptiven TPU ](https://cloud.google.com/tpu/docs/preemptible?hl=de) . 
  * Überprüfen Sie die [ Preise ](https://cloud.google.com/tpu/docs/pricing?hl=de) für Cloud TPU-Knoten auf Abruf und normale Cloud TPU-Knoten. 

**CHANGED:**

Cloud TPU ist jetzt in Europa, im asiatisch-pazifischen Raum sowie in den
Vereinigten Staaten verfügbar. Sehen Sie sich die [ Preisdetails
](https://cloud.google.com/tpu/docs/pricing?hl=de) pro Region an. Die
folgenden Zonen sind verfügbar:

  * **USA**
    * ` us-central1-b `
    * ` us-central1-c `
    * ` us-central1-f ` (nur [ TFRC-Programm ](https://www.tensorflow.org/tfrc/?hl=de) ) 
  * **EU**
    * ` europe-west4-a `
  * **Asien/Pazifik**
    * ` asia-east1-c `

##  12\. Juni 2018

**CHANGED:**

Die Unterstützung für TensorFlow 1.6 endete am 12. Juni 2018. Siehe die
aktuell unterstützten Versionen in der [ Richtlinie für die Cloud TPU-
Versionsverwaltung ](https://cloud.google.com/tpu/docs/supported-
versions?hl=de) .

##  20\. April 2018

**CHANGED:**

Cloud TPU unterstützt jetzt [ TensorFlow 1.8
](https://www.tensorflow.org/versions/r1.8/api_docs/?hl=de) . TensorFlow 1.8
bietet eine höhere Cloud TPU-Leistung sowie verbesserte APIs, Fehlermeldungen
und mehr Zuverlässigkeit.

Die Unterstützung für TensorFlow 1.7 endet am 20. Juni 2018. Weitere
Informationen finden Sie in der [ Richtlinie für die Cloud TPU-Versionierung
](https://cloud.google.com/tpu/docs/supported-versions?hl=de) .

##  2\. April 2018

**CHANGED:**

Cloud TPU unterstützt nun [ TensorFlow 1.7
](https://www.tensorflow.org/versions/r1.7/api_docs/?hl=de) . Die
Unterstützung für TensorFlow 1.6 endet am 2. Juni 2018. Weitere Informationen
finden Sie in der [ Richtlinie für die Cloud TPU-Versionierung
](https://cloud.google.com/tpu/docs/supported-versions?hl=de) .

##  12\. Februar 2018

**FEATURE:**

Cloud TPU ist in der Betaversion verfügbar. Googles revolutionäre TPUs wurden
entwickelt, um die ML-Arbeitslasten mit TensorFlow zu beschleunigen. Jede
Cloud TPU bietet bis zu 180 TeraFLOPS Leistung und damit ausreichend
Rechenleistung, um selbst sehr anspruchsvolle Modelle für maschinelles Lernen
zu trainieren und auszuführen.

  * Erfahren Sie mehr darüber, wie Sie [ TPU-Kontingente beantragen ](https://cloud.google.com/tpu/docs/quota?hl=de) . 
  * Führen Sie die Schritte der [ Schnellstartanleitung ](https://cloud.google.com/tpu/docs/quickstart?hl=de) aus, um Ihre Cloud TPU einzurichten. 
  * Wählen Sie eine [ Anleitung ](https://cloud.google.com/tpu/docs/tutorials?hl=de) aus, um ein bestimmtes Modell auf Ihrer Cloud TPU auszuführen. 

