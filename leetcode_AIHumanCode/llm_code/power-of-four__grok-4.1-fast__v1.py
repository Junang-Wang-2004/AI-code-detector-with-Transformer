class Solution:
    def isPowerOfFour(self, val):
        if val <= 0:
            return False
        while val % 4 == 0:
            val //= 4
        return val == 1
