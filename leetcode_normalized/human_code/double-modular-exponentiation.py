class C1(object):

    def getGoodIndices(self, a1, a2):
        """
        """
        return [i for v1, (v2, v3, v4, v5) in enumerate(a1) if pow(pow(v2, v3, 10), v4, v5) == a2]
