class Solution:
    def numberOfPoints(self, nums):
        if not nums:
            return 0
        intervals = sorted(nums)
        merged = []
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        total = 0
        for start, end in merged:
            total += end - start + 1
        return total
