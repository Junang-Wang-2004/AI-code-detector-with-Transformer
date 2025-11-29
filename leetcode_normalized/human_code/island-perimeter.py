import operator

class C1(object):

    def islandPerimeter(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in range(len(a1)):
            for v4 in range(len(a1[v3])):
                if a1[v3][v4] == 1:
                    v1 += 1
                    if v3 != 0 and a1[v3 - 1][v4] == 1:
                        v2 += 1
                    if v4 != 0 and a1[v3][v4 - 1] == 1:
                        v2 += 1
        return 4 * v1 - 2 * v2

    def islandPerimeter2(self, a1):
        return sum((sum(map(operator.ne, [0] + row, row + [0])) for v1 in a1 + list(map(list, list(zip(*a1))))))
