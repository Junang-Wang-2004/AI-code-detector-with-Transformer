# Time:  O(1)
# Space: O(1)

class Solution(object):
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        while m < n:
            n &= n - 1
        return n


