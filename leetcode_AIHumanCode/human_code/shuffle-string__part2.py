# Time:  O(n)
# Space: O(1)
import itertools


class Solution2(object):
    def restoreString(self, s, indices):
        """
        """
        result = ['']*len(s)
        for i, c in zip(indices, s):
            result[i] = c
        return "".join(result)
