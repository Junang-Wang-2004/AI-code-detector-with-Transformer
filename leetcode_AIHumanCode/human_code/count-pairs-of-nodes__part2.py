# Time:  O(nlogn + q * (n + e))
# Space: O(n + e)
import collections


# two pointers solution
class Solution2(object):
    def countPairs(self, n, edges, queries):
        """
        """
        degree = [0]*(n+1)
        shared = collections.Counter((min(n1, n2), max(n1, n2)) for n1, n2 in edges)
        for n1, n2 in edges:
            degree[n1] += 1
            degree[n2] += 1
        sorted_degree = sorted(degree)
        result = []
        for k, q in enumerate(queries):
            left, right = 1, n
            cnt = 0
            while left < right:
                if q < sorted_degree[left]+sorted_degree[right]:
                    cnt += right-left
                    right -= 1
                else:
                    left += 1
            for (i, j), shared_degree in shared.items():
                if degree[i]+degree[j]-shared_degree <= q < degree[i]+degree[j]:
                    cnt -= 1
            result.append(cnt)
        return result
