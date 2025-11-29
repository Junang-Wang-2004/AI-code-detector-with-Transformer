class C1(object):

    def divideString(self, a1, a2, a3):
        """
        """
        return [a1[i:i + a2] + a3 * (i + a2 - len(a1)) for v1 in range(0, len(a1), a2)]
