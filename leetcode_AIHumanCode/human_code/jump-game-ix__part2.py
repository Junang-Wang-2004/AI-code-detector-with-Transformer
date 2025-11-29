# Time:  O(n)
# Space: O(n)
# graph, prefix sum
class Solution2(object):
    def maxValue(self, nums):
        """
        """
        suffix = [float("inf")]*(len(nums)+1)
        for i in reversed(range(len(nums))):
            suffix[i] = min(suffix[i+1], nums[i])
        result = [0]*len(nums)
        mx = left = 0
        for right in range(len(nums)):
            mx = max(mx, nums[right])
            if mx > suffix[right+1]:
                continue
            while left <= right:
                result[left] = mx
                left += 1
        return result
