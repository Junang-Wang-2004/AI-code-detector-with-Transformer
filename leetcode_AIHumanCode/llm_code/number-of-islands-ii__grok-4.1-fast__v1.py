class Solution:
    def numIslands2(self, rows, cols, updates):
        par = {}
        sz = {}
        cnt = 0
        ans = []
        nbrs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def idx(r, c):
            return r * cols + c

        def root(u):
            if par[u] != u:
                par[u] = root(par[u])
            return par[u]

        def link(a, b):
            pa, pb = root(a), root(b)
            if pa == pb:
                return False
            if sz[pa] < sz[pb]:
                par[pa] = pb
                sz[pb] += sz[pa]
            else:
                par[pb] = pa
                sz[pa] += sz[pb]
            return True

        for r, c in updates:
            i = idx(r, c)
            par[i] = i
            sz[i] = 1
            cnt += 1
            for dr, dc in nbrs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    j = idx(nr, nc)
                    if j in par and link(i, j):
                        cnt -= 1
            ans.append(cnt)
        return ans
