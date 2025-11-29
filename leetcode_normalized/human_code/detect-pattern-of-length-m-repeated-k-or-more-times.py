class C1(object):

    def containsPattern(self, a1, a2, a3):
        """
        """
        v1 = 0
        for v2 in range(len(a1) - a2):
            if a1[v2] != a1[v2 + a2]:
                v1 = 0
                continue
            v1 += 1
            if v1 == (a3 - 1) * a2:
                return True
        return False
