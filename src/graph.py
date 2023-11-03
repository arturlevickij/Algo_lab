def read_graph_from_file(file_path):
    graph_from_file = {}
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split(":")
            key = data[0]
            if len(data) > 1 and data[1]:
                value = data[1].split(',')
            else:
                value = []
            graph_from_file[key] = value
    return graph_from_file


file_path = "input.txt"
graph_from_file = read_graph_from_file(file_path)



def directed_graph(graph):
    nodes = set(graph.keys())
    edge = {node: 0 for node in graph}
    for node in graph:
        for key in graph[node]:
            edge[key] += 1
    for start in graph:
        some_structure = [start]
        visited = set()
        node_keys = []
        while some_structure:
            current_vertex = some_structure.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                node_keys.append(current_vertex)
                for root in graph[current_vertex]:
                    some_structure.append(root)
        if set(node_keys) == nodes and edge[start] == 0:
            return node_keys[0]
        if all(graph[node] for node in graph) and set(node_keys) == nodes and edge[start] != 0:
            return node_keys[0]
    return -1


result = directed_graph(graph_from_file)


with open("output.txt", "w") as file:
    if result != -1:
        file.write(f"Directed graph: {result}\n")
    else:
        file.write("-1.\n")
