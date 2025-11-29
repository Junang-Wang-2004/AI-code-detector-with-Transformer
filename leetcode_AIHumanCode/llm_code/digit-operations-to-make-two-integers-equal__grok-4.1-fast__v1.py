import heapq
from collections import defaultdict

class Solution:
    def minOperations(self, n, m):
        mx = max(n, m)
        limit = 1
        while limit < mx:
            limit *= 10
        limit *= 2
        
        spf = list(range(limit + 1))
        spf[0] = spf[1] = 0
        for i in range(2, int(limit ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, limit + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        if spf[n] == n:
            return -1
        
        dist = defaultdict(lambda: float('inf'))
        dist[n] = n
        pq = [(n, n)]
        visited = set()
        
        while pq:
            cost, curr = heapq.heappop(pq)
            if curr in visited:
                continue
            visited.add(curr)
            if curr == m:
                return cost
            
            pos = 1
            while pos <= curr:
                prefix = curr // pos
                dig = prefix % 10
                low = 1 if prefix < 10 else 0
                for ch in (-1, 1):
                    ndig = dig + ch
                    if low <= ndig <= 9:
                        neigh = curr + ch * pos
                        if 0 < neigh <= limit and spf[neigh] != neigh:
                            ncost = cost + neigh
                            if ncost < dist[neigh]:
                                dist[neigh] = ncost
                                heapq.heappush(pq, (ncost, neigh))
                pos *= 10
        return -1
