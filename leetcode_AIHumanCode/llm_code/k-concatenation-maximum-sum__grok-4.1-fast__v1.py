class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        MOD = 10**9 + 7
        n = len(arr)
        if n == 0:
            return 0
        arr_sum = sum(arr)
        max_current = max_global = arr[0]
        for i in range(1, n):
            max_current = max(arr[i], max_current + arr[i])
            max_global = max(max_global, max_current)
        max_one = max_global
        prefix_sum = 0
        max_prefix = float('-inf')
        for num in arr:
            prefix_sum += num
            max_prefix = max(max_prefix, prefix_sum)
        suffix_sum = 0
        max_suffix = float('-inf')
        for i in range(n - 1, -1, -1):
            suffix_sum += arr[i]
            max_suffix = max(max_suffix, suffix_sum)
        if k == 1:
            return max(max_one, 0) % MOD
        max_two = max(max_one, max_prefix + max_suffix)
        result = max(max_two, 0) + max(0, k - 2) * max(arr_sum, 0)
        return result % MOD
