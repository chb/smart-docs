---
layout: page
title: SMART REST API
includenav: smartnav.markdown
---
{% include JB/setup %}

<div class="simple_box">
  <p>N.B. This is highly preliminary, not a commitment or final version of any
  particular API or data model. This is purely for internal collaboration and
  preview purposes.</p>
  {% include githublink %}
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

Click here for the list of [Changes to the API and Payloads for the
latest release](/updates/smart_0.6/).


# Overview

The SMART API provides access to individual resources (medications, fulfillment
events, prescription events, problems, etc.) and groups of these resources in a
[RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer) API.


## REST Design Principles

In general you can interact with a:

* Group of resources using:
  * `GET` to retrieve a group of resources such as `/medications/`
* Single resource using:
  * `GET` to retrieve a single resource such as /medications/{medication_id}

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
App howto][].

[build a REST app howto]: /howto/build_a_rest_app/

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
   setting a user's preferences _for that app only_. These calls are also
   signed as "3-legged" OAuth calls, using an app's consumer token +
   access token. (Future versions of the SMART API may allow an app to 
   read another's preferences or add a "global" set of user preferences.) 

---
---
---

<!-- GENERATED DOCS INSERTED BELOW THIS LINE - DON'T EDIT REMOVE ME! -->



# Container Calls

## App Manifest
<ul>
<li>URI:<code> GET /apps/{descriptor}/manifest </code></li>
<li>Client method name:<code> get_app_manifest </code></li>
</ul>
Returns a JSON SMART UI app manifest for the app matching {descriptor}, or 404.  Note that {descriptor} can be an app ID like "got-statins <br><br>
<ul>
<li>URI:<code> GET /apps/manifests/ </code></li>
<li>Client method name:<code> get_app_manifests </code></li>
</ul>
Returns a JSON list of all SMART UI app manifests installed on the container. <br><br>
[App Manifest RDF](../data_model/#App_Manifest)


## ContainerManifest
<ul>
<li>URI:<code> GET /manifest </code></li>
<li>Client method name:<code> get_container_manifest </code></li>
</ul>
Get manifest for a container <br><br>
[ContainerManifest RDF](../data_model/#ContainerManifest)


## Demographics
<ul>
<li>URI:<code> GET /records/search </code></li>
<li>Client method name:<code> search_records </code></li>
</ul>
Get an RDF graph of sp:Demographics elements for all patients that match the query.  Matching treats family_name and given_name as the *beginning* of a name.  For instance given_name='J' matches /^J/i and thus matchs 'Josh'. Date of birth is an ISO8601 string like "2008-03-21"; gender is "male" or "female".  Gender, date_of_birth, zipcode, and medical_record_number must match exactly.
	<br><br>
[Demographics RDF](../data_model/#Demographics)


## Ontology
<ul>
<li>URI:<code> GET /ontology </code></li>
<li>Client method name:<code> get_ontology </code></li>
</ul>
Get the ontology used by a SMART container <br><br>
[Ontology RDF](../data_model/#Ontology)


## User
<ul>
<li>URI:<code> GET /users/search </code></li>
<li>Client method name:<code> search_users </code></li>
</ul>
Get users by name (or all users if blank) <br><br>
<ul>
<li>URI:<code> GET /users/{user_id} </code></li>
<li>Client method name:<code> get_user </code></li>
</ul>
Get a single user by ID <br><br>
[User RDF](../data_model/#User)



# Record Calls

## Allergy
<ul>
<li>URI:<code> GET /records/{record_id}/allergies/ </code></li>
<li>Client method name:<code> get_allergies </code></li>
</ul>
Get all Allergies and Allergy Exclusions for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/allergies/{allergy_id} </code></li>
<li>Client method name:<code> get_allergy </code></li>
</ul>
Get one Allergy for a patient <br><br>
[Allergy RDF](../data_model/#Allergy)


## Clinical Note
<ul>
<li>URI:<code> POST /records/{record_id}/clinical_notes/ </code></li>
<li>Client method name:<code> post_clinical_note </code></li>
</ul>
Post a Clinical Note for a patient. The body of the post should contain SMART RDF/XML serialization of the clinical note without the belongsTo predicate. The clinical note will be added to the collection of notes and the call will return a a copy of the posted data to indicate as successful posting. <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/clinical_notes/{clinical_note_id} </code></li>
<li>Client method name:<code> get_clinical_note </code></li>
</ul>
Get one Clinical Note for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/clinical_notes/ </code></li>
<li>Client method name:<code> get_clinical_notes </code></li>
</ul>
Get all Clinical Notes for a patient <br><br>
[Clinical Note RDF](../data_model/#Clinical_Note)


## Demographics
<ul>
<li>URI:<code> GET /records/{record_id}/demographics </code></li>
<li>Client method name:<code> get_demographics </code></li>
</ul>
Get Demographics for a patient <br><br>
[Demographics RDF](../data_model/#Demographics)


## Document
<ul>
<li>URI:<code> GET /records/{record_id}/documents/{document_id} </code></li>
<li>Client method name:<code> get_document </code></li>
</ul>
Allows a SMART app to request a single document. The optional `format` parameter sets the output format of the call. The possible values are `metadata`, `raw`, and `combined`. In `format=metadata` mode, the container returns metadata and desceriptors of the document in RDF-XML. In `format=combined` mode the call returns the serialized document content in addition to all the data from the `format=metadata` mode. In `format=raw` mode, SMART returns the raw document content with the proper MIME type. In the absence of a `format` parameter, the API defaults to `format=raw`. <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/documents/ </code></li>
<li>Client method name:<code> get_documents </code></li>
</ul>
Returns data about all the available documents for the patient record subject to the standard filter restrictions. The optional `format` parameter sets the output format of the call. The possible values are `metadata` and `combined`. In `format=metadata` mode, the container returns metadata and desceriptors of the documents in RDF-XML. In `format=combined` mode the call returns the serialized documents' content in addition to all the data from the `format=metadata` mode. In the absence of a `format` parameter, the API defaults to `format=metadata`. <br><br>
[Document RDF](../data_model/#Document)


## Encounter
<ul>
<li>URI:<code> GET /records/{record_id}/encounters/ </code></li>
<li>Client method name:<code> get_encounters </code></li>
</ul>
Get all Encounters for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/encounters/{encounter_id} </code></li>
<li>Client method name:<code> get_encounter </code></li>
</ul>
Get one Encounter for a patient <br><br>
[Encounter RDF](../data_model/#Encounter)


## Family History Observation
<ul>
<li>URI:<code> GET /records/{record_id}/family_history/ </code></li>
<li>Client method name:<code> get_family_history_observations </code></li>
</ul>
Get all Family Histories for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/family_history/{family_history_id} </code></li>
<li>Client method name:<code> get_family_history_observation </code></li>
</ul>
Get one Family History for a patient <br><br>
[Family History Observation RDF](../data_model/#Family_History_Observation)


## Fulfillment
<ul>
<li>URI:<code> GET /records/{record_id}/fulfillments/ </code></li>
<li>Client method name:<code> get_fulfillments </code></li>
</ul>
Get all Fulfillments for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/fulfillments/{fulfillment_id} </code></li>
<li>Client method name:<code> get_fulfillment </code></li>
</ul>
Get one Fulfillment for a patient <br><br>
[Fulfillment RDF](../data_model/#Fulfillment)


## Immunization
<ul>
<li>URI:<code> GET /records/{record_id}/immunizations/{immunization_id} </code></li>
<li>Client method name:<code> get_immunization </code></li>
</ul>
Get one Immunization for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/immunizations/ </code></li>
<li>Client method name:<code> get_immunizations </code></li>
</ul>
Get all Immunizations for a patient <br><br>
[Immunization RDF](../data_model/#Immunization)


## Lab Panel
<ul>
<li>URI:<code> GET /records/{record_id}/lab_panels/ </code></li>
<li>Client method name:<code> get_lab_panels </code></li>
</ul>
Get all Lab Panels for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/lab_panels/ </code></li>
<li>Client method name:<code> get_lab_panel </code></li>
</ul>
Get one Lab Panel for a patient <br><br>
[Lab Panel RDF](../data_model/#Lab_Panel)


## Lab Result
<ul>
<li>URI:<code> GET /records/{record_id}/lab_results/{lab_result_id} </code></li>
<li>Client method name:<code> get_lab_result </code></li>
</ul>
Get one Lab Result for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/lab_results/ </code></li>
<li>Client method name:<code> get_lab_results </code></li>
</ul>
Get all Lab Results for a patient <br><br>
[Lab Result RDF](../data_model/#Lab_Result)


## Medication
<ul>
<li>URI:<code> GET /records/{record_id}/medications/ </code></li>
<li>Client method name:<code> get_medications </code></li>
</ul>
Get all Medications for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/medications/{medication_id} </code></li>
<li>Client method name:<code> get_medication </code></li>
</ul>
Get one Medication for a patient <br><br>
[Medication RDF](../data_model/#Medication)


## Photograph
<ul>
<li>URI:<code> GET /records/{record_id}/photograph </code></li>
<li>Client method name:<code> get_photograph </code></li>
</ul>
Get one Photograph for a patient <br><br>
[Photograph RDF](../data_model/#Photograph)


## Problem
<ul>
<li>URI:<code> GET /records/{record_id}/problems/{problem_id} </code></li>
<li>Client method name:<code> get_problem </code></li>
</ul>
Get one Problem for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/problems/ </code></li>
<li>Client method name:<code> get_problems </code></li>
</ul>
Get all Problems for a patient <br><br>
[Problem RDF](../data_model/#Problem)


## Procedure
<ul>
<li>URI:<code> GET /records/{record_id}/procedures/ </code></li>
<li>Client method name:<code> get_procedures </code></li>
</ul>
Get all Procedures for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/procedures/{procedure_id} </code></li>
<li>Client method name:<code> get_procedure </code></li>
</ul>
Get one Procedure for a patient <br><br>
[Procedure RDF](../data_model/#Procedure)


## Scratchpad Data
<ul>
<li>URI:<code> GET /records/{record_id}/apps/{smart_app_id}/scratchpad </code></li>
<li>Client method name:<code> get_scratchpad_data </code></li>
</ul>
Returns the scratchpad blob unicode data stored in the patient's account by a previous run of the owner app in the response body. An app can ready any other app's scratchpad. If not data is available the call will return an empty string. <br><br>
<ul>
<li>URI:<code> DELETE /records/{record_id}/apps/{smart_app_id}/scratchpad </code></li>
<li>Client method name:<code> delete_scratchpad_data </code></li>
</ul>
Purges the scratchpad data stored in the SMART container for the selected app. If everything goes well, this call will respond with HTTP 200 status code. <br><br>
<ul>
<li>URI:<code> PUT /records/{record_id}/apps/{smart_app_id}/scratchpad </code></li>
<li>Client method name:<code> put_scratchpad_data </code></li>
</ul>
Stores scratchpad data in the patient's account in the SMART container scoped to the current app. The HTTP request body represents the unicode-encoded data blob. The app chooses the best format for the data that makes sense for its use case (it is unstructured from SMART's perspective). If the data save was successful, the SMART server will respond with an HTTP 200 code and include the stored data in the response body. It is the app's responsibility to compare the response with the intended data content. If there are any discrepancies, then a concurrency problem occured while writing the data and the app should request a fresh copy of the scratchpad data stored on the server, merge it with its local copy and attempt writing it again. <br><br>
[Scratchpad Data RDF](../data_model/#Scratchpad_Data)


## Social History
<ul>
<li>URI:<code> GET /records/{record_id}/social_history </code></li>
<li>Client method name:<code> get_social_history </code></li>
</ul>
Get Social History for a patient <br><br>
[Social History RDF](../data_model/#Social_History)


## Vital Sign Set
<ul>
<li>URI:<code> GET /records/{record_id}/vital_sign_sets/ </code></li>
<li>Client method name:<code> get_vital_sign_sets </code></li>
</ul>
Get all Vital Sign Sets for a patient <br><br>
<ul>
<li>URI:<code> GET /records/{record_id}/vital_sign_sets/{vital_sign_set_id} </code></li>
<li>Client method name:<code> get_vital_sign_set </code></li>
</ul>
Get one Vital Sign Set for a patient <br><br>
[Vital Sign Set RDF](../data_model/#Vital_Sign_Set)



# User Calls

## User Preferences
<ul>
<li>URI:<code> DELETE /users/{user_id}/apps/{smart_app_id}/preferences </code></li>
<li>Client method name:<code> delete_user_preferences </code></li>
</ul>
Purges the user preferences stored in the SMART container for the selected app. If everything goes well, this call will respond with HTTP 200 status code. <br><br>
<ul>
<li>URI:<code> PUT /users/{user_id}/apps/{smart_app_id}/preferences </code></li>
<li>Client method name:<code> put_user_preferences </code></li>
</ul>
Stores preferences data in the user's account in the SMART container scoped to the current app. The HTTP request body represents the unicode-encoded data blob. The app chooses the best format for the data that makes sense for its use case (it is unstructured from SMART's perspective). If the data save was successful, the SMART server will respond with an HTTP 200 code and include the stored data in the response body. It is the app's responsibility to compare the response with the intended data content. If there are any discrepancies, then a concurrency problem occured while writing the data and the app should request a fresh copy of the preferences data stored on the server, merge it with its local copy and attempt writing it again. <br><br>
<ul>
<li>URI:<code> GET /users/{user_id}/apps/{smart_app_id}/preferences </code></li>
<li>Client method name:<code> get_user_preferences </code></li>
</ul>
Returns the preferences blob unicode data stored in the user's account by a previous run of the app in the response body. If not data is available the call will return an empty string. <br><br>
[User Preferences RDF](../data_model/#User_Preferences)


