#! usr/bin/python
# Basic graph structure

import types

class Vertex:
    "Define vertex class"
    def __init__(self, key, color = None):
        self.id = key
        self.connected_to = {}
        self.color = color
        self.connectedTo = {}
    
    def __call__(self):
        return self

    def getID(self):
        return self.id

    def getColor(self):
        return self.color
    
    def addNeighbour(self, vertex, weight = None):
        if isinstance(vertex, Vertex):
            self.connectedTo[vertex] = weight
        else:
            raise TypeError("Vertex is not present in graphs")
    
    def getDegree(self):
        return len(self.connectedTo.keys())

#class Edge:
#    "Define edge class"
#    def __init__(self, startVertex, endVertex, label = None, weight = None):
#        if isinstance(startVertex, Vertex) and isinstance(endVertex, Vertex):
#            self.startVertex = startVertex
#            self.endVertex = endVertex
#            self.label = label
#            self.weight = weight
#        else:
#            raise TypeError("Vertices not present in graphs")
#    
#    def getID(self):
#        return self.label
#
#    def getWeight(self):
#        return self.weight

class Graph:
    "Define Undirexted graph class"
    
    def __init__(self):
        self.vertex_list = {}

    def addVertex(self, key):
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex

    def addEdge(self, key1, key2, weight = None):
        if key1 in self.vertex_list.keys() and key2 in self.vertex_list.keys():
            self.vertex_list[key1].addNeighbour(self.vertex_list[key2], weight)        
            self.vertex_list[key2].addNeighbour(self.vertex_list[key1], weight)        
        else:
            raise TypeError("Edges can be added to existing vertices only")

        
    def vertices(self):
        return self.vertex_list.keys()

    def edges(self):
        E = []
        for u in self.vertex_list.values():
            for v in u.connectedTo.keys():
                if not (v.getID(), u.getID()) in E:
                    E.append((u.getID(), v.getID()))
        return E

    def getVertex(self, key):
        "Returns the vertex if it present in graph"
        if key in self.vertex_list:
            return self.vertex_list[key]
        else:
            return None

    def deleteEdge(self, key1, key2):
        "Delete the edge from graph"
        if key1 in self.vertex_list.keys() and key2 in self.vertex_list.keys():
            for v in self.vertex_list[key1].connectedTo.keys():
                if v.getID() == key2:
                    del self.vertex_list[key1].connectedTo[v]
            
            for v in self.vertex_list[key2].connectedTo.keys():
                if v.getID() == key1:
                    del self.vertex_list[key2].connectedTo[v]

    def deleteVertex(self, key):
        "Delete the vertex in the graph."
        if key in self.vertex_list:
            for u in self.getVertex(key).connectedTo.keys():
                self.deleteEdge(key, u.getID())

            del self.vertex_list[key]
