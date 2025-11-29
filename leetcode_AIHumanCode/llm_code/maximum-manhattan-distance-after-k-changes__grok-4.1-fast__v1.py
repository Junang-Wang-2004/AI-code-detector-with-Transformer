class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        moves = {'E': (1, 0), 'W': (-1, 0), 'N': (0, 1), 'S': (0, -1)}
        px, py = 0, 0
        farthest = 0
        for step in range(1, len(s) + 1):
            dx, dy = moves[s[step - 1]]
            px += dx
            py += dy
            dist = abs(px) + abs(py)
            farthest = max(farthest, min(dist + 2 * k, step))
        return farthest
