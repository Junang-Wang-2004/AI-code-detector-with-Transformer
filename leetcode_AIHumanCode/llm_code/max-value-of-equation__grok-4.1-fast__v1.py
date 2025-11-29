import collections

class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        best = float('-inf')
        window = collections.deque()
        n = len(points)
        for i in range(n):
            cx = points[i][0]
            cy = points[i][1]
            while window and points[window[0]][0] < cx - k:
                window.popleft()
            if window:
                j = window[0]
                best = max(best, points[j][1] - points[j][0] + cy + cx)
            cval = cy - cx
            while window and points[window[-1]][1] - points[window[-1]][0] <= cval:
                window.pop()
            window.append(i)
        return best
