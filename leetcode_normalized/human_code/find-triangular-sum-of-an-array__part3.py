class C1(object):

    def triangularSum(self, a1):
        """
        """
        for v1 in reversed(range(len(a1))):
            for v2 in range(v1):
                a1[v2] = (a1[v2] + a1[v2 + 1]) % 10
        return a1[0]
