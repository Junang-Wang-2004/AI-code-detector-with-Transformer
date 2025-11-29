class C1(object):

    def findErrorNums(self, a1):
        """
        """
        v1 = len(a1)
        v2 = sum(a1) - v1 * (v1 + 1) // 2
        v3 = (sum((x * x for v4 in a1)) - v1 * (v1 + 1) * (2 * v1 + 1) / 6) // v2
        return ((v3 + v2) // 2, (v3 - v2) // 2)
