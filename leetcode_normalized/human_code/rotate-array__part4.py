class C1(object):
    """
    """

    def rotate(self, a1, a2):
        """
        """
        a1[:] = a1[len(a1) - a2:] + a1[:len(a1) - a2]
