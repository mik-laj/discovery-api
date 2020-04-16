#  Notes de version

Cette page répertorie les mises à jour en production de Cloud TPU. Consultez-
la régulièrement pour obtenir des informations sur les fonctionnalités
nouvelles ou mises à jour, les corrections de bugs, les problèmes connus et
les fonctionnalités obsolètes.

Pour recevoir les dernières mises à jour de ce produit, ajoutez l'URL de cette
page à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  7 mai 2019

**FEATURE:**

Le pod Cloud TPU v2 est disponible en version bêta.

Comme les ressources TPU peuvent évoluer d'un Cloud TPU unique à un pod Cloud
TPU, vous n'avez pas besoin de choisir entre un Cloud TPU unique et un pod
Cloud TPU. Vous pouvez demander des parties de pods Cloud TPU sous forme de
_tranches_ ou d'ensembles de cœurs. Ainsi, vous n'achetez que la puissance de
traitement dont vous avez besoin.

[ Avantages du pod Cloud TPU (bêta) par rapport à un appareil Cloud TPU v2
unique : ](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=fr)

  * Augmentation de la vitesse d'entraînement pour une itération rapide en R&D 
  * Augmentation de la productivité humaine en fournissant des calculs de machine learning (ML) automatiquement évolutifs 
  * Possibilité d'entraîner des modèles bien plus volumineux 

**FEATURE:**

Le pod Cloud TPU v3 est disponible en version bêta.

Comme les ressources TPU peuvent évoluer d'un Cloud TPU unique à un pod Cloud
TPU, vous n'avez pas besoin de choisir entre un Cloud TPU unique et un pod
Cloud TPU. Vous pouvez demander des parties de pods Cloud TPU sous forme de
_tranches_ ou d'ensembles de cœurs. Ainsi, vous n'achetez que la puissance de
traitement dont vous avez besoin.

[ Avantages du pod Cloud TPU (bêta) par rapport à un appareil Cloud TPU v3
unique : ](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=fr)

  * Augmentation de la vitesse d'entraînement pour une itération rapide en R&D 
  * Augmentation de la productivité humaine en fournissant des calculs de machine learning (ML) automatiquement évolutifs 
  * Possibilité d'entraîner des modèles bien plus volumineux 

Avantages du pod Cloud TPU v3 _(bêta)_ par rapport au pod Cloud TPU v2
_(bêta)_ :

* Traitement plus rapide et plus grande mémoire : 

  * Pod v2 : 11,5 pétaflops et 4 To de mémoire intégrée (HBM) 
  * Pod v3 : 100 pétaflops et 32 To de mémoire HBM avec refroidissement liquide 

* Possibilité d'entraîner des modèles encore plus volumineux 

##  11 mars 2019

**CHANGED:**

Cloud TPU est désormais compatible avec la version 1.13 de TensorFlow [
](https://www.tensorflow.org/versions/r1.13/api_docs/?hl=fr) . La
compatibilité des versions 1.8 et 1.9 de TensorFlow a été supprimée.

Pour connaître les versions de TensorFlow actuellement compatibles, consultez
le [ règlement de gestion des versions de Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=fr) .

##  31 janvier 2019

**FEATURE:**

Cloud TPU v3 est maintenant en phase de disponibilité générale. Cloud TPU v3
dispose du double de la mémoire par rapport à v2. Cette nouveauté offre de
meilleures performances et permet la compatibilité d'un plus grand nombre de
classes de modèles, par exemple des réseaux résiduels (ResNet) plus profonds
et des images plus grandes avec RetinaNet. Les modèles existants qui
s'exécutent sur Cloud TPU v2 continueront de fonctionner. Consultez le [ guide
des versions de Cloud TPU ](https://cloud.google.com/tpu/docs/deciding-tpu-
version?hl=fr) pour obtenir plus d'informations.

##  8 novembre 2018

**CHANGED:**

Cloud TPU est désormais compatible avec la [ version 1.12 de TensorFlow
](https://www.tensorflow.org/versions/r1.12/api_docs/?hl=fr) . Cette version
comprend des améliorations pour Keras sur les Cloud TPU, intègre des
optimisations de performances dans l'ensemble de la pile logicielle, et
fournit des API, des messages d'erreur et une fiabilité améliorés.

Pour connaître les versions de TensorFlow actuellement compatibles, consultez
le [ règlement de gestion des versions de Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=fr) .

##  7 novembre 2018

**FEATURE:**

Le pod Cloud TPU v2 est disponible en version alpha.

Comme les ressources TPU peuvent évoluer d'un Cloud TPU unique à un pod Cloud
TPU, vous n'avez pas besoin de choisir entre un Cloud TPU unique et un pod
Cloud TPU. Vous pouvez demander des parties de pods Cloud TPU sous forme de
_tranches_ ou d'ensembles de cœurs. Ainsi, vous n'achetez que la puissance de
traitement dont vous avez besoin.

[ Avantages du pod Cloud TPU (alpha) :
](https://cloud.google.com/tpu/docs/deciding-pod-versus-tpu?hl=fr)

  * Augmentation de la vitesse d'entraînement pour une itération rapide en R&D 
  * Augmentation de la productivité humaine en fournissant des calculs de machine learning (ML) automatiquement évolutifs 
  * Possibilité d'entraîner des modèles bien plus volumineux que sur un accélérateur ML unique 

##  10 octobre 2018

**FEATURE:**

Cloud TPU v3 est disponible en version bêta. Dans votre configuration, vous
avez donc maintenant le choix entre v2 et v3.

  * Cloud TPU v3 dispose du double de la mémoire par rapport à v2. Cette nouveauté offre de meilleures performances et permet la compatibilité d'un plus grand nombre de classes de modèles, par exemple des réseaux résiduels (ResNet) plus profonds et des images plus grandes avec RetinaNet. 
  * Les modèles existants qui s'exécutent sur Cloud TPU v2 continueront à fonctionner. 
  * Consultez le [ guide des versions de Cloud TPU ](https://cloud.google.com/tpu/docs/deciding-tpu-version?hl=fr) pour obtenir plus d'informations. 

##  10 octobre 2018

**CHANGED:**

Les TPU préemptifs sont maintenant en phase de disponibilité générale. Un TPU
préemptif est un nœud Cloud TPU que vous pouvez créer et exécuter à un coût
bien inférieur à celui des nœuds normaux. Cependant, Cloud TPU peut
interrompre (préempter) ce type de nœud s'il a besoin d'accéder aux ressources
à d'autres fins.

  * Découvrez comment [ utiliser un TPU préemptif ](https://cloud.google.com/tpu/docs/preemptible?hl=fr) . 
  * Consultez les [ tarifs ](https://cloud.google.com/tpu/docs/pricing?hl=fr) des nœuds Cloud TPU normaux et préemptifs. 

##  27 septembre 2018

**CHANGED:**

Cloud TPU est désormais compatible avec la [ version 1.11 de TensorFlow
](https://www.tensorflow.org/versions/r1.11/api_docs/?hl=fr) . Cette version
offre la compatibilité, à titre expérimental, de tous les éléments suivants
présents sur Cloud TPU : Keras, Colab, exécution rapide, LARS, RNN et [ Mesh
TensorFlow
](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/mesh_tensorflow/README.md)
. Cette release présente également une intégration [ Cloud Bigtable
](https://cloud.google.com/bigtable/?hl=fr) hautes performances, de nouvelles
optimisations du compilateur XLA, d'autres optimisations des performances sur
l'ensemble de la pile logicielle, ainsi que des API, des messages d'erreur et
une fiabilité améliorés.

Pour connaître les versions de TensorFlow actuellement compatibles, consultez
le [ règlement de gestion des versions de Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=fr) .

##  7 septembre 2018

**CHANGED:**

La version 1.7 de TensorFlow n'est plus compatible depuis le 7 septembre 2018.
Pour connaître les versions actuellement compatibles, consultez le [ règlement
de gestion des versions de Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=fr) .

##  24 juillet 2018

**CHANGED:**

Nous sommes ravis d'annoncer des tarifs promotionnels pour Cloud TPU, qui
permettent de bénéficier de réductions importantes. Le tableau ci-dessous
présente les anciens tarifs et les nouveaux tarifs disponibles à partir
d'aujourd'hui :

###  États-Unis

|  Ancien tarif par TPU et par heure  |  Nouveau tarif par TPU et par heure  
---|---|---  
Cloud TPU  |  6,50 $ USD  |  4,50 $ USD  
TPU préemptif  |  1,95 $ USD  |  1,35 $ USD  
  
###  Europe

|  Ancien tarif par TPU et par heure  |  Nouveau tarif par TPU et par heure  
---|---|---  
Cloud TPU  |  7,15 $ USD  |  4,95 $ USD  
TPU préemptif  |  2,15 $ USD  |  1,485 $ USD  
  
###  Asie-Pacifique

|  Ancien tarif par TPU et par heure  |  Nouveau tarif par TPU et par heure  
---|---|---  
Cloud TPU  |  7,54 $ USD  |  5,22 $ USD  
TPU préemptif  |  2,26 $ USD  |  1,566 $ USD  
  
Pour en savoir plus, consultez la [ grille tarifaire
](https://cloud.google.com/tpu/docs/pricing?hl=fr) .

##  12 juillet 2018

**FEATURE:**

Cloud TPU est maintenant disponible dans Google Kubernetes Engine en tant que
fonctionnalité bêta. Exécutez votre charge de travail de machine learning dans
un cluster Kubernetes sur GCP, et laissez GKE gérer et faire évoluer les
ressources Cloud TPU à votre place.

  * Suivez le [ tutoriel ](https://cloud.google.com/tpu/docs/tutorials/kubernetes-engine-resnet?hl=fr) pour l'entraînement du modèle TensorFlow ResNet-50 sur Cloud TPU et GKE. 
  * Consultez le [ guide de configuration de GKE ](https://cloud.google.com/tpu/docs/kubernetes-engine-setup?hl=fr) pour obtenir des instructions rapides concernant l'exécution de Cloud TPU avec GKE. 

##  2 juillet 2018

**CHANGED:**

Cloud TPU est désormais compatible avec la [ version 1.9 de TensorFlow
](https://www.tensorflow.org/versions/r1.9/api_docs/?hl=fr) . Cette version
accroît les performances de Cloud TPU, et offre des API, des messages d'erreur
et une fiabilité améliorés.

##  27 juin 2018

**FEATURE:**

Cloud TPU est maintenant en phase de disponibilité générale. Les TPU
révolutionnaires de Google ont été conçus pour accélérer les charges de
travail de machine learning au moyen de TensorFlow. Grâce à une capacité de
traitement pouvant aller jusqu'à 180 téraflops, chaque ressource Cloud TPU
fournit la puissance de calcul nécessaire à l'entraînement et à l'exécution de
modèles de machine learning de pointe.

  * Suivez le [ guide de démarrage rapide ](https://cloud.google.com/tpu/docs/quickstart?hl=fr) pour configurer votre instance Cloud TPU. 
  * Choisissez un [ tutoriel ](https://cloud.google.com/tpu/docs/tutorials?hl=fr) pour exécuter un modèle spécifique sur votre ressource Cloud TPU. 

##  18 juin 2018

**FEATURE:**

Les TPU préemptifs sont maintenant disponibles en version _bêta_ . Un TPU
préemptif est un nœud Cloud TPU que vous pouvez créer et exécuter à un coût
bien inférieur à celui des nœuds normaux. Cependant, Cloud TPU peut
interrompre (préempter) ce type de nœud s'il a besoin d'accéder aux ressources
à d'autres fins.

  * Découvrez comment [ utiliser un TPU préemptif ](https://cloud.google.com/tpu/docs/preemptible?hl=fr) . 
  * Consultez les [ tarifs ](https://cloud.google.com/tpu/docs/pricing?hl=fr) des nœuds Cloud TPU normaux et préemptifs. 

**CHANGED:**

Cloud TPU est maintenant disponible dans les régions Europe et Asie-Pacifique
ainsi qu'aux États-Unis. Consultez les [ détails des tarifs
](https://cloud.google.com/tpu/docs/pricing?hl=fr) par région. Les zones
suivantes sont disponibles :

  * **États-Unis**
    * ` us-central1-b `
    * ` us-central1-c `
    * ` us-central1-f ` ( [ programme TFRC ](https://www.tensorflow.org/tfrc/?hl=fr) uniquement) 
  * **Europe**
    * ` europe-west4-a `
  * **Asie-Pacifique**
    * ` asia-east1-c `

##  12 juin 2018

**CHANGED:**

La version 1.6 de TensorFlow n'est plus compatible depuis le 12 juin 2018.
Pour connaître les versions actuellement compatibles, consultez le [ règlement
de gestion des versions de Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=fr) .

##  20 avril 2018

**CHANGED:**

Cloud TPU est désormais compatible avec la [ version 1.8 de TensorFlow
](https://www.tensorflow.org/versions/r1.8/api_docs/?hl=fr) . Cette version
accroît les performances de Cloud TPU, et offre des API, des messages d'erreur
et une fiabilité améliorés.

La version 1.7 de TensorFlow n'est plus compatible depuis le 20 juin 2018.
Pour en savoir plus, consultez le [ règlement de gestion des versions de Cloud
TPU ](https://cloud.google.com/tpu/docs/supported-versions?hl=fr) .

##  2 avril 2018

**CHANGED:**

Cloud TPU est désormais compatible avec la [ version 1.7 de TensorFlow
](https://www.tensorflow.org/versions/r1.7/api_docs/?hl=fr) . La version 1.6
de TensorFlow n'est plus compatible depuis le 2 juin 2018. Pour en savoir
plus, consultez le [ règlement de gestion des versions de Cloud TPU
](https://cloud.google.com/tpu/docs/supported-versions?hl=fr) .

##  12 février 2018

**FEATURE:**

Cloud TPU est disponible en version bêta. Les TPU révolutionnaires de Google
ont été conçus pour accélérer les charges de travail de machine learning au
moyen de TensorFlow. Grâce à une capacité de traitement pouvant aller jusqu'à
180 téraflops, chaque ressource Cloud TPU fournit la puissance de calcul
nécessaire à l'entraînement et à l'exécution de modèles de machine learning de
pointe.

  * Découvrez comment [ demander un quota de TPU ](https://cloud.google.com/tpu/docs/quota?hl=fr) . 
  * Suivez le [ guide de démarrage rapide ](https://cloud.google.com/tpu/docs/quickstart?hl=fr) pour configurer votre ressource Cloud TPU. 
  * Choisissez un [ tutoriel ](https://cloud.google.com/tpu/docs/tutorials?hl=fr) pour exécuter un modèle spécifique sur votre instance Cloud TPU. 

