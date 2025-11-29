class C1:

    def findChampion(self, a1, a2):
        v1 = set()
        for v2, v3 in a2:
            v1.add(v3)
        if len(v1) != a1 - 1:
            return -1
        v4 = a1 * (a1 - 1) // 2
        v5 = sum(v1)
        return v4 - v5
