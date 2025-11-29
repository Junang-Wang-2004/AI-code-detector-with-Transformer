class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.components -= 1
        return True


class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        dsu = DSU(n + 1)
        edges = []
        for i in range(1, n + 1):
            edges.append((wells[i - 1], 0, i))
        for house1, house2, cost in pipes:
            edges.append((cost, house1, house2))
        edges.sort()
        ans = 0
        for cost, u, v in edges:
            if dsu.merge(u, v):
                ans += cost
                if dsu.components == 1:
                    return ans
        return ans
