class C1(object):

    def minRemoval(self, a1, a2):
        v1 = sorted(a1)
        v2 = len(v1)
        v3 = 0
        for v4 in range(v2):
            v5 = a2 * v1[v4]
            v6 = v4
            v7 = v2 - 1
            while v6 <= v7:
                v8 = (v6 + v7) // 2
                if v1[v8] <= v5:
                    v6 = v8 + 1
                else:
                    v7 = v8 - 1
            v9 = v7
            if v9 >= v4:
                v3 = max(v3, v9 - v4 + 1)
        return v2 - v3
