#  Release notes

This page documents production updates to Cloud Build. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/cloudbuild-release-notes.xml `

##  June 12, 2020

**CHANGED:**

Upgraded to Docker server version 19.03.8.

##  March 12, 2020

**FEATURE:**

The [ Create trigger ](https://console.cloud.google.com/cloud-build/triggers)
page on the Cloud Console has been updated. To learn more about creating build
triggers, see [ Creating and managing triggers
](https://cloud.google.com/cloud-build/docs/running-builds/create-manage-
triggers) .

##  February 06, 2020

**FEATURE:**

[ GitHub App triggers ](https://cloud.google.com/cloud-build/docs/create-
github-app-triggers) is now Generally Available.

**FEATURE:**

The [ Cloud Build Dashboard ](https://console.cloud.google.com/cloud-
build/dashboard) , which provides a high-level overview of recent builds for
build triggers, is now Generally Available. For information about the
Dashboard, see [ Viewing the Dashboard ](https://cloud.google.com/cloud-
build/docs/view-build-results#viewing_the_dashboard) .

##  January 30, 2020

**FEATURE:**

The [ Build history ](/release-notes/console.google.com/cloud-build/builds)
page and Build details page in the Google Cloud Platform Console are updated.

##  December 13, 2019

**FEATURE:**

Closing pull requests will now cancel running builds in pull requests
associated with [ GitHub App triggers ](https://cloud.google.com/cloud-
build/docs/create-github-app-triggers) .

##  September 26, 2019

**FEATURE:**

[ GitHub App triggers ](https://cloud.google.com/cloud-build/docs/create-
github-app-triggers) Beta is now released. New [ substitution variable values
](https://cloud.google.com/cloud-build/docs/configuring-builds/substitute-
variable-values#using_default_substitutions) are now available for GitHub pull
requests.

**FEATURE:**

Users can now create build triggers to start builds on [ GitHub pull requests
](https://console.cloud.google.com/cloud-build/triggers/add) .

**FEATURE:**

GitHub App trigger results are posted to GitHub via the GitHub Checks API.

##  August 29, 2019

**FEATURE:**

Added a new [ Cloud Build Settings ](https://console.cloud.google.com/cloud-
build/settings) page in the GCP Console for managing service account
permissions.

**FEATURE:**

[ CI/CD developer hub ](https://cloud.google.com/docs/ci-cd/) is now
available.

##  July 12, 2019

**CHANGED:**

Exposed the quota for concurrent builds in the GCP Console [ Quotas
](https://console.cloud.google.com/iam-
admin/quotas?service=cloudbuild.googleapis.com%22) page.

This also allows projects to lower the number of concurrent builds that can be
run at one time, or request a higher limit from the GCP Console.

##  June 27, 2019

**FEATURE:**

Environment variables can now be [ defined globally
](https://cloud.google.com/cloud-build/docs/build-config) for all build steps
in a build.

##  June 20, 2019

**FEATURE:**

Cloud Build now provides [ Customer-Managed Encryption Keys (CMEK) compliance
](https://cloud.google.com/cloud-build/docs/securing-builds/cmek) .

##  June 19, 2019

**FEATURE:**

[ ` gke-deploy ` builder ](https://github.com/GoogleCloudPlatform/cloud-
builders/tree/master/gke-deploy) is now available.

##  May 27, 2019

**FEATURE:**

[ Build triggers ](https://cloud.google.com/cloud-build/docs/running-
builds/automate-builds) with inverted regex can now be run in specified
branches.

##  May 20, 2019

**CHANGED:**

Upgraded to Docker server version 18.09.3.

##  March 08, 2019

**FEATURE:**

Users interested in Cloud Build Alpha features can join the [ Alpha Features
group ](https://forms.gle/wf1KyQdJwGJY4eee7) .

##  February 12, 2019

**FEATURE:**

Repository to project mapping is now available in the [ Google Cloud Build
GitHub app ](https://github.com/marketplace/google-cloud-build) .

##  January 09, 2019

**CHANGED:**

Upgraded to Docker version 18.09.0.

##  October 18, 2018

**CHANGED:**

Upgraded to Docker version 18.06.1.

##  July 24, 2018

**FEATURE:**

  * Container Builder is now named Cloud Build. 
  * Added a new top-level menu for [ Cloud Build ](http://console.cloud.google.com/cloud-build) in the GCP Console. 
  * The ` gcloud ` commands for Cloud Build are updated to ` gcloud builds ... ` . 
  * Added [ support for storing non-container artifacts ](https://cloud.google.com/cloud-build/docs/configuring-builds/store-images-artifacts) to a Cloud Storage bucket. 
  * Added support for providing [ filepath filters ](https://cloud.google.com/cloud-build/docs/running-builds/automate-builds) to trigger a build only on changes to the specified files or subdirectories. 
  * Added a new [ Google Cloud Build GitHub app ](https://cloud.google.com/cloud-build/docs/run-builds-on-github) . 

##  March 06, 2018

**CHANGED:**

Upgraded to Docker version 17.12.0.

##  February 28, 2018

**FEATURE:**

Cloud Build provides [ ` timeout ` and ` status `
](https://cloud.google.com/cloud-build/docs/view-build-results) for build
steps.

##  January 10, 2018

**FEATURE:**

Added support for [ ` gcloudignore `
](https://cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) .

##  November 02, 2017

**FEATURE:**

[ Community-contributed build steps
](https://github.com/GoogleCloudPlatform/cloud-builders-community) released.

##  October 28, 2017

**FEATURE:**

[ Cloud Build plugin for Jenkins ](https://plugins.jenkins.io/google-
cloudbuild) is now available.

##  October 25, 2017

**FEATURE:**

  * Lowered per-minute pricing for the default n1-standard-1 machine from $0.0034 to $0.003. 
  * Added [ two new machine types with 8 CPU and 32 CPU ](https://cloud.google.com/cloud-build/docs/api/reference/rest/v1/projects.builds#machinetype) . 
  * Added an option to select a [ custom disk size ](https://cloud.google.com/cloud-build/docs/api/reference/rest/v1/projects.builds#buildoptions) . 

For more information, see the [ Pricing ](https://cloud.google.com/cloud-
build/pricing) documentation.

##  October 10, 2017

**CHANGED:**

Builds are not triggered if the commit message includes ` [skip ci] ` or ` [ci
skip] ` .

##  August 28, 2017

**CHANGED:**

Upgraded to Docker version 17.06.1.

##  August 23, 2017

**CHANGED:**

Builds accept ` secrets ` and build steps accept ` secretEnv ` to specify
environment variables with values that have been encrypted using [ Cloud KMS
](https://cloud.google.com/kms/) .

See [ Encrypting an Environment Variable Using the CryptoKey
](https://cloud.google.com/cloud-build/docs/securing-builds/use-encrypted-
secrets-credentials#encrypting_an_environment_variable_using_the_cryptokey) .

##  August 03, 2017

**FEATURE:**

Build steps accept ` volumes ` to persist specified paths across build steps.

##  July 26, 2017

**FEATURE:**

` cloud-build-local ` , a tool for running builds locally, is available. You
can install the tool using ` gcloud components install cloud-build-local ` .

To learn more, see [ Running builds locally ](https://cloud.google.com/cloud-
build/docs/concepts/overview#running_builds_locally) .

##  July 18, 2017

**FEATURE:**

` gradle ` is now a [ supported build step
](https://github.com/GoogleCloudPlatform/cloud-
builders/tree/master/java/gradle) .

##  July 10, 2017

**FEATURE:**

` homevol ` mounted across build steps as ` $HOME ` directory.

##  June 15, 2017

**FEATURE:**

` kubectl ` is now [ supported build step
](https://github.com/GoogleCloudPlatform/cloud-builders/tree/master/kubectl) .

##  June 07, 2017

**FEATURE:**

Expanded [ builder service account permissions
](https://cloud.google.com/cloud-build/docs/how-to/service-account-
permissions) to empower end-user and IAM-based control over builder robot
permissions, thereby enabling ` gcloud app deploy ` , ` kubectl ` , and other
permissioned APIs to be called as part of a build.

##  May 27, 2017

**CHANGED:**

Upgraded to Docker version 17.05.

##  March 06, 2017

**FEATURE:**

**General availability** of user interface in Google Cloud Platform Console,
including [ build history ](https://console.cloud.google.com/gcr/builds) menu.

**Beta release** of [ build triggers
](https://console.cloud.google.com/gcr/builds) .

##  January 23, 2017

**CHANGED:**

Upgraded to Docker version 1.12.6.

##  December 15, 2016

**FEATURE:**

**General availability** of Cloud Build API.

[ Supported build steps ](https://github.com/GoogleCloudPlatform/cloud-
builders) released.

##  November 23, 2016

**FEATURE:**

**General availability** of [ Cloud SDK CLI
](https://cloud.google.com/sdk/gcloud/reference/builds/) to Cloud Build.

##  November 02, 2016

**FEATURE:**

**Beta release** of [ Cloud SDK CLI
](https://cloud.google.com/sdk/gcloud/reference/builds/) to Cloud Build.

##  August 22, 2016

**CHANGED:**

Upgraded to Docker version 1.9.1.

##  July 20, 2016

**FEATURE:**

**Alpha release** of [ Cloud SDK CLI
](https://cloud.google.com//sdk/gcloud/reference/builds/) to Cloud Build.

##  January 14, 2016

**FEATURE:**

**Beta release** of Cloud Build.

