class Solution(object):
    def findLatestStep(self, arr, m):
        n = len(arr)
        parent = list(range(n + 2))
        sz = [0] * (n + 2)
        cnt = 0
        res = -1
        def find(u):
            r = u
            while parent[r] != r:
                r = parent[r]
            x = u
            while x != r:
                nxt = parent[x]
                parent[x] = r
                x = nxt
            return r
        def unite(u, v):
            nonlocal cnt
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return
            su = sz[pu]
            sv = sz[pv]
            if su == m:
                cnt -= 1
            if sv == m:
                cnt -= 1
            if su < sv:
                pu, pv = pv, pu
            parent[pv] = pu
            sz[pu] += sz[pv]
            if sz[pu] == m:
                cnt += 1
        for i in range(n):
            pos = arr[i]
            sz[pos] = 1
            if m == 1:
                cnt += 1
            if sz[pos - 1] > 0:
                unite(pos - 1, pos)
            if sz[pos + 1] > 0:
                unite(pos + 1, pos)
            if cnt > 0:
                res = i + 1
        return res
