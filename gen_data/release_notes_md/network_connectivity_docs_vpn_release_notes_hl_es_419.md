#  Notas de la versión

En esta página, se encuentran notas de la versión de funciones y
actualizaciones de Cloud VPN.

Puedes ver las últimas actualizaciones de productos de todo Google Cloud en la
página [ Notas de la versión de Google Cloud
](https://cloud.google.com/release-notes?hl=es-419) .

Para recibir las últimas actualizaciones de productos, agrega la URL de esta
página a tu [ lector de feeds
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , o agrega
directamente la URL del feed: ` https://cloud.google.com/feeds/cloudvpn-
release-notes.xml `

##  June 16, 2020

**CHANGED:**

The public documentation for Cloud VPN is now located under the [ Network
Connectivity page ](https://cloud.google.com/network-
connectivity/docs/?hl=es-419) .

##  June 15, 2020

**FEATURE:**

Cloud VPN now supports [ an org-level policy
](https://cloud.google.com/vpn/docs/concepts/overview?hl=es-419#vpn-org-
policy) that restricts peer IP addresses through a Cloud VPN tunnel.

##  June 08, 2020

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/?hl=es-419#available)
asia-southeast2 (Jakarta, Indonesia).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing?hl=es-419) .

##  April 20, 2020

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/?hl=es-419#available)
us-west4 (Las Vegas, Nevada, USA).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing?hl=es-419) .

##  February 24, 2020

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/?hl=es-419#available)
us-west3 (Salt Lake City, Utah, USA).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing?hl=es-419) .

##  January 24, 2020

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/?hl=es-419#available)
asia-northeast3 (Seoul).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing?hl=es-419) .

##  October 30, 2019

**FIXED:**

In the Stackdriver Metrics Explorer, the ` sent_packets_count ` and `
received_packets_count ` metrics for a Cloud VPN gateway reported double the
actual count.

These metrics now report an accurate count on a per tunnel basis.

##  September 27, 2019

**FEATURE:**

[ HA VPN ](https://cloud.google.com/vpn/docs/concepts/overview?hl=es-419) is
Generally Available.

**ISSUE:**

GCP resources specific to HA VPN, including ` compute.vpnGateways ` and `
compute.externalVpnGateways ` , are not yet displayed in [ Cloud Asset
Inventory ](https://cloud.google.com/resource-manager/docs/cloud-asset-
inventory/overview?hl=es-419) , or [ Cloud Security Command Center
](https://cloud.google.com/security-command-center/docs/how-to-assets-
display?hl=es-419#viewing_by_asset_type) .

The ` compute.vpnTunnels ` resource is listed in both locations and is
required for a working HA VPN connection.

**ISSUE:**

To view Monitoring metrics for HA VPN, you must use Metrics Explorer. See the
[ Viewing logs and metrics page ](https://cloud.google.com/vpn/docs/how-
to/viewing-logs-metrics?hl=es-419#viewing-monitoring-dashboards) .

**ISSUE:**

When setting up Cloud VPN tunnels to AWS, [ using IKEv2 and configuring fewer
IKE transform sets ](https://cloud.google.com/vpn/docs/how-to/creating-ha-
vpn?hl=es-419#aws-known-issue) is required.

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

