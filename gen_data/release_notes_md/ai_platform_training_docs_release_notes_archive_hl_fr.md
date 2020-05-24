#  Notes de version archivées

Vous pouvez consulter les dernières mises à jour de produits pour l'ensemble
de Google Cloud sur la page [ Notes de version de Google Cloud
](https://cloud.google.com/release-notes?hl=fr) .

Le 10 avril 2019, Cloud Machine Learning Engine a cédé la place à [ AI
Platform Training ](https://cloud.google.com/ai-platform/training?hl=fr) et [
AI Platform Prediction ](https://cloud.google.com/ai-
platform/prediction?hl=fr) . Cette page détaille l'historique des mises à jour
de Cloud ML Engine.

Vous pouvez consulter les notes de version actuelles :

  * [ Notes de version d'AI Platform Training ](https://cloud.google.com/ai-platform/training/docs/release-notes?hl=fr)
  * [ Notes de version d'AI Platform Prediction ](https://cloud.google.com/ai-platform/prediction/docs/release-notes?hl=fr)

##  1er avril 2019

**FEATURE:**

Cloud ML Engine propose désormais des tarifs réduits pour l'entraînement, la
prédiction en ligne et la prédiction par lot.

Apprenez-en plus sur les [ tarifs de Cloud ML Engine
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=fr) .

##  28 mars 2019

**FEATURE:**

Cloud ML Engine propose désormais des entraînements à l'aide d'algorithmes
intégrés. Vous pouvez envoyer vos données pour qu'elles soient automatiquement
prétraitées, et entraîner un modèle avec l' [ algorithme de l'apprenant
linéaire ](https://www.tensorflow.org/tutorials/representation/linear?hl=fr)
et l' [ algorithme large et profond ](https://ai.googleblog.com/2016/06/wide-
deep-learning-better-together-with.html) de TensorFlow, et avec les
algorithmes [ XGBoost
](https://xgboost.readthedocs.io/en/latest/tutorials/model.html) sans écrire
de code.

Apprenez-en plus sur l' [ entraînement à l'aide d'algorithmes intégrés
](https://cloud.google.com/ai-platform/training/docs/algorithms?hl=fr) .

##  25 mars 2019

**CHANGED:**

La version d'exécution 1.13 de Cloud ML Engine est désormais compatible avec
TensorFlow 1.13.1. Consultez la [ liste des versions d'exécution
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=fr) pour connaître l'ensemble des packages inclus dans la version
1.13.

##  8 mars 2019

**FEATURE:**

L'entraînement TPU dans la version d'exécution 1.9 de Cloud ML Engine n'est
plus disponible depuis le 8 mars 2019. Consultez les versions actuellement
compatibles dans la [ liste des versions d'exécution
](https://cloud.google.com/ai-platform/training/docs/tensorflow/runtime-
version-list?hl=fr#tpu-support) .

##  6 mars 2019

**FEATURE:**

La version d'exécution 1.13 de Cloud ML Engine est maintenant compatible avec
l'entraînement et la prédiction. Cette version est compatible avec TensorFlow
1.13 et inclut d'autres packages répertoriés dans la [ liste des versions
d'exécution ](https://cloud.google.com/ai-platform/training/docs/runtime-
version-list?hl=fr) .

L'entraînement TPU dans la version d'exécution 1.13 n'est pas disponible pour
le moment.

##  1er mars 2019

**FEATURE:**

[ AI Platform Notebooks ](https://cloud.google.com/ai-
platform/training/docs/notebooks/overview?hl=fr) est désormais disponible en
version bêta. AI Platform Notebooks permet de créer et gérer des instances de
machine virtuelle (VM) pré-empaquetées avec [ JupyterLab
](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)
et une suite de logiciels de deep learning.

Pour en savoir plus, consultez la [ présentation d'AI Platform Notebooks
](https://cloud.google.com/ai-platform/training/docs/notebooks/overview?hl=fr)
et le [ guide de création d'une instance de notebook
](https://cloud.google.com/ai-platform/training/docs/notebooks/create-
new?hl=fr) .

##  13 février 2019

**FEATURE:**

Cloud TPU est désormais accessible à tous pour l'entraînement des modèles
TensorFlow. Les TPU (Tensor Processing Unit) sont des accélérateurs développés
spécifiquement par Google pour les charges de travail de machine learning.

Découvrez comment [ utiliser les TPU pour entraîner vos modèles
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=fr) sur
Cloud ML Engine et prenez connaissance des [ tarifs
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=fr) .

##  7 février 2019

**FEATURE:**

L'entraînement avec des conteneurs personnalisés est maintenant disponible en
version bêta. Cette fonctionnalité vous permet d’exécuter votre application
d’entraînement sur Cloud ML Engine à l’aide d’une image Docker personnalisée.
Vous pouvez créer votre conteneur personnalisé avec les frameworks ML de votre
choix. Pour vos premiers pas, commencez par [ entraîner un modèle PyTorch à
l'aide de conteneurs personnalisés ](https://cloud.google.com/ai-
platform/training/docs/custom-containers-training?hl=fr) .

**FEATURE:**

Vous pouvez maintenant configurer des tâches d'entraînement avec certains
types de machines Compute Engine. Vous disposerez ainsi d'une plus grande
flexibilité pour affecter des ressources informatiques à vos tâches
d'entraînement. Cette fonctionnalité est disponible en version bêta.

Lorsque vous configurez vos tâches avec des types de machine Compute Engine,
vous pouvez y rattacher un ensemble personnalisé de GPU.

Renseignez-vous sur [ les types de machines Compute Engine
](https://cloud.google.com/ai-platform/training/docs/machine-
types?hl=fr#compute-engine-machine-types) , [ les rattachements de GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=fr#compute-
engine-machine-types-with-gpu) et [ les tarifs ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=fr) .

**FEATURE:**

Les GPU P4 sont maintenant disponibles en version bêta pour l'entraînement.
Pour en savoir plus, consultez les guides d' [ utilisation des GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=fr) , [
leur disponibilité régionale ](https://cloud.google.com/ml-
engine/docs/tensorflow/regions?hl=fr#training_with_accelerators) et [ leurs
tarifs ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=fr) .

##  1er février 2019

**CHANGED:**

Les processeurs quatre cœurs sont désormais disponibles en version bêta pour
la prédiction en ligne. Les noms des types de machines ont été modifiés, et
les tarifs ont évolué.

  * Définissez ` machineType ` sur [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=fr) afin de spécifier le type de machine à utiliser pour la diffusion. Utilisez ` mls1-c4-m2 ` pour les processeurs à quatre cœurs. La valeur par défaut est le processeur à cœur unique ` mls1-c1-m2 ` . 
  * Les noms de machines suivants utilisés dans la version alpha sont **obsolètes** : ` mls1-highmem-1 ` et ` mls1-highcpu-4 ` . 
  * Pour plus d'informations, reportez-vous au guide sur la [ prédiction en ligne ](https://cloud.google.com/ai-platform/training/docs/online-predict?hl=fr#machine-types) . 
  * Consultez les nouveaux [ tarifs ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=fr) pour les différents types de machines de diffusion. 

##  25 janvier 2019

**FEATURE:**

La prédiction en ligne est maintenant disponible dans la région us-east4.
Consultez le guide de la [ disponibilité des régions
](https://cloud.google.com/ai-platform/training/docs/regions?hl=fr) .

##  10 janvier 2019

**FEATURE:**

Les GPU V100 sont désormais accessibles à tous pour l'entraînement. Pour en
savoir plus, consultez les sections [ Utiliser les GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=fr) et [
Tarifs ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=fr) .

##  19 décembre 2018

**FEATURE:**

Les versions d'exécution 1.11 et 1.12 de Cloud ML Engine sont maintenant
compatibles avec l'entraînement et la prédiction. Ces versions sont
compatibles avec TensorFlow 1.11 et 1.12 respectivement, ainsi qu'avec les
autres packages énumérés dans la [ liste des versions d'exécution
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=fr) .

L'entraînement TPU est maintenant disponible dans les versions d'exécution
1.11 et 1.12 de Cloud ML Engine. La version 1.10 n'est pas compatible.
Consultez les versions actuellement compatibles dans la [ liste des versions
d'exécution ](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-
version-list?hl=fr#tpu-support) .

**CHANGED:**

Chaque version d'exécution de Cloud ML Engine inclut désormais [ joblib
](https://joblib.readthedocs.io/en/latest/) . La version d'exécution la plus
ancienne incluant joblib est la version 1.4.

##  26 octobre 2018

**CHANGED:**

L'entraînement TPU pour la version d'exécution 1.8 de Cloud ML n'est plus
disponible depuis le 26 octobre 2018. Consultez les versions actuellement
compatibles dans la [ liste des versions d'exécution
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=fr#tpu-support) .

##  11 octobre 2018

**ISSUE:**

Le déploiement de la version d'exécution 1.11 de Cloud ML Engine est annulé en
raison d' [ erreurs dues à une non-correspondance de version CuDNN
](https://stackoverflow.com/q/52733440) au cours de l'entraînement sur GPU. La
solution actuelle consiste à utiliser la version d'exécution 1.10. Reportez-
vous à la [ liste des versions d'exécution ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list?hl=fr) pour en savoir plus.

##  5 octobre 2018

**FEATURE:**

La version d'exécution 1.6 de Cloud ML Engine est maintenant disponible pour
l'entraînement et la prédiction. Cette version est compatible avec TensorFlow
1.10 et d'autres packages répertoriés dans la [ liste des versions d'exécution
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=fr) .

##  31 août 2018

**FEATURE:**

La version d'exécution 1.10 de Cloud ML Engine est désormais disponible pour
l'apprentissage et la prédiction. Cette version est compatible avec TensorFlow
1.10 et d'autres packages répertoriés dans la [ liste des versions d'exécution
](https://cloud.google.com/ai-platform/training/docs/runtime-version-
list?hl=fr) .

##  27 août 2018

**FEATURE:**

Les GPU V100 sont maintenant disponibles en version bêta pour l'entraînement.
Leur utilisation entraîne désormais des frais. Pour en savoir plus, consultez
les sections [ Utiliser les GPU ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=fr) et [ Tarifs
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=fr) .

**FEATURE:**

Les GPU P100 sont désormais accessibles à tous pour l'entraînement. Pour en
savoir plus, consultez les sections [ Utiliser les GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=fr) et [
Tarifs ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=fr) .

**FEATURE:**

L'entraînement est désormais disponible dans deux nouvelles régions : us-west1
et europe-west4. Consultez la page dédiée aux [ régions
](https://cloud.google.com/ai-platform/training/docs/regions?hl=fr) pour en
savoir plus.

##  24 août 2018

**CHANGED:**

L'apprentissage TPU pour la version d'exécution 1.7 de Cloud ML n'est plus
disponible depuis le 24 août 2018. Consultez les versions actuellement
compatibles dans la [ liste des versions d'exécution
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=fr#tpu-support) .

##  9 août 2018

**CHANGED:**

Nous sommes ravis d'annoncer d'importantes réductions tarifaires pour la
prédiction en ligne avec AI Platform Training.

Le tableau suivant indique les anciens tarifs et les nouveaux :

Région  |  Ancien prix par nœud et par heure  |  Nouveau prix par nœud et par
heure  
---|---|---  
États-Unis  |  0,30 USD  |  0,056 USD  
Europe  |  0,348 USD  |  0,061 USD  
Asie-Pacifique  |  0,348 USD  |  0,071 USD  
  
Pour en savoir plus, consultez notre [ grille tarifaire
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=fr) .

##  8 août 2018

**CHANGED:**

Nous sommes ravis d'annoncer la mise en place de tarifs promotionnels pour
Cloud TPU avec AI Platform Training. Les utilisateurs pourront ainsi
bénéficier de réductions importantes.

Le tableau suivant indique les anciens tarifs et les nouveaux :

Région : États-Unis  |  Ancien prix par TPU et par heure  |  Nouveau prix par
TPU et par heure  
---|---|---  
Niveau d'évolutivité : ` BASIC_TPU ` _(bêta)_ |  9,7674 USD  |  6,8474 USD  
Type de machine personnalisé : ` cloud_tpu ` _(bêta)_ |  9,4900 USD  |  6,5700
USD  
  
Veuillez noter que ce tableau n'indique les prix que pour la région des États-
Unis. La disponibilité de Cloud TPU sur Cloud ML Engine reste inchangée. Pour
en savoir plus, consultez notre [ grille tarifaire
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=fr) .

##  6 août 2018

**FEATURE:**

La version d'exécution 1.9 de Cloud ML Engine est désormais disponible pour
l'apprentissage et la prédiction. Cette version est compatible avec TensorFlow
1.9 et d'autres packages répertoriés dans la [ liste des versions d'exécution
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=fr) .

##  23 juillet 2018

**FEATURE:**

Cloud ML Engine est désormais compatible avec **scikit-learn** et **XGBoost**
pour l'apprentissage. Cette fonctionnalité est accessible à tous. Consultez le
guide [ Entraînement avec scikit-learn et XGBoost sur Cloud ML Engine
](https://cloud.google.com/ml-engine/docs/scikit/getting-started-
training?hl=fr) .

**FEATURE:**

La prédiction en ligne via **scikit-learn** et **XGBoost** est désormais
accessible à tous.

  * Définissez ` framework ` sur [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=fr) pour spécifier votre framework de machine learning lorsque vous créez une version de modèle. Les valeurs valides sont ` TENSORFLOW ` , ` SCIKIT_LEARN ` et ` XGBOOST ` . La valeur par défaut est ` TENSORFLOW ` . Si vous spécifiez ` SCIKIT_LEARN ` ou ` XGBOOST ` , vous devez également définir la valeur ` runtimeVersion ` sur "1.4" ou une version ultérieure dans la version du modèle. 
  * Consultez le guide sur [ l'apprentissage en local et les prédictions en ligne avec scikit-learn et XGBoost ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=fr) . 

##  12 juillet 2018

**FEATURE:**

Vous pouvez ajouter des étiquettes à vos ressources AI Platform Training ( [
tâches ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=fr) , [ modèles
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models?hl=fr) et [ versions
de modèles ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=fr) ),
puis les utiliser pour organiser les ressources en catégories. Les [
opérations ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.operations?hl=fr) peuvent
aussi bénéficier d'étiquettes, mais celles-ci sont alors dérivées de la
ressource à laquelle l'opération s'applique. Consultez [ cette page
](https://cloud.google.com/ml-engine/docs/tensorflow/resource-labels?hl=fr)
pour savoir comment ajouter et utiliser des étiquettes.

##  26 juin 2018

**CHANGED:**

Les régions supplémentaires suivantes sont désormais entièrement disponibles :

  * us-east1 
  * asia-northeast1 

Obtenez plus d'informations sur la [ disponibilité des régions
](https://cloud.google.com/ai-platform/training/docs/regions?hl=fr) .

##  13 juin 2018

**CHANGED:**

L'apprentissage TPU pour la version d'exécution 1.6 de Cloud ML n'est plus
disponible depuis le 13 juin 2018. Consultez les versions actuellement
compatibles dans la [ liste des versions d'exécution
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=fr#tpu-support) .

##  29 mai 2018

**CHANGED:**

Vous pouvez désormais utiliser Cloud TPU ( _bêta_ ) avec TensorFlow 1.8 et la
version d'exécution 1.8 de Cloud ML Engine.

_Informations générales_ : Cloud TPU est disponible avec Cloud ML Engine
depuis le 14 mai dans les versions d'exécution 1.6 et 1.7. La version
d'exécution 1.8 est sortie la semaine dernière, alors que Cloud TPU n'était
pas encore compatible avec TensorFlow 1.8. Ces deux outils sont désormais
compatibles. Découvrez comment [ utiliser des TPU pour entraîner vos modèles
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=fr) sur
Cloud ML Engine.

##  16 mai 2018

**FEATURE:**

La version d'exécution 1.8 de Cloud ML Engine est désormais disponible pour
l'apprentissage et la prédiction. Cette version est compatible avec TensorFlow
1.8 et d'autres packages répertoriés dans la [ liste des versions d'exécution
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=fr) .

##  15 mai 2018

**FEATURE:**

Vous pouvez désormais mettre à jour le nombre minimal de nœuds pour l' [
autoscaling ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.models.versions?hl=fr#autoscaling)
sur une version de modèle existante, ou spécifier cet attribut lors de la
création d'une version.

##  14 mai 2018

**FEATURE:**

Cloud ML Engine propose désormais Cloud TPU _(bêta)_ pour l'apprentissage des
modèles TensorFlow. Les TPU (Tensor Processing Unit) sont des ASIC
spécifiquement développés par Google pour accélérer les charges de travail de
machine learning. Découvrez comment [ entraîner vos modèles à l'aide des TPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-tpus?hl=fr) sur
Cloud ML Engine.

##  26 avril 2018

**FEATURE:**

La version d'exécution 1.7 de Cloud ML Engine est maintenant disponible pour
l'apprentissage et la prédiction. Cette version est compatible avec TensorFlow
1.7 et d'autres packages répertoriés dans la [ liste des versions d'exécution
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=fr) .

##  16 avril 2018

**FEATURE:**

**Algorithmes d'hyperparamètres** : lorsque vous ajustez les hyperparamètres
dans votre tâche d'entraînement, vous pouvez désormais spécifier un algorithme
de recherche dans [ HyperparameterSpec ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs?hl=fr#hyperparameterspec)
. Les valeurs disponibles sont les suivantes :

  * ` GRID_SEARCH ` : une recherche par quadrillage simple dans l'espace réalisable. Cette option est particulièrement utile si vous souhaitez indiquer un nombre d'essais supérieur au nombre de points définis dans l'espace réalisable. Dans ce cas, si vous ne spécifiez pas de recherche par quadrillage, l'algorithme par défaut de Cloud ML Engine peut générer des suggestions en double. Si vous utilisez la recherche par quadrillage, tous les paramètres doivent être de type ` INTEGER ` , ` CATEGORICAL ` ou ` DISCRETE ` . 
  * ` RANDOM_SEARCH ` : une recherche aléatoire simple dans l'espace réalisable. 

Si vous ne spécifiez pas d'algorithme, votre tâche utilise l'algorithme par
défaut de Cloud ML Engine, qui va guider la recherche de paramètres pour
obtenir la solution optimale avec une recherche plus efficace dans l'espace
des paramètres. Pour en savoir plus sur ces réglages, consultez la page [
Présentation des réglages d'hyperparamètres ](https://cloud.google.com/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview?hl=fr) .

##  5 avril 2018

**FEATURE:**

Cloud ML Engine est désormais compatible avec **scikit-learn** et **XGBoost**
pour la prédiction en ligne. Cette fonctionnalité est en _version bêta_ .

  * Définissez ` framework ` sur [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=fr) pour spécifier votre framework de machine learning lorsque vous créez une version de modèle. Les valeurs valides sont ` TENSORFLOW ` , ` SCIKIT_LEARN ` et ` XGBOOST ` . La valeur par défaut est ` TENSORFLOW ` . Si vous spécifiez ` SCIKIT_LEARN ` ou ` XGBOOST ` , vous devez également définir la valeur ` runtimeVersion ` sur "1.4" ou une version ultérieure dans la version du modèle. 
  * Consultez le guide consacré à [ scikit-learn et XGBoost sur Cloud ML Engine ](https://cloud.google.com/ml-engine/docs/scikit/quickstart?hl=fr) . 

**FEATURE:**

Python 3.5 est disponible pour la prédiction en ligne.

  * Définissez ` pythonVersion ` sur [ ` projects.models.versions.create ` ](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions?hl=fr) pour spécifier votre version de Python lorsque vous créez une version de modèle. La valeur par défaut est Python 2.7. 
  * Pour en savoir plus sur les packages disponibles dans Cloud ML Engine, consultez la [ liste des versions d'exécution ](https://cloud.google.com/ml-engine/docs/scikit/runtime-version-list?hl=fr) . 

##  20 mars 2018

**FEATURE:**

La version d'exécution 1.6 de Cloud ML Engine est maintenant disponible pour
l'apprentissage et la prédiction. Cette version est compatible avec TensorFlow
1.6 et d'autres packages répertoriés dans la [ liste des versions d'exécution
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=fr) .

##  13 mars 2018

**FEATURE:**

La version d'exécution de Cloud ML Engine pour TensorFlow 1.5 est maintenant
disponible pour l'apprentissage et la prédiction. Pour plus d'informations,
consultez la [ liste des versions d'exécution ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=fr) .

##  8 février 2018

**FEATURE:**

Des fonctionnalités pour les réglages d'hyperparamètres ont été ajoutées :
arrêt automatique anticipé des essais, reprise d'une tâche de réglage
d'hyperparamètres précédente et optimisations d'efficacité supplémentaires
lorsque vous exécutez des tâches similaires. Pour en savoir plus, consultez la
[ présentation des réglages d'hyperparamètres ](https://cloud.google.com/ml-
engine/docs/tensorflow/hyperparameter-tuning-overview?hl=fr) .

##  14 décembre 2017

**FEATURE:**

La version d'exécution de Cloud ML Engine pour TensorFlow 1.4 est maintenant
disponible pour l'apprentissage et la prédiction. Pour plus d'informations,
consultez la [ liste des versions d'exécution ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=fr) .

**FEATURE:**

Python 3 est maintenant disponible pour l'apprentissage dans le cadre de la
version d'exécution de Cloud ML Engine pour TensorFlow 1.4. Pour plus
d'informations, consultez la [ liste des versions d'exécution
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=fr) .

**FEATURE:**

La prédiction en ligne est maintenant accessible aux services à cœur unique.
Consultez le guide sur la [ prédiction en ligne ](https://cloud.google.com/ml-
engine/docs/tensorflow/online-predict?hl=fr) , ainsi que l' [ article de blog
](https://cloud.google.com/blog/big-data/2017/12/bringing-cloud-ml-engine-to-
more-developers-with-online-prediction-features-and-reduced-prices?hl=fr) .

**FEATURE:**

Le prix a été réduit et simplifié pour l'entraînement et la prédiction.
Consultez le [ détail des tarifs ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=fr) , l' [ article de blog
](https://cloud.google.com/blog/big-data/2017/12/bringing-cloud-ml-engine-to-
more-developers-with-online-prediction-features-and-reduced-prices?hl=fr) et
le comparatif des anciens et nouveaux tarifs sur la page [ Questions
fréquentes sur les tarifs ](https://cloud.google.com/ml-
engine/docs/tensorflow/pricing-faq?hl=fr) .

**FEATURE:**

Les GPU P100 sont maintenant disponibles en version bêta. et leur utilisation
entraîne des frais. Pour en savoir plus, consultez les sections [ Utiliser les
GPU ](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=fr) et
[ Tarifs ](https://cloud.google.com/ai-platform/training/docs/pricing?hl=fr) .

##  26 octobre 2017

**FEATURE:**

La journalisation d'audit pour Cloud ML Engine est maintenant disponible en
version bêta. Pour plus d'informations, consultez la section [ Afficher les
journaux d'audit ](https://cloud.google.com/ml-engine/docs/tensorflow/audit-
logs?hl=fr) .

##  25 septembre 2017

**FEATURE:**

Les rôles IAM prédéfinis pour Cloud ML Engine sont maintenant disponibles pour
une utilisation générale. Pour plus d'informations, consultez la section [
Contrôle des accès ](https://cloud.google.com/ml-
engine/docs/tensorflow/access-control?hl=fr) .

##  27 juin 2017

**FEATURE:**

La version d'exécution de Cloud ML Engine pour TensorFlow 1.2 est maintenant
disponible pour l'apprentissage et la prédiction. Pour plus d'informations,
consultez la [ liste des versions d'exécution ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=fr) .

**DEPRECATED:**

Les anciennes versions d'exécution avec TensorFlow 0.11 et 0.12 ne sont plus
compatibles avec Cloud ML Engine. Pour en savoir plus, consultez la [ liste
des versions d'exécution ](https://cloud.google.com/ml-
engine/docs/tensorflow/runtime-version-list?hl=fr) et les [ calendriers de
compatibilité pour les anciennes versions d'exécution
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=fr#runtime-version-support) .

##  9 mai 2017

**FEATURE:**

La disponibilité générale des machines compatibles GPU a été annoncée. Pour
plus d'informations, consultez la section [ Utiliser les GPU pour les modèles
d'apprentissage dans le cloud ](https://cloud.google.com/ml-
engine/docs/tensorflow/using-gpus?hl=fr) .

##  27 avril 2017

**FEATURE:**

Les GPU sont maintenant disponibles dans la région us-central1. Pour consulter
la liste complète des régions acceptant les GPU, consultez la section [
Utiliser les GPU pour les modèles d'apprentissage dans le cloud
](https://cloud.google.com/ml-engine/docs/tensorflow/using-
gpus?hl=fr#requesting_gpu-enabled_machines) .

##  Version 1 (8 mars 2017)

**FEATURE:**

La disponibilité générale d'AI Platform Training a été annoncée. La version 1
de Cloud ML Engine est disponible pour une utilisation générale pour les
modèles d'apprentissage, le déploiement de modèles et la génération de
prédictions par lot. La fonctionnalité de [ réglage d'hyperparamètres
](https://cloud.google.com/ml-engine/docs/tensorflow/hyperparameter-tuning-
overview?hl=fr) est également disponible pour une utilisation générale, mais
les prédictions en ligne et les [ machines compatibles GPU
](https://cloud.google.com/ml-engine/docs/tensorflow/using-gpus?hl=fr) restent
en version bêta.

**FEATURE:**

La prédiction en ligne se trouve maintenant à l' [ étape de lancement
](https://cloud.google.com/terms/launch-stages?hl=fr) de la version bêta. Son
utilisation est soumise aux [ règles de tarification
](https://cloud.google.com/ai-platform/training/docs/pricing?hl=fr) de Cloud
ML Engine et suit la même formule de tarification que la prédiction par lot.
Bien qu'elle reste en version bêta, la prédiction en ligne n'est pas destinée
à être utilisée dans des applications critiques.

**CHANGED:**

Les environnements utilisés par Cloud ML Engine pour entraîner des modèles et
obtenir des prévisions ont été définis en tant que [ versions d'exécution
](https://cloud.google.com/ml-engine/docs/tensorflow/versioning?hl=fr) de
Cloud ML Engine. Vous pouvez spécifier une version d'exécution compatible à
utiliser lors de l'apprentissage, la définition d'une ressource de modèle ou
la demande de prédictions par lot. La principale différence entre les versions
d'exécution réside pour le moment dans la version de TensorFlow compatible,
mais d'autres différences peuvent apparaître au fil du temps. Pour plus
d'informations, consultez la [ liste des versions d'exécution
](https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-
list?hl=fr) .

**CHANGED:**

Vous pouvez désormais exécuter des tâches de prédiction par lot sur les
modèles SavedModel TensorFlow stockés dans Google Cloud Storage, et non
hébergés en tant que version de modèle dans Cloud ML Engine. Au lieu de
fournir un modèle ou un ID de version lorsque vous créez votre tâche, vous
pouvez utiliser l'URI de votre modèle SavedModel.

**DEPRECATED:**

Le SDK Google Cloud Machine Learning, précédemment publié en version alpha,
est obsolète et ne sera plus compatible à compter du 7 mai 2017. La plupart
des fonctionnalités fournies par le SDK ont été transférées vers le nouveau
package TensorFlow, [ tf.Transform ](https://github.com/tensorflow/transform)
Vous pouvez utiliser la technologie ou l'outil de votre choix pour le
prétraitement de vos données de saisie. Toutefois, nous recommandons
d'utiliser la bibliothèque ` tf.Transform ` ainsi que les services disponibles
sur Google Cloud Platform, y compris Google Cloud Dataflow, Google Cloud
Dataproc et Google BigQuery.

##  Version 1 bêta (29 septembre 2016)

**FEATURE:**

La prédiction en ligne est une fonctionnalité alpha. Bien que AI Platform
Training soit globalement dans sa phase bêta, la prédiction en ligne subit
toujours des changements significatifs pour améliorer les performances. Elle
ne vous sera pas [ facturée ](https://cloud.google.com/ai-
platform/training/docs/pricing?hl=fr) tant qu'elle ne sera disponible qu'en
version alpha.

**FEATURE:**

Le prétraitement et les autres fonctionnalités du SDK Cloud ML Engine sont en
version alpha. Le SDK est en cours de développement afin d'améliorer
l'intégration de Cloud ML Engine à Apache Beam.

