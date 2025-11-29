# Time:  O(n * k * r + n * r^2)
# Space: O(n * k * r)
# prefix sum, dp
class Solution(object):
    def maxValue(self, nums, k):
        """
        """
        left = [[set() if j else {0} for j in range(k+1)] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            for j in range(1, len(left[i+1])):
                left[i+1][j] = set(left[i][j])
                for x in left[i][j-1]:
                    left[i+1][j].add(x|nums[i])
        right = [[set() if j else {0} for j in range(k+1)] for i in range(len(nums)+1)]
        for i in reversed(range(len(nums))):
            for j in range(1, len(right[i])):
                right[i][j] = set(right[i+1][j])
                for x in right[i+1][j-1]:
                    right[i][j].add(x|nums[i])
        return max(l^r for i in range(k, (len(nums)-k)+1) for l in left[i][k] for r in right[i][k])
