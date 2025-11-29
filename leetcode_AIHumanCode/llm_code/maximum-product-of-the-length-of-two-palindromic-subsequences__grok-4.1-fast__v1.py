class Solution:
    def maxProduct(self, s):
        n = len(s)
        N = 1 << n
        vals = [0] * N
        for m in range(N):
            idxs = [i for i in range(n) if m & (1 << i)]
            sz = len(idxs)
            pal = True
            for k in range(sz // 2):
                if s[idxs[k]] != s[idxs[sz - 1 - k]]:
                    pal = False
                    break
            if pal:
                vals[m] = sz
        maxp = vals[:]
        for b in range(n):
            for m in range(N):
                if m & (1 << b):
                    p = m ^ (1 << b)
                    maxp[m] = max(maxp[m], maxp[p])
        tot = N - 1
        res = 0
        for m in range(N):
            if vals[m] == 0:
                continue
            rest = tot ^ m
            res = max(res, vals[m] * maxp[rest])
        return res
