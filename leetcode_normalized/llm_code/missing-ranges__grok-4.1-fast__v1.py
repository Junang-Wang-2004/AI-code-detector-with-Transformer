class C1:

    def findMissingRanges(self, a1, a2, a3):
        v1 = []
        v2 = a2
        for v3 in a1:
            if v3 > v2:
                if v2 == v3 - 1:
                    v1.append(str(v2))
                else:
                    v1.append(f'{v2}->{v3 - 1}')
            v2 = v3 + 1
        if a3 >= v2:
            if v2 == a3:
                v1.append(str(v2))
            else:
                v1.append(f'{v2}->{a3}')
        return v1
