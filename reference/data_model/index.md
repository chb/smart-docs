---
layout: page
title: SMART Data Model
includenav: smartnav.markdown
---
{% include JB/setup %}

{% include example_format_tabs_top.html %}

<div class='simple_box'>
  This is highly preliminary, not a commitment or final version of any
  particular API or data model. This is purely for internal collaboration and
  preview purposes.
</div>


<div id="toc"></div>


# Changelog

Click here for the list of [Changes to the API and Payloads](../change_log/).
And here is an [Atom Feed](https://github.com/chb/smart-docs-testing/gh-pages.atom)
if you would like to keep up to date that way as well.


# RDF Overview

SMART API calls return data in the form of RDF graphs. Within these graphs,
top-level SMART data objects have fully dereferenceable URIs. For instance,
let's consider a SMART-enabled EMR hosted with its API base at
<http://sample_smart_emr.com/smart-app/>. An individual medication in this EMR
might be retrievable via:

    GET http://sample_smart_emr.com/smart-app/records/123456/medications/664373).

When you issue a GET request for a top-level SMART object like a medication,
you'll receive a graph containing:

1. The object itself
2. All properties linking it to "core data" elements (such as a medication's `drugName`,
   which is a `CodedValue` node)
3. All properties linking it to other top-level SMART objects
4. All "core data" elements belonging to the elements in (3)

For instance, when you `GET` a medication, you'll get all the information about
that medication and any fulfillments that belong to it! Likewise, when you `GET`
a fulfillment, you'll get all the information about that fulfillment and the
medication to which it belongs.

Another way to say this is: when you make an API call for data, the graph you
receive goes one top-level SMART element deep.


# Important note: RDF/XML Serializations are not unique!

It's important to understand that SMART API calls return RDF graphs [RDF/XML][]
&mdash; and for a given graph, there are _multiple_ possible serializations. We
don't make guarantees about how a graph will be serialized, beyond saying that
it's valid RDF/XML. So to consume the SMART API, you should parse the RDF/XML
payloads as RDF/XML &mdash; for example, `don't` try to query them directly with
xpath!

[RDF/XML]: http://www.w3.org/TR/REC-rdf-syntax/

To give a concrete example, a medication might be serialized as:

{% highlight html %}
  <sp:Medication>
    ... { additional properties here }....
  </sp:Medication>
{% endhighlight  %}

Or you could see the equivalent:

{% highlight html %}
  <rdf:Description>
        <rdf:type rdf:resource="http://smartplatforms.org/terms#Medication"/>
    ... { additional properties here }....
  </rdf:Description>
{% endhighlight  %}

# Namespaces

A common set of namespace prefixes is used for the examples below. These are:


<table class="table table-striped">
  <caption align="bottom">RDF Namespaces</caption>
  <tr>
    <td>dcterms</td>
    <td><a href="http://purl.org/dc/terms/">http://purl.org/dc/terms/</a></td>
    <td>Dublin core terms</td>
  </tr>
  
   <tr>
    <td>foaf</td>
    <td><a href="http://xmlns.com/foaf/0.1/">http://xmlns.com/foaf/0.1/</a></td>
    <td>Friend of a friend</td>
  </tr>
  
   <tr>
    <td>rdf</td>
    <td><a href="http://www.w3.org/1999/02/22-rdf-syntax-ns#">http://www.w3.org/1999/02/22-rdf-syntax-ns#</a></td>
    <td>Resource description framework</td>
  </tr>
  
  <tr>
    <td>sp</td>
    <td><a href="http://smartplatforms.org/terms#">http://smartplatforms.org/terms#</a></td>
    <td>Smart platforms root namespace</td>
  </tr>
  
  <tr>
    <td>v</td>
    <td><a href="http://www.w3.org/2006/vcard/ns#">http://www.w3.org/2006/vcard/ns#</a></td>
    <td>vCard namespace</td>
  </tr>
</table>


# Naming Conventions in the SMART Ontology

We use the prefix `sp` to designate the <http://smartplatforms.org/terms>
namespace. Within this namespace, we use a simple convention to differentiate 
between classes and predicates:

* Class names are designated by `CamelCase` with a capitalized first character.
  Examples: `sp:Medication` and `sp:LabResult`.

* Predicate names are designated by `camelCase` with a lower-case first character.
  Examples: `sp:medication` or `sp:valueAndUnit`.

You may wonder why classes and predicates tend to have similar names. For
example, we define a class `sp:Medication` as well as a predicate `sp:medication`.
Here's why: a predicate like `sp:medication` is used to indicate that a clinical
statement is associated with a medication; a class like `sp:Medication` is used to
indicate that a clinical statement is a medication. For example, each
`sp:Fulfillment` statement is associated with a `sp:Medication` statement via the
predicate `sp:medication`. This makes sense when we consider a few RDF triples
that expresses the basic pattern, associating a fulfillment with its medication
via the `sp:medication` predicate

{% highlight html %}
  _:f123 rdf:type sp:Fulfillment.   # declares a Fulfillment statement
  _:m456 rdf:type sp:Medication.    # declares a Medication statement
  _:f123 sp:medication _:m456.      # links the Fulfillment to its Medication
{% endhighlight  %}


---

# Clinical Statement Types


## <span id='Alert'>`Alert`</span>

`Alert` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


Alerts are a way for an application to generate a message (about a patient record) intended for a human recipient.

<div id='Alert_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Alert_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Alert_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Alert_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Alert_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"> 

  <sp:Alert> 
    <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
    <sp:notes>Patient with T2DM is overdue for HbA1c</sp:notes>
    <sp:severity>
      <sp:CodedValue>
        <dcterms:title>Warning</dcterms:title>
        <sp:code>
          <spcode:AlertSeverity rdf:about="http://smartplatforms.org/terms/codes/AlertSeverity#warning">
            <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
            <dcterms:title>Warning</dcterms:title> 
            <sp:system>http://smartplatforms.org/terms/codes/AlertSeverity#</sp:system>
            <dcterms:identifier>warning</dcterms:identifier> 
          </spcode:AlertSeverity>   
        </sp:code>
      </sp:CodedValue>

    </sp:severity> 
  </sp:Alert>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:DIawMmoL574 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Alert> .
_:DIawMmoL574 <http://smartplatforms.org/terms#notes> "Patient with T2DM is overdue for HbA1c" .
_:DIawMmoL574 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL574 <http://smartplatforms.org/terms#severity> _:DIawMmoL575 .
_:DIawMmoL575 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL575 <http://purl.org/dc/terms/title> "Warning" .
_:DIawMmoL575 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/AlertSeverity#warning> .
<http://smartplatforms.org/terms/codes/AlertSeverity#warning> <http://purl.org/dc/terms/identifier> "warning" .
<http://smartplatforms.org/terms/codes/AlertSeverity#warning> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/AlertSeverity> .
<http://smartplatforms.org/terms/codes/AlertSeverity#warning> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/AlertSeverity#warning> <http://purl.org/dc/terms/title> "Warning" .
<http://smartplatforms.org/terms/codes/AlertSeverity#warning> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/AlertSeverity#" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://smartplatforms.org/terms/codes/AlertSeverity#warning> a sp:Code,
        spcode:AlertSeverity;
    dcterms:identifier "warning";
    dcterms:title "Warning";
    sp:system "http://smartplatforms.org/terms/codes/AlertSeverity#" .

[] a sp:Alert;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:notes "Patient with T2DM is overdue for HbA1c";
    sp:severity [ a sp:CodedValue;
            dcterms:title "Warning";
            sp:code <http://smartplatforms.org/terms/codes/AlertSeverity#warning> ] .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://chb.github.com/smart-docs-testing/reference/datamodel/contexts/smart_context.jsonld",
  "@id": [
    {
      "@id": "http://smartplatforms.org/terms/codes/AlertSeverity#warning",
      "@type": [
        "http://smartplatforms.org/terms/codes/AlertSeverity",
        "Code"
      ],
      "dcterms__identifier": "warning",
      "dcterms__title": "Warning",
      "system": "http://smartplatforms.org/terms/codes/AlertSeverity#"
    },
    {
      "@type": "Alert",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "notes": "Patient with T2DM is overdue for HbA1c",
      "severity": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://smartplatforms.org/terms/codes/AlertSeverity#warning"
        },
        "dcterms__title": "Warning"
      }
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Alert</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


alertLevel
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#alertLevel</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#AlertLevel'>AlertLevel</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
'>


notes
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#notes</span>
<br />
Message intended for a human recipient.	 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='Allergy'>`Allergy`</span>

`Allergy` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


SMART provides structure for representing alleriges accoring to well-specified standard vocabularies. A patient with no known allergies produces an AllergyExclusion providing further details (see below). Otherwise, each allergy has a category (drug, food, etc.), a severity, a reaction, and a substance or class of substances. Since we want these allergies to work as inputs to automated computations, we require specific coding systems to represent substances and classes of substances.

1. A drug allergy to a particular drug (e.g. cephalexin) must define a "substance" field with an ingredient-type RxNorm code (tty="IN"). (This is to avoid overly-specific statements like "the patient is allergic to a 500mg cephalexin oral tablet"!)

2. A drug allergy to an entire class of drugs (e.g. sulfonamides) must define a "class" field with an NDFRT code for the drug class.

3. A food or environmental allergy must define a "substance" field with a UNII code.

For instance, below are two allergies: first, an allergy to the entire class of sulfonamides (note the sp:class predicate and the NDFRT code provided); then, an allergy to a single cephalosporin drug, cephalexin (note the sp:substance predicate and the RxNorm Ingredient CUI provided):

<div id='Allergy_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Allergy_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Allergy_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Allergy_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Allergy_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"> 
      <sp:Allergy>
      <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
      <sp:drugClassAllergen>
      <sp:CodedValue>
        <dcterms:title>Sulfonamide Antibacterial</dcterms:title>
        <sp:code>
        <spcode:NDFRT rdf:about="http://purl.bioontology.org/ontology/NDFRT/N0000175503">
          <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
          <dcterms:title>Sulfonamide Antibacterial</dcterms:title>
          <sp:system>http://purl.bioontology.org/ontology/NDFRT/</sp:system>
          <dcterms:identifier>N0000175503</dcterms:identifier>
        </spcode:NDFRT>
        </sp:code>
      </sp:CodedValue>

      </sp:drugClassAllergen>
      <sp:severity>
      <sp:CodedValue>
          <dcterms:title>Severe</dcterms:title>
        <sp:code>
        <spcode:AllergySeverity rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/24484000">
          <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
          <dcterms:title>Severe</dcterms:title>
          <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
          <dcterms:identifier>24484000</dcterms:identifier>
        </spcode:AllergySeverity>
        </sp:code>
      </sp:CodedValue>
      </sp:severity>
      <sp:allergicReaction>
      <sp:CodedValue>
          <dcterms:title>Anaphylaxis</dcterms:title>
        <sp:code>
        <spcode:SNOMED rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/39579001">
          <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
          <dcterms:title>Anaphylaxis</dcterms:title>
          <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
          <dcterms:identifier>39579001</dcterms:identifier>
        </spcode:SNOMED>
        </sp:code>
      </sp:CodedValue>

      </sp:allergicReaction>
      <sp:category>
      <sp:CodedValue>
          <dcterms:title>Drug allergy</dcterms:title>   
        <sp:code>
        <spcode:AllergyCategory rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/416098002">
          <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
          <dcterms:title>Drug allergy</dcterms:title>   
          <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
          <dcterms:identifier>416098002</dcterms:identifier>
        </spcode:AllergyCategory>
        </sp:code>
      </sp:CodedValue>

      </sp:category>
   </sp:Allergy>

  <sp:Allergy>
      <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
      <sp:drugAllergen>
      <sp:CodedValue>
          <dcterms:title>Cephalexin</dcterms:title>
        <sp:code>
        <spcode:RxNorm_Ingredient rdf:about="http://purl.bioontology.org/ontology/RXNORM/2231">
          <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
          <dcterms:title>Cephalexin</dcterms:title>
          <sp:system>http://purl.bioontology.org/ontology/RXNORM/</sp:system>
          <dcterms:identifier>2231</dcterms:identifier>
        </spcode:RxNorm_Ingredient>
        </sp:code>
      </sp:CodedValue>

      </sp:drugAllergen>
      <sp:severity>
      <sp:CodedValue>
          <dcterms:title>Severe</dcterms:title>
        <sp:code>
        <spcode:AllergySeverity rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/24484000">
          <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
          <dcterms:title>Severe</dcterms:title>
          <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
          <dcterms:identifier>24484000</dcterms:identifier>
        </spcode:AllergySeverity>
        </sp:code>
      </sp:CodedValue>

      </sp:severity>
      <sp:allergicReaction>
      <sp:CodedValue>
          <dcterms:title>Anaphylaxis</dcterms:title>
        <sp:code>
        <spcode:SNOMED rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/39579001">
          <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
          <dcterms:title>Anaphylaxis</dcterms:title>
          <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
          <dcterms:identifier>39579001</dcterms:identifier>
        </spcode:SNOMED>
        </sp:code>
      </sp:CodedValue>

      </sp:allergicReaction>
      <sp:category>
      <sp:CodedValue>
          <dcterms:title>Drug allergy</dcterms:title>   
        <sp:code>
        <spcode:AllergyCategory rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/416098002">
          <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
          <dcterms:title>Drug allergy</dcterms:title>   
          <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
          <dcterms:identifier>416098002</dcterms:identifier>
        </spcode:AllergyCategory>
        </sp:code>
      </sp:CodedValue>

      </sp:category>
   </sp:Allergy>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:DIawMmoL589 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL589 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/NDFRT/N0000175503> .
_:DIawMmoL589 <http://purl.org/dc/terms/title> "Sulfonamide Antibacterial" .
_:DIawMmoL590 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL590 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/24484000> .
_:DIawMmoL590 <http://purl.org/dc/terms/title> "Severe" .
_:DIawMmoL596 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL596 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/39579001> .
_:DIawMmoL596 <http://purl.org/dc/terms/title> "Anaphylaxis" .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/SNOMED> .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://purl.org/dc/terms/identifier> "39579001" .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://purl.org/dc/terms/title> "Anaphylaxis" .
_:DIawMmoL597 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL597 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/416098002> .
_:DIawMmoL597 <http://purl.org/dc/terms/title> "Drug allergy" .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/AllergySeverity> .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://purl.org/dc/terms/identifier> "24484000" .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://purl.org/dc/terms/title> "Severe" .
_:DIawMmoL591 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL591 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/39579001> .
_:DIawMmoL591 <http://purl.org/dc/terms/title> "Anaphylaxis" .
_:DIawMmoL595 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL595 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/24484000> .
_:DIawMmoL595 <http://purl.org/dc/terms/title> "Severe" .
_:DIawMmoL588 <http://smartplatforms.org/terms#severity> _:DIawMmoL590 .
_:DIawMmoL588 <http://smartplatforms.org/terms#category> _:DIawMmoL592 .
_:DIawMmoL588 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL588 <http://smartplatforms.org/terms#drugClassAllergen> _:DIawMmoL589 .
_:DIawMmoL588 <http://smartplatforms.org/terms#allergicReaction> _:DIawMmoL591 .
_:DIawMmoL588 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Allergy> .
_:DIawMmoL593 <http://smartplatforms.org/terms#severity> _:DIawMmoL595 .
_:DIawMmoL593 <http://smartplatforms.org/terms#drugAllergen> _:DIawMmoL594 .
_:DIawMmoL593 <http://smartplatforms.org/terms#category> _:DIawMmoL597 .
_:DIawMmoL593 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL593 <http://smartplatforms.org/terms#allergicReaction> _:DIawMmoL596 .
_:DIawMmoL593 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Allergy> .
_:DIawMmoL594 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL594 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/RXNORM/2231> .
_:DIawMmoL594 <http://purl.org/dc/terms/title> "Cephalexin" .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/RxNorm_Ingredient> .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/RXNORM/" .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://purl.org/dc/terms/identifier> "2231" .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://purl.org/dc/terms/title> "Cephalexin" .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/AllergyCategory> .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://purl.org/dc/terms/identifier> "416098002" .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://purl.org/dc/terms/title> "Drug allergy" .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/NDFRT> .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/NDFRT/" .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://purl.org/dc/terms/identifier> "N0000175503" .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://purl.org/dc/terms/title> "Sulfonamide Antibacterial" .
_:DIawMmoL592 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL592 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/416098002> .
_:DIawMmoL592 <http://purl.org/dc/terms/title> "Drug allergy" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://purl.bioontology.org/ontology/NDFRT/N0000175503> a sp:Code,
        spcode:NDFRT;
    dcterms:identifier "N0000175503";
    dcterms:title "Sulfonamide Antibacterial";
    sp:system "http://purl.bioontology.org/ontology/NDFRT/" .

<http://purl.bioontology.org/ontology/RXNORM/2231> a sp:Code,
        spcode:RxNorm_Ingredient;
    dcterms:identifier "2231";
    dcterms:title "Cephalexin";
    sp:system "http://purl.bioontology.org/ontology/RXNORM/" .

<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> a sp:Code,
        spcode:AllergySeverity;
    dcterms:identifier "24484000";
    dcterms:title "Severe";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .

<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> a sp:Code,
        spcode:SNOMED;
    dcterms:identifier "39579001";
    dcterms:title "Anaphylaxis";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .

<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> a sp:Code,
        spcode:AllergyCategory;
    dcterms:identifier "416098002";
    dcterms:title "Drug allergy";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .

[] a sp:Allergy;
    sp:allergicReaction [ a sp:CodedValue;
            dcterms:title "Anaphylaxis";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/39579001> ];
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:category [ a sp:CodedValue;
            dcterms:title "Drug allergy";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/416098002> ];
    sp:drugClassAllergen [ a sp:CodedValue;
            dcterms:title "Sulfonamide Antibacterial";
            sp:code <http://purl.bioontology.org/ontology/NDFRT/N0000175503> ];
    sp:severity [ a sp:CodedValue;
            dcterms:title "Severe";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/24484000> ] .

[] a sp:Allergy;
    sp:allergicReaction [ a sp:CodedValue;
            dcterms:title "Anaphylaxis";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/39579001> ];
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:category [ a sp:CodedValue;
            dcterms:title "Drug allergy";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/416098002> ];
    sp:drugAllergen [ a sp:CodedValue;
            dcterms:title "Cephalexin";
            sp:code <http://purl.bioontology.org/ontology/RXNORM/2231> ];
    sp:severity [ a sp:CodedValue;
            dcterms:title "Severe";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/24484000> ] .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://chb.github.com/smart-docs-testing/reference/datamodel/contexts/smart_context.jsonld",
  "@id": [
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/416098002",
      "@type": [
        "Code",
        "spcode__AllergyCategory"
      ],
      "dcterms__identifier": "416098002",
      "dcterms__title": "Drug allergy",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    },
    {
      "@type": "Allergy",
      "allergicReaction": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/39579001"
        },
        "dcterms__title": "Anaphylaxis"
      },
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "category": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/416098002"
        },
        "dcterms__title": "Drug allergy"
      },
      "drugAllergen": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/RXNORM/2231"
        },
        "dcterms__title": "Cephalexin"
      },
      "severity": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/24484000"
        },
        "dcterms__title": "Severe"
      }
    },
    {
      "@type": "Allergy",
      "allergicReaction": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/39579001"
        },
        "dcterms__title": "Anaphylaxis"
      },
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "category": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/416098002"
        },
        "dcterms__title": "Drug allergy"
      },
      "drugClassAllergen": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/NDFRT/N0000175503"
        },
        "dcterms__title": "Sulfonamide Antibacterial"
      },
      "severity": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/24484000"
        },
        "dcterms__title": "Severe"
      }
    },
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/39579001",
      "@type": [
        "Code",
        "spcode__SNOMED"
      ],
      "dcterms__identifier": "39579001",
      "dcterms__title": "Anaphylaxis",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/NDFRT/N0000175503",
      "@type": [
        "Code",
        "spcode__NDFRT"
      ],
      "dcterms__identifier": "N0000175503",
      "dcterms__title": "Sulfonamide Antibacterial",
      "system": "http://purl.bioontology.org/ontology/NDFRT/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/24484000",
      "@type": [
        "Code",
        "spcode__AllergySeverity"
      ],
      "dcterms__identifier": "24484000",
      "dcterms__title": "Severe",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/RXNORM/2231",
      "@type": [
        "Code",
        "spcode__RxNorm_Ingredient"
      ],
      "dcterms__identifier": "2231",
      "dcterms__title": "Cephalexin",
      "system": "http://purl.bioontology.org/ontology/RXNORM/"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Allergy</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


allergicReaction
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#allergicReaction</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#SNOMED'>SNOMED</a>
Reaction associated with an allergy.  Code drawn from SNOMED-CT.
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


category
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#category</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#AllergyCategory'>AllergyCategory</a>
Category of an allergy (food, drug, other substance).
</td>
</tr>

<tr><td style='width: 30%;
'>


drugAllergen
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#drugAllergen</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#RxNorm_Ingredient'>RxNorm_Ingredient</a>
For drug allergies, an RxNorm Concept at the ingredient level (TTY='in').
</td>
</tr>

<tr><td style='width: 30%;
'>


drugClassAllergen
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#drugClassAllergen</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#NDFRT'>NDFRT</a>
Class of allergen, e.g. Sulfonamides or ACE inhibitors.  RDF Code node with code drawn from
            NDF-RT: http://purl.bioontology.org/ontology/NDFRT/{NDFRT_ID}
</td>
</tr>

<tr><td style='width: 30%;
'>


foodAllergen
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#foodAllergen</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#UNII'>UNII</a>
Substance acting as a food or environmental allergen.  For environmental and food substance is a UNII:

</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


severity
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#severity</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#AllergySeverity'>AllergySeverity</a>
Severity of an allergy	
</td>
</tr>

</table>

## <span id='Allergy_Exclusion'>`Allergy Exclusion`</span>

`Allergy Exclusion` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


In clinical documentation, asserting that a patient has "No known allergies" is very different from not mentioning whether a patient has any allergies.  It's a positive affirmation that a question was asked and answered.  SMART models this information as an explicit clinical statement of the type AllergyExclusion.

While it might seem inelegant to expose explicit AllergyExclusion statements, this model is designed to combat a clinical modeling pattern where a single flag ("isNegated" or "negationIndicator" for example) negates the meaning of an entire statement.  Interpreting statements in a world where negation flags exist can be tricky.  Every app has to understand the subtlety of this flag -- and it's not always clear what it means to negate a statement with multiple parts.  For more information about exclusion statements in clinical modeling, see http://omowizard.wordpress.com/2011/06/06/unambiguous-data-positive-presence-positive-absence/.

<div id='Allergy_Exclusion_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Allergy_Exclusion_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Allergy_Exclusion_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Allergy_Exclusion_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Allergy_Exclusion_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"> 

<sp:AllergyExclusion>
  <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
  <sp:allergyExclusionName>
      <sp:CodedValue>
        <dcterms:title>No known allergies</dcterms:title>
        <sp:code>
          <spcode:AllergyExclusion rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/160244002">
           <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
           <dcterms:title>No known allergies</dcterms:title>
           <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
           <dcterms:identifier>160244002</dcterms:identifier>
          </spcode:AllergyExclusion>
        </sp:code>
      </sp:CodedValue>
  </sp:allergyExclusionName>
</sp:AllergyExclusion>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:DIawMmoL623 <http://purl.org/dc/terms/title> "No known allergies" .
_:DIawMmoL623 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL623 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/160244002> .
_:DIawMmoL622 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#AllergyExclusion> .
_:DIawMmoL622 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL622 <http://smartplatforms.org/terms#allergyExclusionName> _:DIawMmoL623 .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://purl.org/dc/terms/title> "No known allergies" .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/AllergyExclusion> .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://purl.org/dc/terms/identifier> "160244002" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> a sp:Code,
        spcode:AllergyExclusion;
    dcterms:identifier "160244002";
    dcterms:title "No known allergies";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .

[] a sp:AllergyExclusion;
    sp:allergyExclusionName [ a sp:CodedValue;
            dcterms:title "No known allergies";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/160244002> ];
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591> .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://chb.github.com/smart-docs-testing/reference/datamodel/contexts/smart_context.jsonld",
  "@id": [
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/160244002",
      "@type": [
        "Code",
        "spcode__AllergyExclusion"
      ],
      "dcterms__identifier": "160244002",
      "dcterms__title": "No known allergies",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    },
    {
      "@type": "AllergyExclusion",
      "allergyExclusionName": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/160244002"
        },
        "dcterms__title": "No known allergies"
      },
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      }
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#AllergyExclusion</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


allergyExclusionName
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#allergyExclusionName</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#AllergyExclusion'>AllergyExclusion</a>
Nature of the allergy exclusion.
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

</table>

## <span id='Demographics'>`Demographics`</span>

`Demographics` is a subtype of and inherits properties from:
[Component](#Component), [Person](#Person), [SMART Statement](#SMART_Statement), [VCard](#VCard)


In RDF/XML, patient Bob Odenkirk looks like this: 

<div id='Demographics_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Demographics_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Demographics_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Demographics_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Demographics_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:v="http://www.w3.org/2006/vcard/ns#"
  xmlns:foaf="http://xmlns.com/foaf/0.1/">
   <sp:Demographics>
     <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
     <v:n>
        <v:Name>
            <v:given-name>Bob</v:given-name>
            <v:additional-name>J</v:additional-name>
            <v:family-name>Odenkirk</v:family-name>
        </v:Name>
     </v:n>

     <v:adr>
        <v:Address>
          <rdf:type rdf:resource="http://www.w3.org/2006/vcard/ns#Home" />
          <rdf:type rdf:resource="http://www.w3.org/2006/vcard/ns#Pref" />

          <v:street-address>15 Main St</v:street-address>
          <v:extended-address>Apt 2</v:extended-address>
          <v:locality>Wonderland</v:locality>
          <v:region>OZ</v:region>
          <v:postal-code>54321</v:postal-code>
          <v:country>USA</v:country>
        </v:Address>
     </v:adr>

     <v:tel>
        <v:Tel>
          <rdf:type rdf:resource="http://www.w3.org/2006/vcard/ns#Home" />
          <rdf:type rdf:resource="http://www.w3.org/2006/vcard/ns#Pref" />
          <rdf:value>800-555-1212</rdf:value>
        </v:Tel>
     </v:tel>

     <v:tel>
        <v:Tel>
          <rdf:type rdf:resource="http://www.w3.org/2006/vcard/ns#Cell" />
          <rdf:value>800-555-1515</rdf:value>
        </v:Tel>
     </v:tel>

     <foaf:gender>male</foaf:gender>
     <v:bday>1959-12-25</v:bday>
     <v:email>bob.odenkirk@example.com</v:email>

     <sp:medicalRecordNumber>
       <sp:Code>
        <dcterms:title>My Hospital Record 2304575</dcterms:title> 
        <dcterms:identifier>2304575</dcterms:identifier> 
        <sp:system>My Hospital Record</sp:system> 
       </sp:Code>
     </sp:medicalRecordNumber>

   </sp:Demographics>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:DIawMmoL637 <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "800-555-1515" .
_:DIawMmoL637 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Cell> .
_:DIawMmoL637 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Tel> .
_:DIawMmoL635 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Pref> .
_:DIawMmoL635 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Address> .
_:DIawMmoL635 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Home> .
_:DIawMmoL635 <http://www.w3.org/2006/vcard/ns#postal-code> "54321" .
_:DIawMmoL635 <http://www.w3.org/2006/vcard/ns#region> "OZ" .
_:DIawMmoL635 <http://www.w3.org/2006/vcard/ns#extended-address> "Apt 2" .
_:DIawMmoL635 <http://www.w3.org/2006/vcard/ns#locality> "Wonderland" .
_:DIawMmoL635 <http://www.w3.org/2006/vcard/ns#street-address> "15 Main St" .
_:DIawMmoL635 <http://www.w3.org/2006/vcard/ns#country> "USA" .
_:DIawMmoL634 <http://www.w3.org/2006/vcard/ns#given-name> "Bob" .
_:DIawMmoL634 <http://www.w3.org/2006/vcard/ns#family-name> "Odenkirk" .
_:DIawMmoL634 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .
_:DIawMmoL634 <http://www.w3.org/2006/vcard/ns#additional-name> "J" .
_:DIawMmoL636 <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "800-555-1212" .
_:DIawMmoL636 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Pref> .
_:DIawMmoL636 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Tel> .
_:DIawMmoL636 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Home> .
_:DIawMmoL633 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Demographics> .
_:DIawMmoL633 <http://xmlns.com/foaf/0.1/gender> "male" .
_:DIawMmoL633 <http://www.w3.org/2006/vcard/ns#adr> _:DIawMmoL635 .
_:DIawMmoL633 <http://www.w3.org/2006/vcard/ns#bday> "1959-12-25" .
_:DIawMmoL633 <http://smartplatforms.org/terms#medicalRecordNumber> _:DIawMmoL638 .
_:DIawMmoL633 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL633 <http://www.w3.org/2006/vcard/ns#n> _:DIawMmoL634 .
_:DIawMmoL633 <http://www.w3.org/2006/vcard/ns#tel> _:DIawMmoL637 .
_:DIawMmoL633 <http://www.w3.org/2006/vcard/ns#tel> _:DIawMmoL636 .
_:DIawMmoL633 <http://www.w3.org/2006/vcard/ns#email> "bob.odenkirk@example.com" .
_:DIawMmoL638 <http://smartplatforms.org/terms#system> "My Hospital Record" .
_:DIawMmoL638 <http://purl.org/dc/terms/title> "My Hospital Record 2304575" .
_:DIawMmoL638 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
_:DIawMmoL638 <http://purl.org/dc/terms/identifier> "2304575" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

[] a sp:Demographics;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:medicalRecordNumber [ a sp:Code;
            dcterms:identifier "2304575";
            dcterms:title "My Hospital Record 2304575";
            sp:system "My Hospital Record" ];
    vcard:adr [ a vcard:Address,
                vcard:Home,
                vcard:Pref;
            vcard:country "USA";
            vcard:extended-address "Apt 2";
            vcard:locality "Wonderland";
            vcard:postal-code "54321";
            vcard:region "OZ";
            vcard:street-address "15 Main St" ];
    vcard:bday "1959-12-25";
    vcard:email "bob.odenkirk@example.com";
    vcard:n [ a vcard:Name;
            vcard:additional-name "J";
            vcard:family-name "Odenkirk";
            vcard:given-name "Bob" ];
    vcard:tel [ a vcard:Home,
                vcard:Pref,
                vcard:Tel;
            rdf:value "800-555-1212" ],
        [ a vcard:Cell,
                vcard:Tel;
            rdf:value "800-555-1515" ];
    foaf:gender "male" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://chb.github.com/smart-docs-testing/reference/datamodel/contexts/smart_context.jsonld",
  "@type": "Demographics",
  "belongsTo": {
    "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
  },
  "foaf__gender": "male",
  "medicalRecordNumber": [
    {
      "@type": "Code",
      "dcterms__identifier": "2304575",
      "dcterms__title": "My Hospital Record 2304575",
      "system": "My Hospital Record"
    }
  ],
  "vcard__adr": [
    {
      "@type": [
        "vcard__Pref",
        "vcard__Address",
        "vcard__Home"
      ],
      "http://www.w3.org/2006/vcard/ns#country": "USA",
      "vcard__extended_address": "Apt 2",
      "vcard__locality": "Wonderland",
      "vcard__postal_code": "54321",
      "vcard__region": "OZ",
      "vcard__street_address": "15 Main St"
    }
  ],
  "vcard__bday": "1959-12-25",
  "vcard__email": [
    "bob.odenkirk@example.com"
  ],
  "vcard__n": {
    "@type": "vcard__Name",
    "vcard__additional_name": [
      "J"
    ],
    "vcard__family_name": "Odenkirk",
    "vcard__given_name": "Bob"
  },
  "vcard__tel": [
    {
      "@type": [
        "vcard__Cell",
        "vcard__Tel"
      ],
      "rdf__value": "800-555-1515"
    },
    {
      "@type": [
        "vcard__Pref",
        "vcard__Tel",
        "vcard__Home"
      ],
      "rdf__value": "800-555-1212"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Demographics</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
'>


ethnicity
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#ethnicity</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


medicalRecordNumber
<br />
<span style='font-size: small; font-weight: normal'>Required: 1 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#medicalRecordNumber</span>
<br />
<a href='#Code'>Code</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


preferredLanguage
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#preferredLanguage</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


race
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#race</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


adr
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#adr</span>
<br />
<a href='#Address'>Address</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


bday
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#bday</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


email
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#email</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


n
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#n</span>
<br />
<a href='#Name'>Name</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


tel
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#tel</span>
<br />
<a href='#Tel'>Tel</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


gender
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://xmlns.com/foaf/0.1/gender</span>
<br />
A person's (administrative) gender.  This should consist of the string "male" or "female". <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='Encounter'>`Encounter`</span>

`Encounter` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


<div id='Encounter_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Encounter_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Encounter_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Encounter_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Encounter_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:v="http://www.w3.org/2006/vcard/ns#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"> 
      <sp:Encounter>
      <sp:belongsTo  rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
      <sp:startDate>2010-05-12T04:00:00Z</sp:startDate>
      <sp:endDate>2010-05-12T04:20:00Z</sp:endDate>
      <sp:encounterType>
       <sp:CodedValue>
         <dcterms:title>Ambulatory encounter</dcterms:title>
         <sp:code>
          <spcode:EncounterType rdf:about="http://smartplatforms.org/terms/codes/EncounterType#ambulatory">
            <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
            <dcterms:title>Ambulatory encounter</dcterms:title>
            <sp:system>http://smartplatforms.org/terms/codes/EncounterType#</sp:system>
            <dcterms:identifier>ambulatory</dcterms:identifier> 
          </spcode:EncounterType>       
         </sp:code>
       </sp:CodedValue>

      </sp:encounterType>
    </sp:Encounter>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:DIawMmoL675 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Encounter> .
_:DIawMmoL675 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL675 <http://smartplatforms.org/terms#endDate> "2010-05-12T04:20:00Z" .
_:DIawMmoL675 <http://smartplatforms.org/terms#startDate> "2010-05-12T04:00:00Z" .
_:DIawMmoL675 <http://smartplatforms.org/terms#encounterType> _:DIawMmoL676 .
_:DIawMmoL676 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL676 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/EncounterType#ambulatory> .
_:DIawMmoL676 <http://purl.org/dc/terms/title> "Ambulatory encounter" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/EncounterType> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/identifier> "ambulatory" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/EncounterType#" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/title> "Ambulatory encounter" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> a sp:Code,
        spcode:EncounterType;
    dcterms:identifier "ambulatory";
    dcterms:title "Ambulatory encounter";
    sp:system "http://smartplatforms.org/terms/codes/EncounterType#" .

[] a sp:Encounter;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:encounterType [ a sp:CodedValue;
            dcterms:title "Ambulatory encounter";
            sp:code <http://smartplatforms.org/terms/codes/EncounterType#ambulatory> ];
    sp:endDate "2010-05-12T04:20:00Z";
    sp:startDate "2010-05-12T04:00:00Z" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://chb.github.com/smart-docs-testing/reference/datamodel/contexts/smart_context.jsonld",
  "@id": [
    {
      "@type": "Encounter",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "encounterType": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://smartplatforms.org/terms/codes/EncounterType#ambulatory"
        },
        "dcterms__title": "Ambulatory encounter"
      },
      "endDate": "2010-05-12T04:20:00Z",
      "startDate": "2010-05-12T04:00:00Z"
    },
    {
      "@id": "http://smartplatforms.org/terms/codes/EncounterType#ambulatory",
      "@type": [
        "Code",
        "spcode__EncounterType"
      ],
      "dcterms__identifier": "ambulatory",
      "dcterms__title": "Ambulatory encounter",
      "system": "http://smartplatforms.org/terms/codes/EncounterType#"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Encounter</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


encounterType
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#encounterType</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#EncounterType'>EncounterType</a>
Type of encounter
</td>
</tr>

<tr><td style='width: 30%;
'>


endDate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#endDate</span>
<br />
Date when encounter ended <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


facility
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#facility</span>
<br />
<a href='#Organization'>Organization</a>
Facility where encounter occurred
</td>
</tr>

<tr><td style='width: 30%;
'>


provider
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#provider</span>
<br />
<a href='#Provider'>Provider</a>
Provider responsible for encounter
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


startDate
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#startDate</span>
<br />
Date when encounter began <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

</table>

## <span id='Fulfillment'>`Fulfillment`</span>

`Fulfillment` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


<div id='Fulfillment_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Fulfillment_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Fulfillment_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Fulfillment_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Fulfillment_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:foaf="http://xmlns.com/foaf/0.1/"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:v="http://www.w3.org/2006/vcard/ns#">
 <sp:Fulfillment>
    <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
    <dcterms:date>2010-05-12T04:00:00Z</dcterms:date>
    <sp:medication rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591/medications/123" />
    <sp:provider>
      <sp:Provider>
        <v:n>
          <v:Name>
           <v:given-name>Joshua</v:given-name>
           <v:family-name>Mandel</v:family-name>
          </v:Name>
        </v:n>
        <sp:npiNumber>5235235</sp:npiNumber>
        <sp:deaNumber>325555555</sp:deaNumber>
      </sp:Provider>
    </sp:provider>
    <sp:pharmacy>
      <sp:Pharmacy>
        <sp:ncpdpId>5235235</sp:ncpdpId>
            <v:organization-name>CVS #588</v:organization-name>
            <v:adr>
              <v:Address>
                <v:street-address>111 Lake Drive</v:street-address>
                <v:locality>WonderCity</v:locality>
                <v:postal-code>5555</v:postal-code>
                <v:country-name>Australia</v:country-name>
              </v:Address>
              </v:adr>
      </sp:Pharmacy>
    </sp:pharmacy>
    <sp:pbm>T00000000001011</sp:pbm>
    <sp:quantityDispensed>
      <sp:ValueAndUnit>
        <sp:value>60</sp:value>
        <sp:unit>{tablet}</sp:unit>
      </sp:ValueAndUnit>
    </sp:quantityDispensed>
    <sp:dispenseDaysSupply>30</sp:dispenseDaysSupply>
 </sp:Fulfillment>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:DIawMmoL698 <http://smartplatforms.org/terms#quantityDispensed> _:DIawMmoL703 .
_:DIawMmoL698 <http://smartplatforms.org/terms#pbm> "T00000000001011" .
_:DIawMmoL698 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Fulfillment> .
_:DIawMmoL698 <http://smartplatforms.org/terms#pharmacy> _:DIawMmoL701 .
_:DIawMmoL698 <http://smartplatforms.org/terms#medication> <http://sandbox-api.smartplatforms.org/records/2169591/medications/123> .
_:DIawMmoL698 <http://smartplatforms.org/terms#dispenseDaysSupply> "30" .
_:DIawMmoL698 <http://purl.org/dc/terms/date> "2010-05-12T04:00:00Z" .
_:DIawMmoL698 <http://smartplatforms.org/terms#provider> _:DIawMmoL699 .
_:DIawMmoL698 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL702 <http://www.w3.org/2006/vcard/ns#street-address> "111 Lake Drive" .
_:DIawMmoL702 <http://www.w3.org/2006/vcard/ns#postal-code> "5555" .
_:DIawMmoL702 <http://www.w3.org/2006/vcard/ns#country-name> "Australia" .
_:DIawMmoL702 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Address> .
_:DIawMmoL702 <http://www.w3.org/2006/vcard/ns#locality> "WonderCity" .
_:DIawMmoL699 <http://www.w3.org/2006/vcard/ns#n> _:DIawMmoL700 .
_:DIawMmoL699 <http://smartplatforms.org/terms#npiNumber> "5235235" .
_:DIawMmoL699 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Provider> .
_:DIawMmoL699 <http://smartplatforms.org/terms#deaNumber> "325555555" .
_:DIawMmoL700 <http://www.w3.org/2006/vcard/ns#given-name> "Joshua" .
_:DIawMmoL700 <http://www.w3.org/2006/vcard/ns#family-name> "Mandel" .
_:DIawMmoL700 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .
_:DIawMmoL701 <http://smartplatforms.org/terms#ncpdpId> "5235235" .
_:DIawMmoL701 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Pharmacy> .
_:DIawMmoL701 <http://www.w3.org/2006/vcard/ns#organization-name> "CVS #588" .
_:DIawMmoL701 <http://www.w3.org/2006/vcard/ns#adr> _:DIawMmoL702 .
_:DIawMmoL703 <http://smartplatforms.org/terms#value> "60" .
_:DIawMmoL703 <http://smartplatforms.org/terms#unit> "{tablet}" .
_:DIawMmoL703 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

[] a sp:Fulfillment;
    dcterms:date "2010-05-12T04:00:00Z";
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:dispenseDaysSupply "30";
    sp:medication <http://sandbox-api.smartplatforms.org/records/2169591/medications/123>;
    sp:pbm "T00000000001011";
    sp:pharmacy [ a sp:Pharmacy;
            sp:ncpdpId "5235235";
            vcard:adr [ a vcard:Address;
                    vcard:country-name "Australia";
                    vcard:locality "WonderCity";
                    vcard:postal-code "5555";
                    vcard:street-address "111 Lake Drive" ];
            vcard:organization-name "CVS #588" ];
    sp:provider [ a sp:Provider;
            sp:deaNumber "325555555";
            sp:npiNumber "5235235";
            vcard:n [ a vcard:Name;
                    vcard:family-name "Mandel";
                    vcard:given-name "Joshua" ] ];
    sp:quantityDispensed [ a sp:ValueAndUnit;
            sp:unit "{tablet}";
            sp:value "60" ] .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://chb.github.com/smart-docs-testing/reference/datamodel/contexts/smart_context.jsonld",
  "@type": "Fulfillment",
  "belongsTo": {
    "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
  },
  "dcterms__date": "2010-05-12T04:00:00Z",
  "dispenseDaysSupply": "30",
  "medication": {
    "@id": "http://sandbox-api.smartplatforms.org/records/2169591/medications/123"
  },
  "pbm": "T00000000001011",
  "pharmacy": {
    "@type": "Pharmacy",
    "ncpdpId": "5235235",
    "vcard__adr": [
      {
        "@type": "vcard__Address",
        "vcard__country_name": "Australia",
        "vcard__locality": "WonderCity",
        "vcard__postal_code": "5555",
        "vcard__street_address": "111 Lake Drive"
      }
    ],
    "vcard__organization_name": "CVS #588"
  },
  "provider": {
    "@type": "Provider",
    "deaNumber": "325555555",
    "npiNumber": "5235235",
    "vcard__n": {
      "@type": "vcard__Name",
      "vcard__family_name": "Mandel",
      "vcard__given_name": "Joshua"
    }
  },
  "quantityDispensed": {
    "@type": "ValueAndUnit",
    "unit": "{tablet}",
    "value": "60"
  }
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Fulfillment</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


date
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/date</span>
<br />
Date on which medication was dispensed <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


dispenseDaysSupply
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#dispenseDaysSupply</span>
<br />
The number of days' supply dispensed <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


medication
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#medication</span>
<br />
<a href='#Medication'>Medication</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


pbm
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#pbm</span>
<br />
The PBM providing payment for medications <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


pharmacy
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#pharmacy</span>
<br />
<a href='#Pharmacy'>Pharmacy</a>
The pharmacy that dispensed the medication
</td>
</tr>

<tr><td style='width: 30%;
'>


provider
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#provider</span>
<br />
<a href='#Provider'>Provider</a>
Clinician who prescribed the medication
</td>
</tr>

<tr><td style='width: 30%;
'>


quantityDispensed
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#quantityDispensed</span>
<br />
<a href='#ValueAndUnit'>ValueAndUnit</a>
Quantity dispensed, with units
</td>
</tr>

</table>

## <span id='Immunization'>`Immunization`</span>

`Immunization` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


Explicit record of an immunization given or not given to the patient.

<div id='Immunization_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Immunization_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Immunization_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Immunization_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Immunization_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"> 

   <sp:Immunization>
	  <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
	  <dcterms:date>2010-05-12T04:00:00Z</dcterms:date>

	  <sp:administrationStatus>
	    <sp:CodedValue>
	      <dcterms:title>Not Administered</dcterms:title>
	      <sp:code>
	        <sp:Code rdf:about="http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered">
	          <rdf:type rdf:resource="http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus" /> 
	          <dcterms:title>Not Administered</dcterms:title>
	          <sp:system>http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#</sp:system>
	          <dcterms:identifier>notAdministered</dcterms:identifier>
	        </sp:Code>
	      </sp:code>
	    </sp:CodedValue>
	  </sp:administrationStatus>

	  <sp:refusalReason>
	    <sp:CodedValue>
	      <dcterms:title>Allergy to vaccine/vaccine components, or allergy to eggs</dcterms:title>
	      <sp:code>
	        <sp:Code rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy">
	          <rdf:type rdf:resource="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason" /> 
	          <dcterms:title>Allergy to vaccine/vaccine components, or allergy to eggs</dcterms:title>
	          <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
	          <dcterms:identifier>allergy</dcterms:identifier>
	        </sp:Code>
	      </sp:code>
	    </sp:CodedValue>
	  </sp:refusalReason>

	  <sp:productName>
	    <sp:CodedValue>
	      <dcterms:title>typhoid, oral</dcterms:title>
	      <sp:code>
	        <sp:Code rdf:about="http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25">
	          <rdf:type rdf:resource="http://smartplatforms.org/terms/codes/ImmunizationProduct" /> 
	          <dcterms:title>typhoid, oral</dcterms:title>
	          <sp:system>http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#</sp:system>
	          <dcterms:identifier>25</dcterms:identifier>
	        </sp:Code>
	      </sp:code>
	    </sp:CodedValue>
	  </sp:productName>

	  <sp:productClass>
	    <sp:CodedValue>
	      <dcterms:title>TYPHOID</dcterms:title>
	      <sp:code>
	        <sp:Code rdf:about="http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID">
	          <rdf:type rdf:resource="http://smartplatforms.org/terms/codes/ImmunizationClass" /> 
	          <dcterms:title>TYPHOID</dcterms:title>
	          <sp:system>http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#</sp:system>
	          <dcterms:identifier>TYPHOID</dcterms:identifier>
	        </sp:Code>
	      </sp:code>
	    </sp:CodedValue>
	  </sp:productClass>

   </sp:Immunization>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:DIawMmoL733 <http://purl.org/dc/terms/title> "Allergy to vaccine/vaccine components, or allergy to eggs" .
_:DIawMmoL733 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> .
_:DIawMmoL733 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://purl.org/dc/terms/title> "Allergy to vaccine/vaccine components, or allergy to eggs" .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#" .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationRefusalReason> .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://purl.org/dc/terms/identifier> "allergy" .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://purl.org/dc/terms/title> "Not Administered" .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#" .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus> .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://purl.org/dc/terms/identifier> "notAdministered" .
_:DIawMmoL734 <http://purl.org/dc/terms/title> "typhoid, oral" .
_:DIawMmoL734 <http://smartplatforms.org/terms#code> <http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> .
_:DIawMmoL734 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL731 <http://smartplatforms.org/terms#administrationStatus> _:DIawMmoL732 .
_:DIawMmoL731 <http://smartplatforms.org/terms#productName> _:DIawMmoL734 .
_:DIawMmoL731 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Immunization> .
_:DIawMmoL731 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL731 <http://smartplatforms.org/terms#productClass> _:DIawMmoL735 .
_:DIawMmoL731 <http://purl.org/dc/terms/date> "2010-05-12T04:00:00Z" .
_:DIawMmoL731 <http://smartplatforms.org/terms#refusalReason> _:DIawMmoL733 .
_:DIawMmoL732 <http://purl.org/dc/terms/title> "Not Administered" .
_:DIawMmoL732 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> .
_:DIawMmoL732 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://purl.org/dc/terms/title> "typhoid, oral" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://smartplatforms.org/terms#system> "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationProduct> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://purl.org/dc/terms/identifier> "25" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://purl.org/dc/terms/title> "TYPHOID" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://smartplatforms.org/terms#system> "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationClass> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://purl.org/dc/terms/identifier> "TYPHOID" .
_:DIawMmoL735 <http://purl.org/dc/terms/title> "TYPHOID" .
_:DIawMmoL735 <http://smartplatforms.org/terms#code> <http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> .
_:DIawMmoL735 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> a sp:Code,
        spcode:ImmunizationAdministrationStatus;
    dcterms:identifier "notAdministered";
    dcterms:title "Not Administered";
    sp:system "http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#" .

<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> a sp:Code,
        spcode:ImmunizationRefusalReason;
    dcterms:identifier "allergy";
    dcterms:title "Allergy to vaccine/vaccine components, or allergy to eggs";
    sp:system "http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#" .

<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> a sp:Code,
        spcode:ImmunizationProduct;
    dcterms:identifier "25";
    dcterms:title "typhoid, oral";
    sp:system "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#" .

<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> a sp:Code,
        spcode:ImmunizationClass;
    dcterms:identifier "TYPHOID";
    dcterms:title "TYPHOID";
    sp:system "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#" .

[] a sp:Immunization;
    dcterms:date "2010-05-12T04:00:00Z";
    sp:administrationStatus [ a sp:CodedValue;
            dcterms:title "Not Administered";
            sp:code <http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> ];
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:productClass [ a sp:CodedValue;
            dcterms:title "TYPHOID";
            sp:code <http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> ];
    sp:productName [ a sp:CodedValue;
            dcterms:title "typhoid, oral";
            sp:code <http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> ];
    sp:refusalReason [ a sp:CodedValue;
            dcterms:title "Allergy to vaccine/vaccine components, or allergy to eggs";
            sp:code <http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> ] .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://chb.github.com/smart-docs-testing/reference/datamodel/contexts/smart_context.jsonld",
  "@id": [
    {
      "@id": "http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered",
      "@type": [
        "Code",
        "spcode__ImmunizationAdministrationStatus"
      ],
      "dcterms__identifier": "notAdministered",
      "dcterms__title": "Not Administered",
      "system": "http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#"
    },
    {
      "@type": "Immunization",
      "administrationStatus": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered"
        },
        "dcterms__title": "Not Administered"
      },
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "dcterms__date": "2010-05-12T04:00:00Z",
      "productClass": [
        {
          "@type": "CodedValue",
          "code": {
            "@id": "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID"
          },
          "dcterms__title": "TYPHOID"
        }
      ],
      "productName": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25"
        },
        "dcterms__title": "typhoid, oral"
      },
      "refusalReason": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy"
        },
        "dcterms__title": "Allergy to vaccine/vaccine components, or allergy to eggs"
      }
    },
    {
      "@id": "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID",
      "@type": [
        "Code",
        "spcode__ImmunizationClass"
      ],
      "dcterms__identifier": "TYPHOID",
      "dcterms__title": "TYPHOID",
      "system": "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#"
    },
    {
      "@id": "http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy",
      "@type": [
        "Code",
        "spcode__ImmunizationRefusalReason"
      ],
      "dcterms__identifier": "allergy",
      "dcterms__title": "Allergy to vaccine/vaccine components, or allergy to eggs",
      "system": "http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#"
    },
    {
      "@id": "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25",
      "@type": [
        "Code",
        "spcode__ImmunizationProduct"
      ],
      "dcterms__identifier": "25",
      "dcterms__title": "typhoid, oral",
      "system": "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Immunization</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


date
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/date</span>
<br />
ISO8601 formatted date and time when the medication was administered or offered. <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


administrationStatus
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#administrationStatus</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#ImmunizationAdministrationStatus'>ImmunizationAdministrationStatus</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
'>


productClass
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#productClass</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#ImmunizationClass'>ImmunizationClass</a>
coded name for the product class, according to the set of codes in the CDC Vaccine Groups controlled vocabulary.  For example, a class code meaning 'Rotavirus' would be assigned for a specific product such as Rotarix product.


productClass codes are drawn from the CDC's Vaccine Group vocabulary.  URIs are of the form:
http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#code


For example, the URI for the ROTAVIRUS code is:
http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#ROTAVIRUS
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


productName
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#productName</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#ImmunizationProduct'>ImmunizationProduct</a>
coded describing the product according to the set of codes in the CVX for immunizationa controlled vocabulary.  CVX Code URIs should be represented as:

http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#{code}


For exampe, the code for "adenovirus, type 4" is 54, and its URI is:

http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#54
</td>
</tr>

<tr><td style='width: 30%;
'>


refusalReason
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#refusalReason</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#ImmunizationRefusalReason'>ImmunizationRefusalReason</a>
If the administration status indicates this vaccination was refused, refusalReason is a CodedValue whose code is belongs to a controlled vocabulary of refusal reasons.
</td>
</tr>

</table>

## <span id='Lab_Result'>`Lab Result`</span>

`Lab Result` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


In RDF/XML, a serum sodium result looks like this: 

<div id='Lab_Result_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Lab_Result_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Lab_Result_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Lab_Result_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Lab_Result_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:sp="http://smartplatforms.org/terms#" 
  xmlns:dcterms="http://purl.org/dc/terms/" 
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
  xmlns:foaf="http://xmlns.com/foaf/0.1/"
  xmlns:v="http://www.w3.org/2006/vcard/ns#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/">

  <sp:LabResult>
      <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
      <sp:labName>
    <sp:CodedValue>
            <dcterms:title>Serum sodium</dcterms:title>
            <sp:provenance>
              <sp:CodeProvenance>
                <sp:sourceCode rdf:resource="http://my.local.coding.system/01234" />
                <dcterms:title>Random blood sodium level</dcterms:title>
                <sp:translationFidelity rdf:resource="http://smartplatforms.org/terms/codes/TranslationFidelity#verified"/>
              </sp:CodeProvenance>
            </sp:provenance>
        <sp:code>
              <spcode:LOINC rdf:about="http://purl.bioontology.org/ontology/LNC/2951-2">
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Serum sodium</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
                <dcterms:identifier>2951-2</dcterms:identifier> 
              </spcode:LOINC>    
          </sp:code>
        </sp:CodedValue>
      </sp:labName>

      <sp:quantitativeResult>
        <sp:QuantitativeResult>
          <sp:valueAndUnit>
            <sp:ValueAndUnit>
              <sp:value>140</sp:value>
              <sp:unit>mEq/L</sp:unit>
            </sp:ValueAndUnit>
          </sp:valueAndUnit>
          <sp:normalRange>
             <sp:ValueRange>
              <sp:minimum>
                <sp:ValueAndUnit>
                   <sp:value>135</sp:value>
                   <sp:unit>mEq/L</sp:unit>
                </sp:ValueAndUnit>
              </sp:minimum>
              <sp:maximum>
                <sp:ValueAndUnit>
                   <sp:value>145</sp:value>
                   <sp:unit>mEq/L</sp:unit>
                </sp:ValueAndUnit>
              </sp:maximum>
             </sp:ValueRange>
          </sp:normalRange>
          <sp:nonCriticalRange>
             <sp:ValueRange>
              <sp:minimum>
                <sp:ValueAndUnit>
                   <sp:value>120</sp:value>
                   <sp:unit>mEq/L</sp:unit>
                </sp:ValueAndUnit>
              </sp:minimum>
              <sp:maximum>
                <sp:ValueAndUnit>
                   <sp:value>155</sp:value>
                   <sp:unit>mEq/L</sp:unit>
                </sp:ValueAndUnit>
              </sp:maximum>
             </sp:ValueRange>
          </sp:nonCriticalRange>
        </sp:QuantitativeResult>
      </sp:quantitativeResult>
      <sp:accessionNumber>AC09205823577</sp:accessionNumber>
      <sp:labStatus>
    <sp:CodedValue>
      <dcterms:title>Final results: complete and verified</dcterms:title>      
      <sp:code>
        <spcode:LabResultStatus rdf:about="http://smartplatforms.org/terms/codes/LabStatus#final">
          <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
          <dcterms:title>Final</dcterms:title>      
          <sp:system>http://smartplatforms.org/terms/codes/LabStatus#</sp:system>
          <dcterms:identifier>final</dcterms:identifier> 
        </spcode:LabResultStatus>    
      </sp:code>
    </sp:CodedValue>

      </sp:labStatus>
      <sp:abnormalInterpretation>
    <sp:CodedValue>
      <dcterms:title>Normal</dcterms:title>      
      <sp:code>
        <spcode:LabResultInterpretation rdf:about="http://smartplatforms.org/terms/codes/LabResultInterpretation#normal">
          <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
          <dcterms:title>Normal</dcterms:title>      
          <sp:system>http://smartplatforms.org/terms/codes/LabResultInterpretation#</sp:system>
          <dcterms:identifier>normal</dcterms:identifier> 
        </spcode:LabResultInterpretation>    
      </sp:code>
    </sp:CodedValue>

      </sp:abnormalInterpretation>
      <sp:specimenCollected>
        <sp:Attribution>
          <sp:startDate>2010-12-27T17:00:00</sp:startDate>
        </sp:Attribution>
      </sp:specimenCollected>
      <sp:notes>Blood sample appears to have hemolyzed</sp:notes>
   </sp:LabResult>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/LabResultStatus> .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://purl.org/dc/terms/title> "Final" .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://purl.org/dc/terms/identifier> "final" .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/LabStatus#" .
_:DIawMmoL763 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:DIawMmoL763 <http://smartplatforms.org/terms#unit> "mEq/L" .
_:DIawMmoL763 <http://smartplatforms.org/terms#value> "135" .
_:DIawMmoL759 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodeProvenance> .
_:DIawMmoL759 <http://purl.org/dc/terms/title> "Random blood sodium level" .
_:DIawMmoL759 <http://smartplatforms.org/terms#sourceCode> <http://my.local.coding.system/01234> .
_:DIawMmoL759 <http://smartplatforms.org/terms#translationFidelity> <http://smartplatforms.org/terms/codes/TranslationFidelity#verified> .
_:DIawMmoL766 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:DIawMmoL766 <http://smartplatforms.org/terms#unit> "mEq/L" .
_:DIawMmoL766 <http://smartplatforms.org/terms#value> "120" .
_:DIawMmoL761 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:DIawMmoL761 <http://smartplatforms.org/terms#unit> "mEq/L" .
_:DIawMmoL761 <http://smartplatforms.org/terms#value> "140" .
_:DIawMmoL760 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#QuantitativeResult> .
_:DIawMmoL760 <http://smartplatforms.org/terms#normalRange> _:DIawMmoL762 .
_:DIawMmoL760 <http://smartplatforms.org/terms#nonCriticalRange> _:DIawMmoL765 .
_:DIawMmoL760 <http://smartplatforms.org/terms#valueAndUnit> _:DIawMmoL761 .
_:DIawMmoL768 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL768 <http://purl.org/dc/terms/title> "Final results: complete and verified" .
_:DIawMmoL768 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/LabStatus#final> .
_:DIawMmoL770 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Attribution> .
_:DIawMmoL770 <http://smartplatforms.org/terms#startDate> "2010-12-27T17:00:00" .
_:DIawMmoL769 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL769 <http://purl.org/dc/terms/title> "Normal" .
_:DIawMmoL769 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> .
_:DIawMmoL765 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueRange> .
_:DIawMmoL765 <http://smartplatforms.org/terms#maximum> _:DIawMmoL767 .
_:DIawMmoL765 <http://smartplatforms.org/terms#minimum> _:DIawMmoL766 .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/LabResultInterpretation> .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://purl.org/dc/terms/title> "Normal" .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://purl.org/dc/terms/identifier> "normal" .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/LabResultInterpretation#" .
_:DIawMmoL767 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:DIawMmoL767 <http://smartplatforms.org/terms#unit> "mEq/L" .
_:DIawMmoL767 <http://smartplatforms.org/terms#value> "155" .
_:DIawMmoL764 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:DIawMmoL764 <http://smartplatforms.org/terms#unit> "mEq/L" .
_:DIawMmoL764 <http://smartplatforms.org/terms#value> "145" .
_:DIawMmoL757 <http://smartplatforms.org/terms#labName> _:DIawMmoL758 .
_:DIawMmoL757 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL757 <http://smartplatforms.org/terms#specimenCollected> _:DIawMmoL770 .
_:DIawMmoL757 <http://smartplatforms.org/terms#labStatus> _:DIawMmoL768 .
_:DIawMmoL757 <http://smartplatforms.org/terms#accessionNumber> "AC09205823577" .
_:DIawMmoL757 <http://smartplatforms.org/terms#abnormalInterpretation> _:DIawMmoL769 .
_:DIawMmoL757 <http://smartplatforms.org/terms#quantitativeResult> _:DIawMmoL760 .
_:DIawMmoL757 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#LabResult> .
_:DIawMmoL757 <http://smartplatforms.org/terms#notes> "Blood sample appears to have hemolyzed" .
_:DIawMmoL762 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueRange> .
_:DIawMmoL762 <http://smartplatforms.org/terms#maximum> _:DIawMmoL764 .
_:DIawMmoL762 <http://smartplatforms.org/terms#minimum> _:DIawMmoL763 .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/LOINC> .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://purl.org/dc/terms/title> "Serum sodium" .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://purl.org/dc/terms/identifier> "2951-2" .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
_:DIawMmoL758 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL758 <http://purl.org/dc/terms/title> "Serum sodium" .
_:DIawMmoL758 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/2951-2> .
_:DIawMmoL758 <http://smartplatforms.org/terms#provenance> _:DIawMmoL759 .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://purl.bioontology.org/ontology/LNC/2951-2> a sp:Code,
        spcode:LOINC;
    dcterms:identifier "2951-2";
    dcterms:title "Serum sodium";
    sp:system "http://purl.bioontology.org/ontology/LNC/" .

<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> a sp:Code,
        spcode:LabResultInterpretation;
    dcterms:identifier "normal";
    dcterms:title "Normal";
    sp:system "http://smartplatforms.org/terms/codes/LabResultInterpretation#" .

<http://smartplatforms.org/terms/codes/LabStatus#final> a sp:Code,
        spcode:LabResultStatus;
    dcterms:identifier "final";
    dcterms:title "Final";
    sp:system "http://smartplatforms.org/terms/codes/LabStatus#" .

[] a sp:LabResult;
    sp:abnormalInterpretation [ a sp:CodedValue;
            dcterms:title "Normal";
            sp:code <http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> ];
    sp:accessionNumber "AC09205823577";
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:labName [ a sp:CodedValue;
            dcterms:title "Serum sodium";
            sp:code <http://purl.bioontology.org/ontology/LNC/2951-2>;
            sp:provenance [ a sp:CodeProvenance;
                    dcterms:title "Random blood sodium level";
                    sp:sourceCode <http://my.local.coding.system/01234>;
                    sp:translationFidelity <http://smartplatforms.org/terms/codes/TranslationFidelity#verified> ] ];
    sp:labStatus [ a sp:CodedValue;
            dcterms:title "Final results: complete and verified";
            sp:code <http://smartplatforms.org/terms/codes/LabStatus#final> ];
    sp:notes "Blood sample appears to have hemolyzed";
    sp:quantitativeResult [ a sp:QuantitativeResult;
            sp:nonCriticalRange [ a sp:ValueRange;
                    sp:maximum [ a sp:ValueAndUnit;
                            sp:unit "mEq/L";
                            sp:value "155" ];
                    sp:minimum [ a sp:ValueAndUnit;
                            sp:unit "mEq/L";
                            sp:value "120" ] ];
            sp:normalRange [ a sp:ValueRange;
                    sp:maximum [ a sp:ValueAndUnit;
                            sp:unit "mEq/L";
                            sp:value "145" ];
                    sp:minimum [ a sp:ValueAndUnit;
                            sp:unit "mEq/L";
                            sp:value "135" ] ];
            sp:valueAndUnit [ a sp:ValueAndUnit;
                    sp:unit "mEq/L";
                    sp:value "140" ] ];
    sp:specimenCollected [ a sp:Attribution;
            sp:startDate "2010-12-27T17:00:00" ] .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://chb.github.com/smart-docs-testing/reference/datamodel/contexts/smart_context.jsonld",
  "@id": [
    {
      "@id": "http://smartplatforms.org/terms/codes/LabStatus#final",
      "@type": [
        "spcode__LabResultStatus",
        "Code"
      ],
      "dcterms__identifier": "final",
      "dcterms__title": "Final",
      "system": "http://smartplatforms.org/terms/codes/LabStatus#"
    },
    {
      "@id": "http://smartplatforms.org/terms/codes/LabResultInterpretation#normal",
      "@type": [
        "spcode__LabResultInterpretation",
        "Code"
      ],
      "dcterms__identifier": "normal",
      "dcterms__title": "Normal",
      "system": "http://smartplatforms.org/terms/codes/LabResultInterpretation#"
    },
    {
      "@type": "LabResult",
      "abnormalInterpretation": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://smartplatforms.org/terms/codes/LabResultInterpretation#normal"
        },
        "dcterms__title": "Normal"
      },
      "accessionNumber": "AC09205823577",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "labName": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/LNC/2951-2"
        },
        "dcterms__title": "Serum sodium",
        "provenance": {
          "@type": "CodeProvenance",
          "dcterms__title": "Random blood sodium level",
          "sourceCode": {
            "@id": "http://my.local.coding.system/01234"
          },
          "translationFidelity": {
            "@id": "http://smartplatforms.org/terms/codes/TranslationFidelity#verified"
          }
        }
      },
      "labStatus": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://smartplatforms.org/terms/codes/LabStatus#final"
        },
        "dcterms__title": "Final results: complete and verified"
      },
      "notes": "Blood sample appears to have hemolyzed",
      "quantitativeResult": {
        "@type": "QuantitativeResult",
        "nonCriticalRange": {
          "@type": "ValueRange",
          "maximum": {
            "@type": "ValueAndUnit",
            "unit": "mEq/L",
            "value": "155"
          },
          "minimum": {
            "@type": "ValueAndUnit",
            "unit": "mEq/L",
            "value": "120"
          }
        },
        "normalRange": {
          "@type": "ValueRange",
          "maximum": {
            "@type": "ValueAndUnit",
            "unit": "mEq/L",
            "value": "145"
          },
          "minimum": {
            "@type": "ValueAndUnit",
            "unit": "mEq/L",
            "value": "135"
          }
        },
        "valueAndUnit": {
          "@type": "ValueAndUnit",
          "unit": "mEq/L",
          "value": "140"
        }
      },
      "specimenCollected": {
        "@type": "Attribution",
        "startDate": "2010-12-27T17:00:00"
      }
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/2951-2",
      "@type": [
        "Code",
        "spcode__LOINC"
      ],
      "dcterms__identifier": "2951-2",
      "dcterms__title": "Serum sodium",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#LabResult</caption>
<tbody>
<tr><td style='width: 30%;
'>


abnormalInterpretation
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#abnormalInterpretation</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#LabResultInterpretation'>LabResultInterpretation</a>
Abnormal interpretation status for this lab
</td>
</tr>

<tr><td style='width: 30%;
'>


accessionNumber
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#accessionNumber</span>
<br />
External accession number for a lab result <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


labName
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#labName</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#LOINC'>LOINC</a>
LOINC Coded Value for result (e.g. with title='Serum Sodium' and code=http://purl.bioontology.org/ontology/LNC/2951-2
</td>
</tr>

<tr><td style='width: 30%;
'>


labStatus
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#labStatus</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#LabResultStatus'>LabResultStatus</a>
Workflow status of this lab value (e.g. "finalized")
</td>
</tr>

<tr><td style='width: 30%;
'>


narrativeResult
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#narrativeResult</span>
<br />
<a href='#NarrativeResult'>NarrativeResult</a>
Narrative result, if any.
</td>
</tr>

<tr><td style='width: 30%;
'>


notes
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#notes</span>
<br />
Free-text notes about this result. <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


quantitativeResult
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#quantitativeResult</span>
<br />
<a href='#QuantitativeResult'>QuantitativeResult</a>
Qualitative result, if any
</td>
</tr>

<tr><td style='width: 30%;
'>


specimenCollected
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#specimenCollected</span>
<br />
<a href='#Attribution'>Attribution</a>
Attribution specificying when specimen was collected and who was responsible for them.
</td>
</tr>

</table>

## <span id='Medical_Record'>`Medical Record`</span>


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#MedicalRecord</caption>
<tbody>
<tr><td style='width: 30%;
'>


hasStatement
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#hasStatement</span>
<br />
<a href='#SMART_Statement'>SMART Statement</a>
</td>
</tr>

</table>

## <span id='Medication'>`Medication`</span>

`Medication` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


The SMART medication type expresses a medication at the level of an RxNorm branded or generic drug concept (e.g. "20 mg generic loratadine" or "20 mg brand-name claritin").  A medication may include start- and end-dates, as well as a free-text "instructions" field describing how it should be taken.  When the instructions are simple enough, we also represent them in a structured way, aiming to capture about 80% of outpatient medication dosing schedules.  A very simple semantic structure defines how much to take ("quantity") and how often ("frequency"). Both quantity and frequency are defined with expressions from [http://www.unitsofmeasure.org The Unified Code for Units of Measure], or UCUM (see below).

In RDF/XML notation, a patient on oral amitriptyline 50 mg tablets might provide the following RDF sub-graph as part of a medication list:
    

<div id='Medication_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Medication_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Medication_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Medication_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Medication_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"
  xmlns:dcterms="http://purl.org/dc/terms/">
   <sp:Medication>
      <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
      <sp:drugName>
      <sp:CodedValue>
          <dcterms:title>AMITRIPTYLINE HCL 50 MG TAB</dcterms:title>
          <sp:code>
            <spcode:RxNorm_Semantic rdf:about="http://purl.bioontology.org/ontology/RXNORM/856845">
              <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
              <sp:system>http://purl.bioontology.org/ontology/RXNORM/</sp:system>
              <dcterms:identifier>856845</dcterms:identifier>
              <dcterms:title>AMITRIPTYLINE HCL 50 MG TAB</dcterms:title>
            </spcode:RxNorm_Semantic>    
          </sp:code>
      </sp:CodedValue>
      </sp:drugName>
      <sp:startDate>2007-03-14</sp:startDate>
      <sp:endDate>2007-08-14</sp:endDate>
      <sp:instructions>Take two tablets twice daily as needed for pain</sp:instructions>
      <sp:quantity>
          <sp:ValueAndUnit>
            <sp:value>2</sp:value>
            <sp:unit>{tablet}</sp:unit>
          </sp:ValueAndUnit>
      </sp:quantity>
      <sp:frequency>
          <sp:ValueAndUnit>
            <sp:value>2</sp:value>
            <sp:unit>/d</sp:unit>
          </sp:ValueAndUnit>
      </sp:frequency>
   </sp:Medication>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/RxNorm_Semantic> .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/RXNORM/" .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://purl.org/dc/terms/identifier> "856845" .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://purl.org/dc/terms/title> "AMITRIPTYLINE HCL 50 MG TAB" .
_:DIawMmoL806 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:DIawMmoL806 <http://smartplatforms.org/terms#value> "2" .
_:DIawMmoL806 <http://smartplatforms.org/terms#unit> "{tablet}" .
_:DIawMmoL805 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL805 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/RXNORM/856845> .
_:DIawMmoL805 <http://purl.org/dc/terms/title> "AMITRIPTYLINE HCL 50 MG TAB" .
_:DIawMmoL804 <http://smartplatforms.org/terms#endDate> "2007-08-14" .
_:DIawMmoL804 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL804 <http://smartplatforms.org/terms#drugName> _:DIawMmoL805 .
_:DIawMmoL804 <http://smartplatforms.org/terms#startDate> "2007-03-14" .
_:DIawMmoL804 <http://smartplatforms.org/terms#frequency> _:DIawMmoL807 .
_:DIawMmoL804 <http://smartplatforms.org/terms#quantity> _:DIawMmoL806 .
_:DIawMmoL804 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Medication> .
_:DIawMmoL804 <http://smartplatforms.org/terms#instructions> "Take two tablets twice daily as needed for pain" .
_:DIawMmoL807 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:DIawMmoL807 <http://smartplatforms.org/terms#value> "2" .
_:DIawMmoL807 <http://smartplatforms.org/terms#unit> "/d" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://purl.bioontology.org/ontology/RXNORM/856845> a sp:Code,
        spcode:RxNorm_Semantic;
    dcterms:identifier "856845";
    dcterms:title "AMITRIPTYLINE HCL 50 MG TAB";
    sp:system "http://purl.bioontology.org/ontology/RXNORM/" .

[] a sp:Medication;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:drugName [ a sp:CodedValue;
            dcterms:title "AMITRIPTYLINE HCL 50 MG TAB";
            sp:code <http://purl.bioontology.org/ontology/RXNORM/856845> ];
    sp:endDate "2007-08-14";
    sp:frequency [ a sp:ValueAndUnit;
            sp:unit "/d";
            sp:value "2" ];
    sp:instructions "Take two tablets twice daily as needed for pain";
    sp:quantity [ a sp:ValueAndUnit;
            sp:unit "{tablet}";
            sp:value "2" ];
    sp:startDate "2007-03-14" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://chb.github.com/smart-docs-testing/reference/datamodel/contexts/smart_context.jsonld",
  "@id": [
    {
      "@id": "http://purl.bioontology.org/ontology/RXNORM/856845",
      "@type": [
        "Code",
        "spcode__RxNorm_Semantic"
      ],
      "dcterms__identifier": "856845",
      "dcterms__title": "AMITRIPTYLINE HCL 50 MG TAB",
      "system": "http://purl.bioontology.org/ontology/RXNORM/"
    },
    {
      "@type": "Medication",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "drugName": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/RXNORM/856845"
        },
        "dcterms__title": "AMITRIPTYLINE HCL 50 MG TAB"
      },
      "endDate": "2007-08-14",
      "frequency": {
        "@type": "ValueAndUnit",
        "unit": "/d",
        "value": "2"
      },
      "instructions": "Take two tablets twice daily as needed for pain",
      "quantity": {
        "@type": "ValueAndUnit",
        "unit": "{tablet}",
        "value": "2"
      },
      "startDate": "2007-03-14"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Medication</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


drugName
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#drugName</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#RxNorm_Semantic'>RxNorm_Semantic</a>
RxNorm Concept ID for this medication.  Note: the RxNorm CUI for a SMART medication should have one of the following four types:  SCD (Semantic Clinical Drug), SBD (Semantic Branded Drug), GPCK (Generic Pack), BPCK (Brand Name Pack).   Restricting medications to these four RxNorm types can also be expressed as "TTY in ('SCD','SBD','GPCK','BPCK')" -- and this restriction ensures that SMART medications use concepts of the appropriate specificity:  concepts like "650 mg generic acetaminophen" or "20 mg brand-name Claritin".   Please note that SMART medications do not include explicit structured data about pill strength, concentration, or precise ingredients.  These data are available through RxNorm, including through the free [http://rxnav.nlm.nih.gov/RxNormRestAPI.html RxNav REST API].  Code element with code drawn from http://purl.bioontology.org/ontology/RXNORM/{rxcui}
</td>
</tr>

<tr><td style='width: 30%;
'>


endDate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#endDate</span>
<br />

	When the patient stopped taking a medication 
	 <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


frequency
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#frequency</span>
<br />
<a href='#ValueAndUnit'>ValueAndUnit</a>

For a medication with a simple dosing schedule, record how often to take the medication.  The frequency should be recorded as a [http://www.unitsofmeasure.org/ UCUM] expression.  In this case we use a restricted subset of UCUM that defines the following units only:  "/d" (per day), "/wk" (per week), "/mo" (per month).  For example, you would express the concept of "TID" or "three times daily" as a ValueAndUnit node with quantity="3", unit="/d". 
	
</td>
</tr>

<tr><td style='width: 30%;
'>


fulfillment
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#fulfillment</span>
<br />
<a href='#Fulfillment'>Fulfillment</a>

A single fulfillment event (that is, the medication was dispensed to the patient by a pharmacy)
	
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


instructions
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#instructions</span>
<br />

	Clinician-supplied instructions from the prescription signature 
	 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


provenance
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#provenance</span>
<br />
<a href='#Code'>Code</a> where code comes from <a href='#MedicationProvenance'>MedicationProvenance</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


quantity
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#quantity</span>
<br />
<a href='#ValueAndUnit'>ValueAndUnit</a>

For a medication with a simple dosing schedule, record the amount to take with each administration.  The quantity should be recorded as a [http://www.unitsofmeasure.org/ UCUM] expression.  For some medications, the appoporiate quantity will be a volume (e.g. "5 mL" of an oral acetaminophen solution).  For other medications, the appropriate quantity may be expresses in terms of tablets, puffs, or actuations:  UCUM call these "non-units", and they should be written inside of curly braces to avoid confusion.  For example, you would express "1 tablet" as a ValueAndUnit node with quantity="1", unit="{tablet}".
	
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


startDate
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#startDate</span>
<br />

	When the patient started taking a medication 
	 <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

</table>

## <span id='Problem'>`Problem`</span>

`Problem` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


<div id='Problem_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Problem_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Problem_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Problem_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Problem_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"> 
    <sp:Problem>
      <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
      <sp:problemName>
      <sp:CodedValue>
          <dcterms:title>Backache (finding)</dcterms:title>      
          <sp:code>
            <spcode:SNOMED rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/161891005">
              <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
              <dcterms:title>Backache (finding)</dcterms:title>      
              <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
              <dcterms:identifier>161891005</dcterms:identifier> 
            </spcode:SNOMED>
          </sp:code>
      </sp:CodedValue>
      </sp:problemName>
      <sp:startDate>2007-06-12</sp:startDate>
      <sp:endDate>2007-08-01</sp:endDate>
    </sp:Problem>
</rdf:RDF>

{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:DIawMmoL839 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/161891005> .
_:DIawMmoL839 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL839 <http://purl.org/dc/terms/title> "Backache (finding)" .
_:DIawMmoL838 <http://smartplatforms.org/terms#startDate> "2007-06-12" .
_:DIawMmoL838 <http://smartplatforms.org/terms#endDate> "2007-08-01" .
_:DIawMmoL838 <http://smartplatforms.org/terms#problemName> _:DIawMmoL839 .
_:DIawMmoL838 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Problem> .
_:DIawMmoL838 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://purl.org/dc/terms/identifier> "161891005" .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/SNOMED> .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://purl.org/dc/terms/title> "Backache (finding)" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> a sp:Code,
        spcode:SNOMED;
    dcterms:identifier "161891005";
    dcterms:title "Backache (finding)";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .

[] a sp:Problem;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:endDate "2007-08-01";
    sp:problemName [ a sp:CodedValue;
            dcterms:title "Backache (finding)";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/161891005> ];
    sp:startDate "2007-06-12" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://chb.github.com/smart-docs-testing/reference/datamodel/contexts/smart_context.jsonld",
  "@id": [
    {
      "@type": "Problem",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "endDate": "2007-08-01",
      "problemName": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/161891005"
        },
        "dcterms__title": "Backache (finding)"
      },
      "startDate": "2007-06-12"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/161891005",
      "@type": [
        "spcode__SNOMED",
        "Code"
      ],
      "dcterms__identifier": "161891005",
      "dcterms__title": "Backache (finding)",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Problem</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
'>


endDate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#endDate</span>
<br />
Date on which problem resolved, if any. <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


notes
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#notes</span>
<br />
Additional notes about the problem <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


problemName
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#problemName</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#SNOMED'>SNOMED</a>
SNOMED-CT Concept for the problem
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


startDate
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#startDate</span>
<br />
Date on which problem began <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

</table>

## <span id='SMART_Statement'>`SMART Statement`</span>


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Statement</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

</table>

## <span id='User_Preferences'>`User Preferences`</span>


## <span id='VitalSigns'>`VitalSigns`</span>

`VitalSigns` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


<div id='VitalSigns_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#VitalSigns_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#VitalSigns_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#VitalSigns_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#VitalSigns_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:foaf="http://xmlns.com/foaf/0.1/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:v="http://www.w3.org/2006/vcard/ns#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"> 

  <sp:VitalSigns>
    <sp:belongsTo  rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
    <dcterms:date>2010-05-12T04:00:00Z</dcterms:date>
    <sp:encounter>
      <sp:Encounter>
        <sp:belongsTo  rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
        <sp:startDate>2010-05-12T04:00:00Z</sp:startDate>
        <sp:endDate>2010-05-12T04:20:00Z</sp:endDate>
        <sp:encounterType>
          <sp:CodedValue>
            <dcterms:title>Ambulatory encounter</dcterms:title>
            <sp:code>
              <spcode:EncounterType rdf:about="http://smartplatforms.org/terms/codes/EncounterType#ambulatory">
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Ambulatory encounter</dcterms:title>
                <sp:system>http://smartplatforms.org/terms/codes/EncounterType#</sp:system>
                <dcterms:identifier>ambulatory</dcterms:identifier> 
              </spcode:EncounterType>       
            </sp:code>
          </sp:CodedValue>
        </sp:encounterType>
      </sp:Encounter>    
    </sp:encounter>
    <sp:height>
      <sp:VitalSign>
        <sp:vitalName>
          <sp:CodedValue>
            <dcterms:title>Body height</dcterms:title>
            <sp:code>
              <spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8302-2">
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Body height</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
                <dcterms:identifier>8302-2</dcterms:identifier> 
              </spcode:VitalSign>    
            </sp:code>
          </sp:CodedValue>
        </sp:vitalName>
        <sp:value>1.80</sp:value>
        <sp:unit>m</sp:unit>
      </sp:VitalSign>
    </sp:height>
    <sp:weight>
      <sp:VitalSign>
        <sp:vitalName>
          <sp:CodedValue>
            <dcterms:title>Body weight</dcterms:title>
            <sp:code>    
              <spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/3141-9">
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Body weight</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
                <dcterms:identifier>3141-9</dcterms:identifier> 
              </spcode:VitalSign>
            </sp:code>
          </sp:CodedValue>
        </sp:vitalName>
        <sp:value>70.8</sp:value>
        <sp:unit>kg</sp:unit>
      </sp:VitalSign>
    </sp:weight>
    <sp:bodyMassIndex>
      <sp:VitalSign>
        <sp:vitalName>
          <sp:CodedValue>
            <dcterms:title>Body mass index</dcterms:title>
            <sp:code>
              <spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/39156-5">
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Body mass index</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
                <dcterms:identifier>39156-5</dcterms:identifier> 
              </spcode:VitalSign>        
            </sp:code>
          </sp:CodedValue>
        </sp:vitalName>
        <sp:value>21.8</sp:value>
        <sp:unit>kg/m2</sp:unit>
      </sp:VitalSign>
    </sp:bodyMassIndex>
    <sp:respiratoryRate>
      <sp:VitalSign>
        <sp:vitalName>
          <sp:CodedValue>
            <dcterms:title>Respiration rate</dcterms:title>
            <sp:code>
              <spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/9279-1">
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Respiration rate</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
                <dcterms:identifier>9279-1</dcterms:identifier> 
              </spcode:VitalSign>    
            </sp:code>
          </sp:CodedValue>
        </sp:vitalName>
        <sp:value>16</sp:value>
        <sp:unit>{breaths}/min</sp:unit>
      </sp:VitalSign>
    </sp:respiratoryRate>
    <sp:heartRate>
      <sp:VitalSign>
        <sp:vitalName>
          <sp:CodedValue>
            <dcterms:title>Heart rate</dcterms:title>
            <sp:code>
              <spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8867-4">
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Heart rate</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
                <dcterms:identifier>8867-4</dcterms:identifier> 
              </spcode:VitalSign>
            </sp:code>
          </sp:CodedValue>
        </sp:vitalName>
        <sp:value>70</sp:value>
        <sp:unit>{beats}/min</sp:unit>
      </sp:VitalSign>
    </sp:heartRate>
    <sp:oxygenSaturation>
      <sp:VitalSign>
        <sp:vitalName>
          <sp:CodedValue>
            <dcterms:title>Oxygen saturation</dcterms:title>
            <sp:code>
              <spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/2710-2">
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Oxygen saturation</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
                <dcterms:identifier>2710-2</dcterms:identifier> 
              </spcode:VitalSign>        
            </sp:code>
          </sp:CodedValue>
        </sp:vitalName>
        <sp:value>99</sp:value>
        <sp:unit>%{HemoglobinSaturation}</sp:unit>
      </sp:VitalSign>
    </sp:oxygenSaturation>
    <sp:temperature>
      <sp:VitalSign>
        <sp:vitalName>
          <sp:CodedValue>
            <dcterms:title>Body temperature</dcterms:title>
            <sp:code>
              <spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8310-5">
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Body temperature</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
                <dcterms:identifier>8310-5</dcterms:identifier> 
              </spcode:VitalSign>        
            </sp:code>
          </sp:CodedValue>
        </sp:vitalName>
        <sp:value>37</sp:value>
        <sp:unit>Cel</sp:unit>
      </sp:VitalSign>
    </sp:temperature>
    <sp:bloodPressure>
      <sp:BloodPressure>
        <sp:systolic>
          <sp:VitalSign>
            <sp:vitalName>
              <sp:CodedValue>
                <dcterms:title>Intravascular systolic</dcterms:title>
                <sp:code>
                  <spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8480-6">
                    <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                    <dcterms:title>Intravascular systolic</dcterms:title>
                    <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
                    <dcterms:identifier>8480-6</dcterms:identifier> 
                  </spcode:VitalSign>        
                </sp:code>
              </sp:CodedValue>
            </sp:vitalName>
            <sp:value>132</sp:value>
            <sp:unit>mm[Hg]</sp:unit>
          </sp:VitalSign>
        </sp:systolic>
        <sp:diastolic>
          <sp:VitalSign>
            <sp:vitalName>
              <sp:CodedValue>
                <dcterms:title>Intravascular diastolic</dcterms:title>
                <sp:code>
                  <spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8462-4">
                    <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                    <dcterms:title>Intravascular diastolic</dcterms:title>
                    <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
                    <dcterms:identifier>8462-4</dcterms:identifier> 
                  </spcode:VitalSign>        
                </sp:code>
              </sp:CodedValue>
            </sp:vitalName>
            <sp:value>82</sp:value>
            <sp:unit>mm[Hg]</sp:unit>
          </sp:VitalSign>
        </sp:diastolic>
        <sp:bodyPosition>
          <sp:CodedValue>
            <dcterms:title>Sitting</dcterms:title>
            <sp:code>
              <spcode:BloodPressureBodyPosition rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/33586001" >
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Sitting</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
                <dcterms:identifier>33586001</dcterms:identifier> 
              </spcode:BloodPressureBodyPosition>        
            </sp:code>
          </sp:CodedValue>
        </sp:bodyPosition>
        <sp:bodySite>
          <sp:CodedValue>
            <dcterms:title>Right arm</dcterms:title>
            <sp:code>
              <spcode:BloodPressureBodySite rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/368209003" >
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Right arm</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
                <dcterms:identifier>368209003</dcterms:identifier> 
              </spcode:BloodPressureBodySite>        
            </sp:code>
          </sp:CodedValue>
        </sp:bodySite>
      </sp:BloodPressure>
    </sp:bloodPressure>
  </sp:VitalSigns>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:DIawMmoL870 <http://smartplatforms.org/terms#unit> "{breaths}/min" .
_:DIawMmoL870 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:DIawMmoL870 <http://smartplatforms.org/terms#value> "16" .
_:DIawMmoL870 <http://smartplatforms.org/terms#vitalName> _:DIawMmoL871 .
_:DIawMmoL866 <http://smartplatforms.org/terms#unit> "kg" .
_:DIawMmoL866 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:DIawMmoL866 <http://smartplatforms.org/terms#value> "70.8" .
_:DIawMmoL866 <http://smartplatforms.org/terms#vitalName> _:DIawMmoL867 .
_:DIawMmoL861 <http://smartplatforms.org/terms#bloodPressure> _:DIawMmoL878 .
_:DIawMmoL861 <http://smartplatforms.org/terms#heartRate> _:DIawMmoL872 .
_:DIawMmoL861 <http://smartplatforms.org/terms#temperature> _:DIawMmoL876 .
_:DIawMmoL861 <http://smartplatforms.org/terms#respiratoryRate> _:DIawMmoL870 .
_:DIawMmoL861 <http://smartplatforms.org/terms#bodyMassIndex> _:DIawMmoL868 .
_:DIawMmoL861 <http://smartplatforms.org/terms#height> _:DIawMmoL864 .
_:DIawMmoL861 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSigns> .
_:DIawMmoL861 <http://smartplatforms.org/terms#encounter> _:DIawMmoL862 .
_:DIawMmoL861 <http://smartplatforms.org/terms#oxygenSaturation> _:DIawMmoL874 .
_:DIawMmoL861 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL861 <http://purl.org/dc/terms/date> "2010-05-12T04:00:00Z" .
_:DIawMmoL861 <http://smartplatforms.org/terms#weight> _:DIawMmoL866 .
_:DIawMmoL872 <http://smartplatforms.org/terms#unit> "{beats}/min" .
_:DIawMmoL872 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:DIawMmoL872 <http://smartplatforms.org/terms#value> "70" .
_:DIawMmoL872 <http://smartplatforms.org/terms#vitalName> _:DIawMmoL873 .
_:DIawMmoL877 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8310-5> .
_:DIawMmoL877 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL877 <http://purl.org/dc/terms/title> "Body temperature" .
_:DIawMmoL867 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/3141-9> .
_:DIawMmoL867 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL867 <http://purl.org/dc/terms/title> "Body weight" .
_:DIawMmoL879 <http://smartplatforms.org/terms#unit> "mm[Hg]" .
_:DIawMmoL879 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:DIawMmoL879 <http://smartplatforms.org/terms#value> "132" .
_:DIawMmoL879 <http://smartplatforms.org/terms#vitalName> _:DIawMmoL880 .
_:DIawMmoL882 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8462-4> .
_:DIawMmoL882 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL882 <http://purl.org/dc/terms/title> "Intravascular diastolic" .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://purl.org/dc/terms/identifier> "3141-9" .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://purl.org/dc/terms/title> "Body weight" .
_:DIawMmoL883 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/33586001> .
_:DIawMmoL883 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL883 <http://purl.org/dc/terms/title> "Sitting" .
_:DIawMmoL884 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/368209003> .
_:DIawMmoL884 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL884 <http://purl.org/dc/terms/title> "Right arm" .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://purl.org/dc/terms/identifier> "8302-2" .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://purl.org/dc/terms/title> "Body height" .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://purl.org/dc/terms/identifier> "2710-2" .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://purl.org/dc/terms/title> "Oxygen saturation" .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://purl.org/dc/terms/identifier> "8462-4" .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://purl.org/dc/terms/title> "Intravascular diastolic" .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://purl.org/dc/terms/identifier> "8480-6" .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://purl.org/dc/terms/title> "Intravascular systolic" .
_:DIawMmoL873 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8867-4> .
_:DIawMmoL873 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL873 <http://purl.org/dc/terms/title> "Heart rate" .
_:DIawMmoL881 <http://smartplatforms.org/terms#unit> "mm[Hg]" .
_:DIawMmoL881 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:DIawMmoL881 <http://smartplatforms.org/terms#value> "82" .
_:DIawMmoL881 <http://smartplatforms.org/terms#vitalName> _:DIawMmoL882 .
_:DIawMmoL880 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8480-6> .
_:DIawMmoL880 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL880 <http://purl.org/dc/terms/title> "Intravascular systolic" .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://purl.org/dc/terms/identifier> "9279-1" .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://purl.org/dc/terms/title> "Respiration rate" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/EncounterType#" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/identifier> "ambulatory" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/EncounterType> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/title> "Ambulatory encounter" .
_:DIawMmoL876 <http://smartplatforms.org/terms#unit> "Cel" .
_:DIawMmoL876 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:DIawMmoL876 <http://smartplatforms.org/terms#value> "37" .
_:DIawMmoL876 <http://smartplatforms.org/terms#vitalName> _:DIawMmoL877 .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://purl.org/dc/terms/identifier> "39156-5" .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://purl.org/dc/terms/title> "Body mass index" .
_:DIawMmoL868 <http://smartplatforms.org/terms#unit> "kg/m2" .
_:DIawMmoL868 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:DIawMmoL868 <http://smartplatforms.org/terms#value> "21.8" .
_:DIawMmoL868 <http://smartplatforms.org/terms#vitalName> _:DIawMmoL869 .
_:DIawMmoL862 <http://smartplatforms.org/terms#encounterType> _:DIawMmoL863 .
_:DIawMmoL862 <http://smartplatforms.org/terms#startDate> "2010-05-12T04:00:00Z" .
_:DIawMmoL862 <http://smartplatforms.org/terms#endDate> "2010-05-12T04:20:00Z" .
_:DIawMmoL862 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Encounter> .
_:DIawMmoL862 <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:DIawMmoL869 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/39156-5> .
_:DIawMmoL869 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL869 <http://purl.org/dc/terms/title> "Body mass index" .
_:DIawMmoL865 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8302-2> .
_:DIawMmoL865 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL865 <http://purl.org/dc/terms/title> "Body height" .
_:DIawMmoL878 <http://smartplatforms.org/terms#systolic> _:DIawMmoL879 .
_:DIawMmoL878 <http://smartplatforms.org/terms#bodySite> _:DIawMmoL884 .
_:DIawMmoL878 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#BloodPressure> .
_:DIawMmoL878 <http://smartplatforms.org/terms#bodyPosition> _:DIawMmoL883 .
_:DIawMmoL878 <http://smartplatforms.org/terms#diastolic> _:DIawMmoL881 .
_:DIawMmoL863 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/EncounterType#ambulatory> .
_:DIawMmoL863 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL863 <http://purl.org/dc/terms/title> "Ambulatory encounter" .
_:DIawMmoL871 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/9279-1> .
_:DIawMmoL871 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL871 <http://purl.org/dc/terms/title> "Respiration rate" .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://purl.org/dc/terms/identifier> "8310-5" .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://purl.org/dc/terms/title> "Body temperature" .
_:DIawMmoL874 <http://smartplatforms.org/terms#unit> "%{HemoglobinSaturation}" .
_:DIawMmoL874 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:DIawMmoL874 <http://smartplatforms.org/terms#value> "99" .
_:DIawMmoL874 <http://smartplatforms.org/terms#vitalName> _:DIawMmoL875 .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://purl.org/dc/terms/identifier> "368209003" .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/BloodPressureBodySite> .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://purl.org/dc/terms/title> "Right arm" .
_:DIawMmoL875 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/2710-2> .
_:DIawMmoL875 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:DIawMmoL875 <http://purl.org/dc/terms/title> "Oxygen saturation" .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://purl.org/dc/terms/identifier> "33586001" .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/BloodPressureBodyPosition> .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://purl.org/dc/terms/title> "Sitting" .
_:DIawMmoL864 <http://smartplatforms.org/terms#unit> "m" .
_:DIawMmoL864 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:DIawMmoL864 <http://smartplatforms.org/terms#value> "1.80" .
_:DIawMmoL864 <http://smartplatforms.org/terms#vitalName> _:DIawMmoL865 .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://purl.org/dc/terms/identifier> "8867-4" .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://purl.org/dc/terms/title> "Heart rate" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://purl.bioontology.org/ontology/LNC/2710-2> a sp:Code,
        spcode:VitalSign;
    dcterms:identifier "2710-2";
    dcterms:title "Oxygen saturation";
    sp:system "http://purl.bioontology.org/ontology/LNC/" .

<http://purl.bioontology.org/ontology/LNC/3141-9> a sp:Code,
        spcode:VitalSign;
    dcterms:identifier "3141-9";
    dcterms:title "Body weight";
    sp:system "http://purl.bioontology.org/ontology/LNC/" .

<http://purl.bioontology.org/ontology/LNC/39156-5> a sp:Code,
        spcode:VitalSign;
    dcterms:identifier "39156-5";
    dcterms:title "Body mass index";
    sp:system "http://purl.bioontology.org/ontology/LNC/" .

<http://purl.bioontology.org/ontology/LNC/8302-2> a sp:Code,
        spcode:VitalSign;
    dcterms:identifier "8302-2";
    dcterms:title "Body height";
    sp:system "http://purl.bioontology.org/ontology/LNC/" .

<http://purl.bioontology.org/ontology/LNC/8310-5> a sp:Code,
        spcode:VitalSign;
    dcterms:identifier "8310-5";
    dcterms:title "Body temperature";
    sp:system "http://purl.bioontology.org/ontology/LNC/" .

<http://purl.bioontology.org/ontology/LNC/8462-4> a sp:Code,
        spcode:VitalSign;
    dcterms:identifier "8462-4";
    dcterms:title "Intravascular diastolic";
    sp:system "http://purl.bioontology.org/ontology/LNC/" .

<http://purl.bioontology.org/ontology/LNC/8480-6> a sp:Code,
        spcode:VitalSign;
    dcterms:identifier "8480-6";
    dcterms:title "Intravascular systolic";
    sp:system "http://purl.bioontology.org/ontology/LNC/" .

<http://purl.bioontology.org/ontology/LNC/8867-4> a sp:Code,
        spcode:VitalSign;
    dcterms:identifier "8867-4";
    dcterms:title "Heart rate";
    sp:system "http://purl.bioontology.org/ontology/LNC/" .

<http://purl.bioontology.org/ontology/LNC/9279-1> a sp:Code,
        spcode:VitalSign;
    dcterms:identifier "9279-1";
    dcterms:title "Respiration rate";
    sp:system "http://purl.bioontology.org/ontology/LNC/" .

<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> a sp:Code,
        spcode:BloodPressureBodyPosition;
    dcterms:identifier "33586001";
    dcterms:title "Sitting";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .

<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> a sp:Code,
        spcode:BloodPressureBodySite;
    dcterms:identifier "368209003";
    dcterms:title "Right arm";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .

<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> a sp:Code,
        spcode:EncounterType;
    dcterms:identifier "ambulatory";
    dcterms:title "Ambulatory encounter";
    sp:system "http://smartplatforms.org/terms/codes/EncounterType#" .

[] a sp:VitalSigns;
    dcterms:date "2010-05-12T04:00:00Z";
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:bloodPressure [ a sp:BloodPressure;
            sp:bodyPosition [ a sp:CodedValue;
                    dcterms:title "Sitting";
                    sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/33586001> ];
            sp:bodySite [ a sp:CodedValue;
                    dcterms:title "Right arm";
                    sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/368209003> ];
            sp:diastolic [ a sp:VitalSign;
                    sp:unit "mm[Hg]";
                    sp:value "82";
                    sp:vitalName [ a sp:CodedValue;
                            dcterms:title "Intravascular diastolic";
                            sp:code <http://purl.bioontology.org/ontology/LNC/8462-4> ] ];
            sp:systolic [ a sp:VitalSign;
                    sp:unit "mm[Hg]";
                    sp:value "132";
                    sp:vitalName [ a sp:CodedValue;
                            dcterms:title "Intravascular systolic";
                            sp:code <http://purl.bioontology.org/ontology/LNC/8480-6> ] ] ];
    sp:bodyMassIndex [ a sp:VitalSign;
            sp:unit "kg/m2";
            sp:value "21.8";
            sp:vitalName [ a sp:CodedValue;
                    dcterms:title "Body mass index";
                    sp:code <http://purl.bioontology.org/ontology/LNC/39156-5> ] ];
    sp:encounter [ a sp:Encounter;
            sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
            sp:encounterType [ a sp:CodedValue;
                    dcterms:title "Ambulatory encounter";
                    sp:code <http://smartplatforms.org/terms/codes/EncounterType#ambulatory> ];
            sp:endDate "2010-05-12T04:20:00Z";
            sp:startDate "2010-05-12T04:00:00Z" ];
    sp:heartRate [ a sp:VitalSign;
            sp:unit "{beats}/min";
            sp:value "70";
            sp:vitalName [ a sp:CodedValue;
                    dcterms:title "Heart rate";
                    sp:code <http://purl.bioontology.org/ontology/LNC/8867-4> ] ];
    sp:height [ a sp:VitalSign;
            sp:unit "m";
            sp:value "1.80";
            sp:vitalName [ a sp:CodedValue;
                    dcterms:title "Body height";
                    sp:code <http://purl.bioontology.org/ontology/LNC/8302-2> ] ];
    sp:oxygenSaturation [ a sp:VitalSign;
            sp:unit "%{HemoglobinSaturation}";
            sp:value "99";
            sp:vitalName [ a sp:CodedValue;
                    dcterms:title "Oxygen saturation";
                    sp:code <http://purl.bioontology.org/ontology/LNC/2710-2> ] ];
    sp:respiratoryRate [ a sp:VitalSign;
            sp:unit "{breaths}/min";
            sp:value "16";
            sp:vitalName [ a sp:CodedValue;
                    dcterms:title "Respiration rate";
                    sp:code <http://purl.bioontology.org/ontology/LNC/9279-1> ] ];
    sp:temperature [ a sp:VitalSign;
            sp:unit "Cel";
            sp:value "37";
            sp:vitalName [ a sp:CodedValue;
                    dcterms:title "Body temperature";
                    sp:code <http://purl.bioontology.org/ontology/LNC/8310-5> ] ];
    sp:weight [ a sp:VitalSign;
            sp:unit "kg";
            sp:value "70.8";
            sp:vitalName [ a sp:CodedValue;
                    dcterms:title "Body weight";
                    sp:code <http://purl.bioontology.org/ontology/LNC/3141-9> ] ] .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://chb.github.com/smart-docs-testing/reference/datamodel/contexts/smart_context.jsonld",
  "@id": [
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/3141-9",
      "@type": [
        "spcode__VitalSign",
        "Code"
      ],
      "dcterms__identifier": "3141-9",
      "dcterms__title": "Body weight",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/39156-5",
      "@type": [
        "spcode__VitalSign",
        "Code"
      ],
      "dcterms__identifier": "39156-5",
      "dcterms__title": "Body mass index",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/8302-2",
      "@type": [
        "spcode__VitalSign",
        "Code"
      ],
      "dcterms__identifier": "8302-2",
      "dcterms__title": "Body height",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/8480-6",
      "@type": [
        "spcode__VitalSign",
        "Code"
      ],
      "dcterms__identifier": "8480-6",
      "dcterms__title": "Intravascular systolic",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/9279-1",
      "@type": [
        "spcode__VitalSign",
        "Code"
      ],
      "dcterms__identifier": "9279-1",
      "dcterms__title": "Respiration rate",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/2710-2",
      "@type": [
        "spcode__VitalSign",
        "Code"
      ],
      "dcterms__identifier": "2710-2",
      "dcterms__title": "Oxygen saturation",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@type": "VitalSigns",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "bloodPressure": {
        "@type": "BloodPressure",
        "bodyPosition": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/33586001"
          },
          "dcterms__title": "Sitting"
        },
        "bodySite": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/368209003"
          },
          "dcterms__title": "Right arm"
        },
        "diastolic": {
          "@type": "VitalSign",
          "unit": "mm[Hg]",
          "value": "82",
          "vitalName": {
            "@type": "CodedValue",
            "code": {
              "@id": "http://purl.bioontology.org/ontology/LNC/8462-4"
            },
            "dcterms__title": "Intravascular diastolic"
          }
        },
        "systolic": {
          "@type": "VitalSign",
          "unit": "mm[Hg]",
          "value": "132",
          "vitalName": {
            "@type": "CodedValue",
            "code": {
              "@id": "http://purl.bioontology.org/ontology/LNC/8480-6"
            },
            "dcterms__title": "Intravascular systolic"
          }
        }
      },
      "bodyMassIndex": {
        "@type": "VitalSign",
        "unit": "kg/m2",
        "value": "21.8",
        "vitalName": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/LNC/39156-5"
          },
          "dcterms__title": "Body mass index"
        }
      },
      "dcterms__date": "2010-05-12T04:00:00Z",
      "encounter": {
        "@type": "Encounter",
        "belongsTo": {
          "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
        },
        "encounterType": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://smartplatforms.org/terms/codes/EncounterType#ambulatory"
          },
          "dcterms__title": "Ambulatory encounter"
        },
        "endDate": "2010-05-12T04:20:00Z",
        "startDate": "2010-05-12T04:00:00Z"
      },
      "heartRate": {
        "@type": "VitalSign",
        "unit": "{beats}/min",
        "value": "70",
        "vitalName": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/LNC/8867-4"
          },
          "dcterms__title": "Heart rate"
        }
      },
      "height": {
        "@type": "VitalSign",
        "unit": "m",
        "value": "1.80",
        "vitalName": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/LNC/8302-2"
          },
          "dcterms__title": "Body height"
        }
      },
      "oxygenSaturation": {
        "@type": "VitalSign",
        "unit": "%{HemoglobinSaturation}",
        "value": "99",
        "vitalName": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/LNC/2710-2"
          },
          "dcterms__title": "Oxygen saturation"
        }
      },
      "respiratoryRate": {
        "@type": "VitalSign",
        "unit": "{breaths}/min",
        "value": "16",
        "vitalName": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/LNC/9279-1"
          },
          "dcterms__title": "Respiration rate"
        }
      },
      "temperature": {
        "@type": "VitalSign",
        "unit": "Cel",
        "value": "37",
        "vitalName": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/LNC/8310-5"
          },
          "dcterms__title": "Body temperature"
        }
      },
      "weight": {
        "@type": "VitalSign",
        "unit": "kg",
        "value": "70.8",
        "vitalName": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/LNC/3141-9"
          },
          "dcterms__title": "Body weight"
        }
      }
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/8310-5",
      "@type": [
        "spcode__VitalSign",
        "Code"
      ],
      "dcterms__identifier": "8310-5",
      "dcterms__title": "Body temperature",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/33586001",
      "@type": [
        "spcode__BloodPressureBodyPosition",
        "Code"
      ],
      "dcterms__identifier": "33586001",
      "dcterms__title": "Sitting",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/368209003",
      "@type": [
        "Code",
        "spcode__BloodPressureBodySite"
      ],
      "dcterms__identifier": "368209003",
      "dcterms__title": "Right arm",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/8867-4",
      "@type": [
        "spcode__VitalSign",
        "Code"
      ],
      "dcterms__identifier": "8867-4",
      "dcterms__title": "Heart rate",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://smartplatforms.org/terms/codes/EncounterType#ambulatory",
      "@type": [
        "spcode__EncounterType",
        "Code"
      ],
      "dcterms__identifier": "ambulatory",
      "dcterms__title": "Ambulatory encounter",
      "system": "http://smartplatforms.org/terms/codes/EncounterType#"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/8462-4",
      "@type": [
        "spcode__VitalSign",
        "Code"
      ],
      "dcterms__identifier": "8462-4",
      "dcterms__title": "Intravascular diastolic",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#VitalSigns</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


date
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/date</span>
<br />
Date + time when vital signs were recorded <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


belongsTo
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#belongsTo</span>
<br />
<a href='#Medical_Record'>Medical Record</a>
The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
'>


bloodPressure
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#bloodPressure</span>
<br />
<a href='#BloodPressure'>BloodPressure</a>
Patient's systolic + diastolic Blood Pressure in mmHg, with optinal position coding
</td>
</tr>

<tr><td style='width: 30%;
'>


bodyMassIndex
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#bodyMassIndex</span>
<br />
<a href='#VitalSign'>VitalSign</a>where unit has value: kg/m2
Patient's Body Mass Index.  
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


encounter
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#encounter</span>
<br />
<a href='#Encounter'>Encounter</a>
Encounter at which vital signs were measured. This should specify a date and encounter type, at minimum.
</td>
</tr>

<tr><td style='width: 30%;
'>


heartRate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#heartRate</span>
<br />
<a href='#VitalSign'>VitalSign</a>where unit has value: {beats}/min
Patient's Heart Rate per minute. 
</td>
</tr>

<tr><td style='width: 30%;
'>


height
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#height</span>
<br />
<a href='#VitalSign'>VitalSign</a>where unit has value: m
Patient's height in meters.  
</td>
</tr>

<tr><td style='width: 30%;
'>


oxygenSaturation
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#oxygenSaturation</span>
<br />
<a href='#VitalSign'>VitalSign</a>where unit has value: %{HemoglobinSaturation}
Patient's oxygen saturation in percent.  
</td>
</tr>

<tr><td style='width: 30%;
'>


respiratoryRate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#respiratoryRate</span>
<br />
<a href='#VitalSign'>VitalSign</a>where unit has value: {breaths}/min
Patient's Respiratory Rate per minute. 
</td>
</tr>

<tr><td style='width: 30%;
'>


temperature
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#temperature</span>
<br />
<a href='#VitalSign'>VitalSign</a>where unit has value: Cel
Patient's Temperature in Celcius. 
</td>
</tr>

<tr><td style='width: 30%;
'>


weight
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#weight</span>
<br />
<a href='#VitalSign'>VitalSign</a>where unit has value: kg
Patient's weight in kg. 
</td>
</tr>

</table>

# Component Types


## <span id='Address'>`Address`</span>

`Address` is a subtype of and inherits properties from:
[Component](#Component)


A v:Address element can be given additional types to indicate:

 * Preferred Status (v:Pref)
 * Home address (v:Home)
 * Work address (v:Work)


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://www.w3.org/2006/vcard/ns#Address</caption>
<tbody>
<tr><td style='width: 30%;
'>


country-name
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#country-name</span>
<br />
Country name <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


extended-address
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#extended-address</span>
<br />
City Name <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


locality
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#locality</span>
<br />
City Name <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


postal-code
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#postal-code</span>
<br />
Postal code <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


region
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#region</span>
<br />
e.g. state abbreviation <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


street-address
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#street-address</span>
<br />
Street address <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='Attribution'>`Attribution`</span>

`Attribution` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Attribution</caption>
<tbody>
<tr><td style='width: 30%;
'>


endDate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#endDate</span>
<br />
End Time of attributed event (if instantaneous, this is not provided) <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


participant
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#participant</span>
<br />
<a href='#Participant'>Participant</a>
Participant in Attribution
</td>
</tr>

<tr><td style='width: 30%;
'>


startDate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#startDate</span>
<br />
Start Time of attributed event (if instantaneous, this is the only time) <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

</table>

## <span id='BloodPressure'>`BloodPressure`</span>

`BloodPressure` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#BloodPressure</caption>
<tbody>
<tr><td style='width: 30%;
'>


bodyPosition
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#bodyPosition</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#BloodPressureBodyPosition'>BloodPressureBodyPosition</a>
Position of patient when blood pressure was recorded
</td>
</tr>

<tr><td style='width: 30%;
'>


bodySite
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#bodySite</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#BloodPressureBodySite'>BloodPressureBodySite</a>
Site on patient's body where blood pressure was recorded
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


diastolic
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#diastolic</span>
<br />
<a href='#VitalSign'>VitalSign</a>where unit has value: mm[Hg]
diastolic blood pressure in mmHG. 
</td>
</tr>

<tr><td style='width: 30%;
'>


method
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#method</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#BloodPressureMethod'>BloodPressureMethod</a>
Method by which blood pressure was recorded.
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


systolic
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#systolic</span>
<br />
<a href='#VitalSign'>VitalSign</a>where unit has value: mm[Hg]
systolic blood pressure in mmHG.
</td>
</tr>

</table>

## <span id='Code'>`Code`</span>

`Code` is a subtype of and inherits properties from:
[Component](#Component), [DataType](#DataType)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Code</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='CodeProvenance'>`CodeProvenance`</span>

`CodeProvenance` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#CodeProvenance</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


sourceCode
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#sourceCode</span>
<br />
 <a href='http://www.w3.org/2001/XMLSchema#anyURI'>xsd:anyURI</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


translationFidelity
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#translationFidelity</span>
<br />
<a href='#TranslationFidelity_code'>TranslationFidelity code</a>
</td>
</tr>

</table>

## <span id='Coded_Value'>`Coded Value`</span>

`Coded Value` is a subtype of and inherits properties from:
[Component](#Component), [DataType](#DataType)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#CodedValue</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


code
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#code</span>
<br />
<a href='#Code'>Code</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


provenance
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#provenance</span>
<br />
<a href='#CodeProvenance'>CodeProvenance</a>
</td>
</tr>

</table>

## <span id='DataType'>`DataType`</span>

`DataType` is a subtype of and inherits properties from:
[Component](#Component)



## <span id='Name'>`Name`</span>

`Name` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://www.w3.org/2006/vcard/ns#Name</caption>
<tbody>
<tr><td style='width: 30%;
'>


additional-name
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#additional-name</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


family-name
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#family-name</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


given-name
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#given-name</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


honorific-prefix
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#honorific-prefix</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


honorific-suffix
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#honorific-suffix</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='NarrativeResult'>`NarrativeResult`</span>

`NarrativeResult` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#NarrativeResult</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


value
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#value</span>
<br />
Value of result (free text) <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='NominalResult'>`NominalResult`</span>

`NominalResult` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#NominalResult</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


value
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#value</span>
<br />
value of result (free text). <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='OrdinalResult'>`OrdinalResult`</span>

`OrdinalResult` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#OrdinalResult</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


value
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#value</span>
<br />
value of result (free text). <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='Organization'>`Organization`</span>

`Organization` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Organization</caption>
<tbody>
<tr><td style='width: 30%;
'>


adr
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#adr</span>
<br />
<a href='#Address'>Address</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


organization-name
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#organization-name</span>
<br />
Name of the organization <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='Participant'>`Participant`</span>

`Participant` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Participant</caption>
<tbody>
<tr><td style='width: 30%;
'>


organization
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#organization</span>
<br />
<a href='#Organization'>Organization</a>
Organization of participant
</td>
</tr>

<tr><td style='width: 30%;
'>


person
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#person</span>
<br />
<a href='#Person'>Person</a>
Person who participated
</td>
</tr>

<tr><td style='width: 30%;
'>


role
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#role</span>
<br />
Role of participant (free text) <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='Person'>`Person`</span>

`Person` is a subtype of and inherits properties from:
[Component](#Component), [VCard](#VCard)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Person</caption>
<tbody>
<tr><td style='width: 30%;
'>


ethnicity
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#ethnicity</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


preferredLanguage
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#preferredLanguage</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


race
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#race</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


adr
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#adr</span>
<br />
<a href='#Address'>Address</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


bday
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#bday</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


email
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#email</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


n
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#n</span>
<br />
<a href='#Name'>Name</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


tel
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#tel</span>
<br />
<a href='#Tel'>Tel</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


gender
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://xmlns.com/foaf/0.1/gender</span>
<br />
A person's (administrative) gender.  This should consist of the string "male" or "female". <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='Pharmacy'>`Pharmacy`</span>

`Pharmacy` is a subtype of and inherits properties from:
[Component](#Component), [Organization](#Organization)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Pharmacy</caption>
<tbody>
<tr><td style='width: 30%;
'>


ncpdpId
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#ncpdpId</span>
<br />
Pharmacy's National Council for Prescription Drug Programs ID Number (NCPDP ID) <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


adr
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#adr</span>
<br />
<a href='#Address'>Address</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


organization-name
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#organization-name</span>
<br />
Name of the organization <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='Provider'>`Provider`</span>

`Provider` is a subtype of and inherits properties from:
[Component](#Component), [Person](#Person), [VCard](#VCard)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Provider</caption>
<tbody>
<tr><td style='width: 30%;
'>


deaNumber
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#deaNumber</span>
<br />
Provider's Drug Enforcement Agency Number <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


ethnicity
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#ethnicity</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


npiNumber
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#npiNumber</span>
<br />
Provider's National Provider Identification Number <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


preferredLanguage
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#preferredLanguage</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


race
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#race</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


adr
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#adr</span>
<br />
<a href='#Address'>Address</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


bday
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#bday</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


email
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#email</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


n
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#n</span>
<br />
<a href='#Name'>Name</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


tel
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#tel</span>
<br />
<a href='#Tel'>Tel</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


gender
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://xmlns.com/foaf/0.1/gender</span>
<br />
A person's (administrative) gender.  This should consist of the string "male" or "female". <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='QuantitativeResult'>`QuantitativeResult`</span>

`QuantitativeResult` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#QuantitativeResult</caption>
<tbody>
<tr><td style='width: 30%;
'>


nonCriticalRange
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#nonCriticalRange</span>
<br />
<a href='#ValueRange'>ValueRange</a>
Non-critical range for result.  (Results outside this range are considered "critical.")
</td>
</tr>

<tr><td style='width: 30%;
'>


normalRange
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#normalRange</span>
<br />
<a href='#ValueRange'>ValueRange</a>
Normal range for result. (Results outside this range are considered "abnormal".)
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


valueAndUnit
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#valueAndUnit</span>
<br />
<a href='#ValueAndUnit'>ValueAndUnit</a>
Value and unit
</td>
</tr>

</table>

## <span id='Tel'>`Tel`</span>

`Tel` is a subtype of and inherits properties from:
[Component](#Component)


A v:Tel element can be given additional types to indicate:

 * Preferred Status (v:Pref)
 * Cell phone (v:Cell)
 * Home phone (v:Home)
 * Work phone (v:Work)


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://www.w3.org/2006/vcard/ns#Tel</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


value
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/1999/02/22-rdf-syntax-ns#value</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='VCard'>`VCard`</span>

`VCard` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://www.w3.org/2006/vcard/ns#VCard</caption>
<tbody>
<tr><td style='width: 30%;
'>


adr
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#adr</span>
<br />
<a href='#Address'>Address</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


bday
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#bday</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


email
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#email</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


n
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#n</span>
<br />
<a href='#Name'>Name</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


tel
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#tel</span>
<br />
<a href='#Tel'>Tel</a>
</td>
</tr>

</table>

## <span id='ValueAndUnit'>`ValueAndUnit`</span>

`ValueAndUnit` is a subtype of and inherits properties from:
[Component](#Component), [DataType](#DataType)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#ValueAndUnit</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


unit
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#unit</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


value
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#value</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='ValueRange'>`ValueRange`</span>

`ValueRange` is a subtype of and inherits properties from:
[Component](#Component), [DataType](#DataType)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#ValueRange</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


maximum
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#maximum</span>
<br />
<a href='#ValueAndUnit'>ValueAndUnit</a>
Maximum value in range (not inclusive)
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


minimum
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#minimum</span>
<br />
<a href='#ValueAndUnit'>ValueAndUnit</a>
Minimum value in range (inclusive)
</td>
</tr>

</table>

## <span id='ValueRatio'>`ValueRatio`</span>

`ValueRatio` is a subtype of and inherits properties from:
[Component](#Component), [DataType](#DataType)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#ValueRatio</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


denominator
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#denominator</span>
<br />
<a href='#ValueAndUnit'>ValueAndUnit</a>
Denominator of the ratio.
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


numerator
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#numerator</span>
<br />
<a href='#ValueAndUnit'>ValueAndUnit</a>
Numerator of the ratio.
</td>
</tr>

</table>

## <span id='VitalSign'>`VitalSign`</span>

`VitalSign` is a subtype of and inherits properties from:
[Component](#Component), [DataType](#DataType), [ValueAndUnit](#ValueAndUnit)


Vital Sign:  includes a LOINC code specifying which measurement is being reported, alongside a value and unit.


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#VitalSign</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


unit
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#unit</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


value
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#value</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


vitalName
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#vitalName</span>
<br />
<a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#VitalSign'>VitalSign</a>
LOINC Coded Value for the vital sign type
</td>
</tr>

</table>

# Container-level Types


## <span id='App_Manifest'>`App Manifest`</span>


## <span id='ContainerManifest'>`ContainerManifest`</span>

A SMART Container exposes a manifest describing its properties and capabilities as a JSON structure.  The example below is for a container that provides Demographics, Encounters, and Vital Signs only.

<div id='ContainerManifest_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#ContainerManifest_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#ContainerManifest_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#ContainerManifest_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#ContainerManifest_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}

{
    smart_version: "0.5.0",
    api_base: "http://sandbox-api.smartplatforms.org",
    name: "SMART v0.5 Sandbox",
    description: "Public sandbox to demonstrate the SMART API",
    admin: "info@smartplatforms.org",

    launch_urls: {
        "authorize_token": "http://localhost:7001/oauth/authorize", 
        "exchange_token": "http://localhost:7000/oauth/access_token", 
        "request_token": "http://localhost:7000/oauth/request_token"
    }, 

    capabilities: {
        "http://smartplatforms.org/terms#Demographics": {
            "methods": [
                "GET"
            ]
        }, 
        "http://smartplatforms.org/terms#Encounter": {
            "methods": [
                "GET"
            ]
        }, 
        "http://smartplatforms.org/terms#VitalSigns": {
            "methods": [
                "GET"
            ]
        }
    }
}

{% endhighlight %}</div>


## <span id='Ontology'>`Ontology`</span>

An OWL ontology representing SMART data types + API calls

<div id='Ontology_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Ontology_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Ontology_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Ontology_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Ontology_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        
<div class='rdf_xml active'>{% highlight xml %}
See: http://sandbox-api.smartplatforms.org/ontology
{% endhighlight %}</div>


## <span id='User'>`User`</span>

`User` is a subtype of and inherits properties from:
[Component](#Component), [Person](#Person), [VCard](#VCard)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#User</caption>
<tbody>
<tr><td style='width: 30%;
'>


department
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#department</span>
<br />
A user's department <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


ethnicity
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#ethnicity</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


preferredLanguage
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#preferredLanguage</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


race
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#race</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


role
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#role</span>
<br />
A user's role <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


adr
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#adr</span>
<br />
<a href='#Address'>Address</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


bday
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#bday</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


email
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#email</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


n
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#n</span>
<br />
<a href='#Name'>Name</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


tel
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#tel</span>
<br />
<a href='#Tel'>Tel</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


gender
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://xmlns.com/foaf/0.1/gender</span>
<br />
A person's (administrative) gender.  This should consist of the string "male" or "female". <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

# Data code Types


## <span id='AlertLevel_code'>`AlertLevel code`</span>

`AlertLevel` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


Constrained to one of: 
 {% highlight xml %}


<spcode:AlertLevel rdf:about="http://smartplatforms.org/terms/codes/AlertLevel#warning">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Warning</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/AlertLevel#</sp:system>
  <dcterms:identifier>warning</dcterms:identifier>
</spcode:AlertLevel>



<spcode:AlertLevel rdf:about="http://smartplatforms.org/terms/codes/AlertLevel#severe">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Severe</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/AlertLevel#</sp:system>
  <dcterms:identifier>severe</dcterms:identifier>
</spcode:AlertLevel>



<spcode:AlertLevel rdf:about="http://smartplatforms.org/terms/codes/AlertLevel#info">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Info</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/AlertLevel#</sp:system>
  <dcterms:identifier>info</dcterms:identifier>
</spcode:AlertLevel>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/AlertLevel</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='AllergyCategory_code'>`AllergyCategory code`</span>

`AllergyCategory` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [SNOMED](#SNOMED)


Constrained to one of: 
 {% highlight xml %}


<spcode:AllergyCategory rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/414285001">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Food allergy</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>414285001</dcterms:identifier>
</spcode:AllergyCategory>



<spcode:AllergyCategory rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/426232007">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Environmental allergy</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>426232007</dcterms:identifier>
</spcode:AllergyCategory>



<spcode:AllergyCategory rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/416098002">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Drug allergy</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>416098002</dcterms:identifier>
</spcode:AllergyCategory>



<spcode:AllergyCategory rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/59037007">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Drug intolerance</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>59037007</dcterms:identifier>
</spcode:AllergyCategory>



<spcode:AllergyCategory rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/235719002">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Food intolerance</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>235719002</dcterms:identifier>
</spcode:AllergyCategory>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/AllergyCategory</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='AllergyExclusion_code'>`AllergyExclusion code`</span>

`AllergyExclusion` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [SNOMED](#SNOMED)


Constrained to one of: 
 {% highlight xml %}


<spcode:AllergyExclusion rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/160244002">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>No known allergies</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>160244002</dcterms:identifier>
</spcode:AllergyExclusion>



<spcode:AllergyExclusion rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/428607008">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>No known environmental allergy</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>428607008</dcterms:identifier>
</spcode:AllergyExclusion>



<spcode:AllergyExclusion rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/429625007">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>No known food allergy</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>429625007</dcterms:identifier>
</spcode:AllergyExclusion>



<spcode:AllergyExclusion rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/409137002">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>No known history of drug allergy</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>409137002</dcterms:identifier>
</spcode:AllergyExclusion>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/AllergyExclusion</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='AllergySeverity_code'>`AllergySeverity code`</span>

`AllergySeverity` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [SNOMED](#SNOMED)


Constrained to one of: 
 {% highlight xml %}


<spcode:AllergySeverity rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/255604002">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Mild</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>255604002</dcterms:identifier>
</spcode:AllergySeverity>



<spcode:AllergySeverity rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/442452003">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Life threatening</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>442452003</dcterms:identifier>
</spcode:AllergySeverity>



<spcode:AllergySeverity rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/6736007">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Moderate</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>6736007</dcterms:identifier>
</spcode:AllergySeverity>



<spcode:AllergySeverity rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/399166001">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Fatal</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>399166001</dcterms:identifier>
</spcode:AllergySeverity>



<spcode:AllergySeverity rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/24484000">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Severe</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>24484000</dcterms:identifier>
</spcode:AllergySeverity>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/AllergySeverity</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='BloodPressureBodyPosition_code'>`BloodPressureBodyPosition code`</span>

`BloodPressureBodyPosition` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [SNOMED](#SNOMED)


Constrained to one of: 
 {% highlight xml %}


<spcode:BloodPressureBodyPosition rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/40199007">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Supine</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>40199007</dcterms:identifier>
</spcode:BloodPressureBodyPosition>



<spcode:BloodPressureBodyPosition rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/33586001">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Sitting</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>33586001</dcterms:identifier>
</spcode:BloodPressureBodyPosition>



<spcode:BloodPressureBodyPosition rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/10904000">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Standing</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>10904000</dcterms:identifier>
</spcode:BloodPressureBodyPosition>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/BloodPressureBodyPosition</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='BloodPressureBodySite_code'>`BloodPressureBodySite code`</span>

`BloodPressureBodySite` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [SNOMED](#SNOMED)


Constrained to one of: 
 {% highlight xml %}


<spcode:BloodPressureBodySite rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/61396006">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Left thigh</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>61396006</dcterms:identifier>
</spcode:BloodPressureBodySite>



<spcode:BloodPressureBodySite rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/368209003">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Right arm</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>368209003</dcterms:identifier>
</spcode:BloodPressureBodySite>



<spcode:BloodPressureBodySite rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/11207009">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Right thigh</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>11207009</dcterms:identifier>
</spcode:BloodPressureBodySite>



<spcode:BloodPressureBodySite rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/368208006">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Left arm</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>368208006</dcterms:identifier>
</spcode:BloodPressureBodySite>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/BloodPressureBodySite</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='BloodPressureMethod_code'>`BloodPressureMethod code`</span>

`BloodPressureMethod` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


Constrained to one of: 
 {% highlight xml %}


<spcode:BloodPressureMethod rdf:about="http://smartplatforms.org/terms/codes/BloodPressureMethod#invasive">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Invasive</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/BloodPressureMethod#</sp:system>
  <dcterms:identifier>invasive</dcterms:identifier>
</spcode:BloodPressureMethod>



<spcode:BloodPressureMethod rdf:about="http://smartplatforms.org/terms/codes/BloodPressureMethod#palpation">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Palpation</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/BloodPressureMethod#</sp:system>
  <dcterms:identifier>palpation</dcterms:identifier>
</spcode:BloodPressureMethod>



<spcode:BloodPressureMethod rdf:about="http://smartplatforms.org/terms/codes/BloodPressureMethod#machine">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Machine</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/BloodPressureMethod#</sp:system>
  <dcterms:identifier>machine</dcterms:identifier>
</spcode:BloodPressureMethod>



<spcode:BloodPressureMethod rdf:about="http://smartplatforms.org/terms/codes/BloodPressureMethod#auscultation">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Auscultation</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/BloodPressureMethod#</sp:system>
  <dcterms:identifier>auscultation</dcterms:identifier>
</spcode:BloodPressureMethod>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/BloodPressureMethod</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='EncounterType_code'>`EncounterType code`</span>

`EncounterType` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


Constrained to one of: 
 {% highlight xml %}


<spcode:EncounterType rdf:about="http://smartplatforms.org/terms/codes/EncounterType#home">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Home encounter</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/EncounterType#</sp:system>
  <dcterms:identifier>home</dcterms:identifier>
</spcode:EncounterType>



<spcode:EncounterType rdf:about="http://smartplatforms.org/terms/codes/EncounterType#emergency">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Emergency encounter</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/EncounterType#</sp:system>
  <dcterms:identifier>emergency</dcterms:identifier>
</spcode:EncounterType>



<spcode:EncounterType rdf:about="http://smartplatforms.org/terms/codes/EncounterType#ambulatory">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Ambulatory encounter</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/EncounterType#</sp:system>
  <dcterms:identifier>ambulatory</dcterms:identifier>
</spcode:EncounterType>



<spcode:EncounterType rdf:about="http://smartplatforms.org/terms/codes/EncounterType#inpatient">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Inpatient encounter</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/EncounterType#</sp:system>
  <dcterms:identifier>inpatient</dcterms:identifier>
</spcode:EncounterType>



<spcode:EncounterType rdf:about="http://smartplatforms.org/terms/codes/EncounterType#field">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Field encounter</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/EncounterType#</sp:system>
  <dcterms:identifier>field</dcterms:identifier>
</spcode:EncounterType>



<spcode:EncounterType rdf:about="http://smartplatforms.org/terms/codes/EncounterType#virtual">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Virtual encounter</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/EncounterType#</sp:system>
  <dcterms:identifier>virtual</dcterms:identifier>
</spcode:EncounterType>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/EncounterType</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='ImmunizationAdministrationStatus_code'>`ImmunizationAdministrationStatus code`</span>

`ImmunizationAdministrationStatus` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


Constrained to one of: 
 {% highlight xml %}


<spcode:ImmunizationAdministrationStatus rdf:about="http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#doseGiven">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Dose Given</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#</sp:system>
  <dcterms:identifier>doseGiven</dcterms:identifier>
</spcode:ImmunizationAdministrationStatus>



<spcode:ImmunizationAdministrationStatus rdf:about="http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Not Administered</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#</sp:system>
  <dcterms:identifier>notAdministered</dcterms:identifier>
</spcode:ImmunizationAdministrationStatus>



<spcode:ImmunizationAdministrationStatus rdf:about="http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#partialDose">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Dose Partially Administered</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#</sp:system>
  <dcterms:identifier>partialDose</dcterms:identifier>
</spcode:ImmunizationAdministrationStatus>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='ImmunizationClass_code'>`ImmunizationClass code`</span>

`ImmunizationClass` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


codes are drawn from the CDC's Vaccine Group vocabulary.  URIs are of the form:

http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#code


system = http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/ImmunizationClass</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='ImmunizationProduct_code'>`ImmunizationProduct code`</span>

`ImmunizationProduct` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


codes are drawn from the CDC's Vaccine Group vocabulary.  URIs are of the form:

http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#code


system = http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/ImmunizationProduct</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='ImmunizationRefusalReason_code'>`ImmunizationRefusalReason code`</span>

`ImmunizationRefusalReason` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


Constrained to one of: 
 {% highlight xml %}


<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#vaccineUnavailable">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Vaccine unavailable at visit</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>vaccineUnavailable</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#patientUndergoingDesensitizationTherapy">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Patient undergoing desensitization therapy</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>patientUndergoingDesensitizationTherapy</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#notIndicatedPerGuidelines">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Not indicated per guidelines</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>notIndicatedPerGuidelines</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#recentChemoOrRadiaton">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Recent chemotherapy/radiaton</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>recentChemoOrRadiaton</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Allergy to vaccine/vaccine components, or allergy to eggs</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>allergy</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#providerDeferred">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Provider deferred</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>providerDeferred</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#documentedImmunityOrPreviousDisease">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Documented immunity or previous disease</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>documentedImmunityOrPreviousDisease</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#previouslyVaccinated">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Previously vaccinated</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>previouslyVaccinated</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#contraindicated">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Contraindicated</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>contraindicated</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#patientOrParentRefused">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Patient/parent refused</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>patientOrParentRefused</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#comfortMeasuresOnly">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Comfort Measures Only</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>comfortMeasuresOnly</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#possiblePriorAllergyOrReaction">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Possible allergy/reaction to prior dose</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>possiblePriorAllergyOrReaction</dcterms:identifier>
</spcode:ImmunizationRefusalReason>



<spcode:ImmunizationRefusalReason rdf:about="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#recentOrganOrStemCellTransplant">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Recent organ/stem cell transplant</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#</sp:system>
  <dcterms:identifier>recentOrganOrStemCellTransplant</dcterms:identifier>
</spcode:ImmunizationRefusalReason>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/ImmunizationRefusalReason</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='LOINC_code'>`LOINC code`</span>

`LOINC` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


LOINC code where URI matches:  http://purl.bioontology.org/ontology/LNC/{loinc_code}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/LOINC</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='LabResultInterpretation_code'>`LabResultInterpretation code`</span>

`LabResultInterpretation` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


Constrained to one of: 
 {% highlight xml %}


<spcode:LabResultInterpretation rdf:about="http://smartplatforms.org/terms/codes/LabResultInterpretation#normal">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Normal</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/LabResultInterpretation#</sp:system>
  <dcterms:identifier>normal</dcterms:identifier>
</spcode:LabResultInterpretation>



<spcode:LabResultInterpretation rdf:about="http://smartplatforms.org/terms/codes/LabResultInterpretation#critical">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Critical</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/LabResultInterpretation#</sp:system>
  <dcterms:identifier>critical</dcterms:identifier>
</spcode:LabResultInterpretation>



<spcode:LabResultInterpretation rdf:about="http://smartplatforms.org/terms/codes/LabResultInterpretation#abnormal">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Abnormal</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/LabResultInterpretation#</sp:system>
  <dcterms:identifier>abnormal</dcterms:identifier>
</spcode:LabResultInterpretation>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/LabResultInterpretation</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='LabResultStatus_code'>`LabResultStatus code`</span>

`LabResultStatus` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


Constrained to one of: 
 {% highlight xml %}


<spcode:LabResultStatus rdf:about="http://smartplatforms.org/terms/codes/LabStatus#correction">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Correction</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/LabStatus#</sp:system>
  <dcterms:identifier>correction</dcterms:identifier>
</spcode:LabResultStatus>



<spcode:LabResultStatus rdf:about="http://smartplatforms.org/terms/codes/LabStatus#preliminary">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Preliminary</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/LabStatus#</sp:system>
  <dcterms:identifier>preliminary</dcterms:identifier>
</spcode:LabResultStatus>



<spcode:LabResultStatus rdf:about="http://smartplatforms.org/terms/codes/LabStatus#final">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Final</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/LabStatus#</sp:system>
  <dcterms:identifier>final</dcterms:identifier>
</spcode:LabResultStatus>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/LabResultStatus</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='MedicalRecordNumber_code'>`MedicalRecordNumber code`</span>

`MedicalRecordNumber` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/MedicalRecordNumber</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='MedicationProvenance_code'>`MedicationProvenance code`</span>

`MedicationProvenance` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


Constrained to one of: 
 {% highlight xml %}


<spcode:MedicationProvenance rdf:about="http://smartplatforms.org/terms/codes/MedicationProvenance#prescription">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Derived by prescription</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/MedicationProvenance#</sp:system>
  <dcterms:identifier>prescription</dcterms:identifier>
</spcode:MedicationProvenance>



<spcode:MedicationProvenance rdf:about="http://smartplatforms.org/terms/codes/MedicationProvenance#fulfillment">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Derived by fulfillment</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/MedicationProvenance#</sp:system>
  <dcterms:identifier>fulfillment</dcterms:identifier>
</spcode:MedicationProvenance>



<spcode:MedicationProvenance rdf:about="http://smartplatforms.org/terms/codes/MedicationProvenance#administration">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Derived by administration</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/MedicationProvenance#</sp:system>
  <dcterms:identifier>administration</dcterms:identifier>
</spcode:MedicationProvenance>



<spcode:MedicationProvenance rdf:about="http://smartplatforms.org/terms/codes/MedicationProvenance#reconciliation">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Derived by medication reconciliation</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/MedicationProvenance#</sp:system>
  <dcterms:identifier>reconciliation</dcterms:identifier>
</spcode:MedicationProvenance>



<spcode:MedicationProvenance rdf:about="http://smartplatforms.org/terms/codes/MedicationProvenance#patientReport">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Derived by patient report</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/MedicationProvenance#</sp:system>
  <dcterms:identifier>patientReport</dcterms:identifier>
</spcode:MedicationProvenance>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/MedicationProvenance</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='NDFRT_code'>`NDFRT code`</span>

`NDFRT` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/NDFRT</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='RxNorm_code'>`RxNorm code`</span>

`RxNorm` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/RxNorm</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='RxNorm_Ingredient_code'>`RxNorm_Ingredient code`</span>

`RxNorm_Ingredient` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [RxNorm](#RxNorm)


RxNorm TTY='in'


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/RxNorm_Ingredient</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='RxNorm_Semantic_code'>`RxNorm_Semantic code`</span>

`RxNorm_Semantic` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [RxNorm](#RxNorm)


RxNorm TTY in ('SCD','SBD','GPCK','BPCK')


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/RxNorm_Semantic</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='SNOMED_code'>`SNOMED code`</span>

`SNOMED` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


SNOMED code with URI matchign http://purl.bioontology.org/ontology/SNOMEDCT/{snomed_concept_id}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/SNOMED</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='TranslationFidelity_code'>`TranslationFidelity code`</span>

`TranslationFidelity` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


Constrained to one of: 
 {% highlight xml %}


<spcode:TranslationFidelity rdf:about="http://smartplatforms.org/terms/codes/TranslationFidelity#automated">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Automated</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/TranslationFidelity#</sp:system>
  <dcterms:identifier>automated</dcterms:identifier>
</spcode:TranslationFidelity>



<spcode:TranslationFidelity rdf:about="http://smartplatforms.org/terms/codes/TranslationFidelity#unmappable">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Unmappable</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/TranslationFidelity#</sp:system>
  <dcterms:identifier>unmappable</dcterms:identifier>
</spcode:TranslationFidelity>



<spcode:TranslationFidelity rdf:about="http://smartplatforms.org/terms/codes/TranslationFidelity#verified">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Verified</dcterms:title>
  <sp:system>http://smartplatforms.org/terms/codes/TranslationFidelity#</sp:system>
  <dcterms:identifier>verified</dcterms:identifier>
</spcode:TranslationFidelity>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/TranslationFidelity</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='UNII_code'>`UNII code`</span>

`UNII` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType)


UNII code with URI matching http://fda.gov/UNII/{UNII}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/UNII</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

## <span id='VitalSign_code'>`VitalSign code`</span>

`VitalSign` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [LOINC](#LOINC)


Constrained to one of: 
 {% highlight xml %}


<spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8462-4">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Intravascular diastolic</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
  <dcterms:identifier>8462-4</dcterms:identifier>
</spcode:VitalSign>



<spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/9279-1">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Respiration rate</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
  <dcterms:identifier>9279-1</dcterms:identifier>
</spcode:VitalSign>



<spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/39156-5">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Body mass index</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
  <dcterms:identifier>39156-5</dcterms:identifier>
</spcode:VitalSign>



<spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8310-5">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Body temperature</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
  <dcterms:identifier>8310-5</dcterms:identifier>
</spcode:VitalSign>



<spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/2710-2">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Oxygen saturation</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
  <dcterms:identifier>2710-2</dcterms:identifier>
</spcode:VitalSign>



<spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8302-2">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Body height</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
  <dcterms:identifier>8302-2</dcterms:identifier>
</spcode:VitalSign>



<spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8867-4">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Heart rate</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
  <dcterms:identifier>8867-4</dcterms:identifier>
</spcode:VitalSign>



<spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8480-6">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Intravascular systolic</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
  <dcterms:identifier>8480-6</dcterms:identifier>
</spcode:VitalSign>



<spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/3141-9">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Body weight</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
  <dcterms:identifier>3141-9</dcterms:identifier>
</spcode:VitalSign>



<spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8306-3">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Body height (lying)</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
  <dcterms:identifier>8306-3</dcterms:identifier>
</spcode:VitalSign>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/VitalSign</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


identifier
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/identifier</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


title
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


system
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#system</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>
