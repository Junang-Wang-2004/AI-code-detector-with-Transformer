# Time:  O(n^2)
# Space: O(n^2)
# prefix sum
class Solution3(object):
    def countQuadruplets(self, nums):
        """
        """
        left = [[0]*(len(nums)+1) for _ in range(len(nums))]
        for j in range(len(nums)):
            for i in range(j):
                left[j][i+1] = left[j][i] + int(nums[i] < nums[j])
        right = [[0]*(len(nums)+1) for _ in range(len(nums))]
        for j in range(len(nums)):
            for i in reversed(range(j+1, len(nums))):
                right[j][i] = right[j][i+1] + int(nums[i] > nums[j])
        result = 0
        for k in range(len(nums)):
            for j in range(k):
                if nums[k] < nums[j]:
                    result += left[k][j]*right[j][k+1]
        return result
