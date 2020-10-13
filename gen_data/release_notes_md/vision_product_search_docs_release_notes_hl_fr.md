#  Notes de version

Cette page répertorie les mises à jour en production de Vision Product Search.
Nous recommandons aux développeurs de Vision Product Search de consulter
régulièrement cette liste pour prendre connaissance des nouvelles annonces.

Vous pouvez consulter les dernières mises à jour de produits pour l'ensemble
de Google Cloud sur la page [ Notes de version de Google Cloud
](https://cloud.google.com/release-notes?hl=fr) .

Pour recevoir les dernières mises à jour concernant ce produit, ajoutez l'URL
de cette page à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou ajoutez l'URL
du flux directement : ` https://cloud.google.com/feeds/visionproductsearch-
release-notes.xml `

##  September 18, 2019

**FEATURE:**

**Packaged goods and general vertical** :

The following product categories have been updated or added for General
Availability:

  * ` packagedgoods-v1 ` (updated) 
  * ` general-v1 ` (added) 

**FEATURE:**

**Batch deletion**

Batch deletion is now offered for the following product types:

  * All products in a specific product set 
  * All products not in any product set 

See the [ "Deleting resources" ](https://cloud.google.com/vision/product-
search/docs/delete-resources?hl=fr#batch_resource_deletion) topic for more
information.

**CHANGED:**

**Model update** : The Object Localizer model has been updated.

**CHANGED:**

Responses to ` images:annotate ` requests now include an [ ` objectAnnotation
` ](https://cloud.google.com/vision/product-
search/docs/reference/rest/v1/AnnotateImageResponse?hl=fr#objectannotation)
field with a label for the object defined by the bounding box indicated. See
the [ "Searching for products" ](https://cloud.google.com/vision/product-
search/docs/searching?hl=fr) topic for more information.

**CHANGED:**

**VPC Service Controls**

Vision Product Search VPC Service Controls provide additional security for
your pipeline's resources and services. To learn more about VPC Service
Controls, see the [ VPC Service Controls overview
](https://cloud.google.com/vpc-service-controls/docs/overview?hl=fr) .

To learn about the limitations of using Vision Product Search with VPC Service
Controls, see the [ supported products and limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-products?hl=fr)
.

##  June 07, 2019

**FEATURE:**

**Packaged goods vertical** : Adds support for a ` packagedgoods-v1 ` product
category in addition to other [ supported product categories
](https://cloud.google.com/vision/product-search/docs/product-
categories?hl=fr) .

**CHANGED:**

The following product categories have been updated:

  * ` homegoods-v2 `
  * ` apparel-v2 `
  * ` toys-v2 `

The corresponding legacy categories ( ` homegoods ` , ` apparel ` , and ` toys
` ) are still supported, but the updated categories should be used for new
products.

##  December 10, 2018

**FEATURE:**

**Cloud Vision API Product Search General Availability (GA) Release**

**FEATURE:**

**Toys vertical** : Adds support for a ` toys ` product category in addition
to other [ supported product categories
](https://cloud.google.com/vision/product-search/docs/product-
categories?hl=fr) .

**FEATURE:**

**Multi-detection** : Detects [ multiple products
](https://cloud.google.com/vision/product-search/docs/searching-
response?hl=fr#multiple-product_images_multi-detection_response) in an image,
and then provides similar products to each product found.

##  July 24, 2018

**FEATURE:**

**Beta Release of Vision Product Search**

The Beta version of Vision Product Search is now available.

