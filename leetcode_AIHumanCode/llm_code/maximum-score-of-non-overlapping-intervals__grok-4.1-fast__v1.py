import bisect

class Solution:
    def maximumWeight(self, intervals):
        K = 4
        idx_map = {}
        ivs = []
        for i, (s, e, v) in enumerate(intervals):
            ky = (s, e, v)
            if ky not in idx_map:
                idx_map[ky] = i
                ivs.append((e, s, v, i))
        ivs.sort(key=lambda x: x[0])
        m = len(ivs)
        INF = 2 * 10**9 + 7
        dp = [[(0, []) for _ in range(K + 1)] for _ in range(m + 1)]
        for p in range(m):
            _, st, vl, idd = ivs[p]
            pr = bisect.bisect_right(ivs, (st, INF, INF, INF)) - 1
            for c in range(1, K + 1):
                pneg, plist = dp[pr + 1][c - 1]
                tneg = pneg - vl
                tlist = plist[:]
                bisect.insort(tlist, idd)
                sneg, slist = dp[p][c]
                dp[p + 1][c] = (tneg, tlist) if tneg < sneg else (sneg, slist)
        return dp[m][K][1]
