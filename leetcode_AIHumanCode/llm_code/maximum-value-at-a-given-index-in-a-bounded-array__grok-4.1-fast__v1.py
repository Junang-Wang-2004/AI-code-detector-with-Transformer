class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        extra = maxSum - n
        lo = 0
        hi = extra
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self._feasible(mid, index, n - index, extra):
                lo = mid
            else:
                hi = mid - 1
        return lo + 1

    def _feasible(self, h: int, left_len: int, right_len: int, extra: int) -> bool:
        def side(hh: int, len_side: int) -> int:
            if hh < 0:
                return 0
            bot = max(0, hh - (len_side - 1))
            cnt = hh - bot + 1
            return (hh + bot) * cnt // 2

        sum_left = side(h, left_len)
        sum_right = side(h, right_len)
        return sum_left + sum_right - h <= extra
