# Modern Relationships

# As the utility of graphs is not hidden from anyone, we ask you to design a directional graph in this exercise to store the names of individuals and their relationships. After creating such a graph, you should be able to determine whether there is a relationship between person x and person y.

# Input:
# The number of input rows is specified in the first line, and in the following n lines of input, the name of a person and the individuals they are associated with are received. In the last row, two names are given to you. The first name is the source, and the second name is the destination for the search.

# Note: There is no need to validate the data, and their accuracy is guaranteed.

# Example Input:
# 6
# Ali#Mohammad-Zahra-Sara-Mohsen
# Mohammad#Reza
# Jafar#Sara
# Mohsen#Ahmad
# Ahmad#Arman
# Arman#Reza
# Ali-Reza

# Explanation:
# In the above input, the number 6 indicates how many input rows the graph has! It doesn't end with a line break. We are asked to determine if Ali has a relationship with Reza!

# Sample Output:
# True

# Explanation:
# Since the node Ali is related to Mohammad and the node Mohammad is related to Reza, we can conclude that the nodes Ali and Reza are connected to each other.

# This is solved by using the deep-first search (DFS) algorithm in graph theory


def is_path(graph, source, target):
    visited_nodes = {source}

    queue = [source]

    while True:
        if target in graph[source] - visited_nodes:
            return True

        elif len(graph[source] - visited_nodes) > 0:
            source = list(graph[source] - visited_nodes)[0]
            visited_nodes.add(source)
            queue.append(source)

        else:
            queue.pop()

            if len(queue) == 0:
                return False

            source = queue[-1]


graph = {}
num_nods = int(input())

for ii in range(num_nods):
    str = input()

    node = str[: str.index("#")]

    edges = str[str.index("#") + 1 :]

    neighbors = set(edges.split("-"))

    graph[node] = neighbors


all_nodes = set()
for nodes in graph:
    all_nodes = all_nodes | graph[nodes]

for nodes in all_nodes:
    if graph.get(nodes) == None:
        graph[nodes] = set()


str2 = list(input().split("-"))

source = str2[0]
target = str2[1]

print(is_path(graph, source, target))
