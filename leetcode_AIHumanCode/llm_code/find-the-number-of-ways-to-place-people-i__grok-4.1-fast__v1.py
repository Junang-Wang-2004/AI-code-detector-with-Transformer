class Solution:
    def numberOfPairs(self, points):
        n = len(points)
        order = sorted(range(n), key=lambda idx: (points[idx][0], -points[idx][1]))
        ans = 0
        for i in range(n):
            ymax = float('-inf')
            yi = points[order[i]][1]
            for j in range(i + 1, n):
                yj = points[order[j]][1]
                if yi < yj:
                    continue
                if yj > ymax:
                    ymax = yj
                    ans += 1
        return ans
