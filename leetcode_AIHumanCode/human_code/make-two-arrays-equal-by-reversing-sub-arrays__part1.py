# Time:  O(n)
# Space: O(n)

import collections


class Solution(object):
    def canBeEqual(self, target, arr):
        """
        """
        return collections.Counter(target) == collections.Counter(arr)


