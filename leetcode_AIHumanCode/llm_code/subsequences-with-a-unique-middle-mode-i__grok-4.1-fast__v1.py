import collections

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD = 10**9 + 7
        def c(n, k):
            if k < 0 or k > n: return 0
            if k == 0: return 1
            if k == 1: return n
            return n * (n - 1) // 2
        n = len(nums)
        rf = collections.Counter(nums)
        lf = collections.Counter()
        slsq = 0
        srsq = 0
        scrs = 0
        sl2r = 0
        slr2 = 0
        srsq = sum(f * f for f in rf.values())
        ans = 0
        for i in range(n):
            v = nums[i]
            slsq -= lf[v] * lf[v]
            srsq -= rf[v] * rf[v]
            scrs -= lf[v] * rf[v]
            sl2r -= lf[v] * lf[v] * rf[v]
            slr2 -= lf[v] * rf[v] * rf[v]
            rf[v] -= 1
            A = lf[v]
            B = rf[v]
            lt = i
            rt = n - i - 1
            nlt = lt - A
            nrt = rt - B
            contrib = 0
            for kl in range(3):
                wl = c(A, kl) * c(nlt, 2 - kl)
                for kr in range(3):
                    if kl + kr < 2: continue
                    wr = c(B, kr) * c(nrt, 2 - kr)
                    contrib = (contrib + wl * wr) % MOD
            ans = (ans + contrib) % MOD
            # f=2 kl=1 kr=0
            total_nv12 = nlt * c(nrt, 2)
            psr = (srsq - nrt) // 2
            md12 = nrt * scrs - slr2
            gnv12 = total_nv12 - nlt * psr - md12
            if gnv12 > 0:
                contrib2 = c(A, 1) * c(B, 0) * gnv12 % MOD
                ans = (ans + contrib2) % MOD
            # f=2 kl=0 kr=1
            total_nv21 = nrt * c(nlt, 2)
            psl = (slsq - nlt) // 2
            md21 = nlt * scrs - sl2r
            gnv21 = total_nv21 - nrt * psl - md21
            if gnv21 > 0:
                contrib2 = c(A, 0) * c(B, 1) * gnv21 % MOD
                ans = (ans + contrib2) % MOD
            lf[v] += 1
            slsq += lf[v] * lf[v]
            srsq += rf[v] * rf[v]
            scrs += lf[v] * rf[v]
            sl2r += lf[v] * lf[v] * rf[v]
            slr2 += lf[v] * rf[v] * rf[v]
        return ans
