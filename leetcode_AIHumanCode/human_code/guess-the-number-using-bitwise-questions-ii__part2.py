from functools import reduce
# Time:  O(logr)
# Space: O(1)
# bit manipulation
class Solution2(object):
    def findNumber(self):
        """
        """
        BIT_COUNT = 30
        return reduce(lambda accu, i: accu|(1<<i if commonBits(1<<i)-commonBits(1<<i) == 1 else 0), range(BIT_COUNT), 0)
