class Solution:
    def validTree(self, n, edges):
        if n == 0:
            return True
        par = list(range(n))
        rnk = [0] * n
        
        def get_root(x):
            if par[x] != x:
                par[x] = get_root(par[x])
            return par[x]
        
        def merge(a, b):
            ra, rb = get_root(a), get_root(b)
            if ra == rb:
                return False
            if rnk[ra] < rnk[rb]:
                par[ra] = rb
            elif rnk[ra] > rnk[rb]:
                par[rb] = ra
            else:
                par[rb] = ra
                rnk[ra] += 1
            return True
        
        parts = n
        for x, y in edges:
            if x >= n or y >= n or not merge(x, y):
                return False
            parts -= 1
        
        return parts == 1
