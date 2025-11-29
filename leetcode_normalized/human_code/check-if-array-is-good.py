class C1(object):

    def isGood(self, a1):
        """
        """
        v1 = [0] * len(a1)
        for v2 in a1:
            if v2 < len(v1):
                v1[v2] += 1
            else:
                return False
        return all((v1[v2] == 1 for v2 in range(1, len(a1) - 1)))
