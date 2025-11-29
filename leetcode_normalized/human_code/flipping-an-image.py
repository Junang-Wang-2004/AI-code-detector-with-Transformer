class C1(object):

    def flipAndInvertImage(self, a1):
        """
        """
        for v1 in a1:
            for v2 in range((len(v1) + 1) // 2):
                v1[v2], v1[~v2] = (v1[~v2] ^ 1, v1[v2] ^ 1)
        return a1
