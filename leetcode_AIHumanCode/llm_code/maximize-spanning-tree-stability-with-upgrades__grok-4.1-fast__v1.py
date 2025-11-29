class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        cur = x
        while cur != root:
            nxt = self.parent[cur]
            self.parent[cur] = root
            cur = nxt
        return root

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        return True


class Solution:
    def maxStability(self, n, edges, k):
        dsu = DSU(n)
        stab = float("inf")
        edge_cnt = 0
        for x, y, w, req in edges:
            if not req:
                continue
            if not dsu.unite(x, y):
                return -1
            stab = min(stab, w)
            edge_cnt += 1
        opts = [(w, x, y) for x, y, w, req in edges if not req]
        opts.sort(reverse=True)
        target = n - 1
        res = stab
        for w, x, y in opts:
            if dsu.unite(x, y):
                edge_cnt += 1
                if edge_cnt == target - k:
                    res = min(res, w)
                elif edge_cnt == target:
                    res = min(res, 2 * w)
        return res if edge_cnt == target else -1
