# Time:  O(nlogn)
# Space: O(n)
# constructive algorithms, sort, binary search, greedy, prefix sum
class Solution4(object):
    def maxIncreasingGroups(self, usageLimits):
        """
        """
        def check(l):
            return all((i+1)*i//2 <= prefix[len(usageLimits)-(l-i)] for i in range(1, l+1))

        usageLimits.sort()
        prefix = [0]*(len(usageLimits)+1)
        for i in range(len(usageLimits)):
            prefix[i+1] = prefix[i]+usageLimits[i]
        left, right = 1, len(usageLimits)
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid):
                right = mid-1
            else:
                left = mid+1
        return right
