# Time:  O(n * p)
# Space: O(1)

# string
class Solution(object):
    def prefixCount(self, words, pref):
        """
        """
        return sum(x.startswith(pref) for x in words)
