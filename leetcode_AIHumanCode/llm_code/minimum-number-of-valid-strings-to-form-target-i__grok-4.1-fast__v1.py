class Solution:
    def minValidStrings(self, words, target):
        n = len(target)
        A = ord('a')
        MOD1 = 1000000007
        BASE1 = 131
        MOD2 = 1000000009
        BASE2 = 137
        power1 = [1] * (n + 1)
        power2 = [1] * (n + 1)
        for i in range(1, n + 1):
            power1[i] = power1[i - 1] * BASE1 % MOD1
            power2[i] = power2[i - 1] * BASE2 % MOD2
        hashs = set()
        for w in words:
            hh1 = 0
            hh2 = 0
            for cc in w:
                vv = ord(cc) - A + 1
                hh1 = (hh1 * BASE1 + vv) % MOD1
                hh2 = (hh2 * BASE2 + vv) % MOD2
                hashs.add((hh1, hh2))
        dp = [0] * (n + 1)
        h1 = 0
        h2 = 0
        lft = 0
        for rgt in range(n):
            v = ord(target[rgt]) - A + 1
            h1 = (h1 * BASE1 + v) % MOD1
            h2 = (h2 * BASE2 + v) % MOD2
            while lft <= rgt and (h1, h2) not in hashs:
                vl = ord(target[lft]) - A + 1
                plen1 = power1[rgt - lft]
                h1 = (h1 - vl * plen1 % MOD1 + MOD1) % MOD1
                plen2 = power2[rgt - lft]
                h2 = (h2 - vl * plen2 % MOD2 + MOD2) % MOD2
                lft += 1
            if lft > rgt:
                return -1
            dp[rgt + 1] = dp[lft] + 1
        return dp[n]
