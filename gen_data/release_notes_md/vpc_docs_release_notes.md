#  Release notes

This page contains release notes for features and updates to Google Cloud
Platform VPC networking.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/vpc-release-notes.xml `

##  June 12, 2020

**FEATURE:**

[ Firewall Rules Logging metadata controls
](https://cloud.google.com/vpc/docs/firewall-rules-logging#log-format) is now
available in **Beta** .

##  June 08, 2020

**FEATURE:**

For auto mode VPC networks, added a new subnet ` 10.184.0.0/20 ` for the
Jakarta ` asia-southeast2 ` region. For more information, see [ Auto mode IP
ranges ](https://cloud.google.com/vpc/docs/vpc#ip-ranges) .

##  June 03, 2020

**FEATURE:**

[ Hierarchical firewall policies ](https://cloud.google.com/vpc/docs/firewall-
policies) are now available in **Beta** .

##  May 29, 2020

**FEATURE:**

GKE annotations and advanced controls for [ VPC Flow Logs
](https://cloud.google.com/vpc/docs/using-flow-logs) is now available in
**General Availability** .

##  May 18, 2020

**FEATURE:**

Subnets in VPC networks now support IP addresses other than RFC 1918
addresses. For more information, see [ Subnet ranges
](https://cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges) .

##  April 29, 2020

**CHANGED:**

Google Cloud now encrypts VPC traffic within the boundaries of the data
centers in _asia-east2_ . We will roll out this feature gradually to other
regions. Google Cloud already encrypts VPC traffic _between all data centers_
as described in [ Encryption in Transit in Google Cloud
](https://cloud.google.com/security/encryption-in-transit#virtual-network) .

##  April 24, 2020

**FEATURE:**

[ Private Google Access for on-premises hosts
](https://cloud.google.com/vpc/docs/private-access-options#pga-onprem) permits
on-premises hosts to send traffic from any internal IP addresses, not just RFC
1918 addresses. This feature is now **Generally Available** .

##  April 20, 2020

**FEATURE:**

For auto mode VPC networks, added a new subnet ` 10.182.0.0/20 ` for the Las
Vegas ` us-west4 ` region. For more information, see [ Auto mode IP ranges
](https://cloud.google.com/vpc/docs/vpc#ip-ranges) .

**CHANGED:**

[ Packet Mirroring pricing ](https://cloud.google.com/vpc/network-
pricing#packet-mirroring) will come into effect from June 20, 2020. There is
no charge for Packet Mirroring until that time.

##  March 03, 2020

**FEATURE:**

[ Packet MIrroring ](https://cloud.google.com/vpc/docs/packet-mirroring) is
now available in **General Availability** .

##  February 24, 2020

**FEATURE:**

For auto mode VPC networks, added a new subnet ` 10.180.0.0/20 ` for the Salt
Lake City ` us-west3 ` region. For more information, see [ Auto mode IP ranges
](https://cloud.google.com/vpc/docs/vpc#ip-ranges) .

##  January 24, 2020

**CHANGED:**

For auto mode VPC networks, added a new subnet ` 10.178.0.0/20 ` for the Seoul
` asia-northeast3 ` region. For more information, see [ Auto mode IP ranges
](https://cloud.google.com/vpc/docs/vpc#ip-ranges) .

##  January 01, 2020

**CHANGED:**

Google now charges for static external IPv4 addresses that are in use, except
for ones that are used by forwarding rules. For more information, see the [
Network pricing ](https://cloud.google.com/vpc/network-pricing#ipaddress) .

##  December 19, 2019

**FEATURE:**

[ Private Google Access for on-premises hosts
](https://cloud.google.com/vpc/docs/private-access-options#pga-onprem) now
permits on-premises hosts to send traffic from any internal IP addresses, not
just RFC 1918 addresses. This feature is now available in **Beta** .

##  December 11, 2019

**FEATURE:**

[ Serverless VPC Access ](https://cloud.google.com/vpc/docs/configure-
serverless-vpc-access) is now **Generally Available** .

##  November 22, 2019

**FEATURE:**

Virtual machines with 2 or 4 vCPUs now have a maximum egress rate of 10 Gbps.
This feature is Generally Available. For more information, see [ Machine types
](http://cloud.google.com/compute/docs/machine-types) in the Compute Engine
documentation.

##  November 18, 2019

**FEATURE:**

The ` private.googleapis.com ` virtual IP address range for [ Private Google
Access for on-premises hosts ](https://cloud.google.com/vpc/docs/private-
access-options) is **Generally Available** .

##  November 13, 2019

**FEATURE:**

For VPC Network Peering, [ importing and exporting custom routes
](https://cloud.google.com/vpc/docs/vpc-peering) are now **General Available**
.

**FEATURE:**

[ Packet MIrroring ](https://cloud.google.com/vpc/docs/packet-mirroring) is
now available in **Beta** .

##  September 23, 2019

**CHANGED:**

The [ quotas ](https://cloud.google.com/vpc/docs/quota) for subnet ranges per
network and per peering group have changed.

##  September 20, 2019

**FEATURE:**

[ VPC Flow Logs log volume reduction
](https://cloud.google.com/vpc/docs/using-flow-logs#log-sampling) is now
available in **General Availability** .

##  August 13, 2019

**FEATURE:**

The ` private.googleapis.com ` virtual IP address range for [ Private Google
Access for on-premises hosts ](https://cloud.google.com/vpc/docs/private-
access-options) is in **Beta** .

##  June 19, 2019

**FEATURE:**

The increased egress rate of [ 32Gbps of network I/O
](https://cloud.google.com/vpc/docs/quota#per_instance) for virtual machines
that use either the Skylake CPU platform or ultramem machine types, is now
available in **General Availability** .

##  April 09, 2019

**FEATURE:**

[ Serverless VPC Access ](https://cloud.google.com/vpc/docs/configure-
serverless-vpc-access) is now available in **Beta** .

##  April 05, 2019

**FEATURE:**

You can get up to [ 32Gbps of network I/O
](https://cloud.google.com/vpc/docs/quota#per_instance) for virtual machines
that use either the Skylake CPU platform or ultramem machine types. This
increased egress rate is now available in **Beta** .

##  April 04, 2019

**FEATURE:**

[ VPC Flow Logs log volume reduction
](https://cloud.google.com/vpc/docs/using-flow-logs#log-sampling) is now
available in **Beta** .

##  April 01, 2019

**FEATURE:**

For VPC Network Peering, [ importing and exporting custom routes
](https://cloud.google.com/vpc/docs/vpc-peering) is now available in **Beta**
.

##  March 27, 2019

**FEATURE:**

[ Private services access ](https://cloud.google.com/vpc/docs/private-access-
options) is now available in **General Availability** .

##  February 07, 2019

**CHANGED:**

You can disable the [ default network
](https://cloud.google.com/vpc/docs/vpc#default-network) creation for new
projects. You must [ create an organization policy
](https://cloud.google.com/resource-manager/docs/organization-policy/creating-
managing-policies) and add the ` compute.skipDefaultNetworkCreation `
constraint.

##  February 01, 2019

**FEATURE:**

The [ private access option ](https://cloud.google.com/vpc/docs/private-
access-options) for on-premises hosts is now **Generally Available** . On-
premises hosts with only private IP addresses can access Google APIs through a
Cloud VPN or Cloud Interconnect connections (hybrid connectivity scenarios).

##  January 24, 2019

**DEPRECATED:**

The [ IPv4Range
](https://cloud.google.com/compute/docs/reference/rest/v1/networks) field for
creating [ legacy networks ](https://cloud.google.com/vpc/docs/legacy) is now
deprecated and will shut down on **February 1, 2020** .

##  January 09, 2019

**FEATURE:**

[ Firewall rules logging ](https://cloud.google.com/vpc/docs/firewall-rules-
logging) is now available in **General Availability** .

##  December 20, 2018

**FEATURE:**

IP address allocation for [ private services access
](https://cloud.google.com/vpc/docs/configure-private-services-
access#allocating-range) is now available in **General Availability** .

##  October 19, 2018

**FEATURE:**

[ Private Google Access for on-premises hosts
](https://cloud.google.com/vpc/docs/private-access-options) is now available
in **Beta** . On-premises hosts with only private IP addresses can now access
Google APIs through Cloud VPN or Cloud Interconnect connections (hybrid
connectivity scenarios).

##  September 26, 2018

**FEATURE:**

[ Private services access ](https://cloud.google.com/vpc/docs/private-access-
options) provides a private connection between your VPC network and a network
owned by Google or a third party. Private services access is in **Beta** .

##  September 18, 2018

**FEATURE:**

[ Firewall rules logging ](https://cloud.google.com/vpc/docs/firewall-rules-
logging) is now available in **Beta** .

##  September 05, 2018

**FEATURE:**

The ability to [ Disable firewall rules
](https://cloud.google.com/vpc/docs/firewalls#enforcement) is now available in
**General Availability** .

##  July 31, 2018

**FEATURE:**

In Shared VPC service projects, [ listing usable
](https://cloud.google.com/vpc/docs/provisioning-shared-
vpc#discovering_subnets_that_can_be_used) subnets in the host project is now
available in **General Availability** .

##  June 28, 2018

**FEATURE:**

[ VPC Flow Logs ](https://cloud.google.com/vpc/docs/using-flow-logs) are now
available in **General Availability** .

##  May 09, 2018

**FEATURE:**

[ Folder support for Shared VPC ](https://cloud.google.com/vpc/docs/shared-
vpc#iam_in_shared_vpc) is now available in **Beta** .

##  May 01, 2018

**FEATURE:**

The ability to [ Disable firewall rules
](https://cloud.google.com/vpc/docs/firewalls#enforcement) is now available in
**Beta** .

##  April 23, 2018

**FEATURE:**

[ Add/Delete Alias IP Ranges ](https://cloud.google.com/vpc/docs/alias-ip) is
now available in **General Availability** .

##  March 29, 2018

**FEATURE:**

[ VPC Flow Logs ](https://cloud.google.com/vpc/docs/using-flow-logs) are now
available in **Beta** .

##  November 13, 2017

**CHANGED:**

VPC Networks documentation has moved to [ https://cloud.google.com/vpc/docs
](https://cloud.google.com/vpc/docs) .

##  September 05, 2017

**FEATURE:**

[ Alias IP Ranges ](https://cloud.google.com/vpc/docs/alias-ip) allows you to
assign additional IP addresses to a VM instance. These addresses can be used
by containers running on the VM. Alias IP Ranges is now available in **General
Availability** .

**FEATURE:**

[ Firewall Rules egress and deny rules
](https://cloud.google.com/vpc/docs/firewalls) allows you to create firewall
rules that govern egress as well as ingress traffic. You can now also create
deny rules and you can prioritize the order in which rules are evaluated.
Firewall Rules egress and deny rules is now available in **General
Availability** .

##  August 18, 2017

**FEATURE:**

[ Multiple Network Interfaces ](https://cloud.google.com/vpc/docs/multiple-
interfaces-concepts) allows a VM instance to have more than one virtual
network interfaces. Each interface must point to a different VPC network.
Multiple Network Interfaces is now available in **General Availability** .

##  August 11, 2017

**FEATURE:**

Add support for specifying a static internal IP to **Beta** . See [ Reserving
a Static Internal IP Address ](https://cloud.google.com/compute/docs/ip-
addresses/reserve-static-internal-ip-address) for more information.

##  July 14, 2017

**FEATURE:**

[ VPC Network Peering ](https://cloud.google.com/vpc/docs/vpc-peering) allows
you to peer VPC networks, even networks in different organizations, so that
the networks can communicate with each other using internal IP addresses. VPC
Network Peering is now available in **General Availability** .

##  June 21, 2017

**FEATURE:**

[ Multiple Network Interfaces ](https://cloud.google.com/vpc/docs/multiple-
interfaces-concepts) allows a VM instance to have more than one virtual
network interface. Each interface must point to a different VPC network.
Multiple Network Interfaces is now available in **Beta** .

##  June 07, 2017

**FEATURE:**

[ Shared VPC ](https://cloud.google.com/vpc/docs/shared-vpc) (Previously
Cross-Project Networking (XPN)) is now available in **General Availability** .

##  May 22, 2017

**FEATURE:**

[ Alias IP Ranges ](https://cloud.google.com/vpc/docs/alias-ip) allows you to
assign additional IP addresses to a VM instance. These addresses can be used
by containers running on the VM. Alias IP Ranges is now available in **Beta**
.

##  May 08, 2017

**FEATURE:**

[ VPC Network Peering ](https://cloud.google.com/vpc/docs/vpc-peering) allows
you to peer VPC networks, even networks in different organizations, so that
the networks can communicate with each other using internal IP addresses. VPC
Network Peering is now available in **Beta** .

##  May 04, 2017

**FEATURE:**

[ Private Google Access ](https://cloud.google.com/vpc/docs/private-access-
options) allows Compute Engine VM instances to access Google APIs using an
internal IP address only. Private Google Access is now available in **General
Availability** .

##  May 01, 2017

**CHANGED:**

Decoupled labels and tags so that creating either a label or a tag will not
create the opposing resource. For example, creating a label will no longer
create a tag and vice-versa. For more information, read [ Relationship between
instance labels and network tags
](https://cloud.google.com/compute/docs/labeling-resources#labels_tags) .

**CHANGED:**

You can now find information about network tags in the [ VPC networking
](https://cloud.google.com/vpc/docs/add-remove-network-tags) documentation.

##  April 17, 2017

**FEATURE:**

[ Firewall Rules egress and deny rules
](https://cloud.google.com/vpc/docs/firewalls) allows you to create firewall
rules that govern egress as well as ingress traffic. You can now also create
deny rules and you can prioritize the order in which rules are evaluated.
Firewall Rules egress and deny rules is now available in **Beta** .

##  March 09, 2017

**FEATURE:**

[ Shared VPC ](https://cloud.google.com/vpc/docs/shared-vpc) allows you to
share a VPC network with other GCP projects. Shared VPC is now available in
**Beta** .

##  March 07, 2017

**FEATURE:**

[ Private Google Access ](https://cloud.google.com/vpc/docs/private-access-
options) allows Compute Engine VM instances to access Google APIs using an
internal IP address only. Private Google Access is now available in **Beta** .

##  December 21, 2016

**FEATURE:**

Added ICMP support for [ forwarding rules
](https://cloud.google.com/vpc/docs/forwarding-rules) .

##  May 11, 2016

**FEATURE:**

The following VPC IAM roles are now generally available: `
roles/compute.networkAdmin ` , ` roles/compute.securityAdmin ` , `
roles/iam.serviceAccountActor `

For more information, read the [ IAM
](https://cloud.google.com/compute/docs/access/iam) documentation.

##  November 04, 2014

**CHANGED:**

Lowered network pricing. See [ Network pricing
](https://cloud.google.com/vpc/network-pricing) for more information.

##  May 05, 2014

**CHANGED:**

Updated default firewall rule names. Default firewall rules are automatically
created with every project. These rules were previously named ` default-
internal ` and ` default-ssh ` . New projects will have the same default
firewalls but with the following new names:

  * ` default-allow-internal ` \- Allows network connections of any protocol and port between any two instances. 
  * ` default-allow-ssh ` \- Allows TCP connections from any source to any instance on the network, over port 22. 

**CHANGED:**

Introduced new default firewall rule that will be created with each new
project.

  * ` default-allow-icmp ` \- Allows ICMP traffic from any source to any instance on the network. 

##  December 17, 2013

**FEATURE:**

Released new Protocol Forwarding feature. [ Forwarding rules
](https://cloud.google.com/vpc/docs/forwarding-rules) allows you to forward
traffic to a single virtual machine instance, using a target.instance.
Protocol forwarding provides support for these additional features:

  * ` AH ` : [ IP Authentication Header ](http://tools.ietf.org/html/rfc4302.html) protocol 
  * ` ESP ` : [ IP Encapsulating Security Payload ](http://www.ietf.org/rfc/rfc2406.txt) protocol 
  * ` SCTP ` : [ Stream Control Transmission ](http://www.ietf.org/rfc/rfc2960.txt) protocol 

**FEATURE:**

Added support for new [ Target Instance resources
](https://cloud.google.com/load-balancing/docs/forwarding-rules) , which
allows for non-NAT'ed traffic to be forwarded to a single virtual machine
instance. See [ Forwarding rules
](https://cloud.google.com/vpc/docs/forwarding-rules) for more information.

