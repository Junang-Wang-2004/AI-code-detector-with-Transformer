from functools import reduce

class C1(object):

    def setZeroes(self, a1):
        v1 = reduce(lambda acc, i: acc or a1[i][0] == 0, range(len(a1)), False)
        v2 = reduce(lambda acc, j: acc or a1[0][j] == 0, range(len(a1[0])), False)
        for v3 in range(1, len(a1)):
            for v4 in range(1, len(a1[0])):
                if a1[v3][v4] == 0:
                    a1[v3][0], a1[0][v4] = (0, 0)
        for v3 in range(1, len(a1)):
            for v4 in range(1, len(a1[0])):
                if a1[v3][0] == 0 or a1[0][v4] == 0:
                    a1[v3][v4] = 0
        if v1:
            for v3 in range(len(a1)):
                a1[v3][0] = 0
        if v2:
            for v4 in range(len(a1[0])):
                a1[0][v4] = 0
