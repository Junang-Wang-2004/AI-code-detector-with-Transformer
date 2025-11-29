# Time:  O(m * n)
# Space: O(k), k is min(m * n, max(x for arr in arrays for x in arr))
import collections


class Solution2(object):
    def longestCommomSubsequence(self, arrays):
        """
        """
        return [num for num, cnt in collections.Counter(x for arr in arrays for x in arr).items() if cnt == len(arrays)]
