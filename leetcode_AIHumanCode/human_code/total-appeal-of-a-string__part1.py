# Time:  O(n)
# Space: O(26)

# combinatorics
class Solution(object):
    def appealSum(self, s):
        """
        """
        result = curr = 0
        lookup = [-1]*26
        for i, c in enumerate(s):
            result += (i-lookup[ord(c)-ord('a')])*(len(s)-i)
            lookup[ord(c)-ord('a')] = i
        return result


