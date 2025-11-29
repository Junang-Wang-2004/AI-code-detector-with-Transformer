# Time:  precompute: O(r)
#        runtime:    O(nlogx)
# Space: O(r + n)
import collections


# number theory, dfs, freq table
class Solution2(object):
    def sumOfAncestors(self, n, edges, nums):
        """
        """
        def prime_factors(x):
            result = 1
            while x != 1:
                if result%SPF[x] == 0:
                    result //= SPF[x]
                else:
                    result *= SPF[x]
                x //= SPF[x]
            return result

        def dfs(u, p):
            x = prime_factors(nums[u])
            result = cnt[x]
            cnt[x] += 1
            for v in adj[u]:
                if v == p:
                    continue
                result += dfs(v, u)
            cnt[x] -= 1
            return result

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        cnt = collections.defaultdict(int)
        return dfs(0, -1)
