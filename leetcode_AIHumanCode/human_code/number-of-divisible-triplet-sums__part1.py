# Time:  O(n^2)
# Space: O(n)

import collections


# freq table
class Solution(object):
    def divisibleTripletCount(self, nums, d):
        """
        """
        result = 0
        cnt = collections.Counter()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j])%d in cnt:
                    result += cnt[(nums[i]+nums[j])%d]
            cnt[-nums[i]%d] += 1
        return result


