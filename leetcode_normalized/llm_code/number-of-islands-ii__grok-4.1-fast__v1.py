class C1:

    def numIslands2(self, a1, a2, a3):
        v1 = {}
        v2 = {}
        v3 = 0
        v4 = []
        v5 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def idx(a1, a2):
            return a1 * a2 + a2

        def root(a1):
            if v1[a1] != a1:
                v1[a1] = root(v1[a1])
            return v1[a1]

        def link(a1, a2):
            v1, v2 = (root(a1), root(a2))
            if v1 == v2:
                return False
            if v2[v1] < v2[v2]:
                v1[v1] = v2
                v2[v2] += v2[v1]
            else:
                v1[v2] = v1
                v2[v1] += v2[v2]
            return True
        for v6, v7 in a3:
            v8 = idx(v6, v7)
            v1[v8] = v8
            v2[v8] = 1
            v3 += 1
            for v9, v10 in v5:
                v11, v12 = (v6 + v9, v7 + v10)
                if 0 <= v11 < a1 and 0 <= v12 < a2:
                    v13 = idx(v11, v12)
                    if v13 in v1 and link(v8, v13):
                        v3 -= 1
            v4.append(v3)
        return v4
