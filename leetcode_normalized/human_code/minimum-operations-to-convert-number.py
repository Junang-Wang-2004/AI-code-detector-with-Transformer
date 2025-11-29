class C1(object):

    def minimumOperations(self, a1, a2, a3):
        """
        """
        v1 = 1000
        a1 = [y for v3 in a1 if v3 and any((0 <= nx <= v1 for v4 in (v3, a3 - v3, a3 + v3, a3 ^ v3)))]
        v5 = [(a2, 0)]
        v6 = {a2}
        while v5:
            v7 = []
            for v8, v9 in v5:
                for v3 in a1:
                    for v4 in (v8 + v3, v8 - v3, v8 ^ v3):
                        if v4 == a3:
                            return v9 + 1
                        if not 0 <= v4 <= v1 or v4 in v6:
                            continue
                        v6.add(v4)
                        v5.append((v4, v9 + 1))
            v5 = v7
        return -1
