class C1(object):

    def getMaxGridHappiness(self, a1, a2, a3, a4):
        """
        """

        def left(a1):
            return a1[-1] if len(a1) % a2 else 0

        def up(a1):
            return a1[-a2] if len(a1) >= a2 else 0

        def count_total(a1, a2, a3):
            return a3 - 30 * ((left(a1) == 1) + (up(a1) == 1)) + 20 * ((left(a1) == 2) + (up(a1) == 2)) + (120 - 30 * ((left(a1) != 0) + (up(a1) != 0))) * (a2 == 1) + (40 + 20 * ((left(a1) != 0) + (up(a1) != 0))) * (a2 == 2)

        def iter_backtracking(a1, a2):
            v1 = 0
            v2 = []
            v3 = [(2, (a1, a2, 0))]
            while v3:
                v4, v5 = v3.pop()
                if v4 == 2:
                    a1, a2, v8 = v5
                    if len(v2) == a1 * a2 or (a1 == 0 and a2 == 0):
                        v1 = max(v1, v8)
                        continue
                    if v8 + (a1 + a2) * 120 < v1:
                        continue
                    if a2 > 0:
                        v3.append((3, tuple()))
                        v3.append((2, (a1, a2 - 1, count_total(v2, 2, v8))))
                        v3.append((1, (2,)))
                    if a1 > 0:
                        v3.append((3, tuple()))
                        v3.append((2, (a1 - 1, a2, count_total(v2, 1, v8))))
                        v3.append((1, (1,)))
                    if left(v2) or up(v2):
                        v3.append((3, tuple()))
                        v3.append((2, (a1, a2, v8)))
                        v3.append((1, (0,)))
                elif v4 == 1:
                    v9 = v5[0]
                    v2.append(v9)
                elif v4 == 3:
                    v2.pop()
            return v1
        return iter_backtracking(a3, a4)
