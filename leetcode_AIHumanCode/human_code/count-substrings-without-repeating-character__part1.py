# Time:  O(n)
# Space: O(1)

# two pointers, sliding window
class Solution(object):
    def numberOfSpecialSubstrings(self, s):
        """
        """
        result = left = 0
        lookup = [-1]*26
        for right in range(len(s)):
            if lookup[ord(s[right])-ord('a')] >= left:
                left = lookup[ord(s[right])-ord('a')]+1
            lookup[ord(s[right])-ord('a')] = right
            result += (right-left+1)
        return result


