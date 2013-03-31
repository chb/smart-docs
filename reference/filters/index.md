---
layout: page
title: SMART API Filters and Pagination
includenav: smartnav.markdown
---
{% include JB/setup %}

<div class='simple_box'>
  {% include githublink %}
</div>

<div id="toc"></div>

The SMART API offers a basic filtering capability to narrow down large
clinical statement result sets on the server before returning data to
the client. As of SMART 0.6, for all API calls that return multiple
SMART Clinical Statements (e.g. `GET /records/xxx/lab_results`), you can
attach date filters if relevant to the returned data type, and in a few
select cases other datatype specific filters (such as LOINC codes on lab
results) as URL parameters.


# Common Date Filters

All SMART API calls for clinical statements that have a `date` or
`startDate` attribute can now be filtered on those attributes by sending
the following query parameters in the request.

Note: even if the data includes an `endDate`, it is not used by any of
the current filters.

- `date_from`
- `date_from_excluding`
- `date_from_including`
- `date_to`
- `date_to_excluding`
- `date_to_including`


# Statement Specific Filters

The following calls have additional filters:

## [Lab Results](/reference/data_model/#Lab_Result)

  `loinc`: a pipe-separated LOINC codes. e.g. `loinc=29571-7|38478-4`

## [Vital Sign Sets](/reference/data_model/#Vital_Sign_Set)

  `encounter_type`: pipe-separated encounter types. e.g. `encounter_type=ambulatory`

## [Medications](/reference/data_model/#Medication)

  `rxnorm`: a pipe-separated list of RXNORM codes. e.g. `rxnorm=856845`

## [Problems](/reference/data_model/#Problem)

  `snomed`: a pipe-seperated list of SNOMED codes. e.g. `snomed=161891005i`

## [Procedures](/reference/data_model/#Procedure)

  `snomed`: a pipe-seperated list of SNOMED codes. e.g. `snomed=161891005`


# The Default Sort Order and Paginating Results

Each SMART API call that returns sets of Clinical Statements now have a
default sort order defined for them based on either the `date` or
`startDate` attribute. The previously defined `offset` parameter has
been removed. This requires a change in an app's pagination strategy to
use date filters, the `limit` parameter, and the metadata in the
`ResponseSummary` to paginate results.  See
also `resultsReturned` and `totalResultCount` in the `ResponseSummary`
object in the next section.

The default behavior of any call is to return all results, if no limit
is supplied in the request.


# Response Summary

To complement the filtering and pagination API, each query response
includes a `api:ResponseSummary`. e.g.

    <rdf:Description rdf:nodeID="Naa3f4ca7b6024d6ab616aa31fa5ab528">
        <api:processingTimeMs rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">19</api:processingTimeMs>
        <rdf:type rdf:resource="http://smartplatforms.org/terms/api#ResponseSummary"/>
        <api:resultsReturned rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2</api:resultsReturned>
        <api:totalResultCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2</api:totalResultCount>
        <api:resultOrder rdf:nodeID="Nff3cac65263543dfa82450b51355c031"/>
      </rdf:Description>
