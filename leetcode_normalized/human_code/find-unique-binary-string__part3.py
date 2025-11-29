class C1(object):

    def findAllDifferentBinaryStrings(self, a1):
        """
        """
        v1 = set([int(x, 2) for v2 in a1])
        return [bin(i)[2:].zfill(len(a1[0])) for v3 in range(2 ** len(a1[0])) if v3 not in v1]
