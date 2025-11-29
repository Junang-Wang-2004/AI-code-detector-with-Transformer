class Solution(object):
    def minimumScore(self, s, t):
        n = len(s)
        m = len(t)
        suf = [0] * n
        cnt = 0
        for i in range(n - 1, -1, -1):
            if cnt < m and s[i] == t[m - 1 - cnt]:
                cnt += 1
            suf[i] = cnt
        res = m - cnt
        p = 0
        for i in range(n):
            covered = p + suf[i]
            res = min(res, m - min(m, covered))
            if p < m and s[i] == t[p]:
                p += 1
        res = min(res, m - p)
        return res
