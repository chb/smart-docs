---
layout: page
title: SMART REST API
includenav: smartnav.markdown
---
{% include JB/setup %}

<div class="simple_box">
  N.B. This is highly preliminary, not a commitment or final version of any
  particular API or data model. This is purely for internal collaboration and
  preview purposes.
</div>

<div id="toc"></div>


The calls below are all written with respect to the base URL /. But any given
SMART container will place all API calls its own base URL, e.g.
`http://sample_smart_emr.com/smart-base/`

Any individual item that can be retrieved via `GET` should have a
_fully-dereferenceable_ `URI`. To continue the example above, a medication in our
sample EMR might have the `URI`:
`http://sample_smart_emr.com/smart-base/records/123456/medications/664373`

# Changelog

[Changes to API + Payloads](../change_log/)

[Atom Feed FIXME]


# Overview

The SMART API provides access to individual resources (medications, fulfillment
events, prescription events, problems, etc.) and groups of these resources.


## Read-only API

Please note that for the time being, the SMART API remains read-only. We are
excited about continuing to define our read/write API &mdash; but we want make our
early APIs as easy as possible for EMR and PHR vendors to expose.


## REST Design Principles

In general you can interact with a:

* Group of resources using:
  * `GET` to retrieve a group of resources such as `/medications/`
  * `POST` to add a group of resources such as `/problems`. `POST`ing will add new
    resources every time it is called; in other words, `POST` is not idempotent. 
* Single resource using:
  * `GET` to retrieve a single resource such as /medications/{medication_id}
  * `DELETE` to remove a single resource
  * `PUT` to add a single resource tagged with an `external_id`.

    When a resource is `PUT`, it replaces any existing resource with the same
    `external_id`. In other words, `PUT` is idempotent. When `PUT`ting a resource
    such as a medication that may contain child resources (e.g. fulfillment events),
    these child nodes must not be included in the graph. Rather, they must be
    separately attached with another API call once the parent medication is `PUT`
    and has received an internal SMART id. So, `PUT`ting a medication with two
    fulfillments actually takes three API calls: one for the medication, and one for
    each (child) fulfillment event.


# OWL Ontology File

The API calls listed below, as well as the RDF/XML payloads, are also defined in
a machine-readable OWL file. The OWL file has been used to generate the
documentation below, as well as our client-side REST libraries and API
Playground app.


# Container Calls

## App Manifest

    GET /apps/{descriptor}/manifest

Returns a JSON SMART UI app manifest for the app matching `{descriptor}`, or `404`.
Note that `{descriptor}` can be an app ID like
`"got-statins@apps.smartplatforms.org"` or an intent string like
`"view_medications"`.

    GET /apps/manifests/

Returns a JSON list of all SMART UI app manifests installed on the container.
FIXME LINK RDF Payload description


## Capabilities

    GET /capabilities/

Get capabilities for a container. FIXME LINK RDF Payload description


## Demographics

    GET /records/search?given_name={given_name}&family_name={family_name}&zipcode={zipcode}&birthday={birthday}&gender={gender}&medical_record_number={medical_record_number}

Get an RDF graph of `sp:Demographics` elements for all patients that match the
query. Matching treats `family_name` and `given_name` as the *beginning* of a
name. For instance `given_name='J'` matches `/^J/i` and thus matches `Josh`.
Birthday is an `ISO8601` string like `2008-03-21`; gender is `male` or `female`.
`gender`, `birthday`, `zipcode`, and `medical_record_number` must match exactly.
FIXME LINK RDF Payload description


## Ontology

    GET /ontology

Get the ontology used by a SMART container. FIXME LINK RDF Payload description


## User

    GET /users/search?given_name={given_name}&family_name={family_name}

Get users by name (or all users if blank).

    GET /users/{user_id}

Get a single user by internal ID.

FIXME LINK RDF Payload description


# Record Calls

## Allergy

    GET /records/{record_id}/allergies/

Get all allergies for a patient.

    GET /records/{record_id}/allergies/{allergy_id}

Get allergies for a patient.

FIXME LINK RDF Payload description
  
  
## Demographics

    GET /records/{record_id}/demographics

Get all demographics for a patient.

FIXME LINK RDF Payload description


## Encounter

    GET /records/{record_id}/encounters/

Get all encounters for a patient.

GET /records/{record_id}/encounters/{encounter_id}

Get an encounter for a patient.

FIXME LINK RDF Payload description


## Fulfillment

    GET /records/{record_id}/fulfillments/

Get all fulfillments for a patient.

    GET /records/{record_id}/fulfillments/{fulfillment_id}

Get one fulfillment for a patient.

FIXME LINK RDF Payload description


## Immunization

FIXME LINK RDF Payload description

    GET /records/{record_id}/immunizations/

Get all immunizations for a patient.

    GET /records/{record_id}/immunizations/{immunization_id}

Get one immunization for a patient.


## Lab Result

    GET /records/{record_id}/lab_results/

Get all lab results for a patient.

    GET /records/{record_id}/lab_results/{lab_result_id}

Get one lab result for a patient.

FIXME LINK RDF Payload description


## Medical Record

FIXME LINK RDF Payload description


## Medication

    GET /records/{record_id}/medications/

Get all medications for a patient.

    GET /records/{record_id}/medications/{medication_id}

Get medication for a patient.

FIXME LINK RDF Payload description


## Problem

    GET /records/{record_id}/problems/

Get all problems for a patient

    GET /records/{record_id}/problems/{problem_id}

Get one problem for a patient.

FIXME LINK RDF Payload description


## User Preferences

    GET /accounts/{user_id}/apps/{smart_app_id}/preferences

Get user preferences for an app.

FIXME LINK RDF Payload description


## VitalSigns

    GET /records/{record_id}/vital_signs/

Get all vital signs for a patient

    GET /records/{record_id}/vital_signs/{vital_signs_id}

Get one vital sign for a patient

FIXME LINK RDF Payload description
