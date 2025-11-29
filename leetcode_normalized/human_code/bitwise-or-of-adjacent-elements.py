class C1(object):

    def orArray(self, a1):
        """
        """
        return [a1[i] | a1[i + 1] for v1 in range(len(a1) - 1)]
