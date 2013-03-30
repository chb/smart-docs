---
layout: page
title: SMART API Filters and Pagination
includenav: smartnav.markdown
---

{% include JB/setup %}

<div id='under_construction' class='red_box_thin'>
    This document is in the process of being updated to
    SMART v0.6 and will be ready shortly.
</div>

# Query Filtering and Pagination Tutorial

Note: Read the filtering and pagination [reference](/reference/filters/)
before reading this tutorial to familiarize youself with the details.

The SMART API now has the ability to return filtered and paginated data for
two data types: [lab results](/reference/data_model/#Lab_Result) and [vital
sign sets](/reference/data_model/#Vital_Sign_Set). This allows you to
limit the results returned from these calls instead of the previous
behavior of returning all of the record's labs or vitals which in many
real-world settings could return a large and unwieldy set of data.

Both the SMART REST and SMART Connect APIs expose this functionality, and
adding filtering and paging to your queries is a simple matter of adding a
few query parameters to your SMART API calls. By default all results of the
requested type in the record are returned in the default sort order. In
addition, a `responseSummary` object has been added to the results returned
which provides your callback functions a set of useful metadata that can be
used to make further calls.

We'll demonstrate this using the SMART Connect JSON-LD API and give an
brief code sample for the SMART REST Python client as well.

## An Javascript Example for Filtering Lab Results

For this example, we'll be using the SMART JSON-LD interface described
[here](../intro_to_jsonld/) to the SMART Connect Javascript library.

To start let's set up a query with the following parameters:

- Filter the labs to find this patient's LDL results. LDL's have three
  LOINC codes that differ only in the method used to find the result. We'll
  make a pipe (|) seperated string of these codes: `"13457-7|2089-1|18262-6"`
- Find the results from 2010-01-01 to 2012-01-01 using the `"date_from"`
  and `"date_to"` parameters.
- Lastly, let's restrict the number of returned results to a "page" 
  of 10 results by setting the `limit` parameter to `10` and the
  `offset` parameter to `0`. To fetch the next "page" of ten results,
  you would set the `offset` to `10` and keep the limit at `10`.

The parameters above are passed to the `get_lab_results` call as
a standard Javascript object and the results are passed to your
callback function in the same way as the other API calls:

{% highlight javascript %}
    SMART.get_lab_results({
        'date_from': '2010-01-01',
        'date_to':   '2012-01-01',
        'loinc':     '13457-7|2089-1|18262-6',
        'limit':     10,
        'offset':    0
    }).then(function(r){
        var ldls = r.objects.of_type.LabResult;
        $.each(ldls, function(i, ldl){
            // ouput each lab to the console
            var date = ldl.dcterms__date;
            var value = ldl.quantitativeResult.valueAndUnit.value;
            var unit = r.quantitativeResult.valueAndUnit.unit;
            console.log('LDL result: ', date, value, unit);
        })
      
        // view the responseSummary object
        var rs = r.objects.of_type.ResponseSummary;
        console.log('resultsReturned', rs.resultsReturned);
        console.log('totalResultCount', rs.totalResultCount);
        console.log('nextPageURL', rs.nextPageURL);
    })
{% endhighlight %}

## Filtering Vital Sign Sets

For `Vital Sign Sets` all of the above parameters are the same except for
one: instead of being able to filter the results on a set of LOINC codes
you can filter on the `encounter_type` with two types supported:
`ambulatory` or `inpatient`.

## Future Work

We plan on adding filtering and pagination features of more calls in the
API and adding richer sets of filtering criteria in the future.
