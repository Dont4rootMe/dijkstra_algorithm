from collections import defaultdict
from typing import List, Dict


class Graph:
    def __make_graph__(self, init_graph: Dict[str, str]):
        graph = init_graph.copy()
        for node, edges in init_graph.items():
            for virt_node, vertex_value in edges.items():
                if not node in graph[virt_node].keys():
                    graph[virt_node][node] = vertex_value
                
        return graph
    
    
    def __init__(self, nodes: List[str] | None, init_graph: Dict[str, str] | list[list[int]]):
        self.nodes = nodes
        
        if isinstance(init_graph, list):
            temp = defaultdict(lambda: {})
            for i in range(len(init_graph)):
                for j in range(len(init_graph[i])):
                    temp[i][j] = init_graph[i][j]
            init_graph = temp
        else:
            self.graph = self.__make_graph__(init_graph)

    def get_nodes(self):
        return self.nodes
    
    def get_edges(self, node: str | int):
        return self.graph[node].keys()
    
    def value(self, node1: str | int, node2: str | int):
        return self.graph[node1][node2]