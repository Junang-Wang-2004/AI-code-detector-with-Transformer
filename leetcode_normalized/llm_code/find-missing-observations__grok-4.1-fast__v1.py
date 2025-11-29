class C1:

    def missingRolls(self, a1, a2, a3):
        v1 = sum(a1)
        v2 = len(a1) + a3
        v3 = a2 * v2
        v4 = v3 - v1
        if v4 < a3 or v4 > 6 * a3:
            return []
        v5 = v4 // a3
        v6 = v4 % a3
        v7 = []
        for v8 in range(a3):
            if v8 < v6:
                v7.append(v5 + 1)
            else:
                v7.append(v5)
        return v7
