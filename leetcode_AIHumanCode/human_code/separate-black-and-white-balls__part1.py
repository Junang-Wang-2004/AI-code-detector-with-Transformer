# Time:  O(n)
# Space: O(1)

# two pointers
class Solution(object):
    def minimumSteps(self, s):
        """
        """
        result = left = 0
        for right in range(len(s)):
            if s[right] != '0':
                continue
            result += right-left
            left += 1
        return result


