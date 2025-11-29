class C1(object):

    def minimumJumps(self, a1, a2, a3, a4):
        v1 = set(a1)
        v2 = max(a1) if a1 else 0
        v3 = max(a4, v2) + a2 + 2 * a3
        v4 = set()
        v5 = [(0, True)]
        v4.add((0, True))
        v6 = 0
        while v5:
            v7 = []
            for v8, v9 in v5:
                if v8 == a4:
                    return v6
                v10 = v8 + a2
                if v10 <= v3 and v10 not in v1:
                    v11 = (v10, True)
                    if v11 not in v4:
                        v4.add(v11)
                        v7.append(v11)
                if v9:
                    v12 = v8 - a3
                    if v12 >= 0 and v12 not in v1:
                        v13 = (v12, False)
                        if v13 not in v4:
                            v4.add(v13)
                            v7.append(v13)
            v5 = v7
            v6 += 1
        return -1
