class Solution:
    def countPaths(self, n, edges):
        is_p = [True] * (n + 1)
        is_p[0] = is_p[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_p[i]:
                for j in range(i * i, n + 1, i):
                    is_p[j] = False
        
        class UF:
            def __init__(self, size):
                self.parent = list(range(size))
                self.csize = [1] * size
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def merge(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return
                if self.csize[px] < self.csize[py]:
                    px, py = py, px
                self.parent[py] = px
                self.csize[px] += self.csize[py]
            
            def csize_of(self, x):
                return self.csize[self.find(x)]
        
        uf = UF(n)
        for a, b in edges:
            x, y = a - 1, b - 1
            if not is_p[x + 1] and not is_p[y + 1]:
                uf.merge(x, y)
        
        multipliers = [1] * n
        res = 0
        for a, b in edges:
            x, y = a - 1, b - 1
            if is_p[x + 1] == is_p[y + 1]:
                continue
            if not is_p[x + 1]:
                x, y = y, x
            block_sz = uf.csize_of(y)
            res += multipliers[x] * block_sz
            multipliers[x] += block_sz
        return res
