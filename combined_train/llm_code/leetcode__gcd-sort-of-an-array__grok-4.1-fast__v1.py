class C1(object):

    def gcdSort(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return True
        v2 = max(a1)
        v3 = list(range(v2 + 1))
        v4 = [0] * (v2 + 1)

        def find(a1):
            v1 = a1
            while v3[v1] != v1:
                v1 = v3[v1]
            v2 = a1
            while v2 != v1:
                v3 = v3[v2]
                v3[v2] = v1
                v2 = v3
            return v1

        def unite(a1, a2):
            v1 = find(a1)
            v2 = find(a2)
            if v1 == v2:
                return
            if v4[v1] < v4[v2]:
                v3[v1] = v2
            elif v4[v1] > v4[v2]:
                v3[v2] = v1
            else:
                v3[v2] = v1
                v4[v1] += 1
        v5 = list(range(v2 + 1))
        v6 = int(v2 ** 0.5) + 1
        for v7 in range(2, v6):
            if v5[v7] == v7:
                for v8 in range(v7 * v7, v2 + 1, v7):
                    if v5[v8] == v8:
                        v5[v8] = v7
        v9 = set(a1)
        for v10 in v9:
            if v10 < 2:
                continue
            v11 = v10
            while v11 > 1:
                v12 = v5[v11]
                unite(v10 - 1, v12 - 1)
                while v11 % v12 == 0:
                    v11 //= v12
        v13 = sorted(a1)
        for v7 in range(v1):
            if find(a1[v7] - 1) != find(v13[v7] - 1):
                return False
        return True
