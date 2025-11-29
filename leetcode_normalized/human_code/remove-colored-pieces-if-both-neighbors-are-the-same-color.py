class C1(object):

    def winnerOfGame(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in range(1, len(a1) - 1):
            if not a1[v3 - 1] == a1[v3] == a1[v3 + 1]:
                continue
            if a1[v3] == 'A':
                v1 += 1
            else:
                v2 += 1
        return v1 > v2
