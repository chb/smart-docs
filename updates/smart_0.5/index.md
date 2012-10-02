---
layout: page
title: SMART 0.5 Update Guide (Apps + Containers)
includenav: smartnav.markdown
---
{% include JB/setup %}

<div id="toc"></div>

# What's new in SMART 0.5

## New and Improved Data Models

SMART 0.5 adds support for three new clinical statement types:

* [Clinical Notes](/reference/data_model#Clinical_Note)
* [Procedures](/reference/data_model#Procedure) 
* [Social History](/reference/data_model#Social_History) (currently tracks smoking status)

We've also updated the models in SMART 0.5 with more consistent naming and date
handling, as well as specific improvements described below.

Also, the [Lab Panel](/reference/data_model#Lab_Panel) model is now part of our auto-generated
online documentation. A panel has a code of its own, and groups together individual
lab results which can also be queried independently. Please, take a look in case you 
haven't seen this model before.
    
For a full description of the SMART 0.5 data models, visit our [Data Model Page](/reference/data_model)

## New and Improved Sample Apps

* The _API Verifier_ app has been updated to support SMART 0.5 container
  validation. Also the API Verifier is now able to validate SMART
  app manifests.

* The _Blood Pressure Centiles_ app has been updated to provide progressive
  loading capabilities (both manual and automated) in a configurable way.The
  app takes advantage of the new pagination capability of the SMART 0.5 (see
  below).

* Last but not least, we introduce the _Diabetes Monograph_, which presents
  an at-a-glance, integrated dashboard focused on diabetes management
  and risk assessment.

## Filtering and Paginating API Results

SMART 0.5 introduces filters to narrow down queries, as well as a mechanism to
fetch results in pages rather than all at once.  For example, a SMART app can
search for lab results that match a particular LOINC code, or vital signs
recorded with a given date range.  To request the first 10 lab results that
have LOINC code of `29571-7` or `38478-4` and occurred between January 1, 2010
and December 31, 2012, you can apply filters like:

{% highlight html %}
GET /records/1234567/lab_results/?loinc=29571-7|38478-4&date_from=2010-01-01&date_to=2012-12-31&limit=10&offset=0
{% endhighlight %}

Your app will only receive clinical statements matching the supplied filters.
An attached `ResponseSummary` object describes the result set.

For further information, review our [Filtering API](/reference/filters).


## Improved JavaScript Library: Working with SMART Data as JSON-LD

The SMART Connect JavaScript library now presents SMART data in two forms, for
your convenience:  an RDF graph interface (as before), and a new JSON Linked
Data interface.  JSON-LD provides a convenient way for Web apps to interact
with SMART RDF data as simple, familiar JSON structures.  

See our [Introduction to JSON-LD](/howto/intro_to_jsonld/) for details.

Also, the JavaScript client now has a fail callback handler that can be
used to process a callback in the event that the app is launched outside
the context of a SMART container. Your app could, for instance, decide
to provide directions ot the user about launching from  within a container
or switch to an alternative mode if that happens.

### Code pattern: 
{% highlight javascript %}
SMART.ready(function () {
    // Fetch SMART data and do work
}).fail(function () {
    // App launched outside a container
});
{% endhighlight %}

## Container Manifest API

We've consolidated the `/version` and `/capabilities` API calls at a common
`/manifest` endpoint.  To learn about a container, apps can simply
`GET/manifest` to obtain a JSON description of its capabilities.

For an example, see: <http://sandbox-api.smartplatforms.org/manifest>

## Change in the REST call path for the preferences API calls

The call path for the REST call for the preferences API is now
'GET /users/{user_id}/apps/{smart_app_id}/preferences' (used to be
'GET /accounts/{user_id}/apps/{smart_app_id}/preferences').

## No more alerts

The alerts data model (from SMART  0.4) has been dropped in SMART 0.5.
     
# HOWTO:  Update Your SMART Apps to SMART 0.5
## Updating Your API Call Names
Both the SMART Connect (JavaScript) and SMART Python clients have been updated
to support a new common naming convention for the API call convenience methods.
In order to use these libraries, you will have to update the names of the API
call methods that you use in your apps. For example, in a SMART Connect app, if
you use a call like `SMART.PROBLEMS_get()`, you will need to change it to
`SMART.get_problems()`. Similarly, in a SMART REST app, you will have to change
`SMART.records_X_problems_GET()` to `SMART.get_problems()`.

For a complete list of the convenience method names in the SMART 0.5 clients,
please see our [REST API documentation](/reference/rest_api/).

## Adjust For a Few Data Model Changes

There have been a few changes and simplifications to the existing SMART data
models that may require you to change your code:

1. `LabResult` elements now simply have a `dcterms:date` property indicating
the clinically effective time of the measurement (`specimenCollected` has
been removed). No more hunting through attributions to figure out dates!

2. `Vital Signs` elements been renamed to `Vital Sign Set` for clarity (since
each `Vital Sign Set` contains a set of results that were recorded together).

3. `Vital Signs` elements may now include head circumference measurements
(`headCircumference`), measured in `cm`.

4. `Allergy` elements now support three types of allergens:  medications
(`drugAllergen`), medication classes (`drugClassAllergen`) and other
(`otherAllergen`). 


## Take Advantage of New SMART 0.5 Features

First off, take advantage of the new clinical notes, procedures, and smoking
history data models as well as the filtering and pagination call parameters.
Here is how you can execute a SMART API call with filters via the Python and 
JavaScript clients.

### Python example:
{% highlight python %}
labs = SMART.get_lab_results(loinc = "29571-7|38478-4", limit = 10)
print labs
{% endhighlight %}

### JavaScript example: 
{% highlight javascript %}
SMART.get_lab_results({
  loinc: "29571-7|38478-4", 
  limit: 10
  offset: 0
}).success(function(r){
  console.log(r.objects.of_type.LabResult);
});
{% endhighlight %}

If you're writing a SMART Connect app, you should check out the JSON-LD
interface we now supply with each API response.  This interface provides an
intuitive alternative to `rdfquery` by letting you build SMART Connect apps
without SPARQL queries.

# HOWTO:  Update Your Container to SMART 0.5

## Implement data model updates

SMART 0.5 Containers should implement the small data model changes described
above ("Adjust For a few Data Model Changes").  These include updated date
predicates for labs and a renamed `VitalSignSet` data type.

## Implement new API call and deprecate the ones that are no longer needed

The `/version` and  `/capabilities` calls have been removed from the SMART 0.5
specification.  Instead, please implement the new `/manifest` container
manifest call based on the example from
<http://sandbox-api.smartplatforms.org/manifest>.

New clinical models (clinical notes, procedures, and social history) can be
exposed according to our updated [data models](/reference/data_model). 

## Implement the Filtering and Pagination Parameters in Your API Request Handlers

Please see our [Filtering API] (/reference/filters) page for details about the
new filtering and pagination capabilities introduced in SMART 0.5.

## Implement authorization policies

SMART 0.5 makes authorization policies more explicit by assigning each API
endpoint to one of three groups (public access; user-restricted access;
app-restricted access).  For full details see our [REST API
Page](/reference/rest_api).

## Change in the REST call path for the preferences API calls

Update the call path to 'GET /users/{user_id}/apps/{smart_app_id}/preferences'

## Deprecate your Alerts API

If you did have the Alerts API implemented in your SMART 0.4 container,
you should deprecate (or disable) the code related to it.

## Test With the API Verifier

Run the API Verifier app to validate your SMART 0.5 container. The API Verifier
does not yet test the filtering and pagination readiness of your container and some
other features of the SMART 0.5 standard. However, it will do a reasonable job
at checking the RDF and JSON output of your API calls.


