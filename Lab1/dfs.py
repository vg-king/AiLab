def dfs(node, graph, visited):
    visited.add(node)
    print(node, end=" ")

    for neigh in graph[node]:
        if neigh not in visited:
            dfs(neigh, graph, visited)


graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

visited = set()
dfs(0, graph, visited)
