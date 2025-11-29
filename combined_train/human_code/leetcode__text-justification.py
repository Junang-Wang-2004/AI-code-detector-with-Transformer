class C1(object):

    def fullJustify(self, a1, a2):
        """
        """

        def addSpaces(a1, a2, a3, a4):
            if a1 < a2:
                return 1 if a4 else a3 // a2 + int(a1 < a3 % a2)
            return 0

        def connect(a1, a2, a3, a4, a5, a6):
            v1 = []
            v2 = a4 - a3
            for v3 in range(v2):
                v1 += (a1[a3 + v3],)
                v1 += (' ' * addSpaces(v3, v2 - 1, a2 - a5, a6),)
            v4 = ''.join(v1)
            if len(v4) < a2:
                v4 += ' ' * (a2 - len(v4))
            return v4
        v1 = []
        v2, v3 = (0, 0)
        for v4 in range(len(a1)):
            if v3 + len(a1[v4]) + (v4 - v2) > a2:
                v1 += (connect(a1, a2, v2, v4, v3, False),)
                v2, v3 = (v4, 0)
            v3 += len(a1[v4])
        v1 += (connect(a1, a2, v2, len(a1), v3, True),)
        return v1
