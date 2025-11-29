# Time:  O(n)
# Space: O(1)

# string
class Solution(object):
    def kthCharacter(self, s, k):
        """
        """
        l = 0
        for i in range(len(s)):
            if s[i] == ' ':
                l = 0
                k -= 1
            else:
                l += 1
                k -= l
            if k < 0:
                break
        return s[i]
