class C1(object):

    def closedIsland(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def fill(a1, a2, a3):
            if not (0 <= a2 < len(a1) and 0 <= a3 < len(a1[0]) and (a1[a2][a3] == 0)):
                return False
            a1[a2][a3] = 1
            for v1, v2 in v1:
                fill(a1, a2 + v1, a3 + v2)
            return True
        for v2 in range(len(a1[0])):
            fill(a1, 0, v2)
            fill(a1, len(a1) - 1, v2)
        for v3 in range(1, len(a1)):
            fill(a1, v3, 0)
            fill(a1, v3, len(a1[0]) - 1)
        v4 = 0
        for v3 in range(1, len(a1) - 1):
            for v2 in range(1, len(a1[0]) - 1):
                if fill(a1, v3, v2):
                    v4 += 1
        return v4
