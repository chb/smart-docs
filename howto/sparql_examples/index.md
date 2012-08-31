---
layout: page
title: SPARQL Examples for SMART
includenav: smartnav.markdown
---

{% include JB/setup %}

<div id="toc"> </div>


# SPARQL by Example

This page provides a set of example queries to help you get started interacting
with SMART patient record data. We'll build out several example SPARQL queries,
but please feel free to add on new material as you discover useful tidbits!


## Running Queries: Live In-browser or in Your Own Environment

You can use the form below to try out queries right away. Please note that to
use the live query tool, you'll need to include a `FROM <graph>` clause in your
query to supply data. If you're running these queries in your own environment,
you'll run them in the context of a particular graph (e.g. Patient Smith's
medication graph), rather than specifying `FROM` directly in the query.

Or you could run these examples on your own via:

* The command line using [rasqal](http://librdf.org/rasqal)
* Python, Perl, PHP, or Ruby using [librdf](http://librdf.org)
* Java using [Jena](http://jena.sourceforge.net),
  [Sesame](http://www.openrdf.org), or [Mulgara](http://www.mulgara.org)
* Javascript - when possible, we'll also provide examples that will work with the
  [rdfquery](http://code.google.com/p/rdfquery/) javascript library which is
  automatically provided by the [smart-api-client.js](/libraries/javascript/).


# The Examples

## Examining a Medication List

Let's work with some medication data, the kind returned by a SMART API call to
`GET /records/{record_id}/medications/`. To start off, let's write a query to find
the name of each medication in the list:

### Find Medication Names

<textarea id='q_med_names'></textarea>
<button onclick='javascript:run_query($("#q_med_names"), "meds");'>
  Run Query on Sample Medications List
</button>

Note the use of the `distinct` keyword: as in SQL, distinct will prune the list
for duplicates. So if the two medications in the patient record have the same
name, this query will collapse them into one result.

With `rdfquery`, we can achieve a similar result:

{% highlight javascript %}
 SMART.get_medications().success(function(response) {
      var fill_dates = response.graph
          .where("?m rdf:type sp:Medication")
          .where("?med sp:drugName ?medc")
          .where("?medc dcterms:title ?t");
   });
{% endhighlight %}
### Find Medication Quantities + Frequencies

<textarea id='q_med_quants'></textarea>
<button onclick='javascript:run_query($("#q_med_quants"), "meds");'>
  Run Query on Sample Medications List
</button>

### Find Medication Fulfillment Dates

<textarea id='q_med_dates'></textarea>
<button onclick='javascript:run_query($("#q_med_dates"), "meds");'>
  Run Query on Sample Medications List
</button>

{% highlight javascript %}
    SMART.get_medications().success(function(response) {
      var fill_dates = response.graph
          .where("?m rdf:type sp:Medication")
          .where("?m sp:fulfillment ?fill")
          .where("?med sp:drugName ?medc")
          .where("?medc dcterms:title ?t")
          .where("?fill dcterms:date ?fill_date");
  });
{% endhighlight  %}

### Find Medications Fulfilled Since January 2009

<textarea id='q_med_since'></textarea>
<button onclick='javascript:run_query($("#q_med_since"), "meds");'>
  Run Query on Sample Medications List
</button>


Again a similar result with `rdfquery`

{% highlight javascript %}
    SMART.get_medications().success(function(response) {
        var fill_dates = response.graph
            .where("?m rdf:type sp:Medication")
            .where("?m sp:fulfillment ?fill")
            .where("?med sp:drugName ?medc")
            .where("?medc dcterms:title ?t")
            .where("?fill dcterms:date ?fill_date")
            .filter(function() {
                return Date.parse(this.fill_date.value) >  Date.parse("2009-01-01T00:00:00Z");
             });
    });
{% endhighlight  %}

## Getting some Demographics

Here's a query that pulls out the first and last name from a patient's
demographics

### Find Patient's Name

<textarea id='q_demographics'></textarea>
<button onclick='javascript:run_query($("#q_demographics"), "demographics");'>
  Run Query on Sample Demographics
</button>

With rdfquery, we can achieve a similar result: 

{% highlight javascript %}
    SMART.get_demographics().success(function(response) {
        var person = response.graph
            .where("?d rdf:type  sp:Demographics")
            .where("?d v:n  ?name")
            .where("?name v:given-name ?fn")
            .where("?name v:family-name ?ln");
    });
{% endhighlight  %}

## Getting some Problems

Here's a query that pulls out the name of each problem

### Find Patient's Problems

<textarea id='q_problems'></textarea>
<button onclick='javascript:run_query($("#q_problems"), "problems");'>
  Run Query on Sample Problem List
</button>

With rdfquery, we can achieve a similar result

{% highlight javascript %}
    SMART.get_problems().success(function(response) {
        var person = response.graph
            .where("?pr rdf:type sp:Problem")
            .where("?pr sp:problemName ?pn")
            .where("?pn dcterms:title ?p");
      });
{% endhighlight  %}


### Finding Quantitative Labs

<textarea id='q_labs'></textarea>
<button onclick='javascript:run_query($("#q_labs"), "labs");'>
  Run Query on Sample Labs
</button>


<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js'></script>
<script src='examples.js'></script>
<script>
  $.each(examples, function(i,e){
    var tb = $("#"+e.id);
    tb.css({width: e.width+"em", height: e.height+"em"});
    tb.val(e.q);
  });
</script>

<script src='rdf_store.js'></script>
<script>
  run_query = function(qta, store) {
    var q = qta.val();  
    var f = qta.next();

    if (f.is("div[class='response']")) {
      f.remove();  
    }

    f = $("<div class='response' style='padding: 4px; border: 1px dashed black; width: 100%; overflow-x: hidden; overflow-y: auto; height: 10em;'></div>");
    qta.after(f);
    stores[store].execute(q, 
      function(success, results){
        f.html(resultsToTable(results));
      });
  };

  var resultsToTable = function(results){
    var t = "<table><tr>",
        heads = [];

        if (results.triples) {
          results = results.triples;
          results = $.map(results, function(r){
            return {
              subject: {value: r.subject.nominalValue},
              predicate: {value: r.predicate.nominalValue},
              object: {value: r.object.nominalValue},
            }
          });

          results = results.sort(function(a,b){
            if (a.subject.value > b.subject.value) return 1;
            if (a.subject.value < b.subject.value) return -1;
            return 0;
          });
        }
        if (results.length > 0) {
          $.each(results[0], function(k,v){
            t += "<th>"+k+"</th>";
            heads.push(k);
          });
        }
        t += "</tr>"
      $.each(results, function(i,r){
        t += "<tr>";
          $.each(heads, function(i,k){
            t += "<td>"+r[k].value+"</td>";
          });
          t += "</tr>";
      });
      t += "</table>";
    return t;
  };

  var stores = {
    meds: new rdfstore.Store(),
    labs: new rdfstore.Store(),
    demographics: new rdfstore.Store(),
    problems: new rdfstore.Store(),
  };

  $.each(stores, function(k,v) {
    $.ajax(k+".xml",{"dataType": "text"}).then(function(r){
      stores[k].load("application/rdf+xml", r, function(s,r){
      });
    });
  });

</script>
