MOD = 10**9 + 7

class Solution:
    def assignEdgeWeights(self, edges, queries):
        n = len(edges)
        graph = [[] for _ in range(n + 1)]
        for x, y in edges:
            x -= 1
            y -= 1
            graph[x].append(y)
            graph[y].append(x)
        
        LOG = 18
        parent = [[-1] * (n + 1) for _ in range(LOG)]
        depths = [0] * (n + 1)
        
        def preorder(node, prev, dep):
            parent[0][node] = prev
            depths[node] = dep
            for neigh in graph[node]:
                if neigh != prev:
                    preorder(neigh, node, dep + 1)
        
        preorder(0, -1, 0)
        
        for lvl in range(1, LOG):
            for idx in range(n + 1):
                if parent[lvl - 1][idx] != -1:
                    parent[lvl][idx] = parent[lvl - 1][parent[lvl - 1][idx]]
        
        def lowest_common_ancestor(a, b):
            if depths[a] > depths[b]:
                a, b = b, a
            delta = depths[b] - depths[a]
            k = 0
            while delta > 0:
                if delta & 1:
                    b = parent[k][b]
                delta >>= 1
                k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if parent[k][a] != parent[k][b]:
                    a = parent[k][a]
                    b = parent[k][b]
            return parent[0][a]
        
        answers = []
        for pair in queries:
            p, q = pair[0] - 1, pair[1] - 1
            if p == q:
                answers.append(0)
                continue
            lca_node = lowest_common_ancestor(p, q)
            path_len = depths[p] + depths[q] - 2 * depths[lca_node]
            answers.append(pow(2, path_len - 1, MOD))
        return answers
