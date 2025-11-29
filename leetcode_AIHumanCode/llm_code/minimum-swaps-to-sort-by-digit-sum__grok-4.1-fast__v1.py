class Solution(object):
    def minSwaps(self, nums):
        def digit_sum(val):
            total = 0
            while val > 0:
                total += val % 10
                val //= 10
            return total

        n = len(nums)
        indexed = [(digit_sum(nums[i]), nums[i], i) for i in range(n)]
        sorted_indexed = sorted(indexed)
        dest = [0] * n
        for j, (_, _, src) in enumerate(sorted_indexed):
            dest[src] = j
        seen = [False] * n
        swaps = 0
        for begin in range(n):
            if not seen[begin]:
                length = 0
                pos = begin
                while not seen[pos]:
                    seen[pos] = True
                    length += 1
                    pos = dest[pos]
                swaps += length - 1
        return swaps
