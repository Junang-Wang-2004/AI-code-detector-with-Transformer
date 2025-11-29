class Solution:
    def longestCommonPrefix(self, strs):
        def pref_len(a, b):
            m = min(len(a), len(b))
            for i in range(m):
                if a[i] != b[i]:
                    return i
            return m

        n = len(strs)
        if n < 2:
            return [0] * n

        adj_lcp = [pref_len(strs[j], strs[j + 1]) for j in range(n - 1)]

        pmax = [0]
        for v in adj_lcp:
            pmax.append(max(pmax[-1], v))

        smax = [0] * n
        for j in range(n - 2, -1, -1):
            smax[j] = max(adj_lcp[j], smax[j + 1])

        bridges = [0] * n
        for i in range(1, n - 1):
            bridges[i] = pref_len(strs[i - 1], strs[i + 1])

        ans = []
        for i in range(n):
            lmax = pmax[i - 1] if i >= 1 else 0
            rmax = smax[i + 1] if i + 1 < n else 0
            ans.append(max(lmax, rmax, bridges[i]))
        return ans
