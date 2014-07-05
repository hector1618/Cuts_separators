#! usr/bin/python
import os,sys,inspect
#currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parentdir = os.path.dirname(currentdir)
#sys.path.insert(1, parentdir)
sys.path.insert(0, '../../graph') 
import graph


def vc_reduction1(g, k):
    """
    Reduction1 = If G contains an isolated vertex v, delete v from g. New instance is (g\{v}, k-1)
    """
    if isinstance(g, graph.Graph):
        for v in g.vertices():
            if g.getVertex(v).getDegree() == 0:
                g.deleteVertex(v)

    return (g, k)


def vc_reduction2(g, k):
    """
    If G contains a vertex v of degree at least k + 1, then delete v from G and decrement parameter k by 1.
    """
    if isinstance(g, graph.Graph):
        for v in g.vertices():
            if g.getVertex(v).getDegree() > k:
                g.deleteVertex(v)

    return (g, k - 1)
    


def vertex_cover(g, k):
    """
    Graph g, integer k. Return (g, k) as reduced instance.
    """
    while True:
        g1, k1 = vc_reduction1(g, k)
        g2, k2 = vc_reduction2(g1, k1)
        if (g, k) == (g2, k2):
            break
        else:
            g, k = g2, k2

    return g, k
