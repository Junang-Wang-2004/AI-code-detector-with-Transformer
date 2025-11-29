# Time:  O(n)
# Space: O(n)
class Solution2_Recu(object):
    def minTime(self, n, edges, hasApple):
        """
        """
        def dfs(graph, par, node, has_subtree):
            result, extra = 0, int(hasApple[node])
            for nei in graph[node]:
                if nei == par:
                    continue
                count = dfs(graph, node, nei, hasApple)
                result += count
                extra |= bool(count)
            return result+extra
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return 2*max(dfs(graph, -1, 0, hasApple)-1, 0)
