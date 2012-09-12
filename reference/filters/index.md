---
layout: page
title: SMART API Filters and Pagination
includenav: smartnav.markdown
---
{% include JB/setup %}
<div class='simple_box'>
  <p>
  This is a new API feature in the SMART v0.5 release. It is stable
enough for use, however it is likely that minor elements of the API may
change over time.
  </p>
  {% include githublink %}
</div>

<div id="toc"></div>

# Query filters on "fetch all" calls
The SMART 0.5 API introduces a basic filtering capability to narrow down result
sets.  For API calls that return SMART Clinical Statements (e.g. `GET
/records/xxx/lab_results`), you can attach filters as URL parameters.

Our initial focus is to support the highest-volume data:
lab results and vital sign sets.

Here's how filtering works.

##  Filtering Lab Results
Parameters for `GET /records/xxx/lab_results/`:

* `date_from`: earliest result to fetch.  e.g. `date_from=2000-05-01`

* `date_to`: latest result to fetch.  e.g. `date_to=2012-01-01`

* `loinc`: pipe-separated LOINC codes.  e.g. `loinc=29571-7|38478-4`

## Filtering Vital Sign Sets
Parameters for `GET /records/xxx/vital_sign_sets`:

* `date_from`: earliest result to fetch.  e.g. `date_from=2000-05-01`

* `date_to`: latest result to fetch.  e.g. `date_to=2012-01-01`

* `encounter_type`: pipe-separated encounter types.  e.g. `encounter_type=ambulatory`

# Paginating results

Along with the filters described above, each "fetch all" call can now return
paginated results. Just attach `limit=` and `offset=` parameters to a query.
For instance, to fetch the first page of twenty results, you could add:

```
limit=20&offset=0
```

The default behavior of any call is to return all results, if no limit
is supplied in the request.

# Sorting Results
When paginating results, a default sort order is applied.  This default presents
results sorted by date, i.e using the `dcterms:date` or `sp:startDate` property.

A future API release is expected to support custom sort orders.

# Response Summary
To complement the filtering and pagination API, each query response includes a
`spapi:ResponseSummary`.  The response summary provides a `nextPageURL` as well
as a `resultOrder` to simplify traversal of results in client code.

```
[] a spapi:ResponseSummary; 
smartapi:processingTimeMs: "120";
smartapi:nextPageURL: "http://sandbox-api.smartplatforms.org/records/123/medications/1235?limit=10&offset=20";
smartapi:resultsReturned: 7;
smartapi:totalResultCount: 200;
smartapi:resultOrder (<http://sandbox-api.smartplatforms.org/records/123/medications/1235>,
<http://sandbox-api.smartplatforms.org/records/123/medications/963>,
<http://sandbox-api.smartplatforms.org/records/123/medications/8254>,
<http://sandbox-api.smartplatforms.org/records/123/medications/9732>,
<http://sandbox-api.smartplatforms.org/records/123/medications/235>,
<http://sandbox-api.smartplatforms.org/records/123/medications/87342>,
<http://sandbox-api.smartplatforms.org/records/123/medications/2336>);
```

# More details: Reference Implementation

The examples below provide background on how we've implemented filters in the
SMART Reference EMR.

## Each parameter decomposes to a rule that can be expressed in SPARQL. 

### Rules for LabResults

#### `loinc=x|y|z` ? 
```
sp:labName/sp:code ?l. 
FILTER(
   ?l = uri(<http://purl.bioontology.org/ontology/LNC/x>) ||
   ?l = uri(<http://purl.bioontology.org/ontology/LNC/y>) ||
   ?l = uri(<http://purl.bioontology.org/ontology/LNC/z>)
)
```
#### `date_from=x` ? 
```
sp:specimenCollected/sp:startDate ?d. 
FILTER(?d >= x).
)
```

### Rules for VitalSigns

#### `encounter_type=x`?
```
?v sp:encounter/sp:encounterType/sp:code ?c. 
FILTER(c=uri(<http://smartplatforms.org/terms/codes/EncounterType#x>)
```
