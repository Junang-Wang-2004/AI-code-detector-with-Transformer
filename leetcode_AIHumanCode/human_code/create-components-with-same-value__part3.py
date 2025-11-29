# Time:  O(n * sqrt(n))
# Space: O(n)
# dfs, greedy
class Solution3(object):
    def componentValue(self, nums, edges):
        """
        """
        def dfs(u, p, target):
            total = nums[u]
            for v in adj[u]:
                if v == p:
                    continue
                total += dfs(v, u, target)
            return total if total != target else 0

        result = 0
        adj = [[] for _ in range(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total = sum(nums)
        for cnt in reversed(range(2, len(nums)+1)):
            if total%cnt == 0 and dfs(0, -1, total//cnt) == 0:
                return cnt-1
        return 0
