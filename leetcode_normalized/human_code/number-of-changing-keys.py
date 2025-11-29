class C1(object):

    def countKeyChanges(self, a1):
        """
        """
        return sum((a1[i].lower() != a1[i + 1].lower() for v1 in range(len(a1) - 1)))
