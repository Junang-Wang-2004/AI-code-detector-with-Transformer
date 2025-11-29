class Solution(object):
    def numberOfPairs(self, nums):
        counts = {}
        for value in nums:
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1
        total_pairs = 0
        for frequency in counts.values():
            total_pairs += frequency // 2
        remaining = len(nums) - 2 * total_pairs
        return [total_pairs, remaining]
