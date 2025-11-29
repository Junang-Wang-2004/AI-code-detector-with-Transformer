class C1:

    def __init__(self, a1):
        self.length = len(a1)
        self.data = [None] * (4 * self.length)
        self._build(1, 0, self.length - 1, a1)

    def _build(self, a1, a2, a3, a4):
        if a2 == a3:
            v1 = a4[a2]
            self.data[a1] = [v1, v1, 1, 1, 1, 1]
            return
        v2 = (a2 + a3) // 2
        self._build(2 * a1, a2, v2, a4)
        self._build(2 * a1 + 1, v2 + 1, a3, a4)
        self.data[a1] = self._merge(self.data[2 * a1], self.data[2 * a1 + 1])

    def _merge(self, a1, a2):
        v1, v2, v3, v4, v5, v6 = a1
        v7, v8, v9, v10, v11, v12 = a2
        v13 = v1
        v14 = v8
        v15 = v3 + v9 if v3 == v5 and v2 == v7 else v3
        v16 = v10 + v4 if v10 == v11 and v7 == v2 else v10
        v17 = v5 + v11
        v18 = max(v6, v12, v4 + v9 if v2 == v7 else 0)
        return [v13, v14, v15, v16, v17, v18]

    def change(self, a1, a2):
        self._change(1, 0, self.length - 1, a1, a2)

    def _change(self, a1, a2, a3, a4, a5):
        if a2 == a3:
            self.data[a1] = [a5, a5, 1, 1, 1, 1]
            return
        v1 = (a2 + a3) // 2
        if a4 <= v1:
            self._change(2 * a1, a2, v1, a4, a5)
        else:
            self._change(2 * a1 + 1, v1 + 1, a3, a4, a5)
        self.data[a1] = self._merge(self.data[2 * a1], self.data[2 * a1 + 1])

    def current_max(self):
        return self.data[1][5]

class C2:

    def longestRepeating(self, a1, a2, a3):
        v1 = C1(a1)
        v2 = []
        for v3, v4 in zip(a2, a3):
            v1.change(v4, v3)
            v2.append(v1.current_max())
        return v2
