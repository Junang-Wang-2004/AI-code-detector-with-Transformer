class C1:

    def depthSumInverse(self, a1):
        v1 = [(elem, 0) for v2 in a1]
        v3 = []
        v4 = 0
        while v1:
            v5, v6 = v1.pop(0)
            v4 = max(v4, v6)
            while len(v3) <= v6:
                v3.append(0)
            if v5.isInteger():
                v3[v6] += v5.getInteger()
            else:
                for v7 in v5.getList():
                    v1.append((v7, v6 + 1))
        v8 = 0
        v9 = len(v3)
        for v10, v11 in enumerate(v3):
            v8 += v11 * (v9 - v10)
        return v8
