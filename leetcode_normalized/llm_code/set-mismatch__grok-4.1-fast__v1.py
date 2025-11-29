class C1:

    def findErrorNums(self, a1):
        v1 = len(a1)
        v2 = v1 * (v1 + 1) // 2
        v3 = v1 * (v1 + 1) * (2 * v1 + 1) // 6
        v4 = sum(a1)
        v5 = sum((x * x for v6 in a1))
        v7 = v4 - v2
        v8 = v5 - v3
        v9 = v8 // v7
        v10 = (v9 + v7) // 2
        v11 = v9 - v10
        return [v10, v11]
