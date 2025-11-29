# Time:  O(n)
# Space: O(1)

# graph, prefix sum
class Solution(object):
    def maxValue(self, nums):
        """
        """
        result = [0]*len(nums)
        result[0] = nums[0]
        for i in range(len(nums)-1):
            result[i+1] = max(result[i], nums[i+1])
        mn = float("inf")
        for i in reversed(range(len(nums))):
            if result[i] > mn:
                result[i] = result[i+1]
            mn = min(mn, nums[i])
        return result


