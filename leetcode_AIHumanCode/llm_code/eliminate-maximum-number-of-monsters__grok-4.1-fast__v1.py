class Solution:
    def eliminateMaximum(self, dist, speed):
        n = len(dist)
        arr_times = sorted((d - 1) // s for d, s in zip(dist, speed))
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if mid < len(arr_times) and mid <= arr_times[mid]:
                left = mid + 1
            else:
                right = mid
        return left
