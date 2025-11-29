class C1(object):

    def concatenatedDivisibility(self, a1, a2):
        """
        """

        def length(a1):
            v1 = 0
            while a1:
                v1 += 1
                a1 //= 10
            return max(v1, 1)
        v1 = [length(x) for v2 in a1]
        v3 = max(v1)
        v4 = [0] * (v3 + 1)
        v4[0] = 1 % a2
        for v5 in range(len(v4) - 1):
            v4[v5 + 1] = v4[v5] * 10 % a2
        v6 = [[False] * a2 for v7 in range(1 << len(a1))]
        v6[-1][0] = True
        for v8 in reversed(range(len(v6) - 1)):
            for v9 in range(a2):
                for v5, v10 in enumerate(v1):
                    if v8 & 1 << v5:
                        continue
                    if v6[v8 | 1 << v5][(v9 * v4[v10] + a1[v5]) % a2]:
                        v6[v8][v9] = True
                        break
        v11 = []
        if not v6[0][0]:
            return v11
        v12 = sorted(((v2, v5) for v5, v2 in enumerate(a1)))
        v8 = v9 = 0
        for v7 in range(len(a1)):
            for v7, v5 in v12:
                if v8 & 1 << v5:
                    continue
                if v6[v8 | 1 << v5][(v9 * v4[v1[v5]] + a1[v5]) % a2]:
                    v11.append(a1[v5])
                    v8 |= 1 << v5
                    v9 = (v9 * v4[v1[v5]] + a1[v5]) % a2
                    break
        return v11
