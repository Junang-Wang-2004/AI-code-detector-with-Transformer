class C1:

    def countBinarySubstrings(self, a1):
        if not a1:
            return 0
        v1 = []
        v2 = 1
        v3 = a1[0]
        for v4 in a1[1:]:
            if v4 == v3:
                v2 += 1
            else:
                v1.append(v2)
                v2 = 1
                v3 = v4
        v1.append(v2)
        v5 = 0
        for v6 in range(1, len(v1)):
            v5 += min(v1[v6 - 1], v1[v6])
        return v5
