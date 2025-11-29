class Solution:
    def trimMean(self, arr):
        n = len(arr)
        trim_size = n // 20
        sorted_arr = sorted(arr)
        mid_sum = sum(sorted_arr[trim_size:n - trim_size])
        mid_count = n - 2 * trim_size
        return mid_sum / mid_count
