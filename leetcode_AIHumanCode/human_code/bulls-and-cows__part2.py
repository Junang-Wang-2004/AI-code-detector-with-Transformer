# Time:  O(n)
# Space: O(10) = O(1)

import operator


# One pass solution.
from collections import defaultdict, Counter



class Solution2(object):
    def getHint(self, secret, guess):
        """
        """
        A = sum(map(operator.eq, secret, guess))
        B = sum((Counter(secret) & Counter(guess)).values()) - A
        return "%dA%dB" % (A, B)

