---
layout: page
title: SMART API Filters and Pagination
includenav: smartnav.markdown
---
{% include JB/setup %}
<div id="toc"></div>


# API Design
Allow `GET` parameters on the existing "fetch all" calls starting with:
* `/records/xxx/lab_results/`
* `/records/xxx/vital_signs/`.  

Each parameter decomposes to a rule that can be expressed in SPARQL. 

# Specific rules for each clinical statement type

## Rules for LabResults

### `loinc=x|y|z` ? 
```
sp:labName/sp:code ?l. 
FILTER(
   ?l = uri(<http://purl.bioontology.org/ontology/LNC/x>) ||
   ?l = uri(<http://purl.bioontology.org/ontology/LNC/y>) ||
   ?l = uri(<http://purl.bioontology.org/ontology/LNC/z>)
)
```
### `date_from=x` ? 
```
sp:specimenCollected/sp:startDate ?d. 
FILTER(?d >= x).
)
```

## Rules for VitalSigns
? Determine whether to support queries across clinical statements (vitals ? encounter)

### `encounter_type=x`?
```
?v sp:encounter/sp:encounterType/sp:code ?c. 
FILTER(c=uri(<http://smartplatforms.org/terms/codes/EncounterType#x>’)
```


# Each API response includes a Summary
Each API response comes with a `spapi:ResponseSummary` attached.  For example

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
