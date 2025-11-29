# Time:  O(m * n * log(m * n))
# Space: O(m * n)
import heapq


# Dijkstra algorithm solution
class Solution2(object):
    def maximumMinimumPath(self, A):
        """
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_heap = [(-A[0][0], 0, 0)]
        lookup = set([(0, 0)])
        while max_heap:
            i, r, c = heapq.heappop(max_heap)
            if r == len(A)-1 and c == len(A[0])-1:
                return -i
            for d in directions:
                nr, nc = r+d[0], c+d[1]
                if 0 <= nr < len(A) and \
                   0 <= nc < len(A[0]) and \
                   (nr, nc) not in lookup:
                    heapq.heappush(max_heap, (-min(-i, A[nr][nc]), nr, nc))
                    lookup.add((nr, nc))    
        return -1
