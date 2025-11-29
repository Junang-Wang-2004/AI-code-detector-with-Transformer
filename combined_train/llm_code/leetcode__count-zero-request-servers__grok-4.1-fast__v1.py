class C1:

    def countServers(self, a1, a2, a3, a4):
        v1 = []
        for v2, v3 in a2:
            v4 = v2 - 1
            v1.append((v3, 0, 1, v4))
            v1.append((v3 + a3 + 1, 0, -1, v4))
        for v5, v6 in enumerate(a4):
            v1.append((v6, 1, 0, v5))
        v1.sort(key=lambda e: (e[0], e[1]))
        v7 = [0] * a1
        v8 = 0
        v9 = [0] * len(a4)
        for v10, v11, v12, v13 in v1:
            if v11 == 0:
                v14 = v13
                v15 = v7[v14]
                v7[v14] += v12
                v16 = v7[v14]
                if v15 == 0 and v16 > 0:
                    v8 += 1
                elif v15 > 0 and v16 == 0:
                    v8 -= 1
            else:
                v9[v13] = a1 - v8
        return v9
