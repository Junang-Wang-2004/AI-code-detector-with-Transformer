import heapq

class Solution:
    def predictPartyVictory(self, senate):
        n = len(senate)
        r_pq = []
        d_pq = []
        for i in range(n):
            if senate[i] == 'R':
                heapq.heappush(r_pq, i)
            else:
                heapq.heappush(d_pq, i)
        while r_pq and d_pq:
            r_pos = heapq.heappop(r_pq)
            d_pos = heapq.heappop(d_pq)
            if r_pos < d_pos:
                heapq.heappush(r_pq, r_pos + n)
            else:
                heapq.heappush(d_pq, d_pos + n)
        return "Radiant" if r_pq else "Dire"
