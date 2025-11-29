# Time:  O(n)
# Space: O(1)

class Solution(object):
    def generateTheString(self, n):
        """
        """
        result = ['a']*(n-1)
        result.append('a' if n%2 else 'b')
        return "".join(result)
