class C1:

    def minPatches(self, a1, a2):
        v1 = 0
        v2 = 0
        v3 = 0
        while v2 < a2:
            if v3 < len(a1) and a1[v3] <= v2 + 1:
                v2 += a1[v3]
                v3 += 1
            else:
                v4 = v2 + 1
                v2 += v4
                v1 += 1
        return v1
