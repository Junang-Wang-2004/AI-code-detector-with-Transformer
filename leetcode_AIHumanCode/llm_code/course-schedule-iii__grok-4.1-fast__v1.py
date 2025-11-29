import heapq
import operator

class Solution:
    def scheduleCourse(self, courses):
        sched = sorted(courses, key=operator.itemgetter(1))
        pq = []
        time = 0
        for dur, dl in sched:
            time += dur
            heapq.heappush(pq, -dur)
            if time > dl:
                time += heapq.heappop(pq)
        return len(pq)
