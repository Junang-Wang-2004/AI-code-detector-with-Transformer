class C1(object):

    def carPooling(self, a1, a2):
        """
        """
        v1 = [x for v2, v3, v4 in a1 for v5 in [[v3, v2], [v4, -v2]]]
        v1.sort()
        for v6, v2 in v1:
            a2 -= v2
            if a2 < 0:
                return False
        return True
