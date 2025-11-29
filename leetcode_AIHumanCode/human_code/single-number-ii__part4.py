# Time:  O(n)
# Space: O(1)

import collections


class Solution4(object):
    def singleNumber(self, nums):
        """
        """
        return (sum(set(nums)) * 3 - sum(nums)) / 2


#  every element appears 4 times except for one with 2 times
