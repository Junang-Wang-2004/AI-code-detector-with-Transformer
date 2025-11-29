import collections
import heapq

class Solution:
    def avoidFlood(self, rains):
        flood_days = collections.defaultdict(list)
        for d, lk in enumerate(rains):
            if lk:
                flood_days[lk].append(d)
        curr_idx = {lk: 0 for lk in flood_days}
        pq = []
        res = []
        for d in range(len(rains)):
            lk = rains[d]
            if lk != 0:
                res.append(-1)
                idx = curr_idx[lk]
                if idx + 1 < len(flood_days[lk]):
                    nxt_d = flood_days[lk][idx + 1]
                    heapq.heappush(pq, (nxt_d, lk))
                    curr_idx[lk] += 1
            else:
                if pq:
                    dl, tgt = heapq.heappop(pq)
                    if dl <= d:
                        return []
                    res.append(tgt)
                else:
                    res.append(1)
        return res if not pq else []
