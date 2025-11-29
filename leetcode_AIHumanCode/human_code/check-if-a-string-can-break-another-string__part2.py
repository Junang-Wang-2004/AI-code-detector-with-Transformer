# Time:  O(nlogn)
# Space: O(1)
import itertools


class Solution2(object):
    def checkIfCanBreak(self, s1, s2):
        """
        """
        return not {1, -1}.issubset(set(cmp(a, b) for a, b in zip(sorted(s1), sorted(s2))))


