class C1(object):

    def recoverArray(self, a1):
        a1.sort()
        v1 = len(a1) // 2
        v2 = {}
        for v3 in a1:
            v2[v3] = v2.get(v3, 0) + 1
        for v4 in range(1, v1 + 1):
            v5 = a1[v4] - a1[0]
            if v5 == 0 or v5 % 2 != 0:
                continue
            v6 = v5 // 2
            v7 = v2.copy()
            v8 = []
            v9 = True
            for v10 in a1:
                if v7.get(v10, 0) == 0:
                    continue
                v11 = v10 + 2 * v6
                if v7.get(v11, 0) == 0:
                    v9 = False
                    break
                v7[v10] -= 1
                v7[v11] -= 1
                v8.append(v10 + v6)
            if v9:
                return v8
        return []
