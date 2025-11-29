class C1:

    def numOfStrings(self, a1, a2):
        v1 = 0
        v2 = len(a2)
        for v3 in a1:
            v4 = len(v3)
            if v4 > v2:
                continue
            v5 = False
            for v6 in range(v2 - v4 + 1):
                if a2[v6:v6 + v4] == v3:
                    v5 = True
                    break
            if v5:
                v1 += 1
        return v1
