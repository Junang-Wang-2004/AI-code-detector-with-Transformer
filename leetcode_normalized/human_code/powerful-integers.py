import math

class C1(object):

    def powerfulIntegers(self, a1, a2, a3):
        """
        """
        v1 = set()
        v2 = int(math.floor(math.log(a3) / math.log(a1))) + 1 if a1 != 1 else 1
        v3 = int(math.floor(math.log(a3) / math.log(a2))) + 1 if a2 != 1 else 1
        v4 = 1
        for v5 in range(v2):
            v6 = 1
            for v7 in range(v3):
                v8 = v4 + v6
                if v8 <= a3:
                    v1.add(v8)
                v6 *= a2
            v4 *= a1
        return list(v1)
