# Time:  O(n)
# Space: O(1)

import collections


class Solution3(object):
    def singleNumber(self, nums):
        """
        """
        return list((collections.Counter(list(set(nums)) * 3) - collections.Counter(nums)).keys())[0]


