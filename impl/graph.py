from collections import defaultdict
from impl.graph_node import GraphNode

class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed
    
    def add_node(self, node: GraphNode):
        if node not in self.adj:
            self.adj[node] = []

    def remove_node(self, node: GraphNode):
        del self.adj[node]
        for key in self.adj:
            self.adj[key] = [neighbor for neighbor in self.adj[key] if neighbor != node]

    def add_edge(self, u: GraphNode, v: GraphNode):
        if u not in self.adj or v not in self.adj:
            raise KeyError(f"add nodes before edges: {u}, {v}")
        
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def remove_edge(self, u: GraphNode, v: GraphNode):
        self.adj[u].remove(v)
        if not self.directed:
            self.adj[v].remove(u)
