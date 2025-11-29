class Solution:
    def minConnectedGroups(self, intervals, k):
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        if n == 0:
            return 0
        group_starts = []
        cur_max_end = float('-inf')
        for i in range(n):
            if cur_max_end < intervals[i][0]:
                group_starts.append(i)
            cur_max_end = max(cur_max_end, intervals[i][1])
        total_groups = len(group_starts)
        def bisect_right(arr, x):
            low = 0
            high = len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] <= x:
                    low = mid + 1
                else:
                    high = mid
            return low
        max_saved = 0
        l = 0
        for r in range(n):
            while l < n and intervals[r][0] - intervals[l][1] > k:
                l += 1
            cnt = bisect_right(group_starts, r) - bisect_right(group_starts, l)
            if cnt > max_saved:
                max_saved = cnt
        return total_groups - max_saved
