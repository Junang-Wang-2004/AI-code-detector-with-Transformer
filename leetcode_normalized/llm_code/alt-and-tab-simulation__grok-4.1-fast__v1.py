class C1:

    def simulationResult(self, a1, a2):
        v1 = set()
        v2 = []
        for v3 in range(len(a2) - 1, -1, -1):
            v4 = a2[v3]
            if v4 not in v1:
                v1.add(v4)
                v2.append(v4)
        for v5 in a1:
            if v5 not in v1:
                v2.append(v5)
        return v2
