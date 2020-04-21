#  Notas de lançamento

Nesta página, você encontra as notas de lançamento de recursos e atualizações
do Cloud VPN.

Para receber as atualizações de produtos mais recentes, adicione o URL desta
página ao [ leitor de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) (em inglês) ou
adicione o URL do feed diretamente: ` https://cloud.google.com/feeds/cloudvpn-
release-notes.xml `

##  April 20, 2020

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/?hl=pt_br#available) us-
west4 (Las Vegas, Nevada, USA).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing?hl=pt_br) .

##  February 24, 2020

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/?hl=pt_br#available) us-
west3 (Salt Lake City, Utah, USA).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing?hl=pt_br) .

##  January 24, 2020

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/?hl=pt_br#available)
asia-northeast3 (Seoul).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing?hl=pt_br) .

##  October 30, 2019

**FIXED:**

In the Stackdriver Metrics Explorer, the ` sent_packets_count ` and `
received_packets_count ` metrics for a Cloud VPN gateway reported double the
actual count.

These metrics now report an accurate count on a per tunnel basis.

##  September 27, 2019

**FEATURE:**

[ HA VPN ](https://cloud.google.com/vpn/docs/concepts/overview?hl=pt_br) is
Generally Available.

**ISSUE:**

GCP resources specific to HA VPN, including ` compute.vpnGateways ` and `
compute.externalVpnGateways ` , are not yet displayed in [ Cloud Asset
Inventory ](https://cloud.google.com/resource-manager/docs/cloud-asset-
inventory/overview?hl=pt_br) , or [ Cloud Security Command Center
](https://cloud.google.com/security-command-center/docs/how-to-assets-
display?hl=pt_br#viewing_by_asset_type) .

The ` compute.vpnTunnels ` resource is listed in both locations and is
required for a working HA VPN connection.

**ISSUE:**

To view Monitoring metrics for HA VPN, you must use Metrics Explorer. See the
[ Viewing logs and metrics page ](https://cloud.google.com/vpn/docs/how-
to/viewing-logs-metrics?hl=pt_br#viewing-monitoring-dashboards) .

**ISSUE:**

When setting up Cloud VPN tunnels to AWS, [ using IKEv2 and configuring fewer
IKE transform sets ](https://cloud.google.com/vpn/docs/how-to/creating-ha-
vpn?hl=pt_br#aws-known-issue) is required.

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

