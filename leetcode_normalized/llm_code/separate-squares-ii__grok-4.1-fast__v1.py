class C1:

    def separateSquares(self, a1):
        v1 = set()
        v2 = []
        for v3, v4, v5 in a1:
            v2.append((v4, 1, v3, v3 + v5))
            v2.append((v4 + v5, -1, v3, v3 + v5))
            v1.add(v3)
            v1.add(v3 + v5)
        v2.sort(key=lambda t: (t[0], -t[1]))
        v6 = sorted(v1)
        if not v6:
            return 0.0
        v7 = {p: i for v8, v9 in enumerate(v6)}
        v10 = C2(v6)
        v11 = []
        v12 = v2[0][0]
        for v13, v14, v15, v16 in v2:
            if v13 > v12:
                v11.append((v12, v13, v10.query()))
                v12 = v13
            v17 = v7[v15]
            v18 = v7[v16]
            v10.update(v17, v18, v14)
        v19 = sum(((hy - ly) * w for v20, v21, v22 in v11))
        v23 = v19 / 2
        v24 = 0.0
        for v20, v21, v22 in v11:
            if v22 > 0:
                v25 = (v21 - v20) * v22
                if v24 + v25 >= v23:
                    return v20 + (v23 - v24) / v22
                v24 += v25
        return 0.0

class C2:

    def __init__(self, a1):
        self.xpos = a1
        self.segn = len(a1) - 1
        if self.segn <= 0:
            return
        self.clen = [0] * (4 * self.segn)
        self.vals = [0.0] * (4 * self.segn)
        self.maxl = [0.0] * (4 * self.segn)
        self._makefull(1, 0, self.segn - 1)

    def _makefull(self, a1, a2, a3):
        if a2 == a3:
            self.maxl[a1] = self.xpos[a2 + 1] - self.xpos[a2]
            return
        v1 = (a2 + a3) // 2
        self._makefull(2 * a1, a2, v1)
        self._makefull(2 * a1 + 1, v1 + 1, a3)
        self.maxl[a1] = self.maxl[2 * a1] + self.maxl[2 * a1 + 1]

    def update(self, a1, a2, a3):
        if self.segn <= 0:
            return
        self._mod(1, 0, self.segn - 1, a1, a2, a3)

    def _mod(self, a1, a2, a3, a4, a5, a6):
        if a5 <= a2 or a3 < a4:
            return
        if a4 <= a2 and a3 <= a5:
            self.clen[a1] += a6
        else:
            v1 = (a2 + a3) // 2
            self._mod(2 * a1, a2, v1, a4, a5, a6)
            self._mod(2 * a1 + 1, v1 + 1, a3, a4, a5, a6)
        if self.clen[a1] > 0:
            self.vals[a1] = self.maxl[a1]
        elif a2 == a3:
            self.vals[a1] = 0.0
        else:
            self.vals[a1] = self.vals[2 * a1] + self.vals[2 * a1 + 1]

    def query(self):
        if self.segn <= 0:
            return 0.0
        return self.vals[1]
