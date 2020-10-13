#  Archivierte Versionshinweise

Die neuesten Produktaktualisierungen für Google Cloud finden Sie auf der Seite
mit den [ Google Cloud-Versionshinweisen ](https://cloud.google.com/release-
notes?hl=de) .

Am 10. April 2019 wurde die Cloud Machine Learning Engine zu [ AI Platform
Training ](https://cloud.google.com/ai-platform/training?hl=de) und [ AI
Platform Prediction ](https://cloud.google.com/ai-platform/prediction?hl=de) .
Auf dieser Seite sind die bisherigen Aktualisierungen von Cloud ML Engine
dokumentiert.

Die aktuellen Versionshinweise finden Sie hier:

  * [ Versionshinweise zu AI Platform Training ](https://cloud.google.com/ai-platform/training/docs/release-notes?hl=de)
  * [ Versionshinweise zu AI Platform Prediction ](https://cloud.google.com/ai-platform/prediction/docs/release-notes?hl=de)

##  1\. April 2019

**FEATURE:**

Cloud ML Engine bietet jetzt reduzierte Preise für Training, Onlinevorhersagen
und Batchvorhersagen.

Weitere Informationen zu den [ Preisen für Cloud ML Engine
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=de)

##  28\. März 2019

**FEATURE:**

Cloud ML Engine bietet jetzt Training mit integrierten Algorithmen. Sie können
Ihre Daten für die automatische Vorverarbeitung einreichen und ein Modell
anhand der Algorithmen [ Linear Learner
](https://www.tensorflow.org/tutorials/representation/linear?hl=de) und [ Wide
and Deep ](https://ai.googleblog.com/2016/06/wide-deep-learning-better-
together-with.html) von TensorFlow sowie des Algorithmus [ XGBoost
](https://xgboost.readthedocs.io/en/latest/tutorials/model.html) trainieren,
ohne Code schreiben zu müssen.

[ Weitere Informationen zum Trainieren mit integrierten Algorithmen
](https://cloud.google.com/ai-platform/training/docs/algorithms?hl=de)

##  25\. März 2019

**CHANGED:**

Die Cloud ML Engine-Laufzeitversion 1.13 unterstützt jetzt TensorFlow 1.13.1.
[ In der Laufzeitversionsliste ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=de) finden Sie alle in der
Laufzeitversion 1.13 enthaltenen Pakete.

##  8\. März 2019

**FEATURE:**

Die Unterstützung für das Training mit TPUs in der Cloud ML Engine-
Laufzeitversion 1.9 endete am 8. März 2019. Aktuell unterstützte Versionen
finden Sie [ in der Laufzeitversionsliste ](https://cloud.google.com/ai-
platform/training/docs/tensorflow/runtime-version-list?hl=de#tpu-support) .

##  6\. März 2019

**FEATURE:**

Die Cloud ML Engine-Laufzeitversion 1.13 ist jetzt zum Trainieren und für
Vorhersagen verfügbar. Diese Version unterstützt TensorFlow 1.13 und andere
Pakete, die [ in der Laufzeitversionsliste ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=de) aufgeführt sind.

Das Training mit TPUs wird in der Laufzeitversion 1.13 derzeit nicht
unterstützt.

##  1\. März 2019

**FEATURE:**

[ AI Platform Notebooks ](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=de) steht jetzt als Betaversion
zur Verfügung. Mit AI Platform Notebooks können Sie Instanzen von virtuellen
Maschinen (VM) erstellen und verwalten, die mit [ JupyterLab
](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)
und einer Suite von Deep-Learning-Software vorkonfiguriert sind.

Weitere Informationen finden Sie im [ Überblick über AI Platform Notebooks
](https://cloud.google.com/ai-platform/training/docs/notebooks/overview?hl=de)
und in der [ Anleitung zum Erstellen einer neuen Notebookinstanz
](https://cloud.google.com/ai-platform/training/docs/notebooks/create-
new?hl=de) .

##  13\. Februar 2019

**FEATURE:**

Cloud TPU ist jetzt allgemein zum Trainieren von TensorFlow-Modellen
verfügbar. Tensor Processing Units (TPUs) sind Beschleuniger, die von Google
speziell für ML-Arbeitslasten entwickelt wurden.

So [ verwenden Sie TPUs zum Trainieren von Modellen
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=de) in
Cloud ML Engine. [ Hier erfahren Sie mehr zu den Preisen
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=de) .

##  7\. Februar 2019

**FEATURE:**

Das Training mit benutzerdefinierten Containern steht jetzt als Betaversion
zur Verfügung. Mit dieser Funktion können Sie Ihre Trainingsanwendung in Cloud
ML Engine mit einem benutzerdefinierten Docker-Image ausführen. Sie können den
benutzerdefinierten Container mit einem beliebigen ML-Framework erstellen. Für
den Anfang empfehlen wir das [ Trainieren eines PyTorch-Modells mit
benutzerdefinierten Containern ](https://cloud.google.com/ai-
platform/training/docs/custom-containers-training?hl=de) .

**FEATURE:**

Sie können jetzt Trainingsjobs mit bestimmten Compute Engine-Maschinentypen
konfigurieren. Dies eröffnet Ihnen zusätzliche Flexibilität bei der Zuordnung
von Rechenressourcen zu Trainingsjobs. Dieses Feature ist als Betaversion
verfügbar.

Sie können beim Konfigurieren eines Jobs mit Compute Engine-Maschinentypen
einen benutzerdefinierten Satz von GPUs anhängen.

Weitere Informationen zu [ Compute Engine-Maschinentypen
](https://cloud.google.com/ai-platform/training/docs/machine-
types?hl=de#compute-engine-machine-types) , [ GPU-Anhängen
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=de#compute-
engine-machine-types-with-gpu) und [ deren Preisen
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=de) .

**FEATURE:**

P4-GPUs sind jetzt in der Betaversion zum Trainieren verfügbar. Weitere
Informationen zur [ Verwendung von GPUs ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=de) , der [ regionalen Verfügbarkeit
](https://cloud.google.com/ml-
engine/docs/tensorflow/regions?hl=de#training_with_accelerators) und [ zur
Preisgestaltung ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=de) .

##  01\. Februar 2019

**CHANGED:**

Quad-Core-CPUs sind jetzt in der Betaversion für Onlinevorhersagen verfügbar.
Die Namen der Maschinentypen wurden geändert und die Preise aktualisiert.

  * Legen Sie ` machineType ` auf [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=de) fest, um den für die Bereitstellung zu verwendenden Maschinentyp anzugeben. Verwenden Sie ` mls1-c4-m2 ` für Quad-Core-CPUs. Der Standardwert ist die Single-Core-CPU ` mls1-c1-m2 ` . 
  * Die folgenden in der Alphaversion verwendeten Maschinennamen wurden **eingestellt** : ` mls1-highmem-1 ` und ` mls1-highcpu-4 ` . 
  * Weitere Informationen finden Sie unter [ Onlinevorhersage ](https://cloud.google.com/ai-platform/training/docs/online-predict?hl=de#machine-types) . 
  * Die aktuellen Preise der Maschinentypen [ finden Sie unter "Preise" ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=de) . 

##  25\. Januar 2019

**FEATURE:**

Die Onlinevorhersage ist jetzt in der Region "us-east4" verfügbar. Weitere
Informationen erhalten Sie im [ Leitfaden zur regionalen Verfügbarkeit
](https://cloud.google.com/ai-platform/training/docs/regions?hl=de) .

##  10\. Januar 2019

**FEATURE:**

V100-GPUs sind jetzt allgemein zum Trainieren verfügbar. Weitere Informationen
zur [ Verwendung von GPUs ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=de) und zur [ Preisgestaltung
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=de) .

##  19\. Dezember 2018

**FEATURE:**

Die Cloud ML Engine-Laufzeitversionen 1.11 und 1.12 sind jetzt zum Trainieren
und für Vorhersagen verfügbar. Diese Versionen unterstützen TensorFlow 1.11
bzw. 1.12 und andere Pakete, die in der [ Laufzeitversionsliste
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=de) aufgeführt sind.

Die Cloud ML Engine-Laufzeitversionen 1.11 und 1.12 unterstützen jetzt TPU-
Training, Version 1.10 nicht. Aktuell unterstützte Versionen finden Sie in der
[ Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de#tpu-support) .

**CHANGED:**

Jede Cloud ML Engine-Laufzeitversion enthält jetzt [ joblib
](https://joblib.readthedocs.io/en/latest/) . Version 1.4 ist die früheste
Laufzeitversion, die joblib enthält.

##  26\. Oktober 2018

**CHANGED:**

TPU-Training für die Cloud ML-Laufzeitversion 1.8 wird seit dem 26. Oktober
2018 nicht mehr unterstützt. Aktuell unterstützte Versionen finden Sie [ in
der Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de#tpu-support) .

##  11\. Oktober 2018

**ISSUE:**

Die Cloud ML Engine-Laufzeitversion 1.11 wird aufgrund von [ Fehlern
zurückgesetzt, die durch eine nicht übereinstimmende CuDNN-Version
](https://stackoverflow.com/q/52733440) während des GPU-Trainings verursacht
wurden. Verwenden Sie die Laufzeitversion 1.10, um das Problem zu umgehen.
Weitere Informationen finden Sie [ in der Laufzeitversionsliste
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=de) .

##  5\. Oktober 2018

**FEATURE:**

Die Cloud ML Engine-Laufzeitversion 1.11 ist jetzt zum Trainieren und für
Vorhersagen verfügbar. Diese Version unterstützt TensorFlow 1.11 und andere
Pakete, die [ in der Laufzeitversionsliste ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=de) aufgeführt sind.

##  31\. August 2018

**FEATURE:**

Die Cloud ML Engine-Laufzeitversion 1.10 ist jetzt zum Trainieren und für
Vorhersagen verfügbar. Diese Version unterstützt TensorFlow 1.10 und andere
Pakete, die [ in der Laufzeitversionsliste ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=de) aufgeführt sind.

##  27\. August 2018

**FEATURE:**

V100-GPUs sind jetzt in der Betaversion zum Trainieren verfügbar. Für die
Verwendung von V100-GPUs fallen jetzt Gebühren an. Weitere Informationen zur [
Verwendung von GPUs ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=de) und zur [ Preisgestaltung
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=de) .

**FEATURE:**

P100-GPUs sind jetzt allgemein zum Trainieren verfügbar. Weitere Informationen
zur [ Verwendung von GPUs ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=de) und zur [ Preisgestaltung
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=de) .

**FEATURE:**

Zwei neue Regionen, "us-west1" und "europe-west4", sind jetzt zum Trainieren
verfügbar. Weitere Informationen finden Sie [ auf der Seite "Regionen"
](https://cloud.google.com/ai-platform/training/docs/regions?hl=de) .

##  24\. August 2018

**CHANGED:**

TPU-Training für die Cloud ML-Laufzeitversion 1.7 wird seit dem 24. August
2018 nicht mehr unterstützt. Aktuell unterstützte Versionen finden Sie [ in
der Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de#tpu-support) .

##  9\. August 2018

**CHANGED:**

Wir freuen uns, bedeutende Preissenkungen für Onlinevorhersagen mit AI
Platform Training ankündigen zu können.

In der folgenden Tabelle sind die bisherigen und die neuen Preise aufgeführt:

Region  |  Bisheriger Preis pro Knoten pro Stunde  |  Neuer Preis pro Knoten
pro Stunde  
---|---|---  
USA  |  0,30 $  |  0,056 $  
Europa  |  0,348 $  |  0,061 $  
Asiatisch-pazifischer Raum  |  0,348 $  |  0,071 $  
  
[ Weitere Informationen zu den Preisen ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=de)

##  8\. August 2018

**CHANGED:**

Wir freuen uns, Aktionspreise für Cloud TPU mit AI Platform Training
ankündigen zu können, was erhebliche Preissenkungen bedeutet.

In der folgenden Tabelle sind die bisherigen und die neuen Preise aufgeführt:

Region: USA  |  Bisheriger Preis pro TPU pro Stunde  |  Neuer Preis pro TPU
pro Stunde  
---|---|---  
Skalierungsstufe: ` BASIC_TPU ` _ _(Beta)_ |  9,7674 $  |  6,8474 $  
Benutzerdefinierter Maschinentyp: ` cloud_tpu ` _(Beta)_ |  9,4900 $  |
6,5700 $  
  
Diese Tabelle enthält nur Preise für die Region "USA". Die Cloud TPU-
Verfügbarkeit in der Cloud ML Engine wurde nicht geändert. Weitere
Informationen finden Sie [ in der Preisübersicht
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=de) .

##  6\. August 2018

**FEATURE:**

Die Cloud ML Engine-Laufzeitversion 1.9 ist jetzt zum Trainieren und für
Vorhersagen verfügbar. Diese Version unterstützt TensorFlow 1.9 und andere
Pakete, die [ in der Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de) aufgeführt sind.

##  23\. Juli 2018

**FEATURE:**

Cloud ML Engine unterstützt jetzt **scikit-learn** und **XGBoost** zum
Trainieren. Diese Funktion ist allgemein verfügbar. Weitere Informationen
finden Sie unter [ Training mit scikit-learn und XGBoost unter Cloud ML Engine
](https://cloud.google.com/ml-engine/docs/scikit/getting-started-
training?hl=de) .

**FEATURE:**

Unterstützung für Onlinevorhersagen für **scikit-learn** und **XGBoost** ist
jetzt allgemein verfügbar.

  * Legen Sie ` framework ` auf [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=de) fest, um beim Erstellen einer Modellversion Ihr Framework für maschinelles Lernen anzugeben. Gültige Werte sind ` TENSORFLOW ` , ` SCIKIT_LEARN ` und ` XGBOOST ` . Der Standardwert ist ` TENSORFLOW ` . Wenn Sie ` SCIKIT_LEARN ` oder ` XGBOOST ` angeben, müssen Sie für die Modellversion ` runtimeVersion ` auf 1.4 oder höher festlegen. 
  * Weitere Informationen finden Sie unter [ Lokales Training und Onlinevorhersagen mit scikit-learn und XGBoost ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=de) . 

##  12\. Juli 2018

**FEATURE:**

Sie können für Ihre AI Platform Training-Ressourcen Labels vergeben ( [ Jobs
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=de) , [ Modelle
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models?hl=de) und [
Modellversionen ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=de) ).
Anschließend können Sie diese Labels verwenden, um die Ressourcen in
Kategorien zu organisieren. Labels sind auch [ für Vorgänge
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.operations?hl=de) verfügbar.
Sie werden jedoch von der Ressource abgeleitet, auf die der Vorgang angewendet
wird. Weitere Informationen finden Sie unter [ Labels hinzufügen und verwenden
](https://cloud.google.com/ml-engine/docs/tensorflow/resource-labels?hl=de) .

##  26\. Juni 2018

**CHANGED:**

Die folgenden zusätzlichen Regionen sind jetzt vollständig verfügbar:

  * us-east1 
  * asia-northeast1 

Weitere Informationen finden Sie unter [ Verfügbarkeit der Regionen
](https://cloud.google.com/ai-platform/training/docs/regions?hl=de) .

##  13\. Juni 2018

**CHANGED:**

TPU-Training für die Cloud ML-Laufzeitversion 1.6 wird seit dem 13. Juni 2018
nicht mehr unterstützt. Aktuell unterstützte Versionen finden Sie in der [
Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de#tpu-support) .

##  29\. Mai 2018

**CHANGED:**

Sie können Cloud TPU ( _Beta_ ) jetzt mit TensorFlow 1.8 und Cloud ML Engine-
Laufzeitversion 1.8 verwenden.

_Hintergrundinformationen:_ Cloud TPU ist seit dem 14. Mai in den Cloud ML
Engine-Laufzeitversionen 1.6 und 1.7 verfügbar. Letzte Woche wurde die
Laufzeitversion 1.8 veröffentlicht. Zu diesem Zeitpunkt war Cloud TPU jedoch
noch nicht mit TensorFlow 1.8 verfügbar. Jetzt ist es so weit. [ Hier finden
Sie weitere Informationen zum Trainieren Ihrer Modelle mit TPUs
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=de) in
Cloud ML Engine.

##  16\. Mai 2018

**FEATURE:**

Die Cloud ML Engine-Laufzeitversion 1.8 ist jetzt zum Trainieren und für
Vorhersagen verfügbar. Diese Version unterstützt TensorFlow 1.8 und andere
Pakete, die in der [ Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de) aufgeführt sind.

##  15\. Mai 2018

**FEATURE:**

Sie können jetzt die Mindestzahl der Knoten für das [ Autoscaling
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=de#autoscaling)
bei einer vorhandenen Modellversion aktualisieren und das Attribut beim
Erstellen einer neuen Version festlegen.

##  14\. Mai 2018

**FEATURE:**

In Cloud ML Engine lassen sich ab jetzt mit Cloud TPU _(Beta)_ TensorFlow-
Modelle trainieren. Tensor Processing Units (TPUs) sind von Google speziell
entwickelte ASICs, die dazu dienen, ML-Arbeitslasten zu beschleunigen. Weitere
Informationen zur [ Verwendung von TPUs zum Trainieren von Modellen
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=de) in
Cloud ML Engine.

##  26\. April 2018

**FEATURE:**

Die Cloud ML Engine-Laufzeitversion 1.7 ist jetzt zum Trainieren und für
Vorhersagen verfügbar. Diese Version unterstützt TensorFlow 1.7 und andere
Pakete, die in der [ Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de) aufgeführt sind.

##  16\. April 2018

**FEATURE:**

**Hyperparameter-Algorithmen** : Wenn Sie die Hyperparameter in Ihrem
Trainingsjob optimieren möchten, können Sie dazu nun einen Suchalgorithmus in
[ HyperparameterSpec ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=de#hyperparameterspec)
festlegen. Verfügbare Werte sind:

  * ` GRID_SEARCH ` : Eine einfache Rastersuche im zulässigen Bereich. Diese Option ist besonders nützlich, wenn Sie mehr Tests festlegen möchten als die Zahl der Punkte im zulässigen Bereich. Ist in solchen Fällen keine Rastersuche festgelegt, generiert der Cloud ML Engine-Standardalgorithmus möglicherweise doppelte Vorschläge. Alle Parameter müssen vom Typ ` INTEGER ` , ` CATEGORICAL ` oder ` DISCRETE ` sein, um die Rastersuche nutzen zu können. 
  * ` RANDOM_SEARCH ` : Eine einfache Zufallssuche im zulässigen Bereich. 

Wenn Sie keinen Algorithmus angeben, verwendet der Job den Cloud ML Engine-
Standardalgorithmus, der die Parametersuche steuert, um im Parameterbereich zu
einer optimalen Lösung zu gelangen. Weitere Informationen zur Abstimmung von
Hyperparametern finden Sie in der [ Übersicht zur Hyperparameter-Abstimmung
](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-tuning-
overview?hl=de) .

##  5\. April 2018

**FEATURE:**

Cloud ML Engine unterstützt jetzt **scikit-learn** und **XGBoost** für
Onlinevorhersagen. Dieses Feature befindet sich _in der Betaphase_ .

  * Legen Sie ` framework ` auf [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=de) fest, um beim Erstellen einer Modellversion Ihr Framework für maschinelles Lernen anzugeben. Gültige Werte sind ` TENSORFLOW ` , ` SCIKIT_LEARN ` und ` XGBOOST ` . Der Standardwert ist ` TENSORFLOW ` . Wenn Sie ` SCIKIT_LEARN ` oder ` XGBOOST ` angeben, müssen Sie für die Modellversion ` runtimeVersion ` auf 1.4 oder höher festlegen. 
  * Weitere Informationen finden Sie in der Anleitung [ scikit-learn und XGBoost unter Cloud ML Engine ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=de) . 

**FEATURE:**

Python 3.5 ist für Onlinevorhersagen verfügbar.

  * Legen Sie ` pythonVersion ` auf [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=de) fest, um beim Erstellen einer Modellversion Ihre Version von Python anzugeben. Python 2.7 ist der Standard. 
  * Details zu allen verfügbaren Paketen in Cloud ML Engine finden Sie in der [ Laufzeitversionsliste ](https://cloud.google.com/ml-engine/docs/scikit/runtime-version-list?hl=de) . 

##  20\. März 2018

**FEATURE:**

Die Cloud ML Engine-Laufzeitversion 1.6 ist jetzt zum Trainieren und für
Vorhersagen verfügbar. Diese Version unterstützt TensorFlow 1.6 und andere
Pakete, die in der [ Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de) aufgeführt sind.

##  13\. März 2018

**FEATURE:**

Die Cloud ML Engine-Laufzeitversion für TensorFlow 1.5 ist jetzt zum
Trainieren und für Vorhersagen verfügbar. Weitere Informationen finden Sie in
der [ Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de) .

##  8\. Februar 2018

**FEATURE:**

Es wurden neue Features für die Abstimmung von Hyperparametern hinzugefügt:
automatisches vorzeitiges Beenden von Tests, Wiederaufnahme eines vorherigen
Hyperparameter-Abstimmungsjobs und zusätzliche Effizienzoptimierungen beim
Ausführen ähnlicher Jobs. Weitere Informationen finden Sie unter [ Überblick
zur Hyperparameter-Abstimmung ](https://cloud.google.com/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview?hl=de) .

##  14\. Dezember 2017

**FEATURE:**

Die Cloud ML Engine-Laufzeitversion für TensorFlow 1.4 ist jetzt zum
Trainieren und für Vorhersagen verfügbar. Weitere Informationen finden Sie in
der [ Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de) .

**FEATURE:**

Python 3 ist jetzt zum Trainieren im Rahmen der Cloud ML Engine-
Laufzeitversion für TensorFlow 1.4 verfügbar. Weitere Informationen finden Sie
in der [ Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de) .

**FEATURE:**

Onlinevorhersagen sind jetzt allgemein für die Einzelkernbereitstellung
verfügbar. Weitere Informationen finden Sie in der Anleitung zur [
Onlinevorhersage ](https://cloud.google.com/ml-engine/docs/tensorflow/online-
predict?hl=de) und im [ Blogpost ](https://cloud.google.com/blog/big-
data/2017/12/bringing-cloud-ml-engine-to-more-developers-with-online-
prediction-features-and-reduced-prices?hl=de) .

**FEATURE:**

Die Preise wurden sowohl für Training als auch für Vorhersage reduziert und
vereinfacht. Weitere Informationen finden Sie unter [ Preise
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=de) , im [
Blogpost ](https://cloud.google.com/blog/big-data/2017/12/bringing-cloud-ml-
engine-to-more-developers-with-online-prediction-features-and-reduced-
prices?hl=de) und in den [ FAQ zur Preisgestaltung
](https://cloud.google.com/ml-engine/docs/tensorflow/pricing-faq?hl=de) , die
einen Vergleich der alten und aktuellen Preise enthalten.

**FEATURE:**

P100 GPUs sind jetzt in der Betaversion verfügbar. Für die Verwendung von P100
GPUs fallen jetzt Gebühren an. Weitere Informationen zur [ Verwendung von GPUs
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=de) und zur
[ Preisgestaltung ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=de) .

##  26\. Oktober 2017

**FEATURE:**

Audit-Logging für Cloud ML Engine ist jetzt in der Betaversion verfügbar.
Weitere Informationen finden Sie unter [ Audit-Logs ansehen
](https://cloud.google.com/ml-engine/docs/tensorflow/audit-logs?hl=de) .

##  25\. September 2017

**FEATURE:**

Vordefinierte IAM-Rollen für Cloud ML Engine sind jetzt allgemein verfügbar.
Weitere Informationen finden Sie unter [ Zugriffssteuerung
](https://cloud.google.com/ml-engine/docs/tensorflow/access-control?hl=de) .

##  27\. Juni 2017

**FEATURE:**

Die Cloud ML Engine-Laufzeitversion für TensorFlow 1.2 ist jetzt zum
Trainieren und für Vorhersagen verfügbar. Weitere Informationen finden Sie in
der [ Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de) .

**DEPRECATED:**

Die älteren Laufzeitversionen mit TensorFlow 0.11 und 0.12 werden von der
Cloud ML Engine nicht mehr unterstützt. Weitere Informationen finden Sie in
der [ Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de) und unter [ Unterstützung
für ältere Laufzeitversionen mit Angabe der Zeiträume
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=de#runtime-version-support) .

##  9\. Mai 2017

**FEATURE:**

GPU-fähige Maschinen sind jetzt allgemein verfügbar. Weitere Informationen
finden Sie unter [ GPUs für Trainingsmodelle in der Cloud verwenden
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=de) .

##  27\. April 2017

**FEATURE:**

GPUs sind jetzt in der Region "us-central1" verfügbar. Eine vollständige Liste
der Regionen, die GPUs unterstützen, finden Sie unter [ GPUs für
Trainingsmodelle in der Cloud verwenden ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=de#requesting_gpu-enabled_machines) .

##  v1 (8. März 2017)

**FEATURE:**

Ankündigung der allgemeinen Verfügbarkeit von AI Platform Training. Version 1
von Cloud ML Engine ist allgemein für Trainingsmodelle, für
Bereitstellungsmodelle und für das Generieren von Batchvorhersagen verfügbar.
Das Feature der [ Hyperparameter-Abstimmung ](https://cloud.google.com/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview?hl=de) ist ebenfalls
allgemein verfügbar. Dagegen befinden sich die Onlinevorhersage und [ GPU-
fähige Maschinen ](https://cloud.google.com/ml-engine/docs/tensorflow/using-
gpus?hl=de) noch in der Betaphase.

**FEATURE:**

Onlinevorhersagen befinden sich jetzt in der [ Betastartphase
](https://cloud.google.com/terms/launch-stages?hl=de) . Ihre Verwendung
unterliegt nun dem Cloud ML Engine- [ Preismodell
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=de) und folgt
der gleichen Preisformel wie die Batchvorhersage. Da sich Onlinevorhersagen
noch in der Betaphase befinden, sollten sie nicht in geschäftskritischen
Anwendungen verwendet werden.

**CHANGED:**

Die Umgebungen, die Cloud ML Engine zum Trainieren von Modellen und zum
Durchführen von Vorhersagen verwendet, wurden als Cloud ML Engine- [
Laufzeitversionen ](https://cloud.google.com/ml-
engine/docs/tensorflow/versioning?hl=de) definiert. Sie können zum Trainieren,
für die Definition einer Modellressource oder bei Anfragen für
Batchvorhersagen die Verwendung einer unterstützten Laufzeitversion festlegen.
Laufzeitversionen unterscheiden sich zum jetzigen Zeitpunkt primär in der von
einer Laufzeitversion unterstützten TensorFlow-Version. Es können im Laufe der
Zeit aber noch weitere Unterschiede hinzukommen. Ausführliche Informationen
dazu finden Sie in der [ Laufzeitversionsliste ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=de) .

**CHANGED:**

Sie können nun Batchvorhersagejobs mit TensorFlow-SavedModels ausführen, die
in Google Cloud Storage gespeichert sind und nicht als Modellversion in Cloud
ML Engine gehostet werden. Statt beim Erstellen Ihres Jobs ein Modell oder
eine Versions-ID bereitzustellen, können Sie den URI Ihres SavedModel
verwenden.

**DEPRECATED:**

Das Google Cloud Machine Learning SDK, das bisher als Alphaversion freigegeben
war, wurde eingestellt. Es wird ab dem 7. Mai 2017 nicht mehr unterstützt. Der
größte Teil der Funktionalität des SDK wurde in das neue TensorFlow-Paket [
tf.Transform ](https://github.com/tensorflow/transform) eingebunden. Sie
können für die Vorverarbeitung Ihrer Eingabedaten jede beliebige Technologie
bzw. jedes beliebige Tool verwenden. Wir empfehlen jedoch ` tf.Transform `
sowie Dienste, die auf der Google Cloud Platform verfügbar sind,
einschließlich Google Cloud Dataflow, Google Cloud Dataproc und Google
BigQuery.

##  v1beta1 (29. September 2016)

**FEATURE:**

Onlinevorhersagen sind ein Alphafeature. Obwohl sich AI Platform Training
insgesamt in der Betaphase befindet, werden für Onlinevorhersagen immer noch
erhebliche Änderungen zur Leistungsverbesserung durchgeführt.
Onlinevorhersagen werden [ nicht in Rechnung gestellt
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=de) , solange
sie sich in der Alphaphase befinden.

**FEATURE:**

Die Vorverarbeitung und die übrigen Funktionen des Cloud ML Engine SDK sind
Alphafunktionen. Das SDK wird weiterhin aktiv weiterentwickelt, um die
Einbindung von Cloud ML Engine in Apache Beam zu optimieren.

