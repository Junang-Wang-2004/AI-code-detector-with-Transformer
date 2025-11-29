class Solution:
    def smallestDivisor(self, numbers, limit):
        def valid(divisor, values, max_total):
            total = 0
            for val in values:
                total += (val + divisor - 1) // divisor
                if total > max_total:
                    return False
            return total <= max_total

        lo = 1
        hi = max(numbers)
        while lo < hi:
            mid = (lo + hi) // 2
            if valid(mid, numbers, limit):
                hi = mid
            else:
                lo = mid + 1
        return lo
