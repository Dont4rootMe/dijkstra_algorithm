import sys
from graph import Graph

def dijkstra_algorithm(graph: Graph, start_node: str | int):
    closed = list(graph.get_nodes()) 
    curr_path = {}
    observed = {}
 
    max_value = sys.maxsize
    for node in closed:
        curr_path[node] = max_value

    curr_path[start_node] = 0
    
    while closed:
        # get minimal lasted node
        node_min = closed[closed.index(min(closed, key=lambda x: curr_path[x]))]

        edges = graph.get_edges(node_min)
        for edge in edges:
            pending_vertex_value = curr_path[node_min] + graph.value(node_min, edge)
            if pending_vertex_value < curr_path[edge]:
                curr_path[edge] = pending_vertex_value
                observed[edge] = node_min
        closed.remove(node_min)
    
    return observed, curr_path

def print_result(observed, curr_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = observed[node]

    path.append(start_node)
    
    print(f'Лучший маршрут из {start_node} в {target_node}: {curr_path[target_node]}')
    print(" -> ".join(reversed(path)))

