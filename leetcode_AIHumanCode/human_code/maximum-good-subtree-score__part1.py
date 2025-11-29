# Time:  O(n * (2^10)^2)
# Space: O(2^10)

import collections


# bitmasks, iterative dfs, tree dp
class Solution(object):
    def goodSubtreeSum(self, vals, par):
        """
        """
        MOD = 10**9+7
        def get_mask(x):
            mask = 0
            while x:
                x, d = divmod(x, 10)
                if mask&(1<<d):
                    return -1
                mask |= 1<<d
            return mask

        def iter_dfs():
            result = 0
            ret = collections.defaultdict(int)
            stk = [(1, (0, ret))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, ret = args
                    ret[0] = 0
                    mask = get_mask(vals[u])
                    if mask != -1:
                        ret[mask] = vals[u]
                    stk.append((4, (u, ret)))
                    stk.append((2, (u, 0, ret)))
                elif step == 2:
                    u, i, ret = args
                    if i == len(adj[u]):
                        continue
                    v = adj[u][i]
                    stk.append((2, (u, i+1, ret)))
                    new_ret = collections.defaultdict(int)
                    stk.append((3, (new_ret, ret)))
                    stk.append((1, (v, new_ret)))
                elif step == 3:
                    new_ret, ret = args
                    for m1, v1 in list(ret.items()):
                        for m2, v2 in new_ret.items():
                            if m1&m2:
                                continue
                            ret[m1|m2] =  max(ret[m1|m2], v1+v2)
                elif step == 4:
                    u, ret = args
                    result = (result+max(ret.values()))%MOD
            return result

        adj = [[] for _ in range(len(vals))]
        for u in range(1, len(par)):
            adj[par[u]].append(u)
        return iter_dfs()


