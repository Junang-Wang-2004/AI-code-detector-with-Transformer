class C1(object):

    def colorBorder(self, a1, a2, a3, a4):
        v1 = len(a1)
        if v1 == 0:
            return a1
        v2 = len(a1[0])
        v3 = a1[a2][a3]
        v4 = set([(a2, a3)])
        v5 = [(a2, a3)]
        v6 = []
        v7 = [-1, 0, 1, 0]
        v8 = [0, 1, 0, -1]
        while v5:
            v9, v10 = v5.pop()
            v11 = 0
            for v12 in range(4):
                v13 = v9 + v7[v12]
                v14 = v10 + v8[v12]
                if 0 <= v13 < v1 and 0 <= v14 < v2 and (a1[v13][v14] == v3):
                    v11 += 1
                v15 = (v13, v14)
                if 0 <= v13 < v1 and 0 <= v14 < v2 and (a1[v13][v14] == v3) and (v15 not in v4):
                    v4.add(v15)
                    v5.append(v15)
            if v11 < 4:
                v6.append((v9, v10))
        for v9, v10 in v6:
            a1[v9][v10] = a4
        return a1
