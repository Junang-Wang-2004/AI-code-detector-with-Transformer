from collections import defaultdict


class Solution:
    def longestEqualSubarray(self, nums, k):
        positions = defaultdict(list)
        for idx, val in enumerate(nums):
            positions[val].append(idx)
        maximum = 0
        for coords in positions.values():
            length = len(coords)
            right = 0
            for left in range(length):
                while right < length and coords[right] <= coords[left] + (right - left) + k:
                    right += 1
                maximum = max(maximum, right - left)
        return maximum
