# Time:  O(nlog(logm)), n the length of nums, m is the max value of nums
# Space: O(logm)

import bisect


class Solution(object):
    def __init__(self):
        M = 10**5
        self.__lookup = [0]
        i = 10
        while i < M:
            self.__lookup.append(i)
            i *= 10
        self.__lookup.append(i)

    def findNumbers(self, nums):
        """
        """
        def digit_count(n):
            return bisect.bisect_right(self.__lookup, n)

        return sum(digit_count(n) % 2 == 0 for n in nums)
    

