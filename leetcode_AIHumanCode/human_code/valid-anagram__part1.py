# Time:  O(n)
# Space: O(1)

import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        """
        if len(s) != len(t):
            return False
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return False
        return True


