#  Release Notes

This page documents production updates to Vision Product Search. We recommend
that Vision Product Search developers periodically check this list for any new
announcements.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/cloud-vision-api-product-
search-release-notes.xml `

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
search/docs/delete-resources#batch_resource_deletion) topic for more
information.

**CHANGED:**

**Model update** : The Object Localizer model has been updated.

**CHANGED:**

Responses to ` images:annotate ` requests now include an [ ` objectAnnotation
` ](https://cloud.google.com/vision/product-
search/docs/reference/rest/v1/AnnotateImageResponse#objectannotation) field
with a label for the object defined by the bounding box indicated. See the [
"Searching for products" ](https://cloud.google.com/vision/product-
search/docs/searching) topic for more information.

**CHANGED:**

**VPC Service Controls**

Vision Product Search VPC Service Controls provide additional security for
your pipeline's resources and services. To learn more about VPC Service
Controls, see the [ VPC Service Controls overview
](https://cloud.google.com/vpc-service-controls/docs/overview) .

To learn about the limitations in using Vision Product Search with VPC Service
Controls, see the [ supported products and limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-products) .

##  June 07, 2019

**FEATURE:**

**Packaged goods vertical** : Adds support for a ` packagedgoods-v1 ` product
category in addition to other [ supported product categories
](https://cloud.google.com/vision/product-search/docs/product-categories) .

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
](https://cloud.google.com/vision/product-search/docs/product-categories) .

**FEATURE:**

**Multi-detection** : Detects [ multiple products
](https://cloud.google.com/vision/product-search/docs/searching-
response#multiple-product_images_multi-detection_response) in an image, and
then provides similar products to each product found.

##  July 24, 2018

**FEATURE:**

**Beta Release of Vision Product Search**

The Beta version of Vision Product Search is now available.

