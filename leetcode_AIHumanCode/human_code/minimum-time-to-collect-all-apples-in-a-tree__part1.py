# Time:  O(n)
# Space: O(n)

import collections


class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        """
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        result = [0, 0]
        s = [(1, (-1, 0, result))]
        while s:
            step, params = s.pop()
            if step == 1:
                par, node, ret = params
                ret[:] = [0, int(hasApple[node])]
                for nei in reversed(graph[node]):
                    if nei == par:
                        continue
                    new_ret = [0, 0]
                    s.append((2, (new_ret, ret)))
                    s.append((1, (node, nei, new_ret)))
            else:
                new_ret, ret = params
                ret[0] += new_ret[0]+new_ret[1]
                ret[1] |= bool(new_ret[0]+new_ret[1])
        return 2*result[0]


