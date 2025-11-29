class C1(object):

    def shortestSuperstring(self, a1):
        """
        """
        v1 = len(a1)
        v2 = [[0] * v1 for v3 in range(v1)]
        for v4, v5 in enumerate(a1):
            for v6, v7 in enumerate(a1):
                for v8 in reversed(range(min(len(v5), len(v7)))):
                    if v7[:v8].startswith(v5[len(v5) - v8:]):
                        v2[v4][v6] = v8
                        break
        v9 = [[0] * v1 for v3 in range(1 << v1)]
        v10 = [[None] * v1 for v3 in range(1 << v1)]
        for v11 in range(1, 1 << v1):
            for v12 in range(v1):
                if v11 >> v12 & 1 == 0:
                    continue
                v13 = v11 ^ 1 << v12
                for v4 in range(v1):
                    if v13 >> v4 & 1 == 0:
                        continue
                    v14 = v9[v13][v4] + v2[v4][v12]
                    if v14 > v9[v11][v12]:
                        v9[v11][v12] = v14
                        v10[v11][v12] = v4
        v12 = max(range(v1), key=v9[-1].__getitem__)
        v15 = []
        v11 = (1 << v1) - 1
        while v12 is not None:
            v15.append(v12)
            v11, v12 = (v11 ^ 1 << v12, v10[v11][v12])
        v15.reverse()
        v16 = set(v15)
        v15.extend([v4 for v4 in range(v1) if v4 not in v16])
        v17 = [a1[v15[0]]]
        for v4 in range(1, len(v15)):
            v18 = v2[v15[v4 - 1]][v15[v4]]
            v17.append(a1[v15[v4]][v18:])
        return ''.join(v17)
