# Time:  O(n + m)
# Space: O(n + m)
import collections
import itertools


class Solution2(object):
    def oddCells(self, n, m, indices):
        """
        """
        fn = lambda x: sum(count&1 for count in collections.Counter(x).values())
        row_sum, col_sum = list(map(fn, zip(*indices)))
        return row_sum*m+col_sum*n-2*row_sum*col_sum
