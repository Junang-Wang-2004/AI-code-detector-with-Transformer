# Time:  O(n * n!)
# Space: O(n)

import collections
import itertools


class Solution2(object):
    def generatePalindromes(self, s):
        """
        """
        cnt = collections.Counter(s)
        mid = tuple(k for k, v in cnt.items() if v % 2)
        chars = ''.join(k * (v / 2) for k, v in cnt.items())
        return [''.join(half_palindrome + mid + half_palindrome[::-1]) \
                for half_palindrome in set(itertools.permutations(chars))] if len(mid) < 2 else []

