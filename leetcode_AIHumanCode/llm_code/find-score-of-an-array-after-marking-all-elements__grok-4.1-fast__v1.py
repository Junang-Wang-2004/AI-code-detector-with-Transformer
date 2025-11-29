class Solution(object):
    def findScore(self, nums):
        n = len(nums)
        marked = [False] * n
        score = 0
        items = sorted((nums[j], j) for j in range(n))
        for num_val, idx in items:
            if marked[idx]:
                continue
            marked[idx] = True
            score += num_val
            if idx > 0:
                marked[idx - 1] = True
            if idx < n - 1:
                marked[idx + 1] = True
        return score
