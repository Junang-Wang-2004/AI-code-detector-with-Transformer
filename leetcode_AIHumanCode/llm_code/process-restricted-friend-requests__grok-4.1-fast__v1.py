class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.p[px] = py
        elif self.rank[px] > self.rank[py]:
            self.p[py] = px
        else:
            self.p[py] = px
            self.rank[px] += 1
        return True


class Solution:
    def friendRequests(self, n, restrictions, requests):
        dsu = DSU(n)
        res = []
        for a, b in requests:
            ra = dsu.find(a)
            rb = dsu.find(b)
            if ra == rb:
                res.append(True)
                continue
            valid = True
            for c, d in restrictions:
                rc = dsu.find(c)
                rd = dsu.find(d)
                if (rc == ra and rd == rb) or (rc == rb and rd == ra):
                    valid = False
                    break
            res.append(valid)
            if valid:
                dsu.unite(a, b)
        return res
