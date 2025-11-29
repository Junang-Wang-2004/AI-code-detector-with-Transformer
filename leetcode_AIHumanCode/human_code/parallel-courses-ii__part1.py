# Time:  O((n * C(c, min(c, k))) * 2^n)
# Space: O(2^n)

import itertools


class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        """
        reqs = [0]*n
        for u, v in dependencies:
            reqs[v-1] |= 1 << (u-1)
        dp = [n]*(1<<n)
        dp[0] = 0
        for mask in range(1<<n):
            candidates = []
            for v in range(n):
                if (mask&(1<<v)) == 0 and (mask&reqs[v]) == reqs[v]:
                    candidates.append(v)
            for choice in itertools.combinations(candidates, min(len(candidates), k)):
                new_mask = mask
                for v in choice:
                    new_mask |= 1<<v
                dp[new_mask] = min(dp[new_mask], dp[mask]+1)
        return dp[-1]


