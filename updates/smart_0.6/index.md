---
layout: page
title: SMART 0.6 Update Guide (Apps + Containers)
includenav: smartnav.markdown
---
{% include JB/setup %}

<div id="toc"></div>


# What's new in SMART 0.6

## Native Apps Workflow

SMART 0.6 containers are now exposing standard OAuth endpoints. This means the 
SMART API is no longer limited to web apps only, any platform capable of managing 
OAuth tokens and performing REST calls is now able to exchange data with a SMART 
container. This opens the door for native app development in general and mobile 
apps in particular.

To help kickstart native mobile apps we have created an [iOS
framework][] for app developers, its Android counterpart is coming soon.

[iOS framework]: https://github.com/chb/SMARTFramework-ios


## Documents API

The new [Documents API][] enables SMART containers to serve documents pertaining
to the patient. The documents can be returned either as URLs or inlined in the
SMART RDF. The single-document API call can also return the raw document data.
Documents can include patient images, radiography images, EKG data files,
scanned documents, clinical notes, etc.

[documents api]: /reference/data_model/#Document

### Photographs

The [Photographs API][] provides access to specific image documents that represent the
patient. This allows SMART applications to show a patient photo (if available)
to support an even more personal clinician-patient interaction. The photographs are
returned in the Documents model format. The intent of these photographs is to show
a head shot of the patient.

[photographs api]: /reference/data_model/#Photograph


## Family History API

SMART 0.6 introduces the new [Family History
API](/reference/data_model/#Family_History_Observation) which can be
used to expose facts and findings pertaining to a patient's biological
relative. The relatives are classified based on SNOMED CT. The facts
that can stated about the relative include:

* Date of birth and/or date of death
* Height
* Any problem that can be expressed through SNOMED CT

## Scratchpad API

The new SMART 0.6 Scratchpad API enables SMART apps to store data pertaining
to a patient record in free form format. This is, the app decides on the format
of the data that it wants to store (self-structured) making the data opaque to
the container. All SMART apps are allowed read access to the scratchpad data
for the in-scope patient of all other apps, which provides a basic 
interoperability facility accross apps.

Because SMART an app has access to the scratchpad that it owns regardless
of the user who runs it, there is always the possibility that a user overwrites
the data stored by another user. A container is free to implement collision detection
support for its scratchpad facilities.

*Note:* The SMART reference implementation scratchpad is not collision-safe.
Data may be lost by multiple copies of an app trying to write in parallel. Production
implementations are encouraged to implement a system that will, for example,
provide locks and dirty-state notification via HTTP error codes to apps writing
to the scratchpad. See the [REST API](/reference/rest_api/) for more
details.

## Clinical Notes Write API

We have added a simple API to POST simple plain text notes to a record
using a non-destructive write operation. See the [clinical note][] data
model.

[clinical note]: /reference/data_model/#Clinical_Note

## Extended Demographic API

The demographics API has been extended in SMART 0.6 to include two additional
optional fields, "Date of Death" and "Gestataional Age at Birth". The gestational
age at birth is the the week from the estimated date of conception that
the patient has been born at (most people are born in the 40th week of the
pregnancy). See the [demographics data model](/reference/data_model/#Demographics)
for details.

## Filters/Pagination

Date filters have now been specified for all medical record APIs and
date properties have been added to the various data models that lacked
them.

Additional filters have been added to:

- `medications`: a list of pipe separated `rxnorm` codes
- `problems`: a list of pipe separated `snomed` codes
- `procedures`: a list of pipe separated `snomed` codes

An element's single `data` property or `start_date` will be
used as the default for sorting and filtering.

Also, SMART 0.6 no longer supports the `offset` pagnation
parameter that was introduced in SMART 0.5.

See the [Filters and Pagination](/howto/filters) tutorial for more
details.

## Height is now expressed in centimeters

In SMART 0.5, the height units used in the vital sign sets model used to meters.
In SMART 0.6 the height units used in the vital sign sets and the new family history
APIs have been changed to centimeters.
     


# HOWTO:  Update Your SMART Apps to SMART 0.6

## Update height units from meters to centimeters

If your SMART application queries SMART for height data, make sure that you update
your code so that it anticipates the height in centimeters (cm) as defined by the
new SMART 0.6 specification.

## REST apps

Check out our new [REST app tutorial][] to learn about the code needed to
use the SMART python client and update your REST apps accordingly.
(Note: The Java client has not yet been updated to SMART 0.6.)

[rest app tutorial](/howto/build_a_rest_app)



# HOWTO:  Update Your Container to SMART 0.6

## Implement OAuth endpoints

SMART 0.6 requires your container to expose a standalone record selection 
endpoint and the [standard OAuth 1.0 endpoints][oauth].

### The new user endpoint is:

    /apps/{{app_id}}/launch

The purpose of this web page is to allow the user to select a record against 
which to run the SMART app. Whether you display a list of records available 
to the user or choose a different approach is up to you.  

As soon as the user selects a record, the browser should redirect to the
app's `index` URL, with appended parameters `record_id` and `api_base`.

### The OAuth endpoints are:

* **Request Token** usually at `/oauth/request_token`  
  Endpoint to obtain an OAuth request token. The `oauth_callback` parameter 
  should be ignored and is assumed to be `oob`; it must be specified in the app 
  manifest. An additional parameter `smart_record_id`, identifying the record 
  to which to tie the token, must be present when requesting a token.
  
* **Authorize Token** usually at `/oauth/authorize`  
  Endpoint to let the user authorize an OAuth request token. This address is 
  usually loaded in a web browser and **will display a UI**.  
  
  The page should have the user log in (if he hasn't done so previously) and 
  should ask the user to authorize the given app to access container data, 
  along with a button to authorize. If a user has authorized an app before 
  there is no need to ask him again and the token should be authorized 
  automatically after login. If the app is authorized, the browser should 
  redirect the user to the app's `oauth_callback` URL, specified in the app manifest.
  
* **Exchange Token** usually at `/oauth/access_token`  
  Endpoint to exchange the request token with an OAuth access token, if a valid 
  request token and a valid token verifier is presented.

### Server Manifest

These four endpoint URLS must be placed in the server manifest under the
top-level key `launch_urls`, for example:

```
"launch_urls": {
    "app_launch": "https://smart.emr.com/apps/{{app_id}}/launch", 
    "authorize_token": "https://smart.emr.com/oauth/authorize", 
    "exchange_token": "https://smart.emr.com/oauth/access_token", 
    "request_token": "https://smart.emr.com/oauth/request_token"
},
```

### Endpoint UI

Keep in mind that the record selection page as well as the token authorization 
page may be requested for a standalone REST app, displaying in a user's desktop 
browser, or from a native app on a mobile phone. We suggest you use
[CSS media queries][css-media] to provide a slick UI in either case.

[oauth]: http://tools.ietf.org/html/rfc5849
[css-media]: http://css-tricks.com/css-media-queries/


## Update height units from meters to centimeters

Starting with SMART 0.6 the height units should be returned to the SMART apps
in centimeters (cm) instead of meters (m). Make sure that you update your
container accordingly.

## Update filters/pagination implementation

Extend your filters engine with the new `date_[from/to]_[incluse/exclusive]` filters. Also,
implement the new SMART 0.6 filters as described in the filters/pagination documentation.
You may also want to disable the "offset" pagination filter.

## Implement new APIs (Documents, Family History, Scratchpad)

You should implement the new Documents, Family History, and Scratchpad APIs, as outlined in the
"What's new in SMART 0.6" section. Make sure that your container manifest call properly
describes your container's support for these APIs and test your API output with the
API Verifier.

## Extend existing APIs

SMART 0.6 adds two optional fields to the Demographics API (date of death, and gestational age at birth)
as well as write capabilities for the Clinical Notes API. You should consider implemnting these estensions
to empower the next generation of SMART applications.
