class C1(object):

    def recoverOrder(self, a1, a2):
        """
        """
        v1 = set(a2)
        return [x for v2 in a1 if v2 in v1]
