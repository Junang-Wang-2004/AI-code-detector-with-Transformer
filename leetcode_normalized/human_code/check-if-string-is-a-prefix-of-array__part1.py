class C1(object):

    def isPrefixString(self, a1, a2):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v1 == len(a2) or a2[v1][v2] != v3:
                return False
            v2 += 1
            if v2 == len(a2[v1]):
                v1 += 1
                v2 = 0
        return v2 == 0
