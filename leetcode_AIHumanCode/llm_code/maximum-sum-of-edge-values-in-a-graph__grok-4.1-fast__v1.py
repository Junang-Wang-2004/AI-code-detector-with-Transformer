from typing import List
import heapq
from collections import deque

class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        non_triv = []
        for i in range(n):
            if visited[i]:
                continue
            q = deque([i])
            visited[i] = True
            comp = [i]
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
                        comp.append(v)
            sz = len(comp)
            if sz >= 2:
                is_cyc = all(len(adj[x]) == 2 for x in comp)
                non_triv.append((sz, is_cyc))
        non_triv.sort(reverse=True)
        m = len(non_triv)
        starter_to_cid = {}
        for i in range(m):
            starter = n - 2 * i
            if starter >= 1:
                starter_to_cid[starter] = i
        comps = [[non_triv[j][0], non_triv[j][1], 0, 0, 0] for j in range(m)]
        h = []
        res = 0
        for k in range(n, 0, -1):
            if k in starter_to_cid:
                cid = starter_to_cid[k]
                c = comps[cid]
                c[2] = k
                c[3] = k
                c[4] = 1
                if c[0] > 1:
                    heapq.heappush(h, (-k, cid))
            else:
                while h:
                    neg_a, cid = heapq.heappop(h)
                    a = -neg_a
                    c = comps[cid]
                    if c[4] >= c[0] or c[2] != a:
                        continue
                    res += a * k
                    c[2] = c[3]
                    c[3] = k
                    c[4] += 1
                    if c[4] == c[0] and c[1]:
                        res += c[2] * c[3]
                    if c[4] < c[0]:
                        heapq.heappush(h, (-c[2], cid))
                    break
        return res
