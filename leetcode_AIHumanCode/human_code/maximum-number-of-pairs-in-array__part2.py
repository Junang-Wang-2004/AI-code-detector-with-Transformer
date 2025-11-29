# Time:  O(n)
# Space: O(r), r = max(nums)
import collections


# freq table
class Solution2(object):
    def numberOfPairs(self, nums):
        """
        """
        cnt = collections.Counter(nums)
        pair_cnt = sum(x//2 for x in cnt.values())
        return [pair_cnt, len(nums)-2*pair_cnt]
