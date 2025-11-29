# Time:  O(n^2)
# Space: O(n^2)

import collections


# freq table
class Solution(object):
    def numberOfSubsequences(self, nums):
        """
        """
        cnt = collections.defaultdict(int)
        result = 0
        for r in range(4, len(nums)-2):
            q = r-2
            for p in range((q-2)+1):
                cnt[float(nums[p])/nums[q]] += 1
            for s in range(r+2, len(nums)):
                result += cnt[float(nums[s])/nums[r]]
        return result


