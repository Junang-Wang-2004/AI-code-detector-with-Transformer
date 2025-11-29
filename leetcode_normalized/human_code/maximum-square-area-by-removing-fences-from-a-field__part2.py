class C1(object):

    def maximizeSquareArea(self, a1, a2, a3, a4):
        """
        """
        v1 = 10 ** 9 + 7

        def diff(a1, a2, a3):
            a1.append(1)
            a1.append(a2)
            for v1 in range(len(a1)):
                for v2 in range(v1 + 1, len(a1)):
                    if not a3:
                        lookup.add(abs(a1[v1] - a1[v2]))
                        continue
                    if abs(a1[v1] - a1[v2]) in lookup:
                        result[0] = max(result[0], (a1[v1] - a1[v2]) ** 2)
        if len(a3) > len(a4):
            a3, a4 = (a4, a3)
            a1, a2 = (a2, a1)
        v6 = [-1]
        v7 = set()
        diff(a3, a1, False)
        diff(a4, a2, True)
        return v6[0] % v1 if v6[0] != -1 else -1
