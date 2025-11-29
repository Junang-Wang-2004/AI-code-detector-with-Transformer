class Solution(object):
    def subsequencePairCount(self, nums):
        if not nums:
            return 0
        MOD = 10**9 + 7
        mx = max(nums)
        nn = len(nums)
        maxp2 = 2 * nn + 5
        p2 = [1] * (maxp2 + 1)
        for k in range(1, maxp2 + 1):
            p2[k] = p2[k - 1] * 2 % MOD
        p3 = [1] * (nn + 5)
        for k in range(1, nn + 5):
            p3[k] = p3[k - 1] * 3 % MOD
        muu = [0] * (mx + 1)
        muu[1] = 1
        vis = [False] * (mx + 1)
        ps = []
        for ii in range(2, mx + 1):
            if not vis[ii]:
                ps.append(ii)
                muu[ii] = -1
            for pp in ps:
                if ii * pp > mx:
                    break
                vis[ii * pp] = True
                if ii % pp == 0:
                    muu[ii * pp] = 0
                    break
                else:
                    muu[ii * pp] = -muu[ii]
        fr = [0] * (mx + 1)
        for val in nums:
            fr[val] += 1
        totdiv = [fr[jj] for jj in range(mx + 1)]
        for dd in range(1, mx + 1):
            for mmul in range(dd * 2, mx + 1, dd):
                totdiv[dd] += totdiv[mmul]
        fval = [[0] * (mx + 1) for _ in range(mx + 1)]
        def gc(x, y):
            while y != 0:
                x, y = y, x % y
            return x
        for x1 in range(1, mx + 1):
            for x2 in range(x1, mx + 1):
                llcm = x1 * x2 // gc(x1, x2)
                cll = totdiv[llcm] if llcm <= mx else 0
                cxx1 = totdiv[x1]
                cxx2 = totdiv[x2]
                e2 = cxx1 - cll + cxx2 - cll
                tempv = p3[cll] * p2[e2] % MOD
                tempv = (tempv - p2[cxx1] - p2[cxx2] + 1 + 2 * MOD) % MOD
                fval[x1][x2] = fval[x2][x1] = tempv
        res = 0
        for gg in range(1, mx + 1):
            mk = mx // gg
            for i1 in range(1, mk + 1):
                m1 = muu[i1]
                if m1 == 0:
                    continue
                d11 = gg * i1
                for i2 in range(1, mk + 1):
                    m2 = muu[i2]
                    d22 = gg * i2
                    contr = m1 * m2 * fval[d11][d22]
                    res = (res + contr) % MOD
        return res
