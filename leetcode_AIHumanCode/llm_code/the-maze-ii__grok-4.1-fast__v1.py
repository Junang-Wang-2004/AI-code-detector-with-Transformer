import heapq

class Solution:
    def shortestDistance(self, maze, start, destination):
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dest_r, dest_c = destination
        dists = [[float('inf')] * cols for _ in range(rows)]
        sr, sc = start
        dists[sr][sc] = 0
        pq = [(0, sr, sc)]
        while pq:
            d, r, c = heapq.heappop(pq)
            if r == dest_r and c == dest_c:
                return d
            if d > dists[r][c]:
                continue
            for dr, dc in directions:
                cr, cc = r, c
                steps = 0
                while True:
                    nr = cr + dr
                    nc = cc + dc
                    if not (0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0):
                        break
                    cr, cc = nr, nc
                    steps += 1
                nd = d + steps
                if nd < dists[cr][cc]:
                    dists[cr][cc] = nd
                    heapq.heappush(pq, (nd, cr, cc))
        return -1
