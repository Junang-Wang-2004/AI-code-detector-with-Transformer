class C1(object):

    def maxRectangleArea(self, a1, a2):
        v1 = {}
        for v2 in range(len(a1)):
            v3 = a1[v2]
            if v3 not in v1:
                v1[v3] = []
            v1[v3].append(a2[v2])
        v4 = sorted(v1)
        v5 = sorted(set(a2))
        v6 = {val: idx + 1 for v7, v8 in enumerate(v5)}
        v9 = len(v5)

        class FenwickTree(object):

            def __init__(self, a1):
                self.size = a1
                self.data = [0] * (a1 + 2)

            def modify(self, a1, a2):
                while a1 <= self.size:
                    self.data[a1] += a2
                    a1 += a1 & -a1

            def sum_up_to(self, a1):
                v1 = 0
                while a1 > 0:
                    v1 += self.data[a1]
                    a1 -= a1 & -a1
                return v1
        v10 = FenwickTree(v9)
        v11 = {}
        v12 = -1
        for v13 in v4:
            v14 = sorted(v1[v13])
            if len(v14) >= 2:
                for v15 in range(len(v14) - 1):
                    v16 = v14[v15]
                    v17 = v14[v15 + 1]
                    v18 = v6[v16]
                    v19 = v6[v17]
                    v20 = v10.sum_up_to(v19) - v10.sum_up_to(v18 - 1)
                    v21 = (v18, v19)
                    if v21 in v11 and v11[v21][0] == v20:
                        v22 = v13 - v11[v21][1]
                        v23 = v17 - v16
                        v24 = v22 * v23
                        if v24 > v12:
                            v12 = v24
                    v11[v21] = (v20 + 2, v13)
            for v25 in v14:
                v10.modify(v6[v25], 1)
        return v12
