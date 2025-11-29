# Time:  O(n)
# Space: O(26)
import collections


# freq table
class Solution2(object):
    def minimumLength(self, s):
        """
        """
        return sum(2-x%2 for x in collections.Counter(s).values())
