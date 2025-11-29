# Time:  O(n + e)
# Space: O(h)
import collections


# dfs, two pointers, sliding window, prefix sum
class Solution2(object):
    def longestSpecialPath(self, edges, nums):
        """
        """
        def dfs(u, p, d, left):
            prev_d, lookup[nums[u]-1] = lookup[nums[u]-1], d
            new_left = left[:]
            curr = prev_d
            for i in range(len(new_left)):
                if curr > new_left[i]:
                    curr, new_left[i] = new_left[i], curr
            result[0] = min(result[0], [-(prefix[(d-1)+1]-prefix[new_left[1]+1]), d-new_left[1]])
            for v, l in adj[u]:
                if v == p:
                    continue
                prefix.append(prefix[-1]+l)
                dfs(v, u, d+1, new_left)
                prefix.pop()
            lookup[nums[u]-1] = prev_d
    
        adj = [[] for _ in range(len(nums))]
        for u, v, l in edges:
            adj[u].append((v, l))
            adj[v].append((u, l))
        lookup = collections.defaultdict(lambda: -1)
        prefix = [0]
        result = [[float("inf"), float("inf")]]
        dfs(0, -1, 0, [-1]*2)
        return [-result[0][0], result[0][1]]
