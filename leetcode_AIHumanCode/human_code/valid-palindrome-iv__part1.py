# Time:  O(n)
# Space: O(1)

# string, two pointers
class Solution(object):
    def makePalindrome(self, s):
        """
        """
        return sum(s[i] != s[~i] for i in range(len(s)//2)) <= 2


