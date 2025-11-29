class C1(object):

    def minimumCost(self, a1, a2, a3):
        v1 = list(range(a1))
        v2 = [0] * a1

        def find(a1):
            v1 = a1
            while v1[v1] != v1:
                v1 = v1[v1]
            while a1 != v1:
                v2 = v1[a1]
                v1[a1] = v1
                a1 = v2
            return v1

        def unite(a1, a2):
            v1 = find(a1)
            v2 = find(a2)
            if v1 == v2:
                return
            if v2[v1] < v2[v2]:
                v1[v1] = v2
            elif v2[v1] > v2[v2]:
                v1[v2] = v1
            else:
                v1[v2] = v1
                v2[v1] += 1
        for v3, v4, v5 in a2:
            unite(v3, v4)
        v6 = [-1] * a1
        for v3, v4, v7 in a2:
            v8 = find(v3)
            v6[v8] &= v7
        v9 = []
        for v10, v11 in a3:
            v12 = find(v10)
            v13 = find(v11)
            if v12 != v13:
                v9.append(-1)
            elif v10 == v11:
                v9.append(0)
            else:
                v9.append(v6[v12])
        return v9
