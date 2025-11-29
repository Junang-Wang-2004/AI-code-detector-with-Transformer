class Solution(object):
    def possibleStringCount(self, word, k):
        MOD = 10**9 + 7
        group_lens = []
        i = 0
        n = len(word)
        while i < n:
            start = i
            while i < n and word[i] == word[start]:
                i += 1
            group_lens.append(i - start)
        r = len(group_lens)
        prod = 1
        for ln in group_lens:
            prod = prod * ln % MOD
        if k <= r:
            return prod
        sz = k - r
        ways = [0] * sz
        ways[0] = 1
        for ln in group_lens:
            pref = [0] * (sz + 1)
            for j in range(sz):
                pref[j + 1] = (pref[j] + ways[j]) % MOD
            for j in range(sz):
                lo = max(0, j - ln + 1)
                ways[j] = (pref[j + 1] - pref[lo] + MOD) % MOD
        cum = sum(ways) % MOD
        return (prod - cum + MOD) % MOD
