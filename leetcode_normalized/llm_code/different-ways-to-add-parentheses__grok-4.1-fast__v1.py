import re

class C1:

    def diffWaysToCompute(self, a1):
        v1 = re.findall('\\d+|[+\\-*]', a1)
        v2 = []
        v3 = []
        for v4 in v1:
            if v4 in '+-*':
                v3.append(v4)
            else:
                v2.append(int(v4))
        v5 = len(v2)
        v6 = [[[] for v7 in range(v5)] for v7 in range(v5)]
        for v8 in range(v5):
            v6[v8][v8] = [v2[v8]]
        for v9 in range(2, v5 + 1):
            for v10 in range(v5 - v9 + 1):
                v11 = v10 + v9 - 1
                for v12 in range(v10, v11):
                    v13 = v6[v10][v12]
                    v14 = v6[v12 + 1][v11]
                    v15 = v3[v12]
                    for v16 in v13:
                        for v17 in v14:
                            if v15 == '+':
                                v6[v10][v11].append(v16 + v17)
                            elif v15 == '-':
                                v6[v10][v11].append(v16 - v17)
                            else:
                                v6[v10][v11].append(v16 * v17)
        return v6[0][v5 - 1]
