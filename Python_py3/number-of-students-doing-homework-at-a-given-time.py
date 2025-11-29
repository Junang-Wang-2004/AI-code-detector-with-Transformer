# Time:  O(n)
# Space: O(1)

import itertools


class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        """
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))
