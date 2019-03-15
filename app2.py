from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF, XSD, SKOS
import os
import pprint

# g = Graph('IOMemory', URIRef("http://tern.org.au/ontology/corveg"))
g = Graph()

#  Create an identifier to use as the subject
# mosheh = BNode()
n = Namespace('http://rooiport.com.au/Company')

# Bind a few prefix, namespace paires for more readable ouput
g.bind('skos', SKOS)
g.bind('dc', DC)
g.bind('foaf', FOAF)
g.bind('xsd', XSD)
g.bind('rooi', n)

# Add triples using store's add method
g.add((n['mosheh'], RDF.type, FOAF.Person))
g.add((n['mosheh'], FOAF.nick, Literal("mosheh", lang="he")))
g.add((n['mosheh'], FOAF.age, Literal("40", datatype=XSD.integer)))
g.add((n['mosheh'], FOAF.name, Literal("Mosheh EliYahu")))
g.add((n['mosheh'], FOAF.mbox, URIRef("mailto:mosheh@example.org")))

# Iterate over triples in store and print them out
for (s, p, o) in g:
    print(s, p, o)

for stmt in g:
    pprint.pprint(stmt)

# For each foaf:Person in the store print out its mbox property
print(".......printing mboxes")
for person in g.subjects(RDF.type, FOAF.Person):
    for mbox in g.objects(person, FOAF.mbox):
        print(mbox)

# Save the triples to a file
g.serialize(os.path.join("output/turtle.ttl"),format='turtle')
g.serialize(os.path.join("output/n-triple.nt"),format='nt')
# g.serialize(os.path.join("output/quads.nq"),format='nquads')
print(g.serialize(format='turtle'))
