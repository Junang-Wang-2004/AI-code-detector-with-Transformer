from typing import List

class DSU:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        qcnt = len(queries)
        qlists = [[] for _ in range(n)]
        for qi, nodes in enumerate(queries):
            for node in nodes:
                qlists[node].append(qi)
        dsu = DSU(n)
        rep_dist = [0] * n
        path_dist = [0] * n
        seen = [False] * n
        res = [0] * qcnt

        def traverse(node: int) -> None:
            for qi in qlists[node]:
                res[qi] += path_dist[node]
                for other in queries[qi]:
                    if seen[other]:
                        res[qi] -= path_dist[rep_dist[dsu.find(other)]]
            seen[node] = True
            for nxt, wt in graph[node]:
                if seen[nxt]:
                    continue
                path_dist[nxt] = path_dist[node] + wt
                traverse(nxt)
                dsu.unite(nxt, node)
                rep_dist[dsu.find(node)] = node

        traverse(0)
        return res
