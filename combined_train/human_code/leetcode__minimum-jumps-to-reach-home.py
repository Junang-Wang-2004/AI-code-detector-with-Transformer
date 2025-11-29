class C1(object):

    def minimumJumps(self, a1, a2, a3, a4):
        """
        """
        v1 = max(a1)
        v2 = a4 + a3 if a2 >= a3 else max(a4, v1) + a2 + (a3 + a2)
        v3 = set()
        for v4 in a1:
            v3.add((v4, True))
            v3.add((v4, False))
        v5 = 0
        v6 = [(0, True)]
        v3.add((0, True))
        while v6:
            v7 = []
            for v4, v8 in v6:
                if v4 == a4:
                    return v5
                if v4 + a2 <= v2 and (v4 + a2, True) not in v3:
                    v3.add((v4 + a2, True))
                    v7.append((v4 + a2, True))
                if not v8:
                    continue
                if v4 - a3 >= 0 and (v4 - a3, False) not in v3:
                    v3.add((v4 - a3, False))
                    v7.append((v4 - a3, False))
            v6 = v7
            v5 += 1
        return -1
