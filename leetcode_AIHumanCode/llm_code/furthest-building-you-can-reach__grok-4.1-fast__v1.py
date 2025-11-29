import heapq


class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        pq = []
        remain_bricks = bricks
        remain_ladders = ladders
        n = len(heights)
        for pos in range(n - 1):
            climb = heights[pos + 1] - heights[pos]
            if climb > 0:
                heapq.heappush(pq, -climb)
                remain_bricks -= climb
                while remain_bricks < 0 and remain_ladders > 0:
                    remain_bricks -= heapq.heappop(pq)
                    remain_ladders -= 1
                if remain_bricks < 0:
                    return pos
        return n - 1
