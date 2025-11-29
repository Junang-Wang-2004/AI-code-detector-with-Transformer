class Solution(object):
    def countGood(self, nums, k):
        n = len(nums)
        total = n * (n + 1) // 2
        freq = {}
        j = 0
        dup_pairs = 0
        small = 0
        for r in range(n):
            x = nums[r]
            prev = freq.get(x, 0)
            dup_pairs += prev
            freq[x] = prev + 1
            while dup_pairs >= k and j <= r:
                y = nums[j]
                prev_y = freq.get(y, 0)
                dup_pairs -= prev_y - 1
                freq[y] = prev_y - 1
                j += 1
            small += r - j + 1
        return total - small
