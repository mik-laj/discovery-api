**NOTE:** Some aspects of this product are in Beta. The hybrid installation
options are GA. To join the Beta program, reach out to your Apigee
representative.

#  Apigee Adapter for Envoy release notes

For more information, see the following resources:

  * _[ Apigee Adapter for Envoy documentation ](/api-platform/envoy-adapter/latest/concepts) _
  * _Questions or issues?_ Contact [ Apigee Support ](https://cloud.google.com/apigee/support/)
  * _Release notifications_ : Go to [ Apigee Release Schedule ](https://status.apigee.com) and click the **Subscribe To Updates** button 

##  v1.0.0

On Friday, July 31, we released the GA version of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you
**must** add the ` --force-proxy-install ` flag to the ` provision ` command.
This flag forces the Apigee proxy to be replaced with the latest proxy. See [
Apigee hybrid example ](/api-platform/envoy-adapter/latest/example-hybrid) .

##  Supported platforms

We publish binaries for MacOS, Linux, and Windows.

We publish docker images from scratch, Ubuntu, and Ubuntu with Boring Crypto.

In version 1.0.0 we support the following platforms:

  * Apigee hybrid version 1.3 
  * Istio versions 1.5, 1.6 
  * Envoy versions 1.14, 1.15 

###  Additions and changes

Between the v1.0-beta4 release and GA, the following additions changes were
made to the adapter:

  * **Go Boring builds**

A new build is now available that uses [ FIPS compliant Go BoringSSL libraries
](https://kupczynski.info/2019/12/15/fips-golang.html) .

  * **Log level flag changes**

The logging level flags for the apigee-remote-service-envoy service have been
changed for consistency:

Old flag  |  New flag  
---|---  
` log_level ` |  ` log-level `  
` json_log ` |  ` json-log `  
  * **New CLI flags**

New flags were added to the CLI ` token ` commands:

Flag  |  Description  
---|---  
` --legacy ` |  Set this flag if you are using Apigee Edge Cloud.  
` --opdk ` |  Set this flag if you are using Apigee Edge for Private Cloud.  

