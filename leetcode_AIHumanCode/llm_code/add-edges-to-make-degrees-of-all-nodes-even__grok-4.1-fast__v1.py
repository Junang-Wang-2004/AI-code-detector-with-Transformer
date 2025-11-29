class Solution(object):
    def isPossible(self, n, edges):
        graph = [set() for _ in range(n)]
        for uu, vv in edges:
            u = uu - 1
            v = vv - 1
            graph[u].add(v)
            graph[v].add(u)
        odd_vertices = [i for i in range(n) if len(graph[i]) % 2 == 1]
        num_odds = len(odd_vertices)
        if num_odds == 0:
            return True
        if num_odds not in (2, 4):
            return False
        if num_odds == 2:
            p, q = odd_vertices
            np = graph[p]
            nq = graph[q]
            if q not in np:
                return True
            covered = np.union(nq)
            return len(covered) < n
        # num_odds == 4
        w, x, y, z = odd_vertices
        checks = [
            (z not in graph[w] and y not in graph[x]),
            (y not in graph[w] and z not in graph[x]),
            (x not in graph[w] and y not in graph[z])
        ]
        return any(checks)
