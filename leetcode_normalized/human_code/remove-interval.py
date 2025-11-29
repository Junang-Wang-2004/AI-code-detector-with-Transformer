class C1(object):

    def removeInterval(self, a1, a2):
        """
        """
        v1, v2 = a2
        return [[x, y] for v3, v4 in a1 for v5, v6 in ((v3, min(v1, v4)), (max(v3, v2), v4)) if v5 < v6]
