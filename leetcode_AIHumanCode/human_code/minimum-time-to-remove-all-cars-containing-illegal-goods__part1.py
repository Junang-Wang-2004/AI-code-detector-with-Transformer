# Time:  O(n)
# Space: O(1)

# dp
class Solution(object):
    def minimumTime(self, s):
        """
        """
        left = 0
        result = left+(len(s)-0)
        for i in range(1, len(s)+1):
            left = min(left+2*(s[i-1] == '1'), i)
            result = min(result, left+(len(s)-i))
        return result


