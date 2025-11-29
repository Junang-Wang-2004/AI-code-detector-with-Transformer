# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        """
        if n == 0:
            return 1
        result = cnt = 1
        for i in range(n-1):
            cnt *= 9-i
            result += cnt
        return 1+9*result


