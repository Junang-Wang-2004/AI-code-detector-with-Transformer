# Time:  O(nlogn + n * k^2)
# Space: O(n * k^2)

import bisect


# dp, binary search
class Solution(object):
    def maximumWeight(self, intervals):
        """
        """
        K = 4
        lookup = {}
        for i, (l, r, w) in enumerate(intervals):
            if (r, l, w) not in lookup:
                lookup[r, l, w] = i
        sorted_intervals = sorted(iter(lookup.keys()), key=lambda x: x[0])
        dp = [[[0, []] for _ in range(K+1)] for _ in range(len(sorted_intervals)+1)]
        for i in range(len(dp)-1):
            j = bisect.bisect_right(sorted_intervals, (sorted_intervals[i][1], 0, 0))-1
            idx = lookup[sorted_intervals[i]]
            for k in range(1, len(dp[i])):
                new_dp = [dp[j+1][k-1][0]-sorted_intervals[i][2], dp[j+1][k-1][1][:]]
                insort(new_dp[1], idx)
                dp[i+1][k] = min(dp[i][k], new_dp)
        return dp[len(sorted_intervals)][K][1]


