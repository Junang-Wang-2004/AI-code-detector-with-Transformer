import math
from functools import reduce

class C1(object):

    def abbreviateProduct(self, a1, a2):
        """
        """
        v1 = v2 = 5
        v3 = 10 ** (v1 + v2)
        v4, v5 = (1, 0)
        v6 = False
        for v7 in range(a1, a2 + 1):
            v4 *= v7
            while not v4 % 10:
                v4 //= 10
                v5 += 1
            v8, v4 = divmod(v4, v3)
            if v8:
                v6 = True
        if not v6:
            return '%se%s' % (v4, v5)
        v9 = reduce(lambda x, y: (x + y) % 1, (math.log10(v7) for v7 in range(a1, a2 + 1)))
        v10 = str(int(10 ** (v9 + (v1 - 1))))
        v11 = str(v4 % 10 ** v2).zfill(v2)
        return '%s...%se%s' % (v10, v11, v5)
