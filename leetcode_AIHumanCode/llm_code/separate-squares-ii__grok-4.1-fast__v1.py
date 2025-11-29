class Solution:
    def separateSquares(self, squares):
        pts = set()
        evts = []
        for px, py, pl in squares:
            evts.append((py, 1, px, px + pl))
            evts.append((py + pl, -1, px, px + pl))
            pts.add(px)
            pts.add(px + pl)
        evts.sort(key=lambda t: (t[0], -t[1]))
        xlist = sorted(pts)
        if not xlist:
            return 0.0
        rankx = {p: i for i, p in enumerate(xlist)}
        tree = CoverTree(xlist)

        segments = []
        lasty = evts[0][0]
        for cy, act, lx, rx in evts:
            if cy > lasty:
                segments.append((lasty, cy, tree.query()))
                lasty = cy
            lefti = rankx[lx]
            righti = rankx[rx]
            tree.update(lefti, righti, act)

        totarea = sum((hy - ly) * w for ly, hy, w in segments)
        target = totarea / 2
        cum = 0.0
        for ly, hy, w in segments:
            if w > 0:
                add = (hy - ly) * w
                if cum + add >= target:
                    return ly + (target - cum) / w
                cum += add
        return 0.0


class CoverTree:
    def __init__(self, xpos):
        self.xpos = xpos
        self.segn = len(xpos) - 1
        if self.segn <= 0:
            return
        self.clen = [0] * (4 * self.segn)
        self.vals = [0.0] * (4 * self.segn)
        self.maxl = [0.0] * (4 * self.segn)
        self._makefull(1, 0, self.segn - 1)

    def _makefull(self, no, st, en):
        if st == en:
            self.maxl[no] = self.xpos[st + 1] - self.xpos[st]
            return
        md = (st + en) // 2
        self._makefull(2 * no, st, md)
        self._makefull(2 * no + 1, md + 1, en)
        self.maxl[no] = self.maxl[2 * no] + self.maxl[2 * no + 1]

    def update(self, l, r, v):
        if self.segn <= 0:
            return
        self._mod(1, 0, self.segn - 1, l, r, v)

    def _mod(self, no, st, en, l, r, v):
        if r <= st or en < l:
            return
        if l <= st and en <= r:
            self.clen[no] += v
        else:
            md = (st + en) // 2
            self._mod(2 * no, st, md, l, r, v)
            self._mod(2 * no + 1, md + 1, en, l, r, v)
        if self.clen[no] > 0:
            self.vals[no] = self.maxl[no]
        else:
            if st == en:
                self.vals[no] = 0.0
            else:
                self.vals[no] = self.vals[2 * no] + self.vals[2 * no + 1]

    def query(self):
        if self.segn <= 0:
            return 0.0
        return self.vals[1]
