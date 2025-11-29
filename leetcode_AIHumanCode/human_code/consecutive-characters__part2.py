# Time:  O(n)
# Space: O(n)
import itertools


class Solution2(object):
    def maxPower(self, s):
        return max(len(list(v)) for _, v in itertools.groupby(s))
