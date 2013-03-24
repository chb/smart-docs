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

Click here for the list of [Changes to the API and Payloads for the
latest release](/updates/smart_0.5/).


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
      <sp:startDate>2007-06-12</sp:startDate>
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
      <sp:startDate>2007-06-12</sp:startDate>
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
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://smartplatforms.org/terms#allergicReaction> _:N199fa9806c8740e8926e1fd3d5265394 .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://smartplatforms.org/terms#category> _:Nd179bb45bfc1425bacda6a4dec7700dc .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://smartplatforms.org/terms#startDate> "2007-06-12" .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Allergy> .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://smartplatforms.org/terms#drugClassAllergen> _:N5f66eadc43a442c097a2b855dfcf5041 .
<http://sandbox-api.smartplatforms.org/records/2169591/allergies/873252> <http://smartplatforms.org/terms#severity> _:Nb236521838cb45a7886cdc8a2ee38201 .
_:N2644c802637c4cc5902db799fb6a2a85 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N2644c802637c4cc5902db799fb6a2a85 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/416098002> .
_:N2644c802637c4cc5902db799fb6a2a85 <http://purl.org/dc/terms/title> "Drug allergy" .
_:Nb236521838cb45a7886cdc8a2ee38201 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Nb236521838cb45a7886cdc8a2ee38201 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/24484000> .
_:Nb236521838cb45a7886cdc8a2ee38201 <http://purl.org/dc/terms/title> "Severe" .
_:N721cbbfdfdf642fabfa61d0c70c74f21 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N721cbbfdfdf642fabfa61d0c70c74f21 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/RXNORM/2231> .
_:N721cbbfdfdf642fabfa61d0c70c74f21 <http://purl.org/dc/terms/title> "Cephalexin" .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/SNOMED> .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://purl.org/dc/terms/identifier> "39579001" .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://purl.org/dc/terms/title> "Anaphylaxis" .
<http://purl.bioontology.org/ontology/SNOMEDCT/39579001> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/AllergySeverity> .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://purl.org/dc/terms/identifier> "24484000" .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://purl.org/dc/terms/title> "Severe" .
<http://purl.bioontology.org/ontology/SNOMEDCT/24484000> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/AllergyCategory> .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://purl.org/dc/terms/identifier> "416098002" .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://purl.org/dc/terms/title> "Drug allergy" .
<http://purl.bioontology.org/ontology/SNOMEDCT/416098002> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
_:Nf40b09d9f3c14b388cae9b37382cba01 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Nf40b09d9f3c14b388cae9b37382cba01 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/39579001> .
_:Nf40b09d9f3c14b388cae9b37382cba01 <http://purl.org/dc/terms/title> "Anaphylaxis" .
_:N199fa9806c8740e8926e1fd3d5265394 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N199fa9806c8740e8926e1fd3d5265394 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/39579001> .
_:N199fa9806c8740e8926e1fd3d5265394 <http://purl.org/dc/terms/title> "Anaphylaxis" .
_:Nd179bb45bfc1425bacda6a4dec7700dc <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Nd179bb45bfc1425bacda6a4dec7700dc <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/416098002> .
_:Nd179bb45bfc1425bacda6a4dec7700dc <http://purl.org/dc/terms/title> "Drug allergy" .
_:Nf1df6d4dcc004b83956ae62719e0ed7c <http://smartplatforms.org/terms#allergicReaction> _:Nf40b09d9f3c14b388cae9b37382cba01 .
_:Nf1df6d4dcc004b83956ae62719e0ed7c <http://smartplatforms.org/terms#category> _:N2644c802637c4cc5902db799fb6a2a85 .
_:Nf1df6d4dcc004b83956ae62719e0ed7c <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:Nf1df6d4dcc004b83956ae62719e0ed7c <http://smartplatforms.org/terms#startDate> "2007-06-12" .
_:Nf1df6d4dcc004b83956ae62719e0ed7c <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Allergy> .
_:Nf1df6d4dcc004b83956ae62719e0ed7c <http://smartplatforms.org/terms#drugAllergen> _:N721cbbfdfdf642fabfa61d0c70c74f21 .
_:Nf1df6d4dcc004b83956ae62719e0ed7c <http://smartplatforms.org/terms#severity> _:N8f94ce127e0a4faa9bac77cd0b4fd61d .
_:N8f94ce127e0a4faa9bac77cd0b4fd61d <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N8f94ce127e0a4faa9bac77cd0b4fd61d <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/24484000> .
_:N8f94ce127e0a4faa9bac77cd0b4fd61d <http://purl.org/dc/terms/title> "Severe" .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/NDFRT> .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://purl.org/dc/terms/identifier> "N0000175503" .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://purl.org/dc/terms/title> "Sulfonamide Antibacterial" .
<http://purl.bioontology.org/ontology/NDFRT/N0000175503> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/NDFRT/" .
_:N5f66eadc43a442c097a2b855dfcf5041 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N5f66eadc43a442c097a2b855dfcf5041 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/NDFRT/N0000175503> .
_:N5f66eadc43a442c097a2b855dfcf5041 <http://purl.org/dc/terms/title> "Sulfonamide Antibacterial" .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/RxNorm_Ingredient> .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://purl.org/dc/terms/identifier> "2231" .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://purl.org/dc/terms/title> "Cephalexin" .
<http://purl.bioontology.org/ontology/RXNORM/2231> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/RXNORM/" .


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
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/24484000> ];
    sp:startDate "2007-06-12" .

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
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/24484000> ];
    sp:startDate "2007-06-12" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
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
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/39579001",
      "@type": [
        "spcode__SNOMED",
        "Code"
      ],
      "dcterms__identifier": "39579001",
      "dcterms__title": "Anaphylaxis",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/NDFRT/N0000175503",
      "@type": [
        "spcode__NDFRT",
        "Code"
      ],
      "dcterms__identifier": "N0000175503",
      "dcterms__title": "Sulfonamide Antibacterial",
      "system": "http://purl.bioontology.org/ontology/NDFRT/"
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
      },
      "startDate": "2007-06-12"
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
      },
      "startDate": "2007-06-12"
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
font-weight: bold'>


endDate
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#endDate</span>
<br />
Date on which allergy ended as an ISO-8601 string. <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
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
<br><br>Substance acting as a food, environmental, or other allergen.  For environmental and food substance is a UNII.
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

<tr><td style='width: 30%;
font-weight: bold'>


startDate
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#startDate</span>
<br />
Date on which allergy began as an ISO-8601 string. <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

</table>

<h2 id='Allergy_Exclusion'><code>Allergy Exclusion</code></h2>

`Allergy Exclusion` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


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
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://purl.org/dc/terms/title> "No known allergies" .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/AllergyExclusion> .
<http://purl.bioontology.org/ontology/SNOMEDCT/160244002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://sandbox-api.smartplatforms.org/records/2169591/allergy_exclusions/987235> <http://smartplatforms.org/terms#allergyExclusionName> _:N90c8052364824b16a9275499b06553bf .
<http://sandbox-api.smartplatforms.org/records/2169591/allergy_exclusions/987235> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/allergy_exclusions/987235> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#AllergyExclusion> .
_:N90c8052364824b16a9275499b06553bf <http://purl.org/dc/terms/title> "No known allergies" .
_:N90c8052364824b16a9275499b06553bf <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/160244002> .
_:N90c8052364824b16a9275499b06553bf <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .


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


date
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://purl.org/dc/terms/date</span>
<br />
Date when this affirmation was made as an ISO-8601 string. <a href='http://www.w3.org/2001/XMLSchema#dateTime'>xsd:dateTime</a>
</td>
</tr>

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
[Document](#Document), [SMART Statement](#SMART_Statement)


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
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:v="http://www.w3.org/2006/vcard/ns#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"
>
 <sp:ClinicalNote rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335">
    <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
    <dcterms:date>2012-05-17</dcterms:date>
    <dcterms:title>Cardiology clinic follow-up</dcterms:title>
    <dcterms:format>
          <dcterms:MediaTypeOrExtent rdf:about="http://purl.org/NET/mediatypes/text/plain">
                <rdfs:label>text/plain</rdfs:label>
          </dcterms:MediaTypeOrExtent>
     </dcterms:format>
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
    <sp:resource>
        <sp:Resource>
            <sp:content>
                <sp:Content>
                   <encoding>UTF-8</encoding>
                   <value>Patient states recent difficulties with sleeping and concentration due to current problem.</value>
                </sp:Content>
            </sp:content>
        </sp:Resource>
    </sp:resource>
 </sp:ClinicalNote>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
<http://purl.org/NET/mediatypes/text/plain> <http://www.w3.org/2000/01/rdf-schema#label> "text/plain" .
<http://purl.org/NET/mediatypes/text/plain> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.org/dc/terms/MediaTypeOrExtent> .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://purl.org/dc/terms/format> <http://purl.org/NET/mediatypes/text/plain> .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ClinicalNote> .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://purl.org/dc/terms/title> "Cardiology clinic follow-up" .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://purl.org/dc/terms/date> "2012-05-17" .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://smartplatforms.org/terms#resource> _:N4a2f8172b6f94a279a0de7cfb528f34a .
<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> <http://smartplatforms.org/terms#provider> _:N24b65332af574bd0b50571ca810b8819 .
_:N24b65332af574bd0b50571ca810b8819 <http://www.w3.org/2006/vcard/ns#n> _:Na96ed6525a1148e39607f8a5760f0af7 .
_:N24b65332af574bd0b50571ca810b8819 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Provider> .
_:N4a2f8172b6f94a279a0de7cfb528f34a <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Resource> .
_:N4a2f8172b6f94a279a0de7cfb528f34a <http://smartplatforms.org/terms#content> _:N3e7f33df315649438c758808123f37cf .
_:Na96ed6525a1148e39607f8a5760f0af7 <http://www.w3.org/2006/vcard/ns#given-name> "Joshua" .
_:Na96ed6525a1148e39607f8a5760f0af7 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .
_:Na96ed6525a1148e39607f8a5760f0af7 <http://www.w3.org/2006/vcard/ns#family-name> "Mandel" .
_:N3e7f33df315649438c758808123f37cf <encoding> "UTF-8" .
_:N3e7f33df315649438c758808123f37cf <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Content> .
_:N3e7f33df315649438c758808123f37cf <value> "Patient states recent difficulties with sleeping and concentration due to current problem." .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

<http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335> a sp:ClinicalNote;
    dcterms:date "2012-05-17";
    dcterms:format <http://purl.org/NET/mediatypes/text/plain>;
    dcterms:title "Cardiology clinic follow-up";
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:provider [ a sp:Provider;
            vcard:n [ a vcard:Name;
                    vcard:family-name "Mandel";
                    vcard:given-name "Joshua" ] ];
    sp:resource [ a sp:Resource;
            sp:content [ a sp:Content;
                    <encoding> "UTF-8";
                    <value> "Patient states recent difficulties with sleeping and concentration due to current problem." ] ] .

<http://purl.org/NET/mediatypes/text/plain> a dcterms:MediaTypeOrExtent;
    rdfs:label "text/plain" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://purl.org/NET/mediatypes/text/plain",
      "@type": "dcterms__MediaTypeOrExtent",
      "rdfs__label": "text/plain"
    },
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/clinical_notes/827335",
      "@type": "ClinicalNote",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "dcterms__date": "2012-05-17",
      "dcterms__format": {
        "@id": "http://purl.org/NET/mediatypes/text/plain"
      },
      "dcterms__title": "Cardiology clinic follow-up",
      "provider": {
        "@type": "Provider",
        "vcard__n": {
          "@type": "vcard__Name",
          "vcard__family_name": "Mandel",
          "vcard__given_name": "Joshua"
        }
      },
      "resource": [
        {
          "@type": "Resource",
          "content": {
            "@type": "Content",
            "encoding": "UTF-8",
            "value": "Patient states recent difficulties with sleeping and concentration due to current problem."
          }
        }
      ]
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#ClinicalNote</caption>
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
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

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
<br><br>
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
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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


classification
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#classification</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


fileName
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#fileName</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


fileSize
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#fileSize</span>
<br />
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a> where unit has value: byte</span>
<br><br>
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
<br><br>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


resource
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#resource</span>
<br />
<span style='font-size: small'><a href='#Resource'>Resource</a></span>
<br><br>
</td>
</tr>

</table>

<h2 id='Demographics'><code>Demographics</code></h2>

`Demographics` is a subtype of and inherits properties from:
[Component](#Component), [Person](#Person), [SMART Statement](#SMART_Statement), [VCard](#VCard)


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
     <v:deathdate>2012-11-18</v:deathdate>
     <v:email>bob.odenkirk@example.com</v:email>
     
     <sp:ethnicity>Welsh</sp:ethnicity>
     <sp:race>Caucasian</sp:race>
     <sp:preferredLanguage>English</sp:preferredLanguage>

     <sp:gestationalAgeAtBirth>
       <sp:GestationalAgeAtBirth>
         <sp:value>37.6</sp:value>
         <sp:unit>wk</sp:unit>
       </sp:GestationalAgeAtBirth>
     </sp:gestationalAgeAtBirth>
     
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
_:N63c5203b38394b1899c6d5e3546ad460 <http://www.w3.org/2006/vcard/ns#given-name> "Bob" .
_:N63c5203b38394b1899c6d5e3546ad460 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .
_:N63c5203b38394b1899c6d5e3546ad460 <http://www.w3.org/2006/vcard/ns#family-name> "Odenkirk" .
_:N63c5203b38394b1899c6d5e3546ad460 <http://www.w3.org/2006/vcard/ns#additional-name> "J" .
_:N066053c9ff5c4726ad7ec38b46d884ad <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Pref> .
_:N066053c9ff5c4726ad7ec38b46d884ad <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Tel> .
_:N066053c9ff5c4726ad7ec38b46d884ad <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Home> .
_:N066053c9ff5c4726ad7ec38b46d884ad <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "800-555-1212" .
_:N4ad9e59c275548faa8b2da0c789740c5 <http://smartplatforms.org/terms#value> "37.6" .
_:N4ad9e59c275548faa8b2da0c789740c5 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#GestationalAgeAtBirth> .
_:N4ad9e59c275548faa8b2da0c789740c5 <http://smartplatforms.org/terms#unit> "wk" .
_:N26722addf2f245bd8338229b4151a872 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Tel> .
_:N26722addf2f245bd8338229b4151a872 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Cell> .
_:N26722addf2f245bd8338229b4151a872 <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "800-555-1515" .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#adr> _:N94ced203d1514938b05228933fae7558 .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#bday> "1959-12-25" .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#email> "bob.odenkirk@example.com" .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://smartplatforms.org/terms#ethnicity> "Welsh" .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://smartplatforms.org/terms#medicalRecordNumber> _:N5d2b18558bd24e369c388af1910015a6 .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://smartplatforms.org/terms#preferredLanguage> "English" .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Demographics> .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#tel> _:N26722addf2f245bd8338229b4151a872 .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#tel> _:N066053c9ff5c4726ad7ec38b46d884ad .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#deathdate> "2012-11-18" .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://xmlns.com/foaf/0.1/gender> "male" .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://smartplatforms.org/terms#gestationalAgeAtBirth> _:N4ad9e59c275548faa8b2da0c789740c5 .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://www.w3.org/2006/vcard/ns#n> _:N63c5203b38394b1899c6d5e3546ad460 .
<http://sandbox-api.smartplatforms.org/records/2169591/demographics> <http://smartplatforms.org/terms#race> "Caucasian" .
_:N5d2b18558bd24e369c388af1910015a6 <http://purl.org/dc/terms/title> "My Hospital Record 2304575" .
_:N5d2b18558bd24e369c388af1910015a6 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
_:N5d2b18558bd24e369c388af1910015a6 <http://smartplatforms.org/terms#system> "My Hospital Record" .
_:N5d2b18558bd24e369c388af1910015a6 <http://purl.org/dc/terms/identifier> "2304575" .
_:N94ced203d1514938b05228933fae7558 <http://www.w3.org/2006/vcard/ns#country> "USA" .
_:N94ced203d1514938b05228933fae7558 <http://www.w3.org/2006/vcard/ns#region> "OZ" .
_:N94ced203d1514938b05228933fae7558 <http://www.w3.org/2006/vcard/ns#street-address> "15 Main St" .
_:N94ced203d1514938b05228933fae7558 <http://www.w3.org/2006/vcard/ns#postal-code> "54321" .
_:N94ced203d1514938b05228933fae7558 <http://www.w3.org/2006/vcard/ns#locality> "Wonderland" .
_:N94ced203d1514938b05228933fae7558 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Home> .
_:N94ced203d1514938b05228933fae7558 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Pref> .
_:N94ced203d1514938b05228933fae7558 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Address> .
_:N94ced203d1514938b05228933fae7558 <http://www.w3.org/2006/vcard/ns#extended-address> "Apt 2" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

<http://sandbox-api.smartplatforms.org/records/2169591/demographics> a sp:Demographics;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:ethnicity "Welsh";
    sp:gestationalAgeAtBirth [ a sp:GestationalAgeAtBirth;
            sp:unit "wk";
            sp:value "37.6" ];
    sp:medicalRecordNumber [ a sp:Code;
            dcterms:identifier "2304575";
            dcterms:title "My Hospital Record 2304575";
            sp:system "My Hospital Record" ];
    sp:preferredLanguage "English";
    sp:race "Caucasian";
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
    vcard:deathdate "2012-11-18";
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
  "ethnicity": "Welsh",
  "foaf__gender": "male",
  "gestationalAgeAtBirth": {
    "@type": "http://smartplatforms.org/terms#GestationalAgeAtBirth",
    "unit": "wk",
    "value": "37.6"
  },
  "medicalRecordNumber": [
    {
      "@type": "Code",
      "dcterms__identifier": "2304575",
      "dcterms__title": "My Hospital Record 2304575",
      "system": "My Hospital Record"
    }
  ],
  "preferredLanguage": "English",
  "race": "Caucasian",
  "vcard__adr": [
    {
      "@type": [
        "vcard__Home",
        "vcard__Pref",
        "vcard__Address"
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
  "vcard__deathdate": "2012-11-18",
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
        "vcard__Tel",
        "vcard__Cell"
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
'>


gestationalAgeAtBirth
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#gestationalAgeAtBirth</span>
<br />
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a> where unit has value: wk</span>
<br><br>
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
Date of birth as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


deathdate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#deathdate</span>
<br />
Date of death as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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

<h2 id='Document'><code>Document</code></h2>

`Document` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


<div id='Document_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Document_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Document_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Document_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Document_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:v="http://www.w3.org/2006/vcard/ns#"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:dcterms="http://purl.org/dc/terms/"> 
      <sp:Document rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/documents/632678">
      <sp:belongsTo  rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
      <sp:fileName>reportScan.png</sp:fileName>
      <dcterms:title>Image of a report received from NGD about the patient</dcterms:title>
      <dcterms:date>2010-05-12T04:00:00Z</dcterms:date>
      <dcterms:format>
             <dcterms:MediaTypeOrExtent rdf:about="http://purl.org/NET/mediatypes/image/png">
                   <rdfs:label>image/png</rdfs:label>
            </dcterms:MediaTypeOrExtent>
      </dcterms:format>
      <sp:provider>
        <sp:Provider>
          <v:n>
            <v:Name>
             <v:given-name>John</v:given-name>
             <v:family-name>Smith</v:family-name>
            </v:Name>
          </v:n>
        </sp:Provider>
      </sp:provider>
      <sp:fileSize>
        <sp:ValueAndUnit>
          <sp:value>2917</sp:value>
          <sp:unit>byte</sp:unit>
        </sp:ValueAndUnit>
      </sp:fileSize>
      <sp:resource>
        <sp:Resource>
           <sp:location>http://sandbox-api.smartplatforms.org/records/2169591/documents/632678</sp:location>
           <sp:hash>
              <sp:Hash>
                 <sp:algorithm>SHA-256</sp:algorithm>
                 <sp:value>0e7981902c6c410d673771a3dd0a830712c15930bdec77701922138ea950c620</sp:value>
              </sp:Hash>
           </sp:hash>
          <sp:content>
              <sp:Content>
                 <sp:encoding>Base64</sp:encoding>
                 <sp:value>iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAAACXBIWXMAAAsTAAALEwEAmpwYAAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iAlEtvUhUIIFJCi4AUkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCMFVEsDIoK2AfkIaKOg6OIisr74Xuja9a89+bN/rXXPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEKJHAAEAizZCFz/SMBAPh+PDwrIsAHvgABeNMLCADATZvAMByH/w/qQplcAYCEAcB0kThLCIAUAEB6jkKmAEBGAYCdmCZTAKAEAGDLY2LjAFAtAGAnf+bTAICd+Jl7AQBblCEVAaCRACATZYhEAGg7AKzPVopFAFgwABRmS8Q5ANgtADBJV2ZIALC3AMDOEAuyAAgMADBRiIUpAAR7AGDIIyN4AISZABRG8lc88SuuEOcqAAB4mbI8uSQ5RYFbCC1xB1dXLh4ozkkXKxQ2YQJhmkAuwnmZGTKBNA/g88wAAKCRFRHgg/P9eM4Ors7ONo62Dl8t6r8G/yJiYuP+5c+rcEAAAOF0ftH+LC+zGoA7BoBt/qIl7gRoXgugdfeLZrIPQLUAoOnaV/Nw+H48PEWhkLnZ2eXk5NhKxEJbYcpXff5nwl/AV/1s+X48/Pf14L7iJIEyXYFHBPjgwsz0TKUcz5IJhGLc5o9H/LcL//wd0yLESWK5WCoU41EScY5EmozzMqUiiUKSKcUl0v9k4t8s+wM+3zUAsGo+AXuRLahdYwP2SycQWHTA4vcAAPK7b8HUKAgDgGiD4c93/+8//UegJQCAZkmScQAAXkQkLlTKsz/HCAAARKCBKrBBG/TBGCzABhzBBdzBC/xgNoRCJMTCQhBCCmSAHHJgKayCQiiGzbAdKmAv1EAdNMBRaIaTcA4uwlW4Dj1wD/phCJ7BKLyBCQRByAgTYSHaiAFiilgjjggXmYX4IcFIBBKLJCDJiBRRIkuRNUgxUopUIFVIHfI9cgI5h1xGupE7yAAygvyGvEcxlIGyUT3UDLVDuag3GoRGogvQZHQxmo8WoJvQcrQaPYw2oefQq2gP2o8+Q8cwwOgYBzPEbDAuxsNCsTgsCZNjy7EirAyrxhqwVqwDu4n1Y8+xdwQSgUXACTYEd0IgYR5BSFhMWE7YSKggHCQ0EdoJNwkDhFHCJyKTqEu0JroR+cQYYjIxh1hILCPWEo8TLxB7iEPENyQSiUMyJ7mQAkmxpFTSEtJG0m5SI+ksqZs0SBojk8naZGuyBzmULCAryIXkneTD5DPkG+Qh8lsKnWJAcaT4U+IoUspqShnlEOU05QZlmDJBVaOaUt2ooVQRNY9aQq2htlKvUYeoEzR1mjnNgxZJS6WtopXTGmgXaPdpr+h0uhHdlR5Ol9BX0svpR+iX6AP0dwwNhhWDx4hnKBmbGAcYZxl3GK+YTKYZ04sZx1QwNzHrmOeZD5lvVVgqtip8FZHKCpVKlSaVGyovVKmqpqreqgtV81XLVI+pXlN9rkZVM1PjqQnUlqtVqp1Q61MbU2epO6iHqmeob1Q/pH5Z/YkGWcNMw09DpFGgsV/jvMYgC2MZs3gsIWsNq4Z1gTXEJrHN2Xx2KruY/R27iz2qqaE5QzNKM1ezUvOUZj8H45hx+Jx0TgnnKKeX836K3hTvKeIpG6Y0TLkxZVxrqpaXllirSKtRq0frvTau7aedpr1Fu1n7gQ5Bx0onXCdHZ4/OBZ3nU9lT3acKpxZNPTr1ri6qa6UbobtEd79up+6Ynr5egJ5Mb6feeb3n+hx9L/1U/W36p/VHDFgGswwkBtsMzhg8xTVxbzwdL8fb8VFDXcNAQ6VhlWGX4YSRudE8o9VGjUYPjGnGXOMk423GbcajJgYmISZLTepN7ppSTbmmKaY7TDtMx83MzaLN1pk1mz0x1zLnm+eb15vft2BaeFostqi2uGVJsuRaplnutrxuhVo5WaVYVVpds0atna0l1rutu6cRp7lOk06rntZnw7Dxtsm2qbcZsOXYBtuutm22fWFnYhdnt8Wuw+6TvZN9un2N/T0HDYfZDqsdWh1+c7RyFDpWOt6azpzuP33F9JbpL2dYzxDP2DPjthPLKcRpnVOb00dnF2e5c4PziIuJS4LLLpc+Lpsbxt3IveRKdPVxXeF60vWdm7Obwu2o26/uNu5p7ofcn8w0nymeWTNz0MPIQ+BR5dE/C5+VMGvfrH5PQ0+BZ7XnIy9jL5FXrdewt6V3qvdh7xc+9j5yn+M+4zw33jLeWV/MN8C3yLfLT8Nvnl+F30N/I/9k/3r/0QCngCUBZwOJgUGBWwL7+Hp8Ib+OPzrbZfay2e1BjKC5QRVBj4KtguXBrSFoyOyQrSH355jOkc5pDoVQfujW0Adh5mGLw34MJ4WHhVeGP45wiFga0TGXNXfR3ENz30T6RJZE3ptnMU85ry1KNSo+qi5qPNo3ujS6P8YuZlnM1VidWElsSxw5LiquNm5svt/87fOH4p3iC+N7F5gvyF1weaHOwvSFpxapLhIsOpZATIhOOJTwQRAqqBaMJfITdyWOCnnCHcJnIi/RNtGI2ENcKh5O8kgqTXqS7JG8NXkkxTOlLOW5hCepkLxMDUzdmzqeFpp2IG0yPTq9MYOSkZBxQqohTZO2Z+pn5mZ2y6xlhbL+xW6Lty8elQfJa7OQrAVZLQq2QqboVFoo1yoHsmdlV2a/zYnKOZarnivN7cyzytuQN5zvn//tEsIS4ZK2pYZLVy0dWOa9rGo5sjxxedsK4xUFK4ZWBqw8uIq2Km3VT6vtV5eufr0mek1rgV7ByoLBtQFr6wtVCuWFfevc1+1dT1gvWd+1YfqGnRs+FYmKrhTbF5cVf9go3HjlG4dvyr+Z3JS0qavEuWTPZtJm6ebeLZ5bDpaql+aXDm4N2dq0Dd9WtO319kXbL5fNKNu7g7ZDuaO/PLi8ZafJzs07P1SkVPRU+lQ27tLdtWHX+G7R7ht7vPY07NXbW7z3/T7JvttVAVVN1WbVZftJ+7P3P66Jqun4lvttXa1ObXHtxwPSA/0HIw6217nU1R3SPVRSj9Yr60cOxx++/p3vdy0NNg1VjZzG4iNwRHnk6fcJ3/ceDTradox7rOEH0x92HWcdL2pCmvKaRptTmvtbYlu6T8w+0dbq3nr8R9sfD5w0PFl5SvNUyWna6YLTk2fyz4ydlZ19fi753GDborZ752PO32oPb++6EHTh0kX/i+c7vDvOXPK4dPKy2+UTV7hXmq86X23qdOo8/pPTT8e7nLuarrlca7nuer21e2b36RueN87d9L158Rb/1tWeOT3dvfN6b/fF9/XfFt1+cif9zsu72Xcn7q28T7xf9EDtQdlD3YfVP1v+3Njv3H9qwHeg89HcR/cGhYPP/pH1jw9DBY+Zj8uGDYbrnjg+OTniP3L96fynQ89kzyaeF/6i/suuFxYvfvjV69fO0ZjRoZfyl5O/bXyl/erA6xmv28bCxh6+yXgzMV70VvvtwXfcdx3vo98PT+R8IH8o/2j5sfVT0Kf7kxmTk/8EA5jz/GMzLdsAAAAgY0hSTQAAeiUAAICDAAD5/wAAgOkAAHUwAADqYAAAOpgAABdvkl/FRgAAAJBJREFUeNrsk8EJwzAMRb+7gVbwLFpBK3gFzyKtkFm0ilZQDoZQih2SFnoo/Scb8czTB5fMxLt54IP8GmxmpRQzO6NzEWYGwMy5zhyOiEECiIgVPNfetg1A7/0439AWkVprZhKRiNzTBtBaG6+c9DIZqOqLnape3dndiei5OXe/uvOo6ri21lbm5f+rvgjvAwD4pUXFTxdeKwAAAABJRU5ErkJggg==</sp:value>
              </sp:Content>
           </sp:content>
        </sp:Resource>
      </sp:resource>
      <sp:classification>scan</sp:classification>
      <sp:classification>image</sp:classification>
      <sp:classification>report</sp:classification>
    </sp:Document>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:N023d3732d4394a249a535545406203c2 <http://smartplatforms.org/terms#value> "iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAAACXBIWXMAAAsTAAALEwEAmpwYAAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iAlEtvUhUIIFJCi4AUkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCMFVEsDIoK2AfkIaKOg6OIisr74Xuja9a89+bN/rXXPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEKJHAAEAizZCFz/SMBAPh+PDwrIsAHvgABeNMLCADATZvAMByH/w/qQplcAYCEAcB0kThLCIAUAEB6jkKmAEBGAYCdmCZTAKAEAGDLY2LjAFAtAGAnf+bTAICd+Jl7AQBblCEVAaCRACATZYhEAGg7AKzPVopFAFgwABRmS8Q5ANgtADBJV2ZIALC3AMDOEAuyAAgMADBRiIUpAAR7AGDIIyN4AISZABRG8lc88SuuEOcqAAB4mbI8uSQ5RYFbCC1xB1dXLh4ozkkXKxQ2YQJhmkAuwnmZGTKBNA/g88wAAKCRFRHgg/P9eM4Ors7ONo62Dl8t6r8G/yJiYuP+5c+rcEAAAOF0ftH+LC+zGoA7BoBt/qIl7gRoXgugdfeLZrIPQLUAoOnaV/Nw+H48PEWhkLnZ2eXk5NhKxEJbYcpXff5nwl/AV/1s+X48/Pf14L7iJIEyXYFHBPjgwsz0TKUcz5IJhGLc5o9H/LcL//wd0yLESWK5WCoU41EScY5EmozzMqUiiUKSKcUl0v9k4t8s+wM+3zUAsGo+AXuRLahdYwP2SycQWHTA4vcAAPK7b8HUKAgDgGiD4c93/+8//UegJQCAZkmScQAAXkQkLlTKsz/HCAAARKCBKrBBG/TBGCzABhzBBdzBC/xgNoRCJMTCQhBCCmSAHHJgKayCQiiGzbAdKmAv1EAdNMBRaIaTcA4uwlW4Dj1wD/phCJ7BKLyBCQRByAgTYSHaiAFiilgjjggXmYX4IcFIBBKLJCDJiBRRIkuRNUgxUopUIFVIHfI9cgI5h1xGupE7yAAygvyGvEcxlIGyUT3UDLVDuag3GoRGogvQZHQxmo8WoJvQcrQaPYw2oefQq2gP2o8+Q8cwwOgYBzPEbDAuxsNCsTgsCZNjy7EirAyrxhqwVqwDu4n1Y8+xdwQSgUXACTYEd0IgYR5BSFhMWE7YSKggHCQ0EdoJNwkDhFHCJyKTqEu0JroR+cQYYjIxh1hILCPWEo8TLxB7iEPENyQSiUMyJ7mQAkmxpFTSEtJG0m5SI+ksqZs0SBojk8naZGuyBzmULCAryIXkneTD5DPkG+Qh8lsKnWJAcaT4U+IoUspqShnlEOU05QZlmDJBVaOaUt2ooVQRNY9aQq2htlKvUYeoEzR1mjnNgxZJS6WtopXTGmgXaPdpr+h0uhHdlR5Ol9BX0svpR+iX6AP0dwwNhhWDx4hnKBmbGAcYZxl3GK+YTKYZ04sZx1QwNzHrmOeZD5lvVVgqtip8FZHKCpVKlSaVGyovVKmqpqreqgtV81XLVI+pXlN9rkZVM1PjqQnUlqtVqp1Q61MbU2epO6iHqmeob1Q/pH5Z/YkGWcNMw09DpFGgsV/jvMYgC2MZs3gsIWsNq4Z1gTXEJrHN2Xx2KruY/R27iz2qqaE5QzNKM1ezUvOUZj8H45hx+Jx0TgnnKKeX836K3hTvKeIpG6Y0TLkxZVxrqpaXllirSKtRq0frvTau7aedpr1Fu1n7gQ5Bx0onXCdHZ4/OBZ3nU9lT3acKpxZNPTr1ri6qa6UbobtEd79up+6Ynr5egJ5Mb6feeb3n+hx9L/1U/W36p/VHDFgGswwkBtsMzhg8xTVxbzwdL8fb8VFDXcNAQ6VhlWGX4YSRudE8o9VGjUYPjGnGXOMk423GbcajJgYmISZLTepN7ppSTbmmKaY7TDtMx83MzaLN1pk1mz0x1zLnm+eb15vft2BaeFostqi2uGVJsuRaplnutrxuhVo5WaVYVVpds0atna0l1rutu6cRp7lOk06rntZnw7Dxtsm2qbcZsOXYBtuutm22fWFnYhdnt8Wuw+6TvZN9un2N/T0HDYfZDqsdWh1+c7RyFDpWOt6azpzuP33F9JbpL2dYzxDP2DPjthPLKcRpnVOb00dnF2e5c4PziIuJS4LLLpc+Lpsbxt3IveRKdPVxXeF60vWdm7Obwu2o26/uNu5p7ofcn8w0nymeWTNz0MPIQ+BR5dE/C5+VMGvfrH5PQ0+BZ7XnIy9jL5FXrdewt6V3qvdh7xc+9j5yn+M+4zw33jLeWV/MN8C3yLfLT8Nvnl+F30N/I/9k/3r/0QCngCUBZwOJgUGBWwL7+Hp8Ib+OPzrbZfay2e1BjKC5QRVBj4KtguXBrSFoyOyQrSH355jOkc5pDoVQfujW0Adh5mGLw34MJ4WHhVeGP45wiFga0TGXNXfR3ENz30T6RJZE3ptnMU85ry1KNSo+qi5qPNo3ujS6P8YuZlnM1VidWElsSxw5LiquNm5svt/87fOH4p3iC+N7F5gvyF1weaHOwvSFpxapLhIsOpZATIhOOJTwQRAqqBaMJfITdyWOCnnCHcJnIi/RNtGI2ENcKh5O8kgqTXqS7JG8NXkkxTOlLOW5hCepkLxMDUzdmzqeFpp2IG0yPTq9MYOSkZBxQqohTZO2Z+pn5mZ2y6xlhbL+xW6Lty8elQfJa7OQrAVZLQq2QqboVFoo1yoHsmdlV2a/zYnKOZarnivN7cyzytuQN5zvn//tEsIS4ZK2pYZLVy0dWOa9rGo5sjxxedsK4xUFK4ZWBqw8uIq2Km3VT6vtV5eufr0mek1rgV7ByoLBtQFr6wtVCuWFfevc1+1dT1gvWd+1YfqGnRs+FYmKrhTbF5cVf9go3HjlG4dvyr+Z3JS0qavEuWTPZtJm6ebeLZ5bDpaql+aXDm4N2dq0Dd9WtO319kXbL5fNKNu7g7ZDuaO/PLi8ZafJzs07P1SkVPRU+lQ27tLdtWHX+G7R7ht7vPY07NXbW7z3/T7JvttVAVVN1WbVZftJ+7P3P66Jqun4lvttXa1ObXHtxwPSA/0HIw6217nU1R3SPVRSj9Yr60cOxx++/p3vdy0NNg1VjZzG4iNwRHnk6fcJ3/ceDTradox7rOEH0x92HWcdL2pCmvKaRptTmvtbYlu6T8w+0dbq3nr8R9sfD5w0PFl5SvNUyWna6YLTk2fyz4ydlZ19fi753GDborZ752PO32oPb++6EHTh0kX/i+c7vDvOXPK4dPKy2+UTV7hXmq86X23qdOo8/pPTT8e7nLuarrlca7nuer21e2b36RueN87d9L158Rb/1tWeOT3dvfN6b/fF9/XfFt1+cif9zsu72Xcn7q28T7xf9EDtQdlD3YfVP1v+3Njv3H9qwHeg89HcR/cGhYPP/pH1jw9DBY+Zj8uGDYbrnjg+OTniP3L96fynQ89kzyaeF/6i/suuFxYvfvjV69fO0ZjRoZfyl5O/bXyl/erA6xmv28bCxh6+yXgzMV70VvvtwXfcdx3vo98PT+R8IH8o/2j5sfVT0Kf7kxmTk/8EA5jz/GMzLdsAAAAgY0hSTQAAeiUAAICDAAD5/wAAgOkAAHUwAADqYAAAOpgAABdvkl/FRgAAAJBJREFUeNrsk8EJwzAMRb+7gVbwLFpBK3gFzyKtkFm0ilZQDoZQih2SFnoo/Scb8czTB5fMxLt54IP8GmxmpRQzO6NzEWYGwMy5zhyOiEECiIgVPNfetg1A7/0439AWkVprZhKRiNzTBtBaG6+c9DIZqOqLnape3dndiei5OXe/uvOo6ri21lbm5f+rvgjvAwD4pUXFTxdeKwAAAABJRU5ErkJggg==" .
_:N023d3732d4394a249a535545406203c2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Content> .
_:N023d3732d4394a249a535545406203c2 <http://smartplatforms.org/terms#encoding> "Base64" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#fileName> "reportScan.png" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://purl.org/dc/terms/date> "2010-05-12T04:00:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://purl.org/dc/terms/format> <http://purl.org/NET/mediatypes/image/png> .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://purl.org/dc/terms/title> "Image of a report received from NGD about the patient" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Document> .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#resource> _:N57c3cf6971f3428ab69370145c824553 .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#provider> _:N0da02313670e42fd990fa69e5b75df13 .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#classification> "report" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#classification> "image" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#classification> "scan" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#fileSize> _:N9bcdf37cfaf64a148ff20559fe64575b .
<http://purl.org/NET/mediatypes/image/png> <http://www.w3.org/2000/01/rdf-schema#label> "image/png" .
<http://purl.org/NET/mediatypes/image/png> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.org/dc/terms/MediaTypeOrExtent> .
_:N57c3cf6971f3428ab69370145c824553 <http://smartplatforms.org/terms#content> _:N023d3732d4394a249a535545406203c2 .
_:N57c3cf6971f3428ab69370145c824553 <http://smartplatforms.org/terms#location> "http://sandbox-api.smartplatforms.org/records/2169591/documents/632678" .
_:N57c3cf6971f3428ab69370145c824553 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Resource> .
_:N57c3cf6971f3428ab69370145c824553 <http://smartplatforms.org/terms#hash> _:Nb638fffbe867414d9e7d0aec11ca8f12 .
_:N9bcdf37cfaf64a148ff20559fe64575b <http://smartplatforms.org/terms#value> "2917" .
_:N9bcdf37cfaf64a148ff20559fe64575b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:N9bcdf37cfaf64a148ff20559fe64575b <http://smartplatforms.org/terms#unit> "byte" .
_:N0da02313670e42fd990fa69e5b75df13 <http://www.w3.org/2006/vcard/ns#n> _:Nda27b7a720204ba1b0b66f730b01cb25 .
_:N0da02313670e42fd990fa69e5b75df13 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Provider> .
_:Nb638fffbe867414d9e7d0aec11ca8f12 <http://smartplatforms.org/terms#value> "0e7981902c6c410d673771a3dd0a830712c15930bdec77701922138ea950c620" .
_:Nb638fffbe867414d9e7d0aec11ca8f12 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Hash> .
_:Nb638fffbe867414d9e7d0aec11ca8f12 <http://smartplatforms.org/terms#algorithm> "SHA-256" .
_:Nda27b7a720204ba1b0b66f730b01cb25 <http://www.w3.org/2006/vcard/ns#given-name> "John" .
_:Nda27b7a720204ba1b0b66f730b01cb25 <http://www.w3.org/2006/vcard/ns#family-name> "Smith" .
_:Nda27b7a720204ba1b0b66f730b01cb25 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> a sp:Document;
    dcterms:date "2010-05-12T04:00:00Z";
    dcterms:format <http://purl.org/NET/mediatypes/image/png>;
    dcterms:title "Image of a report received from NGD about the patient";
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:classification "image",
        "report",
        "scan";
    sp:fileName "reportScan.png";
    sp:fileSize [ a sp:ValueAndUnit;
            sp:unit "byte";
            sp:value "2917" ];
    sp:provider [ a sp:Provider;
            vcard:n [ a vcard:Name;
                    vcard:family-name "Smith";
                    vcard:given-name "John" ] ];
    sp:resource [ a sp:Resource;
            sp:content [ a sp:Content;
                    sp:encoding "Base64";
                    sp:value "iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAAACXBIWXMAAAsTAAALEwEAmpwYAAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iAlEtvUhUIIFJCi4AUkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCMFVEsDIoK2AfkIaKOg6OIisr74Xuja9a89+bN/rXXPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEKJHAAEAizZCFz/SMBAPh+PDwrIsAHvgABeNMLCADATZvAMByH/w/qQplcAYCEAcB0kThLCIAUAEB6jkKmAEBGAYCdmCZTAKAEAGDLY2LjAFAtAGAnf+bTAICd+Jl7AQBblCEVAaCRACATZYhEAGg7AKzPVopFAFgwABRmS8Q5ANgtADBJV2ZIALC3AMDOEAuyAAgMADBRiIUpAAR7AGDIIyN4AISZABRG8lc88SuuEOcqAAB4mbI8uSQ5RYFbCC1xB1dXLh4ozkkXKxQ2YQJhmkAuwnmZGTKBNA/g88wAAKCRFRHgg/P9eM4Ors7ONo62Dl8t6r8G/yJiYuP+5c+rcEAAAOF0ftH+LC+zGoA7BoBt/qIl7gRoXgugdfeLZrIPQLUAoOnaV/Nw+H48PEWhkLnZ2eXk5NhKxEJbYcpXff5nwl/AV/1s+X48/Pf14L7iJIEyXYFHBPjgwsz0TKUcz5IJhGLc5o9H/LcL//wd0yLESWK5WCoU41EScY5EmozzMqUiiUKSKcUl0v9k4t8s+wM+3zUAsGo+AXuRLahdYwP2SycQWHTA4vcAAPK7b8HUKAgDgGiD4c93/+8//UegJQCAZkmScQAAXkQkLlTKsz/HCAAARKCBKrBBG/TBGCzABhzBBdzBC/xgNoRCJMTCQhBCCmSAHHJgKayCQiiGzbAdKmAv1EAdNMBRaIaTcA4uwlW4Dj1wD/phCJ7BKLyBCQRByAgTYSHaiAFiilgjjggXmYX4IcFIBBKLJCDJiBRRIkuRNUgxUopUIFVIHfI9cgI5h1xGupE7yAAygvyGvEcxlIGyUT3UDLVDuag3GoRGogvQZHQxmo8WoJvQcrQaPYw2oefQq2gP2o8+Q8cwwOgYBzPEbDAuxsNCsTgsCZNjy7EirAyrxhqwVqwDu4n1Y8+xdwQSgUXACTYEd0IgYR5BSFhMWE7YSKggHCQ0EdoJNwkDhFHCJyKTqEu0JroR+cQYYjIxh1hILCPWEo8TLxB7iEPENyQSiUMyJ7mQAkmxpFTSEtJG0m5SI+ksqZs0SBojk8naZGuyBzmULCAryIXkneTD5DPkG+Qh8lsKnWJAcaT4U+IoUspqShnlEOU05QZlmDJBVaOaUt2ooVQRNY9aQq2htlKvUYeoEzR1mjnNgxZJS6WtopXTGmgXaPdpr+h0uhHdlR5Ol9BX0svpR+iX6AP0dwwNhhWDx4hnKBmbGAcYZxl3GK+YTKYZ04sZx1QwNzHrmOeZD5lvVVgqtip8FZHKCpVKlSaVGyovVKmqpqreqgtV81XLVI+pXlN9rkZVM1PjqQnUlqtVqp1Q61MbU2epO6iHqmeob1Q/pH5Z/YkGWcNMw09DpFGgsV/jvMYgC2MZs3gsIWsNq4Z1gTXEJrHN2Xx2KruY/R27iz2qqaE5QzNKM1ezUvOUZj8H45hx+Jx0TgnnKKeX836K3hTvKeIpG6Y0TLkxZVxrqpaXllirSKtRq0frvTau7aedpr1Fu1n7gQ5Bx0onXCdHZ4/OBZ3nU9lT3acKpxZNPTr1ri6qa6UbobtEd79up+6Ynr5egJ5Mb6feeb3n+hx9L/1U/W36p/VHDFgGswwkBtsMzhg8xTVxbzwdL8fb8VFDXcNAQ6VhlWGX4YSRudE8o9VGjUYPjGnGXOMk423GbcajJgYmISZLTepN7ppSTbmmKaY7TDtMx83MzaLN1pk1mz0x1zLnm+eb15vft2BaeFostqi2uGVJsuRaplnutrxuhVo5WaVYVVpds0atna0l1rutu6cRp7lOk06rntZnw7Dxtsm2qbcZsOXYBtuutm22fWFnYhdnt8Wuw+6TvZN9un2N/T0HDYfZDqsdWh1+c7RyFDpWOt6azpzuP33F9JbpL2dYzxDP2DPjthPLKcRpnVOb00dnF2e5c4PziIuJS4LLLpc+Lpsbxt3IveRKdPVxXeF60vWdm7Obwu2o26/uNu5p7ofcn8w0nymeWTNz0MPIQ+BR5dE/C5+VMGvfrH5PQ0+BZ7XnIy9jL5FXrdewt6V3qvdh7xc+9j5yn+M+4zw33jLeWV/MN8C3yLfLT8Nvnl+F30N/I/9k/3r/0QCngCUBZwOJgUGBWwL7+Hp8Ib+OPzrbZfay2e1BjKC5QRVBj4KtguXBrSFoyOyQrSH355jOkc5pDoVQfujW0Adh5mGLw34MJ4WHhVeGP45wiFga0TGXNXfR3ENz30T6RJZE3ptnMU85ry1KNSo+qi5qPNo3ujS6P8YuZlnM1VidWElsSxw5LiquNm5svt/87fOH4p3iC+N7F5gvyF1weaHOwvSFpxapLhIsOpZATIhOOJTwQRAqqBaMJfITdyWOCnnCHcJnIi/RNtGI2ENcKh5O8kgqTXqS7JG8NXkkxTOlLOW5hCepkLxMDUzdmzqeFpp2IG0yPTq9MYOSkZBxQqohTZO2Z+pn5mZ2y6xlhbL+xW6Lty8elQfJa7OQrAVZLQq2QqboVFoo1yoHsmdlV2a/zYnKOZarnivN7cyzytuQN5zvn//tEsIS4ZK2pYZLVy0dWOa9rGo5sjxxedsK4xUFK4ZWBqw8uIq2Km3VT6vtV5eufr0mek1rgV7ByoLBtQFr6wtVCuWFfevc1+1dT1gvWd+1YfqGnRs+FYmKrhTbF5cVf9go3HjlG4dvyr+Z3JS0qavEuWTPZtJm6ebeLZ5bDpaql+aXDm4N2dq0Dd9WtO319kXbL5fNKNu7g7ZDuaO/PLi8ZafJzs07P1SkVPRU+lQ27tLdtWHX+G7R7ht7vPY07NXbW7z3/T7JvttVAVVN1WbVZftJ+7P3P66Jqun4lvttXa1ObXHtxwPSA/0HIw6217nU1R3SPVRSj9Yr60cOxx++/p3vdy0NNg1VjZzG4iNwRHnk6fcJ3/ceDTradox7rOEH0x92HWcdL2pCmvKaRptTmvtbYlu6T8w+0dbq3nr8R9sfD5w0PFl5SvNUyWna6YLTk2fyz4ydlZ19fi753GDborZ752PO32oPb++6EHTh0kX/i+c7vDvOXPK4dPKy2+UTV7hXmq86X23qdOo8/pPTT8e7nLuarrlca7nuer21e2b36RueN87d9L158Rb/1tWeOT3dvfN6b/fF9/XfFt1+cif9zsu72Xcn7q28T7xf9EDtQdlD3YfVP1v+3Njv3H9qwHeg89HcR/cGhYPP/pH1jw9DBY+Zj8uGDYbrnjg+OTniP3L96fynQ89kzyaeF/6i/suuFxYvfvjV69fO0ZjRoZfyl5O/bXyl/erA6xmv28bCxh6+yXgzMV70VvvtwXfcdx3vo98PT+R8IH8o/2j5sfVT0Kf7kxmTk/8EA5jz/GMzLdsAAAAgY0hSTQAAeiUAAICDAAD5/wAAgOkAAHUwAADqYAAAOpgAABdvkl/FRgAAAJBJREFUeNrsk8EJwzAMRb+7gVbwLFpBK3gFzyKtkFm0ilZQDoZQih2SFnoo/Scb8czTB5fMxLt54IP8GmxmpRQzO6NzEWYGwMy5zhyOiEECiIgVPNfetg1A7/0439AWkVprZhKRiNzTBtBaG6+c9DIZqOqLnape3dndiei5OXe/uvOo6ri21lbm5f+rvgjvAwD4pUXFTxdeKwAAAABJRU5ErkJggg==" ];
            sp:hash [ a sp:Hash;
                    sp:algorithm "SHA-256";
                    sp:value "0e7981902c6c410d673771a3dd0a830712c15930bdec77701922138ea950c620" ];
            sp:location "http://sandbox-api.smartplatforms.org/records/2169591/documents/632678" ] .

<http://purl.org/NET/mediatypes/image/png> a dcterms:MediaTypeOrExtent;
    rdfs:label "image/png" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://purl.org/NET/mediatypes/image/png",
      "@type": "dcterms__MediaTypeOrExtent",
      "rdfs__label": "image/png"
    },
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/documents/632678",
      "@type": "Document",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "classification": [
        "report",
        "image",
        "scan"
      ],
      "dcterms__date": "2010-05-12T04:00:00Z",
      "dcterms__format": {
        "@id": "http://purl.org/NET/mediatypes/image/png"
      },
      "dcterms__title": "Image of a report received from NGD about the patient",
      "fileName": "reportScan.png",
      "fileSize": {
        "@type": "ValueAndUnit",
        "unit": "byte",
        "value": "2917"
      },
      "provider": {
        "@type": "Provider",
        "vcard__n": {
          "@type": "vcard__Name",
          "vcard__family_name": "Smith",
          "vcard__given_name": "John"
        }
      },
      "resource": [
        {
          "@type": "Resource",
          "content": {
            "@type": "Content",
            "encoding": "Base64",
            "value": "iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAAACXBIWXMAAAsTAAALEwEAmpwYAAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iAlEtvUhUIIFJCi4AUkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCMFVEsDIoK2AfkIaKOg6OIisr74Xuja9a89+bN/rXXPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEKJHAAEAizZCFz/SMBAPh+PDwrIsAHvgABeNMLCADATZvAMByH/w/qQplcAYCEAcB0kThLCIAUAEB6jkKmAEBGAYCdmCZTAKAEAGDLY2LjAFAtAGAnf+bTAICd+Jl7AQBblCEVAaCRACATZYhEAGg7AKzPVopFAFgwABRmS8Q5ANgtADBJV2ZIALC3AMDOEAuyAAgMADBRiIUpAAR7AGDIIyN4AISZABRG8lc88SuuEOcqAAB4mbI8uSQ5RYFbCC1xB1dXLh4ozkkXKxQ2YQJhmkAuwnmZGTKBNA/g88wAAKCRFRHgg/P9eM4Ors7ONo62Dl8t6r8G/yJiYuP+5c+rcEAAAOF0ftH+LC+zGoA7BoBt/qIl7gRoXgugdfeLZrIPQLUAoOnaV/Nw+H48PEWhkLnZ2eXk5NhKxEJbYcpXff5nwl/AV/1s+X48/Pf14L7iJIEyXYFHBPjgwsz0TKUcz5IJhGLc5o9H/LcL//wd0yLESWK5WCoU41EScY5EmozzMqUiiUKSKcUl0v9k4t8s+wM+3zUAsGo+AXuRLahdYwP2SycQWHTA4vcAAPK7b8HUKAgDgGiD4c93/+8//UegJQCAZkmScQAAXkQkLlTKsz/HCAAARKCBKrBBG/TBGCzABhzBBdzBC/xgNoRCJMTCQhBCCmSAHHJgKayCQiiGzbAdKmAv1EAdNMBRaIaTcA4uwlW4Dj1wD/phCJ7BKLyBCQRByAgTYSHaiAFiilgjjggXmYX4IcFIBBKLJCDJiBRRIkuRNUgxUopUIFVIHfI9cgI5h1xGupE7yAAygvyGvEcxlIGyUT3UDLVDuag3GoRGogvQZHQxmo8WoJvQcrQaPYw2oefQq2gP2o8+Q8cwwOgYBzPEbDAuxsNCsTgsCZNjy7EirAyrxhqwVqwDu4n1Y8+xdwQSgUXACTYEd0IgYR5BSFhMWE7YSKggHCQ0EdoJNwkDhFHCJyKTqEu0JroR+cQYYjIxh1hILCPWEo8TLxB7iEPENyQSiUMyJ7mQAkmxpFTSEtJG0m5SI+ksqZs0SBojk8naZGuyBzmULCAryIXkneTD5DPkG+Qh8lsKnWJAcaT4U+IoUspqShnlEOU05QZlmDJBVaOaUt2ooVQRNY9aQq2htlKvUYeoEzR1mjnNgxZJS6WtopXTGmgXaPdpr+h0uhHdlR5Ol9BX0svpR+iX6AP0dwwNhhWDx4hnKBmbGAcYZxl3GK+YTKYZ04sZx1QwNzHrmOeZD5lvVVgqtip8FZHKCpVKlSaVGyovVKmqpqreqgtV81XLVI+pXlN9rkZVM1PjqQnUlqtVqp1Q61MbU2epO6iHqmeob1Q/pH5Z/YkGWcNMw09DpFGgsV/jvMYgC2MZs3gsIWsNq4Z1gTXEJrHN2Xx2KruY/R27iz2qqaE5QzNKM1ezUvOUZj8H45hx+Jx0TgnnKKeX836K3hTvKeIpG6Y0TLkxZVxrqpaXllirSKtRq0frvTau7aedpr1Fu1n7gQ5Bx0onXCdHZ4/OBZ3nU9lT3acKpxZNPTr1ri6qa6UbobtEd79up+6Ynr5egJ5Mb6feeb3n+hx9L/1U/W36p/VHDFgGswwkBtsMzhg8xTVxbzwdL8fb8VFDXcNAQ6VhlWGX4YSRudE8o9VGjUYPjGnGXOMk423GbcajJgYmISZLTepN7ppSTbmmKaY7TDtMx83MzaLN1pk1mz0x1zLnm+eb15vft2BaeFostqi2uGVJsuRaplnutrxuhVo5WaVYVVpds0atna0l1rutu6cRp7lOk06rntZnw7Dxtsm2qbcZsOXYBtuutm22fWFnYhdnt8Wuw+6TvZN9un2N/T0HDYfZDqsdWh1+c7RyFDpWOt6azpzuP33F9JbpL2dYzxDP2DPjthPLKcRpnVOb00dnF2e5c4PziIuJS4LLLpc+Lpsbxt3IveRKdPVxXeF60vWdm7Obwu2o26/uNu5p7ofcn8w0nymeWTNz0MPIQ+BR5dE/C5+VMGvfrH5PQ0+BZ7XnIy9jL5FXrdewt6V3qvdh7xc+9j5yn+M+4zw33jLeWV/MN8C3yLfLT8Nvnl+F30N/I/9k/3r/0QCngCUBZwOJgUGBWwL7+Hp8Ib+OPzrbZfay2e1BjKC5QRVBj4KtguXBrSFoyOyQrSH355jOkc5pDoVQfujW0Adh5mGLw34MJ4WHhVeGP45wiFga0TGXNXfR3ENz30T6RJZE3ptnMU85ry1KNSo+qi5qPNo3ujS6P8YuZlnM1VidWElsSxw5LiquNm5svt/87fOH4p3iC+N7F5gvyF1weaHOwvSFpxapLhIsOpZATIhOOJTwQRAqqBaMJfITdyWOCnnCHcJnIi/RNtGI2ENcKh5O8kgqTXqS7JG8NXkkxTOlLOW5hCepkLxMDUzdmzqeFpp2IG0yPTq9MYOSkZBxQqohTZO2Z+pn5mZ2y6xlhbL+xW6Lty8elQfJa7OQrAVZLQq2QqboVFoo1yoHsmdlV2a/zYnKOZarnivN7cyzytuQN5zvn//tEsIS4ZK2pYZLVy0dWOa9rGo5sjxxedsK4xUFK4ZWBqw8uIq2Km3VT6vtV5eufr0mek1rgV7ByoLBtQFr6wtVCuWFfevc1+1dT1gvWd+1YfqGnRs+FYmKrhTbF5cVf9go3HjlG4dvyr+Z3JS0qavEuWTPZtJm6ebeLZ5bDpaql+aXDm4N2dq0Dd9WtO319kXbL5fNKNu7g7ZDuaO/PLi8ZafJzs07P1SkVPRU+lQ27tLdtWHX+G7R7ht7vPY07NXbW7z3/T7JvttVAVVN1WbVZftJ+7P3P66Jqun4lvttXa1ObXHtxwPSA/0HIw6217nU1R3SPVRSj9Yr60cOxx++/p3vdy0NNg1VjZzG4iNwRHnk6fcJ3/ceDTradox7rOEH0x92HWcdL2pCmvKaRptTmvtbYlu6T8w+0dbq3nr8R9sfD5w0PFl5SvNUyWna6YLTk2fyz4ydlZ19fi753GDborZ752PO32oPb++6EHTh0kX/i+c7vDvOXPK4dPKy2+UTV7hXmq86X23qdOo8/pPTT8e7nLuarrlca7nuer21e2b36RueN87d9L158Rb/1tWeOT3dvfN6b/fF9/XfFt1+cif9zsu72Xcn7q28T7xf9EDtQdlD3YfVP1v+3Njv3H9qwHeg89HcR/cGhYPP/pH1jw9DBY+Zj8uGDYbrnjg+OTniP3L96fynQ89kzyaeF/6i/suuFxYvfvjV69fO0ZjRoZfyl5O/bXyl/erA6xmv28bCxh6+yXgzMV70VvvtwXfcdx3vo98PT+R8IH8o/2j5sfVT0Kf7kxmTk/8EA5jz/GMzLdsAAAAgY0hSTQAAeiUAAICDAAD5/wAAgOkAAHUwAADqYAAAOpgAABdvkl/FRgAAAJBJREFUeNrsk8EJwzAMRb+7gVbwLFpBK3gFzyKtkFm0ilZQDoZQih2SFnoo/Scb8czTB5fMxLt54IP8GmxmpRQzO6NzEWYGwMy5zhyOiEECiIgVPNfetg1A7/0439AWkVprZhKRiNzTBtBaG6+c9DIZqOqLnape3dndiei5OXe/uvOo6ri21lbm5f+rvgjvAwD4pUXFTxdeKwAAAABJRU5ErkJggg=="
          },
          "hash": {
            "@type": "Hash",
            "algorithm": "SHA-256",
            "value": "0e7981902c6c410d673771a3dd0a830712c15930bdec77701922138ea950c620"
          },
          "location": "http://sandbox-api.smartplatforms.org/records/2169591/documents/632678"
        }
      ]
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Document</caption>
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
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

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
<br><br>
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
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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


classification
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#classification</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


fileName
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#fileName</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


fileSize
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#fileSize</span>
<br />
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a> where unit has value: byte</span>
<br><br>
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
<br><br>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


resource
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#resource</span>
<br />
<span style='font-size: small'><a href='#Resource'>Resource</a></span>
<br><br>
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
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#endDate> "2010-05-12T04:20:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#encounterType> _:N396b9fd1536a43209b696e65d0af81b5 .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Encounter> .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#startDate> "2010-05-12T04:00:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/EncounterType#" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/EncounterType> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/identifier> "ambulatory" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/title> "Ambulatory encounter" .
_:N396b9fd1536a43209b696e65d0af81b5 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N396b9fd1536a43209b696e65d0af81b5 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/EncounterType#ambulatory> .
_:N396b9fd1536a43209b696e65d0af81b5 <http://purl.org/dc/terms/title> "Ambulatory encounter" .


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

<h2 id='Family_History_Observation'><code>Family History Observation</code></h2>

`Family History Observation` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


<div id='Family_History_Observation_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Family_History_Observation_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Family_History_Observation_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Family_History_Observation_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Family_History_Observation_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:spcode="http://smartplatforms.org/terms/codes/"
  xmlns:v="http://www.w3.org/2006/vcard/ns#"> 
  <sp:FamilyHistory rdf:about="http://sandbox-api.smartplatforms.org/records/123456/family_histories/123456">
    <sp:belongsTo rdf:resource="http://sandbox-api.smartplatforms.org/records/123456" />
    <sp:aboutRelative>
      <sp:CodedValue>
        <dcterms:title>Grand-father</dcterms:title>
        <sp:code>
          <spcode:SNOMED rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/34871008">
            <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
            <dcterms:title>Grand-father</dcterms:title>
            <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
            <dcterms:identifier>34871008</dcterms:identifier>
          </spcode:SNOMED>
        </sp:code>
      </sp:CodedValue>
    </sp:aboutRelative>
    <v:bday>1959-12-25</v:bday>
    <v:deathdate>2012-11-18</v:deathdate>
    <sp:hasProblem>
      <sp:CodedValue>
        <dcterms:title>Diabetes mellitus</dcterms:title>   
        <sp:code>
          <spcode:SNOMED rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/73211009">
            <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
            <dcterms:title>Diabetes mellitus</dcterms:title>
            <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
            <dcterms:identifier>73211009</dcterms:identifier>
          </spcode:SNOMED>
        </sp:code>
      </sp:CodedValue>
    </sp:hasProblem>
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
        <sp:value>180</sp:value>
        <sp:unit>cm</sp:unit>
      </sp:VitalSign>
    </sp:height>
  </sp:FamilyHistory>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
<http://sandbox-api.smartplatforms.org/records/123456/family_histories/123456> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#FamilyHistory> .
<http://sandbox-api.smartplatforms.org/records/123456/family_histories/123456> <http://www.w3.org/2006/vcard/ns#deathdate> "2012-11-18" .
<http://sandbox-api.smartplatforms.org/records/123456/family_histories/123456> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/123456> .
<http://sandbox-api.smartplatforms.org/records/123456/family_histories/123456> <http://www.w3.org/2006/vcard/ns#bday> "1959-12-25" .
<http://sandbox-api.smartplatforms.org/records/123456/family_histories/123456> <http://smartplatforms.org/terms#height> _:N0fdf8529f1054dca93d281117821773a .
<http://sandbox-api.smartplatforms.org/records/123456/family_histories/123456> <http://smartplatforms.org/terms#aboutRelative> _:N5f8bf66b58e64bd69ff45f378ab7b567 .
<http://sandbox-api.smartplatforms.org/records/123456/family_histories/123456> <http://smartplatforms.org/terms#hasProblem> _:N14c0e332f0e94f438b6e47a1128b9e4f .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://purl.org/dc/terms/identifier> "8302-2" .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://purl.org/dc/terms/title> "Body height" .
_:N14c0e332f0e94f438b6e47a1128b9e4f <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N14c0e332f0e94f438b6e47a1128b9e4f <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/73211009> .
_:N14c0e332f0e94f438b6e47a1128b9e4f <http://purl.org/dc/terms/title> "Diabetes mellitus" .
<http://purl.bioontology.org/ontology/SNOMEDCT/34871008> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/34871008> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/SNOMED> .
<http://purl.bioontology.org/ontology/SNOMEDCT/34871008> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/34871008> <http://purl.org/dc/terms/identifier> "34871008" .
<http://purl.bioontology.org/ontology/SNOMEDCT/34871008> <http://purl.org/dc/terms/title> "Grand-father" .
<http://purl.bioontology.org/ontology/SNOMEDCT/73211009> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/73211009> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/SNOMED> .
<http://purl.bioontology.org/ontology/SNOMEDCT/73211009> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/73211009> <http://purl.org/dc/terms/identifier> "73211009" .
<http://purl.bioontology.org/ontology/SNOMEDCT/73211009> <http://purl.org/dc/terms/title> "Diabetes mellitus" .
_:N850edb2b29aa43a58594c47d98826319 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N850edb2b29aa43a58594c47d98826319 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8302-2> .
_:N850edb2b29aa43a58594c47d98826319 <http://purl.org/dc/terms/title> "Body height" .
_:N0fdf8529f1054dca93d281117821773a <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:N0fdf8529f1054dca93d281117821773a <http://smartplatforms.org/terms#vitalName> _:N850edb2b29aa43a58594c47d98826319 .
_:N0fdf8529f1054dca93d281117821773a <http://smartplatforms.org/terms#unit> "cm" .
_:N0fdf8529f1054dca93d281117821773a <http://smartplatforms.org/terms#value> "180" .
_:N5f8bf66b58e64bd69ff45f378ab7b567 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N5f8bf66b58e64bd69ff45f378ab7b567 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/34871008> .
_:N5f8bf66b58e64bd69ff45f378ab7b567 <http://purl.org/dc/terms/title> "Grand-father" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

<http://sandbox-api.smartplatforms.org/records/123456/family_histories/123456> a sp:FamilyHistory;
    sp:aboutRelative [ a sp:CodedValue;
            dcterms:title "Grand-father";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/34871008> ];
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/123456>;
    sp:hasProblem [ a sp:CodedValue;
            dcterms:title "Diabetes mellitus";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/73211009> ];
    sp:height [ a sp:VitalSign;
            sp:unit "cm";
            sp:value "180";
            sp:vitalName [ a sp:CodedValue;
                    dcterms:title "Body height";
                    sp:code <http://purl.bioontology.org/ontology/LNC/8302-2> ] ];
    vcard:bday "1959-12-25";
    vcard:deathdate "2012-11-18" .

<http://purl.bioontology.org/ontology/LNC/8302-2> a sp:Code,
        spcode:VitalSign;
    dcterms:identifier "8302-2";
    dcterms:title "Body height";
    sp:system "http://purl.bioontology.org/ontology/LNC/" .

<http://purl.bioontology.org/ontology/SNOMEDCT/34871008> a sp:Code,
        spcode:SNOMED;
    dcterms:identifier "34871008";
    dcterms:title "Grand-father";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .

<http://purl.bioontology.org/ontology/SNOMEDCT/73211009> a sp:Code,
        spcode:SNOMED;
    dcterms:identifier "73211009";
    dcterms:title "Diabetes mellitus";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/73211009",
      "@type": [
        "Code",
        "spcode__SNOMED"
      ],
      "dcterms__identifier": "73211009",
      "dcterms__title": "Diabetes mellitus",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
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
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/34871008",
      "@type": [
        "Code",
        "spcode__SNOMED"
      ],
      "dcterms__identifier": "34871008",
      "dcterms__title": "Grand-father",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    },
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/123456/family_histories/123456",
      "@type": "FamilyHistory",
      "aboutRelative": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/34871008"
        },
        "dcterms__title": "Grand-father"
      },
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/123456"
      },
      "hasProblem": [
        {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/73211009"
          },
          "dcterms__title": "Diabetes mellitus"
        }
      ],
      "height": {
        "@type": "VitalSign",
        "unit": "cm",
        "value": "180",
        "vitalName": {
          "@type": "CodedValue",
          "code": {
            "@id": "http://purl.bioontology.org/ontology/LNC/8302-2"
          },
          "dcterms__title": "Body height"
        }
      },
      "vcard__bday": "1959-12-25",
      "vcard__deathdate": "2012-11-18"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#FamilyHistory</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


aboutRelative
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#aboutRelative</span>
<br />
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#SNOMED_code'>SNOMED</a></span>
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


hasProblem
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#hasProblem</span>
<br />
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a> where code comes from <a href='#SNOMED_code'>SNOMED</a></span>
<br><br>
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
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: cm</span>
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
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


deathdate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#deathdate</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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
_:N3207a6d4c06e46a4b2c45e65c75787e1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Address> .
_:N3207a6d4c06e46a4b2c45e65c75787e1 <http://www.w3.org/2006/vcard/ns#street-address> "111 Lake Drive" .
_:N3207a6d4c06e46a4b2c45e65c75787e1 <http://www.w3.org/2006/vcard/ns#country-name> "Australia" .
_:N3207a6d4c06e46a4b2c45e65c75787e1 <http://www.w3.org/2006/vcard/ns#locality> "WonderCity" .
_:N3207a6d4c06e46a4b2c45e65c75787e1 <http://www.w3.org/2006/vcard/ns#postal-code> "5555" .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#pbm> "T00000000001011" .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://purl.org/dc/terms/date> "2010-05-12T04:00:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#pharmacy> _:N7e19fcfe1dae46d8bbebab3780672e63 .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#provider> _:Nabe3afc0d22c409aa589b19457f5dbee .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Fulfillment> .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#medication> <http://sandbox-api.smartplatforms.org/records/2169591/medications/123> .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#quantityDispensed> _:N3282a625914d4522a37adc4f31593f01 .
<http://sandbox-api.smartplatforms.org/records/2169591/fulfillments/63221> <http://smartplatforms.org/terms#dispenseDaysSupply> "30" .
_:Nabe3afc0d22c409aa589b19457f5dbee <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Provider> .
_:Nabe3afc0d22c409aa589b19457f5dbee <http://smartplatforms.org/terms#deaNumber> "325555555" .
_:Nabe3afc0d22c409aa589b19457f5dbee <http://www.w3.org/2006/vcard/ns#n> _:N3ac87fec151e4138ae6e26a3dac05a35 .
_:Nabe3afc0d22c409aa589b19457f5dbee <http://smartplatforms.org/terms#npiNumber> "5235235" .
_:N3ac87fec151e4138ae6e26a3dac05a35 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .
_:N3ac87fec151e4138ae6e26a3dac05a35 <http://www.w3.org/2006/vcard/ns#given-name> "Joshua" .
_:N3ac87fec151e4138ae6e26a3dac05a35 <http://www.w3.org/2006/vcard/ns#family-name> "Mandel" .
_:N7e19fcfe1dae46d8bbebab3780672e63 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Pharmacy> .
_:N7e19fcfe1dae46d8bbebab3780672e63 <http://www.w3.org/2006/vcard/ns#organization-name> "CVS #588" .
_:N7e19fcfe1dae46d8bbebab3780672e63 <http://www.w3.org/2006/vcard/ns#adr> _:N3207a6d4c06e46a4b2c45e65c75787e1 .
_:N7e19fcfe1dae46d8bbebab3780672e63 <http://smartplatforms.org/terms#ncpdpId> "5235235" .
_:N3282a625914d4522a37adc4f31593f01 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:N3282a625914d4522a37adc4f31593f01 <http://smartplatforms.org/terms#unit> "{tablet}" .
_:N3282a625914d4522a37adc4f31593f01 <http://smartplatforms.org/terms#value> "60" .


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
_:Ne291c2d7ff1946efa0b1d945b637c629 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Ne291c2d7ff1946efa0b1d945b637c629 <http://smartplatforms.org/terms#code> <http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> .
_:Ne291c2d7ff1946efa0b1d945b637c629 <http://purl.org/dc/terms/title> "typhoid, oral" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://purl.org/dc/terms/identifier> "25" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://smartplatforms.org/terms#system> "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationProduct> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25> <http://purl.org/dc/terms/title> "typhoid, oral" .
_:Nd7a40f07710645d88973eea2090f14b7 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Nd7a40f07710645d88973eea2090f14b7 <http://smartplatforms.org/terms#code> <http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> .
_:Nd7a40f07710645d88973eea2090f14b7 <http://purl.org/dc/terms/title> "TYPHOID" .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://purl.org/dc/terms/identifier> "notAdministered" .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#" .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus> .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> <http://purl.org/dc/terms/title> "Not Administered" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://purl.org/dc/terms/identifier> "TYPHOID" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://smartplatforms.org/terms#system> "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#" .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationClass> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#TYPHOID> <http://purl.org/dc/terms/title> "TYPHOID" .
_:Nd6f5996e87a24ed9a05960377daecf3a <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Nd6f5996e87a24ed9a05960377daecf3a <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered> .
_:Nd6f5996e87a24ed9a05960377daecf3a <http://purl.org/dc/terms/title> "Not Administered" .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://purl.org/dc/terms/identifier> "allergy" .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#" .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/ImmunizationRefusalReason> .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> <http://purl.org/dc/terms/title> "Allergy to vaccine/vaccine components, or allergy to eggs" .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://purl.org/dc/terms/date> "2010-05-12T04:00:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://smartplatforms.org/terms#refusalReason> _:N9c589ffc088e4dbbb1ef0cf55bb925b2 .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://smartplatforms.org/terms#administrationStatus> _:Nd6f5996e87a24ed9a05960377daecf3a .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Immunization> .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://smartplatforms.org/terms#productName> _:Ne291c2d7ff1946efa0b1d945b637c629 .
<http://sandbox-api.smartplatforms.org/records/2169591/immunizations/418972> <http://smartplatforms.org/terms#productClass> _:Nd7a40f07710645d88973eea2090f14b7 .
_:N9c589ffc088e4dbbb1ef0cf55bb925b2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N9c589ffc088e4dbbb1ef0cf55bb925b2 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#allergy> .
_:N9c589ffc088e4dbbb1ef0cf55bb925b2 <http://purl.org/dc/terms/title> "Allergy to vaccine/vaccine components, or allergy to eggs" .


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
      "@id": "http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#notAdministered",
      "@type": [
        "spcode__ImmunizationAdministrationStatus",
        "Code"
      ],
      "dcterms__identifier": "notAdministered",
      "dcterms__title": "Not Administered",
      "system": "http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#"
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
      "@id": "http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#25",
      "@type": [
        "spcode__ImmunizationProduct",
        "Code"
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
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/LabResultInterpretation#" .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://purl.org/dc/terms/title> "Normal" .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/LabResultInterpretation> .
<http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> <http://purl.org/dc/terms/identifier> "normal" .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://purl.org/dc/terms/title> "Serum sodium" .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/LOINC> .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/2951-2> <http://purl.org/dc/terms/identifier> "2951-2" .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#abnormalInterpretation> _:Nec7f153247e847b1b06787cf99a61dc2 .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#notes> "Blood sample appears to have hemolyzed" .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#labName> _:N0b29be2fe0df4e3c9ceb572caef3437c .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#quantitativeResult> _:N9041eba63ba748b2b3fb115e9132959e .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#accessionNumber> "AC09205823577" .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://purl.org/dc/terms/date> "2010-12-27T17:00:00" .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://smartplatforms.org/terms#labStatus> _:N5dc06ecf27ba43b7bc06d52f2e2cec82 .
<http://sandbox-api.smartplatforms.org/records/2169591/lab_results/2891724> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#LabResult> .
_:N5dc06ecf27ba43b7bc06d52f2e2cec82 <http://purl.org/dc/terms/title> "Final results: complete and verified" .
_:N5dc06ecf27ba43b7bc06d52f2e2cec82 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N5dc06ecf27ba43b7bc06d52f2e2cec82 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/LabStatus#final> .
_:N9041eba63ba748b2b3fb115e9132959e <http://smartplatforms.org/terms#nonCriticalRange> _:Nb9c1b4e8127949b58c06109846b297ff .
_:N9041eba63ba748b2b3fb115e9132959e <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#QuantitativeResult> .
_:N9041eba63ba748b2b3fb115e9132959e <http://smartplatforms.org/terms#normalRange> _:Nd6623d1d285840478581cdb81f989c45 .
_:N9041eba63ba748b2b3fb115e9132959e <http://smartplatforms.org/terms#valueAndUnit> _:N5a39a238bddc4e2184b4ff3c36968e13 .
_:N0b29be2fe0df4e3c9ceb572caef3437c <http://purl.org/dc/terms/title> "Serum sodium" .
_:N0b29be2fe0df4e3c9ceb572caef3437c <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N0b29be2fe0df4e3c9ceb572caef3437c <http://smartplatforms.org/terms#provenance> _:N87a7887b7bc14f4f8e049876eb560c4b .
_:N0b29be2fe0df4e3c9ceb572caef3437c <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/2951-2> .
_:N87a7887b7bc14f4f8e049876eb560c4b <http://smartplatforms.org/terms#sourceCode> <http://my.local.coding.system/01234> .
_:N87a7887b7bc14f4f8e049876eb560c4b <http://purl.org/dc/terms/title> "Random blood sodium level" .
_:N87a7887b7bc14f4f8e049876eb560c4b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodeProvenance> .
_:N87a7887b7bc14f4f8e049876eb560c4b <http://smartplatforms.org/terms#translationFidelity> <http://smartplatforms.org/terms/codes/TranslationFidelity#verified> .
_:N36347c0d0aa34917a88dbdb424048ff6 <http://smartplatforms.org/terms#value> "145" .
_:N36347c0d0aa34917a88dbdb424048ff6 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:N36347c0d0aa34917a88dbdb424048ff6 <http://smartplatforms.org/terms#unit> "mEq/L" .
_:N5a39a238bddc4e2184b4ff3c36968e13 <http://smartplatforms.org/terms#value> "140" .
_:N5a39a238bddc4e2184b4ff3c36968e13 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:N5a39a238bddc4e2184b4ff3c36968e13 <http://smartplatforms.org/terms#unit> "mEq/L" .
_:Nb9c1b4e8127949b58c06109846b297ff <http://smartplatforms.org/terms#minimum> _:N4b914fc1a8fe4694b9e0f1bcac8b07aa .
_:Nb9c1b4e8127949b58c06109846b297ff <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueRange> .
_:Nb9c1b4e8127949b58c06109846b297ff <http://smartplatforms.org/terms#maximum> _:Nd5b26968948a4b1eafbc50b27969687b .
_:Nec7f153247e847b1b06787cf99a61dc2 <http://purl.org/dc/terms/title> "Normal" .
_:Nec7f153247e847b1b06787cf99a61dc2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Nec7f153247e847b1b06787cf99a61dc2 <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/LabResultInterpretation#normal> .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/LabStatus#" .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://purl.org/dc/terms/title> "Final" .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/LabResultStatus> .
<http://smartplatforms.org/terms/codes/LabStatus#final> <http://purl.org/dc/terms/identifier> "final" .
_:Nd5b26968948a4b1eafbc50b27969687b <http://smartplatforms.org/terms#value> "155" .
_:Nd5b26968948a4b1eafbc50b27969687b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:Nd5b26968948a4b1eafbc50b27969687b <http://smartplatforms.org/terms#unit> "mEq/L" .
_:N4b914fc1a8fe4694b9e0f1bcac8b07aa <http://smartplatforms.org/terms#value> "120" .
_:N4b914fc1a8fe4694b9e0f1bcac8b07aa <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:N4b914fc1a8fe4694b9e0f1bcac8b07aa <http://smartplatforms.org/terms#unit> "mEq/L" .
_:Nacb0e47f2ace4c8e9baa5bc7dff0e502 <http://smartplatforms.org/terms#value> "135" .
_:Nacb0e47f2ace4c8e9baa5bc7dff0e502 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:Nacb0e47f2ace4c8e9baa5bc7dff0e502 <http://smartplatforms.org/terms#unit> "mEq/L" .
_:Nd6623d1d285840478581cdb81f989c45 <http://smartplatforms.org/terms#minimum> _:Nacb0e47f2ace4c8e9baa5bc7dff0e502 .
_:Nd6623d1d285840478581cdb81f989c45 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueRange> .
_:Nd6623d1d285840478581cdb81f989c45 <http://smartplatforms.org/terms#maximum> _:N36347c0d0aa34917a88dbdb424048ff6 .


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
      "@id": "http://smartplatforms.org/terms/codes/LabStatus#final",
      "@type": [
        "Code",
        "spcode__LabResultStatus"
      ],
      "dcterms__identifier": "final",
      "dcterms__title": "Final",
      "system": "http://smartplatforms.org/terms/codes/LabStatus#"
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

<h2 id='Medical_Image'><code>Medical Image</code></h2>

`Medical Image` is a subtype of and inherits properties from:
[Document](#Document), [SMART Statement](#SMART_Statement)


<div id='Medical_Image_examples'>

<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#Medical_Image_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#Medical_Image_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#Medical_Image_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#Medical_Image_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
<div class='rdf_xml active'>{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:sp="http://smartplatforms.org/terms#"
  xmlns:v="http://www.w3.org/2006/vcard/ns#"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:dcterms="http://purl.org/dc/terms/"> 
      <sp:Document rdf:about="http://sandbox-api.smartplatforms.org/records/2169591/documents/632678">
      <sp:belongsTo  rdf:resource="http://sandbox-api.smartplatforms.org/records/2169591" />
      <sp:fileName>IM-0002-0001.dcm</sp:fileName>
      <dcterms:title>Heart CT Scan</dcterms:title>
      <dcterms:date>2004-09-30T12:14:00.6848</dcterms:date>
      <dcterms:format>
             <dcterms:MediaTypeOrExtent rdf:about="http://purl.org/NET/mediatypes/application/dicom">
                   <rdfs:label>application/dicom</rdfs:label>
            </dcterms:MediaTypeOrExtent>
      </dcterms:format>
      <sp:provider>
        <sp:Provider>
          <v:n>
            <v:Name>
             <v:given-name>John</v:given-name>
             <v:family-name>Smith</v:family-name>
            </v:Name>
          </v:n>
        </sp:Provider>
      </sp:provider>
      <sp:resource>
        <sp:Resource>
           <sp:location>http://sandbox-api.smartplatforms.org/records/2169591/medical_images/632678</sp:location>
           <sp:hash>
              <sp:Hash>
                 <sp:algorithm>SHA-256</sp:algorithm>
                 <sp:value>0e7981902c6c410d673771a3dd0a830712c15930bdec77701922138ea950c620</sp:value>
              </sp:Hash>
           </sp:hash>
        </sp:Resource>
      </sp:resource>
      <sp:classification>image</sp:classification>
      <sp:classification>dicom</sp:classification>
      <sp:modality>CT</sp:modality>
      <sp:bodySite>
          <sp:CodedValue>
            <dcterms:title>Entire heart (body structure)</dcterms:title>
            <sp:code>
              <sp:Code rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/302509004" >
                <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" /> 
                <dcterms:title>Entire heart (body structure)</dcterms:title>
                <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
                <dcterms:identifier>302509004</dcterms:identifier> 
              </sp:Code>        
            </sp:code>
          </sp:CodedValue>
       </sp:bodySite>
    </sp:Document>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
_:N12a1396d7902452482550a0b7e3f65e9 <http://www.w3.org/2006/vcard/ns#n> _:Na4f2533293364183927881ac25625ec2 .
_:N12a1396d7902452482550a0b7e3f65e9 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Provider> .
_:Nf652b00a9231451e97614f4ffe0a3b50 <http://smartplatforms.org/terms#location> "http://sandbox-api.smartplatforms.org/records/2169591/medical_images/632678" .
_:Nf652b00a9231451e97614f4ffe0a3b50 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Resource> .
_:Nf652b00a9231451e97614f4ffe0a3b50 <http://smartplatforms.org/terms#hash> _:Nb32ad8889a654ec18ef02631aa48b90a .
<http://purl.org/NET/mediatypes/application/dicom> <http://www.w3.org/2000/01/rdf-schema#label> "application/dicom" .
<http://purl.org/NET/mediatypes/application/dicom> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://purl.org/dc/terms/MediaTypeOrExtent> .
_:N14894c458ca04b3eab2c8712fead4063 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N14894c458ca04b3eab2c8712fead4063 <http://purl.org/dc/terms/title> "Entire heart (body structure)" .
_:N14894c458ca04b3eab2c8712fead4063 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/302509004> .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#classification> "image" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#classification> "dicom" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://purl.org/dc/terms/date> "2004-09-30T12:14:00.6848" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Document> .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://purl.org/dc/terms/title> "Heart CT Scan" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://purl.org/dc/terms/format> <http://purl.org/NET/mediatypes/application/dicom> .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#resource> _:Nf652b00a9231451e97614f4ffe0a3b50 .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#fileName> "IM-0002-0001.dcm" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#bodySite> _:N14894c458ca04b3eab2c8712fead4063 .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#modality> "CT" .
<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> <http://smartplatforms.org/terms#provider> _:N12a1396d7902452482550a0b7e3f65e9 .
_:Nb32ad8889a654ec18ef02631aa48b90a <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Hash> .
_:Nb32ad8889a654ec18ef02631aa48b90a <http://smartplatforms.org/terms#algorithm> "SHA-256" .
_:Nb32ad8889a654ec18ef02631aa48b90a <http://smartplatforms.org/terms#value> "0e7981902c6c410d673771a3dd0a830712c15930bdec77701922138ea950c620" .
_:Na4f2533293364183927881ac25625ec2 <http://www.w3.org/2006/vcard/ns#family-name> "Smith" .
_:Na4f2533293364183927881ac25625ec2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .
_:Na4f2533293364183927881ac25625ec2 <http://www.w3.org/2006/vcard/ns#given-name> "John" .
<http://purl.bioontology.org/ontology/SNOMEDCT/302509004> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/302509004> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/302509004> <http://purl.org/dc/terms/title> "Entire heart (body structure)" .
<http://purl.bioontology.org/ontology/SNOMEDCT/302509004> <http://purl.org/dc/terms/identifier> "302509004" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

<http://sandbox-api.smartplatforms.org/records/2169591/documents/632678> a sp:Document;
    dcterms:date "2004-09-30T12:14:00.6848";
    dcterms:format <http://purl.org/NET/mediatypes/application/dicom>;
    dcterms:title "Heart CT Scan";
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:bodySite [ a sp:CodedValue;
            dcterms:title "Entire heart (body structure)";
            sp:code <http://purl.bioontology.org/ontology/SNOMEDCT/302509004> ];
    sp:classification "dicom",
        "image";
    sp:fileName "IM-0002-0001.dcm";
    sp:modality "CT";
    sp:provider [ a sp:Provider;
            vcard:n [ a vcard:Name;
                    vcard:family-name "Smith";
                    vcard:given-name "John" ] ];
    sp:resource [ a sp:Resource;
            sp:hash [ a sp:Hash;
                    sp:algorithm "SHA-256";
                    sp:value "0e7981902c6c410d673771a3dd0a830712c15930bdec77701922138ea950c620" ];
            sp:location "http://sandbox-api.smartplatforms.org/records/2169591/medical_images/632678" ] .

<http://purl.bioontology.org/ontology/SNOMEDCT/302509004> a sp:Code;
    dcterms:identifier "302509004";
    dcterms:title "Entire heart (body structure)";
    sp:system "http://purl.bioontology.org/ontology/SNOMEDCT/" .

<http://purl.org/NET/mediatypes/application/dicom> a dcterms:MediaTypeOrExtent;
    rdfs:label "application/dicom" .


{% endhighlight %}</div>

<div class='json_ld'>{% highlight javascript %}
{
  "@context": "http://dev.smartplatforms.org/reference/data_model/contexts/smart_context.jsonld",
  "@graph": [
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/302509004",
      "@type": "Code",
      "dcterms__identifier": "302509004",
      "dcterms__title": "Entire heart (body structure)",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    },
    {
      "@id": "http://sandbox-api.smartplatforms.org/records/2169591/documents/632678",
      "@type": "Document",
      "belongsTo": {
        "@id": "http://sandbox-api.smartplatforms.org/records/2169591"
      },
      "bodySite": {
        "@type": "CodedValue",
        "code": {
          "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/302509004"
        },
        "dcterms__title": "Entire heart (body structure)"
      },
      "classification": [
        "image",
        "dicom"
      ],
      "dcterms__date": "2004-09-30T12:14:00.6848",
      "dcterms__format": {
        "@id": "http://purl.org/NET/mediatypes/application/dicom"
      },
      "dcterms__title": "Heart CT Scan",
      "fileName": "IM-0002-0001.dcm",
      "modality": "CT",
      "provider": {
        "@type": "Provider",
        "vcard__n": {
          "@type": "vcard__Name",
          "vcard__family_name": "Smith",
          "vcard__given_name": "John"
        }
      },
      "resource": [
        {
          "@type": "Resource",
          "hash": {
            "@type": "Hash",
            "algorithm": "SHA-256",
            "value": "0e7981902c6c410d673771a3dd0a830712c15930bdec77701922138ea950c620"
          },
          "location": "http://sandbox-api.smartplatforms.org/records/2169591/medical_images/632678"
        }
      ]
    },
    {
      "@id": "http://purl.org/NET/mediatypes/application/dicom",
      "@type": "dcterms__MediaTypeOrExtent",
      "rdfs__label": "application/dicom"
    }
  ]
}
{% endhighlight %}</div>

</div>

<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#MedicalImage</caption>
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
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

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
<br><br>
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
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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


bodySite
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#bodySite</span>
<br />
<span style='font-size: small'><a href='#Coded_Value'>Coded Value</a></span>
<br><br>
</td>
</tr>

<tr><td style='width: 30%;
'>


classification
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#classification</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


fileName
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#fileName</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


fileSize
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#fileSize</span>
<br />
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a> where unit has value: byte</span>
<br><br>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


modality
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#modality</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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
<br><br>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


resource
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#resource</span>
<br />
<span style='font-size: small'><a href='#Resource'>Resource</a></span>
<br><br>
</td>
</tr>

</table>

<h2 id='Medication'><code>Medication</code></h2>

`Medication` is a subtype of and inherits properties from:
[SMART Statement](#SMART_Statement)


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
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#frequency> _:N7cde3870716a4e9ca9ff79184473ea3c .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#instructions> "Take two tablets twice daily as needed for pain" .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#quantity> _:N6910d0b05e3a4dcd910f4decbfcc2486 .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#drugName> _:N8e1a8a5c07a84789bd5d9992a1cada17 .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#endDate> "2007-08-14" .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Medication> .
<http://sandbox-api.smartplatforms.org/records/2169591/medications/123> <http://smartplatforms.org/terms#startDate> "2007-03-14" .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/RXNORM/" .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/RxNorm_Semantic> .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://purl.org/dc/terms/title> "AMITRIPTYLINE HCL 50 MG TAB" .
<http://purl.bioontology.org/ontology/RXNORM/856845> <http://purl.org/dc/terms/identifier> "856845" .
_:N7cde3870716a4e9ca9ff79184473ea3c <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:N7cde3870716a4e9ca9ff79184473ea3c <http://smartplatforms.org/terms#value> "2" .
_:N7cde3870716a4e9ca9ff79184473ea3c <http://smartplatforms.org/terms#unit> "/d" .
_:N8e1a8a5c07a84789bd5d9992a1cada17 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/RXNORM/856845> .
_:N8e1a8a5c07a84789bd5d9992a1cada17 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N8e1a8a5c07a84789bd5d9992a1cada17 <http://purl.org/dc/terms/title> "AMITRIPTYLINE HCL 50 MG TAB" .
_:N6910d0b05e3a4dcd910f4decbfcc2486 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#ValueAndUnit> .
_:N6910d0b05e3a4dcd910f4decbfcc2486 <http://smartplatforms.org/terms#value> "2" .
_:N6910d0b05e3a4dcd910f4decbfcc2486 <http://smartplatforms.org/terms#unit> "{tablet}" .


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

<h2 id='Photograph'><code>Photograph</code></h2>

`Photograph` is a subtype of and inherits properties from:
[Document](#Document), [SMART Statement](#SMART_Statement)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Photograph</caption>
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
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

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
<br><br>
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
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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


classification
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or more</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#classification</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


fileName
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#fileName</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


fileSize
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#fileSize</span>
<br />
<span style='font-size: small'><a href='#ValueAndUnit'>ValueAndUnit</a> where unit has value: byte</span>
<br><br>
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
<br><br>
</td>
</tr>

<tr><td style='width: 30%;
font-weight: bold'>


resource
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#resource</span>
<br />
<span style='font-size: small'><a href='#Resource'>Resource</a></span>
<br><br>
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
      <sp:notes>also suggested some home exercises</sp:notes>
    </sp:Problem>
</rdf:RDF>

{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> <http://smartplatforms.org/terms#startDate> "2007-06-12" .
<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> <http://smartplatforms.org/terms#notes> "also suggested some home exercises" .
<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> <http://smartplatforms.org/terms#problemName> _:Nedfbd07d034b4d1193b9f61fe4fb8fec .
<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Problem> .
<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> <http://smartplatforms.org/terms#endDate> "2007-08-01" .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://purl.org/dc/terms/title> "Backache (finding)" .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/SNOMED> .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://purl.org/dc/terms/identifier> "161891005" .
<http://purl.bioontology.org/ontology/SNOMEDCT/161891005> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
_:Nedfbd07d034b4d1193b9f61fe4fb8fec <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/161891005> .
_:Nedfbd07d034b4d1193b9f61fe4fb8fec <http://purl.org/dc/terms/title> "Backache (finding)" .
_:Nedfbd07d034b4d1193b9f61fe4fb8fec <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://sandbox-api.smartplatforms.org/records/2169591/problems/961237> a sp:Problem;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:endDate "2007-08-01";
    sp:notes "also suggested some home exercises";
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
      "notes": "also suggested some home exercises",
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
    <sp:notes>Patient claimed to have already had an appendectomy</sp:notes>
 </sp:Procedure>
</rdf:RDF>
{% endhighlight %}</div>

<div class='n_triples'>{% highlight xml %}
<http://purl.bioontology.org/ontology/SNOMEDCT/80146002> <http://purl.org/dc/terms/title> "Appendectomy" .
<http://purl.bioontology.org/ontology/SNOMEDCT/80146002> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/80146002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/80146002> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/Procedure> .
<http://purl.bioontology.org/ontology/SNOMEDCT/80146002> <http://purl.org/dc/terms/identifier> "80146002" .
<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> <http://purl.org/dc/terms/date> "2011-02-15" .
<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> <http://smartplatforms.org/terms#procedureName> _:N14d6651ffb5e45eda5dae01c92d3d01f .
<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> <http://smartplatforms.org/terms#notes> "Patient claimed to have already had an appendectomy" .
<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Procedure> .
<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> <http://smartplatforms.org/terms#provider> _:Nedabce34ec4244a5b03bd2b21a594339 .
_:N14d6651ffb5e45eda5dae01c92d3d01f <http://purl.org/dc/terms/title> "" .
_:N14d6651ffb5e45eda5dae01c92d3d01f <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/80146002> .
_:N14d6651ffb5e45eda5dae01c92d3d01f <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Nedabce34ec4244a5b03bd2b21a594339 <http://www.w3.org/2006/vcard/ns#n> _:N9ef0a023cb1442d394cfc1823122da34 .
_:Nedabce34ec4244a5b03bd2b21a594339 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Provider> .
_:N9ef0a023cb1442d394cfc1823122da34 <http://www.w3.org/2006/vcard/ns#family-name> "Mandel" .
_:N9ef0a023cb1442d394cfc1823122da34 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Name> .
_:N9ef0a023cb1442d394cfc1823122da34 <http://www.w3.org/2006/vcard/ns#given-name> "Joshua" .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .

<http://sandbox-api.smartplatforms.org/records/2169591/procedures/5897235> a sp:Procedure;
    dcterms:date "2011-02-15";
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:notes "Patient claimed to have already had an appendectomy";
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
      "notes": "Patient claimed to have already had an appendectomy",
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
font-weight: bold'>


date
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
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
          <dcterms:title>Former smoker</dcterms:title>      
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
<http://purl.bioontology.org/ontology/SNOMEDCT/8517006> <http://purl.org/dc/terms/title> "Former smoker" .
<http://purl.bioontology.org/ontology/SNOMEDCT/8517006> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/SmokingStatus> .
<http://purl.bioontology.org/ontology/SNOMEDCT/8517006> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/8517006> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/8517006> <http://purl.org/dc/terms/identifier> "8517006" .
<http://sandbox-api.smartplatforms.org/records/2169591/social_history> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#SocialHistory> .
<http://sandbox-api.smartplatforms.org/records/2169591/social_history> <http://smartplatforms.org/terms#smokingStatus> _:N46174ea4d89d425aaa0594e5ca419229 .
<http://sandbox-api.smartplatforms.org/records/2169591/social_history> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
_:N46174ea4d89d425aaa0594e5ca419229 <http://purl.org/dc/terms/title> "Former smoker" .
_:N46174ea4d89d425aaa0594e5ca419229 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N46174ea4d89d425aaa0594e5ca419229 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/8517006> .


{% endhighlight %}</div>

<div class='turtle'>{% highlight xml %}
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix sp: <http://smartplatforms.org/terms#> .
@prefix spcode: <http://smartplatforms.org/terms/codes/> .

<http://sandbox-api.smartplatforms.org/records/2169591/social_history> a sp:SocialHistory;
    sp:belongsTo <http://sandbox-api.smartplatforms.org/records/2169591>;
    sp:smokingStatus [ a sp:CodedValue;
            dcterms:title "Former smoker";
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
        "dcterms__title": "Former smoker"
      }
    },
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/8517006",
      "@type": [
        "spcode__SmokingStatus",
        "Code"
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
        <sp:value>180</sp:value>
        <sp:unit>cm</sp:unit>
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
        <sp:value>56.4</sp:value>
        <sp:unit>cm</sp:unit>
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
_:N2787604f0b19472aa180cca608ddd846 <http://purl.org/dc/terms/title> "Body weight" .
_:N2787604f0b19472aa180cca608ddd846 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/3141-9> .
_:N2787604f0b19472aa180cca608ddd846 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://purl.org/dc/terms/title> "Right arm" .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://purl.org/dc/terms/identifier> "368209003" .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/BloodPressureBodySite> .
<http://purl.bioontology.org/ontology/SNOMEDCT/368209003> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
_:N661865189e3a4fd18a787e6de03c2a3b <http://purl.org/dc/terms/title> "Intravascular diastolic" .
_:N661865189e3a4fd18a787e6de03c2a3b <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8462-4> .
_:N661865189e3a4fd18a787e6de03c2a3b <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Nc7d43fbe1a3240cfbe841769aff4eaa0 <http://smartplatforms.org/terms#value> "37" .
_:Nc7d43fbe1a3240cfbe841769aff4eaa0 <http://smartplatforms.org/terms#vitalName> _:Ndb7f2f1398984881b048e54fb279c1cb .
_:Nc7d43fbe1a3240cfbe841769aff4eaa0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:Nc7d43fbe1a3240cfbe841769aff4eaa0 <http://smartplatforms.org/terms#unit> "Cel" .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://purl.org/dc/terms/title> "Oxygen saturation" .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://purl.org/dc/terms/identifier> "2710-2" .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/2710-2> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
_:N4502a5b6226a4d969a30a69f75aa35ee <http://purl.org/dc/terms/title> "Right arm" .
_:N4502a5b6226a4d969a30a69f75aa35ee <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/368209003> .
_:N4502a5b6226a4d969a30a69f75aa35ee <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N2b74cedb019047f0b95a46d0b8f555b5 <http://purl.org/dc/terms/title> "Head circumference" .
_:N2b74cedb019047f0b95a46d0b8f555b5 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8287-5> .
_:N2b74cedb019047f0b95a46d0b8f555b5 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N9993327dd15747708ad0afa076a88d43 <http://purl.org/dc/terms/title> "Respiration rate" .
_:N9993327dd15747708ad0afa076a88d43 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/9279-1> .
_:N9993327dd15747708ad0afa076a88d43 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N01dc00843d9241e5a32a81ee2c7a7554 <http://smartplatforms.org/terms#value> "21.8" .
_:N01dc00843d9241e5a32a81ee2c7a7554 <http://smartplatforms.org/terms#vitalName> _:Naecbf7ad1f3e4ca09f68de192de106ec .
_:N01dc00843d9241e5a32a81ee2c7a7554 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:N01dc00843d9241e5a32a81ee2c7a7554 <http://smartplatforms.org/terms#unit> "kg/m2" .
_:N219976ec59e4435a9ce424e96e867bfa <http://smartplatforms.org/terms#value> "70" .
_:N219976ec59e4435a9ce424e96e867bfa <http://smartplatforms.org/terms#vitalName> _:N6690da7940a74a01b8ea02c1d26a7107 .
_:N219976ec59e4435a9ce424e96e867bfa <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:N219976ec59e4435a9ce424e96e867bfa <http://smartplatforms.org/terms#unit> "{beats}/min" .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://purl.org/dc/terms/title> "Intravascular systolic" .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://purl.org/dc/terms/identifier> "8480-6" .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8480-6> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
_:N6f94ddde37334b2bb67f428edc89e471 <http://purl.org/dc/terms/title> "Body height" .
_:N6f94ddde37334b2bb67f428edc89e471 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8302-2> .
_:N6f94ddde37334b2bb67f428edc89e471 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N42d744dfacb94854a98b0b90ee7eef04 <http://smartplatforms.org/terms#value> "99" .
_:N42d744dfacb94854a98b0b90ee7eef04 <http://smartplatforms.org/terms#vitalName> _:N0ad034db048e4035b4b85f31544dc061 .
_:N42d744dfacb94854a98b0b90ee7eef04 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:N42d744dfacb94854a98b0b90ee7eef04 <http://smartplatforms.org/terms#unit> "%{HemoglobinSaturation}" .
_:Nac2d05246f0c4ea48ebf64e1eddfab76 <http://smartplatforms.org/terms#value> "180" .
_:Nac2d05246f0c4ea48ebf64e1eddfab76 <http://smartplatforms.org/terms#vitalName> _:N6f94ddde37334b2bb67f428edc89e471 .
_:Nac2d05246f0c4ea48ebf64e1eddfab76 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:Nac2d05246f0c4ea48ebf64e1eddfab76 <http://smartplatforms.org/terms#unit> "cm" .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#encounterType> _:Nf0ce340f316448258d1c7d56b9d7e35f .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#startDate> "2010-05-12T04:00:00Z" .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Encounter> .
<http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> <http://smartplatforms.org/terms#endDate> "2010-05-12T04:20:00Z" .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://purl.org/dc/terms/title> "Body mass index" .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://purl.org/dc/terms/identifier> "39156-5" .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/39156-5> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://purl.org/dc/terms/title> "Body weight" .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://purl.org/dc/terms/identifier> "3141-9" .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/3141-9> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://purl.org/dc/terms/title> "Intravascular diastolic" .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://purl.org/dc/terms/identifier> "8462-4" .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8462-4> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
_:Nc1fbeb599f1c4a87902f662b21374a86 <http://smartplatforms.org/terms#value> "70.8" .
_:Nc1fbeb599f1c4a87902f662b21374a86 <http://smartplatforms.org/terms#vitalName> _:N2787604f0b19472aa180cca608ddd846 .
_:Nc1fbeb599f1c4a87902f662b21374a86 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:Nc1fbeb599f1c4a87902f662b21374a86 <http://smartplatforms.org/terms#unit> "kg" .
_:N71c617955e6742a683d1345ce248bd19 <http://smartplatforms.org/terms#value> "132" .
_:N71c617955e6742a683d1345ce248bd19 <http://smartplatforms.org/terms#vitalName> _:Nad65d6a9dd2549c792164d7ad25d6b24 .
_:N71c617955e6742a683d1345ce248bd19 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:N71c617955e6742a683d1345ce248bd19 <http://smartplatforms.org/terms#unit> "mm[Hg]" .
_:Nac1f6f99de8b422d9f984100f1c5756a <http://smartplatforms.org/terms#value> "16" .
_:Nac1f6f99de8b422d9f984100f1c5756a <http://smartplatforms.org/terms#vitalName> _:N9993327dd15747708ad0afa076a88d43 .
_:Nac1f6f99de8b422d9f984100f1c5756a <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:Nac1f6f99de8b422d9f984100f1c5756a <http://smartplatforms.org/terms#unit> "{breaths}/min" .
_:N9ffba3ef2a2e4d4f9309924b5520d395 <http://smartplatforms.org/terms#value> "56.4" .
_:N9ffba3ef2a2e4d4f9309924b5520d395 <http://smartplatforms.org/terms#vitalName> _:N2b74cedb019047f0b95a46d0b8f555b5 .
_:N9ffba3ef2a2e4d4f9309924b5520d395 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:N9ffba3ef2a2e4d4f9309924b5520d395 <http://smartplatforms.org/terms#unit> "cm" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/title> "Ambulatory encounter" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://purl.org/dc/terms/identifier> "ambulatory" .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/EncounterType> .
<http://smartplatforms.org/terms/codes/EncounterType#ambulatory> <http://smartplatforms.org/terms#system> "http://smartplatforms.org/terms/codes/EncounterType#" .
_:Ndb7f2f1398984881b048e54fb279c1cb <http://purl.org/dc/terms/title> "Body temperature" .
_:Ndb7f2f1398984881b048e54fb279c1cb <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8310-5> .
_:Ndb7f2f1398984881b048e54fb279c1cb <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Nad65d6a9dd2549c792164d7ad25d6b24 <http://purl.org/dc/terms/title> "Intravascular systolic" .
_:Nad65d6a9dd2549c792164d7ad25d6b24 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8480-6> .
_:Nad65d6a9dd2549c792164d7ad25d6b24 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Nfe25e489b56f472595ab72c799940dd8 <http://smartplatforms.org/terms#value> "82" .
_:Nfe25e489b56f472595ab72c799940dd8 <http://smartplatforms.org/terms#vitalName> _:N661865189e3a4fd18a787e6de03c2a3b .
_:Nfe25e489b56f472595ab72c799940dd8 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSign> .
_:Nfe25e489b56f472595ab72c799940dd8 <http://smartplatforms.org/terms#unit> "mm[Hg]" .
_:Naecbf7ad1f3e4ca09f68de192de106ec <http://purl.org/dc/terms/title> "Body mass index" .
_:Naecbf7ad1f3e4ca09f68de192de106ec <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/39156-5> .
_:Naecbf7ad1f3e4ca09f68de192de106ec <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Ncdb0fe83669e4c0192a8bf68671d5e27 <http://purl.org/dc/terms/title> "Sitting" .
_:Ncdb0fe83669e4c0192a8bf68671d5e27 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/SNOMEDCT/33586001> .
_:Ncdb0fe83669e4c0192a8bf68671d5e27 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:Nf0ce340f316448258d1c7d56b9d7e35f <http://purl.org/dc/terms/title> "Ambulatory encounter" .
_:Nf0ce340f316448258d1c7d56b9d7e35f <http://smartplatforms.org/terms#code> <http://smartplatforms.org/terms/codes/EncounterType#ambulatory> .
_:Nf0ce340f316448258d1c7d56b9d7e35f <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
_:N6690da7940a74a01b8ea02c1d26a7107 <http://purl.org/dc/terms/title> "Heart rate" .
_:N6690da7940a74a01b8ea02c1d26a7107 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/8867-4> .
_:N6690da7940a74a01b8ea02c1d26a7107 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://purl.org/dc/terms/title> "Body height" .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://purl.org/dc/terms/identifier> "8302-2" .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8302-2> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://purl.org/dc/terms/title> "Body temperature" .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://purl.org/dc/terms/identifier> "8310-5" .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8310-5> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#heartRate> _:N219976ec59e4435a9ce424e96e867bfa .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#oxygenSaturation> _:N42d744dfacb94854a98b0b90ee7eef04 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#headCircumference> _:N9ffba3ef2a2e4d4f9309924b5520d395 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#temperature> _:Nc7d43fbe1a3240cfbe841769aff4eaa0 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#VitalSignSet> .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#height> _:Nac2d05246f0c4ea48ebf64e1eddfab76 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#weight> _:Nc1fbeb599f1c4a87902f662b21374a86 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#encounter> <http://sandbox-api.smartplatforms.org/records/2169591/encounters/252352> .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#belongsTo> <http://sandbox-api.smartplatforms.org/records/2169591> .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#bodyMassIndex> _:N01dc00843d9241e5a32a81ee2c7a7554 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#bloodPressure> _:N99eaf0c6fd7640c1ade43ed7f54d3103 .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://smartplatforms.org/terms#respiratoryRate> _:Nac1f6f99de8b422d9f984100f1c5756a .
<http://sandbox-api.smartplatforms.org/records/2169591/vital_sign_sets/823523> <http://purl.org/dc/terms/date> "2010-05-12T04:00:00Z" .
<http://purl.bioontology.org/ontology/LNC/8287-5> <http://purl.org/dc/terms/title> "Head circumference" .
<http://purl.bioontology.org/ontology/LNC/8287-5> <http://purl.org/dc/terms/identifier> "8287-5" .
<http://purl.bioontology.org/ontology/LNC/8287-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8287-5> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8287-5> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://purl.org/dc/terms/title> "Sitting" .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://purl.org/dc/terms/identifier> "33586001" .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/BloodPressureBodyPosition> .
<http://purl.bioontology.org/ontology/SNOMEDCT/33586001> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/SNOMEDCT/" .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://purl.org/dc/terms/title> "Heart rate" .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://purl.org/dc/terms/identifier> "8867-4" .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/8867-4> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://purl.org/dc/terms/title> "Respiration rate" .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://purl.org/dc/terms/identifier> "9279-1" .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#Code> .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms/codes/VitalSign> .
<http://purl.bioontology.org/ontology/LNC/9279-1> <http://smartplatforms.org/terms#system> "http://purl.bioontology.org/ontology/LNC/" .
_:N99eaf0c6fd7640c1ade43ed7f54d3103 <http://smartplatforms.org/terms#bodySite> _:N4502a5b6226a4d969a30a69f75aa35ee .
_:N99eaf0c6fd7640c1ade43ed7f54d3103 <http://smartplatforms.org/terms#systolic> _:N71c617955e6742a683d1345ce248bd19 .
_:N99eaf0c6fd7640c1ade43ed7f54d3103 <http://smartplatforms.org/terms#bodyPosition> _:Ncdb0fe83669e4c0192a8bf68671d5e27 .
_:N99eaf0c6fd7640c1ade43ed7f54d3103 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#BloodPressure> .
_:N99eaf0c6fd7640c1ade43ed7f54d3103 <http://smartplatforms.org/terms#diastolic> _:Nfe25e489b56f472595ab72c799940dd8 .
_:N0ad034db048e4035b4b85f31544dc061 <http://purl.org/dc/terms/title> "Oxygen saturation" .
_:N0ad034db048e4035b4b85f31544dc061 <http://smartplatforms.org/terms#code> <http://purl.bioontology.org/ontology/LNC/2710-2> .
_:N0ad034db048e4035b4b85f31544dc061 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://smartplatforms.org/terms#CodedValue> .


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
            sp:unit "cm";
            sp:value "56.4";
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
            sp:unit "cm";
            sp:value "180";
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
      "@id": "http://purl.bioontology.org/ontology/LNC/9279-1",
      "@type": [
        "Code",
        "spcode__VitalSign"
      ],
      "dcterms__identifier": "9279-1",
      "dcterms__title": "Respiration rate",
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
        "unit": "cm",
        "value": "56.4",
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
        "unit": "cm",
        "value": "180",
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
      "@id": "http://purl.bioontology.org/ontology/LNC/8480-6",
      "@type": [
        "Code",
        "spcode__VitalSign"
      ],
      "dcterms__identifier": "8480-6",
      "dcterms__title": "Intravascular systolic",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/8462-4",
      "@type": [
        "Code",
        "spcode__VitalSign"
      ],
      "dcterms__identifier": "8462-4",
      "dcterms__title": "Intravascular diastolic",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/SNOMEDCT/33586001",
      "@type": [
        "Code",
        "spcode__BloodPressureBodyPosition"
      ],
      "dcterms__identifier": "33586001",
      "dcterms__title": "Sitting",
      "system": "http://purl.bioontology.org/ontology/SNOMEDCT/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/2710-2",
      "@type": [
        "Code",
        "spcode__VitalSign"
      ],
      "dcterms__identifier": "2710-2",
      "dcterms__title": "Oxygen saturation",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/8287-5",
      "@type": [
        "Code",
        "spcode__VitalSign"
      ],
      "dcterms__identifier": "8287-5",
      "dcterms__title": "Head circumference",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/8310-5",
      "@type": [
        "Code",
        "spcode__VitalSign"
      ],
      "dcterms__identifier": "8310-5",
      "dcterms__title": "Body temperature",
      "system": "http://purl.bioontology.org/ontology/LNC/"
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
        "Code",
        "spcode__VitalSign"
      ],
      "dcterms__identifier": "8867-4",
      "dcterms__title": "Heart rate",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/39156-5",
      "@type": [
        "Code",
        "spcode__VitalSign"
      ],
      "dcterms__identifier": "39156-5",
      "dcterms__title": "Body mass index",
      "system": "http://purl.bioontology.org/ontology/LNC/"
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/8302-2",
      "@type": [
        "Code",
        "spcode__VitalSign"
      ],
      "dcterms__identifier": "8302-2",
      "dcterms__title": "Body height",
      "system": "http://purl.bioontology.org/ontology/LNC/"
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
    },
    {
      "@id": "http://purl.bioontology.org/ontology/LNC/3141-9",
      "@type": [
        "Code",
        "spcode__VitalSign"
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
<span style='font-size: small'><a href='#VitalSign'>VitalSign</a> where unit has value: cm</span>
<br><br>Patient's height in centimeters.  
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

<h2 id='Content'><code>Content</code></h2>

`Content` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Content</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


encoding
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#encoding</span>
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

<h2 id='DataType'><code>DataType</code></h2>

`DataType` is a subtype of and inherits properties from:
[Component](#Component)



<h2 id='Hash'><code>Hash</code></h2>

`Hash` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Hash</caption>
<tbody>
<tr><td style='width: 30%;
font-weight: bold'>


algorithm
<br />
<span style='font-size: small; font-weight: normal'>Required: exactly 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#algorithm</span>
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

<h2 id='MediaTypeOrExtent'><code>MediaTypeOrExtent</code></h2>

`MediaTypeOrExtent` is a subtype of and inherits properties from:
[Component](#Component), [DataType](#DataType)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://purl.org/dc/terms/MediaTypeOrExtent</caption>
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
Date of birth as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


deathdate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#deathdate</span>
<br />
Date of death as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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
Date of birth as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


deathdate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#deathdate</span>
<br />
Date of death as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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

<h2 id='Resource'><code>Resource</code></h2>

`Resource` is a subtype of and inherits properties from:
[Component](#Component)



<table class='table table-striped'>
<caption align='bottom' style='font-style: italic'>http://smartplatforms.org/terms#Resource</caption>
<tbody>
<tr><td style='width: 30%;
'>


content
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#content</span>
<br />
<span style='font-size: small'><a href='#Content'>Content</a></span>
<br><br>
</td>
</tr>

<tr><td style='width: 30%;
'>


hash
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#hash</span>
<br />
<span style='font-size: small'><a href='#Hash'>Hash</a></span>
<br><br>
</td>
</tr>

<tr><td style='width: 30%;
'>


location
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://smartplatforms.org/terms#location</span>
<br />
 <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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
Date of birth as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


deathdate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#deathdate</span>
<br />
Date of death as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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


<h2 id='Scratchpad_Data'><code>Scratchpad Data</code></h2>


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
Date of birth as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
</td>
</tr>

<tr><td style='width: 30%;
'>


deathdate
<br />
<span style='font-size: small; font-weight: normal'>Optional: 0 or 1</span>
</td>
<td style='width: 70%'>
<span style='font-size: small'>http://www.w3.org/2006/vcard/ns#deathdate</span>
<br />
Date of death as an ISO-8601 string <a href='http://www.w3.org/2000/01/rdf-schema#Literal'>rdfs:Literal</a>
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


Constrained to one of: 
 {% highlight xml %}


<spcode:ProblemStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/55561003">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Active</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>55561003</dcterms:identifier>
</spcode:ProblemStatus>



<spcode:ProblemStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/73425007">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Inactive</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>73425007</dcterms:identifier>
</spcode:ProblemStatus>



<spcode:ProblemStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/413322009">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Resolved</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>413322009</dcterms:identifier>
</spcode:ProblemStatus>

{% endhighlight %}


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
  <dcterms:title>Unknown if ever smoked</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>266927001</dcterms:identifier>
</spcode:SmokingStatus>



<spcode:SmokingStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/8517006">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Former smoker</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>8517006</dcterms:identifier>
</spcode:SmokingStatus>



<spcode:SmokingStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/266919005">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Never smoker</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>266919005</dcterms:identifier>
</spcode:SmokingStatus>



<spcode:SmokingStatus rdf:about="http://purl.bioontology.org/ontology/SNOMEDCT/428041000124106">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Current some day smoker</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/SNOMEDCT/</sp:system>
  <dcterms:identifier>428041000124106</dcterms:identifier>
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



<spcode:VitalSign rdf:about="http://purl.bioontology.org/ontology/LNC/8287-5">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>Head circumference</dcterms:title>
  <sp:system>http://purl.bioontology.org/ontology/LNC/</sp:system>
  <dcterms:identifier>8287-5</dcterms:identifier>
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
