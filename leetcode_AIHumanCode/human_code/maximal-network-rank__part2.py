# Time:  O(m + nlogn + k^2), k is the number of values greater or equal to top2
# Space: O(m + n)
import collections


# optimized from Solution3
class Solution2(object):
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
        sorted_idx = list(range(n))
        sorted_idx.sort(key=lambda x:-degree[x])
        m = 2
        while m < n:
            if degree[sorted_idx[m]] != degree[sorted_idx[1]]:
                break
            m += 1
        result = degree[sorted_idx[0]] + degree[sorted_idx[1]] - 1  # at least sum(top2 values) - 1
        for i in range(m-1):  # only need to check pairs of top2 values
            for j in range(i+1, m):
                if degree[sorted_idx[i]]+degree[sorted_idx[j]]-int(sorted_idx[i] in adj and sorted_idx[j] in adj[sorted_idx[i]]) > result:  # if equal to ideal sum of top2 values, break
                    return degree[sorted_idx[i]]+degree[sorted_idx[j]]-int(sorted_idx[i] in adj and sorted_idx[j] in adj[sorted_idx[i]])                                                 
        return result


