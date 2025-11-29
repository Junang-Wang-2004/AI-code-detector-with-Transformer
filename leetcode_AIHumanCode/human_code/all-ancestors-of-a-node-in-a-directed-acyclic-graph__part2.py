# Time:  O(|V| * |E| * log(|V| * |E|))
# Space: O(|V| + |E|)
# bfs
class Solution2(object):
    def getAncestors(self, n, edges):
        """
        """
        def bfs(adj, i, result):
            lookup = [False]*len(adj)
            q = [i]
            lookup[i] = True
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.append(v)
                        result[i].append(v)
                q = new_q
            result[i].sort()

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[v].append(u)
        result = [[] for _ in range(n)]
        for u in range(n):
            bfs(adj, u, result) 
        return result


