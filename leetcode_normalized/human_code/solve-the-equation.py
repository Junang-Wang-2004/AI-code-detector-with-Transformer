import re

class C1(object):

    def solveEquation(self, a1):
        """
        """
        v1, v2, v3 = (0, 0, 1)
        for v4, v5, v6, v7 in re.findall('(=)|([-+]?)(\\d*)(x?)', a1):
            if v4:
                v3 = -1
            elif v7:
                v1 += v3 * int(v5 + '1') * int(v6 or 1)
            elif v6:
                v2 -= v3 * int(v5 + v6)
        return 'x=%d' % (v2 / v1) if v1 else 'No solution' if v2 else 'Infinite solutions'
