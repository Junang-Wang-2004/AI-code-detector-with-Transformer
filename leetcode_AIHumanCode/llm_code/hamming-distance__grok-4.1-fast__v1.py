class Solution:
    def hammingDistance(self, x, y):
        result = 0
        for _ in range(32):
            if (x & 1) != (y & 1):
                result += 1
            x >>= 1
            y >>= 1
        return result
