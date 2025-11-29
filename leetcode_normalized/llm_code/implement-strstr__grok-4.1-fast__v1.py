class C1:

    def strStr(self, a1, a2):
        if not a2:
            return 0
        v1, v2 = (len(a1), len(a2))
        for v3 in range(v1 - v2 + 1):
            v4 = 0
            while v4 < v2 and a1[v3 + v4] == a2[v4]:
                v4 += 1
            if v4 == v2:
                return v3
        return -1
