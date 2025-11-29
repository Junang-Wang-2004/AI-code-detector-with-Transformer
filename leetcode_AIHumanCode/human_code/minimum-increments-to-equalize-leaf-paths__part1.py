# Time:  O(n)
# Space: O(n)

# iterative dfs
class Solution(object):
    def minIncrease(self, n, edges, cost):
        """
        """
        def iter_dfs():
            result = n-1
            mx = [0]*len(adj)
            stk = [(1, (0, -1))]
            while stk:
                step, (u, p) = stk.pop()
                if step == 1:
                    stk.append((2, (u, p)))
                    for v in reversed(adj[u]):
                        if v != p:
                            stk.append((1, (v, u)))
                elif step == 2:
                    cnt = 0
                    for v in adj[u]:
                        if v == p or mx[v] < mx[u]:
                            continue
                        if mx[v] > mx[u]:
                            mx[u] = mx[v]
                            cnt = 0
                        cnt += 1
                    result -= cnt
                    mx[u] += cost[u]
            return result

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return iter_dfs()


