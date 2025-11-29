# Time:  O(logn)
# Space: O(logn)
# Recursive solution.
class Solution2(object):
    def myPow(self, x, n):
        """
        """
        if n < 0 and n != -n:
            return 1.0 / self.myPow(x, -n)
        if n == 0:
            return 1
        v = self.myPow(x, n / 2)
        if n % 2 == 0:
            return v * v
        else:
            return v * v * x


