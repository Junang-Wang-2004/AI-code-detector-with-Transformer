import heapq

class Solution:
    def minTime(self, n, k, m, time, mul):
        full = (1 << n) - 1
        INF = float('inf')
        max_t = [0] * (1 << n)
        for i in range(n):
            ti = 1 << i
            for mask in range(1 << n):
                if mask & ti:
                    max_t[mask] = max(max_t[mask], time[i])
        pc = [bin(i).count('1') for i in range(1 << n)]
        dist = [[[INF] * (1 << n) for _ in range(m)] for _ in range(2)]
        pq = []
        dist[0][0][full] = 0.0
        heapq.heappush(pq, (0.0, 0, 0, full))
        while pq:
            d, r, s, mask = heapq.heappop(pq)
            if d > dist[r][s][mask]:
                continue
            if mask == 0:
                return d
            if r == 0:
                sub = mask
                while sub > 0:
                    if pc[sub] <= k:
                        t = max_t[sub] * mul[s]
                        nr = 1
                        ns = (s + int(t)) % m
                        nm = mask ^ sub
                        nd = d + t
                        if dist[nr][ns][nm] > nd:
                            dist[nr][ns][nm] = nd
                            heapq.heappush(pq, (nd, nr, ns, nm))
                    sub = (sub - 1) & mask
            else:
                for i in range(n):
                    if (mask & (1 << i)) == 0:
                        sub = 1 << i
                        t = max_t[sub] * mul[s]
                        nr = 0
                        ns = (s + int(t)) % m
                        nm = mask ^ sub
                        nd = d + t
                        if dist[nr][ns][nm] > nd:
                            dist[nr][ns][nm] = nd
                            heapq.heappush(pq, (nd, nr, ns, nm))
        return -1.0
