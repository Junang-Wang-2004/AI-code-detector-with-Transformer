class Solution:
    def maximumBags(self, cap, stones, extra):
        diffs = sorted(capacity - stone for capacity, stone in zip(cap, stones))
        total_needed = 0
        filled = 0
        for need in diffs:
            total_needed += need
            if total_needed > extra:
                return filled
            filled += 1
        return filled
