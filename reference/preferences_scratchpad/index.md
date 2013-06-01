---
layout: page
title: SMART Preferences and Scratchpad APIs
includenav: smartnav.markdown
---
{% include JB/setup %}

<div class='simple_box'>
  {% include githublink %}
</div>

<div id="toc"></div>

The SMART preferences and scratchpad APIs provide a facility that SMART apps
can use to persist data about the application and user preferences, notes about
the patient record, and other pertinant data. While the two APIs are similar,
they have diferent intent and therefore a different scope. In both instances,
SMART does not mandate a speific format for the data stored, only that it can be
serialized in unicode. Each app is responsible for choosing an appropriate
serialization format for its data.


## Preferences API

The preferences API provides a way for your app to store data within
the SMART container automatically scoped on per user and app basis. The
data can be stored in any format that makes sense to the app. In the
SMART Connect client, you can now call the `get_user_preferences`,
`put_user_preferences`, and `delete_user_preferences` methods. For the put methods
you will have to provide a MIME content type for the data that you are
storing within the container.

## Scratchpad API

The SMART 0.6 Scratchpad API enables SMART apps to store data pertaining
to a patient record in free form format. This is, the app decides on the format
of the data that it wants to store (self-structured) making the data opaque to
the container. All SMART apps are allowed read access to the scratchpad data
for the in-scope patient of all other apps, which provides a basic 
interoperability facility accross apps.

Because a SMART app has access to the scratchpad that it owns regardless
of the user who runs it, there is always the possibility that a user overwrites
the data stored by another user. A container is free to implement collision detection
support for its scratchpad facilities.

*Note:* The SMART reference implementation scratchpad is not collision-safe.
Data may be lost by multiple copies of an app trying to write in parallel. Production
implementations are encouraged to implement a system that will, for example,
provide locks and dirty-state notification via HTTP error codes to apps writing
to the scratchpad. See the [REST API](/reference/rest_api/) for more
details on the API.