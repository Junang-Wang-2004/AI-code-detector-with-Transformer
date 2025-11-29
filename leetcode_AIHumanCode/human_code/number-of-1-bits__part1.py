# Time:  O(32), bit shift in python is not O(1), it's O(k), k is the number of bits shifted
#             , see https://github.com/python/cpython/blob/2.7/Objects/longobject.c#L3652
# Space: O(1)

class Solution(object):
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n & 0x0F0F0F0F) + ((n >> 4) & 0x0F0F0F0F)
        n = (n & 0x00FF00FF) + ((n >> 8) & 0x00FF00FF)
        n = (n & 0x0000FFFF) + ((n >> 16) & 0x0000FFFF)
        return n


