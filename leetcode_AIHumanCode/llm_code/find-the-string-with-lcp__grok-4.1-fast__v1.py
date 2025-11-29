class Solution:
    def findTheString(self, lcp):
        n = len(lcp)
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def unite(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    unite(i, j)
        components = set(find(i) for i in range(n))
        if len(components) > 26:
            return ""
        mapping = {}
        next_char = 0
        chars = [0] * n
        for i in range(n):
            root = find(i)
            if root not in mapping:
                mapping[root] = next_char
                next_char += 1
            chars[i] = mapping[root]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if chars[i] == chars[j]:
                    val = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)
                else:
                    val = 0
                if val != lcp[i][j]:
                    return ""
        return "".join(chr(ord('a') + c) for c in chars)
