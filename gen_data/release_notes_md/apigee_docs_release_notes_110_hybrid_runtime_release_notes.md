**NOTE:** Some aspects of this product are in Beta. The hybrid installation
options are GA. To join the Beta program, reach out to your Apigee
representative.

#  1.1.0 - Apigee hybrid runtime release notes

On January 27, 2020, Google released Apigee hybrid runtime version 1.1.0. This
section describes new features and changes released in version 1.1.0.

**NOTE:** The Apigee APIs, Apigee hybrid UI, GCP integrated services, and
integrated portal are in [ Beta ](https://cloud.google.com/products/#product-
launch-stages) . All other Apigee hybrid components are GA. For more
information, see [ Versioning and terminology
](/apigee/docs/hybrid/terminology) .  For more information, see the following
resources:

  * _[ Learn more about hybrid ](/apigee/docs/hybrid/what-is-hybrid) _ or _[ Start installing ](/apigee/docs/hybrid/big-picture) _
  * _Create a paid account:_ Contact [ Apigee Sales ](https://pages.apigee.com/contact-sales-reg.html)
  * _Questions or issues?_ Contact [ Apigee Support ](https://cloud.google.com/apigee/support/)

##  Upgrading

You cannot upgrade from 1.0.0 to 1.1.0, and the new version is not backward
compatible with version 1.0.0. Version 1.1.0 requires a new installation.

##  New features and improvements

###  Apigee Connect (Alpha release)

Apigee Connect Alpha allows the Apigee hybrid MART service to connect to the
management plane without requiring you to expose the MART endpoint. If you use
Apigee Connect, you do not need to configure the MART ingress gateway with a
host alias and an authorized DNS certificate. For details, please contact your
Apigee representative.

###  Base path routing

Base path routing allows you to configure and manage how Apigee hybrid routes
API proxy calls to specific environments. For details, see [ Configure base
path routing ](/apigee/docs/hybrid/base-path-routing) .

##  Changes

The following changes have been made for hybrid runtime version 1.1.0. Some of
these changes, as noted, are **not backward incompatible** with version 1.0.0.

  * The ` apigeectl ` CLI now installs Istio in the ` istio-system ` namespace. This is the default namespace for Istio. This change is **backward incompatible** with hybrid version 1.0.0. 
  * The ` apigeectl ` CLI now installs CertManager into the ` cert-manager ` namespace. This change is **backward incompatible** with hybrid version 1.0.0. 
  * The supported version of Istio deployed with Apigee hybrid runtime has been migrated to 1.4.2 because version 1.2.x is no longer supported. 

##  Bugs fixed

The following issues listed in the Apigee hybrid 1.0.0 release notes have been
fixed:

Issue  |  Description  
---|---  
144886537  |  Base path routing is not working in Apigee hybrid v1.0.0. When
the overrides is setup to route to different environments with the same
hostAlias, the ingress does not route to the environment based on path.  |
143774187  |  The hybrid UI displays the label "Company" in the Apps view.  
  
##  Known issues

The following table describes the known issues for this release:

Issue  |  Description  
---|---  
N/A  |  You cannot use a "*" for the ` hostAlias ` property for both the `
mart ` and ` envs ` configurations. The best practice is to use a specific
hostname for the ` mart ` configuration.  
N/A  |  Setting ` HTTP_PROXY ` , ` HTTPS_PROXY ` , and ` NO_PROXY ` variables
is not supported in the Apigee Connect Alpha version.  
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
](https://cloud.google.com/hybrid/reference/apis/rest/v1/organizations.environments.apis.revisions.debugsessions/list)
does not include the session in this list. The API only includes sessions in
the response if the session contains at least one transaction.  
144436206  |  In the **Cache Performance** view, the Cache Hit Ratio
calculation is incorrect.  
144321491  |  Apigee hybrid logs "Creating missing cache" notifications that
indicate a potential performance degradation. These messages are expected and
can be ignored.  
144321144  |  Proxies with secure  virtual hosts cannot be reloaded.  
144286363  |

Debug mask in env.json does not mask response data.

The following API to update the env.json debug mask with a responseJSONPaths
field does not work:

    
    
    PATCH /v1/organizations/org/environments/env/debugmask?replaceRepeatedFields=true
    {
      "responseJSONPaths": ["$.maskedDataEnv"]
    }

To work around this issue with trace, you can delete an entire trace session
in the UI, or you can use the trace APIs to delete individual transactions
within a session.  
  
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

