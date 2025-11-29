class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

class Solution:
    def canReachCorner(self, X, Y, circles):
        n = len(circles)
        if n == 0:
            return True
        uf = UnionFind(n + 2)
        start = n
        goal = n + 1
        for i in range(n):
            cx, cy, cr = circles[i]
            if cx - cr <= 0 or cy + cr >= Y:
                uf.unite(i, start)
            if cx + cr >= X or cy - cr <= 0:
                uf.unite(i, goal)
        for i in range(n):
            x1, y1, r1 = circles[i]
            for j in range(i):
                x2, y2, r2 = circles[j]
                dx = x1 - x2
                dy = y1 - y2
                if dx * dx + dy * dy <= (r1 + r2) * (r1 + r2):
                    uf.unite(i, j)
        return uf.find(start) != uf.find(goal)
