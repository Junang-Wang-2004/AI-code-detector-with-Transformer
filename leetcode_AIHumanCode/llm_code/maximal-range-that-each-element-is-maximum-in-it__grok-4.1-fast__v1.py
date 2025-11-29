class Solution(object):
    def maximumLengthOfRanges(self, nums):
        n = len(nums)
        prev = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
            stack.append(i)
        nxt = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                nxt[i] = stack[-1]
            stack.append(i)
        return [nxt[i] - prev[i] - 1 for i in range(n)]
