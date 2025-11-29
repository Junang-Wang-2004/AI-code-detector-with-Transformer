# Time:  O(n)
# Space: O(l), l is the max length of words
class Solution2(object):
    def firstPalindrome(self, words):
        """
        """
        return next((x for x in words if x == x[::-1]), "")
