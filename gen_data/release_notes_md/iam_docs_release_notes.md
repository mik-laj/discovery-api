#  Release notes

This page documents production updates to Identity and Access Management.
Check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

**Note:** To learn about changes to the IAM permissions for each Google Cloud
service, see the [ permissions change log ](/iam/docs/permissions-change-log)
.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/iam-release-notes.xml `

##  July 01, 2020

**CHANGED:**

The organization policy constraint to [ prevent automatic role grants to Cloud
IAM service accounts ](https://cloud.google.com/resource-
manager/docs/organization-policy/restricting-service-
accounts#disable_service_account_default_grants) is now [ generally available
](https://cloud.google.com/products/#product-launch-stages) . To improve
security, we strongly recommend that you enable this constraint.

**CHANGED:**

Starting on July 27, 2020, IAM policies will identify deleted members that are
bound to a role. Deleted members have the prefix ` deleted: ` and the suffix `
?uid=  numeric-id  ` .

For example, if you delete the account for the user ` tamika@example.com ` ,
and a policy binds that user to a role, the policy shows an identifier similar
to ` deleted:user:tamika@example.com?uid=123456789012345678901 ` .

For ` SetIamPolicy ` requests, you can use this new syntax starting on July
27. For ` GetIamPolicy ` and ` SetIamPolicy ` responses, you might see the new
prefix and suffix in some, but not all, responses until we finish rolling out
the change. We expect to complete the rollout by July 31, 2020.

See the documentation for a [ detailed example
](https://cloud.google.com/iam/docs/policies#example-deleted-member) , as well
as guidance on [ updating policies that contain deleted members
](https://cloud.google.com/iam/docs/policies#handle-deleted-members) .

**ISSUE:**

Starting on July 27, 2020, if a binding in a policy refers to a deleted member
(for example, ` deleted:user:tamika@example.com?uid=123456789012345678901 ` ),
you cannot add a binding for a newly created member with the same name (in
this case, ` user:tamika@example.com ` ). If you try to add a binding for the
newly created member, IAM will apply the binding to the deleted member
instead.

To resolve this issue, see our guidance on [ updating policies that contain
deleted members ](https://cloud.google.com/iam/docs/policies#handle-deleted-
members) .

##  June 22, 2020

**DEPRECATED:**

Using the Cloud IAM API to sign JSON Web Tokens (JWTs) or binary blobs is now
deprecated.

  * If you use the Cloud IAM API or its client libraries to sign JWTs or binary blobs, you must [ migrate to the Service Account Credentials API ](https://cloud.google.com/iam/docs/migrating-to-credentials-api) before July 1, 2021. 
  * If you use the ` gcloud ` command-line tool to sign JWTs, you must [ prepare for changes to the ` gcloud ` tool ](https://cloud.google.com/iam/docs/migrating-to-credentials-api#gcloud) before July 1, 2021. 

##  May 18, 2020

**CHANGED:**

Recommendations from the [ Cloud IAM recommender
](https://cloud.google.com/iam/docs/recommender-overview) can now include [
suggestions to create custom roles
](https://cloud.google.com/iam/docs/recommender-overview#custom-roles) .

##  April 01, 2020

**FEATURE:**

When you [ use a service account key to access Google Cloud
](https://cloud.google.com/iam/docs/audit-logging/examples-service-
accounts#auth-service-account-key) , your audit logs now identify the key that
was used.

##  March 17, 2020

**CHANGED:**

[ Forwarding rule attributes ](https://cloud.google.com/iam/docs/conditions-
attribute-reference#forwarding-rule) for Cloud IAM Conditions are now [
generally available ](https://cloud.google.com/products/#product-launch-
stages) . You can use these attributes to specify the types of [ forwarding
rules ](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts)
that a member can create.

##  March 05, 2020

**FEATURE:**

For Cloud Storage buckets, you can now use [ Credential Access Boundaries
](https://cloud.google.com/iam/docs/downscoping-short-lived-credentials) ,
currently in beta, to downscope the permissions that a short-lived credential
can use.

##  February 28, 2020

**CHANGED:**

[ Cloud IAM Conditions ](https://cloud.google.com/iam/docs/conditions-
overview) are now [ generally available
](https://cloud.google.com/products/#product-launch-stages) . You can use
Cloud IAM Conditions to define and enforce conditional, attribute-based access
control for Google Cloud resources.

**FEATURE:**

For Cloud IAM Conditions, you can now use the ` extract() ` function to [
extract a value from a resource name
](https://cloud.google.com/iam/docs/conditions-attribute-reference#extract) .
This function enables condition expressions to refer to an arbitrary part of
the resource name.

##  February 21, 2020

**CHANGED:**

A version 1 [ Cloud IAM policy ](https://cloud.google.com/iam/docs/policies)
can now include [ conditional role bindings
](https://cloud.google.com/iam/docs/conditions-overview) . The role name in
these bindings includes the string ` withcond ` , followed by a hash value.
For example: ` roles/iam.serviceAccountAdmin_withcond_2b17cc25d2cd9e2c54d8 `

If you see the string ` withcond ` in a Cloud IAM policy, follow the steps in
the [ troubleshooting guide
](https://cloud.google.com/iam/docs/troubleshooting-withcond) .

##  February 18, 2020

**CHANGED:**

You can now learn about [ Cloud IAM audit logging for service accounts
](https://cloud.google.com/iam/docs/audit-logging/) and see [ examples of
audit logs for service accounts ](https://cloud.google.com/iam/docs/audit-
logging/examples-service-accounts) .

##  February 13, 2020

**CHANGED:**

The [ Cloud IAM recommender ](https://cloud.google.com/iam/docs/recommender-
overview) is now [ generally available
](https://cloud.google.com/products/#product-launch-stages) . The Cloud IAM
recommender helps you enforce the principle of least privilege by ensuring
that members have only the permissions that they actually use.

##  February 04, 2020

**FEATURE:**

Cloud IAM Conditions now supports [ forwarding rule attributes
](https://cloud.google.com/iam/docs/conditions-attribute-reference#forwarding-
rule) , currently in beta. You can use these attributes to specify the types
of [ forwarding rules ](https://cloud.google.com/load-
balancing/docs/forwarding-rule-concepts) that a member can create.

##  December 17, 2019

**CHANGED:**

[ Policy Troubleshooter ](https://cloud.google.com/iam/docs/troubleshooting-
access) is now [ generally available
](https://cloud.google.com/products/#product-launch-stages) . Use Policy
Troubleshooter to determine why a user has access to a resource or doesn't
have permission to call an API.

##  December 13, 2019

**CHANGED:**

On December 9, we [ announced ](https://cloud.google.com/iam/docs/release-
notes#December_09_2019) that Cloud IAM policies would now identify deleted
members. We have temporarily reverted this change. Cloud IAM policies no
longer identify deleted members.

##  December 12, 2019

**FEATURE:**

[ Cloud IAM Conditions ](https://cloud.google.com/iam/docs/conditions-
overview) are now available in public beta. You can use Cloud IAM Conditions
to define and enforce conditional, attribute-based access control for Google
Cloud resources.

##  December 09, 2019

**CHANGED:**

Cloud IAM policies now identify deleted members that are bound to a role.
Deleted members have the prefix ` deleted: ` and the suffix ` ?uid=
[NUMERIC_ID]  ` .

For example, if you delete the account for the user ` bob@example.com ` , and
a policy binds that user to a role, the policy shows an identifier similar to
` deleted:user:bob@example.com?uid=123456789012345678901 ` .

For ` SetIamPolicy ` requests, you can use this new syntax starting today. For
` GetIamPolicy ` and ` SetIamPolicy ` responses, because we are still rolling
out this change, you might see the new prefix and suffix in some, but not all,
responses. We expect to complete the rollout by December 13, 2019.

**ISSUE:**

If a binding in a policy refers to a deleted member (for example, `
deleted:user:bob@example.com?uid=123456789012345678901 ` ), you cannot add a
binding for a newly created member with the same name (in this case, `
user:bob@example.com ` ). If you try to add a binding for the newly created
member, Cloud IAM will apply the binding to the deleted member instead.

##  September 23, 2019

**FEATURE:**

The [ Cloud IAM recommender ](https://cloud.google.com/iam/docs/recommender-
overview) is now available in beta. The Cloud IAM recommender helps you
enforce the principle of least privilege by ensuring that members have only
the permissions that they actually use.

##  September 18, 2019

**FEATURE:**

You can now [ upload a public key for a service account
](https://cloud.google.com/iam/docs/creating-managing-service-account-
keys#uploading) , which causes service account keys to be signed with that
public key. This feature is available in beta.

##  August 20, 2019

**CHANGED:**

The Service Account Credentials API is now [ generally available
](https://cloud.google.com/products/#product-launch-stages) . Use this API to
[ create short-lived service account credentials
](https://cloud.google.com/iam/docs/creating-short-lived-service-account-
credentials) .

##  March 28, 2019

**FEATURE:**

When you [ create ](https://cloud.google.com/iam/docs/creating-managing-
service-accounts#creating) or [ update
](https://cloud.google.com/iam/docs/creating-managing-service-
accounts#updating) a service account, you can now provide a description of the
service account.

##  June 29, 2018

**FEATURE:**

You can now [ create short-lived service account credentials
](https://cloud.google.com/iam/docs/creating-short-lived-service-account-
credentials) with the Service Account Credentials API, available in beta.

##  February 27, 2018

**CHANGED:**

You can now learn how to [ configure Cloud IAM roles to facilitate audit
logging ](https://cloud.google.com/iam/docs/roles-audit-logging) .

##  January 31, 2018

**CHANGED:**

[ Custom roles ](https://cloud.google.com/iam/docs/understanding-custom-roles)
are now [ generally available ](https://cloud.google.com/products/#product-
launch-stages) . You can create a custom Cloud IAM role with one or more
permissions, then grant that custom role to users in your organization.

For more information, see the following topics:

  * [ Understanding custom roles ](https://cloud.google.com/iam/docs/understanding-custom-roles)
  * [ Creating and managing custom roles ](https://cloud.google.com/iam/docs/creating-custom-roles)
  * [ Maintaining custom roles with Deployment Manager ](https://cloud.google.com/iam/docs/maintain-custom-roles-deployment-manager)
  * [ Support level for permissions in custom roles ](https://cloud.google.com/iam/docs/custom-roles-permissions-support)

##  September 27, 2017

**CHANGED:**

[ Custom roles ](https://cloud.google.com/iam/docs/understanding-custom-roles)
are now available in beta. You can create a custom Cloud IAM role with one or
more permissions, then grant that custom role to users in your organization.

##  September 14, 2017

**CHANGED:**

You can now refer to the [ IAM permissions change log
](https://cloud.google.com/iam/docs/permissions-change-log) to determine what
permissions have changed recently. Use this change log to help you maintain
and troubleshoot your custom roles.

##  July 06, 2017

**CHANGED:**

You can now learn how to configure [ IAM roles for networking-related job
functions ](https://cloud.google.com/iam/docs/job-functions/networking) .

##  June 28, 2017

**CHANGED:**

[ Custom roles ](https://cloud.google.com/iam/docs/understanding-custom-roles)
are now available in a public alpha. You can create a custom Cloud IAM role
with one or more permissions, then grant that custom role to users in your
organization.

##  May 24, 2017

**CHANGED:**

You can now learn how to configure [ IAM roles for billing-related job
functions ](https://cloud.google.com/iam/docs/job-functions/billing) .

##  March 08, 2017

**FEATURE:**

[ Custom roles ](https://cloud.google.com/iam/docs/understanding-custom-roles)
are now available in a private alpha. You can create a custom Cloud IAM role
with one or more permissions, then grant that custom role to users in your
organization.

##  May 10, 2016

**CHANGED:**

Cloud IAM is now [ generally available
](https://cloud.google.com/products/#product-launch-stages) .

##  March 28, 2016

**CHANGED:**

Documentation is now available to help you [ understand service accounts
](https://cloud.google.com/iam/docs/understanding-service-accounts) and [ use
IAM securely ](https://cloud.google.com/iam/docs/using-iam-securely) .

##  March 08, 2016

**FEATURE:**

Cloud IAM is now available in beta.

