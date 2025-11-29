class C1(object):

    def hasAllCodes(self, a1, a2):
        """
        """
        return 2 ** a2 <= len(a1) and len({a1[i:i + a2] for v1 in range(len(a1) - a2 + 1)}) == 2 ** a2
