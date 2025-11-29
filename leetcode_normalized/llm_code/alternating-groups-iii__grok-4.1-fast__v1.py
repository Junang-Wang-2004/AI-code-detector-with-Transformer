from sortedcontainers import SortedList

class C1:

    def numberOfAlternatingGroups(self, a1, a2):
        v1 = len(a1)
        v2 = SortedList()

        class Fenwick:

            def __init__(self, a1):
                self.size = a1
                self.tree = [0] * (a1 + 1)

            def upd(self, a1, a2):
                while a1 <= self.size:
                    self.tree[a1] += a2
                    a1 += a1 & -a1

            def pre(self, a1):
                v1 = 0
                while a1 > 0:
                    v1 += self.tree[a1]
                    a1 -= a1 & -a1
                return v1
        v3 = Fenwick(v1)
        v4 = Fenwick(v1)

        def add_bad(a1):
            v2.add(a1)
            v1 = len(v2)
            if v1 == 1:
                v3.upd(v1, 1)
                v4.upd(v1, v1)
                return
            v2 = v2.index(a1)
            v3 = (v2 - 1) % v1
            v4 = (v2 + 1) % v1
            v5 = v2[v3]
            v6 = v2[v4]
            v7 = (v6 - v5 - 1) % v1 + 1
            v3.upd(v7, -1)
            v4.upd(v7, -v7)
            v8 = (a1 - v5) % v1
            v3.upd(v8, 1)
            v4.upd(v8, v8)
            v9 = (v6 - a1) % v1
            v3.upd(v9, 1)
            v4.upd(v9, v9)

        def rem_bad(a1):
            if not v2:
                return
            v1 = len(v2)
            v2 = v2.index(a1)
            if v1 == 1:
                v3.upd(v1, -1)
                v4.upd(v1, -v1)
                v2.pop(v2)
                return
            v3 = (v2 - 1) % v1
            v4 = (v2 + 1) % v1
            v5 = v2[v3]
            v6 = v2[v4]
            v7 = (v6 - v5 - 1) % v1 + 1
            v3.upd(v7, 1)
            v4.upd(v7, v7)
            v8 = (a1 - v5) % v1
            v3.upd(v8, -1)
            v4.upd(v8, -v8)
            v9 = (v6 - a1) % v1
            v3.upd(v9, -1)
            v4.upd(v9, -v9)
            v2.pop(v2)
        for v5 in range(v1):
            if a1[v5] == a1[(v5 + 1) % v1]:
                add_bad(v5)
        v6 = []
        for v7 in a2:
            v8 = v7[0]
            if v8 == 1:
                v9 = v7[1]
                if len(v2) == 0:
                    v6.append(v1)
                else:
                    v10 = v3.pre(v1) - v3.pre(v9 - 1)
                    v11 = v4.pre(v1) - v4.pre(v9 - 1)
                    v6.append(v11 - (v9 - 1) * v10)
            else:
                v12 = v7[1]
                v13 = v7[2]
                if a1[v12] == v13:
                    continue
                v14 = (v12 - 1) % v1
                v15 = (v12 + 1) % v1
                v16 = a1[v14] == a1[v12]
                v17 = a1[v12] == a1[v15]
                a1[v12] = v13
                v18 = a1[v14] == a1[v12]
                v19 = a1[v12] == a1[v15]
                if v16 != v18:
                    if v18:
                        add_bad(v14)
                    else:
                        rem_bad(v14)
                if v17 != v19:
                    if v19:
                        add_bad(v12)
                    else:
                        rem_bad(v12)
        return v6
