# Time:  O(logn)
# Space: O(logn)
# Recursive solution.
class Solution2(object):
    def integerReplacement(self, n):
        """
        """
        if n < 4:
            return [0, 0, 1, 2][n]
        if n % 4 in (0, 2):
            return self.integerReplacement(n / 2) + 1
        elif n % 4 == 1:
            return self.integerReplacement((n - 1) / 4) + 3
        else:
            return self.integerReplacement((n + 1) / 4) + 3


