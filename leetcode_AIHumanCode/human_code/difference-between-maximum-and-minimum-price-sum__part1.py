# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp
class Solution(object):
    def maxOutput(self, n, edges, price):
        """
        """
        def iter_dfs():
            result = 0
            stk = [(1, (0, -1, [price[0], 0]))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p, ret = args
                    stk.append((2, (u, p, ret, 0)))
                elif step == 2:
                    u, p, ret, i = args
                    if i == len(adj[u]):
                        continue
                    stk.append((2, (u, p, ret, i+1)))
                    v = adj[u][i]
                    if v == p:
                        continue
                    new_ret = [price[v], 0]  # [max_path_sum, max_path_sum_without_last_node]
                    stk.append((3, (u, new_ret, ret)))
                    stk.append((1, (v, u, new_ret)))
                elif step == 3:
                    u, new_ret, ret = args
                    result = max(result, ret[0]+new_ret[1], ret[1]+new_ret[0])
                    ret[0] = max(ret[0], new_ret[0]+price[u])
                    ret[1] = max(ret[1], new_ret[1]+price[u])
            return result
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return iter_dfs()


