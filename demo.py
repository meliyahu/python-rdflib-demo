import rdflib
import pprint

g = rdflib.Graph()

g.parse('demo.nt', format='nt')

print(len(g))
for stmt in g:
    pprint.pprint(stmt)
