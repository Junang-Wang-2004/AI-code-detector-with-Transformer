class C1(object):

    def powerfulIntegers(self, a1, a2, a3):
        v1 = set()
        v2 = []
        v3 = 1
        while v3 <= a3:
            v2.append(v3)
            if a1 == 1:
                break
            v3 *= a1
        v4 = []
        v5 = 1
        while v5 <= a3:
            v4.append(v5)
            if a2 == 1:
                break
            v5 *= a2
        for v6 in v2:
            for v7 in v4:
                if v6 + v7 <= a3:
                    v1.add(v6 + v7)
        return list(v1)
