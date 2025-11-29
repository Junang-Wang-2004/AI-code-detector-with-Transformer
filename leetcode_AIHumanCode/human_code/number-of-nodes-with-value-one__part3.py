# Time:  O(q + n)
# Space: O(q + logn)
import collections


# dfs
class Solution3(object):
    def numberOfNodes(self, n, queries):
        """
        """
        def dfs(u, curr):
            curr ^= cnt[u]%2
            return curr+sum(dfs(v, curr) for v in range(2*u, min(2*u+1, n)+1))
    
        cnt = collections.Counter(queries)
        return dfs(1, 0)
