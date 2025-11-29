class Solution(object):
    def maxValue(self, nums, k):
        n = len(nums)
        MS = 128
        INF = 10**9
        dp_l = [INF] * MS
        cnt_l = [0] * MS
        pos_l = [n] * MS
        for i in range(n):
            v = nums[i]
            dp_l[v] = 1
            for m in range(MS):
                if (v & m) == v:
                    cnt_l[m] += 1
                dp_l[m | v] = min(dp_l[m | v], dp_l[m] + 1)
            for m in range(MS):
                if cnt_l[m] >= k and dp_l[m] <= k and pos_l[m] == n:
                    pos_l[m] = i
        dp_r = [INF] * MS
        cnt_r = [0] * MS
        pos_r = [-1] * MS
        for i in range(n - 1, -1, -1):
            v = nums[i]
            dp_r[v] = 1
            for m in range(MS):
                if (v & m) == v:
                    cnt_r[m] += 1
                dp_r[m | v] = min(dp_r[m | v], dp_r[m] + 1)
            for m in range(MS):
                if cnt_r[m] >= k and dp_r[m] <= k and pos_r[m] == -1:
                    pos_r[m] = i
        for xv in range(MS - 1, -1, -1):
            for lv in range(1, MS):
                rv = xv ^ lv
                if pos_l[lv] < pos_r[rv]:
                    return xv
        return 0
