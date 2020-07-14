#  출시 노트

이 페이지에는 Cloud Marketplace의 기능과 업데이트에 대한 최신 출시 노트가 포함되어 있습니다.

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서 모든
Google Cloud의 최신 제품 업데이트를 확인할 수 있습니다.

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL을 다음과 같이 직접 추가하세요. `
https://cloud.google.com/feeds/gcpmarketplace-release-notes.xml `

##  July 13, 2020

**CHANGED:**

The IAM permissions required for purchasing the following solutions from
Google Cloud Marketplace have changed:

  * Apache Kafka® on Confluent Cloud™ 
  * DataStax Astra for Apache Cassandra 
  * Elasticsearch Service on Elastic Cloud 
  * NetApp Cloud Volumes Service 
  * Redis Enterprise Cloud 

If you use [ custom roles ](https://cloud.google.com/iam/docs/understanding-
custom-roles?hl=ko) to purchase these solutions, you must update the custom
roles to include the permissions described in [ Access Control for Google
Cloud Marketplace ](https://cloud.google.com/marketplace/docs/access-
control?hl=ko) .

Specifically, if your custom role includes the ` billing.subscriptions.create
` permission, you must update it to include the `
consumerprocurement.orders.place ` and the `
consumerprocurement.accounts.create ` permissions.

If you use the [ Billing Administrator
](https://cloud.google.com/iam/docs/understanding-roles?hl=ko#billing-roles)
role to purchase these solutions, you don't need to take any action.

##  April 14, 2020

**CHANGED:**

Security software agents on Google Cloud Marketplace are now **Generally
available** .

Security software agents are typically part of larger security solutions, and
can be deployed to VM instances in your projects.

[ Learn about Deploying security software agents
](https://cloud.google.com/marketplace/docs/deploy-security-software-
agents?hl=ko) .

##  February 27, 2020

**FEATURE:**

You can deploy security software agents, which are typically part of larger
security solutions, from Google Cloud Marketplace to the VM instances in your
projects.

[ Learn about Deploying security software agents
](https://cloud.google.com/marketplace/docs/deploy-security-software-
agents?hl=ko) .

##  May 10, 2019

**FEATURE:**

Vendors of managed services and Kubernetes applications can now offer trials
of their software. During trials, you can use the software without paying for
the software license.

For information on how you are billed during a trial, see [ Understanding
Billing ](https://cloud.google.com/marketplace/docs/understanding-
billing?hl=ko) .

##  April 09, 2019

**CHANGED:**

Some vendors provide Kubernetes applications that can run on GKE On-Prem
clusters, and clusters that run Istio.

Learn about the [ prerequisites for running Kubernetes applications with GKE
On-Prem or Istio ](https://cloud.google.com/marketplace/docs/kubernetes-
apps/?hl=ko#on-prem-istio-prereqs) .

**FEATURE:**

Kubernetes applications on GCP Marketplace are now **Generally Available** .

For steps to set up a billing plan for Kubernetes applications, see [ Managing
Billing Plans for Kubernetes Applications
](https://cloud.google.com/marketplace/docs/kubernetes-apps/manage-billing-
kubernetes?hl=ko) .

##  July 23, 2018

**FEATURE:**

Vendors of VM solutions can offer trials of their software. During trials, you
can use the software without paying for the software license.

For information on how you are billed during a trial, see [ Understanding
Billing ](https://cloud.google.com/marketplace/docs/understanding-
billing?hl=ko) .

##  July 18, 2018

**CHANGED:**

Google Cloud Launcher is now Google Cloud Platform Marketplace.

**FEATURE:**

GCP Marketplace now includes commercial Kubernetes applications, which you can
deploy to your Google Kubernetes Engine clusters.

For steps to set up a billing plan for Kubernetes applications, see [ Managing
Billing Plans for Kubernetes Applications
](https://cloud.google.com/marketplace/docs/kubernetes-apps/manage-billing-
kubernetes?hl=ko) .

**DEPRECATED:**

The container registry ` launcher.gcr.io ` is deprecated. For steps you need
to take to modify your scripts or configurations, as applicable, see [
Deploying Containers ](https://cloud.google.com/marketplace/docs/container-
images?hl=ko) .

