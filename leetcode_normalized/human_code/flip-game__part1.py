class C1(object):

    def generatePossibleNextMoves(self, a1):
        """
        """
        v1 = []
        v2, v3 = (0, len(a1) - 1)
        while v2 < v3:
            if a1[v2] == '+':
                while v2 < v3 and a1[v2 + 1] == '+':
                    v1.append(a1[:v2] + '--' + a1[v2 + 2:])
                    v2 += 1
            v2 += 1
        return v1
