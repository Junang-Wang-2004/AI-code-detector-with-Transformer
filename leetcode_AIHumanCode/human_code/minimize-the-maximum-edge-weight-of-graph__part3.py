# Time:  O(nlogw + e)
# Space: O(n + e)
import collections


# binary search, bfs
class Solution3(object):
    def minMaxWeight(self, n, edges, threshold):
        """
        """
        def binary_search(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        def check(x):
            cnt = len(adj)
            lookup = [False]*len(adj)
            lookup[0] = True
            cnt -= 1
            q = [0]
            while q:
                new_q = []
                for u in q:
                    for v, w in adj[u].items():
                        if w > x or lookup[v]:
                            continue
                        lookup[v] = True
                        cnt -= 1
                        new_q.append(v)
                q = new_q
            return cnt == 0
    
        adj = [collections.defaultdict(lambda: float("inf")) for _ in range(n)]
        for i, j, w in edges:
            adj[j][i] = min(adj[j][i], w)
        left, right = min(w for _, _, w in edges), max(w for _, _, w in edges)
        result = binary_search(left, right, check)
        return result if result <= right else -1
