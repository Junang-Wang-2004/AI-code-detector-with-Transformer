from collections import deque
from math import inf

class Solution:
    def findShortestCycle(self, n, edges):
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        shortest = inf
        for start_node in range(n):
            dists = [-1] * n
            dists[start_node] = 0
            par = [-1] * n
            q = deque([start_node])
            while q:
                node = q.popleft()
                if 2 * dists[node] + 1 >= shortest:
                    break
                for neighbor in adj_list[node]:
                    if dists[neighbor] == -1:
                        dists[neighbor] = dists[node] + 1
                        par[neighbor] = node
                        if 2 * dists[neighbor] + 1 >= shortest:
                            continue
                        q.append(neighbor)
                    elif neighbor != par[node]:
                        cycle_len = dists[node] + dists[neighbor] + 1
                        if cycle_len < shortest:
                            shortest = cycle_len
        return int(shortest) if shortest != inf else -1
