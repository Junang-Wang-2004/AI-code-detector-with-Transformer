# Time:  O(nlogn)
# Space: O(n)
import itertools


# binary search
class Solution2(object):
    def minCost(self, nums, cost):
        """
        """
        def f(x):
            return sum(abs(y-x)*c for y, c in zip(nums, cost))
    
        def check(x):
            return x+1 == len(idxs) or f(nums[idxs[x]]) < f(nums[idxs[x+1]])

        idxs = list(range(len(nums)))
        idxs.sort(key=lambda x: nums[x])
        left, right = 0, len(idxs)-1
        while left <= right:
            mid = left+(right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return f(nums[idxs[left]])


