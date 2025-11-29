class C1:

    def divisorSubstrings(self, a1, a2):
        v1 = str(a1)
        v2 = len(v1)
        v3 = 0
        for v4 in range(v2 - a2 + 1):
            v5 = int(v1[v4:v4 + a2])
            if v5 != 0 and a1 % v5 == 0:
                v3 += 1
        return v3
