class C1(object):

    def splitArray(self, a1):
        if len(a1) < 7:
            return False
        v1 = [0]
        for v2 in a1:
            v1.append(v1[-1] + v2)
        v3 = len(a1)
        v4 = v1[v3]
        for v5 in range(2, v3 - 1):
            v6 = v1[v5]
            if v6 * 2 != v4:
                continue
            v7 = v6 // 2
            v8 = any((v1[p] == v7 for v9 in range(1, v5)))
            if not v8:
                continue
            v10 = v4 - v7
            v11 = any((v1[v9] == v10 for v9 in range(v5 + 1, v3)))
            if v11:
                return True
        return False
