# Time:  O(nlogn)
# Space: O(n)
import collections


# two pointers, sliding window, freq table
class Solution2(object):
    def maxFrequencyScore(self, nums, k):
        """
        """
        MOD = 10**9+7
        result = curr = 0
        cnt = collections.Counter()
        for i in range(len(nums)):
            if i >= k:
                curr = (curr-pow(nums[i-k], cnt[nums[i-k]], MOD))%MOD
                cnt[nums[i-k]] -= 1
                if cnt[nums[i-k]]:
                    curr = (curr+pow(nums[i-k], cnt[nums[i-k]], MOD))%MOD
            if cnt[nums[i]]:
               curr = (curr-pow(nums[i], cnt[nums[i]], MOD))%MOD
            cnt[nums[i]] += 1
            curr = (curr+pow(nums[i], cnt[nums[i]], MOD))%MOD
            if i >= k-1:
                result = max(result, curr)
        return result
