#  Notas de la versión

En esta página, se documentan las actualizaciones de producción de Vision
Product Search. Recomendamos que los desarrolladores de Vision Product Search
verifiquen de forma periódica esta lista para ver si hay anuncios nuevos.

Puedes ver las últimas actualizaciones de productos de todo Google Cloud en la
página [ Notas de la versión de Google Cloud
](https://cloud.google.com/release-notes?hl=es_419) .

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , o agrega
directamente la URL del feed: `
https://cloud.google.com/feeds/visionproductsearch-release-notes.xml `

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
search/docs/delete-resources?hl=es_419#batch_resource_deletion) topic for more
information.

**CHANGED:**

**Model update** : The Object Localizer model has been updated.

**CHANGED:**

Responses to ` images:annotate ` requests now include an [ ` objectAnnotation
` ](https://cloud.google.com/vision/product-
search/docs/reference/rest/v1/AnnotateImageResponse?hl=es_419#objectannotation)
field with a label for the object defined by the bounding box indicated. See
the [ "Searching for products" ](https://cloud.google.com/vision/product-
search/docs/searching?hl=es_419) topic for more information.

**CHANGED:**

**VPC Service Controls**

Vision Product Search VPC Service Controls provide additional security for
your pipeline's resources and services. To learn more about VPC Service
Controls, see the [ VPC Service Controls overview
](https://cloud.google.com/vpc-service-controls/docs/overview?hl=es_419) .

To learn about the limitations of using Vision Product Search with VPC Service
Controls, see the [ supported products and limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products?hl=es_419) .

##  June 07, 2019

**FEATURE:**

**Packaged goods vertical** : Adds support for a ` packagedgoods-v1 ` product
category in addition to other [ supported product categories
](https://cloud.google.com/vision/product-search/docs/product-
categories?hl=es_419) .

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
categories?hl=es_419) .

**FEATURE:**

**Multi-detection** : Detects [ multiple products
](https://cloud.google.com/vision/product-search/docs/searching-
response?hl=es_419#multiple-product_images_multi-detection_response) in an
image, and then provides similar products to each product found.

##  July 24, 2018

**FEATURE:**

**Beta Release of Vision Product Search**

The Beta version of Vision Product Search is now available.

