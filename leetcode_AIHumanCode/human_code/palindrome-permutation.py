# Time:  O(n)
# Space: O(1)

import collections


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        """
        return sum(v % 2 for v in list(collections.Counter(s).values())) < 2

