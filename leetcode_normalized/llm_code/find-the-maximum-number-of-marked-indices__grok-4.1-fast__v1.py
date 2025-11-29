class C1:

    def maxNumOfMarkedIndices(self, a1):
        a1.sort()
        v1 = len(a1)
        v2 = 0
        v3 = v1 // 2
        for v4 in range(v1 // 2):
            while v3 < v1 and a1[v3] < 2 * a1[v4]:
                v3 += 1
            if v3 < v1:
                v2 += 1
                v3 += 1
        return v2 * 2
