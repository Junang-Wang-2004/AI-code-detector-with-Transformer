# Time:  O(nlogm)
# Space: O(1)

import heapq


# greedy
class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        """
        total = sum(batteries)
        for i in range(len(batteries)):
            batteries[i] = -batteries[i]  # max_heap
        heapq.heapify(batteries)
        while -batteries[0] > total//n:
            n -= 1
            total -= -heapq.heappop(batteries)
        return total//n


