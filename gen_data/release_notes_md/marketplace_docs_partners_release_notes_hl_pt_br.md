#  Notas da versão

Esta página contém as notas de versão mais recentes de recursos e atualizações
dos parceiros do Google Cloud Marketplace.

É possível ver as atualizações mais recentes de todos os produtos do Google
Cloud na página [ Notas da versão do Google Cloud
](https://cloud.google.com/release-notes?hl=pt-br) .

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou adicione o URL
do feed diretamente: ` https://cloud.google.com/feeds/gcp-marketplace-
partners-release-notes.xml `

##  April 16, 2020

**FEATURE:**

You can now create private quotes for VM solutions ( [ alpha
](https://cloud.google.com/products/?hl=EN#product-launch-stages) ).

[ Learn about creating quotes for specific customers
](https://cloud.google.com/marketplace/docs/partners/create-quotes?hl=pt-br) .

##  April 01, 2020

**FEATURE:**

If you sell Kubernetes apps on Google Cloud Marketplace, you can now configure
your app to target clusters where at least one node has a GPU. When users
deploy the app, only clusters with GPUs are shown as valid deployment targets.

[ Learn about modifying your app's ` schema.md ` to check for GPUs
](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-
tools/blob/master/docs/schema.md#gpus) .

[ Read the overview of selling Kubernetes apps on Google Cloud Marketplace
](https://cloud.google.com/marketplace/docs/partners/kubernetes-
solutions/?hl=pt-br) .

##  January 27, 2020

**FEATURE:**

If you sell Managed Services on Google Cloud Marketplace, you can now monitor
your solution's analytics and track your marketing campaigns on the [ Solution
Analytics page
](https://console.cloud.google.com/partner/analytics?_ga=2.65050663.883067678.1580151692-404355855.1580151692&hl=pt-
br) .

For information on interpreting the metrics and setting up tracking campaigns,
see [ Monitoring your solution's analytics
](https://console.cloud.google.com/partner/analytics?_ga=2.65050663.883067678.1580151692-404355855.1580151692&hl=pt-
br) .

##  December 10, 2019

**CHANGED:**

The SKUs for GCP Marketplace's VM solutions are changing, which may affect the
data shown in your reports:

  * In your Customer Insights reports, the ` sku_id ` and ` sku_description ` columns will show new values to reflect the change in SKU. 

  * If your VM solution is priced by usage, the usage report now shows only the resources that you use to set your price. For example, if you set your price by CPU usage, the report will only show information about the user's CPU usage. 

For more information on the reports that you receive, see [ Payments and
reports ](https://cloud.google.com/marketplace/docs/partners/payments-
reporting?hl=pt-br) .

##  November 14, 2019

**FEATURE:**

Private Pricing is now Generally Available (GA). With GCP Marketplace Private
Pricing, you can create custom quotes for specific customers for Kubernetes
applications or Integrated SaaS solutions.

To get started, see [ Creating quotes for specific customers
](https://cloud.google.com/marketplace/docs/partners/create-quotes?hl=pt-br) .

##  October 31, 2019

**FEATURE:**

**Application Manager (Beta)** : If you offer Kubernetes applications on GCP
Marketplace, you can now enable managed updates for the application.

With managed updates, your users can update to new releases of your
application from the GCP Console with a few clicks.

[ Learn about supporting managed updates for your Kubernetes applications
](https://cloud.google.com/marketplace/docs/partners/kubernetes-
solutions/support-managed-updates?hl=pt-br) .

##  September 25, 2019

**FEATURE:**

You can now receive your reports in a Google Drive folder, Cloud Storage
bucket, or both. For steps to set up your reports, see [ Payments and reports
](https://cloud.google.com/marketplace/docs/partners/payments-reporting?hl=pt-
br) .

##  May 21, 2019

**FEATURE:**

If you are selling managed services (Integrated SaaS) solutions, you can now
offer subscription plans for specific periods. For example, you can create a
subscription plan for users who sign up for one year, three years, or more.

Learn more about [ selling managed services on GCP Marketplace
](https://cloud.google.com/marketplace/docs/partners/integrated-saas/?hl=pt-
br) .

##  May 17, 2019

**FEATURE:**

For your Kubernetes applications, you can now [ set up your pricing model in
Partner Portal
](https://cloud.google.com/marketplace/docs/partners/kubernetes-
solutions/select-pricing?hl=pt-br#add-in-partner-portal) .

##  May 10, 2019

**FEATURE:**

If you sell Managed Services or Kubernetes applications on GCP Marketplace,
you can now offer trials of your software. For information on setting up
trials, see:

  * [ Choosing a pricing model for Kubernetes Solutions ](https://cloud.google.com/marketplace/docs/partners/kubernetes-solutions/select-pricing?hl=pt-br)
  * [ Choosing a pricing model for Managed Services ](https://cloud.google.com/marketplace/docs/partners/integrated-saas/select-pricing?hl=pt-br)

##  April 23, 2019

**DEPRECATED:**

GCP Marketplace no longer accepts new Standalone SaaS solutions. For
information about your options, contact the Partner Onboarding team at [
cloud-partner-onboarding+ss@google.com ](mailto:cloud-partner-
onboarding+ss@google.com) . Learn more about [ the solutions that you can
distribute on GCP Marketplace
](https://cloud.google.com/marketplace/docs/partners/?hl=pt-br#supported-
solutions) .

**CHANGED:**

We recommend using the [ open source ` deploymentmanager-autogen ` tool
](https://github.com/GoogleCloudPlatform/deploymentmanager-autogen) to
generate Deployment Manager templates. With Autogen, your deployment package
includes the following capabilities:

  * Quota checks for CPUs and GPUs, so that users cannot deploy your solution if they exceed the quota requirements. 
  * Dynamic price updates in the Deployment Manager page. 
  * Prevents users from choosing GPUs that are not available in the zone that they choose. 

Learn more about [ distributing VM-based solutions on GCP Marketplace
](https://cloud.google.com/marketplace/docs/partners/vm/index?hl=pt-br) .

##  April 09, 2019

**FEATURE:**

Kubernetes applications on GCP Marketplace are now **Generally Available** .

For an overview of selling containerized applications on GCP Marketplace, see
[ Distributing Kubernetes Applications
](https://cloud.google.com/marketplace/docs/partners/kubernetes-
solutions/?hl=pt-br) .

**FEATURE:**

You can now distribute Kubernetes applications that run on GKE On-Prem
clusters, and clusters that run [ Istio ](https://istio.io/) .

Review the [ requirements to support GKE On-Prem
](https://cloud.google.com/marketplace/docs/partners/kubernetes-
solutions/create-app-package?hl=pt-br#on-prem-reqs) , and the [ considerations
for making your application compatible with Istio
](https://cloud.google.com/marketplace/docs/partners/kubernetes-
solutions/create-app-package?hl=pt-br#istio-limitations) .

##  November 16, 2018

**FEATURE:**

The documentation has been updated with information on selling Integrated SaaS
solutions on Google Cloud Platform Marketplace. Integrated SaaS solutions are
software solutions that run on your infrastructure, regardless of location,
but are billed by Google.

For an overview of selling Integrated SaaS solutions on GCP Marketplace, see [
Selling Managed Services
](https://cloud.google.com/marketplace/docs/partners/integrated-saas/?hl=pt-
br) .

##  November 01, 2018

**FEATURE:**

Your monthly reports now include a Customer Insights report, which includes
information on how your customers are using your software on GCP.

For information on Customer Insights reports, see [ Payments and Reporting
](https://cloud.google.com/marketplace/docs/partners/payments-reporting?hl=pt-
br) .

##  September 28, 2018

**FEATURE:**

The documentation has been updated with steps to distribute Kubernetes
applications on Google Cloud Platform Marketplace.

For an overview of selling containerized applications on GCP Marketplace, see
[ Distributing Kubernetes Applications
](https://cloud.google.com/marketplace/docs/partners/kubernetes-
solutions/?hl=pt-br) .

##  July 23, 2018

**FEATURE:**

If you sell VM solutions on GCP Marketplace, you can now offer trials of your
software. For information on setting up trials, see the [ technical setup for
VM solutions ](https://cloud.google.com/marketplace/docs/partners/vm/select-
pricing?hl=pt-br) .

