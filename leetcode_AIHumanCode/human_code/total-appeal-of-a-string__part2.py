# Time:  O(n)
# Space: O(26)
# counting
class Solution2(object):
    def appealSum(self, s):
        """
        """
        result = cnt = 0
        lookup = [-1]*26
        for i, c in enumerate(s):
            cnt += i-lookup[ord(c)-ord('a')]
            lookup[ord(c)-ord('a')] = i
            result += cnt
        return result

