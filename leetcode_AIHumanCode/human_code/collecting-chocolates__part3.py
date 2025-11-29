# Time:  O(n^2)
# Space: O(n)
# brute force
class Solution3(object):
    def minCost(self, nums, x):
        """
        """
        result = [x*k for k in range(len(nums)+1)]
        for i in range(len(nums)):
            curr = nums[i]
            for k in range(len(result)):
                curr = min(curr, nums[(i+k)%len(nums)])
                result[k] += curr
        return min(result)
