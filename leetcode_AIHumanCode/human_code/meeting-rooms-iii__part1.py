# Time:  O(mlogm + n + mlogn)
# Space: O(n)

import heapq


# one heap solution
class Solution(object):
    def mostBooked(self, n, meetings):
        """
        """
        meetings.sort()
        min_heap = [(meetings[0][0], i) for i in range(n)]
        result = [0]*n
        for s, e in meetings:
            while min_heap and min_heap[0][0] < s:
                _, i = heapq.heappop(min_heap)
                heapq.heappush(min_heap, (s, i))
            e2, i = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (e2+(e-s), i))
            result[i] += 1
        return max(range(n), key=lambda x:result[x])


