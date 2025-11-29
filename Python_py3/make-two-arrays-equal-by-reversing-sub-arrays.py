# Time:  O(n)
# Space: O(n)

import collections


class Solution(object):
    def canBeEqual(self, target, arr):
        """
        """
        return collections.Counter(target) == collections.Counter(arr)


# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def canBeEqual(self, target, arr):
        """
        """
        target.sort(), arr.sort()
        return target == arr
