---
layout: page
title: SMART 0.6 Update Guide (Apps + Containers)
includenav: smartnav.markdown
---
{% include JB/setup %}

<div id="toc"></div>

# What's new in SMART 0.6

## Native Apps Workflow

SMART 0.6 containers are now exposing standard OAuth endpoints. This means the SMART API is no longer limited to web apps only, any platform capable of managing OAuth tokens and performing REST calls is now able to exchange data with a SMART container. This opens the door for native app development in general and mobile apps in particular.  
To help kickstart native mobile apps we have created an iOS framework for app developers, its Android counterpart is in the making.


## Documents API

(Nikolai)

    mechanism for encapsulating metadata and links stored in external URLs
    documents include patient images, radiography images, EKG data files, scanned documents
    metadata about the file
    SMART could expose the public URL of the resource OR could proxy through the file and expose an obfuscated link (possibly by adding a “raw=true” parameter to the regular API URL)
    The API call returns the complete collection of data files for the patient
    Optional date and file type filters
    The container maintains an index of the available files

### Patient Images

(Nikolai)

### Radiography Images

(Nikolai / Nich)

## Family History API

(Nikolai)

- Demographics (date of birth, date of death)
- Biometrics (height)
- Problems (unlimited)

## Scratchpad API

    App annotation of patient records handled through and extension of the preferences API scoped to the app-record
    “fire-and-forget” type (non-transactional)
    All apps allowed to read each others’ scratchpads
    Data is “opaque” to the container, but self-structured by the app

## Clinical Notes Write API

(Arjun)

## Extended Demographic API

(Nikolai)

    Date of death
    Gestational Age at Birth

## Filters/Pagination

(Arjun)
     
# HOWTO:  Update Your SMART Apps to SMART 0.6

## Update vitals sign height units from m to cm

(Nikolai)

## REST apps

(Pascal / Arjun)

# HOWTO:  Update Your Container to SMART 0.6

## Implement OAuth endpoints

SMART 0.6 requires your container to expose a standalone record selection 
endpoint and the [standard OAuth 1.0 endpoints][oauth].

### The new user endpoint is:

    /apps/{{app_id}}/launch

The purpose of this web page is to allow the user to select a record against 
which to run the SMART app. Whether you display a list of records available 
to the user or choose a different approach is up to you.  

As soon as the user selects a record, the app's `index` URL, with appended 
parameters `record_id` and `api_base`, should be requested.

### The OAuth endpoints are:

* **Request Token** usually at `/oauth/request_token`  
  Endopoint to obtain an OAuth request token. The `oauth_callback` parameter 
  should be ignored and assumed to be `oob`, it must be specified in the app 
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

These four endpoint URLS must be placed in the server manifest under the top-level key `launch_urls`, for example:

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
browser, or from a native app on a mobile phone. We suggest you use [CSS media queries][css-media] 
to provide a slick UI in either case.

[oauth]: http://tools.ietf.org/html/rfc5849
[css-media]: http://css-tricks.com/css-media-queries/


## Update vitals sign height units from m to cm

(Nikolai)

## Update filters/pagination implementation

(Arjun)

## Implement new APIs (Documents, Family History, Scratchpad)

(Nikolai)

## Extend existing APIs (Demographics, Clinical Notes)

(Nikolai / Arjun)
=
