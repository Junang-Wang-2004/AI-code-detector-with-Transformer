class Solution(object):
    def findMaximums(self, nums):
        n = len(nums)
        prev_small = [-1] * n
        mono = []
        for j in range(n):
            while mono and nums[mono[-1]] >= nums[j]:
                mono.pop()
            if mono:
                prev_small[j] = mono[-1]
            mono.append(j)
        next_small = [n] * n
        mono = []
        for j in range(n - 1, -1, -1):
            while mono and nums[mono[-1]] >= nums[j]:
                mono.pop()
            if mono:
                next_small[j] = mono[-1]
            mono.append(j)
        output = [-1] * n
        for j in range(n):
            span = next_small[j] - prev_small[j] - 1
            idx = span - 1
            output[idx] = max(output[idx], nums[j])
        for j in range(n - 2, -1, -1):
            output[j] = max(output[j], output[j + 1])
        return output
