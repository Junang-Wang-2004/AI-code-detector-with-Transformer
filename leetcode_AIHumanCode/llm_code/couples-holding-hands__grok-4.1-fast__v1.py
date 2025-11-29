class Solution:
    def minSwapsCouples(self, row):
        n = len(row) // 2
        pos = [0] * (2 * n)
        for i, p in enumerate(row):
            pos[p] = i // 2
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def unite(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if rank[px] < rank[py]:
                    parent[px] = py
                elif rank[px] > rank[py]:
                    parent[py] = px
                else:
                    parent[py] = px
                    rank[px] += 1
        for k in range(n):
            unite(pos[2 * k], pos[2 * k + 1])
        comp = set(find(i) for i in range(n))
        return n - len(comp)
