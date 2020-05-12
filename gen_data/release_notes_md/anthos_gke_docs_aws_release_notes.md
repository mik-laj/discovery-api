A new version of Anthos GKE on AWS was released on May 7. See the [ release
notes ](/anthos/gke/docs/aws/release-notes) for information on breaking
changes.

#  Release notes

This page documents production updates to Anthos GKE on AWS. Check this page
for announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

##  May 07, 2020

**BREAKING:**

To upgrade your Anthos GKE on AWS clusters, you need to [ uninstall
](https://cloud.google.com/anthos/gke/docs/aws/how-to/uninstalling) all your
management and user clusters. You also need to download the new version of the
[ ` anthos-gke `
](https://cloud.google.com/anthos/gke/docs/aws/downloads#anthos-gke_cli_tool)
cli tool.

**CHANGED:**

Anthos GKE on AWS now supports [ auto-scaling
](https://cloud.google.com/anthos/gke/docs/aws/how-to/scaling-user-cluster) .
You can enable auto-scaling by changing settings in your AWSNodePools, or
scale your clusters manually by adding new AWSNodePools.

**CHANGED:**

Built-in EBS StorageClass names have been changed to ` standard-rwo ` and `
premium-rwo ` . If you declare the [ ` singlewriter-standard ` or `
singlewriter-premium `
](https://cloud.google.com/anthos/gke/docs/aws/concepts/storage.md)
StorageClasses with your workloads, you must update your workloads when
upgrading.

**CHANGED:**

Anthos GKE on AWS now support for Application-layer secrets encryption with
AWS KMS by passing a KMS key ARN to your [ AWSCluster
](https://cloud.google.com/anthos/gke/docs/aws/reference/awscluster#speccontrolplane)
.

##  April 02, 2020

**FEATURE:**

Initial beta release of Anthos GKE on AWS

**CHANGED:**

The release improves upon earlier releases with:

  * **Improved reliability** : User clusters are now deployed in a high availability (HA) fashion, where both control plane instances as well as node pools can be placed across multiple availability zones. AWS Auto Scaling groups are also now used for resiliency. 

  * **Improved security** : Control plane instances for different user clusters are now isolated in separate security groups. Instance Metadata Service Version 2 (IMDSv2) is enabled to protect against SSRF attacks, and sensitive fields in EC2 metadata are now encrypted. 

  * **Easier to deploy** : The installation process for the management layer has been simplified and performs additional validation checks. It uses Terraform modules for flexible integration into different AWS environments, and customers can now leverage existing security groups and IAM resources to secure clusters. Documentation has been improved and expanded. 

  * **Future-proof storage stack** : We're now using the [ EBS CSI driver ](https://github.com/kubernetes-sigs/aws-ebs-csi-driver) to manage all AWS EBS volumes. The legacy, in-tree Kubernetes EBS driver has been removed entirely, and all upcoming storage features, such as snapshots, will be provided using CSI. 

  * **Updated Kubernetes version** : User clusters are now based on Kubernetes 1.15 and have passed open-source Kubernetes conformance tests. 

