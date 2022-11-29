def dijkstra(graph):
    v_cnt = len(graph)
    d = [0] + [float('inf')] * (v_cnt - 1)
    u = {*range(v_cnt)}
    
    while len(u) > 0:
        # Find the vertex with the minimal d-label
        v = -1
        for candidate in u:
            if v == -1 or d[candidate] < d[v]:
                v = candidate
        
        # Iterate over its adjacent vertices and optimise their labels:
        for w, e in graph[v]:
            d[w] = min(d[w], d[v] + e)
        
        # v is now visited
        u.remove(v)

    return d

test = [
    [(1, 4), (2, 5), (3, 2)],
    [(4, 7)],
    [(4, 4), (5, 2)],
    [(6, 9)],
    [(6, 2)],
    [(4, 1)],
    [(2, 3), (5, 5)]
]

print(dijkstra(test))
