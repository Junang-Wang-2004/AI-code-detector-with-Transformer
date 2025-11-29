import itertools

class Solution:
    def maxSumRangeQuery(self, nums, requests):
        MOD = 10**9 + 7
        n = len(nums)
        delta = [0] * n
        for l, r in requests:
            delta[l] += 1
            if r + 1 < n:
                delta[r + 1] -= 1
        freqs = list(itertools.accumulate(delta))
        vals = sorted(nums)
        frqs = sorted(freqs)
        ans = 0
        for v, f in zip(vals, frqs):
            ans = (ans + v * f) % MOD
        return ans
