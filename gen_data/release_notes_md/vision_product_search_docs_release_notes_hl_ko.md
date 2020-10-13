#  출시 노트

이 페이지는 Vision 제품 검색의 프로덕션 업데이트를 설명합니다. Vision 제품 검색 개발자는 이 목록을 주기적으로 참고하여 새로운
공지사항을 확인하는 것이 좋습니다.

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서 모든
Google Cloud의 최신 제품 업데이트를 확인할 수 있습니다.

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL을 다음과 같이 직접 추가하세요. `
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
search/docs/delete-resources?hl=ko#batch_resource_deletion) topic for more
information.

**CHANGED:**

**Model update** : The Object Localizer model has been updated.

**CHANGED:**

Responses to ` images:annotate ` requests now include an [ ` objectAnnotation
` ](https://cloud.google.com/vision/product-
search/docs/reference/rest/v1/AnnotateImageResponse?hl=ko#objectannotation)
field with a label for the object defined by the bounding box indicated. See
the [ "Searching for products" ](https://cloud.google.com/vision/product-
search/docs/searching?hl=ko) topic for more information.

**CHANGED:**

**VPC Service Controls**

Vision Product Search VPC Service Controls provide additional security for
your pipeline's resources and services. To learn more about VPC Service
Controls, see the [ VPC Service Controls overview
](https://cloud.google.com/vpc-service-controls/docs/overview?hl=ko) .

To learn about the limitations of using Vision Product Search with VPC Service
Controls, see the [ supported products and limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-products?hl=ko)
.

##  June 07, 2019

**FEATURE:**

**Packaged goods vertical** : Adds support for a ` packagedgoods-v1 ` product
category in addition to other [ supported product categories
](https://cloud.google.com/vision/product-search/docs/product-
categories?hl=ko) .

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
categories?hl=ko) .

**FEATURE:**

**Multi-detection** : Detects [ multiple products
](https://cloud.google.com/vision/product-search/docs/searching-
response?hl=ko#multiple-product_images_multi-detection_response) in an image,
and then provides similar products to each product found.

##  July 24, 2018

**FEATURE:**

**Beta Release of Vision Product Search**

The Beta version of Vision Product Search is now available.

