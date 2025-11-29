# Time:  O(nlogn)
# Space: O(1)
# constructive algorithms, sort, binary search, greedy
class Solution3(object):
    def maxIncreasingGroups(self, usageLimits):
        """
        """
        def check(l):
            curr = 0
            for i in range(l):
                curr += usageLimits[~i]-(l-i)
                curr = min(curr, 0)
            for i in range(len(usageLimits)-l):
                curr += usageLimits[i]
            return curr >= 0

        usageLimits.sort()
        left, right = 1, len(usageLimits)
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right


