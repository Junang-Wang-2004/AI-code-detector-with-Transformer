class C1(object):

    def maxMatrixSum(self, a1):
        """
        """
        v1 = sum((abs(x) for v2 in a1 for v3 in v2))
        v4 = min((abs(v3) for v2 in a1 for v3 in v2))
        v5 = sum((v3 < 0 for v2 in a1 for v3 in v2))
        return v1 if v5 % 2 == 0 else v1 - 2 * v4
