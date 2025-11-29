# Time:  O(nlogn)
# Space: O(n)
class Solution3(object):
    def isAnagram(self, s, t):
        """
        """
        return sorted(s) == sorted(t)

