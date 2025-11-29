class C1:

    def findOcurrences(self, a1, a2, a3):
        v1 = a1.split()
        v2 = []
        v3 = len(v1)
        for v4 in range(v3 - 2):
            if v1[v4] == a2 and v1[v4 + 1] == a3:
                v2.append(v1[v4 + 2])
        return v2
