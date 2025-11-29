# Time:  O(n)
# Space: O(1)

# two pointers
class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        """
        result = 0
        for i in range(len(s)):
            left, right = i+1, i
            while left-1 >= 0 and right+1 < len(s) and s[left-1] == '0' and s[right+1] == '1':
                left -= 1
                right += 1
            result = max(result, right-left+1)
        return result


