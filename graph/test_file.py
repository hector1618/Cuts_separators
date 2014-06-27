#! usr/bin/python

import graph

def construct_graph():
    g = graph.Graph()

def add_vertices(g):
    for i in range(6):
        g.addVertex(i)

    #for v in g.vertices():
    #    print v, type(v)


def add_edges(g):
    for v in g.vertices():
        for u in g.vertices():
            g.addEdge(v, u)
            
g = graph.Graph()
print "Constuct graph \t PASS"

add_vertices(g)
print "Add vertices \t PASS"

print g.vertices()

add_edges(g)
print "Add Edges \t PASS"

print g.edges()
