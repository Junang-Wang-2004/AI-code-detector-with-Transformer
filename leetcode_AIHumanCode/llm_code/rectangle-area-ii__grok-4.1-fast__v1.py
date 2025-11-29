class Solution(object):
    def rectangleArea(self, rectangles):
        MOD = 10**9 + 7
        events = []
        coords = set()
        for x0, y0, x1, y1 in rectangles:
            events.append((y0, 1, x0, x1))
            events.append((y1, -1, x0, x1))
            coords.add(x0)
            coords.add(x1)
        Xcoords = sorted(coords)
        n = len(Xcoords)
        if n < 2:
            return 0
        mapping = {Xcoords[i]: i for i in range(n)}
        segcount = n - 1
        treesize = 4 * n
        coverage = [0] * treesize
        measure = [0] * treesize
        totallen = [0] * treesize
        intervals = [Xcoords[i+1] - Xcoords[i] for i in range(segcount)]

        def construct(v, leftb, rightb):
            if leftb == rightb:
                totallen[v] = intervals[leftb]
                return
            m = (leftb + rightb) // 2
            construct(2 * v, leftb, m)
            construct(2 * v + 1, m + 1, rightb)
            totallen[v] = totallen[2 * v] + totallen[2 * v + 1]

        construct(1, 0, segcount - 1)

        def modify(v, leftb, rightb, starti, endi, delta):
            if starti > rightb or endi < leftb:
                return
            if starti <= leftb and rightb <= endi:
                coverage[v] += delta
            else:
                m = (leftb + rightb) // 2
                modify(2 * v, leftb, m, starti, endi, delta)
                modify(2 * v + 1, m + 1, rightb, starti, endi, delta)
            if coverage[v] > 0:
                measure[v] = totallen[v]
            else:
                if leftb == rightb:
                    measure[v] = 0
                else:
                    measure[v] = measure[2 * v] + measure[2 * v + 1]

        events.sort()
        total = 0
        lasty = events[0][0]
        activewidth = 0
        for yval, action, xl, xr in events:
            total = (total + activewidth * (yval - lasty)) % MOD
            segstart = mapping[xl]
            segend = mapping[xr] - 1
            if segstart <= segend:
                modify(1, 0, segcount - 1, segstart, segend, action)
            activewidth = measure[1]
            lasty = yval
        return total
