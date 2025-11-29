class C1(object):

    def generatePossibleNextMoves(self, a1):
        """
      """
        return [a1[:i] + '--' + a1[i + 2:] for v1 in range(len(a1) - 1) if a1[v1:v1 + 2] == '++']
