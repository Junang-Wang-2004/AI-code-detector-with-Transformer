import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            p = succProb[i]
            graph[u].append((v, p))
            graph[v].append((u, p))
        best = [0.0] * n
        best[start] = 1.0
        pq = [(-1.0, start)]
        seen = [False] * n
        while pq:
            neg_prob, node = heapq.heappop(pq)
            if seen[node]:
                continue
            seen[node] = True
            curr_prob = -neg_prob
            for neigh, edge_prob in graph[node]:
                candidate = curr_prob * edge_prob
                if candidate > best[neigh]:
                    best[neigh] = candidate
                    heapq.heappush(pq, (-candidate, neigh))
        return best[end]
