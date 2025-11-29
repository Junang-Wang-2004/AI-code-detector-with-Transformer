# Time:  O(m * n)
# Space: O(m * n)

class Solution(object):
    def highestPeak(self, isWater):
        """
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = []
        for r, row in enumerate(isWater):
            for c, cell in enumerate(row):
                row[c] -= 1
                if not cell:
                    continue
                q.append((r, c))
        while q:
            new_q = []
            for r, c in q:
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc 
                    if not (0 <= nr < len(isWater) and
                            0 <= nc < len(isWater[0]) and
                            isWater[nr][nc] == -1):
                        continue
                    isWater[nr][nc] = isWater[r][c]+1
                    q.append((nr, nc))
            q = new_q
        return isWater


