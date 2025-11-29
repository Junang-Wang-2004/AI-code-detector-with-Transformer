class C1(object):

    def remainingMethods(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a3:
            v1[v3].append(v4)
        v5 = [False] * a1
        v5[a2] = True
        v6 = [a2]
        while v6:
            v7 = []
            for v8 in v6:
                for v9 in v1[v8]:
                    if not v5[v9]:
                        v5[v9] = True
                        v7.append(v9)
            v6 = v7
        v10 = any((not v5[frm] and v5[to] for v11, v12 in a3))
        if v10:
            return list(range(a1))
        return [idx for v13 in range(a1) if not v5[v13]]
