class C1:

    def subStrHash(self, a1, a2, a3, a4, a5):
        v1 = len(a1)
        if v1 < a4:
            return ''
        v2 = pow(a2, a4 - 1, a3)
        v3 = 0
        for v4 in range(a4):
            v3 = (v3 * a2 + ord(a1[v4]) - 96) % a3
        if v3 == a5:
            return a1[:a4]
        for v5 in range(1, v1 - a4 + 1):
            v3 = (v3 - (ord(a1[v5 - 1]) - 96) * v2) % a3
            v3 = (v3 * a2 + ord(a1[v5 + a4 - 1]) - 96) % a3
            if v3 == a5:
                return a1[v5:v5 + a4]
        return ''
