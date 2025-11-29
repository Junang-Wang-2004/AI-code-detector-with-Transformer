from sortedcontainers import SortedList

class C1:

    def getResults(self, a1):
        v1 = sorted((q[1] for v2 in a1 if v2[0] == 1))
        v3 = {v: ii for v4, v5 in enumerate(v1)}
        v6 = len(v1)

        class MaxSegTree:

            def __init__(self, a1):
                self.nn = a1
                self.t = [0] * (4 * a1)

            def _upd(self, a1, a2, a3, a4, a5):
                if a2 == a3:
                    self.t[a1] = a5
                    return
                v1 = (a2 + a3) // 2
                if a4 <= v1:
                    self._upd(2 * a1, a2, v1, a4, a5)
                else:
                    self._upd(2 * a1 + 1, v1 + 1, a3, a4, a5)
                self.t[a1] = max(self.t[2 * a1], self.t[2 * a1 + 1])

            def upd(self, a1, a2):
                self._upd(1, 0, self.nn - 1, a1, a2)

            def _qry(self, a1, a2, a3, a4, a5):
                if a5 < a2 or a3 < a4:
                    return 0
                if a4 <= a2 and a3 <= a5:
                    return self.t[a1]
                v1 = (a2 + a3) // 2
                return max(self._qry(2 * a1, a2, v1, a4, a5), self._qry(2 * a1 + 1, v1 + 1, a3, a4, a5))

            def qry(self, a1, a2):
                return self._qry(1, 0, self.nn - 1, a1, a2)
        v7 = MaxSegTree(v6) if v6 > 0 else None
        v8 = SortedList()
        v9 = []
        for v10 in a1:
            v11 = v10[0]
            v12 = v10[1]
            v13 = v8.bisect_left(v12)
            v14 = v8[v13 - 1] if v13 > 0 else 0
            if v11 == 1:
                v8.add(v12)
                v7.upd(v3[v12], v12 - v14)
                if v13 + 1 < len(v8):
                    v15 = v8[v13 + 1]
                    v7.upd(v3[v15], v15 - v12)
            else:
                v16 = v10[2]
                v17 = v12 - v14
                v18 = v17 >= v16
                if not v18 and v13 > 0:
                    v19 = v3[v8[v13 - 1]]
                    v18 = v7.qry(0, v19) >= v16
                v9.append(v18)
        return v9
