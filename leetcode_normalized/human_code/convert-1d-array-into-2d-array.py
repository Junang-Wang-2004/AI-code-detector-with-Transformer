class C1(object):

    def construct2DArray(self, a1, a2, a3):
        """
        """
        return [a1[i:i + a3] for v1 in range(0, len(a1), a3)] if len(a1) == a2 * a3 else []
