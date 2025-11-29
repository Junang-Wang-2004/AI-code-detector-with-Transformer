# Time:  O(n * sqrt(n))
# Space: O(n)
# iterative dfs, greedy
class Solution2(object):
    def componentValue(self, nums, edges):
        """
        """
        def iter_dfs(target):
            total = nums[:]
            stk = [(1, (0, -1))]
            while stk:
                step, (u, p) = stk.pop()
                if step == 1:
                    stk.append((2, (u, p)))
                    for v in adj[u]:
                        if v == p:
                            continue
                        stk.append((1, (v, u)))
                elif step == 2:
                    for v in adj[u]:
                        if v == p:
                            continue
                        total[u] += total[v]
                    if total[u] == target:
                        total[u] = 0
            return total[0]

        result = 0
        adj = [[] for _ in range(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total = sum(nums)
        for cnt in reversed(range(2, len(nums)+1)):
            if total%cnt == 0 and iter_dfs(total//cnt) == 0:
                return cnt-1
        return 0


