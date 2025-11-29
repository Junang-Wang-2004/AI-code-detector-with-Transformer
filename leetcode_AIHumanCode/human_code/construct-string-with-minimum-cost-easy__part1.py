# Time:  O(n * w * l)
# Space: O(l)

import itertools
from functools import reduce


# dp
class Solution(object):
    def minimumCost(self, target, words, costs):
        """
        """
        INF = float("inf")
        l = max(len(w) for w in words)
        dp = [INF]*(l+1)
        dp[0] = 0
        for i in range(len(target)):
            if dp[i%len(dp)] == INF:
                continue
            for w, c in zip(words, costs):
                if target[i:i+len(w)] == w:
                    dp[(i+len(w))%len(dp)] = min(dp[(i+len(w))%len(dp)], dp[i%len(dp)]+c)
            dp[i%len(dp)] = INF
        return dp[len(target)%len(dp)] if dp[len(target)%len(dp)] != INF else -1


