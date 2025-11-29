import collections

class Solution(object):
    def countSubMultisets(self, nums, l, r):
        MOD = 10**9 + 7
        freq = collections.Counter(nums)
        zeros = freq.pop(0, 0)
        dp = [0] * (r + 1)
        dp[0] = 1
        for val, lim in freq.items():
            for res in range(val):
                pref = [0]
                p = res
                while p <= r:
                    pref.append((pref[-1] + dp[p]) % MOD)
                    p += val
                p = res
                i = 0
                while p <= r:
                    lo = max(0, i - lim)
                    dp[p] = (pref[i + 1] - pref[lo] + MOD) % MOD
                    p += val
                    i += 1
        total = sum(dp[i] for i in range(l, r + 1)) % MOD
        return total * (zeros + 1) % MOD
