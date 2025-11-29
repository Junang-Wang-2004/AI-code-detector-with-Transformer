# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxPower(self, s):
        """
        """
        result, count = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            result = max(result, count)
        return result


