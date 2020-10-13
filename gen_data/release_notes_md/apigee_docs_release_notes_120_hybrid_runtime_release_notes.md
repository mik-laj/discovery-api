**NOTE:** Some aspects of this product are in Beta. The hybrid installation
options are GA. To join the Beta program, reach out to your Apigee
representative.

#  1.2.0 - Apigee hybrid runtime release notes

On April 3, 2020, we released Apigee hybrid runtime version 1.2.0.

For more information, see the following resources:

  * _[ Learn more about hybrid ](/apigee/docs/hybrid/v1.2/what-is-hybrid) _ or _[ Start installing ](/apigee/docs/hybrid/v1.2/big-picture) _
  * _Create a paid account:_ Contact [ Apigee Sales ](https://pages.apigee.com/contact-sales-reg.html)
  * _Questions or issues?_ Contact [ Apigee Support ](https://cloud.google.com/apigee/support/)

####  Help & notifications

**Questions or issues?** [ Get help here
](https://cloud.google.com/apigee/support/) .

**Release notifications** : Go to [ http://status.apigee.com
](http://status.apigee.com) and click **Subscribe to Updates** .

[ Release notes home page ](/apigee/docs/release/notes/apigee-release-notes)

##  Upgrading

To upgrade from version 1.1.1 to 1.2.0, you must make changes in your
overrides file that are incompatible with version 1.1.1. Making these changes
to your overrides file is a prerequisite to performing the upgrade. The new
configuration corrects a problem where in some cases API calls were routed to
the wrong environment. For details, see [ Upgrading Apigee hybrid
](/apigee/docs/hybrid/v1.2/upgrade) .

##  New features and updates

Following are the new features and updates in this release.

###  A new virtual host configuration was added to specify routing rules

The new ` virtualhosts ` configuration feature addresses an issue where the
order in which base paths were routed to multiple environments was uncertain.
For details, see [ Configure virtual hosts ](/apigee/docs/hybrid/v1.2/base-
path-routing) . (150336519)

###  Beta release of the OASValidation policy

The OASValidation (OpenAPI Specification Validation) policy (Beta) enables you
to validate an incoming request or response message against an OpenAPI 3.0
Specification (JSON or YAML). For more information, see [ OASValidation policy
(Beta) ](/apigee/docs/api-platform/reference/policies/oas-validation-policy) .
(144949685)

###  Beta release of WebSocket support

Apigee hybrid supports WebSocket connections. API proxy clients can now
request a protocol upgrade from HTTP to WebSockets. For details, see [ Using
WebSockets (Beta) ](/apigee/docs/hybrid/v1.2/websockets) .

###  Accessing policy secret values from Kubernetes secrets

A new feature lets you access values stored in a Kubernetes secret in proxy
flow variables. For details, see [ Storing data in a Kubernetes secret
](/apigee/docs/hybrid/v1.2/k8s-secrets) . (133377603)

###  Apigee Operators (AO) element replaces ADAC and ADAH

Apigee Operators (AO) Creates and updates low level Kubernetes and Istio
resources that are required to deploy and maintain the AD. For example, the
controller carries out the release of message processors. Also validates the
ApigeeDeployment configuration before persisting it in Kubernetes cluster. AO
replaces Apigee Deployment Admissionhook (ADAH) and Apigee Deployment
Controller (ADC). See [ ao in the Configuration property reference
](/apigee/docs/hybrid/v1.2/config-prop-ref#ao) . (151250559)

###  Replace and deprecate certain cluster and project configuration
properties

Two new configuration properties were added: ` k8sCluster ` and ` gcp ` .
These properties replace the following deprecated properties: ` k8sClusterName
` , ` gcpRegion ` , and ` gcpProjectID ` . For details, see [ Configuration
property reference ](/apigee/docs/hybrid/v1.2/config-prop-ref) . (146299599)

###  Persistent Volume expansion for Cassandra on Kubernetes

A process was added to expand the persistent volume used by apigee-cassandra
to accommodate the storage needs, without needing to add more nodes just to
increase storage. See [ Expand Cassandra persistent volumes
](/apigee/docs/hybrid/v1.2/expand-persistent-volumes) . (138167919)

###  Support additional sources for certs, encryption keys and SAs

New configuration properties were added that provide greater flexibility in
the way you specify TLS certificates, encryption keys, and service account
keys. The new properties are listed below:

  * ` kmsEncryptionPath `
  * ` kmsEncryptionSecret.key `
  * ` kmsEncryptionSecret.name `
  * ` cassandra.backup.serviceAccountSecretRef `
  * ` cassandra.restore.serviceAccountSecretRef `
  * ` envs[].cacheEncryptionPath `
  * ` envs[].cacheEncryptionSecret.key `
  * ` envs[].cacheEncryptionSecret.name `
  * ` envs[].kmsEncryptionPath `
  * ` envs[].kmsEncryptionSecret.key `
  * ` envs[].kmsEncryptionSecret.name `
  * ` envs[].serviceAccountSecretRefs.synchronizer `
  * ` envs[].serviceAccountSecretRefs.udca `
  * ` envs[].sslSecret `
  * ` logger.serviceAccountSecretRef `
  * ` mart.serviceAccountSecretRef `
  * ` mart.sslSecret `
  * ` metrics.serviceAccountSecretRef `
  * ` synchronizer.serviceAccountSecretRef `
  * ` udca.serviceAccountSecretRef `

For more information, see the [ Configuration properties reference
](/apigee/docs/hybrid/v1.2/config-prop-ref) . (145303466)

###  Allow customers to obfuscate data before sending it to analytics

A feature was added that allows you to obfuscate certain analytics data before
it is sent to the management plane. For details, see [ Obfuscate user data for
analytics ](/apigee/docs/hybrid/v1.2/obfuscate-userdata-for-analytics) .
(142578910)

###  Expand persistent volumes for statefulsets

A feature was added that allows you expand the persistent volume used by
apigee-cassandra to accommodate the storage needs, without adding more compute
power. For more information, see [ Expand persistent volumes for statefulsets
](/apigee/docs/release/notes/hybrid/v1.2/expand-persistent-volumes) .
(138167919)

###  Minimum supported versions of GKE, Anthos, and AKS are upgraded

Apigee hybrid now supports GKE 1.14.x, Anthos 1.2, and AKS 1.14.x. (149578101)

###  Support TLS 1.3 for Northbound connections

Two new configuration properties allow you to set the minimum and maximum TLS
version for the ingress: ` ingress.minTLSProtocolVersion ` and `
maxTLSProtocolVersion ` . Possible values are 1.0, 1.1, 1.2 and 1.3. For more
information, see the [ Configuration properties reference
](/apigee/docs/hybrid/v1.2/config-prop-ref) . (117580780)

###  Support forward proxy configuration for hybrid runtime

HTTP forward proxying is now supported for API proxies deployed to an
environment. For details, see [ Configure forward proxying
](/apigee/docs/hybrid/v1.2/forward-proxy) . (148970527)

###  Support multiple hostAliases per environment

A new configuration property, ` envs[].hostAliases ` , has been added. This
property lets you add multiple host aliases to an environment. Use this
element instead of ` hostAlias ` , which has been deprecated. For details, see
[ Adding multiple host aliases to an environment
](/apigee/docs/hybrid/v1.2/environment-create#adding-multiple-host-aliases-to-
an-environment) . (150738495)

###  Allow templates for property sets

A new element <PropertySetRef> was added to the <AssignVariable> element of
the <AssignMessage> policy. <PropertySetRef> allows you to create a property
set name/key pair dynamically. This feature is only available for API proxies
deployed to Apigee hybrid. See [ AssignVariable ](/apigee/docs/api-
platform/reference/policies/assign-message-policy#assignvariable) .
(148612340)

##  Bugs fixed

The following bugs are fixed in this release. This list is primarily for users
checking to see if their support tickets have been fixed. It's not designed to
provide detailed information for all users.

Issue ID  |  Component Name  |  Description  
---|---|---  
147958049  |  Runtime  |  A timing issue in runtime startup sequencing was
addressed that sometimes prevented the synchronizer from starting up properly.  
149867244  |  K8S Platform  |  apigee-cps-setup pod failing in multi-region
setup  
150187652 / 149117839  |  Runtime  |  Could not use hyphens in environment
names.  
149220463  |  MP pod  |  Previously deployed proxies needed to be re-deployed.  
144321144  |  Runtime  |  Proxies with secure virtual hosts could not be
reloaded.  
147685310  |  Runtime  |  Synchronizer initialization failures due to failed
GCP token fetch during initialization.  
151115900  |  Runtime  |  Periodic Internal Probe was not happening for
HybridMART resulting in false positive results.  
  
##  Known issues

The following table describes the known issues for this release:

Issue  |  Description  
---|---  
161658025  |

Inaccurate deployment status for Shared Flows

For Shared Flows, the deployment status is not being reported correctly to the
UI, resulting in an indefinitely spinning deployment icon. If you have
deployed a Shared Flow and see the spinning deployment icon, you must assume
that the deployment has in fact failed.

To obtain the correct deployment status, use the [
v1.organizations.environments.sharedflows.revisions.deployments
](/apigee/docs/reference/apis/apigee/rest#rest-
resource:-v1.organizations.environments.sharedflows.revisions.deployments)
API. For example:

    
    
    curl -s -H "$AUTH" \
    "https://apigee.googleapis.com/v1/o/$ORG/e/$ENV/sharedflows/$FLOW/revisions/$REV/deployments"  
  
N/A  |

Invalid HTTP Header error: The Istio ingress switches all incoming target
responses to the HTTP2 protocol. Because the hybrid message processor only
supports HTTP1, you may see the following error when an API proxy is called:

    
    
    http2 error: Invalid HTTP header field was received: frame type: 1, stream: 1,
       name: [:authority], value: [domain_name]

If you see this error, you can take either of the following actions to correct
the problem:

  * Modify the target service to omit the Host header in the response. 
  * Remove the Host header using the AssignMessage policy in your API proxy if necessary. 

  
144584813  |  If you create a debug session but the session does not yet have
any transactions in it, then the [ List Debug Sessions API
](https://cloud.google.com/hybrid/v1.2/reference/apis/rest/v1/organizations.environments.apis.revisions.debugsessions/list)
does not include the session in this list. The API only includes sessions in
the response if the session contains at least one transaction.  
143659917  |

The PopulateCache policy's expiration setting must be set to an explicit value
between 1 and 30. For example:

    
    
    <ExpirySettings>
      <TimeoutInSec>30</TimeoutInSec>
    </ExpirySettings>  
  
133192879  |

Summary: There is a very high latency when using the API or UI to get your
organization's deployment status. This latency can result in an ` HTTP 204 (No
Content) ` or an ` HTTP 400 (Bad Request) ` response.

Workaround: Refresh your browser (or resend the request).

