#  Release Notes

This page documents production updates to Cloud Billing. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/billing-release-notes.xml `

##  August 12, 2020

**FEATURE:**

Recommendations for Compute Engine committed use discounts are now available
in **beta** . Recommendations provide you opportunities to optimize your
compute costs by analyzing your VM spending trends and recommending committed
use discount contracts. For understanding and purchasing committed use
discount recommendations, see [ the documentation
](https://cloud.google.com/billing/docs/how-to/cud-analysis-resource-
based#understanding_commitment_recommendations) .

##  August 07, 2020

**FEATURE:**

You can now view a summary of all your spend-based committed use discounts
(CUD) and purchase new commitments in the [ commitment dashboard
](https://cloud.google.com/docs/cuds-spend-based#view_commitment_dashboard) .
The dashboard lists the **type** of commitment, **region** it's located,
current **active** commitments, **term** length, and the **start** and **end**
dates for the commitment. See [ the documentation
](https://cloud.google.com/docs/cuds-spend-based#view_commitment_dashboard)
for more details.

##  August 06, 2020

**FEATURE:**

If you have a **negotiated pricing contract** associated with your Cloud
Billing account, **starting with your July 2020 invoice** , the [ **Cloud
Billing report** ](https://cloud.google.com/billing/docs/how-to/reports) and
the [ **Cost Breakdown report** ](https://cloud.google.com/billing/docs/how-
to/cost-breakdown) now support displaying your costs calculated using list
prices, displaying your **negotiated savings** as a separate credit. This view
helps you see how much money you are saving on your Google Cloud costs because
of your negotiated pricing contract.

For information on how to view your list costs and negotiated savings in
reports, see the documentation:

  * [ Learn more about viewing negotiated savings in your **Cloud Billing report** ](https://cloud.google.com/billing/docs/how-to/reports#contract-pricing) . 
  * [ Learn more about viewing negotiated savings in your **Cost Breakdown report** ](https://cloud.google.com/billing/docs/how-to/cost-breakdown#negotiated-savings) . 

##  July 23, 2020

**FEATURE:**

**Export your Cloud Billing account SKU prices to BigQuery.** You can now
export your pricing information for Google Cloud and Google Maps Platform SKUs
to BigQuery. Exporting your pricing data allows you to audit, analyze, and/or
join your pricing data with your exported cost data. The pricing export
includes list prices, pricing tiers, and, when applicable, any promotional or
negotiated pricing. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/export-data-bigquery) for more
details.

##  July 10, 2020

**FEATURE:**

The [ Cost Table report ](https://cloud.google.com/billing/docs/how-to/cost-
table) functionality has been updated to add a **Table configuration**
interface that replaces the previous _Group by_ and _Label_ selectors. Use the
new **Table configuration** dialog to choose a **Label key** and select your
**Group by** options. Additionally, the available **Group by** options have
been enhanced to include a new **Custom grouping** option. Use custom grouping
to view a [ nested cost table ](https://cloud.google.com/billing/docs/how-
to/cost-table#nested_table_view) with your costs grouped by up to three
dimensions that you choose, including label values. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/cost-table) for more details.

##  June 23, 2020

**FEATURE:**

Committed use discounts (CUDs) are now available to purchase for Cloud SQL.
CUDs provide discounted prices in exchange for your commitment to use a
minimum level of resources for a specified term. With spend-based committed
use discounts for Cloud SQL, you can earn a deep discount off your cost of use
in exchange for committing to continuously use database instances in a
particular region for a 1- or 3-year term. See the [ blog
](https://cloud.google.com/blog/products/databases/cloud-sql-database-
instances-now-discounted) and [ documentation
](https://cloud.google.com/docs/cuds) for more details.

##  May 29, 2020

**FEATURE:**

[ ` Labels ` ](https://cloud.google.com/billing/docs/how-to/cost-
table#columns_in_the_cost_table) column added to the [ flat table view
](https://cloud.google.com/billing/docs/how-to/cost-table#flat_table_view) of
the Cloud Billing Cost Table report. The Cost Table report provides a tabular
view of your invoice costs. You can quickly filter your costs by available
fields, such as project, service, SKU, and labels (among other fields), and
you can download the table to CSV for offline analysis. See the [
documentation ](https://cloud.google.com/billing/docs/how-to/cost-table) for
more details.

##  May 27, 2020

**CHANGED:**

New data property now available for Cloud Billing budget alerts that are
configured for [ programmatic notifications
](https://cloud.google.com/billing/docs/how-to/budgets-programmatic-
notifications) . You set up a Cloud Billing budget to trigger an alert
notification based on [ threshold rules
](https://cloud.google.com/billing/docs/how-to/budgets#alert-thresholds) for
_Actual_ or _Forecasted_ spend. Programmatic notifications triggered on
**Forecasted** costs are now identified with the ` forecastThresholdExceeded `
property in the JSON object. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/budgets-programmatic-
notifications#notification_format) for more details.

##  May 21, 2020

**FEATURE:**

Cloud Billing Budget API: new budget filters for groups of subaccounts and
resource labels are now available in the Budget API. See the [ documentation
](https://cloud.google.com/billing/docs/reference/budget/rest/v1beta1/billingAccounts.budgets)
for more details.

##  May 18, 2020

**FEATURE:**

**Cloud Billing budgets emails** : ensure your budget alert emails are seen by
the right people using Cloud Monitoring notifications on your Cloud Billing
budgets. By default, alert emails are sent to Billing Account Administrators.
With the _Monitoring notifications_ feature, you can customize your budget to
send alerts to up to five additional email recipients you specify. See the [
documentation ](https://cloud.google.com/billing/docs/how-to/budgets-
notification-recipients) for more details.

**FEATURE:**

New information is now available on your **Cloud Billing** account
**Overview** page in the **Cloud Console** , featuring at-a-glance summaries
of the top five spending projects and top five spending products over the last
12 months.

To see the updated Billing Account Overview page, go to the [ Manage billing
accounts page ](https://console.cloud.google.com/billing) in the Cloud Console
and sign in, then select the name of the Cloud Billing account you want to
view. The Billing Overview page is displayed with the **BILLING ACCOUNT
OVERVIEW** tab selected. You might need to scroll the page to see all the
features.

##  April 23, 2020

**FEATURE:**

For customers with [ self-serve/online
](https://cloud.google.com/billing/docs/concepts#billing_account_types) Cloud
Billing accounts, you can now find your Cloud Billing documents in the
**Documents** page of the Cloud Billing console. In the Documents page, you
can find your monthly invoices or statements, as well as tax documents, if
applicable to your account. Before this launch, the Documents page was only
available to customers viewing [ invoiced
](https://cloud.google.com/billing/docs/concepts#billing_account_types) Cloud
Billing accounts, while self-serve/online accounts were limited to finding
their Cloud Billing documents in the Transactions page. See the [
⁠documentation ](https://cloud.google.com/billing/docs/how-to/get-invoice) for
more details.

**CHANGED:**

Cost forecasts in Cloud Billing reports has been updated to calculate your
forecasted spend up to 12 months in the future. Previously, the calculation
forecasted your spend for the next 30 days. Cost forecasts make it easier to
see at a glance how your costs are trending and how much you are projected to
spend over a time range you specify. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/reports#cost-forecast) for more
information.

##  April 22, 2020

**FEATURE:**

Budget alerts: new budget filters are now available. In addition to project
and product filters, you can now scope your budgets and alerts for groups of
subaccounts and resource labels. Budget alerts help you stay informed of how
your spend is tracking against your budget so you can avoid billing surprises.
(Note that these filters are not available in the Budgets API in this
release.) See the [ ⁠documentation
](https://cloud.google.com/billing/docs/how-to/budgets) for more details.

##  April 16, 2020

**FEATURE:**

Discount sharing for committed use discounts is now available in **beta** .
With discount sharing enabled, you can apply your purchased commitments across
multiple projects within a single Cloud Billing account. Discount sharing
helps you minimize the overhead of managing each of your commitments
individually and provides increased flexibility so that you can use the
compute options that best suit your needs, while also increasing cost
predictability.

  * For more information about enabling committed use discount sharing, see [ Turning on committed use discount sharing ](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#turning_on_committed_use_discount_sharing) . 
  * For more information on the possible cost savings using committed use discount sharing, see [ Understanding discount sharing ](https://cloud.google.com/billing/docs/how-to/cud-analysis#understanding_discount_sharing) . 

**FEATURE:**

Cloud Billing console now has a Pricing report, providing a tabular view of
the prices of Google’s cloud services SKUs, including Google Cloud, Google
Maps Platform, and G Suite. You can select to view the SKUs with historical
usage on the billing account or all Google Cloud SKUs. If you have a
negotiated contract, the pricing table will include the list price, the
contract price and the effective discount. You can also download the table to
CSV for offline analysis. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/pricing-table) for more
details.

##  March 23, 2020

**FEATURE:**

**Billing health checks** is now available on your **Cloud Billing** account
**Overview** page in the **Cloud Console** . This feature automatically
analyzes the health of your **Cloud Billing** account, then displays the
results in a Billing health checks informational card, helping you avoid
common billing-related issues and to adopt our [ best-practice recommendations
](https://cloud.google.com/billing/docs/onboarding-checklist#checklist_3) . In
the info card, click **_View all health checks_ ** to view a page with
detailed recommendations, explanations, and action items to remedy issues that
could jeopardize the safety or condition of your Cloud Billing account.

To see the **Billing health checks** card, go to the [ Manage billing accounts
page ](https://console.cloud.google.com/billing) in the Cloud Console and sign
in, then select the name of the billing account you want to view. The Billing
Overview page is displayed with the **BILLING ACCOUNT OVERVIEW** tab selected.
Look for the card titled **Billing health checks** .

##  March 02, 2020

**FEATURE:**

The Cost Table report now includes a nested table view, providing a
hierarchical, tree-structured view of your cost data which is helpful when
analyzing your billing data online. You can select your grouping options,
filter your costs by project, service, and SKU (among other fields), and
specify the table columns to be displayed. You can also download the table to
CSV for offline analysis. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/cost-table) for more details.

##  December 04, 2019

**FEATURE:**

The Cloud Billing reports now support filtering and grouping costs by User
Labels. See the [ documentation ](https://cloud.google.com/billing/docs/how-
to/reports#filtering_and_grouping) for more details. Learn more about [ User
Labels ](https://cloud.google.com/resource-manager/docs/creating-managing-
labels) .

##  December 01, 2019

**CHANGED:**

Starting with your November 2019 invoice, we have removed project-level cost
detail from your [ Google Cloud invoices and statements
](https://cloud.google.com/billing/docs/how-to/read-invoice) . If your
organization currently processes the invoice CSV and requires project-level
cost detail, [ download the CSV from the Cost Table report
](https://cloud.google.com/billing/docs/how-to/cost-table) and process it in
place of the invoice CSV.

##  November 18, 2019

**FEATURE:**

The Cloud Billing Committed Use Discounts (CUD) Analysis report is now
available in GA. View the CUD Analysis report to easily visualize the
effectiveness and financial impact of committed use discounts you have
purchased. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/cud-analysis) for more details.
Learn more about [ Committed Use Discounts
](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-
discounts) .

##  November 13, 2019

**CHANGED:**

Cloud Billing data export to BigQuery now reports all service usage at an
hourly granularity. For each reporting service in the export, this means that
the ` usage_start_time ` and ` usage_end_time ` fields will report hourly
data; that is, the usage end time will always be exactly one hour after the
start time. This improves the consistency and data accuracy of your reporting
data across all GCP services, while also providing support for future billing
export changes. See the Cloud Billing [ BigQuery export schema
](https://cloud.google.com/billing/docs/how-to/export-data-
bigquery#billing_data_in) and [ documentation
](https://cloud.google.com/billing/docs/how-to/export-data-bigquery) for more
details.

##  November 12, 2019

**FEATURE:**

The Cloud Billing Budget API is now available in Beta. With the Budget API,
you can view, create, and manage budgets programmatically at scale. Budget
alerts help you stay informed of how your spend is tracking against your
budget so you can avoid billing surprises. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/budget-api-overview) for more
details.

##  September 25, 2019

**FEATURE:**

The Cloud Billing reports page now supports URL bookmarking and sharing. As
you configure your report by setting filters and groupings, your URL updates
to include your selections. You can save your report settings by bookmarking
the URL. You can share the report by copying the URL. See the [ documentation
](https://cloud.google.com/billing/docs/how-
to/reports#changing_chart_settings) for more details.

##  August 27, 2019

**FEATURE:**

Set budget alerts on projects and products. New, more granular budget filters
are now available, allowing you to scope your budgets and alerts for groups of
projects and GCP services. Budget alerts help you stay informed of how your
spend is tracking against your budget so you can avoid billing surprises. See
the [ documentation ](https://cloud.google.com/billing/docs/how-to/budgets)
for more details.

##  August 26, 2019

**CHANGED:**

Billing Navigation—Invoices renamed to Documents: The **Invoices** page in the
GCP Billing Console has been renamed to **Documents** . Additionally, the page
has been refreshed to improve navigation. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/get-invoice#get_your_invoice)
for more details.

##  August 22, 2019

**FEATURE:**

The Cost Table report is now available in Cloud Billing. Use Cost Table
reports to get a tabular view of your invoice costs grouped by project and
SKU. You can quickly filter your costs by project, service, and SKU (among
other fields), and you can download the table to CSV for offline analysis. See
the [ documentation ](https://cloud.google.com/billing/docs/how-to/cost-table)
for more details.

##  August 12, 2019

**CHANGED:**

The Billing Account Overview page in the GCP Console was redesigned to provide
you with an at-a-glance summary of your charges to date, estimated end-of-
month charges, and any credit balances. The functionality of the previous
overview page, such as [ viewing the projects linked to a billing account
](https://cloud.google.com/billing/docs/how-to/view-linked) or [ viewing and
updating billing permissions ](https://cloud.google.com/billing/docs/how-
to/billing-access#update_billing_permissions) , is now available in the new
Account Management page.

  * To see the **updated Billing Account Overview page** , go to the Google Cloud Platform Console [ Manage billing accounts page ](https://console.cloud.google.com/billing) and sign in, then select the name of the billing account you want to view. The Billing Overview page is displayed with the **BILLING ACCOUNT OVERVIEW** tab selected. (Note that to view an at-a-glance summary of your payments and account balance, select the PAYMENT OVERVIEW tab.) 
  * To see the **new Account Management page** , go to the Google Cloud Platform Console [ Manage billing accounts page ](https://console.cloud.google.com/billing) , sign in, and select the name of the billing account you want to view. Then from the Billing menu on the left, click **Account management** . 

##  June 26, 2019

**FEATURE:**

**Complete Billing Record in Reports** : Starting with your May 2019 invoice
(issued in early June 2019), you can configure your Cloud Billing reports to
view your charges by invoice, including invoice-level charges (for example,
taxes, contractual credits, or surcharges) and any rounding errors. Use this
view to reconcile your Cloud Billing reports to your invoice, to the penny.
See the [ documentation ](https://cloud.google.com/billing/docs/how-
to/reports#invoice-charges) for more details.

**Cost Breakdown Reports** : Cost Breakdown reports are now available in Cloud
Billing. Use Cost Breakdown reports for a quick overview of how usage-based
discounts and credits save you money on your GCP invoice. See the [
documentation ](https://cloud.google.com/billing/docs/how-to/cost-breakdown)
for more details.

##  June 11, 2019

**FEATURE:**

The Cloud Billing Committed Use Discounts (CUD) Analysis report is now
available in Beta. View the CUD Analysis report to easily visualize the
effectiveness and financial impact of committed use discounts you have
purchased. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/cud-analysis) for more details.
Learn more about [ Committed Use Discounts
](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-
discounts) .

##  May 22, 2019

**FEATURE:**

The Cloud Billing reports now support filtering and grouping costs by
location, specifically geography (such as _Americas_ ), multi-region (such as
_US_ ), or region (such as _us-east1_ ). See the [ documentation
](https://cloud.google.com/billing/docs/how-to/reports#filtering_and_grouping)
for more details. Learn more about [ Cloud locations
](https://cloud.google.com/about/locations/) .

##  April 01, 2019

**CHANGED:**

Cost forecasts in the Cloud Billing reports now includes both your long term
cost trend as well as any consistent monthly cycles such as sustained use
discounts. Including monthly cycles in your cost forecast makes it easier to
see at a glance how how much you are projected to spend by the end of the
month. See the [ documentation ](https://cloud.google.com/billing/docs/how-
to/reports#cost-forecast) for more details.

##  March 14, 2019

**FEATURE:**

Budget alerts against forecasted costs: You can now configure budget alerts
for when your costs are forecasted to exceed your budget. For each budget you
have configured, you can set multiple budget alert threshold rules, triggered
against either actual costs or forecasted costs, so you can stay informed of
how your spend is tracking against your budget and avoid billing surprises.
See the [ documentation ](https://cloud.google.com/billing/docs/how-
to/budgets) for more details.

##  February 04, 2019

**FEATURE:**

Cloud Billing reports now support detailed credit types in the report
settings.

Previously, costs were reported as cost before credits, credits, and cost
after credits. The credit amount displayed was a sum of all possible credit
types.

With this launch, you can now see what types of credits (discounts,
promotions, etc.) comprise the credit amount displayed in the report. In the
report settings, you can toggle on and off the different types of credits to
customize your report views. See the [ billing reports documentation
](https://cloud.google.com/billing/docs/how-to/reports#credits) for details.

##  December 13, 2018

**FEATURE:**

**Complete Billing Record in Export** : Starting with your January 2019
invoice (issued in early February 2019) you can reconcile your Cloud Billing
export to BigQuery to your invoice, to the penny. The export now includes a `
cost_type ` field to identify regular, tax, adjustment, and rounding error
costs. See the [ documentation ](https://cloud.google.com/billing/docs/how-
to/export-data-bigquery#billing_data_in) and [ example queries
](https://cloud.google.com/billing/docs/how-to/bq-examples) for more details.

**Folders in Export** : Cloud Billing export to BigQuery now includes the
folder(s) and organization (if applicable) that a project belongs to (its
project ancestry). This helps you do things like query costs by folder. See
the [ documentation ](https://cloud.google.com/billing/docs/how-to/export-
data-bigquery#project_ancestry) for more details about `
project.ancestry_numbers ` .

##  November 30, 2018

**FEATURE:**

Cloud Billing reports now support a bar chart view. See the [ billing reports
documentation ](https://cloud.google.com/billing/docs/how-to/reports#bar-
chart) for details.

##  September 17, 2018

**FEATURE:**

Cloud Billing export to BigQuery now includes additional location and system
label fields to let you examine your cost data in more granular detail.
Location details allow you to view your costs in each GCP region and zone,
where supported by the service. System labels allow you to segment your costs
by virtual machine type, number of cores, or amount of RAM. The [ `
compute.googleapis.com/machine_spec `
](https://cloud.google.com/billing/docs/how-to/export-data-
bigquery#available_system_labels) system label should now be used in place of
` sku.description ` to query costs by virtual machine family and geometry. See
the [ documentation ](https://cloud.google.com/billing/docs/how-to/export-
data-bigquery#system_labels) for more details about the new fields.

##  August 06, 2018

**FEATURE:**

A new Cloud Billing IAM permission is now available that gives you finer
control over what cost data your users can see. You can now use [ `
billing.resourceCosts.get ` ](https://cloud.google.com/billing/docs/how-
to/billing-access) to grant project-specific access to cost data like [
billing reports ](https://cloud.google.com/billing/docs/how-to/reports) . The
new permission was added on 08-6, 2018. To give you time to set up your users
with the correct permissions, the new permission will not be enforced until
08-20, 2018. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/billing-access) for more
details.

##  July 09, 2018

**FEATURE:**

Cost forecasts are now available as a GA feature in Cloud Billing reports.
Cost forecasts make it easier to see at a glance how your costs are trending
and how much you are projected to spend. See the [ blog
](https://cloudplatform.googleblog.com/2018/07/predict-your-future-costs-with-
google-cloud-billing-cost-forecast.html) and [ documentation
](https://cloud.google.com/billing/docs/how-to/reports#cost-forecast) for more
details.

##  May 31, 2018

**FEATURE:**

Cloud Billing export to BigQuery now includes the invoice month ( `
invoice.month ` ) that the cost line item appears on. See the [ export schema
documentation ](https://cloud.google.com/billing/docs/how-to/export-data-
bigquery#billing_data_in) and [ example queries
](https://cloud.google.com/billing/docs/how-to/bq-examples) for more details.

##  May 22, 2018

**FEATURE:**

Cloud Billing programmatic notifications for budget alerts is now available in
GA. You can configure programmatic notifications to receive Cloud Pub/Sub
messages about the current status of your budget. See the [ blog
](https://cloudplatform.googleblog.com/2018/05/Better-cost-control-with-
Google-Cloud-Billing-programmatic-notifications.html) and [ documentation
](https://cloud.google.com/billing/docs/how-to/budgets#manage-notifications)
for more details.

##  April 24, 2018

**FEATURE:**

Cloud Billing reports are now available in GA. Billing reports let you quickly
chart your billing account's cloud spending. See the [ blog
](https://cloudplatform.googleblog.com/2018/03/understand-your-spending-at-a-
glance-with-Google-Cloud-Billing-reports-beta.html) and [ documentation
](https://cloud.google.com/billing/docs/how-to/reports) for more details.

##  March 30, 2018

**FEATURE:**

Cloud Billing programmatic notifications for budget alerts is now available in
Beta. You can configure programmatic notifications to receive Cloud Pub/Sub
messages about the current status of your budget. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/budgets#manage-notifications)
for more details.

##  March 20, 2018

**FEATURE:**

Cloud Billing reports are now available in Beta. Billing reports let you
quickly chart your billing account's cloud spending. See the [ blog
](https://cloudplatform.googleblog.com/2018/03/understand-your-spending-at-a-
glance-with-Google-Cloud-Billing-reports-beta.html) and [ documentation
](https://cloud.google.com/billing/docs/how-to/reports) for more details.

##  February 27, 2018

**FEATURE:**

The Cloud Billing Catalog API is now available in GA. The Catalog API offers
programmatic access to pricing metadata on [ Cloud Platform SKUs
](https://cloud.google.com/skus) . See the [ blog
](https://cloudplatform.googleblog.com/2018/02/introducing-Cloud-Billing-
Catalog-API-GCP-pricing-in-real-time.html) and [ documentation
](https://cloud.google.com/billing/v1/how-tos/catalog-api) for more details.

##  November 15, 2017

**FEATURE:**

Cloud Billing export to BigQuery is now available in GA. BigQuery billing
export regularly publishes new SKU usage and cost data to your BigQuery
dataset. You can write SQL queries to understand your spending and use the
BigQuery dataset to drive visualization tools like [ Data Studio
](https://cloud.google.com/data-studio/) . See the [ blog
](https://cloudplatform.googleblog.com/2017/11/monitor-and-manage-your-costs-
with.html) and [ documentation ](https://cloud.google.com/billing/docs/how-
to/export-data-bigquery) for more details.

