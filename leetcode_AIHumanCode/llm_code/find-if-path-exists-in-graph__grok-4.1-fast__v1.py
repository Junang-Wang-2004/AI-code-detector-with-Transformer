class Solution:
    def validPath(self, n, edges, source, dest):
        par = list(range(n))
        sz = [1] * n

        def root(x):
            r = x
            while par[r] != r:
                r = par[r]
            while x != r:
                nxt = par[x]
                par[x] = r
                x = nxt
            return r

        def merge(a, b):
            pa, pb = root(a), root(b)
            if pa == pb:
                return
            if sz[pa] < sz[pb]:
                par[pa] = pb
                sz[pb] += sz[pa]
            else:
                par[pb] = pa
                sz[pa] += sz[pb]

        for a, b in edges:
            merge(a, b)
        return root(source) == root(dest)
