from functools import reduce
# Time:  O(logr)
# Space: O(1)

# bit manipulation
class Solution(object):
    def findNumber(self):
        """
        """
        BIT_COUNT = 30
        result = 0
        prev = commonBits(0)
        for i in range(BIT_COUNT):
            curr = commonBits(1<<i)
            if curr-prev == 1:
                result |= 1<<i
            prev = curr
        return result


