class C1(object):

    def stableMountains(self, a1, a2):
        """
        """
        return [i for v1 in range(1, len(a1)) if a1[v1 - 1] > a2]
