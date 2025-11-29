from collections import Counter
import bisect

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        if not nums:
            return 0
        arr = sorted(nums)
        n = len(arr)
        count = Counter(nums)
        res = 0
        for val in count:
            l = bisect.bisect_left(arr, val - k)
            r = bisect.bisect_right(arr, val + k) - 1
            size = r - l + 1 if l <= r else 0
            f = count[val]
            res = max(res, f + min(size - f, numOperations))
        j = 0
        for i in range(n):
            while arr[i] - arr[j] > 2 * k:
                j += 1
            res = max(res, min(i - j + 1, numOperations))
        return res
