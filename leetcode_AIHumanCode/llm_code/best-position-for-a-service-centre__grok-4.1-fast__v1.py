class Solution:
    def getMinDistSum(self, pts):
        n = len(pts)
        if n == 0:
            return 0.0
        x0 = sum(x for x, _ in pts) / n
        y0 = sum(y for _, y in pts) / n
        loc = [x0, y0]
        TOL = 1e-6
        while True:
            sx, sy, w = 0.0, 0.0, 0.0
            for px, py in pts:
                dx = loc[0] - px
                dy = loc[1] - py
                dd = (dx ** 2 + dy ** 2) ** 0.5
                if dd > TOL:
                    sx += px / dd
                    sy += py / dd
                    w += 1 / dd
            if w == 0:
                break
            nloc = [sx / w, sy / w]
            dx = abs(nloc[0] - loc[0])
            dy = abs(nloc[1] - loc[1])
            loc = nloc
            if dx * n < TOL and dy * n < TOL:
                break
        res = 0.0
        for px, py in pts:
            dx = loc[0] - px
            dy = loc[1] - py
            res += (dx ** 2 + dy ** 2) ** 0.5
        return res
