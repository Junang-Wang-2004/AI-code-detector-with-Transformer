class Solution:
    def countCoprime(self, mat):
        MOD = 10**9 + 7
        maxv = max(max(r) for r in mat)
        spf = list(range(maxv + 1))
        for i in range(2, int(maxv**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, maxv + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        mob = [0] * (maxv + 1)
        mob[1] = 1
        for i in range(2, maxv + 1):
            p = spf[i]
            prev = i // p
            if prev % p == 0:
                mob[i] = 0
            else:
                mob[i] = -mob[prev]
        prod = [1] * (maxv + 1)
        for r in mat:
            fr = [0] * (maxv + 1)
            for x in r:
                fr[x] += 1
            sums = [0] * (maxv + 1)
            for d in range(1, maxv + 1):
                sm = 0
                md = d
                while md <= maxv:
                    sm = (sm + fr[md]) % MOD
                    md += d
                sums[d] = sm
            for d in range(1, maxv + 1):
                prod[d] = prod[d] * sums[d] % MOD
        res = 0
        for d in range(1, maxv + 1):
            res = (res + mob[d] * prod[d]) % MOD
        return res
