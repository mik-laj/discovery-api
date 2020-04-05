#  Release notes

This page documents production updates to Cloud Talent Solution. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/job-release-notes.xml `

##  April 03, 2020

**DEPRECATED:**

As of this date, Cloud Talent Solution Job Search v2 is no longer available.
Calls to v2 will result in error. The deprecation of v2 was first communicated
in August 2018.

##  December 05, 2019

**FEATURE:**

CTS has launched a new [ dashboard management tool
](https://console.cloud.google.com/talent-solution) . This new improvement
provides visual data to give you more insight into:

  1. How your job seekers are engaging with Job Search, by showing see top queries and locations by domain. 
  2. Whether Job Search is properly configured for your application, by showing inconsistencies in your search API integration. 
  3. Whether your client events are properly configured, by showing client events that you can correct or improve to take full advantage of Job Search's machine learning capabilities. 

##  December 03, 2019

**CHANGED:**

JS has improved the algorithm for better street resolution coverage. This will
give you more precise geolocation results when using commute search.

##  November 15, 2019

**FEATURE:**

The following fields have been added to SummarizedProfile:

  * ` group_id `
  * ` application `
  * ` assignment `

**FIXED:**

Bug fix: Required fields are now marked correctly in the BatchUpdateJobs
reference documentation.

**FIXED:**

Bug fix: CTS has fixed a bug that caused deleted companies to be counted
toward the company limit in a job distributor.

##  November 01, 2019

**FEATURE:**

CTS has added validation to ` job.workHour ` . ` workHour ` now allows hour
values between (0-23), otherwise a 400 error is returned.

**FEATURE:**

New enum CONTACT_AUTOMATED_SYSTEM has been added to ProfileEventTypes.

**FEATURE:**

JS has added new field ` query_language_code ` .

##  October 18, 2019

**FIXED:**

Bug fix: Job Search has fixed an issue that caused only some jobs in a
specific location to be returned, rather than all options matching the search
query.

**FIXED:**

Bug fix: Job Search has fixed an issue that caused only some of the results to
be returned when searching on the string "Chief accountant". All results to
this query string are now returned.

##  September 27, 2019

**FIXED:**

Bug fix: CTS has fixed a bug that caused the job export tool to generate fewer
results.

**CHANGED:**

All resource (Tenant, Job, Profile, and so on) Create/Update methods now
return any duplicated resource names in a structured error response to
ALREADY_EXIST errors.

##  August 30, 2019

**CHANGED:**

Job update time is now only tracked if the job was updated by a customer.

##  August 16, 2019

**FIXED:**

Bug fix: CTS has fixed a bug that caused information in the [ ` addresses `
](https://cloud.google.com/talent-solution/job-
search/docs/reference/rpc/google.cloud.talent.v4beta1#job) field to be
appended to ` structuredAddresses ` .

##  July 19, 2019

**CHANGED:**

The maximum size of the [ ` customAttributes `
](https://cloud.google.com/talent-solution/job-
search/docs/reference/rest/v4beta1/JobQuery) filter field of a job has been
increased from 3KB to 6KB.

##  July 02, 2019

**FEATURE:**

Cloud Talent Solution has launched a new [ Batch API
](https://cloud.google.com/talent-solution/job-
search/docs/reference/rpc/google.cloud.talent.v4beta1#batchcreatejobsrequest)
.

**FIXED:**

Bug fix: Cloud Talent Solution has fixed an issue where UpdateJob failed with
a 500 error if the job's name didn't have a ` tenant_id ` .

**CHANGED:**

New documentation added: Create an [ expired job
](https://cloud.google.com/talent-solution/job-
search/docs/reference/rest/v4beta1/projects.jobs#Job) .

**FIXED:**

Bug fix: Cloud Talent Solution has fixed issues related to histogramming
custom attribute facets. An empty histogram expression now throws an error
message.

**CHANGED:**

Cloud Talent Solution has added an exception for an invalid profile name.

##  June 03, 2019

**FEATURE:**

Cloud Talent Solution has launched new [ Batch
](https://cloud.google.com/talent-solution/job-
search/docs/reference/rest/v4beta1/projects.jobs/batchDelete) API calls. These
calls enable you to perform multiple operations at the same time. Note that
Batch API calls only apply to Job resources and CTS does not guarantee how
quickly they will be reflected in search or recommendation responses.

**FIXED:**

Bug fix: Compensation filters are now able to account for jobs that have no
compensation fields set.

**FIXED:**

Cloud Talent Solution fixed an issue that would not allow customers to upload
expired jobs. You are now able to create an expired job and link it to any
associated Application or Assignment records. When loading your historical
data, input the following values:

  * ` postingPublishTime ` =[timestamp when the job was created] 
  * ` postingExpireTime ` =[timestamp when the job was closed] 
  * ` requisitionState ` =[FILLED, LOST, CLOSED] 

##  May 14, 2019

**FEATURE:**

Cloud Talent Solution has launched the v4beta1 version of the API. You can
download these libraries from our Client Libraries page.

**FEATURE:**

Cloud Talent Solution has updated it's documentation to include more code
samples, and better structured examples on how to use the APIs.

**CHANGED:**

Cloud Talent Solution has added validation checks on timestamp related fields
on the job and profile entities.

**CHANGED:**

Customers can now set the ` group_id ` field with their values, rather than
having to use the Cloud Talent Solution auto-generated values for this field.

##  April 26, 2019

**FIXED:**

Cloud Talent Solution has fixed issues causing 500 status messages to be
returned due to discrepancies in the Profile object.

**CHANGED:**

Cloud Talent Solution now allows you to define your own ` group_id ` to
identify the same candidate across multiple profiles.

**FIXED:**

Cloud Talent Solution fixed issues causing the ` excludedJobs ` list in the
search API to work incorrectly.

##  March 15, 2019

**CHANGED:**

For invalid histogram expressions Cloud Talent Solution will now return a 400
response instead of a 500 response.

##  March 01, 2019

**FIXED:**

Fixed a bug in which jobs with multiple locations did not have any identifier
between each location. Added in double quotes as a delimiter between each
location.

##  February 08, 2019

**CHANGED:**

**Additional Commute Search modes:** Cloud Talent Solution now supports
walking and cycling modes of transit for Commute Search.

##  January 21, 2019

**FEATURE:**

**Rank by distance:** Cloud Talent Solution now allows you to order search
results by distance based on a specified location.

**CHANGED:**

**Simplified client events in v3:** Simplified client events provides provides
a set of APIs to implement client events in a clean, easy-to-use manner.

##  January 07, 2019

**CHANGED:**

**Increased the max characters for languageCode:** Cloud Talent Solution now
accepts locale strings from 10 to 16 characters.

**FIXED:**

Fixed a bug which was slowing the performance of the CTS Self-Service Tools.

**FIXED:**

Fixed a bug in which jobs with multiple street addresses were returning only
the first address. Creating job will now return all job locations in
STREET_ADDRESS type if job location is successfully resolved to street
address, otherwise returning job addresses in extracted location type.

##  December 14, 2018

**FEATURE:**

**Diversification level available in v3:** [ DiversificationLevel
](https://cloud.google.com/talent-solution/job-
search/v3/docs/reference/rest/v3p1beta1/DiversificationLevel) controls whether
or not highly similar jobs are returned next to each other in the search
results and is now available in v3 of the API.

##  October 19, 2018

**FEATURE:**

**Cloud Talent Solution now available on APIs Explorer:** Cloud Talent
Solution is now available on [ APIs explorer ]() . Learn more about using APIs
Explorer.

**FEATURE:**

**Multiple languageCodes for auto-complete API:** Cloud Talent Solution now
allows you to specify multiple languageCode filters for the autocomplete API.

**CHANGED:**

**Compensation information now modifiable:** Cloud Talent Solution now allows
you to modify the compensation information of a job using the updateJob API
call.

**CHANGED:**

**Improved error messages:** Cloud Talent Solution has added more context to
error messages that are generated when updating the compensation information
of a job.

##  September 24, 2018

**FEATURE:**

**New beta version:** Cloud Talent Solution has launched a beta version of the
API suite that now supports three additional features - [ custom ranking
](https://cloud.google.com/talent-solution/job-search/v3/docs/custom-ranking)
, [ new histogram expression ](https://cloud.google.com/talent-solution/job-
search/v3/docs/histogram-expression) and, a [ new Pub/Sub API set
](https://cloud.google.com/talent-solution/job-search/v3/docs/quickstart-
pubsub) .

**CHANGED:**

**Improved access control:** Cloud Talent Solution has introduced stronger
access control measures that give developers more flexibility to control data
permissions through Google Cloud Console. See the [ access control
documentation ](https://cloud.google.com/talent-solution/docs/iam) for more
information.

**CHANGED:**

**One-sided compensation ranges:** Previously, Cloud Talent Solution required
both the max and min ranges to be set while defining the compensation range.
This requirement has now been alleviated.

**FIXED:**

**v3 orderBy values:** Previously, Cloud Talent Solution documentation
suggested that orderBy values such as ` postingPublishTime ` would be
accepted, but the API only accepted ` posting_publish_time ` . This has now
been fixed. Cloud Talent Solution will accept both versions and also
capitalized versions of the same values.

##  August 27, 2018

**FEATURE:**

**Military occupational speciality code:** Cloud Talent Solution is proud to
launch a new feature that enables veterans to search for jobs using their
military occupational speciality code.

##  August 03, 2018

**FEATURE:**

**Cloud Talent Solution is now generally available.**

**FEATURE:**

**v3 schema** : Cloud Talent Solution has launched v3 of the job search API.
New customers should use the v3 schema to integrate with the API. Existing
customers on V2 of the API are encouraged to migrate to the new schema as soon
as possible. The v2 version of the Job Search API will continue to be
supported until 8/23/2019. Most new features are only available on the v3.

**FIXED:**

**nextPageToken not yielding page results** : In some cases, using the
nextPageToken to get the next page of results yielded empty search results.
This behavior is now fixed.

##  June 29, 2018

**FEATURE:**

**New method for tagging bot traffic** : Added a BOT device type to indicate
if the device used by the job seeker at the time of the call to the service is
a bot.

##  June 13, 2018

**FEATURE:**

**Cloud Talent Solution is now in an open beta.**

**FEATURE:**

**Self-service tools launched** : Cloud Talent Solution has released some
self-service tools to assist with smoother integration and monitor usage of
the API. Follow the directions in our documentation to learn more.

**FEATURE:**

**New data centers in Europe** : Cloud Talent Solution has opened data centers
in Belgium and the Netherlands to route traffic of European customers and
reduce the overall latency of the service.

**FIXED:**

**Autocomplete issues with different languageCodes** : Previously, Cloud
Talent Solution incorrectly parsed languageCode values in the complete API
request. This is now fixed.

**FIXED:**

**Inability to parse keywords with non-alphanumberic characters** :
Previously, Cloud Talent Solution was unable to parse queries such as A.B.C.D
and match them against literals in the job description field and custom
attribute fields. This is now fixed.

**CHANGED:**

**Limit distributorCompanyId size** : The distributorCompanyId field of a job
now has a limit of 255 characters.

##  May 04, 2018

**CHANGED:**

**Job expiration changes** : This release extends the allowed retention period
for expired jobs within the Google database from 60 days to 90 days (default)
and, [ upon request ](https://cloud.google.com/talent-solution/docs/support) ,
up to 360 days. This release also allows for updating expired jobs (including
re-setting the expiration date of an expired job to a future date) and
updating the ` expireTime ` field introduced in the last release. ` expireTime
` allows customers to set the format of an expiration date to a DateTime (ms
timestamp) instead of a Date at 0:00 UTC. In cases where both the ` expireTime
` and ` expiryDate ` are added to a job, the ` expireTime ` takes precedence.

**CHANGED:**

**Restriction on number of Location filters** : This release restricts the
number of Location filters to no more than 5.

**FIXED:**

**Limit autocomplete results to specific languageCode** : Previously, for `
complete ` API requests, if ` languageCode ` included "en-US" Cloud Job
Discovery incorrectly discarded the "US" bit and returned all jobs with `
languageCode ` starting with "en" even if the search language code had been
set to "en-US". Now only jobs corresponding to the ` languageCode ` are
returned.

**FEATURE:**

**Quota lookup for Google Cloud Projects** : Customers of Cloud Job Discovery
can view the quotas allocated to their Google Cloud Projects by looking up the
[ APIs & Services ](https://console.cloud.google.com/apis/) section of the
Google Cloud Console. If you require more quota than has been allocated, file
a ticket from our [ support page. ](https://cloud.google.com/talent-
solution/docs/support)

##  April 13, 2018

**CHANGED:**

**API Schema changes** : Cloud Job Discovery has added several new fields in
the schema and corresponding deprecated fields in order to standardize the
naming of fields. Deprecated fields have been marked "deprecated" in the
schema.

**DEPRECATED:**

**Several List APIs deprecated** : Several list APIs such as `
listCustomFields ` , ` listJobCategories ` , etc are now deprecated. This
should not impact existing customers since the APIs have been non-active for
the past several months.

**FEATURE:**

Cloud Job Discovery has released new ` customAttribute ` fields on jobs. These
fields work in a similar manner to the existing ` filterableCustomFields ` ,
with the following new features:  
**Define your own custom field name** : The advanced custom fields allow you
to define your own name for the custom fields, rather than use a specific
index value (as is the case in regular custom fields)

  * **Case insensitive search** : The search request is now able to specify if a case sensitive or case insensitive match is required. 
  * **Support for numeric values** : ` customAttributes ` can store either string or numeric values. 
  * **Range based filtering** : ` customAttribute ` search filters can filter jobs between a range of specified values. For example, if a given ` customAttribute ` field is used to store salary information, the ` customAttribute ` filter can be used to return jobs with a certain salary, jobs with a salary greater than a specified value, jobs between a range of specified values, etc. 
  * **Cross-field filtering** : Advanced custom fields also provide customers of Cloud Job Discovery with the ability to define expressions that filter a combination of advanced custom field values. For example, a customer has business logic that states they only want jobs that sponsor visas, or jobs paying more than $100K. A customer can use one advanced custom field to indicate if the job is sponsored, and another for the salary. The customer can then specify a search filter with an expression that defines the logic needed. Only 3 levels of nested expressions are supported. 
  * **Keyword specific search** : Specify a certain ` customAttribute ` in the ` keywordSearchableCustomAttribubte ` of the associated company to ensure search requests that contain a value in the specified custom field return the jobs that contain this value in that custom field. 
  * **SQL based searches:** strong> ` customAttributes ` allows you to define boolean-style expressions in the search request. Cloud Job Discovery automatically parses these expressions, applies the filters to the search request, and returns results accordingly. 
  * **Define custom histogram buckets:** ` customAttributes ` allow customers of Cloud Job Discovery to set custom buckets by which histograms can be calculated. For example, you can use a customAttribute to store salary information, and then create a histogram on the field. You can further create buckets from 10000 - 20000, 20000 - 30000, etc to group all the salaries within these buckets. 

**FEATURE:**

**Merged Search and Histogram call** : The search API structure has been
modified to include a request for a histogram in the same call. This merged
search and histogram API call is backward-compatible, to ensure that you can
continue to use it as before. The histogram returned as a part of this call
respects all the filters of the associated search.

**CHANGED:**

**Change to the way CJD returns fields** : Cloud Job Discovery will no longer
return empty or NULL job fields in the search results. If a job has been
created without a certain field (for example, the ` compensationInfo ` field)
or if this field is set to NULL, the search response will not contain this
field.

**FEATURE:**

**New API for Search for Alerts** : There is a new Search API endpoint - `
searchJobsForAlerts ` that has been created exclusively to provide relevant
job content targeted to passive job seekers (such as for email alert
campaigns). This API is preferred over the current means of specifying the
MODE of a ` searchJobs ` API call to ` EMAIL_ALERT_SEARCH ` . Customers can
also see the quota associated with this type of search in the Google Cloud
Console under the PeriodicTaskGroup.

**CHANGED:**

**Compensation histogram change** : A request to generate a histogram by
compensation does not accept the same searchType to be repeated more than once
on a single request.

**FEATURE:**

**New expiration date features** : A new field - ` expireTime ` has been
introduced on the job object. This field allows customers of Cloud Job
Discovery to specify the exact time a job is set to expire.

**FIXED:**

**nextPageToken throwing 500 error on broadened errors** : Previously, Cloud
Job Discovery was incorrectly throwing 500 errors on search requests that had
the pageToken set such that the set of returned results were only broadened
results ( by setting the flag ` enableBroadening ` to true). This has been
fixed.

**FEATURE:**

**Use regionCode to specify preferred language** : Cloud Job Discovery has
introduced an optional search parameter regionCode to specify the preferred
country in which jobs are to be found in. For example, by setting this field
to UK, a location-based search for jobs in Reading would return jobs in
Reading, UK as opposed to Reading, MA, USA.

##  March 19, 2018

**CHANGED:**

**Improvements to inferred street address coverage** : Cloud Job Discovery can
now infer the street address of more jobs where the actual street address is
not provided. This directly improves the accuracy of searches by commute time
and gives job seekers more visibility into the actual location of the job.

**FEATURE:**

**Allow to update expired jobs** : Updating expired jobs is now supported.
Expired/deleted jobs can also now be reactivated by updating the expiryDate
field. However, a job cannot be reactivated, if there is already an open job
with the same companyName, requisitionId, and locale.

**FIXED:**

**The requestMetadata fields in the search request are now required fields** :
The requestMetadata fields in the search request are now required fields.
Search requests that do not include this information are rejected with a 4xx
error. Customers who have existing Cloud Job Discovery accounts as of
3/12/2018 are exempt from this requirement, but are encouraged to send these
fields with every search request, to maximize the improvements gained from
Cloud Job Discovery.

##  March 09, 2018

**FEATURE:**

**Compensation Currency filter** :A compensation currency filter is now
available. This filter can be set on the search call to ensure only jobs with
a specified currency denomination are returned.

**CHANGED:**

**Create and Update calls are now asynchronous by default** : The default
behavior of job creation and update API requests is now asynchronous.

**FIXED:**

Minor fixes have been made to the accuracy of the histogram API.

**CHANGED:**

**Completion API by company modification** : Completion API suggestions for
company type-aheads will no longer include companies that have no open jobs.
For example, a complete API call for the query "Goog" will not return "Google"
as a suggestion if the company defined as Google in your system does not have
any open jobs.

**FEATURE:**

**New user behavior event** : A new event type,
APPLICATION_REDIRECT_FROM_SERP, has been added to provide the added
flexibility of representing an event where a job seeker tried to apply for a
job from the search results page and was immediately taken to a different
domain to complete the application process.

**DEPRECATED:**

**Removal of telecommmute flag from Job benefits** : The "telecommute" option
has been removed from the job benefit type. Customers are instead encouraged
to set the TELECOMMUTE option under the Region field for jobs that do offer
remote work as an option.

**FEATURE:**

**Histogram support for compensation based filters** : The compensation
filters in the V2 libraries now include histogram support. The API will now
also generate histograms based on the compensation information. This would
support functionality such as providing job counts for filtering by
compensation amount, filtering by currency, etc.

**FEATURE:**

**Sort jobs by compensation** : The API will now allow job seekers to sort
jobs based on compensation information.

##  February 09, 2018

**FEATURE:**

**Commute search in V2** : Searching for jobs by commute time is now possible
in V2 of Cloud Job Discovery. This can be done by setting the CommuteFilter of
the search request. Look up this tutorial for instructions on how to use the
commute filter.

**FEATURE:**

**Extended Compensation Filters** : Jobs can now be created with additional
information regarding overall compensation using the extendedCompensationInfo
field. The extended compensation can further be filtered against using the
extendedCompensationFilter of the search request. This can be further used to
**filter by a range of salaries** , **histogram by salaries** , etc.

**FIXED:**

More use cases that lead to error messages are being tagged with a unique
requestId to help troubleshooting.

**CHANGED:**

**Improved Job recall and counting** : Cloud Job Discovery can now return up
to 5000 jobs with an accurate result count (by setting the search field
enablePreciseResultSize and looking up the totalSize field in the search
response.

**FEATURE:**

**Reduced latency of search calls** : The end to end latency of Cloud Job
Discovery search calls has been reduced.

##  November 21, 2017

**FIXED:**

**Job Language Code** : Fixed a bug where language code "id_id" was converted
to "in_in".

**FIXED:**

**Compensation Filter** : Providing a minimum compensation value that is
greater than the maximum compensation value will now result in an HTTP 400
response code (BAD REQUEST).

**FEATURE:**

Expired jobs are now available for 60 days via jobs.get. Expired jobs are
read-only.

##  November 05, 2017

**FEATURE:**

**Search Offset** : The offset field is now included in the search request.
You can use this field to specify the page of results to return.

**FIXED:**

The histogram call no longer returns a 500 error when the compensation filter
is specified

**FIXED:**

The histogram call now returns an accurate job count for the specified
filters.

**FIXED:**

The completion API now returns values if the scope of the request is specified
as "TENANT".

**FIXED:**

In some cases, deleted/expired jobs were being returned as part of the search
results. This behavior has now been corrected. Deleted/Expired jobs will not
be returned in the search results.

##  October 25, 2017

**FEATURE:**

**Search by Requisition ID** : Recruiters can now specify a particular Job
RequisitionID to search for using the construct _Req:123-somerequisitionId_ in
the query string.

**FEATURE:**

**Specify custom fields that a regular search can match against** : Use the
keywordSearchableCustomFields field of the company object to define which
custom fields a regular search can match against. For example, if this field
contains the values [1,5,10], and the query string is "abcd", then a search
call on this company would also return jobs in which the value "abcd" is in
custom field 1,5 or 10.

**FEATURE:**

**New Histogram facet - Company_Title**

**FEATURE:**

**Delete Jobs by RequisitionID** : There is now a new API call to delete all
jobs with a specific requisitionID. An error will be thrown if the
JobReqisitionID does not exist.

**FEATURE:**

**Filter by Salary** : New JobFilter to filter jobs within a specific salary
range. If a job contains the compensationAmount, the filter will be applied to
the compensationAmount. If a job has no compensationAmount, but does have a
compensationAmountMin and compensationAmountMax, the filter will be applied to
that range (inclusive of range limits).

**CHANGED:**

**Expiration date restriction** : Jobs can now have a maximum expiration date
of 2100/12/31. Any job creation with an expiry date outside this range will
throw an error message.

**CHANGED:**

**Improvements to histogram accuracy** : Improvements have been made to the
accuracy of the histogram count. V2beta1 users must now mandatorily include
the RequestHeader in the histogram call. The requestHeader must be exactly the
same as that of the associated search call.

**FIXED:**

Errors are no longer thrown in certain cases where the location is empty
during job creation/updation.

**FIXED:**

**Improvements to location resolution and latency**

**FIXED:**

Fixed a typo that returned "Singapore, " instead of "Singapore" as a value in
the histogram results.

**FIXED:**

**Detection of job titles and employment types** : Queries such as "intern"
will now look for jobs with an employment type as intern as well as jobs with
the keyword "intern" in the job title or description

**FIXED:**

Fixed a bug that prevented updation of the compensationAmount field to null.

**FIXED:**

Fixed a bug that disregarded the location filter of a search in V2.

##  September 26, 2017

**FEATURE:**

Announcing Cloud Job Discovery private beta release. See the Cloud Job
Discovery Documentation.

##  August 09, 2017

**FEATURE:**

**New Histogram Filter Job_ADMIN1_COUNTRY** : Clients can now retrieve a
histogram by both State (or equivalent) and Country.

Sample response:

    
    
    {
    results:
      {"results":
        [
          {
            "field":"JOB_ADMIN1_COUNTRY",
            "values":
              {
                "WA, US":1,
                "CA, US":3,
                "NJ, US":1,
                "ON, CA":2
              }
          }
        ]
      }
    }
    

**FEATURE:**

**Disable street address identification** : A new flag to disable street
address identification has been introduced to allow clients to explicitly
disallow the API from identifying the underlying street address of a job
during job creation. This is intended for use for staffing agencies where the
identified company address may not correspond to the actual job location.

**FEATURE:**

**New Jobs Analytics tracking event** : A new Pub/Sub event type
APPLICATION_COMPANY_SUBMIT has been added for staffing agencies who submit the
application on behalf of the candidate.

**FIXED:**

**400 errors while updating the same job successively** : The API no longer
throws 400 FAILED_PRECONDITION errors when clients send multiple update
requests at the same time.

**CHANGED:**

**Improvements to error reporting capabilities** : Error reporting and
handling capabilities of the API have been improved. We expect no changes to
the underlying functionality, however, the error messages may have new
formatting in some cases.

##  July 26, 2017

**FEATURE:**

**State and Nationwide Job Posting** : Customers will now be able to specify
certain jobs as Statewide or Nationwide, with these jobs appearing in the
search results of cities within that state or country.

**FEATURE:**

**Contractor for Hire Employment Type** : A new employment type, Contractor
For Hire, has been introduced.

**FEATURE:**

**New Method for email alert Search** : A new search API endpoint has been
introduced specifically for search that provides results to be sent in job
alert emails. The use of this endpoint will help improve relevance for this
use case in the future.

**FEATURE:**

**Search for Jobs published in the last 3 days** : A Published Date type,
PAST_3_DAYS, has been introduced.

**FEATURE:**

**Improved location resolution for commute search** : Commute search will now
give higher relevance scoring to jobs with a specified street level address.

**FIXED:**

**Different SortBy options return different number of results** : The sortBy
option was previously returning a different number of results for sorting by
Published Date and sorting by Title. This issue has now been resolved. The
expected behavior is that sorting by all options except for sorting by
relevance will have the same number of results returned.

##  June 13, 2017

**FEATURE:**

**Histogram by Job Category** : The Histogram API now provides the option to
get a histogram by Job Category.

**FIXED:**

**Resolved Internal Server Error messages** : Internal server error messages
have been resolved for the following cases:

  * Creating a duplicated job. 
  * Calling the listCompanies API or the listCompanyJobsAPI with a negative page size. 
  * Creating a job with a negative compensationAmount, compensationAmountMin or compensationAmountMax. 

**FIXED:**

**Sort By Updated Date** : The sortBy field on UPDATED_DATE_DESC has been
fixed.

**FIXED:**

**JobCategory ANIMAL_CARE** : The JobCategory ANIMAL_CARE has been enhanced to
better recognize related jobs.

##  June 01, 2017

**FEATURE:**

**Commute Search** : The ability to search for jobs by commute time is now
available for initial testing. This feature is experimental and is subject to
improvements and changes in future releases.

**FEATURE:**

**Integration Account Indexing** : Integration accounts will now have instant
indexing capabilities. Jobs uploaded to our database will be searchable within
moments. Queries which cannot be indexed due to quota restrictions will return
an exception and will have to be retried.

**CHANGED:**

**Pub/Sub Event Schema:** Some field names in the pub/sub event schema have
been modified to comply with industry-standard naming conventions. Backward
compatibility support for the old fields exists, but you are encouraged to
work with the Cloud Job Discovery support team to establish a migration
timeline.

**CHANGED:**

**Pub/Sub Event Types:** Specific application types are now available to
record quick applies and apply redirects. If your service offers these
features, consider implementing them to improve search relevancy.

**CHANGED:**

**Company HQ Location:** The Company HQ location parameter has been changed to
be an optional value. Providing this field may increase the relevance of
location-based searches.

