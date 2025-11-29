# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def myPow(self, x, n):
        """
        """
        result = 1
        abs_n = abs(n)
        while abs_n:
            if abs_n & 1:
                result *= x
            abs_n >>= 1
            x *= x

        return 1 / result if n < 0 else result


