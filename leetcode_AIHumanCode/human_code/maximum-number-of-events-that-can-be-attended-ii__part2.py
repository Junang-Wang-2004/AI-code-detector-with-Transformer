# Time:  O(nlogn + n * k)
# Space: O(n * k)
import bisect


class Solution2(object):
    def maxValue(self, events, k):
        """
        """
        events.sort()
        sorted_starts = [x[0] for x in events]
        dp = [[0]*(k+1) for _ in range(len(events)+1)]
        for i in reversed(range(len(events))):
            next_i = bisect.bisect_right(sorted_starts, events[i][1])-1
            for j in range(1, k+1):
                dp[i][j] = max(dp[i+1][j], dp[next_i+1][j-1]+events[i][2])
        return dp[0][-1]
