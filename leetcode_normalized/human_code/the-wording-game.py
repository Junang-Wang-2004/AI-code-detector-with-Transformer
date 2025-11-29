class C1(object):

    def canAliceWin(self, a1, a2):
        """
        """

        def is_closely_greater(a1, a2):
            return ord(a1[0]) - ord(a2[0]) <= 1 and a1 > a2
        v1 = True
        v2, v3 = (0, -1)
        for v4 in range(len({w[0] for v5 in a1}) + len({v5[0] for v5 in a2})):
            v3 = next((v3 for v3 in range(v3 + 1, len(a2)) if is_closely_greater(a2[v3], a1[v2])), len(a2))
            if v3 == len(a2):
                break
            while v3 + 1 < len(a2) and a2[v3 + 1][0] == a2[v3][0]:
                v3 += 1
            a1, a2, v2, v3, v1 = (a2, a1, v3, v2, not v1)
        return v1
