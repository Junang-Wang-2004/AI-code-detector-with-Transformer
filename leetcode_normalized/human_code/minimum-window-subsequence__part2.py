class C1(object):

    def minWindow(self, a1, a2):
        """
        """
        v1 = [[None for v2 in range(len(a1))] for v2 in range(2)]
        for v3, v4 in enumerate(a1):
            if v4 == a2[0]:
                v1[0][v3] = v3
        for v5 in range(1, len(a2)):
            v6 = None
            v1[v5 % 2] = [None] * len(a1)
            for v3, v4 in enumerate(a1):
                if v6 is not None and v4 == a2[v5]:
                    v1[v5 % 2][v3] = v6
                if v1[(v5 - 1) % 2][v3] is not None:
                    v6 = v1[(v5 - 1) % 2][v3]
        v7, v8 = (0, len(a1))
        for v3, v5 in enumerate(v1[(len(a2) - 1) % 2]):
            if v5 >= 0 and v3 - v5 < v8 - v7:
                v7, v8 = (v5, v3)
        return a1[v7:v8 + 1] if v8 < len(a1) else ''
