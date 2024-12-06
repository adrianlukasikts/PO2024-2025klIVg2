from queue import PriorityQueue

capitals = {1: "Warszawa", 2: "Berlin", 3: "Sophia", 4: "Paris", 5: "Cadis", 0: "Londyn"}

graph = [[(5, 10), (2, 7)],
         [(2, 2), (3, 3), (4, 4)],
         [(1, 2), (0, 7), (4, 6)],
         [(1, 3), (4, 5), (5, 8)],
         [(2, 6), (1, 4), (3, 5), (5, 9)],
         [(4, 9), (3, 8), (0, 10)]]

queue = PriorityQueue()

