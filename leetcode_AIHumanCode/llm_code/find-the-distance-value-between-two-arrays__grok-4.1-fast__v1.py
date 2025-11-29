import bisect

class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2_sorted = sorted(arr2)
        count = 0
        for val in arr1:
            start = bisect.bisect_left(arr2_sorted, val - d)
            end = bisect.bisect_right(arr2_sorted, val + d)
            if start == end:
                count += 1
        return count
