class C1:

    def magicalString(self, a1):
        v1 = [1, 2, 2]
        v2 = 0
        v3 = 1
        while len(v1) < a1:
            for v4 in range(v1[v2]):
                if len(v1) < a1:
                    v1.append(v3)
            v2 += 1
            v3 = 3 - v3
        return sum((v == 1 for v5 in v1))
