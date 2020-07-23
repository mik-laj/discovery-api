**NOTE:** Some aspects of this product are in Beta. The hybrid installation
options are GA. To join the Beta program, reach out to your Apigee
representative.

#  1.0.0 (GA) - Apigee hybrid runtime release notes

On November 20, 2019, Google released Apigee hybrid runtime version 1.0.0.
This section describes bug fixes and known issues with version 1.0.0.

**NOTE:** The Apigee APIs, Apigee hybrid UI, GCP integrated services, and
integrated portal are in [ Beta ](https://cloud.google.com/products/#product-
launch-stages) . All other Apigee hybrid components are GA. For more
information, see [ Versioning and terminology
](/apigee/docs/hybrid/terminology) .  For more information, see the following
resources:

  * _[ Learn more about hybrid ](/apigee/docs/hybrid/what-is-hybrid) _ or _[ Start installing ](/apigee/docs/hybrid/big-picture) _
  * _Create a paid account:_ Contact [ Apigee Sales ](https://pages.apigee.com/contact-sales-reg.html)
  * _Questions or issues?_ Contact [ Apigee Support ](https://cloud.google.com/apigee/support/)

###  Known issues (GA)

The following table describes the known issues for this release:

Issue  |  Description  
---|---  
144886537  |  Base path routing is not working in Apigee hybrid v1.0.0. When
the overrides is setup to route to different environments with the same
hostAlias, the ingress does not route to the environment based on path.  
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
  
143774187  |  The hybrid UI displays the label "Company" in the Apps view.  
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
  
123932912  |  With zero-downtime deployment, when deployment of a new revision
fails, the original revision is still undeployed. You will have to re-deploy
the original revision in order to restore its deployment status.  
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

  
  
###  Bugs fixed

The following issues listed in the Apigee hybrid Beta 2 release notes have
been fixed:

Issue  |  Description  
---|---  
**133444606** |

The update developer apps API does not support all documented input fields.  
  
**133192879** |

There is a very high latency when using the API or UI to get your
organization's deployment status. This latency can result in an ` HTTP 204 (No
Content) ` or an ` HTTP 400 (Bad Request) ` response.  
  
**131111865** |

Synchronizer fails when file system gets too full. This is due to the
Kubernetes garbage collection process: it is not triggered until it reaches
85% by default.

Closed: Not reproducible.  
  
##  Unsupported Apigee Edge features

Google does _not_ plan to support the following features in Apigee hybrid:

  * APIs to: 
    * Manipulate KVM entries 
    * Search for or revoke OAuth access tokens (because tokens are hashed) 
  * Developer portal development using Drupal 7 
  * OAuth v1 or [ OAuthv1.0a policy ](/apigee/docs/api-platform/reference/policies/oauth-10-policy-policy)
  * [ ConcurrentRateLimit policy ](/apigee/docs/api-platform/reference/policies/concurrent-rate-limit-policy) rate limiting policy 
  * Trireme (EOL'd on 10/10/2019) 

For a full comparision of features between hybrid and Edge, see [ Compare
hybrid to Edge ](/apigee/docs/hybrid/compare-hybrid-edge) .

##  Next step

  * [ Learn more about hybrid ](/apigee/docs/hybrid/what-is-hybrid)
  * [ Start installing ](/apigee/docs/hybrid/big-picture)

