# Time:  O(n + e)
# Space: O(n + e)
import collections


# dfs, two pointers, sliding window, prefix sum
class Solution2(object):
    def longestSpecialPath(self, edges, nums):
        """
        """
        def dfs(u, p, d, left):
            prev_d, lookup[nums[u]-1] = lookup[nums[u]-1], d
            left = max(left, prev_d)
            result[0] = min(result[0], [-(prefix[(d-1)+1]-prefix[left+1]), d-left])
            for v, l in adj[u]:
                if v == p:
                    continue
                prefix.append(prefix[-1]+l)
                dfs(v, u, d+1, left)
                prefix.pop()
            lookup[nums[u]-1] = prev_d
    
        adj = [[] for _ in range(len(nums))]
        for u, v, l in edges:
            adj[u].append((v, l))
            adj[v].append((u, l))
        lookup = collections.defaultdict(lambda: -1)
        prefix = [0]
        result = [[float("inf"), float("inf")]]
        dfs(0, -1, 0, -1)
        return [-result[0][0], result[0][1]]
