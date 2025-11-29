import collections
import heapq

class Solution(object):
    def rearrangeString(self, s, k):
        if k <= 1:
            return s
        n = len(s)
        count = collections.Counter(s)
        pq = []
        for char, num in count.items():
            heapq.heappush(pq, [-num, char])
        ans = []
        while len(ans) < n:
            buffer = []
            slots = min(k, n - len(ans))
            placed = 0
            while placed < slots and pq:
                cnt_item = heapq.heappop(pq)
                ans.append(cnt_item[1])
                cnt_item[0] += 1
                placed += 1
                if cnt_item[0] < 0:
                    buffer.append(cnt_item)
            if placed < slots:
                return ""
            for item in buffer:
                heapq.heappush(pq, item)
        return "".join(ans)
