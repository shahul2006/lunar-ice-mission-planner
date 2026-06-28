import heapq
import numpy as np


class AStarPlanner:

    def heuristic(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def neighbors(self, node, rows, cols):

        r, c = node

        moves = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        result = []

        for dr, dc in moves:

            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                result.append((nr,nc))

        return result

    def search(self, cost_map, start, goal):

        rows, cols = cost_map.shape

        pq = []

        heapq.heappush(pq,(0,start))

        came = {}

        g = {start:0}

        while pq:

            _, current = heapq.heappop(pq)

            if current == goal:

                path = []

                while current in came:
                    path.append(current)
                    current = came[current]

                path.append(start)

                return path[::-1]

            for n in self.neighbors(current, rows, cols):

                new_cost = g[current] + cost_map[n]

                if n not in g or new_cost < g[n]:

                    g[n] = new_cost

                    priority = new_cost + self.heuristic(n, goal)

                    heapq.heappush(pq,(priority,n))

                    came[n] = current

        return []