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


---

<!-- GENERATED DOCS INSERTED BELOW THIS LINE - DON'T EDIT REMOVE ME! -->



# Container Calls


## App Manifest

Returns a JSON list of all SMART UI app manifests installed on the container.

     GET /apps/manifests/

Returns a JSON SMART UI app manifest for the app matching {descriptor}, or 404.  Note that {descriptor} can be an app ID like "got-statins@apps.smartplatforms.org" or an intent string like "view_medications".

     GET /apps/{descriptor}/manifest


[App Manifest RDF](../data_model/#App_Manifest)

## ContainerManifest

Get manifest for a container

     GET /manifest


[ContainerManifest RDF](../data_model/#ContainerManifest)

## Demographics

Get an RDF graph of sp:Demographics elements for all patients that match the query.  Matching treats family_name and given_name as the *beginning* of a name.  For instance given_name='J' matches /^J/i and thus matchs 'Josh'. Birthday is an ISO8601 string like "2008-03-21"; gender is "male" or "female".  Gender, birthday, zipcode, and medical_record_number must match exactly.
	

     GET /records/search?given_name={given_name}&family_name={family_name}&zipcode={zipcode}&birthday={birthday}&gender={gender}&medical_record_number={medical_record_number}


[Demographics RDF](../data_model/#Demographics)

## Ontology

Get the ontology used by a SMART container

     GET /ontology


[Ontology RDF](../data_model/#Ontology)

## User

Get users by name (or all users if blank)

     GET /users/search?given_name={given_name}&family_name={family_name}

Get a single user by internal ID

     GET /users/{user_id}


[User RDF](../data_model/#User)

# Record Calls


## Alert


[Alert RDF](../data_model/#Alert)

## Allergy

Get all allergies for a patient

     GET /records/{record_id}/allergies/

Get allergies for a patient

     GET /records/{record_id}/allergies/{allergy_id}


[Allergy RDF](../data_model/#Allergy)

## Demographics

Get all demographics for a patient

     GET /records/{record_id}/demographics


[Demographics RDF](../data_model/#Demographics)

## Encounter

Get all encounters for a patient

     GET /records/{record_id}/encounters/

Get encounters for a patient

     GET /records/{record_id}/encounters/{encounter_id}


[Encounter RDF](../data_model/#Encounter)

## Fulfillment

Get fulfillments for a patient

     GET /records/{record_id}/fulfillments/{fulfillment_id}

Get all fulfillments for a patient

     GET /records/{record_id}/fulfillments/


[Fulfillment RDF](../data_model/#Fulfillment)

## Immunization

Get one immunization for a patient

     GET /records/{record_id}/immunizations/{immunization_id}

Get all immunizations for a patient

     GET /records/{record_id}/immunizations/


[Immunization RDF](../data_model/#Immunization)

## Lab Result

Get lab results for a patient

     GET /records/{record_id}/lab_results/{lab_result_id}

Get all lab results for a patient

     GET /records/{record_id}/lab_results/


[Lab Result RDF](../data_model/#Lab_Result)

## Medical Record


[Medical Record RDF](../data_model/#Medical_Record)

## Medication

Get medication for a patient

     GET /records/{record_id}/medications/{medication_id}

Get all medications for a patient

     GET /records/{record_id}/medications/


[Medication RDF](../data_model/#Medication)

## Problem

Get problems for a patient

     GET /records/{record_id}/problems/{problem_id}

Get all problems for a patient

     GET /records/{record_id}/problems/


[Problem RDF](../data_model/#Problem)

## User Preferences

Get user preferences for an app

     GET /accounts/{user_id}/apps/{smart_app_id}/preferences


[User Preferences RDF](../data_model/#User_Preferences)

## VitalSigns

Get all vital signs for a patient

     GET /records/{record_id}/vital_signs/

Get vital signs for a patient

     GET /records/{record_id}/vital_signs/{vital_signs_id}


[VitalSigns RDF](../data_model/#VitalSigns)
