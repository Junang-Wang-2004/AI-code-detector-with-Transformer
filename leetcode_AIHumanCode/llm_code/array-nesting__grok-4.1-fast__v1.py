class Solution:
    def arrayNesting(self, nums):
        n = len(nums)
        seen = [False] * n
        maximum = 0
        for start in range(n):
            if seen[start]:
                continue
            steps = 0
            pos = start
            while not seen[pos]:
                seen[pos] = True
                pos = nums[pos]
                steps += 1
            maximum = max(maximum, steps)
        return maximum
