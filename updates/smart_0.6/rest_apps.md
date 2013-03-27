---
layout: page
title: Updating Your SMART REST App
includenav: smartnav.markdown
---

{% include JB/setup %}

<div id="toc"> </div>

<div class='simple_small_box'>{% include githublink %}</div>

SMART v0.6 introduces significant changes to SMART REST app
authentication and authorization. SMART Containers now implement the
standard [OAuth][] 1.0a authentication delegation protocol. This change
allows for app developers to use more standardized tools to connect to
SMART containers and the creation of native client libraries including
mobile clients.

[oauth]: http://tools.ietf.org/html/rfc5849

You should first read the [Main Page](../../) and
[HOWTO Build a SMART REST App](../build_a_smart_rest_app).


---


## Getting Started

As a prerequisite, you should be familiar the SMART's previous
"simplified" OAuth-based authentication protocol. In general, the
changes will be to conform to the standard ways to using OAuth. This
document will also assume you are using the SMART Python client.


## Update Your App's Manifest

You must add `oauth_callback` item to your app's manifest. Here is a
sample manifest that points to a locally hosted app:

    {
      "name": "SMART REST Minimal",
      "description": "The minimal SMART REST Flask app",
      "author": "Arjun Sanyal & Pascal Pfiffner, Harvard Medical School",
      "id": "minimal-rest-example@apps.smartplatforms.org",
      "mode": "ui",
      "scope": "record",
      "index": "http://localhost:8008/",
      "oauth_callback": "http://localhost:8008/authorize",
      "icon": "http://localhost:8008/static/icon.png",
      "smart_version": "0.6",
      "version": ".1"
    }


## Getting the Latest Client Code

First, you will need to update your app's references to the
`smart_client` to XXX to get the latest changes.

TODO: we should provide a tag at a minimum here.


## Importing SMARTClient

You will only need to change imports such as:

    from smart_client import oauth
    from smart_client.smart import SmartClient

to

    from smart_client.client import SMARTClient

Notice the change in capitalization and there is no need to `import
oauth` anymore.


## Configuring SMARTClient

Instead of just looking for a URL parameter called `oauth_header` that
the container provides your app's index page, you will now need to
provide more information up front to initialize the SMARTClient. For an
app running against a locally hosted SMART contatiner a good way to
define the necessary parameters is with a static `dict`, e.g.:

      # SMART Container OAuth Endpoint Configuration
      _ENDPOINT = {
          "url": "http://localhost:7000",
          "name": "Localhost",
          "app_id": "rest-example@apps.smartplatforms.org",
          "consumer_key": "rest-example@apps.smartplatforms.org",
          "consumer_secret": "changeMEinPRODUCTION!"
      }

The `app_id`, `consumer_key`, and `consumer_secret` here are the
parameters that you defined and recieved when installing your app into
the container.


