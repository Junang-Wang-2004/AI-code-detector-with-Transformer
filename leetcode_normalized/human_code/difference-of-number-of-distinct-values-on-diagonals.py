class C1(object):

    def differenceOfDistinctValues(self, a1):
        """
        """

        def update(a1, a2):
            v1 = set()
            for v2 in range(min(len(a1) - a1, len(a1[0]) - a2)):
                result[a1 + v2][a2 + v2] = len(v1)
                v1.add(a1[a1 + v2][a2 + v2])
            v1.clear()
            for v2 in reversed(range(min(len(a1) - a1, len(a1[0]) - a2))):
                result[a1 + v2][a2 + v2] = abs(result[a1 + v2][a2 + v2] - len(v1))
                v1.add(a1[a1 + v2][a2 + v2])
        v1 = [[0] * len(a1[0]) for v2 in range(len(a1))]
        for v3 in range(len(a1[0])):
            update(0, v3)
        for v4 in range(1, len(a1)):
            update(v4, 0)
        return v1
