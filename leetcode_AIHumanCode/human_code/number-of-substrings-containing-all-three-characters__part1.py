# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        """
        result, left = 0, [-1]*3
        for right, c in enumerate(s):
            left[ord(c)-ord('a')] = right
            result += min(left)+1
        return result


