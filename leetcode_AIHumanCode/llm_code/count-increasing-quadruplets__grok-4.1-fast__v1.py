class Solution(object):
    def countQuadruplets(self, nums):
        n = len(nums)
        left_small = [[0] * (n + 1) for _ in range(n)]
        for k in range(n):
            cum = 0
            for i in range(k):
                cum += (nums[i] < nums[k])
                left_small[k][i + 1] = cum
        right_large = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            cum = 0
            for pos in range(n - 1, j, -1):
                cum += (nums[pos] > nums[j])
                right_large[j][pos] = cum
        res = 0
        for k in range(n):
            for j in range(k):
                if nums[k] < nums[j]:
                    res += left_small[k][j] * right_large[j][k + 1]
        return res
