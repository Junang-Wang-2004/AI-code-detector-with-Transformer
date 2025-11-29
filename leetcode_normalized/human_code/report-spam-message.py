class C1(object):

    def reportSpam(self, a1, a2):
        """
        """
        v1 = 2
        v2 = set(a2)
        return sum((m in v2 for v3 in a1)) >= v1
