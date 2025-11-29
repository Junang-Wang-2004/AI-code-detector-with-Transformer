# Time:  O(n)
# Space: O(n)

import collections


class Solution(object):
    def minReorder(self, n, connections):
        """
        """
        lookup, graph = set(), collections.defaultdict(list)
        for u, v in connections:
            lookup.add(u*n+v)
            graph[v].append(u)
            graph[u].append(v) 
        result = 0
        stk = [(-1, 0)]
        while stk:
            parent, u = stk.pop()
            result += (parent*n+u in lookup)
            for v in reversed(graph[u]):
                if v == parent:
                    continue
                stk.append((u, v))
        return result


