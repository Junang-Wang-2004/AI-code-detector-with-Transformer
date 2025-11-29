class C1(object):

    def minimumOperationsToMakeEqual(self, a1, a2):
        """
        """
        if a2 >= a1:
            return a2 - a1
        v1 = a1 + (a1 - a2)
        v2 = 0
        v3 = {a1}
        v4 = [a1]
        while v4:
            v5 = []
            for a1 in v4:
                if a1 == a2:
                    return v2
                v7 = [a1 + 1, a1 - 1]
                for v8 in (5, 11):
                    if a1 % v8 == 0:
                        v7.append(a1 // v8)
                for v9 in v7:
                    if not (0 <= v9 <= v1 and v9 not in v3):
                        continue
                    v3.add(v9)
                    v5.append(v9)
            v4 = v5
            v2 += 1
        return -1
