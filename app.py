import rdflib as rdf
import os

g = rdf.Graph()
g.parse("http://www.w3.org/People/Berners-Lee/card")

print(f"Found {len(g)} triples")

print("Printing triples:")
for (sub, pred, obj) in g:
    #  print(f" {sub} {pred} {obj}")
    if ( sub, pred, obj) not in g:
        raise Exception("Should be there!")

g.serialize(os.path.join("output/berners.ttl"), format='turtle')
g.serialize(os.path.join("output/berners.nt"), format='nt')
