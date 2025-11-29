class Solution:
    def distinctPoints(self, s, k):
        def delta(ch):
            if ch == 'U':
                return 0, 1
            if ch == 'D':
                return 0, -1
            if ch == 'L':
                return -1, 0
            return 1, 0

        diffs = []
        n = len(s)
        for idx in range(k, n):
            ndx, ndy = delta(s[idx])
            odx, ody = delta(s[idx - k])
            diffs.append((ndx - odx, ndy - ody))

        points = set()
        px, py = 0, 0
        points.add((px, py))
        for dx, dy in diffs:
            px += dx
            py += dy
            points.add((px, py))
        return len(points)
