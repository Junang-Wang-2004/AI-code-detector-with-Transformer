from typing import List
import sys

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        
        def compute_topo():
            indeg = [0] * n
            for u in range(n):
                for v, _ in graph[u]:
                    indeg[v] += 1
            topo = []
            q = [i for i in range(n) if indeg[i] == 0]
            while q:
                nxt = []
                for u in q:
                    topo.append(u)
                    for v, _ in graph[u]:
                        indeg[v] -= 1
                        if indeg[v] == 0:
                            nxt.append(v)
                q = nxt
            return topo
        
        topo_order = compute_topo()
        
        min_val = sys.maxsize
        max_val = 0
        for u in range(n):
            for _, w in graph[u]:
                min_val = min(min_val, w)
                max_val = max(max_val, w)
        
        INF = float('inf')
        
        def feasible(thresh: int) -> bool:
            min_cost = [INF] * n
            min_cost[0] = 0
            for node in topo_order:
                if min_cost[node] == INF:
                    continue
                for neigh, wt in graph[node]:
                    if wt >= thresh and online[neigh]:
                        min_cost[neigh] = min(min_cost[neigh], min_cost[node] + wt)
            return min_cost[n - 1] <= k
        
        low = min_val
        high = max_val
        while low <= high:
            mid = low + (high - low) // 2
            if feasible(mid):
                low = mid + 1
            else:
                high = mid - 1
        candidate = high
        return candidate if candidate >= min_val else -1
