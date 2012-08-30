---
layout: page
title: SMART 0.5 App + Container Update Guide
includenav: smartnav.markdown
---
{% include JB/setup %}

<div class='simple_box'>
  This is highly preliminary, not a commitment or final version of any
  particular API or data model. This is purely for internal collaboration and
  preview purposes.
</div>


<div id="toc"></div>


# What's new in SMART 0.5

## Filtering and Pagination Capabilities

The SMART API GET calls that return multiple medical data objects (i.e.
have "multiple" cardinality) now support parameters for restricting the
result set based on filters and pagination. A SMART application can use
these to request from the server, for instance, the first 10 lab results
that have LOINC code of `29571-7` or `38478-4` and have occured between
January 1, 2010 and December 31, 2012.

The REST call path for such a call will be:

`/records/1234567/lab_results/?loinc=29571-7|38478-4&date_from=2010-01-01&date_to=2012-12-31&limit=10&offset=0`

The RDF that the app receives from the server in reponse to this request
contains only the results matching the filters. Also, the RDF contains a
`ResponseSummary` object describing the result set.

For further information please see <http://dev.smartplatforms.org/reference/filters>


## New Data Models and Consistency Improvements

SMART 0.5 adds support for API calls and data models for procedures,
clinical notes, and smoking history. We have also improved the existing
data models in a a number of ways:

   * More consistent date handling
   * More consistent model and API call names
   * More consistent call categories (record, user, container) and cardinalities
     (single, multiple) describing the the context of the call and the
     type of the result set
     
For further information please see <http://dev.smartplatforms.org/reference/data_model/>


## JSON-LD Payloads in the SMART Connect Client Library

The SMART Connect JavaScript library now comes with built-in JSON-LD
payload transcoding that can be used as an alternative to the RDF graph.

See [the introduction to JSON-LD](/datamodel/intro_to_jsonld/) for details.

## Container Manifest API

The SMART Container no longer exposes the `/version` and `/capabilities` API
calls. Instead, there is now a unified `/manifest` call that exposes an 
all-in-one JSON descriptor of the container. To see an example of what
it looks like, please visit: <http://sandbox-api.smartplatforms.org/manifest>


## New and Improved Sample Apps
   * The _API Verifier_ app has been updated to support SMART 0.5 container
     validation. Also the API Verifier is now able to validate SMART
     app manifests.
     
   * The _Blood Pressure Centiles_ app has been updated to provide progressive
     loading capabilities (both manual and authomated) that are configurable
     by the person hosting the app. The app takes advantage of the new
     pagination capabilty of the SMART 0.5 containers.
     
   * Last but not least, we have added a new app to our sample apps collection
     called _Diabetes Monograph_. It is an exciting app that allow clinicians
     to analyze their patient's records with respect to the diabetes disease.

     
# How to Update Your SMART Apps to SMART 0.5

## Updating Your API Call Names

Both the SMART Connect (JavaScript) and SMART Python clients have been updated
to support a new common naming convention for the API call convenience methods.
In order to use these libraries, you will have to update the names of the API
call methods that you use in your apps. For example, in a SMART Connect app,
if you use a call like `SMART.PROBLEMS_get()`, you will need to change it to
`SMART.get_problems()`. Similarly, in a SMART REST app, you will have to change
`smart_client.records_X_problems_GET()` to `smart_client.get_problems()`. Please
note that the vital signs model (and the related call) have been renamed to
Vital Sign Sets for consistency with the remaining API cals. For a complete
list of the convenience method names in the SMART 0.5 clients, please see
<http://dev.smartplatforms.org/libraries/javascript/>


## Taking Advantage of the New SMART 0.5 API Features

You may want to consider trying out the JSON-LD payload format provided by the 
SMART Connect client as an alternative to the RDF graph payload, if you are 
more comfortable working with a hierarchical object model without having to
write SPARQL queries.

Also, you can take advantage of the new clinical notes, procedures, and smoking
history data models, as well as the filtering and pagination call parameters.
Here is how you can execute a SMART API call with filters via the Python and 
JavaScript clients:

JavaScript: `SMART.get_lab_results({loinc: "29571-7|38478-4", limit: 10})`
Python: `smart_cient.get_lab_results(loinc = "29571-7|38478-4", limit = 10)`


# How to Update Your Container to SMART 0.5

## Update the Existing API Calls and Their Output

One change from SMART 0.4 to 0.5 is that the Vital Signs model is now called
Vital Sign Sets. In order to upgrade, you will need to rename the
`sp:VitalSigns` objects in your RDF to `sp:VitalSignSets`. Also make sure that
your container handles the `/records/12345/vital_sign_sets` call paths. You will
also need to update the date predicates in your RDF output to match the updated
specifications [we need more text here]

## Implement the new API call and deprecate the ones that are no longer needed

The `/version`, `/capabilities`, and `/records/12345/alerts` calls are no longer
part of the SMART standard. Please disable these in your container. Implement the
new `/manifest` container manifest call based on the example from
<http://sandbox-api.smartplatforms.org/manifest>. Also implement the clinical notes,
procedures, and smoking history APIs and data models as described in
<http://dev.smartplatforms.org/reference/data_model/>

## Implement the Filtering and Pagination Parameters in Your API Request Handlers

Please see <http://dev.smartplatforms.org/reference/filters> for details about
the new filtering and pagination capabilties expected by a SMART 0.5 container.

## Test With the API Verifier

Run the API Verifier app to validate your SMART 0.5 container. The API Verifier
does not yet test the filtering and pagination readiness of your container and some
other features of the SMART 0.5 standard. However, it will do a reasonable job
at checking the RDF and JSON output of your API calls.
