import rdflib
import pprint

g = rdflib.Graph()

g.parse('demo.nt', format='nt')

print(f'{len(g)} triples in the graph')
for stmt in g:
    pprint.pprint(stmt)
