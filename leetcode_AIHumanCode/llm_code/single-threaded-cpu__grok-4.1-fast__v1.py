import heapq

class Solution:
    def getOrder(self, tasks):
        n = len(tasks)
        events = sorted((tasks[j][0], tasks[j][1], j) for j in range(n))
        ready = []
        output = []
        now = events[0][0]
        pos = 0
        while pos < n or ready:
            while pos < n and events[pos][0] <= now:
                _, duration, task_id = events[pos]
                heapq.heappush(ready, (duration, task_id))
                pos += 1
            if ready:
                duration, task_id = heapq.heappop(ready)
                now += duration
                output.append(task_id)
            else:
                now = events[pos][0]
        return output
