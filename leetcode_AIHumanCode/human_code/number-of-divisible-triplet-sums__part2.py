# Time:  O(n^2)
# Space: O(n^2)
import collections


# freq table
class Solution2(object):
    def divisibleTripletCount(self, nums, d):
        """
        """
        result = 0
        cnt = collections.Counter()
        for i in range(len(nums)):
            if nums[i]%d in cnt:
                result += cnt[nums[i]%d]
            for j in range(i):
                cnt[-(nums[i]+nums[j])%d] += 1
        return result


