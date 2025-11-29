# Time:  O(n)
# Space: O(min(n, k))

import collections


# prefix sum, freq table
class Solution(object):
    def numGoodSubarrays(self, nums, k):
        """
        """
        result = prefix = 0
        cnt = collections.defaultdict(int)
        cnt[0] = 1
        i = 0
        while i < len(nums):
            j, prefix2 = i, prefix
            while j < len(nums) and nums[j] == nums[i]:
                prefix2 = (prefix2+nums[j])%k
                result += cnt[prefix2]
                j += 1
            while i < j:
                prefix = (prefix+nums[i])%k
                cnt[prefix] += 1
                i += 1
        return result


