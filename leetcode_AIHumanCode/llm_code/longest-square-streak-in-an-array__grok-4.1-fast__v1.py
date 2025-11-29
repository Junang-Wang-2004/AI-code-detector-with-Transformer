class Solution:
    def longestSquareStreak(self, nums):
        unique_sorted = sorted(set(nums))
        lengths = {}
        longest = 0
        for num in unique_sorted:
            sq_root = int(num ** 0.5)
            prior = lengths.get(sq_root, 0) if sq_root * sq_root == num else 0
            lengths[num] = prior + 1
            longest = max(longest, lengths[num])
        return longest if longest > 1 else -1
