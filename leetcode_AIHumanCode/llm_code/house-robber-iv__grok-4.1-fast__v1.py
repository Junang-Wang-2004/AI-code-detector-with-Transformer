class Solution:
    def minCapability(self, nums, k):
        vals = sorted({v for v in nums})
        start, end = 0, len(vals) - 1
        while start <= end:
            pivot = start + (end - start) // 2
            if self._feasible(nums, k, vals[pivot]):
                end = pivot - 1
            else:
                start = pivot + 1
        return vals[start]

    def _feasible(self, arr, target, upper):
        picks = 0
        cursor = 0
        arr_len = len(arr)
        while cursor < arr_len:
            if arr[cursor] <= upper:
                picks += 1
                cursor += 2
            else:
                cursor += 1
        return picks >= target
