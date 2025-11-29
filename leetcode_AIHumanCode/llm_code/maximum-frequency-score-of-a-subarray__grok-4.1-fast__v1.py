import collections

class Solution:
    def maxFrequencyScore(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        if k > n:
            return 0
        freq = collections.defaultdict(int)
        score = 0
        for j in range(k):
            val = nums[j]
            if freq[val] > 0:
                score = (score - pow(val, freq[val], MOD) + MOD) % MOD
            freq[val] += 1
            score = (score + pow(val, freq[val], MOD)) % MOD
        ans = score
        for j in range(k, n):
            rem_val = nums[j - k]
            score = (score - pow(rem_val, freq[rem_val], MOD) + MOD) % MOD
            freq[rem_val] -= 1
            if freq[rem_val] > 0:
                score = (score + pow(rem_val, freq[rem_val], MOD)) % MOD
            new_val = nums[j]
            if freq[new_val] > 0:
                score = (score - pow(new_val, freq[new_val], MOD) + MOD) % MOD
            freq[new_val] += 1
            score = (score + pow(new_val, freq[new_val], MOD)) % MOD
            ans = max(ans, score)
        return ans
