#  Release Notes

This page contains release notes for Deployment Manager.

**Current Version: v2**

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/deploymentmanager-release-
notes.xml `

##  March 30, 2020

**CHANGED:**

If your Python templates use features that are only for Python 2.x, your
templates will now continue to work until **June 2020** .

Learn about [ migrating your templates to Python 3
](https://cloud.google.com/deployment-manager/docs/migrate-to-python3) .

##  December 05, 2019

**CHANGED:**

Deployment Manager now supports templates written in Python 3.

The Python community announced that it will [ sunset Python 2
](https://www.python.org/doc/sunset-python-2/) on January 1, 2020, and is
encouraging all developers to upgrade to Python 3 as soon as they can.

We recommend that you make sure that your Python templates are [ compatible
with Python 3 ](https://cloud.google.com/deployment-manager/docs/migrate-to-
python3) as soon as possible.

##  November 26, 2019

**CHANGED:**

When you're creating your deployments, we recommend using the production-ready
templates from the [ Cloud Foundation Toolkit
](https://cloud.google.com/foundation-toolkit/) . The templates use Google
Cloud's best practices for managing resources.

[ See the list of sample templates ](https://cloud.google.com/deployment-
manager/docs/reference/cloud-foundation-toolkit) .

##  October 02, 2019

**FEATURE:**

You can now use the ` gcp-types/compute-v1:externalVpnGateways ` type to
create [ Compute Engine v1 ExternalVpnGateway resources
](https://cloud.google.com/compute/docs/reference/rest/v1/externalVpnGateways)
.

**FEATURE:**

You can now use the ` gcp-types/compute-v1:vpnGateways ` type to create [
Compute Engine v1 VpnGateway resources
](https://cloud.google.com/compute/docs/reference/rest/v1/vpnGateways) .

##  September 30, 2019

**CHANGED:**

The [ walkthrough of Deployment Manager's best practices
](https://cloud.google.com/deployment-manager/docs/step-by-step-guide/) has
been updated, with an optional interactive version that runs in Cloud Shell.

Try the interactive version here:

[ Open in Cloud Shell
](https://console.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2FGoogleCloudPlatform%2Fdeploymentmanager-
samples&cloudshell_tutorial=walkthroughtutorial.md)

##  July 01, 2019

**FEATURE:**

You can now use the ` gcp-types/cloudresourcemanager-v1 ` type provider to
create IAM mappings for projects and organizations.

For a list of supported type providers, see [ Supported GCP type providers
](https://cloud.google.com/deployment-manager/docs/configuration/supported-
gcp-types) .

##  June 03, 2019

**CHANGED:**

In type providers, the input mappings for header fields are now applied to
getting long-running operations.

For information on creating custom type providers, read the [ guidelines for
creating a type provider ](https://cloud.google.com/deployment-
manager/docs/configuration/type-providers/process-adding-api) .

**FEATURE:**

You can now use Deployment Manager to update labels for Cloud Pub/Sub
resources.

##  May 28, 2019

**CHANGED:**

If you are using the Deployment Manager API, read the [ guidelines for
managing long-running operations ](https://cloud.google.com/deployment-
manager/docs/reference/managing-long-running-operations) .

##  February 27, 2019

**FEATURE:**

Deployment Manager templates can be used in [ Private Catalog
](https://cloud.google.com/private-catalog) .

**FEATURE:**

Added support for Redis v1 API using the type-provider ` gcp-types/redis-v1 `
.

##  November 21, 2018

**FEATURE:**

Added a new template environment variable, ` username ` , which you can use in
Python templates using ` context.env["username"] ` , and in Jinja templates
using ` env["username"] ` .

For information on using environment variables in templates, see [ Using
environment variables ](https://cloud.google.com/deployment-
manager/docs/configuration/templates/use-environment-variables) .

**FEATURE:**

Added support for Cloud DNS v1 RecordSets using the type-provider ` gcp-
types/dns-v1:resourceRecordSets ` .

**FEATURE:**

Added support for Access Context Manager v1beta using the type provider ` gcp-
types/accesscontextmanager-v1beta ` .

For a list of supported type providers, see [ Supported GCP type providers
](https://cloud.google.com/deployment-manager/docs/configuration/supported-
gcp-types) .

##  September 12, 2018

**FEATURE:**

Expanded support for creating and acquiring project folders using the type-
provider ` gcp-types/cloudresourcemanager-v2:folders ` .

For a list of supported type providers, see [ Supported GCP type providers
](https://cloud.google.com/deployment-manager/docs/configuration/supported-
gcp-types) .

##  August 07, 2018

**FEATURE:**

Added glob import support to ` gcloud ` . You can import templates using
wildcards in template paths.

For the syntax to enable glob imports, see the [ SDK release notes
](https://cloud.google.com/sdk/docs/release-notes) .

##  July 03, 2018

**FEATURE:**

When you are creating or updating deployments, you can select a ` CREATE `
policy for new resources. This ensures that if a resource you are trying to
create already exists in the project, the deployment fails.

For information on policies for creating resources, see [ Setting policies for
creating resources ](https://cloud.google.com/deployment-
manager/docs/deployments/#create-policy) .

##  April 24, 2018

**DEPRECATED:**

The ` appengine.v1beta4 ` and ` appengine.v1beta5 ` resource types are no
longer supported.

**FEATURE:**

Updated the ` gcloud ` tool so that you can create deployments directly with [
composite types ](https://cloud.google.com/deployment-
manager/docs/configuration/templates/create-composite-
types#compositetypepropertiescommandline) . Also added new ` --template ` flag
to support [ creating deployments with templates
](https://cloud.google.com/deployment-
manager/docs/configuration/templates/define-template-
properties#templatepropertiescommandline) .

##  July 24, 2017

**FEATURE:**

Added support for [ labels on deployments
](https://cloud.google.com/deployment-manager/docs/deployments/add-labels-
deployments) .

##  April 20, 2017

**FEATURE:**

Added new ` returnValues ` query parameter for the [ ` variables().list `
](https://cloud.google.com/deployment-manager/runtime-
configurator/reference/rest/v1beta1/projects.configs.variables/list) method to
return values for variables that the caller has ` runtimeconfig.variables.get
` permission on.

##  April 12, 2017

**FEATURE:**

Added new [ ` project_number ` environment variable
](https://cloud.google.com/deployment-manager/docs/configuration/adding-
templates#environment_variables) .

##  March 27, 2017

**FEATURE:**

Added new Type Registry feature that allows users to add [ composite types
](https://cloud.google.com/deployment-
manager/docs/fundamentals#composite_types) and add third-party APIs as [ type
providers ](https://cloud.google.com/deployment-
manager/docs/fundamentals#basetypes) . This feature is in **Beta** .

##  February 23, 2017

**FEATURE:**

[ Runtime Configurator ](https://cloud.google.com/deployment-manager/runtime-
configurator) updates: * Converted ` gcloud ` commands so that the command
group is now under ` runtime-config ` * Updated ` gcloud ` commands to the `
gcloud beta ` component.

##  January 27, 2017

**FEATURE:**

Added support to the ` gcloud ` command-line tool for creating [ plaintext
variable values ](https://cloud.google.com/deployment-manager/runtime-
configurator/set-and-get-variables) .

##  January 11, 2017

**FEATURE:**

Updated ` gcloud ` command-line tool syntax so that the ` --properties ` flag
now accepts ` key:value ` pairs. The old syntax, ` key=value ` , will still
work but users should transition to using the new syntax. For more
information, read [ Specifying template properties on the command-line
](https://cloud.google.com/deployment-manager/docs/configuration/adding-
templates#specifying_template_properties_on_the_command-line) .

##  November 20, 2016

**FEATURE:**

Added documentation on configuring Deployment Manager to [ use images from
another project ](https://cloud.google.com/deployment-
manager/docs/configuration/using-images-from-other-projects-for-vm-instances)
.

##  November 01, 2016

**FEATURE:**

[ Runtime Configurator ](https://cloud.google.com/deployment-manager/runtime-
configurator) updates:

  * Added support for [ plaintext variable values ](https://cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables) when creating a variable in the API. This is not yet supported with the ` gcloud ` command-line tool. 
  * Added optional [ ` requestId ` ](https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/create) field for ` create() ` requests to ensure that requests are unique. 

##  October 06, 2016

**FEATURE:**

Added support for specifying IAM policies in your configurations. Read the [
documentation ](https://cloud.google.com/deployment-
manager/docs/configuration/create-configuration-
file#setting_access_control_for_resources_in_a_deployment) for more
information.

##  September 28, 2016

**CHANGED:**

Published a [ Syntax Reference ](https://cloud.google.com/deployment-
manager/docs/configuration/syntax-reference) that describes the syntax of
Deployment Manager.

##  August 26, 2016

**FEATURE:**

Added support for predefined Deployment Manager [ IAM roles
](https://cloud.google.com/deployment-manager/docs/access-
control#predefined_roles) in **Beta** .

##  August 25, 2016

**FEATURE:**

Updated [ resource quotas ](https://cloud.google.com/deployment-
manager/pricing-and-quotas) for [ Runtime Configurator
](https://cloud.google.com/deployment-manager/runtime-configurator) so that it
is now based on amount of data per user instead of the number of resources.
The default quota is 4 MB of data per user. Also, updated quota for API
requests.

**FEATURE:**

Removed the 4 KB limit on variable values for Runtime Configurator.

##  May 10, 2016

**FEATURE:**

Added support for hosting templates externally on Google Cloud Storage or on
another publicly-accessible URL. Read [ Hosting Templates Externally
](https://cloud.google.com/deployment-manager/docs/configuration/hosting-
templates-externally) for more information.

##  February 29, 2016

**FEATURE:**

Added support for [ outputs ](https://cloud.google.com/deployment-
manager/docs/configuration/expose-information-outputs) so you can expose key
properties of your configuration for others to use.

##  November 13, 2015

**FEATURE:**

Added support for [ schemas ](https://cloud.google.com/deployment-
manager/docs/configuration/using-schemas) that allow you to define rules for
using templates. Read [ Using Schemas ](https://cloud.google.com/deployment-
manager/docs/configuration/using-schemas) for more information.

##  November 04, 2015

**DEPRECATED:**

Removed support for ` cluster.v1beta1.cluster ` resource type since Container
Engine v1beta1 API is now [ deprecated ](https://cloud.google.com/kubernetes-
engine/docs/release-notes#july_24_2015) .

**FEATURE:**

Added support for new ` cluster.v1.cluster ` resource type.

##  July 22, 2015

**FEATURE:**

**Launched Deployment Manager into General Availability with v2 API!**

Deployment Manager is now generally available for all users and projects. We
have also:

  * Added new intermediate guide 
  * Updated the navigation structure 

For more information, see the new [ Step-by-step guide
](https://cloud.google.com/deployment-manager/docs/step-by-step-guide/) .

**DEPRECATED:**

Removed ` PATCH ` as possible update policy for the API.

**FEATURE:**

Added new custom methods, ` stop ` and ` cancelPreview ` , to the API.

**DEPRECATED:**

Removed ` intent ` and ` state ` properties from Deployment resources.

**FEATURE:**

Added new boolean ` preview ` query parameter to the API; to preview
deployments, use the query parameter.

**FEATURE:**

Added new ` fingerprint ` requirements to the API, for updating, canceling, or
stopping a deployment.

**CHANGED:**

Updated API error codes.

**FEATURE:**

Refreshed API manifest structure so that templates are now explicitly shown in
the new ` imports ` section of the manifest file.

See [ Updating a Deployment ](https://cloud.google.com/deployment-
manager/docs/deployments/updating-deployments) and [ Viewing a Manifest
](https://cloud.google.com/deployment-manager/docs/deployments/viewing-
manifest) for more information.

**DEPRECATED:**

Removed ` --update-policy ` flag because ` PATCH ` is no longer supported.

**FEATURE:**

Replaced ` deployments cancel ` subcommand with new ` cancel-preview ` and `
stop ` subcommands.

##  July 13, 2015

**FEATURE:**

Updated quota limits so that **delete** and **read requests** are now
unlimited. See [ Quotas ](https://cloud.google.com/deployment-manager/pricing-
and-quotas) for more information.

##  June 18, 2015

**CHANGED:**

Changed ` creationTimestamp ` field to ` insertTime ` .

**FEATURE:**

Added new field called ` updateTime ` .

##  April 30, 2015

**FEATURE:**

Launched Deployment Manager into **Beta** ! Also, launched new [ v2beta2
](https://cloud.google.com/deployment-manager/docs/reference/latest/) API that
includes a number of new and improved features, including server-side
expansion, manifest layouts, update capabilities, and more. See the [
migration guide ](https://cloud.google.com/deployment-
manager/docs/reference/latest/migration-guide) for more information.

##  February 20, 2015

**DEPRECATED:**

Disabled support for external references due to a known bug.

##  February 06, 2015

**FEATURE:**

Added support for [ external references ](https://cloud.google.com/deployment-
manager/docs/configuration-files#external_references) .

##  January 21, 2015

**FEATURE:**

  * Added new Google Container Engine cluster type, ` container.v1beta1.cluster ` that allows you to declare and deploy new Google Container Engine Clusters. 

**FEATURE:**

2015-01-21

FEATURE * Added new tutorial for [ creating a HTTP load-balanced deployment
](https://cloud.google.com/deployment-manager/docs/create-advanced-http-load-
balanced-deployment) .

