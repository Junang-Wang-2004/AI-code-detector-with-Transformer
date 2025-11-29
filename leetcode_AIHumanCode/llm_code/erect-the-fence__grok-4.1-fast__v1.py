class Solution:
    def outerTrees(self, trees):
        pts = sorted(set(map(tuple, trees)))
        if len(pts) <= 1:
            return [list(p) for p in pts]

        def direction(a, b, c):
            return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

        bottom = []
        for p in pts:
            while len(bottom) >= 2 and direction(bottom[-2], bottom[-1], p) < 0:
                bottom.pop()
            bottom.append(p)

        top = []
        rpts = pts[::-1]
        for p in rpts:
            while len(top) >= 2 and direction(top[-2], top[-1], p) < 0:
                top.pop()
            top.append(p)

        candidates = bottom[:-1] + top[:-1]
        hull = set(map(tuple, candidates))
        return [list(pt) for pt in hull]
