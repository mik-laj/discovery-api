#  Release notes

This page documents production updates to Anthos GKE on AWS. Check this page
for announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

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

