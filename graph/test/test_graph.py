#! usr/bin/python

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
import graph

def add_vertices(g):
    for i in range(6):
        g.addVertex(i)

def add_edges(g):
    g.addEdge(5, 1); g.addEdge(0, 3); g.addEdge(2, 5); g.addEdge(4, 2); g.addEdge(4, 3); g.addEdge(1, 5); g.addEdge(3, 5); g.addEdge(2, 3); g.addEdge(1, 4); 
    
            
g = graph.Graph()
assert isinstance(g, graph.Graph)

add_vertices(g)
assert g.vertices() == [0, 1, 2, 3, 4, 5]

add_edges(g)
E = g.edges(); E.sort()
assert E == [(0, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5)]


assert g.getVertex(4).getID() == 4
assert g.getVertex(3).getColor() == None
assert g.getVertex(6) == None
assert g.getVertex(2).getDegree() == 3

g.deleteEdge(1, 5)
E = g.edges(); E.sort()
assert E == [(0, 3), (1, 4), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5)]


g.deleteVertex(4)
E = g.edges(); E.sort()
assert g.vertices() == [0, 1, 2, 3, 5]
assert g.edges() == [(0, 3), (2, 3), (2, 5), (3, 5)]

