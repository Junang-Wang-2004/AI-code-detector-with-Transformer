# Time:  O(n)
# Space: O(n)
class Solution_Recu(object):
    def minTime(self, n, edges, hasApple):
        """
        """
        def dfs(graph, par, node, hasApple):
            result, extra = 0, int(hasApple[node])
            for nei in graph[node]:
                if nei == par:
                    continue
                count, found = dfs(graph, node, nei, hasApple)
                result += count+found
                extra |= bool(count+found)
            return result, extra
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return 2*dfs(graph, -1, 0, hasApple)[0]


