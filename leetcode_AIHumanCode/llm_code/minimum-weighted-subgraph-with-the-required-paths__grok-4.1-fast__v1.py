import heapq

class Solution:
    def minimumWeight(self, n, edges, start1, start2, target):
        fwd = [[] for _ in range(n)]
        rev = [[] for _ in range(n)]
        for u, v, w in edges:
            fwd[u].append((v, w))
            rev[v].append((u, w))
        
        def shortest_paths(g, src):
            dist = [float('inf')] * n
            dist[src] = 0
            pq = [(0, src)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for nei, wt in g[u]:
                    cand = d + wt
                    if cand < dist[nei]:
                        dist[nei] = cand
                        heapq.heappush(pq, (cand, nei))
            return dist
        
        d1 = shortest_paths(fwd, start1)
        d2 = shortest_paths(fwd, start2)
        dt = shortest_paths(rev, target)
        
        ans = float('inf')
        for i in range(n):
            tot = d1[i] + d2[i] + dt[i]
            if tot < ans:
                ans = tot
        return ans if ans < float('inf') else -1
