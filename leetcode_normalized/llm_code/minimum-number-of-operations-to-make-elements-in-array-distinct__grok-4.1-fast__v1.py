class C1:

    def minimumOperations(self, a1):
        v1 = len(a1)
        v2 = set()
        for v3 in range(v1 - 1, -1, -1):
            if a1[v3] in v2:
                return (v3 + 1 + 2) // 3
            v2.add(a1[v3])
        return 0
