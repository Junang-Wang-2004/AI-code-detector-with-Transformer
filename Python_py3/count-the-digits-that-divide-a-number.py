# Time:  O(logn)
# Space: O(1)

# math
class Solution(object):
    def countDigits(self, num):
        """
        """
        result = 0
        curr = num
        while curr:
            result += int(num%(curr%10) == 0)
            curr //= 10
        return result
