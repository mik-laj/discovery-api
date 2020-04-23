#  Release notes

This page documents production updates to Binary Authorization. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/binary-auth-release-notes.xml `

##  March 04, 2020

**DEPRECATED:**

Support for the Binary Authorization Beta API was discontinued on September
16, 2019. As a result, **the Binary Authorization Beta API will stop working
after March 16, 2020.** To prevent service interruption, you must take actions
outlined in the [ Binary Authorization GA Migration Guide
](https://cloud.google.com/binary-authorization/docs/ga-migration-guide) prior
to that date.

##  September 16, 2019

**FEATURE:**

The General Availability (GA) version of Binary Authorization is a feature of
the [ Anthos platform ](https://cloud.google.com/anthos/) . Use of Binary
Authorization is included in the Anthos subscription. Please [ contact
](https://cloud.google.com/anthos/pricing) your sales representative to enroll
in Anthos.

##  April 03, 2019

**FEATURE:**

Binary Authorization now supports asymmetric PKIX key pairs to verify the
identity of attestors. The asymmetric key pairs generated and stored in Cloud
Key Management Service are compliant with the PKIX format. You set up PKIX
keys when you create an attestor using the [ Google Cloud Platform Console
](https://cloud.google.com/binary-authorization/docs/creating-attestors-
console) or the [ CLI ](https://cloud.google.com/binary-
authorization/docs/creating-attestors-cli) .

**FEATURE:**

Binary Authorization now supports [ global policy evaluation mode
](https://cloud.google.com/binary-authorization/docs/key-
concepts#global_policy_evaluation_mode) .

**FEATURE:**

Binary Authorization now supports dryrun mode.

Dryrun mode is a policy setting that allows non-conformant images to be
deployed, but writes details about the policy violation and deployment to the
audit log. Dryrun mode allows you to test a policy in your production
environment before it goes into effect.

You can enable dryrun mode when you configure your policy using the [ Google
Cloud Platform Console ](https://cloud.google.com/binary-
authorization/docs/configuring-policy-console) or the [ CLI
](https://cloud.google.com/binary-authorization/docs/configuring-policy-cli) .

##  July 25, 2018

**ISSUE:**

Default whitelisting of exempt images may be incomplete, depending on the
version of Kubernetes you are deploying to. You may need to add `
gcr.io/google-containers/ ` and ` k8s.io/ ` to the default whitelist.

**ISSUE:**

Error messaging sometimes lacks detail when policies are updated. If you
encounter an error when you update a policy, check the names of any attestor
resources defined to make sure they are correct.

**ISSUE:**

When editing a policy in the UI, you cannot remove/edit existing cluster
specific deployment rules. This is possible using ` gcloud ` commands and the
REST API.

**ISSUE:**

In the UI, you cannot manage the IAM Policy on an Attestor or Binary
Authorization Policy. Project level IAM permissions work as expected.

**ISSUE:**

In the UI, detailed error messages are not shown for invalid whitelist
patterns on a Policy or invalid PGP keys on an Attestor.

