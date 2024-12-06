from queue import PriorityQueue
from sys import maxsize

capitals = {1: "Warszawa", 2: "Berlin", 3: "Sophia", 4: "Paris", 5: "Cadis", 0: "Londyn"}

graph = [[(5, 10), (2, 7)],
         [(2, 2), (3, 3), (4, 4)],
         [(1, 2), (0, 7), (4, 6)],
         [(1, 3), (4, 5), (5, 8)],
         [(2, 6), (1, 4), (3, 5), (5, 9)],
         [(4, 9), (3, 8), (0, 10)]]

queue = PriorityQueue()
dist = [maxsize] * 6
dist[0] = 0
visited = [False] * 6
queue.put((0, 0, 0))
while not queue.empty():
    distance, start_city, end_city = queue.get()
    if not visited[start_city]:
        visited[start_city] = True
        for c, d in graph[start_city]:
            queue.put((d, end_city, c))
        if dist[end_city] > dist[start_city] + distance:
            dist[end_city] = dist[start_city] + distance
#TODO bledny wynik
print(dist[1])


