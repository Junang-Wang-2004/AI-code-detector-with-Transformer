from collections import deque

class Solution:
    def collectTheCoins(self, coins, edges):
        m = len(coins)
        g = [[] for _ in range(m)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        degree = [len(g[i]) for i in range(m)]
        q = deque()
        for i in range(m):
            if degree[i] == 1 and not coins[i]:
                q.append(i)
        alive = m
        while q:
            node = q.popleft()
            if degree[node] != 1 or coins[node]:
                continue
            neigh = g[node][0]
            g[neigh].remove(node)
            g[node] = []
            degree[neigh] -= 1
            degree[node] = 0
            alive -= 1
            if degree[neigh] == 1 and not coins[neigh]:
                q.append(neigh)
        q = deque(i for i in range(m) if degree[i] == 1)
        for _ in range(2):
            next_q = deque()
            while q:
                node = q.popleft()
                if degree[node] != 1:
                    continue
                neigh = g[node][0]
                g[neigh].remove(node)
                g[node] = []
                degree[neigh] -= 1
                degree[node] = 0
                alive -= 1
                if degree[neigh] == 1:
                    next_q.append(neigh)
            q = next_q
        return max(0, (alive - 1) * 2)
