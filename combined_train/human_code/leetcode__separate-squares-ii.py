class C1(object):

    def separateSquares(self, a1):
        """
        """

        class SegmentTreeRecu(object):

            def __init__(self, a1):
                self.sorted_x = a1
                v1 = len(a1) - 1
                v2 = 1 << (v1 - 1).bit_length() + 1
                self.tree = [0] * v2
                self.cnt = [0] * v2

            def update(self, a1, a2, a3, a4, a5, a6):
                if a1 >= a5 or a2 <= a4:
                    return
                if a1 <= a4 and a5 <= a2:
                    self.cnt[a6] += a3
                else:
                    v1 = a4 + (a5 - a4) // 2
                    self.update(a1, a2, a3, a4, v1, 2 * a6)
                    self.update(a1, a2, a3, v1, a5, 2 * a6 + 1)
                if self.cnt[a6] > 0:
                    self.tree[a6] = self.sorted_x[a5] - self.sorted_x[a4]
                elif a5 - a4 == 1:
                    self.tree[a6] = 0
                else:
                    self.tree[a6] = self.tree[2 * a6] + self.tree[2 * a6 + 1]
        v1 = []
        v2 = set()
        for v3, v4, v5 in a1:
            v1.append((v4, 1, v3, v3 + v5))
            v1.append((v4 + v5, -1, v3, v3 + v5))
            v2.add(v3)
            v2.add(v3 + v5)
        v1.sort(key=lambda e: e[0])
        v6 = sorted(v2)
        v7 = {v3: i for v8, v3 in enumerate(v6)}
        v9 = SegmentTreeRecu(v6)
        v10 = v1[0][0]
        v11 = []
        for v4, v12, v13, v14 in v1:
            if v4 != v10:
                v11.append([v10, v4, v9.tree[1]])
                v10 = v4
            v9.update(v7[v13], v7[v14], v12, 0, len(v6) - 1, 1)
        v15 = sum(((y2 - y1) * curr for v16, v17, v18 in v11)) / 2.0
        v19 = 0.0
        for v16, v17, v18 in v11:
            if v19 + (v17 - v16) * v18 >= v15:
                break
            v19 += (v17 - v16) * v18
        return v16 + (v15 - v19) / v18
