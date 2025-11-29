import heapq


class Solution:
    def findShortestWay(self, maze, ball, hole):
        x0, y0 = ball
        hx, hy = hole
        m, n = len(maze), len(maze[0])
        moves = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]

        def slide(x, y, dx, dy):
            nx, ny, cnt = x, y, 0
            while 0 <= nx + dx < m and 0 <= ny + dy < n and not maze[nx + dx][ny + dy]:
                nx += dx
                ny += dy
                cnt += 1
                if nx == hx and ny == hy:
                    return nx, ny, cnt
            return nx, ny, cnt

        pq = []
        heapq.heappush(pq, (0, '', x0, y0))
        vis = set()
        while pq:
            steps, seq, x, y = heapq.heappop(pq)
            key = (x, y)
            if key in vis:
                continue
            vis.add(key)
            if x == hx and y == hy:
                return seq
            for label, dx, dy in moves:
                nx, ny, extra = slide(x, y, dx, dy)
                heapq.heappush(pq, (steps + extra, seq + label, nx, ny))
        return 'impossible'
