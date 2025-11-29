class C1(object):

    def isEscapePossible(self, a1, a2, a3):
        v1 = 1000000
        v2 = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def reachable(a1, a2, a3):
            v1 = set((tuple(pos) for v2 in a1))
            v3 = len(v1)
            v4 = v3 * (v3 - 1) // 2
            v5 = set([a2])
            if len(v5) > v4:
                return True
            v6 = [a2]
            while v6:
                v7 = v6.pop(0)
                if v7 == a3:
                    return True
                for v8, v9 in v2:
                    v10 = v7[0] + v8
                    v11 = v7[1] + v9
                    v12 = (v10, v11)
                    if 0 <= v10 < v1 and 0 <= v11 < v1 and (v12 not in v5) and (v12 not in v1):
                        v5.add(v12)
                        if len(v5) > v4:
                            return True
                        v6.append(v12)
            return False
        v3 = set((tuple(cell) for v4 in a1))
        v5 = tuple(a2)
        v6 = tuple(a3)
        return reachable(v3, v5, v6) and reachable(v3, v6, v5)
