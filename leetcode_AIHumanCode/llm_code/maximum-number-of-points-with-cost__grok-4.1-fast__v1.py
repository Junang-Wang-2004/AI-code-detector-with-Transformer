class Solution(object):
    def maxPoints(self, points):
        if not points:
            return 0
        rows = len(points)
        cols = len(points[0])
        prev_max = points[0][:]
        for r in range(1, rows):
            lmax = [0] * cols
            lmax[0] = prev_max[0]
            for c in range(1, cols):
                lmax[c] = max(lmax[c - 1] - 1, prev_max[c])
            rmax = [0] * cols
            rmax[cols - 1] = prev_max[cols - 1]
            for c in range(cols - 2, -1, -1):
                rmax[c] = max(rmax[c + 1] - 1, prev_max[c])
            curr_max = [0] * cols
            for c in range(cols):
                curr_max[c] = points[r][c] + max(lmax[c], rmax[c])
            prev_max = curr_max
        return max(prev_max)
