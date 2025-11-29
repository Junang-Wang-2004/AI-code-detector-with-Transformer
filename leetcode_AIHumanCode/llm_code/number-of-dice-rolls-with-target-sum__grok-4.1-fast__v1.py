class Solution:
    def numRollsToTarget(self, d, f, target):
        MOD = 10**9 + 7
        if target < d or target > d * f:
            return 0
        ways = [0] * (target + 1)
        ways[0] = 1
        for _ in range(d):
            pref = [0] * (target + 2)
            for j in range(1, target + 2):
                pref[j] = (pref[j - 1] + ways[j - 1]) % MOD
            new_ways = [0] * (target + 1)
            for j in range(1, target + 1):
                left = max(0, j - f)
                new_ways[j] = (pref[j] - pref[left] + MOD) % MOD
            ways = new_ways
        return ways[target]
