class C1:

    def majorityElement(self, a1):
        v1 = v2 = None
        v3 = v4 = 0
        for v5 in a1:
            if v1 == v5:
                v3 += 1
            elif v2 == v5:
                v4 += 1
            elif v3 == 0:
                v1 = v5
                v3 = 1
            elif v4 == 0:
                v2 = v5
                v4 = 1
            else:
                v3 -= 1
                v4 -= 1
        v3 = v4 = 0
        v6 = len(a1)
        v7 = v6 // 3
        for v5 in a1:
            if v1 == v5:
                v3 += 1
            if v2 == v5:
                v4 += 1
        v8 = []
        if v3 > v7:
            v8.append(v1)
        if v4 > v7:
            v8.append(v2)
        return v8
