# Time:  O(n)
# Space: O(n)

# prefix sum
class Solution(object):
    def minimumSum(self, nums):
        """
        """
        INF = float("inf")

        right = [INF]*len(nums)
        curr = INF
        for i in reversed(range(len(nums))):
            right[i] = curr
            curr = min(curr, nums[i])
        result = curr = INF
        for i in range(len(nums)):
            if curr < nums[i] > right[i]:
                result = min(result, curr+nums[i]+right[i])
            curr = min(curr, nums[i])
        return result if result != INF else -1


