var examples = [ {
  id: 'q_med_names',
  width:54,
  height:14,
  q: 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n\
PREFIX sp: <http://smartplatforms.org/terms#>\n\
PREFIX dcterms: <http://purl.org/dc/terms/>\n\
\n\
SELECT  DISTINCT ?t\n\
WHERE {\n\
  ?m rdf:type sp:Medication .\n\
  ?m sp:drugName ?medc.\n\
  ?medc dcterms:title ?t.\n\
}'
},
{
  id: 'q_med_quants',
  width:54,
  height:23,
  q: 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n\
PREFIX sp: <http://smartplatforms.org/terms#>\n\
PREFIX dcterms: <http://purl.org/dc/terms/>\n\
\n\
SELECT  ?t ?quant_val ?quant_unit ?freq_val ?freq_unit\n\
WHERE {\n\
  ?m rdf:type sp:Medication .\n\
  ?m sp:drugName ?medc.\n\
  ?medc dcterms:title ?t.\n\
  ?m sp:quantity ?q.\n\
  ?q sp:value ?quant_val.\n\
  ?q sp:unit ?quant_unit.\n\
  ?m sp:frequency ?f.\n\
  ?f sp:value ?freq_val.\n\
  ?f sp:unit ?freq_unit.\n\
}'
},
{
  id: 'q_med_dates',
  width:54,
  height:18,
  q: 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n\
PREFIX sp: <http://smartplatforms.org/terms#>\n\
PREFIX dcterms: <http://purl.org/dc/terms/>\n\
SELECT  distinct ?t ?fill_date\n\
WHERE {\n\
  ?m rdf:type sp:Medication .\n\
  ?m sp:drugName ?medc.\n\
  ?medc dcterms:title ?t.\n\
  ?m sp:fulfillment ?fill.\n\
  ?f dcterms:date ?fill_date.\n\
}'
},
{
  id: 'q_med_since',
  width:54,
  height:18,
  q: 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n\
PREFIX sp: <http://smartplatforms.org/terms#>\n\
PREFIX dcterms: <http://purl.org/dc/terms/>\n\
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n\
SELECT  distinct ?t\n\
WHERE {\n\
  ?m rdf:type sp:Medication .\n\
  ?m sp:drugName ?medc.\n\
  ?medc dcterms:title ?t.\n\
  ?m sp:fulfillment ?fill.\n\
  ?f dcterms:date ?fill_date.\n\
  FILTER( xsd:dateTime(?fill_date) > "2009-01-01T00:00:00Z"^^xsd:dateTime )\n\
} ORDER BY (?t)'
},
{
  id: 'q_demographics',
  s: 'demographics',
  b: 'Run query on SMART Demographics data',
  width:54,
  height:18,
  q: 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n\
PREFIX sp: <http://smartplatforms.org/terms#>\n\
PREFIX dcterms: <http://purl.org/dc/terms/>\n\
PREFIX foaf: <http://xmlns.com/foaf/0.1/>\n\
PREFIX v: <http://www.w3.org/2006/vcard/ns#>\n\
SELECT ?fn ?ln\n\
WHERE {\n\
  ?d rdf:type sp:Demographics.\n\
  ?d v:n ?name.\n\
  ?name v:given-name ?fn.\n\
  ?name v:family-name ?ln.\n\
}'
},
{
  id: 'q_problems',
  s: 'problems',
  b: 'Run query on SMART Problems data',
  width:54,
  height:14,
  q: 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n\
PREFIX sp: <http://smartplatforms.org/terms#>\n\
PREFIX dcterms: <http://purl.org/dc/terms/>\n\
\n\
SELECT distinct ?p\n\
WHERE {\n\
 ?pr rdf:type sp:Problem .\n\
 ?pr sp:problemName ?pn .\n\
 ?pn dcterms:title ?p .\n\
} ORDER BY ?p'
},
{
  id: 'q_labs',
  width:54,
  height:61,
  q: 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n\
PREFIX sp: <http://smartplatforms.org/terms#> \n\
PREFIX dcterms: <http://purl.org/dc/terms/> \n\
PREFIX foaf:<http://xmlns.com/foaf/0.1/> \n\
PREFIX v:<http://www.w3.org/2006/vcard/ns#> \n\
SELECT  DISTINCT ?loinc_title ?value ?unit ?minvalue ?minunit ?maxvalue ?maxunit \n\
WHERE { \n\
\n\
    ?lr rdf:type sp:LabResult. \n\
    ?lr sp:labName ?labName . \n\
    ?labName dcterms:title ?loinc_title . \n\
    ?lr sp:quantitativeResult ?quantitativeResult . \n\
    ?quantitativeResult sp:valueAndUnit ?valueAndUnit . \n\
    ?valueAndUnit sp:value ?value . \n\
    ?valueAndUnit sp:unit ?unit . \n\
\n\
  OPTIONAL{\n\
    ?labName sp:codeProvenance ?codeProvenance .\n\
    ?codeProvenance dcterms:title ?lab_title.\n\
  } \n\
  OPTIONAL {\n\
    ?quantitativeResult sp:normalRange ?normalRange .\n\
    ?normalRange sp:minimum ?minimum . \n\
    ?minimum sp:value ?minvalue . \n\
    ?minimum sp:unit ?minunit . \n\
    ?normalRange sp:maximum ?maximum . \n\
    ?maximum sp:value ?maxvalue . \n\
    ?maximum sp:unit ?maxunit . \n\
  } \n\
  OPTIONAL{\n\
    ?quantitativeResult sp:nonCriticalRange ?nonCriticalRange .\n\
    ?nonCriticalRange sp:minimum ?ncrminimum .\n\
    ?ncrminimum sp:value ?ncrminvalue .\n\
    ?ncrminimum sp:unit ?ncrminunit .\n\
  } \n\
  OPTIONAL{\n\
    ?lr sp:status ?status .\n\
    ?status dcterms:title ?status_title .\n\
  } \n\
  OPTIONAL{\n\
    ?lr sp:abnormalInterpretation ?abnormalInterpretation.\n\
    ?abnormalInterpretation dcterms:title ?interpretation_title .\n\
  }\n\
}'
}
]
