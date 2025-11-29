class Solution:
    def minimumDeviation(self, nums):
        n = len(nums)
        candidates = []
        for i, val in enumerate(nums):
            start = val * 2 if val % 2 else val
            cur = start
            while True:
                candidates.append((cur, i))
                if cur % 2:
                    break
                cur //= 2
        candidates.sort()
        counts = [0] * n
        full_cover = 0
        min_range = float('inf')
        j = 0
        for i in range(len(candidates)):
            _, idx = candidates[i]
            counts[idx] += 1
            if counts[idx] == 1:
                full_cover += 1
            while full_cover == n and j <= i:
                left_val, left_idx = candidates[j]
                right_val, _ = candidates[i]
                min_range = min(min_range, right_val - left_val)
                counts[left_idx] -= 1
                if counts[left_idx] == 0:
                    full_cover -= 1
                j += 1
        return min_range
