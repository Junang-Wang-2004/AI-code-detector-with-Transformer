# Time:  O(n)
# Space: O(h)

# iterative dfs
class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
        def iter_dfs():
            result = 0
            stk = [(1, (0, -1, 0, [1]))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p, d, ret = args
                    stk.append((3, (d, ret)))
                    for v in adj[u]:
                        if v == p:
                            continue
                        new_ret = [1]
                        stk.append((2, (new_ret, ret)))
                        stk.append((1, (v, u, d+1, new_ret)))
                elif step == 2:
                    new_ret, ret = args
                    ret[0] += new_ret[0]
                elif step == 3:
                    d, ret = args
                    if d:
                        result += ceil_divide(ret[0], seats)
            return result
    
        adj = [[] for _ in range(len(roads)+1)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        return iter_dfs()


