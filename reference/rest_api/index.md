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


The calls below are all written with respect to the base URL /. But any
given SMART container will place all API calls its own base URL, e.g.

    http://sample_smart_emr.com/smart-base/

Any individual item that can be retrieved via `GET` should have a
_fully-dereferenceable_ `URI`. To continue the example above, a
medication in our sample EMR might have the `URI`:

    http://sample_smart_emr.com/smart-base/records/123456/medications/664373


# Changelog

See here for all of the [changes to the API and payloads](../change_log/)


# Overview

The SMART API provides access to individual resources (medications, fulfillment
events, prescription events, problems, etc.) and groups of these resources in a
[RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer) API.


## SMART is a Read-only API

Please note that for the time being, the SMART API remains read-only. We
are excited about continuing to define our read/write API &mdash; but we
want make our early APIs as easy as possible for EMR and PHR vendors to
expose.


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

    When a resource is `PUT`, it replaces any existing resource with the
    same `external_id`. In other words, `PUT` is idempotent. When `PUT`ting
    a resource such as a medication that may contain child resources (e.g.
    fulfillment events), these child nodes must not be included in the
    graph. Rather, they must be separately attached with another API call
    once the parent medication is `PUT` and has received an internal SMART
    id. So, `PUT`ting a medication with two fulfillments actually takes
    three API calls: one for the medication, and one for each (child)
    fulfillment event.


# OWL Ontology File

The API calls listed below, as well as the RDF/XML payloads, are also
defined in a machine-readable OWL file. The OWL file has been used to
generate the documentation below, as well as our client-side REST
libraries and API Playground app.


# SMART REST API Reference

Each `GET` call in the SMART REST API is listed below and grouped by the
"scope" or "access control category" the SMART container applies to the
call. The SMART container implements this access control using the OAuth
tokens passed in with each API request as described in the [build a REST
App howto][] and the [RxReminder app][].

[build a REST app howto]: /howto/build_a_rest_app/
[RxReminder app]:         /howto/rx_reminder/

Currently there are three "scopes" or access control categories:

1. `Container` calls can be made by anyone against the container.
   Examples of this type of call are fetching the container's manifest
   and fetching the container's ontology.  These calls need not
   be OAuth-signed (though it is not incorrect to sign them).

2. `Record` calls are scoped to a (app, user, record) tuple e.g. calls
   to fetch a patient's medical record data. An example would be getting
   the medications in a patient's record. The OAuth credentials for
   the app (e.g. the `consumer_key` and `consumer_secret`) and
   previously fetched OAuth credentials from the server including the
   `smart_record_id` These calls must be signed as "3-legged" 
   OAuth requests, meaning they are signed with a combination of
   the app's consumer token + access token.

3. `User` calls are scoped to a (app, user) tuple and are used for
   setting a user's preferences _for that app only_. (Future versions
   of the SMART API may allow an app to read another's preferences or
   add a "global" set of user preferences. These calls are also
   signed as "3-legged" OAuth calls, using an app's consumer token +
   access token.

---
---
---

<!-- GENERATED DOCS INSERTED BELOW THIS LINE - DON'T EDIT REMOVE ME! -->



# Container Calls

## App Manifest

     GET /apps/{descriptor}/manifest 

Returns a JSON SMART UI app manifest for the app matching {descriptor}, or 404.  Note that {descriptor} can be an app ID like "got-statins

     GET /apps/manifests/ 

Returns a JSON list of all SMART UI app manifests installed on the container.

[App Manifest RDF](../data_model/#App_Manifest)


## ContainerManifest

     GET /manifest 

Get manifest for a container

[ContainerManifest RDF](../data_model/#ContainerManifest)


## Demographics

     GET /records/search 

Get an RDF graph of sp:Demographics elements for all patients that match the query.  Matching treats family_name and given_name as the *beginning* of a name.  For instance given_name='J' matches /^J/i and thus matchs 'Josh'. Birthday is an ISO8601 string like "2008-03-21"; gender is "male" or "female".  Gender, birthday, zipcode, and medical_record_number must match exactly.
	

[Demographics RDF](../data_model/#Demographics)


## Ontology

     GET /ontology 

Get the ontology used by a SMART container

[Ontology RDF](../data_model/#Ontology)


## User

     GET /users/{user_id} 

Get a single user by ID

     GET /users/search 

Get users by name (or all users if blank)

[User RDF](../data_model/#User)



# Record Calls

## Allergy

     GET /records/{record_id}/allergies/ 

Get all Allergies and Allergy Exclusions for a patient

     GET /records/{record_id}/allergies/{allergy_id} 

Get one Allergy for a patient

[Allergy RDF](../data_model/#Allergy)


## Clinical Note

     GET /records/{record_id}/clinical_notes/{clinical_note_id} 

Get one Clinical Note for a patient

     GET /records/{record_id}/clinical_notes/ 

Get all Clinical Notes for a patient

[Clinical Note RDF](../data_model/#Clinical_Note)


## Demographics

     GET /records/{record_id}/demographics 

Get Demographics for a patient

[Demographics RDF](../data_model/#Demographics)


## Encounter

     GET /records/{record_id}/encounters/ 

Get all Encounters for a patient

     GET /records/{record_id}/encounters/{encounter_id} 

Get one Encounter for a patient

[Encounter RDF](../data_model/#Encounter)


## Fulfillment

     GET /records/{record_id}/fulfillments/ 

Get all Fulfillments for a patient

     GET /records/{record_id}/fulfillments/{fulfillment_id} 

Get one Fulfillment for a patient

[Fulfillment RDF](../data_model/#Fulfillment)


## Immunization

     GET /records/{record_id}/immunizations/{immunization_id} 

Get one Immunization for a patient

     GET /records/{record_id}/immunizations/ 

Get all Immunizations for a patient

[Immunization RDF](../data_model/#Immunization)


## Lab Panel

     GET /records/{record_id}/lab_panels/ 

Get all Lab Panels for a patient

     GET /records/{record_id}/lab_panels/ 

Get one Lab Panel for a patient

[Lab Panel RDF](../data_model/#Lab_Panel)


## Lab Result

     GET /records/{record_id}/lab_results/{lab_result_id} 

Get one Lab Result for a patient

     GET /records/{record_id}/lab_results/ 

Get all Lab Results for a patient

[Lab Result RDF](../data_model/#Lab_Result)


## Medication

     GET /records/{record_id}/medications/ 

Get all Medications for a patient

     GET /records/{record_id}/medications/{medication_id} 

Get one Medication for a patient

[Medication RDF](../data_model/#Medication)


## Problem

     GET /records/{record_id}/problems/ 

Get all Problems for a patient

     GET /records/{record_id}/problems/{problem_id} 

Get one Problem for a patient

[Problem RDF](../data_model/#Problem)


## Procedure

     GET /records/{record_id}/procedures/ 

Get all Procedures for a patient

     GET /records/{record_id}/procedures/{procedure_id} 

Get one Procedure for a patient

[Procedure RDF](../data_model/#Procedure)


## Social History

     GET /records/{record_id}/social_history 

Get Social History for a patient

[Social History RDF](../data_model/#Social_History)


## Vital Sign Set

     GET /records/{record_id}/vital_sign_sets/ 

Get all Vital Sign Sets for a patient

     GET /records/{record_id}/vital_sign_sets/{vital_sign_set_id} 

Get one Vital Sign Set for a patient

[Vital Sign Set RDF](../data_model/#Vital_Sign_Set)



# User Calls

## User Preferences

     GET /users/{user_id}/apps/{smart_app_id}/preferences 

Get user preferences for an app

[User Preferences RDF](../data_model/#User_Preferences)


