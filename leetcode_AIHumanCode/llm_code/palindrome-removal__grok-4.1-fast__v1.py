class Solution(object):
    def minimumMoves(self, arr):
        n = len(arr)
        memo = {}
        def compute(lo, hi):
            if lo > hi:
                return 0
            if lo == hi:
                return 1
            key = (lo, hi)
            if key in memo:
                return memo[key]
            result = 1 + compute(lo + 1, hi)
            if lo + 1 <= hi and arr[lo] == arr[lo + 1]:
                result = min(result, 1 + compute(lo + 2, hi))
            for m in range(lo + 2, hi + 1):
                if arr[lo] == arr[m]:
                    result = min(result, compute(lo + 1, m - 1) + compute(m + 1, hi))
            memo[key] = result
            return result
        return compute(0, n - 1)
