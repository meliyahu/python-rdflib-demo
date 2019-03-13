import rdflib as rdf
import os
g = rdf.Graph()
g.parse("http://bigasterisk.com/foaf.rdf")

print(len(g))
g.serialize(os.path.join("output/bigastrerisk.ttl"), format='turtle')