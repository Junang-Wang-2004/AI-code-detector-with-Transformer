class Solution(object):
    def maxScoreIndices(self, nums):
        n = len(nums)
        num_ones = 0
        for num in nums:
            num_ones += num
        left_zeros = 0
        best = -1
        positions = []
        for end in range(n + 1):
            left_ones = end - left_zeros
            current = left_zeros + num_ones - left_ones
            if current > best:
                best = current
                positions = [end]
            elif current == best:
                positions.append(end)
            if end < n:
                if nums[end] == 0:
                    left_zeros += 1
        return positions
