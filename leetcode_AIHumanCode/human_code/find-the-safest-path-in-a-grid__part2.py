# Time:  O(n^2 * logn)
# Space: O(n^2)
import heapq


# bfs, dijkstra's algorithm
class Solution2(object):
    def maximumSafenessFactor(self, grid):
        """
        """
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def bfs():
            dist = [[0 if grid[r][c] == 1 else -1 for c in range(len(grid[0]))] for r in range(len(grid))]
            q = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c]]
            d = 0
            while q:
                new_q = []
                for r, c in q:
                    for dr, dc in DIRECTIONS:
                        nr, nc = r+dr, c+dc
                        if not (0 <= nr < len(dist) and 0 <= nc < len(dist[0]) and dist[nr][nc] == -1):
                            continue
                        dist[nr][nc] = d+1
                        new_q.append((nr, nc))
                q = new_q
                d += 1
            return dist

        def dijkstra(start, target):
            max_heap = [(-dist[start[0]][start[1]], start)]
            dist[start[0]][start[1]] = -1
            while max_heap:
                curr, u = heapq.heappop(max_heap)
                curr = -curr
                if u == target:
                    return curr
                for dr, dc in DIRECTIONS:
                    nr, nc = u[0]+dr, u[1]+dc
                    if not (0 <= nr < len(dist) and 0 <= nc < len(dist[0]) and dist[nr][nc] != -1):
                        continue
                    heapq.heappush(max_heap, (-min(curr, dist[nr][nc]), (nr, nc)))
                    dist[nr][nc] = -1
            return -1

        dist = bfs()
        return dijkstra(dist, (0, 0), (len(grid)-1, len(grid[0])-1)) 


