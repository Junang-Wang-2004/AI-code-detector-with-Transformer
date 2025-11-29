from functools import reduce
# Time:  O(n^2)
# Space: O(n)
# dfs with stk (slower, sometimes TLE)
class Solution4(object):
    def minimumScore(self, nums, edges):
        """
        """
        def iter_dfs(nums, adj, u, p):
            result = []
            stk = [(1, (u, p, [0]))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p, ret = args
                    new_rets = []
                    stk.append((2, (u, new_rets, ret)))
                    for v in adj[u]:
                        if v == p:
                            continue
                        new_rets.append([0])
                        stk.append((1, (v, u, new_rets[-1])))
                elif step == 2:
                    u, new_rets, ret = args
                    ret[0] = nums[u]
                    for x in new_rets:
                        ret[0] ^= x[0]
                    result.append(ret[0])
            return result
                
        adj = [[] for _ in range(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total = reduce(lambda x, y: x^y, nums)
        result = float("inf")
        for u, v in edges: 
            for candidates in (iter_dfs(nums, adj, u, v), iter_dfs(nums, adj, v, u)):
                total2 = candidates.pop()
                for x in candidates:
                    a, b, c = total^total2, x, total2^x
                    result = min(result, max(a, b, c)-min(a, b, c))
        return result
