# Time:  O(n)
# Space: O(1)

# string
class Solution(object):
    def minLengthAfterRemovals(self, s):
        """
        """
        return abs(s.count('a')-s.count('b'))
