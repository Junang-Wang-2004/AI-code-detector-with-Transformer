class C1:

    def maxSelectedElements(self, a1):
        if not a1:
            return 0
        a1.sort()
        v1 = 1
        v2 = 1
        v3 = 1
        v4 = a1[0]
        for v5 in range(1, len(a1)):
            v6 = a1[v5]
            v7 = v6 - v4
            if v7 == 0:
                v3 = max(v3, v2 + 1)
            elif v7 == 1:
                v2 += 1
                v3 += 1
            elif v7 == 2:
                v2 = v3 + 1
                v3 = 1
            else:
                v2 = 1
                v3 = 1
            v1 = max(v1, v2, v3)
            v4 = v6
        return v1
