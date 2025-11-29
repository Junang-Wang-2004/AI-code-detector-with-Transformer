from functools import reduce

class C1(object):

    def goodSubsetofBinaryMatrix(self, a1):
        """
        """
        v1 = {}
        for v2 in range(len(a1)):
            v3 = reduce(lambda mask, j: v3 | a1[v2][j] << j, range(len(a1[0])), 0)
            if not v3:
                return [v2]
            for v4, v5 in v1.items():
                if v4 & v3 == 0:
                    return [v5, v2]
            v1[v3] = v2
        return []
