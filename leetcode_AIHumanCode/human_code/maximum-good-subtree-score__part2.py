# Time:  O(n * (2^10)^2)
# Space: O(2^10)
import collections


# bitmasks, dfs, tree dp
class Solution2(object):
    def goodSubtreeSum(self, vals, par):
        """
        """
        MOD = 10**9+7
        def get_mask(x):
            mask = 0
            while x:
                x, d = divmod(x, 10)
                if mask&(1<<d):
                    return -1
                mask |= 1<<d
            return mask

        def dfs(u):
            dp = collections.defaultdict(int)
            dp[0] = 0
            mask = get_mask(vals[u])
            if mask != -1:
                dp[mask] = vals[u]
            for v in adj[u]:
                new_dp = dfs(v)
                for m1, v1 in list(dp.items()):
                    for m2, v2 in new_dp.items():
                        if m1&m2:
                            continue
                        dp[m1|m2] =  max(dp[m1|m2], v1+v2)
            result[0] = (result[0]+max(dp.values()))%MOD
            return dp

        adj = [[] for _ in range(len(vals))]
        for u in range(1, len(par)):
            adj[par[u]].append(u)
        result = [0]
        dfs(0)
        return result[0]
