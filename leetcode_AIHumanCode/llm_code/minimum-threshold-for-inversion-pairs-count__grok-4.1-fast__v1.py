from bisect import bisect_left

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 2)

    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & -idx

    def prefix_sum(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res


class Solution:
    def minThreshold(self, nums, k):
        max_val = nums[0]
        upper = 0
        for val in nums[1:]:
            upper = max(upper, max_val - val)
            max_val = max(max_val, val)

        unique_sorted = sorted(set(nums))
        coord = {v: i + 1 for i, v in enumerate(unique_sorted)}
        sz = len(unique_sorted)

        def feasible(thresh):
            ft = FenwickTree(sz)
            pairs = 0
            for num in reversed(nums):
                rk = coord[num]
                target = num - thresh
                start_idx = bisect_left(unique_sorted, target)
                low = start_idx + 1
                high = rk - 1
                if low <= high:
                    pairs += ft.prefix_sum(high) - ft.prefix_sum(low - 1)
                ft.update(rk, 1)
            return pairs >= k

        lo = 0
        hi = upper
        while lo <= hi:
            pivot = lo + (hi - lo) // 2
            if feasible(pivot):
                hi = pivot - 1
            else:
                lo = pivot + 1
        ans = lo
        return ans if ans <= upper else -1
