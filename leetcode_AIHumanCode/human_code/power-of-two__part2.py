# Time:  O(1)
# Space: O(1)

class Solution2(object):
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & ~-n) == 0

