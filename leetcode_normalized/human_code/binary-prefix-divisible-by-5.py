class C1(object):

    def prefixesDivBy5(self, a1):
        """
        """
        for v1 in range(1, len(a1)):
            a1[v1] += a1[v1 - 1] * 2 % 5
        return [x % 5 == 0 for v2 in a1]
