# Time:  O(n)
# Space: O(n)

import collections


class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        """
        lookup = collections.defaultdict(lambda: [False]*3)
        for r, c in reservedSeats:
            if 2 <= c <= 5:
                lookup[r][0] = True
            if 4 <= c <= 7:
                lookup[r][1] = True
            if 6 <= c <= 9:
                lookup[r][2] = True
        result = 2*n
        for a, b, c in lookup.values():
            if not a and not c:
                continue
            if not a or not b or not c:
                result -= 1
                continue
            result -= 2
        return result


