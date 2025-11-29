class C1:

    def findDuplicates(self, a1):
        v1 = []
        v2 = len(a1)
        for v3 in range(v2):
            v4 = abs(a1[v3])
            v5 = v4 - 1
            if a1[v5] < 0:
                v1.append(v4)
            else:
                a1[v5] = -a1[v5]
        return v1
