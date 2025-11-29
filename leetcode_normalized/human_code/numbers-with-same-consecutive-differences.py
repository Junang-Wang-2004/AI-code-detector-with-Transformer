class C1(object):

    def numsSameConsecDiff(self, a1, a2):
        """
        """
        v1 = list(range(10))
        for v2 in range(a1 - 1):
            v1 = [x * 10 + y for v3 in v1 for v4 in set([v3 % 10 + a2, v3 % 10 - a2]) if v3 and 0 <= v4 < 10]
        return v1
