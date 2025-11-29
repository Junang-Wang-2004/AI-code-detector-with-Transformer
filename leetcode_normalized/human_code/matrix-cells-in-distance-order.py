class C1(object):

    def allCellsDistOrder(self, a1, a2, a3, a4):
        """
        """

        def append(a1, a2, a3, a4, a5):
            if 0 <= a3 < a1 and 0 <= a4 < a2:
                a5.append([a3, a4])
        v1 = [[a3, a4]]
        for v2 in range(1, a1 + a2):
            append(a1, a2, a3 - v2, a4, v1)
            for v3 in range(-v2 + 1, v2):
                append(a1, a2, a3 + v3, a4 + abs(v3) - v2, v1)
                append(a1, a2, a3 + v3, a4 + v2 - abs(v3), v1)
            append(a1, a2, a3 + v2, a4, v1)
        return v1
