class Solution:
    def countSubIslands(self, g1, g2):
        if not g2 or not g2[0]:
            return 0
        rows, cols = len(g2), len(g2[0])
        deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def erase(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or g2[r][c] != 1:
                return
            g2[r][c] = 0
            for dr, dc in deltas:
                erase(r + dr, c + dc)
        
        for x in range(rows):
            for y in range(cols):
                if g2[x][y] == 1 and g1[x][y] == 0:
                    erase(x, y)
        
        total = 0
        for x in range(rows):
            for y in range(cols):
                if g2[x][y] == 1:
                    erase(x, y)
                    total += 1
        return total
