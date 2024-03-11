import sys
from graph import Graph

def dijkstra_algorithm(graph: Graph, start_node: str | int, return_distances: bool = False):
    unvisited = list(graph.get_nodes()) 
    curr_path = {}
    previous = {}
    
    dist_map = {}
 
    max_value = sys.maxsize
    for node in unvisited:
        curr_path[node] = max_value

    curr_path[start_node] = 0
    
    while unvisited:
        # get minimal lasted node
        node_min = unvisited[unvisited.index(min(unvisited, key=lambda x: curr_path[x]))]

        edges = graph.get_edges(node_min)
        for edge in edges:
            pending_vertex_value = curr_path[node_min] + graph.value(node_min, edge)
            if pending_vertex_value < curr_path[edge]:
                curr_path[edge] = pending_vertex_value
                previous[edge] = node_min
                
        dist_map[node_min] = curr_path[node_min]
        unvisited.remove(node_min)
    
    return (previous, curr_path, dist_map) if return_distances else (previous, curr_path)

def print_result(previous, curr_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous[node]

    path.append(start_node)
    
    print(f'Лучший маршрут из {start_node} в {target_node}: {curr_path[target_node]}')
    print(" -> ".join(reversed(path)))

