import collections


class Solution:
    def countKDifference(self, nums, k):
        freq = collections.Counter(nums)
        pairs = 0
        for num in freq:
            pairs += freq[num] * freq[num + k]
        return pairs
