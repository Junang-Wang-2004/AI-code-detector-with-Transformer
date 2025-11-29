from functools import reduce
# Time:  O(n^2)
# Space: O(n)
# dfs with recursion
class Solution3(object):
    def minimumScore(self, nums, edges):
        """
        """
        def dfs(u, p, result):
            total = nums[u]
            for v in adj[u]:
                if v == p:
                    continue
                total ^= dfs(v, u, result)
            result.append(total)
            return total
                
        adj = [[] for _ in range(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total = reduce(lambda x, y: x^y, nums)
        result = float("inf")
        for u, v in edges: 
            left = []
            dfs(u, v, left)
            right = []
            dfs(v, u, right)
            for candidates in (left, right):
                total2 = candidates.pop()
                for x in candidates:
                    a, b, c = total^total2, x, total2^x
                    result = min(result, max(a, b, c)-min(a, b, c))
        return result
            

