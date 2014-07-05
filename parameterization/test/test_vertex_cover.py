#! usr/bin/python

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import vertex_cover
sys.path.insert(0, '../../graph') 
import graph

def add_vertices(g):
    for i in range(7):
        g.addVertex(i)

def add_edges(g):
    g.addEdge(5, 1); g.addEdge(0, 3); g.addEdge(2, 5); g.addEdge(4, 2); g.addEdge(4, 3); g.addEdge(1, 5); g.addEdge(3, 5); g.addEdge(2, 3); g.addEdge(1, 4); 
    
            
g = graph.Graph()
assert isinstance(g, graph.Graph)

add_vertices(g)
assert g.vertices() == [0, 1, 2, 3, 4, 5, 6]

add_edges(g)
E = g.edges(); E.sort()
assert E == [(0, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5)]

g1, k1 = vertex_cover.vc_reduction1(g, 3)

assert g1.vertices() == [0, 1, 2, 3, 4, 5]

g2, k2 = vertex_cover.vc_reduction2(g1, 3)

assert g2.vertices() == [0, 1, 2, 4, 5]
E = g2.edges(); E.sort()
assert E == [(1, 4), (1, 5), (2, 4), (2, 5)]
