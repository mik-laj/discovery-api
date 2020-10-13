**NOTE:** Some aspects of this product are in Beta. The hybrid installation
options are GA. To join the Beta program, reach out to your Apigee
representative.

#  20.08.05 - Apigee integrated portal release notes

On Wednesday, August 5, we will begin releasing a new version of the Apigee
integrated portal.

**Resources** :

  * **Questions or issues?** Contact the [ Apigee Community ](https://community.apigee.com/index.html) or [ Apigee Support ](https://community.apigee.com/page/apigee-customer-support) . 
  * Subscribe to release notifications: Go to [ http://status.apigee.com ](https://status.apigee.com) and click **Subscribe to Updates** . 

##  Bugs fixed

The following bugs are fixed in this release. This list is primarily for users
checking to see if their support tickets have been fixed. It's not designed to
provide detailed information for all users.

Issue ID  |  Component Name  |  Description  
---|---|---  
162383847  |  Integrated Portal  |

**Error when activating/deactivating developer account**

An issue has been fixed in the UI that was causing an error similar to the
following (which could be ignored) when activating/deactivating a developer
account:  
` Unable to update user status `  
  
161985144  |  Integrated Portal  |

**External spec URLs do not support redirects**

When importing an OpenAPI Specification using a URL redirects will not be
followed.  
  
161421338  |  Integrated Portal  |

**Duplicate developer programs created and unable to delete**

Developer programs that are not in use by an integrated portal will no longer
be displayed.  
  
161354897  |  Integrated Portal  |

**500 error thrown when creating an integrated portal with existing portal
name**

When creating an integrated portal with the same name as an existing portal,
an appropriate error message is provided.  
  
159946322  |  Integrated Portal  |

**Delete all artifacts when deleting a developer program**

When deleting a developer program, all artifacts that are associated with the
developer program are also deleted.  
  
159925336  |  Integrated Portal  |

**APIs page style changes**

The following changes have been implemented on the APIs page:

  * The **Filter by title and description** field now appears above API cards and spans the top of the page allowing for better visibility of API cards on small screens and 4 API cards to fit per row on a fully expanded browser window 
  * API cards on the APIs page have been made more responsive using CSS Grid Layout 

  
159871255  |  Integrated Portal  |

**Miscellaneous security fixes**  
  
149834093  |  Integrated Portal  |

**Request header` Content-type: application/json ` is getting added to GET
request **

An issue has been fixed that was causing the ` Content-type: application/json
` to be added to GET requests.  
  
148792711  |  Integrated Portal  |

**Read access to developer account information should not be available to all
users**

Read access to developer account information is now controlled by role, and
redacted for users that do not have organization adminstrator or portaladmin
roles.  
  
146486866,  
118358600  |  Integrated Portal  |

**OpenAPI Spec with media type of application/json-patch+json does not render
in SmartDocs** and  
**SmartDocs does not support formData parameters**

The APIs Explorer widget now allows for text input for more request body MIME
types, including JSON mime types ending with "+json", "application/xml",
"application/x-www-form-urlencoded". The full list of mime types that support
text input can be found here: [
https://github.com/codemirror/CodeMirror/blob/master/mode/meta.js#L15-L172
](https://github.com/codemirror/CodeMirror/blob/master/mode/meta.js#L15-L172)  
  
##  Known issues

For a list of known issues with the integrated portal, see [ Known issues with
the integrated portal ](/apigee/docs/release/known-issues#portal) .

