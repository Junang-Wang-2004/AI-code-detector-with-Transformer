# Time:  O(n * l)
# Space: O(1)

import itertools


# string
class Solution(object):
    def countPrefixes(self, words, s):
        """
        """
        return sum(map(s.startswith, words))
