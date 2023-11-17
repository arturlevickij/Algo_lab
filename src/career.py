class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_organization_graph(levels):
    graph = [[Node(value) for value in row] for row in levels]
    for i in range(len(levels) - 1):
        for j in range(len(levels[i])):
            graph[i][j].left = graph[i + 1][j]
            graph[i][j].right = graph[i + 1][j + 1]
    return graph

def max_experience(graph):
    if not graph or not graph[0]:
        return 0
    for i in reversed(range(len(graph) - 1)):
        for j in range(len(graph[i])):
            graph[i][j].value += max(graph[i + 1][j].value, graph[i + 1][j + 1].value)
    return graph[0][0].value

with open("career_in.txt", "r") as file:
    lines = file.readlines()

levels = [list(map(int, line.split())) for line in lines[1:]]

organization_graph = build_organization_graph(levels)

max_total_experience = max_experience(organization_graph)

with open("career_out.txt", "w") as file:
    file.write(str(max_total_experience))
