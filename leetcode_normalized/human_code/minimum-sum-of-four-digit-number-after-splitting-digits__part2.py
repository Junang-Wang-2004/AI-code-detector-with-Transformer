class C1(object):

    def minimumSum(self, a1):
        """
        """
        v1 = sorted(map(int, list(str(a1))))
        v2 = v3 = 0
        for v4 in v1:
            v2 = v2 * 10 + v4
            v2, v3 = (v3, v2)
        return v2 + v3
