# Time:  O(m + n^2)
# Space: O(m + n)
import collections


class Solution3(object):
    def maximalNetworkRank(self, n, roads):
        """
        """
        degree = [0]*n
        adj = collections.defaultdict(set)
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            adj[a].add(b)
            adj[b].add(a)
        result = 0
        for i in range(n-1):
            for j in range(i+1, n):
                result = max(result, degree[i]+degree[j]-int(i in adj and j in adj[i]))
        return result
