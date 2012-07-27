# Generate SMART wiki api docs for use with our Jekyll-based docs site

# how to run:
# (from top of smart-docs-testing repo)
# $ export PYTHONPATH=.:..
# $ python utils/wiki_apidocs.py payload > payload
# $ python utils/wiki_apidocs.py api > api
# (copy payload document into static api document at the appropriate section)

DEBUG = False

import copy
import sys
import yaml
import pprint
import os

# setup the ontology
from smart_common.rdf_tools.rdf_ontology import *
from smart_common.rdf_tools.util import bound_graph, URIRef

# setup the json-ld serializer
sys.path.append('./utils/rdflib-jsonld')

sys.path.append(
  os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rdflib-jsonld')
)


import rdflib_jsonld
from rdflib import plugin
from rdflib.serializer import Serializer
plugin.register('json-ld',
                Serializer,
                'rdflib_jsonld.jsonld_serializer',
                'JsonLDSerializer')


f = None
try:
    f = open(os.getcwd()+'/_config.yml').read()
except:
    raise IOError, "Can't read _config.yml"

if f != None:
    config = yaml.load(f)

SP_STATMENT = "http://smartplatforms.org/terms#Statement"
CONTEXT_URI = config['production_url']+'/reference/datamodel/contexts/smart_context.jsonld'

# create smart_jsonld_context, copied from smart_sample_apps
# could be in smart_common
seen = {}
context = {}
ns = SMART_Class[SP_STATMENT].graph.namespace_manager

def add_term(uri):
    if not isinstance(uri, rdflib.URIRef):
        return

    jname = ns.normalizeUri(uri)
    jname = jname.replace("sp:", "")
    jname = jname.replace(":", "__")
    jname = jname.replace("-","_")
    assert jname not in seen or seen[jname]==uri, \
        "predicate appears in >1 vocab: %s, %s"%(uri, seen[jname])
    seen[jname] = uri
    context[jname] = {"@id": str(uri)}
    return jname

for c in SMART_Class.store.values():
    if not isinstance(c, SMART_Class):
        continue
    add_term(c.uri)

    for p in c.object_properties + c.data_properties:
        added = add_term(p.uri)
        if p.multiple_cardinality:
            context[added]["@container"] = "@set"

if DEBUG:
    print "context:\n "
    pprint.pprint(context)

def strip_smart(s):
    return s.replace("http://smartplatforms.org", "")

def type_start(t):
    name = type_name_string(t)
    if (sp.Code in [x.uri for x in t.parents]):
        name += " code"

    description = t.description
    example = t.example
    name_id = name.replace(' ', '_')

    # add <span id='name'> to these <h2>'s for internal anchors
    print "\n## <span id='%s'>`%s`</span>\n" % (name_id, name)

    if len(t.parents) > 0:
        print "`%s` is a subtype of and inherits properties from:" % type_name_string(t)

        parents = []
        for p in sorted(t.parents, key=lambda x: type_name_string(x)):
            parents.append("[%s](#%s)"%(type_name_string(p),type_name_string(p).replace(' ', '_')))
        print ", ".join(parents)
        print "\n" 

    if description: print "%s"%description+"\n"

    if t.equivalent_classes:
        ec = filter(lambda x: x.one_of, t.equivalent_classes)
        print 'Constrained to one of: \n {% highlight xml %}'
        for member in [x for c in ec for x in c.one_of]:
            ts  = filter(lambda x: x != owl.NamedIndividual, member.type)
            identifier = split_uri(member.uri)
            system = str(member.uri).split(identifier)[0]
            spcode = split_uri(str(t.uri))

            print """\n
<spcode:%s rdf:about="%s">
  <rdf:type rdf:resource="http://smartplatforms.org/terms#Code" />
  <dcterms:title>%s</dcterms:title>
  <sp:system>%s</sp:system>
  <dcterms:identifier>%s</dcterms:identifier>
</spcode:%s>\n""" % (spcode, str(member.uri), member.title, system, identifier, spcode)

        print """{% endhighlight %}\n"""

    if example:
        print "<div id='%s'>" % ( name_id+ "_examples")
        print """
<div class='format_tabs'>
  <ul class="nav nav-tabs" data-tabs="tabs">
    <li style="margin-left: 0px;">Show example in</li>
    <li class="active"><a href="" data-target="#%s_examples > div.rdf_xml" data-toggle="tab">RDF/XML</a></li>
    <li class="">      <a href="" data-target="#%s_examples > div.n_triples" data-toggle="tab">N-Triples</a></li>
    <li class="">      <a href="" data-target="#%s_examples > div.turtle" data-toggle="tab">Turtle</a></li>
    <li class="">      <a href="" data-target="#%s_examples > div.json_ld" data-toggle="tab">JSON-LD</a></li>
  </ul>
</div>
        """ % (name_id, name_id, name_id, name_id)

        print "<div class='rdf_xml active'>{%% highlight xml %%}\n%s\n{%% endhighlight %%}</div>\n"%example
        try:
            ex_graph = parse_rdf(example)
        except:
            return
        print "<div class='n_triples'>{%% highlight xml %%}\n%s\n{%% endhighlight %%}</div>\n"%ex_graph.serialize(format='nt')
        print "<div class='turtle'>{%% highlight xml %%}\n%s\n{%% endhighlight %%}</div>\n"%ex_graph.serialize(format='turtle')

        print "<div class='json_ld'>{%% highlight javascript %%}\n%s\n{%% endhighlight %%}</div>\n"%ex_graph.serialize(
            format='json-ld', indent=2, context=context, context_uri=CONTEXT_URI
        )
        print "</div>"
def properties_start(type):
    print """\n<table class='table table-striped'>\n<caption align='bottom' style='font-style: italic'>%s</caption>\n<tbody>""" % type

def properties_row(property, uri,card, description, required_p):
    print "<tr><td style='width: 30%;"

    if required_p:
        print "font-weight: bold'>"
    else:
        print "'>"

    print """\n
%s
<br />
<span style='font-size: small; font-weight: normal'>%s</span>
</td>
<td style='width: 70%%'>
<span style='font-size: small'>%s</span>
<br />
%s
</td>
</tr>\n"""%(property, card, uri, description)


def properties_end():
    print """</table>"""

def wiki_batch_start(batch):
    print "\n# %s\n"%batch

def type_name_string(t):
    if t.name:
        return str(t.name)
    return split_uri(str(t.uri))

def split_uri(t):
    try: 
        return str(t).rsplit("#",1)[1]
    except:
        try: 
            return str(t).rsplit("/",1)[1]
        except: 
            return ""
    
def wiki_payload_for_type(t):
    type_start(t)    
    wiki_properties_for_type(t)

cardinalities  = {"0 - 1": "Optional: 0 or 1", 
                  "0 - Many": "Optional: 0 or more", 
                  "1": "Required: exactly 1", 
                  "1 - Many": "Required: 1 or more"}
    
def wiki_properties_for_type(t):
    if len(t.object_properties) + len(t.data_properties) == 0:
        return
    properties_start(t.uri)
    for c in sorted(t.object_properties + t.data_properties, key=lambda r: str(r.uri)):
        name = type_name_string(c)
        desc = c.description
        m = bound_graph().namespace_manager
        uri = '['+str(t.uri)+' '+m.normalizeUri(t.uri)+']'

        if type(c) is OWL_ObjectProperty:
            is_code = sp.Code in [p.uri for p in c.to_class.parents] and " code" or ""
            targetname = type_name_string(c.to_class)+ is_code

            desc = "<span style='font-size: small'><a href='#%s'>%s</a>" % (targetname.replace(' ', '_'), targetname)
            further = filter(lambda x: isinstance(x.all_values_from, OWL_Restriction), c.restrictions)
            for f in further:
                p = split_uri(str(f.all_values_from.on_property))
                avf = f.all_values_from
                if avf.has_value:
                    desc += " where "+ p + " has value: %s"%avf.has_value
                else:
                    pc = avf.all_values_from
                    pc = type_name_string(pc)
                    desc += " where "+ p +   " comes from <a href='#%s'>%s</a>"%(pc,pc)

            desc += '</span>\n<br><br>'
            if c.description:
                desc += c.description

        elif type(c) is OWL_DataProperty:
            avf = filter(lambda x: x.all_values_from, c.restrictions)
            if len(avf) >0:
              u = avf[0].all_values_from.uri
              d = "<a href='"+str(u)+"'>"+m.normalizeUri(u)+'</a>'
            else: d =  "<a href='"+str(rdfs.Literal)+"'>"+m.normalizeUri(rdfs.Literal)+'</a>'
            desc += " "+ d
            
        cardinality = cardinalities[c.cardinality_string]
        required_p = False
        if c.cardinality_string[0] == '1':
          required_p = True

        properties_row(name, c.uri, cardinality, desc, required_p)
    properties_end()
    
def wiki_api_for_type(t, calls_for_t):
    print "\n## %s\n"%t.name

    last_description = ""
    for call in calls_for_t:
        if (str(call.method) != "GET"): continue # Document only the GET calls for now!
        if (str(call.description) != last_description):
            print str(call.description)
        
        print "\n    ", strip_smart(str(call.method)), str(call.path)
        
        if (str(call.description) != last_description):
            print ""
            last_description = str(call.description)

    print "\n[%s RDF](../data_model/#%s)"%(t.name, t.name.replace(' ', '_'))        

             
main_types = []
calls_to_document = copy.copy(api_calls)
            
for t in api_types:
    if t.is_statement or len(t.calls) > 0:
        main_types.append(t)
    elif (sp.Component in [x.uri for x in t.parents]):
        main_types.append(t)

def type_sort_order(x): 
    if x.is_statement or len(x.calls) > 0:
        is_record = filter(lambda x: "record" in x, [c.category for c in x.calls])
        if len(is_record) > 0 or len(x.calls) == 0:
            return "Clinical Statement"
        return "Container-level"
    elif sp.Code in [p.uri for p in x.parents]:
        return "Data code"
    else:
        return "Component"

def call_category(x):
    return x.category.split("_")[0].capitalize()

def call_sort_order(x):
    m = {"GET" : 10, "POST":20,"PUT":30,"DELETE":40}    
    ret =  m[x.method]
    if ("items" in x.category): ret -= 1
    ret = call_category(x) + str(x.target) + str(ret)
    return ret

main_types = sorted(main_types, key=lambda x: type_sort_order(x) + str(x.name))
calls_to_document = sorted(calls_to_document, key=call_sort_order)

if __name__=="__main__":
    if "payload" in sys.argv:
        current_batch = None
        for t in main_types: 
            if type_sort_order(t) != current_batch:
                current_batch = type_sort_order(t)
                wiki_batch_start(current_batch+" Types") # e.g. "Record Items" or "Container Items"
            wiki_payload_for_type(t)

            
    if "api" in sys.argv:
        current_batch = None
        processed = []
        for t in calls_to_document: 
            if call_category(t) != current_batch:
                current_batch = call_category(t)
                wiki_batch_start(current_batch+" Calls")
            if (t in processed): continue

            target = SMART_Class[t.target]
            calls_for_t = filter(lambda x: call_category(x)==current_batch, sorted(target.calls))
            processed.extend(calls_for_t)
            wiki_api_for_type(target, calls_for_t)
