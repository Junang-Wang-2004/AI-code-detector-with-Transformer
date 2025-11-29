class C1:

    def findBuildings(self, a1):
        v1 = []
        v2 = 0
        v3 = len(a1)
        for v4 in range(v3 - 1, -1, -1):
            if a1[v4] > v2:
                v1.append(v4)
                v2 = a1[v4]
        v1.reverse()
        return v1
