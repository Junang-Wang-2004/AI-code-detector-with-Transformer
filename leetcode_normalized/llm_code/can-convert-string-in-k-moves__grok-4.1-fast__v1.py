class C1:

    def canConvertString(self, a1, a2, a3):
        if len(a1) != len(a2):
            return False
        v1 = [0] * 26
        for v2 in range(len(a1)):
            v3 = (ord(a2[v2]) - ord(a1[v2])) % 26
            v1[v3] += 1
        for v4 in range(1, 26):
            v5 = v1[v4]
            if v5 > 0 and (v5 - 1) * 26 + v4 > a3:
                return False
        return True
