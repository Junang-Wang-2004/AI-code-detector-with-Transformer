class Solution:
    def numberOfPairs(self, points):
        pts = sorted(points, key=lambda p: (p[0], -p[1]))
        ys = [pt[1] for pt in pts]
        n = len(ys)
        ans = 0
        for i in range(n):
            cur_max = float('-inf')
            for j in range(i + 1, n):
                if ys[i] < ys[j]:
                    continue
                if ys[j] > cur_max:
                    cur_max = ys[j]
                    ans += 1
        return ans
