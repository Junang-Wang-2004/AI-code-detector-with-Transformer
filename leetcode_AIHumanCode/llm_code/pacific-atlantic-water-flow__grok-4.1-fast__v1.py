from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        pac_vis = [[False] * cols for _ in range(rows)]
        atl_vis = [[False] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def flood(visited, borders):
            queue = deque(borders)
            for r, c in borders:
                visited[r][c] = True
            while queue:
                r, c = queue.popleft()
                curr_h = heights[r][c]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and heights[nr][nc] >= curr_h:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        pac_borders = [(i, 0) for i in range(rows)] + [(0, j) for j in range(1, cols)]
        atl_borders = [(i, cols - 1) for i in range(rows)] + [(rows - 1, j) for j in range(cols - 1)]
        flood(pac_vis, pac_borders)
        flood(atl_vis, atl_borders)

        ans = []
        for i in range(rows):
            for j in range(cols):
                if pac_vis[i][j] and atl_vis[i][j]:
                    ans.append([i, j])
        return ans
