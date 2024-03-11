from graph import Graph
from dijkstra import dijkstra_algorithm, print_result

nodes = [str(i) for i in range(8)]
 
init_graph = {}
for node in nodes:
    init_graph[node] = {}
    
init_graph["0"]["1"] = 5
init_graph["0"]["2"] = 4
init_graph["1"]["3"] = 1
init_graph["1"]["4"] = 3
init_graph["4"]["5"] = 5
init_graph["4"]["6"] = 4
init_graph["6"]["5"] = 1
init_graph["7"]["3"] = 2
init_graph["7"]["6"] = 2

graph = Graph(nodes, init_graph)

previous, curr_path, mapper = dijkstra_algorithm(graph=graph, start_node="0", return_distances=True)
print_result(previous, curr_path, start_node="0", target_node="5")
print(mapper)