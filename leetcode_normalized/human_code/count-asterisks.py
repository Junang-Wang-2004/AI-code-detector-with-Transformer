class C1(object):

    def countAsterisks(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in a1:
            if v3 == '|':
                v2 = (v2 + 1) % 2
                continue
            if v3 == '*' and v2 == 0:
                v1 += 1
        return v1
