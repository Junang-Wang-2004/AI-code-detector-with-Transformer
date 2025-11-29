from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        rows = len(image)
        if rows == 0:
            return image
        cols = len(image[0])
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        queue = deque([(sr, sc)])
        image[sr][sc] = newColor
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            row, col = queue.popleft()
            for dr, dc in deltas:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == old_color:
                    image[nr][nc] = newColor
                    queue.append((nr, nc))
        return image
