class Solution:
    def find132pattern(self, nums):
        n = len(nums)
        stack = []
        max_k = float('-inf')
        for i in range(n - 1, -1, -1):
            if nums[i] < max_k:
                return True
            while stack and nums[stack[-1]] < nums[i]:
                max_k = nums[stack.pop()]
            stack.append(i)
        return False
