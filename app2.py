from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF
import os
import pprint

g = Graph()

#  Create an identifier to use as the subject
mosheh = BNode()

# Bind a few prefix, namespace paires for more readable ouput
g.bind('dc', DC)
g.bind('foaf', FOAF)

# Add triples using store's add method
g.add((mosheh, RDF.type, FOAF.Person))
g.add((mosheh, FOAF.nick, Literal("mosheh", lang="he")))
g.add((mosheh, FOAF.name, Literal("Mosheh EliYahu")))
g.add((mosheh, FOAF.mbox, URIRef("mailto:mosheh@example.org")))

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
print(g.serialize(format='turtle'))
