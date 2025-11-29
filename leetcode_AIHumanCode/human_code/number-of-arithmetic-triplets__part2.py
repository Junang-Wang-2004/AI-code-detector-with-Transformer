# Time:  O(n)
# Space: O(n)
import collections


# dp
class Solution2(object):
    def arithmeticTriplets(self, nums, diff):
        """
        """
        result = 0
        cnt1 = collections.Counter()
        cnt2 = collections.Counter()
        for x in nums:
            result += cnt2[x-diff]
            cnt2[x] += cnt1[x-diff]
            cnt1[x] += 1
        return result
