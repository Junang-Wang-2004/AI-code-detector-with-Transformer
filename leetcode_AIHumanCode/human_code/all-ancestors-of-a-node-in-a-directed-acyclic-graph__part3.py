# Time:  O(|V| * |E| * log(|V| * |E|))
# Space: O(|V| + |E|)
# topological sort
class Solution3(object):
    def getAncestors(self, n, edges):
        """
        """
        result = [set() for _ in range(n)]
        in_degree = [0]*n
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
            result[v].add(u)
        q = [u for u, d in enumerate(in_degree) if not d]
        while q:
            new_q = []
            for u in q:
                for v in adj[u]:
                    result[v].update(result[u])
                    in_degree[v] -= 1
                    if not in_degree[v]:
                        new_q.append(v)
            q = new_q
        return [sorted(s) for s in result]
