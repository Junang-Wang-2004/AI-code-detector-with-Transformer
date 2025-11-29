class Solution(object):
    def numDistinctIslands2(self, grid):
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * cols for _ in range(rows)]

        def find_island(sr, sc):
            from collections import deque
            queue = deque([(sr, sc)])
            visited[sr][sc] = True
            coords = []
            while queue:
                r, c = queue.popleft()
                coords.append((r, c))
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            return coords

        def shape_key(pts):
            tfms = [
                lambda r, c: (r, c),
                lambda r, c: (r, -c),
                lambda r, c: (-r, c),
                lambda r, c: (-r, -c),
                lambda r, c: (c, r),
                lambda r, c: (c, -r),
                lambda r, c: (-c, r),
                lambda r, c: (-c, -r)
            ]
            options = []
            for tf in tfms:
                t_coords = sorted(tf(r, c) for r, c in pts)
                base_r, base_c = t_coords[0]
                shifted = tuple((rr - base_r, cc - base_c) for rr, cc in t_coords)
                options.append(shifted)
            return min(options)

        shapes = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    island_coords = find_island(r, c)
                    shapes.add(shape_key(island_coords))
        return len(shapes)
