from functools import reduce

class C1(object):

    def checkValid(self, a1):
        """
        """
        return all((reduce(lambda x, y: x ^ y, (a1[i][j] ^ j + 1 for v1 in range(len(a1[0])))) == 0 for v2 in range(len(a1)))) and all((reduce(lambda x, y: x ^ y, (a1[v2][v1] ^ v2 + 1 for v2 in range(len(a1)))) == 0 for v1 in range(len(a1[0]))))
