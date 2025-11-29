# Time:  O(nlogn)
# Space: O(1)
import itertools


class Solution3(object):
    def checkIfCanBreak(self, s1, s2):
        """
        """
        s1, s2 = sorted(s1), sorted(s2)
        return all(a >= b for a, b in zip(s1, s2)) or \
               all(a <= b for a, b in zip(s1, s2))
