from functools import reduce
# Time:  O(n^2)
# Space: O(n)
# dfs with recursion
class Solution2(object):
    def minimumScore(self, nums, edges):
        """
        """
        def is_ancestor(a, b):
            return left[a] <= left[b] and right[b] <= right[a]

        def dfs(u, p):
            left[u] = cnt[0]
            cnt[0] += 1
            for v in adj[u]:
                if v == p:
                    continue
                dfs(v, u)
                nums[u] ^= nums[v]
            right[u] = cnt[0]
                
        adj = [[] for _ in range(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        cnt = [0]
        left = [0]*len(nums)
        right = [0]*len(nums)
        dfs(0, -1)
        result = float("inf")
        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                if is_ancestor(i, j):
                    a, b, c = nums[0]^nums[i], nums[i]^nums[j], nums[j]
                elif is_ancestor(j, i):
                    a, b, c = nums[0]^nums[j], nums[j]^nums[i], nums[i]
                else:
                    a, b, c = nums[0]^nums[i]^nums[j], nums[i], nums[j]
                result = min(result, max(a, b, c)-min(a, b, c))
        return result
            

