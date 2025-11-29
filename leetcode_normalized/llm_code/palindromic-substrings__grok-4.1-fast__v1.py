class C1:

    def countSubstrings(self, a1):
        v1 = ['^']
        for v2 in a1:
            v1.append('#')
            v1.append(v2)
        v1.append('#')
        v1.append('$')
        v3 = len(v1)
        v4 = [0] * v3
        v5 = 0
        v6 = 0
        for v7 in range(1, v3 - 1):
            v8 = 2 * v5 - v7
            if v7 < v6:
                v4[v7] = min(v6 - v7, v4[v8])
            v9 = v7 - 1 - v4[v7]
            v10 = v7 + 1 + v4[v7]
            while v9 >= 0 and v10 < v3 and (v1[v9] == v1[v10]):
                v4[v7] += 1
                v9 -= 1
                v10 += 1
            if v7 + v4[v7] > v6:
                v5 = v7
                v6 = v7 + v4[v7]
        return sum(((r + 1) // 2 for v11 in v4))
