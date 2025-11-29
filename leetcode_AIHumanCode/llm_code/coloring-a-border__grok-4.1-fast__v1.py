class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        rows = len(grid)
        if rows == 0:
            return grid
        cols = len(grid[0])
        val = grid[r0][c0]
        seen = set([(r0, c0)])
        pile = [(r0, c0)]
        edges = []
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        while pile:
            r, c = pile.pop()
            adj = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == val:
                    adj += 1
                nt = (nr, nc)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == val and nt not in seen:
                    seen.add(nt)
                    pile.append(nt)
            if adj < 4:
                edges.append((r, c))
        for r, c in edges:
            grid[r][c] = color
        return grid
