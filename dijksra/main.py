from queue import PriorityQueue

graph = {
    "Londyn": [(10, "Cadis"), (7, "Berlin")],
    "Warszawa": [(2, "Berlin"), (3, "Sophia"), (4, "Paris")],
    "Berlin": [(2, "Warszawa"), (7, "Londyn"), (6, "Paris")],
    "Sophia": [(3, "Warszawa"), (5, "Paris"), (8, "Cadis")],
    "Paris": [(6, "Berlin"), (4, "Warszawa"), (5, "Sophia"), (9, "Cadis")],
    "Cadis": [(9, "Paris"), (8, "Sophia"), (10, "Londyn")],
}

queue = PriorityQueue()
dist = {city: float("inf") for city in graph.keys()}
dist["Londyn"] = 0
visited = {city: False for city in graph.keys()}
queue.put((0, "Londyn"))
while not queue.empty():
    distance, city = queue.get()
    if not visited[city]:
        visited[city] = True

        for d, c in graph[city]:
            dist[city] = min(dist[city], dist[c] + d)
            queue.put((d, c))




print(dist)
