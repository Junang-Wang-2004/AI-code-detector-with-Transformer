class C1(object):

    def __init__(self, a1, a2):
        self.start, self.end = (a1, a2)
        self.total = self.count = 0
        self._left = self._right = None

    def mid(self):
        return (self.start + self.end) // 2

    def left(self):
        self._left = self._left or C1(self.start, self.mid())
        return self._left

    def right(self):
        self._right = self._right or C1(self.mid(), self.end)
        return self._right

    def update(self, a1, a2, a3, a4):
        if a2 >= a3:
            return 0
        if self.start == a2 and self.end == a3:
            self.count += a4
        else:
            self.left().update(a1, a2, min(self.mid(), a3), a4)
            self.right().update(a1, max(self.mid(), a2), a3, a4)
        if self.count > 0:
            self.total = a1[self.end] - a1[self.start]
        else:
            self.total = self.left().total + self.right().total
        return self.total

class C2(object):

    def rectangleArea(self, a1):
        """
        """
        v1, v2 = (1, -1)
        v3 = []
        v4 = set()
        for v5, v6, v7, v8 in a1:
            v3.append((v6, v1, v5, v7))
            v3.append((v8, v2, v5, v7))
            v4.add(v5)
            v4.add(v7)
        v3.sort()
        v4 = sorted(v4)
        v9 = {x: i for v10, v11 in enumerate(v4)}
        v12 = C1(0, len(v4) - 1)
        v13 = 0
        v14 = 0
        v15 = v3[0][0]
        for v16, v17, v5, v7 in v3:
            v13 += v14 * (v16 - v15)
            v14 = v12.update(v4, v9[v5], v9[v7], v17)
            v15 = v16
        return v13 % (10 ** 9 + 7)
