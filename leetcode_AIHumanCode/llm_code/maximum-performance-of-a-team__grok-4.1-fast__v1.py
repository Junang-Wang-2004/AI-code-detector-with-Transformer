import heapq

class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        MOD = 10**9 + 7
        perf = 0
        total_speed = 0
        pq = []
        order = sorted(range(n), key=lambda i: -efficiency[i])
        for idx in order:
            spd = speed[idx]
            eff = efficiency[idx]
            total_speed += spd
            heapq.heappush(pq, spd)
            if len(pq) > k:
                total_speed -= heapq.heappop(pq)
            perf = max(perf, total_speed * eff)
        return perf % MOD
