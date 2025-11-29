class C1(object):

    def constructTransformedArray(self, a1):
        """
        """
        return [a1[(i + a1[i]) % len(a1)] for v1 in range(len(a1))]
