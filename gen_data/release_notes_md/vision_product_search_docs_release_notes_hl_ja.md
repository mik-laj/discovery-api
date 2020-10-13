#  リリースノート

このページには、Vision Product Search に関する更新内容が記載されています。Vision Product Search
デベロッパーの方には、ここにリストされる発表内容を定期的に確認されることをおすすめします。

[ Google Cloud リリースノート ](https://cloud.google.com/release-notes?hl=ja)
のページで、Google Cloud の最新のプロダクト更新情報をすべて確認できます。

プロダクトのアップデートに関する最新情報を受け取るには、このページの URL を [ フィード リーダー
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) に追加するか、またはフィード
URL ディレクトリ ` https://cloud.google.com/feeds/visionproductsearch-release-
notes.xml ` を直接追加します。

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
search/docs/delete-resources?hl=ja#batch_resource_deletion) topic for more
information.

**CHANGED:**

**Model update** : The Object Localizer model has been updated.

**CHANGED:**

Responses to ` images:annotate ` requests now include an [ ` objectAnnotation
` ](https://cloud.google.com/vision/product-
search/docs/reference/rest/v1/AnnotateImageResponse?hl=ja#objectannotation)
field with a label for the object defined by the bounding box indicated. See
the [ "Searching for products" ](https://cloud.google.com/vision/product-
search/docs/searching?hl=ja) topic for more information.

**CHANGED:**

**VPC Service Controls**

Vision Product Search VPC Service Controls provide additional security for
your pipeline's resources and services. To learn more about VPC Service
Controls, see the [ VPC Service Controls overview
](https://cloud.google.com/vpc-service-controls/docs/overview?hl=ja) .

To learn about the limitations of using Vision Product Search with VPC Service
Controls, see the [ supported products and limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-products?hl=ja)
.

##  June 07, 2019

**FEATURE:**

**Packaged goods vertical** : Adds support for a ` packagedgoods-v1 ` product
category in addition to other [ supported product categories
](https://cloud.google.com/vision/product-search/docs/product-
categories?hl=ja) .

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
categories?hl=ja) .

**FEATURE:**

**Multi-detection** : Detects [ multiple products
](https://cloud.google.com/vision/product-search/docs/searching-
response?hl=ja#multiple-product_images_multi-detection_response) in an image,
and then provides similar products to each product found.

##  July 24, 2018

**FEATURE:**

**Beta Release of Vision Product Search**

The Beta version of Vision Product Search is now available.

