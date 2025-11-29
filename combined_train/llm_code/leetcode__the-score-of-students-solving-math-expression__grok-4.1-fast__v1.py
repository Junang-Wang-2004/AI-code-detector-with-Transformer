class C1(object):

    def scoreOfStudents(self, a1, a2):
        v1 = [int(a1[i]) for v2 in range(0, len(a1), 2)]
        v3 = [a1[v2] for v2 in range(1, len(a1), 2)]
        v4 = len(v1)
        v5 = 1000
        v6 = [[set() for v7 in range(v4)] for v7 in range(v4)]
        for v2 in range(v4):
            v6[v2][v2].add(v1[v2])
        for v8 in range(2, v4 + 1):
            for v2 in range(v4 - v8 + 1):
                v9 = v2 + v8 - 1
                for v10 in range(v2, v9):
                    v11 = v3[v10]
                    v12 = v6[v2][v10]
                    v13 = v6[v10 + 1][v9]
                    if v11 == '+':
                        for v14 in v12:
                            for v15 in v13:
                                v16 = v14 + v15
                                if v16 <= v5:
                                    v6[v2][v9].add(v16)
                    else:
                        for v14 in v12:
                            for v15 in v13:
                                v17 = v14 * v15
                                if v17 <= v5:
                                    v6[v2][v9].add(v17)
        v18 = v6[0][v4 - 1]
        v19 = []
        v20 = v1[0]
        for v21 in range(len(v3)):
            if v3[v21] == '*':
                v20 *= v1[v21 + 1]
            else:
                v19.append(v20)
                v20 = v1[v21 + 1]
        v19.append(v20)
        v22 = sum(v19)
        return sum((5 if a == v22 else 2 if a in v18 else 0 for v23 in a2))
