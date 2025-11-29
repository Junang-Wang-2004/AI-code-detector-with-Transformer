import collections

class Solution(object):
    def shortestBridge(self, A):
        n = len(A)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        q = collections.deque()
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    temp_q = collections.deque([(i, j)])
                    visited.add((i, j))
                    while temp_q:
                        x, y = temp_q.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and A[nx][ny] == 1:
                                visited.add((nx, ny))
                                temp_q.append((nx, ny))
                    q = collections.deque((r, c, 0) for r, c in visited)
                    break
            else:
                continue
            break
        while q:
            x, y, dist = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                if A[nx][ny] == 1:
                    return dist
                visited.add((nx, ny))
                q.append((nx, ny, dist + 1))
