# Time:  O(n)
# Space: O(1)

import collections


class Solution(object):
    def minSteps(self, s, t):
        """
        """
        diff = collections.Counter(s) - collections.Counter(t)
        return sum(diff.values())
