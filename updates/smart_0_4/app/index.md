---
layout: page
title: SMART 0.4 App Update Guide
includenav: smartnav.markdown
---
{% include JB/setup %}

{% include example_format_tabs_top.html %}

<div class='simple_box'>
  This is highly preliminary, not a commitment or final version of any
  particular API or data model. This is purely for internal collaboration and
  preview purposes.
</div>


<div id="toc"></div>


# Overview

SMART 0.4 introduces numerous improvements, including more robust
content-type and error handling. To take advantage of these features
and stay compatible with the SMART API, you’ll need to use the 0.4
client libraries in your app. This guide will help you make the
transition.

# SMART Response Object

Each API call you make through a SMART client library will return a
SMART Response object, encapsulating a number of useful properties.
Every SMART Response object is guaranteed to have at least the `body`
and `contentType` properties.

1. `body`: A string representation of the call result (RDF-XML in the case of
an RDF graph)

2. `contentType`: The MIME type of the response from the API call

For calls that return RDF data (i.e. the calls that return medical record
data), the SMART Response also includes:

1. `graph`: an in-memory graph object with the triples from body loaded and ready to query

For calls that return JSON data (e.g `GET /capabilities` or `GET /manifests`),
the SMART Response also includes:

2. `json`: a parsed JSON object representation of `body`

The basic idea is you can always get at the raw data by accessing the body
property.  But the client libraries will help you by automatically parsing RDF
or JSON data and making these readily available.


# SMART Connect Apps (JavaScript API)

Since each API call returns a SMART Response object, you’ll need to update your
client code to access the graph property for calls that return RDF data.  At
the same time, we’ve separated out the logic for handling successful responses
from errors (more details below).  So the basic template to follow in updating
your old code is:

- (Wrong) Old Way

    SMART.PROBLEMS_get(function(problems) {
      var graph = problems;
      // processing here…
    });

- (Correct) New Way

    SMART.PROBLEMS_get().success(function(problems) {
      var graph = problems.graph;
      // processing here…
    });

## Understanding Error Handling in SMART Connect

The API call methods in SMART Connect have been updated to support jQuery-style
callback handlers. You can now register two separate callbacks:  one for
successful API calls (required) and an optional handler that will be triggered
in the event of an error.  The basic pattern looks like this:

    SMART.MEDICATIONS_get().success(callback_ok).error(callback_err);

Where `callback_ok` and `callback_err` are your callback functions.
`callback_ok` will be called with a SMART response object as argument when the
call succeeds. `callback_err` will be called with a SMART error object in the
event of a failure.

The SMART error object has the following properties:

1. `status`: The status code of the error
2. `message`: An object containing details about the error
   1. `contentType`: The MIME type of the error message descriptor
   2. `data`: The error message description

Putting all of this together we get the following code example:

    SMART.PROBLEMS_get()
         .success(function(problems) {
           var graph = problems.graph;
            // processing here…
         })
         .error(function(e) {
           var status = e.status,
               message = e.message;
           // display error
         });

## No More Global jQuery Object

The SMART connect client no longer exposes its internal jQuery (aka $) object
in the global JavaScript namespace. Therefore when using the new client, your
SMART connect apps will not have jQuery automatically available.  If you do
want to access SMART Connect’s internal jQuery object, it’s available via
`SMART.jQuery` or `SMART.$` 


# SMART REST Apps: Python Library

Since each API call returns a SMART Response object, you’ll need to
update your client code as follows:

- (Wrong) Old Way

    medications = client.records_X_medications_GET()

- (Correct) New Way

    medications = client.records_X_medications_GET().graph

As you can see, all you need to do is fetch the graph property from the
response object.


# SMART REST Apps: Java Library

We haven’t yet updated the SMART Java client library to provide a SMART
Response object with each API response.  Please stay tuned for an
updated -- in the meantime, existing Java apps should continue to work.


# Update any code URIs

For consistency, we’ve aligned our RXNORM, LOINC, and NDFRT, and SNOMED
CT URIs to the BioPortal namespace.  So if you’ve got an app that relies
on specific code URIs, you'll want to update them:

- SNOMED CT 
  - Old: <http://www.ihtsdo.org/snomed-ct/concepts/>
  - New: <http://purl.bioontology.org/ontology/SNOMEDCT/>
- RXNORM
  - Old: <http://rxnav.nlm.nih.gov/REST/rxcui/>
  - New: <http://purl.bioontology.org/ontology/RXNORM/>
- LOINC
  - Old: <http://loinc.org/codes/>
  - New: <http://purl.bioontology.org/ontology/LNC/>
- NDFRT
  - Old: <http://rxnav.nlm.nih.gov/REST/rxcui?idtype=NUI&id=>
  - New: <http://purl.bioontology.org/ontology/NDFRT/>

One advantage of using the BioPortal namespaces is that these code are
“dereferencable” -- meaning that you can paste a code URI directly into
your browser’s URL bar to learn more about the concept.  For example:
<http://purl.bioontology.org/ontology/RXNORM/892650> 


# Updating Your SMART App Manifest File

We’ve simplified the SMART Manifest format by eliminating `intents` and
`base_url` fields.  URLs for your app’s `index` and `icon` are now
expressed directly, without interpolation.  Here’s an example of how to
update your manifest:

- Old Way (wrong)

    {
      "name" : "My App",
      "description" : "A cool SMART app",
      ...
      "intents": ["view_medications"]    ← delete this
      "base_url" : "http://myserver:8001", ← delete this
      "index" :  "{base_url}/smartapp/index.html",
      "icon" :  "{base_url}/smartapp/icon.png"
    }

- New Way (correct)

    {
      "name" : "My App",
      "description" : "A cool SMART app",
      ...
      "index" :  "http://myserver:8001/smartapp/index.html",
      "icon" :  "http://myserver:8001/smartapp/icon.png"
    } 

There are now two optional declarators in the manifest files:

1. `smart_version` indicates the version of the SMART API your app was
   written for
2. `requires` describes the data types your app relies on

Here is an example of a complete manifest with these optional declarators:

    {
      "name" : "My App",
      "description" : "A cool SMART app",
      "author" : "demo",
      "id" : "demo@apps.smartplatforms.org",
      "version" : ".1a",
      "mode" : "ui",
      "scope" : "record",
      "index" :  "http://myserver:8001/smartapp/index.html",
      "icon" :  "http://myserver:8001/smartapp/icon.png",
      "smart_version": "0.4",
      "requires" : {
              "http://smartplatforms.org/terms#Demographics": {
                "methods": ["GET"]
              },
              "http://smartplatforms.org/terms#VitalSigns": {
                "methods": ["GET"]
              }
      }
    }


# New APIs and Calls

## Capabilities

The SMART 0.4 container exposes a JSON description of API calls that it
understands at the `/capabilities/` path. For example, our development
sandbox’s capabilities can be obtained from the following URL:
<http://sandbox-dev.smartplatforms.org:7000/capabilities/>

## Version Number

The version number of the SMART API that the container implements can
now be obtained from the `/version` url. Here is the version number URL
for the development sandbox:
<http://sandbox-dev.smartplatforms.org:7000/version>

## Preferences API

The new preferences API provides a way for your app to store data within
the SMART container automatically scoped on per user and app basis. The
data can be stored in any format that makes sense to the app. In the
SMART Connect client, you can now call the `PREFERENCES_get`,
`PREFERENCES_put`, and `PREFERENCES_delete` methods. For the put methods
you will have to provide a MIME content type for the data that you are
storing within the container. The equivalent calls in the SMART python
client are:

- `accounts_x_apps_x_preferences_GET`
- `accounts_x_apps_x_preferences_PUT`
- `accounts_x_apps_x_preferences_DELETE`

## Immunizations Datatype and API

You can now obtain the patient’s immunization records via the new
`IMMUNIZATIONS_get` (SMART Connect client) or
`records_x_immunizations_GET` (SMART Python client) calls. See
<http://dev.smartplatforms.org/reference/data_model/#Immunization>


# Testing Your Updated App

We will update the public sandbox <http://sandbox.smartplatfoms.org> to
run the new reference container on 4/24/2012. Until then, you are
welcome to test against our development sandbox hosted at the following
<http://sandbox-dev.smartplatforms.org>

Please keep in mind that the development sandbox is only suitable for
development and testing if you want to be on the cutting edge of the
SMART platform. Most developers should stick to the production sandbox,
because it offers better stability.

Also please keep in mind that the accounts on the development sandbox
get purged often, so don’t be surprised if you need to re-register your
account once in a while.
