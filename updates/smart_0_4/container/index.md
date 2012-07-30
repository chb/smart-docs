---
layout: page
title: SMART 0.4 Container Update Guide
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

SMART 0.4 introduces numerous improvements, including standardized
namespaces, new API calls and data models, a mechanism for capabilities
and requirements discovery between the apps and the container, support
for notifications between the apps and the host, and a new API Verifier
tool for testing your container’s data model conformity to the SMART
specifications.

# Prioritizing Updates

For practical reasons, we divide the work of upgrading to SMART 0.4 into
two categories: critical (necessary to run any apps at all) vs.
nice-to-have (new features that some apps may rely on). Here is the
list of updates that are critical for supporting most SMART 0.4 apps:

1. Updated URI schemas in the RDF coded values output e.g. <http://purl.bioontology.org>
2. Updates to the app manifests loader to parse the new app manifest format
3. Updates to `smart-api-container.js` and `smart-helper.js` to support the
   new SMART connect client used by the apps
4. Implementation of host-to-app and app-to-host notifications to support the
   new frame apps

The following updates, while not critical, should also be added to your
container for full conformance to SMART 0.4:

1. Immunization Data Type and API
2. Preferences API
3. Capabilities and Version reporting calls

The updates listed above are described in further details in the
following sections of this document.

# Top Priority

## Update Any Code URIs

For consistency, we’ve aligned our RXNORM, LOINC, and NDFRT, and SNOMED
CT URIs to the BioPortal namespace.  So you should update the code URIs
in your container’s RDF output as follows:

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
“dereferencable” -- meaning that developers can paste a code URI
directly into a browser’s URL bar to learn more about the concept. For
example: <http://purl.bioontology.org/ontology/RXNORM/892650>


## Parsing the  SMART App Manifest Files

We’ve made a few changes to the format of the SMART app manifests. The
`intents` and `base_url` parameters are now deprecated and may safely be
ignored by all containers. The `index` and `icon` parameters are now
fully qualified URLs with no substitutions required. The container may
use the values of these parameters or choose to override them with
custom URLs.

There are now two optional declarators in the manifest files, which app
developers may use to declare the API calls that their app is going to
use and the SMART container version that it is intended for. The
container may use these parameters to determine the app’s compatibility
with the local implementation.

Here is an example of a complete SMART 0.4 app manifest with the new
parts highlighted in green:

<pre>
<code>
{
 "name" : "My App",
 "description" : "A cool SMART app",
 "author" : "demo",
 "id" : "demo@apps.smartplatforms.org",
 "version" : ".1a",
 "mode" : "ui",
 "scope" : "record",
 "index" :  "<span style="color: green">http://myserver:8001</span>/smartapp/index.html",
 "icon" :  "<span style="color: green">http://myserver:8001</span>/smartapp/icon.png",
 <span style="color:green">"smart_version": "0.4",
 "requires" : {
          "http://smartplatforms.org/terms#VitalSigns": {
            "methods": ["GET"]
          },
          "http://smartplatforms.org/terms#Preferences": {
            "methods": ["GET", “PUT”, “DELETE”]
          }
 }
</span>
}
</code>
</pre>



## Updates to `smart-api-container.js`

We’ve made some updates to the `smart-api-container.js` script, which
will necessitate updating your `smart-helper.js` implementation. More
specifically, the `handle_api` function should now accept two callback
functions (one for success and one for error). You should feed the
success callback a message object with two properties:

- `contentType`: The MIME content type of the payload that you are 
  returning (application/rdf+xml, application/json, etc)
- `data`: The payload

The error callback expects an error object with the following properties:

- `status`: The status code of the error
- `message`: An object containing details about the error
  - `contentType`: The MIME type of the error message descriptor
  - `data`: The error message description


# Lower priority

## Support for host->app and app->host Notifications

SMART 0.4 offers a better paradigm for in-browser notifications:  apps
can send notifications to containers, and containers can send
notifications to apps.


### Send notifications to an app

When important events occur, you should notify any running apps.  For
now we define three container-to-app notifications:

1. "backgrounded" when an app instance is hidden from view
2. "foregrounded" when an app instance is restored to view
3. "destroyed" when an app instance is permanently closed

For example, if you permit a user to hide an app, you should call:

    SMART_HOST.notify_app(app_instance, "backgrounded");

And if you restore it to view you should call

  SMART_HOST.notify_app(app_instance, "foregrounded");


### Subscribe to App Notifications

Apps that you've launched may send notifications and requests. For now,
we define only one app-to-container notification:  an app that desires
more screen real estate may sent a `request_fullscreen` notification to
the container. To subscribe to a notification, call `SMART_HOST.on` as
in the example below:

    SMART_HOST.on("request_fullscreen", function(app_instance) {
       // Replace this example with your own resizing code
      $(app_instance.iframe)
         .css({
           width: '100%', 
           height: '100%', 
         });
    });


## New APIs and Calls

### Capabilities

Since not every container exposes every data type, SMART 0.4 allows a
container to express a simple JSON description of API calls that it
understands.  This way an app can `GET /capabilities/` to determine what
data to expect.  The example below shows the capabilities of a container
that provides Demographics, Encounters, and Vital Signs only.

    {
       "http://smartplatforms.org/terms#Demographics": {
           "methods": [
               "GET"
           ]
       }, 
       "http://smartplatforms.org/terms#Encounter": {
           "methods": [
               "GET"
           ]
       }, 
       "http://smartplatforms.org/terms#VitalSigns": {
           "methods": [
               "GET"
           ]
       }
    }

You can see another example at: <http://sandbox-dev.smartplatforms.org:7000/capabilities/>


## Version Number

The version number of the SMART API that the container implements should
now be reported at the `/version` url. The container should return the
version number (for example “0.4”) in plain text. Here is the version
number URL for the development sandbox:
<http://sandbox-dev.smartplatforms.org:7000/version>


## Preferences

The new preferences API provides a way for your app to store data within
the SMART container automatically scoped on per user and app basis. The
data can be stored in any format that makes sense to the app.
The container should accept GET, PUT, and DELETE requests at the following path:

    /accounts/{user_id}/apps/{smart_app_id}/preferences

Here `user_id` is the identifier of the user account that the app wants
to scope the preferences down to, which typically is the e-mail address
of the user. The `smart_app_id` is the identifier of the app, for
example `demo@apps.smartplatforms.org`.

The PUT request should destructively overwrite any existing preferences
for the app on per user basis. The content-type provided in the HTTP
header by the app should be retained by the container together with the
data part of the request and returned back in the HTTP header when a GET
request is issued.


## Immunizations DataType + API

Please refer to our data model wiki:
<http://dev.smartplatforms.org/reference/data_model/#Immunization>


# A Useful Tool: SMART API Verifier

The new API Verifier app executes a series of custom and
automatically-generated (based on the official SMART ontology) tests on
the results of the container's API calls (within the context of a
patient). It will automatically fetch data from the common medical
record call of the container (this version does not handle individual
record item calls and various container-level calls) via both the SMART
Connect and SMART REST interfaces.

Container developers should use the app to verify their container’s
general conformity to the SMART 0.4 specifications. You can either
install the app and run it locally on your own server, or load the
hosted version of the app into your container with the following
manifest:

    http://apiverifier.smartplatforms.org/static/manifests/smart_manifest-0.4.json

Note: While passing the API Verifier's tests does provide a high level
of conformity assurance to the container developer, it does not
guarantee the validity of the data. There are certain data problems
which the current version of the verifier is unable to detect. Therefore
this app should be used as an advising tool and not as proof for SMART
conformity. We recommend running the API Verifier over a variety of
patient records within the container to test a variety of patient data
records and interfaces.
