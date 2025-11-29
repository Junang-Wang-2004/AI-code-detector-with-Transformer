import heapq

class Solution:
    def minInterval(self, intvs, qs):
        intvs.sort(key=lambda x: x[0])
        qlist = sorted(enumerate(qs), key=lambda p: p[1])
        pq = []
        ptr = 0
        ans = [-1] * len(qs)
        for qidx, query in qlist:
            while ptr < len(intvs) and intvs[ptr][0] <= query:
                left, right = intvs[ptr]
                heapq.heappush(pq, (right - left + 1, right))
                ptr += 1
            while pq and pq[0][1] < query:
                heapq.heappop(pq)
            if pq:
                ans[qidx] = pq[0][0]
        return ans
