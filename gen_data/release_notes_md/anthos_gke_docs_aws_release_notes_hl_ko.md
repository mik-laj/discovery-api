Anthos GKE on AWS의 새 버전이 7월 24일 출시되었습니다. 새로운 변경사항에 대한 자세한 내용은 [ 출시 노트
](https://cloud.google.com/anthos/gke/docs/aws/release-notes?hl=ko) 를 참조하세요.

#  출시 노트

이 페이지에서는 Anthos GKE on AWS의 프로덕션 업데이트에 대해 설명합니다. 새로운 기능이나 업데이트된 기능, 버그 수정, 알려진
문제, 지원 중단된 기능에 대한 공지를 이 페이지에서 확인하세요.

[ Google Cloud 출시 노트 ](https://cloud.google.com/release-notes?hl=ko) 페이지에서
Google Cloud의 모든 최신 제품 업데이트를 확인할 수 있습니다.

##  August 04, 2020

**FIXED:**

Anthos GKE on AWS 1.4.1-gke.17 is released. This release fixes a memory leak
that causes clusters to become unresponsive.

To upgrade your clusters, perform the following steps:

  1. Restart your [ control plane instances ](https://cloud.google.com/anthos/gke/docs/aws/troubleshooting?hl=ko#rebooting_your_control_plane) . 
  2. Upgrade your [ management service ](http://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-management?hl=ko) to aws-1.4.1-gke.17. 
  3. Upgrade your [ user cluster's ](http://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-user-cluster?hl=ko) AWSCluster and AWSNodePools to 1.16.9-gke.15. 

**CHANGED:**

Use version 1.16.9-gke.15 for creating new clusters.

##  August 03, 2020

**ISSUE:**

Anthos GKE on AWS 1.4.1-gke.15 clusters will experience a memory leak that
results in an unresponsive cluster. A fix for this issue is in development.

If you are planning to deploy an Anthos GKE on AWS cluster, wait until the fix
is ready.

##  July 24, 2020

**CHANGED:**

Anthos GKE on AWS is now generally available.

**CHANGED:**

Clusters support in-place upgrades, with the ability to upgrade the control
plane and node pools separately.

**CHANGED:**

Clusters can be deployed in a high availability (HA) configuration, where
control plane instances and node pools are spread across multiple availability
zones.

**CHANGED:**

Clusters have been validated to support up to 200 nodes and 6000 pods.

**CHANGED:**

Allows the number of nodes to be scaled dynamically based on traffic volume to
increase utilization and reduce cost, and improve performance

**CHANGED:**

Anthos can be deployed within existing AWS VPCs, leveraging existing security
groups to secure those clusters. Customers can ingress traffic using NLB and
ALBs. Additionally Anthos on AWS supports AWS IAM and OIDC. This makes
deploying Anthos easy, eliminates the need to provision new accounts, and
minimizes configuration of the environment.

**CHANGED:**

With Anthos Config Management enterprises can set policies on their AWS
workloads and with Anthos Service Mesh, they can monitor, manage, and secure
them.

**CHANGED:**

Kubernetes settings (flags and sysctl settings) have been updated to match
GKE.

**BREAKING:**

Upgrades from beta versions are not supported. To install Anthos GKE on AWS,
you must remove your user and management clusters, then reinstall them.

##  May 29, 2020

**CHANGED:**

A new build of Anthos GKE on AWS has been released. This build removes the
need to check AWS IAM privileges when creating a management cluster. **You
don't need to update** if you have not encountered this issue.

To install this build, download the ` anthos-gke ` tool by running the
following command:

` gsutil cp gs://gke-multi-cloud-release/bin/aws-0.2.1-gke.8/anthos-gke . `

Then, recreate your [ Terraform configuration
](https://cloud.google.com/anthos/gke/docs/aws/how-to/installing-
management?hl=ko) and continue with your installation.

##  May 07, 2020

**BREAKING:**

To upgrade your Anthos GKE on AWS clusters, you need to [ uninstall
](https://cloud.google.com/anthos/gke/docs/aws/how-to/uninstalling?hl=ko) all
your management and user clusters. You also need to download the new version
of the [ ` anthos-gke `
](https://cloud.google.com/anthos/gke/docs/aws/downloads?hl=ko#anthos-
gke_cli_tool) cli tool.

**CHANGED:**

Anthos GKE on AWS now supports [ auto-scaling
](https://cloud.google.com/anthos/gke/docs/aws/how-to/scaling-user-
cluster?hl=ko) . You can enable auto-scaling by changing settings in your
AWSNodePools, or scale your clusters manually by adding new AWSNodePools.

**CHANGED:**

Built-in EBS StorageClass names have been changed to ` standard-rwo ` and `
premium-rwo ` . If you declare the [ ` singlewriter-standard ` or `
singlewriter-premium `
](https://cloud.google.com/anthos/gke/docs/aws/concepts/storage.md?hl=ko)
StorageClasses with your workloads, you must update your workloads when
upgrading.

**CHANGED:**

Anthos GKE on AWS now support for Application-layer secrets encryption with
AWS KMS by passing a KMS key ARN to your [ AWSCluster
](https://cloud.google.com/anthos/gke/docs/aws/reference/awscluster?hl=ko#speccontrolplane)
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

