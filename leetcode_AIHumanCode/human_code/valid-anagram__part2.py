# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def isAnagram(self, s, t):
        """
        """
        return collections.Counter(s) == collections.Counter(t)


