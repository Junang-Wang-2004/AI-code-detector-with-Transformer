class C1:

    def getFolderNames(self, a1):
        v1 = set()
        v2 = {}
        v3 = []
        for v4 in a1:
            v5 = v2.get(v4, 0)
            v6 = v4 if v5 == 0 else f'{v4}({v5})'
            while v6 in v1:
                v5 += 1
                v6 = f'{v4}({v5})'
            v3.append(v6)
            v1.add(v6)
            v2[v4] = v5 + 1
        return v3
