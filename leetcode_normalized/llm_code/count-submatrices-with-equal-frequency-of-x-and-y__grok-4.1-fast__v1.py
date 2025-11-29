class C1:

    def numberOfSubmatrices(self, a1):
        v1 = 0
        v2 = 0
        v3 = 0
        for v4 in a1:
            for v5 in v4:
                if v5 == 'X':
                    v1 += 1
                elif v5 == 'Y':
                    v2 += 1
                if v1 == v2 and v1 != 0:
                    v3 += 1
        return v3
