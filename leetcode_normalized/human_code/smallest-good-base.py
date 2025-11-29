import math

class C1(object):

    def smallestGoodBase(self, a1):
        """
        """
        v1 = int(a1)
        v2 = int(math.log(v1, 2))
        for v3 in range(v2, 1, -1):
            v4 = int(v1 ** v3 ** (-1))
            if (v4 ** (v3 + 1) - 1) // (v4 - 1) == v1:
                return str(v4)
        return str(v1 - 1)
