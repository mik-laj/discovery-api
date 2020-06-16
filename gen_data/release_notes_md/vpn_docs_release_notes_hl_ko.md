#  출시 노트

이 페이지에는 Cloud VPN의 기능과 업데이트에 대한 출시 노트가 포함되어 있습니다.

최신 제품 업데이트를 받으려면 [ 피드 리더
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 에 이 페이지의 URL을
추가하거나 피드 URL을 다음과 같이 직접 추가하세요. ` https://cloud.google.com/feeds/cloudvpn-
release-notes.xml `

##  June 15, 2020

**FEATURE:**

Cloud VPN now supports [ an org-level policy
](https://cloud.google.com/vpn/docs/concepts/overview?hl=ko#vpn-org-policy)
that restricts peer IP addresses through a Cloud VPN tunnel.

##  June 08, 2020

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/?hl=ko#available) asia-
southeast2 (Jakarta, Indonesia).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing?hl=ko) .

##  April 20, 2020

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/?hl=ko#available) us-
west4 (Las Vegas, Nevada, USA).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing?hl=ko) .

##  February 24, 2020

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/?hl=ko#available) us-
west3 (Salt Lake City, Utah, USA).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing?hl=ko) .

##  January 24, 2020

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/?hl=ko#available) asia-
northeast3 (Seoul).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing?hl=ko) .

##  October 30, 2019

**FIXED:**

In the Stackdriver Metrics Explorer, the ` sent_packets_count ` and `
received_packets_count ` metrics for a Cloud VPN gateway reported double the
actual count.

These metrics now report an accurate count on a per tunnel basis.

##  September 27, 2019

**FEATURE:**

[ HA VPN ](https://cloud.google.com/vpn/docs/concepts/overview?hl=ko) is
Generally Available.

**ISSUE:**

GCP resources specific to HA VPN, including ` compute.vpnGateways ` and `
compute.externalVpnGateways ` , are not yet displayed in [ Cloud Asset
Inventory ](https://cloud.google.com/resource-manager/docs/cloud-asset-
inventory/overview?hl=ko) , or [ Cloud Security Command Center
](https://cloud.google.com/security-command-center/docs/how-to-assets-
display?hl=ko#viewing_by_asset_type) .

The ` compute.vpnTunnels ` resource is listed in both locations and is
required for a working HA VPN connection.

**ISSUE:**

To view Monitoring metrics for HA VPN, you must use Metrics Explorer. See the
[ Viewing logs and metrics page ](https://cloud.google.com/vpn/docs/how-
to/viewing-logs-metrics?hl=ko#viewing-monitoring-dashboards) .

**ISSUE:**

When setting up Cloud VPN tunnels to AWS, [ using IKEv2 and configuring fewer
IKE transform sets ](https://cloud.google.com/vpn/docs/how-to/creating-ha-
vpn?hl=ko#aws-known-issue) is required.

##  May 13, 2019

**FEATURE:**

HA VPN is available in **Beta** .

HA VPN enables you to securely connect your on-premises network to your
Virtual Private Cloud network through a highly-available IPsec VPN connection
in a single region. HA VPN provides a service level availability of 99.99% at
GA.

##  June 05, 2018

**CHANGED:**

Published a major document reorganization and rewrite for Cloud VPN.

##  April 20, 2018

**CHANGED:**

Published a quickstart guide for Cloud VPN.

##  October 31, 2017

**CHANGED:**

Published a standalone guide for Cloud VPN.

##  May 20, 2015

**FEATURE:**

Cloud VPN is **Generally available** .

##  March 05, 2015

**FEATURE:**

Cloud VPN is available in **Beta** .

Cloud VPN enables you to connect your on-premises and Virtual Private Cloud
networks through an IPsec VPN tunnel.

