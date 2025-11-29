class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        segments = []
        i = 0
        num_ones = 0
        while i < n:
            if s[i] == '1':
                num_ones += 1
                i += 1
                continue
            start = i
            while i < n and s[i] == '0':
                i += 1
            segments.append((start, i - start))
        m = len(segments)
        lookup = [-1] * n
        k = 0
        for i in range(n):
            while k < m and segments[k][0] <= i:
                k += 1
            lookup[i] = k - 1
        if m < 2:
            return [num_ones] * len(queries)
        adj_sums = [segments[j][1] + segments[j + 1][1] for j in range(m - 1)]
        N = len(adj_sums)
        logN = 0
        while (1 << logN) <= N:
            logN += 1
        st = [[0] * N for _ in range(logN)]
        st[0] = adj_sums[:]
        for lv in range(1, logN):
            for p in range(N - (1 << lv) + 1):
                st[lv][p] = max(st[lv - 1][p], st[lv - 1][p + (1 << (lv - 1))])
        def range_max(ql, qr):
            if ql > qr:
                return 0
            le = qr - ql + 1
            lv = 0
            while (1 << (lv + 1)) <= le:
                lv += 1
            return max(st[lv][ql], st[lv][qr - (1 << lv) + 1])
        qnum = len(queries)
        result = [num_ones] * qnum
        for qi in range(qnum):
            lp, rp = queries[qi]
            sl = lookup[lp]
            sr = lookup[rp]
            lseg = sl + 1
            rseg = sr - (1 if s[rp] == '0' else 0)
            bonus = range_max(lseg, rseg - 1)
            if s[lp] == '0' and sl >= 0:
                stl, llen = segments[sl]
                taillen = llen - (lp - stl)
                nsidx = sl + 1
                if nsidx < m and nsidx <= rseg:
                    bonus = max(bonus, taillen + segments[nsidx][1])
            if s[rp] == '0' and sr >= 0:
                strg, lreng = segments[sr]
                headlen = rp - strg + 1
                psidx = sr - 1
                if psidx >= 0 and lseg <= psidx:
                    bonus = max(bonus, headlen + segments[psidx][1])
            if s[lp] == '0' and s[rp] == '0' and sl + 1 == sr and sl >= 0:
                stl, llen = segments[sl]
                taillen = llen - (lp - stl)
                strg, lreng = segments[sr]
                headlen = rp - strg + 1
                bonus = max(bonus, taillen + headlen)
            result[qi] = num_ones + bonus
        return result
