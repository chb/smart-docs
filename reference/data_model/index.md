---
layout: page
title: SMART Data Model
includenav: smartnav.markdown
---
{% include JB/setup %}

{% include example_format_tabs_top.html %}

<div class='simple_box'>
  <p>This is highly preliminary, not a commitment or final version of any
  particular API or data model. This is purely for internal collaboration and
  preview purposes.</p>

  {% include githublink %}
</div>


<div id="toc"></div>


# Changelog

Click here for the list of [Changes to the API and Payloads](../change_log/).
And here is an [Atom Feed](https://github.com/chb/smart-docs/commits/gh-pages.atom)
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


<hr>

<!-- GENERATED DOCS INSERTED BELOW THIS LINE - DON'T EDIT OR REMOVE ME! -->



# Clinical Statement Types


<h2 id='Allergy'><code>Allergy</code></h2>

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
      <sp:Allergy rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252">
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
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://purl.org/dc/terms/identifier> "24484000" .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://purl.org/dc/terms/title> "Severe" .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/AllergySeverity> .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://purl.org/dc/terms/identifier> "2231" .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/RXNORM/" .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://purl.org/dc/terms/title> "Cephalexin" .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/RxNorm_Ingredient> .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
_:_7d1cfa97-cef5-4cca-8635-1225bc63b905 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/24484000> .
_:_7d1cfa97-cef5-4cca-8635-1225bc63b905 <http://purl.org/dc/terms/title> "Severe" .
_:_7d1cfa97-cef5-4cca-8635-1225bc63b905 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_eaf17847-7323-4a37-930e-3f5a38f389b2 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/416098002> .
_:_eaf17847-7323-4a37-930e-3f5a38f389b2 <http://purl.org/dc/terms/title> "Drug allergy" .
_:_eaf17847-7323-4a37-930e-3f5a38f389b2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_5ed06906-0991-4694-bbf5-829bb4e47ef6 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/39579001> .
_:_5ed06906-0991-4694-bbf5-829bb4e47ef6 <http://purl.org/dc/terms/title> "Anaphylaxis" .
_:_5ed06906-0991-4694-bbf5-829bb4e47ef6 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_e89158d9-fb14-4725-b21d-852c5265e350 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/39579001> .
_:_e89158d9-fb14-4725-b21d-852c5265e350 <http://purl.org/dc/terms/title> "Anaphylaxis" .
_:_e89158d9-fb14-4725-b21d-852c5265e350 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_88f3e290-14dd-45be-9695-bee18805f7b1 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/NDFRT/N0000175503> .
_:_88f3e290-14dd-45be-9695-bee18805f7b1 <http://purl.org/dc/terms/title> "Sulfonamide Antibacterial" .
_:_88f3e290-14dd-45be-9695-bee18805f7b1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_b01551a2-c85f-45e3-83ba-05c48b8bb2a8 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/416098002> .
_:_b01551a2-c85f-45e3-83ba-05c48b8bb2a8 <http://purl.org/dc/terms/title> "Drug allergy" .
_:_b01551a2-c85f-45e3-83ba-05c48b8bb2a8 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_6f1c74d4-600a-41aa-a5af-05995987152e <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/24484000> .
_:_6f1c74d4-600a-41aa-a5af-05995987152e <http://purl.org/dc/terms/title> "Severe" .
_:_6f1c74d4-600a-41aa-a5af-05995987152e <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://purl.org/dc/terms/identifier> "416098002" .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://purl.org/dc/terms/title> "Drug allergy" .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/AllergyCategory> .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://smartplatforms.org/terms#severity> _:_7d1cfa97-cef5-4cca-8635-1225bc63b905 .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://smartplatforms.org/terms#drugClassAllergen> _:_88f3e290-14dd-45be-9695-bee18805f7b1 .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://smartplatforms.org/terms#allergicReaction> _:_e89158d9-fb14-4725-b21d-852c5265e350 .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Allergy> .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://smartplatforms.org/terms#category> _:_b01551a2-c85f-45e3-83ba-05c48b8bb2a8 .
_:_160ec1b4-4b47-4e5c-a8f9-8e6ddc55d46a <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/RXNORM/2231> .
_:_160ec1b4-4b47-4e5c-a8f9-8e6ddc55d46a <http://purl.org/dc/terms/title> "Cephalexin" .
_:_160ec1b4-4b47-4e5c-a8f9-8e6ddc55d46a <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://purl.org/dc/terms/identifier> "39579001" .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://purl.org/dc/terms/title> "Anaphylaxis" .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/SNOMED> .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://purl.org/dc/terms/identifier> "N0000175503" .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/NDFRT/" .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://purl.org/dc/terms/title> "Sulfonamide Antibacterial" .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/NDFRT> .
_:_c76a250c-cb84-4b8d-82cc-311fd6cdd62e <http://smartplatforms.org/terms#severity> _:_6f1c74d4-600a-41aa-a5af-05995987152e .
_:_c76a250c-cb84-4b8d-82cc-311fd6cdd62e <http://smartplatforms.org/terms#allergicReaction> _:_5ed06906-0991-4694-bbf5-829bb4e47ef6 .
_:_c76a250c-cb84-4b8d-82cc-311fd6cdd62e <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:_c76a250c-cb84-4b8d-82cc-311fd6cdd62e <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Allergy> .
_:_c76a250c-cb84-4b8d-82cc-311fd6cdd62e <http://smartplatforms.org/terms#drugAllergen> _:_160ec1b4-4b47-4e5c-a8f9-8e6ddc55d46a .
_:_c76a250c-cb84-4b8d-82cc-311fd6cdd62e <http://smartplatforms.org/terms#category> _:_eaf17847-7323-4a37-930e-3f5a38f389b2 .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> a sp:Allergy;
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
    sp:drugAllergen [ a sp:CodedValue;
            dcterms:title "Cephalexin";
            sp:code <http://purl.bioontology.org/ontology/RXNORM/2231> ];
    sp:severity [ a sp:CodedValue;
            dcterms:title "Severe";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/24484000> ] .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://purl.bioontology.org/ontology/RXNORM/2231",
      "@type": [
        "spcode__RxNorm_Ingredient",
        "Code"
      ],
      "dcterms__identifier": "2231",
      "dcterms__title": "Cephalexin",
      "system": "http://purl.bioontology.org/ontology/RXNORM/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/24484000",
      "@type": [
        "spcode__AllergySeverity",
        "Code"
      ],
      "dcterms__identifier": "24484000",
      "dcterms__title": "Severe",
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
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252",
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
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/416098002",
      "@type": [
        "spcode__AllergyCategory",
        "Code"
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#SNOMED_code'>SNOMED</a></span>
<br><br>Reaction associated with an allergy.  Code drawn from SNOMED-CT.
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#AllergyCategory_code'>AllergyCategory</a></span>
<br><br>Category of an allergy (food, drug, other substance).
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#RxNorm_Ingredient_code'>RxNorm_Ingredient</a></span>
<br><br>For drug allergies, an RxNorm Concept at the ingredient level (TTY='in').
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#NDFRT_code'>NDFRT</a></span>
<br><br>Class of allergen, e.g. Sulfonamides or ACE inhibitors.  RDF Code node with code drawn from
            NDF-RT: http://purl.bioontology.org/ontology/NDFRT/{NDFRT_ID}
</td>
</tr>

<tr><td style='width: 30%;
'>


otherAllergen
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#otherAllergen</span>
<br />
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#UNII_code'>UNII</a></span>
<br><br>Substance acting as a food, environmenta, or other allergen.  For environmental and food substance is a UNII.
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#AllergySeverity_code'>AllergySeverity</a></span>
<br><br>Severity of an allergy	
</td>
</tr>

</table>

<h2 id='Allergy_Exclusion'><code>Allergy Exclusion</code></h2>

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

<sp:AllergyExclusion rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/allergy_exclusions/987235">
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
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://purl.org/dc/terms/identifier> "160244002" .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/AllergyExclusion> .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://purl.org/dc/terms/title> "No known allergies" .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
_:_9b3ecddf-7112-4632-af80-d38641a7a873 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_9b3ecddf-7112-4632-af80-d38641a7a873 <http://purl.org/dc/terms/title> "No known allergies" .
_:_9b3ecddf-7112-4632-af80-d38641a7a873 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/160244002> .
<http://sandbox-api.smartplatforms.org/records/2169591/allergy_exclusions/987235> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#AllergyExclusion> .
<http://sandbox-api.smartplatforms.org/records/2169591/allergy_exclusions/987235> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/allergy_exclusions/987235> <http://smartplatforms.org/terms#allergyExclusionName> _:_9b3ecddf-7112-4632-af80-d38641a7a873 .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://sandbox-api.smartplatforms.org/records/2169591/allergy_exclusions/987235> a sp:AllergyExclusion;
    sp:allergyExclusionName [ a sp:CodedValue;
            dcterms:title "No known allergies";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/160244002> ];
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591> .

<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> a sp:Code,
        spcode:AllergyExclusion;
    dcterms:identifier "160244002";
    dcterms:title "No known allergies";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/allergy_exclusions/987235",
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
    },
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/160244002",
      "@type": [
        "spcode__AllergyExclusion",
        "Code"
      ],
      "dcterms__identifier": "160244002",
      "dcterms__title": "No known allergies",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#AllergyExclusion_code'>AllergyExclusion</a></span>
<br><br>Nature of the allergy exclusion.
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

</table>

<h2 id='Clinical_Note'><code>Clinical Note</code></h2>

`Clinical Note` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


The SMART Clinical Note model encapsulates a simple clinical note with a date, author, title, and one or more instances of formatted data (as sp:DocumentWithFormat nodes) ,  

The formatted data, in turn, comprises a MIME type and either supply the value inline (via the rdf:value property) or as a URI at which the content can be found (by assigning a URI to the sp:DocumentWithFormat).

<div id='Clinical_Note_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Clinical_Note_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Clinical_Note_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Clinical_Note_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Clinical_Note_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:v="http://www.w3.org/2006/vcard/ns#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"
>
 <sp:ClinicalNote rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335">
    <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
    <dcterms:date>2012-05-17</dcterms:date>
    <dcterms:title>Cardiology clinic follow-up</dcterms:title>
    <dcterms:hasFormat>
         <sp:DocumentWithFormat rdf:about="http://url.of.raw.note/content">
            <dcterms:format rdf:resoruce="http://purl.org/NET/mediatypes/text/html"/>
         </sp:DocumentWithFormat>
    </dcterms:hasFormat>
    <sp:provider>
      <sp:Provider>
        <v:n>
          <v:Name>
           <v:given-name>Joshua</v:given-name>
           <v:family-name>Mandel</v:family-name>
          </v:Name>
        </v:n>
      </sp:Provider>
    </sp:provider>
 </sp:ClinicalNote>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:_7e3c7d9b-a94f-4a79-a7c7-e0a31645d900 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .
_:_7e3c7d9b-a94f-4a79-a7c7-e0a31645d900 <http://www.w3.org/2006/vcard/ns#given-name> "Joshua" .
_:_7e3c7d9b-a94f-4a79-a7c7-e0a31645d900 <http://www.w3.org/2006/vcard/ns#family-name> "Mandel" .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://purl.org/dc/terms/hasFormat> <http://url.of.raw.note/content> .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ClinicalNote> .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://purl.org/dc/terms/title> "Cardiology clinic follow-up" .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://purl.org/dc/terms/date> "2012-05-17" .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://smartplatforms.org/terms#provider> _:_2f08836a-62bc-4cd9-b32d-8db1f84efcfb .
_:_22042caa-e1ea-4316-92b2-dc144fb29499 <http://www.w3.org/1999/02/22-rdf-syntax-ns#resoruce> "http://purl.org/NET/mediatypes/text/html" .
_:_2f08836a-62bc-4cd9-b32d-8db1f84efcfb <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Provider> .
_:_2f08836a-62bc-4cd9-b32d-8db1f84efcfb <http://www.w3.org/2006/vcard/ns#n> _:_7e3c7d9b-a94f-4a79-a7c7-e0a31645d900 .
<http://url.of.raw.note/content> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#DocumentWithFormat> .
<http://url.of.raw.note/content> <http://purl.org/dc/terms/format> _:_22042caa-e1ea-4316-92b2-dc144fb29499 .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> a sp:ClinicalNote;
    dcterms:date "2012-05-17";
    dcterms:hasFormat <http://url.of.raw.note/content>;
    dcterms:title "Cardiology clinic follow-up";
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:provider [ a sp:Provider;
            vcard:n [ a vcard:Name;
                    vcard:family-name "Mandel";
                    vcard:given-name "Joshua" ] ] .

<http://url.of.raw.note/content> a sp:DocumentWithFormat;
    dcterms:format [ rdf:resoruce "http://purl.org/NET/mediatypes/text/html" ] .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://url.of.raw.note/content",
      "@type": "DocumentWithFormat",
      "dcterms__format": {
        "http://www.w3.org/1999/02/22-rdf-syntax-ns#resoruce": "http://purl.org/NET/mediatypes/text/html"
      }
    },
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335",
      "@type": "ClinicalNote",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "dcterms__date": "2012-05-17",
      "dcterms__hasFormat": [
        {
          "@id": "http://url.of.raw.note/content"
        }
      ],
      "dcterms__title": "Cardiology clinic follow-up",
      "provider": {
        "@type": "Provider",
        "vcard__n": {
          "@type": "vcard__Name",
          "vcard__family_name": "Mandel",
          "vcard__given_name": "Joshua"
        }
      }
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#ClinicalNote</caption>
<tbody>
<tr><td style='width: 30%;
'>


date
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/date</span>
<br />
Date on which the note was written, as an ISO-8601 string. <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


hasFormat
<br />
<span style='font-size: small; font-weight: normal'>Required: 1 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/hasFormat</span>
<br />
<span style='font-size: small'><a href='#DocumentWithFormat'>DocumentWithFormat</a></span>
<br><br>Resource identifier for a sp:DocumentWithFormat.  This resource has a dcterms:format indicating its mime type, and a URI that you can dereference (http GET) to obtain the document.
</td>
</tr>

<tr><td style='width: 30%;
'>


title
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/title</span>
<br />
Title of the clinical note, as free-text. <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

</table>

<h2 id='Demographics'><code>Demographics</code></h2>

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
   <sp:Demographics rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/demographics">
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
_:_65e232fa-dd00-4cd1-b815-0f4afb707b36 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Home> .
_:_65e232fa-dd00-4cd1-b815-0f4afb707b36 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Tel> .
_:_65e232fa-dd00-4cd1-b815-0f4afb707b36 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Pref> .
_:_65e232fa-dd00-4cd1-b815-0f4afb707b36 <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "800-555-1212" .
_:_fc06ad93-0425-424b-810f-b1806b05bdbd <http://www.w3.org/2006/vcard/ns#locality> "Wonderland" .
_:_fc06ad93-0425-424b-810f-b1806b05bdbd <http://www.w3.org/2006/vcard/ns#postal-code> "54321" .
_:_fc06ad93-0425-424b-810f-b1806b05bdbd <http://www.w3.org/2006/vcard/ns#street-address> "15 Main St" .
_:_fc06ad93-0425-424b-810f-b1806b05bdbd <http://www.w3.org/2006/vcard/ns#region> "OZ" .
_:_fc06ad93-0425-424b-810f-b1806b05bdbd <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Home> .
_:_fc06ad93-0425-424b-810f-b1806b05bdbd <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Address> .
_:_fc06ad93-0425-424b-810f-b1806b05bdbd <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Pref> .
_:_fc06ad93-0425-424b-810f-b1806b05bdbd <http://www.w3.org/2006/vcard/ns#country> "USA" .
_:_fc06ad93-0425-424b-810f-b1806b05bdbd <http://www.w3.org/2006/vcard/ns#extended-address> "Apt 2" .
_:_f4307d2b-0e22-41f4-9458-ea707b308a8b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
_:_f4307d2b-0e22-41f4-9458-ea707b308a8b <http://purl.org/dc/terms/identifier> "2304575" .
_:_f4307d2b-0e22-41f4-9458-ea707b308a8b <http://purl.org/dc/terms/title> "My Hospital Record 2304575" .
_:_f4307d2b-0e22-41f4-9458-ea707b308a8b <http://smartplatforms.org/terms#system> "My Hospital Record" .
_:_11754e01-db76-414f-bb2a-67e6ed677aae <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .
_:_11754e01-db76-414f-bb2a-67e6ed677aae <http://www.w3.org/2006/vcard/ns#family-name> "Odenkirk" .
_:_11754e01-db76-414f-bb2a-67e6ed677aae <http://www.w3.org/2006/vcard/ns#given-name> "Bob" .
_:_11754e01-db76-414f-bb2a-67e6ed677aae <http://www.w3.org/2006/vcard/ns#additional-name> "J" .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://smartplatforms.org/terms#medicalRecordNumber> _:_f4307d2b-0e22-41f4-9458-ea707b308a8b .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#adr> _:_fc06ad93-0425-424b-810f-b1806b05bdbd .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://xmlns.com/foaf/0.1/gender> "male" .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#email> "bob.odenkirk@example.com" .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Demographics> .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#tel> _:_65e232fa-dd00-4cd1-b815-0f4afb707b36 .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#tel> _:_8179c90a-15b1-4908-a1ac-1818cb71af49 .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#bday> "1959-12-25" .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#n> _:_11754e01-db76-414f-bb2a-67e6ed677aae .
_:_8179c90a-15b1-4908-a1ac-1818cb71af49 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Cell> .
_:_8179c90a-15b1-4908-a1ac-1818cb71af49 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Tel> .
_:_8179c90a-15b1-4908-a1ac-1818cb71af49 <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "800-555-1515" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

<http://sandbox-api.smartplatforms.org/records/2169591/demographics> a sp:Demographics;
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
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@id": "http://sandbox-api.smartplatforms.org/records/2169591/demographics",
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
  "vcard__adr": {
    "@type": [
      "vcard__Home",
      "vcard__Address",
      "vcard__Pref"
    ],
    "http://www.w3.org/2006/vcard/ns#country": "USA",
    "vcard__extended_address": "Apt 2",
    "vcard__locality": "Wonderland",
    "vcard__postal_code": "54321",
    "vcard__region": "OZ",
    "vcard__street_address": "15 Main St"
  },
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
        "vcard__Home",
        "vcard__Tel",
        "vcard__Pref"
      ],
      "rdf__value": "800-555-1212"
    },
    {
      "@type": [
        "vcard__Cell",
        "vcard__Tel"
      ],
      "rdf__value": "800-555-1515"
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
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
<span style='font-size: small'><a href='#Code'>Code</a></span>
<br><br>
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
<span style='font-size: small'><a href='#Address'>Address</a></span>
<br><br>
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
Birthday as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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
<span style='font-size: small'><a href='#Name'>Name</a></span>
<br><br>
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
<span style='font-size: small'><a href='#Tel'>Tel</a></span>
<br><br>
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

<h2 id='Encounter'><code>Encounter</code></h2>

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
      <sp:Encounter rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352">
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
_:_0f2d5eec-8239-4e0d-99b1-b4be74f04936 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/EncounterType#ambulatory> .
_:_0f2d5eec-8239-4e0d-99b1-b4be74f04936 <http://purl.org/dc/terms/title> "Ambulatory encounter" .
_:_0f2d5eec-8239-4e0d-99b1-b4be74f04936 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/identifier> "ambulatory" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/title> "Ambulatory encounter" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/EncounterType> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/EncounterType#" .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#endDate> "2010-05-12T04:20:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#startDate> "2010-05-12T04:00:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Encounter> .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#encounterType> _:_0f2d5eec-8239-4e0d-99b1-b4be74f04936 .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> a sp:Encounter;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:encounterType [ a sp:CodedValue;
            dcterms:title "Ambulatory encounter";
            sp:code <http://smartplatforms.org/terms/codes/EncounterType#ambulatory> ];
    sp:endDate "2010-05-12T04:20:00Z";
    sp:startDate "2010-05-12T04:00:00Z" .

<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> a sp:Code,
        spcode:EncounterType;
    dcterms:identifier "ambulatory";
    dcterms:title "Ambulatory encounter";
    sp:system "http://smartplatforms.org/terms/codes/EncounterType#" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://smartplatforms.org/terms/codes/EncounterType#ambulatory",
      "@type": [
        "Code",
        "spcode__EncounterType"
      ],
      "dcterms__identifier": "ambulatory",
      "dcterms__title": "Ambulatory encounter",
      "system": "http://smartplatforms.org/terms/codes/EncounterType#"
    },
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352",
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#EncounterType_code'>EncounterType</a></span>
<br><br>Type of encounter
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
Date when encounter ended, as an ISO-8601 string <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
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
<span style='font-size: small'><a href='#Organization'>Organization</a></span>
<br><br>Facility where encounter occurred
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
<span style='font-size: small'><a href='#Provider'>Provider</a></span>
<br><br>Provider responsible for encounter
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
Date when encounter began, as an ISO-8601 string <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

</table>

<h2 id='Fulfillment'><code>Fulfillment</code></h2>

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
 <sp:Fulfillment rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221">
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
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#pbm> "T00000000001011" .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Fulfillment> .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#pharmacy> _:_469c6482-4c81-489a-9156-3f3cfcc4dbb8 .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#medication> <http://sandbox-api.smartplatforms.org/records/2169591/medications/123> .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#provider> _:_fb054fe4-c6d4-48c8-bca4-be876e027e1e .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://purl.org/dc/terms/date> "2010-05-12T04:00:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#quantityDispensed> _:_ddee49f1-dc2e-4ac0-bfd9-40533a8cd854 .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#dispenseDaysSupply> "30" .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:_fb054fe4-c6d4-48c8-bca4-be876e027e1e <http://www.w3.org/2006/vcard/ns#n> _:_412c6444-aedb-40df-9d55-f3af544d04e3 .
_:_fb054fe4-c6d4-48c8-bca4-be876e027e1e <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Provider> .
_:_fb054fe4-c6d4-48c8-bca4-be876e027e1e <http://smartplatforms.org/terms#npiNumber> "5235235" .
_:_fb054fe4-c6d4-48c8-bca4-be876e027e1e <http://smartplatforms.org/terms#deaNumber> "325555555" .
_:_469c6482-4c81-489a-9156-3f3cfcc4dbb8 <http://www.w3.org/2006/vcard/ns#adr> _:_b6b276a1-00d9-4943-85cd-6f3b6f2c8d71 .
_:_469c6482-4c81-489a-9156-3f3cfcc4dbb8 <http://smartplatforms.org/terms#ncpdpId> "5235235" .
_:_469c6482-4c81-489a-9156-3f3cfcc4dbb8 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Pharmacy> .
_:_469c6482-4c81-489a-9156-3f3cfcc4dbb8 <http://www.w3.org/2006/vcard/ns#organization-name> "CVS #588" .
_:_ddee49f1-dc2e-4ac0-bfd9-40533a8cd854 <http://smartplatforms.org/terms#unit> "{tablet}" .
_:_ddee49f1-dc2e-4ac0-bfd9-40533a8cd854 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:_ddee49f1-dc2e-4ac0-bfd9-40533a8cd854 <http://smartplatforms.org/terms#value> "60" .
_:_412c6444-aedb-40df-9d55-f3af544d04e3 <http://www.w3.org/2006/vcard/ns#family-name> "Mandel" .
_:_412c6444-aedb-40df-9d55-f3af544d04e3 <http://www.w3.org/2006/vcard/ns#given-name> "Joshua" .
_:_412c6444-aedb-40df-9d55-f3af544d04e3 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .
_:_b6b276a1-00d9-4943-85cd-6f3b6f2c8d71 <http://www.w3.org/2006/vcard/ns#locality> "WonderCity" .
_:_b6b276a1-00d9-4943-85cd-6f3b6f2c8d71 <http://www.w3.org/2006/vcard/ns#street-address> "111 Lake Drive" .
_:_b6b276a1-00d9-4943-85cd-6f3b6f2c8d71 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Address> .
_:_b6b276a1-00d9-4943-85cd-6f3b6f2c8d71 <http://www.w3.org/2006/vcard/ns#postal-code> "5555" .
_:_b6b276a1-00d9-4943-85cd-6f3b6f2c8d71 <http://www.w3.org/2006/vcard/ns#country-name> "Australia" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> a sp:Fulfillment;
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
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@id": "http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221",
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
    "vcard__adr": {
      "@type": "vcard__Address",
      "vcard__country_name": "Australia",
      "vcard__locality": "WonderCity",
      "vcard__postal_code": "5555",
      "vcard__street_address": "111 Lake Drive"
    },
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
Date on which medication was dispensed, as an ISO-8601 string <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
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
<span style='font-size: small'><a href='#Medication'>Medication</a></span>
<br><br>
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
<span style='font-size: small'><a href='#Pharmacy'>Pharmacy</a></span>
<br><br>The pharmacy that dispensed the medication
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
<span style='font-size: small'><a href='#Provider'>Provider</a></span>
<br><br>Clinician who prescribed the medication
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
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a></span>
<br><br>Quantity dispensed, with units
</td>
</tr>

</table>

<h2 id='Immunization'><code>Immunization</code></h2>

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

   <sp:Immunization rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972">
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
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://smartplatforms.org/terms#productClass> _:_0c9a4249-473d-4b8c-8aa7-c93e1a0227ac .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Immunization> .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://smartplatforms.org/terms#administrationStatus> _:_a2c1de94-ecf6-42e7-a1b2-c6d2ca1439eb .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://smartplatforms.org/terms#refusalReason> _:_77cbc01b-98b8-4f1b-b9d3-5991f09c1625 .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://smartplatforms.org/terms#productName> _:_0ef01446-79d3-47b6-b272-558148223116 .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://purl.org/dc/terms/date> "2010-05-12T04:00:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://purl.org/dc/terms/identifier> "notAdministered" .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#" .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus> .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://purl.org/dc/terms/title> "Not Administered" .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://purl.org/dc/terms/identifier> "allergy" .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#" .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationRefusalReason> .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://purl.org/dc/terms/title> "Allergy to vaccine/vaccine components, or allergy to eggs" .
_:_77cbc01b-98b8-4f1b-b9d3-5991f09c1625 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> .
_:_77cbc01b-98b8-4f1b-b9d3-5991f09c1625 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_77cbc01b-98b8-4f1b-b9d3-5991f09c1625 <http://purl.org/dc/terms/title> "Allergy to vaccine/vaccine components, or allergy to eggs" .
_:_0c9a4249-473d-4b8c-8aa7-c93e1a0227ac <http://smartplatforms.org/terms#code> <http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> .
_:_0c9a4249-473d-4b8c-8aa7-c93e1a0227ac <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_0c9a4249-473d-4b8c-8aa7-c93e1a0227ac <http://purl.org/dc/terms/title> "TYPHOID" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://purl.org/dc/terms/identifier> "25" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://smartplatforms.org/terms#system> "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationProduct> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://purl.org/dc/terms/title> "typhoid, oral" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://purl.org/dc/terms/identifier> "TYPHOID" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://smartplatforms.org/terms#system> "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationClass> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://purl.org/dc/terms/title> "TYPHOID" .
_:_0ef01446-79d3-47b6-b272-558148223116 <http://smartplatforms.org/terms#code> <http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> .
_:_0ef01446-79d3-47b6-b272-558148223116 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_0ef01446-79d3-47b6-b272-558148223116 <http://purl.org/dc/terms/title> "typhoid, oral" .
_:_a2c1de94-ecf6-42e7-a1b2-c6d2ca1439eb <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> .
_:_a2c1de94-ecf6-42e7-a1b2-c6d2ca1439eb <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_a2c1de94-ecf6-42e7-a1b2-c6d2ca1439eb <http://purl.org/dc/terms/title> "Not Administered" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> a sp:Immunization;
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


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID",
      "@type": [
        "spcode__ImmunizationClass",
        "Code"
      ],
      "dcterms__identifier": "TYPHOID",
      "dcterms__title": "TYPHOID",
      "system": "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#"
    },
    {
      "@id": "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25",
      "@type": [
        "spcode__ImmunizationProduct",
        "Code"
      ],
      "dcterms__identifier": "25",
      "dcterms__title": "typhoid, oral",
      "system": "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#"
    },
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972",
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
      "@id": "http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy",
      "@type": [
        "spcode__ImmunizationRefusalReason",
        "Code"
      ],
      "dcterms__identifier": "allergy",
      "dcterms__title": "Allergy to vaccine/vaccine components, or allergy to eggs",
      "system": "http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#"
    },
    {
      "@id": "http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered",
      "@type": [
        "spcode__ImmunizationAdministrationStatus",
        "Code"
      ],
      "dcterms__identifier": "notAdministered",
      "dcterms__title": "Not Administered",
      "system": "http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#"
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
Date and time when the medication was administered or offered, as an ISO-8601 string <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#ImmunizationAdministrationStatus_code'>ImmunizationAdministrationStatus</a></span>
<br><br>
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#ImmunizationClass_code'>ImmunizationClass</a></span>
<br><br>coded name for the product class, according to the set of codes in the CDC Vaccine Groups controlled vocabulary.  For example, a class code meaning 'Rotavirus' would be assigned for a specific product such as Rotarix product.


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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#ImmunizationProduct_code'>ImmunizationProduct</a></span>
<br><br>coded describing the product according to the set of codes in the CVX for immunizations controlled vocabulary.  CVX Code URIs should be represented as:

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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#ImmunizationRefusalReason_code'>ImmunizationRefusalReason</a></span>
<br><br>If the administration status indicates this vaccination was refused, refusalReason is a CodedValue whose code is belongs to a controlled vocabulary of refusal reasons.
</td>
</tr>

</table>

<h2 id='Lab_Panel'><code>Lab Panel</code></h2>

`Lab Panel` is a subtype of and inherits properties from:
[Panel](#Panel), [SMART Statement](#SMART_Statement)


<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
No example yet.
{% endhighlight %}</div>


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#LabPanel</caption>
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
'>


labName
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#labName</span>
<br />
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#LOINC_code'>LOINC</a></span>
<br><br>LOINC Coded Value for the result panel, if any
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


labResult
<br />
<span style='font-size: small; font-weight: normal'>Required: 1 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#labResult</span>
<br />
<span style='font-size: small'><a href='#Lab_Result'>Lab Result</a></span>
<br><br>An individual result belonging to this panel
</td>
</tr>

</table>

<h2 id='Lab_Result'><code>Lab Result</code></h2>

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

  <sp:LabResult  rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724">
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
      <dcterms:date>2010-12-27T17:00:00</dcterms:date>
      <sp:notes>Blood sample appears to have hemolyzed</sp:notes>
   </sp:LabResult>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:_c9422d05-09f2-4328-84d1-70d2b84639a8 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:_c9422d05-09f2-4328-84d1-70d2b84639a8 <http://smartplatforms.org/terms#value> "135" .
_:_c9422d05-09f2-4328-84d1-70d2b84639a8 <http://smartplatforms.org/terms#unit> "mEq/L" .
_:_ab2a97bb-8912-4e01-9d9c-a9edb92a2afb <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:_ab2a97bb-8912-4e01-9d9c-a9edb92a2afb <http://smartplatforms.org/terms#value> "155" .
_:_ab2a97bb-8912-4e01-9d9c-a9edb92a2afb <http://smartplatforms.org/terms#unit> "mEq/L" .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/LOINC> .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://purl.org/dc/terms/title> "Serum sodium" .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://purl.org/dc/terms/identifier> "2951-2" .
_:_c21c09e0-949b-4d48-af9c-91c576426e61 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_c21c09e0-949b-4d48-af9c-91c576426e61 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/LabStatus#final> .
_:_c21c09e0-949b-4d48-af9c-91c576426e61 <http://purl.org/dc/terms/title> "Final results: complete and verified" .
_:_e00e14af-31c2-44d3-9fab-fc3f1ffcad88 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueRange> .
_:_e00e14af-31c2-44d3-9fab-fc3f1ffcad88 <http://smartplatforms.org/terms#minimum> _:_d861c8f3-c248-4b2e-9efa-3b658f167173 .
_:_e00e14af-31c2-44d3-9fab-fc3f1ffcad88 <http://smartplatforms.org/terms#maximum> _:_ab2a97bb-8912-4e01-9d9c-a9edb92a2afb .
_:_63949e87-cb9e-441b-b33f-af3d0750ee8b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodeProvenance> .
_:_63949e87-cb9e-441b-b33f-af3d0750ee8b <http://purl.org/dc/terms/title> "Random blood sodium level" .
_:_63949e87-cb9e-441b-b33f-af3d0750ee8b <http://smartplatforms.org/terms#translationFidelity> <http://smartplatforms.org/terms/codes/TranslationFidelity#verified> .
_:_63949e87-cb9e-441b-b33f-af3d0750ee8b <http://smartplatforms.org/terms#sourceCode> <http://my.local.coding.system/01234> .
_:_d861c8f3-c248-4b2e-9efa-3b658f167173 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:_d861c8f3-c248-4b2e-9efa-3b658f167173 <http://smartplatforms.org/terms#value> "120" .
_:_d861c8f3-c248-4b2e-9efa-3b658f167173 <http://smartplatforms.org/terms#unit> "mEq/L" .
_:_aed6b87b-3daf-4367-af04-1897b85116e9 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_aed6b87b-3daf-4367-af04-1897b85116e9 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> .
_:_aed6b87b-3daf-4367-af04-1897b85116e9 <http://purl.org/dc/terms/title> "Normal" .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/LabResultStatus> .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://purl.org/dc/terms/title> "Final" .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/LabStatus#" .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://purl.org/dc/terms/identifier> "final" .
_:_73fb1cb4-141a-47a8-bbef-d1ca4ef096da <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:_73fb1cb4-141a-47a8-bbef-d1ca4ef096da <http://smartplatforms.org/terms#value> "145" .
_:_73fb1cb4-141a-47a8-bbef-d1ca4ef096da <http://smartplatforms.org/terms#unit> "mEq/L" .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#quantitativeResult> _:_12465c74-8b65-4d37-a99c-a3c618357812 .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://purl.org/dc/terms/date> "2010-12-27T17:00:00" .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#labName> _:_7162adf1-b9aa-46b0-a7d6-61bf62c2239b .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#LabResult> .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#notes> "Blood sample appears to have hemolyzed" .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#accessionNumber> "AC09205823577" .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#labStatus> _:_c21c09e0-949b-4d48-af9c-91c576426e61 .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#abnormalInterpretation> _:_aed6b87b-3daf-4367-af04-1897b85116e9 .
_:_12465c74-8b65-4d37-a99c-a3c618357812 <http://smartplatforms.org/terms#valueAndUnit> _:_ce771727-e07a-4bf5-8c37-ebefbc03953f .
_:_12465c74-8b65-4d37-a99c-a3c618357812 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#QuantitativeResult> .
_:_12465c74-8b65-4d37-a99c-a3c618357812 <http://smartplatforms.org/terms#normalRange> _:_b376fe12-6030-4cc4-a73b-f7178381714b .
_:_12465c74-8b65-4d37-a99c-a3c618357812 <http://smartplatforms.org/terms#nonCriticalRange> _:_e00e14af-31c2-44d3-9fab-fc3f1ffcad88 .
_:_7162adf1-b9aa-46b0-a7d6-61bf62c2239b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_7162adf1-b9aa-46b0-a7d6-61bf62c2239b <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/2951-2> .
_:_7162adf1-b9aa-46b0-a7d6-61bf62c2239b <http://purl.org/dc/terms/title> "Serum sodium" .
_:_7162adf1-b9aa-46b0-a7d6-61bf62c2239b <http://smartplatforms.org/terms#provenance> _:_63949e87-cb9e-441b-b33f-af3d0750ee8b .
_:_ce771727-e07a-4bf5-8c37-ebefbc03953f <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:_ce771727-e07a-4bf5-8c37-ebefbc03953f <http://smartplatforms.org/terms#value> "140" .
_:_ce771727-e07a-4bf5-8c37-ebefbc03953f <http://smartplatforms.org/terms#unit> "mEq/L" .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/LabResultInterpretation> .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://purl.org/dc/terms/title> "Normal" .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/LabResultInterpretation#" .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://purl.org/dc/terms/identifier> "normal" .
_:_b376fe12-6030-4cc4-a73b-f7178381714b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueRange> .
_:_b376fe12-6030-4cc4-a73b-f7178381714b <http://smartplatforms.org/terms#minimum> _:_c9422d05-09f2-4328-84d1-70d2b84639a8 .
_:_b376fe12-6030-4cc4-a73b-f7178381714b <http://smartplatforms.org/terms#maximum> _:_73fb1cb4-141a-47a8-bbef-d1ca4ef096da .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> a sp:LabResult;
    dcterms:date "2010-12-27T17:00:00";
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
                    sp:value "140" ] ] .

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


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724",
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
      "dcterms__date": "2010-12-27T17:00:00",
      "labName": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/LNC/2951-2"
        },
        "dcterms__title": "Serum sodium",
        "provenance": [
          {
            "@type": "CodeProvenance",
            "dcterms__title": "Random blood sodium level",
            "sourceCode": {
              "@id": "http://my.local.coding.system/01234"
            },
            "translationFidelity": {
              "@id": "http://smartplatforms.org/terms/codes/TranslationFidelity#verified"
            }
          }
        ]
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
      }
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/2951-2",
      "@type": [
        "spcode__LOINC",
        "Code"
      ],
      "dcterms__identifier": "2951-2",
      "dcterms__title": "Serum sodium",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://smartplatforms.org/terms/codes/LabResultInterpretation#normal",
      "@type": [
        "Code",
        "spcode__LabResultInterpretation"
      ],
      "dcterms__identifier": "normal",
      "dcterms__title": "Normal",
      "system": "http://smartplatforms.org/terms/codes/LabResultInterpretation#"
    },
    {
      "@id": "http://smartplatforms.org/terms/codes/LabStatus#final",
      "@type": [
        "Code",
        "spcode__LabResultStatus"
      ],
      "dcterms__identifier": "final",
      "dcterms__title": "Final",
      "system": "http://smartplatforms.org/terms/codes/LabStatus#"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#LabResult</caption>
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
Clinically effective date and time of measurement, as an ISO-8601 string.  This is the time when a sample was taken from a patient (e.g. time of a blood draw or urine collection). <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


abnormalInterpretation
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#abnormalInterpretation</span>
<br />
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#LabResultInterpretation_code'>LabResultInterpretation</a></span>
<br><br>Abnormal interpretation status for this lab
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#LOINC_code'>LOINC</a></span>
<br><br>LOINC Coded Value for result (e.g. with title='Serum Sodium' and code=http://purl.bioontology.org/ontology/LNC/2951-2
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#LabResultStatus_code'>LabResultStatus</a></span>
<br><br>Workflow status of this lab value (e.g. "finalized")
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
<span style='font-size: small'><a href='#NarrativeResult'>NarrativeResult</a></span>
<br><br>Narrative result, if any.
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
<span style='font-size: small'><a href='#QuantitativeResult'>QuantitativeResult</a></span>
<br><br>Qualitative result, if any
</td>
</tr>

</table>

<h2 id='Medication'><code>Medication</code></h2>

`Medication` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


The SMART medication type expresses a medication at the level of an
            RxNorm branded or generic drug concept (e.g. "20 mg generic loratadine" or "20 mg brand-name
            claritin").  A medication must include a start date and may include an end date as well as a free-text "instructions" field describing how it should be taken.  When the instructions are simple enough, we also represent them in a structured way, aiming to capture about 80% of outpatient medication dosing schedules.  A very simple semantic structure defines how much to take ("quantity") and how often ("frequency"). Both quantity and frequency are defined with expressions from [http://www.unitsofmeasure.org The Unified Code for Units of Measure], or UCUM (see below).

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
   <sp:Medication rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/medications/123">
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
_:_3104bb64-16fa-4413-910a-4ddd60cff25f <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_3104bb64-16fa-4413-910a-4ddd60cff25f <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/RXNORM/856845> .
_:_3104bb64-16fa-4413-910a-4ddd60cff25f <http://purl.org/dc/terms/title> "AMITRIPTYLINE HCL 50 MG TAB" .
_:_7ed3785f-1674-4305-b858-705d21dc8188 <http://smartplatforms.org/terms#unit> "/d" .
_:_7ed3785f-1674-4305-b858-705d21dc8188 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:_7ed3785f-1674-4305-b858-705d21dc8188 <http://smartplatforms.org/terms#value> "2" .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/RxNorm_Semantic> .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/RXNORM/" .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://purl.org/dc/terms/identifier> "856845" .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://purl.org/dc/terms/title> "AMITRIPTYLINE HCL 50 MG TAB" .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#endDate> "2007-08-14" .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Medication> .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#drugName> _:_3104bb64-16fa-4413-910a-4ddd60cff25f .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#quantity> _:_ce90e83d-2ee6-4add-a5c3-db711243b272 .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#instructions> "Take two tablets twice daily as needed for pain" .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#startDate> "2007-03-14" .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#frequency> _:_7ed3785f-1674-4305-b858-705d21dc8188 .
_:_ce90e83d-2ee6-4add-a5c3-db711243b272 <http://smartplatforms.org/terms#unit> "{tablet}" .
_:_ce90e83d-2ee6-4add-a5c3-db711243b272 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:_ce90e83d-2ee6-4add-a5c3-db711243b272 <http://smartplatforms.org/terms#value> "2" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> a sp:Medication;
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

<http://purl.bioontology.org/ontology/RXNORM/856845> a sp:Code,
        spcode:RxNorm_Semantic;
    dcterms:identifier "856845";
    dcterms:title "AMITRIPTYLINE HCL 50 MG TAB";
    sp:system "http://purl.bioontology.org/ontology/RXNORM/" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/medications/123",
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
    },
    {
      "@id": "http://purl.bioontology.org/ontology/RXNORM/856845",
      "@type": [
        "Code",
        "spcode__RxNorm_Semantic"
      ],
      "dcterms__identifier": "856845",
      "dcterms__title": "AMITRIPTYLINE HCL 50 MG TAB",
      "system": "http://purl.bioontology.org/ontology/RXNORM/"
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#RxNorm_Semantic_code'>RxNorm_Semantic</a></span>
<br><br>RxNorm Concept ID for this medication.  Note: the RxNorm CUI for a SMART medication should have one of the following four types:  SCD (Semantic Clinical Drug), SBD (Semantic Branded Drug), GPCK (Generic Pack), BPCK (Brand Name Pack).   Restricting medications to these four RxNorm types can also be expressed as "TTY in ('SCD','SBD','GPCK','BPCK')" -- and this restriction ensures that SMART medications use concepts of the appropriate specificity:  concepts like "650 mg generic acetaminophen" or "20 mg brand-name Claritin".   Please note that SMART medications do not include explicit structured data about pill strength, concentration, or precise ingredients.  These data are available through RxNorm, including through the free [http://rxnav.nlm.nih.gov/RxNormRestAPI.html RxNav REST API].  Code element with code drawn from http://purl.bioontology.org/ontology/RXNORM/{rxcui}
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
When the patient stopped taking a medication, as an ISO-8601 string. <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
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
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a></span>
<br><br>
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
<span style='font-size: small'><a href='#Fulfillment'>Fulfillment</a></span>
<br><br>
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
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#provenance</span>
<br />
<span style='font-size: small'><a href='#Code'>Code</a></span>
<br><br>
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
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a></span>
<br><br>
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
When the patient started taking a medication, as an ISO-8601 string. <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

</table>

<h2 id='Panel'><code>Panel</code></h2>

`Panel` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Panel</caption>
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

</table>

<h2 id='Problem'><code>Problem</code></h2>

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
    <sp:Problem  rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/problems/961237">
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
<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> <http://smartplatforms.org/terms#endDate> "2007-08-01" .
<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> <http://smartplatforms.org/terms#startDate> "2007-06-12" .
<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> <http://smartplatforms.org/terms#problemName> _:_3f9b582f-db63-4e1c-aef1-7e7efa19808e .
<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Problem> .
<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://purl.org/dc/terms/title> "Backache (finding)" .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://purl.org/dc/terms/identifier> "161891005" .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/SNOMED> .
_:_3f9b582f-db63-4e1c-aef1-7e7efa19808e <http://purl.org/dc/terms/title> "Backache (finding)" .
_:_3f9b582f-db63-4e1c-aef1-7e7efa19808e <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/161891005> .
_:_3f9b582f-db63-4e1c-aef1-7e7efa19808e <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> a sp:Problem;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:endDate "2007-08-01";
    sp:problemName [ a sp:CodedValue;
            dcterms:title "Backache (finding)";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/161891005> ];
    sp:startDate "2007-06-12" .

<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> a sp:Code,
        spcode:SNOMED;
    dcterms:identifier "161891005";
    dcterms:title "Backache (finding)";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/problems/961237",
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
        "Code",
        "spcode__SNOMED"
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
'>


encounters
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#encounters</span>
<br />
<span style='font-size: small'><a href='#Encounter'>Encounter</a></span>
<br><br>Encounters at which this problem has been observed.
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
Date on which problem resolve (if any), as an ISO-8601 string. <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#SNOMED_code'>SNOMED</a></span>
<br><br>SNOMED-CT Concept for the problem
</td>
</tr>

<tr><td style='width: 30%;
'>


problemStatus
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#problemStatus</span>
<br />
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#ProblemStatus_code'>ProblemStatus</a></span>
<br><br>Status of this problem, using a SNOMED code for Active, Inactive, or Resolved.
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
Date on which problem began, as an ISO-8601 string. <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

</table>

<h2 id='Procedure'><code>Procedure</code></h2>

`Procedure` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


The SMART Procedure model describes a procedure that has been performed on a patient.  Examples include surgical procedures (such as an appendectomy) and physical exam procedures (such as a diabetic foot exam).  More broadly, the SMART procedure model is used to capture events under SNOMED CT's Procedure hierarchy. 

<div id='Procedure_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Procedure_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Procedure_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Procedure_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Procedure_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"
  xmlns:v="http://www.w3.org/2006/vcard/ns#">
 <sp:Procedure  rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235">
    <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
    <dcterms:date>2011-02-15</dcterms:date>
    <sp:procedureName>
      <sp:CodedValue>
          <dcterms:title></dcterms:title>
          <sp:code>
            <spcode:Procedure rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/80146002">
              <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
              <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
              <dcterms:identifier>80146002</dcterms:identifier>
              <dcterms:title>Appendectomy</dcterms:title>
            </spcode:Procedure>    
          </sp:code>
      </sp:CodedValue>
    </sp:procedureName>
    <sp:provider>
      <sp:Provider>
        <v:n>
          <v:Name>
           <v:given-name>Joshua</v:given-name>
           <v:family-name>Mandel</v:family-name>
          </v:Name>
        </v:n>
      </sp:Provider>
    </sp:provider>
 </sp:Procedure>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
<http://purl.bioontology.org/ontology/SNOMEDCT/80146002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/80146002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/Procedure> .
<http://purl.bioontology.org/ontology/SNOMEDCT/80146002> <http://purl.org/dc/terms/identifier> "80146002" .
<http://purl.bioontology.org/ontology/SNOMEDCT/80146002> <http://purl.org/dc/terms/title> "Appendectomy" .
<http://purl.bioontology.org/ontology/SNOMEDCT/80146002> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
_:_a36dc942-9b14-4c95-b0ea-c0a9e99e929a <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .
_:_a36dc942-9b14-4c95-b0ea-c0a9e99e929a <http://www.w3.org/2006/vcard/ns#given-name> "Joshua" .
_:_a36dc942-9b14-4c95-b0ea-c0a9e99e929a <http://www.w3.org/2006/vcard/ns#family-name> "Mandel" .
_:_1729b2b9-618f-4135-97b6-0156960ebdad <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_1729b2b9-618f-4135-97b6-0156960ebdad <http://purl.org/dc/terms/title> "" .
_:_1729b2b9-618f-4135-97b6-0156960ebdad <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/80146002> .
_:_92a183c1-2147-4590-bb2c-37f7bca7a164 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Provider> .
_:_92a183c1-2147-4590-bb2c-37f7bca7a164 <http://www.w3.org/2006/vcard/ns#n> _:_a36dc942-9b14-4c95-b0ea-c0a9e99e929a .
<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Procedure> .
<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> <http://smartplatforms.org/terms#procedureName> _:_1729b2b9-618f-4135-97b6-0156960ebdad .
<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> <http://smartplatforms.org/terms#provider> _:_92a183c1-2147-4590-bb2c-37f7bca7a164 .
<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> <http://purl.org/dc/terms/date> "2011-02-15" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> a sp:Procedure;
    dcterms:date "2011-02-15";
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:procedureName [ a sp:CodedValue;
            dcterms:title "";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/80146002> ];
    sp:provider [ a sp:Provider;
            vcard:n [ a vcard:Name;
                    vcard:family-name "Mandel";
                    vcard:given-name "Joshua" ] ] .

<http://purl.bioontology.org/ontology/SNOMEDCT/80146002> a sp:Code,
        spcode:Procedure;
    dcterms:identifier "80146002";
    dcterms:title "Appendectomy";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/80146002",
      "@type": [
        "Code",
        "spcode__Procedure"
      ],
      "dcterms__identifier": "80146002",
      "dcterms__title": "Appendectomy",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    },
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235",
      "@type": "Procedure",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "dcterms__date": "2011-02-15",
      "procedureName": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/80146002"
        },
        "dcterms__title": ""
      },
      "provider": {
        "@type": "Provider",
        "vcard__n": {
          "@type": "vcard__Name",
          "vcard__family_name": "Mandel",
          "vcard__given_name": "Joshua"
        }
      }
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Procedure</caption>
<tbody>
<tr><td style='width: 30%;
'>


date
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/date</span>
<br />
When the proceduere was performed, encoded as an ISO-8601 string. <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
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
Free-text notes about this procedure. <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


procedureName
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#procedureName</span>
<br />
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#Procedure_code'>Procedure</a></span>
<br><br>SNOMED CT concept ID (under the procedure hierarchy) for this procedure.  Code element with code drawn from http://purl.bioontology.org/ontology/SNOMEDCT/{cui}
</td>
</tr>

<tr><td style='width: 30%;
'>


procedureStatus
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#procedureStatus</span>
<br />
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#ProcedureStatus_code'>ProcedureStatus</a></span>
<br><br>Status of procedure.  (Active, complete, cancelled, aborted).
</td>
</tr>

<tr><td style='width: 30%;
'>


provider
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#provider</span>
<br />
<span style='font-size: small'><a href='#Provider'>Provider</a></span>
<br><br>Provider responsible for the procedure.
</td>
</tr>

</table>

<h2 id='SMART_Statement'><code>SMART Statement</code></h2>


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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

</table>

<h2 id='Social_History'><code>Social History</code></h2>

`Social History` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


The SMART Social History model describes smoking status accoring to Meaningful Use classifications.  This mode is expected to expand over time to accomodate additional aspects of the social history.

<div id='Social_History_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Social_History_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Social_History_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Social_History_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Social_History_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"> 
    <sp:SocialHistory  rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/social_history">
      <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
      <sp:smokingStatus>
      <sp:CodedValue>
          <dcterms:title>Former smoker)</dcterms:title>      
          <sp:code>
            <spcode:SmokingStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/8517006">
              <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
              <dcterms:title>Former smoker</dcterms:title>      
              <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
              <dcterms:identifier>8517006</dcterms:identifier> 
            </spcode:SmokingStatus>
          </sp:code>
      </sp:CodedValue>
      </sp:smokingStatus>
    </sp:SocialHistory>
</rdf:RDF>

{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
<http://sandbox-api.smartplatforms.org/records/2169591/social_history> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#SocialHistory> .
<http://sandbox-api.smartplatforms.org/records/2169591/social_history> <http://smartplatforms.org/terms#smokingStatus> _:_90943590-a505-4063-accc-87cef6be16cd .
<http://sandbox-api.smartplatforms.org/records/2169591/social_history> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://purl.bioontology.org/ontology/SNOMEDCT/8517006> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/8517006> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/8517006> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/SmokingStatus> .
<http://purl.bioontology.org/ontology/SNOMEDCT/8517006> <http://purl.org/dc/terms/title> "Former smoker" .
<http://purl.bioontology.org/ontology/SNOMEDCT/8517006> <http://purl.org/dc/terms/identifier> "8517006" .
_:_90943590-a505-4063-accc-87cef6be16cd <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_90943590-a505-4063-accc-87cef6be16cd <http://purl.org/dc/terms/title> "Former smoker)" .
_:_90943590-a505-4063-accc-87cef6be16cd <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/8517006> .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://sandbox-api.smartplatforms.org/records/2169591/social_history> a sp:SocialHistory;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:smokingStatus [ a sp:CodedValue;
            dcterms:title "Former smoker)";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/8517006> ] .

<http://purl.bioontology.org/ontology/SNOMEDCT/8517006> a sp:Code,
        spcode:SmokingStatus;
    dcterms:identifier "8517006";
    dcterms:title "Former smoker";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/social_history",
      "@type": "SocialHistory",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "smokingStatus": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/8517006"
        },
        "dcterms__title": "Former smoker)"
      }
    },
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/8517006",
      "@type": [
        "Code",
        "spcode__SmokingStatus"
      ],
      "dcterms__identifier": "8517006",
      "dcterms__title": "Former smoker",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#SocialHistory</caption>
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
</td>
</tr>

<tr><td style='width: 30%;
'>


smokingStatus
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#smokingStatus</span>
<br />
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a></span>
<br><br>A patient's smoking status according the Meaningful Use classification.  This must be one of six prespecified LOINC codes: 

449868002
230059006
8517006
266919005
266927001
405746006


</td>
</tr>

</table>

<h2 id='Vital_Sign_Set'><code>Vital Sign Set</code></h2>

`Vital Sign Set` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


<div id='Vital_Sign_Set_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Vital_Sign_Set_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Vital_Sign_Set_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Vital_Sign_Set_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Vital_Sign_Set_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
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

  <sp:VitalSignSet rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523">
    <sp:belongsTo  rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
    <dcterms:date>2010-05-12T04:00:00Z</dcterms:date>
    <sp:encounter>
      <sp:Encounter rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352">
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
    <sp:headCircumference>
      <sp:VitalSign>
        <sp:vitalName>
          <sp:CodedValue>
            <dcterms:title>Head circumference</dcterms:title>
            <sp:code>
              <spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8287-5">
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Head circumference</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
                <dcterms:identifier>8287-5</dcterms:identifier> 
              </spcode:VitalSign>
            </sp:code>
          </sp:CodedValue>
        </sp:vitalName>
        <sp:value>70</sp:value>
        <sp:unit>{beats}/min</sp:unit>
      </sp:VitalSign>
    </sp:headCircumference>
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
  </sp:VitalSignSet>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://purl.org/dc/terms/identifier> "8310-5" .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://purl.org/dc/terms/title> "Body temperature" .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://purl.org/dc/terms/identifier> "3141-9" .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://purl.org/dc/terms/title> "Body weight" .
_:_d8823996-d52a-4551-8316-727008ba6461 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_d8823996-d52a-4551-8316-727008ba6461 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/9279-1> .
_:_d8823996-d52a-4551-8316-727008ba6461 <http://purl.org/dc/terms/title> "Respiration rate" .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://purl.org/dc/terms/identifier> "39156-5" .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://purl.org/dc/terms/title> "Body mass index" .
_:_b3495535-18c5-4960-b435-3f61db996c46 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_b3495535-18c5-4960-b435-3f61db996c46 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/EncounterType#ambulatory> .
_:_b3495535-18c5-4960-b435-3f61db996c46 <http://purl.org/dc/terms/title> "Ambulatory encounter" .
_:_feb989f9-46b2-4ac5-807f-9e6fcc80fea3 <http://smartplatforms.org/terms#vitalName> _:_965b1b4c-baae-4d38-a7e0-394360265a7d .
_:_feb989f9-46b2-4ac5-807f-9e6fcc80fea3 <http://smartplatforms.org/terms#value> "70.8" .
_:_feb989f9-46b2-4ac5-807f-9e6fcc80fea3 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:_feb989f9-46b2-4ac5-807f-9e6fcc80fea3 <http://smartplatforms.org/terms#unit> "kg" .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://purl.org/dc/terms/identifier> "8480-6" .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://purl.org/dc/terms/title> "Intravascular systolic" .
_:_5f0d48ec-d5d7-4c3a-ba1c-33c66b52c53b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_5f0d48ec-d5d7-4c3a-ba1c-33c66b52c53b <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8480-6> .
_:_5f0d48ec-d5d7-4c3a-ba1c-33c66b52c53b <http://purl.org/dc/terms/title> "Intravascular systolic" .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://purl.org/dc/terms/identifier> "33586001" .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/BloodPressureBodyPosition> .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://purl.org/dc/terms/title> "Sitting" .
_:_417586b7-579c-4be7-8d0e-3186ddf6ede1 <http://smartplatforms.org/terms#vitalName> _:_d8823996-d52a-4551-8316-727008ba6461 .
_:_417586b7-579c-4be7-8d0e-3186ddf6ede1 <http://smartplatforms.org/terms#value> "16" .
_:_417586b7-579c-4be7-8d0e-3186ddf6ede1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:_417586b7-579c-4be7-8d0e-3186ddf6ede1 <http://smartplatforms.org/terms#unit> "{breaths}/min" .
<http://purl.bioontology.org/ontology/LNC/8287-5> <http://purl.org/dc/terms/identifier> "8287-5" .
<http://purl.bioontology.org/ontology/LNC/8287-5> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8287-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8287-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8287-5> <http://purl.org/dc/terms/title> "Head circumference" .
_:_42e25de9-2a13-475a-a494-c0b7c41ab4f5 <http://smartplatforms.org/terms#vitalName> _:_5f0d48ec-d5d7-4c3a-ba1c-33c66b52c53b .
_:_42e25de9-2a13-475a-a494-c0b7c41ab4f5 <http://smartplatforms.org/terms#value> "132" .
_:_42e25de9-2a13-475a-a494-c0b7c41ab4f5 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:_42e25de9-2a13-475a-a494-c0b7c41ab4f5 <http://smartplatforms.org/terms#unit> "mm[Hg]" .
_:_668c7876-4d94-4433-9303-e66f58e6d49b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_668c7876-4d94-4433-9303-e66f58e6d49b <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8867-4> .
_:_668c7876-4d94-4433-9303-e66f58e6d49b <http://purl.org/dc/terms/title> "Heart rate" .
_:_fa2019f2-f536-46fe-9943-6b88ce784886 <http://smartplatforms.org/terms#vitalName> _:_cea753ab-631d-4998-94c4-af781228384f .
_:_fa2019f2-f536-46fe-9943-6b88ce784886 <http://smartplatforms.org/terms#value> "99" .
_:_fa2019f2-f536-46fe-9943-6b88ce784886 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:_fa2019f2-f536-46fe-9943-6b88ce784886 <http://smartplatforms.org/terms#unit> "%{HemoglobinSaturation}" .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://purl.org/dc/terms/identifier> "8462-4" .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://purl.org/dc/terms/title> "Intravascular diastolic" .
_:_4a7f72c8-c89a-4a1a-bb6a-006a0b71ef3b <http://smartplatforms.org/terms#vitalName> _:_54d818eb-3f30-4f0e-9999-8a2744f0c7a1 .
_:_4a7f72c8-c89a-4a1a-bb6a-006a0b71ef3b <http://smartplatforms.org/terms#value> "70" .
_:_4a7f72c8-c89a-4a1a-bb6a-006a0b71ef3b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:_4a7f72c8-c89a-4a1a-bb6a-006a0b71ef3b <http://smartplatforms.org/terms#unit> "{beats}/min" .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#heartRate> _:_0f5b1f35-65c4-4fe1-a67e-8a67667babb3 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#headCircumference> _:_4a7f72c8-c89a-4a1a-bb6a-006a0b71ef3b .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#bloodPressure> _:_d5b7139b-370d-4b9e-ae6e-6c4dfec1deac .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#weight> _:_feb989f9-46b2-4ac5-807f-9e6fcc80fea3 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#bodyMassIndex> _:_ac6a5370-de86-45e8-9af3-d0cdb3954360 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#temperature> _:_47d95e3a-73ad-49e3-bec5-0c0c1f31f922 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#oxygenSaturation> _:_fa2019f2-f536-46fe-9943-6b88ce784886 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://purl.org/dc/terms/date> "2010-05-12T04:00:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#respiratoryRate> _:_417586b7-579c-4be7-8d0e-3186ddf6ede1 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#height> _:_59a561a7-bb8c-480e-b79a-d7d0b5980d63 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#encounter> <http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSignSet> .
_:_c8aa9c53-5be1-4245-8231-7fdfb9a2d7d4 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_c8aa9c53-5be1-4245-8231-7fdfb9a2d7d4 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/368209003> .
_:_c8aa9c53-5be1-4245-8231-7fdfb9a2d7d4 <http://purl.org/dc/terms/title> "Right arm" .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://purl.org/dc/terms/identifier> "8867-4" .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://purl.org/dc/terms/title> "Heart rate" .
_:_965b1b4c-baae-4d38-a7e0-394360265a7d <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_965b1b4c-baae-4d38-a7e0-394360265a7d <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/3141-9> .
_:_965b1b4c-baae-4d38-a7e0-394360265a7d <http://purl.org/dc/terms/title> "Body weight" .
_:_ac58c165-0f28-4666-a81f-2bd3eed7f5e5 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_ac58c165-0f28-4666-a81f-2bd3eed7f5e5 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/39156-5> .
_:_ac58c165-0f28-4666-a81f-2bd3eed7f5e5 <http://purl.org/dc/terms/title> "Body mass index" .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://purl.org/dc/terms/identifier> "2710-2" .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://purl.org/dc/terms/title> "Oxygen saturation" .
_:_0f5b1f35-65c4-4fe1-a67e-8a67667babb3 <http://smartplatforms.org/terms#vitalName> _:_668c7876-4d94-4433-9303-e66f58e6d49b .
_:_0f5b1f35-65c4-4fe1-a67e-8a67667babb3 <http://smartplatforms.org/terms#value> "70" .
_:_0f5b1f35-65c4-4fe1-a67e-8a67667babb3 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:_0f5b1f35-65c4-4fe1-a67e-8a67667babb3 <http://smartplatforms.org/terms#unit> "{beats}/min" .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#encounterType> _:_b3495535-18c5-4960-b435-3f61db996c46 .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Encounter> .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#endDate> "2010-05-12T04:20:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#startDate> "2010-05-12T04:00:00Z" .
_:_d5b7139b-370d-4b9e-ae6e-6c4dfec1deac <http://smartplatforms.org/terms#bodyPosition> _:_e9ca4148-aeda-48e2-8ee8-9cdfa30c9736 .
_:_d5b7139b-370d-4b9e-ae6e-6c4dfec1deac <http://smartplatforms.org/terms#diastolic> _:_5ac67d69-08e0-4556-8d16-73085afe6bcf .
_:_d5b7139b-370d-4b9e-ae6e-6c4dfec1deac <http://smartplatforms.org/terms#bodySite> _:_c8aa9c53-5be1-4245-8231-7fdfb9a2d7d4 .
_:_d5b7139b-370d-4b9e-ae6e-6c4dfec1deac <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#BloodPressure> .
_:_d5b7139b-370d-4b9e-ae6e-6c4dfec1deac <http://smartplatforms.org/terms#systolic> _:_42e25de9-2a13-475a-a494-c0b7c41ab4f5 .
_:_54d818eb-3f30-4f0e-9999-8a2744f0c7a1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_54d818eb-3f30-4f0e-9999-8a2744f0c7a1 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8287-5> .
_:_54d818eb-3f30-4f0e-9999-8a2744f0c7a1 <http://purl.org/dc/terms/title> "Head circumference" .
_:_47d95e3a-73ad-49e3-bec5-0c0c1f31f922 <http://smartplatforms.org/terms#vitalName> _:_bc0f6c9b-7751-43f4-8a35-b3c77cf7e0ef .
_:_47d95e3a-73ad-49e3-bec5-0c0c1f31f922 <http://smartplatforms.org/terms#value> "37" .
_:_47d95e3a-73ad-49e3-bec5-0c0c1f31f922 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:_47d95e3a-73ad-49e3-bec5-0c0c1f31f922 <http://smartplatforms.org/terms#unit> "Cel" .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://purl.org/dc/terms/identifier> "8302-2" .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://purl.org/dc/terms/title> "Body height" .
_:_e9ca4148-aeda-48e2-8ee8-9cdfa30c9736 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_e9ca4148-aeda-48e2-8ee8-9cdfa30c9736 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/33586001> .
_:_e9ca4148-aeda-48e2-8ee8-9cdfa30c9736 <http://purl.org/dc/terms/title> "Sitting" .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://purl.org/dc/terms/identifier> "368209003" .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/BloodPressureBodySite> .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://purl.org/dc/terms/title> "Right arm" .
_:_5ac67d69-08e0-4556-8d16-73085afe6bcf <http://smartplatforms.org/terms#vitalName> _:_5e332837-2131-46be-a423-0ac029b86e65 .
_:_5ac67d69-08e0-4556-8d16-73085afe6bcf <http://smartplatforms.org/terms#value> "82" .
_:_5ac67d69-08e0-4556-8d16-73085afe6bcf <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:_5ac67d69-08e0-4556-8d16-73085afe6bcf <http://smartplatforms.org/terms#unit> "mm[Hg]" .
_:_bc0f6c9b-7751-43f4-8a35-b3c77cf7e0ef <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_bc0f6c9b-7751-43f4-8a35-b3c77cf7e0ef <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8310-5> .
_:_bc0f6c9b-7751-43f4-8a35-b3c77cf7e0ef <http://purl.org/dc/terms/title> "Body temperature" .
_:_5e332837-2131-46be-a423-0ac029b86e65 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_5e332837-2131-46be-a423-0ac029b86e65 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8462-4> .
_:_5e332837-2131-46be-a423-0ac029b86e65 <http://purl.org/dc/terms/title> "Intravascular diastolic" .
_:_2a2f120e-2c0d-4dd0-a076-0d1461e66039 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_2a2f120e-2c0d-4dd0-a076-0d1461e66039 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8302-2> .
_:_2a2f120e-2c0d-4dd0-a076-0d1461e66039 <http://purl.org/dc/terms/title> "Body height" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/identifier> "ambulatory" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/EncounterType#" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/EncounterType> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/title> "Ambulatory encounter" .
_:_59a561a7-bb8c-480e-b79a-d7d0b5980d63 <http://smartplatforms.org/terms#vitalName> _:_2a2f120e-2c0d-4dd0-a076-0d1461e66039 .
_:_59a561a7-bb8c-480e-b79a-d7d0b5980d63 <http://smartplatforms.org/terms#value> "1.80" .
_:_59a561a7-bb8c-480e-b79a-d7d0b5980d63 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:_59a561a7-bb8c-480e-b79a-d7d0b5980d63 <http://smartplatforms.org/terms#unit> "m" .
_:_cea753ab-631d-4998-94c4-af781228384f <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:_cea753ab-631d-4998-94c4-af781228384f <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/2710-2> .
_:_cea753ab-631d-4998-94c4-af781228384f <http://purl.org/dc/terms/title> "Oxygen saturation" .
_:_ac6a5370-de86-45e8-9af3-d0cdb3954360 <http://smartplatforms.org/terms#vitalName> _:_ac58c165-0f28-4666-a81f-2bd3eed7f5e5 .
_:_ac6a5370-de86-45e8-9af3-d0cdb3954360 <http://smartplatforms.org/terms#value> "21.8" .
_:_ac6a5370-de86-45e8-9af3-d0cdb3954360 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:_ac6a5370-de86-45e8-9af3-d0cdb3954360 <http://smartplatforms.org/terms#unit> "kg/m2" .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://purl.org/dc/terms/identifier> "9279-1" .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://purl.org/dc/terms/title> "Respiration rate" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> a sp:VitalSignSet;
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
    sp:encounter <http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352>;
    sp:headCircumference [ a sp:VitalSign;
            sp:unit "{beats}/min";
            sp:value "70";
            sp:vitalName [ a sp:CodedValue;
                    dcterms:title "Head circumference";
                    sp:code <http://purl.bioontology.org/ontology/LNC/8287-5> ] ];
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

<http://purl.bioontology.org/ontology/LNC/8287-5> a sp:Code,
        spcode:VitalSign;
    dcterms:identifier "8287-5";
    dcterms:title "Head circumference";
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

<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> a sp:Encounter;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:encounterType [ a sp:CodedValue;
            dcterms:title "Ambulatory encounter";
            sp:code <http://smartplatforms.org/terms/codes/EncounterType#ambulatory> ];
    sp:endDate "2010-05-12T04:20:00Z";
    sp:startDate "2010-05-12T04:00:00Z" .

<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> a sp:Code,
        spcode:EncounterType;
    dcterms:identifier "ambulatory";
    dcterms:title "Ambulatory encounter";
    sp:system "http://smartplatforms.org/terms/codes/EncounterType#" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
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
      "@id": "http://purl.bioontology.org/ontology/LNC/8287-5",
      "@type": [
        "spcode__VitalSign",
        "Code"
      ],
      "dcterms__identifier": "8287-5",
      "dcterms__title": "Head circumference",
      "system": "http://purl.bioontology.org/ontology/LNC/"
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
      "@id": "http://purl.bioontology.org/ontology/LNC/8462-4",
      "@type": [
        "spcode__VitalSign",
        "Code"
      ],
      "dcterms__identifier": "8462-4",
      "dcterms__title": "Intravascular diastolic",
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
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523",
      "@type": "VitalSignSet",
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
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352"
      },
      "headCircumference": {
        "@type": "VitalSign",
        "unit": "{beats}/min",
        "value": "70",
        "vitalName": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/LNC/8287-5"
          },
          "dcterms__title": "Head circumference"
        }
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
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352",
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
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/33586001",
      "@type": [
        "spcode__BloodPressureBodyPosition",
        "Code"
      ],
      "dcterms__identifier": "33586001",
      "dcterms__title": "Sitting",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#VitalSignSet</caption>
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
Date + time when vital signs were recorded, as an ISO-8601 string. <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
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
<span style='font-size: small'><a href='#Medical_Record'>Medical Record</a></span>
<br><br>The medical record URI to which a clinical statement belongs.  Each clinical statement points back to its medical record so that it can be treated in isolation.
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
<span style='font-size: small'><a href='#BloodPressure'>BloodPressure</a></span>
<br><br>Patient's systolic + diastolic Blood Pressure in mmHg, with optional position coding
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
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: kg/m2</span>
<br><br>Patient's Body Mass Index.  
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
<span style='font-size: small'><a href='#Encounter'>Encounter</a></span>
<br><br>Encounter at which vital signs were measured. This should specify a date and encounter type, at minimum.
</td>
</tr>

<tr><td style='width: 30%;
'>


headCircumference
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#headCircumference</span>
<br />
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: cm</span>
<br><br>
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
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: {beats}/min</span>
<br><br>Patient's Heart Rate per minute. 
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
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: m</span>
<br><br>Patient's height in meters.  
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
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: %{HemoglobinSaturation}</span>
<br><br>Patient's oxygen saturation in percent.  
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
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: {breaths}/min</span>
<br><br>Patient's Respiratory Rate per minute. 
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
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: Cel</span>
<br><br>Patient's Temperature in Celcius. 
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
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: kg</span>
<br><br>Patient's weight in kg. 
</td>
</tr>

</table>

# Component Types


<h2 id='Address'><code>Address</code></h2>

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

<h2 id='Attribution'><code>Attribution</code></h2>

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
<span style='font-size: small'><a href='#Participant'>Participant</a></span>
<br><br>Participant in Attribution
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

<h2 id='BloodPressure'><code>BloodPressure</code></h2>

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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#BloodPressureBodyPosition_code'>BloodPressureBodyPosition</a></span>
<br><br>Position of patient when blood pressure was recorded
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#BloodPressureBodySite_code'>BloodPressureBodySite</a></span>
<br><br>Site on patient's body where blood pressure was recorded
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
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: mm[Hg]</span>
<br><br>diastolic blood pressure in mmHG. 
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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#BloodPressureMethod_code'>BloodPressureMethod</a></span>
<br><br>Method by which blood pressure was recorded.
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
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: mm[Hg]</span>
<br><br>systolic blood pressure in mmHG.
</td>
</tr>

</table>

<h2 id='Code'><code>Code</code></h2>

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

<h2 id='CodeProvenance'><code>CodeProvenance</code></h2>

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
<span style='font-size: small'><a href='#TranslationFidelity_code'>TranslationFidelity code</a></span>
<br><br>
</td>
</tr>

</table>

<h2 id='Coded_Value'><code>Coded Value</code></h2>

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
<span style='font-size: small'><a href='#Code'>Code</a></span>
<br><br>
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
<span style='font-size: small'><a href='#CodeProvenance'>CodeProvenance</a></span>
<br><br>
</td>
</tr>

</table>

<h2 id='DataType'><code>DataType</code></h2>

`DataType` is a subtype of and inherits properties from:
[Component](#Component)



<h2 id='DocumentWithFormat'><code>DocumentWithFormat</code></h2>

`DocumentWithFormat` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#DocumentWithFormat</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


format
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/format</span>
<br />
<span style='font-size: small'><a href='#MediaTypeOrExtent'>MediaTypeOrExtent</a></span>
<br><br>MIME type of the note, as a URI node of the form: http://purl.org/NET/mediatypes/{type}/{subtype}

Examples include:  
  http://purl.org/NET/mediatypes/text/plain
  http://purl.org/NET/mediatypes/text/html
  http://purl.org/NET/mediatypes/application/pdf

</td>
</tr>

<tr><td style='width: 30%;
'>


value
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/1999/02/22-rdf-syntax-ns#value</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

<h2 id='MediaTypeOrExtent'><code>MediaTypeOrExtent</code></h2>

`MediaTypeOrExtent` is a subtype of and inherits properties from:
[Component](#Component), [DataType](#DataType)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://purl.org/dc/terms/title#MediaTypeOrExtent</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


label
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2000/01/rdf-schema#label</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

</table>

<h2 id='Name'><code>Name</code></h2>

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

<h2 id='NarrativeResult'><code>NarrativeResult</code></h2>

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

<h2 id='Organization'><code>Organization</code></h2>

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
<span style='font-size: small'><a href='#Address'>Address</a></span>
<br><br>
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

<h2 id='Participant'><code>Participant</code></h2>

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
<span style='font-size: small'><a href='#Organization'>Organization</a></span>
<br><br>Organization of participant
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
<span style='font-size: small'><a href='#Person'>Person</a></span>
<br><br>Person who participated
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

<h2 id='Person'><code>Person</code></h2>

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
<span style='font-size: small'><a href='#Address'>Address</a></span>
<br><br>
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
Birthday as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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
<span style='font-size: small'><a href='#Name'>Name</a></span>
<br><br>
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
<span style='font-size: small'><a href='#Tel'>Tel</a></span>
<br><br>
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

<h2 id='Pharmacy'><code>Pharmacy</code></h2>

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
<span style='font-size: small'><a href='#Address'>Address</a></span>
<br><br>
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

<h2 id='Provider'><code>Provider</code></h2>

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
<span style='font-size: small'><a href='#Address'>Address</a></span>
<br><br>
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
Birthday as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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
<span style='font-size: small'><a href='#Name'>Name</a></span>
<br><br>
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
<span style='font-size: small'><a href='#Tel'>Tel</a></span>
<br><br>
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

<h2 id='QuantitativeResult'><code>QuantitativeResult</code></h2>

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
<span style='font-size: small'><a href='#ValueRange'>ValueRange</a></span>
<br><br>Non-critical range for result.  (Results outside this range are considered "critical.")
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
<span style='font-size: small'><a href='#ValueRange'>ValueRange</a></span>
<br><br>Normal range for result. (Results outside this range are considered "abnormal".)
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
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a></span>
<br><br>Value and unit
</td>
</tr>

</table>

<h2 id='Tel'><code>Tel</code></h2>

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

<h2 id='VCard'><code>VCard</code></h2>

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
<span style='font-size: small'><a href='#Address'>Address</a></span>
<br><br>
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
Birthday as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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
<span style='font-size: small'><a href='#Name'>Name</a></span>
<br><br>
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
<span style='font-size: small'><a href='#Tel'>Tel</a></span>
<br><br>
</td>
</tr>

</table>

<h2 id='ValueAndUnit'><code>ValueAndUnit</code></h2>

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

<h2 id='ValueRange'><code>ValueRange</code></h2>

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
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a></span>
<br><br>Maximum value in range (not inclusive)
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
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a></span>
<br><br>Minimum value in range (inclusive)
</td>
</tr>

</table>

<h2 id='ValueRatio'><code>ValueRatio</code></h2>

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
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a></span>
<br><br>Denominator of the ratio.
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
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a></span>
<br><br>Numerator of the ratio.
</td>
</tr>

</table>

<h2 id='VitalSign'><code>VitalSign</code></h2>

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
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#VitalSign_code'>VitalSign</a></span>
<br><br>LOINC Coded Value for the vital sign type
</td>
</tr>

</table>

# Container-level Types


<h2 id='App_Manifest'><code>App Manifest</code></h2>


<h2 id='ContainerManifest'><code>ContainerManifest</code></h2>

A SMART Container exposes a manifest describing its properties and capabilities as a JSON structure.  The example below is for a container that provides Demographics, Encounters, and Vital Signs only.

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
        "http://smartplatforms.org/terms#VitalSignSet": {
            "methods": [
                "GET"
            ]
        }
    }
}

{% endhighlight %}</div>


<h2 id='Ontology'><code>Ontology</code></h2>

An OWL ontology representing SMART data types + API calls

<div class='rdf_xml active'>{% highlight xml %}
See: http://sandbox-api.smartplatforms.org/ontology
{% endhighlight %}</div>


<h2 id='User'><code>User</code></h2>

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
<span style='font-size: small'><a href='#Address'>Address</a></span>
<br><br>
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
Birthday as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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
<span style='font-size: small'><a href='#Name'>Name</a></span>
<br><br>
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
<span style='font-size: small'><a href='#Tel'>Tel</a></span>
<br><br>
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

<h2 id='User_Preferences'><code>User Preferences</code></h2>


# Data code Types


<h2 id='AllergyCategory_code'><code>AllergyCategory code</code></h2>

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

<h2 id='AllergyExclusion_code'><code>AllergyExclusion code</code></h2>

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

<h2 id='AllergySeverity_code'><code>AllergySeverity code</code></h2>

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

<h2 id='BloodPressureBodyPosition_code'><code>BloodPressureBodyPosition code</code></h2>

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

<h2 id='BloodPressureBodySite_code'><code>BloodPressureBodySite code</code></h2>

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

<h2 id='BloodPressureMethod_code'><code>BloodPressureMethod code</code></h2>

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

<h2 id='EncounterType_code'><code>EncounterType code</code></h2>

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

<h2 id='ImmunizationAdministrationStatus_code'><code>ImmunizationAdministrationStatus code</code></h2>

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

<h2 id='ImmunizationClass_code'><code>ImmunizationClass code</code></h2>

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

<h2 id='ImmunizationProduct_code'><code>ImmunizationProduct code</code></h2>

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

<h2 id='ImmunizationRefusalReason_code'><code>ImmunizationRefusalReason code</code></h2>

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

<h2 id='LOINC_code'><code>LOINC code</code></h2>

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

<h2 id='LabResultInterpretation_code'><code>LabResultInterpretation code</code></h2>

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

<h2 id='LabResultStatus_code'><code>LabResultStatus code</code></h2>

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

<h2 id='MedicalRecordNumber_code'><code>MedicalRecordNumber code</code></h2>

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

<h2 id='NDFRT_code'><code>NDFRT code</code></h2>

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

<h2 id='ProblemStatus_code'><code>ProblemStatus code</code></h2>

`ProblemStatus` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [SNOMED](#SNOMED)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/ProblemStatus</caption>
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

<h2 id='Procedure_code'><code>Procedure code</code></h2>

`Procedure` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [SNOMED](#SNOMED)


SNOMED Concept from the Procedure hierarchy


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/Procedure</caption>
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

<h2 id='ProcedureStatus_code'><code>ProcedureStatus code</code></h2>

`ProcedureStatus` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [SNOMED](#SNOMED)


Constrained to one of: 
 {% highlight xml %}


<spcode:ProcedureStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/385657008">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Aborted</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>385657008</dcterms:identifier>
</spcode:ProcedureStatus>



<spcode:ProcedureStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/89925002">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Cancelled</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>89925002</dcterms:identifier>
</spcode:ProcedureStatus>



<spcode:ProcedureStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/410523001">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Active</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>410523001</dcterms:identifier>
</spcode:ProcedureStatus>



<spcode:ProcedureStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/385658003">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Complete</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>385658003</dcterms:identifier>
</spcode:ProcedureStatus>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/ProcedureStatus</caption>
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

<h2 id='RxNorm_code'><code>RxNorm code</code></h2>

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

<h2 id='RxNorm_Ingredient_code'><code>RxNorm_Ingredient code</code></h2>

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

<h2 id='RxNorm_Semantic_code'><code>RxNorm_Semantic code</code></h2>

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

<h2 id='SNOMED_code'><code>SNOMED code</code></h2>

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

<h2 id='SmokingStatus_code'><code>SmokingStatus code</code></h2>

`SmokingStatus` is a subtype of and inherits properties from:
[Code](#Code), [Component](#Component), [DataType](#DataType), [SNOMED](#SNOMED)


Constrained to one of: 
 {% highlight xml %}


<spcode:SmokingStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/449868002">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Current every day smoker</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>449868002</dcterms:identifier>
</spcode:SmokingStatus>



<spcode:SmokingStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/266927001">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Smoker, current status unknown</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>266927001</dcterms:identifier>
</spcode:SmokingStatus>



<spcode:SmokingStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/230059006">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Current some day smoker</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>230059006</dcterms:identifier>
</spcode:SmokingStatus>



<spcode:SmokingStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/8517006">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Former smoker</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>8517006</dcterms:identifier>
</spcode:SmokingStatus>



<spcode:SmokingStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/405746006">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Unknown if ever smoked</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>405746006</dcterms:identifier>
</spcode:SmokingStatus>



<spcode:SmokingStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/266919005">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Never smoker</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>266919005</dcterms:identifier>
</spcode:SmokingStatus>

{% endhighlight %}


<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms/codes/SmokingStatus</caption>
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

<h2 id='TranslationFidelity_code'><code>TranslationFidelity code</code></h2>

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

<h2 id='UNII_code'><code>UNII code</code></h2>

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

<h2 id='VitalSign_code'><code>VitalSign code</code></h2>

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
