class C1:

    def validPartition(self, a1):
        v1 = len(a1)
        v2 = [False] * (v1 + 1)
        v2[0] = True
        for v3 in range(1, v1 + 1):
            if v3 >= 2 and a1[v3 - 1] == a1[v3 - 2]:
                v2[v3] = v2[v3] or v2[v3 - 2]
            if v3 >= 3:
                v4, v5, v6 = a1[v3 - 3:v3]
                if v4 == v5 == v6 or v5 == v4 + 1 == v6:
                    v2[v3] = v2[v3] or v2[v3 - 3]
        return v2[v1]
