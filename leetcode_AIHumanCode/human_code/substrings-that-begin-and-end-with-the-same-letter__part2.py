# Time:  O(n)
# Space: O(1)
import collections


class Solution(object):
    def numberOfSubstrings(self, s):
        """
        """
        return sum(v*(v+1)//2 for v in collections.Counter(s).values())
