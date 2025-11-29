# Time:  O(n)
# Space: O(10) = O(1)

import operator


# One pass solution.
from collections import defaultdict, Counter



class Solution(object):
    def getHint(self, secret, guess):
        """
        """
        A, B = 0, 0
        lookup = defaultdict(int)
        for s, g in zip(secret, guess):
            if s == g:
                A += 1
            else:
                B += int(lookup[s] < 0) + int(lookup[g] > 0)
                lookup[s] += 1
                lookup[g] -= 1
        return "%dA%dB" % (A, B)


# Two pass solution.
