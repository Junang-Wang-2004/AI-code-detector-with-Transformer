# Time:  O(n^2)
# Space: O(n)
import collections


# freq table
class Solution3(object):
    def divisibleTripletCount(self, nums, d):
        """
        """
        result = 0
        for i in range(len(nums)):
            cnt = collections.Counter()
            for j in range(i+1, len(nums)):
                result += cnt[nums[j]%d]
                cnt[-(nums[i]+nums[j])%d] += 1
        return result
