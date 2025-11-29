class C1(object):

    def getRow(self, a1):
        v1 = [0] * (a1 + 1)
        for v2 in range(a1 + 1):
            v3 = v1[0] = 1
            for v4 in range(1, v2 + 1):
                v3, v1[v4] = (v1[v4], v3 + v1[v4])
        return v1

    def getRow2(self, a1):
        """
        """
        v1 = [1]
        for v2 in range(a1):
            v1 = [x + y for v3, v4 in zip([0] + v1, v1 + [0])]
        return v1

    def getRow3(self, a1):
        """
        """
        if a1 == 0:
            return [1]
        v1 = [1, 1]

        def add(a1):
            v1 = a1[:1]
            for v2, v3 in enumerate(a1):
                if v2 < len(a1) - 1:
                    v1 += [a1[v2] + a1[v2 + 1]]
            v1 += a1[:1]
            return v1
        while v1[1] < a1:
            v1 = add(v1)
        return v1
