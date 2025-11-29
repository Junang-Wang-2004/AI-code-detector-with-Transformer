class DSU:
    def __init__(self, cells, top):
        self.parent = list(range(cells + 1))
        self.rank = [0] * (cells + 1)
        self.comp_size = [1] * (cells + 1)
        self.comp_size[top] = 0
        self.top = top

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.comp_size[py] += self.comp_size[px]
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.comp_size[px] += self.comp_size[py]
        else:
            self.parent[py] = px
            self.comp_size[px] += self.comp_size[py]
            self.rank[px] += 1
        return True

    def size_top(self):
        return self.comp_size[self.find(self.top)]


class Solution:
    def hitBricks(self, grid, hits):
        rows, cols = len(grid), len(grid[0])
        total = rows * cols
        top_node = total
        temp = [r[:] for r in grid]
        for hr, hc in hits:
            temp[hr][hc] = 0
        dsu = DSU(total, top_node)
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def idx(rr, cc):
            return rr * cols + cc

        for i in range(rows):
            for j in range(cols):
                if temp[i][j]:
                    p = idx(i, j)
                    if i == 0:
                        dsu.unite(p, top_node)
                    if i > 0 and temp[i - 1][j]:
                        dsu.unite(p, idx(i - 1, j))
                    if j > 0 and temp[i][j - 1]:
                        dsu.unite(p, idx(i, j - 1))

        res = []
        for hr, hc in reversed(hits):
            before = dsu.size_top()
            if grid[hr][hc] == 0:
                res.append(0)
                continue
            temp[hr][hc] = 1
            p = idx(hr, hc)
            if hr == 0:
                dsu.unite(p, top_node)
            for dr, dc in deltas:
                nr, nc = hr + dr, hc + dc
                if 0 <= nr < rows and 0 <= nc < cols and temp[nr][nc]:
                    dsu.unite(p, idx(nr, nc))
            after = dsu.size_top()
            res.append(max(0, after - before - 1))
        return res[::-1]
