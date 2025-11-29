class C1:

    def minimalKSum(self, a1, a2):
        v1 = sorted(set(a1))
        v2 = 0
        v3 = 1
        v4 = 0
        v5 = len(v1)
        while a2 > 0:
            if v4 < v5 and v1[v4] == v3:
                v3 += 1
                v4 += 1
                continue
            v2 += v3
            v3 += 1
            a2 -= 1
