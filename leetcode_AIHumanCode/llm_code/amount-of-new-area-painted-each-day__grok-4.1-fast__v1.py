import heapq

class Solution:
    def amountPainted(self, paint):
        n = len(paint)
        events = []
        for i in range(n):
            s, e = paint[i]
            events.append((s, 0, i, e))
            events.append((e, 1, i, e))
        events.sort()
        ans = [0] * n
        active = []
        prev_pos = None
        k = 0
        m = len(events)
        while k < m:
            curr_pos = events[k][0]
            if prev_pos is not None:
                while active and active[0][1] < curr_pos:
                    heapq.heappop(active)
                if active:
                    ans[active[0][0]] += curr_pos - prev_pos
            prev_pos = curr_pos
            while k < m and events[k][0] == curr_pos:
                typ = events[k][1]
                idx = events[k][2]
                if typ == 0:
                    heapq.heappush(active, (idx, events[k][3]))
                k += 1
        return ans
