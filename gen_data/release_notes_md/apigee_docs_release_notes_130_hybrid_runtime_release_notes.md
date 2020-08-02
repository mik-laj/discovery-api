**NOTE:** Some aspects of this product are in Beta. The hybrid installation
options are GA. To join the Beta program, reach out to your Apigee
representative.

#  1.3.0 - Apigee hybrid runtime release notes

On July 30, 2020, we released Apigee hybrid runtime version 1.3.0.

For more information, see the following resources:

  * _[ Learn more about hybrid ](/apigee/docs/hybrid/v1.2/what-is-hybrid) _ or _[ Start installing ](/apigee/docs/hybrid/v1.2/big-picture) _
  * _Create a paid account:_ Contact [ Apigee Sales ](https://pages.apigee.com/contact-sales-reg.html)
  * _Questions or issues?_ Contact [ Apigee Support ](https://cloud.google.com/apigee/support/)

####  Help & notifications

**Private Cloud customers** : Is this cloud release included in your Private
Cloud version? See your version's release notes to see which cloud releases it
contains. Also, see [ About release numbering ](/apigee/docs/release/apigee-
edge-release-process#aboutreleasenumbering) to understand how you can figure
it out by comparing release numbers.

**Questions or issues?** [ Get help here
](https://cloud.google.com/apigee/support/) .

**Release notifications** : Go to [ http://status.apigee.com
](http://status.apigee.com) and click **Subscribe to Updates** .

[ Release notes home page ](/apigee/docs/release/notes/apigee-release-notes)

##  Upgrading

Upgrade to Apigee hybrid v1.3.0 is not supported at this time.

##  New features and updates

This section describes the new features and enhancements in this release.

###  New installation prerequisites

####  cert-manager

Apigee hybrid requires **cert-manager v0.14.2** to manage and verify
certificates. You can use ` kubectl ` to install and configure cert-manager
directly from _github > jetstack > cert-manager _ . See [ Download and install
cert-manager
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/install-
download-cert-manager-istio#download-and-install-cert-manager) .

####  Anthos Service Mesh

Apigee hybrid uses the Istio distribution provided with Anthos Service Mesh
(ASM) version 1.5.x to create and manage the runtime ingress gateway. See [
Download and install ASM
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/install-
download-cert-manager-istio#download-and-install-asm) .

###  Environment groups

Environment groups allow you to logically group environments together.
Environments within each group share the same hostnames. You can group
environments by function, by hostname address, by region if you are
implementing a multi-region hybrid installation, or by any other metric you
choose.

Environment groups provide the same routing features provided by the `
virtualHosts ` property in Apigee hybrid version 1.2.

See [ About environment groups
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/environment-
groups-about) .

###  New CLI command

The following new commands were added to the apigeectl CLI. For more
information about each command, see [ apigeectl
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/cli-reference)
.

Command  |  Description  
---|---  
` encode ` |  Returns a list of encoded names of all the ApigeeDeployments for
the specified organization or the specified environment within the specified
organization.  
  
###  CLI flag changes

The following new flags were added to the apigeectl CLI. For more information
about each command, see [ apigeectl
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/cli-reference)
.

Flag  |  Status  |  Description  
---|---|---  
` --all-envs ` |  New  |  Applies the apigeectl command to all environments
under the organization specified in your overrides config file.  
` --env ` |  New  |  Applies the configuration to the specified organization  
` --datastore ` |  New  |  Applies the configuration to the datastore scope
(Cassandra).  
` --dry-run ` |  Changed  |  Arguments depend on the version of kubectl you
are using:

  * kubectl version 1.7.x or older: ` ‑‑dry‑run=true `
  * kubectl version 1.8.x or newer: ` ‑‑dry‑run=client `

  
` --org ` |  New  |  Applies the configuration to the specified organization.  
` --telemetry ` |  New  |  Applies the configuration for telemetry components:
apigee-logger and apigee-metrics.  
` -c, --components ` |  Removed  |  Instead, apply changes by env, org,
datastore, or telemetry scopes.  
  
###  Unique hashed values for organization and environment names

Apigee hybrid now uses a unique hashed value to keep track of organization and
environment names. This avoids errors when org and env names are too long to
concatenate. You can see the hashed values with the ` apigeectl encode `
command. For example:

    
    
    $ ./apigeectl encode --org hybrid-example
    List of ApigeeDeployments are:
      apigee-connect-agent-hybrid-example-6a82f8a
      apigee-mart-hybrid-example-6a82f8a
      apigee-watcher-hybrid-example-6a82f8a
    
    $ ./apigeectl encode --org hybrid-example --env example-env
    List of ApigeeDeployments are:
      apigee-runtime-hybrid-example-example-env-9e87e2d
      apigee-synchronizer-hybrid-example-example-env-9e87e2d
      apigee-udca-hybrid-example-example-env-9e87e2d
    $

See [ apigeectl
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/cli-reference)
.

###  New axHashSalt configuration property

A new org-level configuration property, axHashSalt, was added. This property
lets you specify the name of a Kubernetes secret that contains a hashing salt
value used to encrypt [ obfuscated user data
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/obfuscate-
userdata-for-analytics) sent to Apigee analytics. For more information, see
the [ Configuration property reference
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/config-prop-
ref) .

###  Added support for mTLS on the Istio ingress

You can configure [ mTLS
](https://en.wikipedia.org/wiki/Mutual_authentication) . on the Istio ingress.
For more information, see [ Configuring mTLS
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/ingress-
tls#configuring-mtls) .

###  Watcher

Apigee Watcher pulls virtual hosts related changes for an org from
synchronizer and makes necessary changes to configure istio ingress.

Watcher introduces:

  * New service account: apigee-watcher 
  * New role: Apigee Runtime Agent 
  * New configuration property: watcher 

See [ Create service accounts
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/install-
download-install#create-service-accounts) and the [ Configuration properties
reference
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/config-prop-
ref#watcher) .

###  GA of the OASValidation policy

The OASValidation policy is now GA.

###  Apigee Connect enabled by default

Apigee Connect is now GA and is enabled by default for all new Apigee
installs. See [ Apigee Connect
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/apigee-
connect) .

###  Metrics enabled by default

Metrics are enabled by default for all new Apigee hybrid installations. See [
Configure metrics collection
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/metrics-
enable) .

###  Changes to the ` virtualHosts ` configuration property

Use environment groups to configure routing rules. This replaces the
virtualHosts:routingRules property. See [ Configuring virtual hosts
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/base-path-
routing) and [ About environment groups
](https://cloud.devsite.corp.google.com/apigee/docs/hybrid/v1.3/environment-
groups-about) .

###  Changes to product limits

The following default limits have been changed:

Limit  |  New value  
---|---  
Message logging payload  |  11 mb  
Target connection timeout  |  600 seconds  
  
##  Bugs fixed

The following bugs are fixed in this release. This list is primarily for users
checking to see if their support tickets have been fixed. It's not designed to
provide detailed information for all users.

Issue ID  |  Description  
---|---  
153755536  |  An issue was fixed where a long environment and/or organization
name caused an error. Org and env names are now truncated to prevent this
problem from occurring. A 32 character limit is also now enforced for org and
env names.  
155913227  |  An issue was fixed where the runtime was unable to connect to
the UDCA (fluentd) endpoint even though UDCA is healthy.  
155913227  |  Unable to connect to UDCA (fluentd) pod  
153755536  |  Error received when environment length is long  
  
##  Known issues

The following table describes the known issues for this release:

Issue  |  Description  
---|---  
161658025  |  Inaccurate deployment status for Shared Flows

For Shared Flows, the deployment status is not being reported correctly to the
UI, resulting in an indefinitely spinning deployment icon. If you have
deployed a Shared Flow and see the spinning deployment icon, you must assume
that the deployment has in fact failed.

To obtain the correct deployment status, use the [
v1.organizations.environments.sharedflows.revisions.deployments
](https://cloud.devsite.corp.google.com/apigee/docs/reference/apis/apigee/rest#rest-
resource:-v1.organizations.environments.sharedflows.revisions.deployments)
API. For example:

` curl -s -H "$AUTH" \ `

`
"https://apigee.googleapis.com/v1/o/$ORG/e/$ENV/sharedflows/$FLOW/revisions/$REV/deployments"
`  
  
146222881  |  Invalid HTTP Header error: The Istio ingress switches all
incoming target responses to the HTTP2 protocol. Because the hybrid message
processor only supports HTTP1, you may see the following error when an API
proxy is called:

` http2 error: Invalid HTTP header field was received: frame type: 1, stream:
1, `

` name: [:authority], value: [domain_name] `

If you see this error, you can take either of the following actions to correct
the problem:

  * Modify the target service to omit the Host header in the response. 
  * Remove the Host header using the AssignMessage policy in your API proxy if necessary. 

  
  
143659917  |  The PopulateCache policy's expiration setting must be set to an
explicit value between 1 and 30. For example:

` <ExpirySettings> `

` <TimeoutInSec>30</TimeoutInSec> `

` </ExpirySettings> `

