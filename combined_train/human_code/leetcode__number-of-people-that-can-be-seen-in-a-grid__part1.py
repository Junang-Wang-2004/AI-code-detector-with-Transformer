class C1(object):

    def seePeople(self, a1):
        """
        """

        def count(a1, a2):
            v1 = 0
            while a2 and a2[-1] < a1:
                a2.pop()
                v1 += 1
            if a2:
                v1 += 1
            if not a2 or a2[-1] != a1:
                a2.append(a1)
            return v1
        v1 = [[0] * len(a1[0]) for v2 in range(len(a1))]
        for v3 in range(len(a1)):
            v4 = []
            for v5 in reversed(range(len(a1[0]))):
                v1[v3][v5] += count(a1[v3][v5], v4)
        for v5 in range(len(a1[0])):
            v4 = []
            for v3 in reversed(range(len(a1))):
                v1[v3][v5] += count(a1[v3][v5], v4)
        return v1
