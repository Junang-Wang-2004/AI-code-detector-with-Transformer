# Time:  O(n)
# Space: O(n)
import collections


class Solution2(object):
    def minReorder(self, n, connections):
        """
        """
        def dfs(n, lookup, graph, parent, u):
            result = (parent*n+u in lookup)
            for v in graph[u]:
                if v == parent:
                    continue
                result += dfs(n, lookup, graph, u, v)  
            return result

        lookup, graph = set(), collections.defaultdict(list)
        for u, v in connections:
            lookup.add(u*n+v)
            graph[v].append(u)
            graph[u].append(v) 
        return dfs(n, lookup, graph, -1, 0)
