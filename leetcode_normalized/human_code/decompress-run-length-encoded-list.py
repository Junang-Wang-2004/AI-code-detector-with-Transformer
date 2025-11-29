class C1(object):

    def decompressRLElist(self, a1):
        """
        """
        return [a1[i + 1] for v1 in range(0, len(a1), 2) for v2 in range(a1[v1])]
